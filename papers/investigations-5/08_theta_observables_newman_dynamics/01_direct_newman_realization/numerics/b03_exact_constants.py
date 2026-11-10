"""Small exact-algebra check for B03 Note09, not a numerical theta test.

2026-11-09 America/New_York. Prepared for Edward Baker with OpenAI Codex
LLM assistance, chat0007. Actual model and effort unavailable in capture.
Run from any directory; writes the small adjacent execution record.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def main():
    # Extremes on p/r in [0,1/6], q/r in [5/6,7/6].
    difference_min = F(5, 6) - F(1, 6)
    difference_max = F(7, 6)
    sum_min = F(5, 6)
    sum_max = F(7, 6) + F(1, 6)
    assert F(2, 3) <= difference_min <= difference_max <= F(4, 3)
    assert F(2, 3) <= sum_min <= sum_max <= F(4, 3)
    square_sum_floor = 2 * F(5, 6) ** 2
    kernel_coefficient = F(1, 4) * F(1, 2) * square_sum_floor
    area = F(1, 6) * (F(7, 6) - F(5, 6))
    mass_coefficient = kernel_coefficient * area
    assert kernel_coefficient == F(25, 144)
    assert mass_coefficient == F(25, 2592)
    # Coefficients of the inherited error polynomial at variance = time.
    error = {
        "bC_mu1_eps_3_over_2": 4 + F(10, 3),
        "bD_eps_2": F(3 + 1, 2),
        "C_squared_eps_2": 1 + 2 + F(5, 4),
        "CD_mu1_eps_5_over_2": F(1, 3) + F(3, 2),
        "D_squared_eps_3": F(1, 2),
    }
    assert list(error.values()) == [F(22, 3), F(2), F(17, 4), F(11, 6), F(1, 2)]
    record = {
        "date": "2026-11-09", "timezone": "America/New_York",
        "prepared_for": "Edward Baker", "assistance": "OpenAI Codex LLM",
        "actual_model": None, "actual_reasoning_effort": None,
        "thread_id": "01a1c389-3fe9-7930-8223-c935cc1920e1",
        "task": "TND-D-B03 r3, one local clarification",
        "evidence": "Exact rational algebra only; analytical trigonometric/source proof is in Note09.",
        "phase_intervals_in_units_of_pi": {
            "q_minus_p": [str(difference_min), str(difference_max)],
            "q_plus_p": [str(sum_min), str(sum_max)],
        },
        "kernel_negative_coefficient": str(kernel_coefficient),
        "rectangle_area_coefficient": str(area),
        "negative_mass_coefficient": str(mass_coefficient),
        "error_coefficients": {k: str(v) for k, v in error.items()},
        "status": "passed",
        "scope": "No theta values, interval certificate, event exclusion, precision claim, or cost comparison.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    destination = Path(__file__).with_name("01_TND_D_B03_EXACT_CONSTANT_CHECK_20261109.json")
    destination.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "passed", "record": str(destination)}))


if __name__ == "__main__":
    main()
