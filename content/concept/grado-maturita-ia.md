---
title: "Grado di maturità dell'amministrazione (modello AgID)"
type: concept
tags: [governance-scolastica, politiche, ai, sistemi]
created: 2026-11-16
updated: 2026-11-16
sources: ["Determinazione AgID n. 17/2025, Allegato A", "Vargiu Scuola, nota SVR 89/2026"]
---

## Definizione
Strumento di **autovalutazione** con cui un'amministrazione misura la propria capacità di adottare e governare sistemi di IA, **prima** di pianificare qualsiasi intervento. Previsto dalle [[entity/agid|Linee guida AgID]] per l'adozione dell'IA nella PA (Determinazione n. 17/2025), che raccomandano l'autovalutazione preliminare a ogni processo strutturato di adozione.

Produce due profili: l'**AS IS** (dove ci si trova oggi) e il **TO BE** (dove si intende arrivare in un orizzonte ragionevole, tipicamente un anno). Il confronto fra i due identifica le priorità di intervento.

## Come funziona
**Cinque dimensioni × quattro livelli** di maturità crescente. Nella declinazione scolastica:

- **A. Dati e patrimonio informativo** — qualità, strutturazione e disponibilità dei dati.
- **B. Metodologie e algoritmi** — conoscenza e uso consapevole degli strumenti disponibili.
- **C. Organizzazione e competenze** — referente, gruppo di lavoro, DPO, competenze interne ed esterne.
- **D. Cultura scolastica** — consapevolezza e apertura del personale, discussione collegiale del tema.
- **E. Relazione con l'utenza scolastica** — informazione, coinvolgimento e partecipazione di studenti e famiglie.

Le prime tre riprendono l'Allegato A della Determinazione AgID; le ultime due sono una declinazione al contesto scolastico delle dimensioni che AgID riferisce alla cultura organizzativa e al rapporto con l'utenza, riformulate per la specificità della comunità educante e la presenza di minori.

Due raccomandazioni operative: **due schede distinte**, una per l'attività didattica e una per quella amministrativa, perché i due ambiti possono avere maturità molto diversa nello stesso istituto; e la **ripetizione a fine anno**, perché «una valutazione compiuta una sola volta è una fotografia; ripetuta nel tempo diventa uno strumento di governo».

La scheda organizzativa è affiancata da un **questionario al personale** che scende al livello operativo: strumenti già in uso, casi d'uso concreti, consapevolezza dei rischi, fabbisogni formativi. È lo strumento che fa emergere la [[concept/shadow-ai|Shadow AI (uso non dichiarato dell'IA)]].

## Applicazioni o esempi
Posizionamenti ricorrenti osservati nelle scuole italiane (osservatorio di un consulente su alcune migliaia di istituti, non rilevazione pubblicata):

- **A**: prevalentemente livello 2–3. Infrastruttura presente (protocollo, registro elettronico, SIDI, UNICA, cloud), ma documenti non strutturati, dati frammentati fra sistemi non interoperabili.
- **B**: livello 1–2. Uso individuale e non regolamentato, senza criteri condivisi di valutazione.
- **C**: molte scuole ancora al livello 1, nessuna struttura dedicata. Obiettivo realistico: livello 3.
- **D**: eterogenea, prevalenza 1–2.
- **E**: **la dimensione più arretrata**, larga prevalenza del livello 1 — nessuna iniziativa di comunicazione verso studenti e famiglie.

## Relazioni con altri concetti
- [[concept/governance-scolastica-ia|Governance scolastica dell'IA]] — l'autovalutazione è il primo atto istruttorio del percorso
- [[concept/piano-istituto-ia|Piano d'Istituto per l'IA (PIA) e Atto di Indirizzo]] — il profilo AS IS è la prima sezione del Piano e ne giustifica le scelte
- [[concept/shadow-ai|Shadow AI (uso non dichiarato dell'IA)]] — il questionario al personale è lo strumento che la fa emergere
- [[concept/caso-uso-ia|Caso d'uso dell'IA (unità di classificazione del rischio)]] — la ricognizione fornisce il materiale da classificare
- [[concept/ia-pubblica-amministrazione|IA nella Pubblica Amministrazione]] — il modello nasce per la PA, la scuola lo declina
- [[concept/divario-digitale|Divario digitale]] — il modello rende misurabile la distanza fra istituti

## Contraddizioni e dibattiti
**Il livello massimo non è l'obiettivo.** «Per un istituto scolastico, raggiungere il livello 4 in tutte le dimensioni è un obiettivo irrealistico e non necessario»: il TO BE ragionevole è avanzare di un livello nelle dimensioni più arretrate. È un'impostazione che contrasta con la lettura delle maturity scale come percorsi obbligati verso il massimo.

**La dimensione più trascurata è quella che la normativa richiede.** La relazione con l'utenza è ovunque al livello più basso, benché Linee Guida MIM e GDPR richiedano trasparenza verso le famiglie quando si adottano strumenti che riguardano minori.

**Un paradosso dell'autovalutazione sincera.** Se la rilevazione sul personale è nominativa e fa emergere un trattamento illecito ancora in corso, il dirigente titolare è tenuto a intervenire e, ricorrendone i presupposti, a valutare gli adempimenti degli artt. 33 e 34 GDPR. La stessa indagine che serve a governare può produrre l'obbligo di notificare una violazione — ed è la ragione per cui si raccomanda la forma anonima.

## Fonti
[[source/vargiu-svr-89-26-grado-maturita-ia|SVR 89/26 — Valutare il grado di maturità dell'amministrazione]], [[source/agid-bozza-di-linee-guida-per-l-adozione-di-ia-nella-pu|AgID — Bozza di linee guida per l'adozione di IA nella Pubblica Amministrazione (v1.0, 2025)]], [[source/linee-guida-agid-ia-pa-2026|Linee Guida AgID per l'adozione di IA nella PA — versione definitiva (det. 169/2026)]]
