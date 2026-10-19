# UAR-02: uniform finite gamma and heat remainder

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**. Separate same-model central-derivation, Gaussian-tail and adversarial readers; internal LLM review, no specialist human review.

**Outcome: proved in-note, with outward checks of the constants.** The finite gamma/heat remainder after the prescribed first correction is uniformly controlled through the growing cutoff, on both frozen-cutoff choices of [UAR-01][contract]. This supplies UAR-02's finite-component input. It is not an estimate of the complete corrected residual: the signed retained correction, RS edge, cutoff transitions and physical anchor remain in their declared destinations. UAR-03 is Ready; UAR-04 waits for its useful edge output.

Classification under [avoid/01][a01]: a quantitative component theorem, not a nonvanishing criterion. Read the [result summaries][results] and [patterns to avoid][avoid], particularly [collision controls][controls], [theta bookkeeping][theta], [scoped claims][a07], [normalization][a08] and [signed recombination][a12]. The correction itself and the Gaussian-shift mechanism are inherited from [S03 Note 06][n06]. The new result is their explicit uniform growing-height error and summed first-jet payment.

## 1. Statement in the selected normalization

Keep exactly UAR-01's M, m0, alpha, A, theta, branches and approximation f_N=(G_N-Chat_N^an)/A. Let

\[
0<t\le1/20,\quad1\le\kappa\le2,\quad L=\kappa/t,
\quad c=4\pi e^L,\quad R=1/L,\quad a_*=\kappa(4-\kappa)/16.
\]

The physical disk is D_c={|z-c|<=R}; its real half-window is W_c. Freeze either extremal natural cutoff on [c-R,c+R], including both integers at a crossing. Then N<=exp(L/2)+1. All assertions below also hold for every finite prefix M<=N, with that prefix in place of N. No floor-defined function is differentiated.

For w=s(z)=(1-iz)/2 or w=1-s(z), put ell=log n and

\[
\begin{aligned}
R_n(w)&=\pi^{-1/2}\int_{\mathbb R}e^{-v^2}
 M(w+\sqrt t\,v)n^{-w-\sqrt t\,v}\,dv,\\
g_n(w)&=\exp\{m_0(w)-w\ell+t(\alpha(w)-\ell)^2/4\},\\
\chi_n(w)&=\frac1{6w}+\alpha'(w)
 \left\{\frac t4+\frac{t^2(\alpha(w)-\ell)^2}{8}\right\},\\
R_n(w)&=g_n(w)(1+\chi_n(w)+e_n(w)).
\end{aligned}                                                    \tag{1}
\]

**Theorem 1 (uniform relative remainder).** On the enlarged physical disk |z-c|<=2, for every 1<=n<=N and either channel,

\[
|e_n(w(z))|<2c^{-2}.                                        \tag{2}
\]

On D_c, the same holomorphic relative error satisfies

\[
|\partial_z e_n(w(z))|<2c^{-2}.                             \tag{3}
\]

The estimate retains all heat weights and phases at n comparable to N. It makes no fixed-mode substitution. The radius-two domain is used for relative-error Cauchy only; the summed normalized mass bound below is on the much smaller D_c.

Let P_N, G_N and K_N be UAR-01's exact finite heat sum, leading finite sum and prescribed signed correction. Define d_(AB,N)=(P_N-G_N-K_N)/A. Then:

**Theorem 2 (summed normalized remainder).** Uniformly on D_c,

\[
|d_{AB,N}|<E_0(c)=\frac{56e^{a_*/t}}{c^2},\qquad
|\partial_zd_{AB,N}|<E_1(c)
 =\frac{56(.6L+1)e^{a_*/t}}{c^2}.                           \tag{4}
\]

On W_c, in the rotating metric Z_d=exp(-i theta)(d-i d_x/omega),

\[
|Z_{d_{AB,N}}|<\Delta_{AB}(c)=\frac{160e^{a_*/t}}{c^2}.      \tag{5}
\]

This is an endpoint remainder payment. At two endpoints add their respective Delta_AB values; it does not include the retained signed model increment or any cutoff-transition sum. In particular (5) cannot be inserted as a bound for the whole piecewise UAR-01 increment.

The scale is explicit:

\[
\frac{e^{a_*/t}}{c^2}
 =\frac1{16\pi^2}\exp\left\{-\frac{\kappa(\kappa+28)}{16t}\right\}.
                                                                    \tag{6}
\]

It is largest at t=1/20, kappa=1. There E0<6.5e-17, E1<8.4e-16 and Delta_AB<1.9e-16; the [outward record][record] gives tighter balls. These are finite-component upper allowances, not measured errors or physical margins.

## 2. Uniform Gaussian shift and central payment

It is enough to prove one channel; the estimates depend on |Im w| and the other is its reflected analytic counterpart. On |z-c|<=2,

\[
\Re w\in[-.5,1.5],\quad |\Im w|\in[c/2-1,c/2+1],\quad
.499c<|w|,|w-1|<.501c,\quad c>10^9.                         \tag{7}
\]

The explicit alpha formula gives |Im alpha|<.8 and |alpha|<=L/2+1. More specifically Re alpha differs from L/2 by less than .002. Since ell<=L/2+.001 and ell>=0, also |alpha-ell|<=L/2+1. These bounds follow from half the logarithm of 2|w|/c and the rational part 1/(2w)+1/(w-1); the [checker][checker] verifies the compressed constants. Set

\[
A_n=\alpha(w)-\ell,\quad b=tA_n/2,\quad
\delta=\sqrt t\,v+b,\quad |b|\le(\kappa/2+t)/2\le.525<.6.
\]

Shift the Gaussian contour by sqrt(t) A_n/2. Its connecting strip stays a distance greater than .49c from the real gamma poles: the imaginary shift in w is at most t|Im alpha|/2<.02. At fixed c,n,t the Gaussian dominates gamma's exp(O(|v| log|v|)) growth on both closing ends. Thus, exactly,

\[
R_n/g_n=\mathbb E e^h,\quad
h=S(w+\delta)+m_0(w+\delta)-m_0(w)-\alpha(w)\delta,
\quad S=\log(M/M_0),\ M_0=e^{m_0},                         \tag{8}
\]

where E is the normalized real Gaussian. Globally, e^h means M(w+delta) exp(-m0(w)-alpha(w)delta); no principal logarithm of a gamma value is presumed. Put

\[
q=1/(6w)+\alpha'(w)\delta^2/2.
\]

The exact Gaussian moments E delta^2=t/2+t^2 A_n^2/4 give Eq=chi_n. In particular its heat-curvature term is prescribed independently of H.

Choose the height-dependent central cutoff |v|<=W=2 sqrt(c), and d=.224|v|+.6. Then |delta|<=d<=.449 sqrt(c), and every Taylor segment w+lambda delta has distances from 0 and 1 greater than .49c. Direct differentiation gives

\[
|\alpha'(w)|<1.01/c,\qquad
\sup_{0\le\lambda\le1}|\alpha''(w+\lambda\delta)|<2.1/c^2.
\]

Import the logarithmic Stirling remainder from [DLMF 5.11(ii)][dlmf], applied to Gamma(z/2):

\[
|S(z)-1/(6z)|\le\frac{\sec^4(\arg z/2)}{45|z|^3}.           \tag{9}
\]

On the central region |arg z|<pi/2+.001, so sec^4(arg z/2)<5 and (9)<c^-3. This is a central-region bound only; it is not applied on the unbounded horizontal tails. Taylor's formula and the reciprocal difference yield

\[
|h-q|<\frac{.7d+.35d^3}{c^2}+c^{-3},\qquad
|h|<\frac{.35+.511d^2}{c}<.11.                              \tag{10}
\]

For example 1/(6(.499)(.49))<.7 is the reciprocal-difference coefficient, and 2.1/6=.35 is the cubic Taylor coefficient. To obtain the second envelope, bound q by [.334002+.505d^2]/c and absorb the smaller terms from the first envelope using d/c<=.449/sqrt(c).

The positive Gaussian moment bounds are

\[
\mathbb E d<.727,\quad\mathbb E d^2<.538,\quad
\mathbb E d^3<.407,\quad\mathbb E d^4<.315.
\]

Their full-line expectations bound the central integrals. Hence

\[
\begin{aligned}
\mathbb E_{|v|\le W}|h-q|&<.65135c^{-2}+c^{-3},\\
\mathbb E_{|v|\le W}|h|^2&<.397196c^{-2},\\
\mathbb E_{|v|\le W}|e^h-1-q|
 &\le\mathbb E|h-q|+\tfrac12e^{.11}\mathbb E|h|^2
 <.874c^{-2}.
\end{aligned}                                                   \tag{11}
\]

## 3. Both complete Gaussian tails

For u=|v|>=2 sqrt(c), write zeta=w+delta and sigma=Re(zeta/2). The enlarged-disk geometry gives

\[
|\delta|\le.225u,\quad
\sigma\le1.05+.112u\le.113u,\quad
|\zeta|,|\zeta-1|\le c+u.
\]

If sigma<=1, gamma recurrence shifts the real part into [1,2]. Every recurrence denominator has modulus greater than one, since the imaginary part stays of size c/4. The gamma integral and log convexity on [1,2] then give |Gamma(zeta/2)|<=1. If sigma>=1, the same integral gives

\[
|\Gamma(\zeta/2)|\le\Gamma(\sigma)\le(2\sigma)^\sigma,
\qquad\log(2\sigma)\le\sigma.
\]

The real gamma bound follows by splitting e^(-v) into two halves, maximizing v^(sigma-1)e^(-v/2), then integrating the remaining e^(-v/2). Therefore log|Gamma(zeta/2)|<.013u^2 in both cases.

The polynomial prefactor contributes less than .001u^2 in logarithmic absolute value: c<=u^2/4 and c+u<=u^2/3, so 4log u is already an upper bound. The remaining factors obey

\[
\begin{aligned}
\log|\pi^{-\zeta/2}e^{-\alpha(w)\delta}|
 &\le1.203+.129u+(L/2+1)(.224u+.6)\\
 &\le1.203+.1293u+.000112u^2<.001u^2.
\end{aligned}                                                   \tag{12}
\]

Here L/2+1<=.5 log c+1<=sqrt(c)/1000<=u/2000. The middle inequality holds at 10^9 and its difference increases thereafter. Directly from m0 and (7),

\[
\Re m_0(w)\ge-\pi c/8-.75\log c-5\ge-c.
\]

The gamma-angle term costs at most pi c/8+1.3, the logarithmic real-power term at most .75 log c, and the remaining constant/linear real terms fit below 3.7; the positive log|w| and log|w-1| can be discarded. Thus the exact tail integrand satisfies

\[
e^{-v^2}|e^h|\le e^{c-.985u^2}\le e^{-.7u^2}.              \tag{13}
\]

For the model, |1+q|<=2+.026u^2/c<=exp(u^2/4), so it has the same safe tail majorant. Integrating both exact tails and both model tails gives

\[
\mathbb E_{|v|>W}|e^h-1-q|
 \le\frac{e^{-2.8c}}{.7\sqrt{\pi c}}<c^{-10}.                \tag{14}
\]

All compressions in (12)-(14) follow from decreasing log u/u^2 or inverse powers, and the stated lower endpoints; the checker records their endpoint reserves and monotonicity conditions. Equations (11) and (14) prove (2), with substantial room below the selected 2/c^2 allowance. The finite Gaussian integrals depend holomorphically on z on the enlarged disk, with locally uniform tail domination, and g_n is nonzero. Radius-one Cauchy around any z in D_c stays inside |z-c|<=2 and proves (3).

## 4. Summing through the growing cutoff

On the real center c, write p_n=g_n(s)/A and retain the full weight

\[
|p_n(c)|=\exp\{t\ell^2/4-(1/2+t\Re\alpha(s)/2)\ell\}.
\]

The exact identity

\[
\Re\alpha(s)=L/2+\tfrac14\log(1+c^{-2})-\frac1{1+c^2}
 \ge L/2-c^{-2}
\]

shows that this is at most 1.000001 times

\[
W_n=n^{-1/2}\exp\{t\ell^2/4-\kappa\ell/4\}.
\]

Let Y=L/2. For n<=exp(Y), W_n is decreasing, and its sum is bounded by one plus its integral. Substitution n=exp(y) gives the exponent

\[
F(y)=(1/2-\kappa/4)y+ty^2/4,
\quad F(Y)=a_*/t,
\quad \int_0^Y e^{F(y)}dy\le\frac{8}{4-\kappa}e^{F(Y)}\le4e^{F(Y)}.
\]

The inequality uses convexity F(y)<=yF(Y)/Y. The possible additional extremal-cutoff mode costs at most one in W_n. Thus the complete one-channel real mass is less than 7 exp(a_*/t), including that extra mode and the exact-alpha factor. This bound is independent of the number of modes.

On D_c the analytic logarithmic derivative is exactly

\[
(\log p_n)_z=i\omega+i\ell/2+i t\ell\alpha'(s)/4.
\]

Use omega=-[beta(s)+beta(1-s)]/4, beta=alpha(1+t alpha'/2), the bounds above and L>=20. They give |omega|<L/4+.501 and |(log p_n)_z|<.6L; the reflected channel has the same bound. Transport from c through D_c costs exp(.6)<2, so the **two-channel** normalized mass is below 28 exp(a_*/t). This mass estimate is not asserted on the radius-two relative-error disk.

Multiply (2)-(3) by these normalized modes and differentiate their products, including A_x/A. This proves (4). For real t and frozen N the combined d_AB is real on the real axis, so

\[
|Z_d|^2=d^2+(d_x/\omega)^2.
\]

UAR-01's bound |omega|>L/4.001 on W_c yields

\[
|Z_d|<56\sqrt{1+[4.001(.6+1/L)]^2}\ e^{a_*/t}/c^2
 <160e^{a_*/t}/c^2,
\]

proving (5). An independent-coordinate triangle bound would not justify the constant 160. The maxima of (4)-(5) follow from (6); for E1, ( .6L+1)exp(-29L/16) decreases for L>=20.

## 5. Comparison, controls and usable scope

The same enlarged-disk argument gives |chi_n|<.5/c. A common **finite-component envelope ledger** before retaining K_N would pay the relative allowance .5/c+2/c^2, with the same normalized mass and derivative factors. After retaining the explicit signed K_N the relative remainder allowance is 2/c^2. Their allowance ratio is 4/(c+4)<4/c. This compares two complete finite-component upper bounds in one ledger; it is neither an actual-error ratio nor a comparison with the strongest complete physical consumer. The signed K_N must still be recombined with the signed edge before an increment norm is taken.

The [fresh source-own control replay][control-record] rejects all five existing event boxes and the separate Euler negative-Laguerre witness in the unchanged downstream interfaces. Its source producer's historical date is preserved separately from this run. No theta constants are assigned to those altered sources. The premise screen is:

| Control family | Premise absent from the complete theta application |
| --- | --- |
| Finite-prime orbit and finite weighted squares | Complete unchanged normalized theta reflection and coefficient sequence. No effective event height is invented for analytic-only constructions. |
| Reflected, shape and positive-primitive sources | The specific theta integer-square expansion with its matching completed gamma/RS source. Shape/reflection alone is insufficient. |
| Euler deformation | Unchanged level-one completed coefficients and edge. Its negative-Laguerre witness is not relabeled as an enclosed event. |
| Polynomial event, counter-kernel and moving wall | The stated arithmetic source representation. Generic transport identities still apply; a future consumer must reject own-source events and pay wall flux. |

The finite gamma-mode estimate also applies wherever those same modes occur; it alone distinguishes no colliding field. The control replay screens the interpretation and unchanged consumer, not the new analytic theorem. No physical acceptance rule has changed.

The [checker][checker] evaluates the proof's scalar reserves and opening maxima at 192/256 bits with outward Arb arithmetic, checks exact correction moments and invalid input/source guards, and pins the mathematical source bytes. The [separate same-model review][review] assesses the analytic proof and fresh scalar replay. Neither same-implementation replay nor a matching hash establishes implementation independence. No complete-source H quadrature, H Taylor data or inferred edge values enter this result.

**Decision:** UAR-02 is Complete at its uniform finite-component gate and supplies a usable error input to the common contract. UAR-03 still owes its signed edge model, complete complex-disk error and cutoff matching. UAR-04 still owes the combined signed bound with every partial prefix and transition. Physical anchors, a total cost advantage, new collision coverage, the real bridge and complex exterior remain open. No manuscript snapshot is created.

[contract]: ../../notes/07_UAR01_CORRECTED_RESIDUAL_AND_TRANSITION_CONTRACT_20261019.md
[n06]: 06_ARITHMETIC_GAMMA_AND_EDGE_CORRECTIONS_20261019.md
[checker]: ../numerics/check_uniform_finite_gamma_heat.py
[record]: ../numerics/UAR02_UNIFORM_FINITE_GAMMA_HEAT_20261019.json
[control-record]: ../numerics/UAR02_SOURCE_CONTROLS_20261019.json
[review]: ../reviews/08_UAR02_UNIFORM_FINITE_GAMMA_HEAT_INTERNAL_REVIEW_20261019.md
[dlmf]: https://dlmf.nist.gov/5.11#ii
[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
