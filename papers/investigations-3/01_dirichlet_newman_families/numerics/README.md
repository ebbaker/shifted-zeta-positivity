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
[note 01](../notes/round-1/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md).
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
  the transferred values exceeded 0.2812 (about 0.30). Review 01 restricts
  the resulting demotion to these two leading-order row-transfer models;
  other first-term-dominance parameters and mollifiers were not tested.

Run from this folder. Both records were generated with Python 3.13.16 on
x86_64 Linux and replayed byte-identically with Python 3.10.12 on aarch64
Linux. Review 01 found byte identity for the benchmark on local macOS,
while the normalization output agreed numerically with differing roundoff
residuals. Byte identity is claimed only for the tested environments;
compare temporary output before replacing a stored record.

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

## Codex review loss diagnostic

17 October 2026. Prepared for Edward Baker with substantial LLM assistance;
**gpt-6.1-sol (Codex), reasoning effort ultra**. The
[contract review](../reviews/01_NORMALIZATION_AND_TRANSFER_CONTRACT_REVIEW_CODEX_20261017.md)
adds a bounded sensitivity check of the permitted loss `delta = C/4` at
conductors `1e8` and `1e12`, both parities, with `a=1` and `b=0`. The
[programme](check_comparison_loss_codex_20261017.py) hash-checks the reviewed
benchmark source, independently integrates its rational ODE in closed form,
and cross-checks the selected minima against Simpson quadrature. It retains
the original height grid. The [record](CHECK_COMPARISON_LOSS_CODEX_20261017.json)
contains the actual local runtime and four planning values. These assume
positive-time persistence and H12; they are not certified bounds.

```sh
python3 -I check_comparison_loss_codex_20261017.py > CHECK_COMPARISON_LOSS_CODEX_20261017.json
```

The review also reports that the original benchmark record replays byte for
byte on local macOS/Python 3.10.0, while the original normalization record
agrees numerically but differs in roundoff residuals. The general
byte-identity wording above has been narrowed accordingly.

| File | SHA-256 |
| --- | --- |
| check_comparison_loss_codex_20261017.py | `9e38938d4aa4b06aab13136fd786c27f975e20fdf9c45118a779997c7e50ac97` |
| CHECK_COMPARISON_LOSS_CODEX_20261017.json | `143c35012a9d0653a77bcbcc3abddee72af452de2a08e817dc45e4a7e5f58027` |

## Round-2 exact scalar certificate

17 October 2026. Prepared for Edward Baker with substantial LLM assistance;
**gpt-6.1-sol (Codex), reasoning effort ultra**. For the
[round-2 analytic note](../notes/round-2/02_BURGERS_FLOOR_AND_CONDITIONAL_COMPARISON_CODEX_20261017.md),
the [programme](certify_dirichlet_scalar_conditional_20261017.py) proves,
using rational arithmetic, that the time-zero floor exceeds 6 for both
parities at q >= 10^12 and that J_6(27/100) > 1/2. The
[record](DIRICHLET_SCALAR_CONDITIONAL_CERTIFICATE_20261017.json) gives
outward decimal displays of the rational enclosures and actual runtime.
Question and domain: one fixed scalar comparison, p=3, C=6, T=27/100,
with a von Mangoldt cutoff of 1000. Baseline: J >= 1/2. Stopping answer:
accept the finite scalar implication only if every exact inequality passes.
At capture, the implication to Lambda <= 0.27 was conditional on H12.
The [round-3 proof](../notes/round-3/03_SINE_TAIL_LIMIT_AND_COMPARISON_CODEX_20261017.md)
now supplies the analytic implication without H12. The numerical record
retains its original conditional-contract wording and certifies only the
same finite scalar inequalities; the theorem is in the note and manuscript.

```sh
python3 -I certify_dirichlet_scalar_conditional_20261017.py
```

All decisions use `fractions.Fraction`; no floating-point decision or
large derived data is involved. Runtime metadata may differ on replay.
The original Claude programmes are byte-preserved references: their
opening docstrings retain the capture-time note path, now superseded by
the working round-1 link above. The legacy benchmark key
`distinct_Lambda_classes` counts conjugacy classes requiring checks,
not proven distinct constants.

| File | SHA-256 |
| --- | --- |
| certify_dirichlet_scalar_conditional_20261017.py | `0b7d513728d6c20ae380bb9b3ea9bc01a8c8963be1d9efd5aab970a4535b4cf9` |
| DIRICHLET_SCALAR_CONDITIONAL_CERTIFICATE_20261017.json | `ff6e250a2340bdc88e00c6c2a9043257d50076c44231d7d0b7fd633de4030837` |
