# QTT-E03 internal manuscript assessment

14 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Recorded dispatch **gpt-6.1-sol /
ultra**. Separate backend attestation unavailable. This is an internal
same-worker assessment of the new integration. It shares proof sources
with the drafting pass and carries no independent specialist review.
See [shared-premise review guidance](../../../../avoid/05_same_model_reviews_and_shared_premises.md).

**Disposition.** The [manuscript](../manuscript/main.tex) carries the fixed
QTT bound and scalar comparison from the [proof in-note](../notes/04_QTT_E01_COMPACT_RANK_ERROR_BOUND_20261114.md),
previously [accepted without mathematical correction within scope](01_QTT_E02_RANK_ERROR_ASSESSMENT_20261114.md).
No mathematical correction to the frozen QTT result was required.

- The complete even source and \(\xi/8\) convention are consistent. In
  the Mellin split the reflection correction is \(1/[s(s-1)]\), and the
  source integration by parts contributes \(1/2\) to \(8H_0\). The heat
  equation has \(\partial_\lambda H=-\partial_z^2H\) and
  \(\partial_\tau W=-u^2W\). The state and readout each carry \(\sqrt h\),
  and the exponential half-sum implements the half-line cosine.
- The midpoint Cauchy circles and Chebyshev ellipse lie in the same
  rectangle. The summand estimate controls the complete series and its
  extension. The radius \(1/16\), cosine bound \(2^{33}\) and rectangle
  bound \(2^{15}\) give \(M_2=2^{57}\). The summed real tail yields
  \(T<2^{-192}\), with the worst heat and transverse weights included.
- Symmetric Laurent coefficients give the factor 2 in the Chebyshev
  tail. The heat factor uses \(0\le\tau u^2\le2\), so the Taylor error
  needs no exponential multiplier. The binomial translation produces
  bond dimension at most \(512+2(64)+1\) in coarse-to-fine order.
  The generator core update squares the running coordinate, and the
  Vandermonde submatrix gives the separately scoped exact multiplier
  rank for positive \(\tau\).
- For the complete integrand the midpoint remainder has bound
  \(M_2 h^3/24\) per cell. The factors \(h=2^{-71}\), \(S_*\le2^{48}\),
  \(2\e^{16}<2^{25}\), and \(65!\ge2^{270}\) give the scaled ledger
  \(2^{-144},2^{-40},2^{-37},2^{-116}\). Their sum is below
  \(2^{-36}\). The scalar integral uses the same polynomial and
  retains tail and both approximation terms. Its exact endpoint
  expression telescopes upon differentiation.
- The optional computed-error transfer distinguishes node perturbation
  from compression against the already perturbed state. The bound is
  conditional on supplied error enclosures. No working precision,
  practical cost, arithmetic sign or height-dependent rank conclusion
  follows from the manuscript.
- The [integration note](../notes/05_QTT_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md)
  records the full control screen. The rank-one atomic event occurs at
  the time and height stated in the draft and lacks the analytic theta
  density. Its collision rules out the stated generic rank-only sign
  inference.

The final source was built with settled references outside the repository
and the text extraction checked across all pages. See the
[small build record](../numerics/03_QTT_ANALYTICAL_MANUSCRIPT_BUILD_20261114.json).
The parent owns the rendered-page and cross-manuscript checks.
