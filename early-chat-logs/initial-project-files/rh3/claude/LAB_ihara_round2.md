# LAB — Ihara round 2: the completed analytic structure, the graph gamma factor, a four-level classification, and F8 reduced to Hankel depth

**2026-08-29.** Executes the Tier-1 items of the round-2 directive (`RH3_Notes.md`, user-supplied),
following `LAB_ihara_round1.md`. All numerics this session at dps 60–500 with the directive's §10
QC (exact charpolys, identity cross-checks, round-trips, precision escalation). Language follows
the directive's §1 guardrails; §1 below records the round-1 errata this round produced.

**Directive scorecard (success criteria §12).**

| criterion | status |
|---|---|
| A. topological bulk theorem | **partial, exact where it holds**: the topological datum is precisely the graph's gamma factor — the Bass block equals −χ(X) × a universal profile (verified to machine identity across graphs); it does not deform the ξ-side tower string, and in the regular family χ ∝ n makes "topology vs volume" inseparable (§2.5–2.6) |
| B. realizability classification | **yes**: four-level classification with proofs/sketches, incl. the new kernel level with the exact count law #exc+_distinct + 2·#exc−_distinct (§3) |
| C. defect-depth theorem | **yes (combinatorial half exact; analytic half asymptotic)**: CF anomaly index = 2n₁−1 / 2n₀−2 at the first failed shifted/unshifted Hankel — verified exactly on all four violating graphs and 20 synthetic cases; depth scales with the exterior Green's function g(a) and log(1/ε) (§4) |
| D. local/global convergence theorem | deferred (round-1 numerics stand; framework identified via moment-functional locality of CF coefficients) |

## 1. Guardrails adopted; round-1 errata

Adopted throughout: "three (now four) detectors", not nested classes without hypotheses;
"global spectral information deforms the far end", not "topology lives in the IR"; boundary/bulk
used only in the inverse-spectral sense. Errata to round 1 found this round:

1. **The ω > 0 "κ_Pick staircase" (round-1 F5) is not an N_κ count.** For ω > 0 the broadened
   exc− response has a **genuinely negative a.c. density band** on the cut (prism C9, ω = 0.15:
   min density −2.13 near x = 9.88, the top edge; a Ramanujan control — Petersen, same ω — has
   strictly positive density, min +0.063). A function with a negative boundary-density band is
   in no N_κ with finite κ: sampled Pick matrices give 0, 1, or 4 negatives depending on point
   placement (all three observed). The round-1 crossing conclusion **stands** — the ℂ⁺ pole of
   q_ω exists iff ω < δ, and that crossing is sharp — but the invariant is the pole (and the
   negative-density band, which itself localizes the violation at the spectral top edge), not a
   κ-count. At ω = 0 exactly (rational case) κ is clean: κ = # distinct exc− eigenvalues.
2. Round-1's "screw positivity ⊂ Nevanlinna ⊂ Stieltjes" phrasing is replaced by the four-level
   table of §3; the levels are inequivalent detectors with different failure invariants, and the
   kernel level (missing in round 1) sits at Ramanujan strength.
3. Round-1 F6's cover statement is weakened per the directive: two examples show the twisted
   spectrum supplying the smallest-τ atoms and the largest far-end deformation; general "IR
   localization of covering topology" remains unproved (larger ensemble: round 3).

## 2. The completed analytic structure (directive §2)

### 2.1 The graph ξ and the exact identities

The Ihara zeta has only poles; the RH objects are zeros of the determinant factor. So the
correct dictionary is:

> **Λ_X(s) := det(I − Au + qu²)|_{u=q^{−s}}** is the graph analogue of ξ (zeros = all towers),
> and `ζ_X(u)^{-1} = (1−u²)^{−χ} Λ_X`, i.e. **the Bass factor with exponent −χ(X) is exactly the
> conversion factor between Λ and 1/ζ — the graph's gamma factor.**

Response (round-1 units, V = log q·(s−½)): 𝔥(V) := −u d/du log Λ_X = Σ_{all λ, both roots c}
m·(c/√q)e^{−V}/(1−(c/√q)e^{−V}). Verified against the independent rational form to 6·10⁻⁶⁰,
and the full ζ-identity (Bass block − 𝔥) likewise. Per tempered eigenvalue the coth expansion
gives exactly: block = [principal pair term + 2πℤ towers] − 1, so

> 𝔥 = (h₊ − W₀) + Γ_triv,  h₊ := all nontrivial tower pair-terms (odd, Herglotz), W₀ := Σ mult,
> Γ_triv := the λ = ±(q+1) blocks (the s = 0,1 pole towers — the ζ-pole-block analogue).

Constant certified numerically: W₀ = Σm (candidate 2Σm fails by 9.0; Σm agrees with a K=4000
tower truncation to 1.7·10⁻⁴ = the truncation tail).

### 2.2 The completed positive string exists and has a closed-form length

The positive completion q₊(z) = h₊(√(−z))/√(−z) is Stieltjes for Ramanujan graphs with atoms at
all (θ_j + 2πk)². Its length has three matching evaluations (closed form, tower sum, derivative
h₊(0⁺)/0⁺) and a **closed form: the edge resolvent**

> **L₊ = Σ_nontriv 2√q·m_j/(2√q − λ_j)**  (= Σ 2m/(4sin²(θ_j/2))).

Exact values: Heawood **L₊ = 16** exactly; prism C6 = 100/7; K4 = 2.2164; Petersen = 10.0777.
This upgrades round-1's empirical "length is gap-dominated" to an identity: the completed length
is the trace of the resolvent at the Ramanujan edge, divergent as λ₂ → 2√q. String synthesis at
matched precision (dps 220–500; the round-1 A6 negative beads at dps 220/K=16 were precision
loss, gone at dps 500): all beads positive at every tower cutoff K, first beads scaling ~1/K
with **nearly equal masses and gaps in the interior — the completed bulk is asymptotically a
homogeneous (Weyl) string**, L converging to L₊ (1.00225 at K=16 vs 1.00777 exact, per vertex).

### 2.3 The signed-defect reading

The honest log-derivative 𝔥 carries the constant −W₀: on the critical axis
Re Σ_nontriv blocks(iy) = −W₀ **exactly** (−9.000000000000 for Petersen at two test y). The
per-period negative a.c. mass exactly cancels the tower atoms' mean: the uncompleted response's
measure is the **fluctuation of the zero set around its Weyl mean** — atoms minus background.
The positive string (§2.2) and the signed defect measure differ precisely by where the Weyl mean
is booked. (This is the finite face of spectral-realization pictures in which zeros appear as an
absorption spectrum; recorded as an observation, not a claim.)

### 2.4 The gamma factor and its χ content

Γ_X = Γ_triv + Bass block, both explicit. Verified: the Bass block's a.c. contribution to the
ζ-side response at shift ω, divided by χ, is a **universal function of x** — identical to all
printed digits across K4 (χ=−2), Petersen (−5), Heawood (−7): density/χ = −0.14264, −0.08135,
+0.12544 at x = 1, 4, 9 (ω = 0.1). Γ_triv is χ-independent (identical for K4 and Petersen) and
detects bipartiteness (extra −(q+1) tower for Heawood). So, in the directive's §2.2 template:

> χ(X) forces exactly one thing: a tower at the strip edge (ordinates πk, Re s ∈ {0,1}-side)
> with multiplicity −χ, whose response block is −χ × a universal profile — a bounded, signed,
> oscillatory a.c. correction, subleading to the Weyl √t growth of the spectral part.

This is the graph-exact realization of NOTE_variation_axes §3.3's "topology enters through the
gamma factor" (Selberg: trivial zeros of multiplicity −χ(2k+1); graphs: constant −χ per tower
point — cleaner).

### 2.5 The decisive caveat (directive §2.4's controls are impossible in-family)

For connected (q+1)-regular graphs, **χ = −n(q−1)/2 is determined by n**: "same n, different
b₁" does not exist at fixed regularity. Topology and volume are the same dial in the regular
family; the Weyl term is itself "topological" in the empty sense. Separating them requires
irregular graphs or boundary — exactly the directive's §6 (round 3, Tier 1 there).

### 2.6 A remark worth recording

The same lock occurs in the Selberg model: Gauss–Bonnet makes area = −2πχ for closed hyperbolic
surfaces. In both laboratories "volume vs topology" only decouples with cusps/boundary
(Selberg) or irregularity (graphs). Any future "topological bulk theorem" must be stated
against that lock.

## 3. Four-level realizability classification (directive §3, with the §9 kernel level)

Setting: principal-truncation response of round 1; ω = 0 unless stated. All claims verified on
the specimen set (Petersen control; dumbbell+4 exc+ m1; prisms C9/C11 exc− m2; C17 exc+ m2 +
exc− m2; dumbbell+6 exc+ m1 + exc− m1; rand40(s4) exc− m1).

| level | criterion | fails iff | failure invariant |
|---|---|---|---|
| 1. pointwise Ψ_ω ≥ 0 | weakest | exc− present **and** not shielded (δ_N > δ_P-type comparison) | first-dip time; blind to exc+ at every shift (verified ω = 0.05/0.2/0.4) |
| 2. Pick/Nevanlinna in z (ω=0) | q has non-real poles | exc− present | κ = # distinct exc− |
| 3. screw-kernel PSD (γ-space) | any exceptional | **≡ Ramanujan** | negatives = **#exc+_distinct + 2·#exc−_distinct** (6/6 specimens) |
| 4. Stieltjes support / string | any exceptional | **≡ Ramanujan** | CF anomaly depth + parity (§4) |

Proof elements. (1) Tempered pair terms are pointwise ≥ 0; an exc+ pair contributes
(e^{b t}−1−bt)/b² summed over b = ±δ−ω, positive and dominating — Siegel shielding, realized
synthetically (round 1) and naturally (C17's delay). (2) exc+ atoms are real with positive
weight (a Nevanlinna measure with negative support — not a negative square); exc− atoms are a
conjugate non-real pole pair. (3) exc+: the kernel block is
sinh(δt)⊗sinh(δs) − (cosh δt − 1)⊗(cosh δs − 1) — an explicit rank-2 (+,−) form: exactly one
negative square, multiplicities scale it without adding rank. exc−: the analogous block spans
{cos πt·(cosh−1), sin πt·sinh, …} with signature (+,+,−,−): two negative squares. Counts
confirmed on all six specimens (1, 2, 2, 2, 3, 3 as the law predicts). (4) is round-1 F1 (a
theorem: positive measure on (0, π²] ⟺ Stieltjes).

Two consequences worth stating. **Kernel-PSD ≡ Stieltjes ≡ Ramanujan at the yes/no level, but
their failure invariants are different coordinates** — the kernel counts type-weighted distinct
exceptionals; the string localizes them by depth. And the finite model now shows exactly which
coincidences among the four levels are special to ζ-like systems (no real zeros): levels 1–2
split off precisely along the Siegel structure. This answers directive §9 Q2 (yes — exc+ graphs
are pointwise-positive at all shifts yet kernel-indefinite) and Q3 (kernel ≠ Pick-in-z; kernel
sits at Stieltjes strength).

## 4. F8 solved at the combinatorial level; depth law asymptotic (directive §4)

### 4.1 The exact index law

For the graph atom sets themselves (dps 400, first negative Hankel dets of the moment sequence;
H = (μ_{i+j}), H¹ = (μ_{i+j+1})):

| graph | n₀ (H) | n₁ (H¹) | law predicts | measured CF anomaly |
|---|---|---|---|---|
| dumbbell+4 | 14 | 9 | 2·9−1 = 17 (length) | 17, length #9 |
| prism C9 | 4 | 4 | 2·4−2 = 6 (mass) | 6, mass #4 |
| prism C11 | 4 | 3 | 2·3−1 = 5 (length) | 5, length #3 |
| rand40(s4) | 5 | 4 | 2·4−1 = 7 (length) | 7, length #4 |

> **First anomalous CF coefficient = index 2n₁−1 (a length) when H¹ fails first (n₁ < n₀), and
> 2n₀−2 (a mass) when H fails at or before H¹.**

Also exact on all 20 synthetic single-defect cases. This is the classical Stieltjes CF↔Hankel
determinant dictionary doing the work; the round-1 mystery "bead depth" **is** the first failed
Hankel order, and the mass/length parity **is** which Hankel family fails. (For a positive
background + exc+ defect, unshifted H never fails before the rank ceiling — positive measure —
matching §3 level 2.)

### 4.2 The depth law (asymptotic, with honest limits)

Synthetic scans (backgrounds: rand24's 23 atoms, then a 68-atom union to lift the rank ceiling;
defect atom weight ε at a; g(a) = exterior Green's function of ℂ∖[0, π²]):

- **Type gap**: exc− sites (top-edge, complex) have g ≈ 0.25–1.0 → depths 3–10; exc+ sites
  (−δ², just below 0) have g ≈ 2δ/π (tiny) → depths 9–26. This reproduces round-1's F8 split
  quantitatively: g(a) for the actual graphs is 0.48–0.57 (exc−, measured beads 3–4) vs 0.063
  (dumbbell+4 exc+, measured bead 9).
- **ε-scaling**: on the rich background the increments per factor 10³ in ε approach the
  potential-theory prediction 1/(2g)·ln(10³): at g = 0.504: measured 7, 11 vs predicted 6.9;
  at g = 0.254: 11 vs 13.6; at g = 0.127: 14 vs 27 — the last still ceiling/precision-limited.
  Working law: **n* ≈ log(C(σ₀)/ε)/(2g(a))** asymptotically; preasymptotic depths are shallower.
- **Size independence** (directive §4.4C): explained — as the background converges (KM limit),
  g(a) and C(σ₀) converge, so n* stabilizes; the 23- vs 68-atom backgrounds already show depth
  drifting only slowly at fixed (a, ε).

Round-3 residue: prove the two halves — the index law from the CF–Hankel determinant formulas
(should be an exercise), and the n* asymptotic from Christoffel-function / orthogonal-polynomial
growth e^{2ng(a)} (standard potential theory, needs the constant made precise).

## 5. Deferred (Tier 2/3), queued for round 3

Irregular graphs — now the **top** item, since §2.5 shows the regular family cannot separate
topology from volume (find adjacency-cospectral, zeta-distinct pairs; do the bulks differ?).
Cover ensemble with controls (directive §5; incl. random 2-lifts and matched rooted balls).
Exact KM/tree string + fixed-depth convergence theorem (directive §8). Magnetic/character
twists (§7). Kernel-PSD windowed version (T_psd) tying back to NOTE_variation_axes §2.4(1).

## 6. Reproduction and QC

New scripts (project copies updated in `claude/lab_ihara_experiments.py`):
`r2a_full_structure.py` + inline fixed rerun (§2: identities A1–A6), inline B-runs (§3: κ
recheck, density signs, kernel Gram counts), `r2c_hankel.py` + inline follow-up (§4: graph
Hankel checks, rich-background scan). QC per directive §10: exact integer charpolys and Yun
multiplicities throughout; two independent evaluations for every analytic identity (blocks vs
rational; closed form vs towers vs derivative); CF round-trips at every synthesis (≤ 10⁻²⁰⁰);
precision escalation resolved the one flagged instability (§2.2); all depth claims report raw
index, bead number, and mass/length parity; all topology claims separated into spectral part
vs Bass/gamma part (§2.4), with the in-family inseparability stated (§2.5).
