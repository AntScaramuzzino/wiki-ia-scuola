---
title: "Riconoscimento delle emozioni (pratica vietata)"
type: concept
tags: [normativa, etica, privacy, governance-scolastica, ai-società]
created: 2026-08-08
updated: 2026-08-08
sources: ["AI Act (art. 5)", "Linee Guida MIM DM 166/2025", "Parere del Garante privacy", "Digital Omnibus 2026"]
---

## Definizione
Il **riconoscimento delle emozioni** è l'inferenza automatica di stati emotivi delle persone a partire da dati biometrici o comportamentali. Negli **istituti di istruzione** è una **pratica vietata** dall'**art. 5 dell'[[source/ai-act-ue|AI Act]]**, cioè ricade nella categoria del **rischio inaccettabile**, salvo motivi medici o di sicurezza. Il divieto è applicabile dal **2 febbraio 2025**.

## Come funziona
- **Divieto, non obbligo attenuabile**: a differenza dell'alto rischio, che si governa con adempimenti ([[concept/dpia-fria|DPIA e FRIA — valutazioni d'impatto]], [[concept/supervisione-umana|Supervisione umana (human-in-the-loop)]]), il rischio inaccettabile non è mitigabile — il sistema semplicemente non può essere messo in uso.
- **Perimetro**: l'art. 5 vieta, insieme al riconoscimento delle emozioni a scuola e sul lavoro, il *social scoring*, le tecniche subliminali manipolative, lo sfruttamento delle vulnerabilità e altre pratiche biometriche; l'Appendice 1 della matrice AgID ne traspone l'elenco per la PA.
- **Recepimento nazionale**: le [[source/linee-guida-mim-dm166-2025|Linee Guida MIM]] vietano espressamente i sistemi di *sentiment analysis* / riconoscimento delle emozioni a scuola; il **Garante privacy**, nel parere sullo schema di decreto, ne ha ribadito il **divieto assoluto**.
- **Calendario**: il *Digital Omnibus* (accordo del 7 maggio 2026) ha rinviato al 2 dicembre 2027 gli obblighi sull'alto rischio dell'Allegato III, ma **non tocca i divieti**, in vigore dal 2 febbraio 2025 e pienamente efficaci.
- **Chi risponde**: l'onere di verifica ricade sulla scuola come [[concept/deployer|Deployer (utilizzatore professionale di IA)]], che deve censire gli strumenti adottati e accertare che non incorporino funzioni vietate.

## Applicazioni o esempi
- Software che rileva attenzione, noia o frustrazione degli studenti da webcam durante la lezione o una prova: vietato.
- Funzioni di *sentiment analysis* incorporate in piattaforme didattiche o di proctoring: da censire ed escludere in fase di adozione.
- Eccezioni ammesse solo per motivi **medici o di sicurezza**, quindi fuori dalla finalità didattica ordinaria.

## Relazioni con altri concetti
- [[concept/ai-act-categorie-rischio|AI Act — categorie di rischio]] — è l'esempio scolastico tipico del rischio inaccettabile
- [[concept/privacy-protezione-dati|Privacy e protezione dei dati]] — il divieto è un presidio contro la profilazione dei minori
- [[concept/deployer|Deployer (utilizzatore professionale di IA)]] — spetta alla scuola verificare l'assenza di funzioni vietate negli strumenti adottati
- [[concept/governance-scolastica-ia|Governance scolastica dell'IA]] — il censimento degli strumenti e il regolamento d'uso rendono operativo il divieto
- [[concept/dati-sintetici|Dati sintetici]] — misura coerente con la logica di non profilare gli studenti
- [[entity/garante-privacy|Garante per la protezione dei dati personali]] — ha ribadito il divieto assoluto nel parere sulle Linee Guida

## Contraddizioni e dibattiti
Una fonte del wiki solleva un nodo di confine non risolto: **come si concilia il divieto di riconoscimento delle emozioni con strumenti di *learning analytics* che inferiscono stati attentivi** ([[source/ia-school|IA@School — Quadro normativo e strategico (EFT Calabria)]])? Il perimetro tra analisi dell'apprendimento e inferenza emotiva non è tracciato in modo operativo dalle fonti disponibili, e resta il rischio che funzioni vietate arrivino in classe incorporate in prodotti commerciali senza che la scuola le riconosca come tali.

## Fonti
[[source/ai-act-ue|AI Act — Regolamento (UE) 2024/1689]], [[source/linee-guida-mim-dm166-2025|Linee Guida MIM per l'IA a scuola (DM 166/2025)]], [[source/ai-act-digital-omnibus-2026|AI Act e Digital Omnibus: applicazione e rinvii (agosto 2026)]], [[source/scuola-ok-del-garante-alle-linee-guida-del-mim-per-l-ia|Scuola: ok del Garante alle Linee guida del MIM per l'IA negli istituti (news)]], [[source/valutazione-d-impatto-dell-intelligenza-artificiale-agi|AgID — Valutazione d'impatto dell'Intelligenza Artificiale (AIIA), v1.0 2025]], [[source/ia-school|IA@School — Quadro normativo e strategico (EFT Calabria)]]
