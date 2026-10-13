#!/usr/bin/env python3
"""Exact rank-two algebra and outward folded-coset Fourier obstruction.

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent model gpt-6-astra (Codex), reasoning effort ultra.
Only the explicitly marked diagnostic uses binary floating arithmetic.
"""
import argparse
from decimal import Decimal
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time

HASHES = {
    'check_block_current.py': '0cfca37632cfaaea522cce2a9514b81eaf9db0bf6213cd243de0f937679627a2',
    'check_complete_current_rectangle.py': 'ac547ff45915d95369afc558f6ee3daa01fb6974ad1569e719dc3f0abcd4c522',
}


class Poly:
    """Small exact four-variable rational polynomial for identity assertions."""
    def __init__(self, terms):
        if isinstance(terms, (int, Fraction)):
            terms = {(0, 0, 0, 0): Fraction(terms)}
        self.terms = {k: Fraction(v) for k, v in terms.items() if v}
    @staticmethod
    def cast(v):
        return v if isinstance(v, Poly) else Poly(v)
    def __add__(self, other):
        terms = dict(self.terms)
        for k, v in self.cast(other).terms.items():
            terms[k] = terms.get(k, 0) + v
        return Poly(terms)
    __radd__ = __add__
    def __neg__(self):
        return Poly({k: -v for k, v in self.terms.items()})
    def __sub__(self, other):
        return self + -self.cast(other)
    def __rsub__(self, other):
        return self.cast(other) + -self
    def __mul__(self, other):
        terms = {}
        for a, b in self.terms.items():
            for c, d in self.cast(other).terms.items():
                key = tuple(x + y for x, y in zip(a, c))
                terms[key] = terms.get(key, 0) + b*d
        return Poly(terms)
    __rmul__ = __mul__
    def __pow__(self, n):
        out = Poly(1)
        for _ in range(n):
            out = out*self
        return out
    def __truediv__(self, n):
        return self*Fraction(1, n)
    def __eq__(self, other):
        return self.terms == self.cast(other).terms


def d_source(poly):
    """D[e^u P(z)e^-z] = e^u [(1-4z)P+4zP']e^-z."""
    out = [0]*(len(poly)+1)
    for k, value in enumerate(poly):
        out[k] += (1+4*k)*value
        out[k+1] -= 4*value
    while out and out[-1] == 0:
        out.pop()
    return out


def exact_checks():
    k, ell, a, b = [Poly({tuple(int(j == i) for j in range(4)): 1}) for i in range(4)]
    n, m = (k+ell)/2, (k-ell)/2
    Q = ((a+b)*(k*k+ell*ell) + 2*(a-b)*k*ell)/4
    assert a*n*n+b*m*m == Q
    assert ((a+b)/4)**2-((a-b)/4)**2 == a*b/4
    # M=[[a+b,a-b],[a-b,a+b]], det(M)=4ab; adj(M)M=4ab I.
    assert (a+b)**2-(a-b)**2 == 4*a*b
    assert (a+b)*(b-a)+(a-b)*(a+b) == 0
    source = d_source(d_source([1])); source[0] -= 1
    assert source == [0, -24, 16]
    assert source[0] == 0
    phi = [Fraction(v, 8) for v in source]
    assert phi == [0, -3, 2]  # +/- n and the factor 1/16 in Phi.
    radius = 7
    original = {(n, m) for n in range(-radius, radius+1) for m in range(-radius, radius+1)}
    image = {(n+m, n-m) for n, m in original}
    inverse_domain = {(k, ell) for k in range(-2*radius, 2*radius+1)
                      for ell in range(-2*radius, 2*radius+1)
                      if (k-ell) % 2 == 0 and abs(k+ell) <= 2*radius and abs(k-ell) <= 2*radius}
    assert image == inverse_domain and len(image) == len(original)
    assert {((k+ell)//2, (k-ell)//2) for k, ell in image} == original
    coset_counts = [sum(k % 2 == j for k, ell in image) for j in (0, 1)]
    assert all((n+m) % 2 == ((n-m) % 2) for n, m in original)
    assert all(((n+m) % 2 == 0) == (n % 2 == m % 2) for n, m in original)
    # General polynomial identities, not finite sample tests.
    s, r = k, ell
    u, v = s+r, s-r
    for j in (0, 1):
        symbol = (-1)**(j+1)*(u*v)**(j+1) - Fraction((-1)**(j+1), 2)*(u*v)**j*(u*u+v*v)
        assert symbol == 2*r*r*(r*r-s*s)**j
        assert symbol*Fraction(2, 4) == r*r*(r*r-s*s)**j
    h, q, shift, kap = k, ell, a, b
    # Real even H has H'=H'''=0 at x=0. Half-transform of raw A is
    # kap*exp(-i*shift*x)*H; raw B is H-A. Store odd derivatives as imaginary parts.
    A = [kap*h, -shift*kap*h, kap*(q-shift**2*h), kap*(shift**3*h-3*shift*q)]
    B = [(1-kap)*h, shift*kap*h, (1-kap)*q+kap*shift**2*h, -A[3]]
    raw0 = -A[1]**2-A[0]*A[2]-B[1]**2-B[0]*B[2]
    raw1 = A[2]**2+A[1]*A[3]+B[2]**2+B[1]*B[3]
    assert raw0 == -(kap**2+(1-kap)**2)*h*q-shift**2*kap*h**2
    assert raw1 == (kap**2+(1-kap)**2)*q**2+(2*kap+2*kap**2)*shift**2*h*q
    return {'status': 'PASS', 'coefficient_field': 'exact rational polynomials',
            'source_insertion_P': source, 'positive_n_Phi_insertion_P_over_8': [str(v) for v in phi],
            'lattice_test_radius': radius, 'lattice_points': len(original), 'even_odd_coset_counts': coset_counts,
            'identities': ['unequal-scale quadratic form including mixed term', 'quadratic-form determinant ab/4',
                           'even-coset Poisson matrix determinant 4ab and inverse numerator',
                           'D_u^2-1 source insertion and zero-axis annihilation',
                           'both-coset lattice bijection on mapped diamond',
                           'J0 and J1 Fourier symbols with Jacobian 2 and H=A/2',
                           'raw shifted-source same-coset J0 and J1 symbols at frequency zero']}


def floating_diagnostics():
    """Finite sums and Simpson samples are diagnostics with no certified tails."""
    def phi_n(u, n):
        z = math.pi*n*n*math.exp(4*u)
        return math.exp(u)*(2*z*z-3*z)*math.exp(-z)
    def direct(u):
        return sum(phi_n(abs(u), n) for n in range(1, 5))
    def sectors(u, v):
        p, q = abs(u), abs(v)
        aa, bb = math.exp(4*p), math.exp(4*q)
        out = [0.0, 0.0]
        for k in range(-8, 9):
            for ell in range(-8, 9):
                if (k-ell) % 2 or abs(k+ell) > 8 or abs(k-ell) > 8:
                    continue
                n, m = (k+ell)//2, (k-ell)//2
                z, w = math.pi*aa*n*n, math.pi*bb*m*m
                # This uses Q from the coupled form, retaining its mixed term.
                Q = math.pi*((aa+bb)*(k*k+ell*ell)+2*(aa-bb)*k*ell)/4
                out[k % 2] += math.exp(p+q)*(16*z*z-24*z)*(16*w*w-24*w)*math.exp(-Q)/256
        return out
    samples = []
    for u, v in [(0.0, 0.0), (.1, .3), (-.2, .05), (.4, -.1)]:
        even, odd = sectors(u, v); product = direct(u)*direct(v)
        assert abs(even+odd-product) <= 2e-14*max(product, 1e-100)
        samples.append({'u': u, 'v': v, 'direct_product': product,
                        'even_coset': even, 'odd_coset': odd,
                        'relative_difference': (even+odd-product)/product})
    # Independent direct kernel and coupled-lattice projections on one finite window.
    cells = 128; s = .2; t = .025
    projected = [[0.0, 0.0, 0.0] for _ in range(2)]
    for i in range(cells+1):
        r = i/cells; weight = (1 if i in (0, cells) else 4 if i % 2 else 2)*2/(3*cells)
        even, odd = sectors(s+r, s-r)
        complete = direct(s+r)*direct(s-r)
        for j in (0, 1):
            multiplier = weight*r*r*(r*r-s*s)**j*math.exp(2*t*(s*s+r*r))
            for index, value in enumerate((complete, even, odd)):
                projected[j][index] += multiplier*value
    for direct_J, even_J, odd_J in projected:
        assert abs(direct_J-even_J-odd_J) <= 2e-13*max(abs(direct_J), 1e-100)
    # Unequal-scale Gaussian Poisson check, keeping both half-shift characters.
    aa, bb = 1.3, 2.7
    primal = [0.0, 0.0]; dual = [0.0, 0.0]
    for n in range(-8, 9):
        for m in range(-8, 9):
            primal[(n+m) % 2] += math.exp(-math.pi*(aa*n*n+bb*m*m))
    for k in range(-20, 21):
        for ell in range(-20, 21):
            qstar = ((aa+bb)*(k*k+ell*ell)-2*(aa-bb)*k*ell)/(4*aa*bb)
            value = math.exp(-math.pi*qstar)/(2*math.sqrt(aa*bb))
            dual[0] += value
            dual[1] += (-1)**(k+ell)*value
    assert all(abs(p-d) < 3e-15 for p, d in zip(primal, dual))
    # Differentiate the Poisson prefactor together with its Gaussian, as required.
    p, q = .1, .3
    differentiated_dual = [0.0, 0.0]
    for k in range(-24, 25):
        for ell in range(-24, 25):
            z = math.pi*math.exp(-4*p)*(k+ell)**2/4
            w = math.pi*math.exp(-4*q)*(k-ell)**2/4
            value = math.exp(-p-q)*(16*z*z-24*z)*(16*w*w-24*w)*math.exp(-z-w)/512
            differentiated_dual[0] += value
            differentiated_dual[1] += (-1)**(k+ell)*value
    differentiated_primal = sectors(p, q)
    assert all(abs(p-d) < 3e-16 for p, d in zip(differentiated_primal, differentiated_dual))
    return {'status': 'PASS_DIAGNOSTIC_ONLY', 'arithmetic': 'binary64; finite sums and finite Simpson window; no tail payment',
            'product_samples': samples, 'kernel_parameters': {'s': s, 't': t, 'r_half_window': [0, 1], 'cells': cells},
            'J0_direct_even_odd': projected[0], 'J1_direct_even_odd': projected[1],
            'unequal_scale_Poisson_check': {'a': aa, 'b': bb, 'primal_even_odd': primal, 'dual_even_odd': dual},
            'differentiated_Poisson_check': {'p': p, 'q': q, 'primal_even_odd': differentiated_primal,
                                            'dual_even_odd': differentiated_dual}}


def certificate(cells, interval_dir):
    for name, digest in HASHES.items():
        if hashlib.sha256((interval_dir/name).read_bytes()).hexdigest() != digest:
            raise RuntimeError('Retained interval source mismatch: '+name)
    sys.path.insert(0, str(interval_dir))
    from check_complete_current_rectangle import I, pi_interval, reduced_trig, absmax, PRECISION
    pi = pi_interval(); x = I(60); radius = I(1); width = radius/cells
    polys = [[0, -3, 2]]
    for _ in range(4):
        polys.append(d_source(polys[-1]))
    def evaluate(poly, z):
        value = I(0)
        for coefficient in reversed(poly):
            value = value*z+coefficient
        return value
    def source_jets(u):
        out = [[I(0) for _ in range(5)] for _ in range(2)]
        e4, e1 = (4*u).exp(), u.exp()
        for n in (1, 2, 3):
            z = pi*n*n*e4; prefactor = e1*(-z).exp()
            for j in range(5):
                out[n % 2][j] += prefactor*evaluate(polys[j], z)
        return out
    def integrand(u):
        source = source_jets(u)
        sine, cosine = reduced_trig(x*u, pi)
        trig = [cosine, -sine, -cosine, sine]
        return [[u**j*trig[j]*source[sector][0] for j in range(4)] for sector in (0, 1)]
    totals = [[I(0) for _ in range(4)] for _ in range(2)]
    errors = [[I(0) for _ in range(4)] for _ in range(2)]
    moment_ranges = [I(0), I(0)]
    left_values = integrand(I(0))
    for cell in range(cells):
        left, right = width*cell, width*(cell+1)
        box = I(left.lo, right.hi); midpoint = (left+right)/2
        middle_values, right_values = integrand(midpoint), integrand(right)
        source = source_jets(box)
        for index, order in enumerate((0, 2)):
            moment_ranges[index] += width*box**order*(source[0][0]+source[1][0])
        for sector in (0, 1):
            for j in range(4):
                totals[sector][j] += width*(left_values[sector][j]+4*middle_values[sector][j]+right_values[sector][j])/6
                # Multinomial Leibniz bound for the fourth u derivative.
                fourth = I(0)
                for a in range(min(j, 4)+1):
                    for b in range(5-a):
                        c = 4-a-b
                        coefficient = (math.factorial(4)//(math.factorial(a)*math.factorial(b)*math.factorial(c))
                                       *math.factorial(j)//math.factorial(j-a))
                        fourth += coefficient*box**(j-a)*x**b*I(absmax(source[sector][c]))
                errors[sector][j] += width**5*fourth/2880
        left_values = right_values
    # All omitted theta terms n>=4, allocated safely to each parity sector.
    # e^(9u-pi*n²e^(4u)) <= e^(-pi*n²) e^(-(4pi*n²-9)u).
    # Consecutive n term ratios <= (5/4)^4 exp(-9pi); replace n by 4 in the slope.
    ratio = (I(5)/4)**4*(-9*pi).exp()
    assert ratio.hi < 1
    theta_prefactor = 2*pi**2*4**4*(-16*pi).exp()/(1-ratio)
    slope = 64*pi-9
    theta_tails = [theta_prefactor*math.factorial(j)/slope**(j+1) for j in range(4)]
    # Full-source u>=1 tail. Phi <=4pi² exp(9u-pi e^(4u)), from ratio16exp(-3pi)<1/2.
    assert (16*(-3*pi).exp()).hi < Decimal('.5')
    tail_prefactor = 4*pi**2*(9*radius-pi*(4*radius).exp()).exp()
    kappa = 4*pi*(4*radius).exp()-9
    u_tails = [tail_prefactor*sum((math.comb(j, ell)*radius**(j-ell)*math.factorial(ell)/kappa**(ell+1)
                                  for ell in range(j+1)), I(0)) for j in range(4)]
    paid = []
    for sector in (0, 1):
        row = []
        for j in range(4):
            error = errors[sector][j]+theta_tails[j]+u_tails[j]
            row.append(totals[sector][j]+I(error.hi.copy_negate(), error.hi))
        paid.append(row)
    A, B = paid
    diagonal = [A[j+1]**2-A[j]*A[j+2]+B[j+1]**2-B[j]*B[j+2] for j in (0, 1)]
    mixed = [2*A[j+1]*B[j+1]-A[j]*B[j+2]-B[j]*A[j+2] for j in (0, 1)]
    assert all(v.hi < 0 for v in diagonal)
    moments = [value+I(0, (theta_tails[order]+u_tails[order]).hi)
               for value, order in zip(moment_ranges, (0, 2))]
    H0, I2 = moments
    shift = I(2).ln()/2; sqrt2 = shift.exp()
    raw_diagonal = [(2-sqrt2)*H0*I2-shift**2*H0**2/sqrt2,
                    (2-sqrt2)*I2**2-(1+sqrt2)*shift**2*H0*I2]
    assert all(v.hi < 0 for v in raw_diagonal)
    return {'status': 'PASS', 'arithmetic': str(PRECISION)+'-digit outward Decimal; exact integer derivative polynomials; explicit trigonometric remainders',
            'time': ['0', '0'], 'physical_frequency_x': x.strings(), 'kernel_Fourier_frequency': (2*x).strings(),
            'half_source_window': radius.strings(), 'Simpson_panels': cells, 'theta_terms': [1, 2, 3],
            'source_derivative_polynomials_DkPhi_n': polys,
            'source_definition': 'A(u)=sum_even_positive_n phi_n(|u|), B(u)=sum_odd_positive_n phi_n(|u|)',
            'jet_definition': 'h_A^(j)(x)=integral_0^infinity u^j cos(xu+j*pi/2) A(u) du; same for B',
            'retained_finite_jets': [[v.strings() for v in row] for row in totals],
            'Simpson_fourth_derivative_error_bounds': [[v.strings() for v in row] for row in errors],
            'complete_omitted_theta_tail_bounds_per_sector': [v.strings() for v in theta_tails],
            'complete_source_u_tail_bounds_per_sector': [v.strings() for v in u_tails],
            'paid_half_source_jets': [[v.strings() for v in row] for row in paid],
            'same_parity_coset_Fourier_J0_J1': [v.strings() for v in diagonal],
            'opposite_parity_coset_Fourier_J0_J1': [v.strings() for v in mixed],
            'raw_unfolded_coset_zero_frequency_certificate': {
                'time': '0', 'physical_frequency_x': '0',
                'definition': 'A_raw(u)=Phi_e(u+log(2)/2)/sqrt(2), B_raw=Phi_e-A_raw; this is different from the folded parity sources',
                'complete_H0_I2': [v.strings() for v in moments],
                'shift_a': shift.strings(), 'sqrt2': sqrt2.strings(),
                'moment_integration': '1024 outward cell ranges on [0,1] (or the --cells count), complete n>=4 and u>=1 tails',
                'same_parity_coset_Fourier_J0_J1': [v.strings() for v in raw_diagonal],
                'formulas': ['(2-sqrt2)*H0*I2-a^2*H0^2/sqrt2', '(2-sqrt2)*I2^2-(1+sqrt2)*a^2*H0*I2'],
                'scope': 'Both raw same-parity sector Fourier responses are negative at x=0. These do not assert a sign for the full source.'},
            'scope': 'Both same-parity folded-coset responses are strictly negative at t=0,x=60 with all tails paid. This refutes separate-coset autocorrelation/positive-definiteness claims, not complete-kernel positivity or either stationary sign.',
            'limitations': ['This is one frequency at one time, selected by floating diagnostics.',
                            'No stationary equation is asserted for either source sector.',
                            'The two sectors must be added before imposing the physical stationary conditions.',
                            'No RH implication or global complete-kernel sign is established.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', type=Path)
    parser.add_argument('--cells', type=int, default=1024)
    parser.add_argument('--interval-source-dir', type=Path,
                        default=Path(__file__).resolve().parents[4]/'quasi-rh-exponent-descent'/'newman_collisions'/'13_microlocal_phase_space'/'numerics')
    args = parser.parse_args(); assert args.cells > 0
    started = time.perf_counter()
    result = {'date': '2026-10-13', 'prepared_for': 'Edward Baker', 'model': 'gpt-6-astra (Codex)',
              'reasoning_effort': 'ultra; inherited from recorded parent session',
              'acknowledgment': 'Substantial LLM assistance; internal algebra and outward arithmetic replay, not independent validation.',
              'exact_algebra': exact_checks(), 'floating_diagnostics': floating_diagnostics(),
              'outward_certificate': certificate(args.cells, args.interval_source_dir),
              'imported_sources': HASHES, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'python_version': platform.python_version(), 'runtime_seconds': str(time.perf_counter()-started)}
    if args.record:
        args.record.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'exact_algebra': result['exact_algebra']['status'],
                      'floating_diagnostics': result['floating_diagnostics']['status'],
                      'outward_certificate': result['outward_certificate']['status'],
                      'same_coset_J0_J1': result['outward_certificate']['same_parity_coset_Fourier_J0_J1'],
                      'runtime_seconds': result['runtime_seconds']}, indent=2))


if __name__ == '__main__':
    main()
