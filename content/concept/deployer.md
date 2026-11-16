---
title: "Deployer (utilizzatore professionale di IA)"
type: concept
tags: [ai, normativa, politiche, governance-scolastica]
created: 2026-06-21
updated: 2026-08-08
sources: ["AI Act (art. 3)", "Linee Guida MIM DM 166/2025", "Linee guida AgID IA nella PA"]
---

## Definizione
Il **deployer** è, ai sensi dell'art. 3, punto 4, dell'[[source/ai-act-ue|AI Act]], il soggetto che utilizza un sistema di IA **sotto la propria autorità** nell'ambito di un'attività professionale (distinto dal *fornitore*, che lo sviluppa o immette sul mercato).

## Come funziona
Le [[source/linee-guida-mim-dm166-2025|Linee Guida MIM]] qualificano formalmente la **scuola come deployer**: non un utente privato, ma un utilizzatore professionale che si assume **piena responsabilità giuridica, tecnica ed etica** dei sistemi che adotta. Lo stesso inquadramento vale per le amministrazioni pubbliche (vedi [[concept/ia-pubblica-amministrazione|IA nella Pubblica Amministrazione]]). Da questo ruolo discendono gli obblighi di [[concept/dpia-fria|DPIA e FRIA — valutazioni d'impatto]], trasparenza e [[concept/supervisione-umana|Supervisione umana (human-in-the-loop)]].

## Applicazioni o esempi
- La scuola che adotta un tutor IA o un software valutativo agisce come deployer: deve informare gli utenti, valutare i rischi e garantire l'oversight umano.

## Relazioni con altri concetti
- [[concept/governance-scolastica-ia|Governance scolastica dell'IA]] — il ruolo di deployer è il fondamento della governance d'istituto
- [[concept/dpia-fria|DPIA e FRIA — valutazioni d'impatto]] — obblighi di valutazione in capo al deployer
- [[concept/ai-act-categorie-rischio|AI Act — categorie di rischio]] — il deployer valuta la categoria di rischio
- [[concept/supervisione-umana|Supervisione umana (human-in-the-loop)]] — responsabilità di controllo umano
- [[concept/trasparenza-algoritmica|Trasparenza algoritmica (art. 50 AI Act)]] — l'obbligo di informare gli utenti (art. 50) grava sul deployer
- [[concept/riconoscimento-emozioni|Riconoscimento delle emozioni (pratica vietata)]] — spetta al deployer verificare che gli strumenti non incorporino pratiche vietate

## Contraddizioni e dibattiti
Il peso degli obblighi del deployer (specie la FRIA) è ritenuto da alcune fonti gravoso per le scuole. Vedi [[source/linee-guida-ia-a-scuola-aspetti-normativi-e-operativi|Linee Guida IA a Scuola: Aspetti Normativi e Operativi (webinar)]].

## Fonti
[[source/ai-act-ue|AI Act — Regolamento (UE) 2024/1689]], [[source/linee-guida-mim-dm166-2025|Linee Guida MIM per l'IA a scuola (DM 166/2025)]], [[source/agid-bozza-di-linee-guida-per-l-adozione-di-ia-nella-pu|AgID — Bozza di linee guida per l'adozione di IA nella Pubblica Amministrazione (v1.0, 2025)]], [[source/ai-act-digital-omnibus-2026|AI Act e Digital Omnibus: applicazione e rinvii (agosto 2026)]], [[source/galli-ia-nella-didattica-2025|Galli — L'intelligenza artificiale nella didattica: opportunità, rischi e regole (2025)]]

## Analisi correlate
- [[analyses/2026-08-29-scegliere-strumento-ia-classe|Scegliere uno strumento di IA per la classe: i filtri che vengono prima della didattica]] — cosa comporta in concreto, in fase di adozione, essere deployer anziché utente

## Aggiornamento — 16 novembre 2026: il salto da deployer a fornitore

> **Non è una gradazione, è un cambio di regime.** Una scuola che sviluppi un proprio sistema di IA — o che ne personalizzi uno esistente *al punto da modificarne la finalità prevista*, a maggior ragione se lo mette a disposizione di altri, anche gratuitamente o nell'ambito di una rete di istituti — **assume la qualifica di fornitore**. Con essa: documentazione tecnica, sistema di gestione della qualità e dei rischi lungo l'intero ciclo di vita, governo dei dati di addestramento, valutazione di conformità, marcatura, registrazione nella banca dati europea e sorveglianza successiva all'immissione sul mercato. Sono adempimenti che presuppongono un controllo sul funzionamento del sistema che la scuola, utilizzatrice di un prodotto altrui, non ha.
>
> L'**art. 25 dell'AI Act** produce lo stesso effetto per via di destinazione: se la scuola destina un assistente generativo generico a una delle funzioni dell'Allegato III, quello strumento diventa un sistema ad alto rischio e la scuola è considerata fornitore.
>
> «La crescente disponibilità di modelli aperti e di ambienti che consentono di costruire assistenti personalizzati rende oggi tecnicamente semplice ciò che sul piano giuridico semplice non è affatto.» Prima di avviare qualsiasi iniziativa di sviluppo o personalizzazione avanzata — anche se nasce come progetto didattico o sperimentazione di un gruppo di docenti — la scuola deve valutarne preventivamente le implicazioni con il DPO e il referente per l'IA.
>
> Vedi [[source/vargiu-svr-87-26-quadro-normativo-ia-scuola|SVR 87/26 — Il quadro normativo per l'adozione dell'IA a scuola]], [[source/vargiu-svr-90-26-casi-uso-ia|SVR 90/26 — I casi d'uso dell'IA a scuola: classificarli prima di scegliere gli strumenti]] e [[concept/caso-uso-ia|Caso d'uso dell'IA (unità di classificazione del rischio)]].
>
> **Il docente che usa l'IA a titolo personale non è un deployer: lo è l'istituzione.** Se un docente immette dati di alunni in un'applicazione non autorizzata, la responsabilità «non è soltanto sua: è anche dell'istituzione che non ha governato il fenomeno, non ha adottato regole e non ha formato il personale». È la ragione per cui il [[concept/regolamento-ia-istituto|Regolamento]] non è un adempimento formale ma la misura organizzativa che circoscrive la responsabilità della scuola.
