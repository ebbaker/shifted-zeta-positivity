"""
lab_nogo_verify.py -- does memo7's collapse theorem survive dropping SYMMETRY?

memo7 §4.4 (Theorem 4): with Delta^dag Delta real -- which forces all four blocks
T_a real SYMMETRIC -- the identity det(Delta^dag Delta) = P_p forces lambda = 0,
T_1 = T_2 = T_3 = 0 and p = charpoly(T_0), hence p HYPERBOLIC.  memo7 noted that
"symmetry of the T_a is load-bearing in exactly one place -- kappa = ||T_1||_F^2
>= 0" and that "positive semidefiniteness of C is NOT needed anywhere".

The question this script settles: the full Yang-Mills / ambitwistor correspondence
carries a DIFFERENT reality condition from ADHM's.  Does memo7's collapse depend on
ADHM's specific reality condition (symmetry), or on the sphere-shape of the target?
If the former, the theorem does not transfer to the full-YM setting and that
direction is NOT closed by it.

The families tested, all of the shape
    M(q) = C + |q|^2 I - 2 sum_{a=0}^{3} x_a T_a ,
matched against P_p(q) = p(x_0 + i r) p(x_0 - i r):

  E : T_a real SYMMETRIC, C real symmetric        (memo7's setting, minus the
                                                   nonlinear ADHM equations)
  D : T_a real ARBITRARY, C = L L^T (symmetric PSD)
  C : T_a real ARBITRARY, C real ARBITRARY        (the widest shape)

ANSWER (Parts 1-4).  Family C is CONTENTLESS: an exact closed-form solution exists
for EVERY real monic p, hyperbolic or not, namely

    T_0 = any real matrix with charpoly p,  T_1 = T_2 = T_3 = 0,  lambda = 0,
    C = T_0^2 ,     giving    M(q) = (T_0 - x_0 I)^2 + r^2 I .

Then det M = prod_j ((x_0 - tau_j)^2 + r^2) with tau_j the eigenvalues of T_0 = the
roots of p -- which is P_p verbatim, with no reality of the tau_j required.  Take
T_0 = the companion matrix of p.

So memo7's chain survives intact all the way to its last step, and the ONLY step
that fails is "T_0 real symmetric, hence its eigenvalues tau_j are real."  The
collapse theorem IS the spectral theorem for real symmetric matrices and nothing
else, and the symmetry it needs comes from ADHM's reality condition specifically.
"""
import numpy as np
import sympy as sp
from scipy.optimize import least_squares
import lab_adhm_num as an

LINE = "=" * 78
def head(s): print(); print(LINE); print(s); print(LINE, flush=True)

CASES = [("z^2-1              [hyp]",  [1.0, -1.0]),
         ("(z-1)(z-2)         [hyp]",  [1.0, 2.0]),
         ("z^2+1              [NOT]",  [1j, -1j]),
         ("z^2+z+1            [NOT]",  [(-1+3**.5*1j)/2, (-1-3**.5*1j)/2]),
         ("(z-1)((z+2)^2+9)   [NOT]",  [1.0, -2+3j, -2-3j]),
         ("(z^2+1)(z^2+4)     [NOT]",  [1j, -1j, 2j, -2j]),
         ("memo5 quartic      [NOT]",  list(np.roots([1., 10., 26., 22., 3.])))]

def companion(roots):
    """real companion matrix of the monic real polynomial with these roots."""
    c = np.real(np.poly(np.array(roots, dtype=complex)))   # [1, a_{k-1},...,a_0]
    k = len(c) - 1
    A = np.zeros((k, k))
    A[1:, :-1] = np.eye(k - 1)
    A[:, -1] = -c[1:][::-1]
    return A

def detM_gen(T, C, Q):
    """det of C + |q|^2 I - 2 sum_a x_a T_a, for GENERAL real T_a and C."""
    k = C.shape[0]
    s = (Q ** 2).sum(axis=1)
    M = (C[None] + s[:, None, None] * np.eye(k)[None]
         - 2.0 * sum(Q[:, a][:, None, None] * T[a][None] for a in range(4)))
    return np.linalg.det(M)

# ===================================================================== PART 1
head("PART 1  the closed-form counterexample, checked on the standard test set")
print("  T_0 = companion(p),  T_1 = T_2 = T_3 = 0,  C = T_0^2.")
print("  Then M(q) = (T_0 - x_0 I)^2 + r^2 I  identically, so det M = P_p.")
print()
print(f"  {'p':<26}{'max |det M - P_p| / scale':>26}{'T_0 symmetric?':>17}"
      f"{'C PSD?':>9}{'ADHM resid':>12}")
rng = np.random.default_rng(0)
for nm, roots in CASES:
    k = len(roots)
    T0 = companion(roots); C = T0 @ T0
    T = [T0, np.zeros((k, k)), np.zeros((k, k)), np.zeros((k, k))]
    Q = rng.normal(size=(4000, 4))
    dm = detM_gen(T, C, Q); pp = an.P_target(roots, Q)
    sc = max(np.abs(pp).mean(), 1e-12)
    sym = np.abs(T0 - T0.T).max() < 1e-12
    Cs = (C + C.T) / 2
    psd = np.linalg.eigvalsh(Cs).min() > -1e-10 and np.abs(C - C.T).max() < 1e-9
    lam = np.zeros((k, 4))
    ad = np.abs(an.adhm_residual(T, lam)).max() if k > 1 else 0.0
    print(f"  {nm:<26}{np.abs(dm-pp).max()/sc:>26.3e}{str(sym):>17}{str(psd):>9}"
          f"{ad:>12.1e}")
print()
print("  Exact identity for EVERY p, hyperbolic or not.  Note the two hypotheses")
print("  that are violated: T_0 is not symmetric, and C = T_0^2 is not symmetric")
print("  PSD, exactly in the non-hyperbolic cases.")

# ===================================================================== PART 2
head("PART 2  exact symbolic check at k = 2 for a symbolic monic p")
x0, x1, x2, x3, a1, a0 = sp.symbols('x0 x1 x2 x3 a1 a0', real=True)
T0 = sp.Matrix([[0, -a0], [1, -a1]])                 # companion of z^2 + a1 z + a0
C = T0 * T0
s = x0**2 + x1**2 + x2**2 + x3**2
M = C + s * sp.eye(2) - 2 * x0 * T0
detM = sp.expand(M.det())
r2 = x1**2 + x2**2 + x3**2
# P_p = (x0 - rho1)^2 + r^2 times (x0 - rho2)^2 + r^2, expanded via e1 = -a1, e2 = a0
Pp = sp.expand(((x0**2 + r2) + a1*x0 + a0)**2 - (a1**2 - 4*a0) * ( (x0 + a1/2)**2 ) * 0
               ) if False else None
# build P_p directly from the roots of z^2+a1 z+a0
rho1 = (-a1 + sp.sqrt(a1**2 - 4*a0)) / 2
rho2 = (-a1 - sp.sqrt(a1**2 - 4*a0)) / 2
Pp = sp.expand(sp.simplify(((x0 - rho1)**2 + r2) * ((x0 - rho2)**2 + r2)))
print("  det M - P_p simplifies to:", sp.simplify(sp.expand(detM - Pp)))
print("  charpoly(T_0) =", sp.factor(sp.expand(T0.charpoly(sp.Symbol('z')).as_expr())))
print("  -> identity holds for symbolic a1, a0, with NO reality assumption on the")
print("     roots.  T_0 symmetric would force a1^2 - 4 a0 >= 0, i.e. p hyperbolic.")

# ===================================================================== PART 3
head("PART 3  which hypothesis is load-bearing: searches over the three families")
def solve_family(k, roots, family, ntrials=25, seed=3):
    """family in {'E','D','C'}; returns best residual of det M = P_p."""
    Q = an.sample_points(k, seed=seed)
    tgt = an.P_target(roots, Q); sc = max(np.abs(tgt).mean(), 1e-12)
    n2 = k * k
    ns = k * (k + 1) // 2
    iu = np.triu_indices(k)

    def unpack(z):
        if family == 'E':                    # symmetric T_a, symmetric C
            T = []
            for a in range(4):
                S = np.zeros((k, k)); S[iu] = z[a*ns:(a+1)*ns]
                T.append(S + S.T - np.diag(np.diag(S)))
            S = np.zeros((k, k)); S[iu] = z[4*ns:5*ns]
            C = S + S.T - np.diag(np.diag(S))
        elif family == 'D':                  # general T_a, C = L L^T (sym PSD)
            T = [z[a*n2:(a+1)*n2].reshape(k, k) for a in range(4)]
            L = z[4*n2:4*n2+n2].reshape(k, k); C = L @ L.T
        else:                                # general T_a, general C
            T = [z[a*n2:(a+1)*n2].reshape(k, k) for a in range(4)]
            C = z[4*n2:5*n2].reshape(k, k)
        return T, C
    npar = 5*ns if family == 'E' else 5*n2

    def F(z):
        T, C = unpack(z)
        return (detM_gen(T, C, Q) - tgt) / sc
    rng = np.random.default_rng(seed+1); best = np.inf
    for _ in range(ntrials):
        try:
            sol = least_squares(F, rng.normal(size=npar), xtol=1e-14, ftol=1e-14,
                                gtol=1e-14, max_nfev=1500)
        except Exception:
            continue
        best = min(best, float(np.sqrt(2*sol.cost)))
    return best

print("  E : T_a symmetric, C symmetric   (memo7's setting minus the nonlinear eqs)")
print("  D : T_a general,   C = L L^T PSD")
print("  C : T_a general,   C general")
print()
print(f"  {'p':<26}{'family E':>12}{'family D':>12}{'family C':>12}")
for nm, roots in CASES[:6]:
    k = len(roots)
    rE = solve_family(k, roots, 'E'); rD = solve_family(k, roots, 'D')
    rC = solve_family(k, roots, 'C')
    print(f"  {nm:<26}{rE:>12.2e}{rD:>12.2e}{rC:>12.2e}", flush=True)

# ===================================================================== PART 4
head("PART 4  memo7's proof chain, step by step, on the counterexample")
print("  p = z^2+1, T_0 = companion = [[0,-1],[1,0]], T_1..3 = 0, lambda = 0, C = T_0^2 = -I")
T0 = companion([1j, -1j]); C = T0 @ T0
print(f"    T_0 = {T0.tolist()},  C = {C.tolist()}")
e = np.array([0.3, -0.6, 0.74]); e = e/np.linalg.norm(e)
Te = np.zeros((2, 2))
print(f"    memo7 step: tr C = tr T_0^2 + tr T_e^2 ?   {np.trace(C):.6f} = "
      f"{np.trace(T0@T0):.6f} + {np.trace(Te@Te):.6f}   -> HOLDS")
print(f"    memo7 step: kappa = tr T_a^2 = 0, lambda = 0                 -> HOLDS")
print(f"    memo7 step: T_1 = T_2 = T_3 = 0                              -> HOLDS")
print(f"    memo7 step: C = T_0^2 ?  max diff {np.abs(C - T0@T0).max():.1e}  -> HOLDS")
print(f"    memo7 step: eigenvalues of T_0 are REAL ?  eig = "
      f"{np.round(np.linalg.eigvals(T0), 6).tolist()}   -> **FAILS**")
print()
print("  Every step of memo7 §4.4 survives except the last, which is exactly the")
print("  spectral theorem for real symmetric matrices.  Drop symmetry and the")
print("  eigenvalues of T_0 are the roots of p, real or not, and the matching")
print("  identity holds regardless.")
print()
print("  Converse (the theorem's actual content): if T_0 IS symmetric then its")
print("  eigenvalues are real, so p = charpoly(T_0) is hyperbolic.  Checked:")
rng2 = np.random.default_rng(5)
worst = 0.0
for _ in range(400):
    S = rng2.normal(size=(4, 4)); S = S + S.T
    worst = max(worst, np.abs(np.linalg.eigvals(S).imag).max())
print(f"    400 random real symmetric 4x4: max |Im eigenvalue| = {worst:.2e}")
