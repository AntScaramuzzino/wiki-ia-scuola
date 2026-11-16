---
title: "Caso d'uso dell'IA (unità di classificazione del rischio)"
type: concept
tags: [normativa, governance-scolastica, ai, politiche, privacy]
created: 2026-11-16
updated: 2026-11-16
sources: ["Vargiu Scuola, note SVR 90/2026 e 91/2026", "Determinazione AgID n. 17/2025", "AI Act (artt. 6, 25, Allegato III)"]
---

## Definizione
Il **caso d'uso** è l'unità rispetto a cui si classifica il rischio di un impiego dell'IA. Non coincide con lo strumento: è la combinazione di **quattro elementi**.

1. la **finalità** perseguita — a quale scopo istituzionale l'impiego è diretto;
2. l'**attività** che si svolge in concreto (produrre una scheda di esercizi, redigere una circolare, correggere una verifica);
3. i **dati** che vi entrano (nessun dato personale, dati pseudonimizzati, dati identificativi, categorie particolari);
4. il **soggetto** che opera e il **contesto** (docente, personale amministrativo, studente; in classe sotto supervisione o in autonomia).

Modificando uno solo dei quattro, la valutazione cambia **a parità di strumento impiegato**.

## Come funziona
Ciascun elemento governa una valutazione diversa: la **finalità** determina la classificazione ai sensi dell'AI Act; i **dati** determinano la valutazione ai sensi del GDPR; **soggetto e contesto** stabiliscono chi possa procedere e con quali cautele.

Da qui l'ordine del percorso: **prima si classificano i casi d'uso, poi si scelgono gli strumenti**. La [[entity/agid|Determinazione AgID 17/2025]] richiede la mappatura dei casi d'uso come attività distinta dalla scelta delle soluzioni tecnologiche. Lo strumento operativo è un **Registro dei casi d'uso**, allegato al [[concept/piano-istituto-ia|Piano d'Istituto]], affiancato da una scheda di istruttoria per i casi che richiedono esame approfondito.

L'onere dell'istruttoria è **proporzionato al rischio dell'impiego**:

| Se l'impiego… | l'istruttoria… |
|---|---|
| non comporta trattamento di dati personali oltre quelli di accesso | è leggera e documentale |
| comporta trattamento di dati personali comuni | richiede valutazione più approfondita |
| incide sulla valutazione degli apprendimenti, tratta dati di alunni in modo sistematico o comporta monitoraggio | richiede valutazione d'impatto approfondita |

## Applicazioni o esempi
- Un assistente generativo che produce una **griglia di correzione** è supporto alla progettazione didattica: rischio minimo. Lo **stesso assistente**, al quale si sottopongano gli elaborati chiedendo una proposta di voto, è destinato alla valutazione dei risultati dell'apprendimento: rientra nell'**Allegato III**, e la scuola ne assume gli obblighi. Non è cambiato lo strumento né l'attività materiale — è cambiato lo scopo.
- **Art. 25 AI Act**: se la scuola modifica la finalità prevista di un sistema destinandolo a una funzione dell'Allegato III, **è considerata fornitore**, non solo deployer.
- **Ambito funzionale, non soggettivo**: la valutazione degli elaborati, la predisposizione di atti e la verbalizzazione degli organi collegiali sono attività **amministrative** anche quando svolte da docenti — e ricadono quindi nei requisiti di qualificazione cloud delle PA.

## Relazioni con altri concetti
- [[concept/ai-act-categorie-rischio|AI Act — categorie di rischio]] — la classificazione si applica al caso d'uso, non al prodotto
- [[concept/dpia|DPIA — Valutazione d'Impatto sulla Protezione dei Dati]] e [[concept/fria|FRIA — Valutazione d'Impatto sui Diritti Fondamentali]] — due valutazioni distinte che il caso d'uso attiva separatamente
- [[concept/deployer|Deployer (utilizzatore professionale di IA)]] — e l'art. 25, che può trasformarlo in fornitore
- [[concept/piano-istituto-ia|Piano d'Istituto per l'IA (PIA) e Atto di Indirizzo]] — il Registro dei casi d'uso è allegato al Piano
- [[concept/ia-generativa-vs-elaborazione|IA generativa e IA di elaborazione]] — una delle due distinzioni che completano la classificazione
- [[concept/grado-maturita-ia|Grado di maturità dell'amministrazione (modello AgID)]] — la ricognizione degli usi in atto fornisce il materiale da classificare
- [[concept/shadow-ai|Shadow AI (uso non dichiarato dell'IA)]] — i casi d'uso da classificare sono anzitutto quelli già in corso

## Contraddizioni e dibattiti
**Classificare i prodotti è metodologicamente sbagliato.** Attribuire a ciascun applicativo un livello di rischio valido per qualunque uso «produce esiti arbitrari e genera un elenco che nessuno saprà aggiornare con criterio». È però ciò che molte scuole fanno, perché la domanda spontanea è «ChatGPT si può usare?» anziché «per quale finalità e con quali dati».

**Le due scale di rischio non si compensano.** Le misure che riducono il rischio privacy non modificano la classificazione ai sensi dell'AI Act: una piattaforma destinata a valutare elaborati resta nell'Allegato III anche se impiegata su prove **pseudonimizzate**. La DPIA può non essere necessaria, ma gli obblighi del deployer e la **FRIA restano dovuti**, perché dipendono dalla finalità del sistema e non dai dati che vi transitano.

**Assenza di dati personali non significa assenza di trattamento**: l'accesso avviene con credenziali istituzionali e il fornitore registra identità, orari e log. Il registro dei trattamenti va comunque aggiornato.

## Fonti
[[source/vargiu-svr-90-26-casi-uso-ia|SVR 90/26 — I casi d'uso dell'IA a scuola: classificarli prima di scegliere gli strumenti]], [[source/vargiu-svr-91-26-strumenti-ia-garanzie|SVR 91/26 — Adottare gli strumenti di IA: quali, come, con quali garanzie]], [[source/vargiu-svr-92-26-piano-istituto-ia|SVR 92/26 — Il Piano d'Istituto per l'intelligenza artificiale]], [[source/agid-bozza-di-linee-guida-per-l-adozione-di-ia-nella-pu|AgID — Bozza di linee guida per l'adozione di IA nella Pubblica Amministrazione (v1.0, 2025)]]
