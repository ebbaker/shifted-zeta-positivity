# Zero deflation and rational resolution: quantitative costs

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded session metadata. Separate same-model derivations
and [internal review][review]; no specialist review or priority claim.

**Outcome:** explicit bounds for justified subtraction of neighboring
zeros; a sharp asymptotic for the actual undeleted Poisson tail; and the
fully optimized failure scale of a specified rational-kernel absolute
prime bound. No original multiple zero, height interval, strict cap
surplus or negative Gaussian deficit is obtained.

This continues [Notes 01–03][notes] under the unchanged [program][program].
The [result index][results], [collision controls][controls] and
[avoid index][avoid] apply, especially [equivalent targets][a01],
[control premises][a02], [scoped exclusions][a07],
[separate payments][a12] and [gain before expansion][a20]. The new
quantitative statements are (6), (9), (18) and (22), together with the
certification errors. They assess named estimating classes; they are
not universal obstructions to using signed arithmetic or zero data.

## 1. Normalization and legitimate subtraction

Assume RH. The nontrivial zeros are `1/2+i lambda`, with arbitrary
multiplicities `m_lambda`; the heat coordinate is `x=2 lambda`, since
`8H(0,x)=xi(1/2+ix/2)`. Fix a target ordinate `gamma>0`, whose unknown
multiplicity `m=m(gamma)` may initially be zero. For `delta>0` set
\[
 K_\delta(r)=\frac{\delta^2}{\delta^2+r^2},\qquad
 B_\delta(\gamma)=\sum_\lambda m_\lambda K_\delta(\lambda-\gamma).
\]
For `delta>1/2`, this is exactly
`delta Re(xi'/xi)(1/2+delta+i gamma)` and has the completed Euler-series
identity in Note 01. All sums count both signs and full multiplicities.

Let `A_gamma(r)=sum_{0<|lambda-gamma|<=r} m_lambda` be the **noncentral**
radial count. Integration by parts gives
\[
 B_\delta-m=2\delta^2\int_0^\infty
 \frac{rA_\gamma(r)}{(\delta^2+r^2)^2}\,dr.                \tag{1}
\]
The positive weight has total mass one. Hence a justified uniform count
error at most `D` transports to an error at most `D`, with norm exactly
one on the class of bounded errors. This does not assert that every
extremizing error is a genuine zeta count error. On a finite range,
\[
 \int_{(0,H]}K_\delta(r)\,dA(r)
 =K_\delta(H)A(H)+\int_0^H[-K_\delta'(r)]A(r)\,dr.         \tag{2}
\]
The endpoint restores total error weight one. The same statement holds
for every power `K_delta^n`, whose value at zero is one.

The standard RH count-error bound is `O(log gamma/log log gamma)`;
passing it through these formulas does not produce an error below one.
For reference, [Goldston–Gonek][gg], equations (1)–(4), Theorem 1 and
Corollary 1, give the counting inputs without assuming simplicity.
For `0<r<gamma` and consistent boundary conventions, writing the
noncentral count as `N(gamma+r)-N(gamma-r)-m(gamma)` retains the unknown
central multiplicity. Subtracting one assumes the desired conclusion.
A safe lower bound must subtract a valid upper bound for `m`.

For an annulus `eta<|lambda-gamma|<=H`, a bound for the error in its own
cumulative count transports with norm `K_delta(eta)` (or its nth power).
That bound must be independently established; subtracting two uncertain
counts requires paying both errors. If `eta<<delta`, the factor is
near one. Discarding a large inner interval leaves its zero mass unknown.

## 2. Finite certification: locations, tails and central membership

Let `Omega` be a finite, independently certified list of noncentral
zeros, retaining each certified multiplicity. The global Lipschitz
constant for the power kernel is
\[
 \sup_r|(K_\delta^n)'(r)|
 =L_{n,\delta}:=\frac{2n}{\delta\sqrt{2n+1}}
 \left(\frac{2n+1}{2n+2}\right)^{n+1}
 \sim\frac{\sqrt{2n/e}}\delta.                            \tag{3}
\]
Indeed its maximum occurs at `|r|/delta=(2n+1)^(-1/2)`.
For `n=1`, this is `3 sqrt(3)/(8 delta)`. Location radii `epsilon_j`
therefore cost at most `L_{n,delta} sum_j m_j epsilon_j` in the subtracted
mass. If the target has radius `epsilon_0`, use `epsilon_j+epsilon_0`
and certify disjointness from the **entire** target interval. The
arithmetic enclosure and completeness of the list must also hold
uniformly at the actual target ordinate. Evaluation only at its guessed
midpoint does not give central mass exactly `m`.

Suppose the list is complete inside radius `H`, except for the central
atom. For `b>delta`, the ratio `K_delta(r)/K_b(r)` decreases with `r>=0`.
Thus
\[
 \sum_{|\lambda-\gamma|\ge H}m_\lambda K_\delta(\lambda-\gamma)^n
 \le K_\delta(H)^{n-1}
 \frac{\delta^2(b^2+H^2)}{b^2(\delta^2+H^2)} B_b(\gamma).
                                                                  \tag{4}
\]
Choose `b=H>max(delta,1/2)` to obtain the usable certificate
\[
 \boxed{\text{tail}\le
 \left(\frac{\delta^2}{\delta^2+H^2}\right)^{n-1}
 \frac{2\delta^2}{\delta^2+H^2}B_H(\gamma).}              \tag{5}
\]
The second sample is at `Re s=1/2+H>1`; its exact gamma, pole and signed
prime terms, or an upper bound paying all of them, must be included.
Boundary atoms may be included in the list or tail consistently.

Let the exact arithmetic sample `S_n=sum m_lambda K_delta^n` lie in
`[T_-,T_+]`, the listed mass in `[L_-,L_+]`, and the tail in `[0,epsilon]`.
Then
\[
 \boxed{m\in[T_- -L_+ -\epsilon,\ T_+ -L_-].}            \tag{6}
\]
Its **width** below one gives at most one integer; a symmetric error
radius below one is insufficient. The upper endpoint below two is the
relevant simplicity test at a certified zero. A narrow interval can
instead correctly recover multiplicity two. No central occurrence may
be subtracted as a supposedly distinct neighbor.

For fixed `delta` and `n=1`, the elementary completed upper envelope
at `b=H` gives `tail << delta^2 log(gamma+H+2)/H` when
`H>=max(1,2 delta)`. This supplies a sufficient window scale. The next
section determines the necessary scale of the **actual** residual,
which cannot be inferred just from this upper bound.

## 3. Sharp cost of the actual fixed-width tail

Fix `delta>0`, put `L=log(gamma/(2 pi))`, and let `H` tend to infinity
with `H=o(gamma)`. Then
\[
 \boxed{\sum_{|\lambda-\gamma|>H}m_\lambda
 \frac{\delta^2}{\delta^2+(\lambda-\gamma)^2}
 =\frac{\delta L}{\pi}\arctan\frac\delta H
  +O_\delta\left(\frac L{H^2}+\frac1\gamma\right)
 \sim\frac{\delta^2L}{\pi H}.}                           \tag{7}
\]
Here RH identifies the ordinate count with the full real product; the
count estimate itself does not assume simplicity.

**Proof.** Write `C_gamma(r)=sum_{|lambda-gamma|<=r}m_lambda` and
`kappa=L/pi`. Riemann–von Mangoldt, in the form
\[
 N(t)=F_0(t)+O(\log(t+2)),\quad
 F_0(t)=\frac t{2\pi}\left(\log\frac t{2\pi}-1\right),\quad F_0(0)=0,
\]
and a centered Taylor expansion give
\[
 C_\gamma(r)=\kappa r+O(L+r^3/\gamma^2),\qquad 0\le r\le\gamma/2.
                                                                  \tag{8}
\]
Endpoint conventions affect only the displayed error; use a
right-continuous `C` throughout. For `gamma/2<=r<gamma` the smooth count
is `F_0(gamma+r)-F_0(gamma-r)`; for `r>=gamma` it is
`F_0(gamma+r)+F_0(r-gamma)`. Subtracting the **same** `kappa r` and
scaling `r=gamma z` gives
`|C_gamma(r)-kappa r| << r(1+log^+(r/gamma))+log(gamma+r+2)`.
This follows from the corresponding combinations of
`(1+z)log(1+z)`, `|1-z|log|1-z|` and `2z`, which are bounded by
`O(z(1+log^+z))` for `z>=1/2`, including `z=1` by continuity.

The strict tail equals
`-K_delta(H)C_gamma(H)+integral_H^infinity (-K_delta')C_gamma`.
Its main term is `kappa integral_H^infinity K_delta`, exactly the
arctangent in (7). Formula (8), including the lower endpoint, costs
`O_delta(L/H^2+1/gamma)`. On `r>=gamma/2`, use the just-proved
subtracted-count bound and `-K_delta'(r)<<_delta r^(-3)`; the cost is
`O_delta(1/gamma+L/gamma^2)`. This proves (7). Bounding the whole far
tail without subtracting its main density would instead pay
`O_delta(L/gamma)`, so would not prove the stated sharper remainder.

In particular, for each fixed `c>0`,
\[
 \boxed{H=cL:\quad \text{tail}\longrightarrow\frac{\delta^2}{\pi c},
 \qquad A_\gamma(H)\sim\frac c\pi L^2.}                  \tag{9}
\]
The central multiplicity is `O(L)` and hence negligible in the count.
Thus a complete fixed-width deletion window with `H=o(L)` and
`H->infinity` leaves unbounded background. Radius `cL` leaves the
specified constant and requires roughly `cL^2/pi` noncentral zeros
counted with multiplicity. A strict limiting tail margin below
`epsilon` needs `c>delta^2/(pi epsilon)`. This statement concerns the
undeleted Poisson tail; it does not rule out separately estimating and
subtracting that tail, using another kernel, or retaining signed data.

## 4. High derivatives sharpen resolution in the Euler half-plane

For `delta>1/2` and integer `n>=1`, put `K_n=K_delta^n` and
`S_n(gamma)=sum_lambda m_lambda K_n(gamma-lambda)`. Their width is of
order `delta/sqrt(n)`, while every derivative stays at
`s=1/2+delta+i gamma`, where the Euler series converges absolutely.
For `a=delta^2`,
\[
 S_n=\frac{a^n}{(n-1)!}(-\partial_a)^{n-1}
 \left[\frac1\delta\Re\frac{\xi'}\xi(1/2+\delta+i\gamma)\right],
 \qquad S_{n+1}=S_n-\frac\delta{2n}\partial_\delta S_n.   \tag{10}
\]
Each finite differentiation is legitimate on compact subsets of
`delta>1/2`; no infinite derivative interchange is asserted.
With angular Fourier convention `Khat(u)=integral K(v)e^(-iuv)dv`,
\[
 \widehat K_n(u)=\frac{\delta\sqrt\pi}{\Gamma(n)}
 \int_0^\infty t^{n-3/2}e^{-t-\delta^2u^2/(4t)}\,dt,
 \quad
 \frac{\widehat K_n(u)}\pi=e^{-\delta u}
 \sum_{d=0}^{n-1}a_{n,d}u^d\quad(u\ge0),                \tag{11}
\]
\[
 a_{n,d}=\frac{\delta^{d+1}(2n-2-d)!}
 {2^{2n-2-d}(n-1)!(n-1-d)!d!}>0.
\]
The integral proves positivity, evenness and monotonic decrease for
`u>=0`. The finite coefficients follow by evaluating the half-integer
integral, agreeing with [DLMF 10.49.1 and 10.49.12][dlmf]. In particular,
`Khat_1=pi delta e^(-delta u)` and
`Khat_2=(pi delta/2)(1+delta u)e^(-delta u)`.

The analytic-strip explicit formula ([Goldston–Gonek][gg], Lemma 1,
with Fourier convention converted) is
\[
 S_n(\gamma)=G_n(\gamma)+P_n(\gamma)-Q_n(\gamma),        \tag{12}
\]
\[
 \begin{aligned}
 G_n(\gamma)&=\frac1{2\pi}\int_{\mathbb R}K_n(v-\gamma)
 [\Re\psi(1/4+iv/2)-\log\pi]\,dv,\\
 P_n(\gamma)&=K_n(\gamma+i/2)+K_n(\gamma-i/2),\\
 Q_n(\gamma)&=\frac1\pi\sum_{j\ge2}\frac{\Lambda(j)}{\sqrt j}
 \widehat K_n(\log j)\cos(\gamma\log j).
 \end{aligned}
\]
The rational test is analytic in a strip wider than `1/2` and decays
there as required. Formula (11) makes every prime term a finite sum of
`Lambda(j)(log j)^d j^(-1/2-delta)` times its cosine, so no critical-strip
Euler continuation is involved. The prime factor is **1/pi**.

## 5. Full optimization of the absolute prime payment

Define the precise estimating class
\[
 C_{n,\delta}=\frac1\pi\sum_{j\ge2}\frac{\Lambda(j)}{\sqrt j}
 \widehat K_n(\log j),\qquad
 U_{n,\delta}(\gamma)=G_n(\gamma)+2|K_n(\gamma+i/2)|+C_{n,\delta}.
                                                                  \tag{13}
\]
Then `m(gamma)<=S_n(gamma)<=U_n(gamma)`. Set
\[
 I_n=\int_{\mathbb R}K_n(v)\,dv
 =\delta\sqrt\pi\frac{\Gamma(n-1/2)}{\Gamma(n)},\qquad
 r_\delta=\frac{\delta^2}{\delta^2-1/4}>1.
\]
At the auxiliary ordinate zero, all prime cosines are one and both
pole terms are `r_delta^n`. Thus the **exact** identity is
\[
 \boxed{C_{n,\delta}=2r_\delta^n+G_n(0)-S_n(0).}         \tag{14}
\]
The exponential payment comes from the pole term in this identity;
the prime number theorem is not needed to estimate it.

For fixed `delta`, the nearest ordinate has distance `d0>0` since
`xi(1/2)!=0`, and `S_n(0)<=K_delta(d0)^(n-1)S_1(0)`.
The gamma integrand differs from its value at zero by `O(v^2)` globally.
Using `integral v^2 K_n=I_n delta^2/(2n-3)` for `n>=2` proves
`G_n(0)=I_n[psi(1/4)-log pi]/(2pi)+O_delta(n^(-3/2))` and hence
`C_n=2r_delta^n+O_delta(n^(-1/2))`.

**Uniformity when delta varies.** The total count and `d0>0` give a
fixed bound `N_abs(T)<=C T^2` for every `T>=0`. Integration by parts
then yields, for `n>=2`,
\[
 S_n(0)\le C\frac{\delta^2}{n-1},\qquad
 |G_n(0)|\le C\left(I_n+\frac{\delta^2}{n-1}\right).      \tag{15}
\]
The second inequality uses a global `C(1+|v|)` bound and
`integral |v|K_n=delta^2/(n-1)`. Constants are independent of both
parameters. Along any sequence with `I_n->0`, the restriction
`delta>1/2` forces `n->infinity`; the gamma ratio gives
`delta^2/n=(1+o(1))I_n^2/pi`. Consequently
`C_n=2r_delta^n+O(I_n)` uniformly in exactly this regime.

We also need a gamma lower bound uniform in both parameters. Every
even unimodal probability density `g` satisfies `g(v)<=1/(2|v|)`.
For its random variable `V`,
`Pr(|gamma+V|<gamma e^(-t))<=min(1,e^(-t)/(1-e^(-t)))`.
The integral of this bound for `t>=0` is `2 log 2`; hence
`E log|gamma+V|>=log gamma-2 log 2`. The gamma integrand is bounded
below globally by `log(|v|/(2pi))-C`. Applying this to `g=K_n/I_n`
proves, with `L=log(gamma/(2pi))`,
\[
 G_n(\gamma)\ge\frac{I_n}{2\pi}(L-C)                   \tag{16}
\]
for every allowed `delta,n`. Logarithmic moments are finite, including
`n=1`.

For each fixed `delta`, choose
`n=floor((log L-2 log log L)/log r_delta)` as `gamma->infinity`.
The prime cost is `O_delta(L/(log L)^2)`. Splitting the gamma integral
at `|v-gamma|=gamma/2`, using the local digamma asymptotic and
`integral |v|K_n=delta^2/(n-1)`, gives
`G_n(gamma)~I_n L/(2pi)` along this sequence. The pole payment is
`O_delta(gamma^(-2))` uniformly in `n>=1` for large gamma.
Conversely (14)–(16) force any competing orders to have
`n log r_delta<=log L+o(log L)`. Therefore
\[
 \inf_{n\ge1}U_{n,\delta}(\gamma)
 =\left(\frac{\delta\sqrt{\log r_\delta}}{2\sqrt\pi}+o(1)\right)
 \frac{L}{\sqrt{\log L}} \qquad(\delta>1/2\text{ fixed}).\tag{17}
\]

In fact the complete two-parameter optimization is
\[
 \boxed{\inf_{\delta>1/2,\ n\ge1}U_{n,\delta}(\gamma)
 =\left(\frac1{4\sqrt\pi}+o(1)\right)
 \frac{\log\gamma}{\sqrt{\log\log\gamma}}.}             \tag{18}
\]
For the upper bound, take arbitrarily large fixed `delta` in (17) and
use `delta sqrt(log r_delta)->1/2`. For the lower bound, only sequences
with `U<=C0 L/sqrt(log L)` can compete. Positivity of (16) at large
height and of both payments forces `I_n=O(1/sqrt(log L))`. The uniform
version of (14) gives `n log r_delta<=log L+o(log L)`, while
`log r_delta>=1/(4delta^2)`. Combining with the uniform gamma ratio
forces `I_n>=(1-o(1))sqrt(pi)/(2sqrt(log L))`. Equation (16) gives
the matching lower constant. No fixed-parameter asymptotic has been
silently extended to variable delta.

This absolute-payment class is weaker than Note 02's optimized Fejer
scale `log gamma/log log gamma`. Its shrinking real-axis width alone
does not yield simplicity. The statement does not cover signed
evaluation or subtraction of independently known zero contributions.

## 6. Effective separation and the heat-flow interface

After subtracting an independently certified finite multiset `Omega`,
write `D_n=S_n-sum_Omega m_lambda K_n`. If every remaining noncentral
zero is at distance at least `d>0`, positivity gives, with
`q=delta^2/(delta^2+d^2)`,
\[
 0\le D_n-m\le q^{n-1}(D_1-m)\le q^{n-1}B_\delta.
                                                                  \tag{19}
\]
Thus a certified `B_delta<=M` pays this residual below `epsilon` for
`n>=1+log(M/epsilon)/log(1+d^2/delta^2)` when `M>epsilon`.
Alternatively, a bound `T` for the remaining inverse-square sum gives
`d>=1/sqrt(T)` and residual at most
`delta^2 T [delta^2 T/(1+delta^2 T)]^(n-1)` (with the empty sum
case immediate). These are error estimates with stated inputs, not
merely the unquantified limit `D_n->m`.

For fixed `delta>1/2`, the elementary envelope has `M=O_delta(log gamma)`.
If a gap of order `1/log gamma` were independently supplied, the stated
budget uses orders of size `log^2 gamma log log gamma`. RH does not
supply that mean-spacing scale as a lower bound for every gap.
Analytic isolation provides some positive gap at each fixed distinct
zero, without such an all-height quantitative bound.

Finite wall continuation gives a finite exterior inverse-square sum,
not its numerical upper bound. At an ordinary double event `x=a=2gamma`,
the coefficient in Note 03's formula
`(v-u)^2=8t-16 S_x t^2+o(t^2)` is `S_x=T_gamma/4`, where `T_gamma`
counts all exterior ordinates before additional subtraction. This
identifies the data in (19) but does not bound them above or force
a later collision.

Any numerical use must also pay the prime tail in (12). For example,
put `sigma=1/2+delta`. For integer `X>=exp(n/sigma)`, each `d` term
after truncation at `X` is at most
\[
 a_{n,d}\left[X^{-\sigma}(\log X)^{d+1}
 +(\sigma-1)^{-d-2}\Gamma(d+2,(\sigma-1)\log X)\right].  \tag{20}
\]
Here the second gamma is the upper incomplete gamma function. Sum over
`0<=d<n`. This follows from `Lambda(j)<=log j`, monotonicity of
`x^(-sigma)(log x)^(d+1)` past `X`, and its integral. No computation
or all-height numerical certificate is claimed here.

## 7. Short audit of nonnegative trigonometric combinations

This extends Note 01's fixed-width screen; it is not another research
program. Write `p_delta(v)=delta/(delta^2+v^2)`,
`C_sigma(t)=sum Lambda(j)j^(-sigma)cos(t log j)`,
`M_sigma=C_sigma(0)>0`, and retain the exact identity
`sum m_lambda p_delta(t-lambda)=A(sigma,t)-C_sigma(t)` of Note 01,
where
\[
 A(\sigma,t)=\Re\left(\frac1{\sigma+it}+\frac1{\sigma-1+it}\right)
 -\tfrac12\log\pi+\tfrac12\Re\psi((\sigma+it)/2).
\]
For `T(theta)=b0+sum_{k=1}^K b_k cos(k theta)>=0`, with `b_k>=0`
for `k>=1` and `sum_{k>=1}b_k>0`, logarithmic coefficient positivity
gives `0<=b0 M_sigma+sum b_k C_sigma(k gamma)`. Keeping the pair
`+/-gamma`, each of multiplicity `m`, and dropping only nonnegative
remaining-zero contributions gives
\[
 m\le U_{\sigma,T}(\gamma):=
 \frac{b_0M_\sigma+\sum_{k\ge1}b_k A(\sigma,k\gamma)}
 {\sum_{k\ge1}b_k[p_\delta((k-1)\gamma)+p_\delta((k+1)\gamma)]}.
                                                                  \tag{21}
\]
Note 01's elementary uniform bound gives
`A(sigma,k gamma)>=a_gamma=0.5 log(gamma/(2pi))-(pi+1)/(4gamma)`.
Every denominator bracket is at most
`d_delta=1/delta+delta/(delta^2+4gamma^2)`, which decreases in `delta`:
its derivative has numerator
`-2delta^4-4gamma^2 delta^2-16gamma^4` after a positive denominator.
Consequently, for large gamma,
\[
 U_{\sigma,T}(\gamma)\ge
 \frac{a_\gamma}{2+2/(1+16\gamma^2)},\qquad
 \boxed{\inf_{\sigma>1,T}U_{\sigma,T}(\gamma)
       =(1/4+o(1))\log\gamma.}                          \tag{22}
\]
The upper asymptotic follows with `T=1+cos theta` and
`sigma=1+(log gamma)^(-1/2)`, using
`M_sigma=(sigma-1)^(-1)+O(1)`. Every bound (21) exceeds two for
`gamma>=2pi exp(9)`. This covers arbitrary finite degree,
height-dependent coefficients and nonnegative sums at different sigma;
the latter form denominator-weighted averages of these bounds.

General positive semidefinite Toeplitz forms allow signed Fourier
coefficients. They give no permission to drop the resulting **signed**
remaining-zero contribution. Such a route would need a new correlated
estimate or a separately proved nonnegative zero kernel with an effective
evaluation. Formula (22) is not a no-go theorem for those constructions.

## 8. Controls and disposition

At an added endpoint Euler-control zero the added rational-power mass is
\[
 2\sum_{j\in\mathbb Z}K_n(2\pi j/\log p)>2,
\]
tending to two. For Note 03's isolated positive-source control, centered
at `gamma=A/2`, the added mass is
`2+2[delta^2/(delta^2+A^2)]^n>2`. Legitimate deletion of any noncentral
part leaves the central mass two. A base zero at the same location only
adds multiplicity. These controls therefore screen the counting and
subtraction steps, including falsely deleting a central occurrence.

Their arithmetic distinctions remain explicit: the Euler control changes
conductor and logarithmic coefficients, some of which are negative; the
isolated polynomial control has no ordinary Dirichlet series and its
de-completed factor satisfies `-D_A'/D_A<0` on the far positive real
axis, as proved in Note 03. Powers of zeta change
gamma degree, pole order and coefficient size. None is a counterexample
satisfying every unchanged zeta-arithmetic premise. The estimator lower
bounds above were proved for the actual zeta data themselves.

The isolated control's added endpoint can approach an original high
zero while keeping the source positive and the endpoint off that zero.
Its exterior inverse-square sum becomes arbitrarily large. Thus source
positivity, the same gamma factor and conductor, the simple-pole order,
and finite wall structure alone supply no local uniform upper bound for
the sum in (19). The pole residue changes, as recorded in Note 03. A bound
using unchanged zeta coefficients remains outside that screen.

The new deflation interface has fully stated location, completeness,
tail and arithmetic costs. No RH estimate provided here meets them
with an upper endpoint below two at every zero. The rational and
nonnegative-combination absolute strategies have been quantitatively
assessed and should not be optimized again without an additional input.
The strict arithmetic, contour-surplus and all-zero gates remain open
in the [progress register][progress].

[notes]: README.md
[program]: ../research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md
[progress]: ../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md
[review]: ../reviews/04_DEFLATION_AND_RESOLUTION_REVIEW_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../../../../avoid/20_volume_without_a_gain.md
[gg]: https://arxiv.org/pdf/math/0511092
[dlmf]: https://dlmf.nist.gov/10.49
