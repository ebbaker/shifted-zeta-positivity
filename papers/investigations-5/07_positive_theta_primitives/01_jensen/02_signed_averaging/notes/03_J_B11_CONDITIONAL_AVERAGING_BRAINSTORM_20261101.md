# Conditional averaging and the next signed theta estimate

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**, research chat `01a19a10-f263-7ec0-8c19-85d2e5e1d41a`.

**Scope:** explanatory brainstorm for **[B] J-B11**, following the author's request to understand the continuation and discuss paths forward. The complete comparison in plan r1 remains open. This is a preliminary discussion, not the completed J-B11 return or a numerical execution request. The conditional tail calculation below has proof-author analytical checking only; inherited results retain their existing internal-review qualifications.

The best-supported first direction within this branch is to average the three inner nodes before estimating the outer node. A cofactor calculation shows that this conditional average tends to the already positive order-three average. Thus the known bad fixed triples coexist with a positive conditional tail. The missing input is an effective estimate retaining the full signed balance through the finite outer-node range.

| Next task | Type and recommended model | Readiness | Output |
| --- | --- | --- | --- |
| Continue J-B11 using conditional inner-node averaging | B; Astra, because the finite-range signed comparison is still a conceptual choice | Preliminary tail reduction available; complete estimate open | One effective tail payment and one joint finite-range estimate, or a precisely identified obstruction |
| Verify a fixed scalar formula if that comparison supplies one | E; Sol | No contract issued | Bounded calculation with complete source, endpoints and errors |

## What the signed average accomplishes

Use the source, coefficient normalization, ordered chambers and notation of [Continuation02](02_CONTINUATION_SIGNED_AVERAGING_20261101.md) and the [overview](../research-overview/01_SIGNED_AVERAGING_RESEARCH_OVERVIEW_20261101.md). At fixed determinant order r,
\[
A_{r,k}=E_{r,k}h_r=\frac{M_{r,k}}{Z_{r,k}},\qquad
M_{r,k}=F_{r,k}D_{r,k},\qquad Z_{r,k}>0.
\]
The density is positive; the observable may take either sign. Increasing k by one multiplies the density by q=product u_j². The exact identity is
\[
A_{4,1}-A_{4,0}=\frac{\operatorname{Cov}_{4,0}(h_4,q)}{E_{4,0}q}.
\]
The triangular determinant supplies the positive anchor
\[
A_{4,0}=34560c_0^4/Z_{4,0}>0.
\]
The default goal is nonnegative covariance. Order-three monotonicity is accepted in [Review01](../../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md). Its FKG argument uses an increasing observable and the lattice inequality for the carrier; [FKG Proposition 1, page 91](https://math.bme.hu/~balint/oktatas/perkolacio/percolation_papers/fortuin_kasteleyn_ginibre.pdf) was checked again for those hypotheses. The repository already catalogs this source. No new external theorem is imported here.

[Initial evaluation01](01_INITIAL_BRANCH_EVALUATION_20261101.md) proves that unchanged canonical h4 fails this coordinatewise premise. For three fixed origin-side source coordinates a<b<c, alpha=f[a,b,c]<0, and
\[
h_4(a,b,c,X)\longrightarrow\alpha,\qquad
\partial_Xh_4=24\alpha X^{-3/2}+O(X^{-2})<0
\]
eventually. This is a local failure of the sufficient mechanism, not a negative full covariance. A signed nonmonotone observable can still have positive covariance with an increasing weight. For example, three equally likely states with h=(1,-1,2) and q=(1,2,3) have covariance 1/3; their q-weighted mean is 5/6, above the original mean 2/3. This example explains the distinction and supplies no theta evidence.

## Averaging the inner nodes repairs the limiting tail sign

Fix k=0 or 1 and write v=u4, X=R(v). Define the unnormalized outer marginals
\[
d_k(v)=\int_{0<u_1<u_2<u_3<v}w_{4,k}(\mathbf u,v)\,d\mathbf u,
\quad
n_k(v)=\int_{0<u_1<u_2<u_3<v}w_{4,k}(\mathbf u,v)h_4(\mathbf u,v)\,d\mathbf u.
\]
Then d_k>0, Z4,k=integral d_k, M4,k=integral n_k, and the conditional average is m_k(v)=n_k(v)/d_k(v).

**Claim derived here, using the accepted source and tail inputs:**
\[
\frac{d_k(v)}{\Phi(v)v^{2k+6}X^3}\longrightarrow Z_{3,k},\qquad
\frac{n_k(v)}{\Phi(v)v^{2k+6}X^3}\longrightarrow M_{3,k}.
\tag{1}
\]
Consequently,
\[
\boxed{m_k(v)\longrightarrow A_{3,k}>0.}\tag{2}
\]
In particular m_0 and m_1 are each positive for all sufficiently large v. Also m_1-m_0 tends to A3,1-A3,0>=0; a nonnegative limiting difference alone is not being used to assert eventual nonnegativity of that difference.

To prove the denominator limit, factor the Vandermondes:
\[
\frac{d_k(v)}{\Phi(v)v^{2k+6}X^3}
=\int_{\Omega_3}\mathbf1_{u_3<v}w_{3,k}(\mathbf u)
\prod_{j=1}^3(1-u_j^2/v^2)(1-R(u_j)/X)\,d\mathbf u.
\]
Every factor tends to one for a fixed triple. On the indicated domain, the first factors lie in [0,1]; since R increases from a finite lower endpoint, the second factors are uniformly bounded for large positive X. The integrable w3,k therefore dominates the integrand up to a constant. Dominated convergence gives Z3,k.

For the numerator, cancel V(R) against the denominator of h4 before estimating. Put q_i(v)=Phi^(2i)(v)/Phi(v), i=0,1,2,3, so q0=1 and q1=X. Let Delta_hat_i be the three-column determinant of the inner source derivatives with row i omitted from rows 0,2,4,6. Expansion in the outer column gives
\[
\frac{n_k(v)}{\Phi(v)v^{2k+6}X^3}
=\sum_{i=0}^3(-1)^{i+3}\frac{q_i(v)}{X^3}
\int_{\Omega_3}\mathbf1_{u_3<v}
\Big(\prod_j u_j^{2k}\Big)V(\mathbf u^2)
\prod_j(1-u_j^2/v^2)\Delta_{\widehat i}(\mathbf u)\,d\mathbf u.
\]
The full-source tail expansion in Initial evaluation01 gives q3/X³->1, q2/X³->0, q1/X³->0 and q0/X³->0. Each inner integral is absolutely convergent: expand its finite determinant, and use fixed derivative theta tails against polynomial moments. The factors involving v are bounded by one. Dominated convergence applies to each of the four integrals. Only i=3 survives, with positive cofactor sign, and its integral is M3,k by the established order-three determinant representation. This proves (1).

This argument keeps the negative origin-side triples. Their contribution is integrated, not omitted or declared small. The positive limiting average comes from the complete order-three signed identity.

## What the limit contributes to the actual comparison

Keep the default comparator. Write
\[
A_{4,1}-A_{4,0}=\int_0^\infty L(v)\,dv,\qquad
L(v)=\frac{n_1(v)}{Z_{4,1}}-\frac{n_0(v)}{Z_{4,0}}.
\tag{3}
\]
Equation (1) implies
\[
\frac{L(v)}{\Phi(v)v^8R(v)^3}
\longrightarrow \frac{M_{3,1}}{Z_{4,1}}>0.
\tag{4}
\]
Thus this particular exact marginal regrouping of the difference has a positive eventual tail. A different centered covariance integrand need not have the same local sign. No claim is made that every natural decomposition has a favorable tail.

The regularity payments for these identities are inherited and explicit. Full evenness supplies the odd endpoint cancellations through Phi^(5)(0) used in the order-four determinant identity. The analytic coordinate u² and the accepted nonzero derivative of R in that coordinate make the coincident divided differences removable, including at the origin. For small v, d_k(v)=O(v^(27+8k)) and n_k(v)=O(v^(27+8k)): the two four-node Vandermondes each contribute degree twelve, the three integrations degree three, and the index weight degree 8k. Hence the outer endpoint is integrable. At infinity the cofactor integrals above and the full fixed-derivative theta tails give absolute integrability. These facts justify the rearrangements; they do not provide a signed finite-range estimate.

The remaining obligation is quantitative. Obtain an effective V and a lower bound for the complete integral in (3), retaining every contribution on [0,V] and a paid tail beyond V. The limit supplies neither a usable V nor a positive total. A negative compact contribution could outweigh the favorable tail. Global smallness of the known bad region has not been proved.

One possible analytical input is the exact derivative linkage
\[
G(u)=F''(u)+2\frac{\Phi'(u)}{\Phi(u)}F'(u)+R(u)F(u),
\quad F=\Phi^{(4)}/\Phi,\quad G=\Phi^{(6)}/\Phi.
\]
It follows by differentiating Phi F=Phi^(4) twice. It may permit cancellations among the four cofactors before bounding them. The identity holds for any suitable nonvanishing source; theta-specific quantitative estimates must still come from the complete canonical source. It is a candidate input, not a positivity theorem. All boundary terms created by any new integration by parts must be retained.

## Alternatives and the decision

An explicit anchor-preserving loss is a possible fallback:
\[
\operatorname{Cov}_{4,0}(h_4,q)\ge-\eta A_{4,0}E_{4,0}q,
\qquad 0\le\eta<1.
\]
It would give A4,1>=(1-eta)A4,0>0. This is a **changed comparator**, requiring an independently obtained eta. Merely demanding covariance greater than -A4,0 E q is exactly the desired positivity and is not an acquired estimate.

A future bounded diagnostic can avoid direct four-dimensional quadrature. Finite determinant expansion and Fubini give
\[
Z_{4,k}=\det\left[\int_0^\infty
u^{2(k+i)}R(u)^j\Phi(u)\,du\right]_{i,j=0}^3.
\]
There is no extra 4! because the original integral uses the ordered chamber. The scalar numerator M4,1 Z4,0-M4,0 Z4,1 decides the sign of the covariance. This is an exact reduction, not sign evidence or an issued computation. Its useful diagnostic question would be whether the stronger normalized comparison even holds, not whether already known D4,1 is positive. Complete errors, fixed work limits and an acceptance test would have to be specified before execution.

**Recommendation:** continue J-B11 with the conditional/cofactor route and one finite-range signed estimate. Keep the full comparison open until that estimate is obtained. The sibling J-B10 Mellin-curvature route remains independent and has its own stronger order-induction motivation; no sibling result is used here. No claim of arbitrary-order propagation follows from this order-four pilot.

## Controls and evidence limits

Read with the [result index](../../../../../../result-summaries/README.md), especially [theta identities](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [controls](../../../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../../../avoid/README.md), especially [target reformulation](../../../../../../avoid/01_restating_the_target.md), [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [joint signed estimates](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

- Gaussian: h4=1 and all conditional averages equal one. This checks normalization. Its derivative-ratio tail coefficients differ from theta, and covariance is exactly zero. The marginal difference in (3) still has a positive eventual tail in this example, demonstrating why (4) alone does not decide the total sign.
- Euler-factor and altered finite-prime sources: they fail the unchanged canonical expansion supplying the present tail ratios and accepted order-three inputs. No uncomputed covariance sign is assigned to them.
- Weighted-square sources: matching finitely many endpoints does not supply the full even canonical source; the required odd endpoints and derivative estimates need separate checking.
- Reflected, shape-only and positive-primitive sources: reflection or positive primitives alone do not supply the canonical tail ratios or accepted order-three monotonicity. The generic cofactor identity can apply to other sources, but its positive limiting conclusion needs its stated inputs.
- A positive-time collision does not refute this finite-order time-zero statement. The actual canonical negative-derivative configurations remain present throughout the conditional integral.

The new tail limits have analytical self-checking only. They do not upgrade the internal status of prior work, prove the full covariance sign, certify a new coefficient range, or establish RH.

## Input versions

SHA-256 values identify the read inputs; they do not validate mathematical claims.

| Input | SHA-256 |
| --- | --- |
| papers/investigations-5/07_positive_theta_primitives/01_jensen/02_signed_averaging/notes/02_CONTINUATION_SIGNED_AVERAGING_20261101.md | `5938121b2a0123a3138519d0c32e02cd934d59a240595b08cfc1a43b2d760da1` |
| papers/investigations-5/07_positive_theta_primitives/01_jensen/02_signed_averaging/notes/01_INITIAL_BRANCH_EVALUATION_20261101.md | `77f4002d697406d74bf591884074637916907acf8225285c659fd8743513400f` |
| papers/investigations-5/07_positive_theta_primitives/01_jensen/02_signed_averaging/research-plan/01_SIGNED_AVERAGING_RESEARCH_PLAN_20261101.md | `3f1a66b146ab7b6e1c7e6ac70d5c33d4ab22f482788381301ad0178e44953213` |
| papers/investigations-5/07_positive_theta_primitives/01_jensen/notes/14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md | `d8b9160e158317462d75a59d7535f500898cfb51345284d33287cf24eafd14f0` |
| papers/investigations-5/07_positive_theta_primitives/01_jensen/reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md | `c13e63e7c017285932e75d2add333b8d683e5ed3b9a096f6e20e31e88e0a2dfe` |
| papers/investigations-5/07_positive_theta_primitives/01_jensen/reviews/02_PARALLEL_BRANCH_EVALUATION_REVIEW_20261101.md | `c862677ba3bb3fe46a1ff6e09431c14fdcd73c425332bc6b2d49726aba0f1884` |
