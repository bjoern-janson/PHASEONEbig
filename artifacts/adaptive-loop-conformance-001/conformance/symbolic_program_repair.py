from __future__ import annotations

import hashlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CORE = ROOT.parent / "adaptive-loop-protocol-001"
sys.path.insert(0, str(CORE))

from provenance import EvaluationContract, Provenance  # noqa: E402
from protocol import reconstitute  # noqa: E402
from transition import Candidate, Consequence, State  # noqa: E402


PROGRAMS = {
    "incumbent": "def classify(x):\n    return 0\n",
    "parity_repair": "def classify(x):\n    return int(x % 2 == 0)\n",
    "sign_repair": "def classify(x):\n    return int(x < 0)\n",
}


def _program_id(name: str) -> str:
    h = hashlib.sha256(PROGRAMS[name].encode()).hexdigest()[:16]
    return f"program-{name}-{h}"


def _compile(program: str):
    ns = {}
    exec(program, {}, ns)
    return ns["classify"]


def _spec(x: int) -> int:
    return int(x % 2 == 0)


def _accuracy(program_name: str, future: tuple[int, ...]) -> float:
    fn = _compile(PROGRAMS[program_name])
    return sum(int(fn(x) == _spec(x)) for x in future) / len(future)


def _transition(*, candidate_name: str, distinction_id: str, transformation_id: str, future_id: str, future: tuple[int, ...], independence_claim: str):
    incumbent_id = _program_id("incumbent")
    candidate_id = _program_id(candidate_name)
    before = State(
        state_id=f"symbolic-{candidate_name}-state-0",
        incumbent_id=incumbent_id,
        incumbent_ref="program://incumbent-return-zero",
    )
    candidate = Candidate(
        candidate_id=candidate_id,
        parent_state_id=before.state_id,
        artifact_ref=f"program://{candidate_name}",
    )
    provenance = Provenance(
        experiment_id=f"symbolic-conformance-{candidate_name}",
        parent_state_id=before.state_id,
        incumbent_id=before.incumbent_id,
        candidate_id=candidate.candidate_id,
        distinction_id=distinction_id,
        transformation_id=transformation_id,
        decision_rule_id="strict-positive-c-improve",
        evaluation_contract=EvaluationContract(
            future_id=future_id,
            viability_measure="held-out behavioral accuracy",
            independence_claim=independence_claim,
            transformation_scope="one predicate/branch; program repair domain declares minimality scope",
            metadata={"future_inputs": list(future), "specification": "1 iff x is even"},
        ),
    )
    inc_v = _accuracy("incumbent", future)
    cand_v = _accuracy(candidate_name, future)
    consequence = Consequence(
        incumbent_viability=inc_v,
        candidate_viability=cand_v,
        evidence_ref=f"symbolic://heldout/{future_id}",
        metadata={"future_inputs": list(future)},
    )
    return reconstitute(
        before=before,
        candidate=candidate,
        consequence=consequence,
        provenance=provenance,
        knowledge_note=f"held-out behavior judged {candidate_name}",
    )


def success_transition():
    return _transition(
        candidate_name="parity_repair",
        distinction_id="symbolic-even-vs-odd",
        transformation_id="symbolic-add-parity-predicate",
        future_id="symbolic-parity-future-a",
        future=(-6, -5, 8, 9),
        independence_claim="held-out inputs were not used to define the parity repair candidate",
    )


def failure_transition():
    return _transition(
        candidate_name="sign_repair",
        distinction_id="symbolic-negative-vs-nonnegative",
        transformation_id="symbolic-add-sign-predicate",
        future_id="symbolic-sign-future-b",
        future=(-6, -5, 8, 9),
        independence_claim="held-out inputs were not used to define the sign-based repair candidate",
    )
