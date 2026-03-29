---
context: fork
tools: Read, Grep, Glob
model: sonnet
---

# Security Audit Skill

CCA-F Exam Domain: D3 (~20%), D5 Context Management (~15%)

This skill runs a security audit as an ISOLATED SUBAGENT.

Key exam concept: `context: fork` means this skill runs in a FORKED context —
it gets its OWN context window, separate from the parent conversation.
The subagent does NOT see the parent's chat history. It starts fresh with
ONLY this skill file's instructions plus whatever files it reads itself.

Why this matters:
- **AP9 prevention**: Same-session self-review suffers from confirmation bias.
  By forking context, the auditor has no knowledge of the developer's intent
  or reasoning — it evaluates the code objectively.
- **Context efficiency**: The auditor's context window isn't polluted with
  unrelated conversation history.
- **Tool restriction**: `tools: Read, Grep, Glob` means this skill can ONLY
  read files — it cannot modify anything (no Write, Edit, or Bash).

---

## Audit Procedure

Scan the codebase for the following security vulnerability categories.
For each finding, report: file path, line number, severity, and remediation.

### 1. Credential Exposure

**Grep** for patterns that indicate hardcoded secrets:

- API keys: `api[_-]?key\s*[:=]`
- Passwords: `password\s*[:=]\s*['"]\w+`
- Tokens: `(secret|token)\s*[:=]\s*['"]`
- Connection strings: `(postgres|mysql|redis):\/\/\w+:\w+@`
- AWS keys: `AKIA[0-9A-Z]{16}`

Severity: CRITICAL
Remediation: Move to environment variables, use a secrets manager.

### 2. Input Validation Gaps

**Grep** for endpoints or handlers that use raw user input without validation:

- `request.body` / `request.json()` without Zod/schema validation
- `request.query` / `request.params` used directly in database queries
- String concatenation in SQL queries (SQL injection)
- Template literals with user input (XSS potential)

Severity: HIGH
Remediation: Add Zod schema validation at every input boundary.

### 3. SQL Injection

**Grep** for SQL query construction patterns:

- String concatenation: `f"SELECT.*{` or `"SELECT " + `
- Template literals in queries: `` `SELECT...${` ``
- Raw query execution without parameterization

Severity: CRITICAL
Remediation: Use parameterized queries or an ORM.

### 4. Cross-Site Scripting (XSS)

**Grep** for patterns that render user input without sanitization:

- `dangerouslySetInnerHTML` with user-controlled content
- `innerHTML` assignments
- `document.write()` with dynamic content
- Template rendering without escaping

Severity: HIGH
Remediation: Use framework auto-escaping, sanitize with DOMPurify for raw HTML.

### 5. Authentication Bypass

**Glob** for API route files and check each one:

- Routes missing authentication middleware
- Routes that check auth but don't return early on failure
- Token validation that doesn't check expiration
- Missing CSRF protection on state-changing endpoints

Severity: CRITICAL
Remediation: Apply authentication middleware consistently via wrapper/decorator.

---

## Report Format

Output a structured security report:

```
## Security Audit Report

**Scan Date**: [date]
**Files Scanned**: [count]
**Findings**: [count by severity]

### CRITICAL Findings
| # | File | Line | Category | Description |
|---|------|------|----------|-------------|
| 1 | ... | ... | ... | ... |

### HIGH Findings
| # | File | Line | Category | Description |
|---|------|------|----------|-------------|

### MEDIUM Findings
| # | File | Line | Category | Description |
|---|------|------|----------|-------------|

### Recommendations
1. [Top priority remediation]
2. ...
```

If no findings in a severity category, report "None found" — do NOT omit the section.
