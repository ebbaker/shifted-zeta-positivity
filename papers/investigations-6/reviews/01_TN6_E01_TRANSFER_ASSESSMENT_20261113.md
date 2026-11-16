# TN6-E01 r1 — Internal transfer assessment

13–14 November 2026, America/New_York. Prepared for **Edward Baker**
with substantial OpenAI Codex LLM assistance. Execution dispatch
**gpt-6.1-sol / ultra**. Actual backend model and effort unavailable.
**Disposition: accepted within the frozen absolute scalar scope.**
This is a separate check by the worker who derived the shared transfer,
using the same provider sources. See the
[shared-premise review guidance][guidance].

The [frozen request][req], [manifest][manifest], and [derivation][proof]
are the assessment inputs. The nine entries in the manifest match
their hashes and sizes. The additional [JCH-E02 review][jreview] has
SHA-256 d04f8e6a4fc9e2f619ab5c2f46a39b416c5ead0baad411b85db914d36c2c3ed3
and accepted JCH-E01 without changing its pinned proof. The pinned
[VCD-E02 review][vreview] likewise records acceptance without correction.

- **Interface.** Dividing the base measure by its mass gives the JCH
  probability measure and divides the monic norm by \(h_0(1/2)=Z_*\).
  The ratio \(h_N(1/2)/h_0(1/2)\) is the product of \(\beta_j(1/2)\)
  through \(j=N\). The index \(N\) pays for the first edge omitted from
  the matrix. The separately evolved matrix is the fixed \(J_N\) with
  generator \(J_N^2\). The clock \(\lambda=1/2-\tau\) multiplies the
  base source by \(e^{-\tau u^2}\).
- **Uniform bound.** Multiplying the exponential and cosine-hyperbolic
  series gives the precise \(S_N\) coefficient, with nonnegative terms
  also at \(x=0\) and \(\tau=0\). The ratio of the VCD norm scale
  \(L_N/4\) to the series evaluation scale \(L_N/2\) gives \(4^{-N}\).
  The heat term uses \((1/2)(L_N/2)^2=L_N^2/8\).
- **Depth.** The ceiling bound \(4N+20\le16KA+24\) and \(A\le3K\)
  imply \(4N+20\le256K^2\) since \(K\ge1\). Thus
  \(L_N\le 2A\). Using \(X\le K\) and \(A^2/2\le3KA/2\), the full
  exponent is at most \(-(3/2)KA\). This is at most
  \(-\log(1/\epsilon)\) since \(KA\ge K\ge\log(1/\epsilon)\).
  Positivity of \(L_N\) at \(N=1\) and \(A\) at \(K=1\) handles the
  degenerate corners, including \(X=0,\epsilon=1\).
- **Controls.** Weighted-square controls share both relevant proof
  premises and retain their actual catalog events. The atomic score
  fails and its exact scalar has zero error at \((T,\pi)\). The single
  Euler-factor envelope failure is for \(p=23\) at \(\lambda=0\).
  It supplies no fixed-base counterexample. The derivation distinguishes
  the reflected quartic score failure, unsettled weaker confinement for
  the small-damping controls, the conditional endpoint construction and
  the changed observation kernel. See [B01][decision] and [controls 12][controls].
- **Consumer.** The same Gaussian rule is algebraically identical to
  the finite scalar chain. The sufficient depth needs neither a
  coefficient table nor the JCH fallback moment. Evaluating and
  certifying the scalar still needs coefficient acquisition,
  \(Z_*\) and finite rounding bounds. The normalized error is
  scaled by the fixed base mass. Relative accuracy, sign exclusion,
  whole-state error and evaluation speed remain outside the conclusion.

No routine correction was needed. This completes the fixed shared
transfer and its internal check.

[req]: ../research-progress/handoffs/TN6-E01-r1.md
[manifest]: ../numerics/04_TN6_E01_INPUT_MANIFEST_20261113.json
[proof]: ../notes/03_TN6_E01_COEFFICIENT_TO_SCALAR_TRANSFER_20261113.md
[jreview]: ../02_jacobi_chain_height_flow/reviews/01_JCH_E02_FINITE_CHAIN_ASSESSMENT_20261113.md
[vreview]: ../03_volterra_coefficient_dynamics/reviews/01_VCD_E02_ENVELOPE_ASSESSMENT_20261113.md
[decision]: ../brainstorm/notes/01_TN6_B01_COEFFICIENT_TO_SCALAR_DECISION_20261113.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[guidance]: ../../../avoid/05_same_model_reviews_and_shared_premises.md
