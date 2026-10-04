#!/usr/bin/env python3
"""Exact finite checks and a floating-point norm diagnostic; no certificate.

Run with Python 3; no third-party dependencies. Generated arrays stay in memory.
Substantial LLM assistance, GPT-6 Codex, inherited configuration, 2026-10-04.
"""
from fractions import Fraction
import json
import math


def mobius_sieve(limit):
    mu = [1] * (limit + 1)
    primes = []
    composite = [False] * (limit + 1)
    for p in range(2, limit + 1):
        if not composite[p]:
            primes.append(p)
            for k in range(p, limit + 1, p):
                composite[k] = True
                mu[k] *= -1
            for k in range(p * p, limit + 1, p * p):
                mu[k] = 0
    mu[0] = 0
    return mu, primes


def main():
    mu, _ = mobius_sieve(32)
    checks = 0
    for nmax in range(2, 33):
        m1 = sum((Fraction(mu[n], n) for n in range(1, nmax + 1)), Fraction())
        for k in range(1, 4 * nmax + 1):
            e_floor = 1 + k * m1 - sum(mu[n] * (k // n) for n in range(1, nmax + 1))
            e_frac = 1 + sum((mu[n] * Fraction(k % n, n) for n in range(1, nmax + 1)), Fraction())
            assert e_floor == e_frac
            if k <= nmax:
                assert e_floor == k * m1
            checks += 1

    # The two sequences use the same exact step formula. Float output is only
    # a scale diagnostic; rigorous norm inequalities are proved in the note.
    rows = []
    p = 200 / 199
    kmax = 100000
    for nmax in (8, 16, 32):
        for smooth in (False, True):
            a = [0.0] + [float(mu[n]) * (1 - math.log(n) / math.log(nmax) if smooth else 1)
                         for n in range(1, nmax + 1)]
            # Accumulate divisor increments for the complete floor sum.
            divisor = [0.0] * (kmax + 1)
            for n in range(1, nmax + 1):
                for k in range(n, kmax + 1, n):
                    divisor[k] += a[n]
            a1 = math.fsum(a[n] / n for n in range(1, nmax + 1))
            cumulative = 0.0
            terms = []
            for k in range(1, kmax + 1):
                cumulative += divisor[k]
                e = 1 + k * a1 - cumulative
                terms.append(abs(e) ** p / (k * (k + 1)))
            finite_mass = math.fsum(terms)
            c = 1 + math.fsum(abs(v) for v in a[2:])
            tail_budget = c ** p / (kmax + 1)
            rows.append({"N": nmax, "construction": "log_taper" if smooth else "raw_mobius",
                         "p": p, "K": kmax, "prepared_moment": a1,
                         "finite_norm_p_power": finite_mass,
                         "analytic_tail_budget_float": tail_budget,
                         "norm_upper_diagnostic": (finite_mass + tail_budget) ** (1 / p)})
    print(json.dumps({"status": "diagnostic_not_interval_certificate", "exact_fraction_checks": checks,
                      "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
