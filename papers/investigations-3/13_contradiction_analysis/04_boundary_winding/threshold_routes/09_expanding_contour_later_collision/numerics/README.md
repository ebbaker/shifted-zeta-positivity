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
