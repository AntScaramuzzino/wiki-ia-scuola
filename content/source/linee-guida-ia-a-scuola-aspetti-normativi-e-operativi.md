---
title: "Linee Guida IA a Scuola: Aspetti Normativi e Operativi (webinar)"
type: source
tags: [ai, educazione, normativa, privacy, governance-scolastica-ia, valutazione, ai-formazione, etica]
created: 2026-06-21
updated: 2026-06-21
sources: ["Linee Guida IA a Scuola: Aspetti Normativi e Operativi"]
---

# Linee Guida IA a Scuola: Aspetti Normativi e Operativi (webinar)

**File raw**: `raw/papers/linee-guida-ia-a-scuola-aspetti-normativi-e-operativi.md`
**Origine**: NotebookLM «Linee Guida sull'Intelligenza Artificiale a Scuola»

## Sommario
Trascrizione di un webinar (relatori Lorenzo e Piergiorgio, esperto/DPO) che analizza criticamente le Linee guida MIM per l'introduzione dell'IA nelle scuole, soffermandosi sugli aspetti normativi e operativi. Il focus è sull'inquadramento della scuola come "deployer" ai sensi dell'AI Act, sugli obblighi di valutazione del rischio (DPIA e FRIA) e sulle pesanti criticità pratiche che ne derivano per i dirigenti scolastici e i DPO. Aggiunge un livello operativo e di problematizzazione assente nelle fonti istituzionali.

## Punti chiave
- L'AI Act classifica i sistemi per rischio (inaccettabile, alto, limitato, minimo); i sistemi usati per valutare i risultati di apprendimento o l'accesso/ammissione agli istituti rientrano tra quelli **ad alto rischio** (Allegato III, art. 6).
- La scuola opera come **deployer**: nel momento in cui il DS attiva l'IA dentro Google Workspace (Gemini) o Microsoft Teams (Copilot), si assume la responsabilità di quanto fa l'IA — non Google né Microsoft.
- Catena privacy GDPR: la scuola è **titolare** del trattamento; deve nominare formalmente (contratto) i fornitori (Google, Microsoft, registro elettronico) come **responsabili** del trattamento e dare loro istruzioni scritte.
- Obbligo di **DPIA / Valutazione d'impatto** (valutazione di impatto sulla protezione dei dati) prima del trattamento; il Garante mette a disposizione un software dedicato. Criticità enorme: la scuola dovrebbe dichiarare le misure di sicurezza e le fonti di rischio interne di Google/Microsoft, informazioni di fatto inaccessibili (segreti industriali).
- Se la scuola classifica il sistema come ad alto rischio, scatta anche l'obbligo di **FRIA** (Fundamental Rights Impact Assessment) previsto dall'AI Act, con descrizione delle misure di sorveglianza umana — difficili da garantire quando lo studente usa lo strumento a casa.
- Minori: gli infra-tredicenni di fatto non possono usare gli strumenti (attivabili solo per i docenti); per i 13-18 occorre cautela e consenso. I prompt non devono trattare dati personali identificativi; rischio concreto di immissione di dati sensibili da parte degli studenti.
- Distinzione tra canale **account scolastico** (scuola deployer, soggetta a obblighi) e canale **personale** (docente che usa ChatGPT a casa con account proprio, senza trattare dati degli studenti).
- Strumenti come Canva che trattano dati degli studenti sono utilizzabili solo previa nomina a responsabile del trattamento con contratto firmato dal dirigente; altrimenti è trattamento illecito.
- Metodo operativo proposto dalle linee guida: ciclo in 5 fasi (definizione, pianificazione, adozione graduale/pilota, monitoraggio, conclusione), ispirato al design thinking; uso dell'acronimo UDHRIA/HUDERIA per la valutazione d'impatto sui diritti fondamentali.

## Entità menzionate
[[entity/mim]] — autore delle linee guida analizzate
[[entity/garante-privacy]] — mette a disposizione il software per la DPIA; ha dato parere sul decreto
[[entity/commissione-europea]] — quadro AI Act di riferimento

## Concetti trattati
[[concept/governance-scolastica-ia]] — ruolo del DS, del DPO e degli organi collegiali
[[concept/privacy-protezione-dati]] — GDPR, titolare/responsabile, DPIA, privacy by design/default
[[concept/valutazione-integrita-accademica]] — uso dell'IA per valutare elaborati (alto rischio)
[[concept/supervisione-umana]] — sorveglianza umana richiesta dalla FRIA
[[concept/llm]] — strumenti come Gemini/Copilot/ChatGPT discussi
[[concept/ia-generativa]] — oggetto dell'adozione scolastica
[[concept/allucinazione]] — citata a proposito della deep research sulla classificazione del rischio
[[concept/alfabetizzazione-ia]] — necessità di un curricolo graduale di introduzione dell'IA

## Citazioni rilevanti
> "A tutti gli effetti il responsabile di quello che fa l'intelligenza artificiale è la scuola, non è Google, non è Microsoft, perché la scuola l'ha selezionata [...] e se ne assume la responsabilità."

> "Il Ministero lo poteva fare una volta sola. [...] Le scuole possono usare tanto Gemini, unico Copilot. [...] Sarebbe stato molto semplice così."

## Contraddizioni o tensioni
Tensione (non contraddizione fattuale) con la narrazione istituzionale di [[source/linee-guida-mim-dm166-2025]] e con l'intervento del direttore D'Amico ([[source/innovazione-digitale-e-strategie-scolastiche-nazionali-]]), che presentano le linee guida come un supporto "senza vincoli". I relatori del webinar evidenziano invece criticità operative gravissime (DPIA e FRIA di fatto impossibili da redigere a regola d'arte; scarico di responsabilità sui DS) e la mancanza di una soluzione "chiavi in mano" da parte del Ministero. Approfondisce operativamente i concetti di deployer e alto rischio già introdotti dalle fonti canoniche [[source/legge-132-2025]] e [[source/ai-act-ue]].

## Domande aperte
- Quale tempo verrà concesso alle scuole per caricare i progetti IA su Piattaforma Unica?
- Le FAQ/checklist promesse su Unica (DM 166) forniranno modelli standard di DPIA/FRIA o l'onere resterà sui singoli istituti?
- Come gestire concretamente la sorveglianza umana quando lo studente usa l'IA fuori dall'orario scolastico?
- È sufficiente disattivare la cronologia delle conversazioni (possibile a livello admin in Gemini) per ridurre il rischio?
