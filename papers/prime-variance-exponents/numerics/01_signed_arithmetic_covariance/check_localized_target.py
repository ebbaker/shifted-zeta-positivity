#!/usr/bin/env python3
"""Exact finite checks for the localized covariance continuation.

Synthetic polynomial probe and prime atom weights p test cofactor/density
algebra; formal prime-log vectors test the exact von Mangoldt identities.
Substantial LLM assistance, GPT-6 (Codex), inherited configuration;
exact serving variant and configured reasoning effort are not exposed.
No Fourier-tail bound or asymptotic arithmetic saving is certified.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import platform
import check_prime_discrepancy_centering as base
import check_aggregated_kernel as agg


def add(a, b, scale=1):
    out = dict(a)
    for p, c in b.items():
        out[p] = out.get(p, 0) + scale * c
        if not out[p]:
            del out[p]
    return out


def formal_arithmetic(limit):
    primes, mu = base.arithmetic(limit)
    logs = [{} for _ in range(limit + 1)]
    lam = [{} for _ in range(limit + 1)]
    for p in primes:
        power = p
        while power <= limit:
            lam[power] = {p: 1}
            for n in range(power, limit + 1, power):
                logs[n][p] = logs[n].get(p, 0) + 1
            power *= p
    return mu, logs, lam


def check_closure():
    limit = 192
    mu, logs, lam = formal_arithmetic(limit)
    comparisons = missing_low_low = 0
    for U in [F(2), F(5, 2), F(3), F(7, 2), F(5), F(13, 2)]:
        for n in range(1, limit + 1):
            full, hi, low_mu, low_lam, low_low = {}, {}, {}, {}, {}
            for d in range(1, n + 1):
                if n % d:
                    continue
                r = n // d
                full = add(full, lam[r], mu[d])
                if d > U and r > U:
                    hi = add(hi, lam[r], mu[d])
                if d <= U:
                    low_mu = add(low_mu, lam[r], mu[d])
                if r <= U:
                    low_lam = add(low_lam, lam[r], mu[d])
                if d <= U and r <= U:
                    low_low = add(low_low, lam[r], mu[d])
            rhs = {p: -mu[n] * e for p, e in logs[n].items() if mu[n]}
            assert full == rhs
            omitted = add(add(rhs, low_mu, -1), low_lam, -1)
            assert hi == add(omitted, low_low)
            comparisons += 2
            missing_low_low += int(hi != omitted)
    assert missing_low_low
    return comparisons, missing_low_low


def check_cofactor(X, U):
    cap = base.floor(2 * X / U)
    primes, mu = base.arithmetic(cap)
    grouped = F(0)
    cofactor = F(0)
    for m in range(base.floor(U) + 1, cap + 1):
        a = sum(mu[d] for d in range(base.floor(U) + 1, m + 1) if m % d == 0)
        atoms = sum((p * base.ell(F(m * p) / X) for p in primes if p > U), F(0))
        density = X / m * base.h(F(m) * U / X)
        grouped += a * (atoms - density) / (base.Q * X)
    for d in range(base.floor(U) + 1, cap + 1):
        for k in range(1, base.floor(2 * X / (d * U)) + 1):
            atoms = sum((p * base.ell(F(k * d * p) / X) for p in primes if p > U), F(0))
            density = X / (k * d) * base.h(F(k * d) * U / X)
            cofactor += mu[d] * (atoms - density) / (base.Q * X)
    assert grouped == cofactor
    return 1


def check_smoothing(X, U, D, h):
    cap = base.floor(2 * X / U)
    primes, _ = base.arithmetic(cap)
    _, mu = base.arithmetic(max(cap, base.floor(U) + h))
    w = {}
    for d in range(base.floor(D) + 1, base.floor(U) + 1):
        terms = {k*d: -1 for k in range(1, base.floor(2 * X / (d * U)) + 1)}
        w[d] = agg.correlation(terms, X, U, 2 * X / U, primes)
    support = list(w)
    weight = lambda n: w.get(n, F(0))
    a = {n: sum((F(mu[n+j]) for j in range(1, h+1)), F(0)) / h for n in support}
    original = sum((mu[n] * w[n] for n in support), F(0))
    smooth = sum((a[n] * w[n] for n in support), F(0))
    residual = restricted = F(0)
    for n in range(1, base.floor(U) + h + 1):
        term = mu[n] * (weight(n) - sum((weight(n-j) for j in range(1, h+1)), F(0))/h)
        residual += term
        if D < n <= U:
            restricted += term
    assert original == smooth + residual
    tv = sum((abs(weight(n+1)-weight(n)) for n in range(0, base.floor(U)+1)), F(0))
    assert abs(residual) <= F(h+1, 2) * tv
    count = len(support)
    mean = sum(a.values(), F(0))/count
    coherent = mean * sum(w.values(), F(0))
    centered = sum(((a[n]-mean)*w[n] for n in support), F(0))
    assert original == coherent + centered + residual
    energy = sum((a[n]**2 for n in support), F(0))
    assert energy == count*mean**2 + sum(((a[n]-mean)**2 for n in support), F(0))
    diagonal = sum(mu[n+j]**2 for j in range(1, h+1) for n in support)
    off_diagonal = sum(mu[n+j]*mu[n+j+r] for r in range(1, h)
                       for j in range(1, h-r+1) for n in support)
    assert h*h*energy == diagonal + 2*off_diagonal
    return 5, int(original != smooth + restricted)


def derivative_pair(poly, logs):
    p, l = {}, {}
    for n, c in poly.items():
        if n:
            p[n-1] = p.get(n-1, F(0)) + n*c
    for n, c in logs.items():
        p[n-1] = p.get(n-1, F(0)) + c
        if n:
            l[n-1] = l.get(n-1, F(0)) + n*c
    return p, l


def moment_pair(poly, logs, power):
    assert all(n+power > -1 for n in set(poly)|set(logs))
    return (sum((c/F(n+power+1) for n,c in poly.items()), F(0))
            - sum((c/F((n+power+1)**2) for n,c in logs.items()), F(0)))


def check_primitive():
    # Synthetic R(v)=v^8, hence F(v)=-(v R''(v))'=-392 v^6.
    # Exact moments use integral_0^1 u^n log(u) du=-1/(n+1)^2.
    comparisons = bad_constant = 0
    for z in range(1, 5):
        for xi in range(1, 5):
            if z == xi:
                poly, logs = {z: -F(2,z), 0: F(2,z)}, {z: F(1), 0: F(1)}
            else:
                poly = {z: F(xi,z*(z-xi)), xi: -F(z,xi*(z-xi)), 0: F(1,z)+F(1,xi)}
                logs = {0: F(1)}
            d1 = derivative_pair(poly,logs)
            d2 = derivative_pair(*d1)
            d3 = derivative_pair(*d2)
            for pair in [(poly,logs),d1,d2]:
                assert sum(pair[0].values(),F(0)) == 0  # values at u=1
                comparisons += 1
            left = -392*moment_pair(poly,logs,6)
            right = 2*moment_pair(*d2,8)+moment_pair(*d3,9)
            for H in [F(1),F(3,2),F(7)]:
                assert left/H**7 == right/H**7
                comparisons += 1
            bad_constant += int(-448*moment_pair(poly,logs,6) != right)
    assert bad_constant
    return comparisons,bad_constant


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args=parser.parse_args()
    formal, low_low = check_closure()
    primitive, bad_primitive_constant = check_primitive()
    cofactor = smooth = endpoint_controls = cases = 0
    for U in [F(3), F(7, 2), F(5), F(11, 2)]:
        for factor in [F(1), F(9, 8), F(3, 2)]:
            X=U*U*factor
            cofactor += check_cofactor(X,U)
            for h in [1,2,3]:
                n, failures = check_smoothing(X,U,(U+1)/2,h)
                smooth += n
                endpoint_controls += failures
                cases += 1
    assert endpoint_controls
    result={
        'date':'2026-10-04', 'status':'EXACT_LOCALIZED_TARGET_ALGEBRA_CHECK',
        'formal_log_comparisons':formal, 'cofactor_density_comparisons':cofactor,
        'smoothing_and_centering_comparisons':smooth,
        'primitive_integration_comparisons':primitive,
        'exact_comparisons':formal+cofactor+smooth+primitive,
        'incorrect_primitive_coefficient_controls':bad_primitive_constant,
        'smoothing_cases':cases, 'omitted_low_low_controls':low_low,
        'omitted_shifted_endpoint_controls':endpoint_controls,
        'python':platform.python_version(),
        'source_sha256':{
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in [Path(__file__),Path(base.__file__),Path(agg.__file__)]
        },
        'scope':'Formal prime-log Mobius/von Mangoldt closure with strict cutoffs; synthetic cofactor and density identities; signed additive smoothing, zero-extended endpoints, centered decomposition, exact shifted autocorrelation; synthetic triple integration by parts and product-cap scaling.',
        'limitations':'No Fourier inversion, spectral tail estimate, fixed-probe constants, actual-mode remainder estimate, global prime bound, or new variance exponent is numerically certified.'
    }
    if args.output:
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
