---
title: "Effective Context Engineering for AI Agents"
speaker: "Anthropic Applied AI team (Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield)"
source: "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
publication_date: "2025-09-29"
themes:
  - context-engineering
  - tool-design-mcp
  - orchestration
  - enforcement-reliability
  - claude-code-workflows
---

# Context Engineering for AI Agents: Distilled

## Core Claims

1. Context engineering is the discipline of optimizing which tokens occupy an LLM's limited context window during inference to maximize usefulness.
2. Context engineering differs fundamentally from prompt engineering: it is iterative and repeats every turn, not a one-time task.
3. Model accuracy degrades as context windows grow ("context rot"), rooted in transformer n² pairwise attention complexity and limited training exposure to very long sequences.
4. Context should be treated as a finite resource with diminishing marginal returns, analogous to limited human working memory.
5. System prompts must use simple, direct language and express behavior as flexible heuristics rather than brittle if/then logic.
6. Tools should be clearly scoped, avoid functional overlap, and return token-efficient results to prevent context pollution.
7. Moving from "load everything upfront" to "just-in-time" retrieval reduces context noise but increases runtime exploration time.
8. Metadata in file references (paths, naming conventions, timestamps) gives agents extra signal without loading content.
9. Long-horizon tasks exceeding a single context window require one of three approaches: compaction, structured note-taking, or sub-agent architectures.

## Patterns & Frameworks

- **Context Rot** — Predictable accuracy degradation as context window size increases; a gradual slope, not a cliff.
- **Just-in-Time Retrieval** — Agent fetches data during execution via tools and lightweight references rather than preloading blobs.
- **Compaction** — Summarize conversation as it nears window limit, keeping key decisions and bugs, dropping redundant tool output.
- **Structured External Memory** — Agent maintains a running NOTES.md file to maintain coherence across multi-hour tasks.
- **Sub-Agent Architectures** — Specialized agents handle narrow tasks with clean context windows, returning condensed summaries to a coordinator.
- **The Anatomy of Effective Context** — Four components: simple system prompts, clearly scoped tools, diverse few-shot examples, and minimal high-signal tokens.

## Numbers & Specifics

- Transformer attention: **n²** pairwise complexity over tokens.
- Tool design principle: **avoid functional overlap** between tools.
- Long-horizon strategy selection: compaction for long conversations, note-taking for iterative build work, multi-agent for complex research.
- Publication: **September 29, 2025**.

## Quotes

> "Thinking in context" — understanding the whole information landscape available to the model at any moment.

> "Context as a finite resource with diminishing marginal returns, analogous to limited human working memory."

> "Just-in-time retrieval, where the agent fetches data during execution via tools and lightweight references rather than pre-loaded blobs."

> "Keep context minimal and high-signal."

> "Find the smallest set of high-signal tokens that maximizes the chance of the desired outcome."

## Applied AI Relevance

- **Context precision directly correlates with agent reliability.** Systematic curation of tokens beats prompt tuning alone for long-horizon work; treat token budget as a design constraint from day one.

- **Hybrid retrieval (upfront + on-demand) is the sweet spot.** Pre-load only bootstrapping metadata and critical references; let agents pull data just-in-time to support progressive discovery without context pollution.

- **For multi-hour agent tasks, structured external memory outperforms compaction.** Use NOTES.md-style patterns and sub-agent handoffs; single-session context compaction alone degrades as tasks extend.

- **Tool design is a context multiplier.** Token-efficient results, clear scoping, and no functional overlap directly reduce context waste and improve agentic selection reliability.
