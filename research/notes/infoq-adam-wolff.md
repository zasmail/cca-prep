---
title: "Engineering at AI Speed: Lessons from the First Agentically Accelerated Software Project"
speaker: "Adam Wolff"
source: "https://www.infoq.com/presentations/engineering-ai/"
event: "QCon San Francisco 2025"
themes:
  - claude-code-workflows
  - gtm-applications
  - karpathy-mental-models
---

# InfoQ: Engineering at AI Speed — Adam Wolff

## Core Claims

1. When AI eliminates implementation as a bottleneck, architectural decision-making becomes the primary constraint on shipping speed.
2. Rapid iteration loops grounded in real user behavior outcompete extended upfront design phases as implementation cost approaches zero.
3. Complexity and requirements reveal themselves through experimentation ("poking"), not pre-specification.
4. Traditional waterfall design docs become economically obsolete when the cost of rewriting code approaches zero.
5. The feedback loop—not the code volume—becomes the only competitive advantage in AI-accelerated development.
6. Transient, parallel execution patterns emerge only after you start building; pre-design misses them.
7. Sunk cost recognition becomes a critical skill: knowing when to abandon approaches (e.g., SQLite persistence after 2 weeks) is as valuable as shipping.

## Patterns & Frameworks

| Pattern | Definition |
|---------|-----------|
| **Discovery-by-building** | Complexity surfaces incrementally during implementation; skip it in pre-design. |
| **Cost inversion** | When code cost → 0, management burden shifts from implementation to iteration velocity & feedback loops. |
| **Transient architecture** | Persistent resources (shared shells, stateful processes) are design anti-patterns; prefer stateless, per-command execution. |
| **Sunk-cost cut** | Regular re-evaluation of experiment viability prevents commitment to dead approaches. |

## Numbers & Specifics

- **Talk duration:** 51 minutes 21 seconds
- **Event:** QCon San Francisco 2025
- **SQLite persistence experiment:** ~2 weeks before abandonment
- **Three case studies:** Terminal cursor/Unicode handling, shell implementation refactor, SQLite persistence trial

## Quotes

1. "the speed of learning becomes the only competitive advantage"
2. "you discover the requirements by poking at them" rather than by specifying them fully in advance
3. "when the implementation cost goes to zero, the feedback loop becomes everything"
4. Unicode-related edge cases in terminal handling required "ongoing refactoring"
5. Initial persistent shell design had to be replaced with "transient, per-command shells to support parallel execution"

## Applied AI Relevance

- **Architectural thinking over coding speed:** Anthropic Applied AI engineers must shift from "how fast can we write code?" to "what is the fastest feedback cycle?" Upfront architecture debates are sunk time when iteration cost is near-zero.
- **Real user behavior drives design:** Solo design docs are replaced by small-batch user testing and rapid iteration cycles; organizations that embrace this win.
- **Complexity discovery is iterative:** Build for the simplest case first (persistent shell), then refactor when real constraints surface (parallelism, transience). Front-loading complexity analysis is waste.
- **Sunk cost discipline is core skill:** Recognizing when a promising experiment (SQLite, native deps) isn't working and cutting losses requires a different mental model than traditional software delivery; teach it explicitly.

---
**Word count:** 280 | **Last updated:** 2026-07-16
