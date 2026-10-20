# Expanding-contour checks and receipts

20 October 2026. Prepared for **Edward Baker** with substantial LLM assistance.
Model **gpt-6-astra (Codex)**, actual effort **ultra**, verified from recorded turn metadata.

- [Exact contour checker](check_expanding_contour_controls.py) and [receipt](EXPANDING_CONTOUR_CONTROLS_20261020.json): Python standard library, 18 exact polynomial cases and three refusals.
- [Bounded theta wrapper](check_bounded_first_jet_extension.py) and [receipt](BOUNDED_THETA_EVENT_GATE_20261020.json): python-flint 0.9.0, four fixed closed cells, 192/256-bit consumer arithmetic using the pinned 160-bit source acquisition. New theta value exclusion only.
- [Input versions](BW09_SOURCE_VERSIONS_20261020.json): working-tree source hashes, including uncommitted notes.
- [Review record](BW09_REVIEW_RECORD_20261020.json): separately reviewed byte versions and same-code replay scope.

Replay from repository root, choosing an output outside the retained records:

```sh
python3 papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/numerics/check_expanding_contour_controls.py --output /tmp/expanding-controls-replay.json
python3 papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/numerics/check_bounded_first_jet_extension.py --repo . --output /tmp/expanding-theta-gate-replay.json
```

The second script requires python-flint and the pinned existing repository source cache. It verifies the original manuscript bytes at the recorded Git commit, records the current manifest separately, and fails if required source versions are unavailable or changed. It never rewrites the cache or silently reuses the old spatial error budget. The first replay is exact rational arithmetic; the second uses outward Arb intervals. No computation tests the full R=1 theta contour.

The [quadratic heat flow illustration](plot_heat_flow_lens.py) generates [PNG](../notes/figures/HEAT_FLOW_LENS_20261020.png) and [SVG](../notes/figures/HEAT_FLOW_LENS_20261020.svg) versions of [Note 06](../notes/06_HEAT_FLOW_CONTOURS_AND_GAUSSIAN_CAP_ENERGY_20261020.md)'s exact rounded contour. It requires NumPy and Matplotlib; this rendering used NumPy 2.5.4 and Matplotlib 3.11.2. Pass `--output-dir` to choose a folder, such as `/tmp/heat-flow-figure`. It illustrates analytic identities and supplies no theta acquisition or interval certificate.

[Notes](../notes/README.md) · [Progress](../research-progress/01_EXPANDING_CONTOUR_PROGRESS_20261020.md).

## Frozen HFCE execution, 20 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra,
actual effort ultra**. The three original contracts were saved before
evaluation; their bytes are retained.

| Consumer | Frozen contract | Exact receipt |
| --- | --- | --- |
| [Direct first-jet baseline](check_hfce_baseline.py) | [Baseline](HFCE_BASELINE_CONTRACT_20261020.md) | [Direct exclusion](HFCE_BASELINE_20261020.json) |
| [Gaussian whole-cap comparison](check_hfce_cap_comparison.py) | [Cap](HFCE_CAP_CONTRACT_20261020.md) | [Bounded estimator failure](HFCE_CAP_COMPARISON_20261020.json) |
| [Localized comparator](check_hfce_localized_comparison.py) | [Localized](HFCE_LOCALIZED_CONTRACT_20261020.md) | [Positive actual average](HFCE_LOCALIZED_COMPARISON_20261020.json) |

Use Python with python-flint 0.9.0. Each script takes `--repo`, `--contract`
and `--output`. The cap script additionally takes `--baseline` pointing
to the direct receipt; its default baseline-wrapper path is the sibling
`check_hfce_baseline.py`. Run the baseline before the cap. The cap's
exit status 1 with `bounded_failure_no_adaptation` is its expected
strict-sign failure, not a source-validation exception.
The localized pointwise-positive gate stops weighted integration.
All scripts use the unchanged exact source cache, zero new quadratures,
192/256-bit arithmetic and one predeclared closed box. No scan or
adaptive retry is performed.

The [review record](HFCE_REVIEW_RECORD_20261020.json) pins final sources,
contracts, notes and receipts and records replay equivalence. The
[research note](../notes/07_FIXED_GAUSSIAN_COMPARISON_20261020.md) proves
the global Gaussian tail premise; code alone does not prove that
analytic input. The manuscript and old cache remain unchanged.
