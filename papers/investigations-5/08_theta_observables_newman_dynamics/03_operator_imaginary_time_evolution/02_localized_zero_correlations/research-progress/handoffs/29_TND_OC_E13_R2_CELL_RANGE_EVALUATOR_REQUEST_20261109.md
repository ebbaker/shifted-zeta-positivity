# TND-OC-E13 r2: fixed cell-range projection evaluator

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, OC chat0011. Recorded issuing-thread
settings `gpt-6-astra / max`; per-turn backend configuration unavailable.

**Type E — execution. Recommended model: GPT-6.1 Sol**, effort chosen by
Edward Baker. Parent: B10 r3. Status: issued, ready, **unactivated**.
The conceptual method and acceptance conditions are fixed in
[Note22][note]. [Progress02][progress] alone owns live status.
This revision changes the evaluation method; Request27 r1 and its
source-call failure remain immutable historical evidence.

## Objective and inputs

Produce a certified interval of radius strictly below 1/200 for exactly
Note19's \(P_{1000}\), or return the first exact failed gate. Use the
complete E13 census and Note22 (5)–(7) endpoint ranges. Retain uniform
centers [1000,2000], h=ell=1, blur epsilon=1/4, both ordered marks,
finite center edges, every pair and the complete omitted tail 2^-32.
This is a finite projected canonical value, not the full pair function
or a collision constraint.

Before substantive work, verify [Inputs29][inputs]. Mathematical/evidence
hash drift fails closed; policy and navigation drift must be inspected
and reported separately. Use the existing python-flint 0.9.0 / FLINT 3.6.0
isolated environment if available, recording the actual runtime. A
different version requires the relevant endpoint API/source check;
an unsupported environment is a named failure, not permission to use
floating arithmetic. No new source/centroid acquisition is authorized.

Required evidence chain:

1. Return27 hash, its exact 388 dyadic cells, execution18 hash, the two
   recorded E13 code hashes, Note21 and assessment17.
2. External E13 `contours.jsonl`: 221,300,387 bytes; stored and canonical
   JSONL hashes both
   `86484de4a0b50cc3230ced7a178b8cd20f027b69602c2dd222c1787b40c2644a`.
   Its original location is recorded in execution18. An explicitly
   supplied relocated path is allowed only with both identical hashes.
3. Run [the source-free geometry/tree check][checker] on that trace.
   Compare all leaves with Return27, outer/child count identities, exact
   partitions, singleton counts, widths, and separation >1/2. Its six
   malformed-census controls must be rejected.

The import retains E13's assessed outward-winding premise. Neither the
hash nor a reparse of decimal source-ball displays establishes fresh
nonvanishing. The source-free checker replays geometry and count
structure, not the library's zeta evaluations. Report that inherited
scope explicitly. Missing evidence must stop r2; do not silently replace
it by approximate roots, the 91 centroids, known realness or a fresh
source campaign. A separately requested source replay is outside r2.

## Fixed proof obligations

Check these once before the canonical endpoint pass, with one bounded
implementation/normalization repair only if the unchanged theorem and
all limits survive:

| ID | Required check |
| --- | --- |
| R1 | Exact census widths u=5/32768, v=15/131072 and adjacent separation 5085/8192>1/2 imply index-k separation >k/2 for arbitrary points in the cells. |
| R2 | Note22 (5)–(7) enclose the full ordered cell products; both erf edges and both mark orders remain. Rational distances give the mark extrema. |
| R3 | Note22 (8)–(10) bound ideal geometric radius by 1261/409600, including the two-erf dependency loss and all distant pairs. This bound is restricted to the acquired singleton separated census. |
| R4 | Cross-cell coefficient n_C n_E and same-cell coefficient n_C(n_C-1) preserve all labels. Generic same-cell inclusion uses K on C×C, not only K(z,z). Current same-cell coefficients vanish because all certified counts equal one. |
| R5 | The point-endpoint arithmetic gate r_L+r_U≤1/1000 plus the complete tail gives the exact rational cap 2189688957/536870912000<41/10000<1/200. Final interval endpoints and the actual radius are independently checked after exact serialization/reparse. |
| R6 | Input hashes, arithmetic semantics, negative controls, elapsed-work counters and first-failure behavior are correct; no claim of a fresh winding audit or measured historical saving is made. |

A mathematical change beyond this fixed proof is a B10 r4 decision.
Do not replace a failed quantitative gate by a statement that the target
is known positive or that low-height zeros are known real.

## Fixed computation

Sort the 388 cells by exact x lower endpoint. Cache each cell's four
scalar mark endpoints from Note22 (6), with their outward balls.
For each of the 75,078 unordered pairs:

1. Form exact M and positive D endpoints.
2. Evaluate four scalar erf values for A_-,A_+, then the clipped
   I_-=max(0,A_-), I_+=min(2/T,A_+).
3. Evaluate the two scalar gap exponentials at the D endpoints.
4. Form both ordered mark products and sum them as H^- and H^+.
5. Add the lower and upper point expressions separately with outward
   arithmetic. Use the exact coefficient c_G=32 sqrt(2)/51.

Every rational and transcendental constant must be enclosed. For a
ball [a,b], a monotone clipping map is enclosed by its endpoint images;
construct the resulting ball outward. Never select the sign of an
uncertain point from its midpoint. Keep the total endpoint expressions
as enclosing balls \(\mathcal L,\mathcal U\); their radii measure
arithmetic uncertainty, not cell-location uncertainty.

After each full pass, measure r_L+r_U exactly and require ≤1/1000.
Take exact dyadic a=inf L and b=sup U; require a≤b. Return
[a-2^-32,b+2^-32]. Test its actual rational half-width strictly below
1/200. Also report the geometric cap and every separate payment.
Serialize both balls using exact dyadic midpoint/radius data, with
exact final endpoint rationals and optional human-readable decimals.
Reload the saved record and repeat the gates. A canonical interval
must not be claimed on overlap, a rounded decimal, or a sampled test.

Use all pairs, even when exponentially small. No truncation, centroid
interpolation, source calls, root refinement, y=0 replacement, observation
change, different center law or missing-tail waiver is permitted.
Deterministic summation order, exact caching of identical arguments,
bounded memory management and API-compatible rounding fixes are routine
implementation choices. Any optimization must preserve (5)–(7).

## Fixed controls and limits

Before the canonical pass, run one finite control batch (at most 32
fixtures and at most 10,000 exp/erf calls, included in the total below).
Use rigorous containment against a direct ordered point sum, not merely
overlapping intervals. A reference ball wholly inside the produced cell
interval proves the comparison; insufficient reference precision is a
failed check until repaired within the same bounds.

- Empty and singleton configurations: exact zero factorial sum.
- A double real point and a double nonreal point: retain 2K(a,a).
- Two distinct points in a common cell, once with a real split and once
  an imaginary split: retain their ordered K values through C×C.
- Unequal marks, for example 1/4 and -1/8, on points near each center
  edge: direct ordered summation must agree with both mark orders.
  Verify the analytic order ratio exp[(16/17)(y-y')].
- Nonzero cell widths: verify point-sum enclosure for exact dyadic
  selections at corners and an interior point. These are software
  controls; Note22 supplies the universal cell inclusion proof.
- Reject corrupted input bytes, noninteger counts, missing/duplicate
  cells and geometry violating the frozen census gates. Geometry
  controls in checker19 may be reused, not weakened.
- Reject a synthetic endpoint-radius sum exceeding 1/1000; reject
  exact final radius 1/200 and any nonfinite ball. Inject a missing
  mark order or self term and verify that the relevant control fails.

Canonical precision ladder: **128, 256, 512 bits**, in order, at most
three complete passes, stopping at the first successful pass. The
formula uses 452,020 exp/erf calls per pass before caching, hence
1,356,060 for all three. Hard cumulative cap **1,400,000 exp/erf calls**,
including controls and any repair; count before each call. Record pi
and square-root evaluations separately, capped at 100 in total.
**Zero canonical source calls, zero moment/centroid calls.**

Use **one worker** and an external **600-second cumulative elapsed
ceiling** from evaluator input validation through trace inspection,
controls and endpoint passes. The supervisor must be able to stop a
long library call and preserve the counters/last completed stage. Code
authoring and environment setup are outside this evaluator clock and
must be reported separately if measured. At most one bounded repair;
all attempts share the same elapsed, call and three-pass limits. No
restarting the ledger after a failure. Do not run the r1 acquisition.

Success: passed inputs/R1–R6/controls, paid arithmetic and final width,
exact reload verification, saved source-bound return. Failure: retain
the first failed gate and actual ledger, any completed interval data,
and its precise scope. Changed method, inputs, target, caps or proof
premise needs **[B] TND-OC-B10 r4 / Astra**, only when specifically
motivated by the returned failure. A result of either kind completes
this E task; it does not automatically activate a successor.

## Files and return

Implement a new r2 evaluator in this investigation's `numerics/`, reuse
the exact geometry checker, and retain small execution/test records.
Write the research result in `notes/`, proof/implementation assessment
in `reviews/`, and a revision-labelled return in `research-progress/handoffs/`.
Update Progress02, concise navigation/history and a model-change
continuation. Preserve r1 code, its immutable request/inputs/return and
all original source evidence. No manuscript or sibling edits.

Keep generated large evidence outside the repository and record exact
locations, sizes and both hashes as required by LARGE_FILES.md. A scalar
result and fixed per-pass summaries should be small; no large pairwise
table is required. Record actual author/date, LLM assistance, available
model/effort metadata, runtime versions, input digests, proof/controls,
all error allowances, call counts, elapsed time, repairs and disposition.
Refresh authentic chat history and arrange its exact-turn final capture.

[note]: ../../notes/22_TND_OC_B10_R3_CELL_RANGES_AND_GAUSSIAN_WIDTH_20261109.md
[inputs]: 29_TND_OC_E13_R2_INPUTS_20261109.json
[progress]: ../02_TND_OC_MARGINAL_PRIORITIES_RESEARCH_PROGRESS_20261108.md
[checker]: ../../numerics/check_b10_r3_cell_geometry.py
