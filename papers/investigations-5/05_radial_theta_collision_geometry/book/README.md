# The theta transform in three dimensions

28 October 2026. Drafted for Edward Baker with substantial LLM assistance,
**gpt-6-astra (Codex), recorded effort xhigh**, chat0015.

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
