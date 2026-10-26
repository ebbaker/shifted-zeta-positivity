# Finite Fluctuation Hierarchies for the Negative-Time Riemann Heat Flow

26 October 2026. Analytical working manuscript for **Edward Baker**,
with substantial LLM assistance, **gpt-6-astra, recorded effort max**,
recurrence chat0005. Source analytical notes: **gpt-6.1-sol, ultra**.

- [Editable main document](main.tex)
- [Local reading PDF](../../../../../output/pdf/heat-density-recurrence/heat-density-recurrence.pdf)
- [Current integration note and source correspondence](../notes/14_EFFECTIVE_MANUSCRIPT_INTEGRATION_20261026.md)
- [Same-session authoring assessment](../reviews/11_EFFECTIVE_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261026.md)
- [Current build record](BUILD_RECORD_20261026.json)
- [Next analytical continuation](../notes/15_ANALYTIC_STRENGTHENING_CONTINUATION_20261026.md)

The 42-page manuscript joins the canonical heat representation and finite
fluctuation recurrence to an effective evaluation theorem. Sections 1–5
develop the approximation choices, fixed-order and compact-time estimates,
and controlled order growth. Sections 6–7 establish coefficient regularity
and the modular evaluation budget. Sections 8–10 supply finite algorithms,
explicit uniform calibration and all-height onset, then the total accuracy,
bit-work and streamed-space bounds. Section 11 orders the further
analytical questions. Appendices retain the finite error gates, population
bounds, source correspondence, elementary enclosures and Gauss conditioning.

The analytical results of Notes09–11 are now integrated. Note12's finite
component implementation and replay are cited only as supporting evidence,
with clickable links to the notes for the cases, measurements and limits.
Neither numerical samples nor compilation supply a premise of the theorems.

The manuscript retains the certified exact-input class, descriptor
separation, both arms, every arithmetic mode, matched RS coefficients and
bounded real completion integral. Its explicit height is sufficient and
very conservative. It proves a terminating analytical construction under
the named source inputs; complete evaluator software and independent
specialist validation remain open. The [sole progress register](../research-progress/01_RECURRENCE_RESEARCH_PROGRESS_20261026.md)
owns status, and broad R05 remains Partial.

## Build and provenance

From the repository root:

    mkdir -p output/pdf/heat-density-recurrence
    latexmk -pdf -interaction=nonstopmode -halt-on-error -cd \
      -jobname=heat-density-recurrence \
      -outdir=../../../../../output/pdf/heat-density-recurrence \
      papers/investigations-5/01_heat_density_asymptotics/recurrence/manuscript/main.tex

Open this folder or main.tex in the desktop LaTeX editor for source editing
and a live preview. The bibliography's local supporting-note links resolve
from the reading PDF's documented output folder.

Generated PDFs and build intermediates belong in the ignored repository
output tree or outside the repository, under [LARGE_FILES.md](../../../../../LARGE_FILES.md).
Keep source and small production records here. Use [DRAFT_HISTORY.md](../DRAFT_HISTORY.md)
for milestones; create no new snapshot folders. The original 27-page
integration is described in [Note07](../notes/07_MANUSCRIPT_INTEGRATION_20261026.md)
and [Review06](../reviews/06_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261026.md).
The current [input manifest](../notes/14_MANUSCRIPT_INPUTS_20261026.json)
identifies the preceding source and build record. Earlier statements that
Notes09–11 awaited integration describe the historical stages.
