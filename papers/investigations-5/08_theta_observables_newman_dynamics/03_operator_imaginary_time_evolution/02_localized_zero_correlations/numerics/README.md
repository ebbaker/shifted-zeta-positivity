**B10 r3 exact geometry and bookkeeping.** [Record19](19_TND_OC_B10_R3_EXACT_GEOMETRY_20261109.json) and [checker](check_b10_r3_cell_geometry.py) verify the imported cell geometry, trace identity, accepted count tree, six malformed-input rejections and rational radius cap. Zero new source/kernel calls; no fresh winding or projected-value certificate. From this investigation root, supply the exact trace location recorded in execution18:

```sh
python3 numerics/check_b10_r3_cell_geometry.py --trace /private/tmp/tnd-oc-e13-r1-01a1c185/contours.jsonl
```

A relocated trace is accepted only with identical stored/canonical hashes. A missing trace fails closed. [Document validation20](20_TND_OC_B10_R3_DOCUMENT_VALIDATION_20261109.json) records preservation, links and size checks. The future E13 r2 evaluator has its own frozen Request29; it has not run here.

9 November 2026. Prepared for Edward Baker with substantial OpenAI Codex assistance, OC chat0011; recorded thread gpt-6-astra/max, per-turn backend configuration unavailable.

## E13 r1 replay

9 November 2026. Prepared for Edward Baker with OpenAI Codex assistance,
OC chat0010, recorded GPT-6.1 Sol / ultra. Use the
[execution record](18_TND_OC_E13_R1_EXECUTION_20261109.json) and
[assessment](../reviews/17_TND_OC_E13_R1_PROOF_AND_IMPLEMENTATION_CHECK_20261109.md).
The actual runtime was Python 3.12.14, python-flint 0.9.0, FLINT 3.6.0,
one FLINT thread. Run from this investigation's root with that isolated
runtime active.

```sh
PYTHONDONTWRITEBYTECODE=1 python numerics/e13_contours.py --self-test
e13_replay_dir=$(mktemp -d /tmp/tnd-oc-e13-replay.XXXXXX)
PYTHONDONTWRITEBYTECODE=1 python numerics/e13_gaussian_pilot.py \
  "$e13_replay_dir/evidence" "$e13_replay_dir/execution.json"
```

The first command runs synthetic polynomial controls only. The second
replays the frozen inputs and the canonical evaluation under an
external 1800-second limit. It writes a new record outside the
repository. The replay is a separate verification run, with its own
record. Read `result.status` to distinguish a certificate from a
structured failed-gate return. The original E13 r1 evidence comes
from one canonical run.

The original large contour log is outside the repository at the
location in the small record. Its ordered JSONL records carry the exact
dyadic edges, subdivision and fragment links, winding enclosures,
moment segment allowances, centroid enclosures and exact dyadic
centroids. Decimal ball displays aid inspection. Replay uses the exact
geometry and recomputes the outward balls. The stored and canonical
content hashes identify the original log. Differences across environments
or timing limits are assessed by replaying the arithmetic gates.
[Source-use15](../references/15_TND_OC_E13_FLINT_SOURCE_USE_20261109.md)
records the version-pinned library chain.

**B10 r2 records.** [Exact constants16](16_TND_OC_B10_R2_EXACT_CONSTANTS_20261109.json)
and [its replay](check_b10_r2_cluster_constants.py) verify rational error
comparisons; [validation17](17_TND_OC_B10_R2_DOCUMENT_VALIDATION_20261109.json)
checks documents and preservation. These records cover the design-stage constants and preservation checks.
9 November 2026. Prepared for Edward Baker with substantial OpenAI Codex assistance, OC chat0009. Recorded current thread settings gpt-6-astra/max; per-turn backend configuration unavailable. Earlier dated routing below is historical.

**B10 r1 document record.** [Validation15](15_TND_OC_B10_R1_DOCUMENT_VALIDATION_20261109.json)
records source hashes and navigation/status checks. It contains no
canonical numerical evaluation or interval certificate. 9 November 2026. Prepared for Edward Baker with substantial OpenAI Codex assistance, OC chat0009. Recorded current thread settings gpt-6-astra/max; per-turn backend configuration unavailable.

**Current — 8 November 2026, B09.** For Edward Baker with OpenAI Codex assistance; actual model/effort unavailable.
[Validation14](14_TND_OC_B09_HANDOFF_VALIDATION_20261108.json) records
source preservation, local links, file sizes and handoff consistency.
These are documentation checks; no mathematical numerical experiment,
canonical profile acquisition or collision-certificate replay occurred.
Earlier routing below is historical.

**Current correction — 8 November 2026, TND-OC-E11.** For Edward Baker
with OpenAI Codex assistance; actual model/effort unavailable, OC chat0006.
[E11 validation13](13_TND_OC_E11_DESTINATION_CORRECTION_VALIDATION_20261108.json): File/link/ownership checks only; no canonical numerical experiment.
[Progress02](../research-progress/02_TND_OC_MARGINAL_PRIORITIES_RESEARCH_PROGRESS_20261108.md)
is the sole live register; earlier dated routing below is historical.

**8 November 2026 — B08 complete.** For Edward Baker with substantial OpenAI Codex assistance; actual model/effort unavailable.

- [B08 validation12](12_TND_OC_B08_SESSION_VALIDATION_20261108.json): protected-input, link, size and setup checks only; no canonical computation.

Earlier dated entries below are historical; the sole register owns live status.

**8 November 2026 — B07:** [validation11](11_TND_OC_B07_SESSION_VALIDATION_20261108.json) records file/input preservation, local links, sizes and authentic-history metadata. B07 performed no canonical numerical evaluation or evaluator implementation. E09 owns the fixed pilot and actual numerical evidence. For Edward Baker with substantial OpenAI Codex assistance, chat0006; actual model/effort unavailable. Earlier routing below is historical.

**8 November 2026 — E08:** [validation10](10_TND_OC_E08_SESSION_VALIDATION_20261108.json) records input hashes, preservation, links and sizes. Analytical assessment only; no mathematical numerical experiment or canonical moment evaluation. For Edward Baker with OpenAI Codex assistance, chat0007; actual model/effort unavailable.

**8 November 2026 — B06:** [validation09](09_TND_OC_B06_SESSION_VALIDATION_20261108.json) records frozen-source, file, link and authentic-history checks only. No mathematical numerical experiment, canonical moment evaluation or collision-certificate replay occurred. New estimates are analytical, with proof-author checking only. For Edward Baker with OpenAI Codex assistance; actual model/effort unavailable, chat0006.

# numerics

**8 November 2026, E06 supporting checks:** [exact record07](07_TND_OC_E06_EXACT_BOOKKEEPING_20261108.json), [check script](check_e06_gaussian_bookkeeping.py), and [validation08](08_TND_OC_E06_MANUSCRIPT_VALIDATION_20261108.json) record weighted factorial normalization, self subtraction, support constants and manuscript production. No canonical-zero evaluation or analytic proof certificate. For Edward Baker with substantial OpenAI Codex assistance; actual model/effort unavailable.

**E05 manuscript, 8 November 2026:** [bookkeeping replay05](05_TND_OC_E05_BOOKKEEPING_REPLAY_20261108.json)
reuses B04's exact finite check, and [validation06](06_TND_OC_E05_MANUSCRIPT_VALIDATION_20261108.json)
records frozen inputs, local links and source-size checks. The manuscript
[build record](../manuscript/BUILD_RECORD.json) records the reading PDF.
Supporting evidence only; no canonical statistic was evaluated.
For Edward Baker with OpenAI Codex assistance; actual model/effort
unavailable, chat0003.

**B04, 8 November 2026:** [exact bookkeeping](check_b04_pair_bookkeeping.py),
[execution03](03_TND_OC_B04_EXACT_BOOKKEEPING_20261108.json) and
[session validation04](04_TND_OC_B04_SESSION_VALIDATION_20261108.json)
record rational folding/constants and file/history checks. No canonical
field or zero was sampled. These are not analytic proof certificates.
Prepared for Edward Baker with substantial OpenAI Codex assistance;
actual recorded model/effort unavailable, chat0003.

Separately authorized finite diagnostics and small code/records; no runs are active. Large derived files remain external.

The sole status owner is this branch's research-progress/02_TND_OC_MARGINAL_PRIORITIES_RESEARCH_PROGRESS_20261108.md. Follow the parent setup and reference workflows.


**B02, 7 November 2026:** [exact check script](check_b02_exact_constants.py)
and [small result](01_TND_OC_B02_EXACT_CONSTANT_CHECK_20261107.json) verify
the radial polynomial control and disk-floor rational constants using
Fraction arithmetic. No canonical field/zero was sampled, no sweep or
optimization was run, and this is not a proof certificate for the analytic
claims. Prepared for Edward Baker with OpenAI Codex assistance; exact
backend model/effort unavailable.

**B03, 8 November 2026:** [session validation](02_TND_OC_B03_SESSION_VALIDATION_20261108.json)
records authentic capture, frozen-input preservation, local-link checks
and exact rational bookkeeping only. It is an administrative/exact-algebra
record, not a canonical numerical experiment or analytic proof certificate.

- [21 — E14 exact bookkeeping](21_TND_OC_E14_EXACT_BOOKKEEPING_20261109.json): inherited cell geometry, exact allowances and input preservation; zero new canonical or projection calls.
- [22 — E14 document validation](22_TND_OC_E14_DOCUMENT_VALIDATION_20261109.json): final source/link/build and frozen-input checks; production evidence only.
