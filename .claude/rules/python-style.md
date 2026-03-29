---
paths: "**/*.py"
---

# Python Style Rules

- Python 3.12+ — use modern syntax (type unions with `|`, match statements)
- Type hints on ALL function signatures (params and return types)
- ruff formatting — run `ruff check --fix` before committing
- AAA test pattern: Arrange (setup) → Act (execute) → Assert (verify), separated by blank lines
- NEVER hardcode API keys — use `os.environ["KEY"]` or `anthropic.Anthropic()` (reads ANTHROPIC_API_KEY automatically)
- Imports: stdlib → third-party → local, sorted by ruff
- Docstrings on all public functions (Google style)
- Use `dataclass` or `TypedDict` for structured data, not raw dicts
