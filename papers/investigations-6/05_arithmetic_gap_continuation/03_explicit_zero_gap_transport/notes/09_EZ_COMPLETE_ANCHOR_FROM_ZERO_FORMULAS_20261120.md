# Summing the unlocated exterior at an all-real anchor

20 November 2026. Prepared for Edward Baker with OpenAI Codex assistance. The desktop thread records gpt-6.2-astra, ultra effort. No separate per-turn configuration is recorded. Analytical estimate for initialization at one time.

The explicit zeros in [parent brainstorm Note 08, (1)–(4)](../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md) give the two marked endpoints and a counted list of neighbors. This note uses the even product at the same time to account for every zero outside that list. The output is an enclosure of each prescribed split moment, including \(M_n\), that can be inserted in the physical gap law. [Parent integer recurrence](../../manuscript/sections/03_hierarchy.tex) · [Root-location errors and the uniform large-time window](08_EZ_LOCALIZATION_TO_MIXED_MOMENTS_20261120.md)

## Data at time \(T\)

Take an independently established all-real anchor for the even physical field \(H(T,\cdot)\), with \(H(T,0)>0\), the parent's paired product and \(\sum_{k\ge1}r_k^{-2}<\infty\). List the positive zero occurrences \(r_k\) in increasing order, retaining multiplicity. Know the first \(K\) with their counts, including the marked simple adjacent endpoints \(a=r_n,\ b=r_{n+1}\). Supply \(0<a<b\le A<R\) and a lower bound \(r_k\ge R\) for all \(k>K\). For example a counted prefix extending past the target can supply \(R\) from a lower bound on its outermost root. The first \(K\) positive roots and their reflections form the head. Both \(-a\) and \(-b\) belong to the exterior. Here \(a\) is the left endpoint. Denote the source mean in the founding note by \(\mu_T\).

From the founding expansion \(r_k=Y((k-\tfrac12)\pi)/\mu_T\), a certified error in \(Y\) is divided by \(\mu_T\) to obtain a position error when the mean is known exactly. With interval source data propagate the uncertainty of the mean too. Alternatively the residue series has position error at most \(r\eta^{j+1}/[L_T(j+1)(1-\eta)]\) after \(j\) terms on its indexed circle of radius \(r\) and ratio bound \(\eta<1\). The convergent inverse and the cubic resummation have their own ranges and remainders. Use the same positions for every row and every adjacent pair. [Parent brainstorm Note 08, §§1–4](../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md)

For \(j\ge1\) the exterior beyond the head has the nonnegative radial power sum
\[
 U_j=\sum_{k>K}r_k^{-2j}
   =-j[v^j]\log\!\left(\sum_{h\ge0}
          \frac{(-1)^h\mathbb E_T U^{2h}}{(2h)!}v^h\right)
      -\sum_{k=1}^{K}r_k^{-2j}.
\]
Here \(U\) under \(\mathbb E_T\) is the frequency variable in the normalized theta integral. The logarithm of \(\prod_k(1-v/r_k^2)\) near zero proves the identity. Each coefficient uses source moments only through order \(2j\). In particular \(U_1=\mathbb E_T U^2/2-\sum_{k\le K}r_k^{-2}\). Enclosures for the coefficient and the head propagate by subtraction. The difference can be much smaller than either input, so an application must report the resulting width. [Founding product and radial sums, §3](../../01_jacobi_integer_hierarchy/brainstorm/notes/07_LARGE_TIME_FACTORIZATION_AND_BACKWARD_PROPAGATION_20261120.md) · [Paired product and count](../../manuscript/sections/02_pair_chain.tex)

## Every integer split row

Fix \(p,q\ge0\), \(m=p+q\ge2\). The row \(S_{n,p,q}\) uses weights \((\rho-b)^{-p}(\rho-a)^{-q}\). Set
\[
 h_d=[v^d]\,(1-bv)^{-p}(1-av)^{-q}.
\]
The pair of exterior occurrences \(+r_k,-r_k\) contributes the sum of the expansions with signs \(1\) and \((-1)^{m+d}\) at degree \(d\). Thus the exact complement to the finite head is
\[
 S^{\rm tail}_{n,p,q}
     =2\sum_{\substack{d\ge0\\m+d\ {\rm even}}}h_d U_{(m+d)/2}.
 \tag{1}
\]
The sum includes the axes \(p=0\) or \(q=0\). All retained coefficients are nonnegative for the chosen positive endpoints. For \(z=A/R<\sigma<1\), truncating before degree \(L\ge0\) gives
\[
 0\le S^{\rm tail}_{n,p,q}
 -2\!\!\sum_{\substack{0\le d<L\\m+d\ {\rm even}}} h_d U_{(m+d)/2}
 \ \le\ \frac{2R^{2-m}U_1}{(1-\sigma)^m}(z/\sigma)^L.
 \tag{2}
\]
Indeed \(h_d\le {m+d-1\choose d}A^d\). On each orbit majorize \(r_k^{-m}\le R^{2-m}r_k^{-2}\) and \((A/r_k)^d\le (z/\sigma)^L\sigma^d\) for \(d\ge L\). Summing the binomial series proves (2) and absolute convergence. The bound is uniform over all targets with the same \(A,R\) and fixed order \(m\). The displayed dependence on \(m\), the ratio \(A/R\), and the uncertainty of \(U_j\) matters if a time recurrence uses successively higher orders.

## The row entering the gap

For \(M_n=S_{n,1,1}\), the first tail term is \(2U_1\). Here \(h_{2j}=\sum_{i=0}^{2j}b^i a^{2j-i}\). A simple bracket, using just one complete source coefficient, is
\[
  2U_1\ \le M_n^{\rm tail}
       \ \le 2U_1+2A^2 U_2\,\frac{3-z^2}{(1-z^2)^2},
       \qquad U_2\le R^{-2}U_1 .
 \tag{3}
\]
This follows by bounding \(h_{2j}\le(2j+1)A^{2j}\) for \(j\ge1\) and using \(U_{j+1}\le R^{-2(j-1)}U_2\). An exact \(U_2\) uses the fourth source moment. The same expansion gives successively finer bounds at fixed clearance. The exterior entries in the head use actual position differences with their interval errors, as in [Note 08](08_EZ_LOCALIZATION_TO_MIXED_MOMENTS_20261120.md).

The primary use of these data is
\[
 g_n'=4/g_n-2g_nM_n,\qquad
 D_n'=2-g_n^2M_n,\qquad D_n=g_n^2/4.
\]
Evaluate \(2-g_n^2M_n\) with the same target endpoints in the gap and in the denominators. When the two terms nearly cancel, their common errors can determine the sign. The full mixed hierarchy then gives instantaneous time derivatives from this same exterior. Formulas (1)–(3) provide a complete single-time input and a truncation cost for it. They supply no time interval, fixed-time uniform-in-height localization, or improvement in the de Bruijn–Newman bound. The all-real and positivity hypotheses of the tail estimate require independent justification wherever it is used again. [Backward cumulative comparison](../../manuscript/sections/04_continuation.tex) · [Proposed time estimate](07_EZ_ZERO_FORMULAS_AND_MIXED_HIERARCHY_CONTINUATION_20261120.md)

## A signed gap estimate from the positions and the exterior

In a smaller growing range of indices the degree-zero tail term in (1) resolves the cancellation in the gap equation. Write \(\mu=\mathbb E_T U,\ \ell=\mu\sqrt\kappa,\ y_j=\mu r_j,\ q_j=(j-\tfrac12)\pi\), and extend by reflection \(y_{1-j}=-y_j\). Fix \(K\asymp\ell\) inside a fixed multiple of the inverse window. As \(T\to\infty\), uniformly for \(n+1\le\sqrt\ell\),
\[
 \ell^2\big(g_n^2M_n-2\big)
   =\pi^2+O\!\left(\kappa^{-1/2}+(n+1)^2/\ell\right).
 \tag{4}
\]
The constants depend on the fixed window and the comparisons for \(K/\ell\). In particular \(D_n'<0\) uniformly on any family \(n+1=o(\sqrt\ell)\) at sufficiently large time. The argument estimates the actual exterior first. The existing current-based theorem gives the same leading drift on a wider large-time window. [Current-based comparison](../manuscript/transport.tex)

To prove (4), set \(\beta=(\sqrt\kappa\,\ell^3)^{-1}\). On a complex disk larger by a fixed factor than all the retained levels, the inverse satisfies \(|Y(q)-q|\ll\kappa^{-1/2}\) and \(Y(q)-q\) vanishes to order three at zero. Indeed \(Y=q+H_o(Y)\) and \(H_o\) has that vanishing order. The larger disk follows by increasing the fixed constant in the founding estimate. Apply the maximum principle to \((Y-q)/q^3\) there and Cauchy to its derivative on a smaller disk. This gives \(|Y'(q)-1|\ll\beta |q|^2\) at the retained real levels and between them. Consequently each signed separation \(y_i-y_j\) has relative error \(O(\beta(q_i^2+q_j^2))\) against \(q_i-q_j\). These bounds are \(o(1)\) even at the edge of the head. [Inverse and variance estimates, §§3–5](../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md)

Compare \(M_n/\mu^2\) with the complete dimensionless lattice moment \(2/\pi^2\). On \(1-K\le j\le K\), omit \(j=n,n+1\). The reciprocal product estimate bounds the difference of the two heads by
\[
 C\beta\sum_j\frac{j^2+(n+1)^2+1}{|j-n|\,|j-n-1|}
       \ \ll\ \beta(K+(n+1)^2).
\]
For the last inequality use \(j^2\le 2(j-n)^2+2n^2\) and the summability of the reciprocal product with both marked indices excluded.

In the tails, \(y_K\asymp K\) and \(y_{n+1}=O(n+1)\). Their ratio is eventually below \(1/2\) in the range of (4). Both the true tail and the clock tail beyond their own degree-zero terms are \(O((n+1)^2/K^3)\). Indeed (3) in dimensionless coordinates uses a fourth-power tail at most \(O(K^{-2})\) times the inverse-square tail, which is \(O(K^{-1})\) by [Note 08, (2)](08_EZ_LOCALIZATION_TO_MIXED_MOMENTS_20261120.md). For the clock use \(\sum_{j>K}q_j^{-4}=O(K^{-3})\). The difference of the two degree-zero terms is exactly
\[
 2\sum_{j>K}(y_j^{-2}-q_j^{-2})
   =\frac{\operatorname{Var}_T(U)}{\mu^2}
     -2\sum_{j\le K,\,j\ge1}(y_j^{-2}-q_j^{-2})
   =\frac{\operatorname{Var}_T(U)}{\mu^2}+O(\beta K).
\]
Here \(\sum_{j\ge1}q_j^{-2}=1/2\). Each positive-head error is \(O(\beta)\) since \(|Y(q)-q|\ll\beta |q|^3\) there. Thus the complete radial source coefficient pays precisely the term that would be lost on dropping the far exterior.

Finally \(\mu g_n=\pi(1+O(\beta(n+1)^2))\), and the saddle gives \(\kappa\operatorname{Var}_T(U)=1+O(\kappa^{-1/2})\) from its second moment about the saddle and the squared shift of the mean. Multiplying the head and tail comparison for \(M_n/\mu^2\) by \((\mu g_n)^2\) proves (4). In this range the positive leading contribution to \(g_n^2M_n-2\) is \(\pi^2\operatorname{Var}_T(U)/\mu^2\).

For a common large-time interval \([t,T]\) and a fixed label in each path, apply (4) at every \(v\in[t,T]\) with a common window constant. If \(t\to\infty\) and \(\sup_{v\in[t,T]}(n+1)^2/\ell_v\to0\), the uniform backward increment is
\[
 D_n(t)-D_n(T)
 =\big(\pi^2+o(1)\big)\int_t^T\ell_v^{-2}\,dv .
 \tag{5}
\]
The indexed real roots must lie on a common counted path, as supplied by the founding large-time labels in this regime. This integration uses the position and exterior estimates on every slice. Continuing from a single anchor down to a fixed small time still requires a time-remainder estimate for the hierarchy. Equations (4)–(5) recover known large-time widening from the generalized hierarchy's first interaction and the canonical variance. They give the scale that a remainder must resolve.

## Controls and status

For an even cosine the data have half-integer lattice zeros. If \(g\) is their spacing, summing the complete translated lattice gives \(g^2M=\sum_{j\in\mathbb Z\setminus\{0,1\}}[j(j-1)]^{-1}=2\) by telescoping each side. Thus the primary readout gives the exact stationary gap. The symmetric orbit sum (1) also follows term by term from this product. Collision examples with an all-real anchor can satisfy the anchor algebra and later collide. The failed premise for continuation is a strict integrated margin at the collision, or earlier loss of the independently counted path. Finite theta-tail and weighted-square controls with nonreal divisors fail the global real-product premise. The specific parent source in (1) must be replaced by a control's own moments when testing it. The per-family screening for a claim at lower time is in the [continuation](07_EZ_ZERO_FORMULAS_AND_MIXED_HIERARCHY_CONTINUATION_20261120.md). [Project controls](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Scope of exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
