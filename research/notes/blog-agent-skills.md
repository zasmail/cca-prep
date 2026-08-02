---
title: Equipping agents for the real world with Agent Skills
speaker: Anthropic Engineering
source: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
themes:
  - skills
  - claude-code-workflows
  - context-engineering
  - tool-design-mcp
  - orchestration
---

# Agent Skills — Distillation

## Core Claims

1. A skill is a filesystem-based specialization module: a directory with a `SKILL.md` file (metadata: `name`, `description`) plus optional bundled reference docs and executable scripts.
2. Progressive disclosure—loading metadata → body → bundled files on-demand—prevents skill complexity from bloating the context window.
3. Skills let a single general-purpose agent specialize across many use cases instead of requiring multiple custom builds, analogous to onboarding docs for a new hire.
4. Bundled executable code (e.g., Python scripts) is more efficient and deterministic than reasoning over extracted tokens; Claude calls scripts as tools rather than reading them into context.
5. Skill authoring begins with observing where real agents fail on production tasks, then authoring skills to fill those capability gaps.
6. Skills are potential security vectors: malicious skills can instruct exfiltration or unintended actions; only install from trusted sources and audit bundled code before use.
7. Naming and descriptions must be refined iteratively based on how Claude actually uses the skill in practice.
8. Skills are available across Claude.ai, Claude Code, Agent SDK, and Developer Platform; roadmap signals future support for skill creation, editing, discovery, and sharing.

## Patterns & Frameworks

**Progressive Disclosure**
Three-tier context loading: metadata preloaded (cheap, signals existence), body loaded on relevance detection, bundled files pulled only as needed. Mirrors manual structure (TOC → chapter → appendix).

**Skill-Driven Authoring Loop**
Run agent on real tasks → identify failure modes → write skill to cover gap → observe usage in practice → refine description/naming → iterate with Claude. Data-driven, not speculative.

**Code-as-Tool Pattern**
Treat bundled scripts as executable tools (deterministic, tested) rather than prompting Claude to reason over extracted code. Reduces token waste on procedural tasks (PDF form extraction, schema validation, etc.).

**Trust Boundary**
Skills are installed into agent context; untrusted skills pose exfiltration and instruction-injection risks. Audit bundled files and external network references before installation.

## Numbers & Specifics

- **3 levels of disclosure**: metadata, body, bundled files
- **4 deployment platforms**: Claude.ai, Claude Code, Agent SDK, Developer Platform
- **2 CCA-F domains tied to skills**: D5 (Context Management), D2 (Tool Design)
- **Future capability**: agents that can create, edit, and evaluate their own skills

## Quotes

1. "Lets one general-purpose agent specialize on demand, instead of building separate custom agents per use case — analogous to onboarding docs for a new hire."

2. "Progressive disclosure is the mechanism that keeps skill-based specialization from consuming the context window — ties to D5 (Context Management) and D2 (Tool Design)."

3. "Watch how Claude actually uses the skill in practice and refine naming/description accordingly."

4. "Skills can instruct an agent to exfiltrate data or take unwanted actions if malicious."

5. "Long-term direction: agents that can create, edit, and evaluate their own skills."

## Applied AI Relevance

- **Production specialization pattern**: Skills enable one codebase/agent to serve many use cases without forking agents per domain, reducing deployment surface.
- **Context optimization as first-class design**: Progressive disclosure is a learnable technique for scaling Claude's context to production complexity; not just a feature, but a context management strategy (exam-critical D5).
- **Code > reasoning for determinism**: Bundled executables beat prompt-based reasoning for tasks requiring guaranteed outputs (validation, extraction); aligns with "programmatic enforcement vs. prompt-based guidance" anti-pattern #3.
- **Security scope expansion**: Skills shift from tool-design threat models (API misuse) to supply-chain models (malicious skills). Audit, version control, and source trust become engineering requirements, not operational concerns.

---

**Word count:** 382 | **Themes:** skills, claude-code-workflows, context-engineering, tool-design-mcp, orchestration
