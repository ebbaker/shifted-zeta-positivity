# J-B05 initial evaluation: a separated-node obstruction at order four

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Contributing worker `/root/branch01`, actual recorded **gpt-6-astra (Codex), effort ultra**, inherited from the coordinator and confirmed in this worker's `turn_context`. Worker runtime identity `01a1999e-ddf1-7b53-9cb2-6093be5e10f0`; parent research-chat identity `01a1999e-49d4-7a52-9e8a-95b0c5c430f1`. The coordinator alone captures the parent chat and edits shared records. This return is internal same-model research with inherited source premises, not independent specialist review.

**Task:** J-B05, B — conceptual evaluation under [Note15](../../notes/15_CONTINUATION_PARALLEL_BRANCH_EVALUATION_20261101.md). **Disposition: the proposed full coordinatewise monotonicity of the unchanged canonical h4 is contradicted.** The bounded evaluation is complete. Its conditional signed-averaging transfer remains valid, but its order-four hypothesis fails at separated nodes.

The precise new finding is:

> Fix three distinct source coordinates in the interval where the accepted origin curvature is negative. As the fourth source coordinate tends to infinity, its partial derivative of h4 is eventually negative.

This is not a negative determinant, a failure of averaged index monotonicity, or an obstruction to every signed-averaging argument. The accepted order-three result and the negative origin C are both used without alteration. No new coefficient range or RH claim results.

## 1. Fixed objects and the actual question

Retain the full physical-time-zero canonical source
\[
\Phi(u)=e^u\sum_{n\ge1}P_0(n^2t)e^{-n^2t},\qquad
P_0(t)=2t^2-3t,\quad t=\pi e^{4u}.
\]
The conventions are
\[
c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du,\quad
c_n=0\ (n<0),\quad \gamma_n=n!c_n,
\]
\[
D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1},\qquad
F_{r,k}=\prod_{j=0}^{r-1}(2k+2j)!.
\]
By the [accepted Review01](../../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md), R=Phi''/Phi is strictly increasing on u>0 and the order-three signed-averaging comparison is established at its recorded internal-review scope. Write I=R((0,infinity)), x=R(u),
\[
f(x)=g_2(x)=\frac{\Phi^{(4)}(u)}{\Phi(u)},\qquad
 g(x)=g_3(x)=\frac{\Phi^{(6)}(u)}{\Phi(u)}.
\]
The unchanged four-node observable is
\[
h_4(x_1,x_2,x_3,x_4)=
\frac{\det[1;x_j;f(x_j);g(x_j)]}{V(x_1,x_2,x_3,x_4)}.       \tag{1}
\]
For increasing nodes the determinant orientation is as displayed. It is symmetric after division by V. Since R'>0, coordinatewise increase in the source variables u is equivalent to coordinatewise increase in x.

[Note14](../../notes/14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md) gives the positive density
\[
w_{4,k}=\Big(\prod_{j=1}^4u_j^{2k}\Phi(u_j)\Big)
 V(\mathbf u^2)V(R(\mathbf u)),\quad Z_{4,k}=\int_{\Omega_4}w_{4,k},
\quad A_{4,k}=F_{4,k}D_{4,k}/Z_{4,k}=\mathbb E_{4,k}h_4.
\]
The coordinatewise monotonicity candidate is a sufficient fixed-order condition, not an RH-equivalent criterion. The exact derivative test below is merely a reformulation of this candidate; the substantive gain is proving that it fails for the actual canonical source.

## 2. Exact separated-node formula

For three fixed distinct nodes a<b<c in I, let f[a,b,c] denote the ordinary second divided difference and p_f the quadratic interpolant to f on these nodes. Put
\[
\alpha=f[a,b,c],\quad\beta=g[a,b,c],\quad
Q(x)=(x-a)(x-b)(x-c).
\]
Subtract the Newton interpolation columns in the determinant (1). The first two rows reduce to the first two Newton basis vectors, leaving the two-by-two determinant
\[
\boxed{h_4(a,b,c,x)=\alpha g[a,b,c,x]-\beta f[a,b,c,x].}    \tag{2}
\]
Equivalently,
\[
f[a,b,c,x]=\frac{f(x)-p_f(x)}{Q(x)},\qquad
 g[a,b,c,x]=\frac{g(x)-p_g(x)}{Q(x)}.                       \tag{3}
\]
These identities can be verified directly by multiplying by V; no positivity theorem is imported. They extend across coincidences by continuity.

Differentiating a divided difference in its last argument adds a repeated copy of that argument. For completeness, this follows by subtracting the two order-three differences with last nodes x and y, dividing by y-x, and letting y tend to x. Therefore
\[
\partial_x h_4(a,b,c,x)=
\alpha g[a,b,c,x,x]-\beta f[a,b,c,x,x].                    \tag{4}
\]
Nonnegativity of (4) for every triple and every fourth node is the full separated-node requirement. It contains information absent from the coincident-node test.

At a completely coincident tuple, (4) has limit
\[
\partial_{x_4}h_4(x,x,x,x)=
\frac{f''(x)g''''(x)-g''(x)f''''(x)}{2!4!}.
\]
Multiplying by four gives Note14's derivative along the diagonal, with denominator 12. Thus the normalization of the confluent limit agrees. A diagonal sign cannot decide (4) when three nodes remain near the origin and the fourth escapes to the tail.

## 3. A finite tail calculation, with its derivative paid

The predeclared finite calculation is the recurrence
\[
P_{j+1}=4tP_j'+(1-4t)P_j,\qquad 0\le j\le6,               \tag{5}
\]
generating only P0 through P7. Its purpose is to identify the first two powers of Phi^(2m)/Phi for m=1,2,3 and control one derivative of their remainders. There is no coefficient scan, quadrature, numerical source sampling, or derivative escalation.

Exact integer recurrence, followed by rational division by P0, gives
\[
\begin{aligned}
q_2(t):=\Phi''/\Phi&=16t^2-88t+O(1),\\
q_4(t):=\Phi^{(4)}/\Phi&=256t^4-3840t^3+O(t^2),\\
q_6(t):=\Phi^{(6)}/\Phi&=4096t^6-116736t^5+O(t^4).        \tag{6}
\end{aligned}
\]
Here and below these are asymptotics of the **full source**. One quick exact check of the coefficients is that the leading coefficient of Pj is 2(-4)^j, while the next coefficient satisfies B_(j+1)=(4j+9)2(-4)^j-4B_j. Consequently the top two coefficients of Pj/P0 are
\[
(-4)^j,\qquad -\frac{j(2j+7)}4(-4)^j.
\]
The finite check returned (16,-88), (256,-3840), and (4096,-116736); its tiny [program](../numerics/j_b05_tail_check.py) and [record](../numerics/J_B05_TAIL_CHECK_20261101.json) retain the exact inputs and outputs.

Here is why the errors in (6) can be differentiated in the manner actually needed. For Mj the absolute coefficient sum of Pj and
\[
B_j^*=\sum_{n\ge2}n^{2j+4}e^{-(n^2-4)}<\infty,
\]
the omitted differentiated source sum satisfies, for t>=1,
\[
|E_j(u)|\le e^u M_j B_j^* t^{j+2}e^{-4t},\qquad 0\le j\le7. \tag{7}
\]
The summable dominating sequence also justifies the differentiations. This is precisely the finite differentiated-tail framework in [Return03, Section 6](../../notes/03_J_E01_R1_REPRESENTATION_AND_ENDPOINT_TAIL_RETURN_20261101.md), with the already available seventh derivative and explicit common bounds in [Note09, Section 3](../../notes/09_J_B02_GLOBAL_TAIL_AND_COMPACT_CERTIFICATE_20261101.md). For t>=3 the positive denominator obeys Phi>=e^u t²e^-t. Hence
\[
q_j=P_j/P_0+O(t^j e^{-3t}),\qquad
\frac{dq_j}{dt}=
\frac{q_{j+1}-q_1q_j}{4t}
=\frac d{dt}(P_j/P_0)+O(t^j e^{-3t}),\quad j\le6.          \tag{8}
\]
The derivative error is derived using E_(j+1), rather than obtained by formally differentiating a big-O statement. The rational functions Pj/P0 have convergent Laurent expansions for t>3/2. Their finite Laurent remainders and first derivatives have the corresponding algebraic bounds. In particular x=q2(t) has dx/dt=32t-88+O(t^-2)+O(t²e^-3t), and its inverse satisfies
\[
t=\frac{\sqrt x}{4}+\frac{11}{4}+O(x^{-1/2}).             \tag{9}
\]
The inverse derivative is obtained from 1/(dx/dt); its denominator is bounded below by a positive multiple of t eventually. Substitution in (6), using (8) for the derivatives, now gives the paired expansions
\[
\begin{aligned}
f(x)&=x^2-16x^{3/2}+O(x),& f'(x)&=2x-24x^{1/2}+O(1),\\
g(x)&=x^3-48x^{5/2}+O(x^2),&g'(x)&=3x^2-120x^{3/2}+O(x).
\end{aligned}                                                        \tag{10}
\]
For example q4-q2² has leading term -1024t³, and q6-q2³ has leading term -49152t⁵. Dividing by x^(3/2)~64t³ and x^(5/2)~1024t⁵ gives -16 and -48, respectively. These joint subtractions are performed before estimating remainders. All constants in the following O bounds may depend on the fixed a,b,c.

Equations (3) and (10), with the fixed quadratic interpolants retained, imply
\[
\begin{aligned}
g[a,b,c,x]&=1-48x^{-1/2}+O(x^{-1}),\\
\frac d{dx}g[a,b,c,x]&=24x^{-3/2}+O(x^{-2}),              \tag{11}\\
f[a,b,c,x]&=O(x^{-1}),\qquad
\frac d{dx}f[a,b,c,x]=O(x^{-2}).                         \tag{12}
\end{aligned}
\]
The leading coefficient in (12) is generally 1-alpha, not 1: the interpolant p_f has leading coefficient alpha. This does not affect its lower asymptotic order. Equations (11)–(12) follow by differentiating the explicit quotient (3) and using both columns of (10); no unspecified remainder is differentiated. In (11), subtracting the quadratic p_g changes only the O(x^-1) term and its O(x^-2) derivative.

## 4. The actual canonical obstruction

The accepted origin calculation gives C<0 on some open interval 0<u<epsilon and R'>0 there. Thus
\[
f''(R(u))=\frac{C(u)}{R'(u)^3}<0.                        \tag{13}
\]
Choose any three distinct a<b<c in the image of that interval. Strict concavity gives
\[
\alpha=f[a,b,c]<0.                                      \tag{14}
\]
For example, the elementary divided-difference mean-value theorem follows by applying Rolle's theorem twice to f minus its quadratic interpolant and gives alpha=f''(xi)/2 for some xi in (a,c). This supplies the strict sign without acquiring a new source value or assuming an uncomputed sign of g.

Combine (2), (11), and (12):
\[
\boxed{\partial_x h_4(a,b,c,x)
=24\alpha x^{-3/2}+O(x^{-2})<0\quad\text{for all sufficiently large }x.} \tag{15}
\]
The leading coefficient is strictly negative; beta is finite and contributes only O(x^-2). Since R(u) tends to infinity and R'(u)>0, (15) is also a negative derivative with respect to the fourth source variable u4. All four nodes are strictly ordered and interior. By continuity, each sufficiently large such tuple has a neighborhood with the same negative derivative.

This proves failure of full coordinatewise monotonicity for the unchanged h4. It also shows h4 tends to the negative limit alpha along these configurations, but the latter observation is not the main argument: signed averaging already allows negative h. The decisive fact is the negative derivative.

No effective value of epsilon or tail cutoff is required to refute a universally quantified monotonicity statement. The proof is existential with strict asymptotic separation. A numeric counterexample is unnecessary, and no such search was run.

## 5. What this does and does not settle

Had h4 been coordinatewise increasing, the inherited association argument would give
\[
A_{4,k+\ell}\ge A_{4,k}\ge A_{4,0}
=\frac{0!2!4!6!\,c_0^4}{Z_{4,0}}
=\frac{34560c_0^4}{Z_{4,0}}>0
\]
for every finite k,ell>=0. This includes all small k, without using large-index asymptotics. Equation (15) prevents this particular sufficient proof from extending to order four. It does **not** prove that Cov_(4,k)(h4,(product u_j)^(2ell)) is negative or that A4,k is nonmonotone. A local negative derivative cannot be substituted for the sign of the full covariance.

The positive triangular k=0 anchor is preserved. The order-three source pair R'>0,K>0 is preserved. Known order-four positivity is preserved. No all-order or small-index positivity problem is solved here. Increasing r requires a different sign mechanism or a weaker signed integral estimate; it cannot be justified by assuming this exact h_r is coordinatewise increasing for every r, because that sequence of hypotheses already fails at r=4.

The domain and regularity obligations are explicit:

- At separated nodes a direct first partial derivative of h4 uses source derivatives through Phi^(7). This proof uses only that order and the inherited negative-curvature result.
- A completely confluent first partial derivative requires g3'''' and therefore source derivatives through order ten at u>0. At the endpoint, using z=u² and the analytic inverse of Rhat(z), the corresponding fourth x derivative can require Phi^(14)(0). Those are requirements of an attempted global confluent test, **not acquisitions performed or recommended here**. Rhat'(0)>0 is inherited, so the regular endpoint coordinate is available.
- The order-four integral identity retains the endpoint terms from integration by parts through Phi^(6); full evenness makes the needed odd values Phi'(0), Phi'''(0), Phi^(5)(0) vanish. A finitely truncated theta sum cannot replace this full-source fact.
- The divided differences have their usual removable collision limits. Compact regularity and full theta tails ensure the signed integrals and every fixed polynomial index tilt are absolutely integrable, as in Note14. Neither coincidence faces nor infinity have been omitted from the target; the contradiction specifically uses a mixed origin/tail configuration.
- The constants in (15) depend on the fixed triple. This is sufficient for the negative result; no uniform growing-order claim is made.

## 6. Control screen and evidence status

The [result index](../../../../../../result-summaries/README.md), its [control cluster](../../../../../../result-summaries/12_collision_controls_and_screening.md) and [theta cluster](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and the [avoid index](../../../../../../avoid/README.md) govern this assessment. In particular retain [target classification](../../../../../../avoid/01_restating_the_target.md), [shape-only controls](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [same-model limitations](../../../../../../avoid/05_same_model_reviews_and_shared_premises.md), [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [no campaign before a question](../../../../../../avoid/10_numerics_ahead_of_the_question.md), and [joint signed estimates](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

| Control | Actual premise screened; no uncomputed signs assigned |
| --- | --- |
| Gaussian exp(-a u²) | The source ratios are monic polynomials of degree i in R, so h4=1. It fails the negative-curvature premise (13) and has a different tail from (10). It checks orientation and the equality case, not theta monotonicity. |
| Euler-factor sources | They fail the unchanged canonical expansion used for (6)–(10). Positivity/evenness alone does not imply either the candidate monotonicity or this canonical obstruction. No signs of their f'' or h4 derivatives are asserted. |
| Weighted-square and finite-prime perturbations | Altered weights fail canonical reconstruction. Finite endpoint matching cannot replace all odd endpoint cancellations when order grows; at order four the three named odd endpoints must be checked. Their particular endpoint signs are not assumed. |
| Reflected super-Gaussian, smooth shape, and positive-primitive controls | Reflection may supply endpoint parity, but not the canonical quantitative tail coefficients or (13). They fail the exact canonical source premise; no h4 sign has been computed for them. |
| Positive-time collision controls | No positive-time collision is used as a counterexample to a time-zero finite-order statement. The counterexample configuration in (15) belongs to the canonical source itself. |

**Established in this note:** the exact interpolation/derivative formulas and the canonical separated-node failure of full h4 coordinatewise monotonicity. **Conditional facts retained:** the higher-order FKG transfer if its hypotheses hold. **Unresolved:** any weaker integrated covariance comparison, full neighboring-index balance, and arbitrary-order/small-index positivity mechanism. No new literature theorem is imported; Newton interpolation, Rolle's theorem, the finite polynomial recurrence and the existing paid theta tail suffice. Existing FKG imports are not re-certified by this return.

## 7. One bounded next action

**Next: [B] J-B05 follow-up — Astra, deferred pending the coordinator's cross-branch priority decision.** Select and assess one *integrated* r=4, k=0 to k=1 covariance estimate that explicitly allows the negative-derivative mixed-node region in (15). The output must be a concrete theta-dependent bound for the complete covariance, with full tails and the positive anchor retained, or a precise failed comparison. A local monotonicity surrogate or the restated condition Cov>=0 is not a gain. Stop if the proposed estimate needs an unproved sign equivalent to that same covariance; do not launch a derivative scan or numerical campaign. The finite pilot would test a new estimating mechanism, not establish a previously unknown order-four coefficient range. There is presently no fixed numerical E contract.

## 8. Input versions and provenance

The worker read the root research/large-file/chat-history instructions, the Note15 packet, the branch brief, Note14, the signed-averaging Note05, relevant origin/tail passages of Returns03/07 and Note09, accepted Review01, the ideas index, live register, and the relevant result/avoid entries. Historical files were read only. No shared navigation, chat registry, certificate, prior note or review was edited. Input hashes below identify the decisive mathematical versions, not proof validity.

| Input | SHA-256 |
| --- | --- |
| 15_CONTINUATION_PARALLEL_BRANCH_EVALUATION_20261101.md | `2d2fd23efd67b019c484ec551f779f1feaf4ffe08046ba457de6d5a3b1ec1f1a` |
| README.md | `ab7b77a4b2b12f3759cd7edd42c8d14502710d5128f24bb57dd179843523861b` |
| 14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md | `d8b9160e158317462d75a59d7535f500898cfb51345284d33287cf24eafd14f0` |
| 05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md | `32f8289741bac117b45399855558b554e1f1430adc7169a8229bfd69448e3cf2` |
| 03_J_E01_R1_REPRESENTATION_AND_ENDPOINT_TAIL_RETURN_20261101.md | `23ce0fa4b4b4553e5775b045724fe3e99676fa495dab22e578f942e6a2bb3875` |
| 07_J_E01_R2_SIGNED_AVERAGING_AND_Q10_P7_RETURN_20261101.md | `202a37845f602efd56c8d11935cb8256c665edbaaae421b1b2fed14c186e97d2` |
| 09_J_B02_GLOBAL_TAIL_AND_COMPACT_CERTIFICATE_20261101.md | `0fb3a7dd974cd858dd0941e6b89863aaaea9f8a62ee172d37de27bd7970cb5a9` |
| 01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md | `c13e63e7c017285932e75d2add333b8d683e5ed3b9a096f6e20e31e88e0a2dfe` |
