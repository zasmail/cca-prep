---
title: Karpathy X canon — Three posts (Agentic engineering, LLM OS, Anthropic)
speaker: Andrej Karpathy
source: https://x.com/karpathy/status/2026731645169185220; https://x.com/karpathy/status/1707437820045062561; https://x.com/karpathy/status/2056753169888334312
themes:
  - karpathy-mental-models
  - claude-code-workflows
  - orchestration
  - model-fundamentals
---

## Core claims

1. Coding capability crossed a discontinuous threshold in December 2025 — not gradual progress, but a sharp break in how programming work gets done.

2. Agents didn't meaningfully work before December; the December leap fundamentally changed their viability as primary tools.

3. The programmer's role is shifting from mostly-typing-code to mostly-orchestrating-and-fixing-agent-output (80/20 flip in weeks).

4. "You're not typing computer code into an editor" anymore — the era of manual programming since computing began is ending.

5. Agentic engineering requires clean decomposition, parallel workflow management, and proactive error prevention before mistakes compound across a codebase.

6. LLMs function as **OS kernels**, orchestrating diverse capabilities (code execution, I/O, memory, security, internet access) as a unified system.

7. The computing industry is stratifying around foundation models the way it did around operating systems (GPT, Claude, Llama competing like Windows/macOS/Linux).

8. An OS brings defaults apps and an app store; same pattern applies to LLM platforms.

## Patterns & frameworks

- **Agentic engineering discipline**: Decompose work cleanly for parallel execution; catch errors before they propagate across agent steps.
- **LLM-as-OS metaphor**: Kernel orchestrates I/O, code execution, memory databases, security — computing concepts carry over (assembly-level traces, attack surface, vulnerabilities, competitive moats).
- **Capability flip**: Single breakthrough in model quality (Dec 2025) inverts the manual/agent ratio; workflow changes faster than explicit retraining.

## Numbers & specifics

- **December 2025**: Inflection point (post dated ~Dec 26, 2025; ~8M+ views)
- **November → December workflow**: 80% manual + 20% agents → 80% agents + 20% human edits
- **Single-threaded execution**: ~10 tokens/second (Hz) — bottleneck for agentic loops
- **OS competitors**: GPT, PaLM, Claude, Llama, Mistral
- **May 19, 2026**: Karpathy joined Anthropic's pretraining team; mandate is using Claude to accelerate pretraining research

## Quotes

1. "It is hard to communicate how much programming has changed due to AI in the last 2 months — not gradually and over time in the 'progress as usual' way, but specifically this last December."

2. "Coding agents basically didn't work before December."

3. "You're not typing computer code into an editor like the way things were since computers were invented, that era is over."

4. "I've never felt this much behind as a programmer. The profession is being dramatically refactored as the bits contributed by the programmer are increasingly sparse and between."

5. "LLMs not as a chatbot, but the kernel process of a new Operating System" orchestrating modalities, code, memory, and security.

## Applied AI relevance

- **Agent-driven development is now the default**, not a nice-to-have. Anthropic engineers must design for orchestration patterns (parallel workflows, error propagation, result merging) rather than single-turn human-in-loop prompting.

- **Programmer-tool fit has inverted**: The leverage point is no longer writing better prompts for humans; it's decomposing work so agents can execute it cleanly and catch errors before compounding.

- **Frontier pretraining directly enables agentic systems**: Why Karpathy moved to Anthropic's pretraining team — marginal gains in base-model capability (reasoning, code generation, planning) become multiplicative in multi-step agentic workflows.

- **OS-layer thinking applies**: Tool choice, security model, app-store ecosystems, and multi-agent coordination are no longer afterthoughts — they're OS-design concerns that must be baked in from the foundation.

---

**Caveat**: Section (a) reconstructed from search-indexed snippets (x.com blocked direct fetch); verify exact wording on x.com if citation fidelity is critical.
