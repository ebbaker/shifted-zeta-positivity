# Cosine and quartic collision responses and their scoped failure

29 October 2026, America/New_York. Research begun 28 October. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Investigation06 chat0003, **Compare auxiliary collision flows**.

**ACF-B01 R1 return: complete as a bounded candidate comparison; no C1
selected and no E01 request issued.** Exactly two flow/observable pairs
are tested: the cosine tilt with its normalized first response, and the
quartic tilt with its normalized first response. The cosine response is
a variance that stays positive at admitted collisions. The quartic
response can vanish at a nondegenerate collision even for a positive,
even, entire source with double-exponential decay and an entire quartic
tilt. Neither tested response mechanism supplies an independent canonical
separating estimate.

The control construction in Section 4 is **proved in-note, with
same-assistant analytical checking only**. It repairs the Gaussian
domain mismatch in the inherited quartic comparison. The failure concerns
these first-response mechanisms using the stated generic premises; it is
not an impossibility result for either flow with additional signed theta
information, higher responses, or a different observable. No theta
collision or threshold claim follows.

The [decision](../brainstorm/02_ACF_B01_CANDIDATE_DECISION_20261029.md),
[live progress](../research-progress/01_AUXILIARY_COLLISION_FLOWS_RESEARCH_PROGRESS_20261028.md)
and [continuation](03_ACF_B01_SCOPED_FAILURE_AND_MODEL_CONTINUATION_20261029.md)
record the task boundary. The [result index][results], [avoid index][avoid],
[collision controls][controls], [target classification][a01],
[shared-premise screen][a02] and [scoped exclusions][a07] govern this return.

## 1 Two fixed candidates and their common domain

Retain the complete canonical source
\[
\Phi(u)=\sum_{n\ge1}
(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\qquad
H(t,z)=\int_0^\infty\Phi(u)e^{tu^2}\cos(zu)\,du.
\tag{1}
\]
Thus \(H_t=-H_{zz}\) and
\(H(0,z)=\xi((1+iz)/2)/8\). Newman time t and auxiliary time s are
independent. The mark a>0 is fixed independently of s and of the running
variable z. Define exactly the following two families:
\[
F_c(t,s,z;a)=\int_0^\infty\Phi(u)e^{tu^2+s\cos(au)}\cos(zu)\,du,
\tag{2}
\]
\[
F_4(t,s,z)=\int_0^\infty\Phi(u)e^{tu^2+su^4}\cos(zu)\,du.
\tag{3}
\]
Both have initial slice \(F_q(t,0,z)=H(t,z)\), including the exact
original xi function at t=0. The complete theta tail makes both entire
in (t,s,z) for fixed real a. Their equations are
\[
\partial_tF_q=-\partial_z^2F_q,\qquad
\partial_sF_c=L_aF_c,\quad
L_af(z)=\tfrac12(f(z+a)+f(z-a)),\qquad
\partial_sF_4=\partial_z^4F_4.
\tag{4}
\]
These statements follow directly under the integral; they require no
well-posedness assertion for arbitrary data of the corresponding PDE.

For real t,s put \(M_q(t,s)=F_q(t,s,0)>0\) and
\(U_q=F_q/M_q\). The normalized fields are real analytic there and
locally holomorphic where \(M_q\ne0\). They are not asserted to be entire
quotients on complex parameter space. Write
\[
M_j(t)=\int_0^\infty u^j\Phi(u)e^{tu^2}\,du,\qquad
\mu_4(t)=M_4(t)/M_0(t)>0.
\]
Our two observables, with fixed perturbation conventions, are
\[
\mathcal O_c(t,a)=\partial_sU_c(t,0,a;a),\qquad
\mathcal O_4(t,a)=\frac{\partial_sU_4(t,0,a)}{\mu_4(t)}.
\tag{5}
\]
The quartic normalization measures its initial response relative to the
positive fourth source moment; it is not a bounded-generator claim.
No addition of a constant or a multiple of u² to either generator is
permitted in this comparison.

The physical question is local to \(0<T\le1/2\), a>0 and a
nondegenerate real double event
\[
H(T,a)=H_z(T,a)=0,\qquad A=H_{zz}(T,a)\ne0.
\tag{6}
\]
One may restrict to any fixed finite rectangle inside that parameter
range. No uniform high-height estimate or higher-multiplicity assertion
is sought. Inherited local squared-gap calculus [Note38][n38] gives
\[
D_t(T,0)=8,\qquad D_s(T,0)=-8R_q(T,a)/A,
\quad R_c=\tfrac12(H(T,0)+H(T,2a)),\quad R_4=H_{zzzz}(T,a).
\tag{7}
\]
In particular, the original heat direction already unfolds every event
in (6). A larger auxiliary speed has no intrinsic significance without
its source and curvature payments.

## 2 Cosine normalization exposes a generic variance

At real t,s let expectation be with respect to the probability density
\(\Phi(u)e^{tu^2+s\cos(au)}/M_c(t,s)\) on the half-line, and put
X(u)=cos(au). Then
\[
m(t,s):=U_c(t,s,a;a)=\mathbb E_s X=\partial_s\log M_c,
\qquad
\partial_sm=\mathbb E_sX^2-(\mathbb E_sX)^2.
\tag{8}
\]
Since the source is positive on intervals and a>0, X is not almost
surely constant. Consequently
\[
0<\partial_sm\le1-m^2\le1
\quad\text{for every real }t,s.
\tag{9}
\]
At an event, m(T,0)=0 and
\[
\mathcal O_c(T,a)=\frac{P_a(T)}{M_0(T)}>0,
\qquad
P_a(T)=\int_0^\infty\Phi(u)e^{Tu^2}\cos^2(au)\,du.
\tag{10}
\]
Neither (8) nor (9) uses H_z=0. The same regular variance response
occurs at simple zeros and away from zeros. Boundedness, monotonicity and
strict convexity of this normalized partition function are therefore
compatible with a physical double event.

For example, the exact [Note38 control][n38] has
\[
\Phi_*(u)=(64u^4+6)e^{-(4+T_c)u^2},\qquad T_c=1/4,
\]
\[
H_*(T_c,z)=C(z^2/4-6)^2e^{-z^2/16},\qquad C=\sqrt\pi/16.
\]
At a=2sqrt(6), A=12Ce^{-3/2}>0, \(M_0=36C\), and
\[
\mathcal O_{c,*}=\frac{18+162e^{-6}}{36}
=\frac12+\frac92e^{-6}\in(0,1).
\tag{11}
\]
It passes the full variance bound at its collision. Its cosine family
is holomorphic on Re t<4+T_c for every complex s,z. Section 4 supplies
additional colliding controls with double-exponential decay and complete
complex-time admissibility; their cosine variance is also strictly positive.

**Decision for this pair:** do not select variance positivity or bounded
normalized response as a canonical separator. This conclusion does not
exclude a further quantitative inequality using the actual theta
coefficients. No such inequality with a defensible separating constant
has been supplied in this round.

## 3 The quartic response has no forced nonzero value

Mass normalization in (3) gives the exact expression
\[
\mathcal O_4(t,a)=\frac{H_{zzzz}(t,a)}{M_4(t)}
-\frac{H(t,a)}{M_0(t)}.
\tag{12}
\]
At (6) this reduces to H_zzzz/M4, a signed fourth-moment integral.
The generic bound is \(|\mathcal O_4(T,a)|\le1\); it has no positive
lower bound furnished by positivity of the source. The following
construction proves that zero is actually attained in a source class
with all the analytic requirements of (2) and (3).

This matters because the inherited quadratic polynomial example is not
a positive integrable Fourier source, while a Gaussian-tail source does
not admit a positive quartic tilt. Neither limitation applies to the
completed construction below.

## 4 A positive double-exponential control with zero quartic response

**Proposition.** Fix any real T and any a>0. For all sufficiently small
nonzero real epsilon there is an even, entire, strictly positive real
source \(\Phi_\epsilon\), with double-exponential decay on the real
axis, such that its quartic family is entire in (t,s,z) and
\[
H_\epsilon(T,a)=H_{\epsilon,z}(T,a)
=H_{\epsilon,zzzz}(T,a)=0,
\qquad H_{\epsilon,zz}(T,a)>0.
\tag{13}
\]
The smallness allowance may depend on a. This is an analytic existence
result, not a numerical epsilon certificate or a global threshold theorem.

### Gaussian seed with an exact double zero

Write r=sqrt(7), k=3+r and \(\alpha_0=a^2/k>0\). Define
\[
G_\alpha(z)=\frac{\sqrt\pi}{2\sqrt\alpha}e^{-z^2/(4\alpha)},
\quad
B(\alpha)=\frac{a^2}{2\alpha^2}-\frac3\alpha,
\quad
C(\alpha)=\frac{a^4}{16\alpha^4}
-\frac{a^2}{4\alpha^3}+\frac3{4\alpha^2}.
\tag{14}
\]
Differentiating the Gaussian cosine transform gives exactly
\[
\int_0^\infty (u^4+B(\alpha)u^2+C(\alpha))e^{-\alpha u^2}
\cos(zu)\,du
=\frac{G_\alpha(z)}{16\alpha^4}(z^2-a^2)^2.
\tag{15}
\]
At alpha0 its polynomial density is strictly positive:
\[
B_0=\frac{r-3}{2\alpha_0},\qquad
C_0=\frac{1+r/8}{\alpha_0^2},\qquad
u^4+B_0u^2+C_0=(u^2+B_0/2)^2+\frac{r}{2\alpha_0^2}>0.
\tag{16}
\]
The curvature of (15) at z=a is
\(G_{\alpha_0}(a)a^2/(2\alpha_0^4)>0\). Along this double-zero family,
the fourth derivative at the mark is
\[
Q(\alpha)=\frac{3G_\alpha(a)}{2\alpha^4}
\left(1-\frac{3a^2}\alpha+\frac{a^4}{2\alpha^2}\right).
\tag{17}
\]
Since a²/alpha0=3+sqrt(7), Q(alpha0)=0 and
\[
Q'(\alpha_0)=-\frac{3\sqrt7\,a^2G_{\alpha_0}(a)}{2\alpha_0^6}\ne0.
\tag{18}
\]
The Gaussian seed is used only to establish a transverse starting point;
its positive-s quartic integral is not used.

### Add the tail while retaining all three exact constraints

Set
\[
K(\epsilon,\alpha,B,C;z)=
\int_0^\infty(u^4+Bu^2+C)e^{-\alpha u^2-\epsilon^2\cosh(4u)}
\cos(zu)\,du.
\tag{19}
\]
This is smooth in real epsilon, alpha>0, B,C and real z, including
epsilon=0. On a neighborhood with alpha>=alpha0/2, each fixed number
of parameter or z derivatives is dominated by a polynomial times
\(e^{-\alpha_0u^2/2+C_*u}\). The factors from epsilon derivatives are
finite powers of cosh(4u); the negative exponential can be bounded by
one. Thus differentiation is justified also across epsilon=0. No
analyticity in epsilon at zero is asserted or needed.

The first two constraints K(a)=K_z(a)=0 determine B,C near their seed
values as smooth functions of (epsilon,alpha). Indeed, at epsilon=0
the determinant of their derivative matrix with respect to (B,C) is
\[
\det\frac{\partial(K(a),K_z(a))}{\partial(B,C)}
=\frac{a}{2\alpha^2}G_\alpha(a)^2>0.
\tag{20}
\]
For example, K_B=G_alpha(1/(2alpha)-z²/(4alpha²)) and K_C=G_alpha
give (20) directly. On the resulting double-zero branch,
K_zzzz(a) at epsilon=0 equals Q(alpha). Equation (18) permits a second
application of the ordinary real implicit function theorem, giving
smooth alpha_epsilon, B_epsilon, C_epsilon with all three constraints
zero and limits alpha0, B0, C0. Positivity of
C_epsilon-B_epsilon²/4 and of alpha_epsilon persists by (16).

Now define the physical source
\[
\boxed{\Phi_\epsilon(u)=
(u^4+B_\epsilon u^2+C_\epsilon)
e^{-(\alpha_\epsilon+T)u^2-\epsilon^2\cosh(4u)}.}
\tag{21}
\]
It is positive and even on the real line and entire in u. At physical
time T, the heat factor cancels the extra -T u² exactly, so (19)
proves the three zero constraints in (13). The positive curvature
persists by continuity from (15).

For fixed epsilon!=0 and complex (t,s,z) in any compact set, the
quartic integrand and any fixed derivative are dominated by a polynomial
times
\[
\exp\{-\epsilon^2\cosh(4u)+C_2u^2+C_4u^4+C_1u\}.
\tag{22}
\]
This is integrable: the first term dominates every displayed polynomial
as u tends to infinity. The same bound applies to the bounded cosine
tilt. Both families are therefore entire in all three parameters. This
proves the proposition without a numerical damping choice.

For these controls, \(\mathcal O_4(T,a)=0\), D_s(T,0)=0 and T'(0)=0
for the local double-event curve. The physical heat derivative remains
D_t=8. No claim is made that the mark does not move in s, or that
higher auxiliary responses vanish. The controls have the same real
double-exponential scale e^{4|u|}; their tail coefficient and prefactors
are not the literal theta tail. They lack its unchanged square
coefficients. Their all-real-zero time sets are not determined here.

## 5 Jets, normalization, boundaries and source payments

For either unnormalized family, every actual running spectral jet
\(J_j=\partial_z^jF_q\) obeys
\[
\partial_tJ_j=-J_{j+2},\qquad
\partial_sJ_j=L_aJ_j\ (c),\quad
\partial_sJ_j=J_{j+4}\ (4).
\tag{23}
\]
For real t,s let \(\mu_j(t,s)=\int u^j\Phi e^{tu^2+sq}/M_q\).
The normalization terms are retained:
\[
\partial_tU_q=-U_{q,zz}-\mu_2U_q,
\]
\[
\partial_sU_c=L_aU_c-mU_c,\qquad
\partial_sU_4=U_{4,zzzz}-\mu_4U_4.
\tag{24}
\]
These equations also hold for their running z derivatives. A derivative
of the cosine mark is different: for V=partial_a F_c,
\[
V_s=L_aV+\tfrac12\{F_{c,z}(z+a)-F_{c,z}(z-a)\},\qquad V|_{s=0}=0.
\tag{25}
\]
Suppressing this forcing would incorrectly identify a mark derivative
with a running spectral derivative.

There is no spatial preparation, integration by parts at u=0, or
propagation of a fixed logarithmic-source operator in these two tests.
Thus no preparation or boundary residual is being set to zero by an
assumption. The constant-coefficient operators in (4) commute with the
physical heat operator; the actual normalization terms (24) remain.
The nonzero preparation and commutator defects of [Note31][n31] belong
to its different fixed feedback system and are not imported or erased.

No finite source truncation is taken. On compact parameters a possible
future truncation at u=U and n=N would have to pay, for each consumed jet,
both the integral over [U,infinity) and the omitted complete-square sum
over [0,U], with weight
\(u^j|q(u)|^l e^{\operatorname{Re}t\,u^2+|s||q(u)|+
|\operatorname{Im}z|u}\). Neither is a free residual. Cosine absolute
majorants grow by at most e^{|s|}; the source difference costs at most
e^{|s|}-1. Quartic majorants instead consume e^{|s|u^4}, with no bounded
multiplier substitute. Domination (22) is qualitative for the control;
it supplies no certified finite epsilon, cutoff or evaluation cost.

## 6 Control screen and comparison with direct information

| Control | What the selected test does | Canonical premise absent or domain qualification |
| --- | --- | --- |
| Note38 polynomial Gaussian | Exact positive cosine variance (11) at its double event | Unchanged theta arithmetic and tail absent; positive quartic s is inadmissible, so this control is not used against the entire quartic family |
| Proposition (21) | Positive cosine variance and exactly zero quartic response at any prescribed fixed T,a; both tilts entire | Full canonical square coefficients and literal theta tail absent; positivity, evenness, entire source and double-exponential decay all hold |
| Euler-factor controls | Cosine variance law holds on their admitted source domain | Modified canonical factors and conductor; no actual theta separating constant is used by (8) |
| Weighted-square and finite-prime controls | The cosine law holds; theta-type source tails also admit quartic tilting | Complete unchanged coefficients or full reflection fail; no zero fourth-response value is asserted for their existing witnesses |
| Reflected super-Gaussian controls | Cosine law holds; quartic tilting uses only its actual convergence neighborhood | Canonical square arithmetic absent; one must not infer entire s from the label super-Gaussian |
| Smooth double-exponential shape and positive-primitive controls | Cosine law holds and real-tail quartic domination holds on their stated domains | Canonical square arithmetic absent; their existing witnesses are not recomputed here |
| Atomic and finite-profile controls | Bounded cosine formulas hold; variance is strict only when cos(au) is nonconstant on support | Continuity and canonical arithmetic absent; no density-based strictness is asserted for every atomic measure |

The survey's three-atom cosine example has cos(pi u)=+1 and -1 on
positive masses, so its variance is strictly positive, equal to one
at its stated auxiliary collision. The table applies the [registered
control scopes][controls]; it is not a new certificate for those witnesses.
Failure of canonical arithmetic is a source distinction, not an acquired
inequality discriminating a control.

At the physical slice both observables are already direct observations:
\[
\mathcal O_c(t,a)=
\frac{H(t,0)+H(t,2a)}{2M_0(t)}
-\left(\frac{H(t,a)}{M_0(t)}\right)^2,
\qquad
\mathcal O_4(t,a)=\frac{H_{zzzz}(t,a)}{M_4(t)}-\frac{H(t,a)}{M_0(t)}.
\tag{26}
\]
An implementation of these first responses does not require auxiliary
evolution. The cosine response consumes a translated H value; the quartic
response consumes a higher moment-weighted jet. These identities establish
no reduction in the information needed for a direct first-jet margin. No evaluated
cost or enlarged theta exclusion domain is claimed. The already paid
direct domains in [heat-flow results][heat] and [Note29][n29] remain the
baseline; rechecking them would be a method test.

## 7 Decision and evidence boundary

This is a **scoped failed design round**, with an analytical counterexample,
rather than an RH-equivalent criterion or a quantitative theta milestone.
The cosine variance response is valid but nonseparating. The quartic
nonzero-first-response premise is false in the admitted generic source
class. Neither result disproves that a useful estimate could exploit
the unchanged complete theta source.

No independent canonical inequality has been acquired or frozen. Asking
E01 simply to repeat (4), (23) and (26) would leave that conceptual issue
unchanged. Therefore this return selects no C1 and releases no E task,
numerical search, PDE simulation or certification packet. The broader
research objective remains open. [Continuation03][continuation] gives
the next bounded conceptual question and model-change instructions.

The Gaussian transform, determinant (20), transverse derivative (18),
positivity margin (16), and domination across epsilon=0 were checked
analytically by the same assistant. The implicit-function construction
has no numerical smallness constant and no independent review. Existing
source notes retain their own review statuses. The repository result and
avoid indexes are not amended by this unassessed design return.

The [literature survey][survey] remains the background; its ZP05 primary
source [Newman and Wu, Section 2.2, Theorem 2][nw] was rechecked for the
distinction between a universal multiplier and a source-specific argument.
No universal-preserver theorem is needed for the proofs above. The
[stable-model exclusions][stable] concern their specified spin and quartic
representations; they are not a theorem against the source tilt (3).

[continuation]: 03_ACF_B01_SCOPED_FAILURE_AND_MODEL_CONTINUATION_20261029.md
[results]: ../../../../result-summaries/README.md
[heat]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[stable]: ../../../../result-summaries/17_constructive_stable_model_obstructions.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[n29]: ../../05_radial_theta_collision_geometry/notes/29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n31]: ../../05_radial_theta_collision_geometry/notes/31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md
[n38]: ../../05_radial_theta_collision_geometry/notes/38_AUXILIARY_SOURCE_FLOWS_AND_COLLISION_RESPONSE_20261028.md
[survey]: ../lit-survey/01_AUXILIARY_COLLISION_FLOWS_ANNOTATED_LITERATURE_SURVEY_20261028.md
[nw]: https://arxiv.org/html/1901.06596v2#S2.SS2
