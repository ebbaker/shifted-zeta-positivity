# Boundary Bootstrap in the Newman Flow

13 November 2026, America/New_York. Author: **Edward Baker**; drafted for
him with substantial OpenAI Codex LLM assistance. The manuscript lead's
actual model and reasoning effort are unavailable in the recorded chat
configuration. E11's distinct reviewer was explicitly dispatched as
**gpt-6.1-sol / ultra**.

The current analytical manuscript is [main.tex](main.tex), with its
development in [sections/](sections/) and citations in
[references.tex](references.tex). It synthesizes this investigation
through the completed E11 assessment, retaining all named-input and
internal-review limits. It does not replace the broader parent manuscript.

The **30-page PDF is outside the repository**:
[Read the manuscript](/Users/Shared/szp-archive/gnp-boundary-bootstrap/manuscript/gnp_boundary_bootstrap_20261113.pdf).
This is a local reading copy, not a public deposit. It is regenerable from
these sources. The [build record](BUILD_RECORD_20261113.json) identifies
the exact source and PDF bytes; a hash establishes identity, not a proof.
No PDF, rendered page, compilation product or snapshot folder is stored
here.

## Analytical organization

1. Canonical theta normalization and the separate curve/common-time quantifiers.
2. Named complex Riemann–Siegel input and derivation of its positive finite-window extension, including the full source exterior, every mode and the correction.
3. Signed exponent-pair envelopes, the scoped A-chain threshold, the five-pair width567/1000, and the exact far-tail join.
4. Complete Green identity, quadratic consumer, contour costs, observation placement and conditional scaling.
5. Conditional width9/16 from the every-center4/66² Poisson budget, with every boundary edge paid.
6. Middle-band localization, center means and whole-dyadic resonator restriction, retaining product coincidences and nearby frequencies.
7. E11-reviewed square-root freezing, sparse logarithmic-cell bounds, and the actual quartic packet with complete background interaction.
8. Collision-control premise screen, source/review provenance and supporting arithmetic.
9. Outstanding moment, carrier, compact-height, time-zero and iteration tasks.

The principal enclosure is for some unevaluated t_*>0, all0<t<=t_* and
|x|>=4pi exp(1/t). Its width is567/1000. Conditional9/16 remains
curve-only and unpaid. Long mean decay and sparse-packet failure do not
decide the every-center moment or the fixed short-center witness.

## Rebuild and verification

From the repository root, with Python3 and a LaTeX installation providing
`latexmk` and `pdflatex`:

```sh
python3 papers/investigations-5/09_green_potentials_newman_flow/02_height_time_boundary_bootstrap/manuscript/build.py \
  --output-dir /private/tmp/gnp-boundary-bootstrap-20261113
```

The build script refuses an output directory inside the repository,
including a path that resolves there through a symlink. All auxiliary
files go to the chosen external directory. Rebuilt PDFs may differ in
metadata bytes; use the source hashes and build record for provenance.
The verified reading copy was copied to the external archive path above.

The production run compiled without LaTeX warnings, unresolved references
or overfull boxes. All30 pages were rendered and visually inspected;
the final reference-page adjustment was re-rendered and checked.
[Review12](../reviews/12_GNP_BB_MANUSCRIPT_PRODUCTION_ASSESSMENT_20261113.md)
records the synthesis self-check, separately from
[E11 Review11](../reviews/11_GNP_BB_E11_ADDITIONAL_AGENT_REVIEW_20261113.md).
No new theta-field evaluation, onset calculation or parameter search was
used. The [small production record](../numerics/24_GNP_BB_MANUSCRIPT_CHECKS_20261113.json)
records source-preservation, reference, link, size and output-location checks.

Follow [LARGE_FILES](../../../../../LARGE_FILES.md), the
[result index](../../../../../result-summaries/README.md) and
[avoid index](../../../../../avoid/README.md), specifically
[heat-flow cluster11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md)
and [scoped exclusions07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
