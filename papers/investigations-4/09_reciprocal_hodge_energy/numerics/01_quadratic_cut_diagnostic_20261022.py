#!/usr/bin/env python3
"""Floating sign/factor diagnostic, not a certificate or theta acquisition.

Prepared for Edward Baker with LLM assistance, gpt-6.1-sol, effort ultra.
2026-10-22. Python standard library only. See Note 02 for the exact proof.
"""

import json
import hashlib
import math
import platform
from pathlib import Path


def midpoint(f, n=16384):
    step = 2 * math.pi / n
    return step * math.fsum(f((j + 0.5) * step) for j in range(n))


def diagnostic(ratio):
    # R=1, a=ratio. Pull back the entire cover, including both sheets.
    q = 1 / ratio
    u0 = math.acosh(q)

    def u(theta):
        return math.asinh(math.sqrt(q * q - math.cos(theta) ** 2))

    def derivative(theta):
        h = q * q - math.cos(theta) ** 2
        return math.cos(theta) * math.sin(theta) / math.sqrt(h * (1 + h))

    energy = 2 * midpoint(u)
    cut = 2 * math.pi * u0
    physical = midpoint(lambda theta: u(theta) - theta * derivative(theta))
    defect = abs(energy - cut - physical)
    lower = 4 * math.pi * math.acosh(q)
    upper = 4 * math.pi * math.asinh(q)
    tau = ratio * ratio / 2
    baseline = (8 / 3) * (4 * math.pi + 2 * math.pi * math.log(2 * math.sqrt(5 / (6 * tau))))
    assert lower <= energy <= upper
    assert energy <= baseline
    # This checks the two separately evaluated boundary payments, including
    # derivative/orientation terms. It does not certify quadrature error.
    assert defect < 1e-6
    return {
        "a_over_R": ratio,
        "energy_floating": energy,
        "analytic_lower_evaluated_in_float": lower,
        "analytic_upper_evaluated_in_float": upper,
        "event_chart_baseline_upper_evaluated_in_float": baseline,
        "cut_contribution_floating": cut,
        "physical_boundary_contribution_floating": physical,
        "boundary_identity_defect_floating": defect,
        "transverse_period_floating": 2 * u0,
        "core_period": "2*pi*i",
    }


if __name__ == "__main__":
    print(json.dumps({
        "date": "2026-10-22",
        "prepared_for": "Edward Baker",
        "model": "gpt-6.1-sol",
        "reasoning_effort": "ultra",
        "status": "floating diagnostic; not a certificate",
        "python": platform.python_version(),
        "midpoint_cells": 16384,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "rows": [diagnostic(a) for a in (0.5, 0.25, 0.0625, 0.00390625)],
    }, indent=2))
