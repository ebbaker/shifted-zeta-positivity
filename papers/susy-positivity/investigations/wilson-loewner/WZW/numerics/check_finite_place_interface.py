#!/usr/bin/env python3
"""Two-prime thermal delay coupling and the finite-Euler completion obstruction.

Prepared for Edward Baker with GPT-6 (Codex) assistance, 2026-09-23.
Effort setting not exposed; not inferred. Floating diagnostics, not certificates.
Only Python 3 and mpmath are required. No sibling imports or external data.
"""
import argparse
import hashlib
import itertools
import json
import platform
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60
CASES, SAMPLES = [], {}
PRIMES = (2, 3)
BETAS = tuple(map(mp.mpf, ('.5', '.8', '1')))
SHELL_CUTOFF = 360
EPS = mp.mpf('.05')


def check(name, value, threshold='1e-48', comparison='<='):
    value, threshold = mp.mpf(value), mp.mpf(threshold)
    passed = bool(mp.isfinite(value) and mp.isfinite(threshold)
                  and (value <= threshold if comparison == '<=' else value >= threshold))
    CASES.append(dict(name=name, value=mp.nstr(value, 30),
                      threshold=mp.nstr(threshold, 30), comparison=comparison,
                      passed=passed, arithmetic='floating'))


def textnum(x):
    return mp.nstr(x, 24)


def loop(l, p):
    r, z = mp.mpf(1)/l, mp.exp(-p*mp.log(l))
    return (z-r)/(1-r*z)


def readout(l, beta, p):
    q = mp.power(l, -beta)
    return q+(1-q)*loop(l, p)


def primitive(n, beta):
    return mp.fprod(1-mp.power(l, -beta) for l in PRIMES if n % l == 0)


def target(n, beta):
    return mp.power(n, (beta-1)/2)*primitive(n, beta)


def delay(k):
    return k[0]*mp.log(2)+k[1]*mp.log(3)


def add(train, key, value):
    train[key] = train.get(key, mp.mpf(0))+value


def stage(incoming, l, enabled, horizon):
    """Solve y=-r f+t v, u=t f+r v, v(t)=u(t-log(l)).

    Sparse trains represent a unit box pulse translated by the actual paths.
    Return outgoing y and loop launch u. No target coefficients enter.
    """
    if not enabled:
        return dict(incoming), {}
    r = mp.mpf(1)/l
    trans = mp.sqrt(1-r*r)
    axis = PRIMES.index(l)
    launch, outgoing = {}, {}
    for key, value in incoming.items():
        add(outgoing, key, -r*value)
        k = 0
        while True:
            shifted = list(key)
            shifted[axis] += k
            shifted = tuple(shifted)
            if delay(shifted) >= horizon:
                break
            add(launch, shifted, trans*r**k*value)
            echo = list(shifted)
            echo[axis] += 1
            echo = tuple(echo)
            if delay(echo) < horizon:
                add(outgoing, echo, trans*trans*r**k*value)
            k += 1
    return outgoing, launch


def pulse_energy(train, start, end):
    """Exact interval-overlap formula evaluated in multiprecision arithmetic.

    Includes interference even when two translated boxes overlap. No time grid.
    """
    total = mp.mpf(0)
    for k, a in train.items():
        left = delay(k)
        for j, b in train.items():
            right = delay(j)
            overlap = max(mp.mpf(0), min(end, left+EPS, right+EPS)
                          - max(start, left, right))
            total += a*mp.conj(b)*overlap/EPS
    return mp.re(total)


def thermal_train(beta, horizon):
    mean, sectors = {}, []
    for enabled in itertools.product((False, True), repeat=2):
        weight = mp.fprod(1-mp.power(l, -beta) if gate else mp.power(l, -beta)
                          for l, gate in zip(PRIMES, enabled))
        y2, u2 = stage({(0, 0): mp.mpf(1)}, 2, enabled[0], horizon)
        out, u3 = stage(y2, 3, enabled[1], horizon)
        for key, value in out.items():
            add(mean, key, weight*value)
        storage = (pulse_energy(u2, horizon-mp.log(2), horizon)
                   + pulse_energy(u3, horizon-mp.log(3), horizon))
        sectors.append((enabled, weight, out, storage))
    return mean, sectors


def arch(p, beta):
    sm, sp = p+(1-beta)/2, p+(1+beta)/2
    return (mp.pi**(beta/2)*mp.gamma(sm/2)/mp.gamma(sp/2)
            * sm*(sm-1)/(sp*(sp-1)))


def finite_euler(p, beta, primes=PRIMES):
    return mp.fprod((1-mp.power(l, -p-(1+beta)/2))
                    /(1-mp.power(l, -p-(1-beta)/2)) for l in primes)


def xi(s):
    if s == 0 or s == 1:
        return mp.mpf('.5')
    return s*(s-1)/2*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)


def residue(beta, primes=PRIMES):
    return (-beta*(1-beta)*mp.pi**((beta-1)/2)*mp.gamma((1-beta)/2)
            * mp.fprod((1-mp.mpf(1)/l)/(1-mp.power(l, beta-1)) for l in primes))


def run():
    # Solve the actual loop boundary equations, independently of the closed form.
    for l in PRIMES:
        r, trans = mp.mpf(1)/l, mp.sqrt(1-mp.mpf(1)/l**2)
        U = mp.matrix([[-r, trans], [trans, r]])
        check(f'vertex_unitarity_{l}', mp.norm(U.T*U-mp.eye(2)))
        for j, p in enumerate((mp.mpf('.2'), mp.mpc(1, '.7'), mp.mpc(3, 2))):
            z = mp.exp(-p*mp.log(l))
            sol = mp.lu_solve(mp.matrix([[1, -trans*z], [0, 1-r*z]]),
                              mp.matrix([-r, trans]))
            check(f'boundary_solve_{l}_{j}', abs(sol[0]-loop(l, p)))
        for j, t in enumerate((mp.mpf(0), mp.mpf('.7'), mp.mpf(3))):
            check(f'loop_boundary_modulus_{l}_{j}', abs(abs(loop(l, 1j*t))**2-1))

    echo_rows, energy_rows = [], []
    for beta in BETAS:
        tag = str(beta)
        # Direct truncated native Gibbs trace; the omitted mass is bounded.
        for l in PRIMES:
            q, p = mp.power(l, -beta), mp.mpc('.3', '.7')
            native = mp.fsum((1-q)*q**m*(loop(l, p) if m == 0 else 1)
                             for m in range(SHELL_CUTOFF+1))
            check(f'native_Gibbs_trace_{tag}_{l}', abs(native-readout(l, beta, p)),
                  q**(SHELL_CUTOFF+1)+mp.mpf('1e-58'))

        # Four thermal sectors: joint scattering, coherent mean, and variance.
        for j, t in enumerate((mp.mpf(0), mp.mpf('.7'), mp.mpf(3))):
            sector = []
            for gates in itertools.product((False, True), repeat=2):
                weight = mp.fprod(1-mp.power(l, -beta) if g else mp.power(l, -beta)
                                  for l, g in zip(PRIMES, gates))
                amplitude = mp.fprod(loop(l, 1j*t) if g else 1
                                     for l, g in zip(PRIMES, gates))
                sector.append((weight, amplitude))
            mean = mp.fsum(w*a for w, a in sector)
            product = mp.fprod(readout(l, beta, 1j*t) for l in PRIMES)
            variance = mp.fsum(w*abs(a-mean)**2 for w, a in sector)
            check(f'coherent_cascade_{tag}_{j}', abs(mean-product))
            check(f'frequency_flux_variance_{tag}_{j}', abs(abs(mean)**2+variance-1))

        train, _ = thermal_train(beta, mp.mpf('2.05'))
        q2, q3 = mp.power(2, -beta), mp.power(3, -beta)
        d2, d3 = q2-(1-q2)/2, q3-(1-q3)/3
        b2, b3 = (1-q2)*mp.mpf(3)/4, (1-q3)*mp.mpf(8)/9
        wanted = {(0, 0): d2*d3, (1, 0): b2*d3, (0, 1): d2*b3,
                  (2, 0): b2*d3/2, (1, 1): b2*b3}
        for key, value in wanted.items():
            check(f'path_echo_{tag}_{2**key[0]*3**key[1]}', abs(train[key]-value))
        check(f'multiplicativity_with_front_{tag}',
              abs(train[(1, 1)]*train[(0, 0)]-train[(1, 0)]*train[(0, 1)]))
        check(f'repetition_ratio_mismatch_{tag}',
              abs(train[(2, 0)]/train[(1, 0)]-mp.power(2, (beta-1)/2)), '.3', '>=')
        check(f'nonzero_direct_front_{tag}',
              abs(mp.fprod(readout(l, beta, mp.mpf(180)) for l in PRIMES)-d2*d3))
        echo_rows.append(dict(beta=tag, direct=textnum(train[(0, 0)]),
                              native={str(n): textnum(train[k]) for n, k in
                                      ((2, (1, 0)), (3, (0, 1)), (4, (2, 0)), (6, (1, 1)))},
                              normalized={str(n): textnum(train[k]/train[(0, 0)]) for n, k in
                                          ((2, (1, 0)), (3, (0, 1)), (4, (2, 0)), (6, (1, 1)))},
                              target={str(n): textnum(target(n, beta)) for n in (2, 3, 4, 6)}))

        # Actual finite-time radiation flux and energy stored in both loops.
        for L in map(mp.mpf, ('.4', '.9', '1.8', '2.05', '3.7')):
            mean, sectors = thermal_train(beta, L)
            inclusive, storage = mp.mpf(0), mp.mpf(0)
            for gates, weight, out, stored in sectors:
                energy = pulse_energy(out, 0, L)
                # Individual sectors are independent of temperature; check once.
                if beta == BETAS[0]:
                    check(f'sector_pulse_flux_{gates}_{L}', abs(energy+stored-1))
                inclusive += weight*energy
                storage += weight*stored
            coherent = pulse_energy(mean, 0, L)
            # Directly integrate the sector deviations, not inclusive-minus-mean.
            variance = mp.mpf(0)
            for _, weight, out, _ in sectors:
                deviation = dict(out)
                for key, value in mean.items():
                    add(deviation, key, -value)
                variance += weight*pulse_energy(deviation, 0, L)
            check(f'averaged_pulse_flux_{tag}_{L}', abs(coherent+variance+storage-1))
            check(f'inclusive_decomposition_{tag}_{L}', abs(inclusive-coherent-variance))
            if L == mp.mpf('2.05'):
                energy_rows.append(dict(beta=tag, horizon=str(L), coherent=textnum(coherent),
                                        incoherent=textnum(variance), stored=textnum(storage)))

    def echo2(omega):
        beta = 2*omega
        return (1-mp.power(2, -beta))*mp.mpf(3)/4*(mp.power(3, -beta)*mp.mpf(4)/3-mp.mpf(1)/3)
    native_tangent = mp.diff(echo2, mp.mpf('.5'))
    target_tangent = mp.diff(lambda w: target(2, 2*w), mp.mpf('.5'))
    check('native_first_echo_tangent', abs(native_tangent-(mp.log(2)/12-mp.log(3)/3)))
    check('target_first_echo_tangent', abs(target_tangent-mp.mpf('1.5')*mp.log(2)))
    check('first_echo_tangent_mismatch', abs(native_tangent-target_tangent), '1.3', '>=')
    def normalized_echo2(omega):
        q = mp.power(2, -2*omega)
        return (1-q)*mp.mpf(3)/4/(mp.mpf('1.5')*q-mp.mpf('.5'))
    normalized_tangent = mp.diff(normalized_echo2, mp.mpf('.5'))
    check('normalized_first_echo_tangent', abs(normalized_tangent-12*mp.log(2)))
    check('normalized_first_echo_tangent_mismatch', abs(normalized_tangent-target_tangent), '7', '>=')
    SAMPLES['tangents_at_half_shift'] = dict(native=textnum(native_tangent),
                                            normalized=textnum(normalized_tangent),
                                            target=textnum(target_tangent))

    # Pole residues from symmetric sampling, then comparison with the full xi ratio.
    pole_rows = []
    for beta in map(mp.mpf, ('.25', '.5', '.8', '.95')):
        d, eps = (1-beta)/2, mp.mpf('1e-12')
        product = lambda p: arch(p, beta)*finite_euler(p, beta)
        sampled = eps*(product(d+eps)-product(d-eps))/2
        exact = residue(beta)
        check(f'finite_product_residue_{beta}', abs(sampled/exact-1), '1e-19')
        check(f'finite_product_gain_near_pole_{beta}', abs(product(d+mp.mpf('.0001'))), '100', '>=')
        for primes in ((2,), (2, 3, 5)):
            sampled_other = eps*(arch(d+eps, beta)*finite_euler(d+eps, beta, primes)
                                 -arch(d-eps, beta)*finite_euler(d-eps, beta, primes))/2
            check(f'other_finite_sets_residue_{beta}_{primes}',
                  abs(sampled_other/residue(beta, primes)-1), '1e-19')
        p = d+mp.mpf('1e-20')
        sm, sp = p+(1-beta)/2, p+(1+beta)/2
        completed = arch(p, beta)*mp.zeta(sm)/mp.zeta(sp)
        check(f'full_xi_factorization_near_cancellation_{beta}', abs(completed-xi(sm)/xi(sp)))
        check(f'full_xi_finite_pole_value_{beta}', abs(completed-2*xi(1-beta)), '1e-19')
        pole_rows.append(dict(beta=str(beta), pole=textnum(d), residue=textnum(exact),
                              full_xi_value=textnum(2*xi(1-beta))))
    eps = mp.mpf('1e-15')
    endpoint_coefficient = -mp.mpf(2)/(3*mp.log(2)*mp.log(3))
    check('half_shift_cubic_boundary_pole',
          abs(eps**3*arch(eps, mp.mpf(1))*finite_euler(eps, mp.mpf(1))/endpoint_coefficient-1), '1e-12')

    # Fixed-state readout lemma is analytic. These samples only illustrate growth.
    check('centered_c2_exceeds_one_at_beta4', target(2, mp.mpf(4)), '2.6', '>=')
    # Norm convergence to identity follows from ||F_l-I|| <= 2.
    beta = mp.mpf('.001')
    bound = 2*mp.fsum(1-mp.power(l, -beta) for l in PRIMES)
    check('small_beta_identity_bound', bound, '.004')
    SAMPLES.update(echo_coefficients=echo_rows, pulse_energy=energy_rows,
                   poles=pole_rows, endpoint_cubic_coefficient=textnum(endpoint_coefficient),
                   small_beta_operator_identity_bound=textnum(bound))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    run()
    assert len({case['name'] for case in CASES}) == len(CASES)
    record = dict(schema_version=1, date='2026-09-23', prepared_for='Edward Baker',
                  model='GPT-6 (Codex; developer-provided identity)',
                  effort='not exposed; not inferred', python=platform.python_version(),
                  mpmath=mp.__version__, program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  parameters=dict(decimal_digits=mp.mp.dps, primes=list(PRIMES),
                                  betas=[str(x) for x in BETAS], vertex_reflection='1/prime',
                                  shell_cutoff=SHELL_CUTOFF, pulse_width=str(EPS),
                                  horizons=['0.4', '0.9', '1.8', '2.05', '3.7']),
                  scope='Native unitary thermal delay model, ordinary finite-time flux, '
                        'arithmetic mismatches and finite-Euler completion pole. '
                        'No successful completed realization, interval proof, or RH result.',
                  case_count=len(CASES), all_pass=all(c['passed'] for c in CASES),
                  cases=CASES, samples=SAMPLES)
    payload = json.dumps(record, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
        print(json.dumps(dict(case_count=len(CASES), all_pass=record['all_pass'])))
        for case in CASES:
            if not case['passed']:
                print(json.dumps(case))
    else:
        print(payload, end='')
    raise SystemExit(not record['all_pass'])


if __name__ == '__main__':
    main()
