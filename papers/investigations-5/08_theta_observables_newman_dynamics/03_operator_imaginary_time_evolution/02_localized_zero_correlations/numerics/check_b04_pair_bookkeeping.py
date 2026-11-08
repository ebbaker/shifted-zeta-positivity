#!/usr/bin/env python3
"""Exact bookkeeping for B04; no canonical-zero evaluation or certificate.

8 November 2026, America/New_York. Prepared for Edward Baker with
substantial OpenAI Codex assistance. Actual model/effort unavailable.
Uses the Python standard library. Prints a small JSON execution record.
"""

from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def kernel(x, y, h=Q(1)):
    return h * h / ((x - y) ** 2 + h * h)


def full_pair(zeros):
    # All test coordinates here lie in w's plateau and v's quadratic part.
    return sum(
        (y * y) * (v * v) * kernel(x, u)
        for j, (x, y) in enumerate(zeros)
        for k, (u, v) in enumerate(zeros)
        if j != k
    )


def folded_pair(upper):
    tensor = sum(
        y * y * v * v * kernel(x, u)
        for x, y in upper
        for u, v in upper
    )
    diagonal = sum(y**4 for _, y in upper)
    return 4 * tensor - 2 * diagonal


def main():
    p = list(map(Q, [1, 0, 0, -10, 15, -6]))
    p_squared = mul(p, p)
    transition_square = sum(c / (i + 1) for i, c in enumerate(p_squared))
    window_square = 1 + transition_square
    cases = [
        [(Q(0), Q(1, 4))],
        [(Q(0), Q(1, 4))] * 2,
        [(Q(-1, 4), Q(1, 4))] * 2 + [(Q(1, 4), Q(1, 3))],
    ]
    records = []
    for upper in cases:
        zeros = upper + [(x, -y) for x, y in upper] + [(Q(0), Q(0))] * 3
        direct, folded = full_pair(zeros), folded_pair(upper)
        assert direct == folded
        records.append({"upper_copies": len(upper), "direct": str(direct),
                        "folded": str(folded)})
    for m in (1, 2, 3):
        d = Q(1, 4)
        upper = [(Q(0), d)] * m
        assert folded_pair(upper) == (4 * m * m - 2 * m) * d**4
    assert full_pair([(Q(0), Q(0))] * 4) == 0
    assert 2 * Q(1, 2)**4 == Q(1, 8)

    # Recalculate bounds from derivative-product formulas, rather than
    # merely asserting the printed final coefficients.
    a0, ax, ay = Q(4), Q(15), Q(23, 2)  # h=b=1
    d = Q(96 + 41)
    d2 = a0 * d + 2 * ax * a0 + 2 * a0 * a0
    ddiag = 2 * a0 * d + 2 * ax * ax + 2 * ay * ay
    assert d2 == 700
    assert ddiag == Q(3621, 2)
    fourth_extra = 4 * ax * ax * 2 + 4 * ax * a0 * 6 + a0 * a0 * 24
    assert fourth_extra == 3624
    assert (Q(17, 2)**2 + 1) / 74 < 1
    assert (16 - 1) / Q(74) == Q(15, 74)
    assert 2 / Q(74) == Q(1, 37)

    source = Path(__file__)
    result = {
        "date_local": "2026-11-08",
        "timezone": "America/New_York",
        "run_at_utc": datetime.now(timezone.utc).isoformat(),
        "prepared_for": "Edward Baker",
        "llm_assistance": "substantial OpenAI Codex",
        "actual_model": None,
        "actual_effort": None,
        "status": "passed",
        "scope": "Exact rational normalization and multiplicity checks only; "
                 "no proof of analytic transfer, canonical smallness, or RH.",
        "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "folding_cases": records,
        "transition_square_integral": str(transition_square),
        "window_square_integral": str(window_square),
        "matched_D2": str(d2),
        "matched_Ddiag": str(ddiag),
        "matched_n_coefficient": str(4 * d2),
        "default_pair_signal": "1/8",
        "polynomial_control_field_error": "d^2/37",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
