from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFORMANCE = ROOT / "conformance"
sys.path.insert(0, str(CONFORMANCE))

from symbolic_program_repair import failure_transition as symbolic_failure  # noqa: E402
from symbolic_program_repair import success_transition as symbolic_success  # noqa: E402
from trace_ace import failure_transition as trace_failure  # noqa: E402
from trace_ace import success_transition as trace_success  # noqa: E402

EXPECTED = {
    "protocol.py": "68e34f3c3d21bc7224f96e2c50c0522fecda4646cce9ef5dee75e4da68660cd6",
    "transition.py": "0a34104e2365a1a87fd0d7c63ba4aaa9a90de362f783bccce621c25d30e7add1",
    "provenance.py": "4fd1e0743e99f6bc01eb9c191e203ff5c2cc206cd0b681157c6c6915112c2d17",
    "tests/test_protocol.py": "6cc9a1c170a95314792de57e61db7ecbacd9c31892156570f38df228006704da",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_frozen_protocol_source_hashes_are_recorded():
    core = ROOT.parent / "adaptive-loop-protocol-001"
    for rel, expected in EXPECTED.items():
        assert sha(core / rel) == expected


def _assert_success(t):
    assert t.consequence.c_improve > 0
    assert t.inherited is True
    assert t.after.incumbent_id == t.candidate.candidate_id
    assert len(t.after.knowledge) == len(t.before.knowledge) + 1


def _assert_failure(t):
    assert t.consequence.c_improve <= 0
    assert t.inherited is False
    assert t.after.incumbent_id == t.before.incumbent_id
    assert t.after.incumbent_ref == t.before.incumbent_ref
    assert len(t.after.knowledge) == len(t.before.knowledge) + 1


def test_trace_success_branch():
    _assert_success(trace_success())


def test_trace_failure_branch():
    _assert_failure(trace_failure())


def test_symbolic_success_branch():
    _assert_success(symbolic_success())


def test_symbolic_failure_branch():
    _assert_failure(symbolic_failure())
