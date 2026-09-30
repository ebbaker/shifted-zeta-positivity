# Certified scalar Sonin traces for the two prescribed sources

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
not exposed. Separate same-model agents derived and reviewed the gamma
calculation, epsilon calculation, and project implications. This is internal
mathematical and computer-assisted evidence, not independent human refereeing.

## Outcome

The scalar calculation requested by the
[previous handoff](SONIN_CONTINUATION_AFTER_ENCLOSURE_TEST_20260929.md)
is complete. Both the unshifted scalar `B_infinity[F]` and the prime-2-transformed
scalar `h0=B_infinity[D2 F]` have been evaluated for each exact prescribed
source, with full contact, source approximation, quadrature alias, and operator
tail errors included. Every final trace interval has width below `10^-5`.
The finite-place positive trace `B2` is still only bounded, not accurately
evaluated. No arithmetic residual sign or new positivity interval is claimed.

The exact source definition is unchanged: `b=9/20`,
`phi(x)=exp(-1/(1-(x/b)^2))` on `|x|<b`, zero otherwise,
`P=-d²/dx²+1/4`, `f0=P phi/||P phi||2`, and
`f1=P(x phi)/||P(x phi)||2`. The sources are compact smooth, unit normalized,
opposite in additive parity, and pole-neutral. Put
`D2=I-2^(-1/2) U_log(2)` with `U_a F(x)=F(x-a)`.

The following decimal intervals are rounded outward from the stored rational endpoints.

| Exact input `H` | `Gamma[H]` | `E_infinity[H]` | `B_infinity[H]` |
|---|---:|---:|---:|
| `f0` | `[1.248341068, 1.248341081]` | `[-0.10998984, -0.10998715]` | `[1.13835123, 1.13835393]` |
| `D2 f0` | `[2.159676398, 2.159676418]` | `[-0.18414608, -0.18413828]` | `[1.97553031, 1.97553814]` |
| `f1` | `[1.337814761, 1.337814775]` | `[-0.14145256, -0.14144956]` | `[1.19636220, 1.19636522]` |
| `D2 f1` | `[1.591820918, 1.591820939]` | `[-0.13477771, -0.13476898]` | `[1.45704321, 1.45705196]` |

The error-kernel contributions are negative for all four tested inputs.
This is compatible with the positive Sonin trace, which is the sum of gamma
and epsilon. It gives no sign for the complete arithmetic residual, which
also includes the finite-place trace increment and prime-power terms.
The subtraction is numerically moderate for these sources; the resolvent's
large norm does not produce catastrophic cancellation in these four scalars.

## 1. Calibration and certified input

Use the Fourier and state-space conventions of the
[canonical audit](SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md):

\[
\mathcal B_\infty[H]=\Gamma[H]+\mathcal E_\infty[H],\qquad
\mathcal E_\infty[H]=\int_{\mathbb R}\kappa_H(t)\epsilon(e^{|t|})\,dt,
\]
\[
\Gamma[H]=\int_{\mathbb R}
\bigl(\Re\psi(1/4+it/2)-\log\pi\bigr)|\widehat H(t)|^2\frac{dt}{2\pi}.
\tag{1}
\]

The cosine cutoff is `C=chi F chi`, with `chi=1_(0,1)`, `R=I-chi`,
`M=(I-C²)^(-1)`. The previous
[prolate certificate](SONIN_PROLATE_RESOLVENT_CERTIFICATE_20260929.md)
gives `I-C² >= gamma I`, `gamma=57/10^6`, `||C||1<2.858`,
and a fixed polynomial smoothed resolvent `S32=C32 R32` with

\[
\|CM-S_{32}\|_1<2.7\,10^{-31}.
\tag{2}
\]

Here `R32` denotes the certified inverse approximant on the polynomial block;
it is different from the spatial projection `R`. The
[source certificate](SONIN_SOURCE_NORM_CERTIFICATES_20260929.md)
supplies normalization and derivative bounds including both endpoint tails.
The new programs check the source program/record hashes. They do not replace
the exact sources by a different bump family.

## 2. Full gamma/contact calculation by Poisson summation

Let `m(t)=Re psi(1/4+it/2)-log pi` and
`w(x)=exp(-x/2)/(1-exp(-2x))` for positive `x`. The digamma difference
integral gives

\[
m(t)-m(0)=2\int_0^\infty w(x)(1-\cos(tx))\,dx.
\tag{3}
\]

Away from zero, the inverse Fourier transform of `m` is `-w(|x|)`.
The local distribution at zero is retained by evaluating the full multiplier
`m` at every Fourier node, including its `-log pi` contact. If the correlation
support of `H` lies in `[-L,L]`, then, for `|x|>L`,

\[
\mathcal F^{-1}(m|\widehat H|^2)(x)
=-\int\kappa_H(u)w(|x-u|)\,du.
\tag{4}
\]

With spatial period `P0>L`, Poisson summation bounds the difference between
the gamma integral and the infinite Fourier trapezoid by

\[
\frac{2\|H\|_1^2\exp((L-P_0)/2)}
{(1-\exp(-P_0/2))(1-\exp(-2(P_0-L)))}.
\tag{5}
\]

The calculation uses `P0=48`, `2^18` spatial samples, spacing
`h_gamma=3/16384`, and Fourier spacing `2pi/48`. It keeps frequency nodes
through `T=2pi*38197/48`, just below `5000`. An Arb complex FFT packs the
real even and odd source arrays; conjugate symmetry recovers their separate
transforms. The prime transform is applied exactly through
`|1-r exp(-it log2)|²=3/2-sqrt(2) cos(t log2)`.

Write `Omega=2pi/h_gamma` and `A4=||F''''||1`. Poisson summation for
source sampling and `|Fhat(t)|<=A4 |t|^-4` bound every retained Fourier
sample's alias error by

\[
\delta_F\le\frac{A_4\pi^4}{45(\Omega-T)^4}.
\tag{6}
\]

Indeed `Omega>2T`, and the two-sided reciprocal-fourth-power sum is
`2 zeta(4)=pi^4/45`. Every transform value is inflated by this error
before squaring. For `H=D2F` the exact positive transport multiplier is
applied to that enclosed square; no separate sampled shifted bump is used.

The remaining **discrete** Fourier tail is bounded by the decreasing
continuous majorant

\[
\frac{\|H''''\|_1^2}{\pi}\frac{T^{-7}}7
\left(6+\tfrac12\log(29/25)+\log T+\tfrac17\right).
\tag{7}
\]

This follows from the already proved multiplier bounds and the integral
test, with the first omitted frequency beyond `T`. It bounds the tail of
the infinite trapezoid sum; (5) separately relates that sum to the integral.
For the shifted source, `||H^(k)||1 <= (1+r)||F^(k)||1` and
`L=9/10+log2`. Thus no Fourier or source endpoint tail is omitted.
At 128-bit Arb precision, final gamma widths are below `2e-8`.

## 3. Polynomial/exponential representation of epsilon

For `rho>=1`, the audited kernel is

\[
\epsilon(\rho)=\operatorname{Tr}(CM B_\rho),\qquad
B_\rho=\chi\vartheta(\rho^{-1})R\mathcal F\chi.
\tag{8}
\]

Its kernel on the unit square is
`2 sqrt(rho) 1_(x>1/rho) cos(2pi rho x y)`, and `||B_rho||<=1`.
Consequently (2) is a uniform error bound in `rho`. It becomes at most
`2.7e-31 ||H||1²` after correlation integration. This is **epsilon**, not
the different cutoff delta kernel used for the previous coarse upper bound.

Write the finite smoothed kernel in monomials,

\[
S_{32}(x,y)=\sum_{i,j=0}^{31}t_{ij}x^{2i}y^{2j}.
\]

The coefficients come from the normalized even Legendre basis by exact
rational polynomial conversion and Arb matrix arithmetic. Truncate the
cosine after `K=80` terms. For `t>=0`, integrating the two monomials gives

\[
e_K(t)=\sum_{k=0}^{K-1}a_k e^{(2k+1/2)t}
-\sum_{j=0}^{31}b_j e^{-(2j+1/2)t},
\tag{9}
\]
\[
a_k=\frac{2(-1)^k(2\pi)^{2k}}{(2k)!}
\sum_{i,j}\frac{t_{ij}}{(2i+2k+1)(2j+2k+1)},
\]
\[
b_j=\sum_{i,k}\frac{2(-1)^k(2\pi)^{2k}t_{ij}}
{(2k)!(2i+2k+1)(2j+2k+1)}.
\tag{10}
\]

In particular the two sums agree at `t=0`, as required by `epsilon(1)=0`.
The working interval includes the slightly extended spline support and has
`rho_max<4.92`. The real cosine Lagrange remainder supplies the simple bound

\[
\|B_\rho-B_{\rho,K}\|
\le 2\sqrt{\rho_{\max}}
\frac{(2\pi\rho_{\max})^{2K}}{(2K)!}.
\tag{11}
\]

The unit-square Hilbert–Schmidt bound suffices here. Multiply (11) by
`||S32||1 <= (2.858+1.5e-40)||R32||F` and add (2).
The resulting uniform kernel error is below `2.701e-31`.
This is an analytic remainder bound, not a comparison of sampled kernels.
The finite exponential sum has substantial intermediate cancellation;
512-bit Arb arithmetic propagates it, and its arithmetic radii are much
smaller than the source approximation error.

## 4. Exact integration against a source spline

Use `h=log2/262144` and the continuous linear interpolant
`Fh(t)=sum c_k beta1(t/h-k)` on the full source support, with zero exterior
nodes. Here `beta1` is the centered unit hat. Each coefficient is rounded
to an integer multiple of `2^-80`; its rounding error is explicitly added.
The grid endpoints are checked in Arb to lie outside the exact source support.
For every source,

\[
\eta_F:=\|F-F_h\|_1
\le\frac{h^2}{8}\|F''\|_1+\eta_{\rm round}.
\tag{12}
\]

The interpolation term is the L1 norm of the Dirichlet Green kernel on each
cell. The full `F''` bound applies across the smooth zero extension.
The normalizer's interval uncertainty is retained in every nodal sample.
For `H=D2F`, `||H-D2Fh||1 <= (1+r) eta_F`.

If the integer source coefficients are `v_k`, form their autocorrelation
`a_m=sum v_k v_(k+m)` by **exact integer polynomial multiplication**.
Then

\[
\kappa_{F_h}(t)=\frac h{2^{160}}
\sum_m a_m\beta_3(t/h-m),
\tag{13}
\]

where `beta3=beta1*beta1` is the centered cubic B-spline. Negative indices
have `a_-m=a_m`. For the transformed source, replace its coefficient by

\[
\tfrac32a_m-r(a_{|m-N|}+a_{m+N}),\qquad N=262144.
\tag{14}
\]

This shift is exact because `Nh=log2`. Large arrays are temporary, regenerable
data and are not saved in the repository; the small record stores their hash.

For a single exponential `exp(lambda |t|)`, set `q=lambda h` and
`A(z)=sum_(m>=0) a_m z^m`. Exact integration of (13) is

\[
\frac{h^2}{2^{160}}\left[
K_4(q)\{2A(e^q)-a_0\}+a_0c_0(q)+2a_1c_1(q)\right],
\tag{15}
\]
\[
K_4(q)=\left(\frac{\sinh(q/2)}{q/2}\right)^4,
\quad c_0(q)=2\sum_{n\ge1\;\mathrm{odd}}
\frac{(2^{n+4}-4)q^n}{(n+4)!},
\quad c_1(q)=2\sum_{n\ge1\;\mathrm{odd}}\frac{q^n}{(n+4)!}.
\tag{16}
\]

Only the splines centered at 0 and ±1 cross the absolute-value corner;
`c0,c1` are their exact corrections. Their series are summed through `n=81`
and bounded geometrically from `n=83`, using `|q|<1`. The polynomial
`A(e^q)` is evaluated in Arb, not a floating FFT. Applying (15) to every
term of (9) gives the enclosed finite-spline epsilon scalar.

The previous spectral expansion, with its normalized exterior vectors, gives

\[
\|\epsilon\|_\infty\le\frac{\|C\|_1}{\sqrt\gamma}<378.552.
\]

Young's inequality therefore bounds replacement of the exact source by

\[
|\mathcal E[H]-\mathcal E[H_h]|
\le378.552\,\eta_H(2\|H\|_1+\eta_H).
\tag{17}
\]

The program uses the sharper Arb value `2.858/sqrt(gamma)`. Kernel errors
are separately multiplied by `(||H||1+eta_H)²`. Source interpolation dominates
the final error; the resolvent and cosine errors are far smaller. A tighter
scalar target would require better source integration, not more precision
in the already certified resolvent.

## 5. Consequence for the existing Galerkin calculation

Keep the previous actual Sonin synthesis `Q=(q20,q24)` and compressed
metric `A=Pi D2*D2 Pi`. Put `m=(1-r)²`, `M=(1+r)²`.
The previous finite matrices already enclosed `B_N` and the finite correction
`c_N` in

\[
\|\mathcal R_N\|_{\rm HS}^2=h_0+c_N,
\quad
\frac{\|\mathcal R_N\|_{\rm HS}^2}{M}
\le\mathcal B_2-B_N
\le\frac{\|\mathcal R_N\|_{\rm HS}^2}{m}.
\tag{18}
\]

Substituting the new `h0` sharply encloses this **Hilbert–Schmidt residual**.
The bounds may also be intersected with `h0/M <= B2 <= h0/m`.
They do not evaluate `B2`, whose inverse-metric dependence remains unresolved.

| Source | Full HS residual squared | Missed positive trace, lower bound | Captured fraction, upper bound |
|---|---:|---:|---:|
| `f0` | `[1.96366722, 1.96368662]` | `>0.67382` | `<1.090%` |
| `f1` | `[1.43298544, 1.43300960]` | `>0.49172` | `<2.422%` |

For reference, the resulting coarse first-prime trace enclosures are
`[0.68124, 22.89784]` and
`[0.50392, 16.71659]`.

These stronger figures explain the earlier omitted-direction test: projection
accuracy was excellent, but this trial choice captured very little of the
source's smoothed trace. The source-specific improvement does not change the
scope of the earlier negative result, nor provide a signed arithmetic bound.

## 6. Reproduction, review, and next task

The new small programs and records are:

- [gamma_scalar_certificate.py](../numerics/gamma_scalar_certificate.py) and [gamma record](../numerics/records/gamma_scalar_certificate.json).
- [sonin_scalar_epsilon.py](../numerics/sonin_scalar_epsilon.py) and [epsilon record](../numerics/records/sonin_scalar_epsilon.json).
- [sonin_scalar_summary.py](../numerics/sonin_scalar_summary.py) and [combined record](../numerics/records/sonin_scalar_summary.json).

Run from `numerics/` with Python and `python-flint 0.9.0`:

```sh
python -B gamma_scalar_certificate.py
python -B sonin_scalar_epsilon.py
python -B sonin_scalar_summary.py
```

All defaults use sibling source/prolate scripts and `records/`. Do not use
`-O` or `-OO`, because the inherited source certificate contains assertions.
Rational endpoints, not rounded displays, specify the stored enclosures.
The combined program verifies generating-script and input hashes and checks
positivity and the `10^-5` scalar-width requirement. Hashes identify inputs;
the interval arithmetic and analytic remainders establish the inequalities.

The [critical review](../reviews/SONIN_SCALAR_TRACE_REVIEW_20260929.md)
records separate checks and the distinction between replay and proof.
The base [project summary](../PROJECT_SUMMARY.md) consolidates the broader
investigation and now supersedes the previous handoff's scalar task.

The next task is to construct trial vectors from the **smoothed source response**
and prove that they capture a specified share of `h0`, or otherwise evaluate
the inverse-metric first-prime trace through controlled return moments.
Choose an accuracy budget tied to that trace scale. An accurate `B2` would
permit a complete residual diagnostic for these inputs; an all-source,
all-support signed estimate would still be needed for the program's main goal.
Keep CCM temporarily closed and the completed finite Weil certificates intact.
