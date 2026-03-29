# /explore-codebase — Incremental Codebase Discovery

## Purpose
Systematically explore an unfamiliar codebase using the 4-step incremental
discovery pattern. This is the exam-tested approach — never try to Read the
entire codebase at once.

## Usage
```
/explore-codebase [path_to_codebase]
```

## The 4-Step Incremental Discovery Pattern

### Step 1: Structure (LS + Glob)
Get the high-level layout without reading any file contents.

**Tools used**: Bash(`ls`), Glob

```
Actions:
- LS the root directory to see top-level structure
- Glob for key files: "**/*.md", "**/package.json", "**/pyproject.toml",
  "**/*.toml", "**/Makefile", "**/Dockerfile"
- Glob for entry points: "**/main.*", "**/app.*", "**/index.*"
- Glob for config files: "**/.env*", "**/settings.*", "**/*.config.*"

Output:
- Project type (Python, Node, Rust, etc.)
- Directory structure summary
- Build system identification
- Entry point locations
```

### Step 2: Threads (Grep + Read)
Follow specific code paths by searching for patterns, then reading relevant files.

**Tools used**: Grep, Read

```
Actions:
- Grep for imports/requires to find dependency patterns
- Grep for class/function definitions in entry points
- Read key files identified in Step 1 (README, main config, entry points)
- Grep for TODO/FIXME/HACK for known issues
- Grep for test patterns to understand testing approach

Output:
- Key abstractions and their locations
- Public API surface
- Known issues and technical debt
- Testing strategy
```

### Step 3: Dependencies (Import/Config Mapping)
Map relationships between modules and external dependencies.

**Tools used**: Grep, Read

```
Actions:
- Read package.json / pyproject.toml / Cargo.toml for external deps
- Grep for import statements to map internal module dependencies
- Grep for environment variable usage (os.environ, process.env)
- Read CI/CD config files (.github/workflows/, .gitlab-ci.yml)
- Grep for database/API connection patterns

Output:
- External dependency list with versions
- Internal module dependency graph
- Environment variables required
- External service integrations
```

### Step 4: Document Findings
Synthesize discoveries into structured findings.

**Tools used**: (analysis — no tools needed)

```
Output format:
- Architecture: [monolith | microservice | serverless | library]
- Language: [primary language + version]
- Build: [build system and commands]
- Entry points: [list of main entry files]
- Key abstractions: [core classes/modules and what they do]
- Dependencies: [critical external deps]
- Env vars: [required environment variables]
- Tests: [testing framework and run command]
- Known issues: [TODOs, FIXMEs found in Step 2]
```

## Anti-Patterns to Avoid
1. **Reading every file** — use Grep to find what matters, then Read selectively
2. **Using Bash('cat')** — use Read for file contents (AP: wrong tool)
3. **Using Bash('find')** — use Glob for file discovery (AP: wrong tool)
4. **Using Bash('grep')** — use Grep for content search (AP: wrong tool)
5. **Skipping Step 1** — structure-first prevents wasted reads on irrelevant files
6. **No documentation of findings** — findings must be structured for reuse

## Exam Connection
- D2 Tool Design: Correct tool selection at each step
- D3 Claude Code Configuration: Understanding built-in tool capabilities
- D1 Agentic Architecture: Systematic multi-step exploration (agentic pattern)

## Prompt Template
```
Explore the codebase at $ARGUMENTS using the 4-step incremental discovery pattern.

Step 1 — Structure: Use LS and Glob to map the project layout.
Step 2 — Threads: Use Grep and Read to follow key code paths.
Step 3 — Dependencies: Map internal and external dependencies.
Step 4 — Document: Produce structured findings.

Report findings in the structured format defined in the exploration guide.
Do NOT read every file — be selective based on what Steps 1-2 reveal.
```
