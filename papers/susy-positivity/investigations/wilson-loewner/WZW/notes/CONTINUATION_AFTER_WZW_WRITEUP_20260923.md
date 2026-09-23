# Continuation after the standalone WZW write-up

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Status:** editorial integration and research handoff, not a new analytical result or numerical run. Independent specialist review remains outstanding.

## Current state

The [standalone manuscript](../manuscript.pdf) and [editable source](../manuscript.tex) now collect the completed WZW pilot and the direct arithmetic-source investigation. This folder was created at the author's request to keep the parent Wilson--Loewner manuscript from growing. Its manuscript sources and PDFs are preserved unchanged. Historical research notes and numerical programs remain at their original locations and are linked from [this note index](README.md).

The main distinction to retain is between three norms: the fixed invariant-tensor norm, the transported Chern--Simons gluing norm, and the unweighted arithmetic operator norm. The constant-driver WZW balance concerns the first. The CS channel norm is preserved in a different metric. Neither has yet been identified with the third.

The arithmetic source construction is exact on a safe half-plane. It defines actual generalized Loewner flows from the completed xi logarithmic derivative and includes all prime, gamma and rational terms. It prescribes arithmetic data to the geometry. A physical derivation of the arithmetic transfer and its norm remains open.

## Next bounded calculation

Work toward a cumulative boundary or canonical response for the arithmetic transfer `K_omega` or its Cayley transform `Z_omega`, starting from the complete source on a safe line. Specify the Hilbert space, input and output maps, identity initial operator, and physical or canonical pairing before asserting contraction.

1. On a window shorter than `log 2`, calculate the complete local, gamma and rational response. Show how the proposed operator has the strong identity limit.
2. When the window crosses `log 2`, recover the generator's first prime-delay coefficient, `-sqrt(2) log(2) cosh(omega log(2))`, with control of every additional boundary or storage term.
3. Derive a cumulative norm balance that permits the already established negative instantaneous generator example. Quantify the cost of removing a safe spectral weight; the current bound is only `||V_(omega,L)|| <= exp(b L)` for `b >= Omega + 1/2`.

Success at these tests would constitute operator-level progress. It would not by itself provide continuation to all lengths and vanishing shift. State any remaining uniformity estimates explicitly.

## Constraints already established

- The raw WZW four-point kernel has a Hilbert--Schmidt initial limit, so this specific smearing does not initialize as the identity on an infinite-dimensional `L2` space.
- Moving Loewner drivers can increase the selected WZW tensor norm. An additional compensating scalar has not been derived from the chosen physical observable.
- A safe positive-real xi source does not automatically continue to zero shift. Whole-half-plane positivity at zero is RH-equivalent.
- The arithmetic logarithmic generator is not a holomorphic positive-real Loewner driver on the full right half-plane, even under RH. Its poles cancel only after multiplication by the transfer.
- Spectral translation, arithmetic shift, generalized Loewner time, boundary capacity, and canonical-system depth have no established common clock.

The explicit canonical-system construction cited from Suzuki has arithmetic shift greater than one; do not confuse it with unconditional innerness at shifts at least one-half, or with the separate source translation. The modular-surface half-shift endpoint is already known in the parent project and does not furnish a continuous smaller-shift family.

## When to resume the physical sewing extension

The concrete WZW question remains the actual slit-sewing map on the boundary affine module `H_(0,1/2)=V_(1/2)`, retaining descendants and the specified endpoint normalization. Its primary matrix elements must recover the completed pilot, and its reflected gluing form must explain the relation to the tensor identity. Prioritize this extension when there is a specified operator readout to compare with the arithmetic source, rather than expanding the finite block calculation alone.

## Preservation and validation

The 72 WZW and 60 arithmetic-source controls are the existing recorded runs of 22 September. The write-up does not add cases or replace those records. See [BUILD.md](../BUILD.md), [the manuscript audit](../reviews/review_codex_manuscript_20260923.md), and [the milestone index](../DRAFT_HISTOR.md). New research notes go in this folder, numerical work in `WZW/numerics` when required, and reviews in `WZW/reviews`.
