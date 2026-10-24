# Progress register: averaged zero-density evolution

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.

This is the investigation's sole research task ledger. The
[overview][overview] defines the objective and equation contracts.
The target is the unnormalized average shape, with spatial averaging,
time averaging, or both, and explicit fluctuation corrections.

**Current state:** first bounded research round completed. The averaging
contract is fixed; a small-window covariance expansion and 17 floating
theta comparisons are recorded. Fixed-region negative-time mean,
potential and covariance coefficients, a complete cosine-cell covariance,
and a conditional regulator-bias bound are derived in-note. No uniform
theta approximation bound, independently validated closure or
boundary-matched reduced solution has been obtained.

**Next:** HDA-04/HDA-06 — pay the positive-time coarse-average transfer
and its covariance on a declared theta domain; HDA-02 — pay an actual
regulator-bias instance before claiming accuracy for averaged zero counts.
Start from the [new-chat continuation][continuation], not from HDA-01 again.

## Status meanings

- **Complete:** the stated deliverable exists with its evidence and scope.
- **Partial:** a concrete part exists, with missing acceptance items listed.
- **Ready:** prerequisites permit starting; no completion is implied.
- **Gated:** depends on named unfinished work.

The research stages below are not started merely because their formulas
or proposed acceptance criteria appear in the overview.

## Task ledger

| ID | Task and required output | Status | Dependencies and remaining acceptance work |
| --- | --- | --- | --- |
| HDA-00 | Establish the investigation, overview, progress register and chat archive | Complete — organization only | [Home][home], [overview][overview], [history][history]. Preserve the author's scope and one canonical chat registration. |
| HDA-01 | Fix the averaging/accuracy contract: domain, kernels, spatial and temporal widths, regulator, norms and validation observations | Complete — first bounded contract | [Note 03][contract] fixes the 17-case schedule, full buffer, centered time filter, regulator protocol and diagnostic targets. Larger-scale or growing-domain work requires a new contract. |
| HDA-02 | Relate the regularized average to smoothed zero counts | Partial — conditional local bound derived | [Note 06][regulator] gives a logarithmic-potential bound with multiplicity-dependent rates. Actual theta lower-bound data and temporal uniformity remain unpaid; the pilot has no quantified zero-count bias. |
| HDA-03 | Determine negative-time asymptotic values and fluctuation scales | Partial — fixed-region coefficients derived | [Note 05][limits] gives R at T^-3, source-anchored U through T^-3, isotropic Q and its Laplacian at T^-5, and regulator crossover checks. Explicit numerical remainder constants, diffusive/growing domains and time-only next-order density corrections remain open. |
| HDA-04 | Determine positive-time asymptotic values and fluctuation scales | Partial — exact cosine-cell mean and covariance | [Note 05][limits] adds mean potential, Q, coarse transverse limits and the extra covariance from further space/time averaging. Complete-source theta transfer, carrier/tail estimates, moving-period commutators and spatial/rank uniformity remain open. |
| HDA-05 | Derive and audit the exact evolution of the smoothed function | Partial — chosen fixed-filter audit recorded | [Notes 02][filtered] and [04][closure] give exact potential/density/current identities and an analytic Laplacian-Q covariance formula. Jet algebra, current finite differences and quadrature refinements were checked in the declared pilot. Moving filters and final boundary traces remain outside this audit. |
| HDA-06 | Approximate the local fluctuation contribution and close the reduced evolution | Partial — local closure and consistency evidence | [Note 04][closure] derives the C2 small-width expansion and compares it with omitting Q in 17 theta samples; both defects improve. Broad-window accuracy, epsilon-uniformity, time-history closure, evolved-solution stability and asymptotic compatibility remain open. |
| HDA-07 | Find solutions satisfying compatible asymptotic, spatial and source boundary conditions | Gated — no solve performed | Requires quantitative HDA-03–04 data and usable HDA-06 closure. The mixed-sign operator, source-fixed harmonic data, current boundary flux and residual amplification must be addressed before a final boundary problem is claimed. |
| HDA-08 | Further constrain and refine solutions against the actual heat evolution | Gated — no reduced solution yet | The pilot supplies an actual-theta quadrature starting point, not an independent evaluator or a trajectory comparison. After HDA-07, measure mean/current errors, closure propagation, held-out trajectories and regulator bias. |
| HDA-09 | Review and deliver a reproducible approximation with its scope and error budget | Gated — final approximation not available | [Round-one assessment][review] is same-assistant only. It audits the bounded deliverables without promoting floating consistency to a certified solution. Independent review and a final error budget remain open. |

## Evidence already available

| Evidence | What it supports | What remains open |
| --- | --- | --- |
| [Opening brainstorm][opening] | Target definition, fixed-window averaged continuity, Gaussian/saddle starting models, source anchoring and control screen | Uniform theta approximation and explicit regulator/averaging error bounds |
| [Cosine-average calculation][checks] | Sixteen floating comparisons of a slice-model average and four transverse-mass checks | Transfer to the actual theta field; these are not certificates or fluctuation-closure tests |
| [Filtered-equation note][filtered] | Exact covariance bookkeeping, real-potential and density equations, current balance and an exact algebraic countercheck to dropping the correction | Extended by the fixed-filter audit and closure pilot below; final boundary and uniformity estimates remain open |
| [Local closure and theta pilot][closure] | C2 small-width expansion, 17 floating source-field comparisons and differentiated/current checks | Broad-average transfer, regulator-uniformity and evolved-solution accuracy |
| [Asymptotic mean and covariance][limits] | Negative-time fixed-region coefficients and exact cosine-cell/coarse covariance formulas | Numerical remainder constants and positive-time theta transfer |
| [Regulator bridge][regulator] | Local multiplicity-sensitive smoothing-bias bound | Actual theta lower-bound data and temporal uniformity |
| [Chat archive][history] | The author's requested scope and continuation | Mathematical evidence is held in the research sources, not established by capture |

## First bounded research round — completed within its stated scope

The [contract][contract] and [execution record][pilot] contain 17 cases
at three centers, with spatial-only, time-only and combined averaging.
No coefficient was fitted. The gradient correction reduced the potential
consistency defect by at least 15.2-fold and the density consistency defect
by at least 30.1-fold against omitting Q. These are sparse, floating
source-field comparisons; no reduced evolution was solved.

The initial wide-window, smaller-regulator filter refinement failed its
Laplacian-Q target. Increasing that case to 40 filter nodes reduced the
last change to 1.84e-8. Finer spatial finite differences were also needed;
the last Richardson density-defect changes were below 6.5e-9 and met the
contract. Source-tail, cutoff and arithmetic errors are not interval-enclosed.

The new negative-time expansion shows why preserving the regulator
in the denominator matters, and supplies a T^-5 isotropic covariance
correction alongside the T^-3 mean. The exact cosine-cell formulas show
that whole-period covariance can remain large and that additional time
or transverse smoothing adds another variance term. The generic
regulator bridge exposes the lower bounds needed to relate a smoothed
regularized density to actual smoothed zero counts.

See the [same-assistant assessment][review] for derivation and validation
limits. The [continuation note][continuation] fixes the next bounded
research step and lists work that should not be repeated.

## Required record for each continuation

For every completed bounded step, record:

- Task ID, status change, date, actual model/effort and evidence paths.
- The target function, domain, \(\epsilon\), kernels and averaging widths.
- Asymptotic values or errors obtained, with derivatives and uniformity.
- The fluctuation terms retained or omitted, and their measured/bounded
  effect on the evolution; keep unresolved terms explicit.
- Boundary/source inputs, model residual, independent comparison error,
  regulator bias and any stability amplification.
- Control outcomes, review scope, remaining uncertainty and the next task.

Do not label a closure validated because it fits its training values or
because the underlying heat residual is zero. Preserve failed candidates
with the exact tested regime; use the [result index][results] and
[avoid index][avoid], especially [fitted laws][fitted] and
[status/evidence alignment][status-rule].

## Decisions and unresolved choices

**Fixed by the author:** unnormalized density; average shape; time
averaging permitted; determine asymptotics and the correct averaged
evolution including local fluctuation effects; solve with compatible
boundary data and refine against the actual equations.

**Fixed for round one:** the contract's domain, kernels, widths, regulator
and defect diagnostics. **Still open for the overall program:** broader
averaging scales, uniformity and regulator removal, sufficient fluctuation
statistics, time-memory closure, a well-posed boundary problem, and
solution accuracy/cost. Make routine research choices explicitly and
continue within the author's scope; these are not requests for permission.

## Update log

| Date | Change | Evidence |
| --- | --- | --- |
| 2026-10-24 | Established the staged research program and ledger from the author's continuation; added exact fluctuation identities without claiming a completed closure | [Overview][overview], [Note 02][filtered], [milestone history](../DRAFT_HISTORY.md) |
| 2026-10-24 | Completed the first bounded round: HDA-01 complete; HDA-02 and HDA-06 advanced to partial; HDA-03–05 extended with asymptotic/covariance derivations and floating comparisons | [Notes 03–06][contract], [pilot][pilot], [assessment][review], [new-chat continuation][continuation] |

[home]: ../README.md
[overview]: ../research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md
[opening]: ../notes/01_AVERAGED_DENSITY_AND_TWO_TIME_LIMITS_BRAINSTORM_20261024.md
[filtered]: ../notes/02_FILTERED_EVOLUTION_AND_FLUCTUATION_IDENTITIES_20261024.md
[checks]: ../numerics/README.md
[history]: ../chat-histories/README.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[fitted]: ../../../../avoid/09_round_floors_and_fitted_laws.md
[status-rule]: ../../../../avoid/06_status_stronger_than_the_evidence.md

[contract]: ../notes/03_FIRST_BOUNDED_AVERAGING_CONTRACT_20261024.md
[closure]: ../notes/04_GRADIENT_CLOSURE_AND_ACTUAL_THETA_PILOT_20261024.md
[limits]: ../notes/05_ASYMPTOTIC_MEAN_SHAPES_AND_FLUCTUATIONS_20261024.md
[regulator]: ../notes/06_REGULATOR_BIAS_FOR_SMOOTHED_ZERO_COUNTS_20261024.md
[pilot]: ../numerics/AVERAGED_THETA_ROUND1_20261024.json
[review]: ../reviews/01_FIRST_RESEARCH_ROUND_SELF_REVIEW_20261024.md
[continuation]: ../notes/07_CONTINUATION_FOR_NEW_CHAT_20261024.md
