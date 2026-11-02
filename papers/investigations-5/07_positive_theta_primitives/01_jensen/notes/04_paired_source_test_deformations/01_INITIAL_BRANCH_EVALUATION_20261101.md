# J-B07: Darboux moment transfer and a scoped absolute-bound comparison

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Contributor **/root/branch04**, actual recorded **gpt-6-astra (Codex), reasoning effort ultra**; child session **01a199a1-c078-7471-addf-037bb4312704**, child turn **01a199a1-c090-70c2-ad42-038bff69b366**, inheriting coordinator session **01a1999e-49d4-7a52-9e8a-95b0c5c430f1**. The child session and turn metadata were read. This is a same-model analytical contribution with inherited source inputs, not independent specialist review. The coordinator alone owns shared records and research-chat capture.

**J-B07 is complete as a bounded conceptual assessment.** The fixed Darboux family preserves every ordinary coefficient needed for \(D_{4,1}\), with an explicit positive transformed moment test and all forcing and endpoint terms retained. For the selected estimating method—absolute source-residual moment bounds followed by a coefficient-box determinant bound—the transformed radii are never smaller than the direct radii. Thus this method supplies **no gain** for the determinant lower bound. This is a proved-in-note comparison for one transformation and one information class, not an exclusion of all paired deformations or of a new signed theta estimate.

**Disposition:** retain the exact moment transfer as a reusable tool; stop the selected absolute-residual/box method. No new coefficient range, higher-order theta sign, root-preservation theorem or numerical campaign is claimed. The accepted \(R'>0,K>0\), normalized order-three comparison and negative origin \(C\) remain unchanged. The order-four, small-index pilot is inside the inherited known positivity baseline.

## 1. Fixed consumer, selected deformation and versions

The consumer is
\[
D_{4,1}=\det[c_{1+j-i}]_{i,j=0}^3,\qquad
c_m=\frac1{(2m)!}\int_0^\infty u^{2m}\Phi(u)\,du,\qquad c_m=0\ (m<0).
\tag{1}
\]
The physical source remains the complete canonical theta source at physical heat time zero. This is a coefficient argument; neither raw moments nor \(\gamma_m=m!c_m\) are substituted for \(c_m\).

Use the existing cosh-seed Darboux construction. The selected member is **\(\kappa=1\)**; formulas below retain a finite \(\kappa\ge0\) where doing so clarifies the comparison within this one family. No second deformation is tested. Write
\[
x=2u,\quad g(x)=4\Phi(x/2),\quad
w_\kappa(x)=\kappa\tanh(\kappa x),\quad
\mathcal A_\kappa=\partial_x-w_\kappa,\quad h_\kappa=\mathcal A_\kappa g.
\tag{2}
\]
The transformed forcing \(h_\kappa\) is part of the pairing. It is not an independently chosen positive source, and the original moment test cannot be left unchanged.

Relevant input versions are working-tree SHA-256 values, not a claim of a committed snapshot:

| Input | SHA-256 |
| --- | --- |
| [Branch brief](README.md) | fd30ddb0e4fe8ada7c47e90f93db6c0f530776b8cf2b1ffad97e28ac9d7dc558 |
| [Note14](../14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md) | d8b9160e158317462d75a59d7535f500898cfb51345284d33287cf24eafd14f0 |
| [Note15 request](../15_CONTINUATION_PARALLEL_BRANCH_EVALUATION_20261101.md) | 2d2fd23efd67b019c484ec551f779f1feaf4ffe08046ba457de6d5a3b1ec1f1a |
| [Accepted Review01](../../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md) | c13e63e7c017285932e75d2add333b8d683e5ed3b9a096f6e20e31e88e0a2dfe |
| [Investigation05 Darboux Note17](../../../../05_radial_theta_collision_geometry/notes/17_RADIAL_DARBOUX_SYSTEMS_PRESERVING_PHYSICAL_OBSERVATION_20261027.md) | 7478de010a5e7245de1e5467d379633d4794a1d588d71dc501867277bc3cc71d |
| Live register at this worker's version check | 56b71423d01ea5d7a70a53b2f99a8a2302ed57a840ad25d1b6842e132dbf3f69 |

Root instructions, model workflow, large-file/history rules, ideas/live register, the accepted review, and the relevant result/avoid/control passages were read. No new external theorem is imported: the needed factorization, integral transfer and norm comparison are proved below. The inherited reference inspection is not upgraded, and no reference-catalog addition is proposed.

## 2. Forced equations and the extension to coefficient extraction

The inherited selected response satisfies
\[
Y''+\lambda Y=g,\qquad
U_\kappa=\mathcal A_\kappa Y,\qquad
U_\kappa''+(\lambda+2w_\kappa')U_\kappa=h_\kappa,
\tag{3}
\]
because \(w_\kappa'+w_\kappa^2=\kappa^2\). Its inverse is
\[
Y=\frac{g-(\partial_x+w_\kappa)U_\kappa}{\lambda+\kappa^2}.
\tag{4}
\]
At the selected \(\kappa=1\), the denominator is nonzero near \(\lambda=0\). The selected response is explicitly \(Y(x;\lambda)=\int_x^\infty \sin(\sqrt\lambda(v-x))g(v)/\sqrt\lambda\,dv\), with the kernel continued at zero. The complete theta tail makes it analytic near zero with the stated selected decay; no sign-dependent existence condition is introduced.

The paired test is
\[
p_\kappa(x;\lambda)
=\frac{\sqrt\lambda\sin(\sqrt\lambda x)+w_\kappa(x)\cos(\sqrt\lambda x)}
       {\lambda+\kappa^2},\qquad
p_\kappa'+w_\kappa p_\kappa=\cos(\sqrt\lambda x),\quad p_\kappa(0;\lambda)=0.
\tag{5}
\]
The numerator is analytic in \(\lambda\) despite its square-root notation. For \(\kappa=1\), (5) is analytic on a neighborhood of zero. Equivalently, the nonsingular formula
\[
p_\kappa(x;\lambda)
=\operatorname{sech}(\kappa x)
  \int_0^x\cosh(\kappa y)\cos(\sqrt\lambda y)\,dy
\tag{6}
\]
defines the same solution, including \(\kappa=0\). This gives directly the extension needed for coefficient extraction, which was not part of the older note's stated compact positive-\(\lambda\) parameter range.

Integration by parts gives
\[
\int_0^\infty p_\kappa h_\kappa\,dx
=[p_\kappa g]_0^\infty-\int_0^\infty(p_\kappa'+w_\kappa p_\kappa)g\,dx
=-\int_0^\infty g(x)\cos(\sqrt\lambda x)\,dx
=-8\sum_{m\ge0}(-1)^m4^m c_m\lambda^m.
\tag{7}
\]
The lower boundary is zero because \(p_\kappa(0;\lambda)=0\), not because the source vanishes at zero. On any fixed complex \(\lambda\)-disk, (6) and its first four \(\lambda\) derivatives are bounded by a polynomial times \(e^{C x}\). The complete theta source and its first derivative decay faster than every fixed exponential. These bounds justify (7), differentiation under its full integral and the outer boundary limit through \(m=4\). The same argument works for each arbitrary finite \(m\); no uniform-in-\(m\) bound is asserted.

The forced system's boundary terms are not discarded. With \(Z=Y_\lambda\), \(V_\kappa=\mathcal A_\kappa Z\), and \(B=Y'(0)\),
\[
U_\kappa(0)=B,\quad
U_\kappa'(0)=g(0)-(\lambda+\kappa^2)Y(0),\quad
V_\kappa'(0)=-Y(0)-(\lambda+\kappa^2)Z(0).
\]
Thus its complete energy identity remains
\[
\int_0^\infty(U_\kappa^2+h_\kappa V_\kappa)\,dx
=(\lambda+\kappa^2)\int_0^\infty(Y^2+gZ)\,dx
-Y(0)B-g(0)B_\lambda.                         \tag{8}
\]
At coefficient extraction \(\lambda=0\), no event condition sets \(B\) or \(B_\lambda\) to zero. Equation (8) supplies no homogeneous positive energy after those boundary terms are omitted. If physical heat time were restored, the forcing law would include
\(\partial_t h_\kappa=x^2h_\kappa/4+xg_t/2\); the extra term is also retained. Physical time is fixed at zero throughout the present assessment.

## 3. Explicit positive moment tests and the complete determinant pairing

Define, for \(m\ge0\),
\[
q_m(x)=\frac{x^{2m}}{8\,4^m(2m)!},\qquad
p_{\kappa,m}(x)=\operatorname{sech}(\kappa x)
 \int_0^x\cosh(\kappa y)q_m(y)\,dy.
\tag{9}
\]
Then \(p_{\kappa,m}\ge0\), \(p_{\kappa,m}(0)=0\), and
\[
p_{\kappa,m}'+w_\kappa p_{\kappa,m}=q_m,\qquad
p_{\kappa,m}(x)\le \frac{x^{2m+1}}{8\,4^m(2m+1)!}.
\tag{10}
\]
The last bound follows from \(\cosh(\kappa y)/\cosh(\kappa x)\le1\) for \(0\le y\le x\). The conversion \(x=2u,\ g=4\Phi(x/2)\) gives exactly
\[
\boxed{c_m=\int_0^\infty q_m g\,dx
=-\int_0^\infty p_{\kappa,m}h_\kappa\,dx.}
\tag{11}
\]
In terms of (7), \(p_{\kappa,m}=(-1)^m(8\,4^m m!)^{-1}
\partial_\lambda^m p_\kappa|_{\lambda=0}\). All constants and signs in (11) agree with direct integration by parts. The complete source and transformed forcing remain under the integrals.

For \(m<0\), set \(q_m=p_{\kappa,m}=0\) as the structural convention in (1); do not invent negative-power moments. Hence the \(4\)-square matrix of preserved entries is
\[
\begin{pmatrix}
c_1&c_2&c_3&c_4\\
c_0&c_1&c_2&c_3\\
0&c_0&c_1&c_2\\
0&0&c_0&c_1
\end{pmatrix}.
\]
Column multilinearity gives the actual full determinant pairing
\[
D_{4,1}
=\int_{(0,\infty)^4}\prod_{j=0}^3h_\kappa(x_j)\,
 \det[p_{\kappa,1+j-i}(x_j)]_{i,j=0}^3\,d\mathbf x.
\tag{12}
\]
The four minus signs in (11) cancel. There is **no \(1/4!\)** in (12): the columns have assigned test indices and this unsymmetrized kernel is integrated on the full product domain. This is a different representation from Note14's symmetric derivative-determinant integrand on an ordered chamber.

Applying integration by parts once in every coordinate pulls (12) back exactly to
\[
D_{4,1}
=\int_{(0,\infty)^4}\prod_{j=0}^3g(x_j)\,
 \det[q_{1+j-i}(x_j)]_{i,j=0}^3\,d\mathbf x.
\tag{13}
\]
Each \(\partial_{x_j}+w_\kappa(x_j)\) acts only on column \(j\), replacing its \(p\)-entries by \(q\)-entries. Every lower face vanishes since all \(p\)-entries in that column vanish at zero; upper faces vanish by the complete tail and polynomial bound (10). Finite determinant expansion gives absolute integrability, so iterated integration and Fubini are justified. No collision face is a boundary of this product integral. These formulas establish preservation for the required moments and determinant, not just at one spectral value.

For a concrete finite consumer, expansion gives
\[
\mathcal P(c_0,\ldots,c_4):=D_{4,1}
=c_1^4-3c_0c_1^2c_2+c_0^2c_2^2+2c_0^2c_1c_3-c_0^3c_4.
\tag{14}
\]
It follows either by expanding the displayed matrix or by the normalized Hessenberg recurrence in Note14 (5). This exact finite expression is the declared object of the estimate below. No coefficient scan or numerical acquisition is performed.

## 4. The selected estimate and its equally informed pullback

Fix the explicit reference \(g_\star(x)=g(0)e^{-x^2}\), and let
\[
\eta=g-g_\star,\qquad h_{\kappa,\star}=\mathcal A_\kappa g_\star,\qquad
\delta h_\kappa=\mathcal A_\kappa\eta.
\]
This is an analytical reference for the estimate; the physical source is not replaced. Both \(\eta\) and \(\eta'\) have all polynomial absolute moments. The reference coefficients are
\[
c_{\star,m}=\frac{g(0)\sqrt\pi}{16}\frac{16^{-m}}{m!}.
\]
Writing \(a=g(0)\sqrt\pi/16\), its determinant is
\(D_{\star,4,1}=a^4\,16^{-4}/24>0\). This familiar Gaussian anchor does not determine the sign of the theta residual.

The single estimating method selected here is: bound each coefficient error by its absolute residual integral, then use the resulting common coefficient box to lower-bound the **complete** polynomial (14). Directly and after Darboux, respectively, the exact radii are
\[
r_m=\int_0^\infty q_m|\eta|\,dx,\qquad
R_{\kappa,m}=\int_0^\infty p_{\kappa,m}|\mathcal A_\kappa\eta|\,dx,
\quad 0\le m\le4,
\tag{15}
\]
and
\[
|c_m-c_{\star,m}|\le r_m,\qquad
|c_m-c_{\star,m}|\le R_{\kappa,m}.              \tag{16}
\]
Even the second radius keeps the joint transformed residual
\(\eta'-w_\kappa\eta\) inside its absolute value. Separately bounding its two terms can only enlarge it.

**Comparison lemma.** Under the stated decay and regularity,
\[
\boxed{r_m\le R_{\kappa,m}\quad(m=0,\ldots,4).} \tag{17}
\]
Indeed \(|\eta|\) is locally absolutely continuous and
\((|\eta|)'=\operatorname{sgn}(\eta)\eta'\) almost everywhere. Thus, with the same vanishing boundaries as before,
\[
\begin{aligned}
r_m
&=\int(p_{\kappa,m}'+w_\kappa p_{\kappa,m})|\eta|\,dx\\
&=\int p_{\kappa,m}\{- (|\eta|)'+w_\kappa|\eta|\}\,dx\\
&=-\int p_{\kappa,m}\operatorname{sgn}(\eta)
                  (\eta'-w_\kappa\eta)\,dx\\
&\le\int p_{\kappa,m}|\mathcal A_\kappa\eta|\,dx
=R_{\kappa,m}.
\end{aligned}
\tag{18}
\]
The same proof follows by smooth approximation of the absolute value. Zeros of \(\eta\) create no additional first-derivative boundary term. Equality occurs, for example, for a nonnegative decreasing residual, for which \(\mathcal A_\kappa\eta\le0\). Thus no strict universal improvement is hidden in (17).

To compare the complete determinant using exactly the selected information, let
\[
\mathcal B(v)=\{z\in\mathbb R^5:|z_m-c_{\star,m}|\le v_m,\ 0\le m\le4\},
\quad L(v)=\min_{z\in\mathcal B(v)}\mathcal P(z).
\tag{19}
\]
The repeated occurrences of each \(c_m\) are kept as the same variable in (14), so this is not an entry-independent matrix relaxation. The boxes are compact and \(\mathcal P\) is continuous. Since (17) gives
\(\mathcal B(r)\subseteq\mathcal B(R_\kappa)\),
\[
\boxed{L(R_\kappa)\le L(r)\le D_{4,1}.}        \tag{20}
\]
A transformed positive lower bound obtained by this method is therefore already implied by the equally informed direct bound. Any common constraints, such as coefficient nonnegativity, may be intersected with both boxes without reversing the inclusion. No separate sign is assigned to the terms in (14).

This is a mathematical comparison of exact norm allowances and the optimal consumer based on those allowances. The finite minima in (19) need not be computed to prove it. It does not assert equal runtime, forbid a convenient way of estimating an allowance, or compare unequal quadratures or precisions. If only an upper bound for \(R_{\kappa,m}\) has been acquired, the direct consumer can use it too because (17) already bounds \(r_m\). A representation can still be useful computationally, but such a benefit has not been measured here.

**What changed from the brief:** every needed moment and the full \(D_{4,1}\) pairing now have explicit transformed tests, and the selected estimate has a proved domination relation to its pullback. **What remains open:** a new theta-specific signed correlation estimate not reduced to the five absolute radii. Formula (20) does not compare such information, nor does it show that all Darboux estimates are equivalent in practicality or that every paired deformation fails.

## 5. Scope, arbitrary order, controls and strictness

The direct moment transfer (11) requires smoothness, integrability and its vanishing paired boundaries. It does **not** require all odd derivatives of \(g\) to vanish at zero: \(p_{\kappa,m}(0)=0\) pays the one lower endpoint for every \(m\). The full canonical evenness is retained, but the weaker hypotheses of this particular transfer must not be confused with Note14's repeated-integration-by-parts derivative determinant formula. A transformed odd forcing is not inserted into that old formula as though it were the original even source.

For each arbitrary finite \(r,k\), all nonnegative coefficient indices in \(D_{r,k}\) are at most \(k+r-1\). Formula (11), the analogue of (12), and (17) apply to that finite set; negative indices remain structural zeros. The column integral acquires the factor \((-1)^r\) when it is written using \(h_\kappa\). The polynomial consumer has increasing complexity, and its norm allowances depend on the indices. The comparison holds at small \(k\), including \(k=1\), but proves no coefficient positivity there. Increasing order does not turn this stopped absolute method into a new source of sign information. The triangular \(D_{r,0}=c_0^r\) anchor remains distinct from Jensen hyperbolicity at shift zero.

| Control | Actual premise check |
| --- | --- |
| Gaussian source | Satisfies the smoothness/tail assumptions, and its coefficients provide the displayed positive reference. Transfer and comparison hold; no theta evidence follows. |
| Euler-factor sources | Their smooth rapidly decaying variants satisfy the same pairing and comparison. They fail unchanged canonical arithmetic, not the Darboux identity. No determinant sign is assigned. |
| Weighted-square and finite-prime sources | When smooth with the required moments, they also satisfy this single-integration moment transfer. Full reflection may fail, so they cannot automatically use the original higher-derivative determinant identity. Altered coefficients fail canonical reconstruction. |
| Reflected smooth/super-Gaussian and positive-primitive sources | Satisfy the comparison when their derivatives have the required absolute moments. Reflection or primitive positivity supplies no omitted signed determinant estimate; they fail the complete canonical square source. |
| Atomic examples | Outside the classical \(C^1\)/absolute-continuity formulation for \(g\) and \(\eta\). Distributional extensions are not used. |
| Positive-time collision controls | Their event signs do not contradict or establish this physical-time-zero finite-order comparison. No collision certificate is rerun. |

The theorem is an information comparison valid on this stated class, not a theta-only positivity mechanism. Consequently it is neither necessary nor justified to claim that the controls fail (17). Their generic applicability explains why this transformation by itself supplies no new arithmetic sign. The [control cluster](../../../../../../result-summaries/12_collision_controls_and_screening.md), [target classification](../../../../../../avoid/01_restating_the_target.md), [joint-estimate rule](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scoped-exclusion rule](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) apply.

Neither conservation of the moments nor the positive Gaussian reference establishes \(D_{4,1}\ge0\), much less strict positivity, without paying the residual. If a future estimate yields only nonnegativity, a strict anchor or strict positive remainder still has to be supplied for a strict-minor criterion.

## 6. Disposition and one bounded next action

**Stop the cosh-seed Darboux absolute-residual/box route as a sign-improving method.** No derivative acquisition, \(\kappa\) optimization or coefficient campaign is warranted for that comparison, since (17) already settles every finite \(\kappa\) in the selected family.

**Next, conditionally: [B] a joint signed determinant residual estimate — Astra.** Continue this tool only if a consuming coefficient branch identifies one specific signed correlation in the complete polynomial (14), or its full integral (12), that a quantitative theta identity could control beyond the absolute radii (15). Keep \(\kappa=1\), \(r=4,k=1\), the complete source and all boundary/forcing terms fixed. The deliverable is one explicit inequality for the complete residual
\(\mathcal P(c_\star+\delta c)-\mathcal P(c_\star)\), its direct pullback using the same information, and either a proved useful margin or a precise unpaid term. Stop after one proposed correlation closes back to the same five absolute radii or requires the determinant sign itself. This is a new conceptual input, not an E implementation contract. No E task is ready from the present return.

The selected transformation is useful as a checked representation and a screening tool. Its present mathematical result is the scoped absence of gain in (20); it creates no dependency that another branch may silently assume solves its sign problem. This return uses no result from the other four parallel workers.
