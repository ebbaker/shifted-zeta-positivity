#!/usr/bin/env python3
"""Exploratory CCM Fourier matrices and the boundary-gauge mechanical realization.

Source definitions: CCM, arXiv:2511.22755v1, (3.13)--(3.18), (5.1)--(5.3).
Uses mpmath quadrature/eigensolvers; results are NOT interval certificates.
No zeta zeros enter the construction. They are used only for a diagnostic.
"""
import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp


def prime_powers(limit):
    out = []
    for p in range(2, limit + 1):
        if any(p % d == 0 for d in range(2, int(p**0.5) + 1)):
            continue
        value = p
        while value <= limit:
            out.append((value, p))
            value *= p
    return sorted(out)


def weil_matrix(limit, nmax):
    length = mp.log(limit)
    terms = [(mp.log(n), mp.log(p) / mp.sqrt(n))
             for n, p in prime_powers(limit)]
    intervals = [length * j / 4 for j in range(5)]

    def distribution(fun, at_zero, derivative_zero, delta=None):
        """Push-forward of Psi-sharp, with the archimedean tail retained."""
        pole = mp.quad(lambda x: 2 * mp.cosh(x / 2) * fun(x), intervals)

        def regular(x):
            if x == 0:
                return (derivative_zero + at_zero / 2) / 2
            difference = delta(x) if delta is not None else fun(x) - at_zero
            numerator = mp.exp(x / 2) * difference + at_zero * mp.expm1(x / 2)
            return numerator / (2 * mp.sinh(x))

        arch = at_zero / 2 * (mp.log(4 * mp.pi) + mp.euler
                             + mp.log(mp.tanh(length / 2)))
        arch += mp.quad(regular, intervals)
        arithmetic = mp.fsum(weight * fun(delay) for delay, weight in terms)
        return pole - arch - arithmetic

    diagonal, divided = {}, {0: mp.mpf(0)}
    for n in range(nmax + 1):
        freq = 2 * mp.pi * n / length
        fun = lambda x: 2 * (1 - x / length) * mp.cos(freq * x)
        delta = lambda x: -4 * mp.sin(freq * x / 2)**2 - 2 * x / length * mp.cos(freq * x)
        diagonal[n] = distribution(fun, mp.mpf(2), -2 / length, delta)
        if n:
            divided[n] = -distribution(lambda x: mp.sin(freq * x), mp.mpf(0), freq) / mp.pi
            divided[-n] = -divided[n]
        diagonal[-n] = diagonal[n]
    indices = list(range(-nmax, nmax + 1))
    matrix = mp.matrix([[diagonal[i] if i == j else
                         (divided[i] - divided[j]) / (i - j)
                         for j in indices] for i in indices])

    # Selected off-diagonal entries reconstructed directly from the correlation
    # formula, independently of the divided-difference assembly above.
    entry_errors = []
    for i, j in [(-nmax, 0), (-1, 1), (1, min(2, nmax))]:
        if i == j:
            continue
        di, dj = 2 * mp.pi * i / length, 2 * mp.pi * j / length
        q = lambda x: (mp.sin(dj * x) - mp.sin(di * x)) / (mp.pi * (i - j))
        direct = distribution(q, mp.mpf(0), -2 / length)
        entry_errors.append(abs(direct - matrix[i + nmax, j + nmax]))
    return matrix, max(entry_errors, default=mp.mpf(0))


def trace(a):
    return mp.fsum(a[i, i] for i in range(a.rows))


def scaled_error(a, b):
    return mp.norm(a - b) / max(mp.mpf(1), mp.norm(a), mp.norm(b))


def xi(z):
    s = mp.mpf('0.5') + 1j * z
    return s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s) / 2


def analyze(limit, n, digits, full=None, full_n=None, entry_error=None):
    mp.mp.dps = digits
    length = mp.log(limit)
    if full is None:
        full, entry_error = weil_matrix(limit, n)
        full_n = n
    start = full_n - n
    w = full[start:start + 2 * n + 1, start:start + 2 * n + 1]
    even = mp.zeros(2 * n + 1, n + 1)
    odd = mp.zeros(2 * n + 1, n)
    even[n, 0] = 1
    for j in range(1, n + 1):
        even[n + j, j] = even[n - j, j] = 1 / mp.sqrt(2)
        odd[n + j, j - 1] = 1 / mp.sqrt(2)
        odd[n - j, j - 1] = -1 / mp.sqrt(2)
    wp, wm = even.T * w * even, odd.T * w * odd
    ep, vp = mp.eigsy(wp)
    em = mp.eigsy(wm, eigvals_only=True)
    epsilon = ep[0]
    if min(ep[1] - epsilon, em[0] - epsilon) <= 0:
        raise ArithmeticError('The required simple-even ground state was not observed.')
    tp, stiffness = wp - epsilon * mp.eye(n + 1), wm - epsilon * mp.eye(n)
    boundary = mp.matrix([[1 / mp.sqrt(length)] + [mp.sqrt(2 / length)] * n])
    ground = vp[:, 0]
    ground /= (boundary * ground)[0]
    r = mp.zeros(n, n + 1)
    integration = mp.zeros(n + 1, n)
    frequencies = [2 * mp.pi * j / length for j in range(1, n + 1)]
    for j, freq in enumerate(frequencies):
        r[j, j + 1] = freq
        integration[0, j] = -mp.sqrt(2) / freq
        integration[j + 1, j] = 1 / freq
    mass = integration.T * tp * integration
    mass_eigen = mp.eigsy((mass + mass.T) / 2, eigvals_only=True)
    if mass_eigen[0] <= 0:
        raise ArithmeticError('The derived mass matrix is not numerically positive.')
    chol = mp.cholesky(mass)
    inv_chol = chol**-1
    normal = inv_chol * stiffness * inv_chol.T
    normal_symmetry = scaled_error(normal, normal.T)
    normal = (normal + normal.T) / 2
    squared = mp.eigsy(normal, eigvals_only=True)
    if squared[0] <= 0:
        raise ArithmeticError('Nonpositive squared frequency.')
    omega = [mp.sqrt(v) for v in squared]

    ground_full = even * ground
    d = mp.diag([2 * mp.pi * j / length for j in range(-n, n + 1)])
    ell = mp.matrix([[1 / mp.sqrt(length)] * (2 * n + 1)])
    a = d - (d * ground_full) * ell
    pencil_residual = scaled_error(r * tp * r.T,
                                   stiffness * mass**-1 * stiffness)
    weighted_residual = scaled_error(a.T * (w - epsilon * mp.eye(2*n+1)),
                                     (w - epsilon * mp.eye(2*n+1)) * a)
    moment_matrix = stiffness**-1 * mass
    moments = []
    target_moments = []
    xi0 = xi(0)
    for k in (1, 2, 3):
        tail = (length / (2 * mp.pi))**(2*k) * (mp.zeta(2*k) - mp.fsum(mp.mpf(j)**(-2*k) for j in range(1,n+1)))
        moments.append(trace(moment_matrix**k) + tail)
        target_moments.append(mp.re(-k * mp.diff(lambda z: mp.log(xi(z) / xi0), 0, 2*k) / mp.factorial(2*k)))

    determinant_errors, transform_errors = [], []
    for z in [mp.mpc('0.7','0.3'), mp.mpc('12','1.7'), mp.mpc('17','0.2')]:
        quotient = mp.det(a - z * mp.eye(2*n+1)) / (-z)
        pencil = mp.det(z*z * mass - stiffness) / mp.det(mass)
        determinant_errors.append(abs(quotient-pencil) / max(1,abs(quotient),abs(pencil)))
        normalized = mp.sin(length*z/2)/(length*z/2)
        normalized *= mp.det(stiffness-z*z*mass) / mp.det(stiffness)
        normalized /= mp.fprod(1-z*z/freq**2 for freq in frequencies)
        transform = 2 / mp.sqrt(length) * mp.sin(length*z/2) * mp.fsum(
            ground_full[j+n]/(z-2*mp.pi*j/length) for j in range(-n,n+1))
        transform /= mp.sqrt(length) * ground_full[n]
        transform_errors.append(abs(normalized-transform)/max(1,abs(normalized),abs(transform)))

    record = {
        'prime_power_cutoff': limit, 'N': n, 'decimal_digits': digits,
        'least_eigenvalue': epsilon,
        'even_gap': ep[1]-epsilon, 'odd_gap': em[0]-epsilon,
        'mass_min_eigenvalue': mass_eigen[0],
        'normalized_ground_mean': mp.sqrt(length)*ground_full[n],
        'first_frequencies': omega[:min(3,n)],
        'first_frequency_errors_against_zeta': [omega[j]-mp.im(mp.zetazero(j+1)) for j in range(min(3,n))],
        'inverse_square_moments_including_free_tail': moments,
        'xi_target_moments': target_moments,
        'moment_errors': [a-b for a,b in zip(moments,target_moments)],
        'free_tail_inverse_square_sum': (length/(2*mp.pi))**2 * (mp.zeta(2)-mp.fsum(mp.mpf(j)**-2 for j in range(1,n+1))),
        'checks': {
            'selected_direct_entry_error': entry_error,
            'boundary_integration': mp.norm(boundary*integration),
            'derivative_integration': mp.norm(r*integration-mp.eye(n)),
            'mass_stiffness_identity': pencil_residual,
            'weighted_selfadjointness': weighted_residual,
            'normal_matrix_symmetry': normal_symmetry,
            'quotient_characteristic_determinant': max(determinant_errors),
            'normalized_fourier_determinant': max(transform_errors)
        }
    }
    tolerance = mp.mpf(10)**(-min(30,digits//2))
    if max(record['checks'].values()) > tolerance:
        raise ArithmeticError('An algebraic reconstruction check failed: '+str(record['checks']))
    return record


def strings(value):
    if isinstance(value, dict):
        return {k:strings(v) for k,v in value.items()}
    if isinstance(value, list):
        return [strings(v) for v in value]
    if isinstance(value, (int,str,bool)) or value is None:
        return value
    return mp.nstr(value, 45)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--digits',type=int,default=120)
    parser.add_argument('--case',action='append',help='Prime-power cutoff,N; may be repeated.')
    parser.add_argument('--output',type=Path,default=Path(__file__).parent/'records'/'mass_stiffness_20260926.json')
    args = parser.parse_args()
    cases = [tuple(map(int,v.split(','))) for v in args.case] if args.case else [(2,4),(5,8),(13,8),(13,16),(13,24)]
    if any(limit<2 or n<2 for limit,n in cases):
        parser.error('Each cutoff and N must be at least 2.')
    mp.mp.dps = args.digits
    report = {'status':'exploratory; not interval-certified','date':'2026-09-26',
              'model':'GPT-6 (Codex); exact variant and effort not exposed',
              'python':platform.python_version(),'mpmath':mp.__version__,
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'cases':[]}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    cache = {}
    for limit,n in cases:
        if limit not in cache:
            nmax = max(nn for xx,nn in cases if xx==limit)
            w,error = weil_matrix(limit,nmax)
            cache[limit]=(w,nmax,error)
        w,nmax,error = cache[limit]
        record = analyze(limit,n,args.digits,w,nmax,error)
        report['cases'].append(strings(record))
        args.output.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps({'cutoff':limit,'N':n,'epsilon':mp.nstr(record['least_eigenvalue'],8),
                          'omega1':mp.nstr(record['first_frequencies'][0],12),
                          'a1':mp.nstr(record['inverse_square_moments_including_free_tail'][0],12),
                          'max_check':mp.nstr(max(record['checks'].values()),4)}),flush=True)


if __name__=='__main__':
    main()
