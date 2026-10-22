# RTD-02: support rejection, controls and the matched comparison

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Coordinating model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**, verified from current turn metadata. This is bounded implementation research and a scoped estimator comparison. Numerical results and disposition are appended below only after execution.

Read the [result index](../../../../result-summaries/README.md), [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), [local geometry](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), and [avoid index](../../../../avoid/README.md), especially [01](../../../../avoid/01_restating_the_target.md), [07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md). The [fixed contract](01_BOUNDED_SUPPORT_COMPARISON_CONTRACT_20261022.md) discloses that the inherited data already predict this support-empty result. The low-height box is already classified within Polymath/Platt–Trudgian coverage in [prior Review 16, §9](../../../investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md) and avoid/11. The present arithmetic justification is the inherited complete-source certificate, not an inference from initial zero verification alone. The invariant is inherited; the scientific question here is the complete acquisition comparison.

## A normalized density with a paid collar

Use the contract's r=10^-9 and b=3r/2 and the physical map F=(H,H_x), oriented by dt wedge dx. Put s=|y|²/r² and g(s)=exp[-s/(1-s)] on 0<=s<1, zero on s>=1. Then

\[
 \rho_r(y)=-\frac{g'(s)}{\pi r^2}
 =\frac{e^{-s/(1-s)}}{\pi r^2(1-s)^2}\quad(s<1)
\]

and rho=0 otherwise. Exponential flatness gives a smooth extension at s=1; composition with |y|² is smooth at the origin. Polar integration gives integral rho=-integral_0^1 g'=1. Its support is the closed radius-r disk, a compact subset of B_b. These two radii avoid confusing support in an open ball with a density whose support meets that ball's boundary. Its maximum is 4/(e pi r²), attained at s=1/2; a global Lipschitz bound is 512/(e³ pi r³). To see it, set z=(1-s)^-1>=1: the scalar derivative is e^(1-z)z³(2-z), use |2-z|<=z and max z⁴e^(1-z)=256/e³, then differentiate s with respect to y. Thus gradient scaling is r^-3. Such amplification must be paid on active cells, even though it does not enter support-empty cells.

Let E=|F|² and beta=(H dH_x-H_x dH)/E. The form

\[
 \alpha=[1-g(E/r^2)]\beta
\]

is smooth at E=0: its scalar coefficient divided by E tends to r^-2. Since det D_(t,x)F=-L1 and dE wedge beta=-2L1 dt wedge dx,

\[
 d\alpha=-2\pi\rho_r(F)L1\,dt\wedge dx.
\]

On the boundary E>b²>r², alpha=beta. Stokes reproduces the existing integral K(D), with no limiting regulator. This is a specialization of the classical degree formula, not a new invariant or signed theta estimate. [Guillemin–Haine §3.6, Theorem 3.6.4 and its proof](https://math.mit.edu/classes/18.952/spring2013/docs/book.pdf), pp. 128–129, was consulted for the proper-map pullback convention. The proof above supplies this density's specialization.

## Scoped comparison theorem

Suppose each cell C receives the same validated first-jet range set R_C, with F(C) contained in R_C. Use the same subdivision tree. If support rejection accepts C by proving R_C misses the closed radius-r disk, then 0 is not in R_C. The identical data therefore certify direct nonvanishing on C. The direct rule can stop at least as early. The argument includes rejected-parent costs: every branch continued by the direct rule must also be continued by the stronger support rejection rule. For Cartesian intervals, a strict sign of one coordinate certifies direct nonvanishing; a coordinate margin greater than r certifies support rejection and also bounds |F|.

This proves a dominance statement only for **support rejection from the same complete range sets and subdivision tree**. It says nothing against active-cell signed integration, cancellation, correlated source information, acquisition amortization, other domains or other target densities. An exact zero integral obtained by support rejection may still be a useful implementation check. It supplies no stricter collision-count allowance than the same cells' direct exclusion. An integral's exact output [0,0] must not be compared to an artificially weakened noninteger winding enclosure: exact winding zero also gives K=0.

## Controls and source-premise audit

The degree identity must retain collisions. It is not intended to reject a collision control. The analytic controls below test signs and payments; polynomial checks exercise the real multiplicity law, not the complex intersection weight.

For H=x²-2t, F=(x²-2t,2x) is a global diffeomorphism of orientation -1, with inverse x=y1/2, t=y1²/8-y0/2 and L1=4. On D_R=F^-1(B_R), R>r, ordinary change of variables gives integral rho(F)L1=1. For a Gaussian it gives

\[
 I_\lambda=1-e^{-\lambda R^2},\quad
 (2\pi)^{-1}\oint_{\partial D_R}e^{-\lambda E}\beta
 =-e^{-\lambda R^2}.
\]

Thus I_lambda<1 on a domain that really contains a collision. The correction restores K=1; dropping it would make the proposed threshold test false. A boundary containing the event must be refused, rather than assigned a fraction of its weight. For H=x³-6tx, L1=18x²+36t, which is negative at t<0,x=0, so generic heat fields cannot justify deleting signed terms. The negative point even lies inside the support when r=1/2: F(-1/100,0)=(0,3/50). On D=(-1,1)² the boundary floor is at least sqrt(2): on either spatial wall the two signed coordinates differ by two; on the time faces |H_x| is at least three. Choose b=3/4 to pay the collar. The full compact integral remains one, despite its negative region. H=x is a collision-free control. An open positive-time domain misses an event at t=0.

The [control register](../../../../result-summaries/12_collision_controls_and_screening.md) supplies the separate arithmetic controls and their already established status:

| Control class | Preserved properties relevant here | Premise absent from the unchanged theta supplier |
| --- | --- | --- |
| Euler-factor | Positive even source, heat equation, substantial completion/arithmetic structure | Original normalized theta coefficients/source change; source has shifts |
| Weighted-square and finite-prime | Positive square support and selected endpoints, prime identities or measurements | Full normalized reflection fails for those constructions; finite-square cases have no all-real heat slice |
| Reflected super-Gaussian | Positive even entire source and strong reflection/primitive properties | Unchanged normalized integer-square theta expansion |
| Smooth shape and positive primitive | Positivity, strong decay/shape and specified primitive completion data | Unchanged arithmetic square expansion |
| RH-conditional close endpoint | All-real positive-time behavior and close normalized source data, with endpoint doubles | Ordinary Dirichlet-series arithmetic; also the pilot covers only t>=1/100 |

This is a matched-premise audit of the proposed finite implementation, not new acquisition of every arithmetic control event. No control is declared rejected. Their generic degree identities remain valid on regular enclosing domains. No numerical check here supports the RH-equivalent global exhaustion or an endpoint simplicity claim.


## Active-support error contract retained for a different comparison

No active-cell estimate is acquired in this support-only opening. If H_j=h_j+delta_j with |delta_j|<=epsilon_j, put ell=h_2²-h_1 h_3 and epsilon_F=(epsilon_0²+epsilon_1²)^(1/2). Then

\[
 \Delta L=2|h_2|\epsilon_2+\epsilon_2^2+|h_1|\epsilon_3
          +|h_3|\epsilon_1+\epsilon_1\epsilon_3,
\]
\[
 |\rho(F)L1-\rho(h_0,h_1)\ell|
 \le {4\over e\pi r^2}\Delta L
       +{512\over e^3\pi r^3}\epsilon_F|\ell|.
\]

Use complete cell suprema, including all source and interpolation errors. Alternatively, integrating a complete full-cell interval range times the cell area is rigorous without a separate quadrature remainder; signed sums and any unresolved support crossings must remain. These estimates identify the active implementation's actual error burden. They are generic bookkeeping and supply no new source discrimination or theta allowance.


## Executed fixed comparison

The [standalone checker](../numerics/check_real_thom_support_pilot.py) replays the complete source and all three consumers; the [small execution record](../numerics/REAL_THOM_SUPPORT_PILOT_20261022.json) contains outward interval values, fixed parameters, supplier/checker hashes, cell intervals, controls and implementation timings. Both the inherited and the copied supplier are retained; the documented invocation verifies the inherited supplier hash.

| Consumer | Complete range/vertex acquisitions after shared source setup | Complete outcome |
| --- | ---: | --- |
| Practical full-boundary winding | 464 segment ranges +234 vertices =698 | Winding exactly zero, hence K=0 |
| Direct full-time interior strips | 255 ranges, 128 accepted strips | Complete direct exclusion, hence K=0 |
| Compact support rejection, collar shared with cover | 255 ranges, 128 accepted strips | Signed integral exactly [0,0], hence K=0 |
| Compact support with a separately acquired boundary floor | 464 floor ranges +255 support ranges =719 | Same exact zero; vertices are unnecessary for the floor |

All share 76 complete midpoint integrals, source modes n<=4 and u<=1 with both complete tails, and the same Taylor enclosure. This opening requires no extra Hxx/Hxxx acquisitions: no cell meets support. The full replay performs 1,208 consumer enclosures because it runs the winding and both interior algorithms separately. An additional single midpoint enclosure is used only by the injected-error diagnostic (1,209 including that diagnostic). This experimental total must not be charged as the standalone cost of each consumer. The optimized compact cover itself validates the boundary collar on the closed rectangle, so the floor is paid once and its additional acquisition cost is zero.

The certified boundary coordinate floor is greater than 1.9066820356e-9. Both full-time covers have a certified floor greater than 7.0703012359e-9, exceeding the fixed b=1.5e-9 and r=1e-9. The complete midpoint source-tail bound is below 3.729e-33 and the Taylor remainder per component below 4.923e-17. These are complete interval conclusions, not values read from samples. The density's cutoff crossings, large derivatives and signed multiplication need no numerical approximation here because the complete range proof makes the integrand identically zero.

The actual four-edge Gaussian regression uses H=x²-2t on (-1,1)², lambda=1. It encloses I in a narrow interval around 0.98862876835135463062 and its full signed boundary correction around -0.01137123164864536938; their difference encloses one. This is separate from the exact target-preimage analytic control above. Exact rational Sturm controls for m=2 through 12, both overall signs, validate the real weights floor(m/2). Support hits, unresolved boxes, nonzero points inside support and the actual midpoint jet with an injected absolute error M return inconclusive; an exact boundary event is refused. Refinement-limit exceptions are failed/inconclusive runs, not certificates. The separate [same-model internal assessment](../reviews/01_OPENING_SUPPORT_COMPARISON_INTERNAL_REVIEW_20261022.md) records replay and corruption checks; this is not external specialist validation.

## Disposition and next gate

**Stop the specified support-rejection pilot as a source of improvement over its same-information direct interior comparator.** It achieves neither a stricter allowance nor fewer acquisitions. The scoped comparison theorem already explains this before numerical replay; the run verifies implementation and cost accounting on the inherited source. It has fewer enclosures than this particular polygon winding implementation, but that is not a demonstrated practical advantage once the 255-call direct comparator is included. Implementation timings are recorded only as machine/run observations, not evidence of a general speed theorem.

RTD-01 and the support-only part of RTD-02 are complete; RTD-03 receives the separate internal review. Active signed bulk integration remains **unimplemented and unstarted**. A further research comparison needs an explicit active-support domain/density and a prospective complete source/error and cost contract that makes active integration informative. Merely reducing r on the same already excluded cells will not supply that benefit. Other domains, densities, coupled estimates and active signed integration remain open. No endpoint treatment, new theta region, global coverage, RH estimate or simplicity result is claimed.
