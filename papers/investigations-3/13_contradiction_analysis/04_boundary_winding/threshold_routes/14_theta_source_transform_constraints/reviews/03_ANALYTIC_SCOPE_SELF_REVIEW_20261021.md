# Self-review: analytic scope and quantitative residual constraints

21 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**.
Authoring-assistant assessment only; no independent specialist review.

Reviewed [Note 03](../notes/03_ANALYTIC_SCOPE_AND_QUANTITATIVE_SOURCE_CONSTRAINTS_20261021.md).

- The earlier no-gain result is an analytic equality for an explicitly
  relaxed pointwise error class. It does not assess all source geometry
  or the cost of all possible evaluators. The two-endpoint comparison
  also has a symbolic positive-difference proof.
- The abstract adjoint bound is stated as an inequality, without an
  unjustified duality or attainment assertion. A nonzero residual defect
  keeps its explicit pairing term.
- The analytic saturating sequence uses G without the heat factor in
  its erf argument. G grows at most linearly along a fixed horizontal
  strip, so the multiplier's at-most Gaussian growth is dominated by
  theta's double-exponential strip decay for each fixed M. Including
  exp(tu^2) inside that argument would invalidate this simple proof.
- Dominated convergence uses |erf(MG)|<=1 on the real axis and the
  integrable weight w|G|. The sequence's derivative at a simple zero
  grows linearly with M. No common quantitative strip norm is claimed.
- The strict regularity loss pairs the two sides of a simple zero.
  Nonnegative factors permit replacing the weight and |G| by their
  lower bounds. The derivative estimate gives the loss
  w0*g*(h^2-2*L*h^3/3); L*h<=1 makes it positive. The admissible class
  is invariant under m -> -m, yielding the absolute-value estimate.
- Cauchy's derivative bound requires a common bound on genuine complex
  discs, not merely real-axis boundedness. The note does not establish
  this hypothesis for a specific approximation residual or claim its
  cost is favorable there.
- The existing S01 paired-tail theorem already proves a strict symbolic
  saving. The explicit connector in Note 02 was also already present
  in S01 Section 2; its provenance has been clarified. Neither is
  presented as newly discovered here.
- Analytic saturation and the strict regularity gap concern error
  allowances, not collisions. The known controls keep their stated
  scopes; no theta exclusion or new arithmetic discriminator follows.

Disposition: retain the two auxiliary analytic facts, prioritize a
quantitative constraint on the actual residual and its physical use,
and require its proof before numerical acquisition. No numerical
checks were used for this continuation.
