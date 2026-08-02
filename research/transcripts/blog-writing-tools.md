---
title: "Writing Effective Tools for Agents — With Agents"
speaker: "Ken Aizawa, with contributions from colleagues across Research, MCP, Product Engineering, Marketing, Design, and Applied AI (Anthropic)"
source_url: "https://www.anthropic.com/engineering/writing-tools-for-agents"
retrieved: 2026-07-16
method: webfetch
publication_date: "2025-09-11"
note: >
  Condensed, paraphrased study notes rather than a verbatim reproduction of
  the original article, in line with copyright limits on reproducing full
  third-party text. Structure and key points are captured; wording is not a
  direct copy. Refer to the source URL for exact original text. URL resolved
  without needing a separate search (page loaded directly at the given slug).
---

# Writing Effective Tools for Agents — With Agents

**Author/Team:** Ken Aizawa (Anthropic), with cross-functional contributors
**Published:** September 11, 2025

## Section Headings (in order)

1. Writing effective tools for agents — with agents
2. What is a tool?
3. How to write tools
   - Building a prototype
   - Running an evaluation
   - Analyzing results
   - Collaborating with agents
4. Principles for writing effective tools
   - Choosing the right tools for agents
   - Namespacing your tools
   - Returning meaningful context from your tools
   - Optimizing tool responses for token efficiency
   - Prompt-engineering your tool descriptions
5. Looking ahead

## Notes by section

**What is a tool?**
Contrasts deterministic software (same input → same output every time) with non-deterministic agents (varying responses). A "tool" is a new kind of contract between the two. Unlike a normal function call, an agent-facing tool must be designed defensively because the agent may misread it, hallucinate arguments, or simply not use it well. Goal: build intuitive tools that widen the range of problems an agent can solve.

**Building a prototype**
Build a working version before formal evaluation. Pull in existing library/API docs to help the agent understand dependencies. Test locally (e.g., via an MCP server or desktop extension) to get hands-on signal before wider rollout, since direct usage surfaces usability issues fast.

**Running an evaluation**
Good evals use realistic tasks drawn from actual workflows, often requiring several chained tool calls against real data. Each task needs a way to check correctness — anything from exact string match to a Claude-based judge. Track more than accuracy: runtime, token usage, and error rate all point to different optimization opportunities and reveal common agent behavior patterns.

**Analyzing results**
Agents can help debug their own tool usage. Reading reasoning/thinking traces surfaces where the agent got confused; reading raw transcripts catches issues you wouldn't have thought to look for. Metric patterns suggest fixes — e.g., repeated redundant calls hint at a missing pagination mechanism, frequent bad parameters hint at unclear descriptions.

**Collaborating with agents**
Developers can use an agent (e.g., Claude Code) to review eval transcripts and iteratively suggest/apply tool improvements — this collaborative loop informed much of the article's guidance.

**Choosing the right tools for agents**
More tools isn't better — agents have real context limits, unlike near-unlimited machine memory. A tool that dumps an entire contact list wastes tokens compared to one that supports targeted search. Prioritize high-impact workflows, consolidate related actions into fewer well-scoped tools, and make sure each tool has a clearly distinct purpose — this reduces agent confusion and wasted intermediate output.

**Namespacing your tools**
Grouping tools under consistent prefixes (by service or by resource) helps the agent tell similar/overlapping tools apart. Prefix vs. suffix naming choices show up as measurable differences in eval performance. Clear naming reduces ambiguity and shifts cognitive load from the agent's reasoning onto the tool's own structure.

**Returning meaningful context**
Favor relevance over maximal flexibility in responses. Use semantic identifiers (names, readable types) instead of opaque ones (UUIDs, MIME types) so the agent can act with more precision. Optional "response format" parameters let the agent choose concise vs. detailed output, trading flexibility against context cost.

**Optimizing tool responses for token efficiency**
Build in pagination, filtering, and truncation with sensible defaults. Truncation messages should actively guide the agent toward a better search strategy rather than just cutting output silently. Error messages should be actionable, not opaque codes — this nudges agents toward more token-conscious usage overall.

**Prompt-engineering tool descriptions**
Tool descriptions are part of the agent's context and materially shape behavior. Clear, unambiguous parameter names, explicit shared context, and precise specs meaningfully improve performance — described as one of the highest-leverage things you can optimize.

**Looking ahead**
As agents get more capable, tool-building practice needs to shift from a deterministic mindset to a non-deterministic one, backed by continuous eval-driven iteration so tools keep pace with the agents using them.
