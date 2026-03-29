# Module 04: Developer Productivity

## Overview
This module teaches the tool selection patterns and codebase exploration strategies
tested on the CCA-F exam. Knowing WHICH tool to use for each task type is a direct
exam question pattern — the wrong tool often "works" but is the anti-pattern answer.

## Domains Covered
| Domain | Weight | Focus |
|--------|--------|-------|
| D2 Tool Design | ~18% | Correct tool selection, tool count limits |
| D3 Claude Code Configuration | ~20% | Built-in tools, MCP server setup |
| D1 Agentic Architecture | ~27% | Tool execution within agentic loops |

## Tier Breakdown

### Starter: Tool Selection Decision Matrix
**File**: `starter/tool_selection.py`

Learn the mapping between task descriptions and correct tools:
- Read file content -> `Read` (not `Bash('cat')`)
- Modify a few lines -> `Edit` (not `Write`)
- Find files by name -> `Glob` (not `Bash('find')`)
- Search file contents -> `Grep` (not `Bash('grep')`)
- Create a new file -> `Write` (not `Edit`)
- Multiple edits in one file -> `MultiEdit` (not sequential `Edit`)
- Run tests/build -> `Bash` (correct — no dedicated tool for execution)

### Intermediate: Codebase Exploration Strategy
**File**: `intermediate/explore_codebase.md`

A slash command that teaches the 4-step incremental discovery pattern:
1. **Structure**: LS + Glob to understand project layout
2. **Threads**: Grep + Read to follow specific code paths
3. **Dependencies**: Map imports, configs, and relationships
4. **Findings**: Document architecture decisions and patterns

### Advanced: MCP Integration
**File**: `advanced/mcp_integration.py`

Build a custom MCP tool wrapper around the fintech-mock server:
- Define tools with proper input_schema
- Handle connection lifecycle
- Map domain operations to MCP tool calls

## Running Tests
```bash
uv run pytest modules/dev_productivity_04/ -v
```

## Key Exam Insights
- The exam WILL present scenarios where Bash "works" but a dedicated tool is correct
- Tool count matters: 5 or fewer tools per agent is the guideline
- MCP servers appear as regular tools to Claude — the integration is transparent
- Always prefer the most specific tool available for the task
