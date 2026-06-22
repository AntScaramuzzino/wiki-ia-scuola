---
title: "WEBINAR — Linee guida del MIM sull'IA: aspetti normativi e didattici (Redaelli, Galli)"
type: source
tags: [ai, educazione, normativa, privacy, governance-scolastica-ia, ai-formazione, valutazione]
created: 2026-06-21
updated: 2026-06-21
sources: ["WEBINAR | Linee guida del MIM sull'Intelligenza Artificiale: aspetti normativi e didattici"]
---

# WEBINAR — Linee guida del MIM sull'IA: aspetti normativi e didattici (Redaelli, Galli)

**File raw**: `raw/notes/linee-guida-del-mim-sull-intelligenza-artificiale-aspetti-normativi-e-.md`
**Origine**: NotebookLM «Linee Guida sull'Intelligenza Artificiale a Scuola»

## Sommario
Trascrizione di un webinar dell'Associazione Culturale Didattica Innovativa con Lorenzo Redaelli (docente, animatore digitale, autore de *La classe potenziata*) sugli aspetti didattici e Piergiorgio Galli (DPO scolastico) sugli aspetti normativi delle linee guida MIM sull'IA. Il webinar legge criticamente il documento, evidenziando come la scuola diventi *deployer* di IA quando attiva Gemini o Copilot nelle proprie piattaforme, e analizza in dettaglio gli adempimenti privacy (DPIA/FRIA) che ne discendono. È una fonte sostanziale: aggiunge interpretazione operativa e casi pratici non presenti nel testo normativo.

## Punti chiave
- Le linee guida MIM sono giudicate generiche, con pochi divieti netti ma "paletti" significativi sul piano della privacy; rinviano alla piattaforma Unica per FAQ e modulistica.
- Concetto centrale: la scuola è **deployer** ai sensi dell'AI Act quando il DS attiva l'IA (Gemini in Workspace, Copilot in Microsoft 365) per docenti/studenti tramite account scolastico — quindi è responsabile dell'uso, non Google/Microsoft.
- Distinzione netta tra **canale account scolastico** (scuola deployer, soggetta a obblighi) e **canale account personale** (es. docente che usa ChatGPT a casa, fuori dal perimetro).
- Sistemi ad alto rischio (AI Act art. 6, Allegato III): l'IA usata per valutare risultati d'apprendimento o determinare ammissioni rientra nell'alto rischio; un LLM che valuta automaticamente elaborati è ad alto rischio, una traduzione no.
- La scuola è **titolare del trattamento**; deve nominare i fornitori (Google, Microsoft, Argo, Spaggiari, Canva) come **responsabili del trattamento** con atto/contratto formale e dare istruzioni scritte.
- **DPIA** (valutazione d'impatto) obbligatoria prima del trattamento; criticità: la scuola deve dichiarare misure di sicurezza e fonti di rischio interne dei fornitori (segreti industriali) — di fatto quasi impraticabile. Esiste il software del Garante per redigerla.
- **FRIA** (valutazione d'impatto sui diritti fondamentali) richiesta se la scuola classifica il sistema come ad alto rischio; comporta misure di sorveglianza umana difficili da garantire (es. uso domestico degli studenti).
- Criticità privacy nei prompt: lo studente può inserire dati sensibili (identità di genere, condizioni di salute) anche senza addestramento del modello; preferibile uso senza dati personali identificativi e disattivazione cronologia conversazioni (possibile a livello admin in Gemini).
- Vincoli sull'età: sotto i 13 anni di fatto inutilizzabile per gli studenti; Canva e strumenti consumer non utilizzabili se trattano dati degli studenti senza nomina a responsabile.
- Auspicio dei relatori: il Ministero avrebbe potuto fare una sola valutazione d'impatto centralizzata per Gemini/Copilot anziché lasciarla a migliaia di dirigenti.

## Entità menzionate
[[entity/mim]] — autore delle linee guida commentate
[[entity/garante-privacy]] — software per la DPIA
[[entity/commissione-europea]] — AI Act, classificazione del rischio

## Concetti trattati
[[concept/governance-scolastica-ia]] — ruolo deployer della scuola, nomine, responsabilità
[[concept/privacy-protezione-dati]] — DPIA, titolare/responsabile, minimizzazione
[[concept/valutazione-integrita-accademica]] — IA per valutare elaborati = alto rischio
[[concept/supervisione-umana]] — sorveglianza umana richiesta dalla FRIA
[[concept/ia-generativa]] — Gemini, Copilot, ChatGPT
[[concept/llm]] — valutazione automatica di elaborati
[[concept/allucinazione]] — citata a proposito delle risposte dei chatbot
[[concept/prompt]] — rischio di inserimento dati personali

## Citazioni rilevanti
> "La scuola diventa deployer di intelligenza artificiale quando attiva l'intelligenza artificiale dentro Google Workspace o dentro Microsoft Teams [...] la responsabilità di quello che fa l'intelligenza artificiale è la scuola."

> "L'aspetto più triste della vita in questo momento è che la scienza raccoglie conoscenza più velocemente di quanto la società raccolga saggezza." (Isaac Asimov, citato in chiusura)

## Contraddizioni o tensioni
Conferma e approfondisce operativamente [[source/linee-guida-mim-dm166-2025]] (fonte canonica): non contraddice il testo normativo ma ne segnala le criticità applicative (DPIA/FRIA difficili da redigere, mancanza di una valutazione centralizzata). Coerente con l'impianto deployer/rischio dell'AI Act ([[source/ai-act-ue]]).

## Domande aperte
- La piattaforma Unica fornirà davvero DPIA/FRIA precompilate o modelli centralizzati?
- Come gestire la sorveglianza umana quando lo studente usa l'IA a casa?
- Canva District con contratto e nomina a responsabile è sufficiente per l'uso con minori?
