"""
lab_ym_landscape.py -- where in Yang-Mills solution space does the freedom live,
and where do the isolation theorems live?

The programme needs two things (brief §1.4):
   (a) ISOLATION: a class in which no member's degeneracy locus contains a
       2-sphere -- and this must be a THEOREM about the class.
   (b) EXISTENCE: cheap.

Self-dual / ADHM has (a)-adjacent rigidity and no freedom.  The proposal is that
full (non-self-dual) Yang-Mills has the freedom.  This script quantifies the
trade-off using the external literature, which is the honest way to test it since
none of these are our own computations.

INPUTS (all from published theorems; see memo17 for citations).
  * Bogomolny:            int|F|^2 >= 8 pi^2 |k|, equality iff (A)SD.
  * Gursky-Kelleher-Streets (CMP 361, 2018), round S^4, SU(2):
        F^+ not== 0  ==>  int|F|^2 >= 8 pi^2 |k| + 16 pi^2 .
    i.e. every genuinely non-self-dual YM connection sits at least TWO charge-one
    instanton actions above the minimum.  Sharp.
  * Taubes (CMP 91, 1983):  Morse index  i >= 2(|k| + 1)  at a non-minimal YM
    connection -- so none is a local minimum.
  * Sadun (CMP 163, 1994), quadrupole family, r,t odd >= 3:
        c_2 = (r^2 - t^2)/8 ,   index = r t ,   nullity = 12  (independent of r,t).
  * Gursky-Kelleher-Streets (CMP 376, 2020): index + nullity is bounded ABOVE by a
    linear function of the energy, and BELOW likewise on Sadun's family -- so the
    non-self-dual sector becomes MORE unstable with energy, not less.

QUESTIONS.
  Q1  Does the GKS gap get stronger at high charge, where the freedom is?
  Q2  How unstable are the known non-self-dual solutions?
  Q3  Do the numbers support "isolation lives only next to the self-dual sector"?
"""
import numpy as np

LINE = "=" * 78
def head(s): print(); print(LINE); print(s); print(LINE, flush=True)

head("Q1  the GKS energy gap is ADDITIVE, so its relative size vanishes")
print("  Bogomolny minimum for charge k:  E_min(k) = 8 pi^2 k.")
print("  GKS: any non-self-dual YM connection has E >= E_min(k) + 16 pi^2.")
print("  So the gap is a FIXED 2 instanton actions, independent of k.")
print()
print(f"  {'charge k':>9}{'E_min / 8pi^2':>15}{'gap / 8pi^2':>13}{'relative gap':>15}")
for k in (1, 2, 3, 5, 10, 50, 100, 1000):
    print(f"  {k:>9}{k:>15}{2:>13}{2.0/k:>15.4f}")
print()
print("  => the gap theorems isolate the (anti-)self-dual STRATUM.  They do not")
print("     become stronger at high charge; the relative gap -> 0.  Whatever")
print("     rigidity they give is a statement about a neighbourhood of the ASD")
print("     locus, and says nothing about the non-self-dual sector where the")
print("     freedom actually is.")

head("Q2  the known non-self-dual solutions are increasingly unstable saddles")
print("  Sadun's quadrupole family (CMP 163, 1994), r,t odd >= 3:")
print("    c_2 = (r^2 - t^2)/8,  Morse index = r*t,  nullity = 12.")
print("  Taubes' lower bound for any non-minimal YM connection: i >= 2(|c_2| + 1).")
print()
print(f"  {'(r,t)':>10}{'c_2':>10}{'index r*t':>11}{'nullity':>9}"
      f"{'Taubes 2(|c2|+1)':>18}{'index/|c2|':>12}")
rows = []
for r in (3, 5, 7, 9, 11, 15, 21):
    for t in (3, 5, 7):
        if t > r: continue
        c2 = (r*r - t*t)/8
        idx = r*t
        taubes = 2*(abs(c2) + 1)
        rows.append((r, t, c2, idx, taubes))
        rat = idx/abs(c2) if c2 != 0 else float('inf')
        print(f"  {f'({r},{t})':>10}{c2:>10.1f}{idx:>11}{12:>9}{taubes:>18.1f}"
              f"{rat:>12.3f}" if c2 != 0 else
              f"  {f'({r},{t})':>10}{c2:>10.1f}{idx:>11}{12:>9}{taubes:>18.1f}{'inf':>12}")
print()
print("  Two readings.  (i) index grows without bound, so these are deep saddles --")
print("  no local minimum, no stability, and by Bourguignon-Lawson any WEAKLY")
print("  STABLE Yang-Mills field on S^4 (SU(2), SU(3), U(2)) is (anti-)self-dual.")
print("  (ii) index/|c_2| stays O(1), matching the GKS index-energy bound: the")
print("  instability scales linearly with the energy.  There is no regime in which")
print("  a non-self-dual solution becomes rigid.")

head("Q3  what the programme needs, against what the literature supplies")
print(f"  {'requirement':<44}{'self-dual / ADHM':>18}{'full YM':>16}")
rows2 = [("existence cheap (big solution space)", "no  (8k-3)", "YES (inf-dim)"),
         ("solution space determined vs overdetermined", "overdet.", "determined"),
         ("nonzero current available", "no", "YES"),
         ("Bogomolny / energy bound available", "yes (equality)", "yes (strict)"),
         ("isolation theorem for the class", "gap thms nearby", "NONE known"),
         ("solutions isolated in moduli", "yes (smooth mod.)", "NO (families)"),
         ("weakly stable members", "yes (minima)", "NONE (Taubes)"),
         ("2-sphere excluded from degeneracy locus", "n/a (no jumping)", "NO -- it is the"),
         ("", "", "generic locus")]
for a, b, c in rows2:
    print(f"  {a:<44}{b:>18}{c:>16}")
print()
print("""  The last row is the decisive one and it is not our computation.  In Sadun's
  family -- the standard construction of non-self-dual Yang-Mills fields on S^4 --
  the solutions are parametrised partly by the HOLONOMY AROUND A 2-SPHERE
  S_+ subset S^4 (a singular orbit of the SO(3) action), and the family includes
  connections with a holonomy singularity along exactly that 2-sphere
  (classification: Sibner-Sibner, CMP 1992).

  So in the very sector where full Yang-Mills has its freedom, a 2-sphere is the
  STANDARD degeneracy locus rather than a forbidden one.  The programme needs
  "no 2-sphere" as a theorem about the class.  The literature says 2-spheres are
  where the interesting non-self-dual solutions live.""")

head("SUMMARY  the trade-off of brief §3, now external")
print("""  Full Yang-Mills buys EXISTENCE at exactly the cost of ISOLATION, and the
  exchange rate is documented by other people's theorems:

    * existence: the YM system after gauge fixing is a DETERMINED second-order
      elliptic system, so local solutions are parametrised by boundary data --
      infinite-dimensional.  The ASD equations are OVERDETERMINED (first order,
      3 equations for 4 unknowns modulo gauge), which is the structural reason
      the instanton moduli space is a finite 8k-3 and full YM has no analogue.
      This is the one place in the whole programme where the finiteness
      criticism of memo15 §0(5) is answered.

    * isolation: every rigidity theorem in the subject has the form
      "small ==> (anti-)self-dual or flat" -- Bourguignon-Lawson-Simons, Min-Oo,
      Dodziuk-Min-Oo, Gerhardt, Nakajima, Feehan I/II, Feehan discreteness,
      Gursky-Kelleher-Streets, Vieira.  Not one isolates a NON-self-dual
      solution.  And Sadun's continuous 2-parameter family shows non-self-dual
      solutions are not isolated even within a single symmetry class.

  So the freedom that makes full Yang-Mills attractive is the same freedom that
  destroys the sphere-free property.  That is brief §3's rigidity/existence
  trade-off again -- but for the first time it is instantiated by an external
  literature rather than by our own matrix computations, at the level of a whole
  PDE theory.""")

head("Q4  do the candidate degeneracy loci even have the right DIMENSION?")
print("""  The zero set of R Xi in H is a union of 2-SPHERES (2-dimensional, one per
  conjugate pair) and POINTS (0-dimensional, one per real zero).  Any locus we
  propose to match it against must be able to be 2-dimensional.

  For a Yang-Mills field on a 4-manifold with structure group G, dim g = d, the
  anti-self-dual curvature F^- is a section of Lambda^2_- tensor g, i.e. a
  3 x d matrix of functions.  The rank-degeneracy loci have codimension
      codim{ rank F^- <= r } = (3 - r)(d - r).
  In a 4-manifold, a locus can contain a 2-sphere only if its dimension is >= 2,
  i.e. codimension <= 2.""")
print()
print(f"  {'G':<10}{'d = dim g':>10}   " + "".join(f"{('r<='+str(r)):>10}" for r in (0,1,2)))
for nm, d in [("U(1)", 1), ("SU(2)/SO(3)", 3), ("U(2)", 4), ("SU(3)", 8), ("SO(4)", 6)]:
    cods = []
    for r in (0, 1, 2):
        if r > min(3, d): cods.append("--"); continue
        c = (3 - r) * (d - r)
        cods.append(f"{c}({max(4-c,0)}d)" if c <= 4 else f"{c}(empty)")
    print(f"  {nm:<10}{d:>10}   " + "".join(f"{x:>10}" for x in cods))
print()
print("  Reading (codim c gives a locus of dimension 4 - c, 'empty' if c > 4):")
print("   * SU(2)/SO(3), d = 3:  codims 9, 4, 1  ->  loci are EMPTY, POINTS, or a")
print("     HYPERSURFACE.  Nothing 2-dimensional.  So no curvature rank locus of an")
print("     SU(2) Yang-Mills field can BE a union of 2-spheres.  The dimensions")
print("     simply do not line up, before any analysis.")
print("   * and the two that are not empty are both dead for other reasons: the")
print("     0-dimensional one is counted by a Thom polynomial in characteristic")
print("     classes (Feher-Nemethi-Rimanyi), hence a deformation invariant, hence")
print("     brief §6.3; the hypersurface can contain spheres, so it supplies no")
print("     isolation theorem.")
print()
print("   * U(2), d = 4, is the ONE case where codim 2 occurs: {rank F^- <= 2} =")
print("     {det of the 3x4 minors degenerate} has codim (3-2)(4-2) = 2, i.e. a")
print("     2-DIMENSIONAL locus, which can be a union of 2-spheres.  This is the")
print("     only slot in the whole family that is not excluded on dimension")
print("     grounds, and U(2) is also inside the Bourguignon-Lawson stability")
print("     theorem's hypothesis.  It is the one concrete thing here worth a day.")
print()
print("  CAVEAT.  'codim c' is the GENERIC codimension.  For a particular Yang-Mills")
print("  field the locus can be larger than generic, so these counts exclude")
print("  matching-by-dimension but do NOT by themselves give an isolation theorem")
print("  (which would need the reverse: a proof that the locus can never be")
print("  2-dimensional for ANY member of the class).")
