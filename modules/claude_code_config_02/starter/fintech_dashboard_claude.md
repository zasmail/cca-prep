# Fintech Dashboard — CLAUDE.md Exercise

CCA-F Exam Domain: D3 Claude Code Configuration (~20%)

Build a complete CLAUDE.md for a Next.js fintech dashboard application.
Fill in every TODO section below. This exercises the exact patterns tested on the exam.

Key concepts:
- CLAUDE.md is the PRIMARY way to give Claude project context
- Hierarchy: user → project → directory → @import → rules
- Only project-level and below are shared via VCS
- @import pulls in rule files and schemas for additional context

---

# Fintech Dashboard

## Project Context

<!-- TODO: Write 2-3 sentences describing the project.
     Include: what it is, who uses it, what tech stack.
     Example: "This is a Next.js 14 fintech dashboard for retail banking customers.
     It displays account balances, transaction history, and supports fund transfers.
     Built with TypeScript, Tailwind CSS, and connects to a REST API backend." -->

## Build Commands

<!-- TODO: Add the standard build commands for a Next.js project.
     Include at minimum:
     - Dev server command
     - Build command
     - Test command (with framework, e.g., vitest or jest)
     - Lint command
     Format as a ```bash code block with comments. -->

## Architecture

<!-- TODO: Describe the directory structure using a tree diagram.
     Must include at minimum:
     - src/app/ (Next.js app router pages)
     - src/app/api/ (API routes)
     - src/components/ (React components)
     - src/lib/ (utilities, API client, auth)
     - src/types/ (TypeScript type definitions)
     Format as a ``` code block. -->

## Coding Conventions

<!-- TODO: List 5-7 coding conventions. Must include:
     1. TypeScript strict mode requirement
     2. Component naming convention (PascalCase)
     3. API route error handling pattern
     4. State management approach
     5. Authentication pattern
     Think about what Claude needs to know to generate CONSISTENT code. -->

## API Patterns

<!-- TODO: Describe the standard API route pattern including:
     - Input validation approach (Zod schemas)
     - Error response shape (must be consistent)
     - Authentication middleware
     - Correlation ID for request tracing
     This maps directly to the rule file in rules/api-routes.md -->

## Imported References

<!-- TODO: Add @import references for:
     1. The API routes rule file: @.claude/rules/api-routes.md
     2. Any shared schemas that API routes should follow

     Key exam concept: @import pulls external files into CLAUDE.md context.
     These are resolved relative to the CLAUDE.md file location. -->

## Security Rules

<!-- TODO: Add 3-4 security rules that MUST be followed.
     Include:
     - No hardcoded API keys or secrets
     - All user input must be validated before use
     - Authentication required on all /api routes except /api/health
     - PII must never be logged

     Key exam concept: Critical rules belong in CLAUDE.md (always loaded)
     AND in hooks (programmatic enforcement). Prompt-only = AP3. -->
