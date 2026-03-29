"""Structured Error Propagation for Multi-Agent Systems — Intermediate Tier.

CCA-F Exam Domains: D1 (~27%), D2 (~18%)

This exercise teaches structured error handling in multi-agent orchestration.
When a subagent fails, the error MUST propagate with full context — never silently.

Key concepts tested:
- AP6: Errors must include category, message, isRetryable, and what was attempted
- AP7: NEVER silently return empty results ({} or []) on failure
- Partial results: If a worker succeeded partially, return what you have + the error
- Error categories determine coordinator retry strategy
"""

from __future__ import annotations


from dataclasses import dataclass, field
from enum import Enum
from typing import Any


# ---------------------------------------------------------------------------
# Error Categories
# ---------------------------------------------------------------------------

class ErrorCategory(Enum):
    """Categorize subagent failures for appropriate coordinator response.

    Key exam concept: Error categories determine the coordinator's retry strategy.
    Not all errors are the same — some are retryable, some aren't.
    """

    TRANSIENT = "transient"
    """Temporary failure — network timeout, rate limit, service unavailable.
    Coordinator should RETRY after a delay.
    """

    VALIDATION = "validation"
    """Invalid input or malformed request.
    Coordinator should NOT retry with same input — fix the input first.
    """

    NOT_FOUND = "not_found"
    """Requested resource doesn't exist.
    Coordinator should try alternative sources or report gap.
    """

    PERMISSION = "permission"
    """Access denied — missing credentials or insufficient permissions.
    Coordinator should NOT retry — escalate to user.
    """


# ---------------------------------------------------------------------------
# Subagent Result
# ---------------------------------------------------------------------------

@dataclass
class SubagentResult:
    """Structured result from a subagent — covers both success and failure.

    Key exam concept: This is the ONLY valid return type from a subagent.
    Success returns data. Failure returns a structured error with full context.
    There is NO third option (silent failure, empty dict, or None).

    Anti-pattern AP7: NEVER do this:
        if error:
            return {}  # WRONG — silent failure
        if error:
            return []  # WRONG — empty results masquerading as success

    Always do this:
        if error:
            return SubagentResult.failure(
                category=ErrorCategory.TRANSIENT,
                message="API timeout after 30s",
                attempted="Fetch pricing data from Bloomberg API",
                alternatives=["Try Reuters API", "Use cached data from 1h ago"]
            )
    """

    success: bool
    data: dict[str, Any] | None = None
    error: dict[str, Any] | None = None
    partial_results: list[dict[str, Any]] = field(default_factory=list)

    @classmethod
    def ok(cls, data: dict[str, Any]) -> "SubagentResult":
        """Create a successful result.

        TODO: Implement this classmethod.

        Args:
            data: The worker's structured findings.

        Returns:
            SubagentResult with success=True and the data.
        """
        # TODO: Implement success result constructor
        raise NotImplementedError("Implement SubagentResult.ok()")

    @classmethod
    def failure(
        cls,
        *,
        category: ErrorCategory,
        message: str,
        attempted: str,
        alternatives: list[str] | None = None,
        partial_results: list[dict[str, Any]] | None = None,
        is_retryable: bool | None = None,
    ) -> "SubagentResult":
        """Create a structured failure result.

        TODO: Implement this classmethod following these rules:

        1. Build the error dict with ALL required fields:
           - "category": The ErrorCategory value (e.g., "transient")
           - "message": Human-readable description of what went wrong
           - "isRetryable": Whether the coordinator should retry
             (auto-detect from category if not explicitly provided:
              TRANSIENT → True, all others → False)
           - "attempted": What the worker was trying to do when it failed
           - "alternatives": Suggested alternative approaches (may be empty list)

        2. Include partial_results if the worker got some data before failing
           Key concept: Partial results are valuable — don't throw them away

        3. Set success=False

        Key exam concept (AP6): Every field serves a purpose:
        - category → determines retry strategy
        - message → human debugging
        - isRetryable → automated retry decision
        - attempted → audit trail
        - alternatives → fallback options

        Args:
            category: Type of failure (determines retry strategy).
            message: Human-readable error description.
            attempted: What the worker was trying to do.
            alternatives: Suggested fallback approaches.
            partial_results: Any data collected before the failure.
            is_retryable: Override auto-detection of retryability.

        Returns:
            SubagentResult with success=False and structured error.
        """
        # TODO: Implement failure result constructor
        # Step 1: Determine retryability (auto-detect or use override)
        # Step 2: Build error dict with ALL required fields
        # Step 3: Include partial_results if provided
        # Step 4: Return SubagentResult with success=False
        raise NotImplementedError("Implement SubagentResult.failure()")

    def is_retryable(self) -> bool:
        """Check if this failure can be retried.

        TODO: Implement this method.

        Returns True only if:
        1. This is a failure (success=False)
        2. The error dict has isRetryable=True

        Returns:
            Whether the coordinator should retry this operation.
        """
        # TODO: Implement retryability check
        raise NotImplementedError("Implement SubagentResult.is_retryable()")

    def get_usable_data(self) -> dict[str, Any] | list[dict[str, Any]]:
        """Get whatever data is available — full results or partial.

        TODO: Implement this method.

        Returns:
        - self.data if success
        - self.partial_results if failure but partial data exists
        - Raises ValueError if no data at all (forces caller to handle)

        Key concept: Partial results are valuable. A worker that found 3 out of
        5 sources before timing out still has useful data.
        """
        # TODO: Implement data extraction with partial result fallback
        raise NotImplementedError("Implement SubagentResult.get_usable_data()")


# ---------------------------------------------------------------------------
# Error Handling Utilities
# ---------------------------------------------------------------------------

def handle_worker_failure(
    result: SubagentResult,
    worker_id: str,
    retry_count: int = 0,
    max_retries: int = 1,
) -> SubagentResult | None:
    """Coordinator-level error handling for worker failures.

    TODO: Implement the coordinator's error handling strategy:

    1. If result is successful → return result as-is
    2. If failure is retryable AND retry_count < max_retries → return None (signal retry)
    3. If failure has partial results → log warning, return result (use partial data)
    4. If failure is not retryable → log error, return result (coordinator handles)

    CRITICAL (AP7): NEVER silently discard the failure. The coordinator must
    either retry, use partial results, or propagate the error to the final report.

    Args:
        result: The SubagentResult from the worker.
        worker_id: Which worker failed (for logging/attribution).
        retry_count: How many times we've already retried.
        max_retries: Maximum retries for transient failures.

    Returns:
        SubagentResult to use, or None if the coordinator should retry.
    """
    # TODO: Implement coordinator error handling strategy
    raise NotImplementedError("Implement handle_worker_failure")
