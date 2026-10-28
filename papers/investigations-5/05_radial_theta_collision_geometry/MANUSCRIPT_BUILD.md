# Working manuscript and reading PDF

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

The single active manuscript is [Radial Darboux Deformations and the Theta Observation](radial_deformations_and_zero_dynamics.tex), in this investigation's base folder. It was drafted for Edward Baker and includes an acknowledgment of LLM assistance and the internal verification scope. The initial version has nine pages. See [the assessment](reviews/11_INITIAL_DEFORMATION_MANUSCRIPT_AND_PROGRAM_ASSESSMENT_20261027.md) and [build record](numerics/12_INITIAL_DEFORMATION_MANUSCRIPT_BUILD_RECORD_20261027.json).

The local [reading PDF](../../../output/pdf/radial-theta-collision-geometry/radial_deformations_and_zero_dynamics.pdf) is generated, ignored output. It is not a tracked manuscript snapshot. Its absence in a fresh clone is expected; regenerate it from the source. Keep future revisions in the same source file and record notable milestones in [DRAFT_HISTORY.md](DRAFT_HISTORY.md).

Run from the repository root with a TeX installation providing latexmk, pdfLaTeX, geometry, lmodern, amsmath, amsthm, mathtools, microtype, xcolor and hyperref:

```sh
mkdir -p output/pdf/radial-theta-collision-geometry
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=output/pdf/radial-theta-collision-geometry \
  papers/investigations-5/05_radial_theta_collision_geometry/radial_deformations_and_zero_dynamics.tex
```

The initial build used TeX Live 2023 and latexmk 4.79. Auxiliary files also belong in the output folder. No external image, bibliography download or shell escape is needed. After content changes, review the compilation diagnostics and render the complete PDF for layout inspection; a successful build alone is not mathematical verification. The manuscript can also be opened in the app's TeX editor for source editing and preview.

The current [overview](research-overview/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_OVERVIEW_20261027.md), [proposal](research-proposal/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_PROPOSAL_20261027.md) and [continuation note](notes/19_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_CONTINUATION_20261027.md) govern the next research session.
