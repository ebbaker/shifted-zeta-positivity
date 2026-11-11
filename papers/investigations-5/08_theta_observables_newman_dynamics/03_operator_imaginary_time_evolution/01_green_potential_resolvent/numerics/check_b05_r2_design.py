#!/usr/bin/env python3
"""Exact design arithmetic and polynomial examples; no theta evaluation.

Prepared for Edward Baker with OpenAI Codex LLM assistance, 2026-11-10.
Actual model/effort unavailable in chat0009. This does not execute E08.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


def unique_named(tree, name):
    found = []
    if isinstance(tree, dict):
        for key, value in tree.items():
            if key == name:
                found.append(value)
            else:
                found.extend(unique_named(value, name))
    elif isinstance(tree, list):
        for value in tree:
            found.extend(unique_named(value, name))
    return found


def endpoint(tree, name, side):
    values = unique_named(tree, name)
    assert len(values) == 1, (name, len(values))
    mantissa, exponent = values[0][side + "_dyadic"]
    return F(int(mantissa)) * F(2) ** int(exponent)


def divided_polynomial(coefficients, knots):
    """Ascending coefficients; each step subtracts the interpolation value."""
    coefficients = list(map(F, coefficients))
    for knot in map(F, knots):
        if len(coefficients) == 1:
            coefficients = [F(0)]
            continue
        quotient = [F(0)] * (len(coefficients) - 1)
        quotient[-1] = coefficients[-1]
        for index in range(len(quotient) - 2, -1, -1):
            quotient[index] = coefficients[index + 1] + knot * quotient[index + 1]
        coefficients = quotient
    return coefficients


def main():
    directory = Path(__file__).resolve().parent
    source = directory / "05_TND_OG_E06_DIRECTED_SCALAR_RECORD_20261110.json"
    inherited = json.loads(source.read_text())
    patches, labels = 264, 264 * 4
    curvature = F(13, 4) + 32 * 32
    mass = 132 * 256 + labels * F(33, 16)
    constant = curvature / 16 + mass / 800
    factor_error = F(1, 2044)
    root_error = F(264 * 24, 2**24)
    quad_error = F(110, 512**2)
    finite_error = F(1, 2000)
    tail = endpoint(inherited, "T", "upper")
    prime = endpoint(inherited, "beta", "upper")
    accuracy = endpoint(inherited, "h", "lower")
    upper_error = 2 * (tail + prime + factor_error + root_error + quad_error + finite_error)
    assert mass == 35970
    assert constant == F(34933, 320) < 110
    assert root_error == F(99, 262144) < F(1, 2000)
    assert factor_error < F(1, 2000) and quad_error < F(1, 2000)
    assert patches * 256 == 67584
    assert upper_error < F(17, 1000) < accuracy
    assert accuracy > F(1, 64)
    assert tail <= accuracy / 12 and prime <= accuracy / 12
    # Independently stated polynomial identities, including nonroot knots.
    assert divided_polynomial([0, 0, 0, 1], [1, 1]) == [2, 1]
    assert divided_polynomial([0, 0, 1], [1]) == [1, 1]
    assert divided_polynomial([F(1, 8), 0, 1], [0, 0]) == [1]
    assert divided_polynomial([1, 2, 3], []) == [1, 2, 3]
    record = {
        "date": "2026-11-10",
        "timezone": "America/New_York",
        "prepared_for": "Edward Baker",
        "llm_assistance": "OpenAI Codex",
        "actual_model": None,
        "actual_effort": None,
        "provenance": "No model/effort configuration in accessible chat0009 source",
        "status": "exact_design_bookkeeping_passed_not_a_theta_certificate",
        "inherited_record": {
            "file": source.name,
            "bytes": source.stat().st_size,
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        },
        "conditional_design": {
            "patches": patches,
            "max_root_labels_with_reuse": labels,
            "panel_width": "1/512",
            "panels": patches * 256,
            "coefficient_integrals_before_sharing": patches * 65,
            "factor_endpoint_values": patches * 257,
            "global_gamma_kernel_nodes": patches * 256 + 1,
            "root_node_pairs_per_primitive": labels * 257,
            "curvature_upper": str(curvature),
            "S_upper": str(mass),
            "C_strict_upper": str(constant),
            "factor_error_upper": str(factor_error),
            "root_error_strict_upper": str(root_error),
            "quadrature_error_strict_upper": str(quad_error),
            "finite_error_allowance": str(finite_error),
            "inherited_T_upper": str(tail),
            "inherited_beta_upper": str(prime),
            "inherited_h_lower": str(accuracy),
            "upper_endpoint_error_upper": str(upper_error),
            "upper_endpoint_error_less_than": "17/1000",
            "all_canonical_gates_acquired": False,
        },
        "polynomial_examples": {
            "z_cubed_at_repeated_one_knots": "x+2",
            "z_squared_at_nonroot_one_knot": "x+1; not x^2/(x-1)",
            "z_squared_plus_one_eighth_at_two_zero_knots": "1",
            "zero_order": "unchanged",
        },
        "field_evaluations": 0,
        "root_certificates_acquired": 0,
        "integration_panels_executed": 0,
        "E08_executed": False,
    }
    destination = directory / "08_TND_OG_B05_R2_EXACT_DESIGN_RECORD_20261110.json"
    destination.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "record": str(destination),
                      "conditional_panels": patches * 256,
                      "conditional_upper_error_less_than": "17/1000"}))


if __name__ == "__main__":
    main()
