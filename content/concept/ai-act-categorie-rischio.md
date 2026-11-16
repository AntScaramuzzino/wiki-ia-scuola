---
title: "AI Act — categorie di rischio"
type: concept
tags: [ai, politiche, normativa, etica]
created: 2026-06-21
updated: 2026-11-16
sources: ["AI Act (Reg. UE 2024/1689)", "Valutazione d'impatto IA - AgID", "Linee Guida MIM DM 166/2025"]
---

## Definizione
L'[[source/ai-act-ue|AI Act]] adotta un **approccio basato sul rischio** (*risk-based approach*) che classifica i sistemi di IA in quattro categorie, a cui corrispondono obblighi proporzionati.

## Come funziona
- **Rischio inaccettabile** — pratiche vietate (divieti applicabili dal 2 febbraio 2025): social scoring, tecniche subliminali manipolative e, in ambito scolastico, il **riconoscimento delle emozioni** (salvo motivi medici/sicurezza).
- **Alto rischio** — impatto significativo su salute, sicurezza e diritti fondamentali; obblighi rigorosi. L'**istruzione** è esplicitamente alto rischio (Allegato III, p. 3; Considerando 56): accesso/ammissione, valutazione degli apprendimenti, livello di istruzione, monitoraggio degli esami.
- **Rischio limitato** — es. chatbot; principalmente obblighi di trasparenza.
- **Rischio minimo o nullo** — es. filtri anti-spam; nessuna regolamentazione specifica.

## Applicazioni o esempi
- A scuola, i software che **valutano gli studenti** ricadono nell'alto rischio → richiedono [[concept/dpia-fria|DPIA e FRIA — valutazioni d'impatto]] e [[concept/supervisione-umana|Supervisione umana (human-in-the-loop)]] tassativa (vedi [[concept/valutazione-integrita-accademica|Valutazione e integrità accademica]]).
- La matrice AgID di valutazione d'impatto opera la stessa classificazione per la PA (vedi [[concept/ia-pubblica-amministrazione|IA nella Pubblica Amministrazione]]).

## Relazioni con altri concetti
- [[concept/governance-scolastica-ia|Governance scolastica dell'IA]] — la categoria di rischio determina gli adempimenti
- [[concept/dpia-fria|DPIA e FRIA — valutazioni d'impatto]] — l'alto rischio attiva la FRIA
- [[concept/fria|FRIA — Valutazione d'Impatto sui Diritti Fondamentali]] — la valutazione d'impatto sui diritti fondamentali in dettaglio
- [[concept/deployer|Deployer (utilizzatore professionale di IA)]] — chi usa il sistema ne valuta il rischio
- [[concept/bias-algoritmico|Bias Algoritmico]] — motivazione della classificazione ad alto rischio dell'istruzione
- [[concept/riconoscimento-emozioni|Riconoscimento delle emozioni (pratica vietata)]] — l'esempio scolastico tipico di rischio inaccettabile
- [[concept/trasparenza-algoritmica|Trasparenza algoritmica (art. 50 AI Act)]] — regime tipico del rischio limitato, operativo dal 2 agosto 2026

## Contraddizioni e dibattiti
Alcune fonti rilevano che gli obblighi per i sistemi ad alto rischio (specie la FRIA) sono di difficile attuazione pratica per le scuole. Vedi [[source/linee-guida-ia-a-scuola-aspetti-normativi-e-operativi|Linee Guida IA a Scuola: Aspetti Normativi e Operativi (webinar)]].

## Aggiornamento — Digital Omnibus (agosto 2026)

> **Claim aggiornato.** Con il *Digital Omnibus* (accordo del 7 maggio 2026) gli obblighi del Titolo III per i sistemi ad **alto rischio dell'Allegato III** — inclusi quelli scolastici (ammissioni, valutazione degli apprendimenti, livello di istruzione) — **non decorrono più dal 2 agosto 2026 ma dal 2 dicembre 2027** (2 agosto 2028 per l'IA nei prodotti regolamentati).
> Dal **2 agosto 2026** sono comunque operativi: autorità di vigilanza, obblighi di **trasparenza** (art. 50), poteri sanzionatori della Commissione, **divieti** (incl. riconoscimento emozioni a scuola) e obbligo di **alfabetizzazione all'IA** (dal 2 febbraio 2025).
> Fonte: rassegna dell'[[news/2026-08-08|8 agosto 2026]].

## Aggiornamento — novembre 2026

> Il calendario è confermato dalla lettura dell'art. 1 del Regolamento (UE) 2026/1744: alto rischio dell'Allegato III dal **2 dicembre 2027**, Allegato I dal 2 agosto 2028, due nuovi divieti dal **2 dicembre 2026**. Per i sistemi ad alto rischio già in uso presso autorità pubbliche resta il 2 agosto 2030 (art. 111, par. 2, sostituito). Le [[source/linee-guida-agid-ia-pa-2026|Linee Guida AgID per l'adozione di IA nella PA — versione definitiva (det. 169/2026)]] chiedono comunque alle PA di classificare ogni sistema e di gestirne i rischi fin da ora (§ 3.3). Vedi [[source/ai-act-digital-omnibus-2026|AI Act e Digital Omnibus: applicazione e rinvii (agosto 2026)]].

## Fonti
[[source/ai-act-ue|AI Act — Regolamento (UE) 2024/1689]], [[source/valutazione-d-impatto-dell-intelligenza-artificiale-agi|AgID — Valutazione d'impatto dell'Intelligenza Artificiale (AIIA), v1.0 2025]], [[source/linee-guida-mim-dm166-2025|Linee Guida MIM per l'IA a scuola (DM 166/2025)]], [[source/ai-act-digital-omnibus-2026|AI Act e Digital Omnibus: applicazione e rinvii (agosto 2026)]]

## Aggiornamento — 16 novembre 2026: la deroga dell'art. 6, par. 3

> **Comparire nell'Allegato III non basta.** L'art. 6, par. 3 esclude dalla classificazione ad alto rischio i sistemi il cui apporto alla decisione resta marginale, in quattro figure alternative: il sistema svolge un **compito procedurale limitato**; **migliora il risultato** di un'attività umana già completata; **rileva scostamenti** da schemi decisionali precedenti senza sostituire la valutazione umana; svolge un **compito meramente preparatorio**.
>
> Due condizioni valgono in ogni caso: la deroga **non opera mai in presenza di profilazione** di persone fisiche, e chi la invoca deve **documentare per iscritto** la valutazione compiuta. «È una via stretta: la correzione meccanica di quiz a risposta chiusa vi rientra plausibilmente, la valutazione di un elaborato argomentativo no.»
>
> **Allegato III, punto 3** (istruzione e formazione professionale), per esteso: determinare l'accesso, l'ammissione o l'assegnazione di persone a istituti di istruzione; **valutare i risultati dell'apprendimento, anche quando siano utilizzati per orientare il processo di apprendimento**; valutare il livello di istruzione appropriato; monitorare e rilevare comportamenti vietati durante le prove. Sono «proprio le funzioni presenti nelle proposte commerciali fatte spesso alle scuole»: correzione automatizzata, piattaforme adattive, proctoring.
>
> **I due nuovi divieti del 2 dicembre 2026** riguardano i sistemi che generano o manipolano materiale intimo non consensuale raffigurante persone riconoscibili (*nudification*) e quelli che generano materiale di abuso sessuale su minori. Per la scuola il riflesso non è sull'adozione ma sull'**e-safety policy** e sul Regolamento: è un fenomeno che si manifesta fra studenti, e la sua qualificazione come pratica vietata dal diritto dell'Unione — oltre che come illecito penale — va portata a conoscenza di alunni e famiglie. Vedi [[concept/deepfake|Deepfake]].
>
> Vedi [[source/vargiu-svr-90-26-casi-uso-ia|SVR 90/26 — I casi d'uso dell'IA a scuola: classificarli prima di scegliere gli strumenti]], [[source/vargiu-svr-87-26-quadro-normativo-ia-scuola|SVR 87/26 — Il quadro normativo per l'adozione dell'IA a scuola]] e [[concept/caso-uso-ia|Caso d'uso dell'IA (unità di classificazione del rischio)]].
