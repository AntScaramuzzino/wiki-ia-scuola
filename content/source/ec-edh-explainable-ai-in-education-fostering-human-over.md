---
title: "EC/EDEH — Explainable AI in education: Fostering human oversight and shared responsibility (2025)"
type: source
tags: [ai, llm, machine-learning, educazione, competenze, etica, normativa, valutazione, ai-formazione]
created: 2026-06-21
updated: 2026-06-21
sources: ["2025 | EC EDH, Explainable AI in education: Fostering human oversight and shared responsibility"]
---

# EC/EDEH — Explainable AI in education: Fostering human oversight and shared responsibility (2025)

**File raw**: `raw/articles/2025-ec-edh-explainable-ai-in-education-fostering-human-oversight-and-.md`
**Origine**: NotebookLM «Linee Guida sull'Intelligenza Artificiale a Scuola»

## Sommario
Report 2025 dello squad dello European Digital Education Hub (EDEH) sull'IA spiegabile (Explainable AI, XAI) in educazione, prodotto per la Commissione Europea ed EACEA. Il documento introduce i fondamenti tecnici ed etici della XAI, ne analizza la conformità con AI Act e GDPR, esamina le prospettive dei diversi stakeholder su casi d'uso (sistemi di tutoring intelligente e generatori di piani di lezione) e definisce le competenze dei docenti per integrare la XAI. Tesi centrale: la spiegabilità è la condizione pratica per la supervisione umana e la responsabilità condivisa nell'IA educativa. (Il file raw contiene il "teaser" pubblico: capitoli 1 completo e indice/estratti dei capitoli 2–4.)

## Punti chiave
- La XAI è definita come sotto-campo dell'IA che fornisce spiegazioni sul perché un sistema produce un certo output; è la base pratica della maggior parte dei sette requisiti per la "trustworthy AI" del High-Level Expert Group della Commissione (2019).
- Quattro concetti core organizzati su due dimensioni: **dimensione tecnica** — trasparenza e interpretabilità; **dimensione umana** — spiegabilità e comprensibilità (understandability).
- Distinzione tra modelli **white-box** (intrinsecamente interpretabili: regole, alberi decisionali) e **black-box** (reti neurali, ensemble): per i secondi si usano tecniche di explainability post-hoc; esiste un trade-off tra performance e interpretabilità.
- Due approcci tecnici: **knowledge-based** (regole, facile da spiegare) e **data-driven/ML** (estrae pattern dai dati, spiegazioni più difficili). Campi critici come educazione e sanità privilegiano la spiegabilità anche a scapito della performance.
- L'AI Act non impone esplicitamente la spiegabilità, ma richiede supervisione umana, data governance, cybersecurity e trasparenza, oltre al diritto di spiegazione nelle decisioni individuali.
- Caratteristiche di una buona spiegazione: chiarezza (linguaggio semplice, dettaglio a livelli), rilevanza, specificità (limiti e incertezze), tracciabilità (responsabilità, auditabilità), consistenza.
- Tre tipi di stakeholder (legislatori/policy-maker; ricercatori/sviluppatori; end-user) e tre livelli di utenza (AI novices, advanced AI users, AI experts).
- Bisogni distintivi della XAI in educazione: accountability, trasparenza, metacognizione e agency degli studenti, conformità legale (GDPR, protezione minori), gestione di dati "rumorosi", prevenzione di misconcezioni, design centrato sulla pedagogia.
- Richiamo al framework "AI Explainability in Practice" dell'Alan Turing Institute e alla tassonomia delle spiegazioni (scope, depth, alternatives, flow).

## Entità menzionate
[[entity/commissione-europea]] — committente del report tramite EACEA; quadro AI Act e linee guida etiche
[[entity/unesco]] — citata per le pratiche di open science a sostegno di equità e inclusione nell'IA

## Concetti trattati
[[concept/intelligenza-artificiale]] — definizione (art. 3 AI Act), autonomia e adattività dei sistemi
[[concept/machine-learning]] — approccio data-driven, parametri numerici, opacità dei modelli
[[concept/llm]] — IA come strumento general-purpose, possibilità di output inaccurati
[[concept/supervisione-umana]] — human oversight come finalità della XAI e requisito AI Act
[[concept/bias-algoritmico]] — trasparenza su dati e fairness, bias nei dataset educativi
[[concept/privacy-protezione-dati]] — conformità GDPR, protezione dei minori
[[concept/alfabetizzazione-ia]] — capacity building, competenze dei docenti verso la XAI
[[concept/valutazione-integrita-accademica]] — auditabilità e accountability nelle valutazioni IA-assistite

## Citazioni rilevanti
> "For an AI system to be trustworthy, we must be able to understand why it behaved a certain way and why it provided a given interpretation."

> "the need to obtain a clear explanation to guarantee that AI is assisting and not deciding."

> "Regarding the AI Act, it does not explicitly stipulate that AI must be explainable. Instead, human oversight, data governance, cybersecurity and transparency are referred to."

## Contraddizioni o tensioni
- Nessuna contraddizione diretta con altre pagine del wiki. Approfondisce il principio di supervisione umana e di trasparenza già presente in [[source/ai-act-ue]] e [[source/unesco-guidance-genai-2023]], introducendo il tema specifico della spiegabilità (XAI), poco coperto altrove.
- Tensione concettuale segnalata dalla fonte stessa: trade-off tra performance dei modelli (favorevole ai black-box) e necessità di spiegabilità (favorevole ai white-box), particolarmente acuto in educazione.

## Domande aperte
- Il file raw è un teaser: capitoli 2 (compliance AI Act/GDPR), 3 (casi d'uso ITS e LPG) e 4 (competenze docenti) sono solo accennati. Vale la pena recuperare il report integrale.
- Come tradurre operativamente le competenze XAI dei docenti nei curricoli (primaria → formazione professionale)?
