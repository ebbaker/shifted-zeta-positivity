# Tensor approximation and coefficient bounds

14 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance. Coordinator backend/effort unavailable; B workers explicitly dispatched **gpt-6-astra / ultra**, E proof/assessment workers **gpt-6.1-sol / ultra**. Dispatch metadata is distinct from backend attestation.

## Summary

Investigation 6's first bounded round gives quantified approximation results for the complete theta source, retaining \(H=\frac12\int W e^{izu}\,du\).

- **Coefficients:** \(\beta_n+\beta_{n+1}\le\operatorname{arcosh}^2(2n+12)/16\), all integer \(n\ge0\), uniformly \(0\le\lambda\le1/2\). Integration by parts and a convex exponential confinement bound prove the estimate from the complete source. Positive weighted-square collision controls can also satisfy it.
- **Finite chain:** the normalized scalar error is at most \(h_N^*\sum_{k=0}^N\tau^kx^{2N-2k}/[k!(2N-2k)!]\). Combining the coefficient envelope gives error at most \(H_{1/2}(0)\varepsilon\) on \(0\le\tau\le1/2, |x|\le X\), for \(N=\lceil4K\log(16K)\rceil\), \(K=X+\log(1/\varepsilon)+1\), \(0<\varepsilon\le1\). This is a sufficient depth, not optimal or measured cost.
- **QTT:** an exact-coefficient polynomial construction has formal rank at most 641 and scaled error below \(2^{-36}\) on its fixed height/offset box. Direct integration of the same polynomial removes the midpoint allowance.
- **Exact cell phase:** weighted source projection and exact sinc readout give absolute error below \(5\cdot10^{-7}\) at \(U=2,L=30\), for every real height, \(|\Im z|\le8\) and allowed time. The fixed center-phase lattice has actual all-real-height error at least \(Z_\lambda/2\).

## Status

Source status: **proved in-note**. Separate same-worker internal assessments accept the fixed bounds without correction. Shared-source checking does not supply independent specialist review. No numerical campaign or interval certificate was produced. The [shared proof](../papers/investigations-6/notes/03_TN6_E01_COEFFICIENT_TO_SCALAR_TRANSFER_20261113.md) states: “Actual state-prefix error and a speed advantage remain unestablished.”

## Caveats

The chain is exactly Gaussian quadrature; its finite coefficients and certified evaluation are unpaid. QTT's source coefficients and ITP's \(2^{32}\) formal masses are exact mathematical inputs, not acquired data. These absolute allowances provide neither relative accuracy at zeros nor a signed-field result. The lattice obstruction is restricted to fixed point-phase cells in a uniform all-height norm. See [controls 12](12_collision_controls_and_screening.md).

## Reusable for

Explicit finite-chain remainder/depth estimates; a full-time coefficient envelope; complete-source approximation error ledgers; separation of phase integration from point-phase aliasing. A new acquisition or signed consumer needs its own bounded contract.

## Where

The [roundup](../papers/investigations-6/notes/04_FIRST_RESEARCH_ROUND_RESULTS_20261114.md) links all four proofs, frozen requests and assessments. The [shared assessment](../papers/investigations-6/reviews/01_TN6_E01_TRANSFER_ASSESSMENT_20261113.md) covers composition. The [continuation](../papers/investigations-6/notes/05_RESEARCH_CONTINUATION_AND_MODEL_HANDOFF_20261114.md) proposes a bounded coefficient-acquisition decision; it does not activate a new campaign.


## Finite acquisition update — 14 November 2026

For Edward Baker with OpenAI Codex assistance; B02 dispatched Astra/Ultra,
E02 and its separate internal E03 assessment Sol 6.1/Ultra; coordinator
backend/effort unavailable. The earlier statements that no interval
certificate exists and coefficient acquisition is unpaid are **superseded
only for the following finite tuple**.

[E02](../papers/investigations-6/notes/06_TN6_E02_CERTIFIED_COEFFICIENT_ACQUISITION_20261114.md)
records “certified within the frozen execution scope”: N=16, seventeen
complete-source even moments and sixteen positive coupling enclosures.
At 256 bits, the ideal nominal scalar has normalized absolute error
below 1.515e-25 on 0<=tau<=1/2, |x|<=8, in units of H_(1/2)(0). Nine
computed readouts meet that bound with rounding included. The 128-bit
coefficient-width gate failed and is preserved. [E03](../papers/investigations-6/reviews/02_TN6_E03_ACQUISITION_ASSESSMENT_20261114.md)
states “Accepted as a finite certificate at the issued scope.” Its one
unchanged replay matched the scientific payload; this remains internal
same-model, shared-premise review.

The chain's instrumented setup plus nine readouts took 1.288 s versus 0.535 s
for direct integration on the original run; achieved radii differ and no
speed law follows. This supplies reusable finite inputs and absolute
readouts, not signed, relative-error or increasing-height conclusions.
See the [roundup](../papers/investigations-6/notes/07_TN6_FINITE_ACQUISITION_ROUND_RESULTS_20261114.md)
and [current continuation](../papers/investigations-6/notes/08_TN6_CONTINUATION_AND_MODEL_HANDOFF_20261114.md).
The [editorial receipt](../papers/investigations-6/numerics/12_TN6_POST_ACQUISITION_GUIDANCE_UPDATE_20261114.json)
and [staging helper](../papers/investigations-6/numerics/prepare_tn6_e02_replay.py)
restore the exact pinned pre-update guidance for replay without changing
scientific inputs or their guards.


## Analytical manuscripts — 14 November 2026

For Edward Baker with OpenAI Codex assistance; manuscript and internal
review workers dispatched Sol 6.1/Ultra, coordinator backend/effort
unavailable. The [four-draft index](../papers/investigations-6/notes/09_ANALYTICAL_MANUSCRIPT_SCOPE_AND_RESULT_MAP_20261114.md)
now gives systematic derivations from the complete source through each
branch's quantitative results, ending with outstanding challenges.
The [cross-review](../papers/investigations-6/reviews/03_TN6_ANALYTICAL_MANUSCRIPT_CROSS_REVIEW_20261114.md)
states: “Accepted as analytical drafts within stated scope.” This is
internal shared-model review with JCH contributor overlap. It preserves
the earlier proofs' status; manuscript integration adds no new numerical
certificate or signed-field conclusion. The [current handoff](../papers/investigations-6/notes/10_ANALYTICAL_MANUSCRIPTS_CONTINUATION_AND_MODEL_HANDOFF_20261114.md)
prioritizes an analytical improvement with a named consumer. All PDFs
are external; editable TeX and small source/build records remain in-tree.
