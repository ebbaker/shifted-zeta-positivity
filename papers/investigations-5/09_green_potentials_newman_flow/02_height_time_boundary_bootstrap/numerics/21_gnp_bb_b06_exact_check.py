#!/usr/bin/env python3
"""Finite rational/provenance checks for B06; no field evaluation or certificate.

Prepared for Edward Baker, 13 November 2026, with OpenAI Codex assistance.
Actual root model and reasoning effort are unavailable in recorded metadata.
"""
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
EXPECTED_E09 = "e3a10effbb7892c8e58f2f5cbc561ad00b6c9f0ea18fd606dc3dff353f1ce1e2"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    a, b, h = F(3, 64), F(5, 16), F(1, 32)
    weights = lambda p: -F(65, 64) * p + p * p / 4
    checks = {
        "low_endpoint_weight": (weights(a), -F(771, 16384)),
        "high_endpoint_weight": (weights(b), -F(75, 256)),
        "middle_absolute_mass": (b / 16, F(5, 256)),
        "common_freezing_error": (h - 1 + b / 16, -F(243, 256)),
        "low_cutoff_movement": (a + h - 1, -F(59, 64)),
        "high_cutoff_movement": (b + h - 1, -F(21, 32)),
        "cell_population_growth_at_lower_edge": (a - h, F(1, 64)),
        "one_cell_mass": (b / 16 - h, -F(3, 256)),
        "one_cell_energy": (b / 8 - 2 * h, -F(3, 128)),
        "all_cells_energy": (b / 8 - h, F(1, 128)),
        "one_cell_full_cross": ((b / 8 - h) / 2 + b / 16 - h, -F(1, 128)),
        "quartic_packet_weight_in_D": (-F(65, 64) + F(1, 16), -F(61, 64)),
        "quartic_packet_norm_in_D": (F(1, 5) - F(61, 64), -F(241, 320)),
        "quartic_packet_energy_in_D": (F(2, 5) - F(61, 32), -F(241, 160)),
        "quartic_packet_energy_in_U": ((F(2, 5) - F(61, 32)) / 4, -F(241, 640)),
        "quartic_packet_norm_in_U": ((F(1, 5) - F(61, 64)) / 4, -F(241, 1280)),
        "quartic_packet_full_cross_in_U": ((F(1, 5) - F(61, 64)) / 4 + F(1, 256), -F(59, 320)),
        "quartic_window_relative_phase_in_D": (4 * h + F(1, 5) - 1, -F(27, 40)),
        "quartic_remainder_coefficient_of_pi": (F(24, 5) / 4**5, F(3, 640)),
    }
    for name, (actual, expected) in checks.items():
        assert actual == expected, (name, actual, expected)
    taylor = [(-1) ** (k + 1) * F(12, k) for k in range(1, 5)]
    assert taylor == [12, -6, 4, -3]
    assert all(x.denominator == 1 for x in taylor)
    assert F(3, 640) * 4 < F(1, 32)  # elementary pi < 4 is sufficient
    assert F(1, 8192) < F(771, 16384) < F(243, 256)
    assert a > F(1, 32) and b < F(1, 2)
    assert a < F(1, 4) < b

    inputs = [
        "research-progress/handoffs/GNP-BB-B06-r1.md",
        "notes/15_GNP_BB_B04_SIGNED_GREEN_ACQUISITION_20261113.md",
        "notes/20_GNP_BB_B05_LOCAL_MOMENT_DECISION_20261113.md",
        "notes/21_GNP_BB_B05_LOCAL_MOMENT_UPPER_ESTIMATES_20261113.md",
        "notes/22_GNP_BB_B05_MOVING_TAIL_RESONATOR_TEST_20261113.md",
        "notes/23_GNP_BB_E09_LOCALIZATION_AND_RESONATOR_MEANS_20261113.md",
        "notes/24_GNP_BB_CONTINUATION_AFTER_LOCAL_MOMENT_SCREEN_20261113.md",
        "reviews/08_GNP_BB_B05_INTEGRATION_ASSESSMENT_20261113.md",
        "reviews/09_GNP_BB_E09_ADDITIONAL_AGENT_REVIEW_20261113.md",
    ]
    assert digest(BASE / inputs[5]) == EXPECTED_E09
    proof = BASE / "notes/25_GNP_BB_B06_SHORT_WINDOW_AND_ACTUAL_PACKET_20261113.md"
    record = {
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "research_date_local": "2026-11-13",
        "timezone": "America/New_York",
        "prepared_for": "Edward Baker",
        "llm_assistance": "OpenAI Codex; same-assistant analytical work and checking",
        "actual_root_model": None,
        "actual_root_reasoning_effort": None,
        "thread_id": "01a1d6f3-5a11-7741-acc9-15b358cb7980",
        "scope": "Exact rational arithmetic and source identity only; not an analytic proof or interval certificate",
        "field_evaluations": 0,
        "height_or_support_scan": False,
        "exact_powers": {k: str(v[0]) for k, v in checks.items()},
        "integer_taylor_coefficients_after_2pi": [int(x) for x in taylor],
        "E09_matches_E10_review_hash": True,
        "inputs": [{"path": p, "bytes": (BASE / p).stat().st_size, "sha256": digest(BASE / p)} for p in inputs],
        "proof": {"path": str(proof.relative_to(BASE)), "bytes": proof.stat().st_size, "sha256": digest(proof)},
        "script_sha256": digest(Path(__file__)),
        "disposition": "All listed finite arithmetic and source-identity checks passed; analytical review is separate",
    }
    out = BASE / "numerics/21_GNP_BB_B06_INPUTS_AND_CHECKS_20261113.json"
    out.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "passed", "rational_powers": len(checks), "record": str(out), "proof_sha256": record["proof"]["sha256"]}))


if __name__ == "__main__":
    main()
