#!/usr/bin/env python3
"""Fixed-support CCM port and inverse-energy diagnostics; no zero data.

Reuses the preserved arithmetic builder. Results are multiprecision checks,
not interval enclosures. Dense matrices live only in memory.
"""
import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp

from check_mass_stiffness import weil_matrix, scaled_error, trace, strings
from check_string_realization import mechanical_pair, local_string


HERE = Path(__file__).resolve().parent
SOURCE_NAMES = ('check_energy_ports.py', 'check_mass_stiffness.py',
                'check_string_realization.py')
RADII = (1, 100, 1000000, 10**12, 10**24)


def string_from_port(mass, stiff, force, lower, normal):
    """Reconstruct with a general real port, fixing first bead mass to one."""
    n = mass.rows
    seed = mp.lu_solve(lower, force)
    beta2 = (seed.T*seed)[0]
    v = seed/mp.sqrt(beta2)
    columns, diag, off = [], [], []
    threshold = mp.power(10, -mp.mp.dps//2)*max(1, mp.norm(normal))
    for j in range(n):
        columns.append(v)
        w = normal*v
        diag.append((v.T*w)[0])
        for _ in range(2):
            for q in columns:
                w -= q*(q.T*w)[0]
        if j+1 < n:
            a = mp.norm(w)
            if a <= threshold:
                raise ArithmeticError('Numerical cyclicity failed; no modes discarded.')
            off.append(a)
            v = -w/a
    u = mp.matrix(n, n)
    for j, v in enumerate(columns):
        u[:, j] = v
    c = mp.diag(diag)
    for j, a in enumerate(off):
        c[j, j+1] = c[j+1, j] = -a
    e1 = mp.eye(n)[:, 0]
    r = mp.lu_solve(c, e1)
    h = r/r[0]
    if min(h) <= 0:
        raise ArithmeticError('Nonpositive static scale.')
    masses = [v*v for v in h]
    springs = [1/r[0]]+[off[j]*h[j]*h[j+1] for j in range(n-1)]
    positions, x = [], mp.mpf(0)
    for k in springs:
        x += 1/k
        positions.append(x)
    moment = mp.fsum(m*x for m, x in zip(masses, positions))
    dh = mp.diag(list(h))
    incidence = mp.eye(n)
    for j in range(1, n):
        incidence[j, j-1] = -1
    ks = incidence.T*mp.diag(springs)*incidence
    ms = mp.diag(masses)
    transform = (lower.T**-1)*u*dh
    static = mp.lu_solve(stiff, force)
    compliance = (force.T*static)[0]
    static_mass = (static.T*mass*static)[0]
    mass_formula = beta2*static_mass/compliance**2
    checks = {
        'orthogonality': scaled_error(u.T*u, mp.eye(n)),
        'intertwining': scaled_error(normal*u, u*c),
        'mass_congruence': scaled_error(transform.T*mass*transform, ms),
        'stiffness_congruence': scaled_error(transform.T*stiff*transform, ks),
        'first_position_formula': abs(positions[0]-compliance/beta2),
        'total_mass_formula': abs(mp.fsum(masses)-mass_formula)/max(1, mass_formula),
        'trace_moment': abs(moment-trace(stiff**-1*mass))/max(1, moment),
    }
    t = mp.mpc('0.7', '0.3')**2
    original = mp.det(stiff-t*mass)/mp.det(stiff)
    rebuilt = mp.det(ks-t*ms)/mp.det(ks)
    checks['determinant'] = abs(original-rebuilt)/max(1, abs(original))
    response = (force.T*mp.lu_solve(stiff-t*mass, force))[0]
    rebuilt_response = beta2*(e1.T*mp.lu_solve(ks-t*ms, e1))[0]
    checks['port_response'] = abs(response-rebuilt_response)/max(1, abs(response))
    def quantile(frac):
        total = mp.mpf(0)
        for m, x in zip(masses, positions):
            total += m*x
            if total >= frac*moment:
                return x
        return positions[-1]
    return dict(
        masses=masses, positions=positions, total_mass=mp.fsum(masses),
        first_position=positions[0], string_length=positions[-1],
        first_jacobi_diagonal=diag[0],
        first_jacobi_offdiagonal=off[0] if off else None,
        inverse_square_trace=moment,
        trace_tail={str(a):mp.fsum(m*x for m,x in zip(masses, positions) if x>a)
                    for a in RADII},
        trace_tail_fraction={str(a):mp.fsum(m*x for m,x in zip(masses, positions) if x>a)/moment
                             for a in RADII},
        trace_quantile_positions={str(a):quantile(mp.mpf(a)) for a in ('0.5','0.9','0.99')},
        mass_bound_from_trace_over_first_position=moment/positions[0],
        checks=checks)


def controls():
    mass, stiff = mp.eye(2), mp.matrix([[2,-1],[-1,2]])
    string = string_from_port(mass, stiff, mp.matrix([1,0]), mp.eye(2), stiff)
    exact_error = max(abs(string['masses'][1]-mp.mpf(1)/4),
                      abs(string['positions'][0]-mp.mpf(2)/3),
                      abs(string['positions'][1]-mp.mpf(8)/3))
    rejected = False
    try:
        string_from_port(mp.eye(2), mp.diag([1,4]), mp.matrix([1,0]),
                         mp.eye(2), mp.diag([1,4]))
    except ArithmeticError as exc:
        rejected = 'cyclicity' in str(exc)
    if not rejected:
        raise ArithmeticError('Noncyclic control was not rejected.')
    # A continuum odd gap is essential: positive finite two-parity pencils
    # alone can have K_N -> 0 and divergent inverse traces.
    return dict(noncyclic_port_rejected=rejected,
                exact_two_bead_checks={**string['checks'], 'known_coefficients':exact_error},
                closing_gap_traces=[1,10,100])


def run(nvalues, digits):
    mp.mp.dps = digits
    length, nmax = mp.log(13), max(nvalues)
    report = dict(date='2026-09-26',
        status='exploratory; not interval-certified',
        model='GPT-6 (Codex); exact variant and reasoning effort not exposed',
        decimal_digits=digits, python=platform.python_version(), mpmath=mp.__version__,
        zero_data_used=False, X=13,
        sources_sha256={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                        for name in SOURCE_NAMES},
        normalization='first bead mass one, for every port and cutoff',
        smooth_profile='q_n = 2^(1-n), n >= 1, truncated at N',
        cases=[], controls=controls())
    print(f'Building X=13, N={nmax}, decimal digits={digits}', flush=True)
    full, entry_error = weil_matrix(13, nmax)
    for n in nvalues:
        start = nmax-n
        pair = mechanical_pair(full[start:start+2*n+1,start:start+2*n+1], n, length)
        mass, stiff = pair['M'], pair['K']
        lower = mp.cholesky(mass)
        inverse_lower = lower**-1
        raw = inverse_lower*stiff*inverse_lower.T
        normal = (raw+raw.T)/2
        e1 = mp.eye(n)[:, 0]
        smooth = mp.matrix([mp.power(2, -j) for j in range(n)])
        ports = dict(force=e1, displacement=mass*e1,
                     smooth_displacement=mass*smooth,
                     inverse_energy_displacement=mass*mp.lu_solve(stiff, mass*e1))
        result = dict(N=n, epsilon=pair['epsilon'],
                      observed_full_ground_gap=pair['gap'],
                      odd_gap=mp.eigsy(stiff, eigvals_only=True)[0],
                      mass_trace=trace(mass),
                      inverse_square_trace=trace(stiff**-1*mass),
                      mass_fourier_tail={str(k):mp.fsum(mass[j,j] for j in range(k,n))
                                         for k in (4,8,16) if k<n},
                      full_inverse_square_trace=trace(stiff**-1*mass)+(length/(2*mp.pi))**2*mp.zeta(2,n+1),
                      ports={}, checks=dict(selected_direct_entry=entry_error,
                                            whitened_symmetry=scaled_error(raw,raw.T)))
        for name, force in ports.items():
            data = string_from_port(mass, stiff, force, lower, normal)
            result['ports'][name] = data
            print(json.dumps(dict(N=n, port=name,
                mass=mp.nstr(data['total_mass'],8), length=mp.nstr(data['string_length'],8),
                tail_fraction_1e6=mp.nstr(data['trace_tail_fraction']['1000000'],8),
                q90=mp.nstr(data['trace_quantile_positions']['0.9'],8))), flush=True)
        # The old implementation is a regression cross-check at the smallest cutoff.
        if n == min(nvalues):
            for name in ('force','displacement'):
                old = local_string(mass, stiff, name)
                new = result['ports'][name]
                result['checks']['legacy_'+name] = max(
                    abs(a-b)/max(1,abs(a),abs(b))
                    for key in ('masses','positions') for a,b in zip(old[key],new[key]))
        report['cases'].append(result)
    residuals = list(report['controls']['exact_two_bead_checks'].values())
    for case in report['cases']:
        residuals += list(case['checks'].values())
        for p in case['ports'].values():
            residuals += list(p['checks'].values())
    report['maximum_scaled_residual'] = max(residuals)
    if max(residuals)>mp.mpf('1e-35'):
        raise ArithmeticError('Reconstruction residual exceeds 1e-35; increase precision.')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--digits', type=int, default=120)
    parser.add_argument('--cutoffs', type=int, nargs='+', default=[8,12,16,24,32])
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.digits<80 or min(args.cutoffs)<2:
        parser.error('Require at least 80 decimal digits and cutoffs >= 2.')
    report = run(sorted(set(args.cutoffs)), args.digits)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(strings(report), indent=2)+'\n')
    print('Maximum scaled residual: '+mp.nstr(report['maximum_scaled_residual'],8), flush=True)


if __name__ == '__main__':
    main()
