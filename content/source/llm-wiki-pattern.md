---
title: "LLM Wiki — Il Pattern del Second Brain"
type: source
tags: [llm, knowledge-management, wiki, second-brain, rag]
created: 2026-04-22
updated: 2026-04-22
sources: [Benvenuto.md]
---

# LLM Wiki — Il Pattern del Second Brain

**File raw**: `Benvenuto.md`

---

## Sommario

Il documento descrive un pattern per costruire una base di conoscenza personale persistente usando LLM. Invece di usare RAG classico (recupero al momento della query), l'LLM costruisce e mantiene incrementalmente un wiki strutturato in markdown che funge da artefatto cumulativo. L'utente cura le fonti e fa domande; l'LLM fa tutto il bookkeeping.

---

## Punti chiave

- **RAG vs Wiki**: RAG ri-deriva la conoscenza ad ogni query. Il wiki la compila una volta e la mantiene aggiornata — la differenza è strutturale, non di qualità
- **Artefatto cumulativo**: ogni fonte aggiunta arricchisce pagine esistenti, non crea un silo separato
- **Tre layer**: fonti raw (immutabili) → wiki (owned dall'LLM) → schema (CLAUDE.md / AGENTS.md)
- **L'utente non scrive il wiki**: l'LLM produce tutto il contenuto; l'utente legge, naviga e guida
- **Le risposte alle query possono diventare pagine**: le analisi non devono andare perse nella chat history
- **Lint periodico**: l'LLM può fare health-check autonomo su contraddizioni, orfani, lacune

---

## Entità menzionate

[[entity/vannevar-bush]] — ideatore del Memex (1945)
[[entity/obsidian]] — IDE per il wiki (graph view, Dataview, Marp)
[[entity/notebooklm]] — esempio di sistema RAG classico (contrasto)
[[entity/qmd]] — motore di ricerca locale per markdown (BM25 + vector)

---

## Concetti trattati

[[concept/rag]] — Retrieval-Augmented Generation, il paradigma alternativo
[[concept/wiki-persistente]] — il concetto centrale: wiki come artefatto cumulativo
[[concept/memex]] — visione di Bush del 1945, precursore concettuale
[[concept/ingest]] — operazione di aggiunta e integrazione di una fonte
[[concept/lint-wiki]] — health-check periodico del wiki
[[concept/schema-agente]] — CLAUDE.md / AGENTS.md come configurazione dell'LLM

---

## Citazioni rilevanti

> "The wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged."

> "Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored."

> "The human's job is to curate sources, direct the analysis, ask good questions. The LLM's job is everything else."

---

## Contraddizioni o tensioni

Nessuna contraddizione interna. La fonte è programmatica e intenzionalmente astratta — non prescrive implementazioni specifiche.

---

## Domande aperte

- Qual è il dominio specifico di questo wiki? (da definire con l'utente)
- Quale soglia di fonti richiede un motore di ricerca (qmd) invece del solo index.md?
- Come gestire fonti in lingue diverse (italiano/inglese)?
