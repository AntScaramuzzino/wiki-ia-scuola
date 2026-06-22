---
title: "RAG — Retrieval-Augmented Generation"
type: concept
tags: [llm, retrieval, knowledge-management]
created: 2026-04-22
updated: 2026-04-22
sources: [llm-wiki-pattern.md]
---

# RAG — Retrieval-Augmented Generation

## Definizione

Paradigma in cui un LLM recupera chunk rilevanti da una collezione di documenti al momento della query e genera una risposta basata su di essi. Non accumula conoscenza tra le sessioni: ogni risposta ri-deriva la sintesi dalle fonti grezze.

## Come funziona

1. I documenti vengono indicizzati (embedding vettoriali o BM25)
2. Al momento della query, i chunk più rilevanti vengono recuperati
3. L'LLM genera una risposta basata su query + chunk recuperati
4. Nulla rimane persistente tra una query e l'altra

## Applicazioni o esempi

- NotebookLM (Google)
- ChatGPT file uploads
- La maggior parte dei chatbot aziendali su documenti

## Relazioni con altri concetti

- [[concept/wiki-persistente]] — il paradigma alternativo: sintesi persistente invece di recupero al volo

## Contraddizioni e dibattiti

RAG ha vantaggi su scala molto grande (milioni di documenti) dove un wiki manuale non è praticabile. Il pattern LLM-Wiki funziona meglio a scala umana: decine-centinaia di fonti curate, dove la qualità della sintesi supera la quantità del recupero.

## Fonti

[[source/llm-wiki-pattern]]
