---
title: "Equipping agents for the real world with Agent Skills"
speaker: Anthropic Engineering
source: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
retrieved: 2026-07-16
method: webfetch
note: >
  Copyright limits prevent saving a full verbatim transcript or a lightly-reworded
  paraphrase of this article. Below is a condensed, independently-written study-note
  summary (substantially shorter than, and restructured from, the source) capturing
  the facts and terminology relevant to CCA-F prep. Refer to the source URL for the
  original text.
published: 2025-10-16
---

# Agent Skills — study notes

## What a Skill is
- A directory containing a `SKILL.md` file (YAML frontmatter: `name`, `description`) plus optional bundled files (reference docs, scripts).
- Lets one general-purpose agent specialize on demand, instead of building separate custom agents per use case — analogous to onboarding docs for a new hire.

## Progressive disclosure (3 levels)
1. **Metadata** (`name` + `description`) — preloaded into the system prompt at startup; cheap, lets the model know the skill exists.
2. **`SKILL.md` body** — loaded into context only when Claude judges the skill relevant.
3. **Bundled reference files / scripts** — pulled in selectively, only as needed during the task.

This lets skills scale in complexity without bloating the context window — similar to a manual's table of contents → chapter → appendix structure.

## Code execution inside skills
- Skills can bundle executable scripts (e.g., Python) that Claude runs as tools rather than reading into context.
- More efficient/deterministic than token-based operations (e.g., a bundled script extracting PDF form fields vs. having the model "reason" through extraction).

## Authoring guidance
- Find gaps first: run the agent on real tasks, see where it struggles, then write skills to cover those gaps.
- Split large `SKILL.md` files into referenced sub-files; separate mutually-exclusive contexts to save tokens; treat code as both a tool and documentation.
- Watch how Claude actually uses the skill in practice and refine naming/description accordingly.
- Iterate collaboratively with Claude — capture successful ad hoc approaches into reusable skill content.

## Security
- Skills can instruct an agent to exfiltrate data or take unwanted actions if malicious.
- Only install skills from trusted sources; audit untrusted skills' bundled files, code, and any instructions that point at external network destinations before use.

## Availability / roadmap
- Live across Claude.ai, Claude Code, the Claude Agent SDK, and the Claude Developer Platform.
- Anthropic signals future support for the full skill lifecycle (create/edit/discover/share/use) and potential complementary use alongside MCP servers for tool-heavy workflows.
- Long-term direction: agents that can create, edit, and evaluate their own skills.

## Exam-relevant takeaway
Progressive disclosure is the mechanism that keeps skill-based specialization from consuming the context window — ties to D5 (Context Management) and D2 (Tool Design: code-as-tool vs. token-based reasoning).
