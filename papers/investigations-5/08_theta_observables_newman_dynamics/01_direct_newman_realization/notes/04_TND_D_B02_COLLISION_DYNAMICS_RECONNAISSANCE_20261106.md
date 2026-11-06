# TND-D-B02: collision dynamics in the conditional realization

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, verified in current turn metadata. Direct-branch chat0003, thread `01a1af86-e5ac-7841-ac70-e37f195c5cef`. **B — conceptual reconnaissance**, author-directed extension of B02. [Intake versions][inputs]; [sole register][progress]; [revised plan r2][plan].

**Disposition:** the initial analysis supports broadening B02 to investigate mechanisms for collision control within the assessed dynamics before selecting a particular estimating target. It identifies a smooth state evolution, a singularity of zero tracking, and exact signed transfers between count sectors. These are **derived here at proof-author/diagnostic scope**, with one local consistency pass, not a new collision exclusion, an assessed theorem, an estimating gain or an E03 request. No collision of the canonical theta family is asserted to exist.

| Next work | Type/model | Readiness and output |
| --- | --- | --- |
| TND-D-B02 continuation | B — Astra; source-specific collision-control structure remains an open conceptual question | Initial reconnaissance complete; later compare at most two structural approaches, then choose one consequential target or record a precise limitation. No follow-up target is selected here. |
| TND-D-E03 | E — Sol; execute a fixed mechanism lemma, identity or estimate | Reserved until B02 supplies its bounded contract. No request issued or execution activated. |

## 1. Scope and the collision being examined

Keep the full radius-1/2 cylinder, unchanged free Hamiltonian, all angular shells and signs, continuous radial momentum, every count outcome, and the source, domains, controller, clock and absolute calibration of [E01 Note02][e01]. [E02 Review01][e02] accepts that construction within its supplied conditional ideal-operation scope; its same-assistant/shared-premise qualifications remain. The [canonical shared E03][shared] is consumed, not repeated. This note changes no physical operation.

A collision means a multiple real zero of the **readout function** at a real observation parameter. It is not a collision of the fixed Hamiltonian's energy levels, nor a node of the prepared positive position density. Begin with an interior nondegenerate double event; higher finite multiplicities are addressed in §6. Temporal endpoints permit only the physical side inside the contracted slab. Complex zeros describe analytic continuation, not complex-valued measurement settings.

Write, with fixed gamma>0,
\[
\lambda(t)=\tfrac12-\gamma t,\quad 0\le t\le\gamma^{-1},\qquad
w_t(v)=\frac{e^{\lambda(t)v^2}\Phi(v)}{Z_{\lambda(t)}},\quad
\mu_r(t)=\int_{\mathbb R}v^r w_t(v)\,dv.
\tag{1}
\]
Here w is the Q_t/interaction-frame density and Z_lambda=2H_lambda(0). Let
\[
p(t)=\frac{H_{\lambda(t)}(0)}{H_{1/2}(0)},\quad
C(t,k)=\int w_t(v)\cos(kv)\,dv,\quad
D(t,k)=p(t)C(t,k)=\frac{H_{\lambda(t)}(k)}{H_{1/2}(0)}.
\tag{2}
\]
Thus q_0,+=(p+D)/2 and q_0,-=(p-D)/2 are the original q_+,q_-, with the added subscript only making the no-count sector explicit. C(t,0)=1 and D(t,0)=p(t)>0, so the event considered has k_* nonzero; by evenness we may discuss k_*>0.

E01's complete source majorants pay every fixed moment and derivative used below. No truncation, arbitrary derivative-order summation or uniform collision margin over all heights is used. The full angular trace remains exactly Tr R=1. Source integrals also justify local joint analyticity in t and the complex readout coordinate, independently of any operator Taylor series.

## 2. State and observation evolve regularly through an event

Differentiating (1), with the E01 moment domination, gives the exact selection law
\[
\partial_t w_t=-\gamma(v^2-\mu_2)w_t,\qquad
\frac{d}{dt}{\mathbb E}_t a(X)=-\gamma\operatorname{Cov}_t(a(X),X^2)
\tag{3}
\]
for the fixed polynomially bounded functions used here. Consequently,
\[
\dot p=-\gamma\mu_2p,\qquad
\dot\mu_2=-\gamma(\mu_4-\mu_2^2),\qquad
\partial_t C=\gamma(C_{kk}+\mu_2 C),\qquad
\boxed{\partial_t D=\gamma D_{kk}.}
\tag{4}
\]
The plus sign in the last equation is essential: laboratory time decreases Newman lambda, whose equation has the opposite sign. The normalization term disappears only for D, not for C.

The normalized positive square root satisfies the already assessed tangent law
\[
\partial_t\sqrt{w_t}=-\frac\gamma2(v^2-\mu_2)\sqrt{w_t},\qquad
\|\partial_t\sqrt{w_t}\|_2^2
=\frac{\gamma^2}{4}(\mu_4-\mu_2^2)<\infty.
\tag{5}
\]
The variance is bounded on the fixed slab by its complete moments. Also p>=Z_-1/2/Z_1/2>0. The prepared conditional density operator has the inherited finite-order smoothness in trace norm: differentiating its rank-one ensemble uses exactly the radial norms and summable angular energy moments paid in E01. No analyticity or norm differentiability of U(t) on the unrestricted Hilbert space is claimed.

Suppose
\[
C(t_*,k_*)=C_k(t_*,k_*)=0,\qquad
A_*:=C_{kk}(t_*,k_*)\ne0,\qquad 0<t_*<\gamma^{-1}.
\tag{6}
\]
At the event,
\[
q_{0,+}=q_{0,-}=p_*/2>0,\quad q_{\rm fail}=1-p_*,\quad
\partial_k q_{0,+}=\partial_k q_{0,-}=0,\quad
\partial_t(q_{0,+}-q_{0,-})=\gamma p_*A_*\ne0.
\tag{7}
\]
No state, normalization or success-probability singularity occurs. It is an equality of two smooth positive probabilities, stationary in the observation parameter and crossed in time.

The exact source conditions are
\[
{\mathbb E}_*\cos(k_*X)=0,\quad
{\mathbb E}_*X\sin(k_*X)=0,\quad
{\mathbb E}_*X^2\cos(k_*X)=-A_*\ne0.
\tag{8}
\]
Positivity of w, positive success mass and monotonic decrease of mu_2 are compatible with all three. The moment mu_2 is a quadrature second moment, not the kinetic energy.

## 3. What the complete count instrument reveals

For the already defined K_j(t,0), set
\[
\sigma_j(t)=K_j(t,0)\rho_*K_j(t,0)^*,\quad
P_j(t)=\operatorname{Tr}\sigma_j(t),\quad
D_j(t,k)=\operatorname{Tr}\big(\sigma_j(t)\cos(kQ_t)\big).
\tag{9}
\]
D_0=D and P_0=p. These are analytical quantities of the existing complete instrument. For j>0, evaluating the same cosine effects on sigma_j is mathematically well-defined; **the frozen operational contract explicitly supplies the selected no-count readout, not an additional guarantee of physical access to a readout after every nonzero count**. No such access is assumed here. An experimental use requiring it needs an explicit access check and a B01 revision if it changes the contract.

The signed factor v^j in each Kraus amplitude is retained. Its two occurrences in this diagonal trace give v^(2j); counts introduce no spinor multiplicity. Direct trace evaluation gives
\[
\begin{aligned}
P_j(t)&=p(t)\frac{(\gamma t)^j}{j!}\mu_{2j}(t),\\
D_j(t,k)&=\frac{(\gamma t)^j}{j!Z_{1/2}}
 \int_{\mathbb R}v^{2j}e^{\lambda(t)v^2}\Phi(v)\cos(kv)\,dv\\
&=\frac{(-\gamma t)^j}{j!}\partial_k^{2j}D(t,k),\qquad |D_j|\le P_j.
\end{aligned}
\tag{10}
\]
All complete moment integrals are finite. For t>0, P_j>0, and the corresponding normalized trace is
\[
D_j/P_j=(-1)^j\,\partial_k^{2j}C/\mu_{2j}.
\tag{11}
\]
The probabilities P_j are smooth and have no event-specific singularity. Their independence of the queried k does not mean that the full count law carries no information about the source; it means a collision does not make that marginal law singular.

For 0<=s<=1, the positive exponential sum and |cos|<=1 justify the complete generating identity
\[
\boxed{\sum_{j\ge0}s^jD_j(t,k)
=\frac{H_{\lambda(t)+s\gamma t}(k)}{H_{1/2}(0)}.}
\tag{12}
\]
Absolute convergence follows from sum s^j P_j<=sum P_j=1. The same source majorants justify each fixed derivative used in (10). In particular
\[
\sum_{j\ge0}D_j(t,k)=C(0,k),\qquad
\boxed{\partial_t D_0=-D_1/t\quad(t>0).}
\tag{13}
\]
The full count-averaged co-moving cosine trace is constant: the evolving Newman readout resides in the conditioned no-count sector. This does not make the whole unconditioned density operator stationary; off-diagonal coherence can change.

For fixed j and t>0 differentiation also yields
\[
\partial_tD_j=\frac jtD_j-\frac{j+1}{t}D_{j+1},\qquad
\partial_tP_j=\frac jtP_j-\frac{j+1}{t}P_{j+1}.
\tag{14}
\]
No derivative of an unproved infinite series is needed. Define the formal joint-effect probabilities q_j,+/-=(P_j+/-D_j)/2. They obey the same finite-j identities; in particular
\[
\partial_tq_{0,+}=-q_{1,+}/t\le0,\qquad
\partial_tq_{0,-}=-q_{1,-}/t\le0.
\tag{15}
\]
Thus at a double collision equal no-count outcome masses have unequal loss rates:
\[
D_1(t_*,k_*)=-\gamma t_*p_*A_*\ne0.
\tag{16}
\]
The first-count signed trace encodes precisely the curvature responsible for the temporal crossing. This is a useful structural dictionary, not yet an inequality constraining that curvature. At t=0 use the integral limits, e.g. D_1/t -> gamma E_0[X^2 cos(kX)]; do not substitute 0/0. Neither taking t to infinity nor changing gamma is part of this result.

## 4. Local collision shape and failure of zero tracking

Let x=k-k_*, tau=t-t_*, and a_*=D_{kk}(t_*,k_*)=p_*A_* \ne0. Paid finite derivatives and (4) give
\[
D(t_*+\tau,k_*+x)=\frac{a_*}{2}(x^2+2\gamma\tau)
+O(|x|^3+|\tau x|+\tau^2).
\tag{17}
\]
The constants and neighborhood depend on the event and source. This is a local expansion, not a uniform estimate over events or a global assertion that theta has an event.

Putting tau=-s^2 and x=sy reduces the leading equation to y^2=2gamma. The analytic implicit-function theorem at its two simple roots gives, for tau<0,
\[
k_\pm(t)=k_*\pm\sqrt{-2\gamma\tau}+O(|\tau|).
\tag{18}
\]
For tau>0, the same local calculation in the analytic readout continuation gives
\[
z_\pm(t)=k_*\pm i\sqrt{2\gamma\tau}+O(|\tau|).
\tag{19}
\]
Isolation of the double zero and a small fixed complex boundary retain its two local zeros counted with multiplicity. The real roots therefore coalesce and leave the real axis in increasing physical time. Decreasing physical time reverses this picture. Equivalently, the real pair lies on the larger-Newman-lambda side. Any complex readout here is solely analytic continuation.

At a simple real zero r(t), implicit differentiation gives
\[
\dot r=-\gamma\frac{D_{kk}}{D_k}
=\frac{D_1}{tD_k}\quad(t>0).
\tag{20}
\]
Its blowup near the double event belongs to locating the zeros of a smooth readout, not to the state dynamics. The separation squared has leading behavior -8gamma tau+o(|tau|). Changing gamma rescales the clock and does not change the collision location in Newman lambda. The free angular energies and omega cancel from these co-moving readout identities; they do not provide an additional local repulsion term.

For the existing ternary observation Y=+1,-1,0 (success plus, success minus, failure), E Y=D and Var Y=p-D^2. At the event this equals p_*>0. Accordingly a vanishing signed mean has no automatically vanishing sampling noise; this is an exact single-trial variance identity, not a new measurement campaign or a proved optimal sample-complexity bound.

## 5. A source-sector interpretation of the imbalance

For a fixed nonzero real k, put c_+(v)=max(cos(kv),0), c_-(v)=max(-cos(kv),0), and
\[
M_\pm={\mathbb E}_t c_\pm(X)>0,\quad
B_\pm=\frac{{\mathbb E}_t[X^2c_\pm(X)]}{M_\pm},\quad C=M_+-M_-.
\tag{21}
\]
These source sectors are analytical decompositions, not the physical effects (I+/-cos)/2. Their boundaries do not depend on t. Complete moments pay time differentiation despite the k-dependent positive-part definition; no k differentiation through the positive-part corners is used.

Equation (3) gives
\[
\partial_t\log(M_+/M_-)=-\gamma(B_+-B_-).
\tag{22}
\]
At C=0, set M_+=M_-=M. Then
\[
C_{kk}=-M(B_+-B_-),\qquad C_t=-\gamma M(B_+-B_-).
\tag{23}
\]
A collision is therefore not just equal positive and negative cosine mass. It also has the stationary sine-moment balance in (8); its nonzero curvature is a difference of second moments between those cosine sectors. The quadratic attenuation weights different radial locations differently, changing that balance. This source-sector picture and the count-sector picture in §3 express the same signed moments.

The elementary covariance bound
\[
|C_t|\le\gamma\sqrt{(\mu_4-\mu_2^2)
\big({\mathbb E}_t\cos^2(kX)-C^2\big)}
\tag{24}
\]
controls an absolute speed but neither its sign nor the simultaneous conditions C=C_k=0. It follows by Cauchy–Schwarz directly from the same source density. It is a generic diagnostic bound, not a new theta collision-control gain.

## 6. Higher multiplicities and endpoints

The double-event interpretation must not silently cover every possible multiple zero. If D has exact finite spatial order m>=2 at an interior event and b_m=partial_k^m D(t_*,k_*)!=0, repeated use of D_t=gamma D_kk yields the leading finite heat polynomial
\[
D(t_*+\epsilon^2\tau,k_*+\epsilon x)
=\frac{b_m\epsilon^m}{m!}
\sum_{r=0}^{\lfloor m/2\rfloor}
\frac{m!\gamma^r\tau^r x^{m-2r}}{r!(m-2r)!}
+o(\epsilon^m)
\tag{25}
\]
uniformly for (tau,x) in a fixed compact set. A finite multivariate Taylor expansion of sufficiently high total order proves this: every lower parabolic-weight coefficient is a spatial derivative of order below m and vanishes. Its constants depend on m; no infinite-order or all-m estimate is asserted.

For even m=2r, (10) gives D_j=0 for j<r and D_r!=0 at t_*>0. For odd m=2r+1>=3, D_j=0 for j<=r and partial_k D_r!=0. A first-count-only diagnostic does not cover all multiplicities. The state and positive normalization remain regular in these cases as well. Extending any proposed mechanism to every relevant multiplicity is a separate obligation; genericity does not prove that theta has only double collisions.

At t=0 or t=gamma^-1, only the side inside the physical slab is an operational statement. Source analytic continuation can describe a two-sided local germ without licensing a controller outside that slab. Source integrals and (4) retain the one-sided endpoint derivatives already justified in E01.

## 7. Control screen on an actual witness inside this slab

Use the [result index][results], [local-collision summary][local], [control register][controls] and [patterns index][avoid], especially [classification][a01], [re-realization][a03], [normalization][a08] and [scoped exclusions][a07]. The local heat polynomial is a translation of established heat-flow geometry into this realization, not a novel universal collision law or evidence against a theta event.

The [reflected super-Gaussian control, section 4, (9)–(12)][control-source] supplies an exact witness. Write
\[
g(v)=e^{-v^4}+\tfrac12e^{-(v-4)^4}+\tfrac12e^{-(v+4)^4},\qquad
\Phi_*(v)=c e^{-v^2/4}g(v),\quad c>0
\tag{26}
\]
with the source's stated positive normalization. At lambda_*=1/4,
\[
H^*_{1/4}(k)=cF(k)(1+\cos4k),\quad
F(k)=\int_0^\infty e^{-v^4}\cos(kv)dv,
\quad k_*=\pi/4,
\tag{27}
\]
and H^*=H^*_k=0 while H^*_{kk}=16cF(pi/4)>0. The source proves F(k)>=M_0(1-k^2/4)>0 for |k|<2, using M_4=M_0/4, M_2<=M_0/2 and cos y>=1-y^2/2. Thus this witness needs no numerical evaluation.

Its admissibility for the present **generic** square-root/count construction can be checked rather than assumed. Derivatives of each exponential in g are polynomials times that exponential, so |g^(l)/g| is bounded by a fixed polynomial, using the positive mixture weights. The finite square-root recurrence of E01 then bounds each derivative of sqrt(g) by a polynomial times sqrt(g). For |v|>=8, g(v)<=2 exp(-v^4/16). Consequently e^((lambda-1/4)v^2/2)sqrt(g) is Schwartz with every fixed mixed derivative on [-1/2,1/2]; positive compact-slab normalization follows as before. The same complete angular R supplies all required full-spectrum moments. The all-count instrument itself is unchanged.

The witness occurs at physical time t_*=1/(4gamma), strictly inside the contracted interval and in its positive-Newman-lambda half. It has smooth state/success/count probabilities, the covariance law, the nonzero D_1 curvature signal and complete-count conservation, yet it collides. It fails the canonical integer-square arithmetic source and canonical theta tail formula, while its own super-Gaussian tails pay the generic domain obligations. **This rules out collision exclusion from these generic properties alone on a range containing this witness.** It does not rule out source-sensitive estimates using the unchanged theta source.

| Other recorded family | Limitation of the present screen |
| --- | --- |
| Euler-factor | Fails the unchanged canonical arithmetic source. Applicable generic filtering/cosine laws survive; no new event computation or full square-root-domain audit of this family is claimed here. |
| Weighted-square / finite-prime | Complete unit coefficients or full canonical reflection fail. Finite endpoint matches do not supply the smooth full-line domain assumptions. |
| Smooth shape / positive primitive | Fails exact theta arithmetic. Generic positivity and applicable source identities are not separating; no new family-specific preparation proof is asserted. |
| Atomic / nonsmooth finite profile | Fourier moments can exist while the present smooth full-line square-root preparation fails. These are not silently realized by the same smooth-state proof. |

## 8. What is promising, and what remains to be found

**Promising for further conceptual work:** the realization separates three objects that can otherwise be conflated: a regular conditional state, a signed readout that develops a multiple zero, and count-sector signed moments that govern that development. In particular (13), (16) and (23) make the collision's dynamical content explicit. This is a reason to examine mechanisms before committing to a particular norm or bound.

**No gain has yet been demonstrated over direct source analysis.** Equations (3), (10), (12), (17) and (23) are all available by differentiating/reweighting the same supplied source. The count labels organize existing weighted moments; they are not independent arithmetic information. Complete-count conservation and decreasing mu_2 do not themselves prevent the control witness. The divergence of a zero velocity is not a hidden singularity or forbidden state transition. Positivity and complete positivity alone leave the signed cancellation unconstrained.

The broadened B02 question is whether an independently justified feature of the **canonical source within this unchanged dynamics** constrains these joint balances or their transport. Two connected viewpoints are available for later comparison: source-sector balance/covariance and count-sector signed-moment transfer. Neither is selected as a follow-up proof target in this return. A useful mechanism could be a source-specific relation, invariant or transport restriction, and need not initially be expressed as one numerical bound. It must eventually name its noncircular premise, exact parameter/height/multiplicity scope, what the relevant controls fail, and the advantage or explanatory consequence relative to direct analysis of the same source.

Merely requiring that C and C_k never vanish together restates collision exclusion. An all-event criterion must be classified against the repository's existing equivalences, including their endpoint and confinement hypotheses; it is not counted as an intermediate gain by giving it a physical name. A higher-order moment hierarchy without a closure or improved estimate is likewise not an automatic advance.

**Author-directed planning decision:** broaden the overview and progress goals to include collision anatomy and mechanisms for collision control, retain quantitative estimates as a complementary objective, and place mechanism discovery before any forced target selection. Preserve the E01/E02 construction and status. The new [plan r2][plan] supersedes only the future B02 framing and corresponding unissued E03 deliverable; plan r1 remains historical and immutable E01 records remain untouched.

## 9. Verification and stopping boundary

One analytical reconnaissance and one local consistency pass were used. The latter checked the laboratory/Newman sign reversal, factors Z=2H(0), normalization subtraction, t and gamma powers in every count identity, the absolute convergence of the complete count sum, the double-event Taylor coefficient, higher-order parabolic coefficients, endpoint restrictions, and the explicit control's square-root domain and witness location. These are author-side checks by the same assistant, not E02, independent review or a new accepted theorem.

The source-use scope is E01 sections 3–6, E02 sections 2–6, and the control's section 4, (9)–(12), inspected directly. Established heat-flow geometry is credited through [summary 13][local]; the needed local formulas are derived above. No new literature theorem, external article or PDF, numerical experiment, manuscript, controller, physical access assumption or E03 execution was introduced. New identities retain proof-author/diagnostic status pending any separately selected assessment.

**Next: [B] TND-D-B02 — Astra**, continue mechanism discovery/comparison when selected by the author; no particular follow-up target has been chosen. E03 remains reserved.

[inputs]: ../research-progress/handoffs/05_TND_D_B02_R2_COLLISION_INPUTS_20261106.json
[progress]: ../research-progress/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_PROGRESS_20261105.md
[plan]: ../research-plan/02_DIRECT_NEWMAN_REALIZATION_RESEARCH_PLAN_R2_20261106.md
[e01]: 02_TND_D_E01_R1_CONDITIONAL_QUADRATURE_REALIZATION_20261106.md
[e02]: ../reviews/01_TND_D_E02_CONDITIONAL_REALIZATION_ASSESSMENT_20261106.md
[shared]: ../../reviews/01_TND_E03_R2_GEOMETRY_SOURCE_AND_TRANSPORT_ASSESSMENT_20261106.md
[results]: ../../../../../result-summaries/README.md
[local]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../avoid/08_normalization_and_constant_slips.md
[control-source]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/04_REFLECTION_POSITIVE_SOURCE_COLLISION_AND_MIXED_SECTORS_20261015.md
