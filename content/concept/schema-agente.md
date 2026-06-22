---
title: "Schema Agente (CLAUDE.md / AGENTS.md)"
type: concept
tags: [workflow, configurazione, llm]
created: 2026-04-22
updated: 2026-04-22
sources: [llm-wiki-pattern.md]
---

# Schema Agente

## Definizione

File di configurazione (CLAUDE.md per Claude Code, AGENTS.md per Codex) che trasforma un LLM generico in un wiki-maintainer disciplinato. Definisce struttura, convenzioni, workflow e regole comportamentali. È il layer che rende il sistema riproducibile tra sessioni diverse.

## Come funziona

Lo schema contiene:
- Struttura delle directory
- Formato delle pagine (frontmatter, sezioni standard)
- Protocollo per ogni operazione (ingest, query, lint)
- Convenzioni di naming
- Regole comportamentali (no invenzioni, cita sempre, aggiorna non duplicare)

L'agente legge questo file all'inizio di ogni sessione prima di qualsiasi altra operazione.

## Applicazioni o esempi

- `CLAUDE.md` in questo wiki (questo file è lo schema di questo wiki)
- Evolve nel tempo: utente e LLM co-evolvono lo schema in base a ciò che funziona

## Relazioni con altri concetti

- [[concept/wiki-persistente]] — lo schema è il layer che governa il wiki
- [[concept/ingest]] — il protocollo di ingest è definito nello schema
- [[concept/lint-wiki]] — il protocollo di lint è definito nello schema

## Fonti

[[source/llm-wiki-pattern]]
