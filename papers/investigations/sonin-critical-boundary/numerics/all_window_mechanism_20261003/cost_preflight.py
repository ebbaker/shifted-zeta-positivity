#!/usr/bin/env python3
"""Float-only cost records for the explicit relative-mode counting bound.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-03.
Model: GPT-6 (Codex); serving variant and reasoning effort are not exposed.
Uses Python's standard library. No support sweep, matrices, or rank expansion.
See notes/ALL_WINDOW_EFFECTIVE_RELATIVE_TAILS_20261003.md, equations12 and19.
"""
import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

LENGTH = 6 / 5
PRIMES = (2, 3)
EPSILONS = (1.0, 0.5, 0.1)
G0 = 57 / 10**6
EULER_GAMMA = 0.577215664901532860606512090082402431


def count_log10(energy):
    """Return logs of exact expression(12) and its simple exponential cap.

    Evaluates only logarithms: (L/(2pi))*(E+1)*sqrt(exp(2(E+1))-1).
    The strictly larger cap replaces the square root by exp(E+1).
    At these parameters their logarithms agree to machine precision.
    """
    if energy < 0:
        raise ValueError('The chosen closed counting formula requires E>=0')
    x = energy + 1
    simple = (math.log(LENGTH / (2 * math.pi)) + math.log(x) + x) / math.log(10)
    correction = math.log1p(-math.exp(-2 * x)) / (2 * math.log(10))
    return dict(expression_12_log10=simple + correction,
                simple_exponential_cap_log10=simple,
                rounded_simple_cap_log10=round(simple))


def active_powers():
    rows = []
    for p in PRIMES:
        m, n = 1, p
        while math.log(n) < LENGTH:
            rows.append(dict(prime=p, exponent=m, power=n,
                             amplitude=2 * math.log(p) / math.sqrt(n)))
            m, n = m + 1, n * p
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('cost_preflight.json'))
    args = parser.parse_args()
    powers = active_powers()
    rho = math.prod(((1 - p**-0.5) / (1 + p**-0.5))**2 for p in PRIMES)
    gamma0 = -EULER_GAMMA - math.pi / 2 - 3 * math.log(2) - math.log(math.pi)
    k0 = LENGTH * math.sqrt((1 - G0) / G0)
    g_s = rho * G0
    k_s = LENGTH * math.sqrt((1 - g_s) / g_s)
    c = sum(row['amplitude'] for row in powers)
    rows = []
    for epsilon in EPSILONS:
        threshold = k_s / epsilon
        direct = threshold + c + k_s - gamma0
        transport = threshold / rho + k0 - gamma0
        rows.append(dict(epsilon=epsilon, spectral_threshold_lambda=threshold,
                         direct_energy=direct, transport_energy=transport,
                         direct=count_log10(direct), transport=count_log10(transport)))
    payload = dict(
        status='FLOATING_RESOURCE_DIAGNOSTIC_NOT_A_CERTIFICATE',
        date='2026-10-03', model='GPT-6 (Codex)',
        serving_variant='not exposed', reasoning_effort='not exposed',
        runtime=dict(python=platform.python_version(), dependencies='standard library only'),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        parameters=dict(L='6/5', prime_set=list(PRIMES), g0='57/1000000',
                        epsilons=list(EPSILONS)),
        constants=dict(rho_s=rho, gamma0=gamma0, k0=k0, g_s=g_s, k_s=k_s,
                       c_s_l=c, active_prime_powers=powers),
        count_bound_formula='L/(2*pi) * (E+1) * sqrt(exp(2*(E+1))-1)',
        direct_energy_formula='Lambda + C_S,L + k_S,L - gamma0',
        transport_energy_formula='Lambda/rho_S + k_0,L - gamma0',
        threshold_formula='Lambda = k_S,L / epsilon',
        rows=rows,
        limitations=[
            'Logs of pessimistic sufficient upper bounds, not measured eigenvalue counts or necessary ranks.',
            'Counts apply separately to positive and negative relative eigenvalues exceeding epsilon in magnitude.',
            'Only the prescribed L=6/5 and three epsilon values are evaluated; no source rank is expanded.',
            'No outward rounding, resolvent columns, source-gap certificate, or all-window positivity is supplied.',
            'The exact count expression and its simple exponential cap differ below floating resolution here.'
        ])
    args.output.write_text(json.dumps(payload, indent=2) + '\n')
    print(json.dumps(dict(output=str(args.output), constants=payload['constants'],
                          rows=rows), indent=2))


if __name__ == '__main__':
    main()
