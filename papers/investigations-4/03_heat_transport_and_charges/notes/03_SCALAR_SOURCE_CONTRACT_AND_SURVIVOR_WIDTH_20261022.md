# Scalar source contract and ordinary-double survivor width

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from the active root turn metadata.

**Status: ICW-02 complete for one parameterized candidate; its direct-comparison
gate fails. A local ordinary-double conditioning bound is proved below.
No theta backward-survival estimate or endpoint exclusion is established.**
This is the default two-scalar-path pilot. Boundary simplification is a
separate objective, developed in [Note 04][boundary], rather than being
rejected merely because it supplies no noncollision theorem.

Read the [result index][results], [avoid index][avoid], [control register][controls],
[target classification][a01], [coupled-estimate rule][a12] and
[scoped-conclusion rule][a07]. [Note 02][previous] supplies the inherited
separation lemma. The [review][review] is internal same-model assessment,
not specialist review. No mathematical priority claim is made.

## 1. One explicit canonical-source pilot

Use the unchanged canonical normalization
\[
 H(t,x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,\quad
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
 \qquad H_t=-H_{xx}.
\]
Thus H(0,z)=xi(1/2+iz/2)/8; the normalization and heat sign were checked
against [Rodgers–Tao, equations (1), (3), (4)][rt]. All coefficients and
full reflection Phi(u)=Phi(-u) are retained. A finite head is not separately
even. Home 02's [source contract][source] and the [BW14 tail interface][tail]
remain authoritative for shared source work.

**Declared parameters.** Fix T=1/4, a finite height chart [A,B], two rational
centers xi_-<xi_+ and positive rational radii r_i with
I_i=[xi_i-r_i,xi_i+r_i] contained in [A,B]. At T, a certified consecutive
simple-root gap contains both centers. For the conditional separation
application, assume its two boundary roots a(t)<b(t) continue simply on
0<t<=T and assume the [all-real paired-product hypotheses][product].
For a theta simplicity application this is explicitly RH-conditional.
No positive lower bound for their unknown endpoint separation is assumed.
This is a parameterized theorem: no actual theta gap, root brackets,
terminal values or trajectories have been acquired in this round.

Initial points may be uncertain by delta_i>=0 around xi_i, with
xi_+-xi_->delta_-+delta_+. Both are required to be in the selected gap at T.
Acquire a common sign sigma and paid bounds
\[
 0<A_i\le\sigma H(T,\xi_i),\qquad
 B_j\ge M_j(T):=\int_0^\infty u^j e^{Tu^2}\Phi(u)\,du\quad(j=1,2).
\]
On u>=0 every source summand is positive. Hence |H_x|<=B_1 and
|H_t|=|H_xx|<=B_2 on the entire real axis and 0<=t<=T.
The scalar current is **v_0=2H_x/H=-2S_1/C_0**, not the phase current.

The candidate acceptance inequalities are
\[
 m_i:=A_i-TB_2-r_iB_1>0,\qquad
 \delta_i+2TB_1/m_i<r_i.                                      \tag{1}
\]
They must be verified from the complete source, not assumed as endpoint
floors. The measurable research success rule is stronger coverage or a
stronger complete gap estimate than direct evaluation given the same data.
Section 3 proves that this particular contract cannot meet that rule.

## 2. Complete error and continuation ledger

Here is an explicit possible acquisition scheme, not an executed certificate.
Keep n<=N and 0<=u<=U, with integers N>=1, U>=1. Write lambda_n=pi n²,
phi_n=(2lambda_n²e^{9u}-3lambda_ne^{5u})e^{-lambda_ne^{4u}}.
Both terms are retained in finite integration. For k=N+1 set
\[
 \rho=((k+1)/k)^4e^{-\pi(2k+1)},\quad b=4\lambda_k-9,\quad
 L_j={2\lambda_k^2e^{-\lambda_k}j!\over(1-\rho)b^{j+1}}.       \tag{2}
\]
This bounds the **entire omitted-mode half-line**, weighted by u^j e^{Tu²}.
Indeed consecutive positive leading terms have ratio at most rho, and
exp(4u)>=1+4u+8u² bounds the remaining integral by a gamma integral.
The sufficient conditions rho<1, b>0, T<=8lambda_k hold here.
For each retained n put
\[
 b_n=4\lambda_ne^{4U}-9-2TU,\qquad
 E_{n,j}=2\lambda_n^2e^{TU^2+9U-\lambda_ne^{4U}}
 \sum_{a=0}^j {j\choose a}{U^{j-a}a!\over b_n^{a+1}}.        \tag{3}
\]
Expanding at u=U bounds its complete exterior ray. The sufficient conditions
b_n>0 and T<=8lambda_ne^{4U} also hold for these parameters. Equations
(2)–(3) hold for every integer j>=0, and cover disjoint omitted pieces.
Dropping the negative summand is only an upper-bound step, not a changed source.

For a composite midpoint rule on the retained rectangle with cell lengths
h_l, a paid error for each scalar kernel f is
\[
 E_{\rm quad}(f)\le\sum_l h_l^3\sup_{\text{cell }l}|f''|/24.
\]
Finite interval arithmetic must enclose these derivatives and all node,
coefficient and transcendental rounding. No estimated floating error is
substituted. Add that acquisition error and L_j+sum E_{n,j} to each
jth-moment/jet enclosure. Terminal value uses j=0; B_1,B_2 use j=1,2.
No sampled C_2 is promoted to a whole-tube observation: the bounds here
come from complete absolute source moments.

The exact jet residuals remain integrals against the **same** omitted
source, with kernels (cos(xu), -u sin(xu), -u²cos(xu)). In a joint support
bound, integrate the absolute value of the combined kernel before splitting
into componentwise allowances. The componentwise sum of (2)–(3) is an explicitly weaker
relaxation used by this candidate. Full reflection is an identity of the
complete sum; no independent symmetrization or adjustable tail is allowed.
A hypothetical event must retain both C_0=S_1=0 simultaneously. No event
location or event-matching observations are supplied here.

| Payment | Rule and scope |
| --- | --- |
| Source modes and exterior ray | Equations (2)–(3), for every retained observation, with unchanged coefficients. |
| Finite integration and arithmetic | Cell derivative bound above plus outward rounding; shared observations remain joint. |
| Terminal root/gap identification | Paid brackets/count and initial-point containment are input premises, presently unacquired. |
| Position uncertainty | delta_i at T, and the entire radius r_i charged through r_i B_1 in (1). |
| Physical-time variation | TB_2, derived from the full source uniformly through t=0. |
| ODE discretization | Zero in the analytic proof below; no numerical wall was substituted. |
| Endpoint limit | Positive fixed m_i and a fixed compact tube, independent of epsilon. |

For completeness, a future computed wall would also need its complete
backward residual R(s)=z'(s)+v_0(T-s,z(s)). On the paid tube,
\[
 |v_0|\le2B_1/m_i,\qquad |\partial_xv_0|\le
 \mathcal L_i:=2(B_2/m_i+B_1^2/m_i^2),
\]
so its position error is at most
exp(mathcal L_i s)[delta_i+integral_0^s exp(-mathcal L_i u)|R(u)|du].
The reference path and its certified uncertainty region must stay in the
paid tube. R must include quotient evaluation error. Propagating sampled H_x or C_2
in time would additionally require M_3 or M_4, or direct interval evaluation
of their kernels over the full parameter cells. Those payments are not
needed by the present analytic proof and are not claimed acquired.

**Continuation proof.** On each whole tube,
sigma H(t,x)>=A_i-(T-t)B_2-|x-xi_i|B_1>=m_i.
Thus the vector field is regular and has the stated speed and Lipschitz
bounds. The strict displacement margin in (1) prevents tube exit by a
first-exit argument in backward time. A path cannot hit a root there.
Standard continuation on the closed tube extends it to t=0, with all
constants independent of epsilon. The two paths remain in the chosen gap
for t>0 because crossing its boundary would require H=0. Under the separate
paired-product sign q>=0, their separation is at least their terminal
separation. This proves a sufficient theorem, not that (1) holds for theta.

## 3. Proved same-information dominance failure

Already without solving an ODE,
\[
 \sigma H(t,\xi_i)\ge A_i-(T-t)B_2\ge A_i-TB_2>0.           \tag{4}
\]
Each successful tube implies (4). In fact its entire stationary interval
I_i has the positive floor m_i. Because the continued gap roots cannot
cross either interval, the direct method gives
\[
 b(t)-a(t)>(\xi_++r_+)-(\xi_--r_-),\qquad 0<t\le T.        \tag{5}
\]
Endpoint limits obey the corresponding non-strict bound. This is stronger
than the initial two-path separation and needs neither the speed inequality
in (1) nor q>=0. One stationary point with a uniform nonzero value already
precludes a finite collision of the two roots enclosing it.

The strongest direct comparator is allowed the complete signed kernel
\[
 H(t,x)=H(T,x)-\int_0^\infty e^{Tu^2}\Phi(u)
       [1-e^{-(T-t)u^2}]\cos(xu)\,du.                     \tag{6}
\]
It receives the same source cells, joint constraints, precision and tails.
Even its unsigned exact-source allowance
D_T=integral (e^{Tu²}-1)Phi(u)du is strictly smaller than T M_2(T).
At finite precision, strict improvement needs its own paid margin; use the
minimum of available rigorous bounds. Equation (5) alone proves dominance,
so no new acquisition or favorable numerical outcome is needed for the stop.

**Decision: stop only the terminal-floor/absolute-moment two-tube candidate
as a means of outperforming direct noncollision estimates.** This is not a
failure of integral simplification, of all moving corridors, or of signed
coupled theta estimates. No cost advantage was measured.

For a noncanonical control below, B_2 may be any valid uniform local
bound for |H_xx|. The floor fails exactly near an ordinary double. For a sufficiently small
local chart around H(0,a)=H_x(0,a)=0, h_2=H_xx(0,a)!=0, H(0,x) has sign h_2
apart from its zero, while H(T,x) has the opposite sign inside the born gap.
Consequently, at every fixed terminal interior point x,
\[
 |H(T,x)|\le |H(T,x)-H(0,x)|\le TB_2.                     \tag{7}
\]
Thus even the direct margin in (4) fails; no asymptotic guess is necessary.
For H=x²-2t, it is exactly 2T-x²<=2T. These local statements use a sufficiently
small T around the control event; they do not assert that the fixed theta
pilot T=1/4 is such a chart.

## 4. A quantitative ordinary-double survival screen

**Proposition (local, collision-compatible).** Let H be real analytic near
an ordinary double at (0,a), satisfying H_t=-H_xx. For a sufficiently small
fixed T>0, let S_epsilon(T) be the terminal positions whose scalar-current
paths remain strictly inside its born gap for all epsilon<=t<=T. Then
\[
 \operatorname{diam}S_\varepsilon(T)\le
 2\sqrt{2(1+LT)}e^{2(L+K)T}{\varepsilon^{5/2}\over T^2}.     \tag{8}
\]
Here L,K are finite event-chart constants defined below. No global all-real
product or theta arithmetic is assumed.

Real analytic preparation gives
\[
 H(t,x)=A(t,x)((x-m(t))^2-D(t)),\quad A\ne0,\quad
 m(0)=a,\quad D(0)=0,\quad D'(0)=2.
\]
The last equality follows from H_t=-H_xx and A(0,a)=h_2/2.
Shrink T so the closed born gap lies in this chart and choose
|D(t)/(2t)-1|<=Lt, LT<=1/2 and |partial_x² log|A||<=K there.
With d=sqrt D and r_±=m±d,
\[
 q={1\over(x-r_-)^2}+{1\over(x-r_+)^2}
       -\partial_x^2\log|A|
 \ge {2\over D}-K\ge {1\over t}-(L+K).                    \tag{9}
\]
The two-pole lower bound is minimized at the midpoint. The last inequality
uses D<=2t(1+Lt) and 1/(1+Lt)>=1-Lt.

On each compact [epsilon,T], every point of the early gap flows forward
inside the gap. Indeed
v_0=2/(x-r_-)+2/(x-r_+)+2A_x/A. Near the left boundary the distance derivative
is 2/(x-r_-)+a bounded remainder, hence positive; the analogous derivative
of distance to the right boundary is also positive near that boundary.
Root derivatives and the other terms are bounded on [epsilon,T]. Neither
boundary is hit forward, and ordinary continuation applies.

This increasing flow maps the early gap exactly onto S_epsilon(T), by
uniqueness. For two such solutions their difference obeys
Delta'<=(-2/t+2(L+K))Delta by (9). Integration yields
Delta(T)<=exp(2(L+K)(T-epsilon))(epsilon/T)² Delta(epsilon).
The early gap length is 2sqrt(D(epsilon)); this proves (8).
In particular at most one fixed terminal datum survives all the way to
zero. Existence of such a datum is not needed or asserted by this argument.

The exponent is sharp. The quadratic first integral from Note 02 gives
S_epsilon(T)=(-r_epsilon,r_epsilon), where
\[
 r_\varepsilon(T-r_\varepsilon^2/10)^2
       ={16\sqrt2\over25}\varepsilon^{5/2},\quad
 0<r_\varepsilon<\sqrt{2T}.
\]
The left side is increasing on that interval, and therefore
\[
 \operatorname{diam}S_\varepsilon(T)
 ={32\sqrt2\over25}{\varepsilon^{5/2}\over T^2}
       [1+O((\varepsilon/T)^5)].                           \tag{10}
\]
This quantifies the conditioning of finite-cutoff tracking. It is not a
universal numerical complexity lower bound, a higher-multiplicity theorem,
a theta discriminator, or a noncollision result. Constants are not asserted
uniform over height, sources or events. The proof is the evidence; the
[small exact-arithmetic checks][checks] are diagnostics only.

## 5. Mandatory controls and next unpaid work

| Control | Application premise not supplied | Quantitative compatibility |
| --- | --- | --- |
| Quadratic | Not the canonical source | Equation (7) fails the floor; (10) retains its collision exactly. |
| Atomic / finite-profile threshold controls | Unchanged theta coefficients, complete profile and eventual threshold simplicity fail | Any actual event-containing floor must fail; ordinary local doubles obey (8). |
| Euler-factor controls | Canonical arithmetic changed | Do not assign an event from a Laguerre witness; if an actual event lies in a tested slab, its floor fails. |
| Weighted-square / finite-source controls | Full reflection fails; no all-real heat time | Their actual event boxes fail the floor; the local theorem needs no global all-real premise. |
| Finite-prime orbit controls | Full reflection and unchanged full sequence fail | Events can escape with different sources; no event in this fixed chart is asserted. |
| Reflected / positive-primitive controls | Canonical square coefficients fail | Their known event-containing boxes cannot satisfy the floor. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet arithmetic fails, despite simple all-real positive-time roots | Actual added doubles force the local floor failure; all-real positive-time geometry alone is insufficient. |

Noncanonical arithmetic is not the reason the generic floor theorem rejects
an event: the quantitative inequality fails there. A collision-free box of
any control may correctly pass. Keep each family's separate preservation
list from [cluster 12][controls]; no new continuation data are invented.

ICW-02 is complete for this scoped failed candidate. ICW-03 still needs a
signed, coupled unchanged-theta estimate that controls backward escape and
the singular C_0 denominator, with constants surviving epsilon->0 and a
matched direct comparison. The separate boundary-simplification objective
can progress without that estimate; see Note 04 and ICW-07. Neither route
supplies I4-H01's entire complex boundary or all-height/multiplicity coverage.

[previous]: 02_INTERIOR_CURRENT_WALLS_AND_BACKWARD_SURVIVAL_20261022.md
[boundary]: 04_PHASE_BOUNDARY_REMOVAL_AND_CAP_REDUCTION_20261022.md
[review]: ../reviews/03_SOURCE_CONTRACT_SURVIVOR_AND_BOUNDARY_REVIEW_20261022.md
[checks]: ../numerics/ICW_ANALYTIC_CHECKS_20261022.json
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[source]: ../../02_theta_source_constraints/README.md
[tail]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/14_theta_source_transform_constraints/notes/04_CANONICAL_TAIL_LAPLACE_CONSTRAINT_AND_COUPLED_ENCLOSURE_20261021.md
[product]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/23_CAP_PHASE_CONCENTRATION_AND_FINITE_TIME_BASELINE_20261021.md
[rt]: https://arxiv.org/html/1801.05914
