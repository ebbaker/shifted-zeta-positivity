# Geometry and exceptional row research directions

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning
effort are not exposed and are not inferred.

## Assessment

The most promising next estimate concerns simultaneous inverse and plain
witness saturation in a small, specified family of exceptional rows.
The strongest geometric alternative is a coherent combination of probes
with the same principal signal, retaining their mixed errors. The repo
supplies useful exact identities and counterexamples for designing these
tests. It does not already prove the required character-family estimate.

The [current extension](GEOMETRY_OPTIMIZATION_20261008.md) and its
source-scoped audits remain conditional on the structural inputs of the
[September 30 paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf).
This research map adds no zero-free theorem. Numerical values below are
diagnostics, not new interval certificates. They are reproduced by
[the sensitivity calculation](../numerics/bottleneck_sensitivity.py) and
its [small record](../numerics/bottleneck_sensitivity.json).

## Continuation results

The [localized next-target note](LOCALIZED_JOINT_WITNESS_TARGET_20261008.md)
now gives a precise conditional payoff. The full amplitude profile and
cutoff retuning remove part of the hard class using the existing moments.
The remaining input is localized to nearly saturated profiles with
`0.36 <= delta <= 0.42` and `0.49 <= q/delta <= 0.50`.
The [joint-witness derivation](JOINT_WITNESS_REDUCTION_20261008.md) shows
that the smaller object `|M S Q|^2` is sufficient; it is preferred to the
schematic mixed sixth moment discussed below. A uniform mixed saving of
`1/5000` would suffice for the next target after both rebalances, but has
not been proved.

The [probe scout](COMMON_SIGNAL_PROBE_SCOUT_20261008.md) constructs two
admissible common-signal responses and their mixed kernel; one-mode
cancellation gives no automatic uniform power gain. The
[off-balance calculation](OFF_BALANCE_GEOMETRY_SCOUT_20261008.md) retains
a dual-length cost that worsens the low boundary near the present geometry.
The remainder of this note records the original research map and its
motivating identities. The current conditional candidate is unchanged.

## Locate the actual obstruction

At the limiting point for fixed \(b=1/8\), the dangerous bin has
\(\delta\simeq0.386688531\), \(x=q/\delta=1/2\), and
\(R^*\simeq0.668416969\). The optimized detector cutoff is
\(t\simeq1.12337656\). The short-witness crossing has inverse length
\(r\simeq0.71498767\) and plain length \(m\simeq0.40838889\).
Here lengths are logarithmic exponents relative to row scale \(U\).
The competing long branch has worst inverse length \(r=t\).

The selected-prime capacities at the short crossing are approximately
\(z_M=0.14250617\) and \(z_P=0.04071605\), while available physical
length is \(\ell/h\simeq0.20527403\). Additional supply alone therefore
does not remove the obstruction. The first inverse-width condition
\(r+2z<1\) is active. The second, \(2r+8z<3\), has slack approximately
\(2r-1=0.430\) at the first capacity boundary.

A useful missing theorem would improve the relevant joint exceptional
set by

\[
\#\mathcal B(\delta,q;U)
\ll U^{R^*(\delta,q)-\eta+\epsilon},\qquad \eta>0,
\]

in a neighborhood of this bin. The high exponent improves exactly by
\(h\eta\). Locally, after retuning \(\ell\), the boundary gain is about
\(0.152469\eta\). This derivative is guidance for selecting a target,
not a globally certified payoff. Existing strict margins must be
certified outside the selected neighborhood.

## First priority retain inverse and plain dependence

The source already combines each witness with selected prime slots.
What remains unused in the marginal comparison is the full dependence
between inverse and plain witnesses. Proposition 8.3 produces both for
the same character presentation and twist height. Proposition 19.2
estimates a marked inverse second moment and a marked plain fourth
moment separately, then uses the better bound.

A concrete investigation is a mixed moment or direct restricted count
for simultaneous saturation of both witnesses and the physical prime
slots. A schematic object is

\[
\sum_{u\in\mathcal U}|M_r(u)|^2|S_m(u)|^4
                  \prod_{i\in I}|Q_i(u)|^2.
\]

Its admissible coefficients, product caps, zero extensions, and common
character must be derived before estimating it. A square-root-size
generic bound cannot be assumed: already \(r+2m\simeq1.5318>1\),
before prime slots are included. Multiplying marginal probabilities or
applying Holder to existing separate bounds supplies no independence.
A gain on one of the competing branches can still improve the final
envelope after the cutoff is rebalanced; it must not be counted as a
gain on both branches without calculation.

The repo's [arithmetic overlap analysis](../../prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/ARITHMETIC_OVERLAP_20261004.md)
is strong motivation: for its actual arithmetic coefficients, an isolated
semiprime sector exceeds every fixed-saving budget even after projection,
so the cofactor/semiprime cross term is compulsory. That theorem concerns
a different observable; it suggests where to look for lost information,
and supplies no estimate for the present character rows.

The [six-factor response](../../prime-variance-exponents/notes/programs/05_higher_multilinear_identities/PRELIMINARY_INVESTIGATION_20261004.md)
provides a second template: an exact retained combination
\(H_3-3H_2+3c_wM_1(Y)x\), with cross-Gram and scalar conditions.
For the ideal character problem, derive a complete truncated
inverse--plain convolution before splitting into dyadic witness pairs.
The cancellation identity \(\mu_K*1=\epsilon\) is exact, but truncated
windows leave boundary terms. All product caps and continuum corrections
must remain. An identity alone does not give the missing power bound.

## Cheap preparation keep the full amplitude profile

The source reduces a physical amplitude vector \((g_i)\) to its weighted
mean \(q=\sum\ell_i g_i/\ell\). A decreasing rearrangement gives a
selected-subset gain \(G(z)\ge qz\) at available length \(z\), up to
the already-budgeted whole-slot mesh loss. Using the actual \(G(z)\)
can improve the comparison away from flat profiles.

At the current obstruction, however, \(q=\delta/2\) and each
\(g_i\le\delta/2\). Thus every positive-length slot is saturated;
rearrangement gives no gain there. The useful outcome is to reduce the
new analytic theorem to a nearly flat, simultaneously saturated class.
This is a tractable preparatory calculation, not the endpoint solution.

Another possible refinement is to use witnesses at two nearby cutoffs
\(t\). Proposition 8.3 allows every \(t\in[1,3/2]\), while the present
application chooses one optimized cutoff. A new cross-scale relation
could constrain rows that repeatedly generate large witnesses. The
selected zero, presentation, and all dyadic subdivisions must remain
compatible. The repo's [large-values assessment](../../prime-variance-exponents/notes/programs/09_large_values_zero_detection/PRELIMINARY_INVESTIGATION_20261004.md)
explains why an allowed isolated exception cannot be eliminated by an
average estimate without actual amplification.

## Geometry use common signal contrasts and complete error energy

With \(b=1/8\) and \(M+\ell=1\), changing \(\ell\) preserves the
affine signal exponent \(C(s)=s-11/16\). This suggests constructing
two or three admissible probes, normalized to the same complete principal
signal, with different slot windows, shapes, or allowed scales.
For normalized probes \(J_j=f+E_j\), contrasts \(J_j-J_0\) have zero
principal signal. A bounded combination with coefficients summing to
one preserves \(f\).

Before triangle inequalities, retain the mixed error Gram \(G\).
In a basis consisting of one signal probe and zero-signal contrasts,
the formal least residual energy is

\[
G_{00}-G_{0C}G_{CC}^{-1}G_{C0},
\]

when the contrast block is positive definite. A singular block requires
an appropriate justified projection or regularization. The repo's
[source-selective Schur analysis](../../investigations/sonin-critical-boundary/notes/selective-loss-program/01_schur_completion_20261003.md)
gives exact residual algebra of this kind and explains why using the
worst scalar inverse can waste relevant information.

The first test should derive the mixed leading kernel near the dangerous
bin. An exact removable leading term or a power-small residual would be
useful. A fixed constant improvement in the Gram changes no exponent.
The Gram and its inverse cannot themselves be unknown objects merely
renaming the estimate. Coefficients must come from explicit controlled
data, satisfy the continuation quantifiers and low bound, and must not
be chosen separately for each unknown row. The full common signal,
excluded set, masks, and normalizers must be checked, not just its
affine power of the scale.

A related scout is an extra compensated operation killing an explicitly
identified nuisance mode of that mixed kernel. The repo's
[actual-error projection](../../investigations/sonin-critical-boundary/notes/selective-loss-program/09_actual_error_projection_and_frequency_20261003.md)
annihilates four concrete trends in its own observable. This is a model
for the calculation, not evidence that the present adverse kernel has
finite rank. The principal residue must survive any new vanishing
moment. The [complete-response analysis](../../investigations/sonin-critical-boundary/notes/selective-loss-program/04_complete_response_and_signed_pairs_20261003.md)
also requires full support and signed pairs; clipping individual terms
or losing caps can create the leading error one then tries to remove.

## Other scale changes and a stronger moment input

Varying \(b\) jointly with \(\ell\) is inexpensive algebraic work but
appears to offer little. A numerical stationary calculation near
\(b=0.1234054\) suggests only about \(1.3\times10^{-7}\) additional
boundary gain beyond the fixed-\(b\) limit. This observation has no new
continuous certificate and is not adopted as a result.

The already-audited perturbation \(M+\ell=1-2r\), \(r\ge0\), is
less efficient locally than increasing \(\ell\). The genuinely new
direction \(M+\ell>1\) invalidates the step that bounds the dual row
length by the physical row length. A useful bounded scout is to retain
the full maximum in that low-energy estimate and compute the extra
cost before optimizing. No previously proved exponent formula should
be extrapolated across this condition.

For a larger analytic advance, strengthen the scale-uniform unmarked
mean square from rows longer than the polynomial to \(H\ge D^\theta\)
with some fixed \(\theta<1\). Assuming that precise normalized bound
with its scale supremum and permitted profiles, sixth-power replication
would replace the long inverse moment exponent by

\[
e_\theta(r)=\max\{1,\,1/6+5\theta r/6\}.
\]

This attacks the long branch directly. It is the same missing input
identified in the [character-family transfer analysis](CHARACTER_FAMILY_TRANSFER_20261008.md).
Its coefficient restrictions matter: an arbitrary bounded residual
weight can cancel Mobius signs and make the desired theorem false.
The repo has no proved bound in this shorter-family range.

## Recommended sequence

1. Keep the full amplitude profile and rigorously isolate the nearly
   saturated bad class. Record the inverse/plain/convolution coefficient
   structure at its actual lengths.
2. Try a mixed or cross-scale witness estimate only for that class,
   and recompute the branch crossing if one bound improves.
3. In parallel, construct two genuinely common-signal probes and derive
   their mixed kernel, with every cap and correction retained. Stop if
   the only benefit is a constant or if the proposed coefficient choice
   depends on the unknown rows.
4. Treat the off-balance geometry and shorter-family mean square as
   separate, larger investigations with explicit new lemmas.

The repo's [arithmetic closure test](../../prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/ARITHMETIC_CLOSURE_ATTEMPT_20261004.md)
shows coherent zero modes survive the complete existing identities.
Separate Mertens and prime-error bounds, extra smoothness alone, more
available slots, or a density bound permitting an isolated exception
are therefore not substitutes for these missing arithmetic inputs.
