---
title: "LLM Wiki gist"
speaker: Andrej Karpathy
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
retrieved: 2026-07-16
method: webfetch
note: >
  This is a detailed structured SUMMARY, not a verbatim reproduction. The
  gist is copyrighted written content; full text (including the extensive
  comment thread) is not reproduced here per copyright policy. Read the
  original at the source URL for exact wording and all 40+ comment-thread
  implementations mentioned.
---

# LLM Wiki — Andrej Karpathy (gist summary)

Created April 4, 2026.

## Core idea

Instead of classic RAG (retrieving raw chunks at query time), have an LLM
agent **incrementally build and maintain a persistent wiki** — a
structured, interlinked set of markdown files — so that synthesis compounds
over time rather than being re-derived on every query.

## Three-layer architecture

1. **Raw sources** — immutable original documents; never modified by the
   LLM.
2. **The wiki** — LLM-generated markdown pages: summaries, entities,
   concepts.
3. **The schema** — a configuration document (e.g. `CLAUDE.md`) that
   defines the wiki's structure and workflows.

## Operations

- **Ingest** — process new sources, update wiki pages, maintain
  cross-references.
- **Query** — search the wiki, synthesize an answer, optionally file the
  result back as a new page.
- **Lint** — health-check the wiki for contradictions, orphan pages, stale
  claims, missing cross-references.

## Supporting files

- `index.md` — a content-oriented catalog with links and summaries.
- `log.md` — a chronological, append-only activity record.

## Optional tooling mentioned

- Search engines (the gist recommends `qmd` for hybrid BM25/vector search).
- Obsidian for IDE-like browsing.
- Marp for slide generation.
- Dataview for dynamic queries.

## Use cases listed

Personal development tracking, research deep-dives, reading companions,
business/team wikis, competitive analysis, hobby documentation.

## Comment thread

The gist attracted an extensive discussion (40+ cited implementations),
including adaptations for code-review verification, infra/ops knowledge,
due-diligence workflows, role-play character knowledge, and offline
personal systems. Not reproduced here — see source for details.

## Short attributed quote

- "The tedious part of maintaining a knowledge base is not the reading or
  the thinking — it's the bookkeeping." — Karpathy

## Limitations of this capture

Structured summary from a single fetch; the comment thread in particular
is only described at a high level, not itemized. Read the source for full
detail.
