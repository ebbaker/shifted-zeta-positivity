# Coefficient core, exponential averages and two-endpoint continuation

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This is the bounded research cycle following Review 05 and the user's instruction to update the overview and continue the recommended program. The current conversation retains formal-replay history **19**. It does not replace history 18 from the preceding integration.

## Outcome and reading order

Read the revised [Overview 02](../../research-overview/02_CHORD_CRITERION_AND_ARITHMETIC_BRIDGE_20261015.md), the [new review](../../reviews/06_COEFFICIENT_CORE_AND_TWO_ENDPOINT_REVIEW_20261015.md), and the four notes below. The manuscript is unchanged. The cycle has supplied a simpler collision target, completed the direct elliptic-shift experiment, certified a stronger non-theta control, and improved the outer budget. The missing theorem is still a coefficient-coupled signed bound for the physical theta transform.

| Note | Result | Status |
| --- | --- | --- |
| [Exponential averages and shrinking chords](../02_signed_turning_control/04_EXPONENTIAL_AVERAGE_AND_SHRINKING_CHORD_TARGETS_20261015.md) | Exact derivative-free observation, source tail multiplied by √E, and a quantified shrinking-window exclusion criterion | Analytic argument with exact finite heat-polynomial controls; theta core unproved |
| [Elliptic shift core](../03_theta_bundles_and_connections/05_ELLIPTIC_SHIFT_CORE_AND_PROJECTION_OBSTRUCTION_20261015.md) | Complete fourth-jet insertion, finite primitive endpoints, boundary-band classification, projected ramp kernel and normalized rigidity | Exact identities and analytic classification; no favorable core term |
| [Two-endpoint square collision](../05_control_families/03_TWO_ENDPOINT_SQUARE_COLLISION_20261015.md) | Positive fixed four-mode source with two odd source endpoints and a double collision at T=1/100 | Validated 160-bit certificate with complete real tails; non-theta |
| [Outer-budget refinement](../06_effective_outer_bridge/01_LOW_INDEX_BUDGET_REFINEMENT_20261015.md) | Low-index constant improved by more than 3,974; conditional sufficient log-height reduced | Analytic refinement under unchanged imported assumptions; no practical overlap |

## The preferred inequality

For `W=h_j`, `j=0,1`, at a full stationary start, retain

\[
\mathcal A_{j,\delta,N}
=W(t,x)^2-e^{-\delta}W(t,x)W_N(t,x+\delta),
\qquad E(t,x)=H(t,x)^2+H_x(t,x)^2.
\]

The next target is `A_(j,1/N,N)≥−K_NE`, for every sufficiently large fixed N and both parity branches, with K_N locally bounded through possible finite events. Only the endpoint is truncated. The Gaussian complete-source tail costs `B exp(−π(N+1)²/4)√E`. At a collision of multiplicity `2r+j`, the limiting full amplitude divided by √E is negative of order `δ^(2r)`.

The decisive order of limits is: fix the event and its finite multiplicity; choose one sufficiently large N so that the Gaussian error is less than half that negative limiting magnitude at δ=1/N; then approach the event at that fixed N. There is no requirement to bound K_N uniformly as N grows and no simultaneous N(t) limit. The full predecessor and its prescribed rightward interval must eventually lie in the claimed domain. A window shrinking arbitrarily fast does not meet this argument.

The original pure-tail theorem and its rate gap a<c remain correct. They are not the preferred route now that the full starting factor can be kept. Positive averaging itself is not a positivity proof. The new exponential weight has a noncompact endpoint on its integration interval and does not inherit rapid Fourier decay from a compactly supported smooth probe.

## Completed arithmetic tests and what they exclude

The direct scalar elliptic shift, with every multiplier derivative retained, gives `Φ_N^+=Φ_N+(φ_(N+1)−φ_N)/2`. Any fixed finite combination of integer shifts whose coefficients sum to one gives only a finite cutoff boundary band. It therefore supplies a useful remainder but leaves the interior sign problem intact. The translated zero mode cancels in the complete operator; estimating its derivative pieces separately creates divergent positive-time integrals. Finite primitive constants must use the truncated endpoint sum, not the complete value 1/2.

The physical source projection of one shift has kernel `a_n=a_0+b|n|` among even polynomial-growth weights. Fixing a_0=1 and the primitive normalization forces b=0. Without fixing a_0, that endpoint alone does not force the ramp coefficient to vanish. This is input rigidity, not a signed estimate.

The new collision at `83.5323729<x_*<83.5323730`, T=1/100, retains `Φ′(0)=Φ‴(0)=0` and `ψ′(0)=ψ‴(0)=ψ^(5)(0)=−1/2`. Its weights are fixed by an exact bracketed-root construction, not by rounded displayed decimals. The fifth source derivative is nonzero. A qualitative implicit-function argument restores a positive infinite square tail, without a numerical perturbation radius. This eliminates the proposed second-endpoint repair as a sufficient sign mechanism; it does not eliminate every finite hierarchy.

The endpoint reduction also gives a normalized high-mode mass bound of approximately `2.0925412638×10^(−6)`. This is a bound in the specifically defined endpoint measure, not a claim that the raw coefficients or every physical transform norm are close to theta.

## The next bounded experiment

Work with the exact amplitude kernel and primitive representation in the exponential-average note. Choose **one** coupled elliptic or reflection insertion before physical scalar restriction. Derive the full two-source identity, including cross terms, heat factors, translated zero modes and affine endpoints. Identify the precise additional relation controlling the indefinite amplitude form. Test that this relation excludes the two-endpoint collision and the projected ramp control where appropriate.

Stop this ansatz if it reduces to the scalar boundary-band identity, merely restates theta uniqueness, or leaves the same indefinite form without an additional constraint. A bilocal product or transverse observation is an open candidate, not an established sign mechanism. Increasing a bounded scalar-shift degree is no longer the next task.

Only after obtaining an explicit coefficient rule should a certified theta pilot test the complete identity at full stationary starts. Fix the rule before observing signs, include all tails, state interval coverage, and explain local boundedness through hypothetical E=0. A finite pilot cannot establish unbounded spectral coverage. A claimed nonnegative form must also be examined on the saved non-theta controls, with the arithmetic hypotheses distinguished explicitly.

For the outer bridge, decide which objective is intended. An explicit asymptotic theorem still needs the imported exponent-pair constant and validity threshold. Practical overlap requires a different nonasymptotic differentiated remainder; the present majorant cannot pay its budget below roughly `L−1=31,424,688`, and the original disc domain starts at L=100002. Extracting a constant alone will not close that gap. The condition tL≥61/24 remains.

## Replay and provenance

The [manifest](../../numerics/COEFFICIENT_CORE_AND_TWO_ENDPOINT_CHECKS_20261015.json) records four installed scripts and receipts: 1,620 exponential-average checks, 481 elliptic checks, 35 outer-budget checks, and 26 mixed or validated endpoint checks. Counts overlap and are not numbers of distinct theorems. The first three use exact standard-library rational arithmetic; the last uses python-flint 0.9.0 at 160 bits and 44 complete integrals. Each was replayed by the coordinator and independently by another collaborator. The analytic arguments were reviewed separately from the finite calculations.

The current manuscript source hash remains `114611f06f0928827045399561d2f83ca6ca9abc1d35a9d5cd7d406c845aa417`. Its existing build record and historical receipts remain unchanged. The new research is not a manuscript integration, an external referee report, a formal proof, or a theta sign certificate.

Use the existing formal-replay [registry](../../../../formal_replay_crosswalk/chat-histories/index.json) and history 19 for this conversation. Refresh through the repository recorder, preserving the identity. The exact current-turn follow-up captures the real final reply only after it has been sent. Later legitimate chat refreshes need not match an earlier provenance checkpoint's file hash.
