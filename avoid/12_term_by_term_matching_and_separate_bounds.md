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

- [S03 correlated residual Note 02](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/02_CORRELATED_ARITHMETIC_RESIDUAL_AND_PAID_TRANSPORT_20261018.md):
  “Subtract the complete approximation at the coefficient level, before
  interval evaluation.” A shared physical residual polynomial retains
  cancellation with its second derivative; signed integration then
  lowers the increment allowance to 0.000266448 against 0.002011747
  for independent endpoints from the same source data. Comparing only
  with the old 0.827470 disk payment would conflate new source accuracy
  with correlation. [Internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/02_CORRELATED_RESIDUAL_INTERNAL_REVIEW_20261018.md).
  Added 18 October 2026 for Edward Baker with substantial LLM assistance,
  **gpt-6.1-sol, actual effort ultra**; finite pilot only.

- [S04 full-cutoff scaling Note 01](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md):
  “Neither can be discarded uniformly.” At n comparable to the growing
  cutoff, the logarithm of the Gaussian amplitude drift is
  kappa^2/(16*t)+o(1), and the heat phase shift tends to pi*kappa/16.
  The fixed-mode power limit therefore fails as a uniform coefficientwise
  replacement, even though the complete phase-retaining scalar has a paid
  exponentially small replacement error. This scopes the failure to that
  coefficientwise approximation; it says nothing about the size or sign of
  the full signed sum. [Internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/reviews/01_FULL_CUTOFF_SCALING_INTERNAL_REVIEW_20261018.md).
  Added 18 October 2026 for Edward Baker with substantial LLM assistance,
  **gpt-6.1-sol, actual effort ultra**; no specialist review.

- [S06 signed transverse Note 02](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/notes/02_SIGNED_TRANSVERSE_ESTIMATE_AND_EXACT_SOURCE_COMPENSATION_20261018.md):
  “The dominant mismatch is the actual lower-endpoint term, not a failed
  tail bound.” The raw positive channel has squared magnitude greater
  than 10^310 E on the pilot. Full source compensation restores a physical
  observation, but the resulting signed current inherits the old physical
  sign. The finite endpoint-subtraction exclusion concerns unbounded
  polynomial-energy magnitude payments, not all compensations.
  [Internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/reviews/02_SIGNED_TRANSVERSE_ESTIMATE_INTERNAL_REVIEW_20261018.md).
  Added 18 October 2026 for Edward Baker with substantial LLM assistance,
  **gpt-6.1-sol, actual effort ultra**.

- [S02 complete-jet Note 03](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/notes/03_COMPLETE_FROZEN_JETS_AND_PAID_CONSUMERS_20261019.md):
  “the same analytic disk residual supplies all three errors.” Independent
  frozen Cauchy boxes certify 1770/4096 signed cells on B; retaining the
  proved real-Schur coefficient class certifies all 4096 without new source
  data. This is an already covered-box result, not global sign control.
  The coherent full consumer and fresh source reference remain stronger
  than frozen. [Separate internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/reviews/03_COMPLETE_JET_INTERNAL_REVIEW_20261019.md).
  Added 19 October 2026 for Edward Baker with substantial LLM assistance,
  **gpt-6.1-sol, ultra**; no specialist review.

- [S03 filtered residual Note 03](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/03_FILTERED_COMPLETE_RESIDUAL_AND_SPLIT_PREFIX_OBSTRUCTION_20261019.md):
  “They must be subtracted before norms.” Separate source/approximation
  prefix triangle payments exceed 1.912087 on B, while the retained signed
  source-informed residual allowance is below 0.000266448. This excludes
  that payment rule, not the signed combined estimator or all transport.
  [Internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/03_FILTERED_RESIDUAL_INTERNAL_REVIEW_20261019.md). Added 19 October 2026 for
  Edward Baker with substantial LLM assistance, **gpt-6.1-sol, ultra**.

- [S03 analytic allowance and kernel-variation Note 04](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/04_PHASE_AWARE_ANALYTIC_ALLOWANCE_AND_KERNEL_VARIATION_OBSTRUCTION_20261019.md):
  “Signed midpoint values cannot cancel that disk.” Even after signed
  source/arithmetic midpoint subtraction, absolute shifted-channel kernel
  derivative payments assign one fixed cell >4037.45136. This excludes that
  variation budget, not signed integration or correlated Taylor models.
  The separate analytic-only phase refinement gives <0.812260;
  source-informed <0.000266448 remains stronger.
  [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/04_PHASE_ALLOWANCE_AND_KERNEL_OBSTRUCTION_INTERNAL_REVIEW_20261019.md). Added 19 October 2026 for Edward Baker with substantial LLM assistance,
  **gpt-6.1-sol, actual effort ultra**; no specialist review.

- [G3 arithmetic Note 06](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/06_ARITHMETIC_GAMMA_AND_EDGE_CORRECTIONS_20261019.md),
  19 October 2026: “C1 alone has the wrong sign” The actual gamma-prefactor correction and
  C1 have opposite signs at the center; finite-mode/edge cancellation varies
  with phase. The finite-mode remainder is proved, while complete independent
  edge jets and the signed prefix remain open. [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/06_ARITHMETIC_GAMMA_AND_EDGE_INTERNAL_REVIEW_20261019.md).
  Added for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, ultra**.

- [G3 complete arithmetic Note 07](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/07_COMPLETE_ARITHMETIC_EDGE_AND_RESIDUAL_INCREMENT_20261019.md),
  19 October 2026: “Add the edge contribution to Z before subtracting the
  anchor and bounding its modulus.” Retaining both signed corrections and
  paying the full coherent remainder gives independent increment<0.000854;
  separate-prefix triangle payments remain excluded in their stated class.
  [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/07_COMPLETE_ARITHMETIC_EDGE_AND_INCREMENT_INTERNAL_REVIEW_20261019.md). Added for Edward Baker with substantial LLM assistance,
  **gpt-6.1-sol, ultra**.

- [S04-T3 Note 03](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/notes/03_UNIFORM_LOCAL_RESIDUAL_TRANSFER_AND_CUTOFF_PAYMENT_OBSTRUCTION_20261019.md),
  19 October 2026: “Actual jumps may cancel.” Uniform local residual charts
  do not preserve a small long-range budget when each natural-cutoff mode
  receives an independent coefficientwise error disk: across the declared
  sector that assigned payment is>.99exp(1/(4t)). This excludes that rule,
  not signed jumps or coherent RS matching. [Same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/reviews/03_UNIFORM_RESIDUAL_TRANSFER_INTERNAL_REVIEW_20261019.md).
  Added for Edward Baker with substantial LLM assistance,
  **gpt-6.1-sol, actual effort ultra**.

- [S07-T2 Note 04](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/04_PAID_PROFILE_TRACE_AND_DIRECT_TAIL_COMPARISON_20261019.md),
  19 October: “The bulk profile norm pays that mass.” The selected N=2
  automorphic cutoff norm pays an annulus between physical integer
  samples; even its exact assigned allowances exceed direct complete-tail
  bounds by >1618 and >34152 before common costs. This is a scoped loss
  of that norm/Cauchy rule, not an actual-error floor or exclusion of
  signed/kernel methods. [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/reviews/04_PAID_PROFILE_TRACE_INTERNAL_REVIEW_20261019.md).
  Added for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, ultra**.

- [S07 options Note 05](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/05_OBSERVATION_OPTIONS_AND_BOUNDED_FEASIBILITY_SCREENS_20261019.md):
  “A cutoff-width sweep under this unchanged rule is not warranted.”
  The omitted physical n=3 sample forces an unchanged-X floor for every
  admissible N=2 cutoff; a V4 split with the same complement norm also
  retains the loss. A changed norm or signed estimate remains outside
  these exclusions. [Internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/reviews/05_OBSERVATION_OPTIONS_INTERNAL_REVIEW_20261019.md).
  Added 19 October for Edward Baker with substantial LLM assistance,
  **gpt-6.1-sol, actual effort ultra**.

## What it cost

The channel-matching program (excluded by the two-channel theorem); the
rank-two coset route; the fixed-\(L\) CCM enlargement; several weeks of
double-precision assembly before an exact formulation replaced it.

## Instead

Keep the pairing that cancels and estimate the pair ([Response 17](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/17_RESPONSE_TO_JOINT_REVIEW_CLAUDE_20261015.md) item 3 of its bounded test: "retain cancellations before taking absolute values"); when a sector must be bounded alone, check first on a control that the sector's sign is not the whole problem; never drop a term without an explicit bound on it in the record; and prefer exact formulations (the Schur localization, the finite Euler identity) to assembled approximations.
