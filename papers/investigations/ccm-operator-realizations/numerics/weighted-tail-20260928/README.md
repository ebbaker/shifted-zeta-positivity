# Bounded weighted prime-return diagnostic

28 September 2026. Prepared for Edward Baker with LLM assistance. Model: GPT-6 (Codex); exact serving variant and reasoning effort not exposed.

These eight prescribed cases check the full prime-power return rate into a central interval for X=20,100,1000,10000 and T=1/2,1. They use no Weil matrices and no zeta-zero data. The integer sieve includes every required prime power through 27183. The kernel has Fourier normalization Xi/4.

The analytic outcome is in the [round-8 synthesis](../../notes/CCM_WEIGHTED_TAIL_AND_DISCRETE_OBSTRUCTION_20260928.md); the numerical formulas, tables, and limitations are in the [diagnostic report](../../reviews/CCM_PRIME_RETURN_DIAGNOSTIC_20260928.md). No finite table is used to infer the uniform exterior theorem.

With Python and `mpmath==1.3.0` available in the normal environment, run from this directory:

```sh
python3 -B check_weighted_prime_tail.py --digits 80 --output /tmp/weighted-prime-tail-80.json
python3 -B check_weighted_prime_tail.py --digits 110 --output /tmp/weighted-prime-tail-110.json
python3 -B summarize_weighted_prime_tail.py --record-a /tmp/weighted-prime-tail-80.json --record-b /tmp/weighted-prime-tail-110.json --output /tmp/weighted-prime-tail-summary.json
```

To verify the saved records without rerunning the arithmetic:

```sh
python3 -B summarize_weighted_prime_tail.py --output /tmp/weighted-prime-tail-saved-check.json
```

The comparison checks the generator source hash and all retained observable strings at their 45-significant-digit serialization, excluding the working precision and roundoff-check fields. It exits unsuccessfully on a mismatch. Saved files are [80-digit observations](weighted-prime-tail-80.json), [110-digit observations](weighted-prime-tail-110.json), and the [comparison record](weighted-prime-tail-summary.json). Only small records are retained; there is no external data archive.

Checks cover the prime-step Stieltjes replay, continuous change of variables, and the observed error against a finite prime-counting envelope bound. These are multiprecision floating computations, with a rapidly converging but not interval-enclosed theta truncation. Matching precision runs and source hashes establish consistency and provenance, not proof, interval certification, or bit-for-bit portability between environments.
