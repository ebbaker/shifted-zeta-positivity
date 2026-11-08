# Green potential research summary and paths forward

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. The current chat registry records
no model or reasoning-effort configuration; neither is inferred from the
task recommendations. Session: “Summarize Green resolvent research”,
thread `01a1b9b7-8624-7e51-9f9b-ba8e5a87a938`.

**Later in this session:** the author requested an analytical manuscript.
[Session04](04_TND_OG_E04_MANUSCRIPT_DEVELOPMENT_20261108.md) records that
completed milestone. This earlier orientation retains its original
no-manuscript status as a historical statement; E03 remains unactivated.

The branch has a positive quantity that detects nonreal zeros, precise
limitations on two ways of estimating it, and a new local theorem for
approximating its boundary logarithm through zeros. The missing advance
is an upper estimate small enough to exclude a specified nonreal zero.
The recommended immediate follow-through is the already frozen E03
assembly. Its success would complete the acquisition method; favorable
values and practical cost remain separate questions.

This is the opening orientation for the author's requested brainstorming,
not a new proof, assessment or numerical task. It leaves E03 **ready and
unactivated**. The [sole register](../../research-progress/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md)
owns live status. [Continuation05](../../continuation-notes/05_TND_OG_B02_RESULTS_AND_MODEL_CHANGE_20261108.md),
[Overview01](../../research-overview/01_TND_OG_GREEN_RESOLVENT_RESEARCH_OVERVIEW_20261107.md)
and [Note04](../../notes/04_TND_OG_B02_ONE_SIDED_BOUNDARY_LOG_ACQUISITION_20261108.md)
supply the current mathematical account.

## What the research is trying to achieve

The exact theta source produces the entire Newman field \(H_\lambda\);
at time zero its zeros correspond to the zeta zeros under the established
change of variable. The logarithmic derivative \(R=H'/H\) and logarithmic
potential \(\log|H|\) expose those zeros as poles and point masses.
Their exact identities organize the problem but do not fix the desired
sign.

The useful observable is the complete strip Green potential
\(J_\lambda^{\rm G}(X)\). It is a sum of positive contributions from
zeros in the upper half-plane, including their multiplicities. Real
zeros, including multiple real zeros, contribute no interior mass.
Consequently this is a test for off-axis zeros, not a test for simplicity.

A zero at horizontal distance at most \(r\) from \(X\) and vertical
distance at least \(d>0\), within the inherited strip \(y\le1\), forces
\[
 J_\lambda^{\rm G}(X)\ge m(d,r)
 =\frac{\sin(\pi/8)d}{\cosh(\pi r/8)}.
\]
An independently established upper bound below that margin excludes
the specified zero class. This is the existing consumer, not a new
criterion. The universal time-zero vanishing target is the RH
reformulation already classified in Overview01; finite checks are not
evidence for that universal statement.

Only at time zero, the exact arithmetic decomposition expresses this
same quantity as a localized logarithmic average on the critical line,
minus an explicit convergent prime sum, plus the known pole correction.
The hard quantity is their **signed difference**. Separate absolute
bounds can erase the cancellation the consumer needs.

## What has actually been established

| Result | What it contributes | Boundary of the claim |
| --- | --- | --- |
| Inherited complete Green identity and prime decomposition | An exact positive zero sum, an explicit single-zero detection margin, and complete boundary/tail bookkeeping | The identity and coarse upper bounds do not supply a favorable margin. The prime formula is time-zero only. |
| B01 source/resolvent conditioning obstruction | A fixed-prime translated-source family has common quantitative bounds; source and fixed safe-line resolvent changes of order \(\eta\) coexist with Green changes of order \(\sqrt{\eta}\) | Excludes a uniform Lipschitz comparison on that enlarged family. It does not exclude theta-specific estimates, a weaker continuity modulus or sufficiently fine resolution. |
| E01 short-mollifier floor, assessed in E02 with an additive correction | A positive asymptotic average floor for the normalized quadratic residual, uniformly over the specified bounded-complex polynomials | One polynomial is used over each padded interval, with length exponent \(\theta<1/2\). This limits that sufficient quadratic recipe; it is not a lower bound for \(J\), an assertion about every center or an exclusion of adaptive/longer/signed methods. |
| B02 local boundary-log estimate | An explicit one-sided integrated log error tending to zero with absolute field error, even through multiple real zeros and zeros of the approximant | Proved in-note with proof-author checking only. It does not complete the global source/tail/prime assembly or bound the true canonical value by the defect margin. |

The scoped obstruction sources are [Note01](../../notes/01_TND_OG_B01_UNIFORM_SOURCE_CONDITIONING_20261107.md)
and [Note02](../../notes/02_TND_OG_E01_SHORT_MOLLIFIER_RESIDUAL_FLOOR_20261107.md),
read with [E02 Review01](../../reviews/01_TND_OG_E02_CLAIM_LEVEL_ASSESSMENT_20261107.md)
and [its correction](../../notes/03_TND_OG_E02_REAL_MIXED_TERM_AND_ACQUISITION_CLARIFICATIONS_20261107.md).
These are internal LLM results/assessments, not independent specialist
human review. Earlier dated “pending” paragraphs in the source files
must be read against the current register.

## Why the latest result changes the available method

A direct estimate of \(H'/H\) needs a lower denominator bound. Such a
bound cannot hold on a real interval containing a zero. B02 instead
uses an upper envelope
\(\log(|\widehat F|+\delta)\), where \(|F-\widehat F|\le\delta\).
It controls the *integrated* error caused by tiny values of \(F\),
using an unconditional safe anchor away from the boundary and growth
on a surrounding disk. No real-boundary lower modulus or zero-free
approximant is required.

This retains the measured logarithm and its sign. It avoids the
hypotheses of the tested short-polynomial quadratic recipe and the
sibling's zero-free harmonic-baseline recipe. The latter comparison is
the one recorded in Note04; this session does not reassess the sibling.

The cost is explicit but weak: the local error behaves as a prefactor
of order \(\log^2(2+|v|)\) times
\((2\delta/M_v)^{1/n_v}\), with \(n_v=O(\log(2+|v|))\).
The exponent deteriorates with height. The E03 source-to-field
multiplier is also deliberately coarse and contains an exponential
of a quadratic height expression. These are reasons to audit practical
cost separately. They are not lower complexity bounds or evidence that
the direct-log method must fail.

## The immediate task and the remaining research choice

[E03 request09](../../research-progress/handoffs/09_TND_OG_E03_SIGNED_LOG_ACQUISITION_REQUEST_20261108.md)
fixes the proof of
\[
 0\le U(X)-J_0^{\rm G}(X)
 \le {\cal E}_{X,R}(\delta)+2{\cal T}(X,R)+2\beta_Q,
 \qquad \beta_Q=\tfrac23Q^{-3/2}.
\]
The local estimate is to be joined to the finite source approximation,
absolute logarithmic tail and prime truncation, with every error paid.
The two factors of two account for replacing signed remainders with
upper allowances. This full statement remains a target.

After that assembly, a directed evaluated upper value
\(\overline U\), with \(U\le\overline U\le U+\eta_{\rm eval}\),
must still satisfy \(\overline U<m(d,r)\).
Shrinking the approximation error does not force the true value to
satisfy this inequality. Finite acquisition for each prescribed tuple
also supplies neither a useful common cutoff nor coverage of every
height and arbitrarily small \(d\).

The following is a discussion menu, not a set of issued successor tasks:

| Path | Type and model recommendation | Concrete purpose and stopping point |
| --- | --- | --- |
| Complete E03, then assess its claims | **E — Sol6.1**, existing ready request; author chooses effort | Obtain the full acquisition theorem or its precise failed clause within the allowed correction cycle. A subsequent assessment is separate. |
| Decide whether a practical finite diagnostic is worthwhile | **B — Astra** to choose the question, scale and comparison; later fixed implementation would be **E — Sol6.1** | First inspect the error budget and define a finite test of accuracy/cost against a comparable direct method. Any pilot would have fixed cases and a stop budget; it would test feasibility, not supply evidence for RH. No pilot is activated here. |
| Seek a source-specific estimate of the signed value | **B — Astra**, conceptual work not yet specified | Identify a quantitative relation in the exact theta/arithmetic data that bounds the log-average/prime difference, including exceptional centers and the small-\(d\) regime. Return at most one bounded proof contract or a precise scoped failure. No such mechanism is selected in this summary. |

The priority is to close E03 as a reusable analytical result, while
keeping the next conceptual discussion focused on the third row.
Improving constants may help a finite diagnostic; it cannot by itself
explain why the canonical signed value must be favorable. Reopening
resolvent dynamics is justified only when it brings a new estimate with
its denominator, residues, boundary terms and quantitative advantage
specified.

## Controls and classification for the discussion

The governing sources are the [result index](../../../../../../../result-summaries/README.md),
especially [collision controls12](../../../../../../../result-summaries/12_collision_controls_and_screening.md),
and the [patterns index](../../../../../../../avoid/README.md):
[target01](../../../../../../../avoid/01_restating_the_target.md),
[control02](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[numerics10](../../../../../../../avoid/10_numerics_ahead_of_the_question.md)
and [known-tests11](../../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md).

For this synthesis the analytical screen is Note04 section 5, checked
against controls12; no new control computation is claimed:

| Control family | Premise unavailable for a canonical application |
| --- | --- |
| Euler-factor controls, including B01's fixed-prime family | The extra factor changes the literal theta/xi field. The canonical prime subtraction and anchor cannot simply be reused; growing-prime examples also alter other arithmetic/growth data. |
| Weighted squares, finite prefixes/tails and finite-prime orbits | Matched finite information does not supply the complete normalized theta coefficients together with full reflection. |
| Reflected super-Gaussian control | Reflection, positivity and Gram positivity do not supply the integer-square theta expansion or the exact xi/zeta identity. |
| Smooth shape and positive-primitive controls | Their preserved shape, primitive and asymptotic data do not supply the canonical square coefficients and exact arithmetic decomposition. |
| Atomic/finite-profile and variable-readout controls | Their stated information does not supply the full canonical source/profile/readout conjunction; no additional canonical constants are assigned to them. |

The generic local logarithmic lemma can also work for an admissible
control with its own constants. For a control with an off-axis zero
in the relevant domain, accurate acquisition must preserve its positive
Green contribution and cannot pass the corresponding strict exclusion
threshold. Missing an exact theta identity does not mean a control
fails every inequality derived from that identity. A future sign
mechanism must identify the *quantitative* distinguishing premise.

Classification is therefore unchanged: Green/resolvent identities are
representations; the local error modulus and scoped floors are
quantitative milestones; E03 is an acquisition target; canonical
smallness is the unpaid value problem. The source-specific path above
is a research question, not a proposed criterion supported by checks.

## Session record

This session adds an orientation note and navigation/history entries,
without changing a frozen request, proof source or live mathematical
status. No manuscript milestone or investigation closure occurs, so no
shared result-summary promotion is made.

The actual chat is registered as **0002** in the branch's
[chat-histories](../../chat-histories/README.md), under its source-provided
title. [The registry](../../chat-histories/index.json) owns current capture
times, sizes, counts, configurations and hashes. Capture succeeded from
the local paginated source; a bounded exact-turn follow-up will wait for
the real final response. Native completion-hook activation is not
asserted.

**Next: [E] TND-OG-E03 — Sol6.1**, the complete signed-log acquisition
proof, with model/effort and activation selected by Edward Baker.

