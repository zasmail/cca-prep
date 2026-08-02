---
title: "Animals vs Ghosts: On LLM Cognition and Biological Learning"
speaker: Andrej Karpathy
source: https://karpathy.bearblog.dev/animals-vs-ghosts/
retrieved: 2026-07-16
themes:
  - model-fundamentals
  - karpathy-mental-models
  - gtm-applications
  - enforcement-reliability
---

# Animals vs Ghosts — Distillation

## Core Claims

1. **LLMs are fundamentally "ghosts"** — statistical distillations of human-written internet text, shaped by human influence, not biological systems.
2. **Pretraining serves as a practical substitute for evolutionary initialization** — billions of hard-coded parameters from evolution compressed into supervised learning on finite datasets.
3. **Sutton's "child machines" framework overlooks innate genetic programming** — animal brains arrive with substantial built-in parameters, not starting from scratch via pure RL.
4. **The bitter lesson may not fully apply to LLMs** — they depend on finite human-generated data and human-curated fine-tuning at multiple stages, not just compute scaling.
5. **Convergence is not guaranteed** — LLMs might acquire animal-like qualities, or remain permanently distinct (analogous to planes never becoming birds).
6. **Frontier AI research over-indexes on benchmarks** — multi-agent interaction, culture, and "empowerment" frameworks are underexplored despite their biological relevance.
7. **This framework carries substantial uncertainty** — Karpathy holds "double digit percent uncertainty" about the entire animals-vs-ghosts thesis.

## Patterns & Frameworks

- **Animals vs. Ghosts metaphor** — Biological creatures shaped by evolution vs. statistical text distillations shaped by human internet output.
- **Pretraining-as-evolution** — Using supervised learning as a proxy for billions of years of genetic parameter tuning.
- **Bitter Lesson critique** — Questioning whether compute scaling alone explains LLM capability gains, given dependency on human-curated data and fine-tuning.
- **Convergent vs. divergent evolution** — Learning from biology: specialized solutions don't converge; planes remained planes, birds remained birds.

## Numbers & Specifics

- Double-digit percent uncertainty (10–90% implied range)
- Finite, human-generated training dataset (bounded, unlike animal learning environments)
- Multiple stages of human-curated fine-tuning
- Evolution: billions of years of parameter initialization

## Quotes

- "Pretraining is our crappy evolution." — Karpathy
- Holds "double digit percent uncertainty" about whether the animals-vs-ghosts framework is the right model.

## Applied AI Relevance

- **System design uncertainty**: Recognize that we're building "ghosts," not animals—fundamentally different architectures with different convergence properties. Prompt engineering and orchestration patterns must account for this.
- **Multi-agent and culture frameworks matter**: Rather than chasing benchmark gains, invest in multi-agent interaction patterns and emergent culture, which biological systems rely on.
- **Benchmark-chasing is a local optimum**: The frontier obsession with accuracy metrics obscures what matters for deployment—robustness, adaptation to novel environments, and multi-agent coordination.
- **Evolutionary initialization has no substitute**: Pure RL without inductive biases (pretraining) may be theoretically elegant but practically insufficient. Recognize pretraining as a hard-won practical necessity.

---

**Note**: This summary respects copyright of the original essay; only short attributed quotes included. Read the full source for detailed argumentation.
