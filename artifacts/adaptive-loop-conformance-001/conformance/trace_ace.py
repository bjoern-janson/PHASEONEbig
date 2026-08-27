from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CORE = ROOT.parent / "adaptive-loop-protocol-001"
sys.path.insert(0, str(CORE))

from provenance import EvaluationContract, Provenance  # noqa: E402
from protocol import reconstitute  # noqa: E402
from transition import Candidate, Consequence, State  # noqa: E402


def _load(name: str) -> dict:
    return json.loads((ROOT / "evidence" / name).read_text())


def success_transition():
    e = _load("trace_structure_seed23.json")
    before = State(
        state_id="trace-success-state-0",
        incumbent_id="trace-objective-prior",
        incumbent_ref="trace://objective-prior",
    )
    candidate = Candidate(
        candidate_id="trace-objective-prior-plus-structure",
        parent_state_id=before.state_id,
        artifact_ref="trace://objective-prior+13-structure",
    )
    provenance = Provenance(
        experiment_id="trace-conformance-success-seed23",
        parent_state_id=before.state_id,
        incumbent_id=before.incumbent_id,
        candidate_id=candidate.candidate_id,
        distinction_id="trace-session-structure-distinction",
        transformation_id="trace-add-13-direct-structure-observables",
        decision_rule_id="strict-positive-c-improve",
        evaluation_contract=EvaluationContract(
            future_id="trace-session-heldout-seed23",
            viability_measure="negative log loss",
            independence_claim=(
                "seed 23 session holdout was not the construction surface used to select "
                "the structure distinction"
            ),
            transformation_scope=(
                "add the 13 predeclared direct transcript-structure observables to the "
                "objective-prior representation; conformance recomputation only"
            ),
        ),
    )
    consequence = Consequence(
        incumbent_viability=-float(e["incumbent_log_loss"]),
        candidate_viability=-float(e["candidate_log_loss"]),
        evidence_ref="evidence/trace_structure_seed23.json",
        metadata={"n": e["n"], "candidate_auc": e["candidate_auc"]},
    )
    return reconstitute(
        before=before,
        candidate=candidate,
        consequence=consequence,
        provenance=provenance,
        knowledge_note="fresh session future supports inheritance of this conformance candidate",
    )


def failure_transition():
    e = _load("trace_lexical_cold52.json")
    before = State(
        state_id="trace-failure-state-k3-survival-ledger",
        incumbent_id="groundup-001",
        incumbent_ref="trace://groundup-001#leaderboard-rank-20",
    )
    candidate = Candidate(
        candidate_id="groundup-001-plus-lexical-support-001",
        parent_state_id=before.state_id,
        artifact_ref="trace://groundup-001+objective-dialogue-lexical-support-001",
    )
    provenance = Provenance(
        experiment_id="trace-conformance-failure-cold52",
        parent_state_id=before.state_id,
        incumbent_id=before.incumbent_id,
        candidate_id=candidate.candidate_id,
        distinction_id="trace-objective-dialogue-dependency",
        transformation_id="trace-one-scalar-lexical-support-001",
        decision_rule_id="strict-positive-c-improve",
        evaluation_contract=EvaluationContract(
            future_id="trace-cold-objective-seed52",
            viability_measure="negative log loss",
            independence_claim=(
                "cold-objective seed 52 has zero objective overlap and zero session overlap; "
                "it was the predeclared hostile transport gate"
            ),
            transformation_scope="one predeclared objective-dialogue lexical-support scalar; no rescue",
        ),
    )
    consequence = Consequence(
        incumbent_viability=-float(e["incumbent_log_loss"]),
        candidate_viability=-float(e["candidate_log_loss"]),
        evidence_ref="evidence/trace_lexical_cold52.json",
        metadata={"n": e["n"], "historical_status": e["status"]},
    )
    return reconstitute(
        before=before,
        candidate=candidate,
        consequence=consequence,
        provenance=provenance,
        knowledge_note=(
            "candidate rejected; lexical support measurement remains killed while the broader "
            "session-objective dependency remains unresolved"
        ),
    )
