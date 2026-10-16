#!/usr/bin/env python3
"""Exact checks of summed kernels and signed divisor localization.

Synthetic compact polynomial ell from the adjacent centering checker;
prime atoms weighted by p, not log(p). No asymptotic bound is tested.
Prepared with substantial LLM assistance, GPT-6 (Codex); configured
reasoning effort and exact serving variant are not exposed.
"""
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path
import platform
import check_prime_discrepancy_centering as base

LP = base.LPOLY
DP = [i * LP[i] for i in range(1, len(LP))]


def integral(poly, scale, left, right, theta):
    """Integral of (theta-t)*poly(scale*t) with compact support [1,2]."""
    lo, hi = max(left, 1 / scale), min(right, 2 / scale)
    if lo >= hi:
        return F(0)
    return sum((c * scale**i * (
        theta * (hi**(i + 1) - lo**(i + 1)) / (i + 1)
        - (hi**(i + 2) - lo**(i + 2)) / (i + 2)
    ) for i, c in enumerate(poly)), F(0))


def error(t, primes):
    return F(sum(p for p in primes if p <= t)) - t


def terms_primitive(terms, X, t):
    return sum((a * base.ell(F(m) * t / X) for m, a in terms.items()), F(0))


def terms_kernel(terms, X, t):
    return sum((a * m * base.kernel(DP, F(m) * t / X) / X**2
                for m, a in terms.items()), F(0))


def correlation(terms, X, U, T, primes, center=False):
    result = F(0)
    points = [U] + [F(p) for p in primes if U < p < T] + [T]
    subtract = error(U, primes) if center else F(0)
    for lo, hi in zip(points, points[1:]):
        theta = F(sum(p for p in primes if p <= lo)) - subtract
        for m, a in terms.items():
            result += a * m / X**2 * integral(DP, F(m) / X, lo, hi, theta)
    return result


def complement_terms(mu, D, cap):
    return {m: -sum(mu[d] for d in range(1, base.floor(D) + 1) if m % d == 0)
            for m in range(1, cap + 1)}


def run_case(X, U):
    cap = base.floor(2 * X / U)
    primes, mu = base.arithmetic(cap)
    direct = {m: sum(mu[d] for d in range(base.floor(U) + 1, m + 1) if m % d == 0)
              for m in range(1, cap + 1)}
    complement = complement_terms(mu, U, cap)
    # delta_1 correction is required as an arithmetic identity.
    assert direct[1] == complement[1] + 1
    assert all(direct[m] == complement[m] for m in range(2, cap + 1))
    comparisons = 2
    singleton_controls = endpoint_controls = terminal_controls = 0
    D = (U + 1) / 2
    low = complement_terms(mu, D, cap)
    high = {m: complement[m] - low[m] for m in complement}
    end = 2 * X / U
    for t in [U, (3 * U + end) / 4, (U + end) / 2, end]:
        p0 = terms_primitive(direct, X, t)
        k0 = terms_kernel(direct, X, t)
        assert p0 == base.ell(t / X) + terms_primitive(complement, X, t)
        assert k0 == base.kernel(DP, t / X) / X**2 + terms_kernel(complement, X, t)
        assert terms_kernel(complement, X, t) == (
            terms_kernel(low, X, t) + terms_kernel(high, X, t))
        assert terms_primitive(complement, X, t) == (
            terms_primitive(low, X, t) + terms_primitive(high, X, t))
        comparisons += 4
        singleton_controls += int(k0 != terms_kernel(complement, X, t))
    # Outside the retained interval, the global singleton term can be visible.
    control_t = F(5, 4) * X
    assert terms_kernel(direct, X, control_t) == (
        base.kernel(DP, control_t / X) / X**2 + terms_kernel(complement, X, control_t))
    comparisons += 1
    singleton_controls += int(terms_kernel(direct, X, control_t) != terms_kernel(complement, X, control_t))

    for T in sorted(set([U, (U + end) / 2, end] + [F(p) for p in primes if U < p < end][:2])):
        for terms in [direct, low, high]:
            corr = correlation(terms, X, U, T, primes)
            boundary = (error(T, primes) * terms_primitive(terms, X, T)
                        - error(U, primes) * terms_primitive(terms, X, U)) / X
            atoms = sum((p * terms_primitive(terms, X, F(p)) for p in primes if U < p <= T), F(0))
            density = sum((a * X / m * (base.h(F(m) * U / X) - base.h(F(m) * T / X))
                           for m, a in terms.items()), F(0))
            assert corr == boundary - (atoms - density) / X
            comparisons += 1
            endpoint_controls += int(boundary != 0)
        lhs = correlation(direct, X, U, T, primes)
        rhs = correlation(low, X, U, T, primes) + correlation(high, X, U, T, primes)
        single = correlation({1: 1}, X, U, T, primes)
        assert lhs == rhs + single
        centered = correlation(direct, X, U, T, primes, center=True)
        assert centered == lhs - error(U, primes) * (
            terms_primitive(direct, X, T) - terms_primitive(direct, X, U)) / X
        comparisons += 2

    # Terminal exact Mobius shell, including real U and boundary m=2U.
    terminal_start = X / U
    terminal_terms = {m: mu[m] for m in range(base.floor(U) + 1, min(cap, base.floor(2 * U)) + 1)}
    for t in [terminal_start, (terminal_start + end) / 2, end]:
        assert terms_kernel(direct, X, t) == terms_kernel(terminal_terms, X, t)
        comparisons += 1
    assert correlation(direct, X, terminal_start, end, primes) == correlation(
        terminal_terms, X, terminal_start, end, primes)
    comparisons += 1
    terminal_controls += int(correlation(direct, X, U, end, primes) != correlation(
        terminal_terms, X, U, end, primes))
    return comparisons, singleton_controls, endpoint_controls, terminal_controls


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    totals = [0, 0, 0, 0]
    cases = 0
    for U in [F(2), F(5, 2), F(3), F(7, 2), F(4), F(5), F(11, 2)]:
        for factor in [F(1), F(9, 8), F(3, 2), F(2)]:
            values = run_case(U * U * factor, U)
            totals = [a + b for a, b in zip(totals, values)]
            cases += 1
    assert all(totals[1:]), 'Negative controls must detect all three invalid simplifications.'
    result = {
        'date': '2026-10-04', 'status': 'EXACT_RATIONAL_KERNEL_CHECK',
        'cases': cases, 'exact_comparisons': totals[0],
        'nonzero_singleton_controls': totals[1],
        'omitted_endpoint_control_failures': totals[2],
        'terminal_shell_used_globally_control_failures': totals[3],
        'python': platform.python_version(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'shared_kernel_source_sha256': hashlib.sha256(Path(base.__file__).read_bytes()).hexdigest(),
        'scope': 'Finite signed kernel identities, divisor split, partial Stieltjes integration, centered error, terminal Mobius shell.',
        'limitations': 'Synthetic polynomial kernel and prime atoms weighted by p. Not fixed-probe constants, Fourier convergence, zeta residues, or an asymptotic power estimate.'
    }
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
