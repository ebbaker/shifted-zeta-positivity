"""
lab_adhm_relax.py -- relaxing the matching condition of memo7 §4.

memo7 required the FULL four-dimensional identity det(Delta^dag Delta) = P_p,
i.e. that the real jumping locus be exactly the zero set of the slice extension
of p.  That is a strong condition.  This script asks what happens if we only
require agreement on ONE SLICE -- the natural reading of "the object restricts
to Xi on a slice".

Three relaxations are tested.

  R1 (one slice).   det(Delta^dag Delta)|_{Pi_e} = P_p|_{Pi_e} for a single
                    unit imaginary e, where Pi_e = { x_0 + y e }.
  R2 (m slices).    the same on m distinct slices.
  R3 (spectrum).    drop matching entirely; ask whether the ADHM equations
                    constrain the quaternionic right-eigenvalue classes of T,
                    which are 2-spheres unless real -- the zero-sphere
                    structure is native to quaternionic linear algebra.

RESULTS (Parts 2-5 below).

  R1 is COMPLETELY CHARACTERISED and CONTENTLESS: it forces lambda = 0,
  T_a = e_a S (a = 1,2,3) for a single real symmetric S, [T_0, S] = 0, and
  sigma-invariance of the joint spectrum (see Part 2) -- so the data is
  commutative and C_e-valued -- and then p = char poly of T_0 + i S, which
  realises EVERY real monic p of degree k, hyperbolic or not.  So relaxing to
  one slice loses all discriminating power AND still kills the noncommutativity.
  Worse on both counts than the full matching.

  R2: the threshold is ONE SLICE PLUS ONE POINT, not two slices.  Within the R1
  family there is an exact deficit formula (Part 3): with t = <Im q, e> and
  r = |Im q|,
      det M(q) = prod_j (B_j - 2 t sigma_j),   P_p(q) = prod_j (B_j - 2 r sigma_j),
      B_j = (x_0 - tau_j)^2 + r^2 + sigma_j^2,
  and Cauchy-Schwarz gives t^2 <= r^2 with equality EXACTLY on Pi_e.  Pairing
  conjugate roots makes every factor strictly decreasing in its argument, so
      det M(q) - P_p(q) > 0  for every q outside Pi_e, whenever S != 0.
  A single off-slice point therefore forces S = 0, i.e. hyperbolicity.  The
  slice is precisely the equality locus of a Cauchy-Schwarz inequality; that is
  why it is blind.

  R3: no.  Admissible ADHM data has non-real right-eigenvalue classes
  generically, so the class does not force isolated zeros.

The mechanism in one line: the whole discriminant is r^2 - t^2, the deviation of
Im q from the slice direction, weighted by the imaginary parts of the roots -- so
it is supported exactly on the 2-sphere directions transverse to any one slice,
and a one-slice condition is evaluated precisely where it vanishes.
"""
import numpy as np
import sympy as sp
from math import comb
from scipy.optimize import least_squares

import lab_adhm_num as an

LINE = "=" * 78


def head(s):
    print()
    print(LINE)
    print(s)
    print(LINE)


# --------------------------------------------------------------- helpers
def slice_points(e, k, seed=0, mult=2):
    """Random points of the slice Pi_e = {x_0 + y e}, as rows of R^4."""
    dim = comb(2 * k + 2, 2)                    # deg-2k polys in (x_0, y)
    rng = np.random.default_rng(seed)
    xy = rng.normal(size=(mult * dim, 2))
    Q = np.zeros((len(xy), 4))
    Q[:, 0] = xy[:, 0]
    for a in range(3):
        Q[:, a + 1] = xy[:, 1] * e[a]
    return Q


def multi_slice_residual(k, roots, es, seed=0, w_adhm=1.0):
    Qs = [slice_points(e, k, seed=seed + 17 * i) for i, e in enumerate(es)]
    tgts = [an.P_target(roots, Q) for Q in Qs]
    scales = [max(np.abs(t).mean(), 1e-12) for t in tgts]

    def F(z):
        T, lam = an.unpack(z, k)
        out = [w_adhm * an.adhm_residual(T, lam)]
        for Q, t, s in zip(Qs, tgts, scales):
            out.append((an.detM(T, lam, Q) - t) / s)
        return np.concatenate(out)
    return F


def search_slices(k, roots, es, ntrials=40, seed=0, scale=1.0):
    F = multi_slice_residual(k, roots, es, seed=seed)
    rng = np.random.default_rng(seed + 1)
    best, bz = np.inf, None
    for _ in range(ntrials):
        try:
            sol = least_squares(F, rng.normal(scale=scale, size=an.nparams(k)),
                                xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=900)
        except Exception:
            continue
        c = float(np.sqrt(2 * sol.cost))
        if c < best:
            best, bz = c, sol.x
    return best, bz


def chi(T):
    """Complex adjoint of a quaternionic matrix: H^{kxk} -> C^{2k x 2k}.
    a+bi+cj+dk -> [[a+bi, c+di],[-c+di, a-bi]].  Eigenvalues of chi(T) are the
    complex eigenvalues of T in conjugate pairs; those with Im >= 0 are the
    standard representatives of the right-eigenvalue classes (spheres unless
    real)."""
    A = T[0] + 1j * T[1]
    B = T[2] + 1j * T[3]
    return np.block([[A, B], [-np.conj(B), np.conj(A)]])


def eig_classes(T):
    ev = np.linalg.eigvals(chi(T))
    return np.array(sorted(ev[ev.imag >= -1e-12], key=lambda z: (z.real, z.imag)))


# ===================================================================== PART 1
head("PART 1  sanity: the complex adjoint and right-eigenvalue classes")
T1 = [np.zeros((1, 1)), np.ones((1, 1)), np.zeros((1, 1)), np.zeros((1, 1))]
print("  T = (i) as a 1x1 quaternionic matrix: eigenvalues of chi(T) =",
      np.round(np.linalg.eigvals(chi(T1)), 12),
      "-> class is the unit sphere, NOT real")
T2 = [np.diag([2.0, -3.0])] + [np.zeros((2, 2))] * 3
print("  T = diag(2,-3) real:                  classes =",
      np.round(eig_classes(T2), 12), "-> real")
# a quaternionic Hermitian matrix must have real classes (spectral theorem)
rng = np.random.default_rng(11)
worst = 0.0
for _ in range(200):
    k = 3
    H = [rng.normal(size=(k, k)) for _ in range(4)]
    H[0] = H[0] + H[0].T                     # T_0 symmetric
    for a in (1, 2, 3):
        H[a] = H[a] - H[a].T                 # T_a antisymmetric  => T^dag = T
    worst = max(worst, np.abs(eig_classes(H).imag).max())
print("  200 random quaternionic HERMITIAN 3x3 (T_0 sym, T_1..3 antisym):")
print("    max |Im| over all right-eigenvalue classes = %.2e  (spectral theorem)" % worst)


# ===================================================================== PART 2
head("PART 2  R1: what matching on ONE slice forces")

print("""  Setting.  Delta^dag Delta real gives (memo7 §2)
      M(q) = C + |q|^2 I - 2 sum_a x_a T_a ,  C = sum_a T_a^2 + Re(lam^dag lam),
  all T_a real symmetric.  Restricting to Pi_e and substituting u = x_0 + eta,
  v = x_0 - eta after y -> i.eta gives, exactly as in memo7 but for this ONE e,
      det( uv I - u N - v Nbar + C ) = p(u) p(v),      N = T_0 + i T_e .
  The u^{k-1}v^{k-1} coefficient still gives the trace relation
      tr C = tr T_0^2 + tr T_e^2 .                                   (*)

  Consequences of (*) alone.  Write g_ab = tr(T_a T_b), a,b >= 1 -- the Gram
  matrix of T_1,T_2,T_3 in the Frobenius inner product, so g >= 0.  Then
  tr T_e^2 = e^T g e and sum_{a>=1} tr T_a^2 = tr g, so (*) reads
      tr g + ||lam||^2 = e^T g e  <=  lam_max(g)  <=  tr g ,
  forcing  ||lam|| = 0,  rank g <= 1,  and e a top eigenvector: g = kappa e e^T.
  Then ||T_a - e_a T_e||^2 = kappa e_a^2 - 2 kappa e_a^2 + kappa e_a^2 = 0, i.e.
      lambda = 0    and    T_a = e_a S   for a = 1,2,3,  S := T_e .
  So T = T_0 + S e is C_e-VALUED.  The ADHM equations then read
  e_a [T_0,S] - eps_abc [e_b S, e_c S] = e_a [T_0,S] = 0, so [T_0,S] = 0.
  Finally C = T_0^2 + S^2 = Nbar N, so det M = pbar(u) p(v) on the slice, with
      p(v) = det(vI - T_0 - i S),   T_0, S commuting real symmetric.

  ONE MORE CONDITION IS NEEDED for sufficiency, and it was missing from the
  first draft of this characterisation (caught by an adversarial review): the
  identity requires pbar = p, i.e. p must have REAL coefficients.  Since T_0
  and S commute they are simultaneously orthogonally diagonalisable, with joint
  eigenvalues (tau_j, sigma_j) and p(v) = prod_j (v - tau_j - i sigma_j); so
  the extra condition is that the joint spectrum be invariant under
  sigma -> -sigma.  Equivalently tr(T_0^m S^n) = 0 for all odd n; in particular
  tr S = 0 is forced, and for k = 2 with p non-hyperbolic T_0 must be scalar.
  Counterexample to the version without it: k = 2, T_0 = 0, S = diag(1,2) meets
  every other listed condition but matches no real p at all.

  Also worth stating: lambda = 0 makes the last row of Delta vanish, so the
  matched data is not a REGULAR ADHM datum -- it sits outside the instanton
  moduli space proper.  (memo7's matched data has the same defect.  It is
  expected, since a nonempty jumping locus is exactly what we asked for, but it
  means the objects being produced are degenerate as gauge theory.)""")

print()
print("  Verifying the characterisation numerically: solve R1 and inspect the")
print("  structure of the solution (e chosen generically).")
e_gen = np.array([0.3, -0.6, 0.74])
e_gen = e_gen / np.linalg.norm(e_gen)
for k, nm, roots in [(2, "z^2-1  (hyperbolic)", [1.0, -1.0]),
                     (2, "z^2+1  (NOT hyp)   ", [1j, -1j]),
                     (3, "(z^2+1)(z-1) (NOT hyp)", [1j, -1j, 1.0])]:
    best, z = search_slices(k, roots, [e_gen], ntrials=30, seed=5)
    T, lam = an.unpack(z, k)
    S = sum(e_gen[a] * T[a + 1] for a in range(3))
    par = max(np.abs(T[a + 1] - e_gen[a] * S).max() for a in range(3))
    print(f"    k={k}  {nm:<24} residual {best:.2e}   |lam| {np.abs(lam).max():.1e}"
          f"   max|T_a - e_a S| {par:.1e}   |[T_0,S]| {np.abs(an.com(T[0], S)).max():.1e}")

print()
print("  Explicit data realising an arbitrary real monic p on one slice")
print("  (T_0 = diag of real parts, S = diag of imaginary parts, e arbitrary):")


def build_R1(roots, e):
    """T_0, S diagonal from the roots; T_a = e_a S; lam = 0."""
    r = np.array(roots, dtype=complex)
    T0 = np.diag(r.real)
    S = np.diag(r.imag)
    T = [T0] + [e[a] * S for a in range(3)]
    lam = np.zeros((len(r), 4))
    return T, lam


tests = [("z^2+1", [1j, -1j]),
         ("z^2+z+1", [(-1 + 3 ** .5 * 1j) / 2, (-1 - 3 ** .5 * 1j) / 2]),
         ("X^4+10X^3+26X^2+22X+3 [memo5]", list(np.roots([1., 10., 26., 22., 3.]))),
         ("(z^2+1)(z^2+4)", [1j, -1j, 2j, -2j])]
for nm, roots in tests:
    k = len(roots)
    T, lam = build_R1(roots, e_gen)
    Q = slice_points(e_gen, k, seed=3)
    ad = np.abs(an.adhm_residual(T, lam)).max()
    err = np.abs(an.detM(T, lam, Q) - an.P_target(roots, Q)).max() / max(
        np.abs(an.P_target(roots, Q)).mean(), 1e-12)
    hyp = all(abs(np.imag(r)) < 1e-9 for r in roots)
    print(f"    {nm:<32} hyperbolic {str(hyp):>5}   ADHM residual {ad:.1e}"
          f"   rel. slice error {err:.1e}")

print()
print("  => R1 is satisfiable for EVERY real monic p.  No discriminating power,")
print("     and the data is forced commutative and C_e-valued anyway.")


# ===================================================================== PART 3
head("PART 3  R2: the threshold is one slice plus ONE POINT")

print("""  Within the R1 family, diagonalise (T_0,S) jointly and put t = <Im q, e>,
  r = |Im q|, A_j = (x_0 - tau_j)^2, B_j = A_j + r^2 + sigma_j^2.  Then
      det M(q) = prod_j (B_j - 2 t sigma_j),     P_p(q) = prod_j (B_j - 2 r sigma_j).
  Conjugate pairing (sigma -> -sigma) turns each into a product over pairs of
      B^2 - 4 s sigma^2   with s = t^2 (left) or r^2 (right),
  and B^2 - 4 r^2 sigma^2 = (A + (r-sigma)^2)(A + (r+sigma)^2) >= 0, so every
  factor is positive and strictly decreasing in s on [0, r^2].  Cauchy-Schwarz
  gives t^2 <= r^2 with equality EXACTLY when Im q is parallel to e, i.e. on
  Pi_e.  Hence
      det M(q) - P_p(q) > 0   for every q outside Pi_e,  whenever S != 0,
  and identically 0 when S = 0.  So ONE off-slice point already forces S = 0,
  i.e. T_1 = T_2 = T_3 = 0 and p hyperbolic.  Two slices is sufficient but far
  from minimal: for e' not parallel to e, S' = (e.e') S and e_a S = (e.e') e'_a S
  force e = (e.e') e', so |e.e'| = 1 and e' = +-e, contradiction; hence S = 0.

  Two caveats.  (1) Pi_e and Pi_{e'} always meet in the real axis, so "the real
  axis of a second slice" adds nothing -- the extra point must be genuinely off
  Pi_e.  (2) The forcing is not uniform: for two slices at angle theta the best
  residual for S != 0 data scales as O(theta^2), so any APPROXIMATE two-slice
  condition with tolerance eps admits non-hyperbolic p once eps >~ theta^2.""")
print()
e2 = np.array([0.8, 0.1, -0.59])
e2 = e2 / np.linalg.norm(e2)
e_orth = np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0])
configs = [("1 slice            ", [e_gen]),
           ("2 slices (generic) ", [e_gen, e2]),
           ("2 slices (orthog.) ", [e_orth[0], e_orth[1]]),
           ("3 slices (i, j, k) ", [np.eye(3)[0], np.eye(3)[1], np.eye(3)[2]])]
print(f"  {'configuration':<20} {'p = z^2+1 (NOT hyp)':>22} {'p = z^2-1 (hyp)':>18}")
for nm, es in configs:
    b_bad, _ = search_slices(2, [1j, -1j], es, ntrials=30, seed=7)
    b_ok, _ = search_slices(2, [1.0, -1.0], es, ntrials=30, seed=7)
    print(f"  {nm:<20} {b_bad:>22.2e} {b_ok:>18.2e}")

# --- one slice plus a single off-slice point -------------------------------
k = 2
Q1 = slice_points(e_gen, k, seed=3)
q0 = np.array([[0.4, 0.0, 0.0, 0.9]])          # generic, not in Pi_e
for nm, roots in [("z^2+1 (NOT hyp)", [1j, -1j]), ("z^2-1 (hyp)    ", [1.0, -1.0])]:
    t1, t0 = an.P_target(roots, Q1), an.P_target(roots, q0)

    def F(z, t1=t1, t0=t0):
        T, lam = an.unpack(z, k)
        return np.concatenate([an.adhm_residual(T, lam),
                               (an.detM(T, lam, Q1) - t1) / max(abs(t1).mean(), 1e-12),
                               (an.detM(T, lam, q0) - t0) / max(abs(t0).mean(), 1e-12)])
    rng2 = np.random.default_rng(1)
    best = np.inf
    for _ in range(40):
        s = least_squares(F, rng2.normal(size=an.nparams(k)), xtol=1e-14,
                          ftol=1e-14, gtol=1e-14, max_nfev=900)
        best = min(best, float(np.sqrt(2 * s.cost)))
    print(f"  1 slice + 1 point    p = {nm}   best residual {best:.2e}")

# --- the deficit formula, verified ----------------------------------------
print()
print("  the deficit formula, checked on 4000 random points of H:")
rng3 = np.random.default_rng(0)
for nm, roots in [("z^2+1", [1j, -1j]),
                  ("(z-1)((z+2)^2+9)", [1.0, -2 + 3j, -2 - 3j]),
                  ("X^4+10X^3+26X^2+22X+3 [memo5]", list(np.roots([1., 10., 26., 22., 3.]))),
                  ("(z-1)(z-2)  [hyperbolic]", [1.0, 2.0])]:
    T, lam = build_R1(roots, e_gen)
    rr = np.array(roots, dtype=complex)
    tau, sig = rr.real, rr.imag
    Q = rng3.normal(size=(4000, 4))
    t = Q[:, 1:] @ e_gen
    r2 = (Q[:, 1:] ** 2).sum(1)
    B = (Q[:, 0][:, None] - tau[None, :]) ** 2 + r2[:, None] + (sig ** 2)[None, :]
    dM_f = np.prod(B - 2 * t[:, None] * sig[None, :], axis=1)
    Pp_f = np.prod(B - 2 * np.sqrt(r2)[:, None] * sig[None, :], axis=1)
    dM, Pp = an.detM(T, lam, Q), an.P_target(roots, Q)
    sc = max(np.abs(dM).mean(), 1e-12)
    print(f"    {nm:<32} formula err {np.abs(dM_f-dM).max()/sc:.1e} / "
          f"{np.abs(Pp_f-Pp).max()/sc:.1e}   min deficit {(dM-Pp).min():+.3e}"
          f"   frac>0 {np.mean(dM-Pp > 1e-9*sc):.3f}")


# ===================================================================== PART 4
head("PART 4  R3: does the ADHM variety force real eigenvalue classes?")

print("  ADHM reality makes T quaternionic SYMMETRIC (T_a all symmetric,")
print("  i.e. T^transpose = T), NOT quaternionic Hermitian -- so the spectral")
print("  theorem does not apply and non-real classes are not excluded a priori.")
print()
for k in (2, 3, 4):
    rng = np.random.default_rng(20 + k)
    ims, n = [], 0
    for _ in range(150):
        sol = least_squares(lambda z: an.adhm_residual(*an.unpack(z, k)),
                            rng.normal(size=an.nparams(k)),
                            xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=900)
        if np.sqrt(2 * sol.cost) > 1e-10:
            continue
        T, lam = an.unpack(sol.x, k)
        nrm = max(np.abs(Ta).max() for Ta in T)
        if nrm < 1e-3:
            continue
        n += 1
        ims.append(np.abs(eig_classes(T).imag).max() / nrm)
    ims = np.array(ims)
    print(f"  k={k}: {n} admissible data; fraction with a NON-REAL eigenvalue class "
          f"(|Im|/|T| > 1e-6): {np.mean(ims > 1e-6):.2f};  median |Im|/|T| = {np.median(ims):.3f}")

print()
print("  => the ADHM equations place no reality constraint on the spectrum:")
print("     zero spheres are permitted, so the class supplies no isolation.")


# ===================================================================== PART 5
head("SUMMARY")
print("""  R1 (one slice) is completely characterised: lambda = 0, T_a = e_a S,
  [T_0,S] = 0, C = T_0^2 + S^2, joint spectrum of (T_0,S) invariant under
  sigma -> -sigma, and p = char poly of T_0 + iS.  Every real monic p arises, so
  the condition has NO discriminating power -- and the data is commutative and
  C_e-valued anyway, so the noncommutativity is lost too.  Relaxing to one slice
  is worse on both counts than the full matching of memo7.

  R2: the threshold is one slice plus ONE off-slice point, by the exact deficit
  formula.  Two slices is sufficient but far from minimal, and non-uniform:
  the forcing degrades as O(theta^2) in the angle between slices.

  R3: admissible ADHM data generically has non-real right-eigenvalue classes,
  so dropping matching in favour of the quaternionic spectrum gives a class
  that permits zero spheres -- no isolation, hence nothing to contradict.

  Mechanism, sharply.  The entire discriminant is r^2 - t^2 -- the deviation of
  Im q from the slice direction e -- weighted by the sigma_j, i.e. by the
  imaginary parts of the roots.  It is supported exactly on the 2-sphere
  directions transverse to any single slice, and the slice is precisely the
  equality locus of the Cauchy-Schwarz inequality t^2 <= r^2.  So a one-slice
  condition is evaluated exactly where the discriminant vanishes: not merely
  weak, but blind by construction.  Two secondary consequences: restricted to
  the slice the data abelianises (T_0 + S e with [T_0,S] = 0 is a C_e-valued
  NORMAL matrix, i.e. ordinary one-variable complex linear algebra), and within
  the R1 family "p hyperbolic" becomes exactly "S = 0", i.e. "T_0 + iS is
  SELF-ADJOINT" -- the relaxation lands on the Hilbert-Polya statement with no
  new input, which is a named destination but not a mechanism.""")
