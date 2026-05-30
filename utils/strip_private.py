#!/usr/bin/env python3
"""Strip notes marked `private: true` from the generated search/graph indices.

Runs AFTER hugo-obsidian + lower_case.py and BEFORE `hugo` builds the site.
A private note is still rendered to HTML by Hugo (so StatiCrypt can encrypt it),
but it must not leak through full-text search, the interaction graph, backlinks,
the sitemap, or any list page.

This script:
  1. Scans content/ for notes whose front matter contains `private: true`.
  2. Removes those slugs from assets/indices/contentIndex.json (full-text search).
  3. Removes them (as source AND target) from assets/indices/linkIndex.json (graph).
  4. Writes the private slug list to `.private-pages.txt` at the repo root so the
     CI StatiCrypt step knows which public/<slug>/index.html files to encrypt.

Slugs match hugo-obsidian's convention: leading "/", lowercase, no ".md".
"""
import json
import os
import re

CONTENT_DIR = "content"
LINK_INDEX = "assets/indices/linkIndex.json"
CONTENT_INDEX = "assets/indices/contentIndex.json"
MANIFEST = ".private-pages.txt"

# Matches a `private: true` line inside the first YAML front matter block.
PRIVATE_RE = re.compile(r"^\s*private\s*:\s*true\s*$", re.IGNORECASE | re.MULTILINE)


def has_front_matter_private(text: str) -> bool:
    """True if the note's YAML front matter sets private: true."""
    if not text.startswith("---"):
        return False
    end = text.find("\n---", 3)
    if end == -1:
        return False
    front = text[3:end]
    return bool(PRIVATE_RE.search(front))


def slug_for(path: str) -> str:
    """content/foo-bar.md -> /foo-bar  (lowercase, matches hugo-obsidian keys)."""
    rel = os.path.relpath(path, CONTENT_DIR)
    rel = rel[:-3] if rel.endswith(".md") else rel
    parts = rel.split(os.sep)
    if parts[-1] in ("index", "_index"):
        parts = parts[:-1]
    return "/" + "/".join(parts).lower()


def find_private_slugs() -> set:
    slugs = set()
    for root, _, files in os.walk(CONTENT_DIR):
        for name in files:
            if not name.endswith(".md"):
                continue
            full = os.path.join(root, name)
            with open(full, encoding="utf-8") as f:
                if has_front_matter_private(f.read()):
                    slugs.add(slug_for(full))
    return slugs


def strip_content_index(private: set):
    if not os.path.exists(CONTENT_INDEX):
        return
    with open(CONTENT_INDEX, encoding="utf-8") as f:
        data = json.load(f)
    for slug in private:
        data.pop(slug, None)
    with open(CONTENT_INDEX, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def strip_link_index(private: set):
    if not os.path.exists(LINK_INDEX):
        return
    with open(LINK_INDEX, encoding="utf-8") as f:
        data = json.load(f)

    def clean_list(items):
        return [
            it for it in items
            if it.get("source") not in private and it.get("target") not in private
        ]

    idx = data.get("index", {})
    # index.links / index.backlinks are dicts keyed by slug -> list of edges
    for bucket in ("links", "backlinks"):
        d = idx.get(bucket, {})
        for slug in private:
            d.pop(slug, None)
        for key in list(d):
            d[key] = clean_list(d[key])
    # top-level flat edge array used by the graph
    if isinstance(data.get("links"), list):
        data["links"] = clean_list(data["links"])

    with open(LINK_INDEX, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def main():
    private = find_private_slugs()
    with open(MANIFEST, "w", encoding="utf-8") as f:
        for slug in sorted(private):
            f.write(slug + "\n")
    if not private:
        print("[strip_private] no private notes found")
        return
    strip_content_index(private)
    strip_link_index(private)
    print(f"[strip_private] stripped {len(private)} private page(s) from indices:")
    for s in sorted(private):
        print("  ", s)


if __name__ == "__main__":
    main()
