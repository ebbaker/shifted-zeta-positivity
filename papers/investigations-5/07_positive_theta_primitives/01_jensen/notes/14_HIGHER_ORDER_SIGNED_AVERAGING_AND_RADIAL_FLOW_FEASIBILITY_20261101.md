# Higher order signed averaging and radial flow feasibility

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**.

**J-B03 complete as a bounded conceptual assessment.** This note explains the increasing-order and small-index obligations and evaluates the author's suggestion that a conservative flow might asymptotically remove the negative part of a determinant integrand. The exact identities and scoped comparisons below have same-assistant analytical checking only. There is no new canonical higher-order sign certificate, numerical campaign, independent review, or RH conclusion. The accepted J-B01–J-E03 result remains unchanged.

The suggestion has a precise sufficient formulation: conserve the desired determinant integral while proving that its total negative mass tends to zero. Pure invertible transport cannot achieve this from a sign-changing integrand; it preserves negative mass. Ordinary heat can reduce negative mass, but its limiting negative mass is exactly the negative part of the unknown conserved integral. A theta-specific estimate controlling that decay, with global existence and boundary accounting, is therefore the missing mathematical input. This does not exclude finding that estimate using a deformation.

| Next question | Type and recommended model | Readiness | Required output |
| --- | --- | --- | --- |
| J-B04: choose a conservative determinant flow and test a theta-specific negative-mass dissipation estimate | B — Astra; the generator and coercive estimate remain conceptual choices | Proposed, not started; depends on this assessment | For the mechanism pilot r=4, k=1, one explicit source-based flow, complete conservation/existence assumptions, and a proved estimate, precise failed premise, or bounded execution contract. Positivity at this order is already in the baseline; a pilot must test a mechanism, not claim a new coefficient range. |

Read with [the accepted review][review], [the signed averaging note][averaging], [the result index][results], especially [theta identities][theta] and [controls][controls], and [the avoid index][avoid], especially [target classification][target], [shape premises][shape], [coordinate changes][coordinates], and [scoped conclusions][scopes].

## 1 The two indices and the complete target

At physical heat time zero put
\[
b_n=\int_0^\infty u^{2n}\Phi(u)\,du,\qquad
c_n=\frac{b_n}{(2n)!},\qquad \gamma_n=n!c_n,
\]
\[
J^{d,n}(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}X^j,
\qquad D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1},
\quad c_j=0\ (j<0).                                      \tag{1}
\]
The degree d and shift n of a Jensen polynomial are different parameters from the size r and starting index k of a Toeplitz minor. In particular, the triangular identity D_{r,0}=c_0^r says nothing by itself about all-degree hyperbolicity at Jensen shift n=0.

The complete Jensen criterion requires every d,n. All d at n=0 suffice because
\[
\partial_X^nJ^{d+n,0}(X)=\frac{(d+n)!}{d!}J^{d,n}(X),        \tag{2}
\]
and derivatives preserve real-rootedness. The classical eventual theorem has quantifiers for each fixed d, all n sufficiently large depending on d. It leaves fixed small n with unbounded d. These are the introduction and Theorem 1 of [Griffin–Ono–Rolen–Zagier, version 1][gorz]; they are background, not a new criterion or estimate.

There is also a useful precise strict-minor bridge: [Katkova, Section 2, Lemma 3][katkova] states that a positive summable sequence belongs to PF_m if, for each 1<=r<=m, all r-column consecutive minors of its first r Toeplitz rows are strictly positive. These are exactly D_{r,k}, k>=0. Here c_n>0 and sum c_n=F(1)<infinity, with F(w)=sum c_n w^n entire. Thus proving strict D_{r,k}>0 for every r,k would supply the full coefficient criterion. The lemma's statement and hypotheses were rechecked; its cited original proof was not independently audited. Merely nonnegative consecutive minors do not automatically meet this strict lemma.

An all-order proof need not have a single numerical constant uniform in r. A theorem valid for each arbitrary finite r, with explicit r-dependent constants, would suffice. A finite list of verified orders would not.

## 2 The all-order integral is already available

Write Omega_r={0<u_1<...<u_r}, V(y)=prod_{a<b}(y_b-y_a), and
\[
\Delta_r(\mathbf u)=\det[\Phi^{(2i)}(u_j)]_{i=0,\ldots,r-1;\,j=1,\ldots,r},
\qquad F_{r,k}=\prod_{j=0}^{r-1}(2k+2j)!.
\]
The audited representation in [Note01][representation] is
\[
M_{r,k}:=F_{r,k}D_{r,k}
=\int_{\Omega_r}\Big(\prod_j u_j^{2k}\Big)
 V(\mathbf u^2)\Delta_r(\mathbf u)\,d\mathbf u.              \tag{3}
\]
Every factor outside Delta_r is positive in the ordered interior. The sign-bearing expression is the full derivative determinant, not the positive theta source alone.

The endpoint identity behind (3) is
\[
\int_0^\infty\frac{u^{2m}}{(2m)!}\Phi^{(2i)}(u)\,du=c_{m-i}.
                                                                    \tag{4}
\]
For m<i, integration by parts leaves -Phi^{(2i-2m-1)}(0), which vanishes by full evenness. Increasing r therefore invokes an increasing family of endpoint cancellations. A source flow that preserves only the first odd endpoint is not enough.

Large k increasingly suppresses a fixed neighborhood of u=0 relative to larger nodes. At small k that particular suppression is absent; the signed integral must be estimated as a whole. Increasing r also increases the derivative order, the number of mixed terms, and the node-collision faces. This is why a fixed-order tail argument does not automatically handle the missing regime.

The first small-index family after the trivial anchor is already substantial. Set e_r=D_{r,1}/c_0^r and e_0=1. Expansion of the upper Hessenberg determinant gives
\[
e_r=\sum_{j=1}^r(-1)^{j-1}\frac{c_j}{c_0}e_{r-j},\qquad
\sum_{r\ge0}e_r z^r=\frac{c_0}{F(-z)}                       \tag{5}
\]
as a formal power-series identity near zero. Thus k=1 with unbounded r already encodes an infinite reciprocal-coefficient sign problem. Equation (5) is explanatory algebra, not a new positivity criterion.

## 3 Two possible forms of a higher-order argument

### Extending signed averaging

Use the accepted R=Phi''/Phi with R'>0. Put x_j=R(u_j), and define
\[
g_i(x)=\left.\frac{\Phi^{(2i)}}{\Phi}\right|_{u=R^{-1}(x)},
\qquad g_0=1,\quad g_1=x,
\]
\[
h_r(\mathbf u)=\frac{\det[g_i(x_j)]_{i=0}^{r-1}}{V(\mathbf x)},
\quad w_{r,k}=\Big(\prod_j u_j^{2k}\Phi(u_j)\Big)
 V(\mathbf u^2)V(R(\mathbf u)),
\]
\[
Z_{r,k}=\int_{\Omega_r}w_{r,k},\quad
A_{r,k}=\frac{F_{r,k}D_{r,k}}{Z_{r,k}}=\mathbb E_{r,k}h_r.    \tag{6}
\]
The alternating numerator divided by the Vandermonde has removable coincident-node limits. All the displayed integrals are finite for each finite r,k: R grows at most exponentially in u, while theta and each fixed derivative have double-exponential decay; w|h| reduces to the absolute integrand of (3).

The pairwise lattice argument in Note05 works for any finite number of nodes: each Vandermonde contributes a product of factors f(u_j)-f(u_i) for increasing f, each satisfying the same meet/join inequality. Thus the finite-grid FKG argument and exhaustion extend, provided the required observable is increasing and the integrals are finite. With q_l=(prod_j u_j)^{2l}, the exact identity is
\[
A_{r,k+l}-A_{r,k}
=\frac{\operatorname{Cov}_{r,k}(h_r,q_l)}{\mathbb E_{r,k}q_l}.
                                                                    \tag{7}
\]
Consequently coordinatewise monotonicity of h_r would give
\[
A_{r,k}\ge A_{r,0}=\frac{F_{r,0}c_0^r}{Z_{r,0}}>0,           \tag{8}
\]
including every small k. The new unpaid hypothesis is monotonicity of h_r for higher r. It is sufficient, potentially stronger than needed, and is not asserted to be RH-equivalent or true for canonical theta.

At r=3, h_3 is the second divided difference of g_2. The accepted K>0 gives g_2'''>0 and hence its coordinatewise increase. At r=4 a new function g_3=Phi^{(6)}/Phi enters. On the coincident-node diagonal,
\[
h_4(x,x,x,x)=\frac{g_2''g_3'''-g_2'''g_3''}{12},\qquad
\frac d{dx}h_4(x,x,x,x)
=\frac{g_2''g_3''''-g_2''''g_3''}{12}.                     \tag{9}
\]
Here primes are x derivatives. The confluent formulas follow by Taylor expansion of the determinant and division by V. Nonnegativity of the last expression is necessary for coordinatewise monotonicity, but not sufficient for all separated configurations. The old sign g_2'''>0 does not settle it. No new source-derivative acquisition or sign computation is performed here.

### Raising order through adjacent determinants

The Desnanot–Jacobi identity for the (r+1)-square Toeplitz block gives
\[
D_{r+1,k}D_{r-1,k}=D_{r,k}^2-D_{r,k-1}D_{r,k+1}.            \tag{10}
\]
Thus, when D_{r-1,k}>0, strict log-concavity of the rth determinant sequence in k proves positivity at order r+1. Mere increase of A_{r,k} does not imply this second-difference inequality.

For k>=1, substituting (6) yields the exact comparison
\[
\frac{D_{r,k}^2}{D_{r,k-1}D_{r,k+1}}
=\frac{A_{r,k}^2}{A_{r,k-1}A_{r,k+1}}
 \frac{Z_{r,k}^2}{Z_{r,k-1}Z_{r,k+1}}
 \frac{F_{r,k-1}F_{r,k+1}}{F_{r,k}^2}.                     \tag{11}
\]
Z is a moment sequence in prod u_j^2 and hence log-convex by Cauchy–Schwarz. The factorial factor favors the opposite direction. A proof must control the full balance, including the A factor, rather than infer it from A's monotonicity. Equations (7) and (10) expose alternative proof obligations, not two completed higher-order mechanisms.

## 4 Giving the proposed flow an exact positivity target

The object to make nonnegative is an integrand for a determinant or an equivalent positivity test. Nonnegativity of an integral representation of the Jensen polynomial as a function of X is not itself hyperbolicity: a polynomial with simple real roots changes sign between them.

Suppose, for each specified r,k, a real density f_s on a domain has
\[
\int f_s=M_{r,k},\qquad f_s^-=\max(-f_s,0),\qquad
N_{r,k}(s)=\int f_s^-.                                    \tag{12}
\]
The hypothesis
\[
N_{r,k}(s)\longrightarrow0                                \tag{13}
\]
implies M_{r,k}>=0, because M=integral f_s^+-N(s)>=-N(s). This is enough to establish nonnegativity of that determinant. To use the strict-minor bridge, add strict positivity: for example a lower bound integral f_s^+>=delta_{r,k}>0 at arbitrarily large s. Alternatively, a valid index comparison can transfer a strictly positive anchor.

L1 convergence to a nonnegative density is sufficient for (13), but is stronger than needed. Pointwise convergence to zero is insufficient; mass can spread or escape. Even eventual pointwise positivity on each fixed compact set needs global control of the remaining negative mass. Moving positive and negative regions must both be included.

A concrete sufficient estimate would be
\[
N'_{r,k}(s)\le-\lambda_{r,k}(s)N_{r,k}(s),\qquad
\int_0^\infty\lambda_{r,k}(s)\,ds=\infty.                  \tag{14}
\]
It would give N(s)<=N(0)exp(-integral_0^s lambda). The rate need not be constant or independent of r,k. What matters is a proof for arbitrary finite orders and the missing small indices from known source information. This is a proposed sufficient estimate, not an acquired bound.

For scalar heat with diffusivity epsilon, at regular zero levels and with sufficient integrability and vanishing boundary flux, integration by parts gives the negative-part dissipation formula
\[
N'(s)=-\varepsilon\int_{\{f_s=0\}}|\nabla f_s|\,dS.        \tag{15}
\]
Smooth convex approximations give the corresponding weak formulation when a zero level is singular. Contraction alone gives N'<=0. To obtain (14), one must bound the interface dissipation below by lambda N. That is a specific coercivity question about the evolved theta determinant density. No such inequality is proved here.

## 5 How the three-dimensional tools apply

### Exact lift and conservation

For spatial X in R^3 let R_X=|X| and u_X=(log R_X)/2, and set
\[
\rho_0(X)=\mathbf1_{R_X\ge1}\frac{\Phi(u_X)}{8\pi R_X^3}.
\]
The spherical Jacobian gives integral rho_0(X)a(u_X)dX=integral_0^infty Phi(u)a(u)du. One exact lift of (3) to (R^3)^r is
\[
f_{r,k}(X_1,\ldots,X_r)
=\frac1{r!}\Big(\prod_j u_j^{2k}\rho_0(X_j)\Big)
 V(\mathbf u^2)
 \det\left[\frac{\Phi^{(2i)}(u_j)}{\Phi(u_j)}\right]_{i,j}.  \tag{16}
\]
It is zero if any R_j<1. The two alternating factors make the product symmetric; the 1/r! converts the full orthant to the ordered chamber. Its integral is exactly M_{r,k}, and all its finite spatial absolute moments exist.

Thus [Investigation05 Note25][heat] supplies a direct template: evolve the complete signed density by a conservative equation on the full space,
\[
\partial_s f_s+\operatorname{div}J_s=0.                   \tag{17}
\]
For example independent three-dimensional heat in each copy is heat on R^{3r}. At higher order the target couples r source points; dimension three of the original lift does not eliminate that coupling. Radial symmetry can reduce evaluation, but not the determinant's order dependence.

This is different from smoothing Phi alone and then inserting the new source into the old determinant formula. The latter generally changes the coefficients. If source and test are evolved separately, the sufficient duality relation is
\[
\partial_s\rho_s=L_s^*\rho_s,\qquad
\partial_s p_s=-L_sp_s,\qquad
\frac d{ds}\int\rho_sp_s=0,                              \tag{18}
\]
with all boundary terms zero or retained. Backward test evolution requires its own existence and bounds; (18) is an identity under those assumptions, not an existence theorem. The [Darboux family][darboux] provides a concrete source-and-test example of this principle.

### What the old flow families can and cannot supply

| Family | Consequence for the proposed negative-mass target |
| --- | --- |
| Positive angular multiplier with normalized spherical mean | For a radial signed density, negative mass is unchanged after angular integration. It can localize its presentation but cannot make N tend to zero. |
| Smooth invertible conservative transport of the complete signed density | The pushforward preserves both positive and negative masses separately. This rules out (13) for an initially sign-changing integrand in this class. |
| Conservative diffusion of the complete signed density | Negative mass contracts. An additional theta-specific decay/coercivity estimate is needed to force its limit to zero. |
| Paired Darboux or source-and-test deformation | The complete integral is preserved, but both factors and boundary/forcing terms matter. No existing theorem gives sign creation or (14) for the higher-order density. |
| Source-only transport with the old observation fixed | Coefficients change; a separate real-rootedness-preservation or return theorem is required. The particular raw radial flow in chat0053 is already obstructed. |

For invertible transport X=Psi_s(Y), conservation gives f_s(Psi_sY)|det DPsi_s|=f_0(Y), hence integral f_s^-=integral f_0^- exactly. The positive angular multiplication statement follows from (Af)^-=Af^- and spherical mean A=1. These are scoped obstructions for those operations, not for all conservative flows.

### The exact ordinary-heat comparison

Let f in L1(R^m) be real with finite first absolute spatial moment, M=integral f, and G_s the unit-mass Gaussian heat kernel. Then
\[
\|G_s*f-MG_s\|_1
\le\frac1{\sqrt{\pi s}}\int|Y|\,|f(Y)|\,dY.              \tag{19}
\]
Indeed write the difference as integral f(Y)[G_s(.-Y)-G_s]dY. A translation along a line and integral of the directional derivative give ||G_s(.-Y)-G_s||_1<=|Y|/sqrt(pi s). This proves (19) without an unknown sign assumption.

The negative-part operation is 1-Lipschitz in L1, so
\[
\left|\|(G_s*f)^-\|_1-\max(-M,0)\right|
\le\frac1{\sqrt{\pi s}}\int|Y|\,|f(Y)|\,dY.              \tag{20}
\]
In particular
\[
\lim_{s\to\infty}\|(G_s*f)^-\|_1=\max(-M,0).             \tag{21}
\]
This applies to (16) for every finite r,k. Ordinary diffusion does asymptotically remove negative mass when the desired determinant is nonnegative. It does not establish that sign merely by being smoothing or positivity preserving. If M<0, the asymptotic Gaussian is negative. The desired negativity decay is exactly equivalent to M>=0 for this fixed heat evolution. A new proof of an estimate such as (14) from theta data could still resolve it; assuming the limit or the sign of the leading Gaussian would not.

Equation (19) also explains why unrescaled pointwise convergence to zero is irrelevant. The spreading Gaussian carries the conserved mass while its pointwise height decays. At a positive M it gives a possible finite-parameter comparison, but using M as a known positive coefficient would assume the target.

A potentially weaker target would be to make an evolved h_r coordinatewise increasing and then use (7) and the positive anchor, rather than make it nonnegative everywhere. Such an approach must preserve or compare every relevant tilted expectation, not merely one integral at one k. No such compatible evolution is constructed here.

## 6 Changing the source instead requires a root theorem

The original Jensen integral is
\[
J^{d,n}(X)=\frac{n!}{(2n)!}\int_0^\infty u^{2n}\Phi(u)
 {}_1F_1\left(-d;n+\tfrac12;-\frac{Xu^2}{4}\right)du.        \tag{22}
\]
The finite hypergeometric kernel is a scaled Laguerre polynomial by [DLMF 18.5.12][dlmf]. Each u>0 kernel has negative real zeros. Their positive averages need not: Note01's measure 0.9 delta_1+0.1 delta_4 gives, at d=2,n=0,
\[
1+\frac52X+\frac{53}{24}X^2,
\qquad \operatorname{disc}=-\frac{31}{12}<0.               \tag{23}
\]
Smooth narrow positive approximations preserve this strict negative discriminant. Thus spatial heat averaging of polynomial-valued densities has no generic hyperbolicity-preservation theorem just from positive weights.

If a different source path is used, its induced polynomial equation and direction must be controlled. For illustration, under an actually derived equation
\[
\partial_sP_s=-a(s,X)\partial_X^2P_s+b(s,X)\partial_XP_s+c(s,X)P_s,
\]
simple real roots satisfy
\[
\dot x_i=2a(s,x_i)\sum_{j\ne i}\frac1{x_i-x_j}-b(s,x_i).    \tag{24}
\]
The second-derivative term is locally repulsive when a>0. This local formula is not a global preservation theorem: degree, leading coefficient, multiple-root limits, endpoint time, and convergence all require proof. No equation of this form connecting a known hyperbolic starting family to theta is supplied here.

The precise raw exterior transport in [chat0053][transport] uses v(X)=X+X/(1+|X|^2), source evolution partial_s rho=div(v rho), and the fixed logarithmic cosine. Its transformed functions have nonreal zeros outside every bounded horizontal strip at each finite s!=0. Merely recentering its moved endpoint also fails. The recorded mechanism is loss of complete endpoint/reflection compatibility. That obstruction excludes this specific family as an all-real intermediate family; it does not exclude different generators or conservative evolution of the complete signed density. The odd logarithmic velocity proposed there preserves evenness, but has no proved hyperbolicity advantage.

## 7 Controls and a bounded next question

The complete Jensen/PF criteria are classical RH-equivalent destinations, stated once. The all-order coordinatewise h_r condition is only a sufficient candidate; no equivalence or canonical validity is claimed. For the fixed ordinary-heat density, negative-mass decay is equivalent to that determinant's nonnegativity by (21). A quantitative theta-based dissipation estimate would be substantive; renaming the same sign would not.

The analytical control screen is:

| Control | Premise and implication for this proposal |
| --- | --- |
| Gaussian source | The ratios Phi^{(2i)}/Phi are monic degree-i polynomials in R, so h_r=1 for every r. It checks normalization and provides an already positive comparison; no theta evidence follows. |
| Two-atom example (23), and smooth positive approximations | They defeat positive averaging as a generic root-preservation argument. The atoms are outside the smooth derivative identity (4); the smooth approximation can be chosen even with rapid decay. |
| Euler-factor sources | Positive/even tails allow the generic finite-order integral and conservative heat construction. They fail canonical theta reconstruction through the altered arithmetic factor. No uncomputed higher-order h_r or dissipation sign is attributed to them. |
| Weighted-square and finite-prime sources | Changed coefficients fail full canonical reconstruction; finitely matched odd endpoints cannot supply (4) at arbitrary orders. Any unmatched endpoint must remain in the formula. |
| Reflected smooth/super-Gaussian and positive-primitive controls | Where the required spatial moments exist, they admit the generic conservative construction. Full reflection or primitive positivity does not supply (14) or all-order h_r monotonicity. They fail the complete theta arithmetic premise. |
| Existing positive-time collision controls | A positive-time collision alone is not a refutation of a time-zero finite-order claim. They screen only the actual hypotheses and conclusions being asserted. |

No collision numerics or new theta sign tests were run. The point of a future theta-specific premise is not merely to name the canonical source; it must yield the quantitative inequality that the generic controls do not provide.

The next useful conceptual question is whether a conservative flux for the explicit lifted r=4,k=1 density can yield (14), or a finite-time positive-mass/negative-mass comparison, from the complete theta differential identities with all boundary and tail terms retained. Compare it with ordinary product heat (19)–(21). Specify the generator from known source data, not an inverse unknown determinant; prove global existence independently of the desired sign; and expose how the argument could depend on r. A failure for one generator is scoped to that generator and estimate.

This is **J-B04, B — Astra, proposed and not started**. No E task is ready until the flow and estimate are fixed. A successful pilot at order four would validate a new method, not extend the known low-order positivity range. Its value would be a credible parameter-dependent mechanism for arbitrary r and the small k regime.

## Reading and verification record

The relevant Investigation05 notes were read as local sources: angular multiplication (20), complete-density conservation/heat (25), paired Darboux deformation (17), the book's fixed-observation uniqueness discussion, and chat0053's source-transport obstruction including its recentered case and surviving odd-velocity candidate. Their internal-review qualifications remain in force.

Primary web passages rechecked on 1 November 2026: Griffin–Ono–Rolen–Zagier version 1 introduction and Theorem 1; Katkova version 1 Section 2 Lemma 3 and strict Theorem D, plus coefficient conventions; DLMF 18.5.12. Existing reading-copy provenance remains in the shared catalog. This is selected-passage inspection, not independent full-paper certification. Equations (5), (7)–(21), and (24) were checked analytically through determinant expansion, confluent Taylor expansion, the cofactor identity, conservation, and the stated heat-kernel argument. No novelty claim is made.

[review]: ../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md
[representation]: 01_J_B01_COEFFICIENT_REPRESENTATION_DECISION_20261101.md
[averaging]: 05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md
[heat]: ../../../05_radial_theta_collision_geometry/notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md
[darboux]: ../../../05_radial_theta_collision_geometry/notes/17_RADIAL_DARBOUX_SYSTEMS_PRESERVING_PHYSICAL_OBSERVATION_20261027.md
[transport]: ../../../05_radial_theta_collision_geometry/notes/CHAT0053_SOURCE_TRANSPORT_UNBOUNDED_STRIP_OBSTRUCTION_20261031.md
[gorz]: https://arxiv.org/html/1902.07321v1
[katkova]: https://arxiv.org/html/math/0505174v1
[dlmf]: https://dlmf.nist.gov/18.5.E12
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[target]: ../../../../../avoid/01_restating_the_target.md
[shape]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[coordinates]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[scopes]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
