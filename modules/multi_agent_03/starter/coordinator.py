"""Multi-Agent Research Coordinator — Starter Tier.

CCA-F Exam Domains: D1 Agentic Architecture (~27%), D2 Tool Design (~18%), D5 Context (~15%)

This exercise teaches the orchestrator-worker pattern (Anthropic Pattern #4).
The coordinator manages ALL inter-agent communication. Workers never talk
to each other directly.

Key concepts tested:
- Coordinator dispatches SCOPED context to each worker (not full history)
- Workers return structured results, coordinator synthesizes
- Conflicting findings get annotated with source attribution
- Errors propagate as structured objects, never silently suppressed
"""

from __future__ import annotations


from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# Data Structures
# ---------------------------------------------------------------------------

@dataclass
class ResearchTask:
    """A scoped research subtask dispatched to a worker.

    Key exam concept: The task contains ONLY what the worker needs.
    No full conversation history, no other workers' results, no coordinator state.
    """

    subtopic: str
    context: str  # Scoped background — NOT the full conversation
    output_format: str  # What structure the worker should return
    max_sources: int = 5


@dataclass
class ResearchFinding:
    """A single finding returned by a research worker."""

    claim: str
    source: str
    confidence: str  # "high", "medium", "low"
    evidence: str
    worker_id: str  # Attribution — which worker produced this


@dataclass
class SynthesizedReport:
    """The coordinator's final synthesized report.

    Key exam concept: When findings conflict, the coordinator annotates BOTH
    with source attribution rather than silently picking one.
    """

    topic: str
    findings: list[ResearchFinding] = field(default_factory=list)
    conflicts: list[dict[str, Any]] = field(default_factory=list)
    summary: str = ""
    sources_consulted: int = 0


# ---------------------------------------------------------------------------
# Tool Definitions — these define what the coordinator can dispatch
# ---------------------------------------------------------------------------

COORDINATOR_TOOLS: list[dict[str, Any]] = [
    {
        "name": "delegate_to_researcher",
        "description": (
            "Dispatch a scoped research subtask to a worker agent. "
            "The worker receives ONLY the subtopic, context, and output_format — "
            "NOT the full conversation history or other workers' results. "
            "Returns structured findings or a structured error."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "subtopic": {
                    "type": "string",
                    "description": "The specific subtopic for this worker to research",
                },
                "context": {
                    "type": "string",
                    "description": (
                        "Scoped background context for this subtopic ONLY. "
                        "Must NOT include full conversation history or other workers' results."
                    ),
                },
                "output_format": {
                    "type": "string",
                    "description": (
                        "The structure the worker should return results in. "
                        "Example: 'Return a JSON object with keys: claims, sources, confidence'"
                    ),
                },
            },
            "required": ["subtopic", "context", "output_format"],
        },
    },
    {
        "name": "synthesize_findings",
        "description": (
            "Combine findings from multiple research workers into a cohesive report. "
            "Identifies agreements, conflicts, and gaps. "
            "Conflicts are annotated with source attribution from both workers — "
            "NEVER silently pick one over the other."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "findings": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "worker_id": {"type": "string"},
                            "subtopic": {"type": "string"},
                            "claims": {
                                "type": "array",
                                "items": {"type": "string"},
                            },
                            "sources": {
                                "type": "array",
                                "items": {"type": "string"},
                            },
                            "confidence": {"type": "string"},
                        },
                        "required": ["worker_id", "subtopic", "claims"],
                    },
                    "description": "Array of findings from each research worker",
                },
            },
            "required": ["findings"],
        },
    },
]


def delegate_to_researcher(
    subtopic: str,
    context: str,
    output_format: str,
) -> dict[str, Any]:
    """Dispatch a scoped research task to a worker subagent.

    TODO: Implement this function following these rules:

    1. Create a ResearchTask with ONLY the provided subtopic, context, and output_format
       - CRITICAL: Do NOT pass full conversation history as context
       - CRITICAL: Do NOT include other workers' results in context
       - The context parameter should be a focused summary relevant to this subtopic

    2. Dispatch the task to the worker (in production, this calls a subagent)
       - In Claude Code, this would use the Agent tool to invoke a worker agent
       - The worker agent file defines its tools and model

    3. Return the worker's structured result:
       - On success: {"status": "success", "findings": [...], "worker_id": "..."}
       - On failure: structured error (see error_propagation.py) — NEVER return {}

    Key exam concept: The coordinator manages ALL communication.
    Workers are stateless — they receive a task and return a result.
    They don't know about other workers or the broader research question.

    Args:
        subtopic: The specific subtopic for this worker to research.
        context: Scoped background — NOT full conversation history.
        output_format: Expected structure for the worker's response.

    Returns:
        Structured result dict with findings or structured error.
    """
    # TODO: Implement delegation to research worker
    # Step 1: Validate inputs
    # Step 2: Create scoped ResearchTask
    # Step 3: Dispatch to worker subagent
    # Step 4: Return structured result or structured error
    raise NotImplementedError(
        "Implement delegate_to_researcher — dispatch scoped tasks to worker subagents"
    )


def synthesize_findings(findings: list[dict[str, Any]]) -> SynthesizedReport:
    """Combine findings from multiple workers into a cohesive report.

    TODO: Implement this function following these rules:

    1. Group findings by subtopic

    2. Identify AGREEMENTS — claims that multiple workers support
       - Strengthen confidence when multiple independent sources agree

    3. Identify CONFLICTS — claims where workers disagree
       - CRITICAL: Annotate BOTH sides with source attribution
       - Format: {"claim_a": "...", "source_a": "worker_1",
       -          "claim_b": "...", "source_b": "worker_2",
       -          "resolution": "needs_further_research"}
       - NEVER silently pick one claim over the other

    4. Identify GAPS — subtopics with no findings or low confidence
       - These may need additional research passes

    5. Generate summary that acknowledges conflicts and gaps honestly

    Key exam concept: The coordinator is the ONLY entity that sees all findings.
    It must handle conflicts transparently, not hide them.

    Args:
        findings: List of finding dicts from each research worker.

    Returns:
        SynthesizedReport with findings, conflicts, and summary.
    """
    # TODO: Implement synthesis logic
    # Step 1: Group findings by subtopic
    # Step 2: Find agreements (same claim, multiple workers)
    # Step 3: Find conflicts (contradictory claims, annotate both)
    # Step 4: Find gaps (missing subtopics or low confidence)
    # Step 5: Generate summary
    raise NotImplementedError(
        "Implement synthesize_findings — combine worker results with conflict annotation"
    )


def run_research_coordinator(
    research_question: str,
    *,
    max_workers: int = 4,
    model: str = "claude-sonnet-4-6",
) -> SynthesizedReport:
    """Run the multi-agent research coordinator.

    TODO: Implement the coordination loop:

    1. Decompose the research question into subtopics
       - Each subtopic should be independently researchable
       - Aim for 2-4 subtopics (don't over-decompose)

    2. Dispatch each subtopic to a worker via delegate_to_researcher()
       - Workers run in PARALLEL when possible (Anthropic Pattern #3: Parallelization)
       - Each worker gets SCOPED context for its subtopic only

    3. Collect all results, handling failures gracefully:
       - If a worker fails with TRANSIENT error → retry once
       - If a worker fails with VALIDATION error → skip with note
       - NEVER silently drop failed results (AP7)

    4. Synthesize all findings via synthesize_findings()

    5. Return the final SynthesizedReport

    Args:
        research_question: The main research question to investigate.
        max_workers: Maximum number of parallel research workers.
        model: Claude model for the coordinator (workers may use different models).

    Returns:
        SynthesizedReport with all findings, conflicts, and summary.
    """
    # TODO: Implement the coordination loop
    raise NotImplementedError(
        "Implement run_research_coordinator — the orchestrator-worker pattern"
    )
