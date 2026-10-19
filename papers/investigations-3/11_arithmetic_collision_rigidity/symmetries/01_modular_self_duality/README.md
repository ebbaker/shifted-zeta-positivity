# S01 Modular self duality

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Authoring model **gpt-6-astra (Codex)**, actual effort **max**.
Initial contextual guide; the bounded execution is recorded below.

## Question and role

Can the known full theta self-duality yield a new quantitative estimate for
the retained oscillatory arithmetic sum? This is the accepted question in
the [original symmetry note][brainstorm]. It supplies an arithmetic premise
for the other directions, especially [cutoff reflection][cutoff] and the
[covariant-jet basis][jets]. Read the [program guide][guide] for the shared
baseline, control map, and comparison rules.

## Exact starting point

\[
 \Theta(q)=\sum_{n\in\mathbb Z}e^{-\pi n^2q}
          =q^{-1/2}\Theta(1/q),\qquad q=e^{4u},
\]
\[
 P(u)=e^u\Theta(e^{4u}),\quad P(-u)=P(u),\quad
 \Phi(u)=\frac{P''(u)-P(u)}{16}=\Phi(-u).
\]

The positive physical heat factor \(e^{tu^2}\) preserves source reflection.
It does not turn the oscillatory transform into a positive norm. Within
even real polynomial-growth integer-square coefficients, full normalized
modular reflection forces the ordinary theta coefficients. The [rigidity
section][rigidity] specifies the exact assumptions, including the endpoint
when starting from source reflection instead of the full theta law.

The [modular cancellation section][cancellation] already cancels all
inverse-power endpoint contributions in the complete source transform.
The [shifted representation][shifted] already uses the complete reflected
source before truncation. Recovering either result is background work,
not a new milestone. The still-open quantity is the signed physical
residual and its first jet.

## Read in this order

1. [Original question and control distinctions][brainstorm] and
   [continuation context][context].
2. [Theta source normalization][source], [modular cancellation][cancellation],
   and [coefficient rigidity][rigidity].
3. [Cancellation-preserving approximation and roadmap][shifted].
4. [Current fixed-cutoff error contract][outer] and [S05][jets] when using
   covariant jets. The [theta result summary][summary] routes to older
   parity and endpoint calculations.

## Bounded first task

Choose one complete representation in which the original and reflected
contributions are combined before truncation. Write the exact paired
quantity, including the spectral phase, heat weight, normalizer, and all
boundary terms. Identify a remainder or correlation that the pairing
could make smaller than the existing estimate. Reuse the known contour
representation if that is the chosen representation; specify the new
estimating step rather than relabeling it.

Use the program's bounded comparison domain or another explicitly justified
domain. Derive value and first-derivative errors on a fixed analytic
neighborhood; add the second derivative if the consumer is a Laguerre
margin. Compare the complete error with the current method. A saving in
an endpoint term already cancelled by the baseline is not a saving in
the complete calculation.

The first deliverable is a short contract and paired-remainder derivation.
A numerical comparison follows only when it can distinguish the proposed
estimate from the baseline. An independently proved bound for the paired
sum is the missing research output.

## Controls and decision rule

Finite-prime and finite weighted-square controls fail full reflection.
Reflected smooth, super-Gaussian, and positive-primitive controls preserve
reflection but lack the normalized theta square expansion. Euler-factor
controls lack the unchanged level-one theta coefficients. Use the
[shared control map][guide] and [control summary][controls] to state the
specific failed premise, not a blanket assertion that every control fails
reflection.

Continue for a certified decrease of the complete error, a matched cost
gain, a new signed region, or a precise obstruction to the chosen pairing.
Stop and record the limitation if the derivation gives only source rigidity,
the known endpoint cancellation, or a restatement of nonvanishing. That
decision concerns this proposed use of the symmetry, not all consequences
of modularity.

## First bounded execution, 18 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual reasoning effort ultra**. The [opening derivation][opening] pairs
the signed nonstationary endpoints before taking their absolute value.
It reduces the arithmetic remainder bound by about 37–38% on the inherited
height-1000 complex neighborhood. With the same retained polynomial and
all common costs paid, complete added errors fall by about 14.8%, 7.2%
and 3.0% for orders 0, 1 and 2 on the closed real rectangle.

The [numerical guide][opening-numerics] links fresh 192/256-bit comparisons
and controls; the [internal review][opening-review] records scope and
source identities. This is an approximation-error milestone. The signed
retained-sum estimate and the global bridge remain open. Recompute the
endpoint allowance before transferring the bound to another domain.
The opening chat is registered in [this direction’s history][opening-chat].

## Complete-consumer integration, 19 October 2026

For Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual
reasoning effort ultra**. [Continuation Note 02](notes/02_COMPLETE_PAIRED_TAIL_CONSUMER_AND_STOPPING_DECISION_20261019.md)
integrates the paired order-0–2 tail through a guarded reusable interface
into the unchanged real signed consumer on B. Fresh 192/256-bit runs retain
40 accepted cells and 116 calls; all 40 reported signed intervals and the
minimum margin are identical within each precision. The inherited complete
added-error decrease is reproduced, but no additional paid-margin, cost or
coverage gain is resolved. [Separate internal review](reviews/02_COMPLETE_CONSUMER_INTEGRATION_INTERNAL_REVIEW_20261019.md)
and fresh source-specific controls pass. S01-T1 is complete as integration
and regression validation; stop further omitted-tail tuning on this pilot.
The retained-core signed estimate remains open. See the [task tracker](../research-progress/01_RESEARCH_TASK_TRACKER_20261018.md).

## Outputs and continuation

Add `notes/`, `numerics/`, and `reviews/` here when the first new output is
produced. Record actual model/effort, source hashes, domain, paid derivatives,
complete error comparison, and controls. Return a useful paired estimate
to S02 or S03, or a specific failed comparison. Existing canonical sources
stay at their linked paths. Apply the [program storage and history rules][guide].

[guide]: ../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[brainstorm]: ../../brainstorm/01_SELF_DUALITY_AND_ADDITIONAL_SYMMETRY_QUESTIONS_20261018.md
[context]: ../../brainstorm/02_SYMMETRY_PROGRAM_CONTINUATION_CONTEXT_20261018.md
[source]: ../../manuscript/positive_arithmetic_packets/sections/01_theta.tex
[cancellation]: ../../manuscript/positive_arithmetic_packets/sections/04_modular_collisions.tex
[rigidity]: ../../manuscript/positive_arithmetic_packets/sections/05_controls.tex
[shifted]: ../../notes/06_CANCELLATION_PRESERVING_APPROXIMATION_AND_NEWMAN_ROADMAP_CODEX_20261018.md
[outer]: ../../manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex
[summary]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[cutoff]: ../02_cutoff_reflection/README.md
[jets]: ../05_covariant_theta_jets/README.md

[opening]: notes/01_PAIRED_ENDPOINT_REMAINDER_AND_BOUNDED_COMPARISON_20261018.md
[opening-numerics]: numerics/README.md
[opening-review]: reviews/01_PAIRED_ENDPOINT_INTERNAL_REVIEW_20261018.md
[opening-chat]: chat-histories/0001_2026-10-18T23-47-36Z_begin-modular-self-duality-work.json
