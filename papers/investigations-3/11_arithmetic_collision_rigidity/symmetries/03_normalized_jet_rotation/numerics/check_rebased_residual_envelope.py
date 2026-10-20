#!/usr/bin/env python3
"""Outward constants and exact fixtures for Note 13's rebased envelope.

19 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Authoring model gpt-6-astra, actual effort max. Execution provenance is
required for new records. The compact-band extension is an analytic proof;
this script does not assign it a numerical onset or physical certificate.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import sys

sys.dont_write_bytecode = True
import flint
from flint import arb, ctx

INV = Path("papers/investigations-3/11_arithmetic_collision_rigidity")
LANE = INV / "symmetries/03_normalized_jet_rotation"
SOURCES = [
    LANE / "notes/13_REBASED_RESIDUAL_AND_COMPACT_SECTOR_EDGE_EXTENSIONS_20261019.md",
    LANE / "numerics/check_rebased_residual_envelope.py",
    LANE / "notes/09_UNIFORM_COHERENT_EDGE_AND_CUTOFF_MATCHING_20261019.md",
    LANE / "notes/10_UNIFORM_SIGNED_RESIDUAL_INCREMENT_20261019.md",
    LANE / "numerics/UAR04_UNIFORM_SIGNED_INCREMENT_20261019.json",
    INV / "symmetries/notes/07_UAR01_CORRECTED_RESIDUAL_AND_TRANSITION_CONTRACT_20261019.md",
    Path("papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/"
         "17_enlarged_state_transport/notes/"
         "22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md"),
]


def check(value, message):
    if not value:
        raise ArithmeticError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_fixtures():
    ra, before, jump, rb = F(5), F(7, 4), F(2, 3), F(-1, 3)
    after = before - jump
    ordinary = (before - ra) + (rb - after)
    check(ordinary == rb - ra + jump, "ordinary integral switch sign")
    check(ordinary != rb - ra - jump, "negative switch mutation")
    check(before - ra == after - ra + jump, "terminal left/right ownership")
    check(rb - after == rb - before + jump, "initial right chart ownership")
    check(-ordinary == ra - rb - jump, "reverse orientation")
    c, beta_max, discrete = F(153, 100), F(12, 7), F(137, 10**6)
    check(c + beta_max + discrete < F(3245, 1000), "prefix reserve")
    check(c < beta_max, "maximum coefficient direction")
    # Q=x^2 at its double event, f=Q, r=0: the full first-jet variation
    # from x=-1 to x=0 has the same norm as the nonzero anchor.
    anchor_norm_squared = F(1)**2 + F(2)**2
    variation_norm_squared = anchor_norm_squared
    event_energy = F(0)**2 + F(0)**2
    check(event_energy == 0 and anchor_norm_squared == variation_norm_squared,
          "zero residual must not imply physical exclusion")
    return {
        "ordinary_positive_switch_sign": True,
        "wrong_sign_mutation_detected": True,
        "terminal_left_right_descriptions_agree": True,
        "initial_right_chart_not_double_counted": True,
        "reverse_orientation": True,
        "exact_prefix_reserve": True,
        "zero_residual_polynomial_event_has_zero_physical_margin": True,
    }


def scalar_checks(bits):
    check(bits in (192, 256), "unsupported precision")
    ctx.prec = bits
    a = arb
    out = lambda x: x.str(38, more=True)
    L = a(20)
    finite_ratio = 10 / a.pi()**2 * (-L).exp()
    edge_ratio = 1000 * (-a("3.49") * L).exp()
    first_term = 3 * (-L / 2).exp()
    retained_coefficient = a("1.53") + a(12)/7 + a(".000137")
    complete_coefficient = retained_coefficient + 2*finite_ratio + 36*edge_ratio
    opening = a("3.246") * (-a(13)/a(".8")).exp()
    later = a("3.246") * (-a("20.25")/a(".8")).exp()
    check(first_term < a(".000137"), "first transition allowance")
    check(finite_ratio < a("2.1e-9"), "finite endpoint remainder")
    check(edge_ratio < a("5e-28"), "edge endpoint remainder")
    check(retained_coefficient < a("3.245"), "retained reserve")
    check(complete_coefficient < a("3.246"), "complete reserve")
    check(opening < a("2.846e-7"), "opening ceiling")
    check(later < a("3.3e-11"), "later-start ceiling")
    return {
        "bits": bits, "all_checks_passed": True,
        "first_transition_relative_allowance": out(first_term),
        "finite_remainder_over_S": out(finite_ratio),
        "edge_remainder_over_S": out(edge_ratio),
        "retained_coefficient": out(retained_coefficient),
        "complete_coefficient": out(complete_coefficient),
        "opening_t_1_20_kappa_1": out(opening),
        "later_start_t_1_20_kappa_3_2": out(later),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--output", type=Path)
    group.add_argument("--verify", type=Path)
    parser.add_argument("--execution-model")
    parser.add_argument("--execution-effort")
    args = parser.parse_args()
    repo = args.repo.resolve()
    pins = {str(path): sha(repo/path) for path in SOURCES}
    fixtures = exact_fixtures()
    runs = [scalar_checks(bits) for bits in (192, 256)]
    if args.verify:
        saved = json.loads(args.verify.read_text())
        check(saved["schema"] == "uar-rebased-envelope-v1", "wrong schema")
        check(saved["source_sha256"] == pins, "missing or stale source pins")
        check(saved["exact_fixtures"] == fixtures, "changed exact fixtures")
        check(saved["runs"] == runs, "changed outward calculations")
        print(json.dumps({"status": "verified", "bits": [192, 256]}))
        return
    check(args.execution_model and args.execution_effort,
          "actual execution provenance required")
    record = {
        "schema": "uar-rebased-envelope-v1",
        "date": "2026-10-19", "timezone": "America/New_York",
        "utc": datetime.now(timezone.utc).isoformat(),
        "prepared_for": "Edward Baker",
        "actual_model": args.execution_model,
        "actual_effort": args.execution_effort,
        "llm_assistance": "Substantial; internal self-review.",
        "python": platform.python_version(), "python_flint": flint.__version__,
        "source_sha256": pins, "exact_fixtures": fixtures, "runs": runs,
        "scope": "Constants and fixtures for the explicit arbitrary-endpoint residual corollary.",
        "limitations": [
            "Uniformity is proved analytically, not by sampled heights.",
            "No numerical onset or constants for a wider compact band.",
            "No H acquisition, retained integral quadrature, physical margin or new coverage.",
            "Existing UAR06 consumer loss remains unchanged.",
            "Internal self-review, not independent specialist validation.",
        ],
    }
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "written", "bits": [192, 256]}))


if __name__ == "__main__":
    main()
