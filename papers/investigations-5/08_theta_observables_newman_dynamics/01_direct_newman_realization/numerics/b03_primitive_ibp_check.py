"""Exact local normalization checks for Brainstorm06; no theta sampling.

2026-11-09 America/New_York, prepared for Edward Baker with OpenAI Codex
LLM assistance, chat0007. Actual model/effort unavailable in capture.
Run from any directory; writes only the small adjacent execution record.
"""

from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json


def multiply(left, right):
    out = {}
    for (i, j), a in left.items():
        for (k, l), b in right.items():
            degree = (i + k, j + l)
            out[degree] = out.get(degree, F(0)) + a * b
    return {degree: value for degree, value in out.items() if value}


def main():
    # Formal commuting derivative variables A=d/da, B=d/db.
    plus = {(2, 0): F(1), (1, 1): F(2), (0, 2): F(1), (0, 0): F(-1)}
    minus = {**plus, (1, 1): F(-2)}
    expected = {(4, 0): F(1), (0, 4): F(1), (2, 2): F(-2),
                (2, 0): F(-2), (0, 2): F(-2), (0, 0): F(1)}
    assert multiply(plus, minus) == expected

    # A distinct elementary primitive: psi=e^(-2u)/4, psi'(0)=-1/2,
    # Phi=(psi''-psi)/8=3e^(-2u)/32. Its moments are exact rationals.
    def primitive_moment(j):
        return F(factorial(j), 4 * 2 ** (j + 1))

    def source_moment(j):
        return F(3, 8) * primitive_moment(j)

    def transferred_moment(j):
        return ((j * (j - 1) * primitive_moment(j - 2)) if j >= 2 else F(0)) - primitive_moment(j)

    cases = []
    for i in range(0, 9, 2):
        for j in range(0, 9, 2):
            left = source_moment(i) * source_moment(j)
            di, dj = transferred_moment(i), transferred_moment(j)
            bulk = di * dj
            faces = F(1, 2) * ((dj if i == 0 else 0) + (di if j == 0 else 0))
            corner = F(1, 4) if i == j == 0 else F(0)
            right = (bulk + faces + corner) / 64
            assert left == right, (i, j, left, right)
            cases.append([i, j])

    # Actual A0 test at lambda=X=v=0 is (p^2+q^2)/2.
    j0, j2 = primitive_moment(0), primitive_moment(2)
    bulk = j0 * j2 - 2 * j0 ** 2
    face = j0 - j2 / 2
    direct = source_moment(0) * source_moment(2)
    assert (bulk + face) / 64 == direct
    assert bulk / 64 != direct  # This test detects a dropped face.

    record = {
        "date": "2026-11-09", "timezone": "America/New_York",
        "prepared_for": "Edward Baker", "assistance": "OpenAI Codex LLM",
        "actual_model": None, "actual_reasoning_effort": None,
        "thread_id": "01a1c389-3fe9-7930-8223-c935cc1920e1",
        "turn_id": "01a1c3c2-5721-7421-a134-8d0037d5413a",
        "task": "TND-D-B03 author-requested primitive/lattice addendum",
        "status": "passed",
        "evidence": "Exact rational algebra, same-assistant local check only.",
        "operator_identity": "passed",
        "even_monomial_cases": cases,
        "limit_check": {"bulk": str(bulk), "face": str(face), "A0": str(direct),
                        "detects_missing_face": True},
        "scope": "No theta values, numerical sign estimate, interval certificate, or independent assessment.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    destination = Path(__file__).with_name("02_TND_D_B03_PRIMITIVE_IBP_CHECK_20261109.json")
    destination.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "passed", "record": str(destination),
                      "limit_check": record["limit_check"]}))


if __name__ == "__main__":
    main()
