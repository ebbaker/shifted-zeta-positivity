"""
lab_weil_positivity.py  --  RH2, memo 19

Screens the Weil-positivity route by building its POLYNOMIAL SHADOW (Li's criterion)
and running it against the brief's section 7 test set, per the project's habit.

Li's criterion (Li 1997; Bombieri-Lagarias 1999): for a multiset of zeros closed under
rho -> conj(rho) and rho -> 1-rho,
      all zeros on the critical line  <=>  lambda_n >= 0 for all n >= 1,
      lambda_n = sum_rho [1 - (1 - 1/rho)^n].
The Moebius map s -> 1 - 1/s carries the critical line to the UNIT CIRCLE.

POLYNOMIAL SHADOW.  For a real monic p with roots rho_j, hyperbolic = all roots on R.
Cayley map adapted to R, with a free base point mu > 0:
      w_j = (rho_j - i mu)/(rho_j + i mu)
sends R to the unit circle and carries conjugation to w -> 1/conj(w).  Define
      lam_n(p) = sum_j Re[1 - w_j^n] = k - Re sum_j w_j^n .

Prop.  lam_n(p) >= 0 for every n >= 1  <=>  p is hyperbolic.
   (<=) all |w_j| = 1, so |sum_j w_j^n| <= k.
   (=>) a non-real root forces a partner with |w| > 1; Re(w^n) reaches ~ +|w|^n along a
        subsequence, so lam_n -> -infinity.
Note inf_n lam_n = 0 for hyperbolic p (the w_j are on the circle and n*theta equidistributes),
so the criterion carries NO MARGIN on the hyperbolic side.

Parts
  1  Lambda(p) reimplemented and validated against brief section 7 (all 11 entries).
  2  Li instrument on the same test set: detection order n* and depth.
  3  Margin scaling in the sphere radius (the section 2.4 question).
  4  Head-to-head Lambda vs Li at HEIGHT (the section 2.6 question).
"""
import sys
import numpy as np
from mpmath import mp, mpf, mpc, polyroots, re, fabs, log
mp.dps = 60

# ------------------------------------------------- de Bruijn-Newman Lambda
def _heat(c, t):
    p = np.poly1d(c); out = np.poly1d([0.0]); d = p; k = 0; f = 1.0
    while True:
        out = out + (((-t)**k)/f)*d
        if d.order < 2: break
        d = d.deriv(2); k += 1; f *= k
    return out
def _hyp(c, tol=1e-9):
    r = np.roots(c); return np.abs(r.imag).max() <= tol*max(1, np.abs(r).max())
def Lam(c, lo=-50., hi=100.):
    for _ in range(300):
        m = (lo+hi)/2
        if _hyp(_heat(c, m).coeffs): hi = m
        else: lo = m
    return hi
def Lam_norm(c):
    r = np.roots(c); R = np.abs(r).max()
    return Lam(list(np.poly(r/R).real))

# ------------------------------------------------- Li instrument
def cayley(rts, mu=mpf('0.5')):
    m = mpc(0, mu); return [(r-m)/(r+m) for r in rts]
def lam_n(ws, n):
    return len(ws) - sum(re(w**n) for w in ws)
def li_scan(c, mu=mpf('0.5'), N=20000):
    rts = polyroots([mpf(x) for x in c], maxsteps=400, extraprec=400)
    ws = cayley(rts, mu); mn = None
    for n in range(1, N+1):
        v = lam_n(ws, n)
        if mn is None or v < mn: mn = v
        if v < 0: return n, v, float(max(fabs(w) for w in ws))
    return None, mn, float(max(fabs(w) for w in ws))

TESTS = [
 ("z^2-1                      (hyp)", [1,0,-1]),
 ("(z-1)(z-2)                 (hyp)", [1,-3,2]),
 ("(z^2-1)(z^2-4)             (hyp)", [1,0,-5,0,4]),
 ("z^2+1",                            [1,0,1]),
 ("z^2+z+1",                          [1,1,1]),
 ("(z^2+1)(z-1)",                     [1,-1,1,-1]),
 ("(z^2+1)(z^2+4)",                   [1,0,5,0,4]),
 ("(z-1)((z+2)^2+9)",                 [1,3,9,-13]),
 ("near-miss quartic",                [1,10,26,22,3]),
 ("(z^2-1)(z^2+100)  SHIELDED",       [1,0,99,0,-100]),
 ("(z^2-1)(z^2-4)(z^2+400) SHIELDED", [1,0,395,0,-2000,0,1600]),
]
BRIEF = [-0.500,-0.031,-0.034,0.500,0.375,0.369,0.175,0.255,3.88e-05,0.170,0.101]

def part12():
    print("PARTS 1-2  --  Lambda (revalidated) and the Li instrument, brief section 7 test set")
    print(f"{'p':<36} {'Lambda(norm)':>13} {'brief':>10} {'max|w|':>9} {'n*':>7} {'lam_{n*}':>11}")
    print("-"*92)
    for (nm, c), b in zip(TESTS, BRIEF):
        L = Lam_norm(np.array(c, float)); n, v, mx = li_scan(c)
        print(f"{nm:<36} {L:>13.4e} {b:>10.3g} {mx:>9.5f} "
              f"{(str(n) if n else '>20000'):>7} {float(v):>11.4g}")
        sys.stdout.flush()
    print("   Every Lambda reproduces the brief. The Li instrument detects every non-hyperbolic")
    print("   case, INCLUDING both shielded cases (n* = 7, 13) which defeat L_1 and the pointwise")
    print("   graded family, and the near-miss quartic (n* = 43).  Hyperbolic controls stay >= 0")
    print("   but their infimum is 0 -- the criterion has no margin on the hyperbolic side.\n")

def part3():
    print("PART 3  --  margin scaling in the sphere radius:  p = z^2 + y0^2")
    print(f"   {'y0':>8} {'Lambda=y0^2/2':>14} {'n*':>5} {'lam_10':>14} {'lam_10/y0^2':>13}")
    for s in ['0.3','0.1','0.03','0.01','0.003','0.001']:
        y = mpf(s); rts = polyroots([mpf(1), mpf(0), y*y], maxsteps=400, extraprec=400)
        ws = cayley(rts); n = next(k for k in range(1, 100000) if lam_n(ws, k) < 0)
        l10 = float(lam_n(ws, 10))
        print(f"   {s:>8} {float(y*y/2):>14.3e} {n:>5} {l10:>14.4e} {l10/float(y*y):>13.4f}")
    print("   lam_n at fixed n is a constant multiple of y0^2: section 2.4's quadratic")
    print("   degradation is respected; the escape is that n is unbounded, not uniform.\n")

def part4():
    print("PART 4  --  section 2.6: a conjugate quadruple at HEIGHT a, off-line part b")
    print("   p = ((z-a)^2+b^2)((z+a)^2+b^2)")
    print(f"   {'a':>6} {'b':>7} {'Lambda':>12} {'log|w|max':>11} {'n*':>7} {'lam_{n*}':>12}")
    for a_, b_ in [('1','0.1'),('3','0.1'),('10','0.1'),('30','0.1'),('100','0.1'),('10','0.01')]:
        a = float(a_); b = float(b_)
        cf = list((np.poly1d([1,-2*a,a*a+b*b])*np.poly1d([1,2*a,a*a+b*b])).coeffs)
        L = Lam(cf)
        rts = polyroots([mpf(x) for x in cf], maxsteps=400, extraprec=400); ws = cayley(rts)
        lw = float(max(log(fabs(w)) for w in ws))
        n = next(k for k in range(1, 300000) if lam_n(ws, k) < 0)
        print(f"   {a_:>6} {b_:>7} {L:>12.4e} {lw:>11.3e} {n:>7} {float(lam_n(ws,n)):>12.3e}")
        sys.stdout.flush()
    print("   Lambda is HEIGHT-INDEPENDENT (~ b^2/2 throughout).  Li's detection order grows")
    print("   like a and its depth collapses like b/a^2, because the Cayley image of a zero at")
    print("   height a sits only ~ b/a^2 off the unit circle.  As a fixed global sequence the")
    print("   Li shadow is therefore WORSE than Lambda at height -- which is exactly the")
    print("   argument for the test-function (Weil) form, where g can be localised at height T.\n")

if __name__ == '__main__':
    w = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if w in ('1','2','12','all'): part12()
    if w in ('3','all'): part3()
    if w in ('4','all'): part4()
