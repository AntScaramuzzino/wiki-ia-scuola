# Architettura del wiki "IA nella scuola"

## Fonte unica di verità

Tutti i contenuti nascono **nel wiki sorgente** su Google Drive:

```
…/Il mio Drive/Brain/LLM-Wiki/LLM-Wiki/
├── raw/          fonti grezze (immutabili, mai pubblicate)
└── wiki/         ← FONTE UNICA. Tutto si scrive qui.
    ├── concept/  entity/  source/  analyses/
    ├── news/         rassegna quotidiana
    ├── social/       bozze per la distribuzione (non pubblicate)
    ├── index.md      overview.md   log.md       crediti.md
```

Questo repo (`~/wiki-ia-scuola`) è **solo la copia pubblicata**.

> ⚠️ Non modificare a mano i file in `content/`: vengono sovrascritti dalla sincronizzazione.

## Flusso di pubblicazione

```
wiki/ (Drive)  →  scripts/sync-content.py  →  content/  →  npx quartz build  →  public/  →  git push  →  Vercel
```

Le cartelle hanno gli **stessi nomi** nel sorgente e nel sito, così i wikilink
`[[concept/fria]]` funzionano identici in Obsidian e online. Alla sola copia
pubblicata vengono applicate due trasformazioni:

1. rimozione dell'H1 iniziale duplicato (Quartz mostra già il `title` del frontmatter);
2. conversione dei wikilink `[[tipo/slug]]` → `[[tipo/slug|Titolo leggibile]]`.

> ⚠️ Le cartelle sono al **singolare** (`concept/`, `entity/`, `source/`). Erano al plurale
> fino al 2026-08-08: con i link scritti al singolare, in Obsidian risultavano tutti rotti.

## Strumenti statici (solo in questo repo)

`quartz/static/strumenti/` contiene pagine HTML autonome che Quartz copia così come sono in `/static/strumenti/`.
(In `content/` no: Quartz toglie l'estensione `.html` ai file non markdown e Vercel non li servirebbe come pagine.) Non hanno
un corrispondente nel wiki sorgente e la sincronizzazione non le tocca.

| File | Cosa è |
|---|---|
| `quartz/static/strumenti/obblighi-ia-pa.html` | Repertorio interattivo delle 87 voci ricavate dalle Linee Guida AgID (det. 169/2026) e vista «Autovalutazione» (`#autovalutazione`: 55 controlli, grafico a rosa come in framework.proftecnologia.it). Rimanda alle pagine del wiki con indirizzi assoluti: se una pagina collegata cambia slug, il file va rigenerato Dal 16/11/2026 è l'«Osservatorio IA nella PA» (Panoramica con mappa, calendario e rischio; scheda del controllo dal grafico; collegamenti anche al wiki Normativa scolastica); si genera dal progetto `osservatorio-ia` (`tools/build.py`), l'analisi dei documenti con l'IA qui è spenta. |
| `quartz/static/strumenti/linee-guida-agid-ia-pa.pdf` | PDF AgID a cui rimandano i collegamenti «Apri la fonte» |
| `quartz/static/strumenti/pdfjs/` | pdf.js (Apache-2.0, pdfjs-dist 4.10.38): il visualizzatore che apre il PDF nella pagina, sulla pagina citata. Lo aggiunge `tools/osservatorio_viewer.py` del repo `proftecnologia-framework`; va rilanciato ogni volta che `obblighi-ia-pa.html` viene rigenerato |

Dalle pagine del wiki si collegano con un `<a href="/static/strumenti/…" target="_blank" data-router-ignore>`,
perché non sono pagine Quartz.

## Script

| Script | Cosa fa |
|---|---|
| `scripts/sync-content.py` | Copia il wiki sorgente in `content/` e applica le trasformazioni |
| `scripts/gen-index.py` | Rigenera `wiki/index.md` dalle pagine esistenti |
| `scripts/link-raw.py` | Collega i file di `raw/` alle pagine source (tracciabilità) |
| `scripts/news-update.sh` | **Non più in uso** — fallback manuale, sostituito dai task Cowork |

## Automazioni (task schedulati di Claude Cowork)

| Task | Quando | Cosa fa |
|---|---|---|
| `wiki-ia-scuola-news` | ogni giorno ~7:08 | Cerca notizie, scrive `wiki/news/<data>.md`, sincronizza, builda, pubblica |
| `wiki-analisi-settimanale` | lunedì ~8:09 | Scrive una nuova analisi in `wiki/analyses/`, la collega, aggiorna il log, pubblica |

Entrambi generano anche i testi pronti per Telegram, Facebook, Instagram e newsletter
in `wiki/social/<data>-*.md`.

I task girano con l'autenticazione dell'app (non con il token della CLI, che veniva revocato)
e **solo con l'app aperta**: se è chiusa all'orario previsto, partono al lancio successivo.

## Distribuzione sui canali

| Canale | Stato | Cosa serve |
|---|---|---|
| Sito | ✅ attivo | — |
| Telegram | ⏳ da configurare | `~/.claude/wiki-telegram.env` con `TELEGRAM_BOT_TOKEN` e `TELEGRAM_CHAT_ID` |
| Facebook | ✋ manuale | Testi pronti in `wiki/social/`; l'invio via API richiede Page access token (Meta) |
| Instagram | ✋ manuale | Come sopra + **un'immagine è obbligatoria** per ogni post |
| Newsletter | ✋ manuale | Testi pronti; l'invio richiede un servizio (Substack/Buttondown/Mailchimp) |
