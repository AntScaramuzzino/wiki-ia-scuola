#!/bin/bash
# Aggiorna la sezione News del wiki "IA nella scuola".
# Eseguito da launchd una volta al giorno (vedi ~/Library/LaunchAgents/it.scaramuzzino.wiki-news.plist).
# Passi: 1) Claude cerca e scrive l'edizione  2) build Quartz  3) commit+push (Vercel ridistribuisce).

set -uo pipefail

REPO="/Users/antonioscaramuzzino/wiki-ia-scuola"
LOG="$REPO/scripts/news.log"
DATE="$(date +%Y-%m-%d)"
DATE_IT="$(LC_TIME=it_IT.UTF-8 date +'%-d %B %Y' 2>/dev/null || date +%Y-%m-%d)"
NEWS_FILE="$REPO/content/news/$DATE.md"
CLAUDE="/Users/antonioscaramuzzino/.local/bin/claude"
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$HOME/.local/bin"

log() { echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" >> "$LOG"; }

log "=== avvio aggiornamento news $DATE ==="
cd "$REPO" || { log "ERRORE: repo non trovato"; exit 1; }

if [ -f "$NEWS_FILE" ]; then
  log "edizione di oggi già presente, esco"
  exit 0
fi

git pull -q --rebase 2>>"$LOG" || log "warning: git pull fallito"

PROMPT=$(cat <<EOF
Sei il redattore della sezione News del wiki "IA nella scuola" ($REPO).

COMPITO: crea l'edizione di oggi ($DATE) con le notizie più rilevanti degli ULTIMI GIORNI
sull'uso dell'intelligenza artificiale nella scuola e nella didattica.

1. Cerca sul web notizie recenti (ultimi 7 giorni, priorità agli ultimi 2-3) su questi ambiti:
   - Normativa e policy italiana (MIM, decreti, PNRR, Garante privacy, AgID)
   - Didattica e pratiche in classe (esperienze, strumenti, metodologie)
   - Ricerca e framework internazionali (UNESCO, OCSE, Commissione europea)
   - Etica, rischi e dibattito pubblico (privacy, bias, integrità accademica)
   Fai più ricerche mirate. Scarta il marketing e i contenuti promozionali.

2. Seleziona da 3 a 6 notizie DAVVERO rilevanti e recenti. Se non trovi nulla di nuovo
   e significativo rispetto alle edizioni già presenti in $REPO/content/news/,
   NON creare il file: termina scrivendo "NESSUNA NOVITA".

3. Scrivi il file $NEWS_FILE in italiano seguendo ESATTAMENTE questo schema:

---
title: "News — $DATE_IT"
type: news
tags: [news, ai-formazione, politiche]
created: $DATE
updated: $DATE
---

# News — $DATE_IT

> In evidenza: <una riga sulla notizia principale>

---

## <Ambito, es. Normativa e policy>

### <Titolo della notizia>
<sintesi redazionale di 2-4 righe, parole tue, MAI copiare il testo della fonte>

📖 Nel wiki: [[concept/...]] · [[source/...]]
🔗 [Nome fonte](URL) · [Altra fonte](URL)

<...ripeti per ogni notizia, raggruppando per ambito...>

---

*Sintesi redazionali a cura di Antonio Scaramuzzino. Per il contenuto completo consultare sempre le fonti originali.*

REGOLE IMPORTANTI:
- Usa SOLO wikilink a pagine esistenti: controlla i nomi file in $REPO/content/concept/,
  $REPO/content/source/, $REPO/content/entity/, $REPO/content/analyses/.
  Il formato è [[concept/nome-file-senza-estensione]]. Non inventare pagine.
- Ogni notizia DEVE avere almeno un link alla fonte originale con URL reale trovato nella ricerca.
- Mai riprodurre il testo delle fonti: solo sintesi originali brevi.
- Niente notizie inventate: se un dato non è nelle fonti, non scriverlo.

4. Infine aggiorna $REPO/content/news/index.md aggiungendo in cima alla lista "## Edizioni"
   la riga: - [[news/$DATE|$DATE_IT]] — <tre parole chiave dell'edizione>
EOF
)

log "chiamo Claude per generare l'edizione..."
"$CLAUDE" -p "$PROMPT" \
  --allowedTools "WebSearch" "WebFetch" "Read" "Write" "Edit" "Glob" "Grep" \
  >> "$LOG" 2>&1
CLAUDE_RC=$?
log "Claude terminato (rc=$CLAUDE_RC)"

if [ ! -f "$NEWS_FILE" ]; then
  log "nessuna edizione creata (nessuna novità o errore) — nessun commit"
  exit 0
fi

log "build Quartz..."
if ! npx quartz build >> "$LOG" 2>&1; then
  log "ERRORE: build fallito — nessun commit"
  exit 1
fi

git add -A
if git diff --cached --quiet; then
  log "nessuna modifica da committare"
  exit 0
fi

git -c user.name="Antonio Scaramuzzino" -c user.email="a.scaramuzzino@gmail.com" \
    commit -q -m "News $DATE: aggiornamento automatico" >> "$LOG" 2>&1
if git push -q origin main >> "$LOG" 2>&1; then
  log "OK: edizione $DATE pubblicata (Vercel ridistribuisce)"
else
  log "ERRORE: push fallito"
  exit 1
fi
