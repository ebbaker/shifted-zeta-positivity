# Topological/SUSY bulk positivity attempt

This active attempt was promoted from `brainstorm` to `attempts`. The exploratory background remains in [the topological note](../../brainstorm/TOPOLOGICAL_BULK_BOUNDARY_POSITIVITY_20260912.md), [the superspace companion](../../brainstorm/SUPERSPACE_COHOMOLOGICAL_BOUNDARY_PAIRINGS_20260912.md), and [the candidate package](../../brainstorm/candidate-bulk-theories/README.md).

Start with [the current continuation](CONTINUATION_FIELD_MIXING_20260912.md). The latest [field-mixing calculation](FIELD_MIXING_20260912.md) defines and eliminates a positive low-mass/history system. It cancels the previous leading cusp exactly, but leaves a nonzero third-derivative jump and an infinite-rank error. It also gives scoped obstructions to pure relaxation of the old energy, finite convex compliance splits, and a simple derivative penalty for the new field.

The [preceding continuation](CONTINUATION_20260912.md) constructs the positive loop evolution that matches the contact and prime delta coefficients at finite coupling. Its continuous remainder is the starting point for the current calculation.

**Status:** explicit positive model responses and scoped analytic failure results, with exact coefficient checks and floating-point diagnostics. No full Weil completion, new full-form positivity range, arithmetic Ward identity, or proof of RH is claimed. The new arguments have not received independent specialist or formal verification.

* [Current diagnostic script](calculations/check_field_mixing.py) and [record](results/field-mixing-diagnostics.json)
* [Current provenance and claims record](results/field-mixing-pass-record.json)
* [Previous loop checker](calculations/check_loop_evolution.py) and [fresh replay](results/loop-evolution-replay.json)
* [Preceding evaluation](review/EVALUATION.md) and [original package record](results/package-record.json)

Only small text, source and record files are needed. All numerical arrays are transient. Large derived data belongs in `szp-archive` under [the root policy](../../../../LARGE_FILES.md); this pass requires no external data archive.
