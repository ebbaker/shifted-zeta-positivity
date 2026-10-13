#!/usr/bin/env python3
"""Checks for the Claude review of the active lifted-theta directions.

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier claude-opus-5-5; the serving
model may differ), Claude Cowork, reasoning effort max.

Standard library only; deterministic; writes a JSON record.

Part A uses exact rational (and Gaussian-rational) arithmetic:
  A1  boost-defect lemma for the Newman weight on Gaussian sources;
  A2  product rule for the Laguerre expression, L(pG)=p^2 L(G)+(p'^2-pp'')G^2;
  A3  d^2/ds^2 [F(s+iT)F(s-iT)] at s=1/2 equals 2(G'^2-GG''), G(T)=F(1/2+iT),
      for polynomials F with F(s)=F(1-s);
  A4  the second s-derivative of the folded constant-term (pole) terms.
Part B is a double-precision numerical replay (composite Gauss-Legendre
quadrature, no interval arithmetic). It is evidence for exact identities
that are proved analytically in the review, not a certificate:
  B1  completed zeta xi_c(s)=pi^{-s/2}Gamma(s/2)zeta(s) from Riemann's theta
      integral (value at 1/2, first zero);
  B2  normalisation of the Fourier-Whittaker expansion of the completed
      Eisenstein series E*(z,w): E*(iy,w)=E*(i/y,w);
  B3  the Eisenstein (rank-two) form of G^2 and of the Laguerre expression
      G'^2-GG'' for G(T)=xi_c(1/2+iT);
  B4  the same for the program's H_0 (first Laguerre expression), against
      direct integrals of the theta source Phi;
  B5  evenness of the raw theta series for Phi and positivity of the
      Euler-factor control sources; their off-line zero offsets.
"""
import argparse
import cmath
import hashlib
import json
import math
import platform
from fractions import Fraction as Q
from pathlib import Path

PI = math.pi

# ----------------------------------------------------------------------------
# Part A: exact checks
# ----------------------------------------------------------------------------


class GQ:
    """Gaussian rational a+bi with Fraction parts."""

    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re = Q(re)
        self.im = Q(im)

    def __add__(self, o):
        o = o if isinstance(o, GQ) else GQ(o)
        return GQ(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __neg__(self):
        return GQ(-self.re, -self.im)

    def __sub__(self, o):
        o = o if isinstance(o, GQ) else GQ(o)
        return GQ(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return GQ(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, GQ) else GQ(o)
        return GQ(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def inv(self):
        d = self.re * self.re + self.im * self.im
        return GQ(self.re / d, -self.im / d)

    def __truediv__(self, o):
        o = o if isinstance(o, GQ) else GQ(o)
        return self * o.inv()

    def __pow__(self, k):
        r = GQ(1)
        for _ in range(k):
            r = r * self
        return r

    def __eq__(self, o):
        o = o if isinstance(o, GQ) else GQ(o)
        return self.re == o.re and self.im == o.im

    def pair(self):
        return [str(self.re), str(self.im)]


def poly_eval(coeffs, z):
    r = GQ(0)
    for c in reversed(coeffs):
        r = r * z + c
    return r


def poly_deriv(coeffs):
    return [k * coeffs[k] for k in range(1, len(coeffs))]


def poly_mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_add(a, b):
    n = max(len(a), len(b))
    return [(a[k] if k < len(a) else 0) + (b[k] if k < len(b) else 0) for k in range(n)]


def poly_scale(a, c):
    return [c * x for x in a]


def check_A1(count):
    """Boost-defect lemma on f(u)=exp(-b u^2), Newman weight exp(t u^2).

    With hat f(x) = (1/2) int exp(ixu) f(u) du and (tau_a f)(u)=f(u+a),
      Newman_t[tau_a f](x) = exp(t a^2) exp(-iax) Newman_t[f](x+2ita).
    Both sides are (1/2)sqrt(pi/(b-t)) exp(Q(x)) with Q quadratic in x; we
    compare the coefficients of Q exactly (x is symbolic).
    """
    cases = []
    for a, b, t in [(Q(1, 3), Q(2), Q(1, 5)), (Q(-3, 4), Q(7, 3), Q(1, 2)),
                    (Q(5, 2), Q(1), Q(-1, 7)), (Q(2, 9), Q(11, 10), Q(1, 20))]:
        assert b > t
        k = b - t
        # LHS exponent: -b a^2 + (ix - 2ab)^2 / (4k)
        # coefficients of x^2, x^1, x^0 (complex)
        lhs = [GQ(-b * a * a) + GQ(4 * a * a * b * b) / GQ(4 * k),  # x^0
               GQ(0, -4 * a * b) / GQ(4 * k),                       # x^1
               GQ(-1) / GQ(4 * k)]                                   # x^2
        # RHS exponent: t a^2 - i a x - (x + 2ita)^2 / (4k)
        rhs = [GQ(t * a * a) - GQ(-4 * t * t * a * a) / GQ(4 * k),
               GQ(0, -a) - GQ(0, 4 * t * a) / GQ(4 * k),
               GQ(-1) / GQ(4 * k)]
        for j in range(3):
            assert lhs[j] == rhs[j], (a, b, t, j)
            count[0] += 1
        cases.append({'a': str(a), 'b': str(b), 't': str(t), 'exponent_coefficients_equal': True})
    return cases


def check_A2(count):
    """L(pG) = p^2 L(G) + (p'^2 - p p'') G^2, L(F)=F'^2-FF'', exact."""
    p = [Q(1, 4), Q(0), Q(1)]  # T^2 + 1/4
    tests = [[Q(3), Q(-1), Q(2), Q(5, 7)], [Q(1), Q(0), Q(-2), Q(0), Q(1, 3)],
             [Q(-2, 5), Q(4), Q(1), Q(-3), Q(2), Q(1, 9)]]
    out = []
    for G in tests:
        def L(F):
            F1, F2 = poly_deriv(F), poly_deriv(poly_deriv(F))
            return poly_add(poly_mul(F1, F1), poly_scale(poly_mul(F, F2), -1))
        pG = poly_mul(p, G)
        lhs = L(pG)
        p1, p2 = poly_deriv(p), poly_deriv(poly_deriv(p))
        corr = poly_add(poly_mul(p1, p1), poly_scale(poly_mul(p, p2), -1))
        rhs = poly_add(poly_mul(poly_mul(p, p), L(G)), poly_mul(corr, poly_mul(G, G)))
        n = max(len(lhs), len(rhs))
        lhs += [Q(0)] * (n - len(lhs))
        rhs += [Q(0)] * (n - len(rhs))
        assert lhs == rhs
        assert corr == [Q(-1, 2), Q(0), Q(2)]  # 2T^2 - 1/2
        count[0] += 1
        out.append({'degree_G': len(G) - 1, 'identity_exact': True})
    return out


def check_A3(count):
    """d^2/ds^2 [F(s+iT)F(s-iT)] at s=1/2 equals 2(G'^2-GG'').

    F is a polynomial in (s-1/2)^2 with rational coefficients, so F(s)=F(1-s)
    and G(T)=F(1/2+iT) is real and even.
    """
    out = []
    for qcoef in [[Q(1), Q(-3), Q(2, 5)], [Q(-7, 3), Q(1), Q(4), Q(-1, 2)]]:
        # F(s) = sum q_k (s-1/2)^{2k}; as polynomial in v=s-1/2.
        Fv = []
        for k, c in enumerate(qcoef):
            Fv += [Q(0)] * (2 * k + 1 - len(Fv))
            Fv[2 * k] += c
        Fv1, Fv2 = poly_deriv(Fv), poly_deriv(poly_deriv(Fv))
        for T in [Q(1, 3), Q(2), Q(-5, 4), Q(7)]:
            iT = GQ(0, T)
            # g(v) = F(v+iT) F(v-iT); g'' at v=0 = F''(iT)F(-iT)+2F'(iT)F'(-iT)+F(iT)F''(-iT)
            g2 = (poly_eval(Fv2, iT) * poly_eval(Fv, -iT)
                  + GQ(2) * poly_eval(Fv1, iT) * poly_eval(Fv1, -iT)
                  + poly_eval(Fv, iT) * poly_eval(Fv2, -iT))
            # G(T) = F(iT) as a real polynomial in T: substitute v = iT
            G = poly_eval(Fv, iT)
            # G'(T) = i F'(iT), G''(T) = -F''(iT)
            G1 = GQ(0, 1) * poly_eval(Fv1, iT)
            G2 = GQ(-1) * poly_eval(Fv2, iT)
            assert G.im == 0 and G1.im == 0 and G2.im == 0
            rhs = GQ(2) * (G1 * G1 - G * G2)
            assert g2 == rhs
            count[0] += 1
        out.append({'F_coefficients_in_(s-1/2)^2k': [str(c) for c in qcoef], 'identity_exact': True})
    return out


def check_A4(count):
    """d^2/ds^2 [1/(s+iT) + 1/(1+iT-s)] at s=1/2 equals 4/(1/2+iT)^3."""
    out = []
    for T in [Q(1, 2), Q(2), Q(6), Q(-3, 7)]:
        s = GQ(Q(1, 2))
        iT = GQ(0, T)
        d2 = GQ(2) / ((s + iT) ** 3) + GQ(2) / ((GQ(1) + iT - s) ** 3)
        assert d2 == GQ(4) / ((GQ(Q(1, 2)) + iT) ** 3)
        count[0] += 1
        out.append({'T': str(T), 'equal': True})
    return out


# ----------------------------------------------------------------------------
# Part B: double-precision numerical replay
# ----------------------------------------------------------------------------


def gauss_legendre(n):
    nodes, weights = [], []
    for i in range(1, n + 1):
        x = math.cos(PI * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-16:
                break
        nodes.append(x)
        weights.append(2 / ((1 - x * x) * dp * dp))
    return nodes, weights


GL_X, GL_W = gauss_legendre(20)


def integrate(f, a, b, panels):
    h = (b - a) / panels
    total = 0
    for j in range(panels):
        lo = a + j * h
        for x, w in zip(GL_X, GL_W):
            total += w * f(lo + 0.5 * h * (x + 1))
    return total * 0.5 * h


def psi(x):
    s, n = 0.0, 1
    while True:
        term = math.exp(-PI * n * n * x)
        s += term
        if term < 1e-40:
            return s
        n += 1


PSI_CACHE = {}


def xi_c_jets(s, order=0):
    """xi_c(s) and its s-derivatives up to `order` (Riemann's theta formula).

    xi_c(s) = 1/(s(s-1)) + int_0^inf psi(e^v)(e^{vs/2}+e^{v(1-s)/2}) dv.
    """
    s = complex(s)
    def f(v):
        key = round(v, 15)
        if key not in PSI_CACHE:
            PSI_CACHE[key] = psi(math.exp(v))
        return PSI_CACHE[key]
    out = []
    for k in range(order + 1):
        def integrand(v, k=k):
            a = cmath.exp(v * s / 2) * (v / 2) ** k
            b = cmath.exp(v * (1 - s) / 2) * (-v / 2) ** k
            return f(v) * (a + b)
        val = integrate(integrand, 0.0, 6.0, 48)
        # derivatives of 1/(s(s-1)) = 1/(s-1) - 1/s
        r = ((-1) ** k) * math.factorial(k) * ((s - 1) ** (-(k + 1)) - s ** (-(k + 1)))
        out.append(r + val)
    return out


def kbessel(nu, z):
    """K_nu(z) = int_0^inf exp(-z cosh t) cosh(nu t) dt, real z>0, complex nu."""
    tmax = math.acosh(max(1.0, 90.0 / z)) + 0.5
    panels = max(8, int(tmax / 0.2) + 1)
    return integrate(lambda t: math.exp(-z * math.cosh(t)) * cmath.cosh(nu * t), 0.0, tmax, panels)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def estar_iy(y, w):
    """Completed Eisenstein series E*(iy,w) from its Fourier-Whittaker expansion."""
    w = complex(w)
    ct = xi_c_jets(2 * w)[0] * y ** w + xi_c_jets(2 * w - 1)[0] * y ** (1 - w)
    total = 0
    n = 1
    while 2 * PI * n * y < 95:
        sig = sum(complex(d) ** (1 - 2 * w) for d in divisors(n))
        total += n ** (w - 0.5) * sig * kbessel(w - 0.5, 2 * PI * n * y)
        n += 1
    return ct + 4 * math.sqrt(y) * total


def hecke_lambda(n, T):
    return sum(math.cos(T * math.log(n / (d * d))) for d in divisors(n))


def kpart(y, T):
    total = 0.0
    n = 1
    while 2 * PI * n * y < 95:
        total += hecke_lambda(n, T) * kbessel(1j * T, 2 * PI * n * y).real
        n += 1
    return 4 * math.sqrt(y) * total


def eisenstein_laguerre(T):
    """Return G^2, L(G) and their Eisenstein-Whittaker evaluations at T."""
    s = 0.5 + 1j * T
    j = xi_c_jets(s, 2)
    G = j[0].real
    G1 = (1j * j[1]).real       # dG/dT = i xi_c'(s)
    G2 = (-j[2]).real           # d^2G/dT^2 = -xi_c''(s)
    LG = G1 * G1 - G * G2
    cache = {}
    def K(y):
        if y not in cache:
            cache[y] = kpart(y, T)
        return cache[y]
    I0 = integrate(lambda y: K(y) / y, 1.0, 16.0, 60)
    I2 = integrate(lambda y: K(y) * math.log(y) ** 2 / y, 1.0, 16.0, 60)
    xw = xi_c_jets(1 + 2j * T)[0]
    pole1 = 4 * (xw / (0.5 + 1j * T)).real
    pole3 = 4 * (xw / (0.5 + 1j * T) ** 3).real
    return {'T': T, 'G': G, 'G_prime': G1, 'G_second': G2,
            'G_squared_direct': G * G, 'G_squared_eisenstein': 2 * I0 - pole1,
            'L_G_direct': LG, 'L_G_eisenstein': I2 - pole3,
            'L_G_cusp_part': I2, 'L_G_constant_term_part': -pole3,
            'G_squared_cusp_part': 2 * I0, 'G_squared_constant_term_part': -pole1}


def Phi(u, nmax=None):
    """Raw theta series for Phi, evaluated termwise at any real u."""
    total = 0.0
    n = 1
    while True:
        e = math.exp(4 * u)
        term = (2 * PI ** 2 * n ** 4 * math.exp(9 * u) - 3 * PI * n * n * math.exp(5 * u)) * math.exp(-PI * n * n * e)
        total += term
        if n > 3 and abs(term) < 1e-30 * max(1.0, abs(total)):
            return total
        n += 1
        if nmax and n > nmax:
            return total


def Phi_scale(u):
    """Sum of absolute values of the raw theta-series terms (cancellation scale)."""
    total = 0.0
    n = 1
    e = math.exp(4 * u)
    while True:
        term = abs(2 * PI ** 2 * n ** 4 * math.exp(9 * u) - 3 * PI * n * n * math.exp(5 * u)) * math.exp(-PI * n * n * e)
        total += term
        if n > 3 and term < 1e-30 * max(1.0, total):
            return total
        n += 1


def H0_jets(x):
    f0 = integrate(lambda u: Phi(u) * math.cos(x * u), 0.0, 1.6, 64)
    f1 = integrate(lambda u: -u * Phi(u) * math.sin(x * u), 0.0, 1.6, 64)
    f2 = integrate(lambda u: -u * u * Phi(u) * math.cos(x * u), 0.0, 1.6, 64)
    return f0, f1, f2


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output')
    args = ap.parse_args()
    count = [0]
    record = {
        'title': 'Checks for the Claude review of the active lifted-theta directions',
        'date': '2026-10-13', 'prepared_for': 'Edward Baker',
        'model': 'Claude Opus 5.5 (configured identifier claude-opus-5-5; serving model may differ)',
        'reasoning_effort': 'max',
        'llm_assistance': 'LLM-prepared internal check; not independent specialist validation',
    }
    A = {'A1_boost_defect_lemma': check_A1(count),
         'A2_laguerre_product_rule': check_A2(count),
         'A3_pair_second_derivative': check_A3(count),
         'A4_folded_pole_terms': check_A4(count)}
    record['part_A_exact'] = A
    record['part_A_assertions'] = count[0]

    B = {}
    tol = 1e-8
    # B1
    xi_half = xi_c_jets(0.5)[0].real
    lit = -8 * 0.49712077818831410991  # xi(1/2)=0.4971207781883141..., xi = s(s-1)xi_c/2
    gamma1 = 14.134725141734693790
    g_at_zero = xi_c_jets(0.5 + 1j * gamma1)[0].real
    g_scale = abs(xi_c_jets(0.5 + 1j * 14.0)[0].real) + abs(xi_c_jets(0.5 + 1j * 14.3)[0].real)
    assert rel(xi_half, lit) < 1e-12
    assert abs(g_at_zero) < 1e-7 * g_scale
    B['B1_xi_c'] = {'xi_c_half': xi_half, 'literature_value': lit, 'relative_error': rel(xi_half, lit),
                    'G_at_first_zero': g_at_zero, 'G_scale_nearby': g_scale}
    # B2
    b2 = []
    for w in [0.8, 0.5 + 3j]:
        e1, e2 = estar_iy(1.25, w), estar_iy(0.8, w)
        assert abs(e1 - e2) < 1e-11 * max(1e-3, abs(e1))
        b2.append({'w': str(w), 'E*(1.25 i)': [e1.real, e1.imag], 'E*(0.8 i)': [e2.real, e2.imag],
                   'abs_difference': abs(e1 - e2)})
    B['B2_eisenstein_normalisation'] = b2
    # B3
    b3 = []
    for T in [0.5, 2.0, 4.0, 6.0, 10.0, gamma1]:
        r = eisenstein_laguerre(T)
        # errors relative to the scale of the two pieces that are added
        sc_G2 = abs(r['G_squared_cusp_part']) + abs(r['G_squared_constant_term_part'])
        sc_LG = abs(r['L_G_cusp_part']) + abs(r['L_G_constant_term_part'])
        r['scaled_err_G2'] = abs(r['G_squared_direct'] - r['G_squared_eisenstein']) / sc_G2
        r['scaled_err_LG'] = abs(r['L_G_direct'] - r['L_G_eisenstein']) / sc_LG
        assert r['scaled_err_G2'] < tol and r['scaled_err_LG'] < tol, r
        b3.append(r)
    B['B3_eisenstein_form_of_G2_and_LG'] = b3
    # B4
    b4 = []
    for r in b3:
        T = r['T']
        if T < 1.0:
            continue
        h0, h1, h2 = H0_jets(2 * T)
        L0_direct = h1 * h1 - h0 * h2
        p = T * T + 0.25
        L0_formula = (p * p * r['L_G_direct'] + (2 * T * T - 0.5) * r['G_squared_direct']) / 1024
        L0_cusp = (p * p * r['L_G_cusp_part'] + (2 * T * T - 0.5) * r['G_squared_cusp_part']) / 1024
        L0_const = (p * p * r['L_G_constant_term_part'] + (2 * T * T - 0.5) * r['G_squared_constant_term_part']) / 1024
        assert abs(h0 + p * r['G'] / 16) < 1e-9 * max(abs(h0), 1e-6)
        assert rel(L0_direct, L0_formula) < 1e-8
        assert rel(L0_direct, L0_cusp + L0_const) < 1e-8
        b4.append({'x': 2 * T, 'H0_direct': h0, 'H0_from_xi_c': -p * r['G'] / 16,
                   'L0_direct': L0_direct, 'L0_eisenstein': L0_formula,
                   'L0_cusp_part': L0_cusp, 'L0_constant_term_part': L0_const,
                   'cusp_share': L0_cusp / L0_direct})
    B['B4_first_laguerre_expression_of_H0'] = b4
    # B5
    even = []
    for u in [0.05, 0.1, 0.2, 0.3, 0.5]:
        a, b = Phi(u), Phi(-u)
        scale = Phi_scale(-u)
        assert abs(a - b) < 1e-13 * scale
        even.append({'u': u, 'Phi(u)': a, 'Phi(-u)_raw_series': b,
                     'abs_difference': abs(a - b), 'raw_series_cancellation_scale': scale})
    controls = []
    for p, c in [(2, 0.5), (101, 0.5), (10 ** 6, 0.9), (10 ** 6, 0.99)]:
        a = 0.5 * math.log(p)
        delta = math.acosh(1 / c) / a          # |Im x| of the multiplier's zeros
        pos = min(Phi(abs(u)) + 0.5 * c * (Phi(abs(u + a)) + Phi(abs(u - a))) for u in [i / 40 for i in range(-48, 49)])
        assert pos > 0
        controls.append({'p': p, 'c': c, 'translation_a': a,
                         'offline_zero_|Im x|': delta,
                         'offline_zero_Re_s_offset': delta / 2,
                         'de_Bruijn_bound_under_RH_delta^2/2': delta * delta / 2,
                         'min_source_on_grid_|u|<=1.2': pos})
    B['B5_theta_series_evenness'] = even
    B['B5_euler_factor_controls'] = controls
    record['part_B_numerical'] = B
    record['limits'] = [
        'Part A is exact. Part B is double-precision quadrature, not interval arithmetic.',
        'B3/B4 replay an identity proved analytically in the review; agreement is evidence, not a certificate.',
        'No genuine-theta stationary sign, collision exclusion, or RH implication is established.',
    ]
    record['software'] = {'python': platform.python_version(),
                          'implementation': platform.python_implementation()}
    record['checker_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    text = json.dumps(record, indent=2, default=str) + '\n'
    if args.output:
        Path(args.output).write_text(text)
    print(text)


if __name__ == '__main__':
    main()
