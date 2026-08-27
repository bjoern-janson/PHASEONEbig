from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Tuple

from provenance import Provenance


@dataclass(frozen=True)
class KnowledgeEvent:
    experiment_id: str
    distinction_id: str
    transformation_id: str
    c_improve: float
    inherited: bool
    note: str = ""


@dataclass(frozen=True)
class State:
    """Protocol state: active artifact reference R plus append-only research state K."""

    state_id: str
    incumbent_id: str
    incumbent_ref: str
    knowledge: Tuple[KnowledgeEvent, ...] = ()


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    parent_state_id: str
    artifact_ref: str


@dataclass(frozen=True)
class Consequence:
    incumbent_viability: float
    candidate_viability: float
    evidence_ref: str | None = None
    metadata: Any = None

    @property
    def c_improve(self) -> float:
        return self.candidate_viability - self.incumbent_viability


@dataclass(frozen=True)
class Transition:
    provenance: Provenance
    before: State
    candidate: Candidate
    consequence: Consequence
    inherited: bool
    after: State
