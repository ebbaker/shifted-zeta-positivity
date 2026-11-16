# VCD-E03 internal manuscript assessment

14 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Recorded dispatch **gpt-6.1-sol /
ultra**. Separate backend attestation unavailable. This is a same-worker
assessment of the integration, sharing sources with the drafting pass.
See [shared-premise review guidance](../../../../avoid/05_same_model_reviews_and_shared_premises.md).

**Disposition.** The [draft](../manuscript/main.tex) integrates the
[coefficient and norm-product proof in-note](../notes/01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md),
previously [accepted without correction within scope](01_VCD_E02_ENVELOPE_ASSESSMENT_20261113.md).
The integration requires no correction to the frozen mathematical claim.

- Theta inversion yields the stated even source. Both derivative
  bounds follow using the summable factor
  \(m^{4+2j}\exp[-\pi(m^2-1)]\) and the same complete tail.
  Fixed powers of \(u\) and fixed Gaussian or exponential tilt do
  not interfere with dominated differentiation and polynomial boundary
  terms. The mass \(Z_\lambda\) and Fourier \(1/2\) survive in the readout.
  In the bounded review response, \(p'(0)=-1/2\) accounts for the
  primitive boundary contribution and the Mellin split gives
  \(H_0(z)=\xi((1-\mathrm i z)/2)/8\).
- Parity and symmetry of multiplication give the monic recurrence.
  Differentiated orthogonality leaves only \(P_{n-2}\) in the monic
  derivative, with coefficient \(-h_n/h_{n-2}\). The logarithmic
  norm derivative gives \(\beta_n+\beta_{n+1}\), and adjacent
  subtraction gives Volterra with the stated forward-\(\lambda\) sign.
- For the orthonormal column the matrix derivative is
  \(A=-(J^2)_--\tfrac12\operatorname{diag}(J^2)\) with strictly
  lower part. Subtracting the commuting \(-J^2/2\) identifies
  \(B=((J^2)_+-(J^2)_-)/2\) and fixes \(J'=BJ-JB\).
  The identity holds entrywise and on finite sequences. The
  spectral readouts use multiplication separately, including its
  domain, rather than asserting bounded-operator Lax dynamics.
- The common confinement estimate uses the positive series mean of
  \(9+12/(2r_m-3)-4r_m\) and the uniform heat term \(2\lambda u\le u\).
  The split at \(1/2\) supplies \(\cosh(4u)-11\).
  The locally absolutely continuous density lemma has the derivative
  integrability, boundary decay and cosine-hyperbolic moment required.
  Integration by parts gives \(2n+1\), followed by Jensen and the
  \(2n+12\) inverse. Monicity and the all-degree quantifier are preserved.
- At the fixed initial time the normalized norm telescopes to
  \(h_N/h_0\). The largest factor is \(B_{N-1}\), with argument
  \(2N+10\). The scalar corollary uses the principal finite block,
  Gaussian exactness through degree \(2N-1\), the monic squared
  Hermite remainder on the real line, and Gaussian averaging with
  variance \(2\tau\). The outer factor \(Z_*/2\) restores the field
  normalization. The fixed approximation uses \(J_N^2\), the square
  after taking the leading block.
- The validated weighted-square witnesses retain every premise of
  the confinement lemma, including the integration by parts across
  the even extension. Their collisions delimit the scope of the bound.
  Other failed premises and untested coefficient comparisons are listed
  in the [integration note](../notes/02_VCD_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md).

The draft built outside the repository with settled references. See
the [small build record](../numerics/02_VCD_ANALYTICAL_MANUSCRIPT_BUILD_20261114.json).
Rendered-page and cross-manuscript checks belong to the parent.
