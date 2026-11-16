---
title: "Pseudonimizzazione delle utenze studente"
type: concept
tags: [privacy, normativa, governance-scolastica, ai, politiche]
created: 2026-11-16
updated: 2026-11-16
sources: ["Garante privacy, provv. n. 787 del 20 ottobre 2026", "Vargiu Scuola, nota SVR 122/2026"]
---

## Definizione
Misura tecnica e organizzativa per cui **gli studenti accedono ai sistemi di IA — in particolare generativi — mediante identificativi che non consentono al fornitore di risalire alla loro identità**. Le informazioni aggiuntive che permettono la re-identificazione sono conservate separatamente dalla scuola e consultabili soltanto dal dirigente scolastico e dai docenti autorizzati.

È prevista dallo schema di decreto ministeriale su cui il [[entity/garante-privacy|Garante]] ha espresso **parere favorevole con il provvedimento n. 787 del 20 ottobre 2026**, reso noto con la newsletter del 12 novembre. Il decreto — previsto dall'**art. 10, comma 3, del DM 166/2025** — alla data del 16 novembre 2026 **non è ancora stato adottato**, e l'allegato tecnico non è pubblicato.

## Come funziona
L'allegato tecnico traduce la regola in **due ambienti distinti**, ciascuno affidato a un soggetto diverso.

| Dominio | Che cosa contiene | Chi lo gestisce |
|---|---|---|
| **A** | Registro elettronico, anagrafica studenti e **tabella di transcodifica** che associa ogni pseudonimo all'identità reale, sotto controllo esclusivo della scuola | Partner tecnologico della scuola (es. fornitore del registro elettronico) |
| **B** | Il sistema di IA, che opera **esclusivamente** con identificativi pseudonimizzati | Partner tecnologico IA, cui è **vietato** trattare dati che consentano l'identificazione |

Entrambi i partner rilasciano alla scuola una **dichiarazione di conformità** alle misure dell'allegato, che individua anche i compiti del dirigente scolastico e le regole con cui i docenti formulano richieste che non consentano di identificare le persone.

La **coincidenza dei due ruoli in capo al medesimo soggetto** è ammessa dal parere solo come ipotesi residuale, con misure ulteriori che rendano effettiva la separazione dei domini.

## Applicazioni o esempi
- Una scuola con Google Workspace for Education potrà ammettere Gemini **per il personale**, ma non potrà consentirlo agli studenti attraverso l'identità rilasciata nel proprio dominio, perché Google sarebbe insieme gestore delle identità e fornitore dell'IA.
- L'**uso mediato dal docente** — lo strumento è impiegato dall'insegnante con la propria utenza e gli studenti non vi accedono con utenze proprie — resta pienamente coerente con lo schema e non richiede pseudonimizzazione.
- Il **personale** non è soggetto all'obbligo: può continuare ad accedere con credenziali istituzionali nominative, con tutele di natura diversa (disciplina lavoristica, attenzione ai dati inseriti, tracciamento delle operazioni).

## Relazioni con altri concetti
- [[concept/privacy-protezione-dati|Privacy e protezione dei dati]] — è un'applicazione del principio di minimizzazione a un contesto nuovo
- [[concept/regolamento-ia-istituto|Regolamento d'istituto per l'uso dell'IA]] — i regolamenti che ammettono l'uso autonomo degli studenti andranno aggiornati
- [[concept/governance-scolastica-ia|Governance scolastica dell'IA]] — l'architettura a due domini è una scelta di governance, non solo tecnica
- [[concept/deployer|Deployer (utilizzatore professionale di IA)]] — la scuola resta titolare e deployer; i due partner sono responsabili del trattamento
- [[concept/alfabetizzazione-ia|Alfabetizzazione all'IA (AI Literacy)]] — lo schema accompagna la misura con campagne informative di disincentivo all'inserimento di dati personali
- [[concept/divario-digitale|Divario digitale]] — l'onere tecnico di costruire i due domini non è alla portata di tutti gli istituti

## Contraddizioni e dibattiti
**La regola arriva prima della condizione che la rende applicabile.** I due ambienti che la quasi totalità delle scuole italiane usa — Google Workspace for Education e Microsoft 365 for Education — fanno coincidere chi gestisce le identità degli studenti e chi fornisce le funzioni di IA: è esattamente l'ipotesi che il parere qualifica come residuale. L'esito pratico è che l'impiego autonomo dell'IA generativa da parte degli studenti diventa, per ora, impraticabile nella generalità degli istituti.

**Il Garante stesso rileva il vuoto.** Le tre osservazioni rivolte al Ministero — supporto alle scuole, standard e servizi-tipo per i fornitori, un servizio di assistenza dedicato — descrivono strumenti che oggi non esistono. È il riconoscimento, da parte dell'autorità di controllo, che la valutazione di un fornitore di IA e la configurazione di un'architettura come quella descritta «richiedono competenze che una singola scuola difficilmente possiede».

**Chi costruisce l'architettura?** Il Dominio A è affidato al fornitore del registro elettronico, soggetto che finora non ha avuto alcun ruolo nell'erogazione di servizi di IA. Il corpus non contiene elementi su disponibilità, costi o tempi di questa integrazione.

## Fonti
[[source/vargiu-svr-122-26-parere-garante-ia-scuola|SVR 122/26 — Il parere del Garante sull'IA a scuola (provv. 787/2026)]], [[source/linee-guida-mim-dm166-2025|Linee Guida MIM per l'IA a scuola (DM 166/2025)]]
