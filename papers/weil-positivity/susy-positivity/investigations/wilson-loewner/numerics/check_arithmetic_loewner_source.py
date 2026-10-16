#!/usr/bin/env python3
"""Arithmetic logarithmic derivative / generalized Loewner source controls.

Prepared for Edward Baker, GPT-6 (Codex), 2026-09-22.
Effort not exposed. Requires mpmath; numerical evaluations are not ball
certificates. No zero table or assumption that all xi zeros are critical.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

import mpmath as mp


def xi(s):
    return s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s) / 2


def H(p):
    return xi(mp.mpf('0.5') + p)


def m(p):
    s = mp.mpf('0.5') + p
    return (1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
            + mp.digamma(s / 2) / 2 + mp.zeta(s, derivative=1) / mp.zeta(s))


def K(p, omega):
    return H(p - omega) / H(p + omega)


def a(p, omega):
    return m(p - omega) + m(p + omega)


def cayley(p):
    return (p - 1) / (p + 1)


def uncayley(w):
    return (1 + w) / (1 - w)


def source(w, eta):
    return m(eta + uncayley(w)) / m(eta + 1)


def rk4(rhs, value, duration, steps):
    dt = duration / steps
    for _ in range(steps):
        k1 = rhs(value)
        k2 = rhs(value + dt * k1 / 2)
        k3 = rhs(value + dt * k2 / 2)
        k4 = rhs(value + dt * k3)
        value += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return value


def prime_powers(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for n in range(2, int(limit ** 0.5) + 1):
        if sieve[n]:
            for multiple in range(n * n, limit + 1, n):
                sieve[multiple] = False
    answer = []
    for prime in range(2, limit + 1):
        if sieve[prime]:
            n = prime
            while n <= limit:
                answer.append((n, mp.log(prime)))
                n *= prime
    return sorted(answer)


def completed_prime_source(p, omega, powers):
    answer = mp.mpc(0)
    for shift in [-omega, omega]:
        s = mp.mpf('0.5') + p + shift
        answer += 1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2 + mp.digamma(s / 2) / 2
        answer -= sum(weight * mp.power(n, -s) for n, weight in powers)
    return answer


def tail_bound(sigma, limit):
    return mp.power(limit, 1 - sigma) * (mp.log(limit) / (sigma - 1) + 1 / (sigma - 1) ** 2)


def toy_m(p, roots):
    return sum(1 / (p - root) for root in roots)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    mp.mp.dps = 40
    cases = []

    def check(name, value, threshold=1e-32, comparison='<=', kind='floating'):
        value = float(value)
        passed = mp.isfinite(value) and (value <= threshold if comparison == '<=' else value >= threshold)
        cases.append(dict(name=name, value=value, threshold=threshold, comparison=comparison,
                          kind=kind, passed=bool(passed)))

    # Exact arithmetic counterexample: H(p)=p^2+4 has only imaginary zeros.
    x, omega, gamma = F(1, 4), F(1, 2), F(2)
    real_m = lambda t: 1 / t + t / (t * t + 4 * gamma * gamma)
    toy_a = real_m(x - omega) + real_m(x + omega)
    k_squared = ((x - omega) ** 2 * ((x - omega) ** 2 + 4 * gamma ** 2)
                 / ((x + omega) ** 2 * ((x + omega) ** 2 + 4 * gamma ** 2)))
    for name, result in [
        ('exact_inner_transfer_below_one', 0 < k_squared < 1),
        ('exact_instantaneous_generator_negative', toy_a < 0),
        ('exact_backward_translation_positive_derivative', gamma ** 2 - F(1, 4) ** 2 > 0),
        ('exact_backward_translation_negative_derivative', gamma ** 2 - F(3) ** 2 < 0),
    ]:
        check(name, 0 if result else 1, 0, kind='exact rational')

    for j, p in enumerate([mp.mpc('1.3', '.4'), mp.mpc('2.5', '3'), mp.mpc('6', '.7')]):
        check(f'xi_log_derivative_{j}', abs(mp.diff(H, p) / H(p) - m(p)))
        for omega in [mp.mpf('.1'), mp.mpf('.4')]:
            kval = K(p, omega)
            check(f'exact_shift_equation_{j}_{omega}', abs(mp.diff(lambda v: K(p, v), omega) + a(p, omega) * kval))
            zval = (1 - kval) / (1 + kval)
            dz = mp.diff(lambda v: (1 - K(p, v)) / (1 + K(p, v)), omega)
            check(f'Cayley_Riccati_{j}_{omega}', abs(dz - a(p, omega) * (1 - zval ** 2) / 2))
            eta = mp.mpf('.5')
            reconstructed = m(eta + 1) * (source(cayley(p - omega - eta), eta)
                                         + source(cayley(p + omega - eta), eta))
            check(f'Loewner_source_reconstructs_arithmetic_{j}_{omega}', abs(reconstructed - a(p, omega)))
        check(f'even_H_{j}', abs(H(-p) - H(p)))

    # Recover the full prime-power coefficient with a rigorous analytic tail
    # formula, but floating evaluations of the residual (not interval bounds).
    limit = 1000
    powers = prime_powers(limit)
    prime_samples = []
    for p in [mp.mpc('5.5', '.7'), mp.mpc('6.5', '2')]:
        omega = mp.mpf('.2')
        residual = abs(completed_prime_source(p, omega, powers) - a(p, omega))
        bound = sum(tail_bound(mp.re(p) + mp.mpf('.5') + sign * omega, limit) for sign in [-1, 1])
        check(f'prime_expansion_tail_{p}', residual / bound, 1.0)
        prime_samples.append(dict(p=str(p), omega=str(omega), residual=str(residual), analytic_tail_bound=str(bound)))

    positivity_samples = []
    for eta in [mp.mpf('.5'), mp.mpf('.8')]:
        check(f'radial_source_normalization_{eta}', abs(source(0, eta) - 1))
        values = [mp.re(source(radius * mp.exp(1j * angle), eta))
                  for radius in [mp.mpf('.3'), mp.mpf('.75')]
                  for angle in [mp.mpf('.2'), 1, 2, 3, 4, 5]]
        minimum = min(values)
        check(f'radial_source_positive_samples_{eta}', minimum, 0.0, '>=')
        positivity_samples.append(dict(eta=str(eta), minimum_real_part=str(minimum), sample_count=len(values)))

    # The regularizing shift is a translation of the source, not Loewner
    # time. Its normalized disk transport equation is an exact identity.
    for eta in [mp.mpf('.5'), mp.mpf('.8')]:
        scale = m(eta + 1)
        logarithmic_scale_derivative = mp.diff(m, eta + 1) / scale
        for w in [mp.mpc('.2', '.3'), mp.mpc('-.7', '.1'), mp.mpc('.4', '-.5')]:
            actual = mp.diff(lambda shift: source(w, shift), eta)
            predicted = ((1 - w) ** 2 * mp.diff(lambda v: source(v, eta), w) / 2
                         - logarithmic_scale_derivative * source(w, eta))
            check(f'normalized_source_translation_PDE_{eta}_{w}', abs(actual - predicted))
        p, shift = mp.mpc('1.4', '.6'), mp.mpf('.2')
        reconstructed = (scale / m(eta + shift + 1)
                         * source(cayley(p + shift), eta))
        check(f'normalized_source_translation_composition_{eta}',
              abs(source(cayley(p), eta + shift) - reconstructed))

    # Genuine generalized Loewner semigroup linearized by log H.
    # Use doubles in the time integrator and 25-digit function evaluation.
    flow_samples = []
    with mp.workdps(25):
        eta = mp.mpf('.5')
        scale = m(eta + 1)
        def velocity(p):
            return complex(scale / m(mp.mpc(p) + eta))
        for p in [complex(1.0, .7), complex(2.0, -1.1)]:
            coarse = rk4(velocity, p, .3, 64)
            fine = rk4(velocity, p, .3, 128)
            check(f'Loewner_flow_refinement_{p}', abs(coarse - fine), 2e-10)
            implicit = H(mp.mpc(fine) + eta) / H(mp.mpc(p) + eta)
            expected = mp.exp(scale * mp.mpf('.3'))
            check(f'Koenigs_linearization_{p}', abs(implicit - expected), 2e-11)
            half = rk4(velocity, p, .15, 64)
            composed = rk4(velocity, half, .15, 64)
            check(f'Loewner_semigroup_composition_{p}', abs(composed - fine), 2e-12)
            check(f'Loewner_half_plane_invariance_{p}', fine.real - p.real, 0, '>=')
            flow_samples.append(dict(initial=[p.real, p.imag], final=[fine.real, fine.imag],
                                     xi_ratio=[float(mp.re(implicit)), float(mp.im(implicit))]))

    # Real-zero model: finite positive radial driving measure, all weights explicit.
    gammas = [mp.mpf(2), mp.mpf(3), mp.mpf(5)]
    roots = [sign * 1j * gamma for gamma in gammas for sign in [-1, 1]]
    normalizer = toy_m(mp.mpf(1), roots)
    atoms = [(cayley(root), 1 / (normalizer * (1 + abs(root) ** 2))) for root in roots]
    check('finite_zero_radial_probability_mass', abs(sum(weight for _, weight in atoms) - 1))
    for w in [mp.mpc('.2', '.3'), mp.mpc('-.7', '.1'), mp.mpc('.4', '-.5')]:
        driver_from_atoms = sum(weight * (zeta + w) / (zeta - w) for zeta, weight in atoms)
        check(f'zero_atoms_reproduce_source_{w}', abs(driver_from_atoms - toy_m(uncayley(w), roots) / normalizer))

    # A symmetric off-axis quartet has the same safe shifted positivity but
    # an interior pole when the shift is decreased. It is a control, not xi.
    delta, gamma = mp.mpf('.25'), mp.mpf(2)
    off_roots = [sx * delta + sy * 1j * gamma for sx in [-1, 1] for sy in [-1, 1]]
    safe_values = [mp.re(toy_m(mp.mpf('.5') + uncayley(w), off_roots))
                   for w in [mp.mpc('.2', '.3'), mp.mpc('-.7', '.1'), mp.mpc('.4', '-.5')]]
    check('off_axis_model_safe_shift_positive', min(safe_values), 0.0, '>=')
    bad_eta = mp.mpf('.1')
    pole = cayley(delta - bad_eta + 1j * gamma)
    check('off_axis_model_interior_pole', abs(pole), .999)
    bad_value = mp.re(toy_m(mp.mpc('.1', '2') + bad_eta, off_roots))
    check('off_axis_model_shifted_negative_witness', -bad_value, 10.0, '>=')

    # An inner family need not have positive infinitesimal multiplicative increments.
    toy_p = mp.mpc('.25', '2')
    toy_h = lambda p: p * p + 4
    toy_k = lambda v: toy_h(toy_p - v) / toy_h(toy_p + v)
    toy_generator = toy_m(toy_p - mp.mpf('.5'), [-2j, 2j]) + toy_m(toy_p + mp.mpf('.5'), [-2j, 2j])
    check('inner_model_negative_generator_float', abs(mp.re(toy_generator) - mp.mpf(toy_a.numerator) / toy_a.denominator))
    check('inner_model_increasing_modulus', mp.diff(lambda v: abs(toy_k(v)) ** 2, mp.mpf('.5')), .1, '>=')
    pole_p = mp.mpc('.5', '2')
    check('inner_model_transfer_zero_cancels_log_pole', abs(toy_h(pole_p - mp.mpf('.5'))), 0)

    record = dict(
        schema_version=1, date='2026-09-22', prepared_for='Edward Baker',
        model='GPT-6 (Codex; developer-provided identity)', effort='not exposed; not inferred',
        scope='Exact rational model controls and floating xi/generalized-Loewner identities; not RH evidence or a physical realization',
        environment=dict(python=platform.python_version(), mpmath=mp.__version__),
        parameters=dict(decimal_precision=40, flow_decimal_precision=25, flow_steps=[64, 128],
                        flow_duration=.3, eta_values=[.5, .8], prime_cutoff=limit),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        case_count=len(cases), exact_rational_cases=sum(c['kind'] == 'exact rational' for c in cases),
        all_pass=all(c['passed'] for c in cases), cases=cases,
        prime_samples=prime_samples, source_samples=positivity_samples, flow_samples=flow_samples,
        counterexamples=dict(exact_negative_generator=str(toy_a), exact_transfer_modulus_squared=str(k_squared),
                             off_axis_shifted_real_part=str(bad_value), off_axis_disk_pole_modulus=str(abs(pole))),
    )
    output = json.dumps(record, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
        print(json.dumps(dict(output=str(args.output), case_count=len(cases), all_pass=record['all_pass'],
                              failed=[c for c in cases if not c['passed']])))
    else:
        print(output, end='')
    raise SystemExit(0 if record['all_pass'] else 1)


if __name__ == '__main__':
    main()
