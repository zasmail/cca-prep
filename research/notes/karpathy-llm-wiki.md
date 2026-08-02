---
title: "LLM Wiki gist"
speaker: Andrej Karpathy
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
date: 2026-04-04
themes:
  - memory
  - context-engineering
  - orchestration
  - karpathy-mental-models
---

# LLM Wiki — Structured Distillation

## Core claims

1. Persistent agent-maintained wiki compounds synthesis over time, whereas classic RAG re-derives answers by retrieving raw chunks at query time.
2. The wiki is LLM-generated markdown (summaries, entities, concepts), not just retrieved raw documents.
3. Three-layer architecture (immutable sources → LLM-generated wiki → schema config) enables both agent operations and human browsing.
4. Ingest-Query-Lint cycle keeps the wiki consistent: new sources update pages, queries synthesize answers optionally filed as new pages, linting detects contradictions and orphans.
5. Bookkeeping (maintaining cross-references, tracking edits, organizing structure) is the costly part of knowledge management; reading and thinking are not.
6. Index (content-oriented catalog) and log (append-only activity record) are essential supporting artifacts, not optional.
7. The schema (e.g., CLAUDE.md) defines wiki structure and workflows, making the system declaratively auditable.

## Patterns & frameworks

- **Three-layer architecture** — raw sources (immutable), wiki layer (LLM-generated and maintained), schema layer (structural config).
- **Ingest-Query-Lint** — three canonical operations: ingest (process new sources, update wiki), query (search, synthesize, optionally file result), lint (health check for contradictions, orphans, staleness).
- **Append-only log** — chronological activity record enables auditability and replay without mutating historical entries.
- **Content-oriented index** — catalog with links and summaries for human and agent navigation, distinct from full-text search.

## Numbers & specifics

- **Created:** April 4, 2026
- **Comment implementations:** 40+ cited adaptations (code-review verification, infra/ops knowledge, due-diligence, role-play character knowledge, offline personal systems)
- **Recommended search tool:** qmd (hybrid BM25/vector search)
- **Optional IDE/tooling:** Obsidian (browser), Marp (slide generation), Dataview (dynamic queries)
- **Use cases mentioned:** personal development tracking, research deep-dives, reading companions, business/team wikis, competitive analysis, hobby documentation

## Quotes

- "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping." — Karpathy

## Applied AI relevance

- **Knowledge compounding over sessions** — Instead of stateless per-query synthesis, structured wikis let agents refine and cross-link knowledge incrementally, reducing hallucination and improving consistency.
- **Auditability via schema + log** — Declaring structure (CLAUDE.md) and logging all mutations makes agent workflows deterministic and inspectable, critical for production reliability.
- **Tool ecosystem integration** — Search, indexing, and lint operations become standalone tools in an agent's toolkit, enabling multi-step knowledge workflows rather than monolithic RAG.
- **Memory without fine-tuning** — Persistent markdown wiki provides context-window-friendly state management without retraining, fitting Claude's 200K–1M context limits and cached prompt patterns.
