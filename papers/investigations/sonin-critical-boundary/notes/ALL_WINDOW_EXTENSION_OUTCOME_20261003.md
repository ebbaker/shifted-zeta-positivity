# Certified two-prime extension and the remaining all-window estimate

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Analytic and implementation checks
were performed by separate agents in the same model family. These are
internal research results, not independent specialist refereeing.

## Completed comparison

The program now crosses the first new-prime threshold. For every

\[
F\in C_c^\infty((-3/5,3/5);\mathbb C),\qquad
\int F=\int e^{x/2}F=\int e^{-x/2}F=0,
\]

the outward certificate proves

\[
\boxed{Q[F]\ge\frac3{2000}\|F\|_2^2.}
\tag{1}
\]

With the fixed finite-place representation `S={2,3}` at exponent `1/2`,
the independent correction bound and the identity `Q=B-K` give

\[
|K[F]|\le3458\|F\|_2^2,\qquad
\boxed{Q[F]\ge\frac3{6916003}B[F].}
\tag{2}
\]

Both parities, complex polarization, and all source directions outside the
finite matrix are included. The three constraints have not been increased.
The smaller windows inherit (1) and (2) by inclusion, using the **same**
`{2,3}` representation for (2). The old length-one `{2}` comparison remains
valid separately; adding an inactive prime does not preserve B and K
individually. The new constants are conservative bounds, not optimal gaps.

The [numerical package](../numerics/all_window_extension_20261003/README.md)
contains the generator and small outward records. The original certificate
was replayed once and left unchanged. The manuscript was not edited.

## What changed in the method

The source multiplier is now the complete two-prime expression

\[
q_L(t)=\gamma(t)-\sqrt2\log2\cos(t\log2)
 -\frac{2\log3}{\sqrt3}\cos(t\log3),
\quad\gamma(t)=\Re\psi(1/4+it/2)-\log\pi.
\]

There are no active higher powers at `L=6/5`. After unitary dilation
`f(y)=sqrt(L)F(Ly)` to `(-1/2,1/2)`, use the full analytic projection
`P_E` off `1, exp(Ly/2), exp(-Ly/2)`, and `v_t=P_E exp(iLty)`.
Instead of replacing `lambda-q_L` by its positive part, form

\[
A_L=\frac L\pi\int_0^T(\lambda-q_L(t))\Re|v_t\rangle\langle v_t|\,dt.
\tag{3}
\]

The cutoff check proves `q_L(t)>=lambda` outside the band. Consequently
`Q>=lambda I-A_L`. All positive energy inside the band is retained before
source compression. This is an improvement to the sufficient bound; it
does not prove a signed prime-density discrepancy estimate.

The general-L formulas and analytic error proof are in the
[scaling audit](../reviews/ALL_WINDOW_SCALING_AUDIT_20261003.md), §§1–4.
In particular the operator has the prefactor L, the plane argument is LT/2,
and `||v_t'||<=L/sqrt(12)`. For signed weights the integrand is smooth,
allowing a second-order midpoint error instead of the earlier
first-variation error for a positive-part weight. The digamma derivative
bound follows from its [partial-fraction expansion](https://dlmf.nist.gov/5.7.E6).

Write `r=lambda-q_L`, `h=T/N`, `Wabs=integral_0^T |r|`, and

\[
V_1=\gamma(T)-\gamma(0)+T\sum c_a a,\quad
V_2=15\sqrt3/2+T\sum c_a a^2.
\]

The integrated second-derivative operator bound is

\[
R_2=V_2+\frac{2L}{\sqrt3}V_1
       +L^2(1/\sqrt{20}+1/6)W_{\rm abs}.
\]

Midpoint error is at most `L h² R2/(8 pi)`. The scalar absolute mass is
independently bounded by its midpoint sum plus `h V1/2`. The complete
Legendre tail, including the analytic moment-vector tails, adds at most
`2L delta_M Wabs/pi`. Taking absolute values in these **error** bounds
does not discard signs in the matrix itself.

## Outward budget and conversion to B

The [preflight](ALL_WINDOW_EXTENSION_PREFLIGHT_20261003.md) preceded the
new outward run and fixed a finite resource envelope. The selected
parameters are `lambda=1/2`, `T=100`, `M=100`, `N=30000`. Arb/Acb builds
two 50-by-50 parity blocks and tests positive LDL pivots for
`(249/500)I-A_M`. The 192-bit run took about 41 seconds. A separate 256-bit
run and implementation audit are documented in the
[certificate review](../reviews/ALL_WINDOW_EXTENSION_CERTIFICATE_REVIEW_20261003.md).

The 192-bit outward endpoints imply the following conservative decimal
bounds; exact rational endpoints are retained in the certificate.

| Quantity | Certified bound |
|---|---:|
| cutoff margin `gamma(100)-1/2-C_L` | greater than 0.0184626 |
| finite matrix upper bound | 0.498 |
| midpoint operator error | less than 0.000320671 |
| all omitted source modes | less than 0.000000009124 |
| combined error | less than 0.000320680 |
| chosen error allowance | 0.0005 |

Thus `Q>=(0.5-0.498-0.0005)I=(3/2000)I`. The finite-rank
operator is zero on its source complement; its positive matrix cap and
the full operator norm error control that complement and all mixed terms.
No floating eigenvalue is an input to the proof.

The recalibrated inherited boundary gap is

\[
g_{23}=(17-12\sqrt2)(7-4\sqrt3)\frac{57}{10^6}.
\]

The exact source nuclear factorization yields
`|K|<=L sqrt((1-g23)/g23)||F||²`. Its outward value at `L=6/5` is
below 3457.345, hence below 3458. This uses the earlier certified
archimedean gap; it does not require compactness of the two-prime kernel.
Finally,

\[
B=Q+K\le Q+3458\|F\|^2
\le\left(1+\frac{6916000}{3}\right)Q,
\]

which proves (2). The revised main term `(3/6916003)B` and the remainder
`(6916000/6916003)B-K` are both nonnegative.

## Diagnosis of the capped failure

The bounded pilot compared exactly two parameter choices at this single
window: `(lambda,T,M)=(1,164,160)` and `(1/2,100,100)`. At the first choice,
the largest capped eigenvalue is about 1.017202, exceeding lambda 1;
the signed value is about 0.997081. At the second choice, the capped
top eigenvalues are about 0.594013 and 0.569901, again too large, while
the signed maximum is about 0.497552. Precision cannot repair this
loss of information in the majorant.

The following values concern normalized, fully moment-projected trial
directions for the second choice. They are **floating diagnostics**, not
additional outward certificates.

| Worst capped direction | Capped lower value | Signed band lower value | Positive energy recovered | Actual-Q integral through 2048 |
|---|---:|---:|---:|---:|
| even | -0.094013 | 0.117601 | 0.211614 | 0.125504 |
| odd | -0.069901 | 0.075316 | 0.145216 | 0.078182 |

The pilot records an analytic nonnegative high-frequency tail, with its
upper formula evaluated in floating arithmetic (about 0.002861 and
0.001071 at 2048); finite quadrature and roundoff are not outward-enclosed.
These values distinguish a poor capped bound from evidence of negative Q.
The full-space certificate (1) supplies the rigorous sign conclusion.
The signed operator has a different worst direction: its finite-Q
diagnostic through 2048 is about 0.004782. No optimal spectral gap is claimed.

The diagnostic sources are exact analytic moment projections of finite
Legendre polynomials, extended by zero. They lie in the logarithmic form
domain and may have endpoint jumps. Smooth neutral sources approximate
them in that form norm, as proved in the scaling audit. The saved trial
coefficients identify these diagnostic directions; they are not part of
the rigorous certificate's input.

## New qualitative advance for the relative route

The [scaling audit, §7](../reviews/ALL_WINDOW_SCALING_AUDIT_20261003.md)
extends relative compactness to **every fixed finite prime set**. The
argument needs only boundedness of K, not a square-integrable K kernel.
The smoothed trace defines a closed positive source form B with the
logarithmic Fourier domain. Fixed support gives compact embedding of
that domain, hence compact resolvent. Injectivity of nonzero compact-source
convolution on a nonzero Sonin space excludes a zero eigenvalue. Therefore
B has a positive fixed-window gap and compact inverse square root. It follows
that `H=B^(-1/2) K B^(-1/2)` is compact and selfadjoint for each fixed S,L.

Dense two-prime resonance locations therefore do not block the relative
compactness reduction. Local square integrability of the unweighted
multi-prime kernel remains a separate question and is unnecessary here.
This removes a qualitative obstacle but supplies no effective constants
as the prime set and window grow.

## Remaining theorem obligation

The program still needs `Q>=0` on an **unbounded** sequence of nested
windows with the same three source constraints. Two precise sufficient
routes now remain:

1. Prove signed-band matrix and complete error bounds with
   `mu_L+epsilon_L<=lambda_L` along such a sequence, with a finite successful
   construction for every member. A finite list of passes is insufficient.
2. Use the now-established fixed-set relative compactness to certify a
   spectral split with `H11<=vartheta_L I`, `vartheta_L<1`, and
   `I-H00-H01 H10/(1-vartheta_L)>=0`, including the mixed block.

For an actual B-spectral complement above Lambda, the crude bounds are
`||H11||<=k/Lambda` and `||H01||<=k/sqrt(beta Lambda)`. Making that split
effective, evaluating its finite block, and replacing overly pessimistic
constants are unresolved. The signed experiment supports preserving
positive source energy, not a bound on centered prime-density error.
The exact centering identity `Q=Gamma+J-E` remains available, but its
signed discrepancy estimate has not been proved.

The absolute-amplitude cutoff still has the doubly exponential scale
identified in the original strategy, and transport constants deteriorate.
An adaptive continuation also needs a nonaccumulation proof. Neither
unweighted `B>=K_plus`, generic place monotonicity, nor RH follows from
this bounded extension. No additional window sweep was started.
