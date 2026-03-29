"""LLM-as-judge grader using Claude Sonnet for CCA-F evaluation.

Uses rubric-based prompting with temperature=0.0 for deterministic scoring.
Returns structured JSON with reasoning, pass/fail verdict, and feedback.
"""

from __future__ import annotations


import json
from dataclasses import dataclass
from typing import Any

import anthropic

from shared.eval.runner import EvalResult


@dataclass
class JudgeRubric:
    """Rubric for LLM-as-judge evaluation."""

    criteria: str
    passing_description: str
    failing_description: str
    exam_domain: str  # D1-D5
    anti_patterns_to_check: list[str]


JUDGE_SYSTEM_PROMPT = """You are an exam grader for the Claude Certified Architect — Foundations (CCA-F) exam.

Evaluate the implementation against the provided rubric. Be strict — the exam tests
architectural judgment, not just whether code runs.

Respond with ONLY valid JSON:
{
    "reasoning": "Brief explanation of your evaluation",
    "score": "pass" or "fail",
    "feedback": "Specific, actionable feedback for the learner",
    "anti_patterns_found": ["list of anti-pattern numbers violated, e.g. '1', '3'"]
}"""


def create_llm_judge(
    rubric: JudgeRubric,
    model: str = "claude-sonnet-4-6-20250514",
) -> callable:
    """Create an LLM-as-judge grading function.

    Args:
        rubric: Evaluation rubric with criteria and anti-patterns.
        model: Claude model to use for judging.

    Returns:
        A grading function compatible with the Grader interface.
    """

    def judge_fn(expected: Any, actual: Any) -> EvalResult:
        client = anthropic.Anthropic()

        user_prompt = f"""## Rubric
Criteria: {rubric.criteria}
Passing: {rubric.passing_description}
Failing: {rubric.failing_description}
Exam Domain: {rubric.exam_domain}
Anti-patterns to check: {', '.join(rubric.anti_patterns_to_check)}

## Expected Output
{json.dumps(expected, indent=2) if not isinstance(expected, str) else expected}

## Actual Output
{json.dumps(actual, indent=2) if not isinstance(actual, str) else actual}

Evaluate the actual output against the rubric. Return JSON only."""

        response = client.messages.create(
            model=model,
            max_tokens=1024,
            temperature=0.0,
            system=JUDGE_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )

        # Parse judge response
        response_text = response.content[0].text
        try:
            verdict = json.loads(response_text)
        except json.JSONDecodeError:
            return EvalResult(
                task_id="judge",
                passed=False,
                score=0.0,
                feedback=f"Judge returned invalid JSON: {response_text[:200]}",
                latency_ms=0,
                cost_usd=_estimate_cost(response, model),
                grader_type="llm",
            )

        passed = verdict.get("score") == "pass"
        return EvalResult(
            task_id="judge",
            passed=passed,
            score=1.0 if passed else 0.0,
            feedback=verdict.get("feedback", "No feedback provided"),
            latency_ms=0,
            cost_usd=_estimate_cost(response, model),
            grader_type="llm",
        )

    return judge_fn


def _estimate_cost(response: anthropic.types.Message, model: str) -> float:
    """Estimate API cost from usage data."""
    input_tokens = response.usage.input_tokens
    output_tokens = response.usage.output_tokens

    # Pricing per million tokens
    pricing = {
        "claude-sonnet-4-6-20250514": {"input": 3.0, "output": 15.0},
        "claude-haiku-4-5-20251001": {"input": 1.0, "output": 5.0},
    }

    rates = pricing.get(model, {"input": 3.0, "output": 15.0})
    cost = (input_tokens * rates["input"] + output_tokens * rates["output"]) / 1_000_000
    return round(cost, 6)
