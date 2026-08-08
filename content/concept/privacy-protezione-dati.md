---
title: "Privacy e protezione dei dati"
type: concept
tags: [ai, privacy, normativa, etica, educazione, ai-società, politiche]
created: 2026-06-21
updated: 2026-08-08
sources: [Legge 132/2025, Regolamento UE 2024/1689 (AI Act), Linee Guida MIM (DM 166/2025), Manifesto + Codice Etico IA Generativa a Scuola (ISIS Europa)]
---

## Definizione
Insieme dei principi e degli adempimenti che la scuola deve rispettare nel trattamento dei dati personali connessi all'uso dell'IA, disciplinati dal GDPR e dall'AI Act. La protezione è una priorità assoluta perché i dati riguardano in maggioranza minori. I sistemi devono essere progettati secondo **privacy by design** e **privacy by default**, limitando la raccolta dei dati allo stretto necessario (minimizzazione).

## Come funziona
- **DPIA (Data Protection Impact Assessment)**: prima di implementare qualsiasi sistema IA, la scuola — in qualità di Titolare del Trattamento — è obbligata a eseguire una Valutazione d'Impatto sulla Protezione dei Dati ai sensi dell'art. 35 del GDPR.
- **FRIA (Fundamental Rights Impact Assessment)**: se la scuola adotta un sistema ad alto rischio (es. valutazione degli studenti), l'Art. 27 dell'AI Act impone di integrare la DPIA con una Valutazione d'Impatto sui Diritti Fondamentali, che descrive processi, categorie di persone interessate, rischi di danno e misure di mitigazione e supervisione.
- **Diritto di non partecipazione (opt-out)**: studenti e famiglie possono scegliere di non far utilizzare i propri dati per l'addestramento dei sistemi di IA, senza discriminazione o limitazione nell'accesso all'istruzione.
- **Divieto di dati sensibili nei prompt**: è vietato/fortemente sconsigliato inserire dati personali, sensibili o identificativi (come PEI e PDP) nei prompt forniti a modelli linguistici aperti.

## Applicazioni o esempi
- Uso di **dati sintetici** al posto di dati reali laddove non strettamente indispensabili, per azzerare i rischi di profilazione (raccomandazione del Garante).
- Revisione delle policy privacy e adozione di regolamenti d'uso che vietino l'inserimento di dati sensibili nei prompt.
- Consultazione obbligatoria del DPO per la stesura di DPIA e FRIA.

## Relazioni con altri concetti
- [[concept/governance-scolastica-ia|Governance scolastica dell'IA]] — DPIA, FRIA e ruolo del DPO sono parte della governance d'istituto.
- [[concept/dpia|DPIA — Valutazione d'Impatto sulla Protezione dei Dati]] — la valutazione d'impatto sulla protezione dati (art. 35 GDPR) in dettaglio.
- [[concept/dpia-fria|DPIA e FRIA — valutazioni d'impatto]] — il quadro che lega DPIA e [[concept/fria|FRIA — Valutazione d'Impatto sui Diritti Fondamentali]].
- [[concept/dati-sintetici|Dati sintetici]] — la misura raccomandata dal Garante per minimizzare il trattamento di dati reali.
- [[concept/opt-out|Diritto di non partecipazione (opt-out)]] — il diritto di non partecipazione all'uso dei dati per l'addestramento.
- [[concept/riconoscimento-emozioni|Riconoscimento delle emozioni (pratica vietata)]] — pratica vietata a scuola, presidio contro la profilazione dei minori.
- [[concept/trasparenza-algoritmica|Trasparenza algoritmica (art. 50 AI Act)]] — obbligo di informare gli utenti dell'interazione con un sistema di IA.
- [[concept/supervisione-umana|Supervisione umana (human-in-the-loop)]] — antropocentrismo e trasparenza sono principi condivisi.
- [[concept/didattica-inclusiva-ia|Didattica inclusiva con IA]] — i dati di PEI/PDP non possono essere inseriti nei prompt.
- [[concept/bias-algoritmico|Bias Algoritmico]] — la profilazione mal gestita può alimentare discriminazioni.
- [[entity/garante-privacy|Garante per la protezione dei dati personali]] — autorità che ha espresso parere sullo schema di decreto MIM.

## Contraddizioni e dibattiti
Il **parere del Garante Privacy** è stato favorevole allo schema di decreto del MIM, ma con condizioni rigorose: prediligere i dati sintetici ai dati reali quando possibile e ribadire il divieto assoluto di pratiche come il riconoscimento delle emozioni. La tensione di fondo è tra l'innovazione didattica basata sui dati e la minimizzazione del trattamento di dati di minori.

## Fonti
[[source/legge-132-2025|Legge 23 settembre 2025, n. 132]], [[source/ai-act-ue|AI Act — Regolamento (UE) 2024/1689]], [[source/linee-guida-mim-dm166-2025|Linee Guida MIM per l'IA a scuola (DM 166/2025)]], [[source/manifesto-codice-etico-isis-europa|Manifesto e Codice Etico IA Generativa a Scuola (ISIS Europa)]]
