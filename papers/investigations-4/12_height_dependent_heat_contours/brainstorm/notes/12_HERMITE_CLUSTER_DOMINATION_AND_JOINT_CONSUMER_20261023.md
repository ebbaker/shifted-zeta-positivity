# Hermite domination for complete real-root clusters

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Status: analytic derivation, with separate-agent same-model internal review recorded in [Review 04](../reviews/04_ANALYTIC_SIMPLICITY_OPENING_ROUND_REVIEW_20261023.md); no specialist review or priority claim.

This supports SIMP-02 in [Overview 02](../research-overview/02_ANALYTIC_RH_TO_SIMPLICITY_PROGRAM_20261023.md). It strengthens the existing finite positive-time transfer to retain the full endpoint Hermite spectrum at every positive time in its real-root interval. It does **not** acquire a theta upper bound. Follow the [result index](../../../../../result-summaries/README.md), [local heat geometry](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../../avoid/README.md), [target classification](../../../../../avoid/01_restating_the_target.md), and [control register](../../../../../result-summaries/12_collision_controls_and_screening.md).

## 1. Hypotheses and result

Let a complete real simple root system of H_t=-H_zz exist on 0<t<=T. For every globally adjacent pair a<b assume the complete root law

\[
 (b-a)'=\frac4{b-a}
 -2(b-a)\sum_{r\ne a,b}\frac1{(a-r)(b-r)},                 \tag{1}
\]

where the sum converges absolutely and contains every other root. These are the inherited canonical theta hypotheses under RH, not consequences of an arbitrary finite truncation. Let x_1(t)<...<x_m(t) be all descendants of one multiplicity-m endpoint site, so that they remain consecutive in the complete ordering. Write h_1<...<h_m for the zeros of the probabilists' monic Hermite polynomial He_m.

**Cluster comparison.** For every i<m and 0<t<=T,

\[
 0<x_{i+1}(t)-x_i(t)
 \le \sqrt{2t}\,(h_{i+1}-h_i).                           \tag{2}
\]

Consequently every pair in the cluster satisfies the corresponding bound obtained by summing (2). This uses the signed influence of the entire exterior population; it does not discard an unsigned error allowance.

For a finite population consisting of complete endpoint sites, define, as in [the spectral section](../../manuscript/spectral_forest.tex),

\[
 L(x)=\sum_{i<j}\frac{(e_i-e_j)(e_i-e_j)^T}{(x_i-x_j)^2},
 \qquad q(t)=\operatorname{Tr}\frac{4tL(x(t))}{I+4tL(x(t))}.
\]

With labels grouped by endpoint site a, (2) gives the **finite-time matrix lower bound**

\[
 4tL(x(t))\succeq\bigoplus_a 2L(h_{m_a}).                \tag{3}
\]

The block on the right has eigenvalues 0,1,...,m_a-1; a simple site contributes a one-dimensional zero block. Thus, putting
H_m=1+1/2+...+1/m,

\[
 \boxed{q(t)\ge\sum_a(m_a-H_{m_a})=:q_0.}                \tag{4}
\]

The previous manuscript proved this expression as a fixed-population t-down-to-zero limit, and proved M<=4q(t) separately from the coarser pair bound g^2<=8t. Formula (4) promotes the full limiting multiplicity cost to a lower bound at every permitted positive time. No height/time limits are exchanged, and monotonicity of q(t) itself is not asserted.

## 2. Cooperative gap proof

Set g_i=x_{i+1}-x_i. For r<i let D_{ri}=g_r+...+g_{i-1}, and for r>i+1 let D_{ir}=g_{i+1}+...+g_{r-1}. The isolated m-root gap vector field is

\[
 F_i(g)=\frac4{g_i}
 -2g_i\left\{\sum_{r<i}\frac1{D_{ri}(D_{ri}+g_i)}
 +\sum_{r>i+1}\frac1{D_{ir}(D_{ir}+g_i)}\right\}.          \tag{5}
\]

For every j!=i, increasing g_j weakly increases F_i: it increases one or more positive D denominators and leaves the other terms unchanged. Thus F is cooperative on the positive orthant and locally Lipschitz there. Also F(cg)=c^{-1}F(g).

Every root outside the cluster lies outside each internal adjacent pair. Its term in (1) is therefore nonpositive. The true vector satisfies

\[
 g'(t)\le F(g(t))\quad\hbox{componentwise}.              \tag{6}
\]

The Hermite root law gives the exact isolated solution
d_i(t)=sqrt(2t)(h_{i+1}-h_i), with d'=F(d) and every d_i'>0. For c>1,

\[
 (cd)'=cF(d)\ge c^{-1}F(d)=F(cd),                        \tag{7}
\]

strictly in every component. The standard local heat expansion is
x_i(t)=a+sqrt(2t)h_i+O(t), so g_i(t)/d_i(t)->1. For a sufficiently small eta>0, g(eta)<cd(eta). Cooperative comparison on [eta,T] gives g<=cd. Explicitly, at a first contact in component i, all other components are at most their comparison values, hence F_i(g)<=F_i(cd); the strict supersolution inequality prevents crossing. The positive gaps on every compact subinterval justify the locally Lipschitz comparison despite the singular endpoint t=0. Let c decrease to one to obtain (2).

For (3), each within-cluster edge weight satisfies
4t/(x_j-x_i)^2>=2/(h_j-h_i)^2. Their differences multiply positive semidefinite edge matrices. Intercluster edges are also positive semidefinite and can be dropped in a lower bound. The Hermite spectrum follows from its differential equation, as proved in the existing spectral section. Eigenvalue ordering, or operator monotonicity of u/(1+u), proves (4).

## 3. A joint negative-time/positive-time consumer

Use the same finite endpoint population in the complete negative-time resource R of [Note 10](10_SIMPLICITY_THEOREM_TARGETS_AND_HYBRID_CONSUMER_20261023.md) and in q(t). Thus

\[
 B:=\sum_{m_a\ge2}2\lfloor m_a/2\rfloor\le R,
 \qquad C:=\sum_a m_a(m_a-1),
 \qquad M:=\sum_{m_a\ge2}m_a.
\]

All windows, coverage weights, earlier populations and inward/outer flux remain in R. Then

\[
 \boxed{M\le\min\left\{N,C,\frac32R,4q(t),
             \frac{3R+C}{4},\frac58R+\frac32q(t)\right\}.} \tag{8}
\]

Only the last entry is new here. Its elementary site inequality is

\[
 m\le\frac58\,2\lfloor m/2\rfloor+\frac32(m-H_m),
 \qquad m\ge2.                                         \tag{9}
\]

For m=2k the slack is 9k/4-3H_(2k)/2; for m=2k+1 it is 9k/4+1/2-3H_(2k+1)/2. Each is zero at k=1 and increases with k, since its two-step increment is 9/4 minus 3/2 times the next two reciprocal integers. Equality holds exactly at doubles and triples. Summing (9), then using B<=R and (4), proves the new entry of (8).

The mixed entry improves both 3R/2 and 4q precisely when R>0 and

\[
 \frac14<\frac{q}{R}<\frac7{12}.                        \tag{10}
\]

This compares these two consumers only; the existing C entries can still be stronger. Its coefficients cannot both be decreased in the abstract two-input conversion: the quadratic and cubic heat births attain (9). No theta resource bound follows by selecting a desired ratio in (10).

There are also multiplicity-class restrictions. For k>=2, the number of endpoint sites with m>=k is at most q(t)/(k-H_k), and their total label mass is at most k q(t)/(k-H_k). The latter uses that H_m/m decreases, so m/(m-H_m) decreases. These are finite analytic consequences, not acquired numerical upper counts for zeta.

## 4. Controls, literature and research decision

The pure heat births e^(-t d_z^2)z^m attain (2)--(4). In particular the quadratic and cubic retain their collision cost; this theorem excludes neither. Any weighted-square, reflected, primitive-compatible or Euler-factor control satisfying the stated complete real-root motion also satisfies the comparison. Controls without such an interval fail that premise. No control must be rejected merely because a generic lower bound holds for it. The theta-close normalized endpoint controls can also satisfy the real-root hypotheses and keep their doubles: an independent upper bound below their cost is still missing. Sparse doubles are compatible with density conclusions.

The complete root equation is classical; see [Rodgers--Tao, Section 4](https://arxiv.org/abs/1801.05914), building on Csordas--Smith--Varga. The present argument is an explicit cooperative comparison using that equation and the inherited Hermite spectrum. The targeted literature check did not establish priority, and no novelty claim is made.

Classification under avoid/01: a proved **generic transfer improvement**, not an arithmetic restriction or a reformulation offered as evidence of simplicity. It resolves the loss of higher-multiplicity information in the prior finite-time comparison. SIMP-02 gains (4) and (8); SIMP-01 still needs a useful upper estimate for the actual canonical R or q (or another multiplicity-sensitive quantity). The companion arithmetic anchor in Note 13 improves a separate acquisition bottleneck, without paying those complete quantities.
