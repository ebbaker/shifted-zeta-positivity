# The integration contour, observation point and zero enclosure

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual model and effort are
unavailable in branch chat0001's recorded configurations.

**Status: explanatory clarification of the existing B01/E01 geometry.**
No new estimate, execution or change to frozen E01 r1. The
[progress register](../research-progress/01_GNP_BB_RESEARCH_PROGRESS_20261113.md)
retains its task states. Read the [result index](../../../../../result-summaries/README.md)
and [avoid index](../../../../../avoid/README.md), especially
[cluster11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[classification01](../../../../../avoid/01_restating_the_target.md) and
[normalization08](../../../../../avoid/08_normalization_and_constant_slips.md).

The three choices are related but distinct:

| Object | Meaning in the current request |
| --- | --- |
| Γ_X=∂D_X | The integration contour: both horizontal edges y=7/8,9/8 and both vertical edges x=X−1,X+1 |
| p_X=X+ib_X | An interior observation point, with b_X=a_X+1/16; it need not be the rectangle's midpoint |
| a_X and a_X−1/16 | The known upper zero bound and the proposed improved bound at the sampled center; neither is an edge of Γ_X |

The compact target is the vertical segment K_X at x=X between the two
zero-bound levels. On the declared domain L_X≥64,

\[
 7/8<a_X-1/16<a_X<b_X=a_X+1/16<9/8.                 \tag{1}
\]

Thus the contour surrounds both the target and the observation. Its
lower edge lies below the whole target. The observation lies above
the known zero band, so initial containment proves it is nonzero;
the quantitative normalized lower bound remains part of E01.
The contour crosses the old allowed band and is not already known
zero-free merely from that enclosure. E01's complete field estimate
must pay its boundary floor, including the new lower edge and sides.

For u=log|H_λ| the complete Green comparison is

\[
 J_{\lambda,D}(p)=\int_{\partial D}u(\zeta)\,d\omega_D^p(\zeta)-u(p).
                                                               \tag{2}
\]

The contour says **where boundary values are integrated**; p says
**where those values predict the interior logarithm**. The harmonic
measure ω_D^p depends on both. Moving p with D fixed changes the
weights and Green signal. Moving the contour changes the domain's
harmonic measure and Green function. These motions are not tied by
b=B/2. The old strip choice B=8,b=4 was a midpoint convenience;
the general strip formulas allow 0<b<B. See the
[overview's complete formulas](../research-overview/01_GNP_BB_RESEARCH_OVERVIEW_20261113.md#boundary-prediction-and-domain-dependence)
and [inherited lower-offset discussion](../../01_riemann_siegel_evolution/brainstorm/notes/12_GNP_RS_LOWER_TRANSVERSE_OFFSET_AND_LOG_OBSERVATION_20261113.md).

There are also two auxiliary disk constructions in
[Note03 §4](03_GNP_BB_B01_COLLAR_COMPARISON_20261113.md#4-both-consumers-using-exactly-the-same-data).
For the derivative estimate, Cauchy integrates on a circle of radius
1/32 centered at each point q of the inward segment. That full circle
must remain inside the region with a proved value estimate. p_X is the
starting anchor, not the center of every derivative circle. Separately,
the disk of radius 1/8 centered at X+i is used only to lower-bound the
rectangle's Green function. It is neither Γ_X nor a derivative disk.

Use Γ_X for the integration contour, p_X (or b_X) for the observation,
and a_X for the zero enclosure in discussion. At each X, λ_X is held
fixed throughout these spatial constructions. This clarification leaves
the [frozen E01 request](../research-progress/handoffs/GNP-BB-E01-r1.md)
and its hashed sources unchanged; the canonical improvement remains
unproved. Next task/model routing remains E01 / GPT-6.1 Sol.
