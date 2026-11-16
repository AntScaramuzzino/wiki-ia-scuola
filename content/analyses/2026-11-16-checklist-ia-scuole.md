---
title: "IA a scuola: checklist di controllo in 55 punti"
type: analysis
tags: [governance-scolastica-ia, normativa, privacy, competenze, politiche]
created: 2026-11-16
updated: 2026-11-16
sources: [linee-guida-agid-ia-pa-2026, dlgs-179-2026, ai-act-ue, ai-act-digital-omnibus-2026, legge-132-2025, linee-guida-mim-dm166-2025]
---

## Domanda
Che cosa deve controllare una scuola statale per capire a che punto è con le regole sull'IA, e quale documento prova ogni risposta?

## Risposta sintetica
Cinquantacinque controlli in dieci aree, ciascuno con l'evidenza documentale che lo dimostra e il riferimento alla fonte. Dieci sono segnati come prioritari: ricognizione degli strumenti, classificazione del rischio, esclusione del riconoscimento delle emozioni, atto del dirigente sulle responsabilità, regole d'uso per il personale, tutela dei dati degli alunni e formazione di tutto il personale. La checklist non certifica la conformità: serve a trovare ciò che manca.

## Analisi

### Come usarla

- Ogni riga è una domanda a cui rispondere Sì, No oppure non applicabile. Un «Sì» vale solo se esiste il documento indicato nella colonna «Evidenza».
- **Tipo** dice da dove viene il controllo: **O** obbligo delle Linee guida AgID o di una norma, valido per ogni scuola statale · **C** obbligo che scatta solo se ricorre la condizione (dati personali, alto rischio, servizio cloud) · **P** prassi prudente proposta in questa analisi, non prescritta.
- **★** segna i dieci controlli da fare per primi.
- **Rif.** rimanda alle voci del <a href="/static/strumenti/obblighi-ia-pa" target="_blank" rel="noopener" data-router-ignore>repertorio interattivo degli obblighi</a> (IA-01 … IA-87) o alla norma.
- Le sezioni F e parte della D si compilano solo se il caso ricorre.
- **Nel wiki** rimanda alla pagina che documenta la fonte o il concetto.
- Per compilarla e vedere il grafico dei risultati usa l'<a href="/static/strumenti/obblighi-ia-pa#autovalutazione" target="_blank" rel="noopener" data-router-ignore>autovalutazione interattiva</a>: quattro livelli per controllo, percentuali per area, risposte salvate nel browser.

### A. Ricognizione e divieti

| N. | Controllo | Evidenza | Tipo | Rif. | Nel wiki |
|:--|:------------------------------------------|:----------------------|:--|:----------|:----------|
| 1 ★ | Esiste un elenco scritto degli strumenti con funzioni di IA usati da uffici e docenti, compresi quelli usati con account personali? | Registro dei casi d'uso | O | IA-01, IA-16 | [[concept/ai-act-categorie-rischio\|Categorie di rischio]] |
| 2 | Per ogni strumento è indicato chi lo usa, per quale scopo e con quali dati? | Registro dei casi d'uso | O | IA-16 | [[concept/ai-act-categorie-rischio\|Categorie di rischio]] |
| 3 ★ | Ogni uso ha un livello di rischio assegnato (vietato, alto, con obblighi di trasparenza, minimo)? | Registro, colonna «rischio» | O | IA-02 | [[concept/ai-act-categorie-rischio\|Categorie di rischio]] |
| 4 ★ | È escluso l'uso di sistemi che rilevano emozioni o attenzione di alunni e personale? | Verifica delle funzioni delle piattaforme; regola scritta | O | AI Act art. 5; IA-04 | [[concept/riconoscimento-emozioni\|Riconoscimento delle emozioni]] |
| 5 | Per ogni strumento è chiaro se la scuola lo usa soltanto o lo ha anche sviluppato o modificato? | Registro, colonna «ruolo» | O | IA-03 | [[concept/deployer\|Deployer]] |
| 6 | Gli usi non autorizzati emersi dalla ricognizione sono stati sospesi o regolarizzati? | Comunicazione del dirigente | P | — | [[concept/ai-act-categorie-rischio\|Categorie di rischio]] |

### B. Responsabilità e regole

| N. | Controllo | Evidenza | Tipo | Rif. | Nel wiki |
|:--|:------------------------------------------|:----------------------|:--|:----------|:----------|
| 7 ★ | Un atto del dirigente indica chi propone, chi valuta, chi autorizza e chi controlla gli usi dell'IA? | Atto organizzativo | O | IA-12 | [[concept/governance-scolastica-ia\|Governance scolastica]] |
| 8 | È individuato un referente interno per l'IA, senza attribuirgli il titolo di Responsabile per la transizione digitale? | Atto di incarico | P | IA-11 | [[concept/governance-scolastica-ia\|Governance scolastica]] |
| 9 | Il Responsabile della protezione dei dati è consultato prima di ogni nuovo uso che tocca dati personali? | Parere o verbale | C | IA-70 | [[entity/garante-privacy\|Garante privacy]] |
| 10 ★ | Esistono regole d'uso scritte per il personale: cosa si può inserire, cosa no, quando serve la verifica di una persona? | Regolamento o circolare | O | IA-06, IA-46 | [[concept/governance-scolastica-ia\|Governance scolastica]] |
| 11 | Le regole dicono che ogni atto e ogni decisione restano di una persona responsabile? | Regolamento | O | IA-06; L. 132/2025 art. 14 | [[concept/supervisione-umana\|Supervisione umana]] · [[source/legge-132-2025\|Legge 132/2025]] |
| 12 | Obiettivi e usi previsti dell'IA sono scritti in un documento della scuola? | PTOF o documento dedicato | O | IA-09 | [[concept/piano-istituto-ia\|Piano d’Istituto per l’IA]] |
| 13 | Quel documento è raccordato con PTOF, piano di formazione e programma annuale (non con il PIAO, da cui le scuole sono escluse)? | PTOF, programma annuale | C | IA-10 | [[concept/piano-istituto-ia\|Piano d’Istituto per l’IA]] |
| 14 | C'è un piano con attività, tempi, responsabili e criteri di verifica? | Piano operativo | O | IA-19 | [[concept/governance-scolastica-ia\|Governance scolastica]] |
| 15 | I progetti didattici con IA sono approvati dagli organi collegiali e inseriti nel PTOF? | Delibere; PTOF | O | Linee guida MIM, DM 166/2025 | [[source/linee-guida-mim-dm166-2025\|Linee guida MIM]] · [[concept/piano-istituto-ia\|Piano d’Istituto per l’IA]] |

### C. Prima di attivare un nuovo strumento

| N. | Controllo | Evidenza | Tipo | Rif. | Nel wiki |
|:--|:------------------------------------------|:----------------------|:--|:----------|:----------|
| 16 | È scritto perché serve, con costi e benefici attesi? | Scheda del caso d'uso | O | IA-14 | [[concept/deployer\|Deployer]] |
| 17 | Sono definiti i requisiti su dati, privacy, sicurezza e accessibilità? | Scheda del caso d'uso | O | IA-17, IA-05 | [[concept/deployer\|Deployer]] |
| 18 | I rischi sono stati valutati e la valutazione è documentata? | Scheda del caso d'uso | O | IA-23 | [[concept/ai-act-categorie-rischio\|Categorie di rischio]] |
| 19 | È fissato almeno un indicatore per giudicare se lo strumento funziona? | Scheda del caso d'uso | O | IA-18 | [[concept/deployer\|Deployer]] |
| 20 | È stata acquisita la documentazione del fornitore: istruzioni, limiti dichiarati, luogo di conservazione dei dati, subfornitori? | Fascicolo del fornitore | O | IA-28, IA-61 | [[concept/deployer\|Deployer]] |
| 21 | Il contratto vieta al fornitore di usare i dati della scuola per addestrare modelli destinati ad altri? | Contratto o atto ex art. 28 GDPR | C | IA-73 | [[concept/deployer\|Deployer]] |
| 22 | Il fornitore che tratta dati personali è nominato responsabile del trattamento? | Atto ex art. 28 GDPR | C | IA-67 | [[concept/deployer\|Deployer]] |

### D. Dati personali e alunni

| N. | Controllo | Evidenza | Tipo | Rif. | Nel wiki |
|:--|:------------------------------------------|:----------------------|:--|:----------|:----------|
| 23 | Per ogni uso con dati personali sono individuate finalità e base giuridica? | Registro dei trattamenti | C | IA-63 | [[concept/privacy-protezione-dati\|Privacy e dati]] |
| 24 | Il registro dei trattamenti è aggiornato con gli usi di IA? | Registro dei trattamenti | C | GDPR art. 30; IA-62 | [[concept/privacy-protezione-dati\|Privacy e dati]] |
| 25 | È stata verificata la necessità della valutazione d'impatto sulla protezione dei dati, e la valutazione è stata svolta quando dovuta? | DPIA, oppure nota motivata di esclusione | C | IA-68 | [[concept/dpia\|DPIA]] |
| 26 ★ | Le regole vietano di inserire in strumenti generalisti dati sanitari, PEI, PDP ed elaborati riconducibili a un alunno? | Regolamento o circolare | C | IA-64, IA-69 | [[concept/privacy-protezione-dati\|Privacy e dati]] |
| 27 ★ | Per gli alunni sotto i 14 anni si usano solo strumenti senza account personale dell'alunno, oppure è stato acquisito il consenso dei genitori? | Elenco strumenti per classe; moduli di consenso | C | L. 132/2025 art. 4, c. 4 | [[source/legge-132-2025\|Legge 132/2025]] |
| 28 | È stata verificata l'età minima prevista dalle condizioni d'uso di ogni strumento usato dagli alunni? | Scheda dello strumento | P | — | [[concept/privacy-protezione-dati\|Privacy e dati]] |
| 29 | L'informativa privacy per famiglie e personale è aggiornata con gli usi di IA? | Informativa pubblicata | C | IA-40 | [[concept/privacy-protezione-dati\|Privacy e dati]] |
| 30 | Il personale autorizzato al trattamento ha ricevuto istruzioni specifiche sull'uso dell'IA? | Atti di autorizzazione | C | IA-66 | [[concept/privacy-protezione-dati\|Privacy e dati]] |

### E. Trasparenza verso famiglie e personale

| N. | Controllo | Evidenza | Tipo | Rif. | Nel wiki |
|:--|:------------------------------------------|:----------------------|:--|:----------|:----------|
| 31 ★ | Famiglie e personale possono sapere quali strumenti di IA usa la scuola e per cosa? | Pagina del sito o circolare | O | IA-38, IA-55 | [[concept/trasparenza-algoritmica\|Trasparenza algoritmica]] |
| 32 | Chi interagisce con un assistente automatico è avvisato che si tratta di un'IA? | Avviso nell'interfaccia | C | AI Act art. 50; IA-39 | [[concept/trasparenza-algoritmica\|Trasparenza algoritmica]] |
| 33 | È indicato a chi rivolgersi per chiedere spiegazioni, contestare un esito e ottenere il riesame di una persona? | Informativa; contatto dedicato | C | IA-43 | [[concept/opt-out\|Opt-out]] |
| 34 | Le informazioni sono scritte in modo comprensibile e accessibile? | Testi pubblicati | O | IA-40 | [[concept/trasparenza-algoritmica\|Trasparenza algoritmica]] |

### F. Usi ad alto rischio (solo se presenti)

Sono ad alto rischio i sistemi che decidono ammissioni o assegnazioni, valutano gli apprendimenti, stabiliscono il percorso dell'alunno, sorvegliano le prove, selezionano o valutano il personale. Gli obblighi dell'AI Act per questi sistemi risultano applicabili dal 2 dicembre 2027; le Linee guida AgID chiedono fin da ora di riconoscerli e presidiarli.

| N. | Controllo | Evidenza | Tipo | Rif. | Nel wiki |
|:--|:------------------------------------------|:----------------------|:--|:----------|:----------|
| 35 ★ | È verificato che nessun sistema attribuisce da solo voti, giudizi, ammissioni o percorsi? | Dichiarazione nel registro | C | AI Act, All. III, p. 3 | [[concept/ai-act-categorie-rischio\|Categorie di rischio]] |
| 36 | Se un uso ad alto rischio c'è: è stata fatta la valutazione d'impatto sui diritti fondamentali prima dell'uso? | FRIA | C | IA-29, IA-30 | [[concept/fria\|FRIA]] |
| 37 | È incaricata una persona, con competenza e autorità, di interpretare gli esiti e intervenire? | Atto di incarico | C | IA-31 | [[concept/supervisione-umana\|Supervisione umana]] |
| 38 | Documenti e registrazioni sono conservati per poter ricostruire le decisioni? | Fascicolo | C | IA-32 | [[concept/ai-act-categorie-rischio\|Categorie di rischio]] |

### G. Formazione

| N. | Controllo | Evidenza | Tipo | Rif. | Nel wiki |
|:--|:------------------------------------------|:----------------------|:--|:----------|:----------|
| 39 ★ | È prevista una formazione di base sull'IA per tutto il personale, ATA compresi? | Piano di formazione | O | AI Act art. 4; IA-44 | [[concept/alfabetizzazione-ia\|Alfabetizzazione all’IA]] |
| 40 | I percorsi sono differenziati per ruolo (dirigente, DSGA, docenti, segreteria, tecnici)? | Piano di formazione | O | IA-44 | [[concept/alfabetizzazione-ia\|Alfabetizzazione all’IA]] |
| 41 | Dirigente e DSGA sono formati su rischi, impatti e conformità delle scelte? | Attestati | O | IA-48 | [[concept/alfabetizzazione-ia\|Alfabetizzazione all’IA]] |
| 42 | La formazione comprende cybersicurezza e protezione dei dati? | Programmi dei corsi | O | IA-54, IA-81 | [[concept/alfabetizzazione-ia\|Alfabetizzazione all’IA]] |
| 43 | Esiste un registro di chi ha seguito quale formazione e quando? | Registro; attestati | O | IA-45, IA-54 | [[concept/alfabetizzazione-ia\|Alfabetizzazione all’IA]] |
| 44 | Le Linee guida AgID e MIM sono state portate a conoscenza di staff e collegio? | Circolare; verbale | O | IA-50 | [[concept/alfabetizzazione-ia\|Alfabetizzazione all’IA]] |

### H. Sicurezza

| N. | Controllo | Evidenza | Tipo | Rif. | Nel wiki |
|:--|:------------------------------------------|:----------------------|:--|:----------|:----------|
| 45 | Prima dell'adozione è stata verificata la sicurezza del servizio e del fornitore? | Scheda dello strumento | O | IA-74, IA-77 | [[entity/acn\|ACN]] |
| 46 | Gli accessi avvengono con account istituzionali e permessi assegnati, non con account personali? | Elenco degli account | O | IA-78 | [[entity/acn\|ACN]] |
| 47 | C'è una procedura per segnalare e gestire un incidente (dati inseriti per errore, esito dannoso, violazione)? | Procedura scritta | O | IA-80 | [[entity/acn\|ACN]] |
| 48 | Alla dismissione di uno strumento i dati sono cancellati o restituiti? | Clausola contrattuale; verbale | O | IA-82 | [[entity/acn\|ACN]] |

### I. Verifica periodica

| N. | Controllo | Evidenza | Tipo | Rif. | Nel wiki |
|:--|:------------------------------------------|:----------------------|:--|:----------|:----------|
| 49 | Gli usi dell'IA e i loro rischi sono riesaminati a cadenza fissata, almeno una volta l'anno? | Verbale di riesame | O | IA-22, IA-25 | [[concept/governance-scolastica-ia\|Governance scolastica]] |
| 50 | Il registro è aggiornato a ogni nuovo strumento o cambio d'uso? | Registro con date | O | IA-16 | [[concept/governance-scolastica-ia\|Governance scolastica]] |
| 51 | Qualcuno segue gli aggiornamenti attesi: decreto MIM sulla formazione (entro il 21 gennaio 2027), chiarimenti sul Responsabile per la transizione digitale? | Incarico al referente | P | D.Lgs. 179/2026 art. 38 | [[source/dlgs-179-2026\|D.Lgs. 179/2026]] · [[entity/mim\|MIM]] |

### J. Novità del D.Lgs. 179/2026

| N. | Controllo | Evidenza | Tipo | Rif. | Nel wiki |
|:--|:------------------------------------------|:----------------------|:--|:----------|:----------|
| 52 | Regolamento d'istituto e Patto educativo di corresponsabilità hanno una sezione sull'uso dell'IA? | Regolamento; Patto | P | D.Lgs. 179/2026 art. 38, c. 6 | [[source/dlgs-179-2026\|D.Lgs. 179/2026]] · [[concept/governance-scolastica-ia\|Governance scolastica]] |
| 53 | È escluso che decisioni sul rapporto di lavoro, provvedimenti disciplinari e valutazioni del personale siano presi solo da un sistema automatico, ed è prevista l'informativa preventiva ai lavoratori? | Procedura; informativa | C | D.Lgs. 179/2026 art. 41 | [[source/dlgs-179-2026\|D.Lgs. 179/2026]] · [[concept/supervisione-umana\|Supervisione umana]] |
| 54 | Se sono in uso sistemi di IA che incidono sull'organizzazione del lavoro, il documento di valutazione dei rischi li considera e i lavoratori sono informati e formati? | DVR; registro della formazione | C | D.Lgs. 179/2026 art. 42 | [[source/dlgs-179-2026\|D.Lgs. 179/2026]] |
| 55 | Nella secondaria, i moduli di orientamento comprendono i percorsi STEAM e le applicazioni dell'IA? | Moduli di orientamento | O | D.Lgs. 179/2026 art. 36, c. 5 | [[source/dlgs-179-2026\|D.Lgs. 179/2026]] |

## Fonti usate
- [[source/linee-guida-agid-ia-pa-2026|Linee Guida AgID per l'adozione di IA nella PA — versione definitiva (det. 169/2026)]]
- [[source/dlgs-179-2026|D.Lgs. 179/2026 — adeguamento all'AI Act, autorità nazionali e IA nella formazione]]
- [[source/ai-act-ue|AI Act — Regolamento (UE) 2024/1689]] · [[source/ai-act-digital-omnibus-2026|AI Act e Digital Omnibus: applicazione e rinvii (agosto 2026)]]
- [[source/legge-132-2025|Legge 23 settembre 2025, n. 132]]
- [[source/linee-guida-mim-dm166-2025|Linee Guida MIM per l'IA a scuola (DM 166/2025)]]
- Ragionamento e fonti esterne: [[analyses/2026-11-16-linee-guida-agid-lette-dalla-scuola|Le Linee guida AgID sull'IA lette dalla scuola]]
- [[concept/governance-scolastica-ia|Governance scolastica dell'IA]] · [[concept/piano-istituto-ia|Piano d'Istituto per l'IA (PIA) e Atto di Indirizzo]] · [[concept/dpia|DPIA — Valutazione d'Impatto sulla Protezione dei Dati]] · [[concept/fria|FRIA — Valutazione d'Impatto sui Diritti Fondamentali]] · [[concept/alfabetizzazione-ia|Alfabetizzazione all'IA (AI Literacy)]] · [[concept/supervisione-umana|Supervisione umana (human-in-the-loop)]]

## Lacune e domande aperte
- La checklist non certifica la conformità: serve a trovare ciò che manca.
- I controlli di tipo O e C traducono in domande obblighi delle fonti; la formulazione e le evidenze indicate sono una proposta redazionale, non testo normativo. La cadenza annuale del controllo 49 è un'indicazione redazionale: le Linee guida chiedono un riesame periodico senza fissare la frequenza.
- Controllo 8: per le scuole statali una nota ministeriale del 2019 indica come Responsabile per la transizione digitale quello del Ministero. Non è stato verificato se sia ancora valida.
- Controllo 15: tratto da fonti secondarie sulle Linee guida MIM, non dal testo del decreto.
- Controllo 52: il decreto non impone alla scuola di modificare regolamento e Patto; prevede che i comitati territoriali promossi dagli Uffici scolastici regionali ne promuovano l'adeguamento.
- Controllo 27: non è chiarito se il consenso dei genitori previsto dalla L. 132/2025 valga anche per gli strumenti scelti dalla scuola. La riga propone la soluzione prudente.
- Sezione F: la data del 2 dicembre 2027 viene da fonti secondarie sul Regolamento (UE) 2026/1744.
- La checklist copre le scuole statali. Per le paritarie le Linee guida AgID non si applicano direttamente.
- Non è un parere legale: i casi dubbi vanno verificati con il Responsabile della protezione dei dati.
