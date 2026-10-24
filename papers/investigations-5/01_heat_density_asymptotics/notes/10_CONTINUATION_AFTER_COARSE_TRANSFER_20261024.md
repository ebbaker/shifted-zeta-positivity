# Continuation after coarse transfer and weak transport

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

**Historical handoff:** the current continuation is [Note 13](13_CONTINUATION_AFTER_TWO_TIME_LIMITS_20261024.md),
which adds the author's two-time-limit, stationarity and Vandermonde directions.
The bounded-round record below is retained unchanged.

This supersedes [Note 07](07_CONTINUATION_FOR_NEW_CHAT_20261024.md) as the
next-step handoff while preserving its first-round record. Continue
`papers/investigations-5/01_heat_density_asymptotics` in the research
checkout. The objective remains the unnormalized average density,
including spatial/time smoothing, fluctuations, compatible boundary
data and comparison with actual theta evolution. No boundary-matched
reduced solution or RH/simplicity result exists.

Read repository AGENTS.md, LARGE_FILES.md, REFERENCE_WORKFLOW.md and
tools/CHAT_HISTORY.md. Read the [result index][results], especially
[heat geometry][geometry] and [collision controls][controls], and the
[avoid index][avoid], especially [classification][a01], [status][a06]
and [scoped conclusions][a07]. Preserve their status words.

## What was added; do not repeat the pilots

- [Note 08][contract] fixes a second contract: t in [512,1024], fixed
  lx=10, hy=.75, epsilon=1e-4, x centers 0,1,2 and y centers 0,.25,.5;
  the extra offline time average is centered at 768 with halfwidth 64.
  The spatial average spans roughly seven to nine density periods.
- [Note 09][transfer] proves conditional complete-source moment bounds
  for f=H/M compared to (1-vz^2/2)cos(mu z). The carrier disks then
  supply the lower bounds needed for the logarithmic regulator estimate.
  The whole finite rectangle, not merely fixed root labels, is covered
  **if its moment premises are supplied**. Numerical inputs are floating.
- A scaled source implementation evaluates weighted mass, zero-measure
  current and its time derivative by contours, with no theta root finding
  or peak quadrature. Across the finite slice/time-average cases the
  leading model Rm=(mu/pi)k_h(y), Jm=-(mu'/pi)x k_h(y) has maximum
  observed relative errors 0.02984%, 0.08560% and 0.35888%, respectively.
  Mu'=2 mu v+m3 is obtained from the complete-source formula numerically.
- The regulator-bound log10 values at t=512,768,1024 are -328.85,
  -649.45 and -1028.87 as floating formula evaluations. They are **not
  certified upper bounds or total numerical errors**. The analytic
  coarse-transfer bounds are substantially more conservative than the
  measured errors. No source-tail/quadrature interval was computed.
- The first contour refinement failed its mass tolerance; the final
  224-node contour computation meets the diagnostic tolerance. The
  original failure, source refinements, displaced contours, time finite
  differences and controls remain in the [record][data].
- Note 09 (15)–(16) keeps phase-cell, transverse and temporal covariance
  terms in a source-anchored potential ansatz. Its Q is defined by the
  model equation. It is bookkeeping, **not an independently validated
  theta covariance closure**. The actual test was the weak current.

The [same-assistant assessment][review] audits these limitations.
The [sole progress ledger][progress] retains HDA-02/04/06 as partial and
HDA-07–09 as gated. The negative-time results from Note 05 and the small-
window round-one results remain valid only at their recorded scope.

## Next bounded step

Prefer one of these two concrete advances, with a new narrow contract:

1. **Certify the source input on a short positive-time slab.** Enclose
   M, mu, v and the absolute exponential third moment, including all
   u/n tails and quadrature. Propagate the disk and kernel constants
   through the slab; retain the absolute regulator scale. Pay contour
   integration errors if claiming measured accuracy, not just the much
   looser analytic transfer. A bounded slice certificate is already a
   meaningful step; do not claim all t in [512,1024] from three samples
   or from temporal quadrature nodes. The record contains sufficient
   margin to choose a small slab without guessing a global theorem.
2. **Measure a genuine differentiated covariance or equivalent current
   error with finite-regulator control.** The weak zero-measure current
   comparison does not certify Delta(Qtheta-Qg), finite-epsilon current,
   or evolved-solution error. Use a logarithmic-potential/weak method
   compatible with the enormous amplitudes and tiny eta. Do not directly
   sample the narrow peaks or call a kinematically defined Q a closure
   test. Keep the source harmonic/additive potential terms and all
   further averaging variances. Changing widths requires commutators.

Computing explicit negative-time derivative remainders remains a useful
alternative, without repeating Note 05's coefficient algebra. A final
boundary solve still needs both time-end budgets, source traces, flux
matching and residual amplification; the mixed-sign PDE has no stability
theorem here. Broader/later slabs and growing-period limits remain open.

Use [coarse_theta_round2.py][script] only at its documented finite scope.
It requires Python 3 and NumPy, and keeps scaled source weights and log
regulator bounds. Reuse the record unless a code change, failure or new
question justifies rerunning. Its real-zero contour interpretation uses
the moment gates; a contour polynomial is not a real-plane kernel weight
for arbitrary complex zeros. No independent evaluator was produced.

## Files and chat identity

Keep derivations in notes, code/small records in numerics, assessments in
reviews, and update the existing research-progress ledger. No manuscript
was edited, no snapshot made and no commit created. DRAFT_HISTORY.md
records the bounded milestone; other repository work must be preserved.

This chat's actual thread id is `01a16fb7-14ae-7d23-a933-972eca16a782`,
history **0002**, title **Continue heat density investigation**, in this
investigation's chat-histories folder. It is distinct from founding
history 0001. Preserve both identities. New chats register their own
actual identity/title/source through tools/refresh_chat_history.py in the
same folder. Refresh at each turn's beginning and end; the documented
exact-turn deferred final capture is the last tool action unless trusted
hook activation is verified. Read current provenance/hashes/counts from
the registry; do not copy stale capture statistics into handoffs.

[contract]: 08_SECOND_BOUNDED_COARSE_AVERAGING_CONTRACT_20261024.md
[transfer]: 09_COMPLETE_SOURCE_MOMENT_TRANSFER_AND_WEAK_CURRENT_20261024.md
[review]: ../reviews/02_COARSE_TRANSFER_AND_WEAK_CURRENT_SELF_REVIEW_20261024.md
[data]: ../numerics/COARSE_THETA_ROUND2_20261024.json
[script]: ../numerics/coarse_theta_round2.py
[progress]: ../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a06]: ../../../../avoid/06_status_stronger_than_the_evidence.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
