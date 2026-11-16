# QTT-E02 — Assessment of the compact rank and error bound

14 November 2026, America/New_York. Prepared for **Edward Baker**
with substantial OpenAI Codex LLM assistance. Tool dispatch
**gpt-6.1-sol / ultra**. Separate backend verification unavailable.
Separate same-worker internal pass with shared source and premises.
See [shared-premise review guidance](../../../../avoid/05_same_model_reviews_and_shared_premises.md).

**Disposition: accepted without mathematical correction within scope.**
All four inputs in the [frozen r1](../research-progress/handoffs/QTT-E02-r1.md)
and all 22 inherited entries matched at assessment. Request SHA-256
2a9b819af94f73d65bd917ee5cb203d84f469089e0bb951aae325d52060fba26.
The [result](../notes/04_QTT_E01_COMPACT_RANK_ERROR_BOUND_20261114.md) is
**proved in-note**, with no independent specialist review. Interpret
“certified upper allowances” in its §3 as proved upper bounds from
analytical inequalities. The frozen wording is retained for provenance.

- **Source, clock and norm.** The half-line integral is the prescribed
  full-line transform with \(1/2\), by complete even reflection.
  \(W_\lambda=e^{-\tau u^2}W_{1/2}\) has the contractive sign.
  The scale is the given explicit \(S(x)\), bounded by \(2^{48}\)
  on \([40,80]\), with no use of gamma division at complex \(z\).
- **Analytical constants.** On the common ellipse/circle rectangle,
  \(t>2n^2\) and \(\cos(4\Im v)>1/2\) hold with room for a locally
  uniform analytic extension. The summand envelope follows from
  \(128/e^2+12/e<38\), and the geometric sum and prefactor give
  \(76\cdot2^8<2^{15}\). Radius \(1/16\) and
  \(|\Im(zv)|<22\) yield \(M_2=2^9\cdot2^{15}\cdot2^{33}=2^{57}\).
  The tail bound pays the complete positive series and the worst
  heat and transverse weights. Its remaining logarithmic prefactor
  is at most \(\rho_u/2\) by the given cubic comparison for \(u\ge2\).
  Substitution gives \(T<2^{-192}\).
- **Polynomial and rank.** The contour bounds the positive Laurent
  coefficients, and Laurent symmetry doubles each nonconstant
  Chebyshev coefficient. The geometric tail gives \(2M_\rho\rho^{-d}/(\rho-1)\).
  Taylor's remainder uses \(0\le\tau u^2\le2\) and the exponential
  derivative bound one on the nonpositive interval. The translated
  monomial vector gives the amplitude at each binary grid point.
  Transposing the scalar orders the cores coarse-to-fine, with
  dimensions \(d+2m+1=641\). Each cosine contraction pays the state
  and observation \(\sqrt h\) factors. The exponential half-sum
  is the cosine and introduces no additional Fourier half-factor.
- **Allowance and scalar comparison.** Midpoint error is for the
  complete integrand, cellwise \(h^3M_2/24\), followed by the
  \(2e^{16}\delta\) node replacement and the tail. For the factorial,
  the block powers sum to \(2+8+24+64+160+12=270\).
  The E01 ledger therefore gives \(2^{-144},2^{-40},2^{-37},2^{-116}\),
  with sum below \(2^{-36}\). The matched scalar polynomial integral
  drops precisely the midpoint contribution. No computed stability,
  working precision, or operation advantage has been established.
  The optional \(e_{\rm node},e_{\rm TT},e_{\rm out}\) each reserve
  at most \(10^{-8}/4\) after their own transfers. Compression is
  measured relative to the already perturbed state, and the
  exact-coefficient construction has no such implementation errors.
- **Controls.** At \(T=1/4,z=17\pi\), the inherited atomic source has
  an exact rank-one collision inside the box and fails the analytic
  density premise. This screens a generic rank-only sign inference.
  The smooth and square-mode controls may admit their own
  approximation theorems, with the disclosed absent literal source
  premises and qualifications. Altering the readout changes the
  physical oscillator/Newman observation. No control was assigned
  an untested numerical allowance.

No response check or numerical run was needed. The fixed QTT round ends
with this exact compact approximation result and same-polynomial comparison.
