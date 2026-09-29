# Uniform exterior coercivity for the full weighted Xi jump form

28 September 2026. Continuation round 8. Prepared for Edward Baker with LLM assistance. Model: GPT-6 (Codex); exact serving variant and configured effort are not exposed. Analytic working derivation, not formal verification or independent human refereeing. Analytic derivation; no numerical sweep or large generated data.

## 1. Result and inputs

The full prime family supplies precisely the exterior coercivity missing from every finite-prime truncation. If u is supported outside `[−R,R]`, then, uniformly over all u in the weighted jump form domain,

\[
\boxed{\quad\mathcal E(u)\ge
\left(\frac14-\eta(R)\right)\|u\|_{L^2(\mu)}^2,
\qquad\eta(R)\longrightarrow0.\quad}                   \tag{1}
\]

The argument is unconditional and applies to arbitrary oscillation, concentration, or complex phase. It uses only prime edges connecting the exterior to a central interval on which u vanishes. The matching exterior Rayleigh upper limit is also 1/4. This is an exterior theorem, not the global mean-zero gap inequality equivalent to RH.

The repository input is [the round-7 complement and weighted-gap note](CCM_COMPLEMENT_DENSITY_AND_WEIGHTED_GAP_20260928.md), Sections 5–6. Keep its literal normalization

\[
\widehat k=\Xi/4,\quad k>0\text{ and even},\quad
d\mu(x)=k(x)c(x)dx,\quad c(x)=\cosh(x/2),\quad
M=\mu(\mathbb R)=1/8.
\]

The positive jump energy is

\[
\mathcal E_\Gamma(u)=\frac12\iint H(|x-y|)k(x)k(y)
|u(x)-u(y)|^2dxdy,\quad H(s)=\frac{e^{-s/2}}{1-e^{-2s}},
\]
\[
\mathcal E_p(u)=\sum_{n\ge2}q_n\int k(x)k(x+\log n)
|u(x+\log n)-u(x)|^2dx,\quad q_n=\frac{\Lambda(n)}{\sqrt n},
\quad\mathcal E=\mathcal E_\Gamma+\mathcal E_p.
\tag{2}
\]

The closed form is the closure of its smooth compact core in L2(μ), as justified in the input note. Bounds below also hold for the maximal finite-jump-energy domain. All inequalities use nonnegative integrals and consequently extend from smooth tests by the closed-form approximation or directly by Fatou/Tonelli.

## 2. An explicit unconditional prime-counting input

Write `ψ(t)=Σ_(n≤t)Λ(n)`. [Johnston–Yang, Theorem 1.1, arXiv:2204.01980v2](https://arxiv.org/html/2204.01980v2#S1.SS2), proves, for every t≥2,

\[
|\psi(t)-t|\le t\delta(\log t),\qquad
\delta(s)=9.39\,s^{1.515}\exp(-0.8274\sqrt s).
\tag{3}
\]

This is an unconditional published-source input; its finite verified-zero ingredients do not amount to assuming RH. No strongest-current-error-term claim is needed. Its constants were checked against the primary text. Only (3), not any RH-strength error estimate, is used below.

The function δ decreases for

\[
s\ge s_0=\left(\frac{2(1.515)}{0.8274}\right)^2<14.
\]

Let `D_0=max{1,δ(s_0)}`. Setting ψ(t)=0 on `[1,2)`, one has `|ψ(t)−t|≤D_0t` for all t≥1. This uniform crude bound and the decreasing tail of δ will also control the complete prime diagonal.

## 3. Uniform central-edge rate by partial summation

For T>0 define

\[
M_T=\int_{-T}^T e^{-y/2}k(y)dy
=\int_{-T}^T k(y)\cosh(y/2)dy,
\]
\[
B_T=2k(T)\cosh(T/2)+
\int_{-T}^T e^{-y/2}|k'(y)+k(y)/2|dy.
\tag{4}
\]

Both are explicit one-dimensional kernel quantities. `M_T↑M`, and `B_T` is bounded uniformly for T≥1, because k and k' decay faster than every exponential. For x>T, put

\[
d_T(x)=\frac1{c(x)}
\sum_{e^{x-T}<n\le e^{x+T}}q_n k(x-\log n).
\tag{5}
\]

Changing the endpoint convention affects only a countable set of x and has no effect on the form estimates. It may equivalently be handled with one-sided Stieltjes endpoint values.

**Lemma 1.** If x−T≥14, then

\[
\left|d_T(x)-\frac{2M_T}{1+e^{-x}}\right|
\le \frac{2B_T}{1+e^{-x}}\delta(x-T).
\tag{6}
\]

**Proof.** Set `a=e^(x−T)`, `b=e^(x+T)` and `h_x(t)=t^−1/2 k(x−log t)`. The sum in (5) before division by c is `∫_(a,b] h_x(t)dψ(t)`. The main integral is

\[
\int_a^b h_x(t)dt=e^{x/2}M_T.
\]

For `E(t)=ψ(t)−t`, Stieltjes integration by parts bounds the error by

\[
\delta(x-T)\left[a|h_x(a)|+b|h_x(b)|+
\int_a^b t|h_x'(t)|dt\right].
\]

Here (3) and monotonicity of δ are uniform throughout the interval. Since

\[
h_x'(t)=-t^{-3/2}[k'(x-\log t)+k(x-\log t)/2],
\]

the bracket equals `e^(x/2) B_T`. Finally `e^(x/2)/c(x)=2/(1+e^−x)`. ∎

## 4. Exterior coercivity with an explicit error

**Theorem 2.** Let R>T≥1 and R−T≥14. Every finite-energy u vanishing μ-almost everywhere on `[−R,R]` satisfies

\[
\boxed{\quad
\mathcal E(u)\ge
\left[2M_T-2M_Te^{-R}-2B_T\delta(R-T)\right]\|u\|_\mu^2.
\quad}                                                  \tag{7}
\]

Evenness is not required for this bound, although it is the sector relevant to the RH criterion.

**Proof.** Retain only the prime edges with one endpoint in `[−T,T]` and the other in the support of u. For an exterior point x>R, these are exactly the inward shifts in (5). On the central endpoint u is zero, so every selected squared difference is `|u(x)|²`; there is no cross term and no regularity estimate on u. For x<−R, evenness of k gives the reflected rate `d_T(|x|)`. Every selected undirected edge is counted once by the positive-shift convention in (2). Hence

\[
\mathcal E(u)\ge\int_{|x|\ge R}d_T(|x|)|u(x)|^2d\mu(x).
\]

Use Lemma 1, `2M_T/(1+e^−x)≥2M_T−2M_Te^−x`, and the monotonicity of δ for |x|≥R. ∎

An explicit choice in (1), valid for R≥28, is

\[
\eta(R)=2(M-M_{R/2})+2M_{R/2}e^{-R}
+2B_{R/2}\delta(R/2).                                  \tag{8}
\]

This is nonnegative and tends to zero. In particular,

\[
\eta(R)=O\!\left(R^{1.515}e^{-0.8274\sqrt{R/2}}\right),
\tag{9}
\]

with much smaller kernel-tail and exponential contributions. The constants B_T are given by (4), rather than presumed numerically certified. The estimate need not be positive at modest R; its unconditional asymptotic coercivity is the claim.

The weaker two-stage argument also suffices: first hold T fixed and send R to infinity, obtaining the floor `2M_T`; then send T to infinity. Formula (8) makes a simultaneous choice explicit and justified.

## 5. The complete prime diagonal tends to 1/4

For the matching upper estimate define the finite continuous diagonal rate

\[
D_p(x)=\frac1{c(x)}\sum_{n\ge2}q_n
[k(x-\log n)+k(x+\log n)].                             \tag{10}
\]

Local convergence of this series and its derivatives follows from the double-exponential decay of k as `log n→∞`, uniformly for x in compact sets. The rate is even.

Put

\[
B_\infty=\int_{\mathbb R}e^{-y/2}|k'(y)+k(y)/2|dy,
\quad B_+(t)=\int_t^\infty e^{-y/2}|k'(y)+k(y)/2|dy,
\]
\[
M_+(t)=\int_t^\infty e^{-y/2}k(y)dy,
\quad C_+=\sum_{n\ge2}(\log n)n^{-5/2}<\infty.
\]

**Lemma 3.** For x≥28,

\[
|D_p(x)-2M|\le\omega(x),\qquad\omega(x)\to0,
\tag{11}
\]

where one admissible explicit bound is

\[
\omega(x)=2Me^{-x}+(1+C_+)\frac{k(x)}{c(x)}
+2M_+(x)+2B_\infty\delta(x/2)+2D_0B_+(x/2).
\tag{12}
\]

**Proof.** For the inward sum `S_−(x)=Σq_n k(x−log n)`, integrate h_x against ψ from 1 to infinity. Integration by parts with E=ψ−t gives

\[
S_-(x)-e^{x/2}\int_{-\infty}^{x}e^{-y/2}k(y)dy
=k(x)-\int_1^\infty E(t)h_x'(t)dt.
\tag{13}
\]

The lower boundary term is k(x), since E(1)=−1; the upper boundary vanishes. On `y=x−log t≤x/2`, use `|E(t)|/t≤δ(x/2)`; on `x/2<y≤x`, use D_0. Thus the error after division by c is at most

\[
\frac{k(x)}{c(x)}+2B_\infty\delta(x/2)+2D_0B_+(x/2).
\]

Replacing the main integral by M adds at most `2M_+(x)`, and replacing `e^(x/2)/c(x)` by 2 adds at most `2Me^−x`.

For the outward sum use the theta-tail bound from the preceding null-kernel note,

\[
k(x+s)\le k(x)e^{-\pi e^{2x}s}\quad(x\ge1,s\ge0).
\]

Since `πe^(2x)≥2` and `Λ(n)≤log n`, its sum is at most `C_+ k(x)`. This proves (12). Every term tends to zero; for x≥28 the displayed bound can also be taken uniformly over x≥R by monotonicity of its terms. ∎

This is a smoothed multiplicative prime-counting statement at `n≈e^x`. It does not require prime counts on the extremely short physical support scale of a narrow test function u: the smoothing profile in (10) is the fixed kernel k.

## 6. A matching exterior Rayleigh upper limit

Let `φ≥0` be a nonzero smooth function supported in `(0,1)`. As in the round-7 finite-prime obstruction, set `A_S=πe^(2S)` and take normalized nonnegative even bumps

\[
u_S(x)=a_S\{\phi(A_S(x-S))+\phi(A_S(-x-S))\},
\qquad\|u_S\|_\mu=1.
\]

Their support is outside `[−S,S]`. Because u_S is nonnegative, expanding each square gives

\[
\mathcal E_p(u_S)\le\int D_p(x)|u_S(x)|^2d\mu(x)
\le\frac14+\sup_{x\ge S}\omega(x).
\tag{14}
\]

The cross terms have the favorable sign; no unproved decorrelation is used. The gamma estimate already proved for these bumps in round 7 is

\[
\mathcal E_\Gamma(u_S)\le Ce^{-S}
+Ce^{-S/2}(1+\log A_S)k(S-1)\longrightarrow0.
\tag{15}
\]

It follows from splitting jump lengths below `1/A_S`, between `1/A_S` and 1, and above 1. The first uses the bump derivative, the second the integrable truncated `1/s` singularity, and the third exponential decay of H. The proof remains unaffected by restoring the full prime family because it estimates only the gamma part.

Combining (7), (14) and (15) gives

\[
\mathcal E(u_S)\longrightarrow\frac14.
\tag{16}
\]

Consequently the even exterior Dirichlet Rayleigh infimum

\[
\beta(R)=\inf\left\{\mathcal E(u)/\|u\|_\mu^2:
0\ne u\in\operatorname{Dom}\mathcal E\text{ even},
\ u=0\text{ on }[-R,R]\right\}
\]

satisfies

\[
\boxed{\quad\lim_{R\to\infty}\beta(R)=\frac14.\quad}   \tag{17}
\]

In fact β(R)≤1/4 for every R, by taking S arbitrarily large. Smooth compact tests already attain the limiting infimum. Their μ-means tend to zero because their supports have μ-measure tending to zero. This proves the exterior threshold in the ordinary norm; any exact mean-zero reformulation must account for the fact that subtracting a constant removes strict exterior support.

## 7. A useful global inequality for spectral localization

The preceding lower bound can be converted to a global inequality without invoking a nonlocal IMS formula. This is supplied to the parallel spectral audit; the additional compactness step is not silently assumed here.

Let `a_R,T=2M_T−2M_Te^−R−2B_Tδ(R−T)`. For |y|≤T define the reverse rate of central-to-exterior prime edges

\[
J_{R,T}(y)=\frac1{c(y)}\sum_{n\ge2}q_n\big[
k(y+\log n)1_{y+\log n\ge R}
+k(y-\log n)1_{y-\log n\le-R}\big],
\quad C_{R,T}=\sup_{|y|\le T}J_{R,T}(y)<\infty.
\tag{18}
\]

The supremum is finite by the uniform superexponential kernel tail; for fixed T it even tends to zero as R increases. Retain the same central-exterior edges and use, for 0<θ<1,

\[
|a-b|^2\ge(1-\theta)|a|^2-(\theta^{-1}-1)|b|^2.
\]

The result, valid for arbitrary u, is

\[
\mathcal E(u)\ge(1-\theta)a_{R,T}
\|1_{|x|\ge R}u\|_\mu^2
-(\theta^{-1}-1)C_{R,T}\|1_{|x|\le T}u\|_\mu^2.
\tag{19}
\]

For every λ<1/4 with λ>0 one can choose T, then R, then θ so that `(1−θ)a_R,T≥λ`. It follows that, for some finite C,

\[
\boxed{\quad\mathcal E(u)\ge\lambda\|u\|_\mu^2
-C\|1_{|x|\le R}u\|_\mu^2.\quad}                     \tag{20}
\]

If restriction of the form domain to compact intervals is compact in L2(μ), (20) implies finite-dimensional spectral projections below every level strictly less than 1/4 by the min–max principle. One should prove that local compactness, or cite an applicable theorem with all hypotheses, before declaring an essential spectral statement. The already-established infinite threshold eigenspace supplies the matching essential upper bound once the lower conclusion is justified.

## 8. Scope

The result repairs a specific obstruction from round 7: finite prime truncations have exterior gap zero, but the **complete** arithmetic jump family has exterior threshold 1/4. The prime number theorem supplies the aggregate central-directed rate uniformly over exterior functions. No finite-L spectral data, assumed ground eigenvectors, or RH-strength prime error estimate enter.

This confines any spectrum strictly below the threshold once local compactness is supplied; it does not exclude such spectrum. Eigenvalues may still lie below 1/4, and the estimate gives no uniform positive distance between them and 1/4. The global mean-zero Poincaré inequality remains the missing RH statement. Further finite-prime calculations do not substitute for the uniform estimate (7), while (7) itself does not substitute for interior spectral control.
