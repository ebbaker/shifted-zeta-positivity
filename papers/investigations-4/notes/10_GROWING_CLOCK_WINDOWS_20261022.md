# Growing clock windows from the existing first-moment bound

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded **gpt-6-astra (Codex), effort max**.

**Status: proved corollary of existing finite inequalities; same-assistant self-review only.** This implements C3–C4 of [Continuation 08](08_CONTINUATION_SHARP_DIVISOR_STABILITY_AND_GROWING_CLOCK_WINDOWS_20261022.md). It uses no new saddle theorem or numerical acquisition. See the [manuscript source](../manuscript/zero_count_heat_transport/sections/08_theta_concentration.tex), [review](../reviews/02_DIVISOR_STABILITY_AND_GROWING_WINDOWS_SELF_REVIEW_20261022.md), [result index](../../../result-summaries/README.md), [cluster 13](../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../avoid/README.md) and [coupled-estimate pattern](../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## Explicit finite statement

Use exactly the canonical source, saddle normalization and complete first absolute moment bound M₁ from manuscript Theorem 9.1. Thus L≥2, t=(4πe^(4L)−9)/(2L), κ=16πe^(4L)−2t, and M₁=O(κ^(−1/2)), with a constant independent of rank. Fix 0<β<π/4 and allow any integer K=K(t)≥1. Put

\[
 s_j=(j-\tfrac12)\pi,\quad Z=s_K+\beta,\quad
 \epsilon_0=ZM_1/L,\quad\epsilon_1=(1+Z)M_1/L.
\]

At each time for which ε₀<sin β and ε₁<cos β, the original finite sign and derivative argument gives exactly the first K positive real roots, all simple, with

\[
 \max_{j\le K}|Lx_j-s_j|\le\arcsin\epsilon_0. \tag{1}
\]

This is a pointwise-in-time implication and does not assume regularity of K. The complement between the root intervals is retained, so it identifies ranks as well as nearby zeros. Since Z≤πK and 1+Z≤(1+π)K, a sufficient asymptotic condition is

\[
 \boxed{K=o(L\sqrt\kappa).} \tag{2}
\]

Both tests then hold eventually, and the unfolded location error is O(K/(L√κ))=o(1), uniformly over all j≤K.

## Matrix constants independent of block size

Select any contiguous block x_(ℓ+1),…,x_(ℓ+m), m≥2 and ℓ+m≤K, at that time. Let y_i=Lx_(ℓ+i)/π, c_i=ℓ+i−1/2, and δ=π⁻¹arcsin ε₀<1/4. The already proved finite comparison is

\[
 \|\mathcal L(y)-\mathcal L(c)\|_{\rm op}
 \le16\delta\sum_{d=1}^{m-1}(d-2\delta)^{-3}.
\]

Because d−2δ≥(1−2δ)d for d≥1,

\[
 \boxed{\|\mathcal L(y)-\mathcal L(c)\|_{\rm op}
 \le\frac{16\zeta(3)}{(1-2\delta)^3}\delta
 \le128\zeta(3)\delta.} \tag{3}
\]

The original factor 16 is two from the derivative of inverse-square distance, two from the maximum gap displacement, two from the two directions along a row, and two from the Laplacian diagonal. The final factor eight comes from (1−2δ)⁻³≤8. No m factor is hidden. One can replace ζ(3) by the elementary upper 3/2 if an entirely elementary numerical constant is preferred.

Under (2), the normalized operator error is **O(K/(L√κ))**, uniformly over these blocks. Multiplying by L²/π² gives physical error **O(KL/√κ)**. Therefore

\[
 \boxed{K=o(\sqrt\kappa/L)} \tag{4}
\]

is a stronger sufficient condition for the absolute physical-matrix error to vanish. It implies (2) since L→∞. The existing Loewner comparisons also remain valid with this δ. At each time the two matrices have the same dimension; (3) is a numerical norm comparison even when that dimension grows, without asserting a limit operator on unspecified spaces.

## What does not follow

This is a spatial clock result for low ranks growing with heat time. It is not high-height statistics at fixed heat time, PCC/GUE, or an endpoint-simplicity theorem. It admits the generic collision controls subject to their own source hypotheses; only the displayed canonical source is assigned the specific M₁ allowance. No favorable sign or collision exclusion follows.

The fixed-m cumulative discriminant identity remains fixed-m. Population changes add entry/exit terms; replacing m by m(t) does not prove a new transport identity. The complete centered exterior residual, its normalization and omitted-root/unit terms are not estimated by (1)–(4).

[BW10 Note 20](../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md) was read. Its differentiated source covariance and higher moment/variance payments are stronger fixed-rank inputs. None is needed or silently imported for this corollary. They require a fresh quantitative import audit if ZHM-09 next seeks velocity or complete-force control on a growing window.
