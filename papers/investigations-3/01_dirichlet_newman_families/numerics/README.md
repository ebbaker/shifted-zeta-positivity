# Dirichlet Newman families: numerics

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

Reproducible code, parameters and small execution records.

Before each run, state the question, domain, baseline, accuracy, resource
limit and stopping answer. Distinguish floating diagnostics from
outward-rounded certificates. Record parameters, environment and actual
model/effort; a replay or hash does not prove the mathematical implication.

Follow [LARGE_FILES.md](../../../../LARGE_FILES.md). Keep regenerable large
outputs external, with a tracked guide and small hash-bound records when
first needed; no large archive is created by this setup.

## Records

17 October 2026. Added by Claude Opus 5.5 (`claude-opus-5-5`, Claude
Cowork, reasoning effort max) for
[note 01](../notes/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md).
Both programmes are standard-library Python and print one deterministic
JSON record, floats rounded to 12 significant figures. They are floating
diagnostics and planning arithmetic, not outward-rounded certificates; no
number in either record bounds a de Bruijn–Newman constant.

| Programme | Record | Note sections | Kind | Run time |
| --- | --- | --- | --- | --- |
| [check_character_normalization_claude_20261017.py](check_character_normalization_claude_20261017.py) | [CHECK_CHARACTER_NORMALIZATION_CLAUDE_20261017.json](CHECK_CHARACTER_NORMALIZATION_CLAUDE_20261017.json) | 1 | floating diagnostic | about 5 s |
| [benchmark_family_contract_claude_20261017.py](benchmark_family_contract_claude_20261017.py) | [BENCHMARK_FAMILY_CONTRACT_CLAUDE_20261017.json](BENCHMARK_FAMILY_CONTRACT_CLAUDE_20261017.json) | 3.1, 4.1–4.6 | numerical (Platt's budget), otherwise planning | under 1 min |

- **Normalization check.** Question: whether the kernel, root numbers and
  conjugate-pair relation of Lemma 1.1 agree with an independent
  evaluation of ξ_χ and with LMFDB. Domain: sixteen primitive characters of
  conductor 3–13, both parities, real and complex; |Re z| ≤ 40,
  |Im z| ≤ 0.9; t = 0 and 0.2. Baseline: ξ_χ from Hurwitz zeta values
  (Euler–Maclaurin) and Stirling's series; LMFDB zeros and signs.
  Accuracy: trapezoid step 0.01 on |u| ≤ 2.6; worst relative disagreement
  3.7·10⁻⁹. No stopping answer was fixed in advance; a disagreement at
  quadrature scale or larger would have voided the normalization table.
- **Benchmark.** Question: whether the consistent transfer of a published
  zeta parameter row gives a planning value below the conditional
  baseline 0.2812 at Platt's verified heights, and what the strip
  comparison gives. Domain: every modulus q ≤ 400,000 with primitive
  characters, both parities; conductors 10³–10¹² for planning. Baselines:
  Corollary 3.2 (0.2812, conditional) and the unconditional 1/2.
  Accuracy: elementary floating arithmetic; Section B sums capped at 10⁶
  terms (the Platt–Trudgian row needs 630,783); Section H by Simpson's
  rule, calibrated against Hakimoglu-Brown's equation (18),
  0.1797275414. Stopping answer, fixed before the run (note Section 4):
  a transferred value above 0.2812 at every modulus Platt covers demotes
  first-term dominance at existing verification heights. It did (0.30).

Run from this folder; each command regenerates its record byte for byte.
Both records were generated with Python 3.13.16 on x86_64 Linux and
replayed byte-identically with Python 3.10.12 on aarch64 Linux.

```sh
python3 -I check_character_normalization_claude_20261017.py > CHECK_CHARACTER_NORMALIZATION_CLAUDE_20261017.json
python3 -I benchmark_family_contract_claude_20261017.py > BENCHMARK_FAMILY_CONTRACT_CLAUDE_20261017.json
```

| File | SHA-256 |
| --- | --- |
| check_character_normalization_claude_20261017.py | `b6a1b383aa73a6c453aec9d91e62056cdd91f928fd04ccedb99a1fc2a6ca6273` |
| CHECK_CHARACTER_NORMALIZATION_CLAUDE_20261017.json | `d37d6cb71fad823733f5d8838641cdea4867ac637db8d1901b8bed6b10822857` |
| benchmark_family_contract_claude_20261017.py | `07ec4ac02e4ef73c90c4e621a688d8ac6296132501c9fa5ce8b353a7ed06fafc` |
| BENCHMARK_FAMILY_CONTRACT_CLAUDE_20261017.json | `828f89b02f427a089ed186e60b97d5fab10b89cd62c8e65c3b8fdc12df8310bd` |

A replay or hash shows the arithmetic is reproducible, not that the
planning hypothesis behind Sections B and E–H holds.
