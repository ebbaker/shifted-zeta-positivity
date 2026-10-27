# Matched raw and shifted source budgets for the physical first jet

27 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.
Chat0005, **Continue heat-flow research**, thread
`01a17e41-99d3-79c1-b932-2bae84ad0d47`; continuation requested after Note14.

**Status: proved in-note complete analytical comparison and fixed-cutoff
calibrations; internal same-model review.** Both source representations
receive the same physical first-jet target, including frequency, arithmetic,
quadrature and coefficient errors. Completion before truncation preserves
an actual exponential error gain. Smaller quadrature order alone does not
establish a smaller optimized total ledger. [Note16][n16] performs that
optimization and gives a positive-slab moving-contour gain. No theta jet
lower bound, new covered slab, or Newman upper bound is obtained.

The assignment is [Note14][n14]. The raw construction is [Note13][n13];
the two-arm contour and sharp mode tail are inherited from
[arithmetic-rigidity Note06][ar06], not new contour methods. The
[result index][results], [controls][controls], [avoid index][avoid],
[classification][a01], [premise screen][a02], [scope][a07] and
[coupled-estimate rule][a12] apply. [Review07][review] records the checks.

## 1. Common domain, target, and exact completion

Fix 0<b<=B<=1/2, A>=0, Delta>=0 and X=A+Delta. On the same real box
t in [b,B], x in [A,X], fix a positive length ell and prescribed errors
epsilon_0,epsilon_1>0 for (H,H_x), optionally divided by an explicitly
positive carrier P(t,x). The raw case is included by setting the contour
shift sigma=0. Otherwise 0<sigma<alpha=pi/8. Put

\[
 c_\sigma=\cos(4\sigma)>0,\quad\eta_\sigma=\pi c_\sigma,
 \quad w_t(v)=e^{tv^2}\Phi(v).
\]

Full theta reflection and contour deformation give exactly

\[
 H(t,x)=\frac{e^{-\sigma x}}2\int_0^\infty
 [w_t(u+i\sigma)e^{ixu}+w_t(u-i\sigma)e^{-ixu}]du.          \tag{1}
\]

This identity precedes both truncations. For the physical derivative
j=0,1, the two integrands acquire factors [i(u+i sigma)]^j and
[-i(u-i sigma)]^j, respectively. The -sigma in the derivative of the
prefactor is included. At sigma=0 the paired formula is precisely the
raw cosine representation, with the same physical derivatives.

The full source is holomorphic in |Im v|<alpha and even there.
Reflection supplies decay on the negative half-line. The remote contour
limit is taken for each fixed sigma<alpha; no uniform strip-edge limit
is asserted. [Polymath equations (3)-(4)][poly] fix the source normalization;
the local contour proof and its limitations are in ar06.

## 2. Frequency and arithmetic tails on both arms

One finite explicit full-source constant is

\[
 I_k(\eta)=\frac12\sum_{h=0}^k\binom kh
       \eta^{-(h+1)/2}\Gamma((h+1)/2),
\quad C_\sigma=e^{\eta_\sigma}
             [2\pi^2 I_4(\eta_\sigma)+3\pi I_2(\eta_\sigma)].
\]

Indeed sum_(n>=1)n^k exp(-eta n^2)<=I_k(eta), by integration over
[n-1,n] with (u+1)^k exp(-eta u^2). Also
(n^2-1)(e^(4u)-1)>=0. Therefore

\[
 |w_t(u\pm i\sigma)|\le e^{-b\sigma^2}C_\sigma
             e^{Bu^2+9u-\eta_\sigma e^{4u}},\qquad u\ge0.
\]

A coarser convenient constant is
C_sigma<=30000 max(1,eta_sigma^(-3)): the relevant half-integer gamma
values are below 2, I_4<=16 max(1,eta^(-3)), I_2<=4 max(1,eta^(-3)),
and e^eta<81, pi^2<10. Either declared upper constant may be used.

For V>=1 let L_V=(eta_sigma/2)e^(4V). The gate

\[
 BV^2+10V\le L_V                                            \tag{2}
\]

propagates to u>=V, since (Bu^2+10u)e^(-4u) decreases there. It proves
the complete frequency error, for j=0,1,

\[
 E_{V,j}(t,x)\le e^{-\sigma x-b\sigma^2}
 C_\sigma(1+\sigma)^j\frac{e^{-L_V}}{4L_V}.                \tag{3}
\]

Here (u+sigma)^j<=(1+sigma)^j e^u supplies the j=1 payment. Substitution
y=L_u proves the factor 1/(4L_V). A sufficient gate onset is
V>=max(1,(1/2)log(2(B+10)/eta_sigma)); sharper choices may test (2)
directly. A raw comparison uses sigma=0 in these same formulas.

Retain unchanged theta modes n=1,...,K and put M=K+1. Require

\[
 \beta_M=4\eta_\sigma M^2-9>0,\quad
 8\eta_\sigma M^2\ge B,\quad
 r_M=((M+1)/M)^4e^{-\eta_\sigma(2M+1)}<1.
\]

Define S_M=(2pi^2 M^4+3pi M^2) exp(-eta_sigma M^2)/(1-r_M).
The sharp inherited tail, using e^(4u)>=1+4u+8u^2, is

\[
 E_{K,0}\le e^{-\sigma x-b\sigma^2}S_M/\beta_M,
\quad E_{K,1}\le e^{-\sigma x-b\sigma^2}S_M
                  (\sigma/\beta_M+1/\beta_M^2).           \tag{4}
\]

The full-half-line omitted-mode bound also pays omitted modes on [0,V].
The two arm factors 1/2 are included. This sharp sigma=0 bound, rather
than Note13's deliberately loose exp(-pi M^2/4), is the equally informed
raw comparator. A shift does not improve every same-M allowance: its
exponent difference is -sigma x+(1-c_sigma)pi M^2, plus prefactors.

## 3. Complete analytic quadrature on the same target

For each box freeze sigma,K,V and choose a source-disk radius delta with
0<delta<=alpha-sigma. A closed endpoint is allowed here because the
retained finite Phi_K is entire; its damping still has modulus at most
one when a disk touches |Im(v+i sigma)|=alpha. Disks for the full
infinite source would require a strict inequality. Disks crossing this
boundary are outside the strip-safe comparison below.

Put S_h(K)=sum_(n=1)^K n^h and

\[
 P_K=2\pi^2 S_4(K)e^{9(V+\delta)}
                     +3\pi S_2(K)e^{5(V+\delta)}.
\]

On each disk |v-u_nu|<=delta about a real node in [0,V], either
physical derivative arm, including its e^(-sigma x), is bounded by

\[
 (V+\sigma+\delta)^jP_K
 \exp\{t[(V+\delta)^2-(\sigma-\delta)_+^2]
                         -(\sigma-\delta)x\}.             \tag{5}
\]

This uses real t>=0, |Im v|<=delta and the complete spectral exponential.
In particular the disk's e^(delta x) loss is paid.

Let mathcal M_j be any proved upper bound for (5)/P(t,x) over the
common box. It is source/carrier data, never a lower bound for H.
Choose 0<theta<1, J=ceil(V/(2theta delta)), h=V/J, and midpoint cells.
Integrate the paired source Taylor polynomial through degree 2q-1:

\[
 Q(t,x)=\frac12\sum_{\nu,\pm}\sum_{k=0}^{q-1}
 \frac{2(h/2)^{2k+1}}{(2k+1)!}
 \partial_u^{2k}\{w_{K,t}(u\pm i\sigma)
                         e^{\pm ix(u\pm i\sigma)}\}_{u=u_\nu}.
                                                               \tag{6}
\]

Cauchy on the disks gives, for both physical derivatives,

\[
 \frac{|E_{Q,j}|}{P}\le
       \frac{V\mathcal M_j}{1-\theta}\theta^{2q}.          \tag{7}
\]

Thus q>=max(1,ceil(log(4V mathcal M_j/((1-theta)epsilon_j)) /
(2log(1/theta)))) pays epsilon_j/4. Use one q satisfying both j targets,
so Q_x is the derivative of the same Q. All parameters remain fixed
during x and t differentiation. Each term still solves heat; source
variable differentiation commutes with partial_t+partial_x^2.

## 4. Carrier targets and finite-arithmetic payment

For A>=4pi an explicit positive comparison carrier is

\[
 W_t(x)=x^{7/4}e^{-\alpha x+(t/16)\log^2(x/(4\pi))}.        \tag{8}
\]

This is a declared normalization, not a lower field bound. The exact
published modulus Gamma_t=|M_t((1+ix)/2)| has this shape times a bounded
positive time factor and (1+O_B(1/x)); its checked formula is in
[source-measurement Note02, Section 3][carrier]. No uninstantiated
asymptotic constant is used for finite inequalities with W.

For (3)-(4), a completely explicit uniform bound is

\[
 \frac{e^{-\sigma x-b\sigma^2}}{W_t(x)}\le
 R_\sigma:=A^{-7/4}
 e^{(\alpha-\sigma)X-(b/16)\log^2(A/(4\pi))-b\sigma^2}.    \tag{9}
\]

Keep t coupled before the quadrature supremum. Define
D_A=(V+delta)^2-(sigma-delta)_+^2-log^2(A/(4pi))/16 and
T_*(D)=BD if D>=0, bD otherwise. Then an explicit (5) bound is

\[
 \mathcal M_j=A^{-7/4}(V+\sigma+\delta)^jP_K
        e^{(\alpha-\sigma+\delta)X+T_*(D_A)}.             \tag{10}
\]

For P=1 use (5) directly. Other positive carriers use their actual
box ratios; do not take unrelated suprema that introduce an avoidable
exp(sigma Delta) loss. For exact Gamma at low heights, its minimum in
time is min(Gamma_b,Gamma_B), unless the sign of its time exponent has
separately been established.

Require (3),(4),(7), after division by the common P, each <=epsilon_j/4.
The fourth quarter pays fixed-coefficient and finite-evaluation error.
A finite explicit coefficient allowance is available. Write
s_(nu,l)^pm=Phi_K^(l)(u_nu pm i sigma)/l! for l<=2q-2, and use Leibniz
in (6). If Z_j bounds the heat/exponential part of (5)/P without P_K,
Cauchy gives the total normalized coefficient error at most

\[
 \frac{hZ_j}{1-\theta^2}
 \sum_{\nu,\pm,l}|\Delta s_{\nu,l}^{\pm}|(h/2)^l.         \tag{11}
\]

For example, approximating every scaled source coefficient
s_(nu,l)^pm(h/2)^l to alpha_coeff gives a sufficient common bound
2V Z_j(2q-1)alpha_coeff/(1-theta^2). Reserve half the final quarter for
this and half for point evaluation. This is a finite acquisition contract,
not an executed interval implementation. Fixed source coefficients
preserve the heat equation. No event amplitude c or multiplicity is used.

Normalize the physical vector, (H,ell H_x)/P. If F=H/P and
g=(log P)_x, it equals (F,ell(F_x+gF)). Dropping g changes the consumer.
For ordinary F_x errors, retain (E_1+|g|E_0)/P, or the correlated shear.
A complex carrier additionally has a phase derivative, of order log x
for M_t, which cannot be replaced by the positive modulus derivative.

## 5. Fixed-cutoff calibrations: why order of operations matters

In this section assume 0<sigma<alpha for the shifted comparator.
Let R_(K,V) be the raw finite cosine integral and S_(K,V) its completed
two-arm shifted counterpart. Exact half-line contour deformation gives

\[
 R_{K,V}-S_{K,V}=D_{K,0}-D_{K,V},
\]
\[
 D_{K,0}=\frac i2\int_0^\sigma e^{-xy}
                       [w_{K,t}(iy)-w_{K,t}(-iy)]dy,
\]
\[
 D_{K,V}=\frac i2\int_0^\sigma e^{-xy}
 [e^{ixV}w_{K,t}(V+iy)-e^{-ixV}w_{K,t}(V-iy)]dy.          \tag{12}
\]

For the full source D_0=0 by reflection. For finite K, however,

\[
 \rho_K=\Phi_K'(0)>0,\quad
 \phi_n'(0)=(30\pi^2n^4-15\pi n^2-8\pi^3n^6)e^{-\pi n^2}.
\]

Every n>=2 term is negative; full Phi'(0)=0 proves rho_K>0.
At V=infinity, fixed K and sigma, uniformly on [b,B],

\[
 R_{K,\infty}=-\rho_K/x^2+O_{K,B}(x^{-4}),\qquad
 S_{K,\infty}=O_{K,B,\sigma}(e^{-\sigma x}).              \tag{13}
\]

Integration by parts gives an explicit remainder
(|w_(K,t)'''(0)|+integral_0^infinity |w_(K,t)''''|)/x^4.
All these finite-mode constants are finite uniformly on the time slab.
The full H also decays exponentially for each fixed shift. Hence its
raw fixed-K approximation error is genuinely algebraic, while (4) gives
an exponential error for truncation after completion. This is an actual
error distinction, not just a nominal prefactor improvement.

At a fixed V>0 the remote endpoint also survives. With the full source,

\[
 R_V=w_t(V)\sin(xV)/x+O(x^{-2}),\quad
 R_V'=Vw_t(V)\cos(xV)/x+O(x^{-2}).                         \tag{14}
\]

Thus ||(R_V,ell R_V')||>=w_t(V)min(1,ell V)/x-C/x^2.
One may take C=(C_0^2+ell^2 C_1^2)^(1/2), with
C_0=|w_t'(V)|+|w_t'(0)|+integral_0^V|w_t''| and
C_1=|w_t(V)+Vw_t'(V)|+integral_0^V|2w_t'+u w_t''|.
No phase removes the leading first-jet signal. Subtracting the true
exponentially small jet gives the same algebraic-error obstruction.
These are **fixed-cutoff** results; they do not refute growing cutoffs
or establish a necessary joint-growing complexity bound.

## 6. Premise screen and disposition

| Control or comparison | Actual premise and outcome |
| --- | --- |
| Raw finite theta modes | Fail full analytic reflection; seam (12) is nonzero. Literal finite-mode continuation also grows at negative real infinity for t>0. |
| Full theta with a fixed frequency wall | Reflection holds; the remote seam remains. The first-jet comparison (14) detects it. |
| Euler-factor sources | Evenness/strip decay may support their own completed contour; the literal unchanged theta coefficients fail. A valid approximation does not reject their collision. |
| Weighted-square / finite-tail, finite-prime controls | Full theta reflection fails. Their seam cannot be discarded. |
| Reflected, smooth-shape, positive-primitive controls | Retain only their documented holomorphy/decay properties; literal theta modes fail. Real-even shape alone supplies neither all these bounds nor exclusion. |
| Atomic / finite-profile threshold controls | Do not have this ordinary analytic theta density. Their real-zero energy comparisons are unrelated to the present source approximation. |
| RH-conditional endpoint controls | Are not unconditional positive-threshold examples; unchanged theta arithmetic still fails. |

CE-02/03 gain a matched whole-box first-jet source contract, not a field
margin. CE-04/06 remain open. [Note16][n16] tests the complete ledger,
including strip radius, positive time and precision dependence. Negative
heights may use canonical parity; the finite shifted model need not be
even, so do not symmetrize it and import an uncontrolled bad arm.

[n13]: 13_UNCONDITIONED_SOURCE_ACQUISITION_AT_COLLISION_SCALE_20261027.md
[n14]: 14_SECOND_RETURN_AND_NEXT_CANONICAL_CALCULATION_20261027.md
[n16]: 16_STRIP_RADIUS_AND_POSITIVE_SLAB_COMPARISON_20261027.md
[review]: ../reviews/07_RAW_SHIFTED_SOURCE_COMPARISON_REVIEW_20261027.md
[ar06]: ../../../investigations-3/11_arithmetic_collision_rigidity/notes/06_CANCELLATION_PRESERVING_APPROXIMATION_AND_NEWMAN_ROADMAP_CODEX_20261018.md
[carrier]: ../../../investigations-3/07_source_measurement_audit/notes/round-1/02_EXPLICIT_THETA_JET_AND_ENDPOINT_BOUNDS_CODEX_20261017.md
[poly]: https://arxiv.org/html/1904.12438v2
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
