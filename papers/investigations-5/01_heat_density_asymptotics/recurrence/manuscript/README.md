# Finite Fluctuation Hierarchies for the Negative-Time Riemann Heat Flow

26 October 2026. Analytical working manuscript for **Edward Baker**,
with substantial LLM assistance. Original integration: **gpt-6-astra, max**,
chat0005. Linear-onset strengthening/integration: **gpt-6.1-sol, actual
effort ultra**, chat0006. Source notes retain their original attribution.

- [Editable main document](main.tex)
- [Local reading PDF](../../../../../output/pdf/heat-density-recurrence/heat-density-recurrence.pdf)
- [Current integration note and source correspondence](../notes/14_EFFECTIVE_MANUSCRIPT_INTEGRATION_20261026.md)
- [Same-session authoring assessment](../reviews/13_UNIFORM_RS_BOUND_ASSESSMENT_20261026.md)
- [Current B02 r2 build record](BUILD_RECORD_20261026_B02_R2.json)
- [Preceding Book-companion build record](BUILD_RECORD_20261026_BOOK_COMPANION.json)
- [Preceding analytical integration record](BUILD_RECORD_AN07_20261026.json)
- [Next analytical continuation](../notes/19_ANALYTICAL_CONTINUATION_AFTER_RS_BOUNDS_20261026.md)

This is the negative-time technical companion to the [central Book](../../book/main.tex),
which gives the common notation and cross-region proof map. Detailed frozen
hierarchy, matched Riemann–Siegel, onset, provider and cost proofs remain
here. The [ansatz companion](../../ansatz/manuscript/main.tex) owns the
positive fixed-order hierarchy and compact positive bridge; its common
finite partition algebra does not transfer domains or physical-consumer
bounds. [Note63](../../notes/63_BOOK_SYNTHESIS_AND_COMPANION_REVISION_PLAN_20261026.md)
sets the production contract. Companion reconciliation: **gpt-6.1-sol,
actual effort ultra**, 26 October 2026.

The manuscript joins the canonical heat representation and finite
fluctuation recurrence to an effective evaluation theorem. Sections 1–5
develop the approximation choices, fixed-order and compact-time estimates,
and controlled order growth. Sections 6–7 establish coefficient regularity
and the modular evaluation budget. The following sections supply finite algorithms, explicit uniform
calibration and all-height onset, then total accuracy, bit work and
streamed-space bounds. The dedicated moving-endpoint section integrates
the complete expanded-domain proof before the outstanding questions. Appendices retain the finite error gates, population
bounds, source correspondence, elementary enclosures and Gauss conditioning.

The analytical results of Notes09–11,16,18 and 20 are now integrated. The
new linear-onset theorem proves L>=64nu, nu=ceil(r+b+2)+1, improving
the retained 2^22nu^4 fallback by 2^16nu³ without changing accuracy,
inputs or any retained component. Note12's finite
component implementation and replay are cited only as supporting evidence,
with clickable links to the notes for the cases, measurements and limits.
Neither numerical samples nor compilation supply a premise of the theorems.

The manuscript retains the certified exact-input class, descriptor
separation, both arms, every arithmetic mode, matched RS coefficients and
bounded real completion integral. Its explicit height is sufficient and
very conservative. It proves a terminating analytical construction under
the named source inputs; complete evaluator software and independent
specialist validation remain open. The [sole progress register](../research-progress/01_RECURRENCE_RESEARCH_PROGRESS_20261026.md)
owns status, and broad R05 remains Partial. Its subsequent AN08 return
is Complete/CLOSED: [Note20](../notes/20_MOVING_LOWER_ENDPOINT_20261026.md)/
[Review14](../reviews/14_MOVING_ENDPOINT_ASSESSMENT_20261026.md) prove
[1/L,2] at sufficient L>=1024nu² with the same strong target. The full proof now has its own manuscript section,
[14_moving_endpoint.tex](sections/14_moving_endpoint.tex), with durable
label `thm:moving-endpoint-delivery` and distinct channel norm
`def:moving-channel-norm`. It retains complete kernel, population, tail,
normalization and delivered-error ledgers, strict rational time witnesses,
a separately paid literal endpoint tag, O(L³) sufficient outer nodes and
leading delivered precision 3L²/(8 log 2). Provider-internal and witness
search costs remain separate. The [1,2] proof and sharper 64nu onset remain
in place; strong negative precision through zero, physical transfer and
complete software certification remain open. B02 r2 integration:
**gpt-6.1-sol, actual effort ultra**, 26 October 2026.

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

The integrated Note18 theorem improves B_F and every D_k by csch(pi)<1/10
on identical domains. A separate enlarged-contour proof gives B_c/16 and
permits eleven fewer nodes per edge at identical jet tolerance. The
finite delivery section retains all node/weight, pi, rounding and transfer
terms. Old bounds and provider remain fallbacks; these are analytical
allowance/count improvements, not a measured whole-evaluator speedup.
Uniform-bound integration: gpt-6.1-sol, actual effort ultra, chat0006.
