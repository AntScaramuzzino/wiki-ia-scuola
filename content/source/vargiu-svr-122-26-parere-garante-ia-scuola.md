---
title: "SVR 122/26 — Il parere del Garante sull'IA a scuola (provv. 787/2026)"
type: source
tags: [normativa, privacy, governance-scolastica, politiche, ai]
created: 2026-11-16
updated: 2026-11-16
sources: ["Vargiu Scuola, nota SVR 122/2026, Assemini, 15 novembre 2026", "Garante per la protezione dei dati personali, provvedimento n. 787 del 20 ottobre 2026 (newsletter del 12 novembre 2026)"]
---

**File raw**: `raw/notes/vargiu-svr-122-26-parere-garante-ia-scuola.pdf` · `raw/notes/vargiu-svr-122-26-parere-garante-ia-scuola.md`
**Origine**: [[entity/vargiu-scuola|Vargiu Scuola]], nota SVR 122/2026, 15 novembre 2026. Commenta il provvedimento del [[entity/garante-privacy|Garante]] n. 787 del 20 ottobre 2026.

## Sommario
La novità normativa più rilevante entrata nel corpus da agosto 2026. Il **Garante ha espresso parere favorevole** sullo schema di decreto con cui il MIM detta le prime indicazioni operative sull'uso dell'IA a scuola — il decreto previsto dall'**art. 10, comma 3, del DM 166/2025**. Lo schema introduce una regola nuova: **gli studenti accedono ai sistemi di IA generativa soltanto con utenze pseudonimizzate**. Il Garante accompagna il parere con tre osservazioni al Ministero che equivalgono al riconoscimento che le scuole, da sole, non ce la fanno.

## Punti chiave
- **Lo stato dell'atto**: è un **parere su uno schema**. Il decreto non è ancora stato adottato e l'allegato tecnico non è pubblicato. Quanto riportato va verificato sul testo definitivo.
- **Il fondamento**: il decreto è quello previsto dall'**art. 10, comma 3, del DM 9 agosto 2025, n. 166**, che rinviava a successivi decreti, sentito il Garante, la disciplina delle modalità con cui le scuole progettano e realizzano le proprie iniziative di IA.
- **La pseudonimizzazione delle utenze studente** è «un'indicazione nuova rispetto alle Linee guida del 2025», che si limitavano a raccomandare richieste formulate preferibilmente senza dati identificativi.
- **L'architettura a due domini** dell'allegato tecnico: **Dominio A** — registro elettronico, anagrafica e **tabella di transcodifica** che associa ciascuno pseudonimo all'identità reale, sotto il controllo esclusivo della scuola e consultabile dal solo dirigente e dai docenti autorizzati; gestito dal partner tecnologico della scuola (es. fornitore del registro). **Dominio B** — il sistema di IA, che opera esclusivamente con identificativi pseudonimizzati; gestito dal partner tecnologico IA, al quale **è vietato trattare dati che consentano l'identificazione**. Entrambi i partner rilasciano alla scuola una **dichiarazione di conformità**.
- **La coincidenza dei due ruoli in capo allo stesso soggetto** è ammessa «soltanto con misure ulteriori che rendano effettiva la separazione dei domini». È precisamente la situazione di **Google Workspace for Education e Microsoft 365 for Education**, dove chi gestisce le identità degli studenti e chi fornisce le funzioni di IA coincidono.
- **Asimmetria studenti/personale**: l'obbligo di pseudonimizzazione riguarda **gli studenti**. Per il personale lo schema prevede tutele di natura diversa — rispetto della disciplina lavoristica, attenzione ai dati inseriti nelle richieste, tracciamento delle operazioni. **Il personale può continuare ad accedere con le proprie credenziali istituzionali nominative.**
- **Altre previsioni dello schema**: astensione dalle pratiche vietate dall'art. 5 del Reg. (UE) 2024/1689, fra cui l'inferenza delle emozioni; attenzione ai sistemi ad alto rischio; divieto per tutti di inserire dati personali nei sistemi generativi, con **campagne informative** di disincentivo; richiamo ai principi dell'art. 5 GDPR; **tracciamento delle operazioni**; fornitori con adeguate garanzie e dati che **di regola non escono dallo Spazio economico europeo**.
- **Le tre osservazioni del Garante al Ministero**: fornire **supporto** alle scuole, anche con futuri interventi regolatori che tengano conto dell'evoluzione tecnologica; **orientare le scelte** stabilendo direttamente standard, requisiti e modelli che i fornitori dovrebbero possedere, e individuando **servizi-tipo**; valutare l'opportunità di creare un **servizio di assistenza** alle scuole, anche nei rapporti con i fornitori.
- **La conseguenza operativa più pesante**: senza accorgimenti tecnici specifici, «l'impiego autonomo degli strumenti generativi da parte degli studenti non sarà praticabile». La scuola con Google Workspace potrà ammettere Gemini al personale **ma non agli studenti tramite l'identità del proprio dominio**. Le scuole che hanno già approvato regolamenti che ammettono l'uso autonomo **dovranno aggiornarli**.
- **L'uso mediato dal docente resta pienamente coerente** con lo schema.
- **La formazione va estesa a tutto il personale**, docente e amministrativo: «non è sufficiente che un gruppo di docenti o le figure referenti seguano attività formative specifiche».

## Entità menzionate
[[entity/garante-privacy|Garante per la protezione dei dati personali]], [[entity/mim|Ministero dell'Istruzione e del Merito (MIM)]], [[entity/vargiu-scuola|Vargiu Scuola]]

## Concetti trattati
[[concept/pseudonimizzazione-utenze-studenti|Pseudonimizzazione delle utenze studente]] — l'architettura a due domini e i suoi presupposti
[[concept/privacy-protezione-dati|Privacy e protezione dei dati]] — minimizzazione, localizzazione SEE, tracciamento
[[concept/governance-scolastica-ia|Governance scolastica dell'IA]] — il riconoscimento che la governance richiede supporto esterno
[[concept/referente-ia|Referente per l'IA (interno ed esterno)]] — la tesi del referente esterno alla luce del parere
[[concept/regolamento-ia-istituto|Regolamento d'istituto per l'uso dell'IA]] — i regolamenti già adottati da aggiornare
[[concept/alfabetizzazione-ia|Alfabetizzazione all'IA (AI Literacy)]] — formazione estesa a tutto il personale
[[concept/riconoscimento-emozioni|Riconoscimento delle emozioni (pratica vietata)]] — fra le pratiche da cui astenersi
[[concept/deployer|Deployer (utilizzatore professionale di IA)]] — le dichiarazioni di conformità dei due partner tecnologici

## Citazioni rilevanti
> "In un contesto delicato come quello scolastico, e con strumenti in continua evoluzione, le singole istituzioni non possono essere lasciate sole nelle scelte che la materia richiede."

> "Allo stato, gli strumenti di supporto sollecitati dal Garante non sono disponibili."

## Contraddizioni o tensioni
**Una tensione nuova, e strutturale: la regola arriva prima della condizione che la rende applicabile.** Il Garante impone la separazione fra chi conosce l'identità dello studente e chi eroga l'IA, ma i due ambienti che la quasi totalità delle scuole italiane usa — Google Workspace for Education e Microsoft 365 for Education — fanno coincidere i due soggetti. È l'ipotesi che il parere qualifica come residuale e che richiede misure ulteriori. Il risultato pratico è che l'uso autonomo dell'IA generativa da parte degli studenti diventa, per ora, impraticabile nella maggior parte degli istituti.

**Il Garante riconosce un vuoto che nessuno colma.** Le tre osservazioni al Ministero — standard per i fornitori, servizi-tipo, servizio di assistenza — descrivono ciò che oggi non esiste. È il riconoscimento istituzionale della tensione che il wiki registrava come «FRIA inassolvibile»: la scuola-deployer non dispone delle informazioni e delle competenze per valutare i fornitori. Qui il rilievo arriva dall'autorità di controllo, non dai commentatori.

**Conferma retroattiva di una scelta prudenziale.** L'impianto delle note 91/26 e 93/26, che escludeva l'uso autonomo degli studenti in prima applicazione, risulta allineato allo schema di decreto. Ma la nota 93/26 definiva le condizioni per l'apertura **senza prevedere la pseudonimizzazione**: tre mesi dopo, quelle condizioni sono insufficienti. Vedi [[source/vargiu-svr-93-26-regolamento-ia|SVR 93/26 — Il Regolamento per l'uso degli strumenti di IA]].

**Interessata, ma non per questo infondata.** La nota conclude che ogni scuola dovrebbe dotarsi di un referente esterno per l'IA — servizio che l'emittente offre. L'argomento (le tre osservazioni del Garante descrivono un bisogno di competenze che l'istituto non ha) sta in piedi da sé; la soluzione proposta è una delle possibili.

## Domande aperte
- Quando sarà adottato il decreto, e il testo definitivo confermerà l'obbligo di pseudonimizzazione nei termini dello schema?
- Chi costruisce in concreto l'architettura a due domini? Il fornitore del registro elettronico ha interesse e competenza per farlo?
- Il Ministero darà seguito alle tre osservazioni del Garante, e in quali tempi?
- Che cosa accade alle scuole che hanno già deliberato l'uso autonomo degli studenti, nel periodo fra il parere e l'adozione del decreto?
