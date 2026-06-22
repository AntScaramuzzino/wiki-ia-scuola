---
title: "FRIA — Valutazione d'Impatto sui Diritti Fondamentali"
type: concept
tags: [normativa, privacy, etica, governance-scolastica, politiche]
created: 2026-06-21
updated: 2026-06-21
sources: ["AI Act (art. 27)", "Linee Guida MIM DM 166/2025", "Presentazione IA Scuola", "Valutazione d'impatto IA - AgID", "Federprivacy - IA nella PA"]
---

# FRIA — Valutazione d'Impatto sui Diritti Fondamentali

## Definizione
La **FRIA** (*Fundamental Rights Impact Assessment*) è la **valutazione d'impatto sui diritti fondamentali** prevista dall'**articolo 27 dell'[[source/ai-act-ue|AI Act]]** (Reg. UE 2024/1689). È obbligatoria, per determinati deployer, **prima di mettere in uso un sistema di IA ad alto rischio** (vedi [[concept/ai-act-categorie-rischio]]) e si affianca, integrandola, alla [[concept/dpia-fria|DPIA]] del GDPR.

Mentre la DPIA è centrata sulla **protezione dei dati personali**, la FRIA guarda all'impatto sui **diritti fondamentali in senso ampio** (dignità, non discriminazione, equità, accesso all'istruzione).

## Come funziona
**Quando scatta a scuola.** Le [[source/linee-guida-mim-dm166-2025|Linee Guida MIM]] (pag. 16) stabiliscono: «Qualora le Istituzioni scolastiche intendano mettere in uso un Sistema di IA ad alto rischio ai sensi dell'articolo 6 dell'AI Act, sono tenute a integrare la DPIA con la valutazione d'impatto sui diritti fondamentali (FRIA)». In ambito educativo sono **ad alto rischio** (Capo II / Allegato III) i sistemi che: determinano accesso/ammissione, **valutano i risultati dell'apprendimento**, valutano il livello di istruzione, o monitorano comportamenti vietati durante le prove.

**Contenuti minimi** (art. 27 AI Act; Linee Guida MIM pag. 17):
- i **rischi specifici di danno** per le categorie o i gruppi di persone interessati;
- la descrizione dell'attuazione delle **misure di sorveglianza umana** ([[concept/supervisione-umana]]), secondo le istruzioni per l'uso;
- le **misure da adottare** qualora i rischi si concretizzino, comprese **governance interna** e **meccanismi di reclamo**.

**Metodo.** Per ogni rischio si effettua una valutazione qualitativa per **gravità** (scala, portata, reversibilità) e **probabilità** di accadimento, in linea con la metodologia **HUDERIA** del Consiglio d'Europa (Linee Guida pag. 23). Il **DPO** è coinvolto; AgID raccomanda di integrare DPIA e FRIA in un **unico processo strutturato** con ufficio legale ed esperti tecnici.

## Applicazioni o esempi
- Adozione di un software che assegna voti o assiste la valutazione → alto rischio → DPIA **+** FRIA obbligatoria.
- Nella PA vale lo stesso schema: i deployer pubblici svolgono la FRIA nei casi previsti e la matrice AgID (AIIA) la operazionalizza (vedi [[concept/ia-pubblica-amministrazione]]).
- Software guidati (es. quelli citati da AgID/Federprivacy) accompagnano passo-passo la compilazione di DPIA/FRIA.

## Relazioni con altri concetti
- [[concept/dpia-fria]] — quadro d'insieme delle due valutazioni; la FRIA **integra** la DPIA
- [[concept/ai-act-categorie-rischio]] — la FRIA è attivata dalla categoria "alto rischio"
- [[concept/privacy-protezione-dati]] — la DPIA (art. 35 GDPR) è il presupposto
- [[concept/supervisione-umana]] — le misure di oversight sono contenuto obbligatorio della FRIA
- [[concept/deployer]] — l'obbligo grava sul deployer (la scuola)
- [[concept/governance-scolastica-ia]] — la FRIA è uno snodo della governance d'istituto
- [[concept/valutazione-integrita-accademica]] — i sistemi di valutazione sono il caso d'uso tipico

## Contraddizioni e dibattiti
- **Difficile attuabilità per le scuole**: più fonti ([[source/linee-guida-ia-a-scuola-aspetti-normativi-e-operativi]]) sostengono che la scuola-deployer non dispone delle informazioni interne dei fornitori (Google, Microsoft) necessarie a una FRIA "a regola d'arte".
- **Adempimento vs processo conoscitivo**: alcune fonti ([[source/l-intelligenza-artificiale-nella-pubblica-amministrazio]]) insistono che FRIA e DPIA non sono meri adempimenti, ma processi che migliorano equità e fiducia — a patto di competenze e strumenti adeguati.

## Fonti
[[source/ai-act-ue]], [[source/linee-guida-mim-dm166-2025]], [[source/presentazione-ia-scuola]], [[source/valutazione-d-impatto-dell-intelligenza-artificiale-agi]], [[source/l-intelligenza-artificiale-nella-pubblica-amministrazio]], [[source/linee-guida-ia-a-scuola-aspetti-normativi-e-operativi]]
