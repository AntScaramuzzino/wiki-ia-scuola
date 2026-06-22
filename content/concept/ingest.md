---
title: "Ingest"
type: concept
tags: [workflow, llm-wiki, operazione]
created: 2026-04-22
updated: 2026-04-22
sources: [llm-wiki-pattern.md]
---

# Ingest

## Definizione

Operazione con cui una fonte raw viene letta, analizzata e integrata nel wiki. È l'azione fondamentale che fa crescere la base di conoscenza.

## Come funziona

1. L'utente indica la fonte da ingierire
2. L'LLM legge il file raw (senza modificarlo)
3. Se interattivo: discute i punti chiave con l'utente
4. Crea `wiki/sources/[slug].md` con sommario e punti chiave
5. Aggiorna/crea pagine entity e concept coinvolte
6. Aggiorna `wiki/overview.md` se necessario
7. Aggiorna `wiki/index.md`
8. Appende una entry a `wiki/log.md`

Una singola fonte tipicamente tocca 5–15 pagine del wiki.

## Applicazioni o esempi

- "Ingesta questo articolo su deep learning"
- "Ingesta il capitolo 3 del libro che ho salvato in raw/books/"
- Ingest batch (meno supervisione, più automatico)

## Relazioni con altri concetti

- [[concept/wiki-persistente]] — l'ingest è ciò che alimenta il wiki
- [[concept/lint-wiki]] — operazione complementare (manutenzione vs crescita)
- [[concept/schema-agente]] — il CLAUDE.md definisce il protocollo di ingest

## Fonti

[[source/llm-wiki-pattern]]
