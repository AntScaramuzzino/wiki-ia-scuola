---
title: "L'IA in segreteria: l'area meno regolata della scuola è quella con più dati veri"
type: analysis
tags: [governance-scolastica-ia, privacy, automazione, normativa, ai-società]
created: 2026-09-19
updated: 2026-09-19
sources: [ia-e-personale-amministrativo-scolastico-applicazioni-e, linee-guida-mim-dm166-2025, agid-bozza-di-linee-guida-per-l-adozione-di-ia-nella-pu, ia-nella-pubblica-amministrazione-pubblicata-la-prima-i, legge-132-2025, ai-act-ue, ai-act-digital-omnibus-2026, dm-219-2025-snodi-formativi, adempimenti-e-cronoprogramma]
---

## Domanda
Che cosa cambia concretamente per DSGA e personale ATA con l'introduzione dell'IA a scuola, e quali obblighi ricadono sulla segreteria e non sulla didattica?

## Risposta sintetica
Cambia meno di quanto promettono i documenti e più di quanto la segreteria sappia. L'area amministrativa è presentata da tutte le fonti come il terreno facile dell'IA — snellimento del back-office, rischio pedagogico nullo — ma è anche l'unica area della scuola in cui l'IA tocca da subito dati personali reali di famiglie e lavoratori, senza il rinvio al 2027 di cui beneficia la didattica e senza un corrispettivo operativo delle Linee Guida. Il risultato è un'asimmetria: sulla valutazione degli apprendimenti il wiki documenta un apparato di adempimenti dettagliato; sulla segreteria documenta un elenco di casi d'uso e nulla sulle garanzie.

## Analisi

### Che cosa dicono davvero le fonti sull'area amministrativa

Le [[source/linee-guida-mim-dm166-2025|Linee Guida MIM (DM 166/2025)]] individuano tre ambiti applicativi — didattica, amministrazione, organizzazione — e collocano DSGA e ATA nel secondo, sotto la voce "snellimento burocratico". La scheda dedicata, [[source/ia-e-personale-amministrativo-scolastico-applicazioni-e|IA e personale amministrativo scolastico]], dettaglia quattro applicazioni: chatbot per lo smistamento delle richieste (orari, iscrizioni, certificazioni), verifica documentale con controllo dei titoli, gestione di comunicazioni e circolari periodiche, gestione di inventario e beni mobili.

È utile essere espliciti su un punto: quella scheda è l'unica pagina del wiki interamente dedicata all'area amministrativa, e la sua stessa nota di ingest rileva che non aggiunge fatti nuovi rispetto alla fonte canonica — ne isola una parte. Tutto ciò che il corpus dice di specifico sulla segreteria sta in quattro righe di casi d'uso e in una prescrizione procedurale: nella sezione "Progetti IA" di [[entity/piattaforma-unica|Piattaforma Unica]], a cui la segreteria accede insieme al DS, **non vanno inseriti dati personali**, solo informazioni generali.

### Il paradosso del rischio: meno vincoli, più esposizione

L'intuizione diffusa è che la segreteria sia l'ambito a rischio basso. Sul piano della classificazione dell'AI Act è vero — ed è proprio questo il problema.

| | Didattica e valutazione | Back-office amministrativo |
|---|---|---|
| Classificazione AI Act | Alto rischio esplicito (Allegato III, p. 3) | Non classificato come tale nelle fonti del wiki; i chatbot ricadono nel rischio limitato |
| Obblighi Titolo III (alto rischio) | **Rinviati al 2 dicembre 2027** dal *Digital Omnibus* | Non applicabili |
| Trasparenza (art. 50) | Operativa dal 2 agosto 2026 | Operativa dal 2 agosto 2026 |
| Alfabetizzazione all'IA | Obbligo dal 2 febbraio 2025 | Obbligo dal 2 febbraio 2025 |
| DPIA (GDPR artt. 35 ss.) | Dovuta, nessun rinvio | Dovuta, nessun rinvio |
| Guida operativa MIM dedicata | Ampia (PIA, RIA, cronoprogramma) | Assente |

Il [[source/ai-act-digital-omnibus-2026|Digital Omnibus]] ha spostato al 2 dicembre 2027 gli obblighi sull'alto rischio dell'Allegato III, istruzione inclusa: la parte didattica ha guadagnato sedici mesi. Quello che **non** è stato rinviato — trasparenza dell'art. 50, divieti, alfabetizzazione — vale invece dal 2 agosto 2026, e vale per la segreteria esattamente come per la classe (vedi [[concept/ai-act-categorie-rischio|categorie di rischio]] e [[concept/trasparenza-algoritmica|trasparenza algoritmica]]). Il GDPR, dal canto suo, non ha mai avuto proroghe: la [[concept/dpia|DPIA]] è dovuta *prima* del trattamento ogni volta che il rischio è elevato, e nel back-office i dati non sono materiale d'esercizio — sono iscrizioni, certificazioni, fascicoli, titoli di servizio.

Detto altrimenti: la didattica ha ottenuto tempo sugli obblighi più pesanti; la segreteria non aveva quegli obblighi, ma ha da subito quelli che restano, e li ha su dati veri.

### Chi risponde, e di che cosa

La catena di governance ricostruita in [[concept/governance-scolastica-ia|governance scolastica dell'IA]] e in [[concept/piano-istituto-ia|Piano d'Istituto per l'IA]] nomina il DSGA tra le figure coinvolte — accanto a DS, Referente IA, Gruppo di Lavoro, DPO, organi collegiali — ma le fonti non gli assegnano compiti propri in materia di IA. Il DS resta Titolare del trattamento e la scuola nel suo insieme assume la qualifica di [[concept/deployer|deployer]].

Questo lascia un vuoto pratico. Chi censisce gli strumenti di IA già in uso negli applicativi di segreteria? Chi verifica che il gestionale adottato non abbia attivato funzioni generative? Chi redige l'informativa quando una famiglia scrive a un indirizzo presidiato da un chatbot? Le fonti indicano il censimento degli strumenti come presupposto della trasparenza, ma non dicono a chi tocchi nell'area amministrativa. Nel [[source/adempimenti-e-cronoprogramma|cronoprogramma]] il DSGA compare nell'elenco dei ruoli e il personale ATA nella "filosofia partecipativa": è un riconoscimento, non un mandato.

### Il vincolo che vale più degli altri: non delegabilità

L'[[source/legge-132-2025|art. 3 della Legge 132/2025]] stabilisce che nessun processo automatizzato può sostituire integralmente la volontà umana. Nella didattica questo principio viene discusso a proposito della valutazione; nel back-office ha un'applicazione più immediata e meno commentata, perché il lavoro di segreteria è fatto in buona parte di atti a rilevanza esterna.

La verifica documentale citata tra i casi d'uso è l'esempio critico: un controllo di titoli assistito da IA produce un esito che incide su posizioni giuridiche di persone. La [[concept/supervisione-umana|supervisione umana]] qui non è una raccomandazione pedagogica, è la condizione di legittimità dell'atto. Lo stesso vale, in forma più tenue, per la produzione di circolari e comunicazioni: il testo generato è pur sempre un atto della scuola, e le [[concept/allucinazione|allucinazioni]] in un avviso su scadenze o adempimenti non sono innocue.

Un precedente concreto è già nel wiki: la circolare in rima del liceo Galileo Ferraris di Torino, riportata nella rassegna del [[news/2026-09-14|14 settembre 2026]], è un caso di uso dell'IA nella comunicazione amministrativa **accompagnato dalla dichiarazione esplicita dell'elaborazione tramite IA**. La rassegna annota che è "tutt'altro che scontata" nelle segreterie: è esattamente la buona pratica che l'art. 50 rende attesa.

### Il termine di paragone della PA: efficienza senza misura

La scuola è PA, e ne eredita il quadro: le [[source/agid-bozza-di-linee-guida-per-l-adozione-di-ia-nella-pu|Linee Guida AgID]] pongono l'efficienza operativa tra i tre ambiti prioritari e mettono a disposizione nove allegati-strumenti (maturità, rischio, impatto, codice etico, casi d'uso, governance, KPI). La [[source/ia-nella-pubblica-amministrazione-pubblicata-la-prima-i|prima indagine AgID]] sulle amministrazioni centrali offre però un avvertimento che la segreteria scolastica farebbe bene a leggere come proprio: su 120 progetti censiti, il 42% ha come obiettivo l'efficienza operativa, oltre il 60% include chatbot, ma **solo il 20% ha KPI definiti**, le competenze interne sono limitate con forte dipendenza da consulenti esterni, e l'indagine rileva scarsa attenzione alla qualità dei dati.

Sono i tre rischi che un back-office scolastico corre nell'identica forma, con meno personale e senza un ufficio IT. Le raccomandazioni AgID — pilota prima della gara, KPI, figure dedicate come *AI Officer* e *Data Steward* — restano nel wiki senza un traducente scolastico: la domanda se quelle figure abbiano un analogo nella scuola è annotata come aperta e non ha risposta nelle fonti (vedi [[concept/ia-pubblica-amministrazione|IA nella Pubblica Amministrazione]]).

### La formazione c'è sulla carta, non nei numeri

Il [[source/dm-219-2025-snodi-formativi|DM 219/2025]] include esplicitamente ATA e DSGA nella formazione generale degli [[concept/snodi-formativi-pnrr|snodi formativi territoriali]], con contenuti mirati: snellimento della burocrazia, conformità normativa, privacy GDPR, supervisione umana sui processi automatizzati. È un elenco pertinente — e la data di fine progetto è inderogabilmente il 31/12/2026.

Ma la formazione dei formatori, cuore della scalabilità a cascata, crea un nucleo di **docenti**-esperti, e il modello di riferimento per i moduli amministrativi è il DigCompEdu, cioè un quadro costruito per gli educatori. La domanda quantitativa è registrata nel wiki e resta senza risposta: quanti dei 5.760 percorsi riguardano il personale ATA e DSGA rispetto ai docenti ([[source/formazione-pnrr-strumenti-2026|Formazione PNRR e strumenti per la classe (stato agosto 2026)]])? Finché quel dato manca, "formazione prevista anche per il personale amministrativo" è un'affermazione che nessuna fonte del corpus permette di verificare.

### Che cosa può fare una segreteria adesso

Ricavato dalle fonti, non da buone intenzioni:

1. **Censire** gli strumenti già in uso, incluse le funzioni generative attivate dentro gestionali e suite d'ufficio. È il presupposto indicato per poter informare in modo veritiero ([[concept/trasparenza-algoritmica|Trasparenza algoritmica (art. 50 AI Act)]]).
2. **Dichiarare** l'uso dell'IA nelle comunicazioni che escono dalla scuola, sul modello del caso di Torino.
3. **Non inserire dati personali** nella sezione "Progetti IA" di Piattaforma Unica: solo informazioni generali.
4. **Attivare la DPIA con il DPO** prima — non dopo — di introdurre un sistema che tratti dati di studenti, famiglie o personale; il DPO è di consultazione obbligatoria.
5. **Tenere la firma umana sull'atto**: ogni esito che incide su una posizione giuridica va validato da una persona, per l'art. 3 della Legge 132/2025.
6. **Portare l'area amministrativa dentro il PIA**, non trattarla come implementazione tecnica a valle del piano didattico.

## Fonti usate
- [[source/ia-e-personale-amministrativo-scolastico-applicazioni-e|IA e personale amministrativo scolastico]]
- [[source/linee-guida-mim-dm166-2025|Linee Guida MIM (DM 166/2025)]]
- [[source/legge-132-2025|Legge 132/2025]]
- [[source/ai-act-ue|AI Act (Reg. UE 2024/1689)]]
- [[source/ai-act-digital-omnibus-2026|AI Act — Digital Omnibus 2026]]
- [[source/agid-bozza-di-linee-guida-per-l-adozione-di-ia-nella-pu|Linee Guida AgID per l'IA nella PA]]
- [[source/ia-nella-pubblica-amministrazione-pubblicata-la-prima-i|Prima indagine AgID sull'IA nella PA]]
- [[source/dm-219-2025-snodi-formativi|DM 219/2025 — snodi formativi]]
- [[source/formazione-pnrr-strumenti-2026|Formazione PNRR e strumenti 2026]]
- [[source/adempimenti-e-cronoprogramma|Adempimenti e cronoprogramma]]
- [[concept/governance-scolastica-ia|Governance scolastica dell'IA]] · [[concept/ia-pubblica-amministrazione|IA nella Pubblica Amministrazione]] · [[concept/ai-act-categorie-rischio|AI Act — categorie di rischio]] · [[concept/trasparenza-algoritmica|Trasparenza algoritmica (art. 50 AI Act)]] · [[concept/dpia|DPIA — Valutazione d'Impatto sulla Protezione dei Dati]] · [[concept/supervisione-umana|Supervisione umana (human-in-the-loop)]] · [[concept/deployer|Deployer (utilizzatore professionale di IA)]] · [[concept/piano-istituto-ia|Piano d'Istituto per l'IA (PIA) e Atto di Indirizzo]] · [[concept/snodi-formativi-pnrr|Snodi formativi PNRR (DM 219/2025)]]
- [[news/2026-09-14|Rassegna del 14 settembre 2026]]

## Lacune e domande aperte
- **Nessun dato di adozione.** Il wiki documenta l'uso dell'IA da parte di studenti e docenti (83% e 66%, [[source/galli-ia-nella-didattica-2025|Galli — L'intelligenza artificiale nella didattica: opportunità, rischi e regole (2025)]]), ma non esiste nel corpus alcuna rilevazione sull'uso dell'IA nelle segreterie scolastiche italiane. Non sappiamo se il fenomeno di cui discutiamo sia marginale o già diffuso.
- **Gestione del personale: regime ignoto.** Le fonti del wiki trattano dell'Allegato III dell'AI Act solo il punto sull'istruzione. Se una segreteria usasse l'IA per selezione, valutazione o gestione del personale, il corpus non dice quale regime si applichi. È una lacuna rilevante, perché è l'ipotesi in cui l'area amministrativa potrebbe rientrare nell'alto rischio da una porta diversa da quella scolastica.
- **Verifica documentale: nessuna fonte spiega come.** È il caso d'uso più delicato tra i quattro elencati ed è citato in una riga, senza indicazioni su affidabilità, soglie di controllo o modalità di validazione.
- **Formazione ATA non quantificata.** Quanti dei 5.760 percorsi PNRR riguardano il personale amministrativo? Il dato manca, e con esso ogni possibilità di valutare se l'obbligo di alfabetizzazione sia coperto per questo profilo.
- **Nessun analogo scolastico di AI Officer e Data Steward.** La domanda è posta dalle fonti AgID e non trova risposta: il wiki non documenta alcuna figura tecnica dedicata ai dati nell'organico scolastico.
- **Nessuna pronuncia sul back-office.** Il parere del Garante nel corpus riguarda lo schema di decreto MIM e la didattica; non risultano indicazioni specifiche sull'uso amministrativo dell'IA nelle scuole.
- **Manca un concetto dedicato.** Il wiki non ha una pagina `concept/` sull'amministrazione scolastica aumentata: l'area è trattata solo come sottosezione di [[concept/governance-scolastica-ia|Governance scolastica dell'IA]] e [[concept/ia-pubblica-amministrazione|IA nella Pubblica Amministrazione]]. Potrebbe valere la pena crearla.
