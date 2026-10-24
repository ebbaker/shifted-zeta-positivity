# Continuation: flexible analytic research toward RH implying simple zeros

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. This is a research handoff and history-verification record, not a new arithmetic estimate or simplicity theorem.

## Governing direction

**Find the strongest analytic result we can establish in support of RH implying simple zeta zeros. Let the successful argument determine the theorem and the manuscript.** The author expressly clarified that we are not necessarily seeking a pre-characterized theorem, and is happy to rewrite `book.tex` if something superior emerges.

The [new research overview][overview] and [supporting progress register][progress] govern this search. Density-one simplicity, a quantitative rate, a record percentage, eventual simplicity, every-zero simplicity, or a useful local restriction are possible outcomes. They are not a required sequence. Neither the resource R, the spectral statistic q, a particular heat scale, a reference field, nor the present manuscript structure is fixed.

Analytic arguments that belong in a coherent selective paper are the overarching goals. Numerical work, symbolic checks, model examples, certificates and additional machinery support a named analytic question. A new representation or a better finite computation is not by itself progress on the desired theorem. Routine analytic exploration remains free to develop; no final theorem statement or numerical target must be chosen before investigating an argument.

This direction supersedes fixed-target readings of [Note 10][targets], including its older density-one “headline target” wording. Its formulas remain useful calibration. [Continuation 09][old-continuation] remains the detailed technical handoff for the current book; its earlier instruction to preserve that manuscript is superseded by the author's explicit willingness to rewrite it. No manuscript was edited during the present discussion.

## Read next

1. [Research overview 02][overview]: objective, flexibility, analytic standards and supporting-work policy.
2. [Progress register 02][progress]: current SIMP-01–03 status and competing analytic approaches.
3. [Note 10][targets]: proved hybrid consumer, checked literature inputs, quantitative thresholds and scope qualifications.
4. [book.tex][book], especially its balance, reference determinant and arithmetic sections; [Review 15][book-review] for their checks and limitations.
5. If pursuing the positive-time route, read [main.tex][main], its [spectral section][spectral], [corrected microscopic reference][reference] and [Research Reset 16][reset]. Use [Continuation 09][old-continuation] for additional technical links rather than repeating all its detail here.

Follow the repository [result index][results] and [avoid index][avoid], particularly [local heat geometry][geometry], [collision controls][controls], [target reformulations][a01], [shared premises][a02], [coupled estimates][a12], and [scoped exclusions][a07]. These standards apply to new proposals as well as inherited ones.

## What this conversation established

The initial request was to assess what useful theorem the existing material could support. The discussion checked the RH-only simplicity benchmark 19/27 and the complementary RH multiplicity moment. It produced a stronger elementary consumer, then organized a flexible analytic program at the author's request.

Write N(T) for zeta zeros with 0<Im rho<=T counted with multiplicity, N_s(T) for simple zeros, and

\[
 M(T)=N(T)-N_s(T),\qquad
 C(T)=\sum_{\rho\ \mathrm{distinct}}m_\rho(m_\rho-1).
\]

Under RH, a complete family of the book's endpoint-covering windows has the resource

\[
 R(T)=\sum_j\left(N_{\psi_j,\mathrm{nr}}(a_j)
                         +F^+_{\psi_j,\mathrm{nr}}\right).
\]

The earlier population, inward flux, outer localization and coverage all belong to this quantity. Note 10 proves

\[
 \boxed{M\le\min\{N,C,3R/2,(3R+C)/4\}.}
\]

The mixed inequality uses

\[
 m\le\tfrac34\,2\lfloor m/2\rfloor+\tfrac14m(m-1)
 \quad(m\ge2),
\]

with equality for doubles and triples. It combines the heat bound's triple worst case with the moment bound's double worst case. This is a checked generic improvement, not a new theta upper estimate or a priority claim.

The published RH moment is C(T)<=(0.3208+o(1))N(T). Consequently a proved asymptotic bound limsup R/N<0.288128395... would beat 19/27; R<=(1/4+o(1))N would yield at least 73.23% simple; R=o(N) would yield density one. These are diagnostics, not the prescribed objective. Note 10 contains the exact threshold, primary references and proof. Its cumulative moment theorem cannot be localized by subtracting two upper bounds to obtain an equally strong dyadic statement.

The planning work created the overview and register, clarified the open theorem direction in Note 10, and added navigation pointers in the investigation and brainstorm guides and the earlier OBF documents. Existing mathematical status and OBF/HDC task identities were preserved. The current work is saved locally; no commit, tag, manuscript snapshot, new numerical campaign or manuscript revision was made in this chat.

## Current mathematical position

| Goal | Actual position |
| --- | --- |
| **SIMP-01: useful canonical arithmetic restriction** | Open. Finite source identities, coupled cancellation and approximation tools are available; useful growing-height size is not acquired. |
| **SIMP-02: strongest simplicity consequence** | Generic consumers available, including the hybrid bound. No new theta simplicity proportion, density theorem, rate or every-zero exclusion. The final theorem remains open. |
| **SIMP-03: selective analytic proof and manuscript** | Open for the new program. The existing book is a finite-scope starting point and may be reorganized or replaced around a superior result. |

The [OBF register][obf] remains the owner of OBF-01–06; [HDC][hdc] retains its technical tasks. SIMP governs the overarching analytic result. Completing every older task is not a prerequisite for a new approach.

The book provides the exact nonreal balance, sharp multiplicity constants, relative determinant H_zz G_z-H_z G_zz, complete-field current limit, finite anchored allowances and the ordered theta head–tail identity. Its source ordering survives positive square reweightings; it does not distinguish theta by itself. Useful canonical bounds for the earlier nonreal population and the complete resource at growing height remain open.

The positive-time route gives M<=4q under the stated complete real-root motion hypotheses, with coefficient/forest machinery and a corrected microscopic arithmetic reference. RH supplies the real-root setting. The missing estimate is small actual q, including reference spectrum and all acquisition/coverage costs; small field error alone does not provide it. Neither approach has been selected as superior. Joint arithmetic moments or a different observable remain welcome.

## How to resume the research

Start an analytic investigation from the best available complete-source information. Identify a promising estimate and how it could restrict multiplicities. Make the provisional question precise enough to reason about, but allow its observable, scale and conclusion to change when the mathematics suggests a better result. Seek actual arithmetic information and preserve coupled cancellations before applying bounds.

For R, estimate the earlier population together with the full relative flux. For q, estimate the actual statistic rather than just its approximation error. For another quantity, prove its useful link to simplicity. Additional hypotheses must be named; an assumed absence of clusters or an unproved pair law cannot be silently included in a result advertised as following from RH alone.

Retain complete populations, exterior forces, approximation errors, carrier and heat-defect terms, localization, overlap and exceptional labels wherever relevant. A two-limit estimate gives only its stated conclusion; a rate needs the appropriate uniformity. A density result permits sparse multiple zeros. An every-zero conclusion through these collision consumers requires control below the cost of one event and complete height coverage.

Use the registered controls on the actual claim. The quadratic and cubic fields saturate the generic collision bounds. Weighted-square controls share source ordering; close normalized endpoint controls obstruct every-zero assertions based on fixed source tolerances. Sparse doubles can coexist with density one. A control must contradict the claimed conclusion before it is required to fail a premise. Failed implementations exclude only their stated information class.

Avoid restarting the completed finite transport/current audit, fixing a percentage or heat-width law as the obligatory target, or opening a numerical scan without a specific analytic purpose. No new confirmation of manuscript flexibility is needed: the author has already authorized reconsidering the book. The next research session should advance the mathematics, with manuscript changes following the result that merits them.

A suitable next-chat prompt is:

> Read this continuation, Overview 02 and Progress 02. Continue analytic research toward the strongest result we can find in support of RH implying simple zeros. Keep the theorem's form, observable, scale and manuscript open. Investigate a promising canonical arithmetic estimate and derive the strongest simplicity consequence it supports; do not assume that density one, a particular percentage, R, q, or the current book structure is mandatory. Use numerical and auxiliary work only to support the analytic argument. Book.tex may be rewritten if a superior result emerges.

## History, verification and saved work

The research checkout is `/Users/ebbaker/Documents/shifted-zeta-positivity`; this program belongs in `papers/investigations-4/12_height_dependent_heat_contours/brainstorm/`. Save derivations in `notes/`, assessments in `reviews/`, and necessary supporting computations in `numerics/`. Follow [LARGE_FILES.md][large]. Keep milestone history concise and create no manuscript snapshot folders. Do not edit synced project sources or generated AGENTS.md files.

This conversation is **Shape a theorem for RH and simple Z**, thread `01a16af3-b685-7cd2-8e74-b2096737475e`, uniquely registered as [brainstorm history 0006][chat]. Preserve its number, filename, title, original creation and first-capture provenance. A genuinely new conversation receives its own identity in this same brainstorm history folder.

The [verification receipt][verification] records the exact checked snapshot: registry identity, stored-byte and canonical-content hashes, a valid linear public-message chain, exact agreement with completed public source messages, unique registration, and the preceding two completed final replies. It also checks that the author's flexible-theorem instruction and permission to rewrite the book are present. Verification concerns transcript integrity and provenance, not mathematical correctness.

Counts and hashes in the receipt are point-in-time values; routine refreshes legitimately change them. This turn's final reply is not present in that pre-final snapshot. The bounded exact-turn worker is arranged as the final tool action to capture the real reply after completion; check its result or refresh at the next turn's start. Trusted native completion capture has not been independently verified here. Use the repository [history workflow][history] at the beginning and end of subsequent replies.

[overview]: ../research-overview/02_ANALYTIC_RH_TO_SIMPLICITY_PROGRAM_20261023.md
[progress]: ../research-progress/02_ANALYTIC_RH_TO_SIMPLICITY_PROGRESS_20261023.md
[targets]: 10_SIMPLICITY_THEOREM_TARGETS_AND_HYBRID_CONSUMER_20261023.md
[old-continuation]: 09_CONTINUATION_BOOK_PROOF_AND_ARITHMETIC_RELATIVE_FLUX_20261023.md
[book]: ../../manuscript/book.tex
[main]: ../../manuscript/main.tex
[spectral]: ../../manuscript/spectral_forest.tex
[book-review]: ../../reviews/15_RELATIVE_FLUX_ANALYTIC_MANUSCRIPT_REVIEW_20261023.md
[reference]: ../../notes/14_MICROSCOPIC_COMPLETE_REFERENCE_AND_HEAT_DEFECT_20261023.md
[reset]: ../../notes/16_RESEARCH_RESET_AND_NEXT_STEPS_20261023.md
[obf]: ../research-progress/01_OPEN_BOUNDARY_FLUX_PROGRESS_20261023.md
[hdc]: ../../research-progress/01_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRESS_20261023.md
[results]: ../../../../../result-summaries/README.md
[geometry]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[large]: ../../../../../LARGE_FILES.md
[history]: ../../../../../tools/CHAT_HISTORY.md
[chat]: ../chat-histories/0006_2026-10-23T22-48-39Z_shape-a-theorem-for-rh-and-simple-z.json
[verification]: ../chat-histories/VERIFICATION_ANALYTIC_RH_TO_SIMPLICITY_20261023.json
