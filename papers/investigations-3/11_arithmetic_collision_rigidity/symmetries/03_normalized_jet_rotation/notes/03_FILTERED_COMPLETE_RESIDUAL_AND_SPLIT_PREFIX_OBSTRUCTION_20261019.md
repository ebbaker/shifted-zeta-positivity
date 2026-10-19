# S03-T1: complete filtered residual and a scoped payment obstruction

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning
effort **ultra**, verified from session metadata. Separate delegated
same-model derivation and adversarial audit; no specialist human review.

**Outcome.** This completes the derivation/scoped-obstruction gate of
S03-T1. A single source-filtered discrepancy, with an explicit physical
tail ledger, is selected for S03-T2. Exact arithmetic-mode symbols expose
the already known leading-pair cancellation and the remaining logarithmic
moments. A certified witness proves that a triangle payment separating the
complete physical-source prefix from the full approximation prefix must
exceed **1.912087** on B. Such a payment cannot improve any retained
residual allowance. This is not a new bound for the recombined residual;
its unexpectedly small complete defect remains a cancellation between
the filtered source and the corrected arithmetic expression.

The [result summaries][summaries] and [patterns to avoid][avoid] were read,
especially [theta bookkeeping][s14], [collision controls][controls],
[reformulations][a1], [scoped failures][a7] and [cancellation][a12]. The
classification is **exact analytic derivation plus a proved scoped
failure of one payment rule**, supported by outward interval checks. No
physical sign, zero-free hypothesis or unknown jet argument is an input.

## Fixed conventions and information class

Use B=`[1/100,1/5] x [999,1001]`, anchor `x0=999`, and exactly the
coherent full analytic family selected by [S02-T2][s02]. Write

\[
F=G_8-\widehat C_8,\quad f=F/A,\quad Q=H/A,\quad r=Q-f,
\quad b=(\log A)_x,\quad \omega=\theta_x<0.
\]

Here A and theta are the original symmetric normalizer and explicit
arithmetic phase. They are not a positive sum of packet amplitudes or the
argument of the physical jet. In terms of `s=(1-ix)/2`,

\[
\begin{aligned}
m_0(s)&=\log s+\log(s-1)-\tfrac s2\log\pi
 +\tfrac12\log(2\pi)-\log16
 +(\tfrac s2-\tfrac12)\log(s/2)-s/2,\\
\alpha(s)&=m_0'(s)=\frac1{2s}+\frac1{s-1}
                       +\tfrac12\log\frac{s}{2\pi},\\
m_t(s)&=m_0(s)+t\alpha(s)^2/4,\\
A&=\exp\{(m_t(s)+m_t(1-s))/2\},\quad
\theta=(m_t(s)-m_t(1-s))/(2i).
\end{aligned}                                                    \tag{1}
\]

Branches are those in S02. A is positive and omega is nonzero on B by
the inherited contract. All spatial derivatives hold cutoffs and source
contour parameters fixed. The varying-center frozen family from S02 is
not used in this derivation.

The theta integer-square source index below is distinct from the
arithmetic Dirichlet index. Arithmetic cutoff N=8 and shifted-source cutoff
m=12 have different meanings. In particular, cancellation of arithmetic
n=1 below is not annihilation of the first theta-source square term.

## The physical annihilator and the arithmetic symbols

Let `D=partial_x-b`, `mu=omega_x/omega`, and define the physical operator

\[
\mathcal L=D^2-\mu D+\omega^2
 =\partial_x^2+q_1\partial_x+q_0,
\quad q_1=-2b-\mu,\quad q_0=\omega^2+b^2-b_x+\mu b.              \tag{2}
\]

For any twice differentiable physical field V,

\[
(D_\theta^2+1)(V/A)=\frac{\mathcal LV}{A\omega^2},\qquad
\mathcal L(Ae^{\pm i\theta})=0.                                  \tag{3}
\]

Indeed D(Ah)=Ah_x; expanding once more proves (2) and (3). The terms
`b_x` and `mu b` are essential. The cancellation of value with second
derivative is the `-omega^2+omega^2` cancellation on these two channels;
the `i omega_x` terms cancel as well. The leading-pair cancellation was
already present in [S03 Note 01][opening] and [Note 07][n07]. Equation (3)
does not assert that the entire residual consists of these channels.

For `ell=log n`, put

\[
p_n=\exp\{-s\ell+t(\ell^2-2\alpha(s)\ell)/4\},\quad
\beta=1+t\alpha'(s)/2,\quad
\lambda_n=i\ell\beta/2,\quad \lambda_n'=t\ell\alpha''(s)/8.
\]

Then `G8/A=2 Re[e^{i theta} sum_(n=1)^8 p_n]`, and product
differentiation gives the exact logarithmic symbol

\[
\mathcal L(Ae^{i\theta}p_n)=Ae^{i\theta}p_n\sigma_n,
\quad \sigma_n=\lambda_n^2+\lambda_n'
                         +(2i\omega-\mu)\lambda_n
\]
\[
\boxed{\sigma_n=
 \ell\{t\alpha''(s)/8-\omega\beta-i\mu\beta/2\}
 -\ell^2\beta^2/4.}                                               \tag{4}
\]

Thus `sigma1=0` exactly and all remaining arithmetic contributions are
explicit first and second logarithmic moments with their original
complex phases. No separate absolute mode sums are taken. At the leading
large-height level `beta~1`, the normalized symbol is
`sigma_n/omega^2 ~ -ell/omega-ell^2/(4omega^2)`.
Near the natural cutoff `ell~-2omega` this is of order one, rather than
small. This observation is a regime diagnostic, not a uniform asymptotic
estimate or a lower bound for the complete residual.

Retain the full correction. With `k=pi/8`,

\[
\widehat C_8=P J_8,\quad P=-\sqrt\pi\,e^{-kx-k^2t}/4,\quad
v=x/2+\pi t/8,\quad a=\sqrt{v/(2\pi)},\quad p=17-2a,
\]
\[
J_8=\sqrt v\{vD(p)-E(p)\},\quad
D(p)=\frac{\cos\pi(p^2/2+3/8)}{2\cos\pi p},\quad
E(p)=\frac{\sin\pi(p^2/2+3/8)-\sqrt2\cos(\pi p/2)}{2\cos\pi p}.
\]

For `h=k+b` its complete contribution is

\[
\mathcal L\widehat C_8=P\{J_{8,xx}-(2h+\mu)J_{8,x}
                  +(h^2-b_x+\mu h+\omega^2)J_8\}.                \tag{5}
\]

Both profile derivatives in (5) remain present. The signed correction
enters the residual with a plus sign because `H-F=H-G8+Chat8`.

## One complete estimable functional

The [complete reflected contour identity][contour] precedes all source
truncation. For real t,x and fixed `0<d<pi/8`,

\[
H(t,x)=\Re\int_0^\infty
 e^{t(u+id)^2+ix(u+id)}\Phi(u+id)\,du,
\]
\[
\Phi(v)=\sum_{j\ge1}(2\pi^2j^4e^{9v}-3\pi j^2e^{5v})
                                       e^{-\pi j^2e^{4v}}.
\]

The full source has the required reflection. A truncated source is not
assigned it, and no individual vertical endpoint term is silently removed.
On B one may freeze the established evaluator's
`d=pi/8-4log(1000)/1000`, `m=12`, `U=2`. Let `Phi_<m` denote its retained
square terms and set

\[
K(t,y,u)=e^{t\zeta^2+iy\zeta}\Phi_{<m}(\zeta),\quad
\zeta=u+id,
\]
\[
\Gamma(t,y,\zeta)=(i\zeta-b)^2-b_x-\mu(i\zeta-b)+\omega^2.
                                                                    \tag{6}
\]

Applying (2) under the convergent integral gives a filtered finite-source
term `Re int_0^U K Gamma du`. All normalization terms have been combined
in Gamma before evaluating a range. The selected S03-T2 functional is

\[
\boxed{\mathcal J_{m,U}(t,x)=\int_{999}^{x}
 \frac{e^{-i\theta(t,y)}}{A(t,y)\omega(t,y)}
 \left[\Re\int_0^U K\Gamma\,du
       -2A\Re\!\left(e^{i\theta}\sum_{n=2}^8p_n\sigma_n\right)
       +\mathcal L\widehat C_8\right]dy.}                          \tag{7}
\]

The inner real part is justified on this real slice only. The outer phase
is complex and stays outside it. A complex disk extension must retain
both holomorphic shifted channels and their factor 1/2.

Formula (7) makes no use of the unknown H or its derivatives in the
retained term. Its inputs are explicit theta-source integrals, finite
arithmetic moments, and the full correction. They must be subtracted
before norms. It is a concrete estimating problem, not yet an estimate.
Using the [existing source residual polynomial][correlated] to evaluate
(7) without further analysis would reproduce the source-informed result,
not establish an independent arithmetic allowance.

## Every remaining payment

Let `T_j(t,y)` be a physical derivative envelope, for j=0,1,2, for the
difference between H and the finite retained source integral in (7).
Split it into the already established **omitted square indices at least m on the whole
half-line** and **retained squares on u>U**. The [effective source
evaluator][evaluator] supplies both; the source tail is not omitted just
because it is tiny. Then

\[
I_r(t,x)=\mathcal J_{m,U}(t,x)+\mathcal E_{m,U}(t,x),\quad
|\mathcal E_{m,U}|\le\int_{999}^{x}
 \frac{T_2+|q_1|T_1+|q_0|T_0}{A|\omega|}\,dy.                   \tag{8}
\]

To prove (8), apply (2) to the physical tail, then integrate
`e^{-i theta} omega R_tail`. In fixed G* units replace `T_j` by
`G* tau_j` and `1/A` by `chi/G*`; G* is never differentiated.

A complete implementation of (7) must additionally pay:

- retained filtered-source quadrature, including its parameter variation;
- evaluation/rounding of (1), (4), (5), Gamma and the phase;
- any source or arithmetic Taylor truncation introduced by that implementation;
- the range variation on every closed t/x cell and the partial final
  spatial cell of every prefix;
- changed contour or cutoff matching if leaving this fixed B contract.

Direct whole-cell integration of outward integrand ranges needs no extra
quadrature discretization remainder in y; point sampling does. The two
tails in (8) are paid once. The analytic S02 residual envelope is an
alternative comparator, not another tail to add to this exact-source
decomposition. An oscillator-calibrated consumer would also need the
separate residual anchor and its uncertainty; (7) starts at zero and
does not set the actual residual anchor to zero.

## The normalized residual has explicit heat forcing

Write `g_n(v)=exp[m0(v)-v ell+t(alpha(v)-ell)^2/4]` for either channel
`v=s,1-s`. Set `a_n=alpha(v)-ell` and
`B_n=a_n(1+t alpha'(v)/2)`; in the next formula only, a prime on B_n
means a derivative in v. Since `(partial_x v)^2=-1/4`,

\[
(\partial_t+\partial_x^2)g_n
 =\tfrac14\{a_n^2-B_n^2-B_n'\}g_n.                            \tag{9}
\]

For the full correction,

\[
(\partial_t+\partial_x^2)\widehat C_8
 =(\partial_x+k)^2\widehat C_8=PJ_{8,xx}.                       \tag{10}
\]

Here the dependence of J on `x/2+kt` proves (10). Consequently, with
`F_heat=(partial_t+partial_x^2)F`, the exact residual equation is

\[
\boxed{r_t+r_{xx}+2br_x+
 \{(\log A)_t+b_x+b^2\}r=-F_{\rm heat}/A.}                     \tag{11}
\]

This follows by substituting `H-F=Ar` in the physical heat equation.
Neither r nor f is propagated by the unmodified physical heat equation.
Equations (9)–(11) identify additional terms a time-propagation method
would owe; they do not bound them or replace (7).

## Scoped obstruction: source and approximation prefixes cannot be split

For any normalized g define
`Z_g=e^{-i theta}(g-i g_x/omega)` and
`I_g=int_999^x e^{-i theta} omega R_g dy`.
Linearity gives `I_r=I_Q-I_f`. Consider precisely the rule that obtains
nonnegative separate allowances `B_Q>=|I_Q|`, `B_f>=|I_f|` and pays
`B_Q+B_f`. It necessarily pays at least `|I_f|`, regardless of the source.

At `t=21/200`, the known full analytic approximation has

\[
\begin{aligned}
Z_f(999)&=2.8669284266209146\ldots+1.6418915890514771\ldots i,\\
Z_f(1001)&=1.0474019402303994\ldots+1.0541841261845584\ldots i,\\
|I_f(1001)|&=|Z_f(1001)-Z_f(999)|
                 =1.91208700026596179777\ldots>1.912087.          \tag{12}
\end{aligned}
\]

The exact-point lower inequality is certified independently at 192 and
256 bits in the [small record][record]. It suffices to obstruct a uniform
upper allowance from this payment rule on B; it is not being used to
prove a uniform bound from a sample. All complete residual references are
much smaller:

| Retained reference | Allowance and information |
| --- | --- |
| Analytic-only independent endpoints | `<0.827470` |
| Complete-source independent endpoints | `<0.002011747` |
| Complete-source signed correlated prefix | `<0.000266448` |

The last two use additional source data. They are not attributed to a
new analytic estimate here. In particular (12) is **not a lower bound for
I_r**, not an obstruction to (7) kept signed, and not a universal no-go
for transport. It quantifies why the source-minus-approximation
cancellation is indispensable: each prefix may be large while their
difference is small. The known annihilation of n=1 alone does not pay it.

## Verification, controls and handoff

The [checker][checker] compares (4)–(6), (9) and (10) with separately
differentiated power series at the nine corner/center combinations.
These support the written identities; they are not a proof by sampling.
It detects omission of normalizer terms and full profile derivatives.
The point obstruction is the only new numerical inequality claimed.

For `H=x^2-2(t-tc)`, `A=1`, `theta=x`, `f=2cos x`, the filtered physical
source is `x^2+2` and the filtered f is zero. At the event x=0 with anchor
-1, `|I_H|=sqrt(5)=|W_H(-1)|`; strict anchor preservation fails. The
oscillator control has zero defect, demonstrating that annihilation is a
generic identity. Both are checked with their own exact formulas.

The [fresh source-specific replay][controlrecord] rejects five event boxes
and the Euler negative-Laguerre witness with their own source errors.
Its legacy producer hardcodes the source-version date 2026-10-18;
execution for this task was on 2026-10-19. No new acceptance consumer was
introduced. Finite-prime/square controls lack the full normalized theta
source; reflected/shape/primitive controls lack its unchanged square
coefficients; Euler controls alter the level-one data; polynomial and
counter-kernel controls lack the exact theta source. These differing
premises, detailed in the [control summary][controls], do not turn the
generic operator identity into an arithmetic bound.

S03-T1 is complete as a derivation and scoped obstruction. **S03-T2 is
Ready** to estimate (7), retaining the source/arithmetic subtraction before
absolute values and declaring its information class. S03-T3 still waits
for that allowance. Existing transport/direct radii and real/complex
coverage are unchanged; the real bridge `(1001,exp(2000))` and global
complex exterior remain open. No manuscript or snapshot is created.

[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[s14]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a1]: ../../../../../../avoid/01_restating_the_target.md
[a7]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[s02]: ../../02_cutoff_reflection/notes/03_COMPLETE_FROZEN_JETS_AND_PAID_CONSUMERS_20261019.md
[opening]: 01_SIGNED_TRANSPORT_AND_DIRECT_JET_COMPARISON_20261018.md
[correlated]: 02_CORRELATED_ARITHMETIC_RESIDUAL_AND_PAID_TRANSPORT_20261018.md
[n07]: ../../../notes/07_HODGE_MODULAR_DUALITY_AND_ROTATION_DEFECT_20261018.md
[contour]: ../../../manuscript/positive_arithmetic_packets/sections/07_shifted_approximation.tex
[evaluator]: ../../../numerics/high_height_consumer/high_height_consumer.py
[record]: ../numerics/S03_FILTERED_MECHANISM_20261019.json
[checker]: ../numerics/check_filtered_residual_mechanism.py
[controlrecord]: ../numerics/S03_T1_SOURCE_CONTROLS_20261019.json
