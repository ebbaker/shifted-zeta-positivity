# Internal review of the analytic simplicity opening round

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. The parent derived Note 12 and checked the arithmetic notes; a separate agent reviewed Note 12, another developed Note 13, and a third independently reviewed Note 13 and checked the published moment comparison. This is internal same-model review, not specialist or formal verification.

**Assessment:** [Note 12](../notes/12_HERMITE_CLUSTER_DOMINATION_AND_JOINT_CONSUMER_20261023.md) and [Note 13](../notes/13_COMPLETE_XI_LOGARITHMIC_HEAT_ANCHOR_20261023.md) have proofs within their stated scopes. The first strengthens finite multiplicity transfer; the second improves the book's particular exterior anchor to a logarithmic negative-heat width. Neither supplies a useful upper bound for the complete multiplicity resource, a new simplicity proportion, density one, or exclusion of an individual zeta multiple zero. The manuscripts are unchanged; these findings belong in the research notes while the decisive arithmetic estimate remains open.

The [result index](../../../../../result-summaries/README.md) and [avoid index](../../../../../avoid/README.md) govern the status, including [shared control premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scoped claims](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [coupled estimates](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## 1. Hermite comparison and joint consumer

The independent review checked the entire proof rather than only examples:

- The gap vector field has nonnegative off-diagonal derivatives. All exterior roots give a nonpositive contribution to internal adjacent gaps because the cluster is consecutive in the complete real ordering.
- A constant multiple c>1 of the Hermite gap solution is a strict supersolution. The local expansion at the multiple endpoint allows comparison from any sufficiently small positive time; taking c down to one handles the singular initial point.
- Summed gap comparisons give each edge-weight lower bound. The block matrix inequality retains within-cluster interactions and drops only positive semidefinite intercluster terms. Thus q(t)>=sum(m-H_m) holds at every permitted positive time, not just in a limiting regime. No monotonicity of q(t) is claimed.
- The even/odd slacks in m<=(5/8)2floor(m/2)+(3/2)(m-H_m) are zero precisely for m=2,3 and increase thereafter. The mixed consumer improves both 3R/2 and 4q exactly on 1/4<q/R<7/12. Existing moment bounds may still be stronger.
- The multiplicity-class count and label bounds use the decreasing ratio H_m/m correctly. The quadratic and cubic heat controls attain the relevant costs; all-real controls are allowed to retain their collisions.

The theorem strengthens the existing finite-time comparison under its full root-motion hypothesis. It makes no claim for a truncated evolution with an unpaid exterior force.

## 2. Complete-xi Euler anchor

The independent arithmetic review checked:

- With z=-2tau+i(2sigma-1), the standard xi coordinate is 1-s; the functional equation recovers xi(s). The Gaussian substitution and contour shift yield exactly the carrier exp(-epsilon L^2/16), shifted argument s-epsilon L/4, and coefficient damping exp(-epsilon(log n)^2/4).
- The shift stays in a fixed Euler half-plane. The local logarithmic gamma remainder is O((|q|+|q|^2)/|tau|) and integrates to O(1/|tau|), uniformly for epsilon<=A/log|tau|.
- After division by the carrier, the full complementary tails are bounded by polynomial factors times exp(C|w|), absorbed by the Gaussian. No tail or coefficient is omitted.
- The Euler product supplies a uniform positive margin; the explicit smoothing loss is epsilon zeta''(1+delta)/4. The fixed-parameter eventual lower bound and the mean-spacing-squared limit exp(-kappa/16) follow.

The parent rechecked these signs and the book comparison. The previous sufficient condition uses an absolute source moment against an exponentially small Euler value. The new proof couples the gamma carrier with the Gaussian before taking moduli, so it supplies a genuine larger admissible width for this anchor. The constants are asymptotic and not numerically evaluated. The theorem provides no complex-time collar bounds, enclosing-disk upper bounds or complete root-path constants; these are separate prerequisites for the book's anchored path theorem.

A literature check found that the structural Gaussian/Dirichlet mechanism is already in [Dobner, arXiv:2005.05142v2](https://arxiv.org/html/2005.05142v2), notably (3), Theorem 4 and Section 4. The result is recorded as a directly normalized Euler-region specialization and a matched improvement to the current book's implementation. It is not a new representation or a confirmed priority claim. The complete canonical factorization distinguishes the stated input from several controls, but an exterior anchor can coexist with interior collisions; no control is falsely excluded.

## 3. Tested alternative: a published logarithmic-derivative bound

The analytic question was whether this available arithmetic input could immediately improve the simplicity conversion. The following calculation answers that question for the specified bound, without closing the broader moment route.

### Imported input and normalization

Assume RH. Let N(T) count nontrivial zeta zeros with 0<gamma<=T with multiplicity, and let Q(T)=sum over distinct such zeros of m_gamma^2. Put L=log T and

\[
I(a,T)=\int_1^T\left|\frac{\zeta'}{\zeta}
 (\tfrac12+a/L+it)\right|^2\,dt,
\quad w(u)=\frac4{4+u^2},
\quad K_a(x)=\frac{a^2}{a^2+\pi^2x^2}.
\]

Both indices in the following sum run over repeated zero labels:

\[
E_a(T)=\frac1{N(T)}\sum_{0<\gamma,\gamma'\le T}
 K_a\!\left(\frac{(\gamma-\gamma')L}{2\pi}\right)w(\gamma-\gamma').
\]

All summands are nonnegative, and each coincident pair contributes one. Consequently Q(T)/N(T)<=E_a(T), exactly, for every a>0.

[Carneiro, Chandee, Chirre and Milinovich, arXiv:2108.09258v2](https://arxiv.org/pdf/2108.09258), Lemma 16, relates this sum to I; its Theorem 5 bounds I using a bandlimited Poisson majorant. At each fixed a>0 their formulas imply

\[
E_a(T)=a+\frac{2aI(a,T)}{T L^2}+o(1),
\qquad
\limsup_{T\to\infty}\frac{I(a,T)}{T L^2}\le U^+(a),
\]
\[
U^+(a)=\frac{\coth a}{4a^2}
 -\frac{\operatorname{csch}^2a}{4a}
 +\frac{\coth a}{2}-\frac12.
\]

These are cumulative estimates. No same-constant dyadic bound follows by subtracting upper bounds. The same paper's Section 1.2, formula (IV), identifies the conjectural asymptotic for every fixed positive displacement with pair correlation under RH; that asymptotic is not an RH-only input.

### Algebraic consequence and exact optimization of this input

The preceding imported input yields

\[
\limsup_{T\to\infty}\frac{Q(T)}{N(T)}\le B(a),
\qquad
B(a)=a+2aU^+(a)
=\frac{\coth a}{2a}-\frac{\operatorname{csch}^2a}{2}+a\coth a.
\]

Here is an elementary independent check of the optimal displacement. For b_n=pi n, the partial-fraction expansion of coth gives

\[
B(a)=1+2\sum_{n=1}^{\infty}
 \left\{\frac{b_n^2}{(a^2+b_n^2)^2}
             +\frac{a^2}{a^2+b_n^2}\right\}.
\]

The series and its derivatives converge locally uniformly for a>0. Setting s=a^2, the derivative of the nth brace is

\[
\frac{b_n^2(s+b_n^2-2)}{(s+b_n^2)^3}>0,
\]

because b_n^2>=pi^2>2. Thus B is strictly increasing and

\[
\inf_{a>0}B(a)=\lim_{a\downarrow0}B(a)
=1+2\sum_{n\ge1}(\pi n)^{-2}=\frac43.
\]

The limits are taken T->infinity first at fixed a, then a->0. Since the nonsimple label count M satisfies M<=Q-N, this particular chain yields only liminf N_s/N>=2/3. It does not improve the checked 19/27 benchmark or the imported Q/N<=1.3208 multiplicity bound already recorded in [Note 10](../notes/10_SIMPLICITY_THEOREM_TARGETS_AND_HYBRID_CONSUMER_20261023.md). The conclusion excludes only improving the consumer by changing a in this specific published upper bound; it does not exclude stronger moment estimates, joint observables, or other arithmetic input.

### Higher moments do not supply a missing RH-only input

[Fan Ge, arXiv:2211.08571v2](https://arxiv.org/pdf/2211.08571v2), Theorem 1.1, obtains limiting higher logarithmic-derivative moments under RH and the additional ES(2K) hypothesis. The displayed definition of ES(2K) on page 2 counts microscopic tuples with not all labels equal, with zeros listed with multiplicity. Repeated zeros therefore already enter the assumed negligible population. Using that theorem as an RH-only simplicity estimate would silently add precisely the kind of cluster restriction the current research program requires us to prove.

This comparison supports seeking genuinely new arithmetic information in the heat routes or a stronger joint moment, without claiming that the logarithmic-derivative direction is closed.

## 4. Research decision

SIMP-01 remains open: a source-specific exterior anchor is improved, but no useful restriction on the earlier nonreal population or actual positive-time q has been acquired. SIMP-02 has a stronger proved generic transfer and joint consumer. SIMP-03 remains open; neither manuscript was rewritten merely to incorporate supporting machinery.

The immediate useful continuation is to determine whether a complete carrier-preserving estimate can control the actual earlier nonreal population and relative flux on a region relevant to endpoint multiplicities, or whether a different arithmetic estimate can upper-bound q. Note 13's fixed Euler margin cannot be extended to the critical strip by dropping its delta-dependence. The particular published displacement bound in Section 3 cannot be improved by varying its parameter alone. These conclusions leave other joint moments and canonical estimates open.

No numerical scan, manuscript snapshot, commit or external publication was made in this round. Analytical comparison, classical-source checks, separate same-model proof review, file/link checks and preservation of earlier work are the relevant verification.


## 5. Strategic reassessment: a direct arithmetic comparison

23 October 2026. Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra (Codex), effort ultra. Two separate same-model agents compared the routes; the parent checked the cited primary-source passages. A separate same-model audit of this section checked the variational optimum, complex residual coefficient and limiting scope. This updates the priority suggested in Section 4, without closing SIMP-01 or imposing a fixed final theorem.

**Recommendation:** first investigate an additional arithmetic coefficient direction in the discrete mollified derivative moments at the zeta zeros. Retain the heat results as supporting tools when a specified arithmetic estimate needs them. The present exterior anchor and Hermite comparison do not upper-bound the actual multiplicity resources. More field approximation alone would leave that gap intact.

This is an established type of simplicity argument, with a proposed extension to investigate. It is not a new simplicity theorem or a claim that other routes cannot work. The immediate question is whether a larger coefficient class supplies a provable gain; a useful different local multiplicity restriction would also serve the overview.

### Baseline and a scoped obstruction

[Bui and Heath-Brown, Section 2](https://arxiv.org/html/1302.5018v1) use

\[
 B(s)=\sum_{n\le y}\mu(n)P\!\left(\frac{\log(y/n)}{\log y}\right)n^{-s},
 \qquad y=T^\theta,\quad 0<\theta<\tfrac12,
 \quad P(0)=0,\quad P(1)=1.
\]

Under RH their first and second moments give the asymptotic simple-zero lower proportion

\[
 F_\theta(P)=
 \frac{(\tfrac12+\theta\int_0^1P)^2}
 {\tfrac13+\theta\int_0^1P+\theta^2(\int_0^1P)^2
       +(12\theta)^{-1}\int_0^1(P')^2}.
\]

For completeness, the elementary variational comparison is as follows. At fixed A=integral P, the least derivative energy among real H^1 functions with these endpoints is
\(1+12(A-1/2)^2\), attained at \(P(u)=u+6(A-1/2)u(1-u)\). This follows by subtracting that quadratic: the cross term integrates to zero using the zero endpoints and integral of the remainder. Maximizing the resulting scalar quotient gives

\[
 \sup_P F_\theta(P)=1-(1+\theta)^{-3},\qquad
 P(u)=(1+\theta)u-\theta u^2.
\]

The limiting value is 19/27 as theta increases to 1/2, after the height limit. Thus reweighting that merely replaces P within this justified class cannot improve its optimum. This does not exclude heat-dependent weights with new arithmetic structure, other coefficient classes or stronger moment estimates. The published error bound is proved at fixed theta<1/2; no endpoint or longer-mollifier theorem is being imported.

### A concrete calculation that decides whether to continue

Write E_T for the average over zero labels 0<gamma<=T, with multiplicity, and L=log(T/(2 pi)). Let w_0=B_0(rho) zeta'(rho)/L for the optimized baseline. For fixed theta let a_0 (real for this baseline) and b_00 be its limiting first and squared moments, c_theta=a_0/b_00, and r_theta=1-c_theta w_0. Then

\[
 \lim E_T|r_\theta|^2=1-F_\theta.
\]

For a candidate w_1=B_1(rho) zeta'(rho)/L, seek justified estimates

\[
 J_\theta=\lim E_T[r_\theta\overline{w_1}],\qquad
 \limsup E_T|w_1|^2\le U_\theta<\infty.
\]

When U_theta>0, use r_theta-(J_theta/U_theta)w_1. Expansion of its squared norm yields

\[
 \liminf\frac{N_s(T)}{N(T)}
 \ge F_\theta+\frac{|J_\theta|^2}{U_\theta}.
\]

Every nonsimple zero label contributes exactly one to the residual square, because both derivative terms vanish there. This is a generic algebraic consumer; the missing source-specific premise is the arithmetic first/cross moment and squared-moment bound. Collision controls remain allowed unless that premise excludes their event cost. Sparse double zeros remain compatible with any fixed positive exceptional proportion, so this route presently targets quantitative progress, not a deduction of every-zero simplicity.

The endpoint baseline moments are a_0=19/24, b_00=57/64, c=8/9 and residual 8/27. These are limits of fixed-theta formulas, not justification for setting y=sqrt(T). A gain over 19/27 requires a proved improvement exceeding 19/27-F_theta at an admissible fixed theta, or a controlled iterated limit with a positive gain.

A first candidate is the squarefree-supported direction

\[
 b_1(n)=\frac{\mu(n)}{(\log y)^2}
 \sum_{\substack{p<q\\pq\mid n}}\log p\log q\,
 P_1\!\left(\frac{\log(y/n)}{\log y}\right),\qquad P_1(0)=0.
\]

This is a Feng-type coefficient, not a new mollifier invention. [Pratt, Robles, Zaharescu and Zeindler, Section 3.2](https://doi.org/10.1007/s40687-019-0199-8) exhibit this family in continuous mollification; their Section 5 warns about replacing squarefree-restricted coefficients by unrestricted convolutions. [Kühn, Robles and Zeindler](https://arxiv.org/abs/1605.02604v3) is an additional prior-art lead, inspected at metadata/abstract level. Their continuous moment results are not the needed discrete moments. The references catalog records these exact reading limits.

The next calculation is therefore the first moment of w_1, its cross moment with w_0, and a usable squared-moment bound, together with all remainders. Compare against existing discrete-moment literature before claiming novelty. If the complete calculation gives J_theta=0, adding that direction to the fixed optimal residual cannot improve it; a broader joint reoptimization would need a separately demonstrated gain. If the error proof requires an unproved extra zero-spacing or longer-mollifier hypothesis, state it and redirect. Do not proceed to numerical coefficient searches on the basis of a diagonal-only gain.

No new arithmetic bound, manuscript revision or mathematical milestone is claimed by this strategic assessment.


## Follow-up outcome — 23 October 2026

The proposed two-prime Feng test is now carried out in [Note 14](../notes/14_DISCRETE_FENG_MOMENT_REDUCTION_20261023.md), with [Review 05](05_DISCRETE_FENG_MOMENT_REVIEW_20261023.md). Its first moment is explicit, but its complete mixed moment has zero residual correlation in the proved high-smoothing class. Thus fixed finite combinations with positive limiting second moment do not improve the baseline at leading order. Low-smoothing moments, null directions and height-dependent optimization are outside this conclusion. This narrows the candidate proposed above; it does not close the broader arithmetic route or produce a new simplicity percentage. Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra (Codex), effort ultra.
