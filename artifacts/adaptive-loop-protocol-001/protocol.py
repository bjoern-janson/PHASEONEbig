from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from provenance import Provenance
from transition import Candidate, Consequence, KnowledgeEvent, State, Transition


class DecisionRule(Protocol):
    rule_id: str

    def __call__(self, consequence: Consequence) -> bool: ...


@dataclass(frozen=True)
class StrictPositiveCImprove:
    rule_id: str = "strict-positive-c-improve"

    def __call__(self, consequence: Consequence) -> bool:
        return consequence.c_improve > 0.0


def reconstitute(
    *,
    before: State,
    candidate: Candidate,
    consequence: Consequence,
    provenance: Provenance,
    decision_rule: DecisionRule | None = None,
    knowledge_note: str = "",
) -> Transition:
    """
    Apply the universal survival protocol to an already-constituted experiment.

    Outside the core: what D means, how T is built, what F/V mean, how future
    independence is established, what minimality means, and how the next D is found.

    Inside the core: identity, parentage, declared evaluation contract, precommitted
    rule identity, consequence, inherit/reject, append-only K, and provenance.
    """

    if candidate.parent_state_id != before.state_id:
        raise ValueError("candidate parent does not match incumbent state")
    if provenance.parent_state_id != before.state_id:
        raise ValueError("provenance parent does not match incumbent state")
    if provenance.incumbent_id != before.incumbent_id:
        raise ValueError("provenance incumbent does not match state incumbent")
    if provenance.candidate_id != candidate.candidate_id:
        raise ValueError("provenance candidate does not match candidate")

    rule = decision_rule or StrictPositiveCImprove()
    if rule.rule_id != provenance.decision_rule_id:
        raise ValueError("decision rule does not match precommitted rule identity")

    inherited = bool(rule(consequence))

    # Every evaluated experiment changes K, including a rejected transformation.
    event = KnowledgeEvent(
        experiment_id=provenance.experiment_id,
        distinction_id=provenance.distinction_id,
        transformation_id=provenance.transformation_id,
        c_improve=consequence.c_improve,
        inherited=inherited,
        note=knowledge_note,
    )
    next_knowledge = before.knowledge + (event,)

    if inherited:
        next_incumbent_id = candidate.candidate_id
        next_incumbent_ref = candidate.artifact_ref
    else:
        next_incumbent_id = before.incumbent_id
        next_incumbent_ref = before.incumbent_ref

    after = State(
        state_id=provenance.experiment_id,
        incumbent_id=next_incumbent_id,
        incumbent_ref=next_incumbent_ref,
        knowledge=next_knowledge,
    )

    return Transition(
        provenance=provenance,
        before=before,
        candidate=candidate,
        consequence=consequence,
        inherited=inherited,
        after=after,
    )
