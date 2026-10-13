"""Is the finite Laguerre family {L_n}_{n=1..deg} COMPLETE for polynomials?
Adversarial search for a non-hyperbolic monic real polynomial with L_n >= 0 for
every n.  If one exists it is a new entry for the brief §9.2 test set and shows
the hierarchy is a hyperbolicity CRITERION only, not a characterisation."""
import numpy as np
from math import factorial
from scipy.optimize import minimize
exec(open('/home/claude/lab_laguerre_grade.py').read().split('# ------------------------------------------------------------------ test sets')[0].split('"""',2)[2])

LINE="="*78
def head(s): print();print(LINE);print(s);print(LINE,flush=True)

def min_over_n(roots, span=6.0, ngrid=20001):
    """min over n = 1..deg of (min over x of L_n), normalised roots."""
    c = poly_from_roots(roots); deg = len(roots)
    worst = np.inf
    for n in range(1, deg+1):
        v, unb = poly_min_real(c if False else L_n(c, n), span=span, ngrid=ngrid)
        if unb: return -np.inf, n
        if v < worst: worst, wn = v, n
    return worst, wn

head("PART 10  adversarial search: non-hyperbolic p with ALL L_n >= 0 ?")
print("  Degree 4: two real roots r1,r2 and one pair a +- i y (y > 0), normalised so")
print("  max|root| = 1.  Maximise min_n min_x L_n over the parameters.  A positive")
print("  optimum would be a counterexample to completeness.")
print()

def quartic_obj(p, sign=-1.0):
    r1, r2, a, ly = p
    y = np.exp(ly)
    roots = [r1, r2, a+1j*y, a-1j*y]
    r = normalise(roots)
    v, _ = min_over_n(r)
    return sign*v

best = (-np.inf, None)
rng = np.random.default_rng(0)
for _ in range(60):
    p0 = np.array([rng.normal(), rng.normal(), rng.normal(), rng.normal()*1.5])
    try:
        s = minimize(quartic_obj, p0, method='Nelder-Mead',
                     options=dict(maxiter=1500, fatol=1e-14, xatol=1e-12))
    except Exception:
        continue
    if -s.fun > best[0]:
        best = (-s.fun, s.x)
v, x = best
r1, r2, a, ly = x; y = np.exp(ly)
roots = normalise([r1, r2, a+1j*y, a-1j*y])
print(f"  best min_n min_x L_n over 60 starts = {v:.6e}")
print(f"    at roots {np.round(roots,6)}   (pair radius {abs(roots[2].imag):.4e})")
wv, wn = min_over_n(roots)
print(f"    worst n = {wn},  value {wv:.6e}")
print()

print("  Degree 6: four real roots and one pair.")
def sextic_obj(p, sign=-1.0):
    r = list(p[:4]); a, ly = p[4], p[5]; y = np.exp(ly)
    roots = r + [a+1j*y, a-1j*y]
    v, _ = min_over_n(normalise(roots))
    return sign*v
best6 = (-np.inf, None)
for _ in range(40):
    p0 = np.concatenate([rng.normal(size=4), [rng.normal(), rng.normal()*1.5]])
    try:
        s = minimize(sextic_obj, p0, method='Nelder-Mead',
                     options=dict(maxiter=2500, fatol=1e-14, xatol=1e-12))
    except Exception:
        continue
    if -s.fun > best6[0]:
        best6 = (-s.fun, s.x)
v6, x6 = best6
rr = list(x6[:4]); a6, ly6 = x6[4], x6[5]; y6 = np.exp(ly6)
roots6 = normalise(rr + [a6+1j*y6, a6-1j*y6])
print(f"  best min_n min_x L_n over 40 starts = {v6:.6e}")
print(f"    at roots {np.round(roots6,6)}   (pair radius {abs(roots6[4].imag):.4e})")
wv6, wn6 = min_over_n(roots6)
print(f"    worst n = {wn6},  value {wv6:.6e}")

head("PART 11  hyperbolic controls under the same objective (sanity)")
for nm, roots in [("z^2-1",[1.,-1.]),("(z^2-1)(z^2-4)",[1.,-1.,2.,-2.]),
                  ("(z-1)(z-2)(z-3)(z-4)",[1.,2.,3.,4.]),
                  ("(z^2-1)(z^2-4)(z^2-9)",[1.,-1.,2.,-2.,3.,-3.])]:
    r = normalise(roots); v, n = min_over_n(r)
    print(f"  {nm:<28} min_n min_x L_n = {v:>13.6e}   (worst n = {n})")
print()
print("  Hyperbolic p must give >= 0 (Laguerre-Polya); any negative value here")
print("  would indicate a bug rather than a discovery.")
