#!/usr/bin/env python3
"""One-off: split docs/test.md (6 articles separated by H1) into Quartz notes.

Each note gets frontmatter (title, lastmod, tags), the leading H1 removed
(Quartz renders the title from frontmatter), and a "Liên quan" section with
wikilinks to related notes. Tags/topics are assigned per article.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "test.md"
OUT = ROOT / "content"

# slug, display title (for wikilinks), tags, related slugs
META = {
    1: dict(
        slug="complexity-ousterhout",
        link="Complexity của Ousterhout",
        tags=["thiết kế phần mềm", "complexity", "A Philosophy of Software Design", "John Ousterhout"],
        lastmod="2026-05-29 10:00:00",
        related=["software-entropy", "tactical-vs-strategic-programming", "the-design-concept"],
    ),
    2: dict(
        slug="software-entropy",
        link="Software Entropy",
        tags=["thiết kế phần mềm", "The Pragmatic Programmer", "nợ kỹ thuật", "chất lượng code"],
        lastmod="2026-05-29 10:10:00",
        related=["complexity-ousterhout", "tactical-vs-strategic-programming"],
    ),
    3: dict(
        slug="no-one-knows-what-they-want",
        link="No one knows what they want",
        tags=["yêu cầu phần mềm", "Agile", "The Pragmatic Programmer", "sản phẩm"],
        lastmod="2026-05-29 10:20:00",
        related=["small-steps-feedback", "the-design-concept"],
    ),
    4: dict(
        slug="the-design-concept",
        link="The Design Concept (Brooks)",
        tags=["thiết kế phần mềm", "tính toàn vẹn khái niệm", "Frederick Brooks", "kiến trúc"],
        lastmod="2026-05-29 10:30:00",
        related=["complexity-ousterhout", "no-one-knows-what-they-want", "tactical-vs-strategic-programming"],
    ),
    5: dict(
        slug="small-steps-feedback",
        link="Bước nhỏ + Feedback loop",
        tags=["feedback loop", "Agile", "TDD", "The Pragmatic Programmer"],
        lastmod="2026-05-29 10:40:00",
        related=["no-one-knows-what-they-want", "tactical-vs-strategic-programming"],
    ),
    6: dict(
        slug="tactical-vs-strategic-programming",
        link="Tactical vs Strategic Programming",
        tags=["thiết kế phần mềm", "nợ kỹ thuật", "A Philosophy of Software Design", "John Ousterhout"],
        lastmod="2026-05-29 10:50:00",
        related=["complexity-ousterhout", "software-entropy", "the-design-concept", "small-steps-feedback"],
    ),
}
# shared topic tag added to every note
COMMON_TAGS = ["lập trình", "triết lý phần mềm"]
LINK_OF = {m["slug"]: m["link"] for m in META.values()}

text = SRC.read_text(encoding="utf-8")
# split on lines that start with a single "# " (H1), keep the heading
parts = re.split(r"(?m)^(?=# [^#])", text)
parts = [p.strip() for p in parts if p.strip()]
assert len(parts) == 6, f"expected 6 articles, got {len(parts)}"

OUT.mkdir(exist_ok=True)
for i, body in enumerate(parts, start=1):
    m = META[i]
    lines = body.split("\n")
    title = lines[0].lstrip("# ").strip()
    rest = "\n".join(lines[1:]).strip()

    tags = COMMON_TAGS + m["tags"]
    assert "'" not in title, f"title has apostrophe, adjust quoting: {title}"
    fm = ["---", f"title: '{title}'", f"lastmod: '{m['lastmod']}'", "tags:"]
    fm += [f"  - {t}" for t in tags]
    fm.append("---")

    related = "\n".join(
        f"- [[{s}|{LINK_OF[s]}]]" for s in m["related"]
    )
    note = "\n".join(fm) + "\n\n" + rest + "\n\n---\n## Liên quan\n" + related + "\n"
    (OUT / f"{m['slug']}.md").write_text(note, encoding="utf-8")
    print(f"wrote content/{m['slug']}.md  ({len(rest)} chars)")
print("done")
