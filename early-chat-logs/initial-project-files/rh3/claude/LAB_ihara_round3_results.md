# LAB — Ihara round 3 results: depth law theoremized (exact threshold identities), transfer to genuine zeta zeros, and a beyond-spectrum zeta bulk

**2026-08-29.** Executes the round-3 directive (`LAB_ihara_round3.md`, user-supplied): Tier 1 in
full, plus the two Tier-2 items with the highest upside (Workstream B on a genuine zeta-zero
background; irregular GM pairs). QC per directive §13 throughout. Scorecard against §15:

| criterion | status |
|---|---|
| A. defect-depth theorem | **achieved, in a stronger (exact, non-asymptotic) form**: rank-one/rank-two determinant identities give exact thresholds; the Green's-function asymptotic is the standard regular-measure limit; edge law g(−δ²) = 2δ/π + O(δ²) derived and verified (§2) |
| B. continuum transfer law | **achieved as strong evidence with an exact local law**: on the first 60 genuine zeta ordinates, g(c) = 2πρ_eq(τ₀²)·|Im c| verified to all printed digits; moment-depth is bandwidth-proportional while time-domain detection is cutoff-free — the two detectors are parametrically inequivalent (§4) |
| C. beyond-spectrum topology | **achieved**: an equal-degree-sequence, adjacency-cospectral, Ihara-distinct pair with visibly different zeta bulks (§5) |
| D. four-level theorem | **completed modulo one proposition**: the count N₋ = #exc+_distinct + 2·#exc−_distinct survived adversarial stress (exact rate ties, near-degenerate pairs); independence proof sketch by growth envelopes; shielding rate-tie theorem with exact critical constant verified (§3) |

## 1. A1 — the CF/Hankel index law is now a theorem

With Δ_n = det(μ_{i+j})_{i,j=0}^{n−1}, Δ'_n = det(μ_{i+j+1})_{i,j=0}^{n−1} (Δ_0 = Δ'_0 = 1),
the lab's CF coefficients satisfy the classical determinant identities **in our exact
convention** (certified to 10⁻¹¹² on a random 6-atom measure):

> m_k = (Δ'_{k−1})² / (Δ_{k−1} Δ_k),  l_k = (Δ_k)² / (Δ'_{k−1} Δ'_k).

Since the numerators are squares, sign(m_k) = sign(Δ_{k−1}Δ_k) and sign(l_k) = sign(Δ'_{k−1}Δ'_k).
With n₀, n₁ the first sign changes of the two determinant families, the first anomalous
coefficient is m_{n₀} at index 2n₀−2 or l_{n₁} at index 2n₁−1, whichever family fails first —
ties go to the mass since 2n−2 < 2n−1. **This is the measured law of round 2, now proved**;
no numerical evidence remains necessary (directive A1 success criterion met).

## 2. A2/A3 — exact detection thresholds; the asymptotic and its ceiling

**Rank-one (exc+).** For σ_ε = σ₀ + ε δ_a, the shifted Hankel matrix perturbs by ε a·vvᵀ,
v = (1, a, …, a^{n−1}), so by the matrix determinant lemma and the Christoffel-function identity
vᵀ(H'_n)⁻¹v = K'_{n−1}(a,a) (CD kernel of t·dσ₀):

> **det H'_n(ε) / det H'_n = 1 + ε a K'_{n−1}(a,a)**  (verified to 10⁻²⁸⁵), hence, exactly,
> **n₁ = min{ n : ε|a| K'_{n−1}(a,a) > 1 }** for a < 0.

Ordinary Hankels never fail (positive measure) — matching level 2 of the anatomy. The
asymptotic n* = log(1/(ε|a|c))/(2g(a)) + o(n) then follows from regular-measure Christoffel
asymptotics K_n(a,a) ≍ e^{2ng(a)} off the support (Stahl–Totik/Totik; **cited, not reproved**).
The finite-background deviation is now part of the statement: for an N₀-atom background
K'_n(a,a) → ∞ as n → N₀ (Christoffel collapse at rank exhaustion), so detection is guaranteed
by the ceiling — measured rates log K'_n/(2n) start near g(a) (0.139 vs 0.127 at n=10) and blow
past it approaching the ceiling, exactly as this predicts.

**Rank-two (exc−).** For a conjugate defect pair at c, c̄ (weights ε/2), the exact 2×2 lemma
(verified to 10⁻²⁷³):

> det H_n(ε)/det H_n = 1 + ε Re K_B(c,c) + (ε²/4)(|K_B(c,c)|² − K_B(c,c̄)²),

K_B the bilinear CD kernel. The ε-linear term oscillates (K_B(c,c) = Σp_j(c)² has rotating
phase); the ε² channel is **negative** (Cauchy–Schwarz: |Σp_j(c)²| ≤ Σ|p_j(c)|² = K_B(c,c̄))
and grows at rate e^{4ng(c)} — measured: −9.8 → −1.1·10⁸ → −3.0·10¹⁷ at n = 4, 8, 12. So exc−
detection runs at twice the exponential rate available to exc+, the analytic root of the
type gap.

**A3 edge law.** For Ω = ℂ∖[0,R], g(−δ²) = acosh-type with expansion 2δ/√R + O(δ²) = 2δ/π at
R = π²; verified to 4–5 digits at δ = 0.05–0.2. Depth divergence n* ≈ (π/4δ)·log(C/ε) as the
defect approaches the admissible edge — criterion A's formula, with the constant now attached
to an exact threshold rather than a fit.

## 3. Kernel count and shielding — the remaining Tier-1 theorems

**Kernel count (directive §10).** N₋ = #exc+_distinct + 2·#exc−_distinct survived five
adversarial cases built to force cancellation: exact rate tie δ_P = δ_N (3 ✓), near-degenerate
0.30/0.31 (3 ✓), two close exc+ (2 ✓), two close exc− (4 ✓), heavy tempered background with a
tiny exc+ (1 ✓). Independence argument (sketch, to be written formally): each block's negative
subspace lives in span{sinh δ_j t, cosh δ_j t − 1} resp. the 4-dim height-π span, and distinct
δ's have distinct exponential growth envelopes; a vanishing combination of negative directions
would force leading-exponent cancellation across distinct rates, impossible. Multiplicity
rescales blocks without adding rank — as conjectured in the directive.

**Shielding rate-tie theorem (directive §11).** For one exc+ (weight m_P) and one exc− (weight
m_N) at the same rate δ − ω, the dominant profile is e^{(δ−ω)t}[A + B·cos(πt + φ)] with
A = m_P/(δ−ω)², |B| = m_N/((δ−ω)² + π²). Eventual positivity ⟺ A > |B|, i.e.

> **critical weight ratio m_N/m_P = ((δ−ω)² + π²)/(δ−ω)²** — the ordinate suppression.

Verified: at δ = 0.3, ω = 0 the predicted critical ratio is 110.66; the sign of min Ψ on
[60,100] flips between 0.9× and 1.1× of it. At equal rates and comparable weights, exc+
**always** shields (a two-order-of-magnitude margin at δ = 0.3): Siegel shielding is generic at
rate ties, quantitatively.

## 4. Workstream B — genuine zeta zeros: the two detectors are parametrically inequivalent

Background: the first N = 60 genuine ordinates (mpmath zetazero; γ₁ = 14.134725,
γ₆₀ = 163.030710), atoms (γ_j², 2); defect: hypothetical off-line pair ρ = ½ + δ ± iτ₀ →
conjugate atoms at (τ₀ ∓ iδ)². Detection computed by the exact §2 lemmas in scaled variables
(orders n₀, n₁ are invariant under t → t/β since H → DHD).

**The local Green's-function law is exact.** For the truncated support interval,
g(c) = 2πρ_eq(τ₀²)·τ₀δ·(scale) agrees with the exact interval Green's function to all printed
digits (0.00524 = 0.00524 at τ₀=20, δ=0.3; 0.00406 = 0.00406 at τ₀=40). For β = γ_N² ≫ τ₀²
this gives g ≈ 2δ/γ_N, hence

> **moment/bulk detection depth: n* ≈ (γ_N/4δ)·log(C/ε) — proportional to the bandwidth.**

Measured accordingly: at every (τ₀, δ) tested, no detection up to n = 26; pushing one case
(τ₀=20, δ=0.3, ε=2, dps 400) to the ceiling: **first failure at n = 55 of a rank-60 section**
(log₁₀ K jumping 2.3 → 5.5 → 8.6 → 11.3 across n = 40…58 — the Christoffel collapse of §2). An
off-line zero of full weight is invisible to the moment problem until the section is ~92%
exhausted.

**Time domain, same defect:** first negative t of Ψ measured at t* with
**t*·δ = 2 log τ₀ + c, c ≈ −4.1** (measured 1.881, 2.040, 2.197 at τ₀ = 20 across δ = 0.3,
0.1, 0.5; 3.34, 3.02 at τ₀ = 40 vs predicted 3.27), and **cutoff-independent** (6.270 at N=60
vs 6.265 at N=40).

**B3 verdict (the duality, resolved asymmetrically).** n*/t* ≈ γ_N/4·(log-ratio): one moment
order buys ~one quarter-period of the highest frequency in the band — a time–bandwidth
(Nyquist-type) relation. As the band → ∞ (the actual zeta measure), the moment/bulk coordinate
pushes any fixed off-line zero to **infinite relative depth**, while the screw/time coordinate
detects it at finite, cutoff-free t* ≈ (2 log τ₀ + O(1))/δ. So the directive's "deep bulk"
principle is confirmed in its strongest form — and its strategic content inverts: the
inverse-spectral bulk ordering is the **wrong search coordinate** for the actual ζ problem;
the time domain is parametrically the right one. This is the moment-side face of the
losslessness/no-free-lunch results (NOTE_variation_axes §2.1, NOTE_oneside §8), now with
explicit constants, and it quantifies from a new side why the papers' time-domain formulation
(margin, windows, L¹) is the efficient coordinate.

## 5. Irregular graphs — the zeta bulk exceeds the adjacency spectrum (criterion C)

Godsil–McKay switching (switching set C inducing a regular subgraph; outside vertices with
0, 2, or 4 neighbours in C), cospectrality certified by **exact integer charpoly equality**,
zeta compared by **exact integer charpoly of the 2m×2m Hashimoto (non-backtracking) matrix**.

Sharp specimen (search seed 25, C-type C4): connected, n = 10, m = 26, min degree 3, **equal
degree sequences [3,4,5,5,5,5,5,6,7,7] and equal adjacency charpolys**
([44, 104, −96, −324, −55, 226, 95, −44, −26, 0, 1]), yet the Ihara/Hashimoto charpolys differ
in 45 coefficients. Consequences, computed: the non-backtracking spectra differ — Perron value
4.39229 vs 4.39243 and, decisively, the sub-leading modulus pair **2.27368 vs 2.24573** (a ~1%
different "zeta spectral gap") — so the zeta-derived response differs at test points (resolvent
gap 7·10⁻³) and any gap-dominated bulk quantity (edge-resolvent-type lengths) differs, while
**every construction of rounds 1–2 (principal string, completed string, kernel counts) is
identical for the two graphs**, being adjacency-spectral. Edge lists recorded in the script for
reproduction. (A first, easier specimen with unequal degree sequences was found at seed 2 and
is retained in the script.) Per the directive's §7.3 guardrail: this shows the zeta bulk holds
*beyond-spectrum* information; it does not by itself produce a hierarchy of topological
invariants — twists remain the route to that (round 4).

## 6. Round-4 queue

1. Write the kernel-independence proposition formally (growth-envelope argument, §3).
2. Twists/graph Artin L-functions (directive §8) — now with the equal-degree GM pair as the
   natural first family to twist.
3. Analytic completed-tower Weyl law (directive §9; the homogeneous-interior observation of
   round 2 §2.2 plus standard Kreĭn–Kasahara Tauberians).
4. Continuum B beyond finite sections: replace the truncated background by the RvM-smoothed
   density and ask whether any renormalized moment coordinate (e.g. per-bandwidth "moment
   density" n/γ_N) gives a cutoff-stable detection functional — the honest remaining version
   of B.
5. Cover ensemble / moment-locality theorem (directive §12).

## 7. Reproduction and QC

Scripts appended to `claude/lab_ihara_experiments.py`: inline A1/A2 runs (determinant-formula
certification 10⁻¹¹²; Uvarov identities 10⁻²⁸⁵/10⁻²⁷³; Christoffel rates; edge law), inline
kernel-stress and shielding runs, `r3b_zeta.py` (+ inline ceiling run at dps 400),
`r3_irregular.py` (+ inline equal-degree search; both specimens' edge lists printed). QC:
zeta ordinates from mpmath zetazero at dps 30 (values used to 25+ digits); all detection orders
computed twice (direct perturbed determinants vs the exact lemmas — agreement at working
precision); scale invariance of (n₀, n₁) used and stated; precision escalation on the ceiling
run (dps 160 → 400); GM cospectrality certified exactly, never assumed from the construction.
