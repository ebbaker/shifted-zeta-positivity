"""
lab_laguerre_grade.py -- running twistor_lift_computation.md §5a / §7 step 1.

twistor_lift §5a proposes the "graded Laguerre hierarchy" as the recommended
spearhead: the sigma-type invariant of §3, crystallised into analysis.  Its two
ingredients:

  (a) the CLASSICAL certificate.  For real entire f of genus <= 1,
          -(log f)''(x) = sum_rho 1/(x-rho)^2 ,   x real,
      in which a real zero contributes (x-rho)^{-2} > 0 while a conjugate pair
      z_0 = a +- i y_0 contributes 2 Re (x-z_0)^{-2}, NEGATIVE for |x-a| < y_0.
      Spheres, and only spheres, push the expression down.  Positivity for all
      real x is the Laguerre inequality L_1 = f'^2 - f f'' >= 0.

  (b) the GRADED family.  The generalised Laguerre expressions
          L_n(f)(x) = sum_{j=0}^{2n} (-1)^{n+j} f^(j)(x) f^(2n-j)(x) / (j!(2n-j)!)
      (so L_1 = f'^2 - f f''), whose non-negativity for all n and all real x
      characterises the Laguerre-Polya class (Csordas-Varga line of work --
      INHERITED, not verified here).  And the closely related moment family
          P_m(x) = sum_rho (x - rho)^{-2m} ,      m = 1, 2, 3, ...
      which is the transparent "sphere-graded" version: a real zero contributes
      |x-rho|^{-2m} > 0 always, while a pair at angle phi = arg(x - z_0)
      contributes 2 |x-z_0|^{-2m} cos(2 m phi), which OSCILLATES in m.

This has never been run.  brief §9.2 requires any new discriminant to be run
against the standard test set, so that is what happens here, plus a set of
deliberately HARD non-hyperbolic cases designed to defeat the family.

QUESTIONS.
  Q1  Does L_1 detect the memo-5 quartic, which passes Newton/first-Turan?
  Q2  Is the graded family COMPLETE, i.e. does some n (or some m) detect every
      non-hyperbolic case?
  Q3  If not, what defeats it, and does that tell us what the right object is?
"""
import numpy as np
from math import comb, factorial

LINE = "=" * 78
def head(s): print(); print(LINE); print(s); print(LINE, flush=True)


# ------------------------------------------------------------------ machinery
def normalise(roots):
    """divide all roots by the largest modulus (a dilation of q; brief §9.1)."""
    r = np.array(roots, dtype=complex)
    return r / np.abs(r).max()


def poly_from_roots(roots):
    return np.real(np.poly(np.array(roots, dtype=complex)))


def L_n(coeffs, n):
    """generalised Laguerre expression, as a polynomial (descending coeffs)."""
    ders = [coeffs]
    for _ in range(2 * n):
        ders.append(np.polyder(ders[-1]) if len(ders[-1]) > 1 else np.array([0.0]))
    out = np.array([0.0])
    for j in range(2 * n + 1):
        term = np.polymul(ders[j], ders[2 * n - j]) * ((-1) ** (n + j) /
               (factorial(j) * factorial(2 * n - j)))
        out = np.polyadd(out, term)
    return out


def poly_min_real(p, span=4.0, ngrid=200001):
    """min over R of a real polynomial: grid + critical points + behaviour at inf."""
    p = np.trim_zeros(np.asarray(p, dtype=float), 'f')
    if p.size == 0:
        return 0.0, False
    if p.size == 1:
        return float(p[0]), False
    deg = p.size - 1
    unbounded = (deg % 2 == 1) or (p[0] < 0)
    xs = [np.linspace(-span, span, ngrid)]
    dp = np.polyder(p)
    if dp.size > 1:
        cr = np.roots(dp)
        cr = cr[np.abs(cr.imag) < 1e-9].real
        if cr.size:
            xs.append(cr)
    X = np.concatenate(xs)
    return float(np.polyval(p, X).min()), unbounded


def P_m_min(roots, m, span=4.0, ngrid=400001, eps=1e-6):
    """min over R of P_m(x) = sum_rho (x-rho)^{-2m}, away from real zeros."""
    r = np.array(roots, dtype=complex)
    X = np.linspace(-span, span, ngrid)
    real_r = r[np.abs(r.imag) < 1e-12].real
    keep = np.ones_like(X, dtype=bool)
    for rr in real_r:
        keep &= np.abs(X - rr) > eps
    X = X[keep]
    V = np.zeros_like(X)
    for rho in r:
        V = V + np.real((X - rho) ** (-2 * m))
    return float(V.min()), float(X[np.argmin(V)])


def turan(roots):
    """first Newton/Turan quantity sum rho^2 = e_1^2 - 2 e_2."""
    r = np.array(roots, dtype=complex)
    return float(np.real(np.sum(r ** 2)))


# ------------------------------------------------------------------ test sets
def jensen_gammas(NM=14, dps=40):
    from mpmath import mp, mpf, quad, exp, pi, factorial as mpfact
    mp.dps = dps

    def Phi(u):
        s = mpf(0); n = 1
        while n <= 60:
            t = (2*pi**2*n**4*exp(mpf(9)*u/2) - 3*pi*n**2*exp(mpf(5)*u/2)) * \
                exp(-pi*n**2*exp(2*u))
            s += t
            if n > 3 and abs(t) < mpf(10)**(-dps-5):
                break
            n += 1
        return s
    M = [quad(lambda u: Phi(u)*u**k, [0, 4]) for k in range(0, 2*NM, 2)]
    b = [4*M[m]/mpfact(2*m) for m in range(NM)]
    return [float(mpfact(m)*b[m]) for m in range(NM)], float(4*M[0])


HYP = [("z^2-1",                 [1.0, -1.0]),
       ("(z-1)(z-2)",            [1.0, 2.0]),
       ("(z-1)(z-2)(z-3)",       [1.0, 2.0, 3.0]),
       ("(z^2-1)(z^2-4)",        [1.0, -1.0, 2.0, -2.0]),
       ("(z-1)^2(z+3)",          [1.0, 1.0, -3.0])]

NONHYP = [("z^2+1",              [1j, -1j]),
          ("z^2+z+1",            [(-1+3**.5*1j)/2, (-1-3**.5*1j)/2]),
          ("(z^2+1)(z-1)",       [1j, -1j, 1.0]),
          ("(z^2+1)(z^2-1)",     [1j, -1j, 1.0, -1.0]),
          ("(z^2+1)(z^2+4)",     [1j, -1j, 2j, -2j]),
          ("(z-1)((z+2)^2+9)",   [1.0, -2+3j, -2-3j]),
          ("memo5 quartic",      list(np.roots([1., 10., 26., 22., 3.])))]

# deliberately hard: a conjugate pair SHIELDED by real zeros, i.e. no real point
# is nearer to the pair than to some real zero.
HARD = [("(z^2-1)(z^2+100)          [pair at +-10i, shielded by +-1]",
         [1.0, -1.0, 10j, -10j]),
        ("(z^2-1)(z^2-4)(z^2+400)   [pair at +-20i, shielded]",
         [1.0, -1.0, 2.0, -2.0, 20j, -20j]),
        ("(z^2-1)(z^2-4)(z^2-9)(z^2+2500) [pair at +-50i, shielded]",
         [1.0, -1.0, 2.0, -2.0, 3.0, -3.0, 50j, -50j]),
        ("(z-1)(z+1)((z-0.5)^2+64)  [asymmetric shielded pair]",
         [1.0, -1.0, 0.5+8j, 0.5-8j])]


def report(title, cases, nmax=6, mmax=8):
    head(title)
    print(f"  {'p':<52}{'Turan':>10}{'first n: L_n<0':>16}{'first m: P_m<0':>16}")
    for nm, roots in cases:
        r = normalise(roots)
        c = poly_from_roots(r)
        deg = len(r)
        firstL = None
        for n in range(1, min(nmax, deg) + 1):
            v, unb = poly_min_real(L_n(c, n))
            if v < -1e-9 * max(1.0, abs(v)) or unb:
                firstL = n; break
        firstP = None
        for m in range(1, mmax + 1):
            v, _ = P_m_min(r, m)
            if v < -1e-9:
                firstP = m; break
        print(f"  {nm:<52}{turan(r):>10.4f}"
              f"{(str(firstL) if firstL else 'none <= %d' % min(nmax,deg)):>16}"
              f"{(str(firstP) if firstP else 'none <= %d' % mmax):>16}", flush=True)


report("PART 1  hyperbolic controls (must show NO detection at any n, m)", HYP)
report("PART 2  standard non-hyperbolic set (brief §9.2)", NONHYP)
report("PART 3  HARD cases: conjugate pairs shielded by real zeros", HARD)


head("PART 4  detail on the memo-5 quartic and on the shielded cases")
for nm, roots in [("memo5 quartic", list(np.roots([1., 10., 26., 22., 3.]))),
                  ("(z^2-1)(z^2+100)", [1.0, -1.0, 10j, -10j]),
                  ("(z^2-1)(z^2-4)(z^2+400)", [1.0, -1.0, 2.0, -2.0, 20j, -20j])]:
    r = normalise(roots); c = poly_from_roots(r)
    print(f"  {nm}   normalised roots {np.round(r, 6)}")
    print(f"    {'n':>3} {'min_x L_n':>16}   |   {'m':>3} {'min_x P_m':>16} {'argmin':>10}")
    for k in range(1, min(6, len(r)) + 1):
        v, unb = poly_min_real(L_n(c, k))
        pv, px = P_m_min(r, k)
        print(f"    {k:>3} {v:>16.6e}{' (unbdd)' if unb else '        '}"
              f"   |   {k:>3} {pv:>16.6e} {px:>10.4f}")
    print()


head("PART 5  why shielding defeats a POINTWISE graded family")
print("""  P_m(x) is dominated, as m -> infinity, by whichever zero is NEAREST to x:
      P_m(x) ~ 2 |x - z_0|^{-2m} cos(2 m phi)   if the nearest zero is a pair at
      angle phi = arg(x - z_0), and  ~ |x - rho|^{-2m} > 0 if it is real.
  So the graded family detects a conjugate pair as soon as that pair is strictly
  nearer to SOME real point than every other zero -- then cos(2 m phi) < 0 for
  infinitely many m and P_m(x) < 0.  A pair a +- i y_0 is nearest at x = a iff
  y_0 < dist(a, other zeros).  If every pair is SHIELDED -- some other zero
  always closer -- the leading term is positive for every real x and every m, and
  the whole pointwise family is blind.  Measured below: the shielding margin.""")
print()
print(f"  {'p':<40}{'y_0':>8}{'nearest other zero to a':>26}{'shielded':>10}")
for nm, roots in HARD:
    r = np.array(roots, dtype=complex)
    for z in r[r.imag > 1e-12]:
        a, y0 = z.real, z.imag
        others = r[np.abs(r - z) > 1e-12]
        others = others[np.abs(others - np.conj(z)) > 1e-12]
        d = np.abs(others - a).min() if others.size else np.inf
        print(f"  {nm.split('[')[0].strip():<40}{y0:>8.2f}{d:>26.4f}{str(y0 > d):>10}")


head("PART 6  control: Jensen polynomials of Xi (must pass everything)")
try:
    gam, m0 = jensen_gammas(NM=12)
    print(f"  moments check: 4*M_0 = {m0:.10f}  vs  xi(1/2) = 0.4971207174")
    for d in (2, 3, 4, 5, 6):
        for nn in (0, 1):
            coeffs_asc = [comb(d, j) * gam[nn + j] for j in range(d + 1)]
            rts = np.roots(list(reversed(coeffs_asc)))
            r = normalise(rts); c = poly_from_roots(r)
            firstL = None
            for k in range(1, min(6, d) + 1):
                v, unb = poly_min_real(L_n(c, k))
                if v < -1e-9 * max(1.0, abs(v)) or unb:
                    firstL = k; break
            firstP = None
            for k in range(1, 9):
                v, _ = P_m_min(r, k)
                if v < -1e-9:
                    firstP = k; break
            nre = int(np.sum(np.abs(rts.imag) > 1e-12 * np.abs(rts).max()))
            print(f"  J^{{{d},{nn}}}: nonreal roots {nre};  first n with L_n<0: "
                  f"{firstL if firstL else 'none'};  first m with P_m<0: "
                  f"{firstP if firstP else 'none'}", flush=True)
except Exception as e:
    print("  (Jensen control skipped:", e, ")")
