---
title: "Diritto di non partecipazione (opt-out)"
type: concept
tags: [privacy, normativa, etica, governance-scolastica, politiche]
created: 2026-08-08
updated: 2026-08-08
sources: ["Linee Guida MIM DM 166/2025", "Presentazione IA Scuola", "Parere del Garante privacy"]
---

## Definizione
Il **diritto di non partecipazione (opt-out)** è la facoltà riconosciuta a studenti e famiglie di **rifiutare che i propri dati siano utilizzati per l'addestramento dei sistemi di IA**, senza subire discriminazioni né limitazioni nell'accesso all'istruzione. È uno dei principi non negoziabili delle [[source/linee-guida-mim-dm166-2025|Linee Guida MIM]], accanto a privacy by design e by default.

## Come funziona
- **Oggetto circoscritto**: l'opt-out riguarda l'uso dei dati per l'**addestramento** dei sistemi, non l'accesso al servizio educativo. Il rifiuto non può tradursi in esclusione dalle attività didattiche o in un trattamento deteriore.
- **Chi lo garantisce**: la scuola, in qualità di Titolare del trattamento e di [[concept/deployer|Deployer (utilizzatore professionale di IA)]], deve rendere la scelta effettivamente esercitabile — informativa chiara, modalità di raccolta della volontà, tracciamento della decisione.
- **Dove si formalizza**: nelle policy privacy riviste, nel Regolamento d'uso e nel Piano d'Istituto per l'IA, cioè negli strumenti della [[concept/governance-scolastica-ia|Governance scolastica dell'IA]].
- **Come si documenta**: la scelta e le misure che la rendono operativa rientrano tra gli elementi da considerare nella [[concept/dpia|DPIA — Valutazione d'Impatto sulla Protezione dei Dati]] e, per i sistemi ad alto rischio, nella [[concept/fria|FRIA — Valutazione d'Impatto sui Diritti Fondamentali]], che deve descrivere anche i **meccanismi di reclamo**.
- **Minori**: si combina con le tutele specifiche per gli infratredicenni (*age gate* e consenso di chi esercita la responsabilità genitoriale) raccomandate dal Garante.

## Applicazioni o esempi
- Modulo di informativa e raccolta della volontà delle famiglie all'avvio di un progetto IA d'istituto.
- Configurazione degli strumenti adottati in modo che i dati degli studenti non alimentino l'addestramento dei modelli del fornitore.
- Ricorso ai [[concept/dati-sintetici|Dati sintetici]] come alternativa strutturale: se non si trattano dati reali, il nodo dell'addestramento non si pone.
- Percorso alternativo equivalente per lo studente che non partecipa a un'attività basata su IA, senza penalizzazione.

## Relazioni con altri concetti
- [[concept/privacy-protezione-dati|Privacy e protezione dei dati]] — l'opt-out è uno dei diritti fondanti del quadro privacy scolastico
- [[concept/dati-sintetici|Dati sintetici]] — misura che rende meno critico il tema del consenso all'addestramento
- [[concept/governance-scolastica-ia|Governance scolastica dell'IA]] — si formalizza in policy, regolamento d'uso e PIA
- [[concept/dpia|DPIA — Valutazione d'Impatto sulla Protezione dei Dati]] — la gestione dell'opt-out è parte delle misure da documentare
- [[concept/trasparenza-algoritmica|Trasparenza algoritmica (art. 50 AI Act)]] — senza informazione preventiva non c'è scelta consapevole
- [[entity/garante-privacy|Garante per la protezione dei dati personali]] — ne ha ribadito la portata nel parere sullo schema di decreto MIM

## Contraddizioni e dibattiti
Tensione documentata nel wiki: le analisi critiche delle Linee Guida MIM segnalano che **la gestione dei dati e dell'opt-out è affermata come principio ma priva di indicazioni operative chiare**, e propongono l'elaborazione di protocolli espliciti per consenso e opt-out. Resta quindi un divario tra il diritto enunciato e gli strumenti concreti per esercitarlo. Un secondo nodo, non risolto dalle fonti, è pratico: garantire l'assenza di discriminazione richiede che l'attività didattica resti pienamente fruibile anche a chi si sottrae.

## Fonti
[[source/linee-guida-mim-dm166-2025|Linee Guida MIM per l'IA a scuola (DM 166/2025)]], [[source/presentazione-ia-scuola|Presentazione IA Scuola — privacy, DPIA e FRIA]], [[source/analisi-delle-linee-guida-mim-sull-ia-nella-scuola|Analisi critica delle Linee Guida MIM sull'IA nella scuola (Gianfranco Bordoni — prospettiva USR Lombardia)]], [[source/scuola-ok-del-garante-alle-linee-guida-del-mim-per-l-ia|Scuola: ok del Garante alle Linee guida del MIM per l'IA negli istituti (news)]]
