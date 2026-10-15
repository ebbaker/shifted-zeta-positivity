# Recurrence manuscript integration review

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating and reviewing model **gpt-6-astra**, reasoning effort **ultra**. This is internal LLM review, not external refereeing or formal verification.

## Integrated scope

The [manuscript](../manuscript/theta_manifold_geometry.tex) now develops the exponential-average criterion, normalized coefficient recurrence, independent-source product and endpoint strips, quantitative recurrence stability, absorption-current approximation, and signed boundary geometry. Its [43-page reading copy](../../../../../output/pdf/theta_manifold_geometry.pdf) includes the proofs, revised abstract, logical-status list, outlook, bibliography and LLM acknowledgment.

The new negative findings are brief, scoped remarks with citations to their detailed notes. The manuscript does not promote the normalization-cancellation failure into a prohibition on all currents; it does not treat generic reflected-source controls as counterexamples within the polynomial-growth theta square class; and it does not infer theta positivity from recurrence stability or a quotient description. The earlier detailed three-square control remains unchanged.

## Separate analytic review

Different agents cross-reviewed the combined manuscript additions. The audits checked:

- The averaged collision sign on both branches, the complete-start Gaussian tail, and the order of choices in the mixed-error theorem: length, cutoff, then approach to the event. A prescribed unbounded cutoff subsequence suffices. Each fixed-index coefficient is locally bounded through the event; no common growth rate across cutoffs is required.
- Projected elliptic recurrence, removal of the affine slope by the complete primitive endpoint, independent source parameters in the mixed addition formula, and the endpoint-only strip geometry.
- The physical mode constant \(C_j(T)=\pi M_j(T)/(4\pi-1)\), the normalization \(\beta_n=8H_n(0,i)\), weighted convergence under \(\sum\beta_n|a_n|<\infty\), the defect identity and the signs of its two lower traces.
- The sharp finite-hierarchy weighted supremum, an actual \(H_a(0,0)\) deviation of order \(1/N\), the Gaussian improvement after fixing the slope, and the finite-depth current's \(\sqrt E\)-preserving transfer.
- The rapidly decreasing sequence-space cokernel, homogeneous finite-dimensional quotient norm, coefficient growth at degeneration, and the implication from a signed trace estimate to the mixed-error chord bound.

Review clarifications were incorporated: \(r\ge1\) in the averaged collision law; the older all-integer-cutoff condition is scoped to its particular theorem; the outlook permits certified subsequences; physical divisions require \(E>0\); local boundedness is explicit; and separate-sector limitations are restricted to the analyzed constructions. “Finite-depth current” avoids claiming finite support of the whole current. The coefficient of \(\sqrt E\), rather than the entire physical error, is identified in the shrinking-length comparison.

Two accidental equation-reference substitutions in the source recurrence note were corrected: `p_n'(B.0)` and `G_beta(B.0)` now evaluate at `0`. The formulas and proofs in the manuscript use the correct values. Earlier manifests retain historical note and manuscript identities; the current integration manifest binds the corrected note.

## Exact replay and compilation

| Replayed checker | Exact rational assertions |
| --- | ---: |
| Exponential average | 1,620 |
| Elliptic coefficient core | 481 |
| Coupled theta product | 1,739 |
| Parity strip cutoff | 1,539 |
| Adjoint recurrence boundary | 6,892 |
| Total overlapping assertions | 12,271 |

All five executions passed. The recurrence checker had also been independently replayed in the preceding research turn. Rational surrogate tests and finite heat-polynomial controls are distinct from the general analytic proofs. Previously validated non-theta collision receipts remain the evidence for those cited controls; their expensive interval calculations were not rerun for this prose integration.

The final source compiled successfully with the desktop LaTeX compiler. The exported reading copy was rebuilt with pdfTeX 1.40.25 and latexmk 4.79. Its final log has no warnings, unresolved references, or overfull/underfull boxes. Static checks found **202 unique labels**, **28 bibliography entries**, no missing citations or references, and no duplicate labels. All local research links resolve after installation.

Every page was rendered at 100 dpi and inspected individually: pages 1–14, 15–28, and 29–43 were assigned to separate reviewers; the coordinator also inspected representative new pages. A split word in the section 11 heading was repaired by shortening the heading. Final changed pages 2 and 36–43 were inspected again; unchanged pages were verified by identical raster hashes. No clipping, overlap, missing glyphs, unreadable formulas or unresolved reference marks remain.

## Build and history provenance

The [build record](../manuscript/BUILD_RECORD.json) and [integration manifest](../numerics/RECURRENCE_MANUSCRIPT_INTEGRATION_CHECKS_20261015.json) identify the final source, export, note, review, scripts and replay outputs. The previous source/PDF identities remain under the prior milestone entry. No manuscript snapshot, commit or tag was created; [draft history](../DRAFT_HISTORY.md) records this working-tree integration. Unrelated working-tree changes were preserved.

The [history verification](../numerics/RECURRENCE_MANUSCRIPT_CHAT_HISTORY_VERIFICATION_20261015.json) checks formal replay identity 20, original creation and first-capture provenance, stored and canonical hashes, exact public-source correspondence, and capture of both preceding final answers. The current unsent final is outside that audit and receives the usual bounded exact-turn follow-up. The [next-chat handoff](../notes/00_research_coordination/09_MANUSCRIPT_RECURRENCE_INTEGRATION_AND_NEXT_CHAT_20261015.md) points to the integrated results and the remaining signed trace experiment.

The manuscript still leaves the complete-theta signed endpoint estimate and full event coverage open. No new global theta sign domain or RH conclusion is asserted.
