# The theta transform in three dimensions

28 October 2026. Drafted for Edward Baker with substantial LLM assistance,
**gpt-6-astra (Codex), recorded effort xhigh**, chat0015.

**Research routing, 29 October 2026:** the renewed conservative-flow estimate work belongs to [Overview05](../research-overview/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_OVERVIEW_20261029.md) and the sole current [Progress05](../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md). The main research text is [Conservative Theta Flows and Collision Amplification](../radial_deformations_and_zero_dynamics.tex); this book remains a background companion. [Note35](../notes/35_CLASSICAL_THETA_MELLIN_ATTRIBUTION_20261028.md) identifies its scalar Mellin formula as classical. The separate E06 task permits a bounded attribution/navigation cleanup; the book source has not been rewritten in this planning update. Prepared for Edward Baker with LLM assistance, gpt-6-astra / max, Investigation06 chat0004.

The [current book draft](main.tex) follows the restored
[rewrite plan](changes/02_REWRITE_20261028.md). Section 1 starts with xi
and the de Bruijn-Newman deformation, then derives the smooth theta
potential V, the rescaled generator G, and the cylinder equations using
the original H normalization. Sections 2–3 treat Mellin symmetry, entire
continuation, spherical means, inversion, and spectral cancellation.

Section 4 separately presents the normalized three-dimensional notation.
Its [alternative planning note](changes/03_THREE_DIMENSIONAL_NOTATION_ALTERNATIVE_20261028.md)
is preserved unchanged from before the reversion. Both approaches are
therefore available without replacing the main notation. Section 5 gives
the cylinder heat, transported Newman, and exact linear-combination
comparisons; Section 6 retains the control scope and open flow choice.

The [11-page reading copy](../../../../output/pdf/radial-theta-collision-geometry-book/theta-transform.pdf)
is generated and ignored by Git. Open this folder in the built-in LaTeX
editor for the editable source and live preview. To build from this folder:

    latexmk -pdf -interaction=nonstopmode -halt-on-error \
      -outdir=../../../../output/pdf/radial-theta-collision-geometry-book main.tex

That command produces main.pdf; the delivered reading copy is named
theta-transform.pdf. Working PDFs remain outside the source folder.

[Assessment21](../reviews/21_BOOK_REWRITE_ASSESSMENT_20261028.md) and
[build record20](../numerics/20_BOOK_REWRITE_BUILD_RECORD_20261028.json)
record the analytical and all-page layout checks. The draft compiled
successfully locally and in the desktop editor. No new collision
exclusion or independent specialist review is claimed.

Earlier setup and motivation remain documented in
[Brainstorm06](../brainstorm/06_BOOK_TRANSFORM_SETUP_20261028.md),
[Assessment20](../reviews/20_BOOK_TRANSFORM_SETUP_ASSESSMENT_20261028.md),
and build records [18](../numerics/18_BOOK_TRANSFORM_SETUP_BUILD_RECORD_20261028.json)
and [19](../numerics/19_BOOK_LAPLACIAN_MOTIVATION_BUILD_RECORD_20261028.json).
The separate conservative-flow manuscript remains in the investigation
root. No manuscript snapshot folder was created.


The [28 October continuation](../brainstorm/10_BOOK_STATE_AND_FLOW_FIRST_CONTINUATION_20261028.md)
records the decision to retain this draft and let the actual flow equations
guide later choices of geometry, field, and preservation requirement.
New alternatives should be developed in separate numbered notes.
28 October 2026; gpt-6-astra / xhigh, chat0015.
