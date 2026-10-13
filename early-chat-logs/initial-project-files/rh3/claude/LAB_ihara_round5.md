# LAB — Ihara round 5: the ω>0 depth law is theorem-grade, the compactification is canonical, and the flux family sees triangles

**2026-08-29.** Executes the round-5 memo (`Round5.md`, user-supplied). The memo's central
caveat — that round 4's continuum depth law is proved only for the smoothed tail, not the
pure-point RH endpoint — is adopted and then largely discharged by its own suggested route: at
ω > 0 the genuine Ψ_ω spectral measure is absolutely continuous, and there the law holds at all
displacements with theorem-grade backing. Two structural lemmas make the compactified
coordinate canonical. All numerics at dps 30–140 with the standing QC.

## 0. Results at a glance

| item | result |
|---|---|
| moment lemma | compactified moments = binomial transform of the Taylor coefficients of q at z = −s₀; "moment depth" **is** Taylor-expansion order of the Weyl function at an interior point (verified 8·10⁻¹³¹) |
| operator lemma | the compactified measure is the spectral measure of the **contraction** B = A(s₀+A)⁻¹ in the state (s₀+A)^{−1/2}φ (one-line proof; verified 10⁻¹⁶) — Q is canonical, not an ad-hoc Möbius trick |
| W1 (a.c. ω>0 law) | interval Green law holds at **all** displacements on the genuine broadened measure (ratios 0.64–1.01, 8 cases); control clean; effective displacement = δ−ω exactly; Totik regularity ⟹ asymptotic is a theorem at ω > 0 |
| ω-dial unification | the round-4 discrete/continuum crossover is resolved by broadening: at ω ≳ spacing/3 no shallow-regime anomaly remains — the double-scaling criterion is empirically (displacement and ω) vs local spacing |
| time domain | derived and verified: **(δ−ω)t\* = 2 log τ + loglog τ + log(2(ξ′/ξ)(½+ω)/(δ−ω)) + o(1)** — constant predicted −2.787 vs measured −2.78 (real ζ margin slope) |
| twists | flux Hessian H_ab(k) validated exactly against brute-force winding enumeration; canonical single-edge-flip multiset separates the GM pair at **k = 3** (triangle–edge incidence) vs k\* = 5 untwisted |

## 1. Two lemmas that make the compactification canonical

**Moment lemma.** With x = λ/(s₀+λ), the compactified moments satisfy
μ̂_k = Σ_{j≤k} C(k,j)(−s₀)^j c_j where q(z) = Σ_j c_j (z+s₀)^j. Proof: ζ = z/(s₀+z) sends
z = −s₀ to ζ = ∞, and Q(ζ) = q(z)(s₀+z)/s₀ has −μ̂_k as its 1/ζ^{k+1} coefficients; the
binomial transform is the change of expansion point. Verified on a rational toy at 8·10⁻¹³¹.
Consequences: (i) *compactified moment depth is literally the order of Taylor expansion of the
Weyl function at an interior point of the resolvent set* — an intrinsic, classical object; (ii)
numerically, moments come from a Cauchy-circle DFT of q (no quadrature of the spiky density),
which is what makes the ω > 0 experiments below possible at Hankel-grade precision.

**Operator lemma (memo §"operator-theoretic interpretation", proved).** If A ≥ 0 has spectral
measure σ in the cyclic state φ, then B := A(s₀+A)⁻¹ is a positive contraction and
⟨ψ, B^k ψ⟩ = ∫ (λ/(s₀+λ))^k dσ(λ)/(s₀+λ) for ψ := (s₀+A)^{−1/2}φ — exactly μ̂_k. Verified to
10⁻¹⁶ on random matrices. So Q is the resolvent data of a canonical bounded compression of the
original string operator, in a canonically reweighted state.

## 2. W1 — the depth law on the genuine a.c. ω>0 measure

Setting: scaled mock band (ordinates γ_j/5, j ≤ 100, smooth tail), Poisson-broadened at shift
ω — the exact structure of the Ψ_ω spectral measure under RH-background; violating quartet at
(τ, δ), δ > ω, entering q exactly through its pair terms: its principal-sheet singularities are
two conjugate atoms at z₁ = −((δ−ω) + iτ)², weight 2 — **the effective displacement is δ−ω**,
the same rate that drives the time-domain criterion. Control: the undefected measure is
Stieltjes-clean to n = 28. Main table (n₀ ≈ n₁ ties throughout, as the rank-two mechanism
predicts; pred = log(1/ε_eff)/(2g), C unfitted):

| τ | δ | ω | δ−ω | n_meas | g(x_c) | pred | ratio |
|---|---|---|---|---|---|---|---|
| 4 | 0.7 | 0.3 | 0.40 | 12 | 0.0939 | 13.2 | 0.91 |
| 4 | 0.5 | 0.3 | 0.20 | 19 | 0.0471 | 26.4 | 0.72 |
| 4 | 0.9 | 0.3 | 0.60 | 9–10 | 0.1402 | 8.9 | 1.01 |
| 6 | 0.7 | 0.3 | 0.40 | 23–24 | 0.0513 | 30.2 | 0.76 |
| 6 | 1.1 | 0.3 | 0.80 | 15–16 | 0.1017 | 15.2 | 0.98 |
| 4 | 0.45 | 0.15 | 0.30 | 14 | 0.0706 | 17.6 | 0.79 |
| 4 | 0.35 | 0.15 | 0.20 | 17–19 | 0.0471 | 26.4 | 0.64 |
| 9 | 1.5 | 0.3 | 1.20 | 23–24 | 0.0752 | 25.3 | 0.91 |

Three conclusions. (i) **The interval law holds at all displacements** — including δ−ω = 0.20,
well below the ordinate spacing 0.45, where the ω = 0 discrete background of round 4 gave
ratio ≈ 0.45; the a.c. measure has no shallow regime. (ii) **Unification**: rows 2 and 7 have
different (δ, ω) but the same δ−ω — same Green distance, same depth. The bulk and time
detectors are driven by the identical displacement parameter. (iii) **Theorem-grade at ω > 0**:
the broadened density is continuous and strictly positive, hence Stahl–Totik regular, so
K_n(x_c) ≍ e^{2ng(x_c)} is a theorem there, and with the exact rank-two threshold identity the
depth law needs no further numerical support at fixed ω > 0. The remaining mathematics is
exactly the memo's double limit: **uniformity as ω ↓ 0**, where regularity degenerates to the
pure-point endpoint; the empirical criterion from rounds 4–5 is that the continuum law needs
(displacement or broadening) ≳ local spacing — for real ζ, spacing 2π/log(τ/2π) → 0, so any
fixed (δ, ω) is eventually in the continuum regime at large height.

## 3. Time domain — both asymptotics, with the constant

At ω > 0 the background has the linear margin slope (ξ′/ξ)(½+ω) (computed from mpmath's ζ
directly — a genuine Ψ_ω-framework quantity; 0.00462092 at ω = 0.1). Balancing the violating
term e^{(δ−ω)t}/((δ−ω)²+τ²) against slope·t:

> **(δ−ω)t\* = 2 log τ + loglog τ + log(2(ξ′/ξ)(½+ω)/(δ−ω)) + o(1).**

The derived constant −2.787 (at ω = 0.1, δ−ω = 0.15) matches the solved thresholds:
the residual column converges −2.955 → −2.783 across τ = 10²…10⁸. At ω = 0 the background is
bounded (no margin), and the round-3/4 form t\*δ = 2 log τ + O(1) stands — no loglog. The
sharpened disparity: time detection 2 log τ/(δ−ω) versus intrinsic bulk depth
~ τ² log τ/(δ−ω)·(constants) — both now with the same displacement parameter.

## 4. Twists — the susceptibility sees triangles

**Hessian validated.** H_ab(k) := −∂²_{φ_aφ_b} log-side winding correlations computed by the
exact insertion formula agree with brute-force enumeration of all closed non-backtracking
k-walks with their homology windings on K4 (brute = k × formula for k = 3, 4; both vanish at
k = 5 — K4 has no NB pentagons). The observable measures Σ_walks h_a h_b exactly.

**Canonical pair separation at k = 3.** Basis-free version: the multiset over the 26 edges of
single-edge ℤ/2-flip trace vectors (tr B_e^k)_{k≤6}. For the GM pair the multisets differ
already at k = 3 — the two graphs distribute their (equal total) triangles differently over
edges — while every adjacency invariant agrees and the untwisted zeta first differs at
pentagons (k\* = 5). So the flux family is strictly finer, canonically, and reaches the
difference at the smallest possible cycle order. (Guardrail: triangle-per-edge counts are
classical combinatorics; the content is their position inside the zeta's flux family —
directive D3.1 answered affirmatively at the first nontrivial level.)

## 5. Repositioning adopted (memo §§ novelty)

Artin factorization is validation, not novelty (Stark–Terras); the GM-pair existence result is
tempered pending the close read of arXiv:2604.20578; the claimed-novel core is now:
(a) the synthesis *support defect → Christoffel threshold → CF/bulk depth*, with its two-regime
structure and the ω-dial resolution; (b) the locality chain *first cycle discrepancy → first
moment discrepancy → first bulk coefficient* (proved via the determinant formulas, verified
twice); (c) the canonical compactification (§1) and the intrinsic depth law at ω > 0 (§2) as
statements about the actual Ψ_ω framework; (d) the two-coordinate disparity with derived
constants (§3).

## 6. Round-6 queue

1. **The ω ↓ 0 uniformity theorem** — now the single central open problem: uniform Christoffel
   asymptotics as the broadened measure degenerates, with the (displacement, ω) vs spacing
   criterion as the target statement.
2. Formal write-ups at paper grade: depth theorem at ω > 0 (Totik citation), kernel index,
   locality chain, the two §1 lemmas (short and self-contained).
3. Flux Hessian's inverse-spectral image: the matrix Weyl function of the B_φ family (bridge to
   the metric-graph M-function track of NOTE_variation_axes §3.2).
4. Real-ζ constants for the intrinsic law (the scaled model fixes structure; constants at
   s₀ = 200 already computed in round 4 §3).
5. Close read of arXiv:2604.20578 before any external positioning of the irregular result.

## 7. Reproduction and QC

Scripts appended to `claude/lab_ihara_experiments.py`: `r5_w1.py` (moment lemma sanity, a.c.
control, W1 table; Cauchy-circle DFT M = 1024 at dps 140, binomial transform, Hankel scans to
n = 48), inline operator-lemma and loglog runs, inline twist runs (Hessian formula vs brute
force; edge-flip trace multisets, exact integers). QC: the moment lemma provides an internal
exactness certificate (toy check 10⁻¹³¹); detection orders stable under DFT size; all twist
data exact integer arithmetic; the W1 prediction column uses no fitted constants.
