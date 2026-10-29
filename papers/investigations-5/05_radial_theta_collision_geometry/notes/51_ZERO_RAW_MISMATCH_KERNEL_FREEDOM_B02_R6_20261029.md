# Zero raw mismatch leaves observation-kernel freedom

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**, Investigation05 **chat0024**, **Continue radial theta research**.

**Task:** one bounded **[B] CTF-B02 R6** information-sufficiency test,
recorded before testing in [Progress05][progress], following [Note50][n50].
The selected input is the raw source relation unused by R5. The tested
consequence is a strictly positive first-jet coercivity allowance from
that relation and the explicitly reduced premises below. It is not a new
RH criterion, an assumed first-jet floor, or a modification of the theta
target.

**Result — proved in-note, same-assistant checks only:** fixing the complete
theta amplitude and its logarithmic source operator, but allowing an even
entire observation kernel, zero raw mismatch does not force a nonzero
observed first jet. An exact polynomial comparison at (T,A)=(1/4,2) has
m=0 and E0>0; hence the infimum of |m|²/E0 in this class is exactly zero.
The same construction can retain any prescribed finite cosine Taylor
prefix. Unit heat preparation produces a genuine nonzero residual, and
the original conservative feedback has the inherited finite auxiliary
deadline on these comparison data.

**Scope is essential:** the comparison kernel is not cosine. It fails the
raw cosine oscillator identity and the physical Newman equation. It is
not an alternative theta source with a physical Newman collision and
does not refute an estimate that uses the full cosine identity. The
canonical theta problem and its manuscript are unchanged. This closes
the selected reduced-premise test; parent B02 and the actual trajectory
deadline problem remain open.

## 1. Premises and the precise claim tested

Use the full theta amplitude from [Note31, Section1][n31]:
\[
q_T(u)=e^{Tu^2}\Phi(u),\qquad
u=\tfrac12\log r,\qquad
\rho_T(r)=\frac{q_T(u)}{8\pi r^3}\quad(r\ge1).
\tag{1}
\]
All square coefficients in Phi remain one; its positive complete tail
and its canonical reflected extension defining the operator are unchanged.
The observation in the *actual* problem is cos(au).

For the comparison class only, let K be a real even polynomial, K(0)=1,
independent of the running variables T,a. This subclass of the permitted
even entire kernels already suffices. Set
\[
F_j^K(T,a;X)
 =\mathbf1_{r\ge1}\rho_T(r)u^j K^{(j)}(au),
 \qquad j=0,1,2.
\tag{2}
\]
These are actual running-a derivatives, not freely specified jet fields.
The prepared pair and second jet at a fixed mark p=(T,A) are
\[
W_0^K=K_1*(F_0^K,F_1^K),\qquad
J_{2,0}^K=K_1*F_2^K.
\tag{3}
\]
Here K_1 is the unit Gaussian heat kernel, not the observation kernel K.

Keep the exact source operator
\[
\mathcal A_T=b\cdot\nabla+c_T,\quad
b=\eta(r)\log r\,X,\quad
c_T=-\eta(r)r\log r\,(\log\rho_T)'(r),
\tag{4}
\]
with the fixed exponential cutoff eta=h(4r-2), zero on r<=1/2 and one on
r>=3/4. The extension, coefficients, full commutators, feedback drift,
and mandatory preparation are those of Notes31/40/47. No tail is truncated.

The tested premise class consists of (1)–(4), the two zero-raw-mismatch
identities below, and the smooth prepared class for the original feedback.
The comparison is allowed to vary K; **the exact identity K=cos is not
among these reduced premises**. The physical rectangle remains
\[
P=[0,1/2]\times[1,6].
\]
For the quantitative test, freeze the interior mark
\[
p_c=(T_c,A_c)=(1/4,2).
\tag{5}
\]
It would suffice to force |m|²>=c E0 with any c>0 on this class, where
m=int W0 and E0=||W0||². The construction below instead attains ratio zero
at this one fixed mark. Neither a uniform positive c on P nor a positive
c at p_c valid for all this class can follow from the reduced premises.

This is a scoped test of the information carried by a source relation,
as required by [avoid/01][a01] and [avoid/07][a07]. No actual theta first-jet
lower bound is assumed or numerically tested.

## 2. The source relation does not select cosine

On r>1, multiplication by rho cancels its logarithmic derivative:
\[
\mathcal A_T(\rho_T g(u,a))=\rho_T u\partial_u g(u,a).
\tag{6}
\]
For g(u,a)=K(au), the chain rule gives
\[
\boxed{\mathcal A_TF_0^K=aF_1^K,\qquad
       \mathcal A_TF_1^K=F_1^K+aF_2^K.}
\tag{7}
\]
The second identity is the actual running-a derivative of the first.
No oscillator equation for K was used. At r=1 the distributional jump of
F0 is multiplied by r log r=0. F1 and F2 themselves vanish there.
Thus (7) also holds distributionally for the whole-space extension (4).

There is a useful converse on u>0,a>0 at each fixed T. The first identity
says u g_u=a g_a. In coordinates x=au, y=a, write g=G(x,y).
Then u g_u-a g_a=-y G_y, so G is independent of y on each connected
characteristic segment. The local solution is an arbitrary K_T(au).
The first-order source relation alone leaves kernel freedom; it does
not force one T-independent kernel either. Our comparisons satisfy the
stronger choice of one fixed K for all T.

This does not correct [Note31, Section5][n31]. That section's literal
source uniqueness keeps cosine fixed and varies the amplitude. Here the
amplitude is fixed and the kernel varies, an expressly different class.

## 3. An exact quartic at the fixed mark

Define the exact positive moments
\[
M_j=\int_0^\infty u^j q_{T_c}(u)\,du.
\tag{8}
\]
Every M_j used here is finite; M0,M2,M4>0 follow from the complete
positive theta tail. No approximation to these moments is needed.

Freeze the real even polynomial
\[
K_*(x)=1-\frac{2M_0}{A_c^2M_2}x^2
          +\frac{M_0}{A_c^4M_4}x^4.
\tag{9}
\]
Its coefficients remain frozen when differentiating T or a. The exact
three-dimensional Jacobian is
\[
4\pi r^2\,dr\,\rho_T(r)=q_T(u)\,du.
\tag{10}
\]
Consequently the comparison observation at T_c is
\[
\begin{split}
H_*(T_c,a)
 &=\int_{\mathbb R^3}F_0^{K_*}(T_c,a)
   =\int_0^\infty q_{T_c}(u)K_*(au)\,du\\
 &=M_0\left(1-\frac{a^2}{A_c^2}\right)^2.
\end{split}
\tag{11}
\]
At A_c=2 this gives exactly
\[
H_*(T_c,A_c)=H_{*,a}(T_c,A_c)=0,\qquad
H_{*,aa}(T_c,A_c)=\frac{8M_0}{A_c^2}=2M_0>0.
\tag{12}
\]
This is an exact double zero of the comparison observation, not a
physical Newman collision. Unit heat convolution preserves both
complete integrals; therefore m=(0,0) for W0 in (3).

The raw F0 is nonzero on a set next to r=1 because K_*(0)=1 and rho>0.
Gaussian convolution is injective on these L2 data: its Fourier
multiplier is exp(-|xi|²), which never vanishes. Hence U0 is nonzero and
E0>0. The theta tail dominates every polynomial in u and every spatial
power; all raw moments exist. Convolution with K1 gives a radial
Schwartz pair, despite the initial jump at r=1. All prepared first and
second absolute moments and all Sobolev norms required in Note28 are
finite.

Thus the ratio is nonnegative throughout this comparison class and is
zero for (9):
\[
\boxed{\inf_K\frac{|\int W_0^K|^2}{\|W_0^K\|_2^2}=0
       \quad\hbox{at }p_c.}
\tag{13}
\]
The denominator is nonzero for every normalized polynomial K in this
class. This is an attained exact obstruction to the stated coercivity,
not an asymptotic smallness calculation.

## 4. Any fixed finite cosine Taylor prefix survives

This is the same two-moment construction, not a second research
candidate. For any integer N>=0 use the cosine coefficients checked in
[DLMF4.19.2][dlmf], with the inspection scope in [reference15][ref15]:
\[
C_N(x)=\sum_{j=0}^N\frac{(-1)^j x^{2j}}{(2j)!},\quad
S_N(a)=\sum_{j=0}^N\frac{(-1)^j M_{2j}a^{2j}}{(2j)!}.
\tag{14}
\]
Put d=2N+2, s_N=S_N(A_c), and t_N=A_c S_N'(A_c). Define
\[
\begin{split}
\gamma_N&=\frac{t_N-(d+2)s_N}{2M_d A_c^d},\\
\delta_N&=\frac{d s_N-t_N}{2M_{d+2} A_c^{d+2}},\\
K_N(x)&=C_N(x)+\gamma_N x^d+\delta_N x^{d+2}.
\end{split}
\tag{15}
\]
Every denominator is strictly positive. If
X_N=gamma_N M_d A_c^d and Y_N=delta_N M_{d+2} A_c^{d+2}, then
\[
X_N+Y_N=-s_N,\qquad dX_N+(d+2)Y_N=-t_N.
\tag{16}
\]
These two identities give
\[
H_{K_N}(T_c,A_c)=0,\qquad
\partial_aH_{K_N}(T_c,A_c)=0.
\tag{17}
\]
Meanwhile K_N and cosine have identical derivatives at x=0 through
order 2N+1. They also give the same observation derivatives at a=0
through that order, for every T, by integration. The N=0 case is
exactly (9).

For every finite N, (7), nonzero prepared energy, finite moments and
(13) remain valid within the class with this prescribed prefix. The
comparison observation is not identically zero, since its value at
a=0 is M0. Its zero at A_c has order at least two; nonzero second
derivative is asserted only for N=0, where (12) proves it.

Quantifiers matter: for each finite N there is a separately frozen
K_N. No single noncosine entire kernel matches all cosine Taylor
coefficients; no convergence of these polynomials to cosine, uniform
coefficient bound, real-axis boundedness, or controlled error from cosine
is asserted. This does not cover full function-valued raw jets at A_c or
quantitative remainders on the observation range.

## 5. Preparation and the feedback deadline are retained

Hold p_c and its feedback path fixed for all running-a derivatives.
Let W=(U,V) and J2 solve the same marked equation
\[
W_s=L_sW,\quad J_{2,s}=L_sJ_2,\qquad
L_s=\Delta+\alpha(s)\operatorname{div}(v\,\cdot),\quad
v=X+\frac{X}{1+r^2},\quad
\alpha=\frac{2G}{D},
\tag{18}
\]
where G=||grad W||², D=int (div v)|W|² and E=E0>0. These are the
original feedback and actual jets of the comparison observation.
The parameter derivatives of the mark itself are not substituted.

With Theta=(A_c V,V+A_c J2) and R=A_Tc W-Theta, (7) gives exactly
\[
R_0=[\mathcal A_{T_c},K_1*](F_0^K,F_1^K),\qquad
R_s=L_sR+[\mathcal A_{T_c},L_s]W.
\tag{19}
\]
Here R_s denotes the auxiliary-time derivative in the second equation.
There is no additional raw-mismatch term. There is also no permission
to drop this commutator, its cutoff derivatives, or the inner ball.

In fact R0 is nonzero for every constructed K_N. Each K_N is nonconstant:
a constant normalized kernel could not give (17). Thus F1 is nonzero,
and Gaussian injectivity gives V0 nonzero. Gaussian convolution of these
rapidly decaying data is real analytic in X. If V0 vanished throughout
r<1/2, analytic continuation would make it zero everywhere, a
contradiction. Since b=c=0 in that ball,
\[
R_{U,0}=-A_c V_0\quad(r<1/2),\qquad
\|\omega R_0\|_2^2>0,\quad \omega=(1+r^2)^{-2}.
\tag{20}
\]
At the unit sphere the exact identity remains
R=(-A_c V,-V-A_c J2), with the same cancellation as Note31. No separate
zero-residual propagation is used.

The fixed operator, true residual and actual J2 satisfy the hypotheses
used in the weighted/local estimates of [Note40][n40] and the supporting
R5 estimate [Note47][n47]. The source-slope and coefficient bounds depend
on the unchanged rho_T. The jet payment is the elementary inequality
||Theta||²<=(A_c²+2)||V||²+2A_c²||J2||². None of these steps uses
K''+K=0. Their finite allowances still depend on the true initial norms
and compression B; no uniform-in-N initial cost is claimed.

The local construction and zero-mass deadline of [Note28, Sections5–6][n28]
apply to any such nonzero Schwartz pair. They use no physical Newman
identity. With
\[
P_0=\int_{\mathbb R^3}|X|\,|W_0(X)|\,dX\in(0,\infty),\qquad
B(s)=\int_0^s\alpha(\tau)\,d\tau,
\]
the exact m=0 gives
\[
\boxed{S_{\max}\le
 \frac{60}{7(5\pi^2)^{2/5}}
 \frac{P_0^{4/5}}{E_0^{2/5}}<\infty,\qquad
 B(s)\longrightarrow\infty\text{ as }s\uparrow S_{\max}.}
\tag{21}
\]
This is an application of the inherited in-note theorem, not a new
well-posedness proof or independent audit of that theorem. It prevents
a regularity-through-deadline conclusion for the whole reduced class.
It does not preclude useful local estimates, estimates with additional
quantitative hypotheses, or an estimate specific to the actual cosine
trajectory.

## 6. The missing physical premise

For any fixed K, direct differentiation of (2) gives the exact defect
\[
F_2^K+u^2F_0^K
 =(\partial_T+\partial_a^2)F_0^K
 =\mathbf1_{r\ge1}\rho_T u^2\{K''(au)+K(au)\}.
\tag{22}
\]
Here multiplication by u² is on the raw exterior density, extended by
zero inside. Every constructed K_N is a nonzero polynomial. Its highest
nonzero degree term survives in K_N''+K_N, so the right side is not
identically zero. At fixed A_c>0 it is nonzero as a spatial function.
The integrated physical equation also fails as an identity in a,T:
if c_D a^D is the top term of K_N(a), the top a^D coefficient of
(partial_T+partial_a²)H_K is c_D M_{D+2}(T), which is nonzero.

Thus the comparisons fail the full cosine oscillator identity, the
physical Newman heat equation, and cosine's bounded real-axis kernel.
No all-real regime, threshold-transfer property or physical collision
claim is assigned to them.

Conversely K''+K=0, K(0)=1, K'(0)=0 forces K=cos: the power-series
recurrence (j+2)(j+1)c_{j+2}=-c_j fixes every coefficient. Adding the full
identity therefore selects the literal target; it does not by itself
prove a new quantitative estimate.

For the *actual theta* prepared family, its raw oscillator identity
takes the nonlocal form
\[
J_{2,0}=-K_1*(u^2F_0),\qquad
J_{2,s}=-\mathcal P_s^{p}\big[K_1*(u^2F_0)\big],
\tag{23}
\]
where P_s^p is the common propagator of the fixed marked alpha path.
It is not J2,s=-u(X)² U_s. Formula (23) identifies information lost by
the reduced premise test; no new estimate using it is selected or
tested in this round.

## 7. Control screening and research disposition

The controls indexed in [result-summaries/12][controls] and the discipline
in [avoid/02][a02] are applied by their exact premises, not by assuming
all controls satisfy all hypotheses.

| Comparison | Premise it fails here | Role in this round |
| --- | --- | --- |
| Euler-factor, weighted-square and finite-prime/source perturbations | Unchanged complete canonical amplitude; in particular the original unit weights/source coefficients | They cannot refute the reduced fixed-amplitude test by themselves |
| Reflected super-Gaussian, smooth shape and positive-primitive controls | The literal complete theta amplitude, even when reflection or finite/all endpoint conditions are shared | Existing R5 operator bounds may admit them with their true raw-mismatch term, but they are outside the new fixed-amplitude premise |
| Atomic/profile threshold controls and RH-conditional endpoint perturbations | The unchanged continuous canonical amplitude; their additional threshold qualifications remain as indexed | No threshold premise is imported into this auxiliary information test |
| Present polynomial kernel family | The full cosine kernel/oscillator and physical Newman equation, while retaining canonical amplitude and zero raw mismatch | Exact counterexample to the explicitly reduced premise class only |

The earlier same-operator colliding control has both a preparatory
commutator and its raw-mismatch contribution. This construction removes
the latter by changing the kernel instead of the source. The distinction
is precisely why it is a new test of an unused premise and **not** a
stronger physical theta counterexample.

**Disposition:** CTF-B02 R6 is complete as a proved in-note scoped
negative, with [same-assistant assessment27][r27]. The attained ratio
zero is the quantitative return. Parent B02 remains partial; E03/B03
remain gated. No numerical source acquisition, new PDE, second candidate,
manuscript integration or physical coverage extension occurred.

Next is **[E] CTF-E08 R6 — Sol**, a fixed assessment of this proof and its
scope under the [issued packet][packet]. [Continuation52][next] gives
model-change guidance. Further work on actual joint cosine/source
compatibility requires a newly recorded B02 candidate after assessment;
(23) is a boundary statement, not an approved estimate. The relevant
established-results and failure-pattern navigation is [result index][results]
and [avoid index][avoid], especially [scoped exclusions][a07] and
[restating the target][a01]. No novelty or specialist-review claim is made.

[n28]: 28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n31]: 31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md
[n40]: 40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md
[n47]: 47_EXTERIOR_SOURCE_RESIDUAL_COUPLING_B02_R5_20261029.md
[n50]: 50_SOURCE_COUPLING_INTEGRATION_AND_MODEL_CONTINUATION_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[r27]: ../reviews/27_ZERO_RAW_MISMATCH_B02_R6_SELF_ASSESSMENT_20261029.md
[packet]: ../research-progress/handoffs/CTF-E08_RAW_COMPATIBILITY_ASSESSMENT_REQUEST_R6_20261029.md
[next]: 52_RAW_COMPATIBILITY_SOL_CONTINUATION_20261029.md
[dlmf]: https://dlmf.nist.gov/4.19.E2
[ref15]: ../references/15_COSINE_KERNEL_COMPATIBILITY_REFERENCES_20261029.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
