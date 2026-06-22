---
title: "Wiki Persistente"
type: concept
tags: [knowledge-management, llm, second-brain]
created: 2026-04-22
updated: 2026-04-22
sources: [llm-wiki-pattern.md]
---

# Wiki Persistente

## Definizione

Un wiki persistente è una raccolta strutturata di file markdown interlinkati che un LLM costruisce e mantiene nel tempo. Si distingue da un sistema RAG classico perché la conoscenza viene sintetizzata una volta (al momento dell'ingest) e poi mantenuta aggiornata — non ri-derivata ad ogni query.

## Come funziona

1. Una fonte raw viene letta dall'LLM
2. L'LLM estrae entità, concetti, claim e relazioni
3. Questi vengono integrati nelle pagine esistenti (o creano pagine nuove)
4. Le cross-reference vengono mantenute: le contraddizioni vengono annotate, non silenziare
5. L'indice viene aggiornato perché l'LLM possa navigarlo nelle sessioni future

## Applicazioni o esempi

- Secondo cervello personale (questo wiki)
- Wiki interno aziendale mantenuto da LLM su Slack/meeting transcripts
- Companion wiki durante la lettura di un libro
- Knowledge base di ricerca su un tema specifico
- Analisi competitiva / due diligence

## Relazioni con altri concetti

- [[concept/rag]] — il paradigma alternativo: recupero al momento della query invece di sintesi persistente
- [[concept/memex]] — precursore concettuale di Bush (1945)
- [[concept/ingest]] — l'operazione che alimenta il wiki
- [[concept/lint-wiki]] — l'operazione che mantiene sano il wiki

## Contraddizioni e dibattiti

Nessuna nella letteratura ingested finora. La fonte principale riconosce che questa è una scelta progettuale con trade-off: richiede più lavoro iniziale per ingest ma query molto più veloci e ricche in seguito.

## Fonti

[[source/llm-wiki-pattern]]
