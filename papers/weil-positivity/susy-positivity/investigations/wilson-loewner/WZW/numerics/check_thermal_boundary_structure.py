#!/usr/bin/env python3
"""Native Kubo load, conservative boundary connection and front rigidity.

Prepared for Edward Baker with GPT-6 (Codex) assistance, 2026-09-23.
Effort not exposed; not inferred. Floating controls, not interval certificates.
Requires only Python 3 and mpmath. No sibling imports or external data.
"""
import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60
CASES, SAMPLES = [], {}
BETAS = tuple(map(mp.mpf, ('.5', '.8', '1')))
PRIMES = (2, 3)
SHELL_CUTOFF = 400


def check(name, value, threshold='1e-45', comparison='<='):
    value, threshold = mp.mpf(value), mp.mpf(threshold)
    passed = bool(mp.isfinite(value) and mp.isfinite(threshold)
                  and (value <= threshold if comparison == '<=' else value >= threshold))
    CASES.append(dict(name=name, value=mp.nstr(value, 30),
                      threshold=mp.nstr(threshold, 30), comparison=comparison,
                      passed=passed, arithmetic='floating'))


def num(x):
    return mp.nstr(x, 24)


def xi(s):
    s = mp.mpc(s)
    if s == 0 or s == 1:
        return mp.mpf('.5')
    if s.real < mp.mpf('.5'):
        return xi(1-s)
    return s*(s-1)/2*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)


def half(p):
    if mp.re(p) > 2:
        return (mp.sqrt(mp.pi)*mp.exp(mp.loggamma(p/2)-mp.loggamma((p+1)/2))
                * (p-1)/(p+1)*mp.zeta(p)/mp.zeta(p+1))
    return xi(p)/xi(p+1)


def target(p, beta):
    return xi(p+(1-beta)/2)/xi(p+(1+beta)/2)


def a_half(p):
    return mp.diff(xi, p)/xi(p)+mp.diff(xi, p+1)/xi(p+1)


def spectral_weights(beta):
    return [(mp.log(l), 2*mp.log(l)*(1-mp.power(l, -beta))) for l in PRIMES]


def admittance(p, beta):
    return mp.fsum(w*p/(p*p+e*e) for e, w in spectral_weights(beta))


def load_mass(beta):
    return mp.fsum(w for _, w in spectral_weights(beta))


def coupled(p, beta, strength=1, port=0):
    r = mp.exp(-port*p)*half(p)
    j = strength*admittance(p, beta)/2
    return (r+j*(1-r))/(1+j*(1-r))


def anchored_tangent(p, port=0):
    r = mp.exp(-port*p)*half(p)
    return -admittance(p, mp.mpf(1))*(1-r)**2/(2*r)


def pulse_state(t, e, w):
    """Oscillator driven by effort U(t)=exp(-t), with zero coherent state."""
    c = mp.sqrt(w)/(1+e*e)
    x = c*(mp.exp(-t)-mp.cos(e*t)+mp.sin(e*t)/e)
    v = c*(-mp.exp(-t)+e*mp.sin(e*t)+mp.cos(e*t))
    return x, v


def run():
    for beta in BETAS:
        for l in PRIMES:
            q, e = mp.power(l, -beta), mp.log(l)
            probs = [(1-q)*q**m for m in range(SHELL_CUTOFF+1)]
            for j, t in enumerate(map(mp.mpf, ('.2', '1.1', '3'))):
                # Infinite ladder matrix elements evaluated on finitely many
                # occupied states: no artificial top-of-ladder commutator.
                corr = mp.fsum(w*(mp.exp(-1j*e*t)
                                  + (mp.exp(1j*e*t) if m else 0))
                               for m, w in enumerate(probs))
                exact = mp.exp(-1j*e*t)+q*mp.exp(1j*e*t)
                check(f'native_correlation_b{beta}_l{l}_t{j}', abs(corr-exact),
                      2*q**(SHELL_CUTOFF+1)+mp.mpf('1e-58'))
                response = 1j*(corr-mp.conj(corr))
                check(f'native_commutator_b{beta}_l{l}_t{j}',
                      abs(response-2*(1-q)*mp.sin(e*t)))
            # Bosonic ladder control: commutator response is temperature independent.
            up = mp.fsum(w*(m+1) for m, w in enumerate(probs))
            down = mp.fsum(w*m for m, w in enumerate(probs))
            check(f'bosonic_commutator_b{beta}_l{l}', abs(up-down-1))
            # Spectral sum over actual adjacent-state transitions telescopes.
            moment = mp.fsum(2*e*((1-q)*q**m-(1-q)*q**(m+1))
                            for m in range(SHELL_CUTOFF+1))
            check(f'commutator_sum_rule_b{beta}_l{l}', abs(moment-2*e*(1-q)))
            # Direct Laplace transform of the retarded time response.
            p = mp.mpc('1.2', '.4')
            integrated = mp.quad(lambda t: mp.exp(-p*t)*2*(1-q)*mp.sin(e*t),
                                 [0, 1, 3, 10, mp.inf])
            check(f'Kubo_Laplace_b{beta}_l{l}', abs(integrated-2*e*(1-q)/(p*p+e*e)))
            check(f'noise_detailed_balance_b{beta}_l{l}',
                  abs((1+q)/(1-q)-mp.coth(beta*e/2)))

        # Actual oscillator work and storage, independently integrated.
        for L in map(mp.mpf, ('.7', '2', '5')):
            weights = spectral_weights(beta)
            def current(t):
                return mp.fsum(mp.sqrt(w)*pulse_state(t, e, w)[1] for e, w in weights)
            supplied = mp.quad(lambda t: mp.exp(-t)*current(t), [0, L])
            stored = mp.fsum((pulse_state(L, e, w)[1]**2
                             + e*e*pulse_state(L, e, w)[0]**2)/2 for e, w in weights)
            check(f'oscillator_work_storage_b{beta}_L{L}', abs(supplied-stored))

        # Full global modular response remains inside the actual connection.
        for strength in map(mp.mpf, ('.25', '1')):
            for j, p in enumerate((mp.mpc('.4', '.3'), mp.mpc(1, 2),
                                   mp.mpc(4), mp.mpc(8, 3))):
                r, y = half(p), strength*admittance(p, beta)
                # Unknowns are core input a and external measured output g:
                # 1 = a + I_load/2, g = r*a + I_load/2.
                mat = mp.matrix([[1+y*(1-r)/2, 0],
                                 [-r-y*(1-r)/2, 1]])
                a, g = mp.lu_solve(mat, mp.matrix([1, 0]))
                expected = coupled(p, beta, strength)
                check(f'boundary_equations_b{beta}_c{strength}_p{j}', abs(g-expected))
                N, D = r+y*(1-r)/2, 1+y*(1-r)/2
                flux = 1-abs(r)**2+mp.re(y)*abs(1-r)**2
                check(f'global_flux_identity_b{beta}_c{strength}_p{j}',
                      abs(abs(D)**2-abs(N)**2-flux))
                check(f'global_contractivity_b{beta}_c{strength}_p{j}',
                      1-abs(expected)**2, 0, '>=')
            for t in map(mp.mpf, ('.4', '2', '6')):
                check(f'boundary_unit_modulus_b{beta}_c{strength}_t{t}',
                      abs(abs(coupled(1j*t, beta, strength))**2-1))

        C = load_mass(beta)
        for p in map(mp.mpf, (16, 64, 256)):
            moment3 = mp.fsum(w*e*e for e, w in spectral_weights(beta))
            defect = C-p*admittance(p, beta)
            check(f'spectral_mass_bound_b{beta}_p{p}', mp.re(defect), 0, '>=')
            check(f'spectral_mass_error_b{beta}_p{p}', abs(defect),
                  moment3/(p*p)+mp.mpf('1e-55'))
        p = mp.mpf(1000000)
        R, K = coupled(p, beta), half(p)
        check(f'front_correction_asymptotic_b{beta}',
              abs(2*p*(R-K)/C-1), '.006')
        check(f'front_power_preserved_b{beta}',
              abs(mp.sqrt(p/(2*mp.pi))*R-1), '.001')
        # A nonzero-frequency load is O(p) at zero, so its correction is O(p^3).
        check(f'zero_frequency_slope_preserved_b{beta}',
              abs(mp.diff(lambda z: coupled(z, beta), 0)-mp.diff(half, 0)))

    rows = []
    for p in map(mp.mpf, (4, 16, 64, 256, 1024)):
        native = anchored_tangent(p)
        required = -a_half(p)/2
        derived = mp.diff(lambda b: mp.log(coupled(p, b, 1-b)), mp.mpf(1))
        check(f'anchored_thermal_tangent_p{p}', abs(derived-native))
        check(f'full_target_tangent_p{p}',
              abs(mp.diff(lambda b: mp.log(target(p, b)), mp.mpf(1))-required))
        rows.append(dict(p=str(p), native=num(mp.re(native)), target=num(mp.re(required)),
                         required_admittance_per_heating=num(mp.re(a_half(p)*half(p)/(1-half(p))**2))))
    p = mp.mpf(1000000)
    limit = -load_mass(mp.mpf(1))/(2*mp.sqrt(2*mp.pi))
    check('native_tangent_decays_as_inverse_sqrt_p',
          abs(mp.sqrt(p)*anchored_tangent(p)/limit-1), '.006')
    check('target_logarithmic_tangent',
          abs((-a_half(p)/2)/(-mp.log(p/(2*mp.pi))/2)-1), '.000001')

    # Positive-port prompt response: p*S tends to half the load mass,
    # while the global core is exponentially delayed.
    beta, b, strength = mp.mpf('.5'), mp.mpf(1), mp.mpf('.5')
    p = mp.mpf(10000)
    check('positive_port_prompt_front',
          abs(2*p*coupled(p, beta, strength, b)/(strength*load_mass(beta))-1), '.0001')

    # Temperature alone cannot anchor an active added load to the bare core.
    p = mp.mpf(16)
    check('fixed_coupling_anchor_mismatch',
          abs(coupled(p, mp.mpf(1))-half(p)), '.01', '>=')
    check('smooth_microscopic_switch_has_zero_tangent',
          abs(mp.diff(lambda beta: coupled(p, beta, (1-beta)**2), mp.mpf(1))))
    # Bounded switching returns to the original core as beta decreases to zero.
    tiny = mp.mpf('1e-8')
    check('hot_limit_returns_to_half_shift',
          abs(coupled(p, tiny, 1-tiny)-half(p)), '1e-8')
    check('hot_limit_is_not_identity',
          abs(coupled(p, tiny, 1-tiny)-1), '.4', '>=')

    SAMPLES.update(tangent_comparison=rows, mass_at_beta1=num(load_mass(mp.mpf(1))),
                   native_tangent_scaled_limit=num(limit),
                   low_frequency_core_slope=num(mp.re(mp.diff(half, 0))),
                   low_frequency_target_slope_beta_derivative=num(mp.re(
                       -mp.diff(lambda s: mp.diff(xi, s)/xi(s), mp.mpf(1)))))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    run()
    assert len({c['name'] for c in CASES}) == len(CASES)
    record = dict(schema_version=1, date='2026-09-23', prepared_for='Edward Baker',
                  model='GPT-6 (Codex; developer-provided identity)',
                  effort='not exposed; not inferred', python=platform.python_version(),
                  mpmath=mp.__version__, program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  parameters=dict(decimal_digits=mp.mp.dps, primes=list(PRIMES),
                                  inverse_temperatures=[str(b) for b in BETAS],
                                  shell_cutoff=SHELL_CUTOFF, couplings_squared=[1, 1],
                                  front_test_p='1000000',
                                  calibrated_strength='1-beta; one-sided at beta=1'),
                  scope='Exact native Kubo response, conservative effective linear boundary load, '
                        'finite-spectral-mass front rigidity and target-tangent failure. '
                        'Not an exact finite-coupling microscopic quantum scattering model, '
                        'a general bulk-coupling obstruction, an interval certificate or an RH result.',
                  case_count=len(CASES), all_pass=all(c['passed'] for c in CASES),
                  cases=CASES, samples=SAMPLES)
    payload = json.dumps(record, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
        print(json.dumps(dict(case_count=len(CASES), all_pass=record['all_pass'])))
        for c in CASES:
            if not c['passed']:
                print(json.dumps(c))
    else:
        print(payload, end='')
    raise SystemExit(not record['all_pass'])


if __name__ == '__main__':
    main()
