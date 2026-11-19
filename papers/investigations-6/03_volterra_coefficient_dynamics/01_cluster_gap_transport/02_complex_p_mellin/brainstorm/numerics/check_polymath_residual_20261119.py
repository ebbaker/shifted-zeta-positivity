"""Exact algebra checks for Discussion11; no canonical source evaluation.

19 November 2026. For Edward Baker with OpenAI Codex assistance.
Chat registry configuration: gpt-6-astra, reasoning effort max.
"""
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


# Polynomial keys are exponents of (t, a, b, c).
def add(*polys):
    out = {}
    for poly in polys:
        for powers, coefficient in poly.items():
            out[powers] = out.get(powers, F(0)) + coefficient
    return {k: v for k, v in out.items() if v}


def scale(poly, scalar):
    return {k: scalar * v for k, v in poly.items() if scalar * v}


def mul(left, right):
    out = {}
    for a, av in left.items():
        for b, bv in right.items():
            key = tuple(x + y for x, y in zip(a, b))
            out[key] = out.get(key, F(0)) + av * bv
    return {k: v for k, v in out.items() if v}


def partial(poly, coordinate):
    out = {}
    for powers, coefficient in poly.items():
        if powers[coordinate]:
            reduced = list(powers)
            reduced[coordinate] -= 1
            out[tuple(reduced)] = coefficient * powers[coordinate]
    return out


def variable(index):
    powers = [0] * 4
    powers[index] = 1
    return {tuple(powers): F(1)}


def main():
    t, a, b, c = (variable(i) for i in range(4))
    # q = (log p)_s. Only a_s=b and b_s=c enter q_s.
    q = add(a, scale(mul(t, mul(a, b)), F(1, 2)))
    qs = add(mul(partial(q, 1), b), mul(partial(q, 2), c))
    from_derivatives = add(scale(mul(a, a), F(1, 4)),
                           scale(add(mul(q, q), qs), F(-1, 4)))
    expected = {
        (0, 0, 1, 0): F(-1, 4),
        (1, 2, 1, 0): F(-1, 4),
        (1, 0, 2, 0): F(-1, 8),
        (1, 1, 0, 1): F(-1, 8),
        (2, 2, 2, 0): F(-1, 16),
    }
    assert from_derivatives == expected
    threshold, start = F(1, 4), F(1, 2)
    initial_D = 2 * (start - threshold)
    duration = start - threshold
    margin = initial_D - 2 * duration
    assert margin == 0
    # s=(1+iz)/2 gives d_z^2 = -d_s^2/4, for either sign.
    assert complex(0, 0.5) ** 2 == complex(-0.25, 0)
    record = {
        "date": "2026-11-19",
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "prepared_for": "Edward Baker",
        "llm_assistance": "OpenAI Codex",
        "recorded_configuration": {"model": "gpt-6-astra", "reasoning_effort": "max",
                                   "provenance": "guarded research chat registry"},
        "status": "exact algebra checks; same-assistant; not a canonical bound",
        "variables": ["t", "a=alpha-log(n)", "b=alpha_prime", "c=alpha_double_prime"],
        "heat_defect_coefficients": [
            {"powers": list(k), "coefficient": str(v)} for k, v in sorted(expected.items())
        ],
        "formal_jet_identity_passed": True,
        "physical_second_derivative_factor": "-1/4",
        "colliding_control": {
            "field_and_reference": "H=P=z^2-2(t-T)",
            "T": str(threshold), "t_start": str(start),
            "field_error": "0", "heat_defect": "0",
            "initial_D": str(initial_D), "backward_collision_duration": str(duration),
            "drift_defect": "2", "strict_margin_at_collision": str(margin),
            "outcome": "strict protection fails at merger despite zero approximation error",
        },
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    destination = Path(__file__).with_name("06_POLYMATH_RESIDUAL_ALGEBRA_20261119.json")
    destination.write_text(json.dumps(record, indent=2) + "\n")
    print("Formal residual identity and colliding quadratic control checked.")


if __name__ == "__main__":
    main()
