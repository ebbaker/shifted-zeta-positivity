# Explicit heat zero counts: round-2 arithmetic

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance: **gpt-6.1-sol (Codex)**, reasoning effort **ultra**.

Question: does the complete remainder budget close at x>=100000, and do
Schwarz–Pick plus conjugate pairing improve the count? Baseline: the
reviewed Note 02 domain x>=2000000 and its comparison-to-count extraction.
Domain: 0<t<=1/2, 3<=y<=4. Accuracy: exact rational inequalities and Taylor
enclosures. Resource limit: four fixed standard-library runs, no zero
survey or parameter sweep. Stopping answer: passing finite constants and
three failing excessive allowances; the analytic proof is in the
[round-2 note](../../notes/round-2/01_LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CODEX_20261017.md).

From the investigation root:

```sh
python3 numerics/round-2/check_lower_cutoff_and_paired_extraction.py
python3 numerics/round-2/check_lower_cutoff_and_paired_extraction.py --comparison-ceiling 69/100
python3 numerics/round-2/check_lower_cutoff_and_paired_extraction.py --kernel-floor 3/10
python3 numerics/round-2/check_lower_cutoff_and_paired_extraction.py --derivative-allowance 3/2
python3 numerics/round-2/check_lower_cutoff_and_paired_extraction.py --write-record numerics/round-2/LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CHECKS_20261017.json
```

The first command exits 0; the three injections exit 1. The last replays
all four commands and writes the small hash-bound [execution record](LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CHECKS_20261017.json).
The derivative injection fails the exact disk-automorphism witness 49/30,
not just a chosen sufficient allowance. The kernel injection fails an
attained real-zero endpoint, including the multiplicity-two case. The
comparison injection fails a sufficient error budget; it is not a
counterexample to H_t. The old 98/a compression is deliberately checked
to fail at the new a=89 endpoint; the proof retains its full denominator.

These are same-model authoring checks of finite constants and class
examples, not formal verification of classical imports or the universal
analytic proof. No new specialist or cross-model review is claimed.
All records stay below 1 MiB under [LARGE_FILES.md](../../../../../LARGE_FILES.md).
