# Imaginary-Time Realization and Collision Geometry of the Newman Family

6 November 2026. Drafted for **Edward Baker** with substantial LLM assistance,
actual **gpt-6-astra / max**, branch chat0004. TND-O-E04/B03 analytical
revision of the single evolving manuscript; initial E03 milestone remains
in the draft history. No snapshot folder is created.

The [editable source](main.tex) and
[32-page reading PDF](../../../../../output/pdf/08_theta_observables_newman_dynamics/operator_imaginary_time_evolution/operator_newman_collision_geometry.pdf)
develop the supplied theta source, operator realization, local event,
source-dependent coefficients and nonreal-zero statistics in one sequence.
The PDF lives only in ignored root output/pdf.

| Sections | Development |
| --- | --- |
| 1–4 | Normalization, complete theta bounds, entire heat orbit, raw Green strip, full cylinder operator/readout and regular global energy |
| 5 | Collision geometry, preserved equations(5.4)–(5.5), critical-curve/exterior coefficient dictionary and conditional real-zero benchmark |
| 6–7 | Complete signed theta moments, half-line primitive and endpoint, contour/error interface, exact moving-lobe balances and scales |
| 8–10 | Interference, source response, finite higher multiplicity, exact smooth collision control and analytical negative-curvature sign |
| 11 | Rodgers–Tao exterior interactions and renormalization, with the collision pole retained |
| 12 | Unconditional complex-difference statistics, conditional ordinate PCC, finite-exception stability, marked statistics, fixed-positive-time tails and transverse motion |
| 13–14 | Evidence boundaries and outstanding analytical tasks |

The author-preferred term is **collision**; “double zero” denotes multiplicity.
All theorem arguments are analytical or explicitly attributed imports.
Inherited rational-algebra checks are ancillary; the schematic is a
quadratic heat model, not theta data. No canonical collision exclusion or
contradiction to Lambda>0 is proved.

## Build and verify

Run from this directory:

~~~sh
bash build.sh
~~~

Requirements: Python3.9+, pdfLaTeX, latexmk, BibTeX, Latin Modern,
microtype, TikZ, hyperref and plainurl.
[prepare_bibliography.py](prepare_bibliography.py) selects17 cited records
from their canonical repository homes into a build-only bibliography in
ignored output/pdf. Newly used complex-statistics articles have their
canonical branch records in
[complex_statistics_sources.bib](../references/complex_statistics_sources.bib);
earlier shared records are reused. No third-party PDFs enter Git.

The [build record](BUILD_RECORD.json) identifies final sources, canonical
bibliographies, PDF and all rendered pages. The final build has no warnings,
unresolved references or overfull/underfull boxes. All32 final page images
were inspected, using identity checks for unchanged pages after the final
reference-layout refinement. Text extraction has no replacement characters.

## Evidence and continuation

[Production check03](../reviews/03_TND_O_E04_B03_ANALYTICAL_AND_PRODUCTION_CHECK_20261106.md)
is a same-author analytical/production check, not independent mathematical
assessment. E01/E02/Q1/Q2 retain their supplied-preparation scope.
New finite identities and sensitivity estimates have proof-author checks;
arithmetic and positive-time tail theorems are imported with their stated
hypotheses. See [source-use07](../references/07_TND_O_B03_COMPLEX_ZERO_STATISTICS_SOURCE_USE_20261106.md),
[research return13](../notes/13_TND_O_B03_COMPLEX_ZERO_STATISTICS_AND_MANUSCRIPT_RETURN_20261106.md)
and [continuation/model-change14](../notes/14_TND_O_E04_B03_CONTINUATION_AND_MODEL_CHANGE_20261106.md).

Section14 identifies the missing canonical coefficient/exception-sensitive
estimate, joint time-height control, event coverage and separate assessment.
Recommended next is proposed **E05/Sol** assessment; no successor is activated.
The [sole progress register](../research-progress/01_OPERATOR_ITE_RESEARCH_PROGRESS_20261106.md)
owns status. Use [result summaries](../../../../../result-summaries/README.md),
[local geometry13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[patterns](../../../../../avoid/README.md) and
[scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
