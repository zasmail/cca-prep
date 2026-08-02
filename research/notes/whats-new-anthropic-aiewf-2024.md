---
title: What's New from Anthropic (AIEWF 2024)
speaker: Alex Albert
source: https://www.youtube.com/watch?v=EuC1GWhQdKE
themes:
  - model-fundamentals
  - tool-design-mcp
  - gtm-applications
  - claude-code-workflows
  - enforcement-reliability
  - evals
  - karpathy-mental-models
---

## Core Claims

1. **Paradigm trap**: Developers are currently bolting AI onto existing products (the "magic star icon" phase) instead of redesigning workflows from ground-up with LLM capabilities as the foundation.
2. **3.5 Sonnet as new default**: Claude 3.5 Sonnet outperforms Claude 3 Opus across benchmarks (MML, human eval, GPT-4 Tool Use) despite being the middle-tier model, not the flagship.
3. **Pull request evals as primary metric**: 3.5 Sonnet scores 64% on PR evaluations (multi-step, iterative code tasks) vs. 38% for Opus—reflects real-world reasoning chains better than academic benchmarks.
4. **Vision as unlock**: Near-perfect OCR and table transcription capabilities open new use cases; model handles complex visual grounding that felt out of reach before.
5. **Content-output separation matters**: Artifacts feature (content divorced from chat) enables collaborative iteration on generated code, documents, and SVGs—crucial for ground-up redesign.
6. **Context grounding via Projects**: Grounding model outputs in user code repos, style guides, and documentation eliminates hallucinations and improves product fit.
7. **Tool use at scale**: Tool use API enables hundreds of tools + structured JSON output, turning Claude into reliable, deterministic workflow engine.
8. **Feature steering for control**: Interpretability research (monosemanticity) allows clamping individual model features, enabling steering API to control outputs beyond prompting alone.
9. **Rapid iteration cycle**: New model tiers (Haiku, Opus 3.5) shipping in months, not years—product teams must design with model improvement as assumption, not hope.
10. **10x pricing advantage**: 3.5 Sonnet at $3/$15 (input/output) = 5x cheaper than Opus, enabling new business models (higher tool density, more complex workflows per request).

## Patterns & Frameworks

**Paradigm mismatch → Innovation gap**: Factories replacing steam with electric didn't improve productivity until redesigned for electricity; mobile just shrinking websites failed until native design—LLM integration mirrors same pattern, waiting for ground-up redesign.

**Eval hierarchy**: Academic benchmarks (MML, human eval) < pull request evaluations (multi-step tasks) < production metrics. PR evals capture iterative reasoning, closer to real agent loops.

**Context as reliability**: Grounding outputs in user knowledge (Projects) replaces prompting for consistency. Reduces hallucination surface.

**Interpretability → Agency**: Feature steering flips interpretability from passive observation (why did it say that?) to active control (turn X down, Y up). Shifts model from black box to tunable system.

## Numbers & Specifics

- **3.5 Sonnet PR eval score**: 64% (vs. 38% Claude 3 Opus)
- **Context window**: 200k tokens
- **Pricing**: $3/M input, $15/M output
- **Cost multiple**: 5x cheaper than Opus
- **Available on**: Anthropic API, AWS Bedrock, Vertex AI
- **Vision improvements**: "Basically replicated it perfectly" on table transcription; OCR now treats these as "Breeze"
- **Artifacts feature**: Hidden for 18+ months, now surfaced as core product
- **Build with Claude contest**: 10K API credits to top 3 projects, running until July 10
- **Feature steering**: Beta-tested with Golden Gate Bridge feature tuning; steering API coming soon to more developers

## Quotes

1. "Despite electricity's obvious superiority, it didn't immediately improve manufacturing productivity—because factory owners tried to replace their old technology with this new technology into an outdated paradigm."

2. "Just as factories went through their 'replace steam engines with electric' phase and tech companies went through their 'just hire a couple mobile web devs' phase, we're now in our 'magic star icon' phase with respect to AI."

3. "Claude 3.5 Sonnet is only the middle model and yet it is better than our last best model, Claude 3 Opus. In my opinion, Claude 3.5 Sonnet is one of the best models in the world right now."

4. "One of the best methods we found for measuring more complicated chains of reasoning is pull requests—they have a defined task, usually take a few steps to solve, and the model is able to iteratively write and test its way to a solution."

5. "Models will become smarter, cheaper, and faster in orders of months not years. When you're planning your product roadmap, be ambitious enough to build with the belief that new models may arrive during your development period."

## Applied AI Relevance

- **Redesign, don't retrofit**: Treat artifacts + projects as foundational product patterns (collaborative document editing, contextual grounding) instead of Claude integrations bolted onto existing UX.
- **Tool use scales complexity**: Hundreds of tools + structured output = predictable, deterministic agent loops; enables building stateful workflows impossible with prompting alone.
- **Eval methodology matters**: Use pull request-style multi-step tasks for internal evals. Academic benchmarks miss real-world reasoning chains (iterative debugging, incremental refinement).
- **Cost enables new patterns**: 5x price drop + instant iteration (Haiku, faster latencies) unlocks dense tool calling, batch processing, and per-user model instances in enterprise workflows.
