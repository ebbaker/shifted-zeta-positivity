# Continuation after radial drift integration

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, Investigation05 **chat0021**, **Continue CTF-B02 R4 estimate**.

**Next: [E] CTF-E07 R2 — Sol.** Prove one conservative analytical bound
for the existing cutoff/drift coefficient B1 that makes the compact
weighted improvement strict. The [issued R2 packet][packet] is the
frozen execution contract. This note does not execute it.

| Task | Type and recommendation | Readiness and output |
| --- | --- | --- |
| **CTF-E07 R2 — default** | **E — Sol:** scalar coefficient and cutoff calculus with a fixed target | Ready, not started; prove B1<=b<455/24 or return one precisely unresolved payment |
| CTF-B02 | B — Astra for a new conceptual estimate | Parent partial; a changed coefficient target, cutoff, weight or functional requires a recorded B revision |
| CTF-E03 / CTF-B03 | E — Sol / B — Astra | Gated; no numerical acquisition or coverage extension follows |

## Reading order and current manuscript

Read [GPT_RESEARCH_MODEL_WORKFLOW][workflow], the sole [Progress05][progress]
and [Overview05][overview]. Then read [Note42][n42], [Review23][review],
manuscript Section7.4, Note40's coefficient definitions and Note31's
exact cutoff. [Build record22][record] identifies the current 24-page
reading copy and preserved sources. [MANUSCRIPT_BUILD][build] gives the
reading/preview paths. The original R1 packet and Notes39–42 remain
unchanged; their issue-stage statements retain their dated meaning.

R4 and its requested E08 integration are complete. Section7.4 proves
K=10G+(21/4)E0-H_rad with H_rad>=0, replacing the old 30E0 allowance.
It sharpens the conditional gradient and expanded weighted estimates
and gives a strictly longer local interval than the old estimate retaining
diffusion. It uses radiality and prepared decay, admits the exact
colliding control, and supplies no theta separator or deadline payment.
The full source/residual/cutoff/actual-jet/sphere/inner-ball terms remain.

The next task is narrower than another conceptual search. The compact
constants satisfy exactly
\[
 \kappa_1-\kappa_{1,\rm rad}
 =\max\{0,455/24-B_1\},\qquad
 \kappa_{1,\rm rad}=265/24+B_1+B_0.
\]
The expanded gain is already unconditional. A proof B1<=b<455/24 would
add the explicit strict gap 455/24-b>0 in the compact coefficient. This
condition was named in Note42; no new functional or source premise is
being selected.

## Fixed question for Sol

Keep the exact weight omega=(1+r^2)^(-2), drift v=lambda(r)X with
lambda=1+1/(1+r^2), and cutoff eta=h(4r-2) from Note31. The R2 packet
specifies the complete scalar coefficient to bound, including eta'.
Pay the zero region r<=1/2, exact transition 1/2<r<3/4 and entire
exterior r>=3/4. Use conservative elementary inequalities; no optimizer,
sampling, PDE evolution, source quadrature or numerical certificate is
needed. B1 depends only on this fixed cutoff/drift, not on T or a.

Return one explicit all-radius b below the threshold and the resulting
conditional compact exponential gain, or name the exact unresolved
inequality and its radial domain. Do not adjust the cutoff, weight,
functional, target or source if an allowance fails. Stop and return to
B02 rather than beginning another attempt. Save the execution in the
notes folder and update the sole register with actual model and effort.
A completed proof may next be assessed proportionately under E08;
that later integration is not asserted by this continuation.

The [result index][results] and [avoid index][avoid] remain required,
especially [controls][controls], [target classification][a01],
[scoped claims][a07] and [combined versus separate bounds][a12]. The exact
Gaussian-polynomial collision at (1/4,2sqrt(6)) stays admitted; use its
same-theta-operator residual with both commutator and raw mismatch terms.
A smaller generic compact coefficient is not collision exclusion.

Review23 is internal Sol assessment by prior contributors, sharing
inherited premises; model roles in Note42 are Astra/max conceptual work
and Sol/ultra parent/checks. No specialist independence is claimed. Keep
this conversation's unique chat0021 archive; future chats register their
own actual identity in this investigation under the standing history tool.

## Pasteable prompt

> Read GPT_RESEARCH_MODEL_WORKFLOW, Progress05, Note43, the frozen
> CTF-E07 R2 request, Notes31/40/42 and manuscript Section7.4. Complete
> [E] CTF-E07 R2 — Sol: one conservative analytical all-radius bound
> B1<=b<455/24 for the unchanged exact cutoff, weight and drift. Retain
> the eta' transition term and pay the infinite tail. Derive the strict
> compact coefficient/exponential comparison using the same information,
> while admitting the colliding control. Return a proof or one precise
> unresolved inequality; no optimization, numerics, second coefficient,
> changed cutoff/functional/source/PDE or automatic extension. Save the
> return, update the sole register with actual model/effort, preserve the
> issued packet and unique chat-history identity, and stop at the boundary.

[packet]: ../research-progress/handoffs/CTF-E07_RADIAL_COMPACT_COEFFICIENT_REQUEST_R2_20261029.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[overview]: ../research-overview/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_OVERVIEW_20261029.md
[n42]: 42_RADIAL_DRIFT_PRODUCTION_IMPROVEMENT_B02_R4_20261029.md
[review]: ../reviews/23_RADIAL_DRIFT_IMPROVEMENT_E08_INTEGRATION_20261029.md
[record]: ../numerics/22_RADIAL_DRIFT_INTEGRATION_BUILD_RECORD_20261029.json
[build]: ../MANUSCRIPT_BUILD.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
