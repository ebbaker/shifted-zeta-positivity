# Continuation after adaptive forcing and differentiated transport

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.

**Continuation entry point superseded by [Note 18](18_CONTINUATION_TOWARD_EXPLICIT_ALL_TIME_APPROXIMATION_20261024.md),
which carries the author's clarified explicit-formula and all-time goal.**
The research results below retain their original scope.

This supersedes [Note 15][old] as the continuation entry point. The user
approved the high-level plan and requested continuation. The first
bounded task is now written in [Note 16][note], with an explicit
regulator, averaged forcing/current budgets, and a differentiated
moving-clock comparison on the existing growing window. The full
boundary-evolution program remains unfinished.

## Read first

Follow repository AGENTS.md, LARGE_FILES.md, REFERENCE_WORKFLOW.md and
tools/CHAT_HISTORY.md. Read the [result index][results], especially
[heat geometry][geometry] and [collision controls][controls], and the
[avoid index][avoid], particularly [status][status-rule] and
[normalizations][normalization]. Then read Note 16, its [assessment][review]
and the [sole progress register][progress]. Notes 12 and 14 retain the
source/carrier and adaptive-regulator definitions used here.

No manuscript source was changed. The maintained 15-page fixed-epsilon
draft remains in manuscript/; Notes 14 and 16 are later extensions.
Save new derivations in notes, computations and small records in
numerics, and reviews in reviews. No manuscript snapshots or generated
PDFs should be added to these folders.

## Results to carry forward, with scope

Keep fixed compact spatial kernels and the p=1 saddle regulator
epsilon=M0*kappa^-1*exp[-x^2/(2kappa)]. On buffered
X~kappa^(1/3), all statements below are eventual analytic results,
proved in-note and same-assistant reviewed:

- Enlarged, fixed phase collars improve the integrated w and logarithmic
  bias allowances to O(kappa^-2). Their radii beta/mu are distinct from
  the O(kappa^-1/2/L) root-localization radii.
- The quotient H_zz/H is split into the actual root-velocity pole and a
  regular part. Its weighted integral is
  O(kappa^-5/3+L^2*kappa^-2).
- The distributional current bridge AT17 and the differentiated exact
  weak-bias identity AT22 pay finite-epsilon current and density-time
  errors. The averaged source is O(kappa^-5/3+L^2*kappa^-2), and
  potential forcing O(L^2*kappa^-2), both o(L/kappa).
- Complete source moment bounds through degree six give
  |m4-3v^2|=O(kappa^-9/4). The identity
  C3-3mu'*v=m3' cancels the leading cubic transport term.
  Every covered root satisfies a'=-(mu'/mu)a+O(kappa^-7/6).
- The moving mu-clock current and density time derivative approximate
  the corresponding adaptive averages with O(L*kappa^-7/6) error,
  smaller than the mean drift scale L/kappa.

Do not replace mu'/mu by 2/kappa in that last growing-window result:
the currently available coefficient error is multiplied by height.
Do not replace the finite moving clock by its constant-density continuum
without the phase-derivative allowance AT27. A continuum derivative
comparison at o(L/kappa) is supplied only on fixed height ranges.

The exact checks cover 16 polynomial and nine moment identities, plus
the radial source cancellation. [Finite allowances][record] retain the
failed collar gate at t=10^4 and the large derivative errors at 10^6
and 10^9. The sampled derivative allowance is below L/kappa at 10^12,
but no interval-certified onset or intervening-time theorem is claimed.

The [six-observation theta pilot][pilot] compares zero-measure current
and time derivative with the moving clock. It uses finite source
quadrature and refinement, with no root fitting. The continuum derivative
discrepancy reaches about 0.3143% of mu'/pi in the sample; the moving
clock discrepancies are tiny, with several at their refinement floor.
They are supporting diagnostics, not proof or finite-epsilon observations.

## Next bounded choice

The immediate forcing/current gate chosen in Note 15 has now been paid
on its declared inner window. A useful next task is an actual covariance
closure audit: specify a candidate from the source-derived mean/current,
then bound or measure the true differentiated covariance residual using
the same complete field and kernels. Defining a covariance to make a
chosen ansatz solve the equation is not independent validation.

The complementary analytic task remains the positive-time outer-height
approximation through amplitude turnover for this prescribed regulator.
It needs a complete complex-saddle estimate. If importing the Polymath
high-height result, inspect the full theorem and hypotheses first; its
earlier catalog entry was only metadata/abstract-checked.

Independent review and interval certification of useful finite gates
can be pursued separately. Before an evolved boundary solution, retain
the true covariance error, outer and negative-time derivative budgets,
source-fixed potential data, compatible boundary flux and stability.
HDA-02--06 remain partial and HDA-07--09 gated. The new bounded
adaptive-transport task HDA-12 is complete at this scope. No RH or
endpoint-simplicity conclusion is an acceptance target.

## Chat identity and records

This is chat **0003**, thread **01a16fe8-5cab-7812-a4cc-e3a30ee34f56**,
original title **Summarize heat-density research**, with one canonical
registration in this investigation's chat-histories/. Preserve its
identity; histories 0001 and 0002 are separate. Use the history tool
at the beginning and end of each reply and the bounded exact-turn
deferred capture as the last tool action until trusted hook activation
is verified. Never prewrite an unsent final reply into a transcript.

The research files belong to the checkout, not the synced project mirror.
Existing unrelated working-tree changes are preserved. No new commit,
manuscript snapshot or generated PDF was created for this bounded round.

[old]: 15_CONTINUATION_AFTER_MANUSCRIPT_AND_VARIABLE_EPSILON_20261024.md
[note]: 16_ADAPTIVE_FORCING_AND_DIFFERENTIATED_CLOCK_20261024.md
[review]: ../reviews/05_ADAPTIVE_TRANSPORT_SELF_REVIEW_20261024.md
[progress]: ../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md
[record]: ../numerics/ADAPTIVE_TRANSPORT_CHECKS_20261024.json
[pilot]: ../numerics/ADAPTIVE_TRANSPORT_THETA_PILOT_20261024.json
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[status-rule]: ../../../../avoid/06_status_stronger_than_the_evidence.md
[normalization]: ../../../../avoid/08_normalization_and_constant_slips.md
