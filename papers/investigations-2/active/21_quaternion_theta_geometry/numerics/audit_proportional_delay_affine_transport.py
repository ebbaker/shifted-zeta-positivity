#!/usr/bin/env python3
"""Replay 1,200 exact rational affine-transport audit evaluations.

Prepared for Edward Baker, 14 October 2026, with substantial LLM assistance.
Recorded parent-session model: gpt-6.1-sol; reasoning effort: ultra.

This reconstructs the independent audit's original loops. The tested
tensor is compared with a direct nested Taylor sum at fixed rational
values, using midpoint source coefficients. It checks finite polynomial
transport algebra, not quadrature, analytic tails, or theta signs.
Standard library only. All audited source files are read-only.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import platform
import runpy


RECORD_NAME = "THETA_CENTERED_RESIDUAL_100_104_20261014.json"
EXPECTED_SHA256 = {
    "pilot_driver": "dbc5be224cb7e88171f3e8f29bde87606edc29833eb2752ea1d20c9e4178e72f",
    "record": "aee1f000150a90e1269faa9a8cfafa6251d581ec0f586f0b09d554ef8822741d",
    "original_driver": "6da9b9c05b465a0067809f9e11bb7d7414f51330afe91c2c38e7cb02fc939afb",
    "contour_source": "b6f0114e1a4de2e1848f20ab0ab2f1022d9b55015184a879ae0c0536a62d6ad6",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def direct_taylor(coefficients, j, eta, dt):
    """Independent nested form, before any affine binomial substitution."""
    return sum(
        (-dt) ** ell * eta ** q * coefficients[j + 2 * ell + q]
        / (factorial(ell) * factorial(q))
        for ell in range(8)
        for q in range(12)
    )


def run(args):
    # Audited inputs live beside the pilot, or at explicit caller paths.
    record = args.record or args.pilot_driver.parent / RECORD_NAME
    require(record.is_file(), "Source record missing; supply --record or place it beside the pilot driver.")
    original = args.original_driver or record.parent / "certify_phase_centered_residual.py"
    contour = args.contour_source or record.parent / "check_shifted_contour_payments.py"
    paths = {
        "pilot_driver": args.pilot_driver,
        "record": record,
        "original_driver": original,
        "contour_source": contour,
    }
    hashes = {name: digest(path) for name, path in paths.items()}
    for name, actual in hashes.items():
        require(actual == EXPECTED_SHA256[name], "audited source hash: " + name)

    # The driver has a guarded CLI, so loading it does not run its pilot.
    tested = runpy.run_path(str(args.pilot_driver))
    raw = json.loads(record.read_text())
    require(raw["script_sha256"] == hashes["original_driver"], "original driver linkage")
    require(raw["imported_source_sha256"] == hashes["contour_source"], "contour linkage")
    lookup = {(tuple(row["x"]), tuple(row["t"])): row for row in raw["cells"]}
    a_interval = tested["iv"](raw["a"])
    a = (a_interval[0] + a_interval[1]) / 2
    mu = a * a + F(1, 16)
    checked = 0
    component_counts = {"retained": 0, "complement": 0, "absorption": 0}

    def midpoint_cjets(row):
        z = [sum(tested["iv"](value)) / 2 for value in row["center_jets"]]
        return [-z[q + 2] - 2 * a * z[q + 1] - mu * z[q] for q in range(len(z) - 2)]

    for j, x in [(0, 101), (1, 103)]:
        for k in range(8):
            key = ((str(x), str(x + 1)), (str(F(k, 16)), str(F(k + 1, 16))))
            prior_k = k // 2
            prior_key = (key[0], (str(F(prior_k, 16)), str(F(prior_k + 1, 16))))
            current = midpoint_cjets(lookup[key])
            prior = midpoint_cjets(lookup[prior_key])
            offset = F(-1 if k % 2 == 0 else 1, 64)
            current_intervals = [(value, value) for value in current]
            prior_intervals = [(value, value) for value in prior]
            current_tensor = tested["tensor"](current_intervals, j)
            prior_tensor = tested["tensor"](prior_intervals, j, F(1, 2), offset)

            for eta in map(F, ["-1/2", "-1/3", "0", "2/5", "1/2"]):
                for dt in map(F, ["-1/32", "-1/64", "0", "1/64", "1/32"]):
                    current_value = direct_taylor(current, j, eta, dt)
                    prior_value = direct_taylor(prior, j, eta, dt / 2 + offset)
                    comparisons = [
                        ("retained", prior_tensor, prior_value),
                        ("complement", tested["combine"](current_tensor, prior_tensor, 1),
                         current_value - prior_value),
                        ("absorption", tested["combine"](current_tensor, prior_tensor, F(1, 2)),
                         current_value - prior_value / 2),
                    ]
                    for name, tensor, expected in comparisons:
                        actual = tested["evaluate"](tensor, (eta, eta), (dt, dt))
                        require(actual == (expected, expected),
                                "affine tensor mismatch: " + str((j, k, eta, dt, name)))
                        checked += 1
                        component_counts[name] += 1

    require(checked == 1200 and set(component_counts.values()) == {400},
            "complete original audit evaluation count")
    receipt = {
        "schema": "inv21_proportional_delay_independent_affine_audit_v1",
        "date": "2026-10-14",
        "prepared_for": "Edward Baker",
        "llm_assistance": "Substantial",
        "recorded_model": "gpt-6.1-sol",
        "recorded_effort": "ultra",
        "status": "PASS",
        "python": platform.python_version(),
        "arithmetic": "Exact fractions.Fraction; no floating-point evaluation.",
        "audit_script_name": Path(__file__).name,
        "audit_script_sha256": digest(Path(__file__)),
        "input_names": {name: path.name for name, path in paths.items()},
        "input_sha256": hashes,
        "source_hash_checks_passed": 4,
        "checked_evaluations": checked,
        "component_counts": component_counts,
        "protocol": {
            "branches": [{"j": 0, "x": [101, 102]}, {"j": 1, "x": [103, 104]}],
            "slabs": list(range(8)),
            "eta_points": ["-1/2", "-1/3", "0", "2/5", "1/2"],
            "dt_points": ["-1/32", "-1/64", "0", "1/64", "1/32"],
            "prior_displacement": "dt/2 + (-1/64 for even slab; +1/64 for odd slab)",
            "centering": "Midpoints of original exact-rational source enclosures; a midpoint, b=1/4.",
            "comparison": "Target affine tensor evaluation equals direct nested 8-by-12 Taylor sum for G, R, and C-G/2.",
        },
        "limitations": [
            "Finite algebra checks reproduce the original 1,200 audit evaluations; they are not a substitute for the analytic binomial proof.",
            "These checks do not replay source quadrature, validate analytic tail lemmas, or prove theta signs or new height coverage.",
        ],
    }
    args.output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "checked_evaluations": checked,
                      "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pilot-driver", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--record", type=Path)
    parser.add_argument("--original-driver", type=Path)
    parser.add_argument("--contour-source", type=Path)
    run(parser.parse_args())
