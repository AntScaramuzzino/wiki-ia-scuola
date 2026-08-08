---
title: "DPIA e FRIA — valutazioni d'impatto"
type: concept
tags: [privacy, normativa, etica, governance-scolastica]
created: 2026-06-21
updated: 2026-06-21
sources: ["Linee Guida MIM DM 166/2025", "AI Act (art. 27)", "GDPR (art. 35)", "Valutazione d'impatto IA - AgID"]
---

> Pagina-quadro sul rapporto tra le due valutazioni. Per il dettaglio: [[concept/dpia|DPIA — Valutazione d'Impatto sulla Protezione dei Dati]] e [[concept/fria|FRIA — Valutazione d'Impatto sui Diritti Fondamentali]].

## Definizione
Due valutazioni d'impatto obbligatorie prima di adottare sistemi di IA:
- **[[concept/dpia|DPIA]]** (*Data Protection Impact Assessment*) — Valutazione d'Impatto sulla Protezione dei Dati, ex art. 35 GDPR.
- **[[concept/fria|FRIA]]** (*Fundamental Rights Impact Assessment*) — Valutazione d'Impatto sui Diritti Fondamentali, ex art. 27 [[source/ai-act-ue|AI Act]], richiesta per i sistemi ad **alto rischio** (vedi [[concept/ai-act-categorie-rischio|AI Act — categorie di rischio]]).

## Come funziona
La scuola, in qualità di [[concept/deployer|Deployer (utilizzatore professionale di IA)]] e Titolare del trattamento, esegue la **DPIA** considerando innovatività e volume dei dati. Se adotta un sistema ad alto rischio (es. valutazione degli apprendimenti), **integra la DPIA con la FRIA**, descrivendo processi, categorie di persone interessate, rischi di danno e misure di mitigazione e supervisione. Il **DPO** è consultato obbligatoriamente. La matrice AgID (AIIA) applica una logica analoga nella PA.

## Applicazioni o esempi
- Adozione di un tutor IA o di software valutativi → DPIA (+ FRIA se alto rischio).
- Raccomandazione ricorrente: preferire [[concept/privacy-protezione-dati|dati sintetici]] e minimizzazione.

## Relazioni con altri concetti
- [[concept/fria|FRIA — Valutazione d'Impatto sui Diritti Fondamentali]] — approfondimento dedicato sulla Valutazione d'Impatto sui Diritti Fondamentali
- [[concept/privacy-protezione-dati|Privacy e protezione dei dati]] — la DPIA è lo strumento cardine
- [[concept/governance-scolastica-ia|Governance scolastica dell'IA]] — adempimento guidato da DS e DPO
- [[concept/ai-act-categorie-rischio|AI Act — categorie di rischio]] — l'alto rischio attiva la FRIA
- [[concept/supervisione-umana|Supervisione umana (human-in-the-loop)]] — le misure di oversight sono parte della FRIA

## Contraddizioni e dibattiti
Più fonti (webinar e analisi) segnalano che la FRIA è di fatto **difficile da assolvere** per le scuole, che non dispongono delle informazioni interne dei fornitori (Google, Microsoft). Vedi [[source/linee-guida-ia-a-scuola-aspetti-normativi-e-operativi|Linee Guida IA a Scuola: Aspetti Normativi e Operativi (webinar)]].

## Fonti
[[source/linee-guida-mim-dm166-2025|Linee Guida MIM per l'IA a scuola (DM 166/2025)]], [[source/ai-act-ue|AI Act — Regolamento (UE) 2024/1689]], [[source/valutazione-d-impatto-dell-intelligenza-artificiale-agi|AgID — Valutazione d'impatto dell'Intelligenza Artificiale (AIIA), v1.0 2025]], [[source/l-intelligenza-artificiale-nella-pubblica-amministrazio|L'IA nella PA e nelle imprese: AgID, AI Act e strumenti per le valutazioni d'impatto (Federprivacy)]]
