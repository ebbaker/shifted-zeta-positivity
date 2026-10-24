# A growing-height stationary clock and its Vandermonde error

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.

**Status: estimates and eventual asymptotics proved in-note; finite
numerical evaluations are floating; same-assistant review only.** This
extends the finite-box [Note 09][coarse] to an explicitly growing height
range. The author's stationary-state and Vandermonde suggestions lead to
a clock after unfolding, a closed physical density approximation, and a
relative asymptotic for the Vandermonde of a growing block. These are
late-time approximation results, not RH, endpoint simplicity, a global
height-uniform limit, or a solution of the averaged boundary problem.

Read the [result index][results], [avoid index][avoid], especially
[classification][a01] and [scope][a07], and [controls][controls]. The
[companion note][negative] supplies the negative-time theorem and explains
why global uniform clock convergence fails at fixed epsilon. We retain
the unnormalized density and its physical amplitude; rescaling is used
only to describe stationarity.

## 1. What the earlier Vandermonde work supplies

The sibling [HDC Note 06][hdc06] defines
Delta=product_(i<j)(x_j-x_i)^2 and the inverse-square Laplacian
L_pair=(1/2) Hessian(-log Delta). [HDC Note 09][hdc09] retains the
complete exterior force, a moving unfolding, and the motion defect of
a clock reference. [LHCT Note 07, Section 4][lhct07] gives a deterministic
Hermite equilibrium for full finite heat polynomials; selected theta
blocks have an additional force and do not inherit that equilibrium.

We use the complete-source concentration from [BW10 Note 20][saddle],
rechecked at its DS7--DS12 proof, rather than deleting that force. The
source theorem gives the late-time clock; the Vandermonde and Hessian
then quantify its stationary shape. The scalar determinant alone cannot
locate a density, since it is translation invariant and does not determine
all gaps. No unproved converse from determinant closeness is used.

## 2. Explicit complete-source concentration inputs

Write, on u>=0,

\[
e^{tu^2}\Phi(u)=2\pi^2e^{q_t(u)}b(u),\quad
q_t(u)=tu^2+9u-\pi e^{4u},
\]
\[
b(u)=\sum_{n\ge1}\left(n^4-\frac{3n^2e^{-4u}}{2\pi}\right)
e^{-\pi(n^2-1)e^{4u}},\qquad 0<b\le C_b=(1-16e^{-3\pi})^{-1}.
\]

Let L be the large saddle and kappa its curvature:

\[
4\pi e^{4L}=2tL+9,\qquad \kappa=8tL-2t+36.
\tag{1}
\]

Equivalently, for sufficiently large t,

\[
L=-\tfrac14 W_{-1}\!\left(-\frac{8\pi}{t}e^{-18/t}\right)
-\frac9{2t},\qquad
L=\tfrac14\{\log t+\log\log t-\log(8\pi)\}
+O\!\left(\frac{\log\log t}{\log t}\right).
\tag{2}
\]

Put d=1/4, c=1/(4e), h_0=kappa^(1/12), and require the inherited
finite gates L>=d, kappa>=32, t/kappa<=1/(4e), and q_t(L-d)>=q_t(0).
They hold for all sufficiently large t. Define

\[
Q_L=16e^{-3\pi e^{4(L-d)}},\quad
d_L=\frac3{2\pi}e^{-4(L-d)}+\frac{Q_L}{1-Q_L},\quad
e_c=e^{(4e/3)\kappa^{-1/4}}(1+d_L)-1.
\]

The following weighted extension of DS8 will be useful. For p=0,1,2,3
and fixed Y>=0, set lambda=Y/sqrt(kappa) and

\[
G_p(Y)=\int_{\mathbb R}|w|^pe^{-w^2/2+\lambda|w|}\,dw,
\]
\[
\begin{split}
D_p(Y)={}&e_cG_p(Y)
+\int_{|w|>h_0}|w|^pe^{\lambda|w|}
       (C_b e^{-cw^2}+e^{-w^2/2})\,dw\\
&+C_b(L\sqrt\kappa)^{p+1}e^{YL-c\kappa d^2}.
\end{split}\tag{3}
\]

All terms are elementary Gaussian tails (or error functions and
recurrences), with no truncated theta input. Let
Z_-=sqrt(2pi)-D_0(0)>0, and define

\[
A_p(Y)=\kappa^{-p/2}\frac{G_p(Y)+D_p(Y)}{Z_-},\quad
e_\mu=\kappa^{-1/2}\frac{D_1(0)}{Z_-},\quad
\widehat B_3(Y)=4e^{Ye_\mu}\{A_3(Y)+e_\mu^3 A_0(Y)\}.
\tag{4}
\]

For M=H(t,0), dP_t=M^(-1)e^(tu^2)Phi(u)du, mu=E_t u,
v=Var_t u, and B_3(Y)=E_t[|u-mu|^3 e^(Y|u-mu|)], these give

\[
|\mu-L|\le e_\mu,\quad v\le A_2(0),\quad
B_3(Y)\le\widehat B_3(Y),\quad
M\ge\frac{2\pi^2e^{q_t(L)}}{\sqrt\kappa}Z_-.
\tag{5}
\]

**Proof of the extension.** The rescaled unnormalized source
B_t(w)=exp(q_t(L+w/sqrt(kappa))-q_t(L)) b(L+w/sqrt(kappa)),
zero for w<-L sqrt(kappa), differs from exp(-w^2/2) by at most
e_c exp(-w^2/2) on |w|<=h_0. On the near-left and right regions it is
bounded by C_b exp(-cw^2); on the far-left interval it is bounded by
C_b exp(-c kappa d^2). These are exactly the rechecked DS8 estimates.
Multiply each by |w|^p exp(lambda |w|); the far-left weight is at most
(L sqrt(kappa))^p exp(YL), with interval length at most L sqrt(kappa).
This proves the weighted L1 error bound (3), including the Gaussian
tail below the half-line. Gaussian odd mean zero gives the sharper
e_mu in (4), rather than the absolute first moment A_1(0).
Finally |u-mu|<=|u-L|+e_mu and (a+b)^3<=4(a^3+b^3) prove (5).

For fixed Y the resulting asymptotic orders are

\[
D_p(Y)=O(\kappa^{-1/4}),\quad e_\mu=O(\kappa^{-3/4}),\quad
v=O(\kappa^{-1}),\quad B_3(Y)=O(\kappa^{-3/2}),
\quad \kappa\sim8tL.
\tag{6}
\]

The stronger signed-mean bound is needed below when replacing mu by
the explicit L in a determinant with a growing number of factors.

## 3. A sharper carrier comparison: cancel transverse growth

Let X=N pi/mu, Y>0, Z=sqrt(X^2+Y^2), and
A(z)=1-vz^2/2. Either actual complete moments or the upper bounds
from (4)--(5) may be used to choose

\[
a_*=1-\tfrac12 vZ^2>0,\qquad
\delta=\frac{Z^3B_3(Y)}{6a_*},\qquad
s=4\delta\le\tfrac12,\quad r=s/\mu<\min\{Y,\pi/(2\mu)\}.
\tag{7}
\]

When upper bounds are used, replace v and B_3 by those upper bounds
in the definitions; the resulting a_* is a lower bound. Assume delta>0.
For f=H/M, the centered-source Taylor formula gives the **pointwise**
bound

\[
\left|f(z)/A(z)-\cos(\mu z)\right|
\le\delta e^{\mu|\operatorname{Im}z|}.
\tag{8}
\]

Outside disks of radius r about the carrier zeros c_j=(j+1/2)pi/mu,

\[
|\cos(\mu z)|\ge e^{\mu|\operatorname{Im}z|-s}\sin s.
\tag{9}
\]

To check (9), write a=mu times the nearest horizontal distance to a
carrier zero, 0<=a<=pi/2, and b=mu |Im z|. If b>=s, use
e^(-b)sinh b>=(1-e^(-2s))/2>=e^(-s)sin s. If b<=s and
a^2+b^2>=s^2, then sin^2 a+sinh^2 b>=sin^2 s, by the decrease
of sin a/a on [0,pi/2] and sinh b>=b. Multiply by e^(-b)>=e^(-s).

For 0<=s<=1/2, e^(-s)sin s>=s/2=2delta. Thus the comparison
has a strict boundary margin. Rouche and conjugation, as in Note 09,
give exactly one real simple zero a_j in each disk and no others in
the rectangle. The outside lower bound is

\[
|f|\ge b_*e^{\mu|\operatorname{Im}z|}\ge b_*,\quad
b_*=a_*(e^{-s}\sin s-\delta)\ge a_*\delta,
\quad |a_j-c_j|\le r.
\tag{10}
\]

Inside each carrier disk, |f(z)|>=c_*|z-a_j| with c_*=b_*/(2r),
by the same zero-free quotient argument as Note 09. The improvement
over that note is specific: exp(mu Y) no longer inflates delta. Its
growth cancels against the carrier at the same transverse coordinate.
No additional zeros or exterior force have been discarded.

## 4. A local count improves the density error

Use k(q)=(315/256)(1-q^2)^4 on [-1,1], zero outside, and
K=k_ell times k_h. For a center (x,y), require
|x|+ell+r<X and |y|+h<=Y. Only carrier centers within ell+r of x
can contribute to the difference of the actual and reference averages.
Their number is at most

\[
n_\ell=2\mu(\ell+r)/\pi+2.
\]

This replaces the total 2N population in Note 09's estimate. Put
eta=epsilon/M and

\[
E_{\rm ph}=\frac{(\pi/\mu)^3}{720}\|k_\ell^{(4)}\|_1,
\quad I_1(a,R)=\pi a^2[1+\log(1+R^2/a^2)].
\]

Then the physical approximate density and its explicit error are

\[
\boxed{R_+(t,x,y)=\frac{L(t)}\pi k_h(y),}
\tag{11}
\]
\[
\boxed{|K*\rho_\epsilon-R_+|
\le k_h(y)\left[\frac{e_\mu}\pi+
n_\ell r\|k_\ell'\|_\infty+E_{\rm ph}\right]+E_{\rm reg},}
\tag{12}
\]
\[
E_{\rm reg}=\frac{\|\Delta K\|_\infty}{4\pi}
\left[\frac{4\ell h\,\eta^2}{b_*^2}
+n_\ell I_1(\eta/c_*,2r)\right].
\tag{13}
\]

For the explicit kernel, C=315/256,
||k_ell'||_infinity=8C(6/7)^3/(sqrt(7)ell^2),
||k_ell^(4)||_1=ell^(-4)||k^(4)||_1, and
||Delta K||_infinity<=8C^2(ell^(-3)h^(-1)+ell^(-1)h^(-3)).
The fourth derivative inside the support is
C(144-1440q^2+1680q^4); its L1 norm follows by splitting at
q^2=(15 +/- 2 sqrt(30))/35.

**Why the bound is local.** Match roots to their disks and apply the
Lipschitz bound to each kernel value. The difference is zero unless
one of the two arguments lies in the kernel support, implying
|c_j-x|<=ell+r. Four integrations by parts in lattice periodization
give E_ph. For the regulator bridge integrate log(1+eta^2/|f|^2)
only over the kernel support: its area is 4ell h, and at most n_ell
carrier disks intersect it. Apply (10) outside disks and the quotient
bound inside. The distributional identity Delta log|H|^2=4pi nu and
integration by parts give (13), including multiplicities. This is not
a pointwise comparison of very narrow regularized peaks.

Widths ell=ell(t,x) are permitted in these static bounds; for each
observation their values are frozen when integrating against the source
coordinates. To differentiate the resulting variable-filter average,
its explicit x and t dependence must be retained. A positive time
average is handled by averaging the right sides and R_+ at the constituent
times, not by evaluating L at the mean time.

## 5. A growing window with a stationary limit

Fix epsilon>0, Y>h>0, and ell>=ell_0>0. Set

\[
N=\left\lfloor\frac{\mu\kappa^{1/3}}\pi\right\rfloor,
\qquad X=N\pi/\mu\sim\kappa^{1/3}.
\tag{14}
\]

All gates in (7) hold eventually: vZ^2=O(kappa^(-1/3)),
delta=O(kappa^(-1/2)), and r=O(kappa^(-1/2)/L).
Using the explicit upper moment allowances gives the same orders and
an available lower bound for M. Equation (13) is smaller than every
fixed inverse power of kappa, since
q_t(L)=tL^2-tL/2+9L-9/4. Thus (12) implies

\[
\boxed{K*\rho_\epsilon(t,x,y)=\frac{L(t)}\pi k_h(y)
+O_{Y,h,\ell_0,\epsilon}(\kappa^{-1/2}+L^{-3}),}
\tag{15}
\]

uniformly for |x|+ell(t,x)+r<X and |y|+h<=Y. The constant is uniform
over ell>=ell_0 satisfying the support condition. Indeed
n_ell r/ell^2=O(delta/ell+delta/(L ell^2)); the phase error decreases
with ell, as does the regulator bound. No growing population factor
remains in this local density error.

In particular, the normalized shape pi R/L tends to k_h(y) with error
O(kappa^(-1/2)/L+L^(-4)) on that growing domain. The physical density
itself grows like (log t)/(4pi) k_h(y). The more elementary expression

\[
\frac{\log t+\log\log t-\log(8\pi)}{4\pi}\,k_h(y)
\tag{16}
\]

also has vanishing absolute error there, with the additional
O(log log t/log t) saddle expansion error. Every fixed height is
eventually included. Uniformity over **all** real x at each finite t
is false for this fixed-regulator averaging class, as Note 11 proves.
The all-height analytic fallback there has a separate absolute budget.

## 6. Vandermonde and Hessian convergence for a growing block

Choose any consecutive m of the 2N enclosed zeros. In source-mean
coordinates y_i=mu a_i/pi, write y_i=c+i+e_i with |e_i|<=e=s/pi.
Here e=O(kappa^(-1/2))<1/2. The equally spaced discriminant is

\[
\Delta_m^{\rm clock}(L)=
\left(\frac\pi L\right)^{m(m-1)}
\prod_{k=1}^{m-1}(k!)^2.
\tag{17}
\]

For H_(m-1)=sum_(d=1)^(m-1) 1/d, the actual determinant satisfies

\[
\boxed{\left|\log\frac{\Delta_m(t)}{
\Delta_m^{\rm clock}(L(t))}\right|\le
\mathcal V_m:=(m(m-1))\frac{e_\mu}{L-e_\mu}
+\frac{4e}{1-2e}\{mH_{m-1}-(m-1)\}.}
\tag{18}
\]

For m=1 the bound and logarithmic ratio are zero. For m>=2, each pair
of index distance d has relative perturbation at most 2e/d. Use
|log(1+v)|<=|v|/(1-|v|), sum m-d pairs, and retain the factor 2
from the squared discriminant. This proves the second term. Changing
the reference scale from mu to L costs the first term, since
|log(L/mu)|<=e_mu/(L-e_mu). Also
product_(d=1)^(m-1) d^(2(m-d))=product_(k=1)^(m-1)(k!)^2.

For every m<=2N=O(L kappa^(1/3)), the full allowance tends to zero:

\[
\mathcal V_m=O\left(L\kappa^{-1/12}
+L\log\kappa\,\kappa^{-1/6}\right)=o(1).
\tag{19}
\]

Thus Delta_m/Delta_m^clock(L)->1 **uniformly for these growing
consecutive blocks**. This uses the signed mean error in (6); replacing
it with the coarser absolute first moment would not prove (19).

The matrix statement is dimension-uniform as well. Let L_clock be
the inverse-square Laplacian of m consecutive integers, and let
L_pair(a) be the matrix of the physical zeros. Pairwise distance
comparison gives the positive-semidefinite inequalities

\[
\boxed{\left(\frac\mu L\right)^2(1+2e)^{-2}L_{\rm clock}
\preceq\left(\frac\pi L\right)^2 L_{\rm pair}(a)
\preceq\left(\frac\mu L\right)^2(1-2e)^{-2}L_{\rm clock}.}
\tag{20}
\]

They include the constant zero mode and compare every nonzero
eigenvalue by the min--max principle. The error factors tend to one.
This is a deterministic unfolded clock, not a stochastic ensemble or a
claim of sine-kernel pair statistics. When m changes with time, (18)
is a slice statement; differentiating it as a fixed-population identity
would require accounting for membership changes.

## 7. The exterior force and the control screen

For a selected block, H=U product_i(z-a_i) gives the exact dynamics
a_i'=2 sum_(j!=i)(a_i-a_j)^(-1)+2(U_z/U)(a_i).
With y_i=alpha a_i, alpha=mu/pi, even a fixed clock reference has a
normalization term (alpha'/alpha)y_i. HDC Note 09's motion defect
retains that term and the complete exterior unit. Our slice estimates
do not prove a vanishing velocity residual or justify backwards
transport from infinity. They do not establish a Lyapunov functional
for the complete theta density.

- For the stationary sine heat field, exterior zeros exactly cancel
  internal repulsion; its clock is stationary without a Gaussian/Hermite
  force law. Its atomic source fails the canonical concentration inputs.
- Full finite Hermite heat polynomials have a stationary Hermite pattern
  after sqrt(t) scaling and can retain a multiple endpoint. They fail
  the unchanged theta source and its logarithmic clock scale. No endpoint
  simplicity conclusion can follow merely from having a stationary limit.
- The positive three-atom double-event control in round two fails the
  carrier gate at its collision (a_*<0). The present generic Rouche lemma
  can hold on a collision-free box of a control; it is not required to
  reject every such box.
- Euler-factor, weighted-square, reflected and primitive-compatible
  controls have the failed source premises recorded in Note 11 and the
  linked control register. Smooth nearby positive sources may inherit
  the same leading late-time behavior while colliding at earlier times.
  The determinant and Hessian comparison themselves apply to any
  ordered configuration satisfying their displacement bounds.

The advance is an explicit enlarging-domain error, including all theta
indices through (3), and the resulting growing-block determinant and
Hessian asymptotics. The computations evaluate formulas and controls;
they do not supply outward-rounded source enclosures or an independently
reviewed theorem. See the [record][data] and [self-review][review].

[negative]: 11_TWO_TIME_LIMITS_ALL_HEIGHT_ERROR_20261024.md
[coarse]: 09_COMPLETE_SOURCE_MOMENT_TRANSFER_AND_WEAK_CURRENT_20261024.md
[saddle]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[hdc06]: ../../../investigations-4/12_height_dependent_heat_contours/notes/06_PAIR_MATRIX_SPECTRUM_AND_ENDPOINT_MULTIPLICITY_20261023.md
[hdc09]: ../../../investigations-4/12_height_dependent_heat_contours/notes/09_BACKWARD_FILTER_TRANSPORT_AND_TERMINAL_PRECISION_20261023.md
[lhct07]: ../../../investigations-4/11_late_heat_caps_and_charge_transport/notes/07_PCC_WEIGHTED_MOMENTS_AND_CAP_PHASE_SCREEN_20261022.md
[data]: ../numerics/TWO_TIME_LIMITS_ROUND3_20261024.json
[review]: ../reviews/03_TWO_TIME_LIMITS_AND_VANDERMONDE_SELF_REVIEW_20261024.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
