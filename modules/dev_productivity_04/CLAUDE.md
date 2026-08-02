# Module 04: Developer Productivity

## Exam Coverage
- **Primary Domains**: D2 Tool Design (~18%), D3 Claude Code Configuration (~20%)
- **Secondary Domain**: D1 Agentic Architecture (~27%)
- **Combined weight**: ~65% of exam touches these domains

## Learning Objectives
1. Select the correct built-in tool for each task type (Read vs Bash('cat'), Edit vs Write, Glob vs Bash('find'))
2. Apply the incremental codebase exploration strategy (structure -> threads -> dependencies -> findings)
3. Integrate MCP servers as custom tool providers for domain-specific operations
4. Recognize AP8: more than 5 tools per agent degrades selection reliability

## Key Patterns
- **Tool selection matrix**: Each task type maps to exactly ONE correct tool — exam tests this directly
- **Incremental discovery**: Never Read the entire codebase; use LS/Glob for structure, Grep/Read for targeted exploration
- **MCP integration**: Custom tools extend Claude Code's capabilities without modifying the core system
- **MultiEdit**: Use for multiple changes to the same file — avoids sequential Edit anti-pattern

## Anti-Patterns Tested
- AP8: More than 5 tools per agent (heuristic, not an official hard limit —
  selection reliability degrades as tool count grows; no official source
  quantifies a percentage. Nov 2025 Tool Search Tool + Programmatic Tool
  Calling reframe this as an architecture choice, letting tool count scale
  into the thousands without a hard cap)
- Using Bash for operations that have dedicated tools (cat, grep, find)
- Using Write to make small edits (overwrites entire file — use Edit instead)
- Using Edit to create new files (Edit requires existing content to match on)

## Progression
- **Starter**: Tool selection decision matrix — learn which tool for which task
- **Intermediate**: Codebase exploration strategy — systematic incremental discovery
- **Advanced**: MCP integration — wrap external services as Claude Code tools
