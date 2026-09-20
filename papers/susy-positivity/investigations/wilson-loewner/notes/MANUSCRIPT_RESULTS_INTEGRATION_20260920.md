# Version 0.4: fixed-window response and localization results

Date: 20 September 2026.  
Prepared for: Edward Baker.  
Model: OpenAI GPT-6 (Codex).  
Reasoning effort: not exposed to the assistant in this session; not inferred.  
Status: manuscript integration and reproducibility record; no independent mathematical review.

## Placement

The matched version 0.4 pair incorporates the two research notes:

- [Fixed-window Wilson response](FIXED_WINDOW_WILSON_RESPONSE_OBSTRUCTION_20260920.md).
- [Localization and the pole cancellation](LOCALIZATION_AND_THE_POLE_CANCELLATION_20260920.md).

The new manuscript Section 5, **A fixed-window test and the localization
question**, follows the physical transfer hypothesis and precedes the
spectral constraints. It explains the complete local/pole matching
condition, the tested response and its failure, and the localization
proposal. Each part cites the corresponding supplementary section.

Supplementary **S10** gives the complete prime-free target for
\(0<L<\log 2\), the hard-delay-cutoff contact term, the finite-shift
factorization, the regulated Gaussian Wilson readout, its nonzero first
variation, and the bounded-derivative and compactness obstructions.
Supplementary **S11** gives the localization context, the exact auxiliary
boson--fermion product, its finite-product proof and the mode-counting test.
Diagnostics and provenance now occupy S12 and S13.

The introduction, research agenda, statement ledger, provenance,
bibliography and package reading map were updated consistently. Both
documents retain the author designation “Drafted for Edward Baker” and
explicit LLM-assistance disclosures. Baker's localization suggestion is
credited in the supplementary discussion.

## Scope preserved

The obstruction concerns the defined regular Gaussian readout and the
specified bounded-derivative class. It does not rule out every Wilson
construction or a controlled singular limit of regulated responses.
The full local term and both poles remain in the arithmetic comparison.

The auxiliary product reproduces the full prime-free gamma/pole factor,
but its modes and normalization are prescribed from the arithmetic
target. No physical localization complex or supersymmetric action is
derived. The literature discussion distinguishes Pestun's equivariant
pairing, Baker's lower-dimensional defect proposal, and Wang's related
endpoint-bilocal framework and unevaluated normal determinant.

Cumulative positive-norm storage remains an independent requirement.
The square-root shift scale for its amplitude, the output defect needed
for spatial Schur gluing, and the later simultaneous depth--shift
continuation remain visible. Neither document assumes an arithmetic
Loewner driver exists.

## Completed checks and preservation

- Both TeX entry points compiled successfully: 18 manuscript pages and
  33 supplementary pages.
- All 51 pages were rendered and visually inspected in full-page contact
  sheets, with enlarged inspection of the newly added sections.
  Equations, contents entries, tables, page breaks and cross-references
  were checked. Final logs contain no unresolved references, multiply
  defined labels, overfull boxes or underfull boxes.
- All four standard-library diagnostic programs were replayed:
  102 smooth-variation, 99 endpoint, 67 reflected-junction and
  31 fixed-window cases, for **299 passing cases**. The regenerated
  records are byte-identical to the previous results; case identities
  and thresholds were unchanged. These finite checks do not certify the
  analytical proofs, quantum positivity or the realization hypothesis.
- The portable validator now includes the fourth diagnostic program.
  The current pair and all four historical snapshots passed identity
  verification. The new snapshot also passed its own portable check.
- [Version 0.4](../drafts/2026-09-20-v04/README.md) preserves both PDFs,
  their complete local TeX inputs, build instructions, diagnostic
  programs and records, source provenance and the portable validator.
  Versions 0.1--0.3 were preserved unchanged.

The delivered PDFs are byte-identical to the visually reviewed builds.
[BUILD_RECORD.json](../BUILD_RECORD.json) records their identities and
the visual-review scope. [MANUSCRIPT_SOURCES.json](../MANUSCRIPT_SOURCES.json)
adds the two research inputs and the focused primary-source checks while
preserving earlier provenance. [PACKAGE_RECORD.json](../PACKAGE_RECORD.json)
records the final live inventory after archival and index updates.

The checks establish reproducibility and file identity, not an
independent mathematical review.
