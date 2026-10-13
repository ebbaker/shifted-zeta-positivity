"""
lab_ade_rigidity.py -- screening the gravitational-instanton route.

The one thing brief §6.5 says is missing is a finite-dimensional Q-algebra (or
Z-lattice) with a positive/definite form.  ALE gravitational instantons supply
EXACTLY that: by Kronheimer, H^2(X;Z) of the minimal resolution of C^2/Gamma is
the ADE root lattice with intersection form = -(Cartan matrix), even and negative
definite, and the (-2)-classes are the roots.  So this is the first object in the
whole programme that is definite AND integral.

Two questions decide whether that is useful.

  Q1 RANK.  memo5's obstruction to the compact hyperkahler Hodge-Riemann tower was
     a RANK gap: the primitive pieces have dim H^m = C(b+m-1,m) - C(b+m-3,m-2) for
     b = b_2 in {7, 8, 23, 24}, and only a sparse set of ranks is reachable, while
     RH needs a definite form of EVERY rank d.  Does the ALE side have the same
     gap?

  Q2 CONTENT.  Kronheimer's lattice is determined by Gamma alone -- it has no
     moduli.  All continuous data lives in the periods alpha_1,alpha_2,alpha_3.
     So can the ALE existence condition cut out the hyperbolic locus?  Kronheimer's
     nondegeneracy condition is: for each root xi, the three periods do not ALL
     annihilate xi -- i.e. the complement of a finite union of real LINEAR
     subspaces of codimension 3, one per root.  The boundary of the hyperbolic
     locus is the discriminant hypersurface.  Is that a union of hyperplanes?

ANSWERS.  Q1: NO gap -- A_d exists for every d >= 1, so ALE evades memo5's rank
obstruction entirely.  This is a genuine correction to the reading of memo5: the
rank problem is specific to the compact Hodge-Riemann tower.  Q2: the discriminant
is irreducible of degree 2(d-1) and is NOT a product of linear forms, so no finite
union of linear subspaces has it as boundary.  The ALE route fails on CONTENT, not
on rank: the lattice is rigid and carries no dependence on p, while the periods
can only produce linear discriminants.
"""
from math import comb
import numpy as np
import sympy as sp

LINE = "=" * 78
def head(s): print(); print(LINE); print(s); print(LINE, flush=True)

# ------------------------------------------------------------------ ADE lattices
def cartan(kind, n):
    A = np.zeros((n, n), dtype=int)
    for i in range(n):
        A[i, i] = 2
    for i in range(n - 1):
        A[i, i+1] = A[i+1, i] = -1
    if kind == 'A':
        pass
    elif kind == 'D':
        A[n-2, n-1] = A[n-1, n-2] = 0
        A[n-3, n-1] = A[n-1, n-3] = -1
    elif kind in ('E6', 'E7', 'E8'):
        m = {'E6': 6, 'E7': 7, 'E8': 8}[kind]
        A = np.zeros((m, m), dtype=int)
        for i in range(m): A[i, i] = 2
        for i in range(m - 2):           # chain 1..m-1
            A[i, i+1] = A[i+1, i] = -1
        A[2, m-1] = A[m-1, 2] = -1       # node attached to the 3rd of the chain
    return A

head("PART 1  the ADE forms: definite, integral, and how many per rank")
print(f"  {'type':>6}{'rank':>6}{'even?':>7}{'neg. def. (as -Cartan)':>26}{'det Cartan':>12}")
rows = []
for n in range(1, 11):
    rows.append(('A', n))
for n in range(4, 11):
    rows.append(('D', n))
for e in ('E6', 'E7', 'E8'):
    rows.append((e, None))
for kind, n in rows:
    A = cartan(kind, n if n else 0)
    m = A.shape[0]
    ev = np.linalg.eigvalsh(A.astype(float))
    even = all(A[i, i] % 2 == 0 for i in range(m))
    negdef = (np.linalg.eigvalsh(-A.astype(float)).max() < 0)
    print(f"  {(kind + (str(n) if n else '')):>6}{m:>6}{str(even):>7}"
          f"{str(negdef):>26}{int(round(np.linalg.det(A.astype(float)))):>12}")

print()
avail = {}
for kind, n in rows:
    m = cartan(kind, n if n else 0).shape[0]
    avail.setdefault(m, []).append(kind + (str(n) if n else ''))
print("  forms available at each rank d (ALE / Kronheimer):")
for d in range(1, 11):
    print(f"    d = {d:>2}:  {avail.get(d, [])}   ({len(avail.get(d, []))} form(s))")
print("  => every rank is reachable (A_d), but with at most THREE forms at that")
print("     rank, all root lattices, and each one a single fixed matrix.")

# ===================================================================== PART 2
head("PART 2  Q1: does ALE inherit memo5's RANK gap?  (No.)")
def dimH(b, m):
    if m < 0: return 0
    return comb(b + m - 1, m) - (comb(b + m - 3, m - 2) if m >= 2 else 0)
tower = set()
for b in (7, 8, 23, 24):
    tower |= {dimH(b, m) for m in range(0, 10)}
tower_hits = sorted(d for d in range(1, 41) if d in tower)
ale_hits = sorted(range(1, 41))                     # A_d for every d
print(f"  compact hyperkahler Hodge-Riemann tower (memo5 / Lab_Tower_Check Part 1):")
print(f"    reachable ranks in 1..40:  {tower_hits}     ({len(tower_hits)} of 40)")
print(f"  ALE gravitational instantons (Kronheimer):")
print(f"    reachable ranks in 1..40:  all of them via A_d      ({len(ale_hits)} of 40)")
print()
print("  => memo5's rank obstruction is SPECIFIC to the compact Hodge-Riemann")
print("     tower.  The ALE side supplies a definite integral form of every rank.")
print("     So on rank alone, the ALE route is not excluded -- unlike memo5's.")

# ===================================================================== PART 3
head("PART 3  Q2: can a union of LINEAR subspaces bound the hyperbolic locus?")
print("""  Kronheimer's existence condition is the complement of a finite union of real
  linear subspaces of codimension 3 (one per root xi: all three periods annihilate
  xi).  So any discriminant the ALE existence condition can express is a finite
  union of linear conditions.  The boundary of the hyperbolic locus is the
  discriminant hypersurface {disc(p) = 0}.  Test: is disc irreducible, and is it a
  product of linear forms in the coefficients?""")
print()
z = sp.Symbol('z')
for d in (2, 3, 4, 5):
    coeffs = [sp.Integer(1)] + [sp.Symbol(f'a{d-1-i}') for i in range(d)]
    p = sum(c * z**(d - i) for i, c in enumerate(coeffs))
    D = sp.factor(sp.discriminant(sp.Poly(p, z)))
    Dp = sp.Poly(D, *[sp.Symbol(f'a{i}') for i in range(d)])
    fac = sp.factor_list(D)
    nlin = sum(1 for f, e in fac[1] if sp.Poly(f, *[sp.Symbol(f'a{i}') for i in range(d)]).total_degree() == 1)
    print(f"  d = {d}:  deg(disc) = {Dp.total_degree():>2};  "
          f"irreducible factors = {len(fac[1])};  linear factors = {nlin};  "
          f"product of linear forms: {str(len(fac[1]) == nlin and nlin > 0)}")
print()
print("  => the discriminant is irreducible of degree 2(d-1) for every d tested and")
print("     is never a product of linear forms.  So no finite union of linear")
print("     subspaces has the hyperbolic locus as its closure, and the ALE")
print("     existence condition cannot express hyperbolicity.")

# ===================================================================== PART 4
head("PART 4  the rationality dichotomy, stated as a screen")
print("""  brief §6.5 says the missing ingredient is rationality.  The gravitational-
  instanton literature sharpens that into a dichotomy.  Two classes of object:

    (a) forms that are INTEGRAL but RIGID.  ADE root lattices (ALE); A_k and D_k
        only (ALF); -I_k (ALF compactified); Hirzebruch-Jung tridiagonal strings
        (toric non-hyperkahler).  Entries are small fixed integers (0, +-1, 2).
        Over Z, definite -- and carrying NO dependence on Xi whatsoever.

    (b) forms that DEPEND ON Xi but are REAL.  The trace forms of the Jensen
        polynomials (Lab_Tower_Check Part 3): entries are power sums of roots of a
        polynomial whose coefficients are gamma(m) = 4 m! M_{2m}/(2m)!, with
        M_k = int Phi(u) u^k du.  Definite, but with no known Q-structure.

  The rationality wall is exactly the statement that NO KNOWN CONSTRUCTION IS IN
  BOTH CLASSES.  (a) has rationality without content; (b) has content without
  rationality.  Weil's argument needs one object with both.

  Screen: for any proposed object, ask two questions -- does the form VARY with
  Xi's data, and is it defined over Q?  Every object in this programme so far
  answers 'yes' to exactly one.""")
print()
print(f"  {'object':<46}{'varies with Xi?':>17}{'over Q?':>10}")
for nm, v, q in [("ADE root lattice (ALE instanton)", "NO", "yes"),
                 ("-I_k (ALF compactification)", "NO", "yes"),
                 ("Hirzebruch-Jung string (toric)", "NO", "yes"),
                 ("hyperkahler BB form q_X", "NO", "yes"),
                 ("trace form of J^{d,n} (Lab_Tower_Check)", "yes", "NO"),
                 ("ADHM C = sum T_a^2 + Re(lam^dag lam)", "yes", "NO"),
                 ("memo9 transverse Hessian c_2", "yes", "NO")]:
    print(f"  {nm:<46}{v:>17}{q:>10}")
