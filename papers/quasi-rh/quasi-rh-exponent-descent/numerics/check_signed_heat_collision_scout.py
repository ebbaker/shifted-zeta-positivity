#!/usr/bin/env python3
"""Finite exact checks for Heat Note 8; prints deterministic JSON, writes nothing.

Prepared for Edward Baker with substantial LLM assistance, 9 October 2026.
Model: GPT-6 (Codex); serving variant and configured reasoning effort are not
exposed and are not inferred. All checks use rational arithmetic.

Scope: kernel algebra, continuous scalar reserves, exponent identities,
positive log-series remainder bounds, and finite signing/partition checks.
No heat functions, physical phases, zeros, large cutoffs, or grids are evaluated.
Polymath's theorem and the note's analytic asymptotics remain proof inputs.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


counts = {}


def require(category, condition):
    if not condition:
        raise AssertionError(category)
    counts[category] = counts.get(category, 0) + 1


def exp_bounds(value, terms=160):
    """Positive Taylor polynomial with a rational geometric upper remainder."""
    value = F(value)
    if not 0 <= value < terms + 2:
        raise ValueError("Unsupported exponential argument")
    term = total = F(1)
    for index in range(1, terms + 1):
        term *= value / index
        total += term
    first_omitted = term * value / (terms + 1)
    upper = total + first_omitted / (1 - value / (terms + 2))
    return total, upper


def poly_add(left, right):
    size = max(len(left), len(right))
    return tuple((left[i] if i < len(left) else 0)
                 + (right[i] if i < len(right) else 0) for i in range(size))


def poly_scale(poly, scalar):
    return tuple(scalar * value for value in poly)


def poly_mul(left, right):
    output = [F(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            output[i + j] += x * y
    return tuple(output)


def unit_circle(parameter):
    parameter = F(parameter)
    return ((1 - parameter**2) / (1 + parameter**2),
            2 * parameter / (1 + parameter**2))


def dot(left, right):
    return sum(x * y for x, y in zip(left, right))


def scalar_checks():
    a = (F(0), F(1, 4), F(-1, 16))
    b = (F(0), F(1, 4), F(1, 16))
    d = (F(0), F(3, 4), F(1, 16))
    require("exponents", poly_add(a, b) == (0, F(1, 2), 0))
    require("exponents", poly_add(d, poly_scale(b, -1)) == (0, F(1, 2), 0))
    require("exponents", poly_add(d, a) == (0, 1, 0))
    # Factored minima on the whole interval 1 <= kappa <= 2.
    require("exponents", poly_add(a, (F(-3, 16),)) ==
            poly_scale(poly_mul((-1, 1), (3, -1)), F(1, 16)))
    require("exponents", poly_add(b, (F(-5, 16),)) ==
            poly_scale(poly_mul((-1, 1), (5, 1)), F(1, 16)))
    require("payment", F(1, 2)**2 + F(2)**2 == F(17, 4))
    require("payment", 25 * F(17, 4) == F(425, 4))
    require("payment", F(13, 10) * (F(101, 100) + F(26, 10) + F(1, 100)) < 5)
    require("payment", 5 * F(27, 10) * F(9, 10) < 4 * F(314, 100))
    require("payment", exp_bounds(10)[0] > 22001)
    require("payment", exp_bounds(20)[0] > 10**9 / F(12))
    require("payment", exp_bounds(F(15, 4))[0] > 40)
    require("payment", exp_bounds(F(251, 1000))[1] < F(13, 10))
    require("payment", exp_bounds(F(25101, 100000))[1] < F(13, 10))
    require("payment", exp_bounds(F(500005, 10**6) + F(1, 10**9))[1] < F(17, 10))
    require("payment", exp_bounds(F(1, 1000) + F(1, 10**9))[1] < F(101, 100))
    require("payment", F(5, 2) / (22000 - F(1, 8)) < F(1, 5000))
    # Edge exponent reserve, using |delta| <= 1e-4, |Delta| <= 1e-9,
    # t <= .05, tL <= 2. Every term has the sign-independent upper bound below.
    edge_reserve = (F(1, 4) + F(1, 2) / 10**4
                    + F(1, 20) / (4 * 10**8)
                    + F(1, 2 * 10**9) + F(1, 40 * 10**13))
    require("payment", edge_reserve < F(251, 1000))
    # U_n bound is continuous for x >= 1e9. With y=C/(x-D),
    # exp(y)-1 <= y/(1-y) gives x*C/(x-D-C) <= .9.
    bound_c, bound_d = F(87600001, 10**8), F(671, 100)
    require("payment", (F(9, 10) - bound_c) * 10**9 >=
            F(9, 10) * (bound_d + bound_c))

    head = sum(F(1, n) for n in range(2, 257))
    require("ellipse", head > F(9, 2))
    require("ellipse", F(61, 100)**4 > F(1, 8))
    require("ellipse", 50**4 < 257**3)
    require("ellipse", 4 * (4 - 1) < 16)
    require("ellipse", (F(9, 2) - F(61, 100)) / 2 > F(103, 100))
    require("ellipse", F(97, 100) - F(61, 100) > F(1, 100) * 16)
    require("ellipse", F(101, 100) * F(2, 100) < F(25, 1000))
    require("ellipse", F(995, 1000) - F(202, 10000) > F(97, 100))
    require("ellipse", F(1005, 1000) + F(202, 10000) < F(103, 100))


def kernel_checks():
    # Rational points of the unit circle supply exact formal sine/cosine data.
    # The full trig-expanded signed kernel is compared to an independent
    # direct Euclidean sum of vectors, retaining drift and all ordered pairs.
    for case in range(1, 33):
        rows = []
        for n in range(1, 8):
            cosine, sine = unit_circle(F(case - 3 * n, case + n))
            weight = F(n + case, n * (case + 2))
            frequency = F(case - n, case + n)
            drift = F(2 * n - case, 13 * (case + n))
            vector = (cosine, frequency * sine - drift * cosine)
            require("signed_kernel", cosine**2 + sine**2 == 1)
            rows.append((weight, cosine, sine, frequency, drift, vector))
        direct = tuple(sum(row[0] * row[5][i] for row in rows) for i in (0, 1))
        expanded = F(0)
        for w, cn, sn, rn, dn, vn in rows:
            for z, cm, sm, rm, dm, vm in rows:
                cos_difference, cos_sum = cn * cm + sn * sm, cn * cm - sn * sm
                sin_difference, sin_sum = sn * cm - cn * sm, sn * cm + cn * sm
                twice_kernel = ((1 + rn * rm + dn * dm) * cos_difference
                                + (1 - rn * rm + dn * dm) * cos_sum
                                + (dn * rm - dm * rn) * sin_difference
                                - (dm * rn + dn * rm) * sin_sum)
                require("signed_kernel", twice_kernel == 2 * dot(vn, vm))
                expanded += w * z * twice_kernel / 2
        require("signed_kernel", expanded == dot(direct, direct))


def signing_checks():
    for case in range(1, 17):
        entries = [F((n * case) % 17 - 8, n + case) for n in range(1, 65)]
        residual = F(0)
        maximum = max(abs(value) for value in entries)
        for value in entries:
            residual = min((residual + value, residual - value), key=abs)
            require("signing", abs(residual) <= maximum)
        # The partition invariant is separate from signing the derivative tail.
        left = right = F(0)
        weights = [abs(value) for value in entries]
        for weight in weights:
            if left <= right:
                left += weight
            else:
                right += weight
            require("signing", abs(left - right) <= maximum)


def log_remainder_checks():
    # Finite exact positive-series tests support the displayed expansion:
    # M^2[-log(1-1/M)] = M + 1/2 + O(1/M).
    # These are not enclosures of an actual phase or a proof of its uniform limit.
    for m in (2, 3, 4, 7, 16, 31, 64, 127, 256, 1024):
        z = F(1, m)
        partial = sum(z**n / n for n in range(3, 41))
        omitted_bound = z**41 / (41 * (1 - z))
        require("log_remainder", partial >= z**3 / 3)
        require("log_remainder", partial + omitted_bound <= z**3 / (3 * (1 - z)))
        require("log_remainder", m**2 * (partial + omitted_bound) <= F(1, 3 * (m - 1)))


def main():
    scalar_checks()
    kernel_checks()
    signing_checks()
    log_remainder_checks()
    record = {
        "investigation": "heat signed shrinking-time collision scout",
        "date": "2026-10-09",
        "model": "GPT-6 (Codex); exact serving variant not exposed",
        "reasoning_effort": "not exposed; not inferred",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "exact fractions; no floating tolerance",
        "assertions": sum(counts.values()),
        "assertions_by_category": dict(sorted(counts.items())),
        "result": "pass",
        "scope": [
            "complete signed kernel with all ordered pairs and amplitude drift",
            "continuous rational exponent, error-payment and ellipse reserves",
            "finite greedy signing, partition and positive-log-series checks",
        ],
        "not_certified": [
            "Polymath approximation theorem or full-disk analytic proof",
            "uniform analytic limits or genuine phase evaluations",
            "collision exclusion, RH, or a full signed lower bound",
        ],
    }
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
