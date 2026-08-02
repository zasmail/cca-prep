---
title: Don't Build Agents, Build Skills Instead
speaker: Barry Zhang & Mahesh Murag
source: https://www.youtube.com/watch?v=CEvIs9y1uog
themes: [skills, tool-design-mcp, context-engineering, orchestration, memory, claude-code-workflows]
---

## Core Claims

1. **Code is the universal interface**—rather than domain-specific scaffolding, code (bash + filesystem) provides general-purpose agent runtime that works across all domains.

2. **Agents lack domain expertise**—intelligence without procedural knowledge makes agents like "Mahesh the genius" instead of "Barry the tax professional"; they cannot guarantee consistent execution.

3. **Skills package transferable procedural knowledge**—organized collections of files that encode best practices, workflows, and scripts that agents can absorb without training.

4. **Progressive disclosure protects context**—show only metadata at runtime; load full skill content on-demand to enable hundreds of composable skills without bloating context window.

5. **Scripts outperform traditional tools**—embedded code is self-documenting, modifiable by agents, and lives in filesystem until needed; tool descriptions decay, become ambiguous, lock agents in.

6. **Skills + MCP + Runtime form convergent architecture**—agents now couple with: (1) runtime providing file system, (2) MCP servers providing external connectivity, (3) skill libraries providing domain expertise.

7. **Non-technical domain experts can build skills**—people in finance, legal, recruiting can now package organizational knowledge without coding; democratizes agent customization.

8. **Skills enable continuous learning**—standardized format means agent output (new skills) can be consumed by future agent versions; Day 30 agent >> Day 1 agent through skill accumulation.

9. **Ecosystem compounds across boundaries**—organizational skill bases improve teams; teams' skills improve communities; community skills improve all agents (MCP server precedent).

10. **Versioning and dependencies will follow**—skills must evolve with testing, dependency tracking, and lineage; early stage now (simple folders), moving toward software-like maturity over weeks/months.

## Patterns & Frameworks

| Pattern | Explanation |
|---------|-------------|
| **Folders as abstraction** | Minimal primitive: organized files + metadata, versionable in Git, shareable via Drive/zip |
| **Progressive disclosure** | Metadata shown at init; skill.md loaded on invocation; rest of folder organized for access |
| **Scripts as reusable tools** | Persistent code in skill, not context; Claude saves recurring patterns (e.g., slide styling) for future use |
| **Three-tier ecosystem** | Foundational (Anthropic), third-party (partners like Notion, Browserbase), enterprise (org-specific best practices) |
| **Agent + MCP + Skills stack** | Architecture layers: agent loop (context mgmt) → runtime (file/code) → MCP (external data) → skills (expertise) |
| **Skill-generated learning** | Agent creates skills for itself using `skill creator` skill; standardized format enables reuse across sessions |
| **Processor → OS → Apps analogy** | Models = processors; agent runtime = OS; skills = applications (where domain value lives) |

## Numbers & Specifics

- **Launch window**: ~5 weeks old at talk date; thousands of skills deployed
- **Context capacity**: hundreds of skills can be loaded via progressive disclosure
- **Build time evolution**: simple (minutes) → current (minutes to hours) → future (weeks to months, software-quality)
- **Deployment scale**: Fortune 100 companies; dev teams serving 1000s–10,000s+ developers
- **Vertical launches**: financial services and life sciences products shipped immediately post-launch with MCP + skills
- **Learning metric**: Day 1 vs. Day 30 agent capability; compounding improvement through skill accumulation
- **Example use case**: Cloud Code writing recurring slide-styling Python script; saved to skill for future use

## Quotes

> "We think code is all we need."
> — Barry Zhang (opening framing)

> "Agents today are a lot like Mahesh. They're brilliant, but they lack expertise."
> — Barry Zhang (core problem statement)

> "Skills are organized collections of files that package composable procedural knowledge for agents. In other words, they're folders. This simplicity is deliberate."
> — Mahesh Murag (definition & design philosophy)

> "Anything that cloud writes down can be used efficiently by a future version of itself. This makes the learning actually transferable."
> — Barry Zhang (continuous learning mechanism)

> "So skills are just the starting point... we think it's time to stop rebuilding agents and start building skills instead."
> — Barry Zhang (closing pivot)

## Applied AI Relevance

- **Abandon tool sprawl**—replace thousands of API-style tool definitions with composable skill folders; each skill encodes expertise + scripts, reducing context overhead and improving selection reliability.

- **Enable org learning loops**—skills are the vehicle for capturing institutional knowledge (processes, best practices, domain guardrails) in a format agents can continuously consume and improve.

- **Design for agent self-improvement**—standardize skill format so agents self-generate skills from their own work; this removes the manual extraction bottleneck and makes Day 30 >> Day 1.

- **Distribute expertise democratically**—third-party & enterprise skills democratize vertical deployment; a tax professional can encode tax logic in a skill; a recruiter can encode hiring workflows—no ML eng required.
