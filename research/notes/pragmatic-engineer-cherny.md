---
title: "Building Claude Code with Boris Cherny"
speaker: "Boris Cherny (Head of Claude Code, Anthropic)"
source: https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny
themes:
  - context-engineering
  - tool-design-mcp
  - orchestration
  - enforcement-reliability
  - claude-code-workflows
  - gtm-applications
---

# Building Claude Code: Distillation

## Core Claims

1. Clean, consistently-migrated codebases produce double-digit productivity gains when paired with AI agents; partially-migrated codebases confuse both models and humans alike.
2. Simple model-driven search (glob/grep) outperforms RAG pipelines with embeddings for codebase navigation.
3. Repetitive code-review feedback patterns scale better when automated as lint rules than handled case-by-case.
4. Safety guardrails and destructive-operation protections are foundational infrastructure, not feature polish.
5. Working prototypes have replaced traditional PRDs as the primary alignment artifact on the Claude Code team.
6. Context-switching across multiple parallel agent workstreams is becoming the core engineering skill.
7. Infrastructure and platform-level fixes have higher leverage than shipping surface-level features.
8. AI tooling will expand engineer capabilities and reach rather than displace the profession.

## Patterns & Frameworks

- **Automation Precedent** — Identify repetitive human feedback patterns and encode them as automatable rules (Meta lint → Claude Code automation).
- **Codebase Quality Compounding** — Consistent code migration and cleanliness directly multiplies model reliability and agent task success.
- **Search-not-RAG** — Model-driven glob/grep operations suffice for codebase navigation; embeddings add complexity without commensurate benefit.
- **Infrastructure Leverage** — Platform-level fixes (guardrails, classifiers, safety) outweigh incremental surface features in total impact.
- **Prototype-First Alignment** — Demonstrate behavior through working code rather than written specification to align teams faster.

## Numbers & Specifics

- **20–30 pull requests/day** — Boris's personal velocity running ~5 parallel Claude Code instances simultaneously.
- **~10 days** — Build time for Claude Cowork, with safety and guardrails prioritized for non-technical user base.
- **Double-digit productivity gains** — Typical multiplier observed in clean vs. partially-migrated codebases.
- **Flat org structure** — Anthropic uses uniform "Member of Technical Staff" title across product, design, and infrastructure roles.

## Quotes

*Note: Source is a paraphrased summary; direct quotes from full audio/video may vary slightly.*

- "Personal productivity at scale" — 20–30 PRs/day via parallel agent instances, not serial depth.
- "Codebase quality compounds" — Clean migrations enable double-digit leverage; partial migrations confuse both humans and models.
- "Search over RAG" — Simple glob/grep beats embedding pipelines for code navigation.
- "Context-switching as the new engineering skill" — High-leverage work is managing multiple parallel workstreams, not single-threaded depth.
- "Printing-press analogy" — Scribes became authors; engineers will expand their reach rather than be displaced by AI.

## Applied AI Relevance

1. **Codebase structure is a reliability lever** — When deploying agents at scale, codebase cleanliness and consistency matter as much as prompt engineering. Invest in migration quality upstream.

2. **Search design > embedding sophistication** — For code navigation and context retrieval, model-driven search patterns (glob, grep, AST-based filtering) outperform complexity. Resist RAG temptation.

3. **Safety guardrails are foundational** — Destructive-operation protection, classifiers, and safety checks are infrastructure, not polish. Build them early, before shipping multi-agent systems to non-technical users.

4. **Automation in patterns, not one-offs** — Recurring feedback/issues should be encoded as automatable rules (lint, hooks, validators) rather than handled case-by-case. Scales your team's expertise.

5. **Orchestration skill** — High-leverage engineers manage multiple parallel agent workflows in parallel. Build mental models and tools for parallel execution and context-switching, not just single-threaded depth.

---

*Distilled from Pragmatic Engineer interview, March 4, 2026 | Length: 585 words*
