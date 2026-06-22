---
title: "Lint Wiki"
type: concept
tags: [workflow, manutenzione, qualità]
created: 2026-04-22
updated: 2026-04-22
sources: [llm-wiki-pattern.md]
---

# Lint Wiki

## Definizione

Operazione periodica di health-check del wiki. L'LLM scansiona le pagine alla ricerca di problemi strutturali, incoerenze e lacune, e propone azioni correttive.

## Come funziona

L'LLM cerca:
- **Pagine orfane**: nessun link in entrata da altre pagine
- **Contraddizioni**: claim opposti sulla stessa entità/concetto in pagine diverse
- **Claim superati**: affermazioni che fonti più recenti hanno smentito o aggiornato
- **Concetti mancanti**: termini usati in molte pagine ma senza pagina dedicata
- **Cross-reference assenti**: link ovvi non presenti
- **Lacune di conoscenza**: aree del dominio non coperte da nessuna fonte

Dopo il lint, l'LLM propone: nuove pagine da creare, aggiornamenti da fare, fonti da cercare.

## Applicazioni o esempi

- "Fai un lint del wiki"
- "Health check — ci sono contraddizioni tra le pagine?"
- Lint automatico periodico (es. ogni 10 ingest)

## Relazioni con altri concetti

- [[concept/ingest]] — operazione complementare (crescita vs manutenzione)
- [[concept/wiki-persistente]] — il lint è ciò che mantiene il wiki sano nel tempo

## Fonti

[[source/llm-wiki-pattern]]
