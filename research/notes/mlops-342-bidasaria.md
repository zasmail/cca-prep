---
title: Building Claude Code — Origin, Product Iterations, & What's Next
speaker: Siddharth Bidasaria (Member of Technical Staff, Anthropic)
source: MLOps Community Podcast #342
themes:
  - claude-code-workflows
  - tool-design-mcp
  - orchestration
  - evals
  - enforcement-reliability
  - model-fundamentals
---

## Core claims

1. File-local access was the breakthrough that made Claude Code feel magical and low friction — eliminating sync/Docker/repo setup.
2. The to-do list feature sustains long-horizon tasks by batching work (e.g., 100 files into 10-file checkpoints) and prevents model stalling after ~30 files.
3. Model step-changes (informally "35" to "37") created discontinuous jumps in task complexity the model could handle.
4. "Unhobbling the model" means deleting bespoke tools in favor of general abstractions (BASH instead of many filesystem-specific tools).
5. Verification is two-part: *model behavior* (does it self-check?) and *tool availability* (can it execute checks?).
6. Unit tests are the pragmatic shortest path to reliable verification; screenshot-based MCP tools (Puppeteer) enable UI iteration.
7. Power users naturally build multi-agent fleets (10–12 instances with assigned personas, communicating via filesystem).
8. Permission management doesn't yet scale to complex multi-agent topologies; the team waits for evidence before adding complexity.
9. Hooks inject user code into Claude Code's lifecycle (e.g., logging every tool call via pre-tool-call hooks).
10. Research and product form a two-way flywheel: user behavior feeds back to research priorities.

## Patterns & frameworks

| Pattern | Explanation |
|---------|-------------|
| **Unhobbling** | Delete bespoke tools; trust the model with general abstractions (BASH, local file access). Scales better than hand-built specificity. |
| **To-do list batching** | For long-horizon tasks, create a structured to-do early to break 100+ files into checkpoints of ~10 and iterate with visibility. |
| **Verification split** | Separate model behavior (self-checking capability) from tool availability (can it run tests/screenshots?). Unit tests are the default. |
| **Persona-assigned fleets** | Multiple Claude instances with defined roles (backend, frontend, etc.) communicate via filesystem for complex tasks. |
| **Hooks as enforcement** | User code runs at lifecycle events (pre/post tool call). Critical for observability and enforcement in complex workflows. |
| **Screenshot iteration** | MCP servers like Puppeteer let the model take screenshots and iterate on web UIs; applies to other verification via tools. |

## Numbers & specifics

- **300 active daily users** in first 2 weeks at a 600-person company (internal launch)
- **~30 files** before model stalls (motivating to-do list feature)
- **100 files batched into 10-file groups** to sustain multi-file edits
- Model versions **"35" and "37"** (informal names; "37" was the step-change point)
- **10–12 Claude instances** in one power-user fleet (each with assigned persona)
- **100+ MCP servers** on some power-user systems
- **Boris Cherny** built initial prototype (terminal access, Spotify control, file read/write)

## Quotes

1. *"There's something here. It feels really ergonomic."* (immediate reaction to Boris's prototype)
2. *"It just felt really magical. It just felt really low friction."* (on file tools eliminating setup friction)
3. *"It's just doing all this stuff for me. I'm just watching."* (on the to-do list feature's satisfying behavior)
4. *"One of the core, like, philosophies of our team is we absolutely love deleting code"* (core philosophy on unbobbling)
5. *"Make sure that I have a unit testing framework that is able to test as large of a surface area as possible of my code"* (practical verification advice)

## Applied AI relevance

- **Tool design at scale:** General abstractions (BASH, file I/O) outperform bespoke tools in both user adoption and model reliability. This principle applies to MCP server design: fewer, more general tools beat many specialized ones.
- **Multi-agent verification is hard:** Fleets and sub-agents are powerful but don't yet have scalable permission or observability frameworks. Unit tests + screenshot-based iteration are the immediate pragmatic solution before complex topologies.
- **Hooks enable enforcement:** Lifecycle injection (pre/post tool call) is where programmatic control lives. Use hooks for logging, permission auditing, and rate-limiting—not prompt-based guidance.
- **Model capability is the bottleneck:** File access and local context eliminated the largest friction point. As models improve, invest in evaluation frameworks that will scale alongside capability growth; don't over-optimize for current model limitations.

---

*Word count: 520 | Themes: claude-code-workflows, tool-design-mcp, orchestration, evals, enforcement-reliability, model-fundamentals*
