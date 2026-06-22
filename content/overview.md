---
title: "Overview"
type: overview
updated: 2026-06-21
sources: [llm-wiki-pattern, linee-guida-mim-dm166-2025, ai-act-ue, legge-132-2025]
---

# Overview

> Sintesi evolutiva dell'intero wiki. Aggiornata dopo ogni ingest significativo per riflettere la comprensione attuale del dominio.

---

## Stato attuale

Il wiki copre due cluster:

1. **Meta — second brain**: il pattern di wiki persistente costruito da LLM (vedi [[source/llm-wiki-pattern]]).
2. **IA nella scuola**: il cluster principale. Le 70 fonti del notebook NotebookLM «Linee Guida sull'Intelligenza Artificiale a Scuola» sono state scaricate in full-text in `raw/` e ingestate (oltre 60 pagine `source`). Copre i quattro assi — didattica, policy, strumenti, etica — con sguardo italiano e internazionale, e include un sotto-filone su **IA nella Pubblica Amministrazione** ([[concept/ia-pubblica-amministrazione]]).

---

## Tesi principale (IA nella scuola)

L'IA entra ufficialmente nella scuola italiana attraverso un'**innovazione proceduralizzata**: non è vietata né lasciata all'iniziativa individuale, ma incanalata in una governance rigorosa che antepone la **centralità della persona** (approccio antropocentrico) e la **supervisione umana** all'automazione. Le [[source/linee-guida-mim-dm166-2025]] anticipano gli obblighi dell'[[source/ai-act-ue]] (pienamente applicabile dal 2 agosto 2026) e della [[source/legge-132-2025]], trasformando ogni scuola in un **"deployer"** giuridicamente responsabile.

---

## Temi emergenti

- **Quadro normativo a tre livelli**: AI Act UE → Legge 132/2025 → Linee Guida MIM. L'istruzione è settore **ad alto rischio** ([[concept/ai-act-categorie-rischio]], Allegato III AI Act). Vedi [[analyses/2026-06-21-quadro-normativo-ia-scuola]].
- **Scuola come [[concept/deployer]]**: responsabilità giuridica che attiva [[concept/dpia-fria]] e [[concept/explainable-ai]].
- **IA nella PA**: [[concept/ia-pubblica-amministrazione]] — quadro AgID (linee guida, strategia, valutazione d'impatto), [[entity/agid]] e [[entity/acn]] autorità nazionali.
- **Governance d'istituto**: [[concept/governance-scolastica-ia]] — atto di indirizzo, Piano d'Istituto per l'IA (PIA) nel PTOF, Referente IA (RIA), DPO, cronoprogramma a.s. 2025/2026.
- **Didattica trasformata**: [[concept/scuola-aumentata]] (docente co-pilota, personalizzazione) e [[concept/didattica-inclusiva-ia]] (UDL, BES/DSA).
- **Competenze e alfabetizzazione**: [[concept/alfabetizzazione-ia]] e il confronto tra framework UNESCO, OECD e DigComp ([[analyses/2026-06-21-confronto-framework-competenze-ia]]).
- **Etica e rischi**: [[concept/privacy-protezione-dati]], [[concept/bias-algoritmico]], [[concept/supervisione-umana]], [[concept/valutazione-integrita-accademica]].
- **Formazione e finanziamenti**: [[concept/snodi-formativi-pnrr]] (DM 219/2025, PNRR, 100 mln €, [[entity/scuola-futura]]).

---

## Tensioni e contraddizioni aperte

- **Innovazione vs controllo**: spinta all'adozione dell'IA contro obblighi stringenti (DPIA/FRIA, opt-out) che possono rallentare le scuole meno attrezzate.
- **FRIA inassolvibile?**: più fonti (webinar, analisi) sostengono che la FRIA è di fatto difficile da svolgere a regola d'arte, perché la scuola-deployer non dispone delle informazioni interne dei fornitori (Google, Microsoft).
- **Centralità del Dirigente Scolastico**: le Linee Guida concentrano la responsabilità sul DS; alcune analisi (es. USR Lombardia) auspicano una governance più collaborativa.
- **Legge 132 vs AI Act**: una disciplina nazionale "a prescindere dal rischio" potrebbe confliggere con l'AI Act (rilievo della Commissione UE).
- **Valutazione automatizzata**: utile ma classificata ad alto rischio; gli AI detector sono inaffidabili — la risposta è spostare il focus dal prodotto al processo.
- **Dominio IA dedicato vs trasversale**: UNESCO/OCSE creano un dominio IA autonomo; DigComp 3.0 integra l'IA in modo trasversale alle competenze digitali.
- **Divario digitale**: rischio di una "scuola a due velocità" tra istituti con risorse/abbonamenti premium e istituti sprovvisti.

---

## Lacune di conoscenza

- Esiti delle prime sperimentazioni ("Progetti IA") sulla Piattaforma Unica: nessun dato d'impatto ancora nel corpus.
- Strumenti specifici e listini (oltre agli esempi didattici): copertura parziale.
- Contesto comparato extra-UE (USA, Asia): assente; il corpus è UE/Italia-centrico.
- Valutazioni indipendenti dell'efficacia degli interventi formativi PNRR.

---

## Cronologia dell'evoluzione

| Data | Evento |
|------|--------|
| 2026-04-22 | Inizializzazione wiki |
| 2026-04-22 | Ingest: pattern del second brain (cluster meta) |
| 2026-06-21 | Ingest: notebook NotebookLM «Linee Guida sull'IA a Scuola» (70 fonti) — nasce il cluster "IA nella scuola" (34 pagine) |
| 2026-06-21 | Ingest glossario competenze digitali (126 voci) + 4 concetti (deepfake, cyberbullismo, disinformazione, gamification) |
| 2026-06-21 | Download full-text delle 70 fonti in `raw/` e ingest completo: 52 nuove pagine source + 6 pagine-ponte (categorie rischio, DPIA/FRIA, deployer, explainable AI, IA-PA, ACN) |
