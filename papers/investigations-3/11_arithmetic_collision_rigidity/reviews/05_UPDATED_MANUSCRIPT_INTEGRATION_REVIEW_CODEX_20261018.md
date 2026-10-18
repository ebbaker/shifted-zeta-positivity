# Updated manuscript integration review

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Coordinating reviewer/editor: **gpt-6-astra, ultra**.
Integration and additional checks: **gpt-6.1-sol, ultra**. These are internal
LLM checks by contributing assistants, with cross-model participation;
they are not independent specialist review.

**Disposition:** Notes 05–06 are incorporated into the canonical manuscript,
with written proofs, revised scalar enclosures and explicit scope limits.
No blocking defect was found in the integration checks. No theta collision
exclusion, new Newman bound or completed physical-jet benchmark is claimed.

## Exact version

The current eight-file LaTeX source-set SHA-256 is
`f6cd484647ef328047e9ac51a577b8260e899aecbfdd5026e9e238079feb823f`. Its individual hashes and canonical hash recipe are in the
[build record](../manuscript/positive_arithmetic_packets/BUILD_RECORD.json).
The preceding seven-file source set was
`9def46d014fb1006ff3a16378f66bcd1b7991ea526739b65e8bbfccaf791962e`; Review 04 assessed that earlier manuscript
alongside the continuation notes. It must not be cited as a hash-identical
review of this revision. No snapshot directory or Git commit was created.

## Mathematical coverage

- Section 3 proves positive real part on the closed strip
  \(|\Im z|\le\pi m^2\), including the strip boundary, for nonzero bounded
  nonnegative packets beginning at \(m\ge2\). The convex-kernel proof
  retains every boundary term.
- The disk-map calculation retains the combined slope/curvature budget
  \(\beta^2+|\beta_x|\le1/(4m^4)\). Keeping both square terms in the
  quotient calculation yields \(|r_x|\le d_mr\) and
  \(|r_{xx}|\le d_m^2r\), rather than weaker separately summed bounds.
  The carrier payment is now \(E/64\); the earlier 117 E estimate remains
  valid historical provenance.
- The unit-strip denominator lower bound is used explicitly in the complex
  residual estimate. Positive-coefficient controls inherit the logarithmic
  bounds exactly, while absolute relative tolerances need the coefficient
  comparison factor \((1+\eta)/(1-\eta)\).
- Section 4 explains carrier invariance and why the full higher-mode
  carrier removes the omitted arithmetic tail without removing first-mode
  cancellation. Section 5 states the stronger geometry retained by controls.
- New Section 6 shifts the complete reflected source before truncation,
  states the admissible domain and every finite-mode tail constant, and
  bounds every fixed spectral derivative. The finite shifted approximant
  is real on the real axis and satisfies the heat equation but need not be
  even. Parameters are frozen before differentiation.
- The near-boundary asymptotic is an upper error bound relative to an
  explicit nonzero envelope. Neither an effective onset nor the cost of
  retained-mode quadrature is supplied. Its mode count is not a complexity
  comparison.
- The finite first-jet criterion includes total evaluation and whole-cell
  errors. No positive margin has been exhibited. A Newman conclusion
  additionally requires all finite, outer and endpoint obligations of the
  selected global theorem.

## Verification and its limits

The [revised checker](../numerics/certify_updated_manuscript.py) replays the
original scalar checks and verifies all nine revised table intervals and
eight rounded headline bounds, using exact fractions and 256-bit outward
dyadic rounding. Its [record](../numerics/UPDATED_MANUSCRIPT_CONSTANTS_20261018.json)
contains source hashes and exact endpoints. It reuses the original interval
engine and is not an independent implementation. The last three table rows
enclose conservative constants with \(\cos(\pi/4)\) replaced by \(7/10\),
not the exact-cosine expressions. The analytic 1/8 and 1/64 bounds do not
depend on decimal certification.

Two terminal LaTeX passes produce a 30-page PDF with no warnings, unresolved
references or overfull/underfull boxes. All pages were rendered; the full
document was inspected through contact sheets and selected readable views.
The final bibliography orphan was repaired and its page rechecked. Text
extraction finds no empty page, unresolved-reference marker or glyph beyond
the relaxed interior rectangle. The build record separately records the
built-in editor compilation result. Compilation and scalar replay do not
validate an unproved sign estimate or an oscillatory-integral evaluator.

The [updated overview and detailed plan](../research-overview/02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md)
assigns every future research stage to GPT-6.1 Sol, planned effort ultra.
It uses the exact existing Investigation 22 pilot, complete error budgets,
adversarial event rejection, signed-estimate work and a full global coverage
ledger. Future same-model sessions remain internal review. Current actual
model contributions are distinguished from that planned configuration.

**Remaining issue:** the arithmetic and contour estimates do not supply a
strict positive physical-scale margin for the complete theta field. This
is the next substantive mathematical obligation, not a document defect.
