# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Working conventions for Claude (read first)

- **User:** Nam, called **Jim**. Tech lead of the Learning team @ Prep Edu (recently
  promoted). Backend dev, ~5 yrs PHP, now using AI to vibe-code Golang (newer to Go).
  Prefers concise, direct responses. Full profile: `.claude-work/memory/user-profile.md`.
- **Private work area:** All of Claude's own outputs, memory, and notes live in
  `.claude-work/` (gitignored — never pushed to GitHub or published). See
  `.claude-work/README.md`. Persistent facts go in `.claude-work/memory/`.
- **`content/` is read-only context:** It's the published second-brain notes — Claude
  reads it to understand what Jim is working on, but does NOT write working files there.

## Repository Overview

This is a public second brain website built with Hugo and the Quartz theme (v3). It automatically publishes Obsidian notes tagged with `#publish` from a private vault to a public website hosted at ssp.sh/brain.

## Architecture

- **Hugo Static Site**: Uses Hugo with Quartz theme for generating the public website
- **Content Processing**: Two utility systems process Obsidian notes:
  - Python scripts (`utils/find-publish-notes.py`) - legacy approach
  - Rust utility (`utils/obsidian-quartz/`) - current preferred approach
- **Link Generation**: Uses `hugo-obsidian` (forked version) to generate backlinks and graph connections
- **Deployment**: Static files generated to `public/` and uploaded via rsync

## Core Commands

### Development and Building
```bash
# Start development server (full build + serve)
make serve

# Run Hugo development server only
make run

# Generate static site without serving
make hugo-generate

# Full deployment (build + upload)
make deploy
```

### Content Processing
```bash
# Process notes using Rust utility (preferred)
make prepare

# Process notes using Python scripts (legacy)
make prepare-python
```

### Deployment
```bash
# Upload to server
make upload

# Quick upload without full rebuild
make upload-only
```

## Required Environment Variables

The content processing requires these environment variables:
- `secondbrain`: Path to private Obsidian vault
- `public_secondbrain`: Path to public content folder

## Key Dependencies

- **Hugo**: Static site generator (`/usr/bin/hugo`)
- **hugo-obsidian**: Backlink generator (`/home/sspaeti/.go/bin/hugo-obsidian`)
- **obsidian-quartz**: Rust utility for content processing (built from `utils/obsidian-quartz/`)
- **Python dependencies**: For legacy scripts (pandoc, frontmatter)

## Content Processing Workflow

1. Notes tagged with `#publish` are identified in the private Obsidian vault
2. Content is processed to:
   - Convert first header to frontmatter
   - Generate social media preview images
   - Copy referenced images
   - Convert filenames to lowercase
3. Hugo generates static site with backlinks and graph visualization
4. Site is deployed via rsync to `sspaeti@sspaeti.com:~/www/ssp/brain`

## Important Notes

- The `hugo-obsidian` tool is a custom fork: https://github.com/sspaeti/hugo-obsidian
- Configuration prevents aliases for multi-word titles to avoid conflicts
- Link indexes are converted to lowercase for proper Hugo compatibility
- Git info is enabled for last modified dates

## Private content (StatiCrypt password gate)

Notes can be published behind a **single shared password** (no user accounts). The repo
stays **public** (GitHub Free can't serve Pages from a private repo), so the source `.md`
of a private note is still readable on GitHub — this gate only protects the *rendered*
page on the live site. Use it for "hide from casual public", not for true secrets.

**To mark a note private**, add to its front matter:
```yaml
private: true
build:
  list: never      # keep out of section/home lists & taxonomies
  render: always   # still render HTML so it can be encrypted
```

**Build pipeline** (in `.github/workflows/deploy.yaml`): `hugo-obsidian` → `lower_case.py`
→ `strip_private.py` → `hugo` → StatiCrypt encrypt.
- `utils/strip_private.py` scans `content/` for `private: true`, removes those slugs from
  `contentIndex.json` (search) and `linkIndex.json` (graph/backlinks), and writes
  `.private-pages.txt`. So private notes never leak through search, graph, or backlinks.
  Hugo's `build.list: never` keeps them out of list pages and the sitemap.
- The CI "Encrypt private pages" step runs `npx staticrypt` on each `public/<slug>/index.html`
  from the manifest, using a fixed salt (`8d74bb7e23de07b2756a973b239b81f0`) and the repo
  secret **`STATICRYPT_PASSWORD`**. If the secret is unset while private pages exist, the
  build **fails on purpose** (never ships unencrypted).

**Local preview:** `make prepare-local` (or `make serve-local`) rebuilds indices with the
strip step but does NOT encrypt — private notes render in full so you can preview them.

## Design System (Claude / Anthropic)

The visual design follows **`DESIGN.md`** (repo root) — the authoritative Anthropic/Claude
theme spec. When touching any HTML/CSS, conform to it. Core idea: the trinity of a tinted
**cream** canvas + **coral** accent + dark **navy** surfaces. Pure white and cool grays/blues
are off-brand.

**Where tokens live:** `assets/styles/custom.scss` `:root` maps DESIGN.md tokens onto the
theme's variables (light/cream) and `[saved-theme="dark"]` maps the dark-navy mode. The full
token set is also exposed as `--c-*` (colors) and `--r-*` (radius) custom properties — **use
those for new components; never inline hex.**

**Color mapping (theme var ← DESIGN token):**
- `--light` ← canvas `#faf9f5` · `--dark` ← ink `#141413` · `--gray` ← body `#3d3d3a`
- `--primary`/`--secondary` ← coral `#cc785c` · `--tertiary` ← coral-active `#a9583e`
- `--lightgray` ← surface-card `#efe9de` · `--outlinegray` ← hairline `#e6dfd8`
- Dark mode: `--light` ← surface-dark `#181715`, `--dark` ← on-dark `#faf9f5`, coral unchanged.

**Typography (`assets/styles/base.scss`):**
- Display/headings: **Cormorant Garamond** (Copernicus/Tiempos substitute), weight 600,
  `letter-spacing: -0.02em`. Never bold-700. `Source Serif 4` is the fallback for full
  Vietnamese diacritic coverage.
- Body/UI: **Inter** (StyreneB substitute), 400 text / 500 labels.
- Code: **JetBrains Mono**.

**Rules (from DESIGN.md Do/Don't):**
- Coral is scarce on individual elements, generous only on full-bleed coral callout cards.
- Border radius is hierarchical: `--r-md` 8px (buttons/inputs), `--r-lg` 12px (cards),
  `--r-pill` (badges/tags).
- Color-block first, shadows rare; depth comes from cream-vs-dark surface contrast.
- Don't introduce a fourth surface tone (no purple/green sections).

**Content/UI language is Vietnamese:** `i18n/en.toml` strings, `date-fmt.html` (`dd/MM/yyyy`),
and `popover.js` (`vi-VN` locale) are localized. Keep new UI text in Vietnamese.

**Tagging convention (controlled vocabulary):** 2–3 tags per note; every tag must group ≥2
notes (avoid one-off tags and umbrella tags that sit on every note); reuse existing tag
phrases rather than inventing synonyms. Tags render as DESIGN.md `badge-pill`s.

**Rich content:** Mermaid code-blocks render as diagrams (`render-codeblock-mermaid.html`).
Raw HTML/SVG/`<canvas>`+`<script>` can be embedded directly in notes (goldmark `unsafe=true`)
for Artifacts-style interactive visuals — keep the whole block free of blank lines so goldmark
treats it as one HTML block.