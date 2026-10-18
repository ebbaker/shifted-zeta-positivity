# Review response, portable proof and the sibling benchmark

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **max**.

**Status:** documentation corrections and analytic proof expansion completed;
the existing quantitative statements retain their proved-in-note status.
The sibling 0.215 proof received an additional same-model audit, with no
blocking mathematical defect found. No new numerical bound or conductor
exponent is claimed in this continuation.

This responds to the four recommendations and next review target in
[review 03](../../reviews/03_CROSS_MODEL_MATHEMATICAL_REVIEW_CODEX_20261017.md).
It follows the [result-summary index](../../../../../result-summaries/README.md),
[avoid index](../../../../../avoid/README.md), the
[heat-flow summary](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[sibling-result caution](../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md),
[status caution](../../../../../avoid/19_status_files_that_lag_the_findings.md)
and [review-independence caution](../../../../../avoid/05_same_model_reviews_and_shared_premises.md).

## Response to the review

| Recommendation | Completed response |
| --- | --- |
| Reconcile status and fix the broken round-1 link | The investigation README now leads with the current comparison, review level and open H12 status. Its obsolete pending-audit description is explicitly historical; the contract link uses `notes/round-1/`. |
| Use the stronger sibling benchmark | The README and manuscript identify 0.215 for the same q >= 10^12 range, at its existing proved-in-note level. The 0.27 initial-floor application and conductor exponent remain distinct results. Historical reviews are preserved. |
| Make the analytic proof portable | The manuscript now includes complete-characteristic estimates, a stated compact-contact lemma, the backward Hermite argument, the global sine-tail floor, confinement, common Gaussian domination, nonvanishing and heat convergence. The exact scalar programme remains a named computational supplement. |
| Record the public conductor-limit discussion | The source ledger and manuscript now cite the incomplete MathOverflow discussion as provenance, with no theorem or priority claim imported. |

The [current source and PDF](../../manuscript/README.md) remain the single
editable manuscript. The [build record](../../manuscript/BUILD_RECORD.json)
identifies the revised source and PDF, the unchanged numerical supplement,
and the preceding version. The historical notes and reviews retain the
versions and statuses that their hashes identify. No snapshot directory
was created.

## Mathematical checks on the expanded proof

The general input has order at most one; it need not obey a finite-type
bound or the stronger O(R log R) growth estimate. The characteristic proof
uses that stronger estimate only for the actual Dirichlet flow or a fixed
sine approximant. The new appendix says this explicitly. For an arbitrary
input, the bound on each canonical factor and the convergent sum of
|rho|^(-sigma), 1 < sigma < 2, supply a common sub-Gaussian majorant for
passing the approximation through the heat operator.

The compact lemma states the growth, nonzeroness, strip, positive floor
and confinement hypotheses. Its strict barrier starts above the entire
initial strip. A simple first contact contradicts zero motion; a multiple
contact has an earlier zero higher by order sqrt(v), whereas the barrier
changes by order v. Reality at the zero endpoint follows from strip
contraction and Hurwitz. The heat inverse excludes an identically zero
limit. Confinement constants may depend on the fixed approximant; they
are never passed to the limit.

The finite arithmetic was not changed or rerun without need. Its exact
replay was completed in review 03. The manuscript was compiled twice
after the final edits with no warnings, unresolved references or box
warnings; all ten rendered pages were inspected. These are authoring
checks of this revision. The new appendix text has not received a separate
specialist review.

## Additional audit of the 0.215 result

The [sibling audit](../../../03_effective_outer_remainders/reviews/03_FAMILY_FLOOR_AND_RESTART_AUDIT_CODEX_20261017.md)
checks the Gamma saddle and transport remainder, every ordinary and
reflected tail, parameter monotonicity, the first interval next to time
zero, and the finite restarted strip comparison. Its
[replay record](../../../03_effective_outer_remainders/numerics/REVIEW_03_FAMILY_REPLAY_CODEX_20261017.json)
pins the sources and both byte-identical outputs.

The audit retains the floor S_chi(x,3,t) > 6 for all real x,
0 <= t <= 1/4 and primitive q >= 10^12, and the resulting
Lambda_chi <= 43/200. The precise conclusions are sufficient positive-time
estimates, not RH-equivalent criteria. The
[existing collision screen](../../../03_effective_outer_remainders/notes/round-2/01_UNIFORM_FAMILY_FLOOR_CODEX_20261017.md)
identifies the arithmetic premises absent from the controls in
[summary 12](../../../../../result-summaries/12_collision_controls_and_screening.md):
the Euler-factor control violates the prime logarithmic-coefficient bound;
the other shape controls do not supply the primitive-character Euler
product and partial-sum estimate. No universal exclusion of their actual
floors is asserted, and no new control computation was required.

One nonblocking documentation finding remains in Project 03's manuscript:
its introductory literature and scope paragraphs predate both the
Ki–Kim–Lee correction and its own round-two consumer. The sibling review
identifies the exact passages and corrections; this continuation does not
silently rewrite that separately maintained manuscript or PDF.

## Model provenance and next decision

Edward Baker chooses models in light of latency and usage, and generally
tries to alternate GPT and Claude for derivation versus review. Earlier
model assignments are suggestions, not requirements. Record actual usage
without recommending a model for the next task.

This session uses gpt-6-astra at max effort. Review 03 of Project 01 used
a different GPT model from its gpt-6.1-sol derivation. The additional
Project 03 audit uses the same model as that project's round-two derivation
(whose recorded effort was ultra). Neither is independent specialist
review, and a different effort level does not change that classification.

The bounded next steps requested here are complete. The current research
benchmark is 0.215 at q >= 10^12. Further mathematical work can be judged
by a sharper general comparison, a better conductor exponent, or a lower
certified conductor threshold. The earlier near-threshold tables,
derivative-circle consumer and zeta 0.18891 claim retain their existing
unproved or conditional inputs; this audit does not certify them.
