#!/usr/bin/env python3
"""Exact downstream arithmetic for Note 01; does not establish premise (C).

Prepared for Edward Baker with substantial LLM assistance, 2026-10-17.
Recorded coordinating model: gpt-6.1-sol; reasoning effort: ultra.
Standard library only. An excessive --kernel-floor is a failure injection.
"""

import argparse
from fractions import Fraction as Q
import json
import sys


def run(kernel_floor):
    checks = []

    def require(name, condition):
        checks.append({"name": name, "passed": bool(condition)})

    q, radius = Q(7, 10), Q(1, 2)
    require("cauchy quotient", q / (radius * (1 - q)) == Q(14, 3))
    # At maximal horizontal displacement, cross multiplication gives
    # 41a - 9a^2 - 9/4 = 9(9/2-a)(a-1/18).
    factors = ([Q(9, 2), -Q(1)], [-Q(1, 18), Q(1)])
    product = [Q(0)] * 3
    for i, left in enumerate(factors[0]):
        for j, right in enumerate(factors[1]):
            product[i+j] += 9 * left * right
    require("kernel polynomial factorization", product == [-Q(9, 4), Q(41), -Q(9)])
    require("lower factor nonnegative on interval", Q(5, 2) - Q(1, 18) > 0)
    endpoint = Q(9, 2) / (Q(9, 2) ** 2 + Q(1, 2) ** 2)
    require("sharp kernel endpoint", endpoint == Q(9, 41))
    require("requested kernel floor not excessive", 0 < kernel_floor <= endpoint)
    require("alpha remainder below one",
            Q(11, 14) + Q(3, 200) + Q(81, 16 * 200**2) < 1)
    require("alpha derivative cutoff", Q(1, 200) + Q(6, 200**2) == Q(103, 20000))
    require("alpha derivative allowance", Q(103, 20000) < Q(3, 500))
    carrier = Q(1, 2) * Q(1, 2) * (1 + Q(1, 4) * Q(3, 500))
    require("carrier coefficient", carrier == Q(2003, 8000))
    coefficient, additive = Q(41, 9) * carrier, Q(41, 9) * Q(14, 3)
    require("count coefficient", coefficient == Q(82123, 72000))
    require("count additive constant", additive == Q(574, 27))
    require("rounded coefficient", coefficient < Q(6, 5))
    require("rounded additive constant", additive < 22)
    reserve_lower = Q(17, 10) - Q(22, 7)**2 / 6
    require("formal limiting comparison reserve", reserve_lower == Q(79, 1470) > 0)
    require("heat logarithm coefficient from s_star", Q(1, 2) * Q(1, 2) == Q(1, 4))
    # Even collision polynomial (z^2-a^2)^2, including reflected roots.
    a, v = Q(201), Q(7, 2)
    roots = [(-a, Q(0), 2), (a, Q(0), 2)]
    count = sum(m for x, y, m in roots if a - Q(1, 2) < x <= a + Q(1, 2))
    poisson = sum(m * (v-y) / ((a-x)**2 + (v-y)**2) for x, y, m in roots)
    require("double root counts as two", count == 2)
    require("collision Poisson accounting", poisson == 2/v + 2*v/(4*a*a+v*v))
    require("count bound permits collision", count <= Q(41, 9) * poisson)
    # Half-open boundary diagnostic, multiplicities distinct from root entries.
    boundary_roots = [(Q(200), 3), (Q(201), 2)]
    require("half-open wall convention",
            sum(m for x, m in boundary_roots if 200 < x <= 201) == 2)
    return {
        "status": "pass" if all(c["passed"] for c in checks) else "fail",
        "kernel_floor": str(kernel_floor),
        "checks": checks,
        "count_coefficient": str(coefficient),
        "count_additive": str(additive),
        "scope": "Exact arithmetic only; the off-axis comparison premise is unproved here.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kernel-floor", type=Q, default=Q(9, 41))
    args = parser.parse_args()
    result = run(args.kernel_floor)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["status"] == "pass" else 1)
