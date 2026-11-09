# B10 r3 source use and arithmetic semantics

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, OC chat0011. Recorded thread settings
`gpt-6-astra / max`; per-turn backend configuration unavailable.

[Note22](../notes/22_TND_OC_B10_R3_CELL_RANGES_AND_GAUSSIAN_WIDTH_20261109.md)
derives its geometric range bound directly. It imports the exact marked
kernel from Note19, the complete theta tail from Note20, and E13's
assessed census from Note21/assessment17/Return27. The source-free trace
and exact constant checks are explicitly narrower than a new winding
certificate. The earlier [FLINT source record15](15_TND_OC_E13_FLINT_SOURCE_USE_20261109.md)
owns the inherited zeta implementation/remainder inspection.

Selected primary documentation inspected on 9 November 2026:

- The FLINT team, [Ball arithmetic](https://flintlib.org/doc/guide/types/ball-arithmetic.html),
  displayed version **3.7.0-dev**, generated 2026-11-09. Checked
  enclosure semantics, exact rational versus binary-float input,
  overestimation/dependency, three-valued predicates, and precision
  versus actual radius. These support the endpoint-ball and exact
  radius contract, not the new Gaussian width inequality. The page
  is development documentation, not proof that the execution runtime
  has changed from E13's FLINT 3.6.0. E13 r2 must record its actual
  version and verify the APIs it uses. Passage inspection only.
- The FLINT team, [arb_hypgeom: error functions](https://flintlib.org/doc/arb_hypgeom/index.html),
  same displayed development version. Checked `arb_hypgeom_erf` and
  its integral normalization; Note22 uses scalar endpoint evaluation.
  No special-function library-wide audit or finite-ladder runtime
  guarantee is claimed. The [module page](https://flintlib.org/doc/arb_hypgeom/index.html)
  remains the stable link if its section anchor changes.
- OpenAI, [Model selection](https://developers.openai.com/api/docs/guides/model-selection),
  retrieved 2026-11-09: Astra is described for ambiguous/deep analytical
  work and GPT-6.1 Sol for complex work with time/cost constraints.
  The concrete B-to-E handoff follows Edward Baker's
  [research workflow](../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md).
  This is model-routing guidance, not a measured cost advantage or
  an assertion of per-turn backend settings. Edward selects effort.

These are online documentation records, not new research-article
imports. No third-party PDF was downloaded or added. The new
[documentation bibliography](b10_cell_range_sources.bib) identifies the
two FLINT pages. No literature novelty claim is made for interval
arithmetic, Gaussian tail summation or the finite source evaluation.
