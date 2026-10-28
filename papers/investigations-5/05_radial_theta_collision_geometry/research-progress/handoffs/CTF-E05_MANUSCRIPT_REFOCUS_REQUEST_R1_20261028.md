# Rewrite the manuscript around conservation of the entire integral

28 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, Investigation05 chat0011, **Summarize commutator approach**.

**Task: CTF-E05. Type: E — execution. Recommended model: Sol. Request revision: R1. Parent: the completed CTF-E04 integration.** The author has specified the editorial direction; the work is a bounded reorganization of accepted material. This request is ready for execution. [Progress04][progress] owns live status. Issuing the instructions does not dispatch a chat or change a model.

## Editorial objective

Make conservation of the complete theta observation the organizing principle from the opening paragraph onward. Bring the reader directly from the canonical source and observation to **Conserving the entire integral**, then to the feedback magnifier and its two estimate tests.

The author explicitly permits earlier sections to be rewritten or deleted, without retaining them as background. Do not satisfy this request by adding a disclaimer while leaving the old sequence dominant, or by moving the old sequence wholesale into an appendix. The earlier proofs remain available in their existing research notes.

Edit the single existing source in place:

/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/05_radial_theta_collision_geometry/radial_deformations_and_zero_dynamics.tex

Keep its editor open. Do not create a replacement document, another source snapshot, a separate PDF, or another tab. Use the built-in compiler on this saved source after editing.

## Inputs and baseline

The [manuscript][manuscript] inspected for this request has 1967 lines, 82925 bytes, and SHA-256:

ecd862c935ffd3587c01f514339b7afeef77e07172d8152bf6950dfbc5dd0a71

Section numbers below refer to that baseline. Re-read the current file and preserve intervening authorized edits; a changed hash is a reason to inspect the difference, not to restore this baseline. [Note33][integration] and [Review19][review19] describe the completed integration. Use [Note25][n25], [Note28][n28], [Note29][n29], [Note31][n31] and [Continuation32][n32] for the retained mathematics and its scope.

Follow the [repository model workflow][workflow], [result index][results] and [avoid index][avoid], especially [geometric and conservative results][geometry], [collision controls][controls], [scoped failures][a07] and [volume without a gain][a20]. This task adds no mathematical claim.

## Target structure

Use the following sequence, allowing small editorial changes to headings:

1. **Purpose and conserved observation.** State the invariant, the collision question and the strategy: preserve the observation and its actual frequency derivative, magnify their simultaneous cancellation, then seek an independent estimate from the complete theta source.
2. **The canonical theta source and observation.** Define the unchanged full theta sum, its physical heat weight, the integral defining H, and the tail and differentiation facts needed below.
3. **Conserving the entire integral.** Make the current Section11 the first substantive flow section, immediately after the source setup. Include local conservation, the whole-space density, ordinary heat, a compact exact-control subsection, and the collision decay diagnostic.
4. **An energy-normalized conservative feedback.** Retain the current Section12 and its proofs.
5. **Positive-carrier comparison and quantitative regularity.** Retain the current Section13 and its comparison with direct first-jet information.
6. **The canonical source relation and its residual.** Retain the current Section14 and its proofs.
7. **The remaining signed theta estimate.** Retain the precise open problem from the current Section15.

Keep the inherited fourth-moment restriction in its appendix. There should be no standalone Darboux, angular-localization, tube-comparison or projected-annular-flow chapter before the conservation section, and no historical appendix containing those removed chapters.

Use **Conservative Theta Flows and Collision Amplification** as the working title and matching PDF title. Retain the current source filename, the author credit to Edward Baker, and the appropriate LLM acknowledgment.

## Changes to the opening and earlier material

Rewrite the abstract around whole-integral conservation, the heat diagnostic, the feedback deadline, the carrier comparison and the source-relation residual. Remove the opening advertisement for Darboux and projected-annular realizations. Retain the conclusion that no new theta collision exclusion or de Bruijn–Newman bound has been obtained.

Rewrite the introduction as the present mathematical program. Remove the promise to retain the pointwise radial requirement as a useful stronger subclass, and remove the chronological roadmap through Sections3–10. Replace wording such as “the weaker requirement” with a direct statement of the chosen invariant. Explain that the general search permits redistribution across radii. A short distinction is enough: the current theta heat and feedback solutions remain radially symmetric, while their profiles change with auxiliary time. Radial symmetry is not preservation of the radial integrand.

Keep the canonical source definitions and tail lemma from current Section2. Remove the tail-flux subsection unless an actual surviving proof uses it; the current conservation and feedback sections do not. Remove current Sections3–7, which develop the selected forced response, Darboux family, its time and deformation laws, interior zero motion, and transported energy. Remove current Sections9–10, which develop the pointwise radial invariant and projected annular response.

This is an editorial change of focus, not a retraction of those results. In particular, the Darboux pairing already preserves a complete integral with a changing source and test function; do not incorrectly describe it as merely preserving the radial integrand.

Rewrite current Section8 as a short control subsection in the new conservation section. Retain the positive-source family, its convergence domain and its exact event in the physical frequency:

\[
\Phi_*(u)=(64u^4+6)e^{-(4+T_c)u^2},\qquad
H_*(T_c,a)=\frac{\sqrt\pi}{16}(a^2/4-6)^2e^{-a^2/16},
\qquad A_*=2\sqrt6.
\]

State that the heat integral converges for t < T_c+4, and identify T_c=1/4 when the later fixed example uses it. Retain why the control satisfies the generic heat and feedback premises but lacks the complete canonical source. The fields Y, Z and their Darboux transforms, the parameter kappa, and their sign argument are unnecessary for this use and can be deleted.

## Dependencies that must survive the deletion

The current Section11 onward has three explicit references into the earlier material: eq:fullthetaflow, lem:tails and eq:Q. Retain the source formula and lemma near the beginning, and move or redirect the full-theta reference. Define Q_(t,N) locally as the N-term truncation when it is first used.

There are additional dependencies that label checking alone will miss:

- The fixed-cosine-kernel qualification uses spherical averaging, currently defined in the removed section. Keep that qualification: preserving every frequency against the same fixed test kernel can force the radial average to remain fixed. Define the average locally, or state the argument directly in radial coordinates. Explain why evolving the full frequency-dependent density permits radial redistribution.
- The heat diagnostic and feedback refer literally to “Section8.” Replace these with a label for the relocated control, and check for all other hard-coded section references.
- Simplify the opening variables and compact-domain statement after removing lambda and kappa. Use the physical frequency a, the fixed mark p=(T,A), Newman time t and auxiliary time s consistently. Keep r=exp(2u); introduce x=log r only if a surviving calculation uses it. Retain the distinction between the fixed mark and the running frequency derivative. Do not enlarge any theorem's parameter range while simplifying notation.
- Keep the source normalization factors, the single exterior integral representing all of H, and the full-space evolving domain. The initially empty unit ball belongs to the evolution.
- Remove the obsolete comparison with a zero-initialized perturbation G after the heat theorem if its only purpose is to recall the deleted projected flow.

Preserve useful existing labels. Remove unused macros and bibliography entries after their final use disappears, and preserve citations supporting every retained theorem.

## Mathematical content to preserve

Keep the current heat conservation and finite-frequency-derivative statements, physical time identity, central decay diagnostic, and their moment allowances. Preserve the fixed feedback equation, unit preparatory smoothing, unit component weight and diffusivity, the selected radial drift, actual marked derivative, local construction, exact gradient identity, finite collision deadline, converse, control, and the scoped failure of the generic initializer comparison.

Keep the sharp carrier inequality and the condition that regularity bounds require an independently established first-jet margin. Keep the source-relation preparation defect, full commutator, actual second frequency derivative, unit-sphere cancellation, inner-ball energy and origin-domain qualification. The stopped variant is the fixed zero-residual substitution; coupled estimates remain open.

Do not alter the equation to break radial symmetry, reopen a stopped comparison, or present global regularity as an independently proved theta estimate. The scope is exposition and dependency repair; no PDE simulation, numerical campaign, new literature survey or new proof strategy is required.

## Verification and completion

Completion requires all of the following:

- The abstract, introduction and section outline agree on the current program. “Conserving the entire integral” follows the source setup as Section3, with no older flow chapter before it.
- The retained arguments are self-contained after deletion. Check both labels and prose dependencies, the exact-control normalization, variable definitions, bibliography, and the distinction between radial symmetry and radial-profile conservation.
- Compile the saved original source with **compile_latex_document**, passing its existing absolute path. Resolve errors and undefined references using that built-in workflow. Do not run a separate PDF build or open another preview. Record what the compiler actually confirms; do not claim visual inspection if none was available.
- Read the result once for continuity and scope. Preserve the current acknowledged proof status and all essential assumptions; do not add repeated disclaimers to replace a coherent explanation.

Save one short editorial return in notes or reviews with the actual model and effort, the request revision, input and output source hashes, a compact old-to-new section map, removed material, retained dependencies and compiler result. Append the completed disposition to Progress04. Update current navigation and MANUSCRIPT_BUILD.md where their title or section descriptions become stale. Add a concise DRAFT_HISTORY.md entry only after the rewrite is complete; do not create a snapshot.

Keep Note33, Review19, record17, earlier notes, old request packets and historical milestone rows as dated records of their versions. Repair current descriptions without rewriting those historical outcomes. Keep this request R1 fixed; append a return link instead of replacing it.

Permitted writes are the existing manuscript, that compact return, the live E05 entry, and necessary current navigation/build-history updates. Preserve unrelated working-tree changes. Root result summaries need no new mathematical entry for an editorial rewrite.

Stop after the rewritten source compiles and the continuity/dependency check is complete. Extract an already proved prerequisite locally when necessary. If a genuine unresolved mathematical premise is discovered, identify it under CTF-B02 and complete the unaffected editorial work; do not invent a new result to make the rewrite appear complete. No new B02 estimate is part of E05.

## Pasteable instruction for Sol

> Complete [E] CTF-E05, request R1, in Investigation05. Read this packet and the sole live Progress04 register. Rewrite the existing radial_deformations_and_zero_dynamics.tex in place so the manuscript moves directly from its purpose and canonical source to “Conserving the entire integral” as Section3, then the feedback, carrier and source-residual results. The author permits deletion of the earlier Darboux and radial-integrand-preserving exposition without keeping it as background. Retain the exact colliding control and every prerequisite of the surviving proofs, distinguish radial symmetry from preserving the radial profile, and preserve all mathematical scopes. Keep the current editor open, compile only through the built-in compiler, and save the concise editorial return and status update specified in the packet.

[progress]: ../04_CONSERVATIVE_THETA_FLOW_RESEARCH_PROGRESS_20261028.md
[manuscript]: ../../radial_deformations_and_zero_dynamics.tex
[integration]: ../../notes/33_NOTES28_29_31_MANUSCRIPT_INTEGRATION_20261028.md
[review19]: ../../reviews/19_CONSERVATIVE_FEEDBACK_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261028.md
[n25]: ../../notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md
[n28]: ../../notes/28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n29]: ../../notes/29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n31]: ../../notes/31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md
[n32]: ../../notes/32_SOURCE_RELATION_COMMUTATOR_CONTINUATION_20261028.md
[workflow]: ../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[geometry]: ../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a20]: ../../../../../avoid/20_volume_without_a_gain.md

## Appended completion return — request R1 unchanged

28 October 2026: **CTF-E05 R1 complete**. [Editorial return](../../notes/34_CTF_E05_MANUSCRIPT_REFOCUS_RETURN_R1_20261028.md) records the in-place rewrite, section map, source hashes, dependency checks and successful built-in compilation. Actual gpt-6.1-sol / ultra, Investigation05 chat0012. [Progress04](../04_CONSERVATIVE_THETA_FLOW_RESEARCH_PROGRESS_20261028.md) owns live status.
