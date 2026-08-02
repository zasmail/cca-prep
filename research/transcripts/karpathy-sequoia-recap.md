---
title: "Sequoia Ascent 2026 recap"
speaker: Andrej Karpathy
source_url: https://karpathy.bearblog.dev/sequoia-ascent-2026/
retrieved: 2026-07-16
method: webfetch
note: >
  This is a detailed structured SUMMARY, not a verbatim transcript. The
  source page is a copyrighted blog post (an AI-generated summary of a
  fireside chat plus an edited transcript); full-text reproduction is not
  reproduced here per copyright policy. Only a few short quotes (<15 words,
  attributed) are included. For the complete wording, read the original at
  the source URL above.
---

# Sequoia Ascent 2026 — Andrej Karpathy fireside chat (recap)

Published April 30, 2026. Page content is an AI-generated summary followed
by an edited transcript of a fireside chat.

## Key sections / arguments, in order

1. **The December 2025 "agentic inflection."** Around December 2025, coding
   agents crossed a reliability threshold — generated code chunks got
   larger and more trustworthy, and programmers shifted from writing
   individual lines to delegating macro-level tasks.

2. **Software 3.0 framework.** Software 1.0 = explicit human-written code;
   2.0 = learned neural-net weights; 3.0 = the context window becomes "the
   main lever" for directing LLM behavior.

3. **MenuGen case study.** A traditional app needs frontend/API/auth/
   payments infra; a "Software 3.0" version lets a multimodal model render
   images directly onto a menu photo — much of the app logic disappears
   into the model call.

4. **Verifiability framework.** Traditional software automates what can be
   *specified*; LLMs automate what can be *verified*. Tasks with automatic
   reward signals (coding, math, tests) improve fastest.

5. **Jagged intelligence thesis.** Capability = verifiability + how much a
   lab emphasized that domain in training (e.g., a chess-capability spike
   tied to expanded chess data). Founders need to judge whether their task
   is "on the model's rails."

6. **Vibe coding vs. agentic engineering.** Vibe coding raises the
   capability floor for casual users; agentic engineering raises the
   ceiling for professional teams and requires oversight, specs, and
   testing. Example given: a MenuGen payment bug where an agent generated
   plausible-looking but flawed code matching the wrong Stripe/Google
   accounts.

7. **What stays human.** Taste, judgment, and oversight remain
   irreplaceable; humans direct agents rather than write every detail.
   Engineering fundamentals (tensor storage, system boundaries, security)
   still matter.

8. **Hiring and infrastructure.** Traditional coding-puzzle interviews are
   misaligned with agentic-era skills; better interviews have candidates
   build something substantial with agents, then get tested on security.
   Agent-native infra needs CLIs, APIs, MCP servers, structured logs, and
   clear permissioning.

9. **"Animals vs. ghosts" framing** (cross-referenced from Karpathy's own
   essay — see companion file `karpathy-animals-vs-ghosts.md`): LLMs aren't
   creatures with intrinsic motivation, they're statistical simulations
   shaped by training data, which argues for empirical testing over
   anthropomorphizing them.

10. **Opportunity space.** Valuable, verifiable domains not yet saturated by
    frontier labs are startup wedges; fine-tuning/RL can lift a base
    model's performance in a specialized niche.

11. **Education / understanding.** Core framing: agents let you outsource
    thinking but not understanding — understanding remains the bottleneck
    for directing agents well.

## A few short attributed quotes

- "I have never felt more behind as a programmer." — Karpathy
- Models can "refactor a 100,000-line codebase ... yet tells me to walk to
  the car wash" — Karpathy, on jagged capability.

## Limitations of this capture

This file is a structured summary compiled from a single fetch of the
bearblog page. It captures the sequence and substance of the talk's
arguments but does not reproduce the post's full prose. Read the source
directly for the complete transcript and exact wording.
