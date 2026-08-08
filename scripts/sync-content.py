#!/usr/bin/env python3
"""
Sincronizza le pagine del wiki sorgente (Obsidian) in content/ per Quartz.

Trasformazioni applicate SOLO alla copia pubblicata (il wiki sorgente resta intatto):
  1. rimuove l'H1 iniziale duplicato (Quartz mostra già il titolo dal frontmatter)
  2. converte i wikilink senza alias [[tipo/slug]] -> [[tipo/slug|Titolo leggibile]]

Uso:  python3 scripts/sync-content.py [--no-copy]
"""
import os, re, sys, shutil, glob

SRC = "/Users/antonioscaramuzzino/Library/CloudStorage/GoogleDrive-a.scaramuzzino@gmail.com/Il mio Drive/Brain/LLM-Wiki/LLM-Wiki/wiki"
DST = "/Users/antonioscaramuzzino/wiki-ia-scuola/content"

# Il wiki sorgente (Obsidian, su Drive) è la FONTE UNICA: tutto nasce lì e viene
# copiato qui con gli stessi nomi, così i wikilink [[concept/...]] funzionano
# identici in Obsidian e sul sito.
FOLDERS = {c: c for c in ("concept", "entity", "source", "analyses", "news", "social")}
ROOT_FILES = ("index.md", "overview.md", "crediti.md")

def copy_from_source():
    for src_dir, dst_dir in FOLDERS.items():
        s, d = os.path.join(SRC, src_dir), os.path.join(DST, dst_dir)
        if not os.path.isdir(s):
            continue
        os.makedirs(d, exist_ok=True)
        for f in glob.glob(os.path.join(s, "*.md")):
            shutil.copy2(f, os.path.join(d, os.path.basename(f)))
    for f in ROOT_FILES:
        p = os.path.join(SRC, f)
        if os.path.exists(p):
            shutil.copy2(p, os.path.join(DST, f))

def title_of(path):
    head = open(path, encoding="utf-8").read(800)
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', head, re.M)
    return m.group(1).strip() if m else None

def build_titles():
    titles = {}
    for f in glob.glob(os.path.join(DST, "**", "*.md"), recursive=True):
        rel = os.path.relpath(f, DST).replace(os.sep, "/")[:-3]  # senza .md
        t = title_of(f)
        if t and not rel.endswith("/index"):
            titles[rel] = t
    return titles

def strip_leading_h1(text):
    parts = text.split("---", 2)
    if len(parts) < 3 or parts[0].strip():
        return text
    fm, body = parts[1], parts[2]
    body = re.sub(r"\A\s*\n#\s+.+?\n", "\n", body, count=1)
    return "---" + fm + "---" + body

def alias_wikilinks(text, titles):
    def repl(m):
        target = m.group(1).strip()
        if "|" in target or "/" not in target:
            return m.group(0)
        base = target.split("#")[0]
        t = titles.get(base)
        return f"[[{target}|{t}]]" if t else m.group(0)
    return re.sub(r"\[\[([^\]]+)\]\]", repl, text)

def main():
    if "--no-copy" not in sys.argv:
        copy_from_source()
        print("copiate le pagine dal wiki sorgente")
    titles = build_titles()
    print(f"titoli mappati: {len(titles)}")
    changed = 0
    for f in glob.glob(os.path.join(DST, "**", "*.md"), recursive=True):
        orig = open(f, encoding="utf-8").read()
        new = alias_wikilinks(strip_leading_h1(orig), titles)
        if new != orig:
            open(f, "w", encoding="utf-8").write(new)
            changed += 1
    print(f"file trasformati: {changed}")

if __name__ == "__main__":
    main()
