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
