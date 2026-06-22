---
title: "qmd"
type: entity
tags: [strumento, software, ricerca, markdown]
created: 2026-04-22
updated: 2026-04-22
sources: [llm-wiki-pattern.md]
---

# qmd

## Descrizione

Motore di ricerca locale per file markdown con ricerca ibrida BM25 + vettoriale e re-ranking LLM. Tutto on-device. Disponibile come CLI (per shell-out dell'LLM) e come server MCP (strumento nativo dell'LLM).

## Ruolo nel dominio

Alternativa all'index.md quando il wiki cresce oltre la scala dove un indice testuale è sufficiente. Consente all'LLM di cercare nel wiki con precision semantica invece di leggere tutto l'indice.

## Connessioni

- [[concept/wiki-persistente]] — strumento di supporto per wiki grandi
- [[entity/obsidian]] — complementare come strumento di navigazione

## Note e aggiornamenti

*2026-04-22*: Menzionato come opzione scalabile. Non installato né necessario allo stato attuale del wiki (0 fonti). Da considerare quando il wiki supera le ~100 pagine.

## Fonti

[[source/llm-wiki-pattern]]
