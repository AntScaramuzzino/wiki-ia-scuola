---
title: "Privacy e protezione dei dati"
type: concept
tags: [ai, privacy, normativa, etica, educazione, ai-società, politiche]
created: 2026-06-21
updated: 2026-09-14
sources: [Legge 132/2025, Regolamento UE 2024/1689 (AI Act), Linee Guida MIM (DM 166/2025), Manifesto + Codice Etico IA Generativa a Scuola (ISIS Europa)]
---

## Definizione
Insieme dei principi e degli adempimenti che la scuola deve rispettare nel trattamento dei dati personali connessi all'uso dell'IA, disciplinati dal GDPR e dall'AI Act. La protezione è una priorità assoluta perché i dati riguardano in maggioranza minori. I sistemi devono essere progettati secondo **privacy by design** e **privacy by default**, limitando la raccolta dei dati allo stretto necessario (minimizzazione).

## Come funziona
- **DPIA (Data Protection Impact Assessment)**: prima di implementare qualsiasi sistema IA, la scuola — in qualità di Titolare del Trattamento — è obbligata a eseguire una Valutazione d'Impatto sulla Protezione dei Dati ai sensi dell'art. 35 del GDPR.
- **FRIA (Fundamental Rights Impact Assessment)**: se la scuola adotta un sistema ad alto rischio (es. valutazione degli studenti), l'Art. 27 dell'AI Act impone di integrare la DPIA con una Valutazione d'Impatto sui Diritti Fondamentali, che descrive processi, categorie di persone interessate, rischi di danno e misure di mitigazione e supervisione.
- **Diritto di non partecipazione (opt-out)**: studenti e famiglie possono scegliere di non far utilizzare i propri dati per l'addestramento dei sistemi di IA, senza discriminazione o limitazione nell'accesso all'istruzione.
- **Divieto di dati sensibili nei prompt**: è vietato/fortemente sconsigliato inserire dati personali, sensibili o identificativi (come PEI e PDP) nei prompt forniti a modelli linguistici aperti.

## Applicazioni o esempi
- Uso di **dati sintetici** al posto di dati reali laddove non strettamente indispensabili, per azzerare i rischi di profilazione (raccomandazione del Garante).
- Revisione delle policy privacy e adozione di regolamenti d'uso che vietino l'inserimento di dati sensibili nei prompt.
- Consultazione obbligatoria del DPO per la stesura di DPIA e FRIA.

## Relazioni con altri concetti
- [[concept/governance-scolastica-ia|Governance scolastica dell'IA]] — DPIA, FRIA e ruolo del DPO sono parte della governance d'istituto.
- [[concept/dpia|DPIA — Valutazione d'Impatto sulla Protezione dei Dati]] — la valutazione d'impatto sulla protezione dati (art. 35 GDPR) in dettaglio.
- [[concept/dpia-fria|DPIA e FRIA — valutazioni d'impatto]] — il quadro che lega DPIA e [[concept/fria|FRIA — Valutazione d'Impatto sui Diritti Fondamentali]].
- [[concept/dati-sintetici|Dati sintetici]] — la misura raccomandata dal Garante per minimizzare il trattamento di dati reali.
- [[concept/opt-out|Diritto di non partecipazione (opt-out)]] — il diritto di non partecipazione all'uso dei dati per l'addestramento.
- [[concept/riconoscimento-emozioni|Riconoscimento delle emozioni (pratica vietata)]] — pratica vietata a scuola, presidio contro la profilazione dei minori.
- [[concept/trasparenza-algoritmica|Trasparenza algoritmica (art. 50 AI Act)]] — obbligo di informare gli utenti dell'interazione con un sistema di IA.
- [[concept/supervisione-umana|Supervisione umana (human-in-the-loop)]] — antropocentrismo e trasparenza sono principi condivisi.
- [[concept/didattica-inclusiva-ia|Didattica inclusiva con IA]] — i dati di PEI/PDP non possono essere inseriti nei prompt.
- [[concept/bias-algoritmico|Bias Algoritmico]] — la profilazione mal gestita può alimentare discriminazioni.
- [[entity/garante-privacy|Garante per la protezione dei dati personali]] — autorità che ha espresso parere sullo schema di decreto MIM.

## Contraddizioni e dibattiti
Il **parere del Garante Privacy** è stato favorevole allo schema di decreto del MIM, ma con condizioni rigorose: prediligere i dati sintetici ai dati reali quando possibile e ribadire il divieto assoluto di pratiche come il riconoscimento delle emozioni. La tensione di fondo è tra l'innovazione didattica basata sui dati e la minimizzazione del trattamento di dati di minori.

## Fonti
[[source/legge-132-2025|Legge 23 settembre 2025, n. 132]], [[source/ai-act-ue|AI Act — Regolamento (UE) 2024/1689]], [[source/linee-guida-mim-dm166-2025|Linee Guida MIM per l'IA a scuola (DM 166/2025)]], [[source/manifesto-codice-etico-isis-europa|Manifesto e Codice Etico IA Generativa a Scuola (ISIS Europa)]], [[source/galli-ia-nella-didattica-2025|Galli — L'intelligenza artificiale nella didattica: opportunità, rischi e regole (2025)]]

## Aggiornamento — settembre 2026

> Il presidio sui dati scolastici può essere fissato **nel contratto di fornitura**, non solo nella norma. Il 9 settembre 2026 i sindacati dei docenti statunitensi (AFT, UFT) e Microsoft hanno sottoscritto un *National AI Safety & Privacy Standard* contrattualmente vincolante: divieto di usare dati di studenti e personale per addestrare modelli o per finalità pubblicitarie, divieto di tracciamento degli studenti tramite IA, obbligo di intervento umano su ogni decisione che riguardi uno studente, controllo della scuola su uso, conservazione e cancellazione. In vigore dal 1° novembre 2026, adottabile senza rinegoziare i contratti esistenti. Cfr. [[news/2026-09-14|14 settembre 2026]].

## Aggiornamento — 16 novembre 2026: le basi giuridiche nella scuola che adotta l'IA

> **Il consenso non è la base giuridica.** Quando è l'istituzione scolastica a impiegare uno strumento di IA nell'esercizio della propria funzione, la base è l'**esecuzione di un compito di interesse pubblico** — art. 6, par. 1, lett. e) GDPR in combinato con l'**art. 2-*ter*** del Codice — come già per il registro elettronico o per la piattaforma Google/Microsoft dell'istituto. Raccoglierlo dove non occorre produce conseguenze concrete: un consenso è revocabile, e la famiglia che lo revoca «si attende legittimamente che il proprio figlio sia escluso dall'attività»; la scuola dovrebbe allora garantire un percorso alternativo per un'attività didattica ordinaria, o disattendere l'aspettativa che ha creato.
>
> **La questione dei minori di quattordici anni.** L'art. 4, c. 4 della [[source/legge-132-2025|legge 132/2025]] subordina al consenso genitoriale l'accesso dei minori di quattordici anni alle tecnologie di IA. Una lettura argomentata — non ancora confermata da orientamenti del Garante o di AgID — sostiene che la norma riproduce l'impianto dell'art. 8 GDPR e dell'art. 2-*quinquies* del Codice e **presuppone un trattamento fondato sul consenso**: il minore che accede per proprio conto, con un proprio account, a un servizio offerto direttamente a lui. Non introduce una base giuridica nuova né deroga al sistema del Regolamento. Subordinare al consenso un'attività curricolare «significherebbe renderla facoltativa, ammettere che una parte della classe ne resti esclusa e introdurre una disparità di trattamento fra alunni». Diverso il caso delle attività **facoltative ed extracurricolari**, dove la richiesta di consenso può essere appropriata «proprio perché il rifiuto non priva l'alunno di nulla che gli sia dovuto». Trattandosi di disposizione recente, si raccomanda di dare conto della scelta e delle sue ragioni nel [[concept/piano-istituto-ia|Piano]] ([[source/vargiu-svr-87-26-quadro-normativo-ia-scuola|SVR 87/26 — Il quadro normativo per l'adozione dell'IA a scuola]]).
>
> **Un limite distinto da quello della base giuridica**: le condizioni contrattuali dei fornitori pongono limiti propri all'attivazione delle funzionalità di IA sugli account degli studenti. È vincolo contrattuale, non questione di consenso, e spetta all'amministratore della piattaforma verificarlo.
>
> **Assenza di dati personali ≠ assenza di trattamento.** Anche quando nulla di personale entra nei contenuti, l'accesso avviene con credenziali istituzionali e il fornitore registra identità dell'utente, orari e log: il registro dei trattamenti va comunque aggiornato ([[source/vargiu-svr-90-26-casi-uso-ia|SVR 90/26 — I casi d'uso dell'IA a scuola: classificarli prima di scegliere gli strumenti]]).
>
> **Dove l'elaborazione avviene davvero.** Per alcune funzioni generative i contenuti possono essere elaborati **fuori dallo Spazio economico europeo**, anche quando la piattaforma garantisce la localizzazione europea per le funzioni ordinarie. Entrambi i grandi fornitori offrono impostazioni che vincolano l'elaborazione a un'area determinata, ma **non sono attive per impostazione predefinita**: è «l'accertamento tecnicamente più delicato» e va compiuto prima dell'impiego ([[source/vargiu-svr-91-26-strumenti-ia-garanzie|SVR 91/26 — Adottare gli strumenti di IA: quali, come, con quali garanzie]]).
>
> **Il caso insidioso: rischio minimo con dati personali.** Un docente che fa riscrivere a un assistente la relazione finale di un alunno con disabilità impiega un sistema a rischio minimo secondo l'AI Act — la riscrittura non rientra nell'Allegato III — e può al tempo stesso compiere un trattamento illecito di **categorie particolari** (art. 9 GDPR, art. 2-*sexies* del Codice). È la ragione per cui i regolamenti d'istituto formulano il divieto in termini di *dati personali* e non di livello di rischio del sistema ([[source/vargiu-svr-92-26-piano-istituto-ia|SVR 92/26 — Il Piano d'Istituto per l'intelligenza artificiale]]).
