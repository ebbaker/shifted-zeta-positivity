"""Cohomological superspace action, boundary Ward identities, and preparation.

Exact Fraction/Grassmann algebra certifies the finite action identities.
NumPy checks canonical quantization, heat kernels, and prime-deformation
formulas. Floating-point results are diagnostics, not interval enclosures.
The continuum and infinite-tower statements are proved in the companion note.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json
import math
import platform
import numpy as np


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return list(map(list, zip(*a)))


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def madd(a, b, sign=1):
    return [[x+sign*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def inverse(a):
    n = len(a)
    rows = [list(row)+unit for row, unit in zip(a, eye(n))]
    for k in range(n):
        pivot = next(i for i in range(k, n) if rows[i][k])
        rows[k], rows[pivot] = rows[pivot], rows[k]
        divisor = rows[k][k]
        rows[k] = [x/divisor for x in rows[k]]
        for i in range(n):
            if i != k:
                factor = rows[i][k]
                rows[i] = [x-factor*y for x, y in zip(rows[i], rows[k])]
    return [row[n:] for row in rows]


# Canonical polynomial algebra: eight even generators followed by nine odd ones.
# Even: b[2], bbar[2], db/dy[2], dbbar/dy[2].
# Odd: c[3], cbar[3], dc/dy[3]. Barred time derivatives are unnecessary here.
NE = 8
NO = 9
UNIT_KEY = ((0,)*NE, 0)


def psum(*polys):
    result = {}
    for p in polys:
        for key, value in p.items():
            result[key] = result.get(key, F(0))+value
    return {key: value for key, value in result.items() if value}


def pscale(p, value):
    return {key: value*x for key, x in p.items() if value*x}


def pmul(p, q):
    result = {}
    for (ep, op), x in p.items():
        for (eq, oq), y in q.items():
            if op & oq:
                continue
            inversions = sum((oq & ((1 << i)-1)).bit_count()
                             for i in range(NO) if op & (1 << i))
            key = (tuple(a+b for a, b in zip(ep, eq)), op | oq)
            result[key] = result.get(key, F(0))+(-1)**inversions*x*y
    return {key: value for key, value in result.items() if value}


def pproduct(factors):
    value = {UNIT_KEY: F(1)}
    for factor in factors:
        value = pmul(value, factor)
    return value


def evar(i):
    exponent = [0]*NE
    exponent[i] = 1
    return {(tuple(exponent), 0): F(1)}


def ovar(i):
    return {((0,)*NE, 1 << i): F(1)}


def q_derivation(p, d):
    # q b = q cbar = 0, q c = D b, q bbar = cbar D.
    # Time derivatives transform by the time derivative of these rules.
    rules = {}
    for j in range(2):
        rules[('e', 2+j)] = psum(*(pscale(ovar(3+i), d[i][j]) for i in range(3)))
    for i in range(3):
        rules[('o', i)] = psum(*(pscale(evar(j), d[i][j]) for j in range(2)))
        rules[('o', 6+i)] = psum(*(pscale(evar(4+j), d[i][j]) for j in range(2)))
    result = {}
    for (exponents, mask), coefficient in p.items():
        generators = [('e', i) for i, power in enumerate(exponents) for _ in range(power)]
        generators += [('o', i) for i in range(NO) if mask & (1 << i)]
        factors = [evar(i) if kind == 'e' else ovar(i) for kind, i in generators]
        odd_before = 0
        for k, generator in enumerate(generators):
            if generator in rules:
                term = pproduct(factors[:k]+[rules[generator]]+factors[k+1:])
                result = psum(result, pscale(term, coefficient*(-1)**odd_before))
            odd_before += generator[0] == 'o'
    return result


def bilinear(left, matrix, right):
    return psum(*(pscale(pmul(left[i], right[j]), value)
                  for i, row in enumerate(matrix) for j, value in enumerate(row)))


def exact_action_checks():
    d = [[F(1), F(0)], [F(0), F(1)], [F(1), F(2)]]
    ds = transpose(d)
    g = mm(ds, d)
    p = madd(eye(3), mm(mm(d, inverse(g)), ds), -1)
    require(mm(p, p) == p and mm(ds, p) == [[0]*3 for _ in range(2)],
            'Harmonic projection identities failed')
    b = [evar(i) for i in range(2)]
    bb = [evar(2+i) for i in range(2)]
    db = [evar(4+i) for i in range(2)]
    c = [ovar(i) for i in range(3)]
    cb = [ovar(3+i) for i in range(3)]
    dc = [ovar(6+i) for i in range(3)]
    kinetic = psum(bilinear(bb, eye(2), db), bilinear(cb, eye(3), dc))
    endpoint = pscale(psum(bilinear(bb, eye(2), b), bilinear(cb, eye(3), c)), -1)
    require(not q_derivation(kinetic, d), 'Kinetic action is not q invariant')
    require(not q_derivation(endpoint, d), 'Coherent endpoint action is not q invariant')
    rows = []
    for lam in [F(0), F(1, 3), F(2)]:
        r = madd(eye(2), [[lam*x for x in row] for row in g])
        hb, hf = mm(r, g), mm(mm(d, r), ds)
        gauge_fermion = bilinear(bb, mm(r, ds), c)
        h = psum(bilinear(bb, hb, b), bilinear(cb, hf, c))
        require(q_derivation(gauge_fermion, d) == h, 'Superspace theta component differs')
        require(not q_derivation(h, d), 'Hamiltonian action is not q closed')
        require(not q_derivation(q_derivation(gauge_fermion, d), d), 'Nilpotency failed')
        require(mm(hf, p) == [[0]*3 for _ in range(3)], 'Protected sector changed')
        rows.append(dict(lambda_value=str(lam),
                         boson_frequency=[[str(x) for x in row] for row in hb],
                         fermion_frequency=[[str(x) for x in row] for row in hf]))
    # Independent variation of the range: D(epsilon)=D+epsilon*E.
    delta = [[F(0), F(1)], [F(0), F(0)], [F(1), F(-1)]]
    dg = madd(mm(transpose(delta), d), mm(ds, delta))
    gi = inverse(g)
    derivative_direct = madd(
        madd(mm(mm(delta, gi), ds), mm(mm(d, gi), transpose(delta))),
        mm(mm(mm(mm(d, gi), dg), gi), ds), -1)
    derivative_direct = [[-x for x in row] for row in derivative_direct]
    derivative_geometric = madd(mm(mm(mm(p, delta), gi), ds),
                               mm(mm(mm(d, gi), transpose(delta)), p))
    derivative_geometric = [[-x for x in row] for row in derivative_geometric]
    require(derivative_direct == derivative_geometric, 'Projection variation formula failed')
    return dict(status='passed', arithmetic='Fraction polynomial and Grassmann algebra',
                D=[[str(x) for x in row] for row in d],
                P=[[str(x) for x in row] for row in p], rows=rows,
                identities=['q kinetic = 0', 'q endpoint = 0', 'q V_R = H_R',
                            'q H_R = 0', 'q squared V_R = 0', 'H_F,R P = 0',
                            'exact projection derivative for a changing D'])


def fock_controls():
    # Complete sectors of total excitation number <= 2; Q preserves this cutoff.
    d = np.array([[1., 0.], [0., 1.], [1., 2.]])
    g = d.T@d
    basis = [(n0, n1, mask) for n0, n1, mask in product(range(3), range(3), range(8))
             if n0+n1+mask.bit_count() <= 2]
    index = {state: i for i, state in enumerate(basis)}
    count = len(basis)
    bosons, fermions = [], []
    for mode in range(2):
        a = np.zeros((count, count))
        for j, state in enumerate(basis):
            numbers = list(state)
            if numbers[mode]:
                coefficient = math.sqrt(numbers[mode])
                numbers[mode] -= 1
                a[index[tuple(numbers)], j] = coefficient
        bosons.append(a)
    for mode in range(3):
        a = np.zeros((count, count))
        for j, (n0, n1, mask) in enumerate(basis):
            if mask & (1 << mode):
                sign = (-1)**(mask & ((1 << mode)-1)).bit_count()
                a[index[(n0, n1, mask ^ (1 << mode))], j] = sign
        fermions.append(a)
    q = sum(d[i, j]*fermions[i].T@bosons[j] for i in range(3) for j in range(2))
    maximum = float(np.max(abs(q@q)))
    rows = []
    for lam in [0., 1/3, 2.]:
        r = np.eye(2)+lam*g
        hb, hf = r@g, d@r@d.T
        v = sum((r@d.T)[j, i]*bosons[j].T@fermions[i]
                for i in range(3) for j in range(2))
        h = sum(hb[i, j]*bosons[i].T@bosons[j] for i in range(2) for j in range(2))
        h += sum(hf[i, j]*fermions[i].T@fermions[j] for i in range(3) for j in range(3))
        ev, rotation = np.linalg.eigh(r)
        dsqrt = d@((rotation*np.sqrt(ev))@rotation.T)
        qr = sum(dsqrt[i, j]*fermions[i].T@bosons[j]
                 for i in range(3) for j in range(2))
        errors = [np.max(abs(q@v+v@q-h)), np.max(abs(qr@qr)),
                  np.max(abs(qr@qr.T+qr.T@qr-h)), np.max(abs(q@h-h@q))]
        maximum = max(maximum, *map(float, errors))
        spectrum = np.linalg.eigvalsh(h)
        require(spectrum.min() > -1e-11, 'Fock Hamiltonian lost positivity')
        ground_dimension = int(np.count_nonzero(abs(spectrum) < 1e-10))
        require(ground_dimension == 2, 'Expected empty vacuum and one harmonic fermion')
        rows.append(dict(lambda_value=lam, zero_energy_states=ground_dimension,
                         lowest_nonzero_frequency=float(spectrum[spectrum > 1e-10].min())))
    require(maximum < 1e-11, 'Canonical supercharge algebra failed')
    return dict(status='passed', total_excitation_cutoff=2, fock_dimension=count,
                largest_algebra_error=maximum, rows=rows,
                scope='Complete invariant excitation sectors; not a truncated CCR identity.')


def exp_symmetric(a, time):
    values, rotation = np.linalg.eigh(a)
    return (rotation*np.exp(-time*values))@rotation.T


def boundary_controls():
    d = np.array([[1., 0.], [0., 1.], [1., 2.]])
    g = d.T@d
    gi = np.linalg.inv(g)
    p = np.eye(3)-d@gi@d.T
    vg = np.array([1+1j, 2-.5j, -.3+1j])
    vf = np.array([.4-1j, -.2+.1j, 2+.7j])
    expected = np.vdot(vg, p@vf)
    maximum = 0.
    raw_derivative_examples = []
    for lam in [0., .2, 2.]:
        r = np.eye(2)+lam*g
        hf = d@r@d.T
        variation = d@g@d.T
        for time in [.01, .2, 1., 4.]:
            heat = exp_symmetric(hf, time)
            formula = p+d@gi@exp_symmetric(r@g, time)@d.T
            maximum = max(maximum, float(np.max(abs(heat-formula))),
                          float(abs(np.vdot(p@vg, heat@p@vf)-expected)))
            # Gluing two half preparations yields the full positive boundary kernel.
            half = exp_symmetric(hf, time/2)
            maximum = max(maximum, float(np.max(abs(half.T@half-heat))))
            ward = np.vdot(p@vf, variation@heat@p@vf)
            maximum = max(maximum, float(abs(ward)))
            raw_derivative = float((-time*np.vdot(vf, variation@heat@vf)).real)
            require(raw_derivative < 1e-10, 'Raw insertion variation has wrong sign')
            raw_derivative_examples.append(dict(lambda_value=lam, time=time,
                                                raw_pairing_derivative=raw_derivative))
    require(maximum < 1e-10, 'Boundary propagator or protected Ward identity failed')
    return dict(status='passed', largest_propagator_gluing_or_ward_error=maximum,
                protected_complex_pairing=[float(expected.real), float(expected.imag)],
                unprotected_boundary_examples=raw_derivative_examples)


def prime_projection_controls():
    ell, r = np.log(2.), 2**(-.5)
    w0 = -np.euler_gamma-np.pi/2-3*np.log(2.)-np.log(np.pi)
    maximum = 0.
    rows = []
    for a, tau, coupling in product([.5, 2.5, 8.5], [.3, 2., 13.], [0., .4, 1.]):
        phase = np.exp(-1j*ell*tau)
        generator = w0-2*ell*r*phase/(1-r*phase)
        m = np.exp(coupling*generator)
        d = np.array([[1.], [1j*tau*m/a]])
        delta = np.array([[0.], [generator*1j*tau*m/a]])
        g = float((d.conj().T@d)[0, 0].real)
        p = np.eye(2)-d@d.conj().T/g
        pdot = -(p@delta@d.conj().T+d@delta.conj().T@p)/g
        x = tau*tau*abs(m)**2/a**2
        response = (2/a)*p[0, 0].real
        derivative = (2/a)*pdot[0, 0].real
        formula = (2/a)*x/(1+x)
        derivative_formula = (2/a)*2*generator.real*x/(1+x)**2
        maximum = max(maximum, abs(response-formula), abs(derivative-derivative_formula))
        rows.append(dict(mass=a, tau=tau, arithmetic_coupling=coupling,
                         response=float(response), arithmetic_derivative=float(derivative)))
    require(maximum < 1e-12, 'First-prime harmonic response variation failed')
    return dict(status='passed', largest_response_or_projection_derivative_error=maximum,
                rows=rows, interpretation='Arithmetic changes D and its harmonic projection; it is not the protected R deformation.')


def tower_preparation_controls():
    a = 2*np.arange(200)+.5
    rows = []
    for time in [.1, .5, 1., 4., 16., 32.]:
        bound = 4*np.exp(-time/4)/(-np.expm1(-6*time))
        maximum_error = 0.
        for tau, qvalue, lam in product([0., .1, 1., 10., 1000.],
                                        [1., 2., 1e6], [0., .2, 2.]):
            g = 1+tau*tau/(qvalue*a*a)
            frequency = a*a*g*(1+lam*g)
            correction = float(np.sum((2/a)/g*np.exp(-time*frequency)))
            require(0 <= correction <= bound*(1+1e-14), 'Preparation bound violated')
            maximum_error = max(maximum_error, correction)
        # Analytic omitted-channel bound; reported decimal values are diagnostic.
        first_omitted = 400.5
        tail_bound = (2/first_omitted)*np.exp(-time*first_omitted**2)/(-np.expm1(-time*1606))
        rows.append(dict(time=time, analytic_bound_float=float(bound),
                         largest_sampled_preparation_correction=maximum_error,
                         omitted_channel_bound_float=float(tail_bound)))
    return dict(status='passed', rows=rows,
                exact_bound='0 <= Z_T - Z_infinity <= 4*exp(-T/4)/(1-exp(-6*T))*I',
                scope='Uniform analytic proof in note. Decimal displays and samples are not interval certificates; tail displays may underflow.')


def common_rate_cutoff_controls():
    rows = []
    fixed_time, tau = .7, 1.3
    previous = None
    for count in [10, 100, 1000, 10000, 100000]:
        a = 2*np.arange(count)+.5
        weights = 2/a
        sigma = float(weights.sum())
        g = 1+tau*tau/(a*a)
        fixed_correction = float(np.sum(weights/g*np.exp(-fixed_time*g)))
        fixed_bound = math.exp(-fixed_time)*sigma
        require(0 <= fixed_correction <= fixed_bound,
                'Common-rate source bound violated')
        # eta_N=log(log(N+e)) tends to infinity; T_N=log(sigma_N)+eta_N.
        eta = math.log(math.log(count+math.e))
        diagonal_time = math.log(sigma)+eta
        diagonal_bound = math.exp(-eta)
        largest = 0.
        for frequency, qvalue in product([0., 1., 10.], [1., 1e6]):
            gx = 1+frequency*frequency/(qvalue*a*a)
            correction = float(np.sum(weights/gx*np.exp(-diagonal_time*gx)))
            require(0 <= correction <= diagonal_bound*(1+1e-14),
                    'Cutoff-dependent preparation bound violated')
            largest = max(largest, correction)
        row = dict(channels=count, total_source_weight=sigma,
                   fixed_time=fixed_time, fixed_frequency=tau,
                   fixed_time_correction=fixed_correction,
                   fixed_time_bound=fixed_bound,
                   diagonal_preparation_time=diagonal_time,
                   diagonal_error_bound=diagonal_bound,
                   largest_sampled_diagonal_error=largest)
        if previous is not None:
            slope = (fixed_correction-previous[1])/math.log(count/previous[0])
            row['logarithmic_growth_slope'] = slope
        rows.append(row)
        previous = count, fixed_correction
    require(abs(rows[-1]['logarithmic_growth_slope']-math.exp(-fixed_time)) < 1e-4,
            'Expected logarithmic source divergence not reproduced')
    return dict(status='passed', rows=rows,
                exact_bound='0 <= C_N,T - K_N <= exp(-T)*sum(k<N, 2/a_k)*I',
                limiting_logarithmic_growth_slope=math.exp(-fixed_time),
                scope='Free external-state norm divergence, not an interaction-loop correction. Analytic cutoff-limit proof in note; numerical samples are diagnostic.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = dict(status='passed', date='2026-09-13',
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  python=platform.python_version(), numpy=np.__version__,
                  exact_superspace_action=exact_action_checks(),
                  canonical_fock_quantization=fock_controls(),
                  boundary_pairing_and_ward=boundary_controls(),
                  first_prime_projection=prime_projection_controls(),
                  infinite_tower_preparation=tower_preparation_controls(),
                  common_rate_cutoff_preparation=common_rate_cutoff_controls(),
                  scope='Explicit free cohomological superspace theory and protected relative boundary pairing. Its first-prime response retains the known residual; no full Weil positivity claim.')
    encoded = json.dumps(report, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
        print(json.dumps(dict(status='passed', output=str(args.output),
                              exact_superspace_action='passed', fock_algebra='passed',
                              protected_ward_identity='passed', first_prime_projection='passed',
                              infinite_tower_preparation_bound='passed',
                              common_rate_cutoff_limit='passed'), indent=2))
    else:
        print(encoded, end='')


if __name__ == '__main__':
    main()
