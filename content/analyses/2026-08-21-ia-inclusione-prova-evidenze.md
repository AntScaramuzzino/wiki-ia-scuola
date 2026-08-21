---
title: "IA e inclusione: la promessa più ripetuta e la meno documentata"
type: analysis
tags: [inclusione, pedagogia, educazione, privacy, ai-formazione]
created: 2026-08-21
updated: 2026-08-21
sources: ["Linee Guida MIM DM 166/2025", "Fiorucci & Bevilacqua scoping review 2024", "OECD Digital Education Outlook 2026", "Guida pratica IA scuola secondaria", "Atto di indirizzo per l'adozione dell'IA (modulistica)", "AI Act", "Parere del Garante privacy"]
---

## Domanda
L'inclusione è l'obiettivo che tutte le fonti di policy mettono in cima quando parlano di IA a scuola: quanto di quella promessa è oggi sostenuta da evidenze e praticabile dentro i vincoli giuridici?

## Risposta sintetica
Nel corpus del wiki l'inclusione è **l'uso dell'IA più promesso e meno documentato**. I documenti di indirizzo la collocano al primo posto tra le finalità didattiche; la ricerca pedagogica italiana registra proprio su questo terreno "notevoli ritardi"; l'unica evidenza di efficacia disponibile (OCSE 2026) è condizionale, non incoraggiante. Soprattutto: i tre vincoli operativi più stringenti — divieto di inserire PEI e PDP nei prompt, divieto di riconoscimento delle emozioni, classificazione ad alto rischio della profilazione — colpiscono esattamente gli usi più "personalizzanti". Ciò che resta immediatamente praticabile è una fascia più modesta ma reale: **trasformare i materiali, non analizzare gli studenti**.

## Analisi

### 1. Cosa promettono i documenti di indirizzo
L'inclusione non è un tema laterale delle policy italiane: è la prima voce operativa dopo la personalizzazione. Le [[source/linee-guida-mim-dm166-2025|Linee Guida MIM (DM 166/2025)]] indicano l'adattamento dei materiali per BES e DSA e il supporto a PEI e PDP tra gli usi tipici del docente "co-pilota"; l'[[source/1-atto-di-indirizzo-per-l-adozione-dell-intelligenza-ar|Atto di indirizzo]] che le scuole stanno adottando elenca, nell'ambito didattico-formativo, "recupero/inclusione BES con tecnologie assistive" e "analisi predittive contro la dispersione"; il [[source/adempimenti-e-cronoprogramma|cronoprogramma d'istituto]] ripete la coppia inclusione-dispersione tra gli obiettivi didattici.

Il contenuto pedagogico di questa promessa è l'[[concept/udl|Universal Design for Learning]]: l'IA renderebbe finalmente sostenibile l'accessibilità *fin dall'origine* — più rappresentazioni dello stesso contenuto, più canali, meno adattamento a posteriori — attraverso tre famiglie di supporti descritte in [[concept/didattica-inclusiva-ia|didattica inclusiva con IA]]: rappresentazioni multimodali, strumenti di accessibilità (sintesi vocale, trascrizione, semplificazione testuale) e calibrazione sulle fragilità individuali.

Il punto da tenere presente è che questa è una **indicazione di policy**, non un risultato misurato. Il wiki non contiene, a oggi, alcun dato d'impatto italiano sull'inclusione mediata dall'IA.

### 2. Cosa dice la ricerca: l'area più promessa è quella più scoperta
Qui il corpus contiene una contraddizione esplicita e documentata. La scoping review di [[source/fiorucci-bevilacqua-scoping-review-2024|Fiorucci e Bevilacqua (2024)]], che mappa 142 articoli su dieci anni di riviste pedagogiche italiane di Fascia A, individua tra le lacune nazionali proprio l'**educazione speciale**: internazionalmente uno dei campi più fecondi per l'IA in educazione, in Italia in "notevoli ritardi".

Due dettagli metodologici rendono il dato ancora più severo:

- degli articoli mappati, **85 su 142 stanno sull'asse epistemologico** (teorico o storico) e solo **57 su quello prasseologico** (sperimentale o empirico): la produzione è più riflessiva che sperimentale;
- gli autori escludono esplicitamente ogni valutazione di qualità dei singoli lavori e segnalano che in molti il disegno di ricerca non è dichiarato.

Dunque non abbiamo solo poca ricerca italiana sull'inclusione con l'IA: quella che c'è è per larga parte teorica. **L'indicazione di policy corre più veloce della ricerca nazionale che dovrebbe sostenerla.**

### 3. L'unica evidenza di efficacia disponibile è condizionale
Il wiki contiene una sola fonte che parla di evidenze empiriche di efficacia, e non è specifica sull'inclusione: l'[[source/oecd-digital-education-outlook-2026|OECD Digital Education Outlook 2026]]. Il suo risultato principale è che la GenAI sostiene l'apprendimento **solo se guidata da principi didattici chiari**; usata senza guida pedagogica, migliora la prestazione senza produrre reali guadagni di apprendimento.

Applicato all'inclusione, questo risultato è più insidioso che altrove. Il rischio tipico della personalizzazione automatica è che la difficoltà scenda, il compito venga completato e il divario di apprendimento resti — anzi si nasconda dietro un output migliore. È lo stesso meccanismo della [[concept/pigrizia-metacognitiva|pigrizia metacognitiva]], applicato agli studenti per cui il sostegno alla metacognizione conta di più. La convergenza con [[source/galli-ia-nella-didattica-2025|Galli (2025)]] rafforza il timore: l'uso studentesco rilevato è "largamente funzionale a scopi immediati e di utilità pratica", non orientato a processi metacognitivi.

### 4. I tre vincoli che tagliano fuori gli usi più ambiziosi
È la parte che un docente o un dirigente deve conoscere prima di progettare, perché i vincoli non colpiscono a caso: colpiscono gli usi più vicini alla promessa.

| Uso proposto dalle fonti | Cornice giuridica | Praticabilità oggi |
|---|---|---|
| Semplificare, riformulare, convertire in mappa o audio un materiale didattico | Nessun trattamento di dati personali se il testo è impersonale | **Praticabile subito** |
| Generare materiali differenziati "calibrati" su PEI e PDP | Divieto di inserire dati sensibili e identificativi nei prompt di modelli aperti ([[concept/privacy-protezione-dati|Privacy e protezione dei dati]]) | **Solo per astrazione**: caso verosimile inventato, mai il documento reale |
| Software che rileva attenzione, noia o frustrazione degli studenti | Pratica **vietata** dall'art. 5 AI Act, rischio inaccettabile ([[concept/riconoscimento-emozioni|Riconoscimento delle emozioni (pratica vietata)]]); divieto ribadito dal [[entity/garante-privacy|Garante]] e in vigore dal 2 febbraio 2025 | **Escluso, senza mitigazioni possibili** |
| Analisi predittive per individuare studenti a rischio di dispersione | L'istruzione è **alto rischio** (Allegato III, p. 3): assegnazione a percorsi e profilazione ([[concept/ai-act-categorie-rischio|AI Act — categorie di rischio]]) → [[concept/dpia-fria|DPIA + FRIA]] e [[concept/supervisione-umana|supervisione umana]] tassativa | **Non impossibile, ma il più oneroso** |

Il paradosso è netto: **i dati che renderebbero la personalizzazione più efficace — quelli di PEI e PDP — sono i meno utilizzabili**, perché sono i più sensibili. Non è un difetto di scrittura delle norme: PEI e PDP contengono dati sulla salute di minori.

Due precisazioni doverose. Primo, la via d'uscita indicata dal Garante e recepita dalla [[source/legge-132-2025|Legge 132/2025]] esiste, e sono i [[concept/dati-sintetici|dati sintetici]] o i casi verosimili inventati: si progetta su un profilo fittizio e si applica il risultato con giudizio professionale. Secondo, il rinvio degli obblighi sull'alto rischio al **2 dicembre 2027** ([[source/ai-act-digital-omnibus-2026|Digital Omnibus]]) non cambia nulla su questo punto — i divieti dell'art. 5 sono già pienamente efficaci, e il rinvio riguarda gli adempimenti, non la liceità del trattamento di dati sanitari di minori, che resta materia GDPR.

Va segnalata infine una zona grigia che le fonti del wiki **non risolvono**: [[source/ia-school|IA@School — Quadro normativo e strategico (EFT Calabria)]] chiede esplicitamente come si conciliano il divieto di riconoscimento delle emozioni e gli strumenti di *learning analytics* che inferiscono stati attentivi. Nessuna fonte disponibile traccia quel confine in modo operativo. Chi acquista una piattaforma con funzioni di questo tipo lo fa quindi senza una linea chiara, e come [[concept/deployer|deployer]] ne risponde.

### 5. Cosa resta, ed è più di quanto sembri
Se si sottraggono gli usi vietati, quelli ad alto rischio e quelli bloccati dal divieto sui dati sensibili, resta la fascia che il corpus chiama accessibilità e multimodalità — e che è, non per caso, la più vicina all'UDL originario:

- **conversione di formato**: lo stesso contenuto in testo, mappa, immagine, audio, così che nessun profilo di apprendimento sia strutturalmente svantaggiato;
- **semplificazione linguistica e testuale** dei materiali, a monte e non a valle della lezione;
- **strumenti assistivi** — sintesi vocale, trascrizione automatica — che il [[source/glossario-competenze-digitali|glossario DigComp 3.0]] classifica come tecnologie assistive e collega alla nozione di accessibilità;
- **produzione di materiali differenziati** costruiti sul bisogno didattico descritto in astratto, non sul documento personale dello studente.

Il tratto comune è che l'IA lavora **sul materiale, non sullo studente**. È una riduzione di ambizione rispetto alla promessa della personalizzazione algoritmica, ma è anche l'unica fascia dove non serve una FRIA e dove il vincolo dell'OCSE — guida pedagogica del docente — è automaticamente soddisfatto, perché è il docente a decidere cosa trasformare e per chi.

### 6. Il contro-effetto: l'IA inclusiva può escludere
Un ultimo elemento, il più scomodo, che il corpus documenta con precisione. L'IA è presentata come leva di equità mentre le condizioni per usarla sono esse stesse distribuite in modo diseguale ([[concept/divario-digitale|Divario digitale]]): l'accesso agli abbonamenti premium separa chi usa i modelli più capaci da chi resta sulle versioni gratuite; il divario è territoriale; e corre anche *dentro* la scuola, tra docenti aggiornati e non.

Le due contromisure finanziate — la riserva di almeno il **40% dei 100 milioni** del [[concept/snodi-formativi-pnrr|DM 219/2025]] alle scuole del Mezzogiorno e la formazione a cascata — sono reali ma indirette: finanziano formazione, non dotazione. E la domanda più pratica che l'inclusione pone, cioè **quali strumenti gratuiti** permettano a una scuola senza budget di fare le stesse cose, resta aperta nel wiki come nella [[source/guida-pratica-ia-secondaria|guida pratica]].

Vale la pena notare che l'equità è trattata dalle fonti come **imperativo categorico e non come effetto atteso** dell'IA: l'[[source/1-atto-di-indirizzo-per-l-adozione-dell-intelligenza-ar|Atto di indirizzo]] la fonda sugli artt. 34 e 38 della Costituzione. È una scelta di impostazione corretta, ed è anche l'ammissione che l'effetto inclusivo non è garantito dalla tecnologia.

## Fonti usate
- [[source/linee-guida-mim-dm166-2025|Linee Guida MIM (DM 166/2025)]]
- [[source/fiorucci-bevilacqua-scoping-review-2024|Fiorucci & Bevilacqua — scoping review 2024]]
- [[source/oecd-digital-education-outlook-2026|OECD Digital Education Outlook 2026]]
- [[source/galli-ia-nella-didattica-2025|Galli — L'IA nella didattica (2025)]]
- [[source/guida-pratica-ia-secondaria|Guida pratica all'IA nella scuola secondaria di I grado]]
- [[source/1-atto-di-indirizzo-per-l-adozione-dell-intelligenza-ar|Atto di indirizzo per l'adozione dell'IA]]
- [[source/adempimenti-e-cronoprogramma|Adempimenti e cronoprogramma]]
- [[source/ai-act-ue|AI Act (Reg. UE 2024/1689)]] · [[source/ai-act-digital-omnibus-2026|Digital Omnibus 2026]]
- [[source/legge-132-2025|Legge 132/2025]] · [[source/scuola-ok-del-garante-alle-linee-guida-del-mim-per-l-ia|Parere del Garante privacy]]
- [[source/glossario-competenze-digitali|Glossario competenze digitali (DigComp 3.0)]] · [[source/ia-school|IA@School — Quadro normativo e strategico (EFT Calabria)]]
- Concetti: [[concept/didattica-inclusiva-ia|Didattica inclusiva con IA]], [[concept/udl|Universal Design for Learning (UDL)]], [[concept/divario-digitale|Divario digitale]], [[concept/privacy-protezione-dati|Privacy e protezione dei dati]], [[concept/riconoscimento-emozioni|Riconoscimento delle emozioni (pratica vietata)]], [[concept/ai-act-categorie-rischio|AI Act — categorie di rischio]], [[concept/dati-sintetici|Dati sintetici]], [[concept/snodi-formativi-pnrr|Snodi formativi PNRR (DM 219/2025)]], [[concept/pigrizia-metacognitiva|Pigrizia metacognitiva]]

## Lacune e domande aperte
- **Nessun dato d'impatto sull'inclusione.** Il wiki non contiene una sola misura di efficacia dell'IA su studenti con BES o DSA — né italiana né internazionale. Tutto ciò che si può dire oggi è che la promessa non è smentita, non che sia verificata.
- **L'evidenza OCSE non è disaggregata per profilo di apprendimento.** Il risultato "prestazione sì, apprendimento no" è generale: non sappiamo se sugli studenti con BES l'effetto sia attenuato o amplificato. È la domanda che più conterebbe.
- **Il confine tra learning analytics e inferenza emotiva non è tracciato.** Nessuna fonte del wiki dà un criterio operativo, e la responsabilità di distinguere ricade sulla scuola-deployer.
- **Le analisi predittive contro la dispersione sono citate come obiettivo senza esame giuridico.** L'Atto di indirizzo e le dichiarazioni politiche le propongono; nessuna fonte del corpus discute se e come una scuola possa svolgerle legittimamente, dato che profilano minori.
- **Nulla sui docenti di sostegno.** Il corpus non contiene indicazioni specifiche per il personale di sostegno né per i CTS/CTI, che compaiono solo come componenti del Gruppo di Lavoro IA.
- **La domanda sugli strumenti gratuiti resta senza risposta.** Rilevata nella guida pratica, ripresa in [[concept/divario-digitale|Divario digitale]], mai colmata: è la lacuna più facilmente colmabile con una ricognizione dedicata.
- **Nessun dato sui percorsi PNRR e l'inclusione.** Le metodologie inclusive figurano tra i contenuti degli snodi formativi, ma non esistono nel wiki valutazioni indipendenti di quei percorsi.
