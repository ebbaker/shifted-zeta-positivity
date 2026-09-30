# Sonin continuation after the actual-projection enclosure test

29 September 2026. Prepared for Edward Baker with LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
not exposed. This is a research handoff, not independent human review.

Read the [main enclosure note](SONIN_ACTUAL_PROJECTION_ENCLOSURES_20260929.md)
and [critical review](../reviews/SONIN_ACTUAL_ENCLOSURE_REVIEW_20260929.md)
first. This is the immediate continuation after the earlier same-day
trace audit and supersedes its proposed enclosure task. Keep CCM
temporarily closed and preserve the completed finite Weil certificates.

## What is now available

- A certificate for the actual cutoff-cosine operator:
  `I-C² >= (57/10^6) I`, `||C||1<2.858`, and an explicit polynomial
  resolvent with inverse error below `9.2e-32` and smoothed trace-norm
  error below `2.7e-31`. See the [derivation](SONIN_PROLATE_RESOLVENT_CERTIFICATE_20260929.md).
- Certified normalizations and L1/derivative norms through order four
  for the exact even and odd sources (A17), with endpoint tails included.
  See the [source certificate](SONIN_SOURCE_NORM_CERTIFICATES_20260929.md).
- Actual Sonin trial vectors `q_n=Pi eta_n`, with a compact smooth
  Legendre seed definition, globally bounded projection errors, and
  finite A/H/J/K interval matrices for degrees 20 and 24.
- A complete but broad Galerkin trace-error enclosure. A single omitted
  degree 21 direction proves missed trace greater than 0.00373 and 0.00712
  for the even and odd sources. Thus the chosen rank-two approximation
  cannot attain a `10^-8 B_infinity` trace-error allocation, regardless
  of numerical precision. This is a scoped accuracy conclusion, not an
  arithmetic residual sign or an impossibility theorem.

## Next single lemma: a controlled scalar smoothed trace

At `L=1`, keep the two exact sources and `S={infinity,2}`. For
`H=D2 F`, evaluate `h0=B_infinity[H]=Gamma[H]+E_infinity[H]`
with a genuine total error budget. Also compute the unshifted scalar
`B_infinity[F]` if it shares the same enclosure machinery.

Use the already certified identity

\[
\epsilon(\rho)=\operatorname{Tr}(C(I-C^2)^{-1}B_\rho),\qquad
B_\rho=\chi\vartheta(\rho^{-1})R\mathcal F\chi,
\]

and replace the smoothed resolvent by the rank 32 polynomial operator.
The uniform error in the kernel epsilon from that replacement is below
`2.7e-31`; after integrating against the source correlation, its contribution
to the scalar error is at most `2.7e-31 ||H||1²`.
The unresolved part is the finite polynomial–cosine integration, its
variation in the scaling parameter, and convolution against the exact
source correlation. Account for cancellation and quadrature errors;
node agreement is not an enclosure. The gamma calculation must include
the full contact. Its Fourier-tail bounds from the source fourth
derivatives are already available; they do not replace interior quadrature.

The coarse bound `h0 <= Gamma_upper + 2.858 ||H||1²` came from the
different cutoff kernel **delta**, via a positive correction. Do not
insert `2.858` as a bound for **epsilon**. The correct scalar trace
evaluation must use the audited epsilon formula above.

Do not begin by enlarging the old degree 20/24 trial space. Its small
projection defect did not guarantee that it captured the smoothed trace.
First establish the scalar trace scale and conditioning. Then, if justified,
choose trial vectors from the source response rather than from projection
convenience alone. Nonorthogonal exact Sonin trial vectors are allowed;
there is no need to introduce a Gram inverse square root.

## What still cannot be claimed

No complete arithmetic residual, Chebyshev return moment, residual sign,
new positivity interval, or arbitrary-support estimate has been obtained.
Accurate scalar archimedean traces would enable later diagnostics; they
would not supply the signed finite-place covariance bound. The previous
place-addition identity remains valid, with complete and partial arithmetic
residuals distinguished.

Preserve the small code/error records in `numerics/`, research in `notes/`,
and reviews in `reviews/`. Every certificate uses python-flint 0.9.0 and
standard Python; reproduce without `-O`/`-OO`. No manuscript or draft
snapshot is needed, and no commit or push is requested.
