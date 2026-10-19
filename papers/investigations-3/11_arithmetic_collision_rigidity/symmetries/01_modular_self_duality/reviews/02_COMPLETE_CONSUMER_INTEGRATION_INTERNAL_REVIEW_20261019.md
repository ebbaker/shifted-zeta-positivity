# Internal review: S01 paired-tail integration in the complete signed consumer

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewer **gpt-6.1-sol (Codex), actual reasoning effort ultra**, inherited from the parent session. A separate delegated reader performed this review and one fresh 192-bit replay. This is internal same-model LLM review, not independent specialist review.

**Assessment: the S01-T1 deliverable and its decision gate pass as reusable integration and regression validation. There is no additional paid-margin, cost or coverage milestone. Stop further tuning of this omitted-mode tail on B.**

## Scope and inspected sources

The reviewer read the repository instructions, result-summary and avoid indexes, the S01 paired-endpoint note and checker, the original high-height evaluator and its real-source comparator, the INT-01 contract, the integration implementation, and the fresh source-specific control implementation and record. The relevant guidance is [collision screening](../../../../../../result-summaries/12_collision_controls_and_screening.md), [preserving cancellation](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [scoped conclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [status matching evidence](../../../../../../avoid/06_status_stronger_than_the_evidence.md).

The inspected implementation was `integrate_paired_tail_consumer.py`, SHA256 `f6b89d07cbf1f6fb7fbdbe0a491545a86c5ecabf9320bccf6285db53c7c1158f`. The INT-01 contract SHA256 was `621e66fd54c12dd5004f02800c041f39bccc6b585fedf8447882d8fce4647548`. The final file locations may differ from the external review staging paths; byte identities are the review pins.

## Integration and complete-budget checks

The reusable `install_paired_tail` interface accepts the fixed real B rectangle `[1/100,1/5] x [999,1001]`, midpoint `(21/200,1000)`, modes 1–11, source cutoff U=2, contour d=pi/8-4 log(1000)/1000, and degrees (24,12). It checks the actual contour enclosure, pi, sin(4d), cos(4d), normalization factor, retained mode list, and arithmetic precision. The existing theorem implementation freshly verifies its phase gap, open source strip, amplitude conditions, signed endpoint allowance and infinite series payment. Only the uniform order-0..2 omitted-mode vector is replaced; the retained-source vector is preserved.

The producer acquires one fresh midpoint setup at each precision. Within a run both consumers share identical exact dyadic midpoint coefficients and quadrature radii. The fingerprint retains those data, the retained-source tail, finite-integral majorant, high-order physical tails and full-H majorant. The original evaluator file is unchanged. Consumer evaluation therefore changes only the intended final physical-tail payment. In particular, the finite-integral Taylor polynomial is never propagated as though it already contained the omitted physical modes.

The whole-box ledger verifies unchanged quadrature, Taylor and retained-source payments, and strictly smaller complete added-error allowances at physical orders 0,1,2. The inherited ratios are approximately 0.8515359468, 0.9278097155 and 0.9700791487. This confirms the opening result in the actual consumer; it does not count that inherited error decrease as a new mathematical milestone.

The adapter does not license another source or domain: the object must carry the genuine complete-theta setup. The wrapper's source pins and fresh construction provide that premise in the executed comparison. The B-only allowance must be recomputed before a different rectangle or complex-wall consumer is considered. The recorded complex tail theorem is not a complete complex-wall comparison, particularly since the old wall includes t=0 and the B allowance uses t>=1/100.

## Independent execution and controls

The reviewer freshly ran the final integration implementation at 192 bits with python-flint 0.9.0. All 40 accepted signed excess intervals were identical between the two policies, and the minimum was identical:

`[8.2608772276838260495687738894918600e-5 +/- 1e-43] Gc^2`.

The four-slab geometry, 40 accepted cells and 116 total consumer calls were unchanged. Thus no resolved paid-margin or work-count gain exists in this consumer. The finite positive margins revalidate existing-box exclusion; they provide no new coverage. The comparison does not assert equality of the underlying true errors or between-precision quadrature results. Arb image-radius rounding can absorb an improvement much smaller than the cell's interval width; the reported identical intervals suffice for the stopping decision without attributing an exact mechanism to every rounded operation.

Additional bounded challenges rejected changed normalization, cosine/sine contour factors, a changed retained mode, a widened contour enclosure, changed U and m, changed arithmetic precision, and a second installation over an already replaced baseline vector. These challenges used the historical exact midpoint cache solely to exercise guards, without asserting that its old manuscript pins match the current manuscript. The actual research replay used fresh data.

The fresh control record applies the unchanged `signed_cell` acceptance expression to source-specific jet balls: five event-containing domains fail the strict gate, and the separate Euler p=41 negative-Laguerre witness is strictly negative. No theta tail or quadrature constants are used for these controls. The five invalid tail parameter cases and non-even-source vertical-boundary fixture through order two pass their rejection checks. The control implementation correctly distinguishes these acceptance challenges from proofs of the tail theorem. Finite-prime and smooth positive-primitive families retain their analytic premise screens because no effective event box is supplied here.

## Comparator and classification

The INT-01 normalization table is correct, including the lower-triangular derivative terms required to convert physical jets to Q jets. The fixed Gc is never differentiated; a varying normalizer cannot be treated as one scalar factor for all derivative orders. Phase-coordinate norm preservation is qualified to real phase.

The established 768-bit real-source representation has complete component error below 2.165e-12 Gc, stronger than the paired shifted value near 3.935e-12 Gc. It uses a different polynomial and precision; the contract retains it as a stronger contextual accuracy reference rather than hiding it or mixing it into the exact same-polynomial ablation. The existing correlated correction and stronger S03 direct consumer likewise remain separate and unbeaten.

Classification: **interval regression validation of an existing proved tail estimate, with a reusable implementation**. S01-T1 can be Complete because the stated integration deliverable exists and its stopping gate has been assessed. The result neither supplies a new retained-core signed estimate nor establishes a general obstruction to other arithmetic or contour methods. EXT-01 stays conditional; the real bridge and complex exterior remain open.

## Review evidence identities

- Independent fresh replay: [S01_CONSUMER_REVIEW_REPLAY_192_20261019.json](../numerics/S01_CONSUMER_REVIEW_REPLAY_192_20261019.json), SHA256 `47d5996fa2d4b3099737c8a5d0d5fbeb999cdb674c3944c1a03f16dbcefff5f0`.
- Interface challenges: [S01_CONSUMER_INTERFACE_GUARDS_20261019.json](../numerics/S01_CONSUMER_INTERFACE_GUARDS_20261019.json), SHA256 `c4d947223f1cbb15706d3188d6cc4da220dff0ca439391dde77ae8e2cdc07028`.
- Source-specific controls inspected: `S01_CONSUMER_CONTROLS_20261019.json`, SHA256 `b8e3180c4c74bbeb5d565edd009928a8bd655eff233955e17be8899741ed5530`.

Hashes identify inspected bytes; they do not certify the mathematics.
