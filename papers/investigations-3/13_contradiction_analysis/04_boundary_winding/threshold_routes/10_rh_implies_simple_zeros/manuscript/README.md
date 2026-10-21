# Analytic consolidation draft

21 October 2026. Drafted for Edward Baker with substantial LLM assistance.
Original derivations: **gpt-6-astra, actual effort ultra**. Integration of
Notes 17–18: **gpt-6-astra, actual effort max**, verified from recorded
session metadata.

[Read the eleven-page PDF](main.pdf) or [edit the canonical LaTeX source](main.tex).
This brief emphasizes the analytic estimates and the missing arithmetic
bound. Section 4 also records the unconditional failure of the unchanged
global heat norm and its sharp logarithmic weight threshold. Sections 5–7
now preserve the normalized complete heat limit, sharp arithmetic repair
over fixed filtered-Gevrey families, and exact-completion obstruction from
Notes 17–18, including the explicit double-profile example and contour
prescriptions. Section 8 compares the shared methods and additional hypotheses
of the originating BW09 investigation. Neither RH nor RH implies
simplicity is proved here. The results have same-model internal review,
with no external specialist validation or novelty claim.

Detailed proofs remain in [Note 15](../notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md),
[Note 16](../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md),
[Note 17](../notes/17_NORMALIZED_HEAT_GLOBAL_LIMIT_AND_ARITHMETIC_COSTS_20261020.md),
and [Note 18](../notes/18_ARITHMETIC_HEAT_TRANSFER_AND_EXACT_COMPLETION_20261021.md).
[Review 16](../reviews/16_GEVREY_GLOBAL_APPROXIMATION_REVIEW_20261020.md)
records the analytic and consolidation checks. The
[progress register](../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md)
retains the open gates, and [draft history](../DRAFT_HISTORY.md) indexes
committed milestones without snapshot folders.

The [integration and discussion note](../brainstorm/03_HEAT_ROOT_MOTION_AND_HIGHER_DIMENSIONAL_CONTOURS_20261021.md)
records this update and the author's questions about moving root caps and
quaternionic/octonionic boundaries. Those exploratory comparisons are
kept separate from the consolidated approximation theorems.

The PDF was built with pdfLaTeX (two clean final passes), then all eleven pages were
rendered and visually checked. Auxiliary build files stay outside the
repository; a [small build receipt](../numerics/MANUSCRIPT_NOTES_17_18_BUILD_20261021.json)
records hashes and scope. Numerical and bounded Lean checks are cited in the brief;
they do not verify the analytic tail theorem.
