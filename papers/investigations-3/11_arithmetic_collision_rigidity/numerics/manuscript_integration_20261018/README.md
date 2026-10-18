# Replay the integrated current manuscript

18 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort max**. This is internal replay by the manuscript
integrator, not independent specialist review.

The [small integration manifest](../MANUSCRIPT_INTEGRATION_REPLAY_20261018.json)
binds the current twelve-file manuscript to fresh numerical checks. It
records stored-byte and canonical parsed-JSON hashes for the generated
outputs. The outputs are reproducible external working files, not required
archival inputs. Original repository certificates and their historical
source hashes have not been overwritten. A current high-height replay must
first regenerate its setup against the current TeX files.

Use Python with python-flint 0.9.0 (recorded interval runtime Python
3.12.14), from the repository root. Choose a fresh external output directory.
The commands below reproduce this turn's actual model/effort labels; future
executions should substitute their own recorded labels.

```sh
inv11_numerics=papers/investigations-3/11_arithmetic_collision_rigidity/numerics
inv11_replay=/tmp/inv11-current-manuscript-replay
mkdir -p "$inv11_replay/pilot"
python3 "$inv11_numerics/certify_updated_manuscript.py" --output "$inv11_replay/RATIONAL_CONSTANTS.json"
python3 "$inv11_numerics/certify_nonstationary_mode_tail.py" --repo . --output "$inv11_replay/EFFECTIVE_TAIL.json" --model gpt-6-astra --effort max
python3 "$inv11_numerics/replay_nonstationary_controls.py" --repo . --receipts "$inv11_replay/control-receipts" --output "$inv11_replay/CONTROLS.json" --execution-model gpt-6-astra --execution-effort max

cp "$inv11_numerics/SHIFTED_EVALUATOR_VALIDATION_20261018.json" "$inv11_replay/pilot/SHIFTED_EVALUATOR_VALIDATION_20261018.json"
python3 "$inv11_numerics/run_plan02_pilot.py" --repo . --receipts "$inv11_replay/pilot" --validation "$inv11_replay/pilot/SHIFTED_EVALUATOR_VALIDATION_20261018.json" --declaration "$inv11_numerics/PREDECLARED_STAGE2_STAGE3_20261018.json" --output "$inv11_replay/pilot/SHIFTED_PILOT_COMPARISON_20261018.json" --signed-output "$inv11_replay/pilot/COMPLETE_MODULAR_SIGNED_ESTIMATE_20261018.json" --execution-model gpt-6-astra --execution-effort max
python3 "$inv11_numerics/replay_plan02_certificates.py" --repo . --records "$inv11_replay/pilot" --output "$inv11_replay/pilot/FINAL_CLAIM_LEDGER_20261018.json" --budget-output "$inv11_replay/pilot/GLOBAL_CONSUMER_BUDGET_20261018.json" --execution-model gpt-6-astra --execution-effort max

python3 "$inv11_numerics/high_height_consumer/high_height_consumer.py" --repo . --output-dir "$inv11_replay/high_height" --execution-model gpt-6-astra --execution-effort max
python3 "$inv11_numerics/high_height_consumer/compare_high_height_real.py" --repo . --setup "$inv11_replay/high_height/SETUP.json" --signed "$inv11_replay/high_height/SIGNED_CONSUMER.json" --wall "$inv11_replay/high_height/VERTICAL_WALL.json" --output "$inv11_replay/high_height/REAL_COMPARISON.json" --execution-model gpt-6-astra --execution-effort max
python3 "$inv11_numerics/high_height_consumer/replay_high_height_consumer.py" --repo . --records "$inv11_replay/high_height" --output "$inv11_replay/high_height/REPLAY.json" --execution-model gpt-6-astra --execution-effort max

python3 "$inv11_numerics/analytic_continuation/replay_analytic_continuation.py" --repo . --output-dir "$inv11_replay/analytic" --execution-model gpt-6-astra --execution-effort max --verify-reference "$inv11_numerics/analytic_continuation/ANALYTIC_CONTINUATION_REPLAY_20261018.json"
```

The retained validation input is deliberate: the fresh D0 replay recomputes
314 signed strips and 128 first-jet cells. To regenerate that validation
input too, use the full evaluator instructions in the [numerical README](../README.md).
The pilot creates fresh Euler and other control receipts needed by its
replayer; copying only the pilot summary is insufficient.

Expected outcomes are the counts and strict lower bounds in the manifest,
with all stated rejection tests passing. Exact hashes include execution
metadata and timings, so a future run need not reproduce them. Numerical
signs are decided by fresh outward arithmetic, never by hash equality.
The high-height factor-two speed gate remains failed. The manuscript cites
the original predeclared timing rather than a new timing from this replay.

The unchanged pilot replayer also emits an older global budget involving
exp(6400); it is a historical output, superseded by the manuscript's current
bridge **1001<|x|<exp(2000)**. The analytic replayer inherits finite coverage;
the separate high-height commands above freshly recompute that coverage's
numerical wall and signed premises. No new Newman bound is established.
