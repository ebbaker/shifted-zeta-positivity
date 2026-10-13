"""
lab_jet_scope.py -- does the 2-jet along a slice "see" the zeros?

The objection: memo9's theorem says the SECOND transverse jet along a slice
Pi_e forces hyperbolicity.  But a jet is infinitesimal.  How can it constrain
zeros far from the slice, which lie outside every neighbourhood it sees?

The objection is well founded, and the answer is that the theorem does NOT
detect zeros.  It forces a PARAMETER, and the parameter implies hyperbolicity by
algebra.  Two things are demonstrated here.

  (A) Inside the R1 family, the 2-jet forces S = 0, and S = 0 => T_0 real
      symmetric => spectrum real => p hyperbolic.  The conclusion travels from
      the jet to the zeros through the SPECTRAL THEOREM, not through any
      statement about a neighbourhood.  So the theorem is a RIGIDITY statement
      about a finite-dimensional polynomial family, not a detection statement.

  (B) One step outside that family the whole thing evaporates -- and not just at
      order 2.  memo12's datum (T_0 = companion matrix of p, T_1=T_2=T_3=0,
      lambda = 0, C = T_0^2) has deficit det M - P_p IDENTICALLY ZERO on all of
      H, hence vanishing jets of EVERY order at EVERY point, for p NON-hyperbolic.
      So even the full global matching condition fails to force hyperbolicity
      once ADHM's reality condition (block symmetry) is dropped.

Conclusion: the order-2 threshold is a fact about the R1 family's rigidity.  It
does not say, and cannot say, that infinitesimal data detects hyperbolicity in
general.  memo9 §5's screen ("any object must place its discriminant at order
>= 2") is therefore overclaimed and is family-specific.
"""
import numpy as np
import lab_adhm_num as an

LINE = "=" * 78
def head(s): print(); print(LINE); print(s); print(LINE, flush=True)

def frame(e):
    a = np.eye(3)[np.argmin(np.abs(e))]
    n1 = a - (a @ e) * e; n1 /= np.linalg.norm(n1)
    n2 = np.cross(e, n1); n2 /= np.linalg.norm(n2)
    return n1, n2

E = np.array([0.3, -0.6, 0.74]); E = E / np.linalg.norm(E)
N1, N2 = frame(E)

def companion(roots):
    c = np.real(np.poly(np.array(roots, dtype=complex))); k = len(c) - 1
    A = np.zeros((k, k)); A[1:, :-1] = np.eye(k - 1); A[:, -1] = -c[1:][::-1]
    return A

def build_R1(roots, e):
    r = np.array(roots, dtype=complex)
    return [np.diag(r.real)] + [e[a] * np.diag(r.imag) for a in range(3)]

def detM_gen(T, C, Q):
    k = C.shape[0]; s = (Q ** 2).sum(axis=1)
    M = (C[None] + s[:, None, None] * np.eye(k)[None]
         - 2.0 * sum(Q[:, a][:, None, None] * T[a][None] for a in range(4)))
    return np.linalg.det(M)

def jets(T, C, roots, x0, t, hs=(1e-2, 1e-3)):
    """value, first and second transverse derivatives of the deficit at a slice
    point, by central differences in the transverse direction n1."""
    def val(nu):
        Q = np.zeros((1, 4)); Q[0, 0] = x0; Q[0, 1:] = t * E + nu * N1
        return float(detM_gen(T, C, Q)[0] - an.P_target(roots, Q)[0])
    out = []
    for h in hs:
        v0, vp, vm = val(0.0), val(h), val(-h)
        out.append((v0, (vp - vm) / (2 * h), (vp - 2 * v0 + vm) / h ** 2))
    return out

CASES = [("z^2-1        [hyperbolic]", [1.0, -1.0]),
         ("z^2+1        [NOT hyp]  ", [1j, -1j]),
         ("z^2+z+1      [NOT hyp]  ", [(-1 + 3 ** .5 * 1j) / 2, (-1 - 3 ** .5 * 1j) / 2]),
         ("memo5 quartic[NOT hyp]  ", list(np.roots([1., 10., 26., 22., 3.])))]

head("(A)  INSIDE the R1 family: the 2-jet is nonzero exactly when p is not hyperbolic")
print("  slice point x_0 = 0.37, t = 0.83.  Deficit jets (value, d/dnu, d2/dnu2).")
print()
print(f"  {'p':<26}{'value':>12}{'1st deriv':>12}{'2nd deriv':>14}{'S = 0?':>9}")
for nm, roots in CASES:
    T = build_R1(roots, E); C = an.Cmat(T, np.zeros((len(roots), 4)))
    (v0, d1, d2), _ = jets(T, C, roots, 0.37, 0.83)
    S = sum(E[a] * T[a + 1] for a in range(3))
    print(f"  {nm:<26}{v0:>12.2e}{d1:>12.2e}{d2:>14.6f}"
          f"{str(np.abs(S).max() < 1e-12):>9}")
print()
print("  The 2nd derivative is the ONLY nonzero entry, and it is nonzero exactly")
print("  for the non-hyperbolic p.  But note what the theorem then does with it:")
print("    2nd deriv = 0  =>  S = 0  =>  T_0 real symmetric  =>  spectrum real")
print("                   =>  p hyperbolic.")
print("  The last three arrows are ALGEBRA (the spectral theorem).  Nothing in the")
print("  chain is a statement about zeros in a neighbourhood of the slice.")

head("(B)  ONE STEP OUTSIDE the family: ALL jets vanish, and p is NOT hyperbolic")
print("  memo12's datum: T_0 = companion(p) (NOT symmetric), T_1=T_2=T_3=0,")
print("  lambda = 0, C = T_0^2.  Then M(q) = (T_0 - x_0 I)^2 + r^2 I identically.")
print()
print(f"  {'p':<26}{'value':>12}{'1st deriv':>12}{'2nd deriv':>12}"
      f"{'global sup|deficit|':>21}")
rng = np.random.default_rng(0)
for nm, roots in CASES:
    T0 = companion(roots); C = T0 @ T0
    k = len(roots)
    T = [T0, np.zeros((k, k)), np.zeros((k, k)), np.zeros((k, k))]
    (v0, d1, d2), _ = jets(T, C, roots, 0.37, 0.83)
    Q = rng.normal(size=(4000, 4))
    g = np.abs(detM_gen(T, C, Q) - an.P_target(roots, Q)).max() / \
        max(np.abs(an.P_target(roots, Q)).mean(), 1e-12)
    print(f"  {nm:<26}{v0:>12.2e}{d1:>12.2e}{d2:>12.2e}{g:>21.2e}")
print()
print("  Every jet vanishes -- at order 2 and at every other order -- because the")
print("  deficit is identically zero on ALL of H (last column).  And p is not")
print("  hyperbolic.  So outside the R1 family, not merely the 2-jet but the FULL")
print("  GLOBAL matching condition fails to force hyperbolicity.")

head("(C)  what this means for the 'order >= 2' screen")
print("""  The 2-jet threshold is a statement about how much data pins down the R1
  FAMILY -- a finite-dimensional family of polynomials, where local data
  determines global data cheaply.  It is not a statement that infinitesimal
  information detects hyperbolicity.

  In particular:
    * order 0 empty  -- proved for R1 (memo8); a well-supported PRINCIPLE
                        elsewhere (5 instances), not a theorem.
    * order 1 empty  -- proved for R1 only, via evenness of the deficit in nu,
                        which follows from M depending on q through (x_0,t,nu^2).
                        A general family's deficit need not be even.
    * order 2 collapse -- proved for R1 only, and (B) shows it FAILS one step
                        outside, where even all orders together do not suffice.

  So memo9 §5's "whatever object is built from Xi, the reality information must
  appear at transverse order >= 2" is OVERCLAIMED.  The defensible version is:
  within a family whose deficit depends on q only through (x_0, t, nu^2), orders
  0 and 1 are empty by evenness.  That is a statement about the family, and it
  should be checked for each new one rather than assumed.""")
