# 02 — Chord criterion, arithmetic bridge and next research steps

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This overview accompanies the integrated [manuscript](../manuscript/theta_manifold_geometry.tex) and [reading copy](../../../../../output/pdf/theta_manifold_geometry.pdf). It supersedes the priorities in [Overview 01](01_RESEARCH_OVERVIEW_20261015.md); the detailed research notes retain the proofs and experimental history.

The investigation now has a substantially sharper target. A finite collision forces a particular two-point product to be negative on a scale proportional to the square root of the physical energy. An arithmetic estimate that is better than this scale would exclude every finite collision multiplicity. The manuscript develops this result, its cutoff transfer, the exact source identities needed to pursue it, and the strongest arithmetic tests. We have not proved that theta satisfies the estimate.

## The strongest result: a starting-energy chord criterion

Write `h_j = ∂_x^j H`, `E = H² + H_x²`, and

\[
\mathcal C_j(t;x,y)=h_j(t,x)\{h_j(t,y)-h_{j+1}(t,y)\},\qquad j=0,1.
\]

The starting point is fully stationary: `h_(j+1)(t,x)=0`. On a short rightward interval where `h_j` never vanishes, a nonnegative chord is exactly a bound of π/4 on the change in its real jet angle. More generally, a uniform lower bound `C_j ≥ −K E(t,x)^γ` with **γ > 1/2** suffices to exclude all covered finite collisions. The exponent is independent of the collision multiplicity. A general error `o(√E(t,x))` also suffices.

The proof uses a fixed nearby endpoint as the stationary start approaches the collision. The allowable interval length must therefore remain positive through the event; a bound only on one shrinking test window is insufficient. The energy must be measured at the **starting point**, including on the odd branch. The threshold is sharp for arbitrary constants: an error proportional to √E can coexist with a quadratic collision.

The [chord and cutoff note](../notes/02_signed_turning_control/02_CENTRAL_ENERGY_CHORD_AND_CUTOFF_TRANSFER_20261015.md) contains the full proof and controls. The [inner-profile note](../notes/02_signed_turning_control/01_INNER_TURNING_PROFILE_20261015.md) explains how the same concentration appears at the smaller spatial scale `x=χ(s)+sξ`. These complementary scales are now integrated into the manuscript.

## The most promising estimate to try next

A useful concrete family would hold for every sufficiently large integer cutoff N:

\[
\mathcal C_j\ge-A E(t,x)e^{aN^2}-B e^{-cN^2},
\qquad a\le a_*<c_0\le c.
\]

All coefficients and the cutoff threshold must come from the complete source and remain locally uniform through possible events. Optimizing N gives an error smaller than √E when the growth rate is strictly below the tail rate. The integer-rounding factor is retained in the proof. Sub-Gaussian growth also works. This makes a broader class of remainder estimates worth considering, but neither a suitable theta decomposition nor the strict rate gap has yet been established.

The next bounded research task should derive **one complete signed identity** for this chord using a relation that couples the theta coefficients. It should identify the favorable term and state exactly how the remainder will be paid. Only then should a certified pilot test the fixed coefficient rule. The cutoff N and the spectral coordinate x are different variables; a cutoff estimate does not automatically settle unbounded spectral coverage.

## What the arithmetic tests changed

Support on the square lattice is insufficient, even with every support-only polynomial localizer and the first source endpoint. A [validated weighted-square control](../notes/05_control_families/01_SQUARE_SUPPORT_ENDPOINT_COLLISION_OBSTRUCTION_20261015.md) has a double collision at time 1/4 near spectral coordinate 44.13035 while retaining positive weights, positive half-line source, and `Φ′(0)=0`. The endpoint normalization can also be imposed. This is a non-theta source; its even extension is only C², and it fails full reflection. A qualitative perturbation restores a positive infinite tail, without providing an explicit numerical perturbation radius.

In contrast, [full reflection rigidity](../notes/05_control_families/02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md) forces a symmetric polynomial-growth weighted integer comb to have constant coefficients. Full source reflection plus the normalized endpoint similarly recovers the theta weights. This is a substantive arithmetic discriminator. It identifies what the support-only relaxation loses, but uniqueness of theta is not yet an inequality for its oscillatory transform. The fiber translation law supplies another form of coefficient coupling; scalar period two alone does not.

The most promising candidates therefore use **full coefficient coupling within the complete signed transform**, with the chord criterion as their measurable target. Increasing a hierarchy that only restricts support will not overcome the known control.

## What the source geometry now supplies

The [complete signed bridge](../notes/03_theta_bundles_and_connections/03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md) expresses the Laguerre and chord observations as exact two-source integrals. In primitive variables the lower endpoint contributes an affine constant. That constant must stay combined with the integral before estimating; otherwise the cancellation relevant to small physical energy is lost.

The [ASD metric classification](../notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md) also corrects the initial concern about cusp growth. Another metric with the same ASD curvature is normalized along the physical path. The restricted connection, and its external two-source product, are flat. Direct tangential curvature therefore supplies no additional sign there. Transverse jet commutators survive and give an exact recurrence; these are included in the manuscript as possible inputs to a future arithmetic identity.

The physical jet surfaces, signed forms and calibrated inclusions remain useful foundations. Their existence alone allows the collision controls, so additional geometric complexity should be justified by a specific improvement in the signed estimate.

## Exploratory routes retained at lower priority

| Route | Established diagnostic | What would justify returning to it |
| --- | --- | --- |
| Period-two contour transport | The complete identity is valid, but the shifted ray and bottom edge have large cancelling terms. Separate absolute sector estimates incur exponential spectral costs. | An estimate that preserves the full packet and its mixed products, with physical-energy scaling. This diagnostic does not rule out coefficients merely locally bounded at each finite height. |
| Natural fiber Hilbert norm | For the particular normalized source lift studied, the norm stays nondecaying while the physical point value decays; the proposed positive-heat Hilbert-valued integral fails. | A different space or a justified procedure that preserves the physical point observation and its decay. |
| Unchanged compact ASD extension | On a compact Kähler surface, a smooth ASD Chern connection and a nonzero holomorphic section force a parallel trivial line bundle, conflicting with degree one on the fibers. | Explicit singular, meromorphic, boundary, or modified-connection data and a demonstrated benefit for the signed estimate. |
| Global Pick or Hermite–Biehler positivity | Such a target may already demand the real-rootedness sought. No suitable new kernel has been proved positive. | A precise kernel and an independently justified positivity mechanism that survives the controls. |
| Outer-domain constants from Investigation 21 | Potentially useful for extending certified spectral coverage, but separate from the small-time collision mechanism. | A bounded computation of the missing constants and a proof joining the covered regions. |

The [contour note](../notes/03_theta_bundles_and_connections/04_PERIOD_TWO_CONTOUR_PACKET_AND_SECTOR_OBSTRUCTION_20261015.md) gives the exact identity and validated checks. The [strategy note](../notes/00_research_coordination/03_PRIORITIZED_SIGNED_BOUND_RESEARCH_PATHS_20261015.md) contains the other diagnostics, their hypotheses and references. Its original proposed support hierarchy and shrinking-window warning are superseded by its continuation notice and the completed results summarized here. These explorations are not extra theorems or hypotheses of the manuscript's main exclusion argument.

## Starting the next chat

Read this overview, the integrated manuscript's chord, complete-source, arithmetic-discrimination and final research sections, and the [integration review](../reviews/04_MANUSCRIPT_INTEGRATION_REVIEW_20261015.md). The [latest detailed research handoff](../notes/00_research_coordination/04_ARITHMETIC_CONTOUR_AND_CHORD_CONTINUATION_20261015.md) supplies the underlying derivations. The first concrete task is to propose a coefficient-coupled full chord identity with an explicit remainder, then test whether its cutoff costs meet the proved transfer criterion.

The existing verification manifests cover 6,897 overlapping exact assertions and 123 validated or mixed assertions across eleven checkers. They support specified algebra and interval calculations; the general collision theorem and reflection rigidity have analytic proofs, and no count is a count of distinct theorems. The [build record](../manuscript/BUILD_RECORD.json) identifies the integrated source and PDF and records its separate manuscript checks.

The conversation keeps its existing formal-replay history identity **18**, as required by the local standing instruction; it is not re-registered in this investigation. Its [canonical history](../../../formal_replay_crosswalk/chat-histories/0018_2026-10-15T11-51-01Z_continue-theta-manifold-research.json) and the [verification checkpoint](../numerics/CHAT_HISTORY_VERIFICATION_20261015.json) provide the handoff provenance. The earlier creation chat remains history 17 in this investigation. A new research chat should normally register here under its own identity. The current reply's final text is captured only after it is actually sent, using the bounded exact-turn follow-up.
