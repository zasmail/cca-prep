---
title: "Effective Context Engineering for AI Agents"
speaker: "Anthropic Applied AI team (Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield; contributions from Rafi Ayub, Hannah Moran, Cal Rueb, Connor Jennings)"
source_url: "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
retrieved: 2026-07-16
method: webfetch
publication_date: "2025-09-29"
note: >
  Condensed, paraphrased study notes rather than a verbatim reproduction of
  the original article, in line with copyright limits on reproducing full
  third-party text. Structure and key points are captured; wording is not a
  direct copy. Refer to the source URL for exact original text.
---

# Effective Context Engineering for AI Agents

**Author/Team:** Anthropic Applied AI team
**Published:** September 29, 2025

## Section Headings (in order)

1. Effective context engineering for AI agents
2. Context engineering vs. prompt engineering
3. Why context engineering is important to building capable agents
4. The anatomy of effective context
5. Context retrieval and agentic search
6. Context engineering for long-horizon tasks
7. Conclusion

## Notes by section

**Intro — Effective context engineering for AI agents**
Frames "context engineering" as the emerging discipline of optimizing which tokens occupy an LLM's limited context window during inference. Context = the complete set of tokens given to the model; the engineering challenge is maximizing their usefulness within model constraints. Requires "thinking in context" — understanding the whole information landscape available to the model at any moment.

**Context engineering vs. prompt engineering**
Prompt engineering = crafting effective instructions, especially system prompts. Context engineering = the broader, ongoing task of managing everything that fills the context across a multi-turn agent run: system instructions, tools, external data, and message history. Key distinction: context engineering is iterative and repeats every turn, whereas prompt engineering is typically a one-time task. As agents run longer, they accumulate more complex context that needs active curation.

**Why context engineering is important to building capable agents**
Cites research on "context rot": model accuracy degrades as context windows grow, rooted in the transformer's n² pairwise attention over tokens, which strains compute and because models have proportionally less training exposure to very long sequences — a gradual degradation, not a cliff. Core framing: treat context as a finite resource with diminishing marginal returns, analogous to limited human working memory.

**The anatomy of effective context**
Practical guidance per component:
- *System prompts*: use simple, direct language pitched at the right altitude — specific enough to steer behavior, but expressed as flexible heuristics rather than brittle if/then logic.
- *Tools*: should be clearly scoped, avoid functional overlap with each other, and return token-efficient results.
- *Examples (few-shot)*: show a diverse set of canonical cases rather than trying to exhaustively enumerate every edge case.
- Overarching principle: keep context minimal and high-signal.

**Context retrieval and agentic search**
Describes moving from "load everything relevant upfront" to "just-in-time" retrieval, where the agent fetches data during execution via tools and lightweight references (file paths, links, IDs) rather than pre-loaded blobs. Compared to human cognition using external indices instead of memorizing everything. Metadata in these references (folder structure, naming conventions, timestamps) gives the agent extra signal. Trade-off: runtime exploration is slower than precomputed retrieval but supports progressive discovery and less context pollution. A hybrid of some upfront retrieval plus autonomous on-demand exploration is often the sweet spot.

**Context engineering for long-horizon tasks**
Addresses staying coherent across work that exceeds a single context window, via three techniques:
- *Compaction*: summarize the conversation as it nears the window limit, keeping key decisions/bugs and dropping redundant tool output.
- *Structured note-taking*: the agent maintains an external memory file (e.g., a running NOTES.md) so it can stay coherent across a multi-hour task.
- *Sub-agent architectures*: specialized sub-agents handle narrow tasks with their own clean context windows and return condensed summaries to a coordinating agent.
Which to use depends on the task: compaction for long back-and-forth conversations, note-taking for iterative build work, multi-agent for complex research.

**Conclusion**
Core principle: find the smallest set of high-signal tokens that maximizes the chance of the desired outcome. As models improve, some of this can become less prescriptive over time, but context remains a scarce resource that needs deliberate curation for reliable agent behavior.
