#!/usr/bin/env python3
"""Aggiunge alle pagine source il puntatore ai file raw corrispondenti,
così che ogni fonte grezza risulti citata e tracciabile."""
import os, re

WIKI = "/Users/antonioscaramuzzino/Library/CloudStorage/GoogleDrive-a.scaramuzzino@gmail.com/Il mio Drive/Brain/LLM-Wiki/LLM-Wiki/wiki"

MAP = {
 "linee-guida-mim-dm166-2025": [
   "raw/papers/2025-mim-linee-guida-per-l-introduzione-dell-intelligenza-artificiale-.md"],
 "ai-act-ue": [
   "raw/papers/2024-ai-act-pdf.md",
   "raw/papers/2024-ai-act-shaping-europe-s-digital-future.md"],
 "legge-132-2025": [
   "raw/papers/2025-legge-132-2025-disposizioni-e-deleghe-al-governo-in-materia-di-in.md"],
 "digcomp-3-0": [
   "raw/papers/2025-digcomp-3-0-jrc144121-01-pdf.md",
   "raw/papers/2026-digcomp-3-0-quadro-europeo-competenze-digitali-italiano-v1-pdf.md",
   "raw/papers/digcomp-3-0-quadro-europeo-competenze-digitali-italiano-v1-pdf.md"],
 "unesco-competenze-docenti-2024": [
   "raw/papers/2024-unesco-ai-competency-framework-for-teachers-cedefop.md"],
 "unesco-competenze-studenti-2024": [
   "raw/papers/2024-unesco-ai-competency-framework-for-students.md"],
 "unesco-guidance-genai-2023": [
   "raw/papers/2023-unesco-guidance-for-generative-al-in-education-and-research-pdf.md"],
 "oecd-ai-literacy-2025": [
   "raw/papers/2025-oecd-ai-literacy-framework-for-primary-secondary-education-oecd-e.md",
   "raw/papers/2025-oecd-ai-literacy-framework-home.md"],
 "guida-pratica-ia-secondaria": [
   "raw/papers/guida-pratica-all-ia-nella-scuola-secondaria.md"],
 "manifesto-codice-etico-isis-europa": [
   "raw/notes/manifesto-dell-intelligenza-artificiale-a-scuola-isis-europa-manifesto.md",
   "raw/papers/codice-etico-pdf.md",
   "raw/papers/codice-etico-intelligenza-artificiale-generativa-a-scuola-una-pagina-p.md"],
 "dm-219-2025-snodi-formativi": [
   "raw/notes/candidatura-snodi-formativi-intelligenza-artificiale-dm219-25-docx.md"],
 "glossario-competenze-digitali": [
   "raw/notes/glossario-pdf.md"],
 "explainable-ai-in-education-fostering-human-oversight-a": [
   "raw/articles/explainable-ai-in-education-fostering-human-oversight-and-shared-respo.md"],
 "in-vigore-dal-10-ottobre-l-obbligo-di-informativa-per-i": [
   "raw/articles/in-vigore-dal-10-ottobre-l-obbligo-di-informativa-per-i-clienti-sull-u.md"],
 "oecd-digital-education-outlook-2026": [
   "raw/papers/062a7394-en.pdf", "raw/papers/65cd27d4-en.pdf"],
}

changed = 0
for slug, raws in MAP.items():
    p = os.path.join(WIKI, "sources", slug + ".md")
    if not os.path.exists(p):
        print("MANCA la pagina:", slug); continue
    t = open(p, encoding="utf-8").read()
    existing = re.search(r"^\*\*File raw\*\*:.*$", t, re.M)
    line = "**File raw**: " + " · ".join(f"`{r}`" for r in raws)
    if existing:
        if existing.group(0) == line:
            continue
        t = t[:existing.start()] + line + t[existing.end():]
    else:
        m = re.search(r"^\*\*Origine\*\*:.*$", t, re.M)
        if m:
            t = t[:m.start()] + line + "\n" + t[m.start():]
        else:  # dopo il titolo H1
            m2 = re.search(r"^#\s+.+$", t, re.M)
            if not m2:
                print("no anchor:", slug); continue
            t = t[:m2.end()] + "\n\n" + line + t[m2.end():]
    open(p, "w", encoding="utf-8").write(t)
    changed += 1
    print(f"collegato: {slug}  ({len(raws)} file)")
print("pagine aggiornate:", changed)
