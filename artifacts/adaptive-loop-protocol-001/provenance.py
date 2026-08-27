from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class EvaluationContract:
    """A declaration supplied by the domain; the core records, but does not prove, it."""

    future_id: str
    viability_measure: str
    independence_claim: str
    transformation_scope: str
    metadata: Mapping[str, Any] | None = None


@dataclass(frozen=True)
class Provenance:
    experiment_id: str
    parent_state_id: str
    incumbent_id: str
    candidate_id: str
    distinction_id: str
    transformation_id: str
    decision_rule_id: str
    evaluation_contract: EvaluationContract
