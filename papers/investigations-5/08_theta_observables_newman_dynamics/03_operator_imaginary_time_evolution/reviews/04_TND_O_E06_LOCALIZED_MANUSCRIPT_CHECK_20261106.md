# E06 localized manuscript: analytical and production check

6 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance from **OpenAI Codex**. The exact current model
identifier and reasoning effort were not exposed in the available session
metadata; neither is inferred from earlier sessions.

## Disposition and scope

**No blocking error was identified in the new derivations inspected.**
The 40-page revision is complete at manuscript-production and proof-author
checking scope. This is the same assistant that prepared the revision;
it is not the separately proposed E05 assessment, a cross-model review,
specialist refereeing or formal verification. The canonical transport
and arithmetic estimates remain hypotheses. No RH or Newman upper-bound
conclusion is claimed.

The actual inputs are recorded in
[Inputs15](../research-progress/handoffs/15_TND_O_E06_LOCALIZED_MANUSCRIPT_INPUTS_20261106.json).
[Note15](../notes/15_TND_O_E06_LOCALIZED_MANUSCRIPT_SYNTHESIS_20261106.md)
describes the synthesis; [source-use09](../references/09_TND_O_E06_LOCALIZED_MANUSCRIPT_SOURCE_USE_20261106.md)
records the selected primary passages inspected. The earlier operator
assessment, its Q1/Q2 qualifications, and historical proof packets retain
their original status.

## Analytical checks

| Result | Check and qualification |
| --- | --- |
| Finite-cluster dynamics and transverse balance, Section 12.1 | Differentiated a simple zero under H_lambda=-H_zz, expanded H_zz/H_z at P=0, and paired ordered transverse terms. The isolated-cluster exterior factor is retained; no unjustified infinite zero sum is used. |
| Pair transport, Theorem 12.2 | Reversed time, cancelled the mutual force in the midpoint, integrated g_z along the entire vertical segment, and solved u_s+4k(s)u=2. The bounds have the correct K=0 limit 2s and correct factor 1/2 in the zeta ordinate. Isolation, nonvanishing and bounds are needed over the full path. |
| Collision jet, equation (12.11) | Substitution into the scalar equation gives u=2s-4 kappa s^2+O(s^3). The midpoint coefficient -2 ell differs from the critical-point coefficient -3 ell. Analytic symmetric coordinates justify the expansions. |
| Strip and real-neighbor comparisons, Section 12.3 | Checked the imported full dynamics/strip theorem and retained maximality, simple labeling and persistent neighbors. The imaginary force converges absolutely. Integrating the two lower differential inequalities yields the stated time budget; the open final strip makes it strict. No canonical tube or new numerical Newman bound is obtained. |
| Weighted transverse balance, Proposition 12.4 | Product differentiation and symmetrization retain the unequal-weight term, moving-window derivative and exterior force with the correct reversed-time signs. Nonnegative weights alone do not make the pair term nonnegative. |
| Coincidence atom, Proposition 14.1 | The finite sum permits a termwise limit. Distinct ordered copies at one ordinate contribute m_t(m_t-1), with exactly two selected orders. Raw moments, density normalization, center dilution and the extra simplicity requirement are separated. |
| Sine reference, Proposition 14.2 | Computed the finite-window expectation from the sine pair density. The autocorrelation translation identity bounds the correction by epsilon^5/q. This is a reference-process calculation and is not asserted for zeta. |
| Weighted Gram identity, Proposition 14.3 | Reflection preserves height weights; the exponential-integral kernel gives the finite Hilbert norm. The selected pair contributes 2w^2[1+W(d)cosh(ad)]. Reverse triangle inequality requires the background norm; positivity alone does not give E>=P. |
| Conditional localized comparison, Corollary 14.4 | Monotonicity supplies the pair lower bound; the background allowance gives the surviving amplitude, and integration over the plateau pays its length/T. The theorem neither supplies the upper estimate nor manufactures exceptions at arbitrarily large height. |
| Published local-statistics limits | Inspected Maples–Rodgers' moment parameters and Rodgers' RH hypothesis in the primary PDFs. Fixed moments and center averages can permit one spike. No statement about the impossibility of every localized strategy is inferred. |

The polynomial heat control attains the K=0 transport bounds. The existing
smooth-source collision and the other controls remain separated by their
failed canonical premises. None is asserted to satisfy the proposed
unproved arithmetic upper inequalities. No machine-symbolic derivation,
interval certification, fresh zero computation or numerical campaign was
run for this revision.

## Production verification

- `bash manuscript/build.sh` completed successfully using latexmk 4.79,
  pdfTeX 1.40.25 (TeX Live 2023) and BibTeX/plainurl.
- The final log has zero warnings, unresolved references, missing-character
  reports or overfull/underfull boxes. The bibliography contains 20 entries.
- The PDF has 40 pages. All pages were rendered at 85 dpi with Ghostscript
  10.00.0 and visually inspected in five contact sheets; pages 26–28,
  33–35 and 38 were additionally inspected individually. No clipping,
  accidental blank pages or layout collisions were identified.
- Ghostscript text extraction contains zero replacement characters. This
  is a limited text-integrity check, not a mathematical validation of PDF
  extraction or every glyph.
- Equations (5.4) and (5.5) keep their original labels. The new principal
  statements are Theorem 12.2, Propositions 12.3–12.4 and 14.1–14.3, and
  Corollary 14.4. Outstanding analytical tasks are Section 16.
- Historical notes/reviews, bound packets, brainstorm Notes04–05,
  canonical bibliography records and chat histories are unchanged by this
  revision. Generated PDFs and build files remain in ignored output/pdf.

The build record and return packet bind the actual source and PDF hashes.
The original checkout could not be edited in this session; the working
revision and patch use its current files, including its pre-existing
uncommitted changes, rather than assuming a clean HEAD. The patch excludes
earlier uncommitted changes and history files. Applying it to the original
checkout is a separate filesystem step, not something completed here.

## Remaining work

The principal analytical needs are a complete canonical tube or barrier,
an exception-sensitive arithmetic upper comparison, useful background and
center-width estimates for the analytic candidate, and event/finite-height
coverage for the intended global conclusion. A separate assessment should
bind the revised 40-page inputs rather than the earlier 32-page packet.
