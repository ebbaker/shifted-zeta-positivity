#!/usr/bin/env python3
"""Finite controls for the orbit-weight / Bost-Connes KMS research note.

These are exact finite combinatorial checks and floating diagnostics, not
interval certificates or a construction of a causal arithmetic response.
Run with Python 3 and mpmath; no external data or sibling imports are used.
Prepared for Edward Baker with GPT-6 (Codex) assistance; effort not exposed.
"""
import argparse
import hashlib
import itertools
import json
import math
import platform
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50
CASES = []
SAMPLES = {}
M = 360


def check(name, value, threshold='1e-39', comparison='<=', exact=False):
    value, threshold = mp.mpf(value), mp.mpf(threshold)
    passed = value <= threshold if comparison == '<=' else value >= threshold
    CASES.append(dict(name=name, value=float(value), threshold=float(threshold),
                      comparison=comparison, passed=bool(passed),
                      arithmetic='exact integer' if exact else 'floating'))


def primes_to(n):
    sieve = bytearray(b'\1') * (n + 1)
    sieve[:2] = b'\0\0'
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\0' * ((n-p*p)//p+1)
    return [p for p in range(2, n+1) if sieve[p]]


def prime_divisors(n):
    ans, d = [], 2
    while d*d <= n:
        if n % d == 0:
            ans.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ans.append(n)
    return ans


def coeff(n, w):
    return mp.power(n, w-mp.mpf('.5')) * mp.fprod(
        1-mp.power(p, -2*w) for p in prime_divisors(n))


def mobius(n):
    ps = prime_divisors(n)
    return 0 if any(n % (p*p) == 0 for p in ps) else (-1)**len(ps)


def affinity(p, beta):
    p = mp.mpf(p)
    return mp.sqrt((1-1/p)*(1-p**(-beta)))/(1-p**(-(beta+1)/2))


def shell_amp(p, beta, m):
    q = mp.power(p, -beta)
    return mp.sqrt((1-q)*q**m)


def run():
    # Integer-dimensional primitive residue counts, computed by enumeration.
    for d in (1, 2, 3):
        for n in (2, 3, 4, 6):
            actual = sum(math.gcd(n, *xs) == 1
                         for xs in itertools.product(range(n), repeat=d))
            expected = n**d
            for p in prime_divisors(n):
                expected = expected // p**d * (p**d-1)
            check(f'primitive_residues_d{d}_n{n}', abs(actual-expected),
                  0, exact=True)
    # Divisibility projections, not truncated unilateral-shift matrices.
    for a, b in ((2, 3), (2, 4), (4, 6), (6, 9)):
        error = sum(((k % a == 0) and (k % b == 0)) !=
                    (k % math.lcm(a, b) == 0) for k in range(1, 109))
        check(f'projection_lcm_{a}_{b}', error, 0, exact=True)
    # Character phases as exponents mod 6: S has phases 0,3; R has 0,2,4.
    chars = [(a, b, (b-a) % 6) for a in (0, 3) for b in (0, 2, 4)]
    check('only_trivial_scalar_character_preserves_cusp',
          int([(a, b) for a, b, t in chars if t == 0] != [(0, 0)]),
          0, exact=True)

    for w in map(mp.mpf, ('.25', '.4', '.5')):
        tag, beta = str(w), 2*w
        row = {}
        for n in (2, 3, 4, 6, 8, 9):
            # Euler quotient convolution using mu(d), independently of product.
            convolution = mp.fsum(mobius(d)*mp.power(n//d, w-mp.mpf('.5'))
                                  * mp.power(d, -w-mp.mpf('.5'))
                                  for d in range(1, n+1) if n % d == 0)
            check(f'coefficient_mobius_w{tag}_n{n}', abs(coeff(n, w)-convolution))
            row[str(n)] = mp.nstr(coeff(n, w), 20)
        SAMPLES[f'coefficients_w{tag}'] = row

        # Genuine finite-place Gibbs state: occupation numbers at 2 and 3.
        # Truncate each normalized geometric law. Omitted mass is at most
        # q2^(M+1)+q3^(M+1); do not renormalize the truncated state.
        q2, q3 = mp.power(2, -beta), mp.power(3, -beta)
        partial_all = (1-q2**(M+1))*(1-q3**(M+1))
        check(f'finite_place_state_mass_w{tag}', abs(1-partial_all),
              q2**(M+1)+q3**(M+1)+mp.mpf('1e-48'))
        # P_6 selects zero occupations in both places.
        native_p6 = (1-q2)*(1-q3)
        check(f'primitive_projection_P6_w{tag}',
              abs(mp.power(6, (beta-1)/2)*native_p6-coeff(6, w)))

        # Full Dirichlet series in a safe convergence half-plane. For real p=8,
        # 0<c_n<=n^(w-1/2), giving an elementary integral remainder bound.
        p, cutoff = mp.mpf(8), 1500
        partial = mp.fsum(coeff(n, w)*mp.power(n, -p)
                          for n in range(1, cutoff+1))
        ratio = mp.zeta(p+mp.mpf('.5')-w)/mp.zeta(p+mp.mpf('.5')+w)
        alpha = p+mp.mpf('.5')-w
        tail_bound = mp.power(cutoff, 1-alpha)/(alpha-1)
        check(f'full_zeta_ratio_series_w{tag}', abs(ratio-partial), tail_bound)
        check(f'full_zeta_ratio_positive_tail_w{tag}', ratio-partial, 0, '>=')

        # Shift derivative of the finite Euler product versus its prime-power
        # logarithmic expansion, which is the prime part of -a_omega.
        ps, repetitions, p = (2, 3, 5), 50, mp.mpf(4)
        def log_euler(omega):
            return mp.fsum(mp.log(1-mp.power(l, -p-mp.mpf('.5')-omega))
                           -mp.log(1-mp.power(l, -p-mp.mpf('.5')+omega))
                           for l in ps)
        series = 2*mp.fsum(mp.log(l)*mp.power(l, -r*(p+mp.mpf('.5')))
                           * mp.cosh(w*r*mp.log(l))
                           for l in ps for r in range(1, repetitions+1))
        check(f'prime_source_derivative_w{tag}', abs(mp.diff(log_euler, w)-series))

        # Isolated input pulse and its first delayed copy on log2<L<log3.
        # Normalize f=epsilon^(-1/2) on (0,epsilon), epsilon=.05 and L=.9.
        eps, L, delay = mp.mpf('.05'), mp.mpf('.9'), mp.log(2)
        c2 = coeff(2, w)
        def output(t):
            return ((1 if 0 < t < eps else 0)
                    + c2*(1 if delay < t < delay+eps else 0))/mp.sqrt(eps)
        energy = mp.quad(lambda t: output(t)**2, [0, eps, delay, delay+eps, L])
        check(f'direct_Euler_pulse_energy_w{tag}', abs(energy-(1+c2*c2)))
        check(f'direct_Euler_noncontractive_w{tag}', energy-1, '.05', '>=')
        SAMPLES[f'direct_Euler_energy_w{tag}'] = mp.nstr(energy, 20)

    check('first_coefficient_shift_tangent',
          abs(mp.diff(lambda w: coeff(2, w), mp.mpf('.5'))-mp.mpf('1.5')*mp.log(2)))

    # Radial Haar half-densities: norm, affinity, and actual unitary dilation.
    for beta in map(mp.mpf, ('.5', '.8', '1')):
        for p in (2, 3):
            tag = f'p{p}_b{beta}'
            q = mp.power(p, -beta)
            norm = mp.fsum(shell_amp(p, beta, m)**2 for m in range(M+1))
            check('state_norm_'+tag, abs(norm-1))
            inner = mp.fsum(shell_amp(p, 1, m)*shell_amp(p, beta, m)
                           for m in range(M+1))
            check('Haar_affinity_'+tag, abs(inner-affinity(p, beta)))
            for r in (-2, 1):
                # Integrate u_beta(x) p^(-r/2) u_beta(p^r x) in Haar shells.
                C = (1-q)/(1-mp.mpf(1)/p)
                corr = mp.fsum(C*(1-mp.mpf(1)/p)*mp.power(p, -m)
                               * mp.power(p, -m*(beta-1)/2)
                               * mp.power(p, -(m+r)*(beta-1)/2)
                               * mp.power(p, -mp.mpf(r)/2)
                               for m in range(max(0, -r), M+1))
                check(f'dilation_correlation_{tag}_r{r}',
                      abs(corr-mp.power(p, -beta*abs(r)/2)))
    for p in (2, 3, 5):
        # Differentiate normalized amplitudes, then sum squared derivatives.
        tangent = mp.fsum(mp.diff(lambda w: shell_amp(p, 2*w, m), mp.mpf('.5'))**2
                          for m in range(M+1))
        formula = mp.log(p)**2 * p/(p-1)**2
        check(f'local_shift_tangent_norm_p{p}', abs(tangent-formula))

    # Finite-place products are samples of an analytically proved divergence;
    # their monotonicity and exact local formula do not prove the infinite limit.
    primes = primes_to(100000)
    table = []
    log_overlap = {mp.mpf('.5'): mp.mpf(0), mp.mpf('.8'): mp.mpf(0)}
    tangent = mp.mpf(0)
    for j, p in enumerate(primes, start=1):
        for beta in log_overlap:
            log_overlap[beta] += mp.log(affinity(p, beta))
        tangent += mp.log(p)**2 * p/(p-1)**2
        if j in (4, 10, 25, 168, 1229, 9592):
            table.append(dict(prime_count=j, largest_prime=p,
                              affinity_beta_half=mp.nstr(mp.exp(log_overlap[mp.mpf('.5')]), 18),
                              affinity_beta_point8=mp.nstr(mp.exp(log_overlap[mp.mpf('.8')]), 18),
                              shift_tangent_norm_squared=mp.nstr(tangent, 18)))
    SAMPLES['finite_place_affinities'] = table
    check('beta_half_overlap_below_2e-12_at_9592_places',
          mp.exp(log_overlap[mp.mpf('.5')]), '2e-12')
    check('shift_tangent_exceeds_66_at_9592_places', tangent, 66, '>=')
    # This tail product measures failure of the finite-vacuum embeddings to be
    # Cauchy: compare first 4 places to all 9592, using baseline vacua elsewhere.
    tail_overlap = mp.exp(log_overlap[mp.mpf('.5')]) / mp.mpf(table[0]['affinity_beta_half'])
    SAMPLES['nested_vacuum_distance_squared_beta_half'] = mp.nstr(2*(1-tail_overlap), 18)
    check('nested_vacuum_distance_squared_exceeds_1p99', 2*(1-tail_overlap), '1.99', '>=')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    run()
    record = dict(schema_version=1, date='2026-09-23', prepared_for='Edward Baker',
                  model='GPT-6 (Codex; developer-provided identity)',
                  effort='not exposed; not inferred', python=platform.python_version(),
                  mpmath=mp.__version__,
                  program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  parameters=dict(decimal_digits=50, shell_cutoff=M,
                                  shifts=['0.25', '0.4', '0.5'],
                                  Dirichlet_cutoff=1500, largest_prime_bound=100000),
                  scope='Primitive orbit coefficient identities, BC diagonal finite-place '
                        'state controls and scoped norm exclusions; no scattering '
                        'construction, interval certificate or RH result',
                  case_count=len(CASES), exact_integer_cases=sum(
                      c['arithmetic']=='exact integer' for c in CASES),
                  all_pass=all(c['passed'] for c in CASES), cases=CASES, samples=SAMPLES)
    output = json.dumps(record, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
        print(json.dumps({k: record[k] for k in ('case_count', 'exact_integer_cases', 'all_pass')}))
        for c in CASES:
            if not c['passed']:
                print(json.dumps(c))
    else:
        print(output, end='')
    raise SystemExit(not record['all_pass'])


if __name__ == '__main__':
    main()
