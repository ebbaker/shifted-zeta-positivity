# CTF-E05 R2: analytical manuscript consolidation

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**, Investigation05 **chat0031**, **Continue CTF-B02 Astra assessment**.

**Completed editorial integration; no new mathematical result claimed.**
At the author's explicit request, the [main manuscript][tex] now develops
the analytical results by their logical dependence. The [28-page reading
copy][pdf] has been compiled and visually checked. Numerics remain
supporting evidence. [Review37][review] is a same-assistant editorial
assessment, not a new independent proof assessment.

The request arrived while Sol assessed R10 in chat0032. That assessment
completed before the manuscript was installed: [Review36][r36] accepts
all eight obligations without mathematical correction and clarifies that
E0 is field energy. This revision incorporates that clarification.
No message was sent to the other chat and no agent was spawned.
Its frozen proof and assessment documents remain unchanged.

## 1. Mathematical organization

| Manuscript location | Analytical role and provenance |
| --- | --- |
| Section 2 | Complete theta source, full-integral heat conservation, exact Gaussian-polynomial control and central-decay diagnostic; Notes25/28 remain the underlying records. |
| Theorem 3.2 | Collision/noncollision lifespan dichotomy, now with the stronger weighted Fourier deadline from the [direct comparison][direct]. |
| Lemma 4.1 and Proposition 4.2 | Exact radial square from Note42, followed immediately by retained-diffusion and local gradient comparisons. |
| Lemma 4.3 and Theorem 4.4 | Sharp mass-energy-moment inequality followed by Note67's explicit uniform radial feedback theorem, assessed in Review36. |
| Proposition 5.1 and Section 5.1 | Complete-source slope and moment proof, H>(70/73)M, and fully analytical K_theta; Notes55/63/67. |
| Section 6 | Exact raw relation, genuine preparation defect, full commutator, sphere cancellation and origin-domain requirement; Note31. |
| Proposition 6.2 | Note51's scoped observation-kernel freedom: fixed theta amplitude and zero raw mismatch do not select cosine. |
| Theorem 7.2 | The strongest established coupled weighted closure is presented once, using Notes40/42/44/47. |
| Section 7.4 and Appendix B | Note55's actual prepared cosine correlation and its supporting second-jet bound. |
| Section 8 | Outstanding analytical, coverage and review tasks. |
| Appendices A/C | Complete coefficient/preparation proofs and inherited fourth-moment domain. |

The first-moment Fourier cap now gives
\[
 S_{\max}\le
 6(10\pi^2)^{-2/5}\mathsf P_0^{4/5}E_0^{-2/5}
 \le S_{\rm w}:=
 6(10\pi^2)^{-2/5}(MR_0)^{2/5}E_0^{-2/5},
 \qquad m=0.
\]
The first inequality uses the actual prepared first absolute moment;
the second uses its carrier upper bound. Both are conditional upper
deadlines. They are not lower regularity horizons.

The uniform theorem states
\[
 g\le K_\infty,\qquad
 a_*\le\alpha\le2K_\infty/3,\qquad B(s)\ge a_*s.
\]
Its positive physical margin is explicit. The full weighted closure
still grows with the horizon after this substitution; no uniform
residual or higher-jet assertion was added.

## 2. Consolidation decisions and scope

**Superseded comparisons are retained in the archive, not used as the
active benchmark.** The old half-energy deadline and its specific weak
initializer-ratio calculation remain in Note28. The manuscript replaces
that deadline, and removes the dependent ratio rather than silently
reuse a formula with a changed denominator.

The successive coarse, radial and source-coupled weighted bounds are
consolidated into the final theorem. The exact radial square is moved
before the carrier argument because it supplies the exponent-7
differential inequality needed by the uniform theorem. The final
source coupling still gives the same-B coefficient improvement 49/600;
it supplies no source-residual advantage for the uniform-feedback
consumer.

Note59's paid finite variance restart remains a cited analytical
refinement. Its long H3 coefficient calculation is not duplicated in the
main text. Note63's second-cancellation estimate remains valid in its
stated split class, but the stronger direct Sw is the manuscript's
active deadline comparison. No numerical acquisition, numerical PDE
evolution, new mark or second research candidate was undertaken.

The Gaussian-polynomial control retains its true raw-mismatch term in
the weighted estimate. The polynomial-kernel comparison fails literal
cosine and the physical Newman equation; it is not a theta collision.
The complete source, preparation, actual fixed-mark jets, full cutoff
commutators, combined sphere numerator and whole inner ball are retained.

## 3. Build, preservation and evidence

[Build record27][build] identifies the prior/current source, PDF and log
hashes. The installed source matches the compiled and rendered source.
Local latexmk and the desktop compiler both succeed. The final local
log has no warnings, undefined references, or overfull/underfull boxes.
All 28 pages were inspected as full-page PNGs at 100 dpi. Eight pages
affected by the final wording/page-break edits were inspected again;
the other 20 images remained byte-identical.

The **123 preexisting proof, review, handoff and companion files** in the
intake baseline remain byte-identical. The separate new editorial intake
was also unchanged when the manuscript was installed; it is now updated
with completion. Earlier notes, assessment packets and reviews retain
their historical status. The old main source is recoverable from the
recorded existing Git commit; no new commit, tag or snapshot folder was
created. The working PDF and log are in ignored repository-root output.

The prior R10 packet's manuscript hash identifies its completed assessment
version. It is intentionally not rewritten to pretend this later
editorial revision was assessed by Sol. Review37 and record27 identify
this new version. The companion manuscript is unchanged.

## 4. Continuation

Read [Continuation72][next] before the next conceptual choice or model
change. The substantive next task remains **[B] CTF-B02 — Astra**, with
one unpaid quantity or precise advantage over the accepted direct bound.
Parent B02 remains partial; numerical acquisition and coverage remain
gated. The manuscript now describes those limits at the end of its main
development.

The [result index][results], especially [spatial-flow results][spatial]
and [collision controls][controls], and the [avoid index][avoid],
especially [target classification][a01], [shared premises][a02],
[scope][a07] and [quantitative utility][a20], retain their authority.
The present milestone is editorial consolidation of those scoped results.

[tex]: ../radial_deformations_and_zero_dynamics.tex
[pdf]: ../../../../output/pdf/radial-theta-collision-geometry/conservative-theta-flows.pdf
[review]: ../reviews/37_ANALYTICAL_MANUSCRIPT_INTEGRATION_REVIEW_20261029.md
[r36]: ../reviews/36_UNIFORM_FEEDBACK_E08_R10_ASSESSMENT_20261029.md
[direct]: CTF_B02_R9_WEIGHTED_DIRECT_COMPARISON_CHAT0029_20261029.md
[build]: ../numerics/27_ANALYTICAL_MANUSCRIPT_BUILD_RECORD_20261029.json
[next]: 72_ANALYTICAL_MANUSCRIPT_AND_MODEL_CONTINUATION_20261029.md
[results]: ../../../../result-summaries/README.md
[spatial]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md

