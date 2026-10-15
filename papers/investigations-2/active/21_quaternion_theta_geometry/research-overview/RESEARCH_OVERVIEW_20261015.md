# Research overview for quaternion theta geometry

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata.

The research objective is to exclude every positive-time real collision of the theta heat flow. The exact endpoint is nonvanishing of the physical first jet, \(E=H^2+H_x^2>0\), for every positive time and real height. The quaternionic and octonionic constructions preserve the relevant observations; the remaining work is a theta-specific signed estimate.

The most effective program pairs a focused arithmetic project above theta=5/2 with a deeper signed estimate in the inner cusp. The latter deserves the larger research investment because the present nonzero zeta-carrier argument depends on theta>2. Finite verification supports these projects through discriminating tests and effective coverage.

## Current established results

Write \(L=\log(|x|/(4\pi))\), \(\theta=tL\), and \(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\), with \(h_j=\partial_x^jH\).

All results below lie in 0<=t<=1/2. The asymptotic statements require t>0; the finite certificates include t=0.

| Result | Domain | Qualification |
| --- | --- | --- |
| Finite physical norm and stationary signs | \(0\le t\le1/2\), \(|x|\le112\), with \(\sqrt E>10^{-17}\) | Laguerre signs are asserted on their respective stationary sets |
| Uniform four-jet approximation and both full strict signs | Sufficiently large \(|x|\), \(0<t\le1/2\), \(\theta\ge61/24\) | Includes the closed boundary; starting height remains unevaluated |
| Explicit outer theorem | \(|x|\ge4\pi e^{10^9}\), \(\theta\ge5\) | Far too large to constitute a practical finite bridge |
| Signed staircase cutoff bounds | Same large-height region \(\theta\ge61/24\), every \(N\ge8\) | Includes the complete Gaussian pair tail; raw cutoffs need not be positive |
| Phase-controlled delayed comparison | Large height and \(\theta\ge13/4\) on current stationary sets | Lies within already established full-sign coverage |
| All-earlier-time comparison | The two new stationary branches in heights 104–112 | Earlier-time stationarity is never assumed |

The manuscript now consolidates these results with the collision analysis, analytic logarithmic-loss rigidity, and conditional transfer lemmas. Its [build record](../manuscript/BUILD_RECORD.json) identifies the current source and PDF. The [continuation note](../notes/00_research_coordination/34_MANUSCRIPT_PROGRAMS_AND_CONTINUATION_20261015.md) supplies the integration and archive verification details.

## PR01 Weighted outer remainders

**Objective:** complete the closed strip \(5/2\le\theta\le8/3\), while preserving exact endpoints, uniform complex-disc estimates, all imported errors, and the distinction between the analytic and source cutoffs.

The existing middle-block condition is sufficient but unproved. A weaker sufficient target is uniform \(o(1)\) control of the actual weighted high-index sum on the shrinking complex discs. The existing low-index and heat-flow errors then yield \(o(1)\) normalized four-jet errors, enough for eventual strict signs. This does not supply the stronger \(O(1/L)\) error rate without further work.

The current catalogued exponential-sum bound at block scale beta=2/5 exceeds the theta=5/2 target by 9/3980 before any fixed saving. A bounded audit of known estimates is useful; a new logarithmic-phase or combined-block cancellation is more likely to change the outcome than an unrestricted search through familiar exponent-pair transformations. Smoothing alone does not eliminate the gap.

**Success:** a proved estimate for the actual weighted remainder, or a signed physical substitute, on a newly covered unbounded strip. **Remaining obligation after success:** the inner cusp below 5/2 and the finite transition.

[Workstream definition and tagged notes](../notes/01_weighted_outer_remainders/README.md)

## PR02 Signed control in the inner cusp

**Objective:** prove a source-prescribed energy-relative lower bound on both full stationary sets, sufficient to exclude candidate collisions and their predecessor curves.

The preferred finite-resolution observation is \(J_{j,N}=-h_jh_{j+2}^{(N)}\), which retains the full amplitude and vanishes automatically at \(E=0\). Seek a paid lower bound with fixed polynomial growth in the cutoff. Complete tails and Young's inequality transfer it to the logarithmic-loss criterion. Coefficients may deteriorate at infinity or as time tends to zero; they must remain locally bounded near each finite positive-time candidate event.

The genuinely new work can be restricted to \(E\le\delta\Gamma^2\), where delta is fixed in advance and Gamma is the explicit nonvanishing Stirling carrier without its zeta factor. On a declared domain with 0<t<=1/2 covering the nearby predecessors of a candidate collision, those predecessors eventually lie in this region. Independent absolute bounds handle the complementary region.

The speculative mechanism is an exact theta or Poisson relation among actual arithmetic block amplitudes. Explore whether transformed boundary terms telescope or whether integrated cumulative moments preserve a useful signed cancellation. The paired form is indefinite for arbitrary amplitudes; positive source weights, heat evolution, and stationary identities alone are insufficient.

**Success:** one new source-derived signed estimate on a declared unbounded inner domain, with a path to coverage of all remaining candidate events. **Failure of a candidate mechanism:** a certified violation on a genuine stationary point, or a precise obstruction to that declared mechanism. An undecided interval enclosure is neither.

[Workstream definition and tagged notes](../notes/02_signed_cusp_control/README.md)

## PR03 Effective heights and finite bridging

**Objective:** evaluate useful analytic starting heights, connect a proved asymptotic region to finite coverage, and supply small certified experiments that discriminate proposed mechanisms.

A pilot should isolate both physical stationary observations at prescribed theta values, including below two, and track complete retained and omitted interactions. Cutoff and precision choices must follow the source-tail and cancellation budgets. Exploratory ratios may suggest a coefficient rule, but independent validation must use a frozen rule and fresh cells.

The present exponent saving 1/20000 is conservative and slow. Evaluate constants and seek sharper effective estimates before planning a large bridge. Repeated small finite extensions alone do not resolve the unbounded cusp.

**Success:** either a closed verified bridge to an evaluated analytic cutoff, or a decisive certified test of a specified inequality. **Non-goal:** treating favorable finite samples as an all-height theorem.

[Workstream definition and tagged notes](../notes/03_effective_bridge/README.md)

## How we are implementing the broader program

The active approach is to turn the global collision criterion into source-specific estimates at the physical energy scale. PR02 is the principal route toward that endpoint. PR01 is a parallel, bounded effort to improve outer coverage and understand the arithmetic obstruction. PR03 supplies effective coverage and carefully chosen tests for both.

The immediate sequence is to specify the complete signed observation and a source-derived coefficient rule, identify a theta relation that could pay its adverse part, and run one affordable certified pilot to discriminate that mechanism. A successful pilot leads to an unbounded-domain lemma; an unsuccessful one leads to a documented obstruction or a revised mechanism. The manuscript integration and conditional transfers establish the present starting point, not completion of that arithmetic step.

## Dependencies and stopping conditions

PR01 supplies additional outer coverage and may improve the inputs to PR03. PR02 addresses the region where the current nonvanishing-carrier argument loses its elementary justification. PR03 tests PR02 mechanisms and closes finite gaps when an affordable analytic endpoint exists.

The global endpoint requires a coverage argument. Even thresholds tending to zero need not cover a fixed hypothetical collision if their starting heights simultaneously tend to infinity. A proof on one closed strip is not a proof of RH.

Deprioritize changes of delay that do not improve the combined signed observation, another hypercomplex representation without a new inequality, universal matrix positivity for arbitrary block phases, and coefficients defined by division by observed energy. Treat modular cancellation and the weighted remainder as proposed arithmetic mechanisms until their bounds are proved.

## Working conventions

Use this folder for the broader program and how its parts fit together. Keep the specific workstream definitions, targets, and incremental arguments in their tagged subfolders under `notes/`. Preserve the canonical historical notes. Save computations and small execution receipts in `numerics/`, reviews in `reviews/`, and concise manuscript milestones in `DRAFT_HISTORY.md`. Do not create manuscript snapshot folders. The current chat remains history 12 in the formal replay lane; its registry is the authority for evolving capture metadata.
