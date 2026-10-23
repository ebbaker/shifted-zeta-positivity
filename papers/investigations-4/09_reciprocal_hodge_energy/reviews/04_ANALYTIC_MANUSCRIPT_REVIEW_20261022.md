# Analytic manuscript review

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance; actual recorded model **gpt-6.1-sol (Codex),
reasoning effort ultra**. A separate agent of the same model reviewed the
assembled text after section drafting. This is internal LLM review, not
independent specialist, human, or formal validation.

**Disposition: analytic draft ready for author review; no mathematical
blocker identified in this internal audit.** The [working manuscript](../manuscript/reciprocal_hodge_energy/main.tex)
and [PDF](../manuscript/reciprocal_hodge_energy/reciprocal_hodge_energy.pdf)
consolidate Notes 01–04 with complete derivations and explicit goals/status.
No endpoint-uniform theta estimate, RH theorem, or simplicity exclusion is
asserted. This review does not change the earlier numerical certificate's
validation status.

## Scope and checks

- Recomputed the two-sheet energy normalization, local branch regularity,
  multiplicity integrability, cylinder coordinates on a shifted disk, and
  the complete direct-coordinate formula.
- Checked coherent primitive constants, paired-cut orientations, the real
  Green identity, both physical boundary contributions, and the quadratic
  cut/physical logarithmic allocations. The compact bilinear identity is
  explicitly separated from the bordered annulus.
- Verified the arcsine core mean, zero-period primitive, odd quotient's
  extension at both branches, full mixed term, and the constants for the
  energy, relative period, and both boundary remainders.
- Reconstructed the complete-source derivative majorant, both Rouché
  counts, real endpoint signs, critical value, root splitting and midpoint
  estimates. Checked the simplex deflation formula and its derivative
  moments, nu/L/K/J, the coarse upper bound, the explicit strict-improvement
  window, and the final ordinary-double logarithmic coefficient.
- Checked every coefficient in the Cauchy derivative tails, uniform
  divided-difference error, primitive/period product allowances, and the
  disjoint omitted-mode/retained-ray tail ledger. Derived the normalization
  appendix independently from Gaussian Poisson summation, Mellin splitting,
  and integration by parts, including f'(0)=-1/2 and xi/8.
- Checked numerical quotations against the existing actual-fiber record;
  no numerical replay was performed in this manuscript round. The separate
  replay remains documented in [Review 03](03_ACTUAL_THETA_FIBER_COMPARISON_REVIEW_20261022.md).
  The numerical discussion occupies one brief supporting section.
- Verified the cited classical normalization against Rodgers–Tao's primary
  paper, the compact relation against the official Grava notes, and Arb
  metadata against the author's arXiv record. No novelty claim is made.

## Correction incorporated

An earlier sentence in the deflation discussion could be read as saying
that the divided difference vanishes at the exact roots. It now correctly
says that the **complete function** vanishes at those roots and that its
divided difference is V. No formula depended on the ambiguous wording.
No further mathematical correction was identified by the final reviewer.

## Artifact and status checks

The delivered PDF has **25 pages**, compiles with both local pdfLaTeX and
the desktop editor, and has no final-log warnings, overfull/underfull boxes,
or unresolved references. All rendered pages were inspected, with dense
equation pages also inspected at full image size. The source/PDF identity
and byte sizes are in [BUILD_RECORD.json](../manuscript/reciprocal_hodge_energy/BUILD_RECORD.json);
the PDF is below the repository's approximate 1 MB limit. Only stable
working sources and the small PDF are saved; no snapshot folder is created.

The [result index](../../../../result-summaries/README.md) and
[avoid index](../../../../avoid/README.md) remain the status gates,
especially [local heat-flow cluster 13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[scoped conclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[normalization](../../../../avoid/08_normalization_and_constant_slips.md),
and [complete coupled estimates](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
The draft quotes the equal-information limitation and keeps the endpoint,
height, multiplicity, and nonreal-zero coverage obligations separate.
