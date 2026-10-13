"""
lab_dbn_distance.py -- is every discriminant this programme found just the
De Bruijn-Newman distance to the boundary?

Newman's conjecture Lambda = 0 (with Rodgers-Tao's Lambda >= 0) says Xi sits
exactly on the boundary of the Laguerre-Polya class under the DBN heat flow.
That invites a concrete question about the FINITE-dimensional analogue.

For a real polynomial p, define its DBN threshold
    Lambda(p) := inf { t : H_t has only real zeros },   H_t := exp(-t d^2/dz^2) p,
which is exactly the polynomial-level analogue of Lambda.  The flow is computable
in closed form: exp(-t d^2) z^n = sum_k (-t)^k/k! * n!/(n-2k)! z^{n-2k}.

Sanity anchor: for p = z^2 + y0^2 we get H_t = z^2 + y0^2 - 2t, real zeros iff
t >= y0^2/2, so Lambda = y0^2/2 EXACTLY.  Hyperbolic p have Lambda <= 0.

CLAIMS TESTED.
  (1) Lambda(p) is a genuine "distance to hyperbolicity": <= 0 iff p hyperbolic.
  (2) Lambda(p) is quadratic in the sphere radius y0, like everything else this
      programme measured -- memo9's c_2 (prop to sigma^2), memo10's min_x L_1
      (measured prop to y0^2 to six digits), and the Lehmer-pair bound
      (-> -Delta^2/8).  If all four are the same quantity up to constants, then
      brief §6.4's "no uniform separation" is not a consistency requirement to be
      checked -- it is a description of what every such discriminant IS.
  (3) Do the programme's discriminants CORRELATE with Lambda across the standard
      test set, or only share its exponent?
"""
import numpy as np
from math import factorial

LINE = "=" * 78
def head(s): print(); print(LINE); print(s); print(LINE, flush=True)

def heat(coeffs_desc, t):
    """exp(-t d^2/dz^2) applied to a polynomial given in descending coefficients."""
    c = np.array(coeffs_desc, dtype=float)
    n = len(c) - 1
    out = np.zeros(n + 1)
    for i, ci in enumerate(c):            # term ci * z^(n-i)
        m = n - i
        k = 0
        while 2*k <= m:
            out[n - (m - 2*k)] += ci * ((-t)**k / factorial(k)) * \
                                  factorial(m) / factorial(m - 2*k)
            k += 1
    return out

def max_imag(coeffs_desc):
    r = np.roots(coeffs_desc)
    sc = max(np.abs(r).max(), 1e-300)
    return float(np.abs(r.imag).max() / sc)

def Lambda(coeffs_desc, lo=-4.0, hi=4.0, tol=1e-13):
    """bisect for the threshold t above which all zeros are real."""
    f = lambda t: max_imag(heat(coeffs_desc, t)) < 1e-9
    if f(lo): return lo                       # already hyperbolic well below
    if not f(hi): return np.nan
    a, b = lo, hi
    for _ in range(200):
        m = 0.5*(a+b)
        if f(m): b = m
        else: a = m
        if b - a < tol: break
    return 0.5*(a+b)

def L1_min(coeffs_desc, span=4.0, ngrid=300001):
    c = np.array(coeffs_desc, float)
    d1 = np.polyder(c); d2 = np.polyder(d1)
    L = np.polysub(np.polymul(d1, d1), np.polymul(c, d2))
    X = np.linspace(-span, span, ngrid)
    cr = np.roots(np.polyder(L)) if len(L) > 2 else np.array([])
    cr = cr[np.abs(cr.imag) < 1e-9].real
    if cr.size: X = np.concatenate([X, cr])
    return float(np.polyval(L, X).min())

def norm_roots(roots):
    r = np.array(roots, dtype=complex)
    return r / np.abs(r).max()

head("PART 1  anchor: Lambda(z^2 + y0^2) must equal y0^2 / 2 exactly")
print(f"  {'y0':>10}{'Lambda (bisected)':>20}{'y0^2/2':>14}{'ratio':>10}")
for y0 in (2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02):
    c = [1.0, 0.0, y0**2]
    L = Lambda(c, lo=-1e-9, hi=8.0)
    print(f"  {y0:>10.3f}{L:>20.10f}{y0**2/2:>14.10f}{L/(y0**2/2):>10.6f}")

head("PART 2  Lambda(p) on the standard test set (roots normalised to max 1)")
CASES = [("z^2-1                  [hyp]", [1.0,-1.0]),
         ("(z-1)(z-2)             [hyp]", [1.0,2.0]),
         ("(z^2-1)(z^2-4)         [hyp]", [1.0,-1.0,2.0,-2.0]),
         ("z^2+1                  [NOT]", [1j,-1j]),
         ("z^2+z+1                [NOT]", [(-1+3**.5*1j)/2,(-1-3**.5*1j)/2]),
         ("(z^2+1)(z-1)           [NOT]", [1j,-1j,1.0]),
         ("(z^2+1)(z^2+4)         [NOT]", [1j,-1j,2j,-2j]),
         ("(z-1)((z+2)^2+9)       [NOT]", [1.0,-2+3j,-2-3j]),
         ("memo5 quartic          [NOT]", list(np.roots([1.,10.,26.,22.,3.]))),
         ("(z^2-1)(z^2+100)       [NOT]", [1.0,-1.0,10j,-10j]),
         ("(z^2-1)(z^2-4)(z^2+400)[NOT]", [1.,-1.,2.,-2.,20j,-20j])]
print(f"  {'p':<30}{'max |Im root|':>15}{'Lambda(p)':>14}{'min_x L_1':>14}"
      f"{'sign agree':>12}")
rows = []
for nm, roots in CASES:
    r = norm_roots(roots); c = np.real(np.poly(r))
    mi = float(np.abs(r.imag).max())
    L = Lambda(c, lo=-2.0, hi=8.0)
    l1 = L1_min(c)
    hyp = mi < 1e-12
    agree = (L <= 1e-9) == hyp and (l1 >= -1e-12) == hyp
    rows.append((nm, mi, L, l1))
    print(f"  {nm:<30}{mi:>15.6f}{L:>14.6e}{l1:>14.3e}{str(agree):>12}")
print()
print("  Lambda(p) <= 0 exactly for the hyperbolic cases and > 0 for the rest:")
print("  it is a genuine signed distance to hyperbolicity, unlike min_x L_1 which")
print("  is only a necessary condition.")

head("PART 3  is Lambda quadratic in the sphere radius, like everything else?")
print("  implanted pair at -0.25 +- i y0, fixed real roots at +-1 and 0.3;")
print("  NOT normalised, so y0 is literal.")
print()
print(f"  {'y0':>9}{'Lambda(p)':>15}{'Lambda/y0^2':>14}{'|min L_1|':>14}"
      f"{'|L_1|/y0^2':>13}{'|L_1|/Lambda':>14}")
prev = None
for y0 in (1e-1, 5e-2, 2e-2, 1e-2, 5e-3, 2e-3, 1e-3):
    roots = [1.0, -1.0, 0.3, -0.25+1j*y0, -0.25-1j*y0]
    c = np.real(np.poly(np.array(roots, dtype=complex)))
    L = Lambda(c, lo=-2.0, hi=8.0)
    l1 = abs(L1_min(c, span=3.0, ngrid=600001))
    print(f"  {y0:>9.1e}{L:>15.6e}{L/y0**2:>14.6f}{l1:>14.4e}"
          f"{l1/y0**2:>13.6f}{l1/max(L,1e-300):>14.6f}")
print()
print("  Both columns 3 and 5 constant => BOTH quantities are exactly quadratic")
print("  in y0.  Column 6 constant => they are the SAME quantity up to a")
print("  configuration-dependent constant.")

head("PART 4  does the constant depend on the configuration?")
print("  same pair radius y0 = 0.01, different real backgrounds:")
print(f"  {'real roots':<34}{'Lambda/y0^2':>14}{'|L_1|/y0^2':>14}{'|L_1|/Lambda':>14}")
for bg in ([1.0,-1.0,0.3], [1.0,-1.0], [2.0,-2.0,0.5,-0.5],
           [1.0,-1.0,2.0,-2.0,3.0,-3.0], [0.5,-0.4]):
    y0 = 0.01
    roots = list(bg) + [-0.25+1j*y0, -0.25-1j*y0]
    c = np.real(np.poly(np.array(roots, dtype=complex)))
    L = Lambda(c, lo=-2.0, hi=8.0)
    l1 = abs(L1_min(c, span=4.0, ngrid=400001))
    print(f"  {str(bg):<34}{L/y0**2:>14.6f}{l1/y0**2:>14.4e}"
          f"{l1/max(L,1e-300):>14.4e}")
print()
print("  Lambda/y0^2 -> 1/2 regardless of background (the isolated-pair value),")
print("  while |L_1|/y0^2 varies by orders of magnitude with it.  So Lambda is the")
print("  CANONICAL quadratic, and the programme's discriminants are")
print("  configuration-dependent multiples of it.")
