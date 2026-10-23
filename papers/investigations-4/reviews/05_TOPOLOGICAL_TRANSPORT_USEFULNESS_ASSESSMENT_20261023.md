# Usefulness of the topological transport formula

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**. Same-assistant assessment, without independent specialist review.

**Assessment: no competitive improvement in a zero-free region, event bound, or verification cost has been established by the focused manuscript.** Its stated analytic estimates remain useful descriptions of boundary pieces. Their potential novelty does not establish their usefulness for the author's chosen goal. Further manuscript polishing should follow a successful quantitative comparison, rather than precede it.

This review concerns [Topological Zero Transport and the Phase of the Discriminant](../manuscript/topological_zero_transport/README.md). It supplements the [literature/proof review](04_TOPOLOGICAL_TRANSPORT_LITERATURE_AND_PROOF_REVIEW_20261023.md) with the more demanding question of what the formula buys. It follows the [result index](../../../result-summaries/README.md), [heat-flow benchmarks](../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [avoid index](../../../avoid/README.md), and the patterns concerning [separate bounds](../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [unproved novelty](../../../avoid/16_unchecked_imports_and_novelty_claims.md), and [volume without a gain](../../../avoid/20_volume_without_a_gain.md). This is a comparative assessment and an exact consequence of an existing identity, not a new RH criterion.

## The estimates in one place

In the manuscript's large-heat regime, let L~log(T)/4, kappa~8TL, K=o(L sqrt(kappa)), and eta_T=(K+1+L²)/(L sqrt(kappa)). Use a fixed imaginary width Y, physical disk radius r/L, and a consecutive population of m<=K roots. All integrals use the unchanged jet (H,H_z).

| Contribution | Established estimate | What it buys for event exclusion |
| --- | --- | --- |
| Full terminal cap I_T | I_T/m tends to r²Y/pi; the finite error is in Theorem 1.1. | A controlled nonzero endpoint, but no bound on the whole event boundary. |
| Vandermonde part | Per root, O(r² eta_T/L²). | Identifies a small component. It is not the leading physical cap. |
| Analytic-factor part | Same leading limit as the full cap. | Retains the common phase missing from root positions alone. |
| Projective spatial walls | Exactly zero for a constant radius along each regular tube. | Removes these walls without estimating root speed. |
| Each imaginary face on [theta T,T] | Per root, O(1/L), with the signed leading coefficient given in Theorem 1.1. | Bounds a late regular piece, outside the possible real-event regime for sufficiently large T. |
| Imaginary faces attached to a fixed event core, with Y=S/L² instead | Each tends to Q/2, with error O((B+m)/L²), for fixed core and population. | Locates the surviving charge; does not bound Q independently. |
| Complete boundary starting at zero | Exact integer balance. | No new nontrivial independent upper on Q is supplied. |

The last fixed-core row uses a different width limit from the preceding rows. These estimates cannot be combined as if they had the same geometry. A bound per root also need not be less than one after multiplication by a growing population; integer-valued topology alone cannot turn relative smallness into event exclusion.

## The cancellation that should be used before any estimates

Let E_(a,T) be the sum of the two outward imaginary-face integrals on regular root tubes over [a,T]+i[-Y,Y]. With the same population and the same projective radius at both ends, manuscript equation (2.9) gives

\[
\boxed{I_T+E_{a,T}=I_a.}
\tag{U1}
\]

This is exact, not an asymptotic near-cancellation. The tube contains no joint zero, and its projective wall has zero flux. The complete boundary degree is therefore zero. Adding such a tube to an early event domain cannot change that domain's charge.

Write B_early for all its other oriented faces, including the negative initial cap and the joining complement. Then

\[
Q=I_T+E_{a,T}+B_{\rm early}=I_a+B_{\rm early}.
\tag{U2}
\]

Consequently, estimating I_T and E_(a,T) separately introduces a conditioning problem that the exact identity removes. Moving T farther out does not improve this complete event balance by itself. If the chosen radius depends on T, the attachment disks and their complements must change together; (U1) remains valid for each individual geometry.

This explains a real cancellation, but it leaves the early signed integral to estimate. It is not an impossibility theorem for using late information: a new propagation inequality could transmit additional information to that earlier boundary. The present manuscript provides no such inequality.

There is also a direct proof-dependency point. The full cap estimate is obtained from the complete-source estimate for the product of H_z at the roots. Its proof and the late-edge proof do not require the Vandermonde perturbation lemma. That lemma supplies the separate pair-component estimate. Thus the draft has not shown that the Vandermonde decomposition makes the complete cap easier to bound than its existing direct scalar representation.

## What the literature already supplies

The [argument principle, DLMF 1.10.9](https://dlmf.nist.gov/1.10.E9), already turns a signed boundary integral into an integer count. Our [earlier complete-boundary calculation, equations (5) and (7)](../notes/03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md) reduces an ordinary-event domain to the winding of its critical value, including the corner and wall cancellations. In that declared local geometry it has the same winding as the discriminant. An equally informed direct method can use this scalar formula. This is a reduction in representation, without a demonstrated estimating advantage.

[Rudolph's paper](https://arxiv.org/pdf/0912.4974), Section 1, explicitly studies fiber integration of Whitehead's Hopf formula. Thus neither integer conservation nor reduction from a three-form to a one-form is a new general principle here. The possible originality is confined to the particular quantitative realization, and remains unconfirmed.

[Polymath](https://arxiv.org/html/1904.12438), introduction and Theorem 1.5, records reality of all zeros for heat time at least 1/2 and proves positive-time high-height reality/localization in the regime x>=exp(C/t). Our T-to-infinity estimates lie inside an already all-real regime. Their detailed cap asymptotics may be new, but they cannot themselves enlarge its off-real zero-free region. The small-heat transition is the relevant comparison problem.

[Rodgers–Tao](https://arxiv.org/html/1801.05914), Sections 7–8, subtract the equilibrium value and its linearization before estimating interactions. Convexity and controlled evolution contribute to their proof of Lambda>=0, under the contradiction assumption Lambda<0. Their localization and exterior interactions belong in our comparison. This is an existing successful coupled mechanism, not an RH proof.

The Ricci-flow analogy identifies the kind of ingredient missing: a quantitative quantity controlling deviation and its evolution. [Perelman's entropy paper](https://arxiv.org/abs/math/0211159) supplies such monotonicity and geometric control in its own setting. The present zero flow satisfies H_t=-H_zz, backward heat in the spatial variable; its late ordering does not automatically import forward geometric smoothing or an entropy inequality.

The field is not exhausted. [Bellotti–Trudgian–Yang, March 2026 preprint, Theorem 1](https://arxiv.org/html/2603.21490v1) gives zeta(sigma+iu) nonzero for u>=3 and sigma>1-1/(4.896 log u), using a more effective combination of symmetry and smoothing in classical zero detectors. The strict inequality here follows the theorem text. This is a contemporary benchmark, not a claim to have audited its proof or identified the strongest region at every height.

## The refined backward-time direction

The author clarified the intended smoothing as reversed real heat time, with an extremely small displacement epsilon(h) that shrinks with height. [Note 13](../notes/13_HEIGHT_DEPENDENT_BACKWARD_HEAT_CONTOURS_20261023.md) derives the complete curved-collar identity

\[
I_0=I_\varepsilon-S_\varepsilon+Q_-\ge I_\varepsilon-S_\varepsilon.
\]

Here S_epsilon includes every outward connecting face and Q_- is the nonnegative degree enclosed in the negative-time collar. Thus a lower-bound consumer does not require an event-free negative-time region. However, those events can weaken the available bound, and the cap's slope contributes explicitly to its pullback. The scale epsilon(h)=c(h)/ell(h)², ell(h)=log(h/(4pi))/4, is a first microscopic normalization to examine; it is not a proved collision-free rule or a theta estimate.

This gives the next comparison a concrete geometry: estimate I_epsilon-S_epsilon together and compare its certified lower bound with direct estimation of I_0 using the same source data. The ordinary heat kernel and degree identity are established tools. An advantage from their use on this contour remains unproved, so the assessment above is unchanged.

## Exact controls and scope of the assessment

For the shifted quadratic heat solution H=z²-2(tau-t_*), choose 0<t_*<a<T and epsilon²<2(a-t_*). Its regular two-root cap is

\[
I_b=\frac{k_\epsilon}{\pi}\arctan\frac{Y}{b-t_*},\qquad
E_{a,T}=\frac{k_\epsilon}{\pi}
\left(\arctan\frac{Y}{a-t_*}-\arctan\frac{Y}{T-t_*}\right).
\]

Their sum is I_a exactly, while an attached core enclosing (t_*,0) has charge one. The stationary sine heat solution has a nonzero cap entirely in the analytic factor and a constant Vandermonde. These analytic substitutions test both cancellations without another numerical campaign.

The [collision-control register](../../../result-summaries/12_collision_controls_and_screening.md) limits broader conclusions. Generic heat geometry accepts the Euler-factor, weighted-square, reflected, and positive-primitive controls. They fail different canonical-source premises: unchanged coefficients, full normalized reflection, or the unchanged integer-square expansion. No new source-specific inequality is proposed in this review that rejects their event-containing domains. Their survival does not rule out a stronger coupled canonical estimate.

## The next result that would justify further manuscript work

The next research deliverable should be one signed or relative inequality that estimates the complete difficult residual after exact cancellations, with its domain, source information, constants and endpoint costs stated. The author's height-dependent negative-time collar is a concrete geometry for this test. The comparison must permit the direct method the same source data, Gaussian smoothing, critical-value/discriminant reductions and signed correlations.

An improvement could be a larger proved zero-free region, a lower effective height threshold, or a substantial reduction in the data or cost needed for the same certified region. An elementary proof under meaningfully weaker hypotheses could also have independent value. No such advantage has yet been demonstrated for this manuscript.

For the author's ultimate goal, an improvement for H_t at small positive t is an intermediate result; it does not automatically give a region for H_0 or for zeta. The relevant propagation and boundary payments must be proved. The present recommendation is to leave both manuscripts intact and make this comparative estimate the next research priority. The current mathematics clarifies the location of the difficulty, but does not establish that the zero-free-region problem has become easier.
