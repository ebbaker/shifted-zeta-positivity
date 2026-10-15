# Arithmetic and contour pilot: a stronger chord target and two rejected relaxations

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata. Three collaborating tasks and the coordinator derived and reviewed the results. This is incremental research; the stable manuscript is unchanged.

## Main outcome

The two bounded experiments from the [strategy note](03_PRIORITIZED_SIGNED_BOUND_RESEARCH_PATHS_20261015.md) are complete. The square-support relaxation fails even when the first source reflection endpoint and primitive normalization are retained. The period-two identity closes exactly but its independent contour sectors incur exponential spectral-height costs. Neither experiment supplies a signed theta estimate.

The positive advance is a more permissive collision-exclusion target. For the pi/4 chord

\[
 \mathcal C_j(t;x,y)=h_j(t,x)[h_j(t,y)-h_{j+1}(t,y)],
 \qquad e=E(t,x)=H(t,x)^2+H_x(t,x)^2,
\]

at full stationarity `h_(j+1)(t,x)=0`, any locally uniform lower bound

\[
 \boxed{\mathcal C_j\ge-o(\sqrt e)}
\]

on every sufficiently short interval where `h_j` is nonzero excludes every finite analytic collision. In particular, an error `K e^gamma` with fixed `gamma>1/2` and locally bounded K suffices. The little-o is uniform in the declared admissible endpoints through each candidate event. Coverage must include a fixed nearby endpoint, not only windows shrinking at a specified rate.

To see the obstruction, keep `y=a+delta` fixed near a collision `(T,a)`, let `x=chi(T-t)` be the full stationary predecessor, and choose delta small enough. The [chord note](../02_signed_turning_control/02_CENTRAL_ENERGY_CHORD_AND_CUTOFF_TRANSFER_20261015.md) proves that the whole interval stays zero-free and

\[
 \frac{\mathcal C_j(t;\chi(T-t),a+\delta)}{\sqrt{E(t,\chi(T-t))}}
 \longrightarrow-c_\delta<0.
\]

The exponent one-half is independent of collision multiplicity. This is stronger than the previously observed fixed-inner-window defect, and supports a wider class of permitted error estimates. The result is a sufficient criterion; no bound of this form has yet been proved for the theta source.

## What each experiment establishes

| Workstream | Established result | Consequence |
| --- | --- | --- |
| [Chord and cutoff transfer](../02_signed_turning_control/02_CENTRAL_ENERGY_CHORD_AND_CUTOFF_TRANSFER_20261015.md) | Inner, parabolic and fixed-endpoint collision tests; physical energy at the starting point is essential | Prefer the chord target when available estimates tolerate a power loss between square-root and linear energy |
| [Square-support collision control](../05_control_families/01_SQUARE_SUPPORT_ENDPOINT_COLLISION_OBSTRUCTION_20261015.md) | Fixed positive weights on three squares collide at T=1/4, x in (44.1303,44.1304), while Phi'(0)=0 and normalized psi'(0)=psi'''(0)=-1/2 | Increasing only the degree of square-support localizers cannot establish collision exclusion for the relaxed class |
| [Reflection rigidity](../05_control_families/02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md) | Polynomial-growth square coefficients plus full modular reflection are constant; normalized physical reflection forces the ordinary theta weights | The control is rejected by genuine coefficient coupling, but input uniqueness is not a signed inequality |
| [Period-two contour packet](../03_theta_bundles_and_connections/04_PERIOD_TWO_CONTOUR_PACKET_AND_SECTOR_OBSTRUCTION_20261015.md) | Complete ray/edge identities and all bilocal products; individual sectors grow exponentially and cancel | Retain the identity, discontinue independent-sector estimates unless a new cancellation-preserving bound is supplied |

The arithmetic control has an analytic extension to strictly positive weights at every square node. This gives a genuine full-support obstruction to support-only constraints; the extension does not come with a numerical epsilon threshold. Its third source odd derivative is nonzero. It is not the even theta source and does not satisfy the full modular or elliptic relation.

## A wider allowable cutoff family for chords

The common all-N family

\[
 Q\ge-Ae\exp(aN^\beta)-B\exp(-cN^2)
\]

with locally bounded nonnegative coefficients, c bounded below, a uniformly bounded cutoff threshold, and `beta<2`, excludes collisions for both the stationary Laguerre and uniformly covered chord targets. Its optimized relative loss is subpower.

For the fixed-endpoint chord criterion, Gaussian cost `beta=2` can also be admitted when fixed local bounds satisfy `a_*<c_0`. Choosing the integer cutoff of order

\[
 \sqrt{\log(1/e)/(a_*+c_0)}
\]

gives a loss `e^(p+o(1))`, where `p=c_0/(a_*+c_0)>1/2`. The integer rounding only contributes a subpower factor. The gap between the growth and tail constants must persist locally; pointwise inequalities with a closing gap are insufficient.

The exact quadratic collision shows why equality cannot be admitted without further information: it satisfies a family with `a=c=1`. The same control shows that paying the chord by endpoint energy, or by the sum of starting and endpoint energies, is not equivalent to paying by starting energy.

This corrects the scope of the earlier strategy warning: a fixed inner scaled window has only a finite chord/energy limit, but the proposed all-short-interval statement also covers parabolic and fixed-endpoint windows, which yield stronger obstructions.

## Verification and limits

The [execution manifest](../../numerics/ARITHMETIC_CONTOUR_CHORD_CHECKS_20261015.json) binds the four new checkers, execution receipts and research/review notes to hashes. The chord and reflection-algebra replays use exact rational arithmetic. The square-source and complete-theta contour replays use Arb/Acb with explicit analytic tails. The [review](../../reviews/03_ARITHMETIC_CONTOUR_AND_CHORD_REVIEW_20261015.md) separates those finite computations from the analytic theorems.

The square-source certificate proves a collision for the declared control, not for theta. The contour record proves bounded identity enclosures with full series/ray tails, not chord positivity at stationary points. The fixed-endpoint exclusion and reflection rigidity are analytic proofs reviewed internally. No new theta sign domain, global zero statement or RH conclusion is asserted.

## Next bounded research step

Use the starting-energy chord target with an allowable error `o(sqrt(E))`; do not insist on exact nonnegativity if a weaker remainder is accessible. Seek a full two-source identity that combines stationarity with a genuine relation between theta coefficients, such as elliptic translation or modular reflection. Apply any absolute estimates only after the signed combination has been formed.

For a finite relaxation, adding the next source endpoint condition is a concrete discriminating test: the three-mode control fails Phi'''(0)=0. A fresh control search must accompany that addition. One failed control does not prove that a larger finite endpoint hierarchy is sufficient, and this turn does not prove that every such hierarchy fails. Merely increasing the support-gap degree would leave the current control admissible and has no benefit for the stated relaxation.

The period-two packet can support such a calculation if it retains all edge and mixed terms. Its sector asymptotics are a reason to reject a proposed estimate that pays those terms independently. Effective outer-domain coverage in Investigation 21 remains a separate route to finite, measurable progress.
