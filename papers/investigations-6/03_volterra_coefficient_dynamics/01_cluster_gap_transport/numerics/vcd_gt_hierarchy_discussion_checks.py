"""Exact algebra checks for the 17 November 2026 hierarchy discussion.

Prepared for Edward Baker with OpenAI Codex LLM assistance.
Actual model/effort unavailable. Same-assistant checks, no specialist review.
No canonical theta evaluations or numerical zero search.
"""

from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def deriv(a):
    return [i * a[i] for i in range(1, len(a))] or [F(0)]


def value(a, x):
    out = F(0)
    for v in reversed(a):
        out = out * x + v
    return out


def mod_quadratic(a, d):
    """Remainder modulo z^2-d, with ascending polynomial coefficients."""
    out = [F(0), F(0)]
    for k, v in enumerate(a):
        out[k % 2] += v * d ** (k // 2)
    return out


def check_case(d, exterior):
    a = [F(1)]
    for w in exterior:
        a = mul(a, [-w, F(1)])
    f = mul([-d, F(0), F(1)], a)
    fz, fzz = deriv(f), deriv(deriv(f))
    a0, a1 = mod_quadratic(a, d)
    r0, r1 = mod_quadratic([-v for v in fzz], d)
    # F_t=-F_zz = Q_t A + Q A_t. Solve the two remainder equations.
    det = 2 * d * a1 * a1 - 2 * a0 * a0
    assert det
    cp = (-a1 * r0 + a0 * r1) / det
    dp = (-2 * d * a1 * r1 + 2 * a0 * r0) / det
    root_velocities = [value(fzz, w) / value(fz, w) for w in exterior]
    m = [1 / (w * w - d) for w in exterior]
    mp = [
        (dp - 2 * w * (velocity - cp)) * mj * mj
        for w, velocity, mj in zip(exterior, root_velocities, m)
    ]
    s = {p: sum((mj ** p for mj in m), F(0)) for p in range(1, 7)}
    t2 = sum((w * mj * mj for w, mj in zip(exterior, m)), F(0))
    actual_m = sum(mp, F(0))
    actual_s2 = 2 * sum((mj * dmj for mj, dmj in zip(m, mp)), F(0))
    predicted_m = 2 * s[1] ** 2 - 12 * s[2] - 16 * d * s[3]
    predicted_s2 = (
        8 * s[1] * s[2] - 32 * s[3]
        + 4 * d * s[2] ** 2 - 40 * d * s[4] + 4 * t2 ** 2
    )
    assert dp == 2 - 4 * s[1] * d
    assert actual_m == predicted_m
    assert actual_s2 == predicted_s2
    return {
        "D": str(d),
        "exterior": [str(w) for w in exterior],
        "center_derivative_from_heat_remainder": str(cp),
        "D_derivative_from_heat_remainder": str(dp),
        "M_derivative": str(actual_m),
        "S2_derivative": str(actual_s2),
        "T2": str(t2),
        "S1_through_S6": [str(s[p]) for p in range(1, 7)],
    }


def main():
    cases = [
        check_case(d, [F(w) for w in exterior])
        for d in [F(-1, 4), F(0), F(1, 4)]
        for exterior in [[], [2], [2, 3], [2, -3], [2, 3, -4], [-2, -3]]
    ]
    plus = check_case(F(1, 4), [F(2), F(3)])
    minus = check_case(F(1, 4), [F(2), F(-3)])
    assert plus["S1_through_S6"] == minus["S1_through_S6"]
    assert plus["S2_derivative"] != minus["S2_derivative"]
    # The entire S(p) agrees: denominator multisets, not only six moments.
    assert sorted(w * w - F(1, 4) for w in [F(2), F(3)]) == sorted(
        w * w - F(1, 4) for w in [F(2), F(-3)]
    )
    q = check_case(F(0), [])
    assert q["D_derivative_from_heat_remainder"] == "2"
    # The even quartic control at its target double: reflected exterior
    # has two occurrences w=-2a; the confluent S2 identity is checked
    # directly using its symmetric pair coordinates.
    a = F(11)
    m_at_double = F(1, 2) / (a * a)
    c_prime = F(2) / a
    d_prime = F(2)
    # S2=(c^2+D)/(8*c^2*(c^2-D)^2) for the reflected exterior pair.
    # At the double, c'=2/a and D'=2 follow from the explicit quartic.
    s2_prime_from_coordinates = (
        -c_prime / (2 * a ** 5) + 3 * d_prime / (8 * a ** 6)
    )
    s1, s2, s3, s4 = (
        2 * (1 / (4 * a * a)) ** p for p in range(1, 5)
    )
    t2 = -1 / (4 * a ** 3)
    assert s1 == m_at_double
    assert 8 * s1 * s2 - 32 * s3 + 4 * t2 ** 2 == s2_prime_from_coordinates
    record = {
        "date": "2026-11-17",
        "prepared_for": "Edward Baker",
        "llm_assistance": "OpenAI Codex",
        "actual_model": None,
        "actual_effort": None,
        "thread_id": "01a1eb96-c257-77a3-96be-ee1cb0279757",
        "turn_id": "01a1ec23-2a18-7653-aca5-eb33ced7ef51",
        "status": "same-assistant exact-arithmetic checks; no independent review",
        "scope": "Finite polynomial heat fields; three target discriminant signs, including a target double. No canonical theta evaluation.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "cases": cases,
        "checks_passed": {
            "gap_law": len(cases),
            "M_law": len(cases),
            "S2_law": len(cases),
            "same_full_denominator_multiset_different_S2_derivative": True,
            "quadratic_double_slope": True,
            "even_quartic_target_and_exterior_double_S2_law": True,
        },
        "nonclosure_example": {"first": plus, "second": minus},
        "limitations": [
            "Examples for nonclosure are real polynomials, not even canonical theta fields.",
            "This does not exclude closure with additional spatial observables.",
            "No signed theta bound, passage margin, or B12 activation.",
        ],
    }
    destination = Path(__file__).with_name(
        "25_VCD_GT_HIERARCHY_DISCUSSION_CHECKS_20261117.json"
    )
    destination.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "passed", "cases": len(cases),
                      "record": str(destination)}))


if __name__ == "__main__":
    main()
