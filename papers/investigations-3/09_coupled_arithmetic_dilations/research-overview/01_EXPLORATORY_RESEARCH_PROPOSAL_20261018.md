# 09: Coupled arithmetic dilation estimates — exploratory research proposal

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6-astra (Codex)**; reasoning effort:
**max**, verified from the authoring turn metadata.

**Status: outlined; research round not yet begun.**

## Research question and intended advance

Can the complete arithmetic dilation relation be estimated in the signed
physical pairing before its large cancelling pieces are separated? The
target is a bound that uses the relation among the shifted field, its lower
interval, and the reflected contribution of the same source.

The first substantive result should treat one finite divisor block on a
stated domain and explain how its cost behaves when blocks are assembled.
The algebra of prime excision and Möbius inversion already exists. Repeating
it, or replacing a complete packet by two individually divergent series,
does not supply the new estimate.

## Exact object to retain

Use the complete theta source and the [packet note's conventions][packets]:

\[
F(t,z)=\int_0^\infty e^{tu^2+izu}\Phi(u)\,du,
\qquad a_d=\tfrac12\log d,
\]
\[
L_d(t,z)=\int_0^{a_d}e^{tv^2+i(z+2ita_d)v}\Phi(v)\,dv,
\]
\[
\mathcal P_d(t,z)=d^{-1/2}e^{ta_d^2-iza_d}
\left[F(t,z+2ita_d)-L_d(t,z)\right].
\]

This is the transform of the divisible-index source
\(D_d\Phi=\sum_{d\mid n}\phi_n\), with
\(D_df(u)=d^{-1/2}f(u+a_d)\). The prefactor, lower interval and shifted
frequency are all part of one observation. Derivatives act on all of them.

For a finite prime set \(P\), the divisor block is
\(\mathcal B_P=\sum_{d\mid Q_P}\mu(d)\mathcal P_d\), where
\(Q_P=\prod_{p\in P}p\). The existing note provides the complete transform,
the lower-boundary cocycle, and source-tail bounds. It also shows that the
separate positive-time Möbius series fail even the term test. The convergence
of their termwise paired difference is the available fact.

The sifted source generally loses even reflection. Its reflected counterpart
must therefore be derived, not asserted equal to it. Likewise, the finite
sieve approximates a sifted source by its first mode; it does not approximate
the full theta transform by that first mode as more primes are removed.
These distinctions are essential to the signed physical transfer.

## Opening research round

1. **Fix the block and the consumer.** Start with one small prime set and a
   declared time range, real-frequency range or strip, and derivative order.
   Choose one existing signed observation, initially \(\mathcal L_0\) or
   the established stationary chord. Record the exact formula connecting
   the complete block to that observation.
2. **Pair before estimating.** Combine the block with the correctly reflected
   expression and retain the boundary cocycle. Keep the complete stationary
   starting factor. If an endpoint approximation is used, state its proved
   error and keep it separate from the unresolved main trace.
3. **Try a joint representation.** Seek a contour identity, coupled integral
   kernel or bilinear form in which cancellation is explicit. Prove its
   convergence and equality to the complete expression before applying a
   norm bound. Compare it with the separate absolute-value estimate on the
   same parameter domain.
4. **Price assembly and degeneration.** State dependence on time, strip
   width, divisor cutoff and every nondegeneracy assumption. Determine which
   estimates survive enlarging the prime set or composing blocks. Record
   explicitly whether the error is absolute, proportional to \(\sqrt E\),
   proportional to \(E\), or requires a lower bound on an auxiliary norm.

One useful restricted bound can justify continuation without solving the
all-event problem. If a lower bound \(E\ge\epsilon\) is assumed, however,
the result does not yet control a collision. Its dependence on \(\epsilon\)
must remain visible. The existing small endpoint remainder does not imply
that the main signed trace has a useful sign.

## What might make the estimate arithmetic

For a weighted source \(\Phi_a=\sum a_n\phi_n\), prime excision carries
coefficient differences \(a_{pn}-a_n\). The constant-coefficient theta
source has an exact family of relations; a generic analytic function in a
strip does not. The estimate should expose how that compatibility interacts
with reflection and the physical observation, rather than merely applying
a universal strip bound to each shifted value.

Three possible bounded experiments are worth distinguishing: one prime with
its exact lower interval; two primes with the composition cocycle; and a
finite block with an explicit omitted-source estimate. Moving to the next
experiment is justified by a new cancellation or an assembly question, not
just a larger cutoff. No experiment has been run as part of this setup.

The [translated-field control][e8] already prevents an automatic estimate of
every auxiliary shifted amplitude by the physical energy: a shifted field
can remain nonzero where \(E=0\). A valid argument must control the specific
paired combination, or prove a new source-specific relation. Defining a
coefficient by division by the vanishing observation is not such a relation.

## Control screen

| Proposed ingredient | Required comparison |
| --- | --- |
| Positive square modes or a support-moment estimate | Weighted three- and four-square controls; identify the coefficient-excision and full-reflection premises they fail |
| Reflection and analytic continuation | Reflected smooth controls; identify the missing normalized square expansion |
| A fixed finite set of prime operators | An Euler-factor modification at an untested prime; show which full coefficient or level premise enters the estimate |
| A generic shifted-field or strip estimate | The colliding heat and translated-field examples; do not assume their shifted norm vanishes with the physical jet |

Use [summary 12][s12] and [Reply 18][reply18] for the actual properties of
each control. A modification at an untested prime is a warning about arguments
using only that finite operator list; it does not establish that every
finite formula using the complete source is powerless.

## Success, useful failure and dependencies

A positive opening result is a signed block estimate with better cancellation
than the declared baseline, or a new relation that makes a previously
uncontrolled trace estimable. To support an infinite assembly, prove a
summable or otherwise justified cost for the complete packets. A finite
improvement alone must retain its finite scope.

A useful obstruction would exhibit a saturating family for a specified block
norm, strip class or pairing, including its actual arithmetic premises.
Divergence after separating packets is already known in [summary 14][s14]
and the [nonlocal audit][nonlocal]; another demonstration is not a new
obstruction to joint estimates.

[08][p08] could provide a joint weighted space; [10][p10] an admissible
auxiliary kernel; [11][p11] a precise collision-scale requirement. This
project can begin without any of them. It differs from [03][p03]'s outer
carrier estimates and [04][p04]'s Sonin mixed-prime response by its complete
half-line arithmetic packets and signed pairing.

The collaborator-facing brief should show the exact block, the two large
cancelling terms, the retained lower boundary, one proposed inequality and
the control that saturates its generic version. Analytic number theory and
complex analysis are the likely areas. Review the opening round as a unit;
continue when it yields a new estimate or a materially informative scoped
failure, not merely more exact bookkeeping.

## Shared scope and research practice

This is an exploratory proposal, not a new theorem, completed experiment or
reviewed research result. The [shared overview][overview] states the common
collision target and classifies its all-event strength. Begin with the
[result summaries][summaries] and [patterns to avoid][avoid]; in particular,
use [criterion classification][a01], [premise-based control screening][a02],
[scoped negative results][a07] and [preservation of paired cancellations][a12].

Save incremental derivations in notes, computations and small records in
numerics, and separate assessments in reviews. Review a coherent research
round, which may contain several notes. Record the actual model, effort,
sources and status in subsequent work. Source links below point to canonical
records; existing results retain the review scope stated in those records.

[Project home](../README.md) · [Proposal index](README.md) · [Source guide](../source-documents/README.md).

[packets]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/11_MULTIPLICATIVE_DILATION_AND_COMPLETE_HEAT_PACKETS_20261015.md
[e8]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/48_E8_CHARACTER_PROJECTION_AND_SIGNED_HEAT_SECTORS_20261015.md
[s12]: ../../../../result-summaries/12_collision_controls_and_screening.md
[reply18]: ../../../investigations-2/active/22_theta_manifold_geometry/reviews/18_REPLY_TO_RESPONSE_17_CLAUDE_20261015.md
[s14]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[nonlocal]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/12_NONLOCAL_ARITHMETIC_MULTIPLIERS_AND_BOUNDARY_OBSTRUCTIONS_20261015.md
[p08]: ../../08_modular_oscillator_estimates/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[p10]: ../../10_modular_auxiliary_functions/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[p11]: ../../11_arithmetic_collision_rigidity/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[p03]: ../../03_effective_outer_remainders/README.md
[p04]: ../../04_sonin_mixed_prime_response/README.md
[overview]: ../../research-overview/02_EXPLORATORY_FIXED_FUNCTION_RESEARCH_PLAN_20261018.md
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
