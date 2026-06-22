---
title: "Il quadro normativo dell'IA nella scuola italiana: i tre livelli"
type: analysis
tags: [ai, normativa, politiche, governance, privacy, ai-società, ai-formazione]
created: 2026-06-21
updated: 2026-06-21
sources: [ai-act-ue, legge-132-2025, linee-guida-mim-dm166-2025]
---

# Il quadro normativo dell'IA nella scuola italiana: i tre livelli

## Domanda
Qual è il quadro normativo che regola l'IA nella scuola italiana e come si articolano i diversi livelli?

## Risposta sintetica
L'IA a scuola è regolata da un'architettura a tre livelli che si incastrano gerarchicamente: il **Regolamento UE 2024/1689 (AI Act)**, pienamente applicabile dal 2 agosto 2026, che classifica l'istruzione come settore ad alto rischio; la **Legge italiana 132/2025** (in vigore dal 10 ottobre 2025), che recepisce il principio antropocentrico e promuove l'AI literacy; e le **Linee Guida MIM (DM 166/2025)**, che traducono entrambe in adempimenti operativi facendo della scuola un "deployer" responsabile. Il filo conduttore dei tre livelli è la centralità decisionale dell'essere umano e una governance proceduralizzata del rischio.

## Analisi

### Gerarchia delle fonti

| Livello | Fonte | Entrata in vigore / applicabilità | Funzione |
|---------|-------|-----------------------------------|----------|
| Europeo | [[source/ai-act-ue]] — Regolamento UE 2024/1689 | In vigore 01/08/2024; pienamente applicabile **02/08/2026** (divieti già dal 02/02/2025) | Quadro giuridico generale basato sul rischio |
| Nazionale | [[source/legge-132-2025]] — Legge 23/09/2025 n. 132 | In vigore **10/10/2025** | Affianca l'AI Act; principi costituzionali e promozione educativa |
| Settoriale/scolastico | [[source/linee-guida-mim-dm166-2025]] — DM 166 del 09/08/2025 (Linee Guida v1.0, pubblicate 29/08/2025) | Cronoprogramma a.s. 2025/2026 | Traduzione operativa per le istituzioni scolastiche |

I tre livelli non sono alternativi ma cumulativi: la scuola deve rispettare contemporaneamente le prescrizioni europee, quelle nazionali e gli adempimenti ministeriali. Le Linee Guida MIM sono uno strumento **proattivo**: anticipando gli obblighi stringenti dell'AI Act, il Ministero offre alle scuole un vantaggio temporale per strutturare un'innovazione controllata prima del 2 agosto 2026.

### Livello 1 — AI Act UE (Regolamento 2024/1689)

L'AI Act è il primo quadro giuridico globale sull'IA, fondato su un approccio proporzionale al rischio (*risk-based approach*) che classifica i sistemi in quattro categorie: rischio inaccettabile (sistemi vietati), alto rischio, rischio limitato (es. chatbot, obblighi di trasparenza) e rischio minimo (es. filtri anti-spam).

**L'istruzione è classificata ad alto rischio** (Allegato III, punto 3). Il **Considerando 56** motiva questa scelta: i sistemi educativi possono determinare l'accesso all'istruzione e quindi incidere profondamente sul percorso professionale e sulla capacità di una persona di garantirsi il sostentamento; se mal progettati, sono intrusivi e possono perpetuare modelli storici di discriminazione (per età, genere, disabilità, etnia).

Sono ad alto rischio i sistemi IA usati per:
1. determinare l'accesso o l'ammissione degli studenti;
2. valutare i risultati dell'apprendimento e assegnare voti che orientano il percorso;
3. valutare il livello di istruzione adeguato a cui una persona potrà accedere;
4. monitorare e rilevare comportamenti vietati durante le prove d'esame.

L'**Articolo 5** vieta inoltre espressamente i sistemi di riconoscimento delle emozioni negli istituti di istruzione (salvo motivi medici o di sicurezza), così come *social scoring* e tecniche subliminali manipolative.

### Livello 2 — Legge italiana 132/2025

La Legge 132/2025 è la **prima normativa nazionale in Europa ad affiancare l'AI Act**. Completa il quadro europeo ponendo l'accento sul rispetto dei diritti e delle libertà costituzionali. Punti salienti per la scuola:

- **Antropocentrismo e non delegabilità (Art. 3):** ricerca e utilizzo dell'IA devono rispettare autonomia e potere decisionale umano; nessun processo automatizzato può sostituire integralmente la volontà umana ([[concept/supervisione-umana]]).
- **Promozione educativa (Art. 24):** potenziamento delle competenze **STEM** nei curricoli e inserimento di percorsi di **alfabetizzazione all'IA** ([[concept/alfabetizzazione-ia]]) per un uso consapevole e l'interpretazione critica degli output.
- **Governance nazionale:** [[entity/agid]] (Agenzia per l'Italia Digitale) e l'Agenzia per la Cybersicurezza Nazionale (ACN) sono designate autorità competenti per vigilanza e promozione.

### Livello 3 — Linee Guida MIM (DM 166/2025)

Emanate da [[entity/mim]], traducono la normativa in adempimenti pratici fondati su principi non negoziabili: centralità della persona, *human-in-the-loop*, equità/inclusione, trasparenza/spiegabilità, tutela della privacy (*by design* e *by default*).

**A. La scuola come "deployer".** L'innovazione giuridica principale è che la scuola assume formalmente la qualifica di **deployer** (utilizzatore professionale) ai sensi dell'Art. 3, punto 4, dell'AI Act: usa i sistemi sotto la propria autorità e se ne assume la piena responsabilità giuridica, tecnica ed etica ([[concept/governance-scolastica-ia]]).

**B. Valutazione del rischio — DPIA e FRIA.**
- **DPIA** (Data Protection Impact Assessment, art. 35 GDPR): obbligatoria prima di implementare qualsiasi sistema IA, in quanto la scuola è Titolare del Trattamento.
- **FRIA** (Fundamental Rights Impact Assessment): se la scuola adotta un sistema ad **alto rischio** (es. valutazione degli studenti), l'**Art. 27 dell'AI Act** impone di integrare la DPIA con una valutazione d'impatto sui diritti fondamentali (processi, categorie di persone interessate, rischi di danno, misure di mitigazione e supervisione). Vedi [[concept/privacy-protezione-dati]].

**C. Trasparenza, privacy, opt-out.** Diritto di non partecipazione (le famiglie possono rifiutare l'uso dei dati per l'addestramento, senza limitazioni all'accesso); divieto di inserire dati sensibili (es. PDP) nei prompt di modelli aperti (minimizzazione dei dati); obbligo di trasparenza ex Art. 50 AI Act (informare quando si interagisce con un'IA).

**D. Supervisione umana.** Nessuna decisione significativa può essere demandata all'algoritmo: il personale deve essere formato per supervisionare, interpretare e all'occorrenza annullare gli output.

**E. Governance d'istituto e atto di indirizzo.** Il Dirigente Scolastico è garante dell'innovazione ed emana l'**Atto di Indirizzo**, che orienta il **Piano d'Istituto per l'IA (PIA)**, integrato nel PTOF. Figure chiave: **Referente per l'IA (RIA)**, **Gruppo di Lavoro per l'IA**, e il **DPO** ([[entity/garante-privacy]] come riferimento esterno), obbligatoriamente consultato per DPIA e FRIA.

### Cronoprogramma operativo (a.s. 2025/2026)

| Fase | Periodo | Adempimenti principali |
|------|---------|------------------------|
| Definizione | Nov–Dic 2025 | Costituzione Gruppo di Lavoro IA e nomina RIA; circolari regolative; analisi *AI readiness* e revisione policy privacy |
| Pianificazione | Gen–Mar 2026 | Avvio formazione personale; elaborazione PIA e Regolamento d'uso; presentazione agli organi collegiali per integrazione nel PTOF |
| Adozione | Apr–Giu 2026 | Adozione formale dei documenti; avvio progetti pilota |
| Conformità | Entro 02/08/2026 | Piena conformità all'AI Act |

Il MIM istituisce inoltre un Servizio Digitale sulla **Piattaforma Unica** (attivo entro ottobre 2025) per condividere le Linee Guida, mappare i "Progetti IA" e fornire strumenti metodologici.

### Sintesi
Il combinato disposto di AI Act, Legge 132/2025 e Linee Guida MIM trasforma il rapporto delle scuole con la tecnologia: l'innovazione è incoraggiata ma sottoposta a una governance rigorosa, etica e proceduralizzata, dove la valutazione del rischio e la centralità decisionale umana sono presupposti non negoziabili.

## Fonti usate
[[source/ai-act-ue]], [[source/legge-132-2025]], [[source/linee-guida-mim-dm166-2025]], [[concept/governance-scolastica-ia]], [[concept/privacy-protezione-dati]], [[concept/supervisione-umana]], [[concept/alfabetizzazione-ia]], [[entity/mim]], [[entity/agid]], [[entity/garante-privacy]]

## Lacune e domande aperte
- Il corpus non dettaglia le sanzioni previste per la non conformità delle scuole agli obblighi AI Act/GDPR.
- Non è chiarito il rapporto operativo tra DPO scolastico e [[entity/garante-privacy]] nei casi ad alto rischio.
- Manca un dettaglio sui criteri tecnici per classificare in concreto un software scolastico come "ad alto rischio" (chi e come effettua la classificazione).
- Da approfondire il ruolo di AgID/ACN nella vigilanza pratica sulle istituzioni scolastiche.
