#!/usr/bin/env python3
"""Rigenera wiki/index.md del second brain a partire dalle pagine esistenti."""
import os, re, glob

WIKI = "/Users/antonioscaramuzzino/Library/CloudStorage/GoogleDrive-a.scaramuzzino@gmail.com/Il mio Drive/Brain/LLM-Wiki/LLM-Wiki/wiki"

def fm(text, key):
    m = re.search(rf"^{key}:\s*(.+)$", text, re.M)
    return m.group(1).strip().strip('"') if m else ""

def section_first_line(text, headers):
    for h in headers:
        m = re.search(rf"^##\s+{re.escape(h)}\s*$", text, re.M)
        if not m:
            continue
        for line in text[m.end():].splitlines():
            s = line.strip()
            if not s or s.startswith(("#", ">", "**File", "**Origine", "**Nota")):
                continue
            return s
    return ""

def clean(s, n=95):
    s = re.sub(r"\[\[[^\]]*?\|([^\]]+)\]\]", r"\1", s)
    s = re.sub(r"\[\[([^\]]+)\]\]", lambda m: m.group(1).split("/")[-1], s)
    s = re.sub(r"[*`>#_]", "", s).strip()
    s = re.sub(r"^-\s*", "", s)
    return (s[:n] + "…") if len(s) > n else s

def load(kind):
    rows = []
    for f in sorted(glob.glob(f"{WIKI}/{kind}/*.md")):
        t = open(f, encoding="utf-8").read()
        slug = os.path.splitext(os.path.basename(f))[0]
        rows.append({
            "slug": slug,
            "created": fm(t, "created"),
            "src": clean(section_first_line(t, ["Sommario"])),
            "ent": clean(section_first_line(t, ["Descrizione", "Ruolo nel dominio"])),
            "con": clean(section_first_line(t, ["Definizione"])),
            "an": clean(section_first_line(t, ["Domanda"])),
        })
    return rows

sources, entities = load("sources"), load("entities")
concepts, analyses = load("concepts"), load("analyses")
total = len(sources) + len(entities) + len(concepts) + len(analyses)

o = ["---", 'title: "Indice del wiki"', "type: index", "updated: 2026-08-08",
     "total_sources: 4", f"total_pages: {total}", "---", "",
     f"Aggiornato: 2026-08-08 — corpus principale: notebook NotebookLM «Linee Guida sull'IA a Scuola» "
     f"(70 fonti in `raw/`) + glossario (126 voci) + rassegna news. {total} pagine.", "",
     "Catalogo dell'intero wiki. Leggi questo file prima di qualsiasi query.", "",
     "Il wiki ha due cluster: **Meta — second brain** (come si costruisce un wiki con LLM) e "
     "**IA nella scuola** (didattica, policy, strumenti, etica; Italia + internazionale).", ""]

o += [f"## Fonti — {len(sources)}", "", "| Pagina | Sommario | Data |", "|--------|----------|------|"]
o += [f"| [[source/{r['slug']}]] | {r['src']} | {r['created']} |" for r in sources] + [""]
o += [f"## Entità — {len(entities)}", "", "| Pagina | Descrizione |", "|--------|-------------|"]
o += [f"| [[entity/{r['slug']}]] | {r['ent']} |" for r in entities] + [""]
o += [f"## Concetti — {len(concepts)}", "", "| Pagina | Definizione breve |", "|--------|-------------------|"]
o += [f"| [[concept/{r['slug']}]] | {r['con']} |" for r in concepts] + [""]
o += [f"## Analisi — {len(analyses)}", "", "| Pagina | Domanda | Data |", "|--------|---------|------|"]
o += [f"| [[analyses/{r['slug']}]] | {r['an']} | {r['created']} |" for r in analyses] + [""]

open(f"{WIKI}/index.md", "w", encoding="utf-8").write("\n".join(o))
print(f"index.md rigenerato: sources={len(sources)} entities={len(entities)} "
      f"concepts={len(concepts)} analyses={len(analyses)} total={total}")
