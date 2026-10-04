# Natural bounds and prospects for the signed covariance program

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred. Parallel
same-model analysis and cross-review, not independent specialist refereeing.
No new zero-free region, fixed variance exponent, or mathematical priority
is claimed.

This continues the [finite cross-spectrum note](FINITE_CROSS_SPECTRUM_20261004.md)
and its predecessors. The purpose is to investigate the natural bound
before selecting a fixed exponent, zero height, or zero proportion.

## Assessment

The natural object is the **complete signed prepared scalar**, bounded by
a scale-dependent envelope. For local exclusion, a family of prepared
probes adapted to height appears better suited than the original fixed
probe. Any fixed positive power saving would exclude a fixed strip at
every sufficiently large zero height. That is much stronger than an
improvement of a classical shrinking zero-free region.

Four concrete deductions are available:

1. Existing zero-free regions and zero-density estimates already improve
   the asymptotic baseline for this particular smoothed probe substantially.
2. The arithmetic and spectral reductions accommodate a general subpower
   envelope with uniform comparison constants.
3. The fixed detector has a quantitative lower height-decay bound away
   from the critical line.
4. A height-adapted prepared family removes that attenuation at its central
   height, at the cost of growing derivative constants and a complex scalar.

These favor investigation of the quantitative local-detection interface.
They do not yet supply an arithmetic estimate that excludes additional
zeros. Improving the recent zero-proportion papers requires a different
correlation or certificate; a smaller tail in our product spectrum does
not give their missing bound.

## 1. The scalar and its stronger classical benchmark

Retain the fixed probe and notation from the previous notes:

\[
\lambda_V(X)=\frac1{qX^3}\int_X^{2X}xV_g(x)\,dx,\quad q=7/3,
\qquad D(s)=\frac{G(1/2-s)}q\frac{2^{s+2}-1}{s+2}.
\]

Integrating the manuscript's complete explicit formula over the shell
gives, for sufficiently large real X,

\[
\lambda_V(X)=-\sum_\rho m_\rho D(\rho)X^{\rho-1}
+O_g(X^{-3}).                                                \tag{1}
\]

The sum is absolutely convergent and includes both ordinate signs and
all multiplicities. Preparation removes the pole at one. The remainder
includes all trivial zeros. Uniformly over the critical strip,

\[
|G(1/2-\rho)|\ll_g(1+|\gamma|)^{-6},\qquad
|D(\rho)|\ll_g(1+|\gamma|)^{-7}.                               \tag{2}
\]

Suppose an established Korobov--Vinogradov region gives, above some fixed
height,

\[
1-\beta\ge
\frac1{Z(\log|\gamma|)^{2/3}(\log\log|\gamma|)^{1/3}}.           \tag{3}
\]

Define

\[
F(X)=\frac{(\log X)^{3/5}}{(\log\log X)^{1/5}},\qquad
C_p(Z)=\frac52\left(\frac23\right)^{3/5}
\left(\frac53\right)^{1/5}p^{2/5}Z^{-3/5}.                    \tag{4}
\]

**Classical-input corollary for this probe.** For each fixed c<C_6(Z)
and d<C_7(Z),

\[
|V_g(x)|\ll_{g,c}x e^{-cF(x)},\qquad
\mathcal V_g(X)\ll_{g,c}X^3e^{-2cF(X)},                        \tag{5}
\]
\[
|\lambda_V(X)|\ll_{g,d}e^{-dF(X)}.                            \tag{6}
\]

The implied constants and starting thresholds depend on c or d.
These are asymptotic bounds, not explicit finite certificates.

### Proof

Fix a small positive eta. Zeros with beta at most 1 minus eta contribute
O(X^(-eta)) to the normalized response and scalar by (2). In the remaining
thin strip, classical Ingham density gives

\[
N(1-\eta,T)\ll_\eta T^{\theta_\eta}(\log T)^5,\qquad
\theta_\eta=\frac{3\eta}{1+\eta}\longrightarrow0.              \tag{7}
\]

Zeros are counted with multiplicity. A modern primary proof and explicit
version is [Chourasiya--Simonic, Corollary 1](https://arxiv.org/html/2507.15184v2).
No density hypothesis or new density optimization is used.

For a coefficient of order height to the power minus p, logarithmic
height blocks bound the remaining sum by polynomial factors in j times

\[
\exp\left[-(p-\theta_\eta)j-
\frac{\log X}{Z(j+1)^{2/3}(\log(j+1))^{1/3}}\right].           \tag{8}
\]

Finite low-height blocks are power-small. With L=log X, elementary
minimization gives, for fixed k>0,

\[
\inf_{y\ge y_0}
\left\{ky+\frac{L}{Zy^{2/3}(\log y)^{1/3}}\right\}
=\bigl(C_k(Z)+o(1)\bigr)F(X).                                \tag{9}
\]

To check the constant, put y=aF(X); after division by F(X), the
expression tends to ka+Z^(-1)(5/3)^(1/3)a^(-2/3), whose minimum is (4).
Reserve an arbitrarily small fraction of kj to sum the polynomial
factors in (8), then take the fixed eta sufficiently small.
This proves every coefficient below C_p. Use p=6 for V_g(x)/x and
p=7 for lambda_V. Integrating the square over the shell proves (5).
All estimates hold uniformly for sufficiently large real X.

Using only N(T)=O(T log T) instead yields C_(p-1). That weaker
benchmark is valid but discards classical thin-strip density information.

### Size and significance

The valid all-height input Z=53.989 is recorded in
[Lee--Leong, equation (3)](https://arxiv.org/html/2208.06141v5).
[Bellotti, Theorem 1.3](https://arxiv.org/pdf/2306.10680) gives the stronger
asymptotic input Z=48.0718. Its fixed initial height range contributes
only a power-small term here.

| Established input Z | Response threshold C_6 | Scalar threshold C_7 | Variance threshold 2C_6 |
| --- | ---: | ---: | ---: |
| 53.989 | 0.4060058893 | 0.4318282489 | 0.8120117786 |
| 48.0718, sufficiently large heights | 0.4352925886 | 0.4629776100 | 0.8705851772 |

Each threshold must be approached from below. No endpoint big-O claim
is made; the decimals evaluate exact formula (4), without outward rounding.

The manuscript currently gives
X^3 (log X)^(3.602) exp[-0.3706 F(X)] by transferring an explicit
unsmoothed Johnston--Yang PNT error. Equations (5)--(6) substantially
improve its asymptotic comparison for the prepared probe. This is a
project corollary of established theorems, not a new zero-free region.
Broader literature novelty has not been established. The manuscript's
explicit finite-range comparison remains useful because the stronger
asymptotic bound above has no computed starting threshold.

Increasing smoothness can improve these constants while weakening a
fixed probe's sensitivity to high zeros. Thus a better scalar decay
coefficient alone is not evidence of new zero exclusion.

## 2. The arithmetic reduction permits a moving envelope

Let Phi(L) tend to infinity with Phi(L)=o(L), and set

\[
r(X)=e^{-\Phi(\log X)},\quad H=r^{-1/7},\quad
U=\sqrt{X/H},\quad D_{\rm div}=U/H,\quad V=CX/U,
\]
\[
T=H[\log(2X)]^{4/7}.                                        \tag{10}
\]

V denotes the product-support cap, not the second Vaughan cutoff;
both Vaughan cutoffs are U. D_div is the complementary divisor cutoff,
not the detector D(s). All support and strict-cutoff conventions survive.

The explicit estimates in the preceding notes give, directly,

\[
\boxed{\lambda_V(X)=\mathcal C_T(X)+O_g(r(X)),\qquad
\mathcal I_{(D_{\rm div},U]}=-q\mathcal C_T(X)+O_g(r(X)).}       \tag{11}
\]

This does not substitute a moving kappa into a theorem with unchecked
kappa-dependent constants. The uniform budget follows from the original
inequalities:

| Source | Bound under (10) |
| --- | --- |
| Density remainder | H^(-8)=r^(8/7) |
| Stieltjes lower boundary | H^(-7)=r |
| Deleted complementary divisors | (D_div/U)^7=r |
| Mixed scalar Vaughan term | (U^2/X)^7=r |
| Remaining scalar Vaughan term | (U/X)^7(1+log X)=o(r) |
| Inner prime powers | U^(-1/2)log X=o(r) |
| Frequency tail | O(r) |

For the final row, the proved tail is

\[
\ll_g\log(2T)\{\Lambda U^{-1}T^{-6}
+\Lambda^2\mathcal L T^{-7}\},
\quad \Lambda=1+\log V,\quad\mathcal L=1+\log(V/U).
\]

Since Phi=o(log X), all three logarithmic factors are O(log(2X)).
The second term is O(H^(-7)). Relative to H^(-7), the first is
O((H/U)[log(2X)]^(-10/7))=o(1).
Also U^(-1/2)log X=exp[-L/4+Phi(L)/28]L=o(r).

Either sign of the finite signed correlation can therefore be studied
at a general envelope r. Equation (11) does not imply an energy envelope
or a curved zero-free region from a scalar subpower bound. For comparison
error o(r), replace Phi by Phi+B in the cutoffs, where B tends to infinity
and Phi+B=o(L).

The most natural fixed-probe arithmetic question is consequently whether
the **complete signed scalar** can beat the smoothed classical benchmark,
with a proved converse that says what additional zeros that improvement
would exclude.

## 3. Separate envelopes remain weaker than the smoothed benchmark

The aggregate kernel gives a more informative bound than its supremum
version:

\[
|\mathcal I(X;U)|\le c_g\frac{U^6}{X^6}
\int_U^{T_*}t^5r_E(t)\,dt,\quad
T_*=CX/U,\quad |E(t)|\le t r_E(t).                            \tag{12}
\]

If |d log r_E/d log t| is at most a<6 on the retained interval, then

\[
|\mathcal I(X;U)|\le\frac{c_gC^6}{6-a}r_E(T_*).                \tag{13}
\]

Thus the kernel weights the upper complementary scale rather than the
worst lower endpoint. This sharpens the bookkeeping but does not beat
section 1.

The exact mixed-discrepancy identity can multiply proved Mertens and
prime-error envelopes without assuming independence. For classical
stretched exponentials at balanced factors it adds their constants,
with the loss from sampling near sqrt(X). Those bounds still fall below
the direct smoothed benchmark. At a common hypothetical zero mode the
exact identity transmits the original detector coefficient, including
multiplicities; see the
[arithmetic closure note](ARITHMETIC_CLOSURE_ATTEMPT_20261004.md).
Factorwise norms or sign deletion do not supply extra zero exclusion.

## 4. Quantifying the fixed detector

The [one-sided sign gate](ONE_SIDED_SIGN_GATE_20261004.md) proves forced
positive and negative limsup amplitudes m_rho |D(rho)|, but does not give
the first excursion interval. The polynomial probe now yields a matching
lower height-decay order on a right substrip.

Fix b0 in (1/2,1], put d=b0-1/2, a=1/4, and z=1/2-s. For
h(v)=(1-16v^2)^8 on [-a,a], repeated integration by parts gives

\[
H_{\rm probe}(z)=\sum_{j=0}^8c_jz^{-9-j}
\{(-1)^je^{az}-e^{-az}\},\qquad
c_j=8^8(8+j)!\binom8j2^j.                                   \tag{14}
\]

For b0<=beta<=1 the leading difference has modulus at least 2sinh(d/4).
Since c1/c0=144 and subsequent coefficient ratios are at most 70,
the remainder has modulus at most
2c0 cosh(1/8)|z|^(-9)144/(|z|-70). Hence, for

\[
|\gamma|\ge\Gamma_d
:=70+\frac{288\cosh(1/8)}{\sinh(d/4)},
\]

|H_probe(z)| is at least c0 sinh(d/4)|z|^(-9).
Using G(z)=z(z^2-1/4)H_probe(z)/sqrt(nu) and
|2^(s+2)-1|>=2^(b0+2)-1 proves

\[
\boxed{|D(\beta+i\gamma)|\asymp_{g,b_0}|\gamma|^{-7}}
\quad(b_0\le\beta\le1,\ |\gamma|\ge\Gamma_d).                  \tag{15}
\]

For b0=3/4, Gamma_d<4712. The threshold is deliberately crude.

This quantifies detector attenuation. It does not isolate a zero from
other contributions over a chosen finite interval. A single-mode
comparison with e^(-Phi(L)) is therefore not a finite exclusion proof.
Indeed, each fixed zero with beta<1 is eventually smaller than every
such subpower envelope. An asymptotic bound with unspecified constants
and starting threshold cannot exclude that individual finite-height zero.

## 5. A height-adapted prepared family

A more natural local-detection observable can be constructed without
giving up exact removal of the pole at one. For real t define

\[
h_t(v)=h(v)e^{itv},\qquad
N_t=\|-h_t'''+\tfrac14h_t'\|_2,\qquad
g_t=(-h_t'''+\tfrac14h_t')/N_t.
\]

As usual, w_t(u)=u^(-1/2)g_t(-log u).
Its transform is exactly

\[
G_t(z)=z(z^2-\tfrac14)H_{\rm probe}(z+it)/N_t.                 \tag{16}
\]

Thus preparation at z=0, +/-1/2 persists. H_probe has only purely
imaginary zeros, so forbidden off-line zeros are still detected.
Writing a_j=||h^(j)||_2^2 gives the exact normalization

\[
N_t^2=a_0t^6+(15a_1+a_0/2)t^4
+(15a_2+3a_1+a_0/16)t^2+(a_3+a_2/2+a_1/16).                 \tag{17}
\]

In particular N_t=|t|^3||h||_2(1+O(t^(-2))). At a zero with
s=beta+it,

\[
|G_t(1/2-s)|\longrightarrow
H_{\rm probe}(1/2-\beta)/\|h\|_2>0,                          \tag{18}
\]

uniformly for beta in a fixed closed right substrip. The high-height
suppression of the original fixed probe has disappeared at the center.

Remove the shell's additional height suppression by defining

\[
\lambda_t(X)=\frac1{qX^{3-it}}
\int_X^{2X}x^{1-it}V_{g_t}(x)\,dx,\qquad
\ell_t(u)=\int_1^2y^{1-it}w_t(u/y)\,dy.
\]

Then lambda_t=(qX)^(-1)sum Lambda(n)ell_t(n/X), and the detector is

\[
D_t(s)=\frac{G_t(1/2-s)}q
\frac{2^{s+2-it}-1}{s+2-it}.                                 \tag{19}
\]

At s=beta+it, the shell factor is (2^(beta+2)-1)/(beta+2).
Thus the complete central coefficient is bounded away from zero at
large t; there is no residual height-to-the-power-minus-seven penalty.

An effective version already follows from exact rational integration:

\[
|D_t(\beta+it)|>0.36
\qquad(3/4\le\beta\le1,\ |t|\ge100).                           \tag{20}
\]

Indeed, a1/a0=704/5, a2/a0=3666432/65, and
a3/a0=463970304/13. Formula (17) then gives
N_t/(|t|^3 sqrt(a0))<1.11. Exact integration also gives
(integral h)/sqrt(a0)>0.455. The polynomial numerator in (16) has
modulus at least |t|^3, while H_probe(1/2-beta)>=integral h.
Finally (2^(beta+2)-1)/(q(beta+2))>0.89 for beta>=3/4:
use monotonicity and the rational check 6.72^4<2048.
The product 0.455 times 0.89 divided by 1.11 exceeds 0.36.
All inequalities in this conservative certificate reduce to exact
rational comparisons; it does not depend on floating estimates.

This advantage has costs. The scalar is complex, so its modulus, or a
justified pair of real observables, must be studied; the existing one-sided
real Landau proof cannot be inherited automatically. Derivative bounds
grow:

\[
\|D^6 w_t\|_{\rm TV}\ll_h(1+|t|)^6,\qquad
\|D^7\ell_t\|_{\rm TV}\ll_h(1+|t|)^7.                          \tag{21}
\]

For example, scalar Vaughan comparison now costs
O_h((1+|t|)^7X^(-7){U^7(1+log X)+(UV)^7}).
Charging that comparison at e^(-Phi(log X)) suggests balanced cutoffs
of size sqrt(X)(1+|t|)^(-1/2)e^(-Phi/14). All continuum coefficients
must also be recomputed for ell_t. If K(s)=(2^(s+2)-1)/(s+2), then

\[
c_t=\int w_t(u)\log u\,du
=-\frac{H_{\rm probe}(-1/2+it)}{2N_t}\ne0,\qquad
\int\ell_t(u)\log u\,du=c_tK(1-it).                           \tag{22}
\]

Thus the continuum survives and must be retained with this coefficient.
It is not q times the old c_w. The ordinary density moment is still zero.

Equations (16)--(22) establish a detector family and its basic resource
cost. They are not a uniform arithmetic estimate, a completed extension
of every earlier reduction, or a finite zero-exclusion theorem. Zero
clusters and cancellation still require a quantitative localization or
power-sum argument. Nevertheless, this family is more closely aligned
with a height-local bound R(X,t) than merely optimizing the decay constant
of the original fixed scalar.

## 6. Relation to the recent zero-proportion results

[Alpoge--Furman](https://arxiv.org/html/2608.13637v2) and
[Lamzouri](https://arxiv.org/html/2609.02882v2) prove an asymptotic
proportion 0.6725007 of simple zeros on the critical line. Their valid
complex-zero certificates turn a quadratic zero sum Q_pc approximately
equal to 1.327499296 times N into a lower count 2N-Q_pc. Here the sum is
sum K(z-s)^2 over their conjugation-invariant zero multiset, with
multiplicity, not an absolute-square sum. It is distinct from our
covariance Q. Such a result
tolerates a finite exceptional set.

Our cross-spectrum phase is instead exactly

\[
e^{i\tau\log H}(n/U)^{-i\tau}(p/U)^{-i\tau}
=e^{i\tau\log(X/(np))}.                                     \tag{23}
\]

It probes products np with coefficients mu(n)log p/(np). Their
pair-correlation calculation probes ratios n/m with prime-pair
coefficients and averages over zero height. Their normalized support one
is tied to prime-polynomial length comparable to zero height; it is
not our frequency cap T. No transfer theorem between these observables
has been proved.

There is an elementary barrier within the existing support-one family.
For every real f in L^2([-1/2,1/2]) with integral one, let

\[
R(f)=\int f^2+\iint|u-v|f(u)f(v)\,du\,dv.
\]

For the Montgomery--Taylor optimizer
f0(u)=cos(sqrt(2)u)/(sqrt(2)sin(1/sqrt(2))), put h=f-f0 and
P(u)=integral from -1/2 to u of h. Its stationary equation and Dirichlet
Poincare give

\[
R(f)=C_{\rm MT}+\int h^2-2\int P^2
\ge C_{\rm MT}+(1-2/\pi^2)\int h^2,
\quad C_{\rm MT}=1.3274992963205885\ldots.                    \tag{24}
\]

Allowing signed real windows or positive mixtures therefore cannot
improve that functional. This does not prohibit different certificates,
higher moments, or additional arithmetic information.

For finite exclusion, a sufficient gate from this count certificate is
Q_pc<N+2,
because a multiple real zero or an off-line conjugate pair gives at
least two bad zeros counted with multiplicity. An excess of order
0.3275 N is far above that threshold. Merely improving a relative
error does not turn the proportion result into a zero-free window.

## 7. Where the evidence points

The immediate attainable improvement is the stronger asymptotic benchmark
in section 1, together with the uniform subpower localization and explicit
detector lemmas. Their broader novelty needs a separate literature audit.

For a new zero-free result, the most aligned investigation is a
quantitative height-local converse for a prepared response, paired with
an estimate for its **complete signed arithmetic form on the continuous
interval required by that converse**. The height-adapted family makes the
detector side more promising, while exposing the derivative and continuum
costs. A converse must retain other zeros, multiplicities, initial caps,
and all errors, and provide a computable detection interval. None of
these costs can be discharged by finite sign samples.

For a new proportion result, the missing bound instead concerns a
height-averaged prime-pair form beyond known normalized support, or a
different valid complex-zero certificate. That is a distinct program,
and the present product-spectrum reduction supplies no direct advance
on its missing estimate.

The evidence supports further investigation of the local detector and
signed-error interface before choosing numerical targets. There is no
current proof that this interface will beat classical zero-free regions.
A fixed-power saving remains an exceptionally ambitious objective;
a modest nonuniform improvement with a proved quantitative detector
would already be significant.

## Verification and limits

Two parallel same-model analyses independently checked the smoothing
benchmark, thin-strip split, saddle constant, absolute zero sum,
multiplicities, trivial zeros, and uniformity on real shells. The
moving-envelope budget was checked directly against the original
comparison and tail inequalities. The endpoint expansion, coefficient
ratios, modulated transform and norm, and support-one barrier were checked
algebraically. Decimal constants were recomputed from exact formula (4).

No prime-data sweep, finite zero certificate, new arithmetic saving, or
change to the manuscript is made here.
