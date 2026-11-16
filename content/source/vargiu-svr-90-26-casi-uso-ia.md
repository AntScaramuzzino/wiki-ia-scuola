---
title: "SVR 90/26 — I casi d'uso dell'IA a scuola: classificarli prima di scegliere gli strumenti"
type: source
tags: [normativa, governance-scolastica, ai, politiche, privacy]
created: 2026-11-16
updated: 2026-11-16
sources: ["Vargiu Scuola, nota SVR 90/2026, Assemini, 21 agosto 2026"]
---

**File raw**: `raw/notes/vargiu-svr-90-26-casi-uso-ia.pdf` · `raw/notes/vargiu-svr-90-26-casi-uso-ia.md`
**Origine**: [[entity/vargiu-scuola|Vargiu Scuola]], nota SVR 90/2026, 21 agosto 2026.

## Sommario
La trattazione più rigorosa, nel corpus, della differenza fra il rischio dell'**AI Act** e il rischio del **GDPR**. Definisce il «caso d'uso» come combinazione di quattro elementi, spiega perché la classificazione non dipende dallo strumento, e chiarisce che pseudonimizzare gli elaborati non declassifica un sistema ad alto rischio.

## Punti chiave
- **Un caso d'uso è la combinazione di quattro elementi**: la **finalità** istituzionale, l'**attività** concreta, i **dati** che vi entrano, il **soggetto e il contesto** in cui opera. Cambiando uno solo, la valutazione cambia a parità di strumento.
- **Due nozioni di rischio che non coincidono**. L'AI Act è **normativa di prodotto**: il rischio è un *criterio di classificazione* predeterminato dal legislatore, opera ex ante e non dipende dalle circostanze — «la scuola non la determina: la riscontra». Il GDPR usa il rischio in senso proprio: probabilità e gravità di un pregiudizio, valutazione contestuale che dipende dalle misure adottate.
- **Il punto più spesso trascurato**: «le misure che riducono il rischio privacy non modificano la classificazione del sistema». Una piattaforma destinata a valutare elaborati resta nell'Allegato III anche su prove pseudonimizzate: la DPIA può non servire, ma gli obblighi del deployer e la **FRIA restano dovuti**, perché dipendono dalla finalità del sistema e non dai dati che vi transitano.
- **Art. 25 AI Act**: se la scuola modifica la finalità prevista di un assistente generico destinandolo a una funzione dell'Allegato III, **è considerata fornitore** — con sistema di gestione dei rischi, documentazione tecnica, sistema qualità, registrazione nella banca dati europea. Adempimenti che presuppongono un controllo sul sistema che la scuola non ha.
- **Allegato III, punto 3** (istruzione): accesso/ammissione/assegnazione; **valutazione dei risultati dell'apprendimento, anche se usati per orientare il processo**; valutazione del livello di istruzione appropriato; monitoraggio di comportamenti vietati durante le prove. «Sono proprio le funzioni presenti nelle proposte commerciali fatte spesso alle scuole.»
- **La deroga dell'art. 6, par. 3** esclude i sistemi il cui apporto è marginale, in quattro figure (compito procedurale limitato; miglioramento di attività umana già completata; rilevazione di scostamenti senza sostituire la valutazione umana; compito meramente preparatorio). **Non opera mai in caso di profilazione**, e chi la invoca deve documentare per iscritto. «È una via stretta: la correzione meccanica di quiz a risposta chiusa vi rientra plausibilmente, la valutazione di un elaborato argomentativo no.»
- **Due nuovi divieti dal 2 dicembre 2026**: sistemi che generano o manipolano materiale intimo non consensuale di persone riconoscibili (*nudification*) e materiale di abuso sessuale su minori. Per la scuola rilevano non per l'adozione ma per l'**e-safety policy** e il Regolamento.
- **Generativo e non generativo**: le funzioni di *elaborazione* (rimozione sfondo, conversione formato, trascrizione del proprio parlato, traduzione, sintesi vocale) trasformano un contenuto che l'utente già possiede. Non vanno sottoposte allo stesso regime: sono «di particolare utilità per gli alunni con bisogni educativi speciali» come strumenti compensativi.
- **Ambito didattico e amministrativo-organizzativo**: la distinzione è **funzionale, non soggettiva**. La valutazione degli elaborati, la predisposizione di atti e la verbalizzazione degli organi collegiali «sono attività amministrative, non didattiche», anche quando svolte da docenti — e ricadono quindi nei requisiti di qualificazione cloud delle PA.
- **Assenza di dati personali ≠ assenza di trattamento**: l'accesso avviene con credenziali istituzionali e il fornitore registra identità, orari e log. Il registro dei trattamenti va comunque aggiornato.

## Entità menzionate
[[entity/vargiu-scuola|Vargiu Scuola]], [[entity/agid|Agenzia per l'Italia Digitale (AgID)]], [[entity/acn|ACN — Agenzia per la Cybersicurezza Nazionale]]

## Concetti trattati
[[concept/caso-uso-ia|Caso d'uso dell'IA (unità di classificazione del rischio)]] — i quattro elementi e il registro dei casi d'uso
[[concept/ai-act-categorie-rischio|AI Act — categorie di rischio]] — le quattro categorie, l'Allegato III, la deroga dell'art. 6, par. 3
[[concept/fria|FRIA — Valutazione d'Impatto sui Diritti Fondamentali]] — dovuta per finalità, non per dati
[[concept/dpia|DPIA — Valutazione d'Impatto sulla Protezione dei Dati]] — e la differenza di metodo rispetto alla FRIA
[[concept/deployer|Deployer (utilizzatore professionale di IA)]] — e l'art. 25 che trasforma il deployer in fornitore
[[concept/ia-generativa-vs-elaborazione|IA generativa e IA di elaborazione]] — la distinzione e le sue conseguenze regolamentari
[[concept/valutazione-integrita-accademica|Valutazione e integrità accademica]] — la valutazione degli elaborati come caso ad alto rischio
[[concept/riconoscimento-emozioni|Riconoscimento delle emozioni (pratica vietata)]] — fra le pratiche vietate dall'art. 5
[[concept/deepfake|Deepfake]] — i nuovi divieti dal 2 dicembre 2026
[[concept/didattica-inclusiva-ia|Didattica inclusiva con IA]] — le funzioni non generative come strumenti compensativi

## Citazioni rilevanti
> "Il livello di rischio non dipende dallo strumento, ma dalla combinazione fra lo strumento e il caso d'uso."

> "Per la scuola questo significa avere tempo per attrezzarsi, non per rimandare."

## Contraddizioni o tensioni
**Risolve un'ambiguità ricorrente nel corpus.** Il wiki ha trattato DPIA e FRIA come adempimenti affini ([[concept/dpia-fria|DPIA e FRIA — valutazioni d'impatto]]). Questa fonte stabilisce che misurano oggetti diversi e **non si compensano**: pseudonimizzare riduce il rischio privacy ma non declassifica il sistema ai fini dell'AI Act. È una precisazione che cambia la lettura della [[concept/fria|FRIA — Valutazione d'Impatto sui Diritti Fondamentali]].

**Ridimensiona la «FRIA inassolvibile»**: la tensione registrata nel wiki (la scuola-deployer non ha le informazioni interne dei fornitori) resta, ma questa fonte la aggira per via strategica — non adottare sistemi ad alto rischio in questa fase, così la FRIA non si pone.

**Nota professionale, non fonte primaria**: la classificazione proposta è una lettura argomentata dell'AI Act, da verificare sul testo del Regolamento e sugli orientamenti della Commissione.

## Domande aperte
- La deroga dell'art. 6, par. 3 regge per la correzione automatica di quiz chiusi? La nota dice «plausibilmente», non con certezza.
- Quante scuole hanno già adottato piattaforme adattive che ricadono nell'Allegato III senza saperlo?
