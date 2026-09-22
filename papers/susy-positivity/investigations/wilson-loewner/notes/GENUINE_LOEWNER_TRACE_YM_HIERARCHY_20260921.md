# Genuine Loewner growth in fixed Yang--Mills theory: the first two quantum evolution equations

21 September 2026. Prepared for Edward Baker.

**Model:** OpenAI GPT-6 (Codex; developer-provided identity).
**Effort:** not exposed in this session; not inferred.
**Status:** internal analytical derivation with explicit smooth-field remainder
bounds and independent floating transport diagnostics. The expectation identities
require the stated regularity and moment assumptions. This is not a construction
of continuum four-dimensional Yang--Mills theory, a closed Makeenko--Migdal
solution, or an independently reviewed result.

## 1. Research decision and concrete result

The user clarified the physical question: fix the bulk theory, generate an
actual curve by a specified Loewner driver, define Wilson observables on that
curve, and derive the induced expectation-value evolution. An explicit value of
the expectation is unnecessary. The family of observables within a fixed theory
is the object of investigation. Arithmetic coupling estimates are a separate
workstream; possible manuscript separation is deferred at the user's request.
Manuscript v0.5 and every snapshot remain unchanged.

For the first calculation choose pure Euclidean SU(N) Yang--Mills, N >= 2, at
theta = 0. Close each genuine growing planar trace by its straight return chord.
This specifies the tip color contraction without introducing matter or changing
the action. At a fixed smooth-field resolution, write Q_t for the resulting
based holonomy and W(t) = <tr Q_t>/N. If q(t) is the tip relative to the start,
put

\[
 k(t)=q_1\dot q_2-q_2\dot q_1.
\]

The exact first equation is

\[
 \boxed{\dot W(t)=i k(t)M_1(t),\qquad
 M_1(t)=\left\langle\frac1N\operatorname{tr}(J_tQ_t)\right\rangle,\quad
 J_t=\int_0^1 r\widehat F_{12,t}(r)\,dr.}                 \tag{1}
\]

Here the hat transports curvature on the chord to the fixed basepoint. Its
equation, including noncommutative ordering, is

\[
 \boxed{\dot M_1(t)=\dot q^\mu M_{D,\mu}(t)+2ik(t)M_2(t).} \tag{2}
\]

Definitions and proofs are below. These equations retain the full interacting
expectation; no Wick rule, independent-field assumption, or large-N
factorization is used. They identify the specific derivative and two-curvature
correlators that must be controlled for closure.

For the actual Loewner driver u(t)=a t, the leading quantum response is also
determined without evaluating a path integral:

\[
 \boxed{W_\tau(t)=1-\frac{2a^2}{81}\,C_\tau\,t^3
                         +O_{\tau,a}(t^{7/2}),\qquad
 C_\tau=\left\langle\frac1N\operatorname{tr}F_{12}[B_\tau](0)^2\right\rangle.}
                                                               \tag{3}
\]

The geometric coefficient is explicit; C_tau is a local gauge-invariant moment
in the same interacting theory, not a fitted coefficient. Section 6 gives an
explicit remainder inequality and its moment assumptions. The subscript tau
denotes a fixed positive gauge-flow resolution, not Loewner time. No claim is
made that (3) survives removal of that resolution uniformly.

## 2. Fixed theory, observable and precise regularity scope

Use Hermitian matrices, tr(T^a T^b)=delta^{ab}/2, and

\[
 F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu-i[A_\mu,A_\nu],\quad
 D_\mu=\partial_\mu-i[A_\mu,\,\cdot\,],\quad
 S[A]=\frac1{2g^2}\int_{\mathbb R^4}\operatorname{tr}F_{\mu\nu}F_{\mu\nu}\,d^4x.
                                                               \tag{4}
\]

The gauge group, coupling, vacuum, and action do not vary with the Loewner
parameter. The planar domain is embedded as x3=x4=0 in fixed spacetime; the
growing slit is geometric data, not a moving physical boundary of the QFT.

For a definite smooth-field observable use the gauge-covariant Yang--Mills flow
at a fixed positive time tau:

\[
 \partial_\tau B_\mu=D^B_\nu F_{\nu\mu}[B],\qquad B_0=A.       \tag{5}
\]

All Wilson transports and curvatures below are evaluated in B_tau, while the
expectation remains over A with action (4). Thus the observable is a flowed
Wilson loop in an interacting theory, not a Gaussian replacement for that
theory. Flow is used only to define a smooth probe and control its small-size
expansion. It has no arithmetic positivity interpretation. Positive-flow local
observables and their perturbative renormalization are discussed by
[Luescher, 1006.4518](https://arxiv.org/abs/1006.4518) and
[Luescher--Weisz, 1101.0963](https://arxiv.org/abs/1101.0963).

The following distinction is essential. Sections 3--6 prove smooth-connection
identities and bounds. Their averaged versions hold in any regulated/flowed YM
construction in which these holonomies exist, derivatives can be passed through
the expectation, and the stated local moments are finite. We have not supplied
a nonperturbative continuum construction or proved those analytic assumptions
for the continuum measure. The source results on local flow observables do not
by themselves prove a theorem about every cusped nonlocal loop used here.
Without positive flow, the equations are bare regulated identities; passing to
renormalized unflowed loops requires the perimeter/cusp/contact terms. No such
terms are silently discarded.

The algebra suppresses tau and writes A,F,D for the selected smooth connection.
This suppression does not identify the flowed field with the integration variable
in a Schwinger--Dyson equation.

## 3. Actual trace and gauge-invariant chord completion

In the upper half-plane use half-plane capacity 2t:

\[
 \partial_t g_t(z)=\frac2{g_t(z)-u(t)},\qquad
 q(t)=\lim_{y\downarrow0}g_t^{-1}(u(t)+iy),\qquad q(0)=0.       \tag{6}
\]

Assume the driver generates a trace, C1 for positive t, with the needed local
integrability at zero. Our analytic example in Section 5 meets this local
condition. No Brownian trace or stochastic contour average is assumed. General
trace regularity is a separate mathematical issue; see
[Lind--Tran, Regularity of Loewner Curves](https://arxiv.org/abs/1411.2164).

Let U_t transport along the actual prefix q[0,t], and let

\[
 R_t(r)=U_A(0\longrightarrow r q(t)),\quad
 Q_t=R_t(1)^{-1}U_t,\quad
 \widehat F_t(r)=R_t(r)^{-1}F_{12}(r q(t))R_t(r).              \tag{7}
\]

Q_t traverses the trace outward and the chord back to the origin. The chord is
part of the independently specified observable. Replacing it changes the
observable and generally its evolution. A different endpoint-state construction
is possible but is not being claimed equivalent to this one. The curve is not
the inverse-map deformation of a separate reference contour used in earlier
notes. Along prefix growth, points already traced remain fixed.

All matrices in (7), except the open R and U, transform by conjugation in the
basepoint fiber. The traces below are gauge invariant. At zero size Q_0=I and
W(0)=1. For pure gauge transport reversing a path gives its inverse; a
scalar-arclength-coupled N=4 Wilson line would not have the same backtracking
identity without additional choices.

## 4. Cancellation of the tip and the first two equations

At the smooth field level, prefix growth gives

\[
 \dot U_t=i A_\mu(q)\dot q^\mu U_t.
\]

Apply the existing ordered-transport variation identity to the outward chord
x(r)=r q(t). Its displacement is r dot(q), and
F_{nu mu} dot(q)^nu q^mu = -k F12. Thus, with
J_t(r)=integral_0^r s Fhat_t(s) ds,

\[
 R_t(r)^{-1}\dot R_t(r)
 =i r R_t(r)^{-1}A_\mu(rq)\dot q^\mu R_t(r)-ik J_t(r).        \tag{8}
\]

At r=1 the first term cancels the entire tip connection when differentiating
R_t(1)^{-1}U_t. The remaining exact matrix equation is

\[
 \boxed{\dot Q_t=ik J_t(1)Q_t.}                              \tag{9}
\]

Taking the normalized trace and the fixed-measure expectation proves (1).
The cancellation is algebraic, before averaging; the insertion average itself
is over the complete interacting measure.

Differentiate the radial curvature using (8):

\[
 \partial_t\widehat F_t(r)
 =r\dot q^\mu\widehat{D_\mu F}_{t}(r)
       +ik[J_t(r),\widehat F_t(r)].                         \tag{10}
\]

Set

\[
 \mathcal D_{\mu,t}=\int_0^1r^2\widehat{D_\mu F}_{t}(r)dr,
 \quad
 \mathcal R_t=\int_0^1r[J_t(r),\widehat F_t(r)]dr,
\]
\[
 \mathcal P_t=\int_{0<s<r<1}rs\widehat F_t(s)\widehat F_t(r)\,ds\,dr.
                                                               \tag{11}
\]

Then dot(J)=dot(q)^mu Dcal_mu+ik Rcal. Splitting the square of the integral
into its two ordered triangles gives the exact identity

\[
 J_t(1)^2+\mathcal R_t=2\mathcal P_t.                        \tag{12}
\]

The order Fhat(s) Fhat(r), s<r, matters. Differentiating JQ and using (9)--(12)
proves (2), with

\[
 M_{D,\mu}=\left\langle N^{-1}\operatorname{tr}(\mathcal D_{\mu,t}Q_t)\right\rangle,
 \qquad
 M_2=\left\langle N^{-1}\operatorname{tr}(\mathcal P_tQ_t)\right\rangle. \tag{13}
\]

In particular,

\[
 \ddot W=i\dot k M_1+ik\dot q^\mu M_{D,\mu}-2k^2 M_2.       \tag{14}
\]

Equations (1)--(2) are a quantum hierarchy, not a scalar closed ODE. Writing
dot(W)/W as an unknown coefficient would not constitute closure. No claim is
made that two moments determine all later ones.

## 5. Explicit Loewner geometry: linear boundary driver

Choose u(t)=a t, a real constant. For w_s=g_s(z)-a s the forward map satisfies
dot(w)=2/w-a. Integrating it from w_0=z to w_t=0 identifies the tip on the
upper-half-plane branch:

\[
 a q+2\log(1-aq/2)=a^2t,\qquad
 \dot q=a-\frac2q.                                         \tag{15}
\]

The second equation is special to this driver. It is not the forward Loewner
map equation evaluated at the singular tip. For a general driver the tip
depends on the driver's history, and no such local formula is assumed.

For a=0 the limit is q=2i sqrt(t). For nonzero a, the analytic expansion in
s=sqrt(t) follows from q dq/ds=2a s q-4s:

\[
 q(t)=2i\sqrt t+\frac{2a}{3}t-\frac{ia^2}{18}t^{3/2}
                         +\frac{a^3}{135}t^2+O_a(t^{5/2}). \tag{16}
\]

An analytic implicit-function theorem applies after q=s v is substituted into
(15) and the double zero is divided out: the derivative in v at v=2i is nonzero.
This justifies the local expansion, rather than merely fitting powers to a
numerical trace.

The oriented area enclosed by the trace and chord is

\[
 \mathcal A(t)=\frac12\int_0^t k(v)dv
 =-\frac{2a}{9}t^{3/2}-\frac{11a^3}{1350}t^{5/2}+O_a(t^{7/2}),
\]
\[
 k(t)=-\frac{2a}{3}\sqrt t-\frac{11a^3}{270}t^{3/2}+O_a(t^{5/2}). \tag{17}
\]

For a>0 this orientation is clockwise, hence negative. A Cartan-valued
constant-curvature check gives Q=exp(i F12 A), fixing both the sign and the
factor of two in (9).

The constant driver is an exact control: its vertical trace and return chord
backtrack, so Q_t=I and W(t)=1 for every gauge configuration and every coupling.
This is a property of this chord-completed observable, not a claim that all
Wilson observables on a straight growing trace are constant.

## 6. Short-time quantum response and an explicit remainder

This subsection uses no Gaussian assumption and no evaluation of the YM
measure. On all chords swept before t, let K0 bound the operator norm of F12
and let K1 bound the norm of e^mu D_mu F12 for every unit planar vector e.
The bounds may depend on the field configuration. Define purely geometric
quantities

\[
 I(t)=\int_0^t|k(v)|dv,\qquad
 I_1(t)=\int_0^t|k(v)|\,|q(v)|dv.                            \tag{18}
\]

Radial covariant differentiation gives

\[
 \|\widehat F_v(r)-F(0)\|\le r|q(v)|K_1,
 \qquad \|J_v-F(0)/2\|\le |q(v)|K_1/3.                    \tag{19}
\]

Let M=integral_0^t k(v)J_v dv. Then
||M-A F(0)|| <= K1 I1/3 and ||M|| <= K0 I/2.
Every J is traceless. Cyclicity of trace turns the second Dyson coefficient
into -tr(M^2)/(2N). Since the evolution (9) is unitary, its third-order integral
remainder is bounded by (K0 I/2)^3/6; no exponential moment assumption is
required. It follows, configuration by configuration, that

\[
 \boxed{\left|\frac1N\operatorname{tr}Q_t-1
          +\frac{\mathcal A(t)^2}{2N}\operatorname{tr}F(0)^2\right|
 \le\frac{K_0K_1}{6}I I_1+\frac{K_0^3}{48}I^3.}             \tag{20}
\]

To see the first constant, use
|tr(M^2-A^2F0^2)|/N <= ||M-AF0|| (||M||+|A| K0) and |A|<=I/2.

Averaging (20) is justified if <K0 K1> and <K0^3> are finite on a fixed small
swept neighborhood. The same right-hand side with these expected moments is
then an explicit error bound for W. For u=a t,
I=O_a(t^(3/2)), I1=O_a(t^2), and (17) proves (3).
The coefficient C_tau is nonnegative for a positive Euclidean YM measure, but
its numerical value is not calculated here. There is no assertion that it is
coupling independent or protected.

The order of limits is fixed: t -> 0 at fixed positive tau (or a smooth UV
regulator), with sufficiently small contour size relative to the resolution.
Removing tau first encounters the usual short-distance/cusp structure and may
invalidate the moment bounds or alter the asymptotics. Thus (3) is an actual
conditional expectation expansion for the specified flowed observable, not a
continuum small-loop OPE theorem for an unsmeared cusped Wilson loop.

## 7. What Makeenko--Migdal supplies, and the specific missing components

### 7.1 A genuine interacting identity, without factorization

At a finite lattice regulator with Wilson action S_lat and product Haar measure,
left-invariant link differentiation obeys the exact integration-by-parts identity

\[
 \langle\nabla_e^a f\rangle=\langle f\,\nabla_e^aS_{\rm lat}\rangle. \tag{21}
\]

For example one can take S_lat=beta sum_p (1-Re tr U_p/N). Differentiating a
Wilson observable and applying the color completeness relation gives the usual
loop deformations and splitting/joining terms. This is an interacting-measure
identity, not a Wick contraction. At finite N the expectations of products must
be retained; replacing them by products of expectations is not automatic.
The continuum formal analogue is <delta O/delta A>=<O delta S/delta A>, with
the full regulator/measure conventions included.

Makeenko's [lecture 3, equations (3.1)--(3.4)](https://arxiv.org/pdf/0810.2183)
relates the covariant divergence of an area insertion to contact and loop-splitting
terms, displaying the factorized large-N version. The supersymmetric extension
there requires an enlarged loop-space operator. This supports looking for
closure; it does not turn a specified first Loewner derivative into a loop-space
Laplacian.

### 7.2 A planar contour does not remove four-dimensional fields

Consider the unflowed smooth expressions first, to display the field components
that the formal YM Schwinger--Dyson equation can address. Put
E_nu = sum_{mu=1}^4 D_mu F_{mu nu}. Then identically on the plane,

\[
 \dot q^1D_1F_{12}+\dot q^2D_2F_{12}
 =\dot q^1E_2-\dot q^2E_1
 -\dot q^1(D_3F_{32}+D_4F_{42})
 +\dot q^2(D_3F_{31}+D_4F_{41}).                             \tag{22}
\]

Thus using an equation for E to replace the derivative moment in (2) leaves an
explicit transverse-current insertion, in addition to contact and splitting
terms and M2. The residual is (22)'s last two terms, radially transported,
integrated with weight r^2, multiplied by Q, and averaged. The planar placement
of the contour does not set it to zero. Symmetry might constrain its average in
a particular sector, but that would require a proved identity.

A local algebraic control shows exactly why deletion is invalid. Let H=T3 in
SU(2), take A2=b(x1^2-x3^2)H/2, and A1=A3=A4=0. Then

\[
 F_{12}=b x_1H,\quad F_{32}=-b x_3H,\quad E_\nu=0,
 \quad D_1F_{12}=bH,\quad D_3F_{32}=-bH.                    \tag{23}
\]

For b=1, the omitted term has operator norm 1/2 although the total equation-of-
motion insertion is zero. This is a local counterexample to a proposed
component replacement, not a YM vacuum calculation or a no-go theorem for
averaged closure. The field is not offered as a finite-action vacuum state.

For the main flowed observable there is a further distinction: E[B_tau] is not
the functional derivative of S[A]. Applying (21) to it differentiates the flow
map B_tau[A], producing its response kernel. One cannot simply import the bare
unflowed contact equation at positive tau. The lattice version supplies a clean
way to formulate these derivatives; obtaining the continuum limit is additional
work. This specific closure task remains uncompleted.

### 7.3 Scope of the result

There is now a specified observable and two exact evolution equations for its
expectations, with an explicit geometric coefficient and a short-time quantum
moment. No closed finite system has been proved. In particular we have not
controlled M2, the transverse-current average, the flow response kernel, or the
unflowed cusp limit by W and M1 alone. This is a precise inventory of the
uncontrolled terms in the attempted reduction, not a universal obstruction.

For comparison, [Shen--Smith--Zhu, lattice Yang--Mills--Higgs](https://arxiv.org/abs/2512.00570)
derives an enlarged system including open lines as well as loops. It is useful
methodological precedent, but it is a different action and does not supply our
closure. It is not silently substituted for fixed pure YM.

## 8. Reproduction and independent checks

Run from this investigation directory:

```sh
python3 -B numerics/check_growing_trace_hierarchy.py --output /tmp/growing-trace-replay.json
```

Python 3 and NumPy are required; no SciPy, SymPy, network access or lattice
ensemble is needed. The saved small record is
`numerics/records/growing-trace-hierarchy-20260921.json`.

The checker derives 12 tip-series coefficients with exact rational arithmetic.
It independently integrates the original prefix Wilson equation for the
noncommuting test connection A1=T1,A2=T2, then closes by the chord. Four samples
include positive, negative and zero driver slopes. Finite differences of these
direct transports check (9), (10), (12) and (2). A spatial gauge transformation
checks the moving endpoint frame. A commuting constant-curvature control fixes
the area sign and the coefficient in (3). It also checks the local four-dimensional
example (23) and evaluates (20) on two deterministic test contours.

Largest recorded errors: loop derivative 1.314e-10; curvature-moment derivative
5.088e-11; first-moment derivative 1.378e-12; ordering identity 2.259e-16;
implicit Loewner trace relation 2.254e-14. Step refinement changes the test loop
by 4.523e-13; gauge transformation changes it by 1.361e-15.

These are floating diagnostics of geometry and matrix calculus. They do not
sample the YM measure, evaluate C_tau, certify continuum renormalization, or
constitute specialist review. The explicit inequality (20) is analytical; the
two numerical evaluations of its terms are diagnostics, not interval bounds.

## 9. What this changes for the program

This calculation takes the clarified direction literally: genuine Loewner trace,
one fixed interacting theory, and an independently chosen gauge-invariant
observable. It replaces the demand for an explicit path-integral value with
an insertion hierarchy whose first coefficients and small-time response are
derived. The driver affects the geometry; the quantum theory controls the
curvature correlators. Neither is identified with the other by assumption.

The next bounded question is whether the first derivative moment can be
reduced by the finite-regulator Schwinger--Dyson equations while retaining the
transverse and flow-response terms, and whether a useful observable sector is
preserved. It is not another Gaussian preparation or an arithmetic append.
The [handoff](RESEARCH_CONTINUATION_AFTER_GROWING_TRACE_20260921.md) records this
scope and the user's proposed future manuscript separation.
