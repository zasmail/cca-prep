---
title: Sequoia Ascent 2026 — Andrej Karpathy fireside chat
speaker: Andrej Karpathy
source: https://karpathy.bearblog.dev/sequoia-ascent-2026/
published: 2026-04-30
themes:
  - karpathy-mental-models
  - model-fundamentals
  - context-engineering
  - enforcement-reliability
  - orchestration
  - tool-design-mcp
  - evals
---

## Core Claims

1. December 2025 marked an "agentic inflection" where LLM-generated code chunks crossed a reliability threshold, enabling programmer delegation of macro-level tasks.
2. Software 3.0 makes the context window "the main lever" for directing LLM behavior, replacing explicit human-written code (1.0) and learned weights (2.0).
3. LLMs automate what can be *verified*, not merely what can be *specified*—a fundamental shift from traditional software engineering.
4. Capability = verifiability + training emphasis: jagged intelligence means a model can refactor 100k lines yet fail at simple commonsense tasks.
5. Vibe coding raises the capability floor for casual users; agentic engineering raises the ceiling for teams and requires oversight, specs, and testing.
6. Taste, judgment, and oversight remain irreplaceably human; agents execute directives but don't replace understanding.
7. Agent-native infrastructure must include CLIs, APIs, MCP servers, structured logs, and clear permissioning.
8. Agents outsource thinking but not understanding—understanding remains the bottleneck for directing agents well.
9. Traditional coding-puzzle interviews are misaligned; evaluate agentic skills via supervised builds with security testing.
10. Verifiable, unsaturated domains are startup wedges where fine-tuning and RL can specialize base models.

## Patterns & Frameworks

- **Software 3.0 framework**: Context window as primary control surface for model behavior.
- **Verifiability framework**: Partition tasks by automatic reward signals (coding, math, tests improve fastest).
- **Jagged intelligence thesis**: Performance is discontinuous; check whether the task sits "on the model's rails."
- **Vibe coding vs. agentic engineering**: Floor-raiser (accessibility) vs. ceiling-raiser (professional oversight).
- **MenuGen case study**: App logic (frontend, auth, payments) dissolves into a multimodal model call rendering directly on images.
- **Animals vs. ghosts**: LLMs are statistical simulations, not creatures with intrinsic agency—favors empirical testing over anthropomorphism.

## Numbers & Specifics

- **Inflection date**: December 2025
- **Code refactoring scale**: 100,000-line codebase
- **Bug example**: MenuGen payment: agent generated syntactically correct but semantically flawed code mismatching Stripe/Google accounts
- **Publication**: April 30, 2026 (Sequoia blog)
- **Training emphasis effect**: Capability spikes in domains with expanded training data (e.g., chess)

## Quotes

- "I have never felt more behind as a programmer." — Karpathy, on the pace of agentic shift.
- Models can "refactor a 100,000-line codebase ... yet tells me to walk to the car wash" — Karpathy, on jagged capability.
- Context window becomes "the main lever" for directing behavior.
- LLMs automate what can be "verified" (vs. specified).
- "Taste, judgment, and oversight remain irreplaceable."

## Applied AI Relevance for Anthropic Engineers

- **Oversight > hype**: Agentic engineering is not vibe coding; it demands security testing, clearspec, and permissioning. Hooks, not prompts, enforce guardrails.
- **Verifiability is the metric**: Prioritize tasks with automatic reward signals (test passage, math correctness, compilability). Fine-tuning and RL compound verifiable wins.
- **Infrastructure is load-bearing**: CLIs, APIs, MCP servers, structured logs, and permissioning design are not nice-to-have; they are prerequisites for multi-agent systems.
- **Task-model fit matters**: Before deploying an agent, diagnose whether the task sits on the model's strong rails (verifiable + training-emphasized). Misalignment is the MenuGen trap.
