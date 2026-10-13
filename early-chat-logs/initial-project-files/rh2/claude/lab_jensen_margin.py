"""
lab_jensen_margin.py -- does Xi's position on the BOUNDARY of the hyperbolic
region have a finite-dimensional shadow?

Lambda = 0 (Newman's conjecture; Lambda >= 0 is Rodgers-Tao) says Xi sits exactly
on the boundary of the Laguerre-Polya class along the De Bruijn-Newman heat flow:
H_t is in LP for every t > 0 and not for any t < 0.  So Xi is a genuine BOUNDARY
point of LP.

But the Jensen polynomials J^{d,n} of Xi have DISTINCT real roots, so each one is
an INTERIOR point of the hyperbolic locus H_d in R^d.  The boundary-ness of Xi is
therefore invisible in any single truncation.  It must show up as d -> infinity:
the margin by which J^{d,n} is interior should degrade to 0.

This script measures that margin three ways, at fixed n as d grows:

  (1) min_x L_1(J)/scale   -- the Laguerre margin used in memo10, on roots
                              normalised to max modulus 1
  (2) min normalised root gap  -- min_j (rho_{j+1}-rho_j) / (rho_max - rho_min)
  (3) the same two quantities for a CONTROL: the Hermite polynomial of the same
      degree, whose roots are the d -> infinity attractor of J^{d,n} as n -> inf
      (Griffin-Ono-Rolen-Zagier).  If Xi's truncations degrade FASTER than the
      Hermite control, that is the finite-dimensional shadow of Lambda = 0.
"""
from math import comb, factorial as ifact
import numpy as np
from mpmath import mp, mpf, quad, exp, pi, polyroots, factorial

mp.dps = 60
LINE = "=" * 78
def head(s): print(); print(LINE); print(s); print(LINE, flush=True)

def Phi(u):
    s = mpf(0); n = 1
    while n <= 80:
        t = (2*pi**2*n**4*exp(mpf(9)*u/2) - 3*pi*n**2*exp(mpf(5)*u/2)) * \
            exp(-pi*n**2*exp(2*u))
        s += t
        if n > 3 and abs(t) < mpf(10)**(-mp.dps-5): break
        n += 1
    return s

NM = 40
print(f"  computing moments M_0..M_{2*(NM-1)} at {mp.dps} digits ...", flush=True)
M = [quad(lambda u: Phi(u)*u**k, [0, 4]) for k in range(0, 2*NM, 2)]
b = [4*M[m]/factorial(2*m) for m in range(NM)]
gam = [factorial(m)*b[m] for m in range(NM)]
print(f"  4*M_0 = {mp.nstr(4*M[0],12)}  vs xi(1/2) = 0.4971207174   "
      f"all b_m > 0: {all(x > 0 for x in b)}", flush=True)

def jensen_roots(d, n):
    c = [comb(d, j)*gam[n+j] for j in range(d+1)]       # ascending
    return polyroots(list(reversed(c)), maxsteps=800, extraprec=1200)

def L1_margin(roots):
    """min over R of f'^2 - f f'' for monic f with these roots, roots scaled to
    max modulus 1; returned relative to the mean |f|^2 scale."""
    r = np.array([complex(x) for x in roots])
    r = r / np.abs(r).max()
    c = np.real(np.poly(r))
    d1 = np.polyder(c); d2 = np.polyder(d1)
    L = np.polysub(np.polymul(d1, d1), np.polymul(c, d2))
    xs = np.linspace(-3, 3, 400001)
    cr = np.roots(np.polyder(L)) if len(L) > 2 else np.array([])
    cr = cr[np.abs(cr.imag) < 1e-9].real
    X = np.concatenate([xs, cr]) if cr.size else xs
    v = np.polyval(L, X)
    sc = np.abs(np.polyval(c, X)).max()**2
    return float(v.min()/max(sc, 1e-300))

def gap(roots):
    r = np.sort(np.array([complex(x).real for x in roots]))
    if len(r) < 2: return np.nan
    return float(np.min(np.diff(r))/(r[-1]-r[0]))

def hermite_roots(d):
    """roots of the degree-d Hermite polynomial H_d (physicists')."""
    c = np.zeros(d+1); c[-1] = 1.0
    return np.polynomial.hermite.hermroots(c[: d+1][::-1][::-1]) if False else \
           np.polynomial.hermite.hermroots(np.eye(d+1)[d])

head("PART 1  the margin of J^{d,n} as d grows, at fixed n")
print(f"  {'d':>3}{'n':>3}{'nonreal roots':>14}{'min root gap (norm)':>21}"
      f"{'L1 margin':>14}{'Hermite gap':>13}{'Hermite L1':>13}")
for n in (0, 1):
    for d in range(2, 15):
        if n + d >= NM: break
        try:
            rts = jensen_roots(d, n)
        except Exception as e:
            print(f"  {d:>3}{n:>3}   (rootfinder failed: {e})"); continue
        nre = sum(1 for x in rts if abs(mp.im(x)) > mpf('1e-30')*abs(x))
        hr = hermite_roots(d)
        print(f"  {d:>3}{n:>3}{nre:>14}{gap(rts):>21.6e}{L1_margin(rts):>14.3e}"
              f"{gap(hr):>13.6e}{L1_margin(hr):>13.3e}", flush=True)
    print()
print("  Reading: if Xi's truncations were 'barely' hyperbolic in a way the")
print("  Hermite attractor is not, the two margin columns would separate.")
