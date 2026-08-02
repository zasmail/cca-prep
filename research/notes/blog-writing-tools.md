---
title: Writing Effective Tools for Agents — With Agents
speaker: Ken Aizawa (Anthropic), with contributions across Research, MCP, Product Engineering, Marketing, Design, Applied AI
source: https://www.anthropic.com/engineering/writing-tools-for-agents
themes:
  - tool-design-mcp
  - evals
  - context-engineering
  - orchestration
---

## Core Claims

1. Tools for agents require defensive design because agents may misuse, misinterpret, or hallucinate arguments unlike deterministic functions.
2. Effective tool-building is iterative: prototype → evaluate on realistic chained tasks → analyze transcripts and reasoning traces → refine collaboratively with agent feedback.
3. Token efficiency matters more than feature completeness because agents have real context limits unlike software systems with near-unlimited memory.
4. Tool naming (namespacing, prefixes, grouping structure) measurably affects agent performance by shifting cognitive load from reasoning onto tool structure.
5. Semantic identifiers and actionable error messages guide agents toward token-conscious behavior rather than requiring human-readable output alone.
6. Tool descriptions are high-leverage context that materially shape agent behavior and deserve engineering rigor equivalent to prompt engineering.
7. Pagination, filtering, and truncation with sensible defaults prevent redundant tool calls and wasted intermediate output.
8. Agents can debug their own tool usage via reasoning traces and raw transcripts, enabling collaborative improvement workflows.

## Patterns & Frameworks

- **Defensive tool design** — Account for agent misinterpretation; contrast with deterministic software mindset
- **Eval-driven iteration** — Prototype locally, evaluate against realistic multi-step workflows, analyze patterns, refine with agent collaboration
- **Token-conscious responses** — Build in pagination, filtering, truncation with defaults; truncation messages should guide better search strategy, not cut silently
- **Semantic naming** — Use readable names and types (e.g., contact name) over opaque identifiers (UUID, MIME type); reduces agent ambiguity
- **Tool scoping** — Prioritize high-impact workflows; consolidate related actions into fewer well-defined tools; each tool needs distinct purpose
- **Namespace structuring** — Group tools by service or resource with consistent prefixes/suffixes; measurably improves agent disambiguation
- **Response flexibility** — Optional "response format" parameters let agent choose concise vs. detailed output, trading flexibility against context cost

## Numbers & Specifics

- **Optimization targets tracked:** accuracy, runtime, token usage, error rate (each points to different improvement opportunities)
- **Evaluation tasks:** drawn from actual workflows, often require multiple chained tool calls against real data
- **Correctness checking:** ranges from exact string match to Claude-based judge
- **Context limits:** agents have real, measurable context constraints; a contact-list dump wastes more tokens than targeted search
- **High-leverage optimization:** tool descriptions (named among highest-leverage optimizations possible)

## Quotes

1. "A tool is a new kind of contract between the two" [deterministic software and non-deterministic agents]
2. "Good evals use realistic tasks drawn from actual workflows, often requiring several chained tool calls against real data"
3. "Agents have real context limits, unlike near-unlimited machine memory"
4. "Tool descriptions are part of the agent's context and materially shape behavior"
5. "Shift from a deterministic mindset to a non-deterministic one, backed by continuous eval-driven iteration"

## Applied AI Relevance

- **Tool design is systems engineering, not API documentation** — Prototyping, evaluation, and iterative refinement are mandatory; transcripts reveal agent confusion patterns you wouldn't predict.
- **Eval transcripts as debugging infrastructure** — Reasoning traces and raw logs show where agents misread tool specs; metric patterns (e.g., redundant calls) directly suggest missing features.
- **Token efficiency cascades** — Better tool responses (truncation guidance, sensible filtering defaults) reduce wasted intermediate output, freeing context for deeper reasoning in the same budget.
- **Collaborative agent-driven improvement is practical today** — Use Claude Code or similar to have agents review their own eval transcripts and propose tool refinements; this loop informed Anthropic's own tool guidance.
