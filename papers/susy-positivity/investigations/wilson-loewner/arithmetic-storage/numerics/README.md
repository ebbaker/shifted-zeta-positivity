# Arithmetic-storage numerics

The first session studies L=11/20, h=1/5, and omega=1/1000. Read the
[analysis](../notes/FIRST_PRIME_CONTINUATION_ANALYSIS_20260924.md) for domains,
tail bounds, proof scope, and the remaining all-input mixed-coupling gap.

- `certify_first_prime_inputs.py` uses standard-library outward rational
  arithmetic. It certifies two all-input local metric floors and diagonal
  defect floors, two specified witness comparisons, and perturbation bounds.
  It does **not** certify the complete first-prime relative norm.
- `diagnose_first_prime_coupling.py` requires NumPy and uses independent
  physical-delay quadrature. Its finite-input norms are diagnostics, not
  all-input upper bounds.
- `check_first_prime_records.py` checks source bindings, nested precision
  records, and a conditional implication whose hypothesis remains unproved.

From the repository root, preserving committed records:

```sh
python3 -B papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/numerics/certify_first_prime_inputs.py --output /tmp/first-prime-inputs-40digits-20260924.json
python3 -B papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/numerics/certify_first_prime_inputs.py --digits 60 --output /tmp/first-prime-inputs-60digits-20260924.json
python3 -B papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/numerics/diagnose_first_prime_coupling.py --certificate /tmp/first-prime-inputs-40digits-20260924.json --output /tmp/first-prime-coupling-diagnostics-20260924.json
python3 -B papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/numerics/check_first_prime_records.py --records /tmp --output /tmp/first-prime-record-checks-20260924.json
```

The interval utility is imported from the existing critical-path anchor; the
floating local-form quadrature is imported from its append diagnostic. Both
dependencies are recorded by source hash. Specify `--repository` when running
copies outside the repository layout. Python must not be run with `-O`.

All generated matrices remain in memory; only small scalar records are saved.
Follow [LARGE_FILES.md](../../../../../../LARGE_FILES.md) for future derived data.
Current evidence: two passing precision runs, 15 nested interval pairs, eight
floating controls, and an exact conditional comparison. Specialist review is
outstanding.

Prepared for Edward Baker, 24 September 2026, with substantial LLM assistance.
Model: GPT-6 (Codex; developer-provided identity). Reasoning effort: not exposed;
not inferred.
