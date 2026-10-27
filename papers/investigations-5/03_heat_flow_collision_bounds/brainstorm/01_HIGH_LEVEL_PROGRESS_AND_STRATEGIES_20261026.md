# Heat-flow collision bounds: progress and current strategies

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. Chat title: “Summarize heat-flow collision bounds.”
Thread: `01a17b22-e902-7773-ad5a-14022601a13a`.

This is a high-level synthesis of the existing research, not a new proof,
numerical run, certificate replay or independent review. It leaves the
sole HCB progress register and all upstream task statuses unchanged.

## Overall position

The investigation is building the link between accurate heat-flow
approximations and inequalities that can rule out a multiple zero. Its
principal goal is **simplicity conditional on RH**. A contradiction at an
unknown positive Newman threshold, and an improvement of a specified
positive Newman upper bound, require additional inputs and remain separate
objectives.

The upstream heat-density work supplies a complete arithmetic model and
normalized first-jet error of order `X^(-3/4)` in the relevant microscopic
regime. The applications investigation supplies calibrated collision
tests. This investigation asks whether the actual canonical arithmetic can
supply those tests' lower bounds, complete zero populations, coefficients
and error margins as the observation scale shrinks.

The main progress is a more explicit and partially demonstrated acquisition
method. **No favorable canonical collision-excluding Poisson bound, global
simplicity theorem, RH proof or new Newman bound has been obtained.**

## What has been accomplished

1. **A transfer that permits internal collisions.** Note01 converts errors
   in a complete cluster's monic coefficients into a bound for its Poisson
   density and second moment. It does not assume internal root separation
   or divide by individual root slopes. Its conservative `y^(-n)`
   dependence, however, becomes expensive at small width or large count.

2. **A complete error allocation.** Note03 fixes the height sequence, time
   interval, contour, normalization, population convention and source
   allowance. If its unproved model and error tests hold, the final
   density excess is at most `5/8`, below the collision threshold `2/3`.
   This is an explicit sufficient contract, not an acquired bound for the
   canonical model.

3. **A genuine asymptotic part of contour acquisition.** Under RH, Note04
   obtains a horizontal-side lower bound `X^(-1/2-o(1))` throughout the
   frozen heat interval. Vertical-side minima reduce to two prescribed
   real endpoint values. Those values and the exact complete integer
   counts remain unproved uniformly. Average zero density does not settle
   the count in these individual microscopic windows.

4. **One finite canonical member.** Note06 supplies real-endpoint heat
   transport and a way to deduce a full contour floor from endpoint floors
   and a complete count. For the unchanged `m=16` case, retained interval
   data establish under RH, throughout the frozen time interval:
   left/right endpoint moduli above `0.8144 / 0.2789`, complete count `1`,
   and full canonical contour modulus above `0.0697`. The original
   contour-integration stage failed. A separately recorded witness obtained
   the count from already retained data with zero new source evaluations.
   This is a finite method comparison; it is not an instantiated finite
   arithmetic-model coefficient certificate or a uniform result.

5. **A quantified conditional uniform extension.** Note07 develops
   high-order endpoint detectors and a smoothed complete-count functional.
   With `q=floor(sqrt(L))`, the detector's source error stays at most
   `X^(-1/4+o(1))`. If its actual endpoint budgets hold, it supplies endpoint
   separation, a whole-time contour floor `X^(-5/8-o(1))`, and eventual
   extraction of the complete integer count without a fixed population
   cap. The detector inequalities and count enclosures themselves have
   not been acquired. This count functional is not the desired second
   moment.

The recent review therefore retains **HCB-02: Partial**. HCB-01's finite
transfer is partial; sharpening it (HCB-03) and proving the direct J bound
(HCB-05) remain open. A favorable P bound with full height coverage
(HCB-04) remains aspirational. Reviews are same-model internal assessments;
specialist and inherited-chain validation remain open.

## Main strategies

| Strategy | Mathematical idea | Present task or limitation |
| --- | --- | --- |
| **P — lead route: Poisson second moment** | Smooth a complete real zero population at width equal to the square root of heat time, square its density, and subtract the known self contribution. Descendants of a multiple endpoint force excess at least `2/3`; a complete bound below that threshold excludes the endpoint. | Obtain the actual arithmetic second moment and transfer it with absolute error below one collision. Preserve mixed arithmetic terms, the exterior analytic factor, counts, tails and integration errors. |
| **J — direct benchmark: joint value and derivative** | Prove that the normalized arithmetic model and its derivative cannot be simultaneously small. A joint norm floor `c X^(-beta)` with `beta<3/4` beats the available approximation error. | The transfer is comparatively simple; the actual arithmetic lower bound is unproved. A positive diagonal or an average over height cannot replace the required complete bound. |
| **RT — whole-cluster force comparison** | Use complete cluster data in the existing Rodgers–Tao root-motion/force framework. Working with a whole cluster can avoid requiring well-resolved internal gaps. | Compare methods on microscopic or growing blocks, retaining exterior forces and corrected boundary/reference terms. Existing RT task ownership remains in Investigation02. |
| **E — complete inverse-gap energy** | A multiple endpoint forces a contribution at least `1/(4t)`. An acquired complete energy upper bound with a strictly smaller leading coefficient would contradict it. | The free double attains the generic coefficient, so a strict improvement needs canonical arithmetic information, with exterior, cutoff and reference payments retained. |
| **V — negative-time vertical moment** | Run to time `-s` and measure the squared imaginary parts of the localized zeros. A multiple endpoint contributes at least `4s+o(s)`. | Seek `o(s)` or a strict coefficient below four, controlling regulator removal, signed cutoffs and the fixed-core limit. This remains a secondary/deferred direction. |

A specified positive Newman-bound improvement is another possible numerical
objective, but no target improvement has been selected. A favorable local
block cannot substitute for the complete global upper-bound conditions.

## The immediate research decisions

There are two separate bottlenecks.

**First, acquire the uniform canonical data.** The latest proposed route is
an actual bound for Note07's endpoint detectors on the unchanged complete
theta source, including evaluation and source margins, followed by an
actual complete-count enclosure. A direct real value/jet bound sufficient
for Note06 is an alternative. The conditional mechanism supplies neither
of these arithmetic estimates automatically.

**Second, make the Poisson transfer efficient enough.** Even the new
conditional contour floor does not meet the retained two-root Poisson
tolerance. Note04 also shows that the specified binomial fallback with its
retained allowance cannot accept populations `n>=6` at sufficiently large
height. This is a failure of that test and allowance, not of every contour
method or the Poisson strategy. Integrated, correlated estimates must be
sharpened and compared with J. The exact scalar-perturbed double's better
error rate is a calibration, not a general-cluster theorem.

My reading of Investigation03's existing plan is therefore: keep P as the lead route,
treat uniform acquisition and sharper transfer as distinct necessary
tasks, and retain J as the direct comparison. Improving a generic upper
envelope or simply adding numerical cases would not by itself close either
gap. Ultimately, a simplicity result needs coverage of every sufficiently
high endpoint core plus the bounded-height remainder; the sparse frozen
family is the present acquisition testbed, not that complete cover.

## Clarification: the positive-threshold RH route remains active

Follow-up, 26 October 2026. Same recorded model and effort as above.
The author correctly points out that Investigation02 retains a direct
RH strategy based on assuming `T=Lambda>0`. The preceding prioritization
summarizes Investigation03's narrower initial task; it does not describe
an abandonment or adverse assessment of that broader route.

Investigation02's [current summary](../../02_heat_flow_rh_applications/summary/CURRENT_SUMMARY.md)
still lists Rodgers–Tao dynamics/energy as its lead direction and the
positive-threshold contradiction as an active follow-up. Its
[positive-threshold note](../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md)
and [RT overview](../../02_heat_flow_rh_applications/rodgers_tao/research-overview/01_RODGERS_TAO_RESEARCH_OVERVIEW_20261026.md)
explicitly retain that aim. A contradiction from `Lambda>0` would prove RH;
RH-conditional simplicity assumes RH and answers a different question.
Neither successful statement by itself should be described as automatically
proving the other.

The local emphasis comes from
[Review51](../../01_heat_density_asymptotics/reviews/51_RH_TARGET_GAP_ANALYSIS_AND_RESEARCH_PRIORITIES_20261026.md)
and Investigation03's scope choice: a known endpoint at time zero, the
original xi slice, RH-supplied realness on the subsequent interval, and
already calibrated J/P/V/E error requirements give a concrete first
acquisition problem. This is a tractability judgment, not evidence that
simplicity is easier or the positive-threshold route less promising.

For `T=Lambda>0`, the existing canonical reduction supplies a finite real
multiple event at time T. Real-root dynamics applies after T, so local P
and energy tests can use elapsed time `s=t-T`; a suitable J estimate can
exclude the common zero directly. The new arithmetic estimates must apply
to `H(T+s,z)` and cover every possible event. A time shift preserves the
heat equation but changes the initial source to `exp(T u^2) Phi(u)`.
The present time-zero acquisition results do not establish those shifted
canonical estimates. Existing field approximations already cover small
positive times; the missing collision-sensitive margins are not simply a
missing field-domain theorem.

The original Rodgers–Tao contradiction also uses spacing information at
the actual zeta slice. With `Lambda>0`, that slice precedes the all-real
interval, so later regular spacing supplies no such contradiction.
Positive T nevertheless has an advantage: uniform exterior estimates can
localize the candidate event to finite height for each fixed T. The
required region grows as T approaches zero. This observation does not
establish a ranking of the two research routes.

The appropriate portfolio interpretation is two related endpoint tracks:
a direct positive-threshold RH track in Investigation02 and a time-zero
RH-conditional simplicity testbed in Investigation03, sharing acquisition
and transfer tools. No live plan or task priority is changed by this
clarification. A primary-source spot check of
[Rodgers–Tao v5](https://arxiv.org/abs/1801.05914v5) and
[Polymath v2](https://arxiv.org/html/1904.12438v2) confirmed the threshold
conventions; no new proof, numerical computation or independent audit was
performed.

## Subsequent author proposal: compare the three dynamical regimes

The author next proposed conditioning Investigation01's all-time/all-height
solution analysis on positive Lambda, zero Lambda with multiple endpoint
zeros, and zero Lambda with simple endpoint zeros. The new
[three-regime brainstorm](02_THREE_REGIME_DYNAMICS_AND_COMPARATIVE_ASYMPTOTICS_20261026.md)
develops that broader descriptive program, including finite-window moment
laws, escape from compact regions, multiplicity proportions, resolution
controls and a proposed comparison with the exact physical equations.
The earlier P/J prioritization above records the preceding local plan;
the new proposal considers which observables to study before choosing an
exclusion inequality. No live scientific task status is changed here.

## Sources and scope safeguards

Primary reading:

- [Research overview and plan](../research-overview/01_COLLISION_BOUNDS_RESEARCH_OVERVIEW_20261026.md).
- [Sole HCB progress register](../research-progress/01_COLLISION_BOUNDS_RESEARCH_PROGRESS_20261026.md).
- [Complete recent-results handoff, Note08](../notes/08_CHAT0001_RESULTS_AND_HANDOFF_20261026.md).
- [Founding finite Poisson transfer, Note01](../notes/01_WHOLE_CLUSTER_POISSON_TRANSFER_AND_ACQUISITION_20261026.md).
- [J/P/V/E target specifications](../../02_heat_flow_rh_applications/rh_simple_zeros/notes/02_TARGET_BOUNDS_FOR_RH_TO_SIMPLICITY_20261026.md).
- [Latest conditional-interface review](../reviews/05_UNIFORM_PROBE_AND_COUNT_INTERNAL_REVIEW_20261026.md).

The repository [result index](../../../../result-summaries/README.md),
[heat-flow results](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md) govern interpretation.
In particular, retain the distinctions in
[target classification](../../../../avoid/01_restating_the_target.md),
[scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [coupled estimates](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
Generic acquisition tools permit internal multiple roots; endpoint
nonvanishing is not itself collision exclusion. No collision-control
certificate was rerun for this synthesis.

This chat is registered uniquely as
[chat0002](../chat-histories/0002_2026-10-27T02-14-07Z_summarize-heat-flow-collision-bounds.json).
The registry holds current capture metadata. The final reply is captured
only after it is actually recorded, using the repository's bounded
exact-turn follow-up.
