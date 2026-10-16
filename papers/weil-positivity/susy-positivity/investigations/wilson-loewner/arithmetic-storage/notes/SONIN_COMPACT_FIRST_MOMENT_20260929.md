# Compact boundary formula for the first compressed Sonin moment

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed. Separate same-model agents checked the boundary identity,
polynomial reduction, and spline arithmetic. These are internal checks, not
independent human refereeing.

## Result and scope

For the prescribed real pole-neutral sources, the first positive spectral
moment of the compressed metric admits an independently computable formula

\[
m_1=\operatorname{Tr}(AH)=\mathcal B_\infty[D_2^2F]-\mathcal C[F].
\tag{1}
\]

The correction below consists entirely of compact integrals involving the
actual Sonin projection. It does not replace that projection by a finite
cosine surrogate. The current polynomial resolvent certificate covers its
infinite-dimensional complement. After an explicit polynomial expansion,
all compact integrals become exact exponential moments of cubic source
splines, with the source replacement separately bounded.

This supplies a first-moment bound on the inverse-metric trace. It is not
an arithmetic residual sign theorem. The numerical certificate and its
combination with the second-transport scalar are separate small records.

The completed internal certificates give the following outward-rounded bounds:

| Quantity | Even source f0 | Odd source f1 |
|---|---:|---:|
| h2 = B_infinity[D2^2 F] | [4.49897631, 4.49933979] | [2.88323626, 2.88364295] |
| Compact correction C | [0.73384862, 0.74236061] | [0.21981897, 0.22889718] |
| Actual first compressed moment m1 | [3.75661571, 3.76549116] | [2.65433908, 2.66382398] |
| First-prime trace B2 | [1.03644381, 8.67999475] | [0.79696516, 6.86726714] |
| Complete arithmetic residual Q1-B2 | [-7.24075680, 0.40279415] | [-5.81945856, 0.25084343] |

The B2 interval widths improve from about 22.22 and 16.21 to 7.64 and 6.07.
Both residual intervals still contain zero. The gain comes from actual
projection information in m1; neither extra digits in h0 nor an assumed
arithmetic answer supplies it. The [combined record](../numerics/records/sonin_first_moment_bounds.json)
contains exact rational endpoints. The
[critical review](../reviews/SONIN_FIRST_MOMENT_REVIEW_20260929.md) distinguishes
this result from the missing residual sign theorem.

## 1. Moment and boundary constraints

Write `P=Pi`, `D=I-r U_a`, `r=p^(-1/2)`, `a=log p`, and
`G=D*D=(1+r²)I-r(U_a+U_-a)`. In this note `p=2`. Let

\[
K=C_F^*C_F,\quad A=PGP|_{\operatorname{Ran}P},\quad
W=PD^*C_F^*,\quad H=WW^*=PGKP.
\]

The source is real, so its correlation is real and even. Consequently `K`
commutes with the cosine involution `Fcal`, as do `G` and `P`. The prescribed
even and odd sources both satisfy this condition. Here `Fcal` denotes the
unitary positive-axis transform with kernel `2 cos(2 pi xy)`; it is not the
source `F`.

In the positive-axis model let `chi=1_(0,1)`, `R=I-chi`,
`C=chi Fcal chi`, `M=(I-C²)^(-1)`, and `S=CM`. The boundary map

\[
Q_bh=(\chi h,\chi\mathcal Fh),\quad
Q_bQ_b^*=\begin{pmatrix}I&C\\C&I\end{pmatrix}
\]

has inverse `[[M,-S],[-S,M]]`, since `||C||<1`. The orthogonal complement
of the Sonin projection is therefore

\[
I-P=Q_b^*\begin{pmatrix}M&-S\\-S&M\end{pmatrix}Q_b.
\tag{2}
\]

Using bounded-factor cyclicity with the smoothed trace-class products,

\[
\begin{aligned}
m_1&=\operatorname{Tr}(PGPGKP),\\
h_2&=\operatorname{Tr}(PG^2KP)=\mathcal B_\infty[D^2F],\\
\mathcal C&=h_2-m_1
=\operatorname{Tr}(PG(I-P)GKP).
\end{aligned}
\tag{3}
\]

Define `L=chi G R` and `X=chi G K R`. Because `P` has zero physical and
Fourier restrictions to `(0,1)`, the boundary rows are

\[
Q_bGP=(LP,L\mathcal FP),\qquad Q_bGKP=(XP,X\mathcal FP).
\]

Substitution into (2) gives the signed compact formula

\[
\boxed{\mathcal C=2\operatorname{Tr}(MXPL^*-SXP\mathcal FL^*).}
\tag{4}
\]

There is no positivity assertion about `C`. This is the boundary expression
for a difference of two positive moments.

## 2. Compact supports and projection kernels

The physical dilation gives

\[
(Lh)(u)=-h(pu)\,1_{(1/p,1)}(u),\quad
(L^*v)(x)=-p^{-1}v(x/p)\,1_{(1,p)}(x).
\tag{5}
\]

In particular `||L||=r`; changing `x=pv` in a kernel composition cancels
the factor `p^(-1)` in `L*`.

Let `kappa= kappa_(DF)`; equivalently

\[
\kappa(t)=(1+r^2)\kappa_F(t)
-r\{\kappa_F(t-a)+\kappa_F(t+a)\}.
\]

Then

\[
X(u,x)=\frac{\kappa(\log(u/x))}{\sqrt{ux}},\quad 0<u<1<x.
\tag{6}
\]

If the source support of `F` has diameter `L0`, its correlation support
lies in `[-L0,L0]`. All nonzero values in (6) lie in
`u>=exp(-L0)/p`, `x<=p exp(L0)`. The diagonal variables introduced
by `L*` additionally lie in `1<=y<=p`. Thus no spatial tail remains in (4).

For `x,y>1`, the kernels required by (4) are

\[
P(x,y)=\delta(x-y)-4\int_0^1\!\int_0^1
\cos(2\pi xu)M(u,v)\cos(2\pi vy)\,du\,dv,
\tag{7}
\]
\[
(P\mathcal F)(x,y)=2\cos(2\pi xy)+4\int_0^1\!\int_0^1
\cos(2\pi xu)S(u,v)\cos(2\pi vy)\,du\,dv.
\tag{8}
\]

The plus sign in (8) follows from `chi Fcal R Fcal R=-C chi Fcal R`.
The nuclear property needed for the traces follows directly by factoring
`X=chi G C_F* J C_F R`, where in logarithmic coordinates
`J=1_(-b,a+b)` and `supp F subset[-b,b]`. Both localized factors are
Hilbert–Schmidt and

\[
\|X\|_1\le(1+r)^2(a+2b)\|F\|_2^2.
\tag{9}
\]

## 3. Polynomial blocks and exponential moments

Represent the certified inverse by `Mtilde=I+E(R32-I)E*`, and the smoothed
inverse by `Stilde=E(C32 R32)E*`, where `E` is the normalized even-Legendre
basis. Convert their finite kernels to monomials:

\[
Mtilde-I=\sum R_{ij}v^{2i}u^{2j},\qquad
Stilde=\sum S_{ij}v^{2i}u^{2j}.
\]

Use `t_k=2(-1)^k(2pi)^(2k)/(2k)!`, `0<=k<K0`, to approximate each cosine
kernel by its Taylor polynomial. Put `V_(k,i)=1/(2k+2i+1)` and
`D_(k,l)=1/(2k+2l+1)`. The *subtracted* kernel in (7), denoted `Apoly`,
and the full kernel in (8), denoted `Bpoly`, have coefficient matrices

\[
A_{kl}=t_kt_l\{D_{kl}+(VRV^T)_{kl}\},\qquad
B_{kl}=t_k\delta_{kl}+t_kt_l(VSV^T)_{kl}.
\tag{10}
\]

Thus `P=delta-Apoly` up to the explicitly bounded errors, and
`P Fcal=Bpoly` up to those errors. The distinction fixes all signs below.

Define `I_lambda(c,d)=int_c^d kappa(t) exp(lambda t)dt`. Write
`lambda_plus=2j+1/2`, `lambda_minus=-2i-1/2`, and `dij=2i+2j+1`.
The substitution `x=u exp(t)` in (6) yields

\[
J_{ij}:=\int_0^1\!\int_1^\infty
X(u,x)u^{2i}x^{2j}\,dx\,du
=\frac{I_{\lambda_+}(0,\infty)-I_{\lambda_-}(0,\infty)}{d_{ij}}.
\tag{11}
\]

Two restricted rectangles also occur:

\[
J^{\rm upper}_{ij}:=\int_0^1\!\int_1^p X(u,x)u^{2i}x^{2j}\,dx\,du
=\frac{I_{\lambda_+}(0,a)-I_{\lambda_-}(0,a)
+(p^{d_{ij}}-1)I_{\lambda_-}(a,\infty)}{d_{ij}},
\tag{12}
\]
\[
J^{\rm lower}_{ij}:=\int_{1/p}^1\!\int_1^\infty X(u,x)u^{2i}x^{2j}\,dx\,du
=\frac{I_{\lambda_+}(0,a)-I_{\lambda_-}(0,a)
+(1-p^{-d_{ij}})I_{\lambda_+}(a,\infty)}{d_{ij}}.
\tag{13}
\]

All integrals at infinity actually stop at the compact correlation support.
With `Vstrip_q=(1-p^(-2q-1))/(2q+1)`, expansion of (4) is

\[
\begin{aligned}
\mathcal C={}&-2ar\,\kappa(a)
+2\sum_{k,l}A_{kl}p^{2l}J^{\rm lower}_{l,k}
-2\sum_{i,j}R_{ij}p^{-2i-1}J^{\rm upper}_{j,i}\\
&+2\sum_{i,j,k,l}(R_{ij}A_{kl}+S_{ij}B_{kl})
p^{2l}Vstrip_{i+l}J_{j,k},
\end{aligned}
\tag{14}
\]

up to the model replacement errors. Matrix multiplication implements the
last coefficient as `2(R.T strip A.T+S.T strip B.T)` with
`strip_(i,l)=p^(2l)Vstrip_(i+l)`. This leaves 240 exponent values for
`K0=120`, with coefficients multiplying whole-half-line and before-`a`
integrals. No positive or negative contribution is discarded.

## 4. Analytic error budget

The inherited certificate gives operator error `eM<9.2e-32` for `Mtilde`
and trace-norm, hence operator, error `eS<2.7e-31` for `Stilde`. Formulae
(7)–(8) give global projection errors at most `eM` and `eS`. Replacing the
outer and inner operators successively bounds their contribution by

\[
2r\|X\|_1\{e_M(1+\|Mtilde\|)+e_S(1+\|Stilde\|)\}.
\tag{15}
\]

For the cosine truncation use the real Taylor remainder
`delta(z)=2 z^(2K0)/(2K0)!`. On `1<=x<=Xmax=p exp(Lh)` and `1<=y<=p`,
let `dx=delta(2pi Xmax)`, `dy=delta(2pi p)`, and
`dc=delta(2pi p Xmax)`. The kernel errors in (7) and (8) are at most

\[
e_P=\|Mtilde\|(2d_x+2d_y+d_xd_y),\quad
e_J=d_c+\|Stilde\|(2d_x+2d_y+d_xd_y).
\]

Their compact operator errors are bounded by these quantities times
`sqrt((Xmax-1)(p-1))`. Equation (4) then bounds the resulting scalar error
by `2r||X||1 sqrt(area)(||Mtilde||eP+||Stilde||eJ)`. With `Lh<=.901`,
`K0=120`, and the fixed polynomial block, (15) is below `4.155e-26`, and
the cosine error is below `1.042e-33` for unit source norm.

Let `Fh` be the piecewise linear source on spacing `h=a/N`, with all node
coefficients rounded to multiples of `2^-80`. Cellwise Dirichlet inversion
of the second derivative gives

\[
\eta_2:=\|F-F_h\|_2
\le\frac{h^2}{\pi^2}\|F''\|_2+\sqrt{L_h}\,e_{\rm node}.
\tag{16}
\]

The exact compact source is smooth across its zero extension. Its certified
global second derivative and normalization include both endpoint tails.
The same localized factorization as (9) shows

\[
\|X_F-X_{F_h}\|_1
\le(1+r)^2(a+L_h)\eta_2(2+\eta_2).
\]

Since the exact `P` and `P Fcal` have norm at most one, and
`||M||,||S||<=gamma^-1`, `gamma=57/10^6`, source replacement in (4) is
at most `4r gamma^-1` times this trace-norm bound. The model errors are
separately multiplied by `(1+eta2)^2`, because they are evaluated on `Fh`.

The exact integer autocorrelation of the quantized source coefficients
gives its cubic spline correlation. The
[exact truncated-spline formulas](SONIN_TRUNCATED_SPLINE_INTEGRALS_20260929.md),
implemented in `arithmetic_truncated_spline.py`, integrate that correlation against each exponential exactly using Arb
arithmetic, including the corner at zero and at `a=Nh`. The shifts in `D`
are integer shifts on this grid. Arithmetic radii are retained through the
large intermediate cancellations. The interval width requirement is a
check of the resulting proof bounds, not a comparison between resolutions.

## 5. Reproduction and implications

The implementation is split into `moment_kernel_polynomial.py` (equations
(10)–(15)), `arithmetic_truncated_spline.py` (exact spline moments), and
`moment_compact_certificate.py` (source replacement, accumulation, record).
The separate `moment_compact_diagnostic.py` used floating compact quadrature
to check signs and scale; its output is explicitly not a certificate.

The polynomial driver accepts `--numerics` to locate the inherited source
and prolate tools. Its small record stores hashes, parameters, rational
endpoints, and separate source/operator/cosine errors. Large temporary
arrays are regenerated and not retained. For the exact first moment,
subtract the correction interval from the independently enclosed scalar
`B_infinity[D2^2F]`. Only then apply the positive spectral-measure bounds
to `B2`; do not substitute the directly known arithmetic form for a missing
transport trace.

## 6. The extra scalar and direct arithmetic controls

The new scalar generator
[sonin_second_transport_scalar.py](../numerics/sonin_second_transport_scalar.py)
extends the [audited scalar method](SONIN_SCALAR_TRACE_CALCULATION_20260929.md)
to D2 squared. Its Fourier multiplier is G squared. On correlations,

\[
G^2=\frac{13}{4}I-3r(U_a+U_{-a})+\frac12(U_{2a}+U_{-2a}).
\]

The source diameter becomes 0.9+2log2; the L1 and derivative bounds acquire
the factor (1+r)^2. The gamma FFT retains the original source alias bound
before applying the exact squared multiplier, and bounds the entire
frequency and Poisson tails for the enlarged support. The epsilon
source-replacement and kernel errors acquire the factor (1+r)^4. The
principal epsilon calculation uses grid 65536, 144 cosine terms and 768-bit
Arb arithmetic; the gamma calculation uses the inherited period 48,
2^18-point FFT and frequency cutoff 5000. Its h2 widths are below 0.001.
A grid 32768/896-bit replay yields overlapping intervals; agreement does
not replace any analytic error estimate.

The independently computed prime correlations and inherited gamma intervals
give Q1[f0] in [1.439237951,1.439237964] and Q1[f1] in
[1.047808580,1.047808594]. See the
[arithmetic and finite-defect note](SONIN_FINITE_MELLIN_DEFECT_20260929.md).
These direct values serve as controls and a target scale. They are not
used to define the finite-place trace or its compressed moment.

## 7. Positive-measure bounds and their information limit

Let m=(1-r)^2 and M0=(1+r)^2; this M0 is the upper bound for A, not the
prolate inverse M used above. Since H is positive trace class,

\[
\nu_F(E)=\operatorname{Tr}(E_A(E)H)\ge0,
\quad\nu_F([m,M_0])=h_0,
\quad\int\lambda\,d\nu_F=m_1,
\quad B_2=\int\lambda^{-1}\,d\nu_F.
\]

The trace is positive without assuming that H commutes with the spectral
projections. Cauchy--Schwarz and the chord bound for 1/lambda imply

\[
\boxed{\frac{h_0^2}{m_1}\le B_2\le
\frac{(m+M_0)h_0-m_1}{mM_0}.}
\tag{17}
\]

The [combiner](../numerics/sonin_first_moment_bounds.py) propagates all
outward input errors and intersects (17) with the earlier valid bounds.
It checks generator and input hashes before using them. Residual intervals
are obtained only after the independent B2 enclosure has been constructed.

These bounds are optimal for positive measures given only mass, mean, and
the interval [m,M0]. For mu=m1/h0, the point mass h0 delta_mu attains the
lower bound; the measure

\[
h_0\left(\frac{M_0-\mu}{M_0-m}\delta_m+
\frac{\mu-m}{M_0-m}\delta_{M_0}\right)
\]

attains the upper bound. Convex mixtures retain mass/mean and fill the
intervening inverse-moment interval. The records certify that, for every
exact mass/mean pair in the present enclosures, the lower extremum is
strictly below the corresponding Q1 and the upper extremum strictly above.
Thus additional precision in h0 and m1 alone cannot decide these residual
signs using only this positive-measure information. These extremizing
measures are generic controls, not actual Sonin counterexamples.

There is a related algebraic example showing that additional uncompressed
scalars do not generically substitute for compressed information. Fix alpha=h0/b in (m,M0), w=(M0-alpha)/(M0-m),
and k>0. In each of N three-dimensional blocks choose

\[
G=\operatorname{diag}(g_0,m,M_0),\quad
K=\operatorname{diag}(0,k,k),\quad
v=(\sqrt{1-\epsilon},\sqrt{\epsilon w},
\sqrt{\epsilon(1-w)}),\quad P=|v\rangle\langle v|,
\quad\epsilon=b/(Nk).
\]

For N large enough epsilon is at most 1. All scalars
Tr(PG^jKP)=b(wm^j+(1-w)M0^j), summed over blocks, are independent of
g0 and N. The inverse compressed trace nevertheless equals
h0/((1-epsilon)g0+epsilon alpha). Taking g0=m or M0 and N large approaches
both mass-only bounds. This is an obstruction to an inference from generic
commuting positive operators; it makes no assertion about which values the
actual Sonin projection can attain. Formula (4) supplies the missing
projection information for the present calculation.

## 8. Decision and reproducibility

The bounded first-moment task is complete. Do not spend further precision
merely shrinking the present intervals: the information limit above persists
even for exact mass and mean. The next numerical ingredient must be an
additional compressed moment, a source-adapted inverse calculation, or a
new constraint on the source spectral measure. Its budget should be tied
to a candidate residual inequality. The all-source signed comparison and
the passage to unbounded support remain open.

The [structural companion](SONIN_FINITE_MELLIN_DEFECT_20260929.md) identifies what a finite Mellin penalty would
require: positivity on the constrained subspace and bounded cross terms
in that residual seminorm. Neither condition is established for the Sonin
residual by the present calculation. The mean-only proposal remains
undecided on the odd test, which is exactly mean-zero.

From the numerics directory, use Python with python-flint 0.9.0, without
-O/-OO, and direct replay outputs outside the repository:

```sh
python -B sonin_second_transport_scalar.py --output /tmp/sonin-h2-replay.json
python -B moment_compact_certificate.py --bits 1152 --output /tmp/sonin-correction-replay.json
python -B arithmetic_prime_diagnostic.py --numerics . --output /tmp/sonin-prime-replay.json
python -B arithmetic_truncated_spline_check.py --output /tmp/sonin-spline-check.json
python -B sonin_first_moment_bounds.py --h2 /tmp/sonin-h2-replay.json --correction /tmp/sonin-correction-replay.json --prime /tmp/sonin-prime-replay.json --output /tmp/sonin-moment-bounds-replay.json
```

The last command verifies record bindings and recomputes the displayed
implications. No grid arrays are retained; only small scripts, source/error
parameters, hashes and records are saved. This continuation creates no
manuscript snapshot, commit, or push. CCM remains temporarily closed.
