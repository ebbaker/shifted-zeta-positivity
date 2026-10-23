#!/usr/bin/env python3
"""Exact algebra diagnostics for the moving-collar brainstorm; no theta data."""
from fractions import Fraction as F
from pathlib import Path
import json


def multiply(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def derivative(p):
    return [F(i) * p[i] for i in range(1, len(p))] or [F(0)]


def evaluate(p, x):
    out = F(0)
    for c in reversed(p):
        out = out * x + c
    return out


roots_list = [
    [F(-1), F(1)],
    [F(-2), F(0), F(3)],
    [F(-3), F(-1), F(2), F(5)],
    [F(0), F(1, 100), F(1), F(3)],
    [F(-7, 3), F(-1, 2), F(2, 5), F(9, 7), F(11, 3)],
]
unit_parameters = [(F(0), F(0)), (F(2), F(0)),
                   (F(1, 3), F(1, 5)), (F(-2, 7), F(-3, 11))]
cluster_cases = 0
root_cases = 0
for roots in roots_list:
    p = [F(1)]
    for root in roots:
        p = multiply(p, [-root, F(1)])
    p1, p2, p3 = derivative(p), derivative(derivative(p)), derivative(derivative(derivative(p)))
    s1 = [sum((1 / (x - y) for y in roots if y != x), F(0)) for x in roots]
    s2 = [sum((1 / (x - y) ** 2 for y in roots if y != x), F(0)) for x in roots]
    assert sum((s * s for s in s1), F(0)) == sum(s2, F(0))
    energy = sum((1 / (roots[k] - roots[j]) ** 2
                  for j in range(len(roots)) for k in range(j + 1, len(roots))), F(0))
    for c, d in unit_parameters:
        # U=exp(c*z+d*z*z/2); evaluate ratios after cancelling U.
        a = [c + d * x for x in roots]
        direct = F(0)
        for j, x in enumerate(roots):
            h1 = evaluate(p1, x)
            h2 = evaluate(p2, x) + 2 * a[j] * h1
            h3 = evaluate(p3, x) + 3 * a[j] * evaluate(p2, x) + 3 * (a[j] ** 2 + d) * h1
            raw = (h2 / h1) ** 2 - h3 / h1
            local = s1[j] ** 2 + 3 * s2[j] + 2 * a[j] * s1[j] + a[j] ** 2 - 3 * d
            assert raw == local
            direct += raw
            root_cases += 1
        remainder = 2 * sum(((a[k] - a[j]) / (roots[k] - roots[j])
                             for j in range(len(roots)) for k in range(j + 1, len(roots))), F(0))
        remainder += sum((v * v - 3 * d for v in a), F(0))
        assert direct == 8 * energy + remainder
        cluster_cases += 1

jet_cases = 0
for h0 in map(F, [-2, 0, 3]):
    for h1 in map(F, [1, 2, 5]):
        for h2 in map(F, [-3, 1, 4]):
            for h3 in map(F, [-2, 3]):
                lag = h1 * h1 - h0 * h2
                if lag == 0:
                    continue
                qt = (-h2 * h1 + h0 * h3) / (h1 * h1)
                qz = lag / (h1 * h1)
                velocity = (h1 * h2 - h0 * h3) / lag
                assert qt + velocity * qz == 0
                direct = (-h3 + velocity * h2) / h1
                assert direct == (h2 * h2 - h1 * h3) / lag
                jet_cases += 1

quadratic_cases = 0
for r in [F(1, 10), F(1, 2), F(1), F(3)]:
    tau_minus_event = r * r / 2
    gap_squared = 4 * r * r
    assert 8 / gap_squared == 1 / tau_minus_event
    assert gap_squared / 8 == tau_minus_event
    quadratic_cases += 1

record = {
    "date": "2026-10-23",
    "timezone": "America/New_York",
    "prepared_for": "Edward Baker",
    "llm_assistance": "Substantial; same-assistant algebra checks",
    "model": "gpt-6-astra",
    "reasoning_effort": "max",
    "arithmetic": "Exact Python fractions",
    "passed": True,
    "cluster_cases": cluster_cases,
    "root_identity_cases": root_cases,
    "material_jet_cases": jet_cases,
    "quadratic_scale_cases": quadratic_cases,
    "scope": "Finite algebra and quadratic normalization only. No canonical-theta evaluation, interval certificate, or independent review.",
}
destination = Path(__file__).with_name("MATERIAL_JET_ENERGY_CHECKS_20261023.json")
destination.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
