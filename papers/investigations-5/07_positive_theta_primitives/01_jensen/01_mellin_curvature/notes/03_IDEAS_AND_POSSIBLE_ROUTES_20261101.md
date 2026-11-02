# Understanding signed Mellin curvature and choosing a first attempt

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**, read from this chat's session metadata. Chat `01a19a10-57b7-7c52-940c-103fc06d15a5`.

**Scope:** the author's explanatory brainstorm begins J-B10's conceptual discussion. This is an orientation and route-selection note, not the completed bounded return required by [plan r1](../research-plan/01_MELLIN_CURVATURE_RESEARCH_PLAN_20261101.md). The Gaussian bound remains unproved. The elementary deductions below have same-assistant analytical checking only. No numerical acquisition, external theorem import, new coefficient range, or arbitrary-order result is claimed.

**Recommendation:** use the complete theta series and its differentiated first-term remainder as the input for an analytical large-Mellin-parameter estimate, retaining the entire signed determinant. Use an exact one-dimensional moment determinant to prepare the compact part. If the pointwise Gaussian comparison is too strong, compare the integrated Gaussian condition as the one alternative. Do not issue numerical execution until the tail, compact expression, errors and work limits have been fixed.

## 1. What the proposed mechanism would accomplish

There are two indices: determinant order r and coefficient index k. The accepted order-three signed averaging moves in k. The proposed curvature estimate would move from r=3 to r=4 through
\[
D_{4,k}D_{2,k}=D_{3,k}^2-D_{3,k-1}D_{3,k+1}.
\]
The current lower-order positivity is available, so the task is a quantitative comparison between adjacent order-three determinants. With
\[
M(k)=F_{3,k}D_{3,k},\quad F_{3,k}=(2k)!(2k+2)!(2k+4)!,
\quad Q_k=\frac{M(k-1)M(k+1)}{M(k)^2},
\]
the exact sign budget is
\[
B_k=\frac{(2k+6)(2k+5)}{2k(2k-1)}.
\]
Given the positive inputs, Q_k<B_k is exactly the next determinant's sign condition, not an independently acquired estimate. The stronger Gaussian comparison is
\[
Q_k\le G_k=\frac{2k+5}{2k-1},
\]
which would imply
\[
D_{4,k}\ge\frac3{k+3}\frac{D_{3,k}^2}{D_{2,k}}>0.
\]
At k=1, G_1=7 and B_1=28. This numerical gap illustrates the strength of the proposed comparison; it says nothing about the actual unknown Q_1. For large k, G_k=1+3/k+O(k^{-2}) while B_k=1+6/k+O(k^{-2}). Both allowances shrink towards one.

The continuous tilt w_s=q^s w_0, q=product u_j^2, moves weight towards larger products of source coordinates as s increases. It is an auxiliary Mellin parameter, not physical heat time. Write Z(s)=integral w_s, A(s)=E_s h_3, M(s)=Z(s)A(s). Accepted signed averaging gives A(s)>=A(0)>0 for real s>=0. It controls increase, not the rate at which that increase changes.

For T=log q and m=E_s T,
\[
\mathcal C(s)=(\log M)''(s)
=\operatorname{Var}_s(T)
+\frac{\operatorname{Cov}_s(h_3,(T-m)^2)}{A(s)}
-\left(\frac{\operatorname{Cov}_s(h_3,T)}{A(s)}\right)^2.
\]
The centered square is not increasing; association cannot sign its covariance with h_3. All three terms must be paid together. The Gaussian comparator is
\[
\kappa_3(s)=\sum_{j=0}^2\sum_{n\ge0}(s+j+\tfrac12+n)^{-2}.
\]
The hierarchy is pointwise C<=kappa, then its triangularly weighted integral on each [k-1,k+1], then Q_k<=G_k, then the exact determinant sign condition. The first implication follows from
\[
\log Q_k=\int_{k-1}^{k+1}(1-|s-k|)\mathcal C(s)\,ds,
\quad
\log G_k=\int_{k-1}^{k+1}(1-|s-k|)\kappa_3(s)\,ds.
\]
Pointwise failure would leave the integrated comparison open. These are identities and sufficient targets, not positivity progress. The [initial assessment](01_INITIAL_BRANCH_EVALUATION_20261101.md) contains their derivations and Gaussian normalization.

## 2. A useful consequence of the accepted theta inputs: h3 is below one

Avoid the conflicting use of T for a source ratio: here write S=Phi^(4)/Phi and S=g(R), R=Phi''/Phi. The accepted source inequality is g'''(R)>0. The complete-source differentiated tail in [Note07, Section 4](../../notes/07_J_E01_R2_SIGNED_AVERAGING_AND_Q10_P7_RETURN_20261101.md) gives, for t=pi exp(4u),
\[
R'=128t^2-352t+O(t^{-1})+O(t^3e^{-3t}),
\]
\[
C=R'S''-S'R''=2^{22}t^6-39\cdot2^{20}t^5+O(t^4)+O(t^8e^{-3t}).
\]
Consequently
\[
g''(R(u))=C/(R')^3\longrightarrow 2.
\]
Since g'' is strictly increasing and has this finite upper limit, g''(x)<2 throughout the source interval. The divided-difference formula has simplex area 1/2:
\[
h_3(\mathbf u)=\int_{a,b\ge0,\ a+b\le1}
g''((1-a-b)R(u_1)+aR(u_2)+bR(u_3))\,da\,db<1.
\]
This includes coincident nodes by continuity. The regular x=u^2 origin formulas in the same note give a finite lower endpoint for g'', so h_3 is also bounded below. Its negative origin region remains present. This deduction uses the full-source error, not an asserted reflection property of the first theta term.

Define beta=1-h_3>0 and epsilon(s)=E_s beta=1-A(s). Then
\[
0<\epsilon(s)\le1-A(0)<1,\qquad \epsilon'(s)\le0,
\]
and exactly
\[
\mathcal C(s)=\operatorname{Var}_s(T)
-\frac{\epsilon''(s)}{1-\epsilon(s)}
-\frac{\epsilon'(s)^2}{(1-\epsilon(s))^2}.
\]
This makes the remaining issue intuitive: the deficit decreases, but its second derivative is not controlled. A negative epsilon'' raises curvature. Splitting off beta has not made the original signed density positive: beta can exceed one where h_3 is negative.

The boundedness addition alone still fails in an information relaxation. In the initial assessment's two-point example, rescale h-values from (1,2) to (1/4,1/2), keeping q in {1,128} and base weights (128,1). Now h<1, A>0 increases and epsilon=1-A decreases within (0,1), but Q is unchanged:
\[
Q_1=16705/576>28.
\]
This example lacks canonical derivative-determinant and Toeplitz realization. It excludes inference from association, monotonicity and the upper bound alone, not a theta-specific deficit estimate. No convexity of epsilon or log-concavity of A is proved here.

## 3. Recommended analytical route and a compact representation

The proposed input is the explicit complete theta series, with its differentiated remainder after the n=1 term. It adds quantitative tail information absent from the two-point relaxation. The first research question is whether it gives a useful curvature estimate for the complete signed M, with relative errors that survive two derivatives in s.

There is an exact simplification for that attempt. Put
\[
H_{ij}^{[p]}(s)=\int_0^\infty u^{2s+2j}(2\log u)^p\Phi^{(2i)}(u)\,du,
\quad i,j,p\in\{0,1,2\}.
\]
Expansion of the two determinants in the ordered-chamber representation gives
\[
M(s)=\det H^{[0]}(s).
\]
Indeed the full-orthant integral is 3! times the ordered one, and expansion and Fubini identify it with 3! det H. This uses no integration by parts at noninteger s. M' is the sum of the three determinants with one column replaced by its H^[1] column. M'' is the sum with one H^[2] column plus twice the sum with two distinct H^[1] columns. Thus 27 scalar integrals describe M,M',M'' without increasing the source derivative order beyond four.

The joint comparison numerator is
\[
\mathcal N(s)=\kappa_3(s)M(s)^2-M(s)M''(s)+M'(s)^2.
\]
Since M(s)>0, N>=0 is equivalent to the selected pointwise Gaussian inequality. This is an exact representation of the same obligation, not a bound. Its concrete advantage is that a future compact method can use one-dimensional source integrals, retain their correlations and avoid divisions by Vandermondes at coincident nodes. Separate absolute interval boxes might still destroy the cancellation and must be assessed before execution.

**Domain payments.** For s in any compact subset of [0,infinity), u^(2s+2j)|log u|^p is integrable at zero, the source derivatives are bounded there, and complete theta decay controls infinity. This justifies the displayed differentiation and Fubini operations. It does not prove N's sign on any interval. In particular [0,2] remains unpaid, as does any intervening compact range and an effective unbounded s-tail. The tail in the spatial variable u and the tail s->infinity are different obligations.

**Formal tail prediction, not an estimate.** Ignoring lower-order factors only to locate the saddle, the exponent is 2s log u-pi exp(4u). Its stationary point u_s solves
\[
u_s e^{4u_s}=s/(2\pi).
\]
The leading stationary exponent has second s-derivative 2/[s(1+4u_s)]. Three nodes therefore suggest
\[
\mathcal C(s)\ \hbox{of scale}\ \frac{6}{s(1+4u_s)}
=O((s\log s)^{-1}),
\quad \kappa_3(s)\sim3/s.
\]
This suggests room in the Gaussian bound at large s. It is not a theorem for M: a proof must handle node repulsion, coalescence, mixed configurations with a node outside the saddle region, the signed h factor, full theta corrections, and differentiated relative remainders. An asymptotic for M with an undifferentiated error is insufficient for log-curvature. No threshold or tail constant has been acquired.

The practical priority is therefore one rigorous signed-tail argument, alongside the exact compact formula above. If it leaves only finite verification, specify the cutoff, endpoint treatment, normalized joint expression, full tails, error correlations and precision/refinement caps in a separate E/Sol contract. No such contract is issued by this discussion.

## 4. One alternative and the decision boundary

If the pointwise comparator fails or its proof introduces an unnecessary obstacle, retain the source and test the integrated Gaussian comparison directly. It permits local regions with C>kappa when other regions compensate. A direct integer method would also avoid needing higher-order real-tilt positivity in a future induction, although it would still need an estimate at each arbitrary finite order.

Changing to this comparator must be explicit. Proving only Q<B would prove the determinant sign but would lose the proposed Gaussian margin. Existing order-four positivity cannot be invoked to establish a new mechanism. A finite r=3 pilot remains distinct from the unresolved arbitrary-order/small-index problem.

## 5. Controls, status and next step

Read with the [result index](../../../../../../result-summaries/README.md), especially [theta inputs](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [collision controls](../../../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../../../avoid/README.md), especially [reformulations](../../../../../../avoid/01_restating_the_target.md), [joint estimates](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

The Gaussian has h=1 and checks the existing comparison's normalization; the strict theta deficit does not apply to it. The rescaled two-point relaxation above shows the new upper bound is insufficient by itself, but fails canonical realization. Euler-factor, reflected super-Gaussian and smooth positive-primitive controls lack the exact complete theta expansion used in the proposed tail route; their quantitative curvature is untested here. Weighted-square and finite-prime perturbations also lack the unchanged full-source reconstruction, and the relevant finite-endpoint versions lack full reflection. Positive-time collisions do not assign a sign to this time-zero finite-order inequality. The moment-determinant identity is generic and excludes none of these controls merely by existing.

No new all-domain estimate or completed J-B10 return is recorded. The source deduction h_3<1 and the exact moment representation are preliminary analytical observations, with no independent review. The next numbered bounded return must distinguish them from any subsequently proved estimate.

**Next: [B] J-B10 — Astra.** Work one full-theta, signed large-s curvature estimate and decide whether it supports the original Gaussian comparator plus a finite compact contract; otherwise return its precise failure. The integrated Gaussian comparison is the single explicit alternative. Numerical execution remains gated under plan r1.
