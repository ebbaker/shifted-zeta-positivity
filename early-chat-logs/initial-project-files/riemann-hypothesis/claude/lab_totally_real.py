"""
lab_totally_real.py -- the totally-real complexification class.

The appendix (appendix_extension_uniqueness.tex, Remark A.7 "why symmetry is
unavoidable") asserts that uniqueness of an extension from a slice "can only
come from symmetry or from holomorphic geometry upstairs -- never from
ellipticity alone", on the grounds that a slice has codimension two and is
therefore polar / massively underdetermined as Cauchy data for the
Cauchy-Fueter system.

That reasoning is specific to Cauchy-Fueter.  It treats the slice as a COMPLEX
line, which it is for slice regularity.  But H carries a 2-sphere of compatible
complex structures, and for a DIFFERENT one the same real 2-plane is MAXIMALLY
TOTALLY REAL -- in which case restriction is a bijection and the relevant
system (dbar for a map C^2 -> C^2) is OVERdetermined, not determined.

Concretely: J_eta(q) := q*eta for a unit imaginary eta.  If I_0 is a unit
imaginary orthogonal to eta, then C_{I_0} = span{1, I_0} is maximally totally
real in (H, J_eta).  This script verifies:

  (1) C_{I_0} is totally real for J_eta  (eta perp I_0), and a complex line for
      J_{I_0} -- the same 2-plane, two different roles.
  (2) Existence and uniqueness: every real-analytic map on C_{I_0} has exactly
      one J_eta-holomorphic extension; entire data gives an entire extension.
  (3) For intrinsic data with stem G, in the coordinates zeta_pm = z_1 +- i w
      the extension is A = (G(zeta_+)+G(zeta_-))/2, B = (G(zeta_+)-G(zeta_-))/2i
      and  Z(F) = Z(G) x Z(G)  -- DISCRETE.  So the class forbids zero spheres
      for free (and, being Stein, forbids any compact component).
  (4) The slice sits as {zeta_- = conj(zeta_+)}; the reality involution is
      tau(zeta_+,zeta_-) = (conj zeta_-, conj zeta_+); and rho in Z(G) is REAL
      iff the diagonal point (rho,rho) is tau-fixed.  (The crunode/acnode
      invariant of twistor_lift_computation.md §3, in a much simpler setting.)
  (5) THE OBSTRUCTION.  The class is preserved only by the circle U(1) fixing
      eta, whose fixed locus in H is the slice C_eta.  A discrete set invariant
      under a connected group lies in the fixed locus.  But Z(F) = Z(G)^2 has
      off-diagonal points, which are not in C_eta.  So Z(F) is U(1)-invariant
      only when |Z(G)| = 1: the symmetry hypothesis is UNSATISFIABLE, and the
      class fails at exactly the same joint as every other rigid class tried --
      rigidity up, existence of the symmetric member down.
"""
import numpy as np
import sympy as sp

LINE = "=" * 78


def head(s):
    print()
    print(LINE)
    print(s)
    print(LINE)


# quaternion arithmetic on length-4 arrays (1,i,j,k)
def qm(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([a1*a2 - b1*b2 - c1*c2 - d1*d2,
                     a1*b2 + b1*a2 + c1*d2 - d1*c2,
                     a1*c2 - b1*d2 + c1*a2 + d1*b2,
                     a1*d2 + b1*c2 - c1*b2 + d1*a2])


def qconj(p):
    return np.array([p[0], -p[1], -p[2], -p[3]])


E = np.eye(4)          # E[0]=1, E[1]=i, E[2]=j, E[3]=k

# =================================================================== PART 1
head("PART 1  the same 2-plane: complex line vs maximally totally real")

for etai, I0i, nm in [(1, 2, "eta = i, I_0 = j  (orthogonal)"),
                      (2, 1, "eta = j, I_0 = i  (orthogonal)"),
                      (1, 1, "eta = i, I_0 = i  (parallel)")]:
    eta, I0 = E[etai], E[I0i]
    # slice C_{I_0} = span{1, I_0};  J_eta(q) = q*eta
    basis = [E[0], I0]
    Jb = [qm(b, eta) for b in basis]
    # totally real  <=>  J(span) is orthogonal to span
    M = np.array([[float(np.dot(jb, b)) for b in basis] for jb in Jb])
    ip = np.abs(M).max()
    # complex line <=> J(span) = span
    proj = np.array([jb - sum(np.dot(jb, b) * b for b in basis) for jb in Jb])
    out = np.abs(proj).max()
    kind = ("TOTALLY REAL" if ip < 1e-12 else
            ("COMPLEX LINE" if out < 1e-12 else "neither"))
    print(f"  {nm:<34}  <J(span),span> = {ip:.1e}   |J(span) mod span| = {out:.1e}"
          f"   -> {kind}")

print()
print("  same real 2-plane C_j: a complex line for J_j, totally real for J_i.")
print("  Remark A.7's codimension-two objection applies to the first reading only.")

# =================================================================== PART 2
head("PART 2  holomorphic coordinates, existence and uniqueness")

print("""  Take eta = i, I_0 = j.  Write q = z_1 + z_2 j with z_1,z_2 in C_i.  Then
      q*i = (i z_1) + (-i z_2) j ,
  so J_i acts as +i on z_1 and -i on z_2: the holomorphic coordinates are
  (z_1, w) with w = conj(z_2).  The slice C_j = {x + y j} is {z_1, w both REAL},
  i.e. R^2 -- maximally totally real, as Part 1 says.

  A real-analytic map R^2 -> R^4 = C^2 complexifies uniquely, so restriction
  from J_i-holomorphic maps to C_j is a BIJECTION on germs, and entire data
  gives an entire extension.  Uniqueness is the identity theorem: a holomorphic
  function vanishing on a maximally totally real submanifold vanishes.""")

z1, w = sp.symbols('z1 w')
x, y = sp.symbols('x y', real=True)
zp, zm = z1 + sp.I * w, z1 - sp.I * w


def extend(Gexpr, zvar):
    """The unique J_i-holomorphic extension of the intrinsic datum with stem G."""
    Gp = Gexpr.subs(zvar, zp)
    Gm = Gexpr.subs(zvar, zm)
    A = sp.expand((Gp + Gm) / 2)
    B = sp.expand((Gp - Gm) / (2 * sp.I))
    return sp.simplify(A), sp.simplify(B)


zz = sp.Symbol('zz')
for nm, G in [("z^2+1", zz**2 + 1), ("z^2-1", zz**2 - 1),
              ("(z^2+1)(z-1)", (zz**2 + 1) * (zz - 1)), ("z^3-2z", zz**3 - 2*zz)]:
    A, B = extend(G, zz)
    # holomorphy: A, B are polynomials in (z_1, w) with no conjugates present
    hol = all(not s.has(sp.conjugate) for s in (A, B)) and \
        A.free_symbols <= {z1, w} and B.free_symbols <= {z1, w}
    # restriction to the slice: z_1 = x, w = y both real, must give the stem
    stem = sp.expand(G.subs(zz, x + sp.I * y))
    alpha, beta = sp.expand(sp.re(stem)), sp.expand(sp.im(stem))
    Ar = sp.expand(A.subs({z1: x, w: y}))
    Br = sp.expand(B.subs({z1: x, w: y}))
    ok = sp.simplify(Ar - alpha) == 0 and sp.simplify(Br - beta) == 0
    print(f"  G = {nm:<14} A,B holomorphic in (z_1,w): {hol};   "
          f"restriction to C_j equals the stem alpha + I_0 beta: {ok}")

# =================================================================== PART 3
head("PART 3  the zero set is Z(G) x Z(G): discrete, no spheres")

print("  F = 0  <=>  A = B = 0  <=>  G(zeta_+) = G(zeta_-) = 0, and")
print("  (zeta_+, zeta_-) is a linear change of coordinates on C^2, so")
print("  Z(F) = Z(G) x Z(G) -- always DISCRETE for nonconstant G.")
print()
for nm, G in [("z^2+1", zz**2 + 1), ("(z^2+1)(z-1)", (zz**2 + 1) * (zz - 1))]:
    A, B = extend(G, zz)
    sols = sp.solve([sp.expand(A), sp.expand(B)], [z1, w], dict=True)
    roots = sp.nroots(sp.Poly(G, zz))
    pred = [(sp.simplify((a + b) / 2), sp.simplify((a - b) / (2 * sp.I)))
            for a in roots for b in roots]
    print(f"  G = {nm:<14} #Z(G) = {len(roots)}   #Z(F) solved = {len(sols)}"
          f"   #Z(G)^2 = {len(roots)**2}   match: {len(sols) == len(roots)**2}")

print()
print("  And independently of the formula: C^2 is Stein, so a zero set has no")
print("  compact positive-dimensional component -- no 2-sphere can occur in the")
print("  zero set of ANY holomorphic map C^2 -> C^2.  Isolation is FREE, with no")
print("  symmetry assumed.  This is what Remark A.7 says cannot happen.")

# =================================================================== PART 4
head("PART 4  the reality involution and the discriminating invariant")

print("""  The slice is C_j = {z_1, w real} = {zeta_- = conj(zeta_+)}, i.e. the fixed
  locus of  tau(zeta_+, zeta_-) = (conj zeta_-, conj zeta_+).  Then:
    * Z(F) cap C_j = {(rho, conj rho) : rho in Z(G)}  -- the k slice zeros,
      matching F|_{C_j} = f.
    * the DIAGONAL point (rho, rho) is tau-fixed iff rho is REAL.
  So reality of the zeros is the tau-type of the diagonal of Z(G) x Z(G) --
  the crunode/acnode invariant of twistor_lift_computation.md §3 again, in the
  simplest possible setting.  In the coordinates (z_1, w):
      the point with zeta_+ = rho, zeta_- = rho' has w = (rho - rho')/(2i),
  so w = 0 exactly on the diagonal, and (rho, conj rho) has w = Im(rho).""")
print()
for nm, G in [("z^2+1", zz**2 + 1), ("z^2-1", zz**2 - 1)]:
    roots = [complex(r) for r in sp.nroots(sp.Poly(G, zz))]
    print(f"  G = {nm:<8}")
    for r in roots:
        wdiag = 0.0
        wslice = r.imag
        print(f"    rho = {r:+.3f}:  w on the diagonal = {wdiag:.1f}"
              f"   w at (rho, conj rho) = {wslice:+.3f}"
              f"   -> rho real: {abs(r.imag) < 1e-12}")

# =================================================================== PART 5
head("PART 5  THE OBSTRUCTION: the symmetry hypothesis is unsatisfiable")

print("""  Which rotations preserve the class?  R_u(q) = u q ubar is J_eta-holomorphic
  iff u eta ubar = eta, i.e. iff u lies in C_eta: only the CIRCLE U(1) fixing
  eta, not SO(3).  (Verified below.)  Its fixed locus in H is
      Fix(U(1)) = {q : u q ubar = q for all u in C_eta} = C_eta ,
  the slice through eta -- in coordinates, {w = 0}.

  Now suppose we ask only for Z(F) to be U(1)-INVARIANT (zero-set symmetry, not
  function symmetry -- the weakest hypothesis that still manufactures spheres
  from off-axis zeros).  A U(1)-orbit is connected; Z(F) is discrete; a
  connected subset of a discrete set is a point; so every point of Z(F) must be
  U(1)-FIXED, i.e. Z(F) subset {w = 0}.  But Z(F) = Z(G) x Z(G) contains
  off-diagonal points (rho, rho') with w = (rho - rho')/(2i) != 0 whenever
  |Z(G)| >= 2.

  So Z(F) is U(1)-invariant only if G has a single zero.  The hypothesis is
  UNSATISFIABLE for any G of degree >= 2, RH or no RH.""")
print()
rng = np.random.default_rng(0)
eta = E[1]
bad = 0
for _ in range(400):
    th = rng.uniform(0, 2 * np.pi)
    u = np.cos(th / 2) * E[0] + np.sin(th / 2) * eta          # u in C_eta
    q = rng.normal(size=4)
    lhs = qm(qm(u, qm(q, eta)), qconj(u))                     # R_u(q * eta)
    rhs = qm(qm(qm(u, q), qconj(u)), eta)                     # R_u(q) * eta
    if np.abs(lhs - rhs).max() > 1e-12:
        bad += 1
print(f"  R_u is J_eta-holomorphic for u in C_eta: violations in 400 trials = {bad}")
bad2 = 0
for _ in range(400):
    v = rng.normal(size=4)
    v[0] = 0.0
    v /= np.linalg.norm(v)                                    # generic imaginary axis
    th = rng.uniform(0.3, 2.8)
    u = np.cos(th / 2) * E[0] + np.sin(th / 2) * v
    q = rng.normal(size=4)
    lhs = qm(qm(u, qm(q, eta)), qconj(u))
    rhs = qm(qm(qm(u, q), qconj(u)), eta)
    if np.abs(lhs - rhs).max() > 1e-9:
        bad2 += 1
print(f"  ... and NOT for generic u: violations in 400 trials = {bad2} (i.e. SO(3) is broken to U(1))")
print()
for nm, G in [("z^2+1", zz**2 + 1), ("z^2-1", zz**2 - 1),
              ("(z^2+1)(z-1)", (zz**2 + 1) * (zz - 1)), ("z-1  [degree 1]", zz - 1)]:
    roots = [complex(r) for r in sp.nroots(sp.Poly(G, zz))]
    ws = [abs((a - b) / 2j) for a in roots for b in roots]
    off = sum(1 for v in ws if v > 1e-12)
    print(f"  G = {nm:<18} |Z(G)| = {len(roots)}   points of Z(F) OFF the fixed locus"
          f" {{w=0}} : {off}   -> U(1)-invariant: {off == 0}")

head("SUMMARY")
print("""  Remark A.7 of the appendix is FALSE as stated.  A rigid, non-equivariant
  class with existence, uniqueness AND automatic isolation does exist: the
  J_eta-holomorphic maps, with the slice C_{I_0} (I_0 perp eta) as maximally
  totally real Cauchy data.  Uniqueness comes from neither symmetry nor twistor
  geometry upstairs but from OVERdetermined ellipticity; the codimension-two
  objection fails because it silently fixes the complex structure for which the
  slice is a complex line.

  But the class fails at the same joint as every other rigid class tried.  Its
  symmetry group is only the circle fixing eta, whose fixed locus is a slice;
  the zero set is the product Z(G) x Z(G), which cannot fit inside a slice; so
  even the WEAKEST useful symmetry hypothesis -- invariance of the zero SET, not
  of the function -- is unsatisfiable in degree >= 2.

  Rigidity up, existence of the symmetric member down.  Recorded as the third
  independent instance of that trade (Fueter/Vekua, ADHM matching, and now the
  totally-real complexification), across three classes with nothing in common
  beyond living on H.""")
