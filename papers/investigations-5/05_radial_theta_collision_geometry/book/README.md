# The theta transform in three dimensions

28 October 2026. Drafted for Edward Baker with substantial LLM assistance,
**gpt-6-astra (Codex), recorded effort max**, chat0013.

The [manuscript](main.tex) opens with the Gaussian coefficient derivation
of the three-dimensional radial Laplacian from
[Note01](../notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md),
the earlier primitive identity, and the resulting logarithmic-radius
observation. It then sets up the density, spatial variables, fixed
observation kernel, restricted inverse, and meaning of a collision under
the transform. The kernel is independent of the auxiliary parameter; the
density is independent of the spectral argument. No auxiliary evolution
is selected.

The distinction between preserving a density, preserving every spectral
observation, and preserving total mass appears in Section 6. For this
logarithmic-radius kernel, preserving every observation fixes the
spherical average at each radius, while allowing nonradial densities.

The local [nine-page reading copy](../../../../output/pdf/radial-theta-collision-geometry-book/theta-transform.pdf)
is generated and ignored by Git. Open this folder in the built-in LaTeX
editor to edit the source and preview it. A terminal build, from this
folder, is:

    latexmk -pdf -interaction=nonstopmode -halt-on-error \
      -outdir=../../../../output/pdf/radial-theta-collision-geometry-book main.tex

This command produces main.pdf in the shared output folder; the delivered
reading copy is named theta-transform.pdf. Working PDFs do not belong in
this source folder.

[Research note](../brainstorm/06_BOOK_TRANSFORM_SETUP_20261028.md),
[same-assistant assessment](../reviews/20_BOOK_TRANSFORM_SETUP_ASSESSMENT_20261028.md),
and [build record](../numerics/18_BOOK_TRANSFORM_SETUP_BUILD_RECORD_20261028.json)
record the choices and verification. The existing conservative-flow
manuscript remains a separate research document.

Laplacian motivation revision: 28 October 2026, drafted for Edward Baker
with substantial LLM assistance, **gpt-6-astra (Codex), recorded effort
xhigh**, chat0014. The exponential kernel remains a working choice.
[Revision build record](../numerics/19_BOOK_LAPLACIAN_MOTIVATION_BUILD_RECORD_20261028.json)
records the current nine-page build; record18 describes the earlier setup.
