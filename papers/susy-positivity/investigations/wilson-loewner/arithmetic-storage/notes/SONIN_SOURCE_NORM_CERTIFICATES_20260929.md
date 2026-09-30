# Certified A17 source norms and smoothness bounds

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the exact serving variant and configured reasoning effort
are not exposed to this subagent. This is an internal mathematical and numerical
audit, not independent human refereeing.

## Result and deliverables

The two exact A17 sources now have certified normalization, L1, and derivative
L2 enclosures through order four. The calculation uses Arb/Acb ball arithmetic,
exact rational polynomial coefficients, rigorous integration over a compact
interior, and an explicit analytic bound on both omitted endpoint tails. It
does not treat agreement between floating-point calculations as certification.

Files:

- [source_norm_enclosures.py](../numerics/source_norm_enclosures.py): derivation-backed calculation and reusable source sampler.
- [source_norm_enclosures.json](../numerics/records/source_norm_enclosures.json): small record with ball displays **and exact rational
  lower/upper endpoints**, polynomial coefficients, and tail bounds.

The record's `gamma_upper_bound_*` fields enclose the **value of an analytic upper
bound**, not the gamma quadratic form itself. The fields called
`normalized_derivative_L1_cauchy_bounds` have the same upper-bound meaning.
No actual Sonin trace, projection approximation, residual sign, or Weil sign
is evaluated by these files.

## 1. Exact source representation

Let `b=9/20`, `y=x/b`, `v=(1-y²)^(-1)`, and `phi(x)=exp(-v)` for
`|x|<b`, extended by zero. Put `P=-d²/dx²+1/4` and

\[
q_0=P\phi,\quad q_1=P(x\phi),\quad f_j=q_j/N_j,\quad N_j=\|q_j\|_2.
\]

Inside the support the exact formulas are

\[
q_0=e^{-v}A_0(v),\quad
A_0(v)=\frac14-\frac{6v^2-12v^3+4v^4}{b^2},
\]
\[
q_1=y e^{-v}A_1(v),\quad
A_1(v)=\frac b4+\frac{-2v^2+12v^3-4v^4}{b}.
\tag{S1}
\]

All derivatives remain `exp(-v)y^epsilon A(v)`, with `epsilon` equal to
zero or one. The exact polynomial recurrences for differentiation in **x** are

\[
(0,A)\longmapsto\left(1,\frac{2v^2(A'-A)}b\right),
\]
\[
(1,A)\longmapsto\left(0,\frac{A+2(v^2-v)(A'-A)}b\right).
\tag{S2}
\]

The code keeps these coefficients rational throughout. This also supplies
reusable exact sampling formulas without numerical differentiation.

The supports are `[-b,b]`, of length `9/10`. Both sources are smooth after
zero extension, have the two required exponential moments zero, and have
opposite additive parity. Their normalized versions are orthonormal in ordinary
L2. Those moment and parity statements are analytic identities, not numerical
near-zero observations.

## 2. Enclosure method, including the endpoint tails

The interior quadrature stops at `y0=255/256`, where
`v0=65536/511`. It integrates on dyadic subintervals between
`0,1/2,3/4,7/8,...,255/256`. Acb is asked for 110-bit relative and
absolute accuracy at a working precision of 192 bits. Every returned integral
is checked to be finite, and its imaginary part must contain zero.

The callback explicitly returns a nonfinite ball when `1-y²` contains zero.
On every remaining complex box the integrand is holomorphic, so its analytic
claim is justified. This matters because [Acb integration requires the callback
to certify analyticity](https://python-flint.readthedocs.io/en/latest/acb.html).
[FLINT's integration routine](https://flintlib.org/doc/acb_calc.html) supplies
rigorous quadrature remainders. The source endpoint is never passed to this
routine as though the zero-extended bump were analytic there.

For a derivative polynomial `A(v)=sum a_k v^k`, put
`A_abs(v)=sum |a_k|v^k`. Since

\[
\frac{dy}{dv}=\frac1{2v^2\sqrt{1-1/v}}
\le\frac1{2y_0v_0^2}\quad(v\ge v_0),
\]

the contribution of **both** endpoint tails to the squared L2 norm is at most

\[
\frac{b}{y_0v_0^2}
\int_{v_0}^{\infty} e^{-2v}A_{\rm abs}(v)^2\,dv.
\tag{S3}
\]

The analogous bound for the absolute L1 tail replaces `e^(-2v) A_abs²`
by `e^(-v) A_abs`. Both are finite polynomial sums of

\[
I_0(\lambda,v_0)=e^{-\lambda v_0}/\lambda,\qquad
I_k(\lambda,v_0)=e^{-\lambda v_0}v_0^k/\lambda
+(k/\lambda)I_{k-1}(\lambda,v_0).
\tag{S4}
\]

These recurrences are evaluated in Arb; no asymptotic remainder is omitted.
The largest squared-norm endpoint bound among the ten integrals is less than
`2.319e-58`, for the fourth derivative of `q0`. Endpoint errors are therefore
smaller than the returned interior quadrature widths.

For the sharper source L1 calculation, each undifferentiated polynomial in
(S1) has exactly one zero on `v>=1`, lying in `(2,3)`. For `A0`, the
derivative after factoring its negative factor has quadratic `4v²-9v+3`;
the polynomial is positive up to `v=2` and strictly decreasing thereafter.
For `A1` the quadratic is `4v²-9v+1`; the polynomial is positive up to
`v=2`, increases to its unique subsequent local maximum, then decreases to
negative infinity. These observations prove the asserted single crossing.
Exact rational bisection encloses each root in 160 steps. Integration splits
at a dyadic lower bound for its corresponding y-coordinate; the tiny uncertain
split interval is bounded explicitly, and (S4) bounds the omitted endpoint.
This avoids integrating a nonsmooth absolute-value function as if analytic.

## 3. Certified values useful for the compact convolution calculation

The following deliberately rounded upper bounds follow from the full record.
Only the first two columns give normalizations, for which short two-sided
intervals are also stated below.

| Quantity | Source 0 | Source 1 |
|---|---:|---:|
| `N_j` (display only) | 10.9248986768676523 | 4.30234515884263583 |
| `||f_j||_1` upper | 0.653950308086 | 0.686080643314 |
| `||f_j'||_2` upper | 38.141554082954 | 39.766716403986 |
| `||f_j''||_2` upper | 3257.758480203371 | 3474.471369613100 |
| `||f_j'''||_2` upper | 488426.334700442 | 528512.654614686 |
| `||f_j''''||_2` upper | 113400080.431470 | 123889858.276645 |

Safe short normalization intervals are

\[
10.924898676867<N_0<10.924898676869,\qquad
4.302345158842<N_1<4.302345158844.
\]

For any derivative order, compact support gives

\[
\|f_j^{(k)}\|_1\le\sqrt{9/10}\,\|f_j^{(k)}\|_2.
\tag{S5}
\]

In particular, sufficient L1 derivative bounds for the root agent's piecewise
linear convolution error estimate are

| Bound | Source 0 | Source 1 |
|---|---:|---:|
| `||f_j'||_1` upper | 36.184255321 | 37.726019671 |
| `||f_j''||_1` upper | 3090.581059252 | 3296.172957907 |

`source_value(source_id,x,derivative_order=0,normalizer=...)` in the code
accepts a real Arb interval wholly inside or outside the support. It rejects
an interval straddling a support endpoint. `record_ball()` reconstructs the
normalizer from its exact rational enclosure. Supplying the normalizer avoids
repeated record reads during grid sampling. The source module sets the Arb
working precision to 192 bits when imported; callers may subsequently increase it.

## 4. A usable gamma upper bound from the derivative norm

Let `m(t)=Re psi(1/4+it/2)-log pi`, the full multiplier including contact.
For `Re w>0`, [DLMF 5.9.13](https://dlmf.nist.gov/5.9.E13) and

\[
0<\frac1{1-e^{-s}}-\frac1s<1\quad(s>0)
\]

give `|psi(w)-log w|<=1/Re w`. Apply this with
`w=5/4+it/2` and use `psi(z)=psi(z+1)-1/z`:

\[
m(t)\le \tfrac12\log(25/16+t^2/4)+\tfrac45-\log\pi
=c_*+\tfrac12\log(1+4t^2/25),
\]

where `c_*=4/5+log(5/4)-log pi<0`. The scalar inequality is also
certified in the record. Dropping its negative constant yields

\[
\boxed{m(t)\le\tfrac12\log(1+4t^2/25).}
\tag{S6}
\]

For an H1 source `H` with `n=||H||_2²`, `k=||H'||_2²`, Plancherel
and Jensen therefore give

\[
\Gamma[H]\le\frac n2\log\left(1+\frac{4k}{25n}\right).
\tag{S7}
\]

The right side is increasing in both nonnegative variables `n,k` (with its
continuous value zero at `n=0`). Thus separate upper bounds for the two norms
can safely be substituted; an unavailable lower bound for `n` is not needed.

For `H=D_2 f=(I-rU_log2)f`, `r=1/sqrt2`, the norm bounds
`n<=(1+r)²` and `k<=(1+r)² ||f'||²` imply

\[
\Gamma[D_2f]\le
\frac{(1+r)^2}{2}\log\left(1+\frac4{25}\|f'\|_2^2\right).
\tag{S8}
\]

Certified upper values are `7.947518228` and `8.068617397` for the two
sources. Their translated support union is allowed here; (S7) has no short
support hypothesis.

If another part of the audit supplies `E>=||e||_infinity`, calibration and
Young's inequality give the useful conditional bounds

\[
0\le\mathcal B_\infty[D_2 f_0]
\le 7.947518228+1.246266361\,E,
\]
\[
0\le\mathcal B_\infty[D_2 f_1]
\le 8.068617397+1.371739701\,E.
\tag{S9}
\]

The coefficient of E comes from `(1+r)² ||f_j||_1²`, using the sharper
L1 enclosures. The lower bound zero uses the already audited positive Sonin
trace, not an assumption of Weil positivity. These are coarse h0 enclosures;
they are not evaluations of h0 or positive lower bounds for it.

## 5. Fourier tail estimates, if later needed

The same compact support gives, for `k=1,2,3,4`,

\[
|\widehat f_j(t)|\le
\min\{\|f_j\|_1,\sqrt{9/10}\|f_j^{(k)}\|_2|t|^{-k}\}.
\tag{S10}
\]

For `H=D2f`, multiply this bound by `1+r`. The digamma integral also
shows `m(t)>=m(0)>-6`; its scalar value is certified in the record. Combining
this with (S6), for `T>=1`, yields

\[
\int_{|t|>T}|m(t)|\,|\widehat H(t)|^2\frac{dt}{2\pi}
\le\frac{(1+r)^2(9/10)\|f^{(k)}\|_2^2}{\pi}
\frac{T^{1-2k}}{2k-1}
\left(6+\frac12\log\frac{29}{25}+\log T+\frac1{2k-1}\right).
\tag{S11}
\]

The factor `1/pi` includes both Fourier tails and the `1/(2pi)` convention.
For `k=4`, `T=10000`, the two absolute gamma-tail upper bounds are less
than `2.367e-12` and `2.825e-12`. No interior Fourier quadrature has been
performed, so these numbers are tail bounds only. The JSON records additional
choices of k and T.

## Limits

These records certify the actual smooth source norms and supply practical
constants for projection/convolution error estimates. They do not certify the
root agent's trial matrices by themselves. In particular, the h0 bounds in
(S9) still need an independently certified prolate error-kernel bound E, and
using them in a Galerkin residual identity requires outward interval matrix
algebra. The derivative growth is substantial; it must not be suppressed when
estimating interpolation error or replacing these sources by sampled arrays.

The [main enclosure note](SONIN_ACTUAL_PROJECTION_ENCLOSURES_20260929.md) combines these constants with the certified projection bounds. For its sharper one-sided scalar estimate, it uses the cutoff-error bound `||delta||_infinity <= ||C||_1 < 2.858`, not that same bound for the different kernel epsilon.
