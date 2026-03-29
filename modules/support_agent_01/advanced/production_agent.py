"""Customer Support Agent — Advanced Tier (Production-Grade).

CCA-F Exam Domains: D1 Agentic Architecture, D4 Prompt Engineering

This exercise combines everything from starter and intermediate tiers
into a production-ready agent with:
- Case-fact extraction (structured data from conversation)
- Error propagation with isError + errorCategory + isRetryable
- Handoff summaries for human escalation
"""

from __future__ import annotations


import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


# ---------------------------------------------------------------------------
# Structured Error Types — AP6 compliance
# ---------------------------------------------------------------------------

class ErrorCategory(Enum):
    """Error categories for structured error propagation.

    Anti-pattern #6: Every error must include a category and retryable flag.
    Anti-pattern #7: NEVER silently suppress — always propagate structured errors.
    """

    TRANSIENT = "TRANSIENT"        # Network timeouts, rate limits — IS retryable
    VALIDATION = "VALIDATION"      # Bad input — NOT retryable
    NOT_FOUND = "NOT_FOUND"        # Resource missing — NOT retryable
    PERMISSION = "PERMISSION"      # Auth/access denied — NOT retryable
    INTERNAL = "INTERNAL"          # Unexpected failure — may be retryable


@dataclass
class StructuredError:
    """Structured error response — exam-compliant format.

    TODO: Implement to_dict() that returns:
    {
        "isError": True,
        "errorCategory": self.category.value,
        "isRetryable": self.is_retryable,
        "error": self.message,
        "code": self.code,
        "attempted": self.attempted_action,
        "alternatives": self.alternatives,
    }
    """

    message: str
    code: str
    category: ErrorCategory
    is_retryable: bool
    attempted_action: str = ""
    alternatives: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convert to the exam-compliant error dict format.

        TODO: Implement this method.
        """
        raise NotImplementedError("Implement StructuredError.to_dict()")


# ---------------------------------------------------------------------------
# Case Facts — extracted structured data from the conversation
# ---------------------------------------------------------------------------

@dataclass
class CaseFacts:
    """Structured facts extracted from the support conversation.

    The agent should populate these as it gathers information through tool calls.
    These facts are used for:
    1. Handoff summaries when escalating to humans
    2. Audit trails for compliance
    3. Structured logging for analytics
    """

    customer_id: str | None = None
    customer_name: str | None = None
    customer_verified: bool = False
    order_ids: list[str] = field(default_factory=list)
    issue_type: str | None = None  # refund, inquiry, complaint, escalation
    refund_amount: float | None = None
    refund_requires_approval: bool = False
    escalation_reason: str | None = None
    resolution: str | None = None
    compliance_flags: list[str] = field(default_factory=list)

    def to_handoff_summary(self) -> str:
        """Generate a structured handoff summary for human escalation.

        TODO: Implement this method to produce a clear, structured summary
        that a human agent can use to continue the case. Include:
        - Customer identity (verified or not)
        - What was attempted and what happened
        - Why it's being escalated (which of the 3 valid triggers)
        - Any compliance flags

        This is NOT a free-text summary — it should be structured and factual.
        """
        raise NotImplementedError("Implement CaseFacts.to_handoff_summary()")


# ---------------------------------------------------------------------------
# Production Agent
# ---------------------------------------------------------------------------

def run_production_agent(
    user_message: str,
    *,
    max_iterations: int = 25,
    model: str = "claude-sonnet-4-6-20250514",
) -> dict[str, Any]:
    """Run the production-grade support agent.

    TODO: Combine patterns from starter and intermediate tiers:

    1. Initialize: Anthropic client, messages, AgentState, CaseFacts
    2. Agentic loop with stop_reason checking (from starter)
    3. PreToolUse/PostToolUse hooks (from intermediate)
    4. NEW — Case fact extraction:
       - After each tool call, update CaseFacts with extracted information
       - get_customer → set customer_id, customer_name, customer_verified
       - lookup_order → add to order_ids
       - process_refund → set refund_amount, refund_requires_approval
       - escalate_to_human → set escalation_reason
    5. NEW — Structured error propagation:
       - When execute_tool fails, create StructuredError
       - Include the error in tool_result with is_error=True
       - Error messages must be SPECIFIC (anti-pattern #6):
         BAD: "Something went wrong"
         GOOD: "Order ORD-1001 not found in system"
    6. NEW — On escalation, include CaseFacts.to_handoff_summary()

    Returns:
        {
            "response": final_text,
            "case_facts": CaseFacts as dict,
            "errors": list of StructuredError dicts,
            "compliance_flags": list of compliance warnings,
        }
    """
    raise NotImplementedError("Implement run_production_agent — the full production agent")
