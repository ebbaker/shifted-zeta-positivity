#!/usr/bin/env python3
"""Exact finite checks for the conservation brainstorm, 18 November 2026.

Prepared for Edward Baker with OpenAI Codex LLM assistance.
Actual model and effort unavailable in the recorded chat configurations.
Standard-library rational arithmetic; no canonical zero computation.
The written arguments, rather than a count of assertions, support general claims.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import platform


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for j, v in enumerate(a):
        out[j] += v
    for j, v in enumerate(b):
        out[j] += v
    return out


def multiply(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def polynomial(roots):
    p = [F(1)]
    for r in roots:
        p = multiply(p, [-F(r), F(1)])
    return p


def derivative(p):
    return [j * p[j] for j in range(1, len(p))] or [F(0)]


def heat(p, t):
    """exp(-t d_z^2) p, with coefficients in ascending order."""
    out = [F(0)] * len(p)
    q = p[:]
    for k in range((len(p) - 1) // 2 + 1):
        out = add(out, [(-t) ** k * x / factorial(k) for x in q])
        q = derivative(derivative(q))
    return out


def autonomous_coefficients(p):
    n = len(p) - 1
    # a_2'=-n(n-1), also without centering; a_1 is constant.
    clock = -p[n - 2] / (n * (n - 1))
    return heat(p, -clock)


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def rank(a):
    a = [row[:] for row in a]
    r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][col]
        a[r] = [x / v for x in a[r]]
        for i in range(r + 1, len(a)):
            v = a[i][col]
            a[i] = [x - v * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def block_check(roots, exterior):
    x = list(map(F, roots))
    ext = list(map(F, exterior))
    n = len(x)
    c = sum(x) / n
    y = [v - c for v in x]
    r = [sum((1 / (v - z) for z in ext), F(0)) for v in x]
    b = -sum((1 / (c - z) ** 2 for z in ext), F(0))
    v = [2 * sum((1 / (q - z) for j, z in enumerate(x) if j != i), F(0))
         + 2 * r[i] for i, q in enumerate(x)]
    cp = sum(v) / n
    yp = [u - cp for u in v]
    p2, p3, p4 = [sum((u ** k for u in y), F(0)) for k in (2, 3, 4)]
    p2p = 2 * sum((u * up for u, up in zip(y, yp)), F(0))
    p3p = 3 * sum((u ** 2 * up for u, up in zip(y, yp)), F(0))
    p4p = 4 * sum((u ** 3 * up for u, up in zip(y, yp)), F(0))
    alpha = F(2 * n - 3, 4 * n * (n - 1))
    k4 = alpha * p2 ** 2 - p4 / 4
    k4p = 2 * alpha * p2 * p2p - p4p / 4
    psi = [u ** 3 - 4 * alpha * p2 * u - p3 / n for u in y]
    flux = -2 * sum((q * rv for q, rv in zip(psi, r)), F(0))
    assert k4p == flux
    assert p3p == 6 * sum(((u ** 2 - p2 / n) * rv
                          for u, rv in zip(y, r)), F(0))
    assert sum(psi) == 0
    assert sum((q * u for q, u in zip(psi, y)), F(0)) == -4 * k4
    # An independent residue evaluation of the combined contour kernel:
    # its inner residues are minus its exterior residues (none at infinity).
    exterior_residues = sum((sum((q / (z - u) for q, u in zip(psi, x)), F(0))
                             + 4 * k4 / (z - c) ** 2 for z in ext), F(0))
    assert k4p - 8 * b * k4 == 2 * exterior_residues
    return {"roots": list(map(str, x)), "exterior": list(map(str, ext)),
            "K4": str(k4), "K4_derivative_direct": str(k4p),
            "K4_derivative_flux": str(flux), "R_z_at_center": str(b),
            "curvature_remainder": str(k4p - 8 * b * k4),
            "combined_contour_remainder": str(2 * exterior_residues)}


def main():
    finite = []
    for n in range(2, 9):
        x = [F(j * j + j, 3) - F(7, 5) for j in range(n)]
        p0 = polynomial(x)
        invariants = autonomous_coefficients(p0)
        for t in (F(-2, 7), F(0), F(1, 5), F(3, 4)):
            pt = heat(p0, t)
            assert heat(pt, -t) == p0
            assert autonomous_coefficients(pt) == invariants
        force = [sum((1 / (a - b) for j, b in enumerate(x) if i != j), F(0))
                 for i, a in enumerate(x)]
        lax = [[2 * force[i] if i == j else 2 / (x[i] - x[j])
                for j in range(n)] for i in range(n)]
        power = [[F(i == j) for j in range(n)] for i in range(n)]
        for k in range(1, n + 1):
            power = matmul(power, lax)
            assert sum(power[i][i] for i in range(n)) == 0
        assert all(value == 0 for row in power for value in row)
        energy = 2 * sum(v * v for v in force) - 4 * sum(
            1 / (x[i] - x[j]) ** 2 for i in range(n) for j in range(i + 1, n))
        assert energy == 0
        finite.append({"degree": n, "heat_pullback": "exact", "autonomous_coefficients": "exact",
                       "L_power_N": "zero matrix", "CM_energy": "0"})

    b = F(2)
    # Collision at physical T=1/20 after translating the time origin.
    p_event = polynomial([-b, -b, b, b])
    values = []
    for tau in (F(-1, 100), F(0), F(1, 100)):
        p = heat(p_event, tau)
        value = p[0] - p[2] ** 2 / 12
        assert value == 2 * b ** 4 / 3
        values.append(str(value))

    jacobians = []
    for head in (1, 2, 3, 4):
        w = list(map(F, range(3, 2 * head + 6)))
        rows = [[-2 * k * z / (z * z - 1) ** (k + 1) for z in w]
                for k in range(1, head + 3)]
        rows += [[F(1 - 2 * k) / (z * z - 1) ** k
                  - F(2 * k) / (z * z - 1) ** (k + 1) for z in w]
                 for k in range(2, head + 3)]
        r = rank(rows)
        assert r == 2 * head + 3
        jacobians.append({"head_order": head, "D": "1", "rank": r,
                          "dimension": len(w)})

    block = [block_check([-2, -1, 1, 2], []),
             block_check([-2, -1, 1, 2], [-5, 5]),
             block_check([-3, -1, 2, 4], [-8, 7, 11]),
             block_check([-4, -2, 1, 3, 5], [-9, 8])]
    assert block[1]["K4_derivative_direct"] == "-55/42"
    assert block[1]["curvature_remainder"] == "-29/350"

    here = Path(__file__).resolve()
    cm = here.parents[2]
    inputs = [cm / "manuscript/sections/02_integer_hierarchy.tex",
              cm / "manuscript/sections/14_coupled_lattice.tex",
              cm / "manuscript/sections/17_forward_statistics.tex",
              cm / "notes/43_VCD_GT_CM_CORRELATION_GAIN_CONTINUATION_20261118.md"]
    record = {
        "date_local": "2026-11-18", "timezone": "America/New_York",
        "intended_author": "Edward Baker", "assistance": "OpenAI Codex LLM assistance",
        "recorded_model": None, "recorded_effort": None,
        "provenance_note": "Current chat registry model_configurations is empty; no settings inferred.",
        "python_version": platform.python_version(), "arithmetic": "fractions.Fraction exact rationals",
        "scope": "Finite algebra controls only; no canonical gap enclosure or independent review.",
        "finite_polynomial_cases": finite,
        "collision_control": {"field": "exp(-(t-T)*d_z^2)(z^2-b^2)^2",
                              "T": "1/20", "b": "2", "relative_times": ["-1/100", "0", "1/100"],
                              "K4_values": values, "result": "Nonzero conserved K4 survives a double collision."},
        "block_flux_cases": block, "moment_coordinate_rank_checks": jacobians,
        "script_sha256": hashlib.sha256(here.read_bytes()).hexdigest(),
        "source_sha256": {str(p.relative_to(cm)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in inputs},
    }
    out = here.with_name("01_CONSERVATION_EXACT_CHECKS_20261118.json")
    out.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "passed", "record": str(out),
                      "nonzero_block_flux": block[1], "collision_K4": values[1]}))


if __name__ == "__main__":
    main()
