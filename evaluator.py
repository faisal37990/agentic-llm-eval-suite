"""
Agentic LLM Evaluation & Adversarial Verifier Harness
Author: Faisal Sharif (@faisal37990)
Description: Programmatic JSON schema verification and multi-dimensional rubric scoring
             for frontier LLM multi-turn agentic evaluation.
"""

import json
import jsonschema
from typing import Dict, Any, List

SAMPLE_SCHEMA = {
    "type": "object",
    "required": ["case_id", "financial_metrics", "strategic_recommendation", "confidence_score"],
    "properties": {
        "case_id": {"type": "string"},
        "financial_metrics": {
            "type": "object",
            "required": ["ebitda_margin", "roi_percentage", "projected_revenue"],
            "properties": {
                "ebitda_margin": {"type": "number", "minimum": -100.0, "maximum": 100.0},
                "roi_percentage": {"type": "number"},
                "projected_revenue": {"type": "number", "minimum": 0}
            }
        },
        "strategic_recommendation": {"type": "string", "minLength": 15},
        "confidence_score": {"type": "number", "minimum": 0.0, "maximum": 1.0}
    }
}

class LLMEvaluationHarness:
    def __init__(self, schema: Dict[str, Any]):
        self.schema = schema

    def verify_schema(self, model_output: Dict[str, Any]) -> (bool, str):
        """Validates structured model output against strict JSON schema."""
        try:
            jsonschema.validate(instance=model_output, schema=self.schema)
            return True, "Valid JSON schema"
        except jsonschema.exceptions.ValidationError as e:
            return False, f"Schema validation error: {e.message}"

    def score_rubric(self, output: Dict[str, Any], golden_solution: Dict[str, Any]) -> Dict[str, float]:
        """Calculates multi-dimensional rubric score against golden reference."""
        scores = {}
        # 1. Numeric precision for financial metrics
        model_metrics = output.get("financial_metrics", {})
        golden_metrics = golden_solution.get("financial_metrics", {})
        
        diffs = []
        for key in golden_metrics:
            if key in model_metrics and golden_metrics[key] != 0:
                rel_diff = abs(model_metrics[key] - golden_metrics[key]) / abs(golden_metrics[key])
                diffs.append(max(0.0, 1.0 - rel_diff))
        
        scores["accuracy"] = (sum(diffs) / len(diffs)) if diffs else 0.0
        scores["format_compliance"] = 1.0 if self.verify_schema(output)[0] else 0.0
        scores["overall"] = round((scores["accuracy"] * 0.7) + (scores["format_compliance"] * 0.3), 3)
        return scores

if __name__ == "__main__":
    print("=" * 65)
    print("  FAISAL SHARIF — AGENTIC LLM EVALUATION HARNESS")
    print("=" * 65)
    harness = LLMEvaluationHarness(SAMPLE_SCHEMA)
    
    mock_agent_output = {
        "case_id": "CASE-BIZ-2026-09",
        "financial_metrics": {
            "ebitda_margin": 18.5,
            "roi_percentage": 24.2,
            "projected_revenue": 14500000.0
        },
        "strategic_recommendation": "Consolidate supplier tiers to capture 15% procurement savings while maintaining SLA.",
        "confidence_score": 0.94
    }
    
    golden = {
        "financial_metrics": {
            "ebitda_margin": 18.2,
            "roi_percentage": 25.0,
            "projected_revenue": 15000000.0
        }
    }
    
    is_valid, msg = harness.verify_schema(mock_agent_output)
    print(f"[Schema Check]: {msg}")
    rubric = harness.score_rubric(mock_agent_output, golden)
    print(f"[Rubric Scores]: Accuracy: {rubric['accuracy']:.1%}, Format: {rubric['format_compliance']:.1%}, Overall: {rubric['overall']}")
    print("=" * 65)
