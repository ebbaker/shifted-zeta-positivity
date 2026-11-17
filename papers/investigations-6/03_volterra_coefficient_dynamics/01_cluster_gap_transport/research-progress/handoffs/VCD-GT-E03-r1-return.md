# VCD-GT-E03 r1 — Physical Jacobi heat-defect return

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Explicit helper dispatch
**gpt-6.1-sol / ultra**. Separate backend attestation and actual lead
configuration are unavailable.

**Complete, proved in-note within the requested class, pending E05
assessment.** The [proof note][note] answers the [frozen r1 request][request]
and its [B01 decision][decision]. The [branch register][register] owns
live task status.

- The finite skew Lax calculation, followed by the last-link
  resolvent derivative, proves
  \(R_N=\beta_N\beta_{N-1}\partial_{\beta_{N-1}}G_N\) for \(N\ge2\)
  and \(R_N=(h_N^*/2\pi i)\oint e^{izw}w/P_N(w)^2\,dw\)
  for \(N\ge1\). The spectral contour encloses the Gaussian nodes.
  The elementary doubled-node simplex calculation gives
  \(R_N=(-1)^{N-1}h_N^*z^{2N-2}
  [\chi_N+z\chi_N'/(2N-1)]/(2N-2)!\).
  It yields \(R_1=\beta_1\) with no retained link derivative, and
  \(R_2=-h_2^*z^2\sin(z\sqrt{\beta_1})/(2z\sqrt{\beta_1})\)
  with the sine quotient understood at zero. The model discriminant
  check at degree two is \(\dot D_2=r_2=-\beta_2D_2\)
  for any fixed contour counting two cosine zeros.
- On the fixed buffered counted circle,
  \(r_N=-(2\pi i)^{-1}\oint_\Gamma(z-c_N)R_N/G_N\,dz\)
  and \(\dot D_N=2+4K_ND_N+r_N\) through a merger.
  The exact physical margin differs from \(W_N(u)D_N(u)\)
  by \(D(v)-D_N(v)+\int_u^v W_N r_N-(\mathcal C-\mathcal C_N)\).
  The note carries the full E02 drift transfer, incoming lower
  gap, signed residual, and outer contour, endpoint and time
  evaluation costs. Its quadratic check saturates the exact
  positive-gap test at the event with zero residual.
- The explicit phase allowance (6) is
  \(O(|z|^2\log^2(N+1)/N)\) uniformly for \(\lambda\in I\subset[0,1/2]\)
  and \(|\Im z|\le1\). The actual residual-to-next-head field-error
  ratio on fixed nonzero compact sets is
  \(\Pi_N/(\beta_{N+1}|z|^4)\) times a factor tending uniformly to
  one, with \(\Pi_N=(2N-1)(2N)(2N+1)(2N+2)\).
  Both models have the same actual data through \(\beta_N\);
  the unacquired \(\beta_{N+1}\) in the actual next-head error
  has the allowance \(B_N-\beta_N\). The exact residual phase
  needs only the retained nodes.
- For the specified norm-only contour and time integration, (19)
  compares its absolute allowance to the direct \(G_{N+1}\) contour
  discriminant allowance. On a comparable fixed circle, with
  comparable floors, a paid collar ratio at most \(1/2\), bounded
  model exponent rate and the degree-only \(B_N\), the allowance
  ratio has order \((v-u)N^4/\log^2(N+1)\). This is a comparison of
  allowances and supplies no lower bound for the actual signed
  contour integral. The direct complete-source baseline pays its
  own Fourier and mass enclosures. No canonical tube, coefficients,
  incoming gap or improvement over the matched direct test was acquired.

All six original request input hashes matched. The completed E01/E02
returns were read before consuming their bounds. The corresponding
verified artefact SHA-256 values are listed below.

| File | SHA-256 |
| --- | --- |
| [E03 request][request] | `6e9526ff6976702b99ef846cec184dc3b353a71c1ce72b99512bb549d31b7479` |
| [E03 proof note][note] | `9e5323bfbc564bc0451b78e1aea4aeee9fb9355b29047467f827f5ccb9a6a828` |
| [E01 return][e01r] | `362ff2b1035ca309c93a00ed9238f9ed39e2826fb14231d89310adbf65ea4fb2` |
| [E02 return][e02r] | `47cdf8c9b7dd6b17d1a9964aa79f6eda3b970c50719b2ba12586a88c8c5ac818` |

The frozen algebraic route succeeds. A gain from the unsigned
residual allowance was not established on the prescribed matched
geometry. B02 owns the unacquired signed cancellation or a different
justified estimation mechanism. This is a bounded helper checkpoint.
The control screen is analytical; no numerical campaign or new
source inequality was used.

[request]: VCD-GT-E03-r1.md
[note]: ../../notes/05_VCD_GT_E03_PHYSICAL_MODEL_DEFECT_20261116.md
[decision]: ../../brainstorm/notes/01_VCD_GT_B01_SIGNED_DEFECT_DECISION_20261116.md
[register]: ../01_VCD_GT_RESEARCH_PROGRESS_20261116.md
[e01r]: VCD-GT-E01-r1-return.md
[e02r]: VCD-GT-E02-r1-return.md
