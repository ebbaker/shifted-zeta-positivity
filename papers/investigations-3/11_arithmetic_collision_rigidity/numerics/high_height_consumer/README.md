# Reproduce the high height signed and vertical wall consumers

18 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**. Internal same-model verification.

The three scripts require Python and python-flint 0.9.0. Run from the
repository root with a fresh external output directory. Use actual model
and effort labels for future runs.

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/high_height_consumer/high_height_consumer.py --repo . --output-dir /tmp/inv11-high-height --execution-model gpt-6.1-sol --execution-effort ultra
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/high_height_consumer/compare_high_height_real.py --repo . --setup /tmp/inv11-high-height/SETUP.json --signed /tmp/inv11-high-height/SIGNED_CONSUMER.json --wall /tmp/inv11-high-height/VERTICAL_WALL.json --output /tmp/inv11-high-height/REAL_COMPARISON.json --execution-model gpt-6.1-sol --execution-effort ultra
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/high_height_consumer/replay_high_height_consumer.py --repo . --records /tmp/inv11-high-height --output /tmp/inv11-high-height/REPLAY.json --execution-model gpt-6.1-sol --execution-effort ultra
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py --repo . --receipts /tmp/inv11-high-height-controls --output /tmp/inv11-high-height/CONTROLS.json --execution-model gpt-6.1-sol --execution-effort ultra
```

`SETUP.json` binds the source hashes and exact binary midpoint/radius
cache. `SIGNED_CONSUMER.json` preserves the failed whole-time geometry
and its single successful time-slab repair. `VERTICAL_WALL.json` reuses
those jets with a fresh complex-strip propagation bound.
`REAL_COMPARISON.json` preserves the rejected relative-tolerance attempt,
its bounded repair and independent real-contour signed/wall margins.
`REPLAY.json` reintegrates at 256 bits, recalculates all accepted cells,
checks exact closed coverage and challenges malformed inputs and an exact
heat-polynomial event. `CONTROLS.json` uses the existing source-specific
collision controls, without substituting theta truncation constants.

The finite-height propagation proof and named published inputs are in
[Note 13](../../notes/02_updated_research_plan/13_VERTICAL_WALL_AND_FINITE_HEIGHT_NONCOLLISION_20261018.md).
The [consumer ledger](HIGH_HEIGHT_CONSUMER_LEDGER_20261018.json) records
precise finite coverage and the unclosed global bridge. Hashes identify
artifacts, not mathematical truth. There is no new Newman bound.
