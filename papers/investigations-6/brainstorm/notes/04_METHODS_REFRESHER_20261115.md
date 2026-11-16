# Methods refresher for the four Investigation 6 papers

15 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. The registered chat has no recorded
model configurations; actual backend model and reasoning effort are
unavailable and are not inferred.

This companion to the [results review](03_MANUSCRIPT_REVIEW_AND_PATHS_FORWARD_20261114.md)
explains the setup, representations and methods. It adds no new estimate,
criterion, numerical experiment or change of research status. The
[result index](../../../../result-summaries/README.md) and
[avoid index](../../../../avoid/README.md), especially
[cluster 18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md)
and [pattern 03](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
provide the result and representation context. The
[control catalog](../../../../result-summaries/12_collision_controls_and_screening.md)
and [pattern 02](../../../../avoid/02_shape_only_arguments_and_the_controls.md)
retain the distinction between representing the field and controlling its zeros.

## Common setup

The starting object is the positive, even, rapidly decaying complete theta
source \(\Phi(u)\). The Newman field is its heat-weighted Fourier transform:

\[
 W_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
 H_\lambda(z)=\frac12\int_{\mathbb R}W_\lambda(u)e^{izu}\,du.
\]

Here \(u\) is the source coordinate, \(x=\Re z\) is the height coordinate
in these papers, and \(\lambda\) is Newman time. Their normalization is
\(H_0(z)=\xi((1-iz)/2)/8\), connecting the time-zero field to the zeta
problem. On \(0\le\lambda\le1/2\), reverse the clock by
\(\tau=1/2-\lambda\); then
\(W_{1/2-\tau}=e^{-\tau u^2}W_{1/2}\).
Thus time evolution is multiplication by a Gaussian in the source
coordinate, while observation at height \(x\) inserts an oscillatory phase.

The common question is how to represent these operations recursively and
still recover the literal scalar field. The constructions mostly give
explicit representations and controlled approximations; they do not begin
with an optimized variational trial state. The four representations also
use different state amplitudes, as specified below.

## 1 QTT Newman flow

**Setup and ansatz.** Discretize a bounded positive \(u\)-interval on a
dyadic grid and label a midpoint by its binary digits
\(u_{\boldsymbol b}=a+\sum_k c_kb_k\). Treat
\(\psi_{\boldsymbol b}=\sqrt h\,W_\lambda(u_{\boldsymbol b})\)
as a many-bit array and represent it by a matrix product
\(A_1(b_1)\cdots A_L(b_L)\). A tensor site is a **binary digit of the
source coordinate**.

**Method.** Approximate the base source by a Chebyshev polynomial and the
Gaussian heat factor by a Taylor polynomial. Their product is a polynomial
whose samples admit explicit tensor cores: each bit applies the binomial
translation that adds its contribution to \(u\). The sampled heat
generator is the square of the binary-coordinate operator. Each Fourier
phase also factors over bits, so two product contractions recover the cosine
readout. The analysis transfers polynomial, spatial-tail and quadrature
errors to the field and compares with direct integration of the same
polynomial. This is a constructive polynomial route to a tensor train.

**Paper pointers:** [QTT manuscript](../../01_qtt_newman_flow/manuscript/main.tex),
§§3–5; `eq:delta` for the polynomial approximation,
`eq:readout` and `eq:Q` for observation, `eq:transfer` for the error transfer.

## 2 Fixed Jacobi chain

**Setup and representation.** Normalize the base source to a probability
measure \(d\mu_*=W_{1/2}(u)du/Z_*\), and construct its orthonormal
polynomials. Multiplication by \(u\) becomes a tridiagonal Jacobi operator
\(J_*\). A chain site is now a **polynomial degree**. Starting at
\(e_0\), the exact prepared state and scalar observation are

\[
 v(\tau,x)=e^{-\tau J_*^2}e^{ixJ_*}e_0,\qquad
 H_{1/2-\tau}(x)=\frac{Z_*}{2}\langle e_0,v(\tau,x)\rangle.
\]

The associated tensor-state encoding is the one-excitation state
\(\sum_n v_n|1_n\rangle\), represented by bond-two matrix products.
The basis and chain coefficients stay fixed as height and time change.

**Method.** Establish the operator realization, translate the two
multipliers into local lattice equations, and truncate the chain to
\(N\) sites for scalar evaluation. Its spectral measure identifies that
evaluation with Gaussian quadrature. Hermite interpolation controls the
cosine quadrature error; averaging over a real Gaussian inserts the heat
factor. Coefficient bounds then control the remainder. The finite
implementation obtains coefficients from even moments and interval
factorization of the parity-separated Gram matrices.

**Paper pointers:** [Jacobi manuscript](../../02_jacobi_chain_height_flow/manuscript/main.tex),
`thm:orbit`, `eq:lattice`, §3 for the one-excitation encoding,
and `eq:finite`/`eq:hermite` for truncation and its remainder.

## 3 Volterra coefficient dynamics

**Setup and representation.** Rebuild the orthogonal-polynomial basis for
the current weight \(W_\lambda\) at every time. Encode the moving source
by its monic recurrence

\[
 uP_n=P_{n+1}+\beta_nP_{n-1},\qquad
 \beta_n=h_n/h_{n-1},\qquad h_n=\int P_n^2W_\lambda\,du.
\]

This gives a **time-dependent chain**, whose squared couplings are
\(\beta_n(\lambda)\). It is the moving-basis companion to the preceding
paper's fixed chain, not an additional guessed family of weights.

**Method.** Differentiate the orthogonality identities with respect to
\(\lambda\). Since \(\partial_\lambda W_\lambda=u^2W_\lambda\), the
derivatives close into the Volterra equation
\(\partial_\lambda\beta_n=\beta_n(\beta_{n+1}-\beta_{n-1})\)
and an entrywise Lax commutator. To introduce quantitative theta input,
bound the logarithmic derivative of the weight, integrate by parts against
\(uP_n^2W_\lambda\), and apply Jensen's inequality. This controls the
coefficients and hence the norm product needed by the fixed-chain remainder.

**Paper pointers:** [Volterra manuscript](../../03_volterra_coefficient_dynamics/manuscript/main.tex),
`eq:recurrence`, `eq:volterra`, `eq:lax`, and `eq:confinement`.
`eq:twochains` displays the moving and fixed scalar representations together.

## 4 Exact infinite dyadic products

**Setup and representation.** Partition the full source line into nested
dyadic cells and use their exact masses
\(m_{L,j}=\int_{I_{L,j}}W_\lambda(u)du\). Prepare amplitudes
\(\sqrt{m_{L,j}}\). Split each parent cell into two children with
amplitudes \(\sqrt{m_{\rm child}/m_{\rm parent}}\), adding one binary
resolution level at a time. Under the common cell embedding, the states
represent \(\sqrt{P_hW_\lambda}\) and approach \(\sqrt{W_\lambda}\).

**Method.** Express refinement as telescoping source factors approaching
the identity on fixed bounded intervals, and factor the Fourier phase
over the binary digits. At finite resolution integrate the phase across
each unresolved cell. Its exact average supplies the sinc factor in

\[
 A_L(\lambda,z)=\frac12\operatorname{sinc}(zh/2)
          \sum_jm_{L,j}e^{izc_{L,j}}.
\]

Weighted density-approximation estimates then control the Fourier readout.
Comparison with center-point phase sampling explains the role of the sinc
factor. The network proceeds through **successive spatial resolutions**;
refinement gates may depend on the whole resolved prefix. Finite-level
time evolution uses masses projected from the exact source at each time.

**Paper pointers:** [Dyadic manuscript](../../04_exact_infinite_tensor_products/manuscript/main.tex),
`eq:mass-isometry`, `eq:telescopes`, `eq:phase-product`, `eq:sinc`,
and `eq:readout`.

## Session capture status

The 14 November final reply had not reached the registered archive. The
source now records an explicit unmoderated/no-display status; a narrow
adapter extension accepts that exact neutral shape and still rejects
moderated, replacement-display and unknown structures. All 92 recorder and
adapter tests passed. Refresh then stopped on an independent integrity
check: source creation time is now `2026-11-14T15:25:12.309Z`, while the
registered original is `2026-11-14T15:25:12.273Z`. Neither timestamp nor
the registered archive was rewritten, and the check was not relaxed.
The original public-message prefix still agrees. An explicitly unregistered
public-text [supplement](../../chat-histories/unregistered_public_supplement_0003_20261115.json)
preserves additional completed messages pending
resolution of that metadata mismatch; it is not a canonical refresh.
