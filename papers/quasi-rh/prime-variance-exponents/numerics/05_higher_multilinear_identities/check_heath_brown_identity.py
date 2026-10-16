#!/usr/bin/env python3
"""Exact finite coefficient check of the capped Heath--Brown identity.

4 October 2026; substantial LLM assistance, GPT-6 Codex inherited model.
Integer dictionaries represent linear combinations of prime logarithms.
This checks finite algebra, not an asymptotic prime estimate.
"""

from math import comb


def factors(n):
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def conv(a, b):
    """Truncated integer Dirichlet convolution."""
    cap = len(a) - 1
    result = [0] * (cap + 1)
    for d in range(1, cap + 1):
        if a[d]:
            for m in range(1, cap // d + 1):
                result[d * m] += a[d] * b[m]
    return result


def add_scaled(target, source, scale):
    for p, coefficient in source.items():
        target[p] = target.get(p, 0) + scale * coefficient
        if target[p] == 0:
            del target[p]


def vector_conv(a, b):
    """Integer sequence convolved with prime-log coefficient vectors."""
    cap = len(a) - 1
    result = [{} for _ in a]
    for d in range(1, cap + 1):
        if a[d]:
            for m in range(1, cap // d + 1):
                if b[m]:
                    add_scaled(result[d * m], b[m], a[d])
    return result


def check(cap, cutoff, order):
    prime_logs = [{}] + [factors(n) for n in range(1, cap + 1)]
    mu_y = [0] * (cap + 1)
    for n in range(1, min(cutoff, cap) + 1):
        exponents = prime_logs[n]
        mu_y[n] = 0 if any(e > 1 for e in exponents.values()) else (-1) ** len(exponents)
    ones = [0] + [1] * cap
    unit = [0] * (cap + 1)
    unit[1] = 1
    lambda_vectors = [{} for _ in range(cap + 1)]
    for n in range(2, cap + 1):
        if len(prime_logs[n]) == 1:
            lambda_vectors[n] = {next(iter(prime_logs[n])): 1}

    truncated_inverse = conv(ones, mu_y)
    residual = [unit[n] - truncated_inverse[n] for n in range(cap + 1)]
    residual_power = unit
    for _ in range(order):
        residual_power = conv(residual_power, residual)
    remainder = vector_conv(residual_power, lambda_vectors)

    rhs = [{} for _ in range(cap + 1)]
    mu_power, one_power = unit, unit
    for j in range(1, order + 1):
        mu_power = conv(mu_power, mu_y)
        if j > 1:
            one_power = conv(one_power, ones)
        term = vector_conv(conv(mu_power, one_power), prime_logs)
        multiplier = (-1) ** (j - 1) * comb(order, j)
        for n in range(1, cap + 1):
            add_scaled(rhs[n], term[n], multiplier)
    zero_remainder = all(not v for v in remainder)
    for n in range(1, cap + 1):
        add_scaled(rhs[n], remainder[n], 1)
        assert rhs[n] == lambda_vectors[n], (cap, cutoff, order, n, rhs[n], lambda_vectors[n])
    if (cutoff + 1) ** order > cap:
        assert zero_remainder
    return zero_remainder


if __name__ == "__main__":
    cases = [(256, 16, 2), (4096, 16, 3), (3000, 10, 3), (512, 3, 2), (1024, 5, 4)]
    for cap, cutoff, order in cases:
        empty = check(cap, cutoff, order)
        print(f"PASS n<= {cap}, Y={cutoff}, K={order}; remainder {'zero' if empty else 'nonzero'}")
    print(f"PASS {sum(case[0] for case in cases)} exact coefficient comparisons; no floating arithmetic")
