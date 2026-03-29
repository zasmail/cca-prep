---
argument-hint: <task-description>
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Plan Then Build

CCA-F Exam Domain: D3 Claude Code Configuration (~20%)

This slash command demonstrates the plan-mode-to-auto-accept workflow pattern.
Run as: `/plan-then-build add account balance chart to the dashboard`

Key exam concepts demonstrated:
- Structured two-phase workflow: plan FIRST, then execute
- Plan mode = read-only exploration (no writes)
- Auto-accept mode = execute the approved plan without interruption
- This pattern prevents wasted work from incorrect assumptions

---

## Phase 1: PLAN (Read-Only Exploration)

**Task**: $ARGUMENTS

Explore the codebase to build a complete implementation plan.
In this phase, ONLY use read operations — do NOT modify any files.

### Step 1: Understand Current State
- **Glob** for files related to the task
- **Read** key files to understand existing patterns, conventions, and architecture
- **Grep** for related functionality that already exists

### Step 2: Identify Dependencies
- What existing modules/components will this touch?
- What new files need to be created?
- Are there shared utilities or types to reuse?
- What tests exist that might need updating?

### Step 3: Write the Plan

Present a structured plan with:

```
## Implementation Plan: $ARGUMENTS

### Files to Create
- path/to/new/file.ts — Description of purpose

### Files to Modify
- path/to/existing/file.ts — What changes and why

### Dependencies
- List any new packages or imports needed

### Test Plan
- List test cases to write (both success and failure paths)

### Risks
- Anything that might break or need careful handling
```

GATE: Present the plan and STOP. Wait for user approval before proceeding.
This is the critical boundary between plan mode and execution mode.

## Phase 2: BUILD (Execute Approved Plan)

Once the plan is approved, execute each step in order:

1. Create new files first (dependencies before dependents)
2. Modify existing files
3. Write tests
4. Run all tests to verify:
   ```bash
   uv run pytest -v
   ```
5. Run linter to verify:
   ```bash
   ruff check .
   ```

### Completion Report
- Files created: [list]
- Files modified: [list]
- Tests: X passing, 0 failing
- Lint: clean

**Why this pattern matters for the exam:**
The plan-then-build pattern maps to the Evaluator-Optimizer orchestration pattern.
The planning phase explores and proposes, the build phase executes.
Separating these phases prevents the common mistake of coding before understanding.
