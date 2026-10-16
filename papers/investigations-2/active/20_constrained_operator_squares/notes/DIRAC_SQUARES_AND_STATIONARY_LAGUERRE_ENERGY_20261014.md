# Dirac squares and stationary Laguerre energy

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6-astra` (Codex), reasoning effort **ultra**.

Relocated to investigation 20 at the author's request on 14 October 2026.
The original 06 path is retained as a forwarding reference.

Edward Baker's 2018 notes suggest a relevant method: construct a positive
quadratic form by introducing a first-order operator and completing a
constrained expression into a square. For the current theta program, the
quantity to factor is the physical Laguerre expression, with its stationary
constraint and full source data retained. A positive square for the heat
generator or source density alone does not supply this sign.

## Source and the operator distinction

The source is Edward B. Baker III, *Notes on the continuum sigma limit*,
17 August 2018, supplied as
[Dirac operator flow](</Users/ebbaker/Library/Mobile Documents/com~apple~CloudDocs/Tex/Greens_Function_Integral/Dirac_operator_flow/Dirac_operator_flow.pdf>).
The most relevant passages are page 3, equations (15)--(24), the spectral
splitting on pages 4--7, and page 12, equations (76)--(79).

With the stated Clifford convention, the Dirac operator satisfies
\(D^2=-\Delta\). On appropriate domains the inverse-Laplacian quadratic
form has the square representation
\[
 \langle f,(-\Delta)^{-1}f\rangle=\|D^{-1}f\|^2,
\]
whenever the inverses and norm exist. This is a useful model for deriving
positivity of a complete quadratic form.

Three different operations must remain distinct. The ordinary dissipative
heat operator is \(e^{-sD^2}\), and its positive operator square root is
\(e^{-sD^2/2}\). The notes' first-order evolution \(e^{sD}\) is a
different family, requiring the positive/negative spectral treatment
discussed there. The Newman equation is
\(\partial_tH=-\partial_x^2H\), with the growing sign \(e^{tD^2}\)
when \(D^2=-\partial_x^2\). For theta the source decay supplies the
necessary analytic vectors; this is not a bounded semigroup on arbitrary
\(L^2\) initial data for positive time.

The many-body square completion on page 12 needs rederivation before use.
Squaring a field linear in density produces a density-density expression;
comparison with the normal-ordered pair interaction must retain the
self-interaction contraction. Also, expanding equation (79),
\(F=G_{1/2}+\sqrt\nu\,a\), produces
\[
 F^\dagger F=G_{1/2}^\dagger G_{1/2}+\nu a^\dagger a
 +\sqrt\nu\,(G_{1/2}^\dagger a+a^\dagger G_{1/2})
\]
for real nonnegative \(\nu\). With the stated density-bilinear definition
of \(G_{1/2}\), the cross terms change particle number. They do not
produce the kinetic term displayed in equation (77), and their
expectations vanish in a fixed-particle-number state. Coefficients also
need matching. The useful import is the constrained-square method;
equations (76)--(79) are not a ready positivity certificate for the theta
problem.

## An exact derivative of a squared critical value

Let \(h(t,x)\) be a sufficiently regular real solution of
\(h_t=-h_{xx}\), and let \(x_s(t)\) be a differentiable stationary
curve, \(h_x(t,x_s(t))=0\). Put \(g(t)=h(t,x_s(t))\). Then
\[
 g'(t)=h_t+(\partial_x h)\,x_s'=-h_{xx}(t,x_s(t)),
\]
It follows exactly that
\[
 \boxed{\mathscr L_0(h;t,x_s(t))
 =g(t)g'(t)=\frac12\frac{d}{dt}g(t)^2.}
 \tag{1}
\]
Thus the first conditional Laguerre inequality is monotonicity of the
squared critical value in Newman time. This is more specific than
monotonicity of a spatially integrated norm.

The same identity supplies both derivative-level targets. Put
\(h_j=\partial_x^jH\), which obeys the same heat equation, and follow
any differentiable curve on which \(\partial_x^{j+1}H=0\). Then
\[
 \boxed{\mathscr L_j(H;t,x_s(t))
 =\frac12\frac{d}{dt}
 \bigl[\partial_x^jH(t,x_s(t))\bigr]^2,\qquad j=0,1.}
 \tag{2}
\]
The identity assumes the curve exists; an ordinary stationary point has
such a local curve by the implicit-function theorem. It is not by itself
a continuation theorem through degenerate stationary points.

At an ordinary double zero \((T_*,X_*)\), equation (1) agrees with the
[previous stationary identity](../../../brainstorm/reviews/LOCAL_COLLISION_THEOREM_PROGRAM_VALUE_CODEX_20261014.md).
The critical value tends to zero from a nonzero value before the collision,
and its square decreases. More precisely,
\[
 g(t)=\int_t^{T_*}h_{xx}(s,x_s(s))\,ds,
\qquad
 \mathscr L_0=-h_{xx}(t,x_s(t))
 \int_t^{T_*}h_{xx}(s,x_s(s))\,ds.
\]
A lower curvature bound \(|h_{xx}|\ge m>0\) with fixed sign yields
\(\mathscr L_0\le-m^2(T_*-t)\). A proposed positive square identity
must distinguish the theta source from controls displaying this behavior.

Equations (1)--(2) use the unnormalized heat solution. If one instead uses
\(C_t=H_t/H_t(0)\), its evolution contains the normalization term
\(-\mu_2(t)C_t\). At a stationary point,
\(\tfrac12\partial_t C_t^2=\mathscr L_0(C_t)-\mu_2 C_t^2\).
Dropping that term changes the proposed monotonicity.

## Why an integrated square does not give the local sign

For decaying real \(h\) with the required Sobolev regularity,
\[
 \frac{d}{dt}\|h\|_2^2=2\|\partial_xh\|_2^2\ge0.
 \tag{3}
\]
This follows from the square of the spatial Dirac operator, but it holds
for collision controls as well. The exact local identities are
\[
 (\partial_t+\partial_x^2)h^2=2h_x^2,
\qquad
 \boxed{\mathscr L_0(h)=2h_x^2-\frac12\partial_x^2(h^2).}
 \tag{4}
\]
Integration removes the total derivative and leaves a nonnegative square.
At a stationary point the displayed square vanishes, leaving the spatial
curvature term. Its sign is the information that integration discarded.

An elementary exact example is
\[
 h(t,x)=1+ce^t\cos x,\qquad 0<c<1.
\]
It solves the backward heat equation and has a positive even spectral
measure. At \(x=\pi\), writing \(C=ce^t\),
\[
 h_x=0,\quad h=1-C,\quad h_{xx}=C,\quad
 \mathscr L_0=-C(1-C)<0\quad(0\le t<\log(1/c)).
 \tag{5}
\]
At \((\log(1/c),\pi)\) it has an ordinary double zero. A finite-dimensional
square-generator representation is explicit:
\[
 D=\operatorname{diag}(0,1,-1),\quad
 v=(1,\sqrt{c/2},\sqrt{c/2}),\quad
 h(t,x)=\langle v,e^{tD^2}e^{ixD}v\rangle.
\]
The positive operator \(e^{tD^2}\) coexists with a signed oscillatory
matrix element. This example screens the proposed generic operator
inference; it is not claimed to satisfy all the arithmetic or decay
hypotheses of the genuine theta source. Investigation 19 provides the
stronger smooth arithmetic controls.

## A paired operator identity retaining the sign problem

There is an exact operator version of the full first Laguerre form.
Let \(d\mu(u)=\tfrac12\Phi_e(u)\,du\), define \(D\) as multiplication
by \(u\) on \(\mathcal H=L^2(\mathbb R,d\mu)\), and put
\[
 w_t(u)=e^{tu^2/2},\qquad W_t=w_t\otimes w_t,\qquad
 A=D\otimes I-I\otimes D,\qquad S=D\otimes I+I\otimes D.
\]
The theta tails imply that these vectors lie in every polynomial domain
used below on compact real time intervals. The normalization is exact:
\[
 H_t(x)=\langle w_t,e^{ixD}w_t\rangle
       =\int e^{tu^2}e^{ixu}\,d\mu(u).
\]
Differentiating this integral and symmetrizing the two spectral variables
gives
\[
 \mathscr L_0(H_t;x)
 =\frac12\iint (u-v)^2 e^{t(u^2+v^2)}
       \cos(x(u+v))\,d\mu(u)d\mu(v),
\]
hence
\[
 \boxed{\mathscr L_0(H_t;x)
 =\frac12\langle AW_t,\cos(xS)AW_t\rangle.}
 \tag{6}
\]
There already is a squared first-order factor, \(A^2\). Its quadratic
form still carries the indefinite multiplier \(\cos(xS)\).
Writing \(C_\pm=(|\cos(xS)|\pm\cos(xS))/2\) by spectral calculus,
\[
 \mathscr L_0
 =\frac12\|C_+^{1/2}AW_t\|^2
 -\frac12\|C_-^{1/2}AW_t\|^2.
 \tag{7}
\]
The open task is a theta-specific domination of the negative term under
\(H_x=0\), or a different source-derived factorization that absorbs it.
Deleting it would delete the cancellation the program needs to estimate.
For the second target the same symmetrization gives
\[
 \mathscr L_1
 =\frac12\langle AW_t,
       (-D\otimes D)\cos(xS)AW_t\rangle,
\]
with the additional signed spectral factor retained.

## Connection to the existing program and a bounded next target

The earlier
[SUSY Dirac scout](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/03_susy_dirac_hodge/notes/1_MOVING_THETA_GROUND_STATE_WARD_RESIDUAL_AND_GAP_LIMIT_20261010.md)
already constructs a positive Dirac square for the normalized theta
density. Its instantaneous ground state \(g_t\) obeys \(B_tg_t=0\),
but Newman evolution has \(B_t\dot g_t=ug_t\). Thus its annihilating
Hamiltonian is not the physical time generator. The same construction
works for smooth collision controls. That finding excludes a generic
shortcut, not all source-specific Dirac constructions.

The [complete paired-kernel program](../../06_paired_kernel_factorization/notes/INITIAL_RESEARCH_PROGRAM_20261013.md)
is a downstream consumer of this operator investigation. A source-derived
factorization \(T_{J_j}=Q_j^\dagger Q_j\) of the complete convolution
operator would give \(\widehat J_j\ge0\), hence the physical sign.
A weaker identity restricted to the stationary locus would be sufficient
for the corresponding conditional target. The
[current gate](../../06_paired_kernel_factorization/README.md) requires all cross-sector cancellations,
endpoints, tails, and both derivative-level targets to remain visible.

A concrete adaptation of the notes' constrained square completion is the
already proposed shape
\[
 \mathscr L_j
 =\|\mathcal A_j\Psi_t\|^2
  +H_t^{(j+1)}M_j
  +\mathcal D_{\rm gluing,j}+E_j,\qquad j=0,1.
 \tag{8}
\]
Here the operators and state must be explicitly constructed from the
complete theta source; \(\mathcal D_{\rm gluing,j}\) is a displayed
full-gluing defect, and \(E_j\) contains all remaining boundary and tail
payments. For genuine theta the defect should vanish, and stationarity
removes the displayed multiplier. The square must dominate any negative
remainder. For a collision control, a violated hypothesis or nonzero
defect must account for (5) or its certified smooth analogue.

The first bounded task is to derive one such identity on a declared
compact cell and test its complete remainder against a stationary
control. A factorization obtained by assuming the target is positive,
using its unknown square root, or dividing by a physical function at
its unknown zeros would be circular. Global height/time coverage and
all-multiplicity continuation remain further obligations after a local
success. Equations (1)--(7) are exact reductions; equation (8) is a
research target, not a constructed positive certificate.

## Continuation results on 14 October 2026

Prepared for Edward Baker with substantial LLM assistance by `gpt-6.1-sol`
(Codex), reasoning effort **ultra**. The
[local multiplier obstruction](LOCAL_MULTIPLIER_AND_FINITE_OBSERVATION_OBSTRUCTIONS_20261014.md)
now excludes bounded linear stationary-multiplier square completions as
operator identities on the full paired core for both j=0 and j=1. This
includes theta-dependent coefficients but leaves a nonlocal identity on a
restricted arithmetic state open. The same note constructs positive
controls preserving any declared finite linear source observations and
local source jets while both stationary signs fail.

The [stationary certificate](2_CERTIFIED_STATIONARY_THETA_AND_EULER_CONTROLS_20261014.md)
proves local positive theta stationary energy margins for both derivative
levels and a strictly negative Euler-control margin on an actual
stationary curve throughout 0.199999 <= t <= 0.200001. Any constrained
identity applicable to that control must retain a quantitatively
sufficient negative defect/remainder. These results refine the domain and
control gates of (8); they do not supply its missing full-gluing square.
