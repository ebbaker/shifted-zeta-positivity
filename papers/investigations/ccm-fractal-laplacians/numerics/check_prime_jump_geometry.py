#!/usr/bin/env python3
"""Prescribed logarithmic-coordinate tests of the CCM resistance proposal.

Exploratory mpmath arithmetic, not interval certification. No zeta-zero data.
Both form identities are tested, without choosing a basis from eigenvectors.
The accompanying note proves the odd-folding obstruction independently.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import sys

import mpmath as mp


def trace(a):
    return mp.fsum(a[i, i] for i in range(a.rows))


def sym(a):
    return (a+a.T)/2


def relative(a, b):
    return mp.norm(a-b)/max(mp.norm(a), mp.norm(b), mp.mpf('1e-1000'))


def max_entry(a):
    return max(abs(x) for x in a)


def block(a, rows, cols):
    return mp.matrix([[a[i, j] for j in cols] for i in rows])


def parity(n):
    even, odd = mp.zeros(2*n+1, n+1), mp.zeros(2*n+1, n)
    even[n, 0] = 1
    for j in range(1, n+1):
        even[n+j, j] = even[n-j, j] = 1/mp.sqrt(2)
        odd[n+j, j-1] = 1/mp.sqrt(2)
        odd[n-j, j-1] = -1/mp.sqrt(2)
    return even, odd


def analytic_components(limit, n, prime_powers):
    """Signed prime and pole contributions in the defining Fourier basis."""
    length = mp.log(limit)
    terms = [(v, p, mp.log(v), mp.log(p)/mp.sqrt(v))
             for v, p in prime_powers(limit)]
    indices = list(range(-n, n+1))

    def correlation(i, j, a):
        if i == j:
            return 2*(1-a/length)*mp.cos(2*mp.pi*i*a/length)
        return (mp.sin(2*mp.pi*j*a/length)-mp.sin(2*mp.pi*i*a/length))/(mp.pi*(i-j))

    prime = mp.matrix([[-mp.fsum(c*correlation(i, j, a) for _, _, a, c in terms)
                        for j in indices] for i in indices])
    pole = mp.matrix([[32*length*mp.sinh(length/4)**2*(length**2-16*mp.pi**2*i*j)
                       /((length**2+16*mp.pi**2*i*i)*(length**2+16*mp.pi**2*j*j))
                       for j in indices] for i in indices])
    weight = mp.fsum(c for _, _, _, c in terms)
    return prime, pole, weight, terms


def dyadic_nodes(n):
    """First n base-two radical inverses; nested, independent of all spectra."""
    result = []
    for j in range(1, n+1):
        bits = bin(j)[2:]
        result.append(Fraction(int(bits[::-1], 2), 2**len(bits)))
    return result


def extrema(a):
    off = [(a[i, j], i+1, j+1) for i in range(a.rows) for j in range(i+1, a.cols)]
    low, high = min(off), max(off)
    tol = mp.power(10, -mp.mp.dps//2)*max(1, max_entry(a))
    return dict(min_offdiagonal=low[0], min_pair=list(low[1:]),
                max_offdiagonal=high[0], max_pair=list(high[1:]),
                positive_offdiagonal_count=sum(x > tol for x, _, _ in off),
                negative_offdiagonal_count=sum(x < -tol for x, _, _ in off),
                min_row_sum=min(mp.fsum(a[i, j] for j in range(a.cols)) for i in range(a.rows)),
                max_absolute_diagonal=max(abs(a[i, i]) for i in range(a.rows)))


def harmonic(stiff, n):
    """Algebraic static extension: old vertices are the first n entries."""
    interior = list(range(n, stiff.rows))
    c = block(stiff, interior, interior)
    b = block(stiff, interior, list(range(n)))
    lower = -(c**-1)*b
    h = mp.zeros(stiff.rows, n)
    h[:n, :] = mp.eye(n)
    h[n:, :] = lower
    return h


def analyze(w, prime, pole, weight, n, length):
    even, odd = parity(n)
    wp, wm = even.T*w*even, odd.T*w*odd
    ep, vp = mp.eigsy(sym(wp))
    em = mp.eigsy(sym(wm), eigvals_only=True)
    epsilon = ep[0]
    gap = min(ep[1]-epsilon, em[0]-epsilon)
    ell = mp.matrix([[1/mp.sqrt(length)]+[mp.sqrt(2/length)]*n])
    boundary = abs((ell*vp[:, 0])[0])
    if gap <= 0 or boundary <= mp.power(10, -mp.mp.dps//3):
        raise ArithmeticError('Simple-even/nonzero-boundary hypotheses not resolved numerically.')
    jmat = mp.zeros(n+1, n)
    for j in range(n):
        d = 2*mp.pi*(j+1)/length
        jmat[0, j], jmat[j+1, j] = -mp.sqrt(2)/d, 1/d
    mass = sym(jmat.T*(wp-epsilon*mp.eye(n+1))*jmat)
    stiff = sym(wm-epsilon*mp.eye(n))
    mass_min = mp.eigsy(mass, eigvals_only=True)[0]
    if mass_min <= 0:
        raise ArithmeticError('Positive mass not resolved numerically.')
    kl = mp.cholesky(stiff)
    ikl = kl**-1
    invfreq = list(reversed(list(mp.eigsy(sym(ikl*mass*ikl.T), eigvals_only=True))))
    tau = trace(stiff**-1*mass)

    nodes = dyadic_nodes(n)
    bmat = mp.matrix([[mp.sqrt(2/length)*mp.sin(mp.pi*(j+1)*mp.mpf(x.numerator)/x.denominator)
                      for j in range(n)] for x in nodes])
    ib = bmat**-1
    kg, mg = sym(ib.T*stiff*ib), sym(ib.T*mass*ib)
    arch = w-prime-pole  # signed negative archimedean contribution
    components = dict(prime=prime, pole=pole, archimedean=arch)
    node_components = {name: sym(ib.T*(odd.T*part*odd)*ib)
                       for name, part in components.items()}
    node_components['ground_shift'] = -epsilon*ib.T*ib
    jump = sym(odd.T*(prime+2*weight*mp.eye(w.rows))*odd)
    jump_min = mp.eigsy(jump, eigvals_only=True)[0]
    if jump_min < -mp.power(10, -mp.mp.dps//2):
        raise ArithmeticError('The full-line prime jump Gram control failed.')
    kstats, mstats = extrema(kg), extrema(mg)
    ki, kj = [v-1 for v in kstats['max_pair']]
    mi, mj = [v-1 for v in mstats['min_pair']]

    def sine_defect(a):
        # sin(2t)^2 = sin(t)^2 + sin(t)*sin(3t), pointwise.
        return a[1, 1]-a[0, 0]-a[0, 2]

    mass_parts = {name: sym(jmat.T*(even.T*part*even)*jmat)
                  for name, part in components.items()}
    mass_parts['ground_shift'] = -epsilon*jmat.T*jmat
    defect = sine_defect(mass)
    checks = dict(stiffness_gram=relative(bmat.T*kg*bmat, stiff),
                  mass_gram=relative(bmat.T*mg*bmat, mass),
                  stiffness_components=relative(sum(node_components.values(), mp.zeros(n)), kg),
                  mass_components=relative(sum(mass_parts.values(), mp.zeros(n)), mass),
                  inverse_trace=abs(tau-mp.fsum(invfreq))/max(1, abs(tau)))
    result = dict(N=n, epsilon=epsilon, simple_even_gap=gap,
                  normalized_ground_boundary_magnitude=boundary,
                  minimum_mass_eigenvalue=mass_min,
                  finite_inverse_trace=tau,
                  first_frequencies=[1/mp.sqrt(x) for x in invfreq[:3]],
                  free_tail_inverse_trace=(length/(2*mp.pi))**2*mp.zeta(2, n+1),
                  node_fractions_of_half_interval=[str(x) for x in nodes],
                  evaluation_condition_frobenius=mp.norm(bmat)*mp.norm(ib),
                  nodal_stiffness=kstats, nodal_mass=mstats,
                  positive_stiffness_witness_components={k:a[ki, kj] for k, a in node_components.items()},
                  negative_mass_witness=dict(pair=[mi+1, mj+1], value=mg[mi, mj]),
                  minimum_prime_jump_eigenvalue=jump_min,
                  nodal_prime_jump=extrema(sym(ib.T*jump*ib)),
                  sine_measure_defect=defect,
                  sine_measure_defect_relative=abs(defect)/max(abs(mass[1,1]), abs(mass[0,0]), abs(mass[0,2])),
                  sine_measure_defect_components={k:sine_defect(a) for k, a in mass_parts.items()},
                  checks=checks)
    return result, dict(K=stiff, M=mass, J=jmat, epsilon=epsilon,
                        B=bmat, Kg=kg, Mg=mg, inverse_frequencies=invfreq)


def compare(coarse, fine):
    n, nf = coarse['K'].rows, fine['K'].rows
    h = harmonic(fine['Kg'], n)
    sk, sm = h.T*fine['Kg']*h, h.T*fine['Mg']*h
    delta = coarse['epsilon']-fine['epsilon']
    edk = fine['K'][:n,:n]-coarse['K']
    edm = fine['M'][:n,:n]-coarse['M']
    lc, lf = coarse['inverse_frequencies'], fine['inverse_frequencies']
    checks = dict(stiffness_fourier_compression=max_entry(edk-delta*mp.eye(n)),
                  mass_fourier_compression=max_entry(edm-delta*coarse['J'].T*coarse['J']))
    # Necessary eigenvalue inequalities for ANY simultaneous form embedding.
    upper = [lf[i]-lc[i] for i in range(n)]
    lower = [lc[i]-lf[i+nf-n] for i in range(n)]
    result = dict(old_N=n, new_N=nf, epsilon_drop=delta,
                  finite_inverse_trace_increase=mp.fsum(lf)-mp.fsum(lc),
                  inverse_spectrum_upper_interlacing_min=min(upper),
                  inverse_spectrum_lower_interlacing_min=min(lower),
                  harmonic_stiffness_relative_defect=relative(sk, coarse['Kg']),
                  harmonic_mass_relative_defect=relative(sm, coarse['Mg']),
                  harmonic_min_entry=min(h), harmonic_max_entry=max(h),
                  checks=checks)
    return result, h


def controls():
    # A positive measure must satisfy the pointwise sine-product identity.
    locations, masses = [mp.mpf(1)/7, mp.mpf(2)/5, mp.mpf(4)/5], [2, 3, 5]
    gram = mp.matrix([[mp.fsum(w*mp.sin(mp.pi*i*t)*mp.sin(mp.pi*j*t)
                                 for t, w in zip(locations, masses))
                       for j in range(1, 5)] for i in range(1, 5)])
    measure_error = abs(gram[1,1]-gram[0,0]-gram[0,2])
    # A grounded three-edge path: Schur energy AND pulled-back mass agree.
    fine_k = mp.matrix([[2,-1,0],[-1,2,-1],[0,-1,1]])
    fine_m = mp.diag([2,3,5])
    h2, h1 = harmonic(fine_k, 2), harmonic(fine_k, 1)
    k2, m2 = h2.T*fine_k*h2, h2.T*fine_m*h2
    h21 = harmonic(k2, 1)
    k1, m1 = h1.T*fine_k*h1, h1.T*fine_m*h1
    return dict(sine_measure_identity=measure_error,
                positive_graph_energy=relative(h21.T*k2*h21, k1),
                positive_graph_mass=relative(h21.T*m2*h21, m1),
                positive_graph_composition=max_entry(h2*h21-h1))


def folding_witness():
    """Two disjoint half-interval tents; direct quadrature of smooth cross term."""
    length, a, h = mp.log(13), mp.log(2), mp.mpf(1)/100
    t0, s0 = (length-a)/2-mp.mpf(1)/10, (length-a)/2+mp.mpf(1)/10

    def kernel(r):
        return 2*mp.cosh(r/2)-mp.exp(r/2)/(2*mp.sinh(r))

    def tent(y):
        return 1-abs(y)

    # Uniform quadrature is avoided at tent corners: split at zero.
    smooth = 2*h*h*mp.quad(lambda u: tent(u)*mp.quad(
        lambda v: tent(v)*(kernel(abs(t0+h*u-s0-h*v))-kernel(length-t0-h*u-s0-h*v)),
        [-1, 0, 1]), [-1, 0, 1])
    prime = 4*mp.log(2)/mp.sqrt(2)*h/3
    lower = Fraction(46, 16875)  # (16/27)h - 32 h^2 at h=1/100
    assert prime+smooth > mp.mpf(lower.numerator)/lower.denominator > 0
    return dict(half_support_centers=[t0,s0], half_width=h,
                prime_cross_energy=prime, smooth_cross_energy=smooth,
                total_cross_energy=prime+smooth, analytic_rational_lower_bound=str(lower),
                scalar_shift_cross_energy='0',
                status='Positive off-diagonal form value for disjoint nonnegative half-interval functions')


def strings(value):
    if isinstance(value, dict):
        return {k:strings(v) for k,v in value.items()}
    if isinstance(value, (list, tuple)):
        return [strings(v) for v in value]
    if isinstance(value, (str, int, bool)) or value is None:
        return value
    return mp.nstr(value, 45)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--digits', type=int, default=100)
    parser.add_argument('--operator-numerics', type=Path,
                        default=Path(__file__).resolve().parents[2]/'ccm-operator-realizations'/'numerics')
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if args.digits < 80:
        parser.error('At least 80 digits are required for the small shifted eigenvalues.')
    sys.path.insert(0, str(args.operator_numerics))
    from check_mass_stiffness import weil_matrix, prime_powers
    mp.mp.dps = args.digits
    full, entry_error = weil_matrix(13, 16)
    prime, pole, weight, terms = analytic_components(13, 16, prime_powers)
    cases, data, comparisons, maps = [], {}, [], {}
    for n in (4, 8, 16):
        start = 16-n
        selection = slice(start, start+2*n+1)
        result, data[n] = analyze(full[selection,selection], prime[selection,selection],
                                  pole[selection,selection], weight, n, mp.log(13))
        cases.append(result)
        print(json.dumps(dict(N=n, epsilon=mp.nstr(result['epsilon'],8),
                              finite_trace=mp.nstr(result['finite_inverse_trace'],10),
                              stiffness_max_offdiag=mp.nstr(result['nodal_stiffness']['max_offdiagonal'],8),
                              mass_min_offdiag=mp.nstr(result['nodal_mass']['min_offdiagonal'],8),
                              sine_mass_defect=mp.nstr(result['sine_measure_defect'],8))), flush=True)
    for nc, nf in ((4,8),(8,16),(4,16)):
        result, maps[nc,nf] = compare(data[nc], data[nf])
        comparisons.append(result)
    composition = relative(maps[8,16]*maps[4,8], maps[4,16])
    positive_controls = controls()
    residuals = [entry_error]+list(positive_controls.values())
    residuals += [v for row in cases+comparisons for v in row['checks'].values()]
    if max(residuals) > mp.mpf('1e-35'):
        raise ArithmeticError('An algebraic/numerical control failed: '+str(max(residuals)))
    # Reconstruct a few source entries by integrating their defining correlations;
    # the imported builder supplies this independent check for the full Weil form.
    record = dict(schema=1, date='2026-09-26',
                  model='GPT-6 (Codex); exact variant and effort setting not exposed',
                  status='Exploratory multiprecision diagnostics; analytic obstruction proved in accompanying note',
                  python=platform.python_version(), mpmath=mp.__version__, decimal_digits=args.digits,
                  sources_sha256={
                      'check_prime_jump_geometry.py':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'check_mass_stiffness.py':hashlib.sha256((args.operator_numerics/'check_mass_stiffness.py').read_bytes()).hexdigest()},
                  zero_data_used=False, full_matrices_saved=False,
                  X=13, L=mp.log(13), prime_power_terms=[dict(power=v, prime=p, delay=a, conductance=c) for v,p,a,c in terms],
                  cases=cases, cutoff_comparisons=comparisons,
                  harmonic_composition_relative_defect=composition,
                  controls=positive_controls, selected_direct_weil_entry_error=entry_error,
                  maximum_control_residual=max(residuals), folding_witness=folding_witness())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(strings(record), indent=2)+'\n')
    print(json.dumps(dict(output=str(args.output), controls='passed',
                          maximum_control_residual=mp.nstr(max(residuals),8))), flush=True)


if __name__ == '__main__':
    main()
