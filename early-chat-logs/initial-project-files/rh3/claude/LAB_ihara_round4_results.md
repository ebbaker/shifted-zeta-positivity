# LAB — Ihara round 4 results: the compactified depth coordinate is intrinsic and bulk-meaningful; two-regime depth law; Artin and moment-locality verified

**2026-08-29.** Executes the round-4 directive (`LAB_ihara_round4.md`, user-supplied): Tier 1 in
full, Tier-2 proof closures, and the Tier-3 topology track (Artin, irregular object, cycle
locality). Scorecard against §13:

| criterion | status |
|---|---|
| A. intrinsic zeta depth law | **achieved as a cutoff-independent law with exact-threshold grounding**, plus an unforeseen two-regime refinement: the continuum Green law holds for δ ≳ local zero spacing; below it, detection is shallower (discrete-support effect) (§3–4) |
| B. bulk interpretation of compactification | **resolved**: Q is the Weyl function of a genuine Kreĭn string with the **same total length** (Q(0) = q(0) exactly); the bead map is non-local except at the far end (m̃_N = m_N + 1/l_N exactly) — so n_comp is a genuine inverse-spectral depth of a canonically associated string, not a relabeling of the original one (§2) |
| C. rigorous four-level closure | **done**: exc− block inertia measured exactly (+,+,−,−) on its 6-dim span with null affine directions; independence via distinct-exponent linear independence; shielding stated with strict inequalities and the equality case resolved (§5) |
| D. topology through twists | **first stage done**: graph Artin factorization verified exactly (ℤ/2 as an integer polynomial identity, ℤ/3 at 10⁻⁵⁰); the GM pair's zeta difference localized to **pentagon** non-backtracking counts (k\* = 5); the Bethe–Hessian gives a legitimate self-adjoint irregular object whose bulk differs at exactly the moment-locality depth (§6) |

## 1. Corrections adopted from the directive

The round-3 wording on the e^{4ng} channel is replaced: solving either threshold gives
n ~ log(1/ε)/(2g) at fixed Green distance; the graph type gap is a **location** (Green
distance) effect, with the rank-two structure supplying the sign mechanism. The raw-moment
coordinate is non-intrinsic for the full zeta measure (divergent moments); round 3 §4's
infinite-depth statement is a statement about that truncation coordinate only. Both now
superseded by the intrinsic construction below.

## 2. B1 — what the compactification is on the bulk side

With x = λ/(s₀+λ), ζ = z/(s₀+z) (s₀ a fixed Möbius scale; the directive's s₀ = 1, we use
s₀ = 200 numerically for conditioning — the asymptotic laws are s₀-independent):
Q(ζ) = q(z)/(1−ζ) has atoms x_j with weights ŵ_j = w_j/(s₀+λ_j) — a finite measure on a
compact subset of [0,1): **all moments exist**. Facts established:

1. **Q is Stieltjes ⟹ (Kreĭn) the Weyl function of another string S̃.** Exact.
2. **Total length is invariant**: Q(0) = q(0) = L. (One line; verified on random strings to
   10⁻⁵⁰ along with everything below.)
3. **The bead map S → S̃ is non-local** in the interior (lengths not individually preserved,
   masses strongly reweighted toward the far end), with one exact local law at the wall:
   m̃_N = m_N + 1/l_N (the 1-bead case [m, l] → [m + 1/l, l] is exact analytically).

Per the directive's guardrail: n_comp is a **compactified inverse-spectral depth** — a genuine
bulk coordinate of S̃, an equal-length canonical companion of the zeta string, not the physical
depth of the original string.

## 3. A1/A3 — the compactified zeta measure is intrinsic; the Green law holds

Background: first 100 genuine ordinates (γ₁₀₀ = 236.524) plus the **analytic RvM tail**
(density log(u/2π)/2π, weight 2 per zero, integrated to ∞). Fixed compactified moments are
cutoff-stable: rel. drift across N = 40 → 100 is 0.15%–0.27% for k = 0…10 (success criterion
A1 met; the residual is the RvM fluctuation term). A worthwhile methods note: an initial
factor-2 bug in the tail density was caught *by the stability test itself* — the drift pattern
is a sensitive diagnostic.

Mapped defect (off-line zero ½+δ±iτ): x_c = λ_c/(s₀+λ_c), effective weight
|ε_eff| = 2/|s₀+λ_c| ~ 2/τ² (height suppression), and the exterior Green distance follows the
predicted edge law — measured against the exact interval Green function of the support hull:

| τ | δ | g exact | g law = 2δ√s₀/(τ²√(1−α)) |
|---|---|---|---|
| 20 | 0.3 | 2.825e−2 | 2.999e−2 |
| 40 | 0.3 | 7.124e−3 | 7.498e−3 |
| 80 | 0.3 | 1.847e−3 | 1.875e−3 |
| 160 | 0.3 | 4.668e−4 | 4.686e−4 |

(0.4% at τ = 160.) With the exact threshold identities of round 3, this grounds the intrinsic
law **n_comp ≈ log(1/ε_eff·C)/(2g) ~ τ²(2 log τ + O(1))·√(1−α)/(4δ√s₀)** — the directive's
τ² log τ / δ scaling with explicit constants.

## 4. A4/A5 — end-to-end test and the two regimes

Scaled model (ordinates γ_j/5, band [2.83, 47.3], s₀ = 8) where crossings are reachable:

- **Discrete regime (δ ≲ local zero spacing ≈ 0.45):** measured depths (n₀ = n₁ ties
  throughout, as the rank-two mechanism predicts) are systematically **shallower** than the
  hull-interval law — τ = 3,4,6,9 at δ = 0.4 give n = 4, 5, 9, 16 vs predictions 2.5–49. Cause
  identified: when the defect's distance is comparable to the local gap between background
  atoms, the true (discrete-support) Green function between atoms exceeds the interval
  approximation — detection is easier. For real ζ, local spacing 2π/log(τ/2π) → 0, so a fixed
  δ is in the **continuum regime at large height**; the discrete regime softens detection only
  for δ below the local spacing.
- **Continuum regime (δ/spacing ≳ 1.5–3):** measured/predicted ratios 0.66–1.20 (order-1
  agreement, constants unfitted).
- **Time domain, same defects:** t*·δ = 2 log τ + 0.2 ± 0.15 across all cases — the robust
  scaling of directive §7, again cutoff-free.

**A5 verdict (cutoff-independent form of the round-3 disparity):** for a hypothetical zero at
height τ, offset δ, the intrinsic compactified bulk detects at depth ~ τ² log τ / δ
(polynomially deep in height), the screw/time coordinate at t* ~ 2 log τ / δ (logarithmic).
Both statements are now intrinsic — no truncation coordinate involved. The strategic reading of
round 3 survives compactification: **the time-domain coordinate is polynomially better adapted
to violation detection than any moment-based inverse-spectral coordinate we have constructed,
and the gap is now quantified height-by-height.**

## 5. Tier-2 closures

**Kernel index.** The exc− block's quadratic form, compressed to its span
{cos πt·cosh δt, sin πt·sinh δt, cos πt·sinh δt, sin πt·cosh δt, 1, t}, has measured inertia
(+, +, −, −, 0, 0) — eigenvalues (−1167, −232, ~0, ~0, +234, +1098) at δ = 0.37 — confirming
signature (+,+,−,−) with null affine directions. Independence across blocks: the functions
e^{±δ_j t}, e^{(±δ_j ± iπ)t}, e^{±iτ_j t}, 1, t have pairwise distinct exponents, hence are
linearly independent; the total form is the direct sum on their span and inertia adds. With the
exc+ 2×2 signature (round 2), **N₋ = #exc+_distinct + 2·#exc−_distinct** is proved.

**Shielding equality case.** Theorem stated with strict inequalities (A > |B| eventually
positive, A < |B| sign-changing, constants as in round 3). At A = |B| the leading term touches
zero on the lattice πt+φ = π and the sign is decided by subleading data; in the tested
configuration (positive tempered background) the exact-critical case is **eventually positive**
(min Ψ on [60,120] = +7.9·10³), and just above critical (ratio ×(1+10⁻⁶)) the first negative
time is pushed beyond the window — the first-crossing time diverges as the ratio decreases to
critical. No "iff at equality" is claimed; the equality criterion is the sign of the subleading
profile at the touch lattice.

**Completed-tower Weyl law.** √y·q₊(−y) = W₀′ to 8 digits already at y = 10⁴ (the error is
exponentially small since h₊(V) − W₀′ = Σ blocks decays like e^{−V}): so q₊(−y) ~ W₀′ y^{−1/2}
**exponentially exactly**, and Kreĭn–Kasahara gives the homogeneous short-distance law with
density ρ₀ = 1/W₀′² (per-vertex Petersen: 1.235, vs measured bead density ~0.8–1.2 at K = 16,
preasymptotic). Edge-saturated Ramanujan case: L₊ = ∞ directly from the closed form.

## 6. Tier-3 topology track

**Artin factorization in the lab.** ζ_{BD(X)}⁻¹ = ζ_X⁻¹·L(u, sign) verified as an **exact
integer polynomial identity** for X = K4 (det(xI−B_{Q3}) = det(xI−B_{K4})·det(xI+B_{K4}));
ℤ/3 cyclic cover of K4 (voltage on one chord): factorization into the three character-twisted
determinants verified at 3.9·10⁻⁵⁰. Twisted Ihara L-functions behave exactly as Artin theory
prescribes — the machinery for round 5's flux experiments is validated.

**C2 — cycle locality of the GM pair.** Exact non-backtracking traces: tr B^k agree for
k ≤ 4 and first differ at **k\* = 5** (1500 vs 1490): the adjacency-cospectral pair differs in
its **pentagon** counts — invisible to all tr A^k, visible to non-backtracking count five.

**C1 — a legitimate irregular inverse-spectral object.** The Bethe–Hessian pencil
H(r) = (r²−1)I − rA + D is real symmetric (self-adjoint ✓) and carries exactly the Ihara
information. For the GM pair: exact charpolys of 25·H(6/5) (and 4·H(5/2)) **differ**; first
power-trace difference at k_H = 4; the spectral-measure CFs first differ at **index 4 = mass
m₃** — precisely the first coefficient whose Hankel determinant (Δ₃, moments to μ₄) sees the
first differing moment. By the round-3 determinant formulas this is a **proof-backed
moment-locality law**: first differing trace order ↔ first differing bulk coefficient, verified
identically at both r values. Caveat honored: H(r) at tested r is not positive definite, so the
CF is formal/indefinite there; the locality statement is independent of positivity, and a
PD normalization (spectral shift) is a round-5 cleanup.

## 7. Literature audit (directive §11, first pass)

The ingredients are classical, as expected: Uvarov/Christoffel spectral transformations of
orthogonal polynomials ([Zhedanov's rational spectral transformations](https://www.researchgate.net/publication/223385653_Rational_spectral_transformations_and_orthogonal_polynomials);
recent matrix versions e.g. [arXiv:2312.05137](https://arxiv.org/pdf/2312.05137)); the
Stieltjes CF ↔ Hankel/QD dictionary ([Stieltjes CF and QD algorithm](https://www.researchgate.net/publication/2549920_Stieltjes_continued_fraction_and_QD_algorithm_Scalar_vector_and_matrix_cases));
the algebra of the finite Stieltjes moment problem ([Pozza–Strakoš](https://www.karlin.mff.cuni.cz/~strakos/download/2018_PozStr.pdf)).
Ihara-vs-cospectrality is an active topic ([cospectrality of joins](https://www.sciencedirect.com/science/article/pii/S0012365X14002209);
[properties determined by the Ihara zeta](https://www.researchgate.net/publication/220342352_Properties_Determined_by_the_Ihara_Zeta_Function_of_a_Graph)),
and one 2026 preprint requires a close read against our irregular direction before any novelty
claim there: [Beyond Bass Collapse: New Irregular Edge-Space Invariants in Ihara Theory
(arXiv:2604.20578)](https://arxiv.org/html/2604.20578). **No source surfaced** for the
synthesis (support defect → Christoffel threshold → CF depth), for the two-regime
discrete/continuum depth law, or for the transfer to zeta-string coordinates — consistent with
the directive's assessment that the synthesis is where the plausible novelty lies. A deeper
audit is queued before any external write-up.

## 8. Round-5 queue

Close read of arXiv:2604.20578 vs §6. Discrete-regime depth law (Green functions of
atoms-plus-interval supports) — the one regime without a formula. Flux derivatives at zero
(directive D3.1–D3.3) on the GM pair, with the validated Artin machinery. PD normalization of
the irregular object. Formal write-up of the intrinsic two-regime law and of §5's proofs.
For the main programme (post human-review): fold the A5 verdict into the Ψ_ω record — the
time-domain coordinate's advantage is now intrinsic, quantified, and cutoff-free.

## 9. Reproduction and QC

Scripts appended to `claude/lab_ihara_experiments.py` (B1 bead-map discovery; fixed-moment
stability with RvM tail; Green-law table; scaled end-to-end + continuum-regime runs; Tier-2
closure runs; Artin/ℤ₃, GM traces, Bethe–Hessian runs). QC: all detection orders scale-invariant
(H → DHD) and computed from exact-lemma and direct-determinant routes; moment-stability test
used as a tail-density diagnostic (§3); integer identities exact (Artin ℤ/2, tr B^k, charpolys);
inertia computations via generalized eigenproblem with Cholesky whitening at dps 60.
