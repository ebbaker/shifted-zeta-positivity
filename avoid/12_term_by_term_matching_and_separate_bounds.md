# Term-by-term matching, separate absolute bounds, separately positive sectors, dropped small terms

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

Sonin working-draft evidence added 17 October 2026 for Edward Baker with
substantial LLM assistance, **gpt-6.1-sol (Codex)**, effort **ultra**.

## The pattern

The target is a small difference of large quantities. An argument matches
the large quantities one at a time, bounds each sector in absolute value,
splits a sum into pieces and asks each piece to be positive, or discards a
term that looks small. Each step is natural and each loses the
cancellation that the target lives on; the result is a bound that is
"doubly exponential" where the truth is \(10^{-28}\), a divergent series
where the paired difference converges, or a sign that is wrong by a term
that "cannot be discarded".

## What it looks like here

Channel-matching programs; separate Möbius and Poisson sectors at
positive heat time; independent positivity of two lattice cosets;
separated complement floors; a Gram tail omitted from a lower bound.

## Evidence

- [Inverse-bulk review](../papers/weil-positivity/susy-positivity/investigations/previous/inverse-bulk-realization/reviews/review_claude_opus_5_20260915.md): "Matching the terms one at a time is matching quantities five to seven orders of magnitude larger than the answer."; the [source-selection continuation](../papers/weil-positivity/susy-positivity/investigations/previous/source-selection-rules/notes/CONTINUATION_20260916.md) calls double-precision term-by-term assembly "the one that cost the most time".
- [Program meta-analysis](../papers/investigations/program-meta-analysis/reviews/PROGRAM_META_ANALYSIS_20260926.md) §4.5: "It pays for large terms independently even where the actual form is extremely small." (the \(L\exp(c\,e^{L/2})\) cutoff, the doubly exponential ranks).
- [09-to-06 review](../papers/investigations-2/brainstorm/reviews/RANK_TWO_TO_PAIRED_KERNEL_REVIEW_CODEX_20261013.md): "The two lattice cosets cannot be treated as independently positive Fourier channels."
- [22 manuscript §12](../papers/investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex) and the [dilation note](../papers/investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/11_MULTIPLICATIVE_DILATION_AND_COMPLETE_HEAT_PACKETS_20261015.md): at every positive heat time the separated Möbius series "fail even the term test" while their paired difference converges rapidly.
- [Storage-depth barrier note](../papers/weil-positivity/shifted-zeta/storage-depth/archive/reviews/NOTE_barrier_theorem_and_ladder_conjecture_20260911.md): with separated complement floors "there is nothing left to gain from sharper arithmetic norm bounds".
- [Finite-response assessment](../papers/weil-positivity/susy-positivity/manuscripts/finite-response-weil-positivity/reviews/assessment_claude_current_draft_20260914.md) §3.2: "Omitting a positive Gram tail destroys the lower-bound property."; [positive-factorizations round-4 review](../papers/weil-positivity/susy-positivity/investigations/previous/positive-factorizations/archive/progress-reports/REVIEW_round4_20260911.md): "Thus these small-looking terms cannot be discarded when designing an even completion."; [open directions](../papers/weil-positivity/susy-positivity/investigations/previous/source-selection-rules/notes/OPEN_DIRECTIONS_20260916.md) §E: a missing \(\psi'\) tail shifts every value by 0.0125.

- [Sonin mixed-prime Note 02, §3](../papers/investigations-3/04_sonin_mixed_prime_response/notes/round-1/02_CORRECTED_SIGNED_WEIL_GRAM_AND_MIXED_SOURCE_ESTIMATES_CODEX_20261017.md): the gamma term “is a principal part of the correction”. The [working manuscript](../papers/investigations-3/04_sonin_mixed_prime_response/manuscript/sonin_mixed_prime_response.tex) records the derivation, accepted in the [Claude cross-model review](../papers/investigations-3/04_sonin_mixed_prime_response/reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md): for the stated prepared class with support length greater than the prime-ratio shift, the isolated metric correction has both unbounded signs while the complete mixed source form is compact. Keep the complete cancellation before estimating sectors.

- [Positive arithmetic packets, Note 04](../papers/investigations-3/11_arithmetic_collision_rigidity/notes/04_POSITIVE_ARITHMETIC_PACKETS_AND_MODULAR_CANCELLATION_CODEX_20261018.md):
  "An accurate relative approximation to the positive arithmetic tail is not
  a relative approximation to the vanishing physical field." Despite a
  uniform relative {2,3} remainder below 7.3e-25, omitting that positive
  remainder leaves an eventually negative inverse-square tail instead of
  full modular cancellation. This concerns the stated fixed finite-prime
  truncation. Added 18 October 2026 for Edward Baker with substantial LLM
  assistance, **gpt-6-astra, max**;
  [same-assistant review](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/02_POSITIVE_PACKET_AND_MODULAR_CANCELLATION_SELF_REVIEW_CODEX_20261018.md). The
  [working manuscript, Section 4](../papers/investigations-3/11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/04_modular_collisions.tex)
  gives the complete proof and states: “The identity alone does not reduce
  the strength of the missing estimate.” [Manuscript self-review](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/03_MANUSCRIPT_SELF_REVIEW_CODEX_20261018.md),
  18 October 2026, **gpt-6-astra, max**.

- [Revised arithmetic-packet manuscript, Section 7](../papers/investigations-3/11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/06_certification.tex):
  “Neither is a lower bound for the complete oscillatory field.” The shifted
  approximation preserves complete reflection before truncation, but its
  tail and envelope estimates still require a positive physical margin.
  [Integration review](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/05_UPDATED_MANUSCRIPT_INTEGRATION_REVIEW_CODEX_20261018.md), 18 October 2026,
  for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, ultra**
  and **gpt-6-astra, ultra**; internal LLM checks only. This limitation
  concerns the estimates proved here, not all contour or modular methods.

## What it cost

The channel-matching program (excluded by the two-channel theorem); the
rank-two coset route; the fixed-\(L\) CCM enlargement; several weeks of
double-precision assembly before an exact formulation replaced it.

## Instead

Keep the pairing that cancels and estimate the pair ([Response 17](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/17_RESPONSE_TO_JOINT_REVIEW_CLAUDE_20261015.md) item 3 of its bounded test: "retain cancellations before taking absolute values"); when a sector must be bounded alone, check first on a control that the sector's sign is not the whole problem; never drop a term without an explicit bound on it in the record; and prefer exact formulations (the Schur localization, the finite Euler identity) to assembled approximations.
