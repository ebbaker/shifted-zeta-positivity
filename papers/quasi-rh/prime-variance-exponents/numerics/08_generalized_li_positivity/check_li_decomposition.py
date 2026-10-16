#!/usr/bin/env python3
"""Exact algebra checks plus finite Li diagnostics with analytic tail budgets.

Python 3 standard library only. Floats are NOT directed-rounding certificates.
No zero data are used. All arrays are transient and no large output is written.
Substantial LLM assistance, GPT-6 Codex, inherited configuration, 2026-10-04.
"""
from fractions import Fraction
import json
import math


def laguerre(n, u):
    # L_{n-1}^{(1)} evaluated from its finite coefficient formula.
    return math.fsum(math.comb(n, j + 1) * (-u) ** j / math.factorial(j) for j in range(n))


def upper_gamma_integer(order, x):
    return math.factorial(order - 1) * math.exp(-x) * math.fsum(
        x ** j / math.factorial(j) for j in range(order))


def lambda_sieve(limit):
    composite = bytearray(limit + 1)
    values = [0.0] * (limit + 1)
    for p in range(2, limit + 1):
        if not composite[p]:
            for k in range(p * p, limit + 1, p):
                composite[k] = 1
            power = p
            while power <= limit:
                values[power] = math.log(p)
                power *= p
    return values


def main():
    exact_checks = 0
    for tau in (Fraction(3, 2), Fraction(19, 10), Fraction(199, 100), Fraction(2)):
        for n in range(1, 13):
            integral = sum((math.comb(n, j + 1) * (-tau) ** j / (tau - 1) ** (j + 1)
                            for j in range(n)), Fraction())
            assert integral == (1 - (-1 / (tau - 1)) ** n) / tau
            for m in (1, 2, 7):
                differentiated_log = sum((math.comb(n, j) * tau ** (j - 1) * (-1) ** (j - 1)
                                          / (tau + 2 * m) ** j for j in range(1, n + 1)), Fraction())
                assert differentiated_log == (1 - (2 * m / (2 * m + tau)) ** n) / tau
            exact_checks += 4

    tau, cutoff, gamma_cutoff = 1.99, 100000, 100000
    values = lambda_sieve(cutoff)
    euler_gamma = 0.577215664901532860606512090082402431
    rows = []
    for n in range(1, 5):
        assert math.log(cutoff) >= n / tau
        prime = math.fsum(values[k] * k ** (-tau) * laguerre(n, tau * math.log(k))
                          for k in range(2, cutoff + 1) if values[k])
        gamma = -n * euler_gamma / 2 + math.fsum(
            n / (2 * m) + math.expm1(-n * math.log1p(tau / (2 * m))) / tau
            for m in range(1, gamma_cutoff + 1))
        h_head = gamma - n * math.log(math.pi) / 2
        continuous = (1 - (-1 / (tau - 1)) ** n) / tau
        prime_tail = math.fsum(math.comb(n, j + 1) * tau ** j / math.factorial(j)
                              * upper_gamma_integer(j + 2, (tau - 1) * math.log(cutoff))
                              / (tau - 1) ** (j + 2) for j in range(n))
        gamma_tail = n * (n + 1) * tau / (8 * gamma_cutoff)
        center = h_head + continuous - prime
        rows.append({"n": n, "tau": tau, "K": cutoff, "M": gamma_cutoff,
                     "elementary_continuum": continuous, "prime_head": prime,
                     "H_gamma_head": h_head, "alpha_center": center,
                     "absolute_prime_tail_budget": prime_tail, "positive_gamma_tail_budget": gamma_tail,
                     "analytic_lower_endpoint_float": center - prime_tail,
                     "analytic_upper_endpoint_float": center + prime_tail + gamma_tail})
    print(json.dumps({"status": "diagnostic_not_interval_certificate", "exact_fraction_checks": exact_checks,
                      "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
