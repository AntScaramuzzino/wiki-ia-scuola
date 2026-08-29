---
title: "Scegliere uno strumento di IA per la classe: i filtri che vengono prima della didattica"
type: analysis
tags: [governance-scolastica-ia, privacy, normativa, ai-formazione, politiche]
created: 2026-08-29
updated: 2026-08-29
sources: [linee-guida-mim-dm166-2025, linee-guida-ia-a-scuola-aspetti-normativi-e-operativi, analisi-delle-linee-guida-mim-sull-ia-nella-scuola, ai-act-ue, oecd-digital-education-outlook-2026, linee-guida-della-ai-nelle-scuole, ia-school]
---

## Domanda
Come si sceglie uno strumento di IA da portare in classe, e chi lo decide davvero?

## Risposta sintetica
La scelta non è del singolo docente: nel momento in cui uno strumento tratta dati di studenti attraverso il canale scolastico, a sceglierlo è la scuola come [[concept/deployer|deployer]], e la decisione è per prima cosa un atto di esclusione. Prima di ogni valutazione didattica agiscono filtri che tagliano fuori intere categorie di prodotti: funzioni vietate, età degli utenti, finalità ad alto rischio, assenza di un contratto di responsabile del trattamento. Solo dopo entra in gioco il criterio pedagogico — e lì l'unica evidenza disponibile nel wiki dice che lo strumento conta meno della guida didattica che lo accompagna. Il nodo irrisolto è che nessuna fonte del corpus fornisce criteri operativi di scelta: le Linee Guida rimandano a standard e certificazioni senza dire come valutarli, con il rischio riconosciuto di favorire i grandi fornitori.

## Analisi

### 1. La domanda va riformulata: non si sceglie uno strumento, si assume una responsabilità

Le [[source/linee-guida-mim-dm166-2025|Linee Guida MIM (DM 166/2025)]] trasformano la scuola da utente a **utilizzatore professionale** ai sensi dell'art. 3, punto 4 dell'[[source/ai-act-ue|AI Act]]. La conseguenza è netta e viene resa esplicita dal webinar tecnico raccolto nel wiki: nel momento in cui il dirigente attiva l'IA dentro la suite d'istituto, «il responsabile di quello che fa l'intelligenza artificiale è la scuola, non è Google, non è Microsoft, perché la scuola l'ha selezionata» ([[source/linee-guida-ia-a-scuola-aspetti-normativi-e-operativi|Linee Guida IA a Scuola: aspetti normativi e operativi]]).

Da qui discende la distinzione più utile in pratica, e la meno presente nel dibattito corrente — quella tra **due canali**:

| Canale | Chi tratta i dati | Regime |
|---|---|---|
| **Account scolastico** (suite d'istituto, registro, piattaforme adottate) | La scuola, come Titolare e [[concept/deployer\|deployer]] | Adozione formale, contratti, valutazioni d'impatto, informative |
| **Account personale del docente**, senza dati di studenti | Il docente come privato | Fuori dal perimetro degli obblighi del deployer |

La stessa fonte precisa che il docente che usa un chatbot a casa, con account proprio, per prepararsi una lezione, non attiva la catena di obblighi; ciò che la attiva è il trattamento di dati di studenti tramite strumenti messi a disposizione dalla scuola. È una distinzione che rende governabile una parte consistente dell'uso reale — e che spiega perché il 66% dei docenti possa già usare l'IA settimanalmente ([[source/galli-ia-nella-didattica-2025|Galli 2025]]) senza che quasi nessuna scuola abbia completato la propria governance.

### 2. I quattro filtri di esclusione: cosa taglia fuori un prodotto prima di guardarne le funzioni

Le fonti convergono su quattro condizioni che non si negoziano e non si mitigano. Se anche una sola scatta, la valutazione didattica non comincia nemmeno.

| Filtro | Cosa esclude | Fonte |
|---|---|---|
| **Pratiche vietate** (art. 5 AI Act) | Qualsiasi funzione di riconoscimento delle emozioni o *sentiment analysis* su studenti, anche incorporata in un prodotto più ampio | [[concept/riconoscimento-emozioni\|Riconoscimento delle emozioni]] |
| **Età degli utenti** | Gli infratredicenni di fatto non possono usare gli strumenti, attivabili solo per i docenti; per la fascia 13-18 servono cautela e consenso | [[source/linee-guida-ia-a-scuola-aspetti-normativi-e-operativi\|webinar normativo]] |
| **Finalità ad alto rischio** | Sistemi che determinano ammissioni, valutano i risultati di apprendimento o sorvegliano le prove: ammessi solo con l'intero apparato di [[concept/dpia-fria\|DPIA + FRIA]] e supervisione qualificata | [[concept/ai-act-categorie-rischio\|Categorie di rischio]] |
| **Assenza di contratto** | Strumenti che trattano dati di studenti senza nomina formale del fornitore a responsabile del trattamento, con istruzioni scritte firmate dal dirigente: il trattamento è illecito | [[source/linee-guida-ia-a-scuola-aspetti-normativi-e-operativi\|webinar normativo]] |

Il primo filtro è il più insidioso perché è **invisibile in fase di acquisto**: il divieto colpisce una funzione, non un prodotto, e nulla garantisce che un fornitore la dichiari. È per questo che il censimento degli strumenti in uso — atto di governance apparentemente burocratico — è in realtà la precondizione operativa del divieto ([[concept/trasparenza-algoritmica|Trasparenza algoritmica]]).

Il quarto è il più frequentemente violato nella pratica: la fonte cita esplicitamente il caso di strumenti diffusissimi nella scuola, utilizzabili solo previa nomina a responsabile del trattamento con contratto firmato — «altrimenti è trattamento illecito».

### 3. Cosa la scuola deve poter documentare, se lo strumento supera i filtri

Superata l'esclusione, restano i requisiti che il [[concept/deployer|deployer]] deve essere in grado di dimostrare. Il webinar divulgativo sulle Linee Guida ([[source/linee-guida-della-ai-nelle-scuole|Linee guida dell'AI nelle scuole]]) e la sintesi formativa [[source/ia-school|IA@School]] li elencano come «requisiti di base» del modello MIM:

- **Certificazione ISO/IEC 27001 e qualificazione AgID del fornitore** — il requisito tecnico esplicito;
- **Informativa ex art. 50 AI Act**: studenti, famiglie e personale devono sapere quando interagiscono con un'IA ([[concept/trasparenza-algoritmica|Trasparenza algoritmica]]), obbligo operativo dal 2 agosto 2026 e **non rinviato** dal Digital Omnibus;
- **Esercitabilità dell'[[concept/opt-out|opt-out]]**: lo strumento deve permettere di escludere i dati degli studenti dall'addestramento, e la scuola deve poterlo dimostrare — il che significa, in concreto, verificare le configurazioni disponibili a livello di amministratore;
- **Configurabilità verso la minimizzazione**: preferire i [[concept/dati-sintetici|dati sintetici]] ai dati reali quando questi non sono strettamente indispensabili, come posto a condizione dal Garante;
- **Spiegabilità sufficiente all'oversight**: la [[concept/supervisione-umana|supervisione umana]] è esercitabile solo se l'output è tracciabile e contestabile ([[concept/explainable-ai|Explainable AI]]);
- **Divieto di dati sensibili nei prompt**: PEI e PDP non entrano nei modelli aperti — vincolo che nessuno strumento risolve al posto della scuola, e che quindi va scritto nel Regolamento d'uso ([[concept/privacy-protezione-dati|Privacy e protezione dei dati]]).

Qui compare la prima asimmetria strutturale: la scuola deve documentare misure di sicurezza e fonti di rischio che risiedono dentro l'infrastruttura del fornitore, e che sono coperte da segreto industriale. È la ragione per cui più fonti del wiki considerano la [[concept/fria|FRIA]] di fatto non assolvibile a regola d'arte da un singolo istituto.

### 4. Il criterio didattico esiste, ed è l'unico su cui il wiki ha evidenza empirica

Nessuno dei requisiti precedenti dice se uno strumento **fa apprendere**. Su questo il corpus ha un solo dato robusto, ed è scomodo: secondo l'[[source/oecd-digital-education-outlook-2026|OECD Digital Education Outlook 2026]], la GenAI sostiene l'apprendimento **solo se guidata da principi didattici chiari**; usata senza guida pedagogica, delegarle i compiti migliora la prestazione senza produrre reali guadagni di apprendimento. La performance sale, l'apprendimento no.

L'implicazione per la scelta è controintuitiva: **la variabile decisiva non è nel prodotto ma nel disegno dell'attività**. La [[source/guida-pratica-ia-secondaria|Guida pratica per la secondaria di I grado]] arriva alla stessa conclusione per via normativa anziché empirica — «l'IA deve essere sempre subordinata a una chiara finalità pedagogica» — e [[source/galli-ia-nella-didattica-2025|Galli]] la conferma dal lato degli usi reali: l'uso studentesco è «largamente funzionale a scopi immediati e di utilità pratica più che orientato a processi di apprendimento approfondito».

Due fonti indipendenti, un dato di adozione e un'evidenza sperimentale, convergono: la domanda «quale strumento» è meno determinante della domanda «dentro quale attività, con quale verifica del processo». Il che rimanda a [[analyses/2026-08-08-valutare-nell-era-dell-ia|Valutare nell'era dell'IA]].

### 5. Il buco: le fonti pongono i requisiti ma non danno criteri di scelta

Questa è la lacuna più netta emersa dalla ricerca interna, ed è denunciata da dentro il sistema. L'analisi di Gianfranco Bordoni ([[source/analisi-delle-linee-guida-mim-sull-ia-nella-scuola|Analisi critica delle Linee Guida MIM]]) elenca sette criticità applicative del DM 166; la sesta è esattamente questa: **riferimenti a standard e certificazioni (ISO, AgID) senza criteri concreti di scelta, con il rischio di favorire i grandi vendor**.

Il rischio non è teorico e si aggancia a una tensione già mappata nel wiki. Se l'ammissibilità di uno strumento passa per certificazioni che solo i grandi fornitori possono esibire, la conformità diventa essa stessa un fattore di concentrazione del mercato — e le scuole con meno risorse restano incastrate tra strumenti gratuiti non conformi e strumenti conformi non sostenibili. È il [[concept/divario-digitale|divario digitale]] nella sua forma più concreta: la stessa capacità di scegliere legalmente è distribuita in modo diseguale. La domanda «quali strumenti gratuiti consentono alle scuole con meno risorse di svolgere le attività di livello *Creare*» è aperta nel wiki e resta senza risposta.

Le contromisure proposte dalle fonti sono tutte di livello sovra-scolastico, non d'istituto: Bordoni propone **supporto regionale nella scelta delle tecnologie, valorizzando l'open source**, un tavolo tecnico e un vademecum operativo. Il webinar normativo osserva, con più asprezza, che la selezione «il Ministero lo poteva fare una volta sola» invece di replicarla in ottomila istituti. Su questo punto il wiki registra una tensione esplicita con la narrazione istituzionale, che presenta le Linee Guida come un supporto «senza vincoli»: le fonti operative le leggono come uno scarico di responsabilità sui dirigenti.

### 6. Una griglia in sette domande, ricavata dalle fonti

Nessuna fonte del corpus fornisce una checklist di selezione. Quella che segue è una **ricomposizione dei vincoli sparsi** nelle fonti citate, non un documento esistente da qualche parte — va letta come tale.

| # | Domanda | Se la risposta è sbagliata |
|---|---|---|
| 1 | Lo strumento inferisce stati emotivi o attentivi degli studenti? | Escluso: pratica vietata |
| 2 | Chi lo userà ha meno di 13 anni? | Attivabile solo per i docenti |
| 3 | Serve a valutare, ammettere o sorvegliare prove? | Alto rischio: DPIA + FRIA e supervisione qualificata, o si rinuncia |
| 4 | Il fornitore è nominabile responsabile del trattamento, con contratto e istruzioni scritte? | Senza contratto il trattamento è illecito |
| 5 | È configurabile per escludere i dati dall'addestramento e limitare la conservazione? | L'opt-out non è esercitabile: requisito non soddisfatto |
| 6 | Possiamo dire a studenti e famiglie che c'è un'IA, e spiegare cosa fa? | Obbligo art. 50 non assolvibile |
| 7 | L'attività in cui lo inseriamo ha una guida didattica esplicita, o delega il compito? | Migliorerà la prestazione, non l'apprendimento |

Le prime sei si rispondono in sede di governance, con DPO e Referente IA; la settima si risponde in consiglio di classe, ed è quella che decide se l'adozione avrà un senso.

## Fonti usate
- [[source/linee-guida-mim-dm166-2025|Linee Guida MIM per l'IA a scuola (DM 166/2025)]]
- [[source/linee-guida-ia-a-scuola-aspetti-normativi-e-operativi|Linee Guida IA a Scuola: aspetti normativi e operativi]]
- [[source/analisi-delle-linee-guida-mim-sull-ia-nella-scuola|Analisi critica delle Linee Guida MIM (Bordoni)]]
- [[source/linee-guida-della-ai-nelle-scuole|Linee guida dell'AI nelle scuole (webinar)]]
- [[source/ia-school|IA@School — Quadro normativo e strategico]]
- [[source/ai-act-ue|AI Act (Reg. UE 2024/1689)]]
- [[source/ai-act-digital-omnibus-2026|AI Act — Digital Omnibus 2026]]
- [[source/oecd-digital-education-outlook-2026|OECD Digital Education Outlook 2026]]
- [[source/galli-ia-nella-didattica-2025|Galli — L'IA nella didattica (2025)]]
- [[source/guida-pratica-ia-secondaria|Guida pratica all'IA nella secondaria di I grado]]
- [[concept/deployer|Deployer]] · [[concept/ai-act-categorie-rischio|Categorie di rischio]] · [[concept/riconoscimento-emozioni|Riconoscimento delle emozioni]] · [[concept/dpia-fria|DPIA e FRIA]] · [[concept/opt-out|Opt-out]] · [[concept/trasparenza-algoritmica|Trasparenza algoritmica]] · [[concept/dati-sintetici|Dati sintetici]] · [[concept/divario-digitale|Divario digitale]] · [[concept/supervisione-umana|Supervisione umana]]

## Lacune e domande aperte
- **Nessun criterio di valutazione dei fornitori esiste nel corpus.** Le fonti citano ISO/IEC 27001 e la qualificazione AgID, ma nessuna spiega come una scuola verifichi queste credenziali, né dove si consulti un elenco di strumenti qualificati per l'ambito scolastico. La griglia della sezione 6 è una ricomposizione, non una fonte.
- **Nessun dato su costi, listini o sostenibilità economica.** L'overview del wiki registra la copertura di strumenti e listini come «parziale»: non è possibile, con le fonti disponibili, dire quale configurazione conforme sia alla portata di un istituto medio.
- **Nessuna valutazione comparativa di strumenti concreti.** Il corpus nomina prodotti (suite d'istituto, chatbot, strumenti di grafica, *Teachable Machine*) ma non contiene alcun confronto di efficacia o conformità tra di essi.
- **Il perimetro tra learning analytics e inferenza emotiva non è tracciato.** [[source/ia-school|IA@School]] solleva la domanda e nessuna fonte la chiude: un sistema che segnala «calo di attenzione» ricade nel divieto? Il filtro 1 della griglia è quindi affilato in linea di principio e sfocato nei casi reali.
- **Effetto del rinvio dell'AI Act sul requisito FRIA delle Linee Guida.** Il Digital Omnibus sposta gli obblighi sull'alto rischio al 2 dicembre 2027, ma le Linee Guida MIM prescrivono la FRIA in proprio: nessuna fonte del wiki chiarisce se la prescrizione ministeriale segua il rinvio o resti autonoma. Per una scuola che oggi valuta uno strumento di supporto alla valutazione, la differenza è sostanziale.
- **Esito delle FAQ e checklist promesse su Piattaforma Unica.** Restano ignoti: se contenessero modelli standard di DPIA/FRIA e criteri di selezione, colmerebbero gran parte di questa analisi.
- **Nessuna fonte documenta esperienze di scelta condivisa tra istituti.** Il caso dei 55 istituti del Friuli-Venezia Giulia che hanno definito linee guida comuni ([[source/il-difficile-rapporto-tra-scuola-e-chatgpt-lucy-sulla-c|Lucy, 2025]]) riguarda l'uso didattico, non la selezione degli strumenti: se la scala d'istituto è troppo piccola per scegliere bene, quale sia la scala giusta resta una domanda aperta.
