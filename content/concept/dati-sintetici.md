---
title: "Dati sintetici"
type: concept
tags: [privacy, normativa, etica, governance-scolastica]
created: 2026-08-08
updated: 2026-08-08
sources: ["Linee Guida MIM DM 166/2025", "Parere del Garante privacy sullo schema di decreto MIM", "Legge 132/2025 (art. 8)"]
---

## Definizione
I **dati sintetici** sono dati generati artificialmente — anche mediante sistemi di IA — che riproducono le proprietà statistiche di dati reali senza riferirsi a persone identificate o identificabili. A scuola sono lo strumento raccomandato per usare l'IA senza trattare dati personali di studenti e docenti, azzerando i rischi di profilazione ([[concept/privacy-protezione-dati|Privacy e protezione dei dati]]).

## Come funziona
- Il **Garante privacy**, nel parere favorevole allo schema di decreto del MIM, pone come condizione l'uso dei dati personali di studenti e docenti **solo se strettamente indispensabili**, prediligendo altrimenti i dati sintetici.
- Sono l'attuazione operativa dei principi di **minimizzazione**, **privacy by design** e **privacy by default**: se il dato reale non è necessario alla finalità didattica o amministrativa, non va trattato.
- Compaiono tra le **misure di mitigazione tipiche** nella [[concept/dpia|DPIA — Valutazione d'Impatto sulla Protezione dei Dati]] e nel processo integrato [[concept/dpia-fria|DPIA e FRIA — valutazioni d'impatto]]: la scelta del dato sintetico riduce gravità e probabilità del rischio residuo.
- La **Legge 132/2025** (art. 8) riconosce a livello nazionale i trattamenti per anonimizzazione, pseudonimizzazione o **sintetizzazione** dei dati, introducendo esplicitamente la nozione di dati sintetici generati da IA.
- L'uso resta una scelta del **deployer** ([[concept/deployer|Deployer (utilizzatore professionale di IA)]]): è la scuola, come Titolare del trattamento, a doverla motivare e documentare.

## Applicazioni o esempi
- Esercitazioni e dimostrazioni in classe su dataset fittizi anziché sui dati reali del registro elettronico.
- Prompt costruiti su casi verosimili ma inventati, in luogo dell'inserimento di dati sensibili o identificativi (PEI, PDP) in modelli linguistici aperti — pratica vietata dalle Linee Guida.
- Progettazione e collaudo di strumenti di analisi didattica prima dell'eventuale trattamento di dati reali.
- Nella PA la stessa raccomandazione ricorre nelle indicazioni AgID sull'adozione dell'IA.

## Relazioni con altri concetti
- [[concept/privacy-protezione-dati|Privacy e protezione dei dati]] — i dati sintetici sono la misura raccomandata dal Garante per minimizzare il trattamento
- [[concept/dpia|DPIA — Valutazione d'Impatto sulla Protezione dei Dati]] — figurano tra le misure di mitigazione da documentare nella valutazione d'impatto
- [[concept/dpia-fria|DPIA e FRIA — valutazioni d'impatto]] — riducono il rischio residuo in entrambe le valutazioni
- [[concept/opt-out|Diritto di non partecipazione (opt-out)]] — alternativa strutturale: se il dato reale non serve, non si pone il problema del consenso all'addestramento
- [[concept/deployer|Deployer (utilizzatore professionale di IA)]] — la scelta e la motivazione spettano alla scuola
- [[entity/garante-privacy|Garante per la protezione dei dati personali]] — autorità che ne raccomanda l'uso

## Contraddizioni e dibattiti
Le fonti del wiki raccomandano i dati sintetici ma non ne discutono i limiti tecnici (fedeltà statistica, rischio di re-identificazione, qualità del dato). Una tensione affine è segnalata in ambito PA, dove è rilevata una **scarsa attenzione alla qualità dei dati** di addestramento, personali o sintetici che siano: il dato sintetico risolve un problema di privacy, non garantisce di per sé un dato adeguato. Resta inoltre aperta la tensione di fondo tra innovazione didattica basata sui dati e minimizzazione del trattamento di dati di minori.

## Fonti
[[source/linee-guida-mim-dm166-2025|Linee Guida MIM per l'IA a scuola (DM 166/2025)]], [[source/scuola-ok-del-garante-alle-linee-guida-del-mim-per-l-ia|Scuola: ok del Garante alle Linee guida del MIM per l'IA negli istituti (news)]], [[source/privacy-e-intelligenza-artificiale-dopo-la-nuova-legge-|Privacy e IA dopo la Legge 132/2025: il modello italiano (Federprivacy)]], [[source/l-intelligenza-artificiale-nel-sistema-istruzione-itali|REPORT — L'IA nel Sistema Istruzione Italiano: analisi delle Linee Guida MIM (DM 166/2025), quadro UE e PNRR]]
