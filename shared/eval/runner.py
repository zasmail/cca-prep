"""Evaluation framework runner for CCA-F exam prep exercises.

Runs test cases through implementation functions, applies multiple graders,
and produces weighted scores with a configurable passing threshold.
"""

from __future__ import annotations


import time
from dataclasses import dataclass, field
from typing import Any, Callable

from shared.eval.metrics import aggregate_results


@dataclass
class EvalResult:
    """Result of a single evaluation test case."""

    task_id: str
    passed: bool
    score: float  # 0.0 to 1.0
    feedback: str
    latency_ms: float
    cost_usd: float = 0.0
    grader_type: str = "rule"  # "rule", "llm", "composite"


@dataclass
class Grader:
    """A grading function with a weight for composite scoring."""

    name: str
    fn: Callable[[Any, Any], EvalResult]  # (expected, actual) -> EvalResult
    weight: float = 1.0


@dataclass
class TestCase:
    """A single test case for evaluation."""

    task_id: str
    input_data: Any
    expected: Any
    metadata: dict = field(default_factory=dict)


def run_eval_suite(
    test_cases: list[TestCase],
    implementation_fn: Callable[[Any], Any],
    graders: list[Grader],
    passing_threshold: float = 0.7,
) -> list[EvalResult]:
    """Run a suite of test cases through an implementation function.

    Each test case is run through the implementation_fn, then scored by
    all graders. The final score is a weighted average across graders.

    Args:
        test_cases: List of test cases with inputs and expected outputs.
        implementation_fn: Function under test — takes input, returns output.
        graders: List of graders with weights for composite scoring.
        passing_threshold: Minimum score to pass (default 0.7).

    Returns:
        List of EvalResult, one per test case.
    """
    results: list[EvalResult] = []
    total_weight = sum(g.weight for g in graders)

    for case in test_cases:
        start = time.perf_counter()
        try:
            actual = implementation_fn(case.input_data)
        except Exception as e:
            elapsed_ms = (time.perf_counter() - start) * 1000
            results.append(EvalResult(
                task_id=case.task_id,
                passed=False,
                score=0.0,
                feedback=f"Implementation raised exception: {e}",
                latency_ms=elapsed_ms,
                grader_type="error",
            ))
            continue

        elapsed_ms = (time.perf_counter() - start) * 1000

        # Run all graders and compute weighted score
        weighted_score = 0.0
        feedback_parts: list[str] = []
        total_cost = 0.0

        for grader in graders:
            grader_result = grader.fn(case.expected, actual)
            weighted_score += grader_result.score * (grader.weight / total_weight)
            feedback_parts.append(f"[{grader.name}] {grader_result.feedback}")
            total_cost += grader_result.cost_usd

        passed = weighted_score >= passing_threshold

        results.append(EvalResult(
            task_id=case.task_id,
            passed=passed,
            score=weighted_score,
            feedback=" | ".join(feedback_parts),
            latency_ms=elapsed_ms,
            cost_usd=total_cost,
            grader_type="composite" if len(graders) > 1 else graders[0].name,
        ))

    return results
