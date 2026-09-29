#!/usr/bin/env python3
"""Bounded diagnostic of the complete prime-power tail-to-core jump rate.

GPT-6 (Codex), 2026-09-28; serving variant and effort not exposed.
Requires mpmath through the normal Python import path. No zero data or
Weil matrices are used. The finite-envelope check is not interval certified.
"""
import argparse
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import platform
import sys

sys.dont_write_bytecode = True
import mpmath as mp

VERSION = '2026-09-28-v1'


@lru_cache(maxsize=16384)
def kernel_pair(x):
    """Literal kernel with Fourier transform Xi/4, and its first derivative."""
    x = mp.mpf(x)
    sign = -1 if x < 0 else 1
    ex = mp.exp(abs(x))
    nmax = int(mp.ceil(mp.sqrt((mp.mp.dps+35)*mp.log(10)/mp.pi)/ex))+2
    values, derivatives = [], []
    for n in range(1, nmax+1):
        base = mp.pi*n*n
        t = base*ex*ex
        prefactor = base**(-mp.mpf('.25'))*t**mp.mpf('1.25')*mp.exp(-t)
        p = t-mp.mpf('1.5')
        values.append(prefactor*p)
        derivatives.append(sign*prefactor*((mp.mpf('2.5')-2*t)*p+2*t))
    return mp.fsum(values), mp.fsum(derivatives)


def prime_powers(limit):
    """Integer sieve: return (prime power, underlying prime) without logs."""
    flags = bytearray(b'\x01')*(limit+1)
    flags[0:2] = b'\x00\x00'
    for p in range(2, math.isqrt(limit)+1):
        if flags[p]:
            flags[p*p:limit+1:p] = b'\x00'*((limit-p*p)//p+1)
    result = []
    for p in range(2, limit+1):
        if flags[p]:
            power = p
            while power <= limit:
                result.append((power, p))
                power *= p
    return sorted(result)


def core_data(T):
    quadrature = lambda f: mp.quad(f, [-T, 0, T], method='gauss-legendre')
    integral = quadrature(lambda y: mp.exp(-y/2)*kernel_pair(y)[0])
    weighted_square = quadrature(lambda y: mp.exp(-y/2)*
        (kernel_pair(y)[1]+kernel_pair(y)[0]/2)**2)
    endpoint = 2*mp.cosh(T/2)*kernel_pair(T)[0]
    # Cauchy-Schwarz bounds the weighted variation; no absolute-value kink
    # or a numerically inferred derivative-zero count enters this bound.
    variation_upper = endpoint + mp.sqrt(4*mp.sinh(T/2)*weighted_square)
    return dict(T=T, core_integral=integral,
        limiting_core_rate=2*integral,
        missing_rate_from_quarter=mp.mpf('.25')-2*integral,
        cauchy_schwarz_variation_upper=variation_upper,
        weighted_derivative_square_integral=weighted_square)


def one_case(X, T, events, core):
    X = mp.mpf(X)
    x = mp.log(X)
    a, b = X*mp.exp(-T), X*mp.exp(T)
    denominator = mp.cosh(x/2)
    alpha = 2*X/(X+1)
    f = lambda t: kernel_pair(mp.log(X/t))[0]/mp.sqrt(t)
    fa, fb = f(a), f(b)
    psi_a = mp.fsum(weight for n, weight in events if n <= a)
    selected = [(n, weight) for n, weight in events if a < n <= b]
    psi = psi_a
    previous_f = fa
    step_integral_terms, direct_terms = [], []
    relative_envelope_values = [abs(psi_a-a)/a]
    absolute_envelope_values = [abs(psi_a-a)]
    for n, weight in selected:
        fn = f(n)
        # Integral of the step function psi(t) against df(t) on the
        # interval ending immediately before this prime-power jump.
        step_integral_terms.append(psi*(fn-previous_f))
        relative_envelope_values.extend((abs(psi-n)/n, abs(psi+weight-n)/n))
        absolute_envelope_values.extend((abs(psi-n), abs(psi+weight-n)))
        psi += weight
        previous_f = fn
        direct_terms.append(weight*fn)
    step_integral_terms.append(psi*(fb-previous_f))
    relative_envelope_values.append(abs(psi-b)/b)
    absolute_envelope_values.append(abs(psi-b))
    eta = max(relative_envelope_values)
    absolute_envelope = max(absolute_envelope_values)
    raw_integral = mp.sqrt(X)*core['core_integral']
    direct_rate = mp.fsum(direct_terms)/denominator
    continuum_rate = alpha*core['core_integral']
    observed_error = direct_rate-continuum_rate
    # E=psi-t. Integrate E df exactly interval-by-interval in terms of
    # endpoint f values and the one smooth integral of f(t) dt.
    integral_E_df = mp.fsum(step_integral_terms)-(b*fb-a*fa)+raw_integral
    boundary_E_f = fb*(psi-b)-fa*(psi_a-a)
    error_from_integration_by_parts = (boundary_E_f-integral_E_df)/denominator
    bound = eta*alpha*core['cauchy_schwarz_variation_upper']
    return dict(X=int(X), x=x, T=T, lower_endpoint=a, upper_endpoint=b,
        prime_power_count=len(selected), psi_at_lower_endpoint=psi_a,
        psi_at_upper_endpoint=psi, complete_prime_power_rate=direct_rate,
        continuum_rate=continuum_rate, limiting_core_rate=core['limiting_core_rate'],
        rate_minus_quarter=direct_rate-mp.mpf('.25'),
        prime_rate_minus_continuum=observed_error,
        finite_interval_relative_PNT_envelope=eta,
        finite_interval_absolute_PNT_envelope=absolute_envelope,
        conditional_error_bound=bound,
        bound_over_observed_absolute_error=bound/abs(observed_error),
        lower_rate_from_finite_envelope=continuum_rate-bound,
        observed_error_within_floating_bound=bool(abs(observed_error) <= bound),
        integration_by_parts_boundary=boundary_E_f/denominator,
        integration_by_parts_integral=integral_E_df/denominator,
        error_from_integration_by_parts=error_from_integration_by_parts,
        checks=dict(integration_by_parts_replay=abs(error_from_integration_by_parts-observed_error),
            continuum_change_of_variables=abs(raw_integral/denominator-continuum_rate)))


def serializable(value):
    if isinstance(value, dict):
        return {key: serializable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serializable(item) for item in value]
    if isinstance(value, mp.mpf):
        return mp.nstr(value, 45)
    return value


def run(digits):
    mp.mp.dps = digits
    kernel_pair.cache_clear()
    values_X = [20, 100, 1000, 10000]
    values_T = [mp.mpf('.5'), mp.mpf(1)]
    limit = int(mp.ceil(max(values_X)*mp.exp(max(values_T))))
    integer_events = prime_powers(limit)
    events = [(n, mp.log(p)) for n, p in integer_events]
    cores = [core_data(T) for T in values_T]
    rows = [one_case(X, T, events, core)
            for X in values_X for T, core in zip(values_T, cores)]
    return dict(date='2026-09-28', version=VERSION, model='GPT-6 (Codex)',
        exact_serving_variant='not exposed', reasoning_effort='not exposed',
        status='Multiprecision floating diagnostic; no interval certification or uniform-in-X numerical claim',
        python=platform.python_version(), mpmath=mp.__version__, digits=digits,
        kernel_fourier_normalization='Xi/4', exact_weighted_mass='1/8',
        zero_data_used=False, Weil_matrices_used=False,
        sieve_limit=limit, total_prime_powers_in_sieve=len(integer_events),
        sieve_scope='All prime powers required by all eight prescribed central windows',
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        core_windows=cores, cases=rows)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--digits', type=int, default=80)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    if args.digits < 60:
        p.error('Use at least 60 working decimal digits')
    report = serializable(run(args.digits))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    for row in report['cases']:
        print(json.dumps({key: row[key] for key in ('X', 'T', 'prime_power_count',
            'complete_prime_power_rate', 'continuum_rate', 'prime_rate_minus_continuum',
            'conditional_error_bound', 'lower_rate_from_finite_envelope')}), flush=True)
