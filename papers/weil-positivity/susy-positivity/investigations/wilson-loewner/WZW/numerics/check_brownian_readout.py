#!/usr/bin/env python3
"""Finite diagnostics for a Brownian bridge / Bessel first-passage readout.

Requires mpmath. No Monte Carlo, zero table, or RH assumption is used.
Floating quadrature and series checks are not interval certificates.
Prepared for Edward Baker, GPT-6 (Codex), 23 September 2026.
Effort not exposed; not inferred.
"""
import argparse
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import platform

import mpmath as mp


TERMS = 12
CASES = []


def check(name, value, threshold, comparison='<='):
    value, threshold = float(value), float(threshold)
    passed = mp.isfinite(value) and (
        value <= threshold if comparison == '<=' else value >= threshold)
    CASES.append(dict(name=name, value=value, threshold=threshold,
                      comparison=comparison, passed=bool(passed), kind='floating'))


def relative(a, b):
    return abs(a - b) / max(mp.mpf(1), abs(b))


def density_small(d):
    return 4 * mp.pi * d**(-mp.mpf('3.5')) * mp.fsum(
        n*n * (mp.pi*n*n - mp.mpf('1.5')*d) * mp.exp(-mp.pi*n*n/d)
        for n in range(1, TERMS + 1))


def density_large(d):
    return 2 * mp.pi * mp.fsum(
        n*n * (2*mp.pi*n*n*d - 3) * mp.exp(-mp.pi*n*n*d)
        for n in range(1, TERMS + 1))


def density(d):
    if d <= 0 or mp.isinf(d):
        return mp.mpf(0)
    return density_small(d) if d < 1 else density_large(d)


def integral(fun):
    return mp.quad(fun, [0, mp.mpf('.25'), mp.mpf('.5'), 1, 2, 4, 8, mp.inf])


@lru_cache(maxsize=None)
def moment(s, derivative=0):
    # s is the exponent of Y=sqrt(D), not of D.
    return integral(lambda d: d**(s/2) * (mp.log(d)/2)**derivative * density(d))


def xi(s):
    s = mp.mpc(s)
    if s in (0, 1):
        return mp.mpf('.5')
    # The reflection avoids individual gamma poles at negative even integers.
    if mp.re(s) < mp.mpf('.5'):
        return xi(1-s)
    return s*(s-1)/2 * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)


def target(p, omega):
    return xi(mp.mpf('.5') + p - omega) / xi(mp.mpf('.5') + p + omega)


def target_source(p, omega):
    return mp.fsum(mp.diff(xi, s)/xi(s)
                   for s in (mp.mpf('.5')+p-omega, mp.mpf('.5')+p+omega))


def native(p, lam):
    if p == 0 or lam == 0:
        return mp.mpf(1)
    z = mp.sqrt(mp.pi * lam * p)
    return (z/mp.sinh(z))**2


def native_density(u, lam):
    return density(u/lam)/lam if u > 0 else mp.mpf(0)


def centered_density(x):
    return 2*mp.exp(mp.mpf('2.5')*x)*density(mp.exp(2*x))/moment(mp.mpf('.5'))


def prime_free(u, omega):
    # Full inherited gamma plus rational kernel. v=u*z^(1/omega)
    # removes its integrable collision singularity in the convolution term.
    A = (2*mp.pi)**omega/mp.gamma(omega)
    def ratio(v):
        return -mp.expm1(-2*v)/(2*v) if v else mp.mpf(1)
    correction = mp.quad(lambda z: mp.exp(-(3-2*omega)*u*z**(1/omega))
                         * ratio(u*z**(1/omega))**(omega-1), [0, 1])
    return A*u**(omega-1) * (
        mp.exp(-(mp.mpf('2.5')-omega)*u)*ratio(u)**(omega-1)
        - 2*u*mp.exp((mp.mpf('.5')-omega)*u)*correction)


def json_complex(z):
    return dict(real=mp.nstr(mp.re(z), 24), imag=mp.nstr(mp.im(z), 24))


def run(dps):
    mp.mp.dps = dps
    omega = mp.mpf('.25')
    observations = {}

    for d in map(mp.mpf, ['.35', '.5', '1', '1.5', '2.5']):
        check(f'dual density formulas d={d}',
              relative(density_small(d), density_large(d)), 1e-32)

    exponents = [mp.mpf(s) for s in ['-2', '-1', '0', '.5', '1', '2', '4']]
    exponents.append(mp.mpc('.5', '3'))
    for s in exponents:
        check(f'density Mellin moment s={s}', relative(moment(s), 2*xi(s)), 1e-30)
    mean = moment(mp.mpf(2))
    variance = moment(mp.mpf(4))-mean**2
    check('exit time mean pi/3', abs(mean-mp.pi/3), 1e-30)
    check('exit time variance pi^2/45', abs(variance-mp.pi**2/45), 1e-30)
    observations['unit_delay_mean'] = mp.nstr(mean, 24)
    observations['unit_delay_variance'] = mp.nstr(variance, 24)

    for p in [mp.mpf('.2'), mp.mpf(1), mp.mpf(5), mp.mpc(1, 2)]:
        actual = integral(lambda d: mp.exp(-p*d)*density(d))
        check(f'density Laplace versus exit ODE p={p}', relative(actual, native(p, 1)), 1e-30)

    p = mp.mpf(2)
    lo, hi = mp.mpf('.5')+p-omega, mp.mpf('.5')+p+omega
    k_from_moments = moment(lo)/moment(hi)
    a_from_moments = moment(lo, 1)/moment(lo) + moment(hi, 1)/moment(hi)
    check('full arithmetic quotient from moments', relative(k_from_moments, target(p, omega)), 1e-30)
    check('full arithmetic source from moment derivatives', relative(a_from_moments, target_source(p, omega)), 1e-30)
    observations['p2_omega_quarter'] = dict(
        arithmetic_transfer=json_complex(target(p, omega)),
        first_passage_transfer=json_complex(native(p, omega)),
        arithmetic_source=json_complex(a_from_moments))
    check('first passage and arithmetic transfers differ', abs(native(p, omega)-target(p, omega)), .1, '>=')

    h = mp.mpf('1e-8')
    check('small radius first variation', abs((1-native(p, h))/h - mp.pi*p/3), 1e-6)
    observations['zero_shift_sources_at_p2'] = dict(
        first_passage=mp.nstr(mp.pi*p/3, 24),
        arithmetic=json_complex(target_source(p, 0)))
    check('zero shift source mismatch', abs(mp.pi*p/3-target_source(p, 0)), 1, '>=')

    for u in map(mp.mpf, ['.02', '.01']):
        A = (2*mp.pi)**omega/mp.gamma(omega)
        scale = A*u**(omega-1)
        check(f'arithmetic collision asymptotic u={u}', abs(prime_free(u, omega)/scale-1), .1)
        check(f'Brownian collision deficit u={u}', abs(native_density(u, omega)/scale), 1e-9)

    ell = mp.log(2)
    c2 = (2**omega-2**(-omega))/mp.sqrt(2)
    A = (2*mp.pi)**omega/mp.gamma(omega)
    first_delay = []
    for eps in map(mp.mpf, ['.001', '.0001']):
        increment = c2*prime_free(eps, omega)
        scaled = eps**(1-omega)*increment
        check(f'first arithmetic delay coefficient eps={eps}', abs(scaled/(c2*A)-1), .005)
        brownian_scaled = eps**(1-omega)*native_density(ell+eps, omega)
        first_delay.append(dict(epsilon=mp.nstr(eps), arithmetic_increment=mp.nstr(increment, 20),
                                arithmetic_scaled=mp.nstr(scaled, 20), brownian_scaled=mp.nstr(brownian_scaled, 20)))
    check('Brownian scaled response vanishes at first prime',
          mp.mpf(first_delay[-1]['brownian_scaled'])/mp.mpf(first_delay[0]['brownian_scaled']), .2)
    observations['first_delay'] = first_delay
    observations['first_delay_expected_scaled_coefficient'] = mp.nstr(c2*A, 24)

    for freq in [1, 4, 10]:
        b = native(mp.j*freq, omega)
        k = target(mp.j*freq, omega)
        check(f'arithmetic boundary modulus freq={freq}', abs(abs(k)-1), 1e-35)
        check(f'positive averaging loses boundary norm freq={freq}', 1-abs(b)**2, .001, '>=')

    # Exact probability identity on (0,L) for f=1_(0,L)/sqrt(L).
    # E||shift_D f||_(0,L)^2 = E(1-D/L)_+; mean output is F_D(t)/sqrt(L).
    L = mp.mpf(1)
    def cdf(d):
        if d <= 0:
            return mp.mpf(0)
        if d < 1:
            return 4*mp.pi*d**(-mp.mpf('1.5'))*mp.fsum(
                n*n*mp.exp(-mp.pi*n*n/d) for n in range(1, TERMS+1))
        return 1+2*mp.fsum((1-2*mp.pi*n*n*d)*mp.exp(-mp.pi*n*n*d)
                          for n in range(1, TERMS+1))
    breaks = [0, omega, 2*omega, L]
    mean_path_energy = mp.quad(lambda u: cdf(u/omega)/L, breaks)
    mean_path_energy_from_density = mp.quad(lambda u: (1-u/L)*native_density(u, omega), breaks)
    output_energy = mp.quad(lambda u: cdf(u/omega)**2/L, breaks)
    conditional_variance = mp.quad(lambda u: (cdf(u/omega)-cdf(u/omega)**2)/L, breaks)
    future_energy = 1-mean_path_energy_from_density
    check('finite window path energy two formulas', abs(mean_path_energy-mean_path_energy_from_density), 1e-30)
    check('finite window variance plus future balance', abs(1-output_energy-conditional_variance-future_energy), 1e-30)
    check('positive conditional variance', conditional_variance, .01, '>=')
    check('positive future energy', future_energy, .1, '>=')
    observations['unit_window_constant_input'] = {
        key:mp.nstr(value, 24) for key,value in dict(output_energy=output_energy,
        conditional_variance=conditional_variance, future_energy=future_energy).items()}

    for x in map(mp.mpf, ['.1', '.3', '.7']):
        check(f'centered log range reflection x={x}', relative(centered_density(x), centered_density(-x)), 1e-30)
    negative_mass = mp.quad(lambda d: d**((mp.mpf('.5')-omega)/2)*density(d),
                            [0, mp.mpf('.25'), mp.mpf('.5'), 1])/moment(mp.mpf('.5')-omega)
    check('native logarithmic readout has negative delays', negative_mass, .5, '>=')
    observations['negative_delay_probability_tilt_quarter'] = mp.nstr(negative_mass, 24)
    phase_values = []
    for freq in [1, 10, 30, 50]:
        # Compute both physical Fourier readouts from density quadrature,
        # independently of the xi formula used for the target. Guard digits
        # compensate for the very small transforms at large frequency.
        with mp.workdps(dps+15):
            plus = moment(mp.mpf('.5')+omega+mp.j*freq)/moment(mp.mpf('.5')+omega)
            minus = moment(mp.mpf('.5')-omega+mp.j*freq)/moment(mp.mpf('.5')-omega)
            check(f'logarithmic density quotient versus arithmetic phase freq={freq}',
                  relative(minus/plus, target(mp.j*freq, omega)), 1e-30)
        phase_values.append(dict(frequency=freq, smoothing_modulus=mp.nstr(abs(plus), 24),
                                 inverse_amplification=mp.nstr(1/abs(plus), 24)))
    observations['logarithmic_smoothing'] = phase_values
    check('logarithmic inverse is already large at frequency 50',
          mp.mpf(phase_values[-1]['inverse_amplification']), 1e9, '>=')

    # Independent precision refinement of the two complex transform integrals.
    coarse_moment = moment(mp.mpc('.5', '3'))
    with mp.workdps(dps+15):
        refined_moment = integral(lambda d: d**(mp.mpc('.5', '3')/2)*density(d))
        check('complex moment precision refinement', relative(coarse_moment, refined_moment), 1e-30)

    return dict(schema_version=1, date='2026-09-23',
                prepared_for='Edward Baker', model='GPT-6 (Codex; developer-provided identity)',
                effort='not exposed; not inferred', python=platform.python_version(),
                dependencies=dict(mpmath=mp.__version__),
                parameters=dict(decimal_precision=dps, theta_terms=TERMS,
                                comparison_shift='.25', exit_scale='.25', norm_window='1'),
                scope='Brownian/Bessel scalar identities, specified averaged first-passage readout, and logarithmic readout diagnostics; no RH test, interval certification, or general Brownian exclusion',
                case_count=len(CASES), all_pass=all(c['passed'] for c in CASES),
                observations=observations, cases=CASES,
                program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--dps', type=int, default=45)
    args=parser.parse_args()
    if args.dps < 40:
        parser.error('Use at least 40 decimal digits for the stated diagnostic thresholds.')
    result=run(args.dps)
    text=json.dumps(result, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
        print(json.dumps(dict(case_count=result['case_count'], all_pass=result['all_pass'],
                              output=str(args.output), failed=[c for c in CASES if not c['passed']])))
    else:
        print(text, end='')
    raise SystemExit(not result['all_pass'])


if __name__ == '__main__':
    main()
