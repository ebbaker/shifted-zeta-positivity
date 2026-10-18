# Explicit heat zero counts: numerics

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

Reproducible code, parameters and small execution records.

Opening work, 17 October 2026: **gpt-6.1-sol (Codex), ultra**, with substantial LLM assistance.
The [exact rational checker](check_local_count_reduction.py) and
[run record](LOCAL_COUNT_REDUCTION_CHECKS_20261017.json) verify downstream constants,
wall conventions, multiplicity accounting and an endpoint failure injection.
They do not prove the off-axis comparison or an unconditional local count.
Run from the investigation root:

```sh
python3 numerics/check_local_count_reduction.py
python3 numerics/check_local_count_reduction.py --kernel-floor 9/40
```

The second command intentionally exits 1.
Before each run, state the question, domain, baseline, accuracy, resource
limit and stopping answer. Distinguish floating diagnostics from
outward-rounded certificates. Record parameters, environment and actual
model/effort; a replay or hash does not prove the mathematical implication.

Follow [LARGE_FILES.md](../../../../LARGE_FILES.md). Keep regenerable large
outputs external, with a tracked guide and small hash-bound records when
first needed; no large archive is created by this setup.

## Round 2: off-axis constants

17 October 2026. Prepared for Edward Baker with substantial LLM assistance:
**gpt-6.1-sol (Codex), ultra**.

The [comparison checker](check_off_axis_comparison.py) and
[record](OFF_AXIS_COMPARISON_CHECKS_20261017.json) verify rational allowances and the
comparison budget for [Note 02](../notes/02_EXPLICIT_OFF_AXIS_COMPARISON_AND_HIGH_HEIGHT_COUNT_20261017.md).
The analytic derivation is now covered by cross-model Review 02; the
finite arithmetic record remains authoring support, not analytic verification. Run from the investigation root:

```sh
python3 numerics/check_off_axis_comparison.py
python3 numerics/check_off_axis_comparison.py --comparison-ceiling 13/20
```

The second command intentionally exits 1 because the current sufficient
budget exceeds that requested ceiling. This is a failure-handling check,
not a counterexample to the actual comparison. No zero survey was run.

## Post-review round-2 continuation

17 October 2026. Prepared for Edward Baker with substantial LLM assistance:
**gpt-6.1-sol (Codex), ultra**. The [new replay package](round-2/README.md)
checks the cutoff x>=100000, the retained remainder prefactor, paired
kernel, disk derivative and three exact failure injections. The old
comparison checker label now describes its endpoint equality honestly;
its script hash and old record have been refreshed. The previous record's
capture time and script hash are retained as provenance.
