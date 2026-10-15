# Center and separation coordinates: full reflection, mixed cutoff sectors and an exact collision control

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This note gives exact two-source formulas, identifies a cutoff-specific cancellation, and proves a control obstruction to arguments using source reflection and generic positive Gram forms alone. It establishes no theta signed-core inequality.

## 1. The full reflected product

For the actual complete theta source, extend `Φ` by its proved even reflection to the whole real line and set

\[
 \mu_t(u)=e^{tu^2}\Phi(u),\qquad
 W_j(t,x)=h_j(t,x)=\frac12\int_{\mathbb R}(iu)^j\mu_t(u)e^{ixu}\,du,
 \qquad j=0,1.
\]

All integrals and derivatives below converge absolutely on compact real time-space sets. Introduce **physical source** center and separation coordinates

\[
 a=(u+v)/2,\qquad b=(u-v)/2,\qquad du\,dv=2\,da\,db,
\]

and the real kernel

\[
 K_j(t;a,b)=(-1)^j(a^2-b^2)^j
            \mu_t(a+b)\mu_t(a-b).
\tag{1}
\]

Full source reflection makes this kernel even separately in `a,b`. It also gives `K_j(b,a)=(-1)^jK_j(a,b)`. These are exact symmetries. The kernel is nonnegative for `j=0`; for `j=1` it has the factor `b²−a²` and is signed.

Multiplication of the full-line transforms, the change of variables, and the separate evenness give

\[
 \boxed{W_j(t,x)W_j(t,x+\delta)
 =\frac12\int_{\mathbb R^2}K_j(t;a,b)
 \cos((2x+\delta)a)\cos(\delta b)\,da\,db.}
\tag{2}
\]

The diagonal is `W_j(t,x)^2=(1/2)∫K_j cos(2xa)`. Thus the complete exponential-average observation has the exact physical kernel

\[
 \boxed{\mathcal A_{j,\delta}
 =\frac12\int_{\mathbb R^2}K_j(t;a,b)
 \{\cos(2xa)-e^{-\delta}\cos((2x+\delta)a)\cos(\delta b)\}\,da\,db.}
\tag{3}
\]

Source reflection has exposed the cosine phases; it has not made them nonnegative. Even branch 0 retains a changing center phase at nonzero spectral coordinate. These physical coordinates must not be confused with a change of **lattice indices** in a theta addition formula: the two changes of variables concern different objects.

## 2. What complete stationarity actually removes

Differentiating (2) at `δ=0` gives

\[
 W_j(t,x)W_{j,x}(t,x)
 =-\frac12\int_{\mathbb R^2}aK_j(t;a,b)\sin(2xa)\,da\,db.
\]

On the full stationary set `W_(j,x)=h_(j+1)=0`, this moment vanishes. Hence (3) is equivalently

\[
\begin{aligned}
 \mathcal A_{j,\delta}
 ={}&(1-e^{-\delta})W_j(t,x)^2\\
 &+\frac{e^{-\delta}}2\int_{\mathbb R^2}K_j(t;a,b)
 \big[\cos(2xa)\{1-\cos(\delta a)\cos(\delta b)\}\\
 &\hspace{43mm}+\sin(2xa)\{\sin(\delta a)\cos(\delta b)-\delta a\}\big]\,da\,db.
\end{aligned}
\tag{4}
\]

The subtracted first-order term uses complete stationarity exactly. The first residual bracket begins at order `δ²`; the second at order `δ³`. Neither has a fixed sign after multiplication by the center phase. At `x=0`, branch 0 is favorable directly: `sin(2xa)=0`, `cos(2xa)=1`, and `1−cos(δa)cos(δb)≥0`. This recovers the elementary bound from the positive cosine source at the origin. It does not extend that sign to general stationary points.

The local collision control below proves that the remaining freedom is substantive, even after imposing source positivity, full source reflection, complete stationarity and every positive Fourier Gram constraint.

## 3. Endpoint-only cutoff creates an essential second sector

For the endpoint-only cutoff define the even extension

\[
 \nu_{t,N}(u)=e^{tu^2}\sum_{n=1}^N\phi_n(|u|).
\]

This is the extension whose full-line Fourier transform is the manuscript's half-line `W_(j,N)`. It is **not** asserted to be the analytic negative-`u` continuation of the finite theta sum, nor to satisfy complete theta reflection. No source-variable differentiation of this extension is needed here.

Put `w_j(a,b)=(-1)^j(a²−b²)^j` and define

\[
 K_{j,N}^{\pm}(a,b)=\frac{w_j(a,b)}2
 \{\mu_t(a+b)\nu_{t,N}(a-b)
 \pm\mu_t(a-b)\nu_{t,N}(a+b)\}.
\tag{5}
\]

The plus kernel is separately even; the minus kernel is separately odd in the two variables. Directly taking the real part of the full-line product gives

\[
\boxed{\begin{aligned}
 W_j(t,x)W_{j,N}(t,x+\delta)
 =\frac12\int_{\mathbb R^2}\big[&K_{j,N}^+\cos((2x+\delta)a)\cos(\delta b)\\
 &+K_{j,N}^-\sin((2x+\delta)a)\sin(\delta b)\big]\,da\,db.
\end{aligned}}
\tag{6}
\]

The sine–sine sector vanishes for **equal** complete sources, but not generally for the mixed complete/cutoff product. Dropping it is not a valid use of reflection.

More precisely, call the two complete integrals in (6) `C_N,S_N`, including their factor `1/2`. Exchanging the sources changes the sign of the minus kernel, so

\[
 \boxed{C_N=\tfrac12\{W_j(x)W_{j,N}(x+\delta)
                      +W_{j,N}(x)W_j(x+\delta)\},}
\]
\[
 \boxed{S_N=\tfrac12\{W_j(x)W_{j,N}(x+\delta)
                      -W_{j,N}(x)W_j(x+\delta)\}.}
\tag{7}
\]

Time arguments are suppressed only in these two displays. At a physical zero of the starting value, the actual mixed product vanishes, while the two sectors can be nonzero and cancel exactly. Replacing the mixed product by its exchange-symmetric sector introduces the extra product `W_(j,N)(x)W_j(x+δ)`, whose starting factor is truncated. Consequently a separate absolute estimate of the two sectors can lose the crucial `√E` payment. The correct factor-preserving estimate is obtained only after recombining

\[
 W_j(x)\{W_j(x+\delta)-W_{j,N}(x+\delta)\}.
\tag{8}
\]

There is a related stationarity warning:

\[
 \left.\partial_\delta[W_j(x)W_{j,N}(x+\delta)]\right|_{\delta=0}
 =W_j(x)W_{j,N}'(x),
\]

which need not vanish under `W_j'(x)=0`. The full-source stationarity subtraction (4) therefore cannot be copied into the mixed cutoff product without its derivative-tail term. One may instead use (4) for the complete product and then use (8).

## 4. An exact reflected super-Gaussian collision

The following fixed-time control makes the missing sign explicit, without a perturbative choice of collision time. Set `T=1/4`,

\[
 \kappa(u)=e^{-u^4},\qquad
 g(u)=\kappa(u)+\tfrac12\kappa(u-4)+\tfrac12\kappa(u+4),
\]
\[
 \Phi_*(u)=c e^{-Tu^2}g(u),\qquad
 c=\left(16\int_0^\infty\cosh(v)e^{-Tv^2}g(v)\,dv\right)^{-1}>0.
\tag{9}
\]

The source is strictly positive, even and entire in `u`, with super-Gaussian real decay of every derivative. Its heat transform is jointly entire in heat time and spectral coordinate. At the exact time T, ordinary Fourier translation gives

\[
 \boxed{H_*(T,x)=cF(x)(1+\cos4x),\qquad
 F(x)=\int_0^\infty e^{-u^4}\cos(xu)\,du.}
\tag{10}
\]

There is an elementary rigorous positive interval for F. Write `M_k=∫₀∞u^k exp(−u⁴)du`. Integration of the derivative of `u exp(−u⁴)` gives `M_4=M_0/4`; Cauchy–Schwarz gives `M_2²≤M_0M_4`, hence `M_2≤M_0/2`. The global inequality `cos z≥1−z²/2` now gives

\[
 \boxed{F(x)\ge M_0(1-x^2/4)>0\qquad(|x|<2).}
\tag{11}
\]

At `x_*=π/4<1`, the factor `1+cos4x` and its first derivative vanish, while its second derivative is 16. Therefore

\[
 H_*(T,x_*)=H_{*,x}(T,x_*)=0,\qquad
 H_{*,xx}(T,x_*)=16cF(x_*)>0.
\tag{12}
\]

This is an exact nondegenerate positive-time collision, with a full stationary predecessor supplied by the analytic implicit-function theorem. It is a control source, **not** the theta source.

For the fixed scale `δ=1/4`, `x_*+δ<29/28<2` and

\[
 H_*(T,x_*+\delta)=cF(x_*+\delta)(1-\cos1)>0.
\]

Thus the exponential-average collision law gives

\[
 \frac{\mathcal A_{0,1/4}(T-s,\chi(s))}
 {\sqrt{E(T-s,\chi(s))}}
 \longrightarrow-d_*<0,\qquad
 d_*=e^{-1/4}cF(\pi/4+1/4)(1-\cos1).
\tag{13}
\]

For example, `e^(−1/4)≥3/4`, `F(π/4+1/4)≥(2295/3136)M_0`, and `1−cos1≥11/24` give an explicit strictly positive rational multiple of `cM_0` as a lower bound for `d_*`. The accompanying Arb check gives `H_xx(T,x_*)≈0.559066893968` and `d_*≈0.011546502002`, with rigorous complete tails. The analytic proof does not depend on these decimal values.

## 5. Reflection, primitive endpoints and all generic Gram constraints still hold

Define the decaying half-line primitive

\[
 \psi_*(u)=8\int_u^\infty\sinh(v-u)\Phi_*(v)\,dv.
\]

It is strictly positive and satisfies `ψ_*″−ψ_*=8Φ_*`. Normalization (9) gives `ψ_*′(0)=−1/2`. Since the source is even, differentiating the ODE proves

\[
 \psi_*^{(2k+1)}(0)=-\tfrac12\quad(k\ge0),\qquad
 P_*(u)=e^u+2\psi_*(u)\text{ is even}.
\tag{14}
\]

The solution extends to an entire primitive by its ODE. The complete reconstruction and its lower endpoint constant therefore hold. These are source-level reflection and endpoint identities. The control is not claimed to possess a section obeying full elliptic automorphy. In fact, it cannot have any nonzero polynomial-growth integer-square source expansion of the manuscript's type. Indeed,

\[
 \log\Phi_*(u)=-u^4+O(u^3)\qquad(u\to+\infty),
\]

whereas, if `Φ_a=∑_(n≥1)a_n φ_n` with polynomial-growth coefficients and `n_0` is the least index with `a_(n_0)≠0`, least-mode dominance gives

\[
 \Phi_a(u)=2a_{n_0}(\pi n_0^2)^2 e^{9u}
       e^{-\pi n_0^2e^{4u}}(1+o(1)),\qquad
 \log|\Phi_a(u)|=-\pi n_0^2e^{4u}+9u+O(1).
\tag{14a}
\]

Polynomial growth controls the remaining mode sum uniformly in this limit. The two decay rates are incompatible. Thus the control lies demonstrably outside the coefficient class in which the manuscript's reflection-rigidity theorem identifies theta.

Moreover, for any finite spectral points `x_k` and complex scalars `z_k`, at every real heat time,

\[
 \sum_{k,\ell}z_k\overline{z_\ell}H_*(t,x_k-x_\ell)
 =\frac12\int_{\mathbb R}\mu_{*,t}(u)
       \left|\sum_kz_ke^{ix_ku}\right|^2du\ge0.
\tag{15}
\]

The same statement holds for every finite Gram matrix of polynomial-exponential test functions in `L²(μ_( *,t)du)`. Thus positivity of all such source/Fourier Gram forms, full source reflection, the complete primitive endpoints, and complete stationarity do not by themselves give the required starting-energy bound. Equation (13) is a counterexample.

This control is a simple exact-time illustration adapted to the present two-source kernel. It is **not** stronger in source-shape properties than [Investigation 21, Note 56](../../../21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md), whose different control also preserves monotonicity, strong log-concavity and positivity of the heat-first primitive cosine transform. Those additional properties are not claimed for (9). The common lesson is that a successful sign mechanism must use arithmetic information beyond the source reflection and generic positive forms.

## 6. The omitted mixed sector can be exhibited in this control

At time T, approximate only the endpoint density by

\[
 \nu_\varepsilon(u)=c\{\kappa(u)
    +(1-\varepsilon)[\kappa(u-4)+\kappa(u+4)]/2\},
 \qquad0<\varepsilon\le1.
\]

This density is positive, even, no larger than `μ_( *,T)=cg`, and converges to it as `ε→0`. Its half Fourier transform is

\[
 W_\varepsilon(x)=cF(x)[1+(1-\varepsilon)\cos4x].
\]

At the exact physical collision, `H_*(T,x_*)=0` but
`W_ε(x_*)=cεF(x_*)>0`. With `δ=1/4`, (7) gives

\[
 C_\varepsilon
 =\tfrac12c^2\varepsilon F(x_*)F(x_*+\delta)(1-\cos1)>0,
 \qquad S_\varepsilon=-C_\varepsilon,
\tag{16}
\]

whereas their sum, the actual complete-start/partial-endpoint product, is zero. This proves that the odd exchange sector is not a removable bookkeeping term even for positive even endpoint approximations. It also displays exactly how independent sector bounds can produce a pure error of order ε at an event where the correct combined remainder is zero. This approximation is a bump-component control, not a theta lattice cutoff; the sector identity (6) itself applies to the actual theta cutoff.

## Verification and decision

The accompanying checker verifies the finite Fourier-sector algebra exactly and supplies validated quadrature for the control's moments, normalization, collision curvature, fixed-endpoint defect and nonzero mixed sectors. Its complete tails use `∫₄∞e^(−u⁴)du≤e^(−256)/256` and, for the normalization integral, `g(u)≤2e^(−u⁴/16)` for `u≥8`, giving a tail at most `e^(−128)/32`. Analytic Fourier translation, reflection, endpoint recurrence, Gram positivity and the collision law have the separate proofs above.

Artifacts: [complete checker](../../numerics/check_theta_center_separation.py) and [execution receipt](../../numerics/THETA_CENTER_SEPARATION_CHECKS_20261015.json). From `numerics/`, run `python3 check_theta_center_separation.py --output THETA_CENTER_SEPARATION_CHECKS_20261015.json` with python-flint 0.9.0 installed. Without `--output`, the result is printed as JSON. The default 160-bit replay passes 38 exact or interval assertions. No sampled theta inequality is asserted.

The bounded conclusion is to preserve both mixed sectors and the complete starting factor in any addition-formula calculation. Full reflection and generic positive forms provide useful symmetries but no new signed estimate here. The remaining arithmetic task is a relation that actually restricts the residual center phase or its coupled integral, beyond the symmetries and constraints that the control satisfies.
