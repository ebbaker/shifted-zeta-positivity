#!/usr/bin/env python3
"""Finite CCM strings, passive-boundary obstruction, and cutoff drift.

Reuses the defining Weil quadrature, not saved eigenvalues. No zeta zeros
are evaluated. Multiprecision diagnostics only; no interval certification.
Run from any directory; see numerics/README.md for reproduction commands.
"""
import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp

from check_mass_stiffness import weil_matrix, scaled_error, trace, strings


def mechanical_pair(w, n, length):
    even, odd = mp.zeros(2*n+1, n+1), mp.zeros(2*n+1, n)
    even[n, 0] = 1
    for j in range(1, n+1):
        even[n+j, j] = even[n-j, j] = 1/mp.sqrt(2)
        odd[n+j, j-1] = 1/mp.sqrt(2)
        odd[n-j, j-1] = -1/mp.sqrt(2)
    wp, wm = even.T*w*even, odd.T*w*odd
    ep, vp = mp.eigsy(wp)
    em = mp.eigsy(wm, eigvals_only=True)
    eps = ep[0]
    if min(ep[1]-eps, em[0]-eps) <= 0:
        raise ArithmeticError('Simple-even hypothesis not observed.')
    ell = mp.matrix([[1/mp.sqrt(length)]+[mp.sqrt(2/length)]*n])
    ground = vp[:, 0]
    boundary = (ell*ground)[0]
    if not boundary:
        raise ArithmeticError('Zero boundary normalization.')
    ground /= boundary
    jmat = mp.zeros(n+1, n)
    rmat = mp.zeros(n, n+1)
    freq = [2*mp.pi*j/length for j in range(1, n+1)]
    for j, d in enumerate(freq):
        jmat[0, j], jmat[j+1, j] = -mp.sqrt(2)/d, 1/d
        rmat[j, j+1] = d
    mass = jmat.T*(wp-eps*mp.eye(n+1))*jmat
    stiff = wm-eps*mp.eye(n)
    return dict(M=mass, K=stiff, J=jmat, epsilon=eps,
                gap=min(ep[1]-eps, em[0]-eps), ground=ground,
                ell=ell, R=rmat, frequencies=freq)


def local_string(mass, stiff, seed_kind='force'):
    """b=e_1 or b=M e_1; cyclicity is checked, never silently assumed."""
    n = mass.rows
    lower = mp.cholesky(mass)
    ilower = lower**-1
    raw = ilower*stiff*ilower.T
    symmetry = scaled_error(raw, raw.T)
    normal = (raw+raw.T)/2
    endpoint = mp.eye(n)[:, 0]
    force = endpoint if seed_kind == 'force' else mass*endpoint
    seed = ilower*force
    seed_norm = mp.norm(seed)
    vec = seed/seed_norm
    columns, diagonal, offdiag = [], [], []
    threshold = mp.power(10, -mp.mp.dps//2)*max(1, mp.norm(normal))
    for i in range(n):
        columns.append(vec)
        work = normal*vec
        diagonal.append((vec.T*work)[0])
        # Twice reorthogonalized Lanczos; alternating sign makes offdiagonal negative.
        for _ in range(2):
            for old in columns:
                work -= old*(old.T*work)[0]
        beta = mp.norm(work)
        if i+1 < n:
            if beta <= threshold:
                raise ArithmeticError('Seed is not numerically cyclic: use a block decomposition.')
            offdiag.append(beta)
            vec = -work/beta
    umat = mp.matrix(n, n)
    for j, col in enumerate(columns):
        umat[:, j] = col
    jacobi = mp.diag(diagonal)
    for j, beta in enumerate(offdiag):
        jacobi[j, j+1] = jacobi[j+1, j] = -beta
    response0 = mp.lu_solve(jacobi, endpoint)
    scale = response0/response0[0]  # first bead mass = 1
    if min(scale) <= 0:
        raise ArithmeticError('Positive static scaling failed.')
    springs = [1/response0[0]] + [offdiag[j]*scale[j]*scale[j+1] for j in range(n-1)]
    masses = [a*a for a in scale]
    positions, total = [], mp.mpf(0)
    for spring in springs:
        total += 1/spring
        positions.append(total)
    dh = mp.diag(list(scale))
    incidence = mp.eye(n)
    for i in range(1, n):
        incidence[i, i-1] = -1
    ks = incidence.T*mp.diag(springs)*incidence
    ms = mp.diag(masses)
    transform = ilower.T*umat*dh
    green = mp.matrix([[min(x, y) for y in positions] for x in positions])
    gram = mp.matrix([[mp.sqrt(masses[i]*masses[j])*green[i, j]
                       for j in range(n)] for i in range(n)])
    inverse = stiff**-1*mass
    moment = mp.fsum(m*x for m, x in zip(masses, positions))
    spectrum = mp.eigsy(jacobi, eigvals_only=True)
    if spectrum[0] <= 0:
        raise ArithmeticError('Positive string spectrum failed.')
    differential = mp.diag([mp.sqrt(k) for k in springs])*incidence*dh**-1
    # Explicit unitary intertwiner from the CCM boundary-gauge Dirac operator.
    dirac = mp.zeros(2*n)
    ccm = mp.zeros(2*n)
    unitary = mp.zeros(2*n)
    dirac[:n, n:] = differential.T
    dirac[n:, :n] = differential
    ccm[:n, n:] = mass**-1*stiff
    ccm[n:, :n] = mp.eye(n)
    unitary[:n, :n] = umat.T*lower.T
    unitary[n:, n:] = differential*umat.T*lower.T
    metric = mp.zeros(2*n)
    metric[:n, :n], metric[n:, n:] = mass, stiff
    checks = dict(normal_symmetry=symmetry,
                  lanczos_orthogonality=scaled_error(umat.T*umat, mp.eye(n)),
                  lanczos_intertwining=scaled_error(normal*umat, umat*jacobi),
                  mass_congruence=scaled_error(transform.T*mass*transform, ms),
                  stiffness_congruence=scaled_error(transform.T*stiff*transform, ks),
                  string_green_kernel=scaled_error(ks**-1, green),
                  trace_mass_moment=abs(trace(inverse)-moment)/max(1, abs(moment)),
                  dirac_metric=scaled_error(unitary.T*unitary, metric),
                  dirac_intertwining=scaled_error(unitary*ccm, dirac*unitary))
    determinant_errors, response_errors = [], []
    for z in (mp.mpc('0.7', '0.3'), mp.mpc('12', '1.7')):
        t = z*z
        original = mp.det(stiff-t*mass)/mp.det(stiff)
        string = mp.det(ks-t*ms)/mp.det(ks)
        strain = mp.det(mp.eye(n)-t*gram)
        determinant_errors += [abs(original-string)/max(1, abs(original)),
                               abs(original-strain)/max(1, abs(original))]
        response = (force.T*mp.lu_solve(stiff-t*mass, force))[0]
        boundary_response = seed_norm**2 * (endpoint.T*mp.lu_solve(ks-t*ms, endpoint))[0]
        response_errors.append(abs(response-boundary_response)/max(1, abs(response)))
    checks['determinant'] = max(determinant_errors)
    checks['boundary_response'] = max(response_errors)
    return dict(seed=seed_kind, masses=masses, springs=springs, positions=positions,
                first_jacobi_diagonal=diagonal[0],
                first_jacobi_offdiagonal=offdiag[0] if n>1 else None,
                smallest_lanczos_offdiagonal=min(offdiag) if offdiag else None,
                first_frequency=mp.sqrt(spectrum[0]),
                trace_inverse_square=moment,
                first_moment_of_string_measure=moment,
                total_mass=mp.fsum(masses), string_length=positions[-1],
                trace_fraction_beyond={str(r):mp.fsum(m*x for m,x in zip(masses,positions) if x>r)/moment
                                       for r in (1,100,1000000)},
                coercive_lower_bound_squared=1/moment,
                checks=checks)


def synthetic_controls():
    """Controls for both excluded behavior and the limited convergence claim."""
    # A genuine passive update has uniform residues and interlacing.
    diagonal = mp.diag([1, 4, 9])
    b = mp.matrix([1, 1, 1])
    values = list(mp.eigsy(diagonal+b*b.T, eigvals_only=True))
    passive_interlaces = all(a <= v <= c for a, v, c in zip([1,4], values, [4,9])) and values[-1]>=9
    # Positive mechanics alone permits an arbitrarily large inverse trace.
    one = local_string(mp.matrix([[100]]), mp.matrix([[1]]))
    # Weak convergence need not be trace-norm convergence on unbounded supports:
    # mu_n=(1/n) delta_n has trace one, eigenvalue one, and vague/weak limit zero.
    return dict(passive_positive_rank_one_interlaces=bool(passive_interlaces),
                passive_eigenvalues=values,
                positive_one_mass_trace=one['trace_inverse_square'],
                positive_one_mass_string_checks=one['checks'],
                escaping_mass_examples=[dict(n=n, mass=mp.mpf(1)/n,
                                            position=n, trace=1,
                                            determinant_at_z_half=mp.mpf('0.75'))
                                        for n in (10,100,1000)])


def run(cases, digits):
    mp.mp.dps = digits
    report = dict(status='exploratory; not interval-certified', date='2026-09-26',
                  model='GPT-6 (Codex); exact variant and reasoning effort not exposed',
                  python=platform.python_version(), mpmath=mp.__version__,
                  decimal_digits=digits, zero_data_used=False,
                  sources_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                                  for p in (Path(__file__), Path(__file__).with_name('check_mass_stiffness.py'))},
                  cases=[], cutoff_comparisons=[], controls=synthetic_controls())
    for limit in sorted(set(x for x, _ in cases)):
        nvalues = sorted(set(n for x,n in cases if x == limit))
        nmax = max(nvalues)
        w, entry_error = weil_matrix(limit, nmax)
        length = mp.log(limit)
        previous = None
        for n in nvalues:
            offset = nmax-n
            pair = mechanical_pair(w[offset:offset+2*n+1, offset:offset+2*n+1], n, length)
            string = local_string(pair['M'], pair['K'])
            displacement_string = local_string(pair['M'], pair['K'], 'displacement')
            residues = [mp.sqrt(2/length)*d*d*pair['ground'][j+1]
                        for j,d in enumerate(pair['frequencies'])]
            residue_scale = mp.fsum(abs(r) for r in residues)
            rmat, g, ell = pair['R'], pair['ground'], pair['ell']
            rank_one = rmat*(mp.eye(n+1)-g*ell)*rmat.T
            string['checks']['rank_one_pencil'] = scaled_error(pair['M']*rank_one, pair['K'])
            string['checks']['selected_direct_entry'] = entry_error
            tail = (length/(2*mp.pi))**2*mp.zeta(2,n+1)
            result = dict(X=limit, L=length, N=n, epsilon=pair['epsilon'],
                          observed_ground_gap=pair['gap'],
                          free_second_frequency=pair['frequencies'][1],
                          first_frequency_exceeds_free_second=bool(string['first_frequency']>pair['frequencies'][1]),
                          normalized_rank_one_residues=[r/residue_scale for r in residues],
                          residue_signs=[int(mp.sign(r)) for r in residues],
                          free_tail_inverse_square_sum=tail,
                          full_inverse_square_trace=string['trace_inverse_square']+tail,
                          string=string, displacement_seed_string=displacement_string)
            report['cases'].append(result)
            if previous:
                oldn, oldpair, oldstring = previous
                delta = oldpair['epsilon']-pair['epsilon']
                mass_restriction = pair['M'][:oldn,:oldn]
                stiff_restriction = pair['K'][:oldn,:oldn]
                q = mp.eye(oldn)[:,0]
                m0 = (q.T*oldpair['M']*q)[0]
                k0 = (q.T*oldpair['K']*q)[0]
                jm = (q.T*oldpair['J'].T*oldpair['J']*q)[0]
                rho0 = k0/m0
                rho1 = (q.T*stiff_restriction*q)[0]/(q.T*mass_restriction*q)[0]
                drift = delta*(1-rho0*jm)/(m0+delta*jm)
                comparison = dict(X=limit, old_N=oldn, new_N=n, epsilon_drop=delta,
                    relative_first_jacobi_change=(string['first_jacobi_diagonal']/oldstring['first_jacobi_diagonal']-1),
                    trial_rayleigh_change=rho1-rho0, predicted_rayleigh_change=drift,
                    checks=dict(mass_compression=scaled_error(mass_restriction, oldpair['M']+delta*oldpair['J'].T*oldpair['J']),
                                stiffness_compression=scaled_error(stiff_restriction, oldpair['K']+delta*mp.eye(oldn)),
                                rayleigh_drift=abs(rho1-rho0-drift)/max(1,abs(rho0),abs(rho1))))
                report['cutoff_comparisons'].append(comparison)
            previous = (n, pair, string)
            print(json.dumps(dict(X=limit, N=n,
                trace=mp.nstr(string['trace_inverse_square'],10),
                string_length=mp.nstr(string['string_length'],8),
                mass=mp.nstr(string['total_mass'],8),
                displacement_string_length=mp.nstr(displacement_string['string_length'],8),
                mixed_residues=min(residues)<0<max(residues),
                max_check=mp.nstr(max(string['checks'].values()),4))), flush=True)
    all_checks = [v for c in report['cases'] for v in c['string']['checks'].values()]
    all_checks += [v for c in report['cases'] for v in c['displacement_seed_string']['checks'].values()]
    all_checks += [v for c in report['cutoff_comparisons'] for v in c['checks'].values()]
    all_checks += list(report['controls']['positive_one_mass_string_checks'].values())
    report['maximum_scaled_residual'] = max(all_checks)
    if not report['controls']['passive_positive_rank_one_interlaces']:
        raise ArithmeticError('Passive control failed.')
    if max(all_checks) > mp.mpf('1e-30'):
        raise ArithmeticError('A reconstruction residual exceeds 1e-30; increase precision.')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--digits', type=int, default=120)
    parser.add_argument('--case', action='append', help='X,N; repeatable.')
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).parent/'records'/'string_realization_120_20260926.json')
    args = parser.parse_args()
    cases = [tuple(map(int, s.split(','))) for s in args.case] if args.case else [(2,4),(5,8),(13,8),(13,12),(13,16)]
    if any(x<2 or n<2 for x,n in cases):
        parser.error('Require X>=2, N>=2.')
    report = run(cases, args.digits)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(strings(report), indent=2)+'\n')


if __name__ == '__main__':
    main()
