import math

from provenance import EvaluationContract, Provenance
from protocol import reconstitute
from transition import Candidate, Consequence, State


def prov(candidate_id: str, experiment_id: str = "exp-1") -> Provenance:
    return Provenance(
        experiment_id=experiment_id,
        parent_state_id="state-0",
        incumbent_id="r0",
        candidate_id=candidate_id,
        distinction_id="d1",
        transformation_id="t1",
        decision_rule_id="strict-positive-c-improve",
        evaluation_contract=EvaluationContract(
            future_id="future-1",
            viability_measure="domain-defined",
            independence_claim="declared independent by domain",
            transformation_scope="declared minimal by domain",
        ),
    )


def test_positive_consequence_inherits_candidate_and_updates_k():
    before = State(state_id="state-0", incumbent_id="r0", incumbent_ref="artifact://r0")
    candidate = Candidate(candidate_id="r1", parent_state_id="state-0", artifact_ref="artifact://r1")
    consequence = Consequence(incumbent_viability=0.50, candidate_viability=0.60)

    t = reconstitute(
        before=before,
        candidate=candidate,
        consequence=consequence,
        provenance=prov("r1"),
    )

    assert t.inherited is True
    assert t.after.incumbent_id == "r1"
    assert t.after.incumbent_ref == "artifact://r1"
    assert len(t.after.knowledge) == 1
    assert math.isclose(t.after.knowledge[-1].c_improve, 0.10, rel_tol=0.0, abs_tol=1e-12)


def test_nonpositive_consequence_rejects_candidate_but_updates_k():
    before = State(state_id="state-0", incumbent_id="r0", incumbent_ref="artifact://r0")
    candidate = Candidate(candidate_id="r1", parent_state_id="state-0", artifact_ref="artifact://r1")
    consequence = Consequence(incumbent_viability=0.60, candidate_viability=0.59)

    t = reconstitute(
        before=before,
        candidate=candidate,
        consequence=consequence,
        provenance=prov("r1"),
        knowledge_note="candidate rejected; search state still advances",
    )

    assert t.inherited is False
    assert t.after.incumbent_id == "r0"
    assert t.after.incumbent_ref == "artifact://r0"
    assert t.after.knowledge != before.knowledge
    assert t.after.knowledge[-1].inherited is False


def test_zero_consequence_is_rejected_but_k_changes():
    before = State(state_id="state-0", incumbent_id="r0", incumbent_ref="artifact://r0")
    candidate = Candidate(candidate_id="r1", parent_state_id="state-0", artifact_ref="artifact://r1")
    consequence = Consequence(incumbent_viability=0.5, candidate_viability=0.5)

    t = reconstitute(
        before=before,
        candidate=candidate,
        consequence=consequence,
        provenance=prov("r1"),
    )

    assert t.inherited is False
    assert t.after.incumbent_ref == before.incumbent_ref
    assert len(t.after.knowledge) == len(before.knowledge) + 1


def test_parentage_mismatch_is_rejected():
    before = State(state_id="state-0", incumbent_id="r0", incumbent_ref="artifact://r0")
    candidate = Candidate(candidate_id="r1", parent_state_id="wrong-parent", artifact_ref="artifact://r1")
    consequence = Consequence(incumbent_viability=0.5, candidate_viability=0.6)

    try:
        reconstitute(
            before=before,
            candidate=candidate,
            consequence=consequence,
            provenance=prov("r1"),
        )
    except ValueError as e:
        assert "candidate parent" in str(e)
    else:
        raise AssertionError("expected parentage violation to be rejected")
