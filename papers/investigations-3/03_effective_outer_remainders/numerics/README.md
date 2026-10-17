# Effective outer remainders: numerics

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
[note 01](../notes/01_HEIGHT_P_TRANSPORT_AND_LEMMA_AP_CLAUDE_20261017.md).
The programme is standard-library Python and prints one deterministic JSON
record (106 kB), floats rounded to 12 significant figures. Its sections
A–D are floating diagnostics, E, F and H a floating evaluation of the
explicit bound of the note's Proposition 4.5, and G planning arithmetic.
None is an outward-rounded certificate, and no number in the record
bounds a de Bruijn–Newman constant.

| Programme | Record | Note sections | Kind | Run time |
| --- | --- | --- | --- | --- |
| [height_p_transport_claude_20261017.py](height_p_transport_claude_20261017.py) | [HEIGHT_P_TRANSPORT_CLAUDE_20261017.json](HEIGHT_P_TRANSPORT_CLAUDE_20261017.json) | 2.2, 5–7 | floating diagnostic (A–D), floating evaluation of a proved bound (E, F, H), planning (G) | 1–2 min |

- **Question.** Whether the explicit remainder E of Proposition 4.5 keeps
  the time-t floor of S(x,p,t) at or above Project 01's time-zero floor
  (Lemma A_p with δ = 0) for 0 < t ≤ 1/2, and from which height ℓ_* and
  conductor on; and whether the transport identity and E agree with
  direct computation.
- **Domain.** Sections B–D: zeta at x from 3 to 25 (identity) and at 10³
  and 10⁴ (transport law); real characters modulo 10007, 10009, 100003,
  1000003 and 1000033 and a cubic character modulo 10009 at
  x ∈ {0, 2, 10}; p ∈ {√5, 3}; t from 0.02 to 1/2. Sections E–H: ℓ from
  about 4 to 40; p ∈ {√5, 2.5, 3, 4} for the thresholds and up to 6 for
  zeta; twenty times 0.001 ≤ t ≤ 1/2; conductors 10⁴–10¹²; zeta at the X
  of Polymath's and Platt–Trudgian's certificates.
- **Baseline.** Project 01's time-zero floor C_{q,a}(p) (its Lemma 3.4)
  and its strip-comparison planning values (its Section 4.6, reproduced in
  section G).
- **Accuracy.** ζ and its derivatives by Euler–Maclaurin, ψ by recurrence
  and asymptotic series (self-checks in section A); real-variable
  majorants interpolated from logarithmic tables (relative error below
  4·10⁻⁵); composite Simpson rules; Gaussian tails beyond 40τ dropped;
  bisection to 0.03 in ℓ and 0.006 in log₁₀ q. Not outward-rounded.
- **Resource limit.** One run of 1–2 minutes on one core.
- **Stopping answer.** None was fixed before this exploratory run. The
  note's Section 9.2 fixes one for the certified rerun: if outward
  rounding moves ℓ₁(√5) above 12, report the certified threshold and
  recompute the conductor thresholds.

Run from this folder:

```sh
python3 -I height_p_transport_claude_20261017.py > HEIGHT_P_TRANSPORT_CLAUDE_20261017.json
```

The record was generated with Python 3.13.16 on x86_64 Linux (about
2 min) and regenerates byte for byte there. A replay with Python 3.10.12
on aarch64 Linux (59 s) agrees in sections A and E–H, which carry the
bound, the thresholds, the floors and the planning values. It differs in
24 floats of sections B–D: three identity differences, all below 10⁻¹⁵
in size, and 21 measured deviations, by at most 4·10⁻¹¹ relative.

| File | SHA-256 |
| --- | --- |
| height_p_transport_claude_20261017.py | `abe3bff66fbf59998a15434d5036a3c0351e664d61c64f11656571ace78a13aa` |
| HEIGHT_P_TRANSPORT_CLAUDE_20261017.json | `e1e2f2b2b19973006484b5f79aa3373a440d981ba46003e28762879fd290341a` |

A replay or hash shows the arithmetic is reproducible, not that the
evaluation is outward-rounded or that E decreases in ℓ between the
sampled values.

### Note 02

17 October 2026. Added by Claude Opus 5.5 (`claude-opus-5-5`, Claude
Cowork, reasoning effort max) for
[note 02](../notes/02_HAKIMOGLU_BROWN_COMPARISON_AND_UNCONDITIONAL_TABLE_CLAUDE_20261017.md).
Both programmes are standard-library Python and print one deterministic
JSON record. The comparison programme imports the note 01 programme from
this folder.

| Programme | Record | Note sections | Kind | Run time |
| --- | --- | --- | --- | --- |
| [hakimoglu_brown_comparison_claude_20261017.py](hakimoglu_brown_comparison_claude_20261017.py) | [HAKIMOGLU_BROWN_COMPARISON_CLAUDE_20261017.json](HAKIMOGLU_BROWN_COMPARISON_CLAUDE_20261017.json) (19 kB) | 3–6, 10 | reproduction of the preprint's printed certificates (A); floating comparison (B); construction of the q0 = 1 table, with exact Bernstein and gate checks and floating scalars (C); planning (D, E) | 2–3 min |
| [unconditional_strip_table_claude_20261017.py](unconditional_strip_table_claude_20261017.py) | [UNCONDITIONAL_STRIP_TABLE_CLAUDE_20261017.json](UNCONDITIONAL_STRIP_TABLE_CLAUDE_20261017.json) (2 kB) | 4 | exact rational checks and a directed-rounding evaluation of the preprint's scalar bounds, for the q0 = 1 table and, as a control, for the preprint's Table 3 | 1–2 min |

- **Question.** Does the preprint's Theorem 12, with its own Proposition 11
  at p = 61/20, reach q = 1/25 by t = 1/5 from the unconditional strip
  M(0) ≤ 1? How do note 01's floors compare with the preprint's? What does
  the derivative kernel give for zeta with note 01's floors, and for
  Project 01's Target A?
- **Domain.** p = 61/20, and 301/100 for the preprint's Table 2. For zeta,
  t ≤ 1/5 in steps of 1/200 at the preprint's X = 60000083951.5, and
  heights 2 ≤ p ≤ 3.5 for the planning runs. For the family, conductors
  10⁶, 10⁸ and 10¹², both parities, 2.25 ≤ p ≤ 4 and t ≤ 1/2.
- **Baseline.** The preprint's printed certificates: its value (18), its
  Tables 2–3 and 5–7, and its margins. Also Platt and Trudgian's published
  0.2, and Project 01's Target A values (note 01, record G).
- **Accuracy.**
  - Certificate: exact rationals for the chain, the Bernstein coefficients
    (eight subintervals) and the gates, with the Taylor sum E_20 as lower
    bound for the exponential. The scalar expressions use decimal
    arithmetic at 32 digits: exp and ln are moved one unit outward, and
    other operations are rounded toward the bound.
  - Comparison: double precision. The polynomial condition is sampled on
    404 × 41 points (planning), except in section C, where it is checked
    exactly.
- **Resource limit.** One run each, a few minutes on one core.
- **Stopping answer.** None was recorded before the exploratory runs. The
  certificate's answer is binary: any failed check voids the table.

Run from this folder; each command regenerates its record byte for byte
with Python 3.13.16 on x86_64 Linux, where both were generated.

```sh
python3 -I hakimoglu_brown_comparison_claude_20261017.py > HAKIMOGLU_BROWN_COMPARISON_CLAUDE_20261017.json
python3 -I unconditional_strip_table_claude_20261017.py > UNCONDITIONAL_STRIP_TABLE_CLAUDE_20261017.json
```

With Python 3.10.12 on aarch64 Linux, the certificate replays byte for byte
(56 s). The comparison record (97 s) differs in two floats of section A,
both at rounding level: 0.004 units of 10⁻¹² in a table difference, and
1.2·10⁻¹⁰ relative in a margin. It does not differ anywhere else.

| File | SHA-256 |
| --- | --- |
| hakimoglu_brown_comparison_claude_20261017.py | `4f78eeab23aa25a676aa80eb61c24b4829d35789384497043c76c76f3139c3de` |
| HAKIMOGLU_BROWN_COMPARISON_CLAUDE_20261017.json | `460a3478b9f0f63af370e3ffb3e884e584f7e7d123cc1cd9e4ac3bf9a1ba660b` |
| unconditional_strip_table_claude_20261017.py | `b212a2b93f2ac191dff23b01e4cd20cdf5fb057e5063ba089189c92b7101fc7e` |
| UNCONDITIONAL_STRIP_TABLE_CLAUDE_20261017.json | `69997f80743411bb952c727f1e8c25b710fe28b14d8a2f995967fb08383eff67` |

A replay shows the arithmetic is reproducible. The certificate's
conclusion is conditional on the preprint's analytic statements, which no
programme checks.
