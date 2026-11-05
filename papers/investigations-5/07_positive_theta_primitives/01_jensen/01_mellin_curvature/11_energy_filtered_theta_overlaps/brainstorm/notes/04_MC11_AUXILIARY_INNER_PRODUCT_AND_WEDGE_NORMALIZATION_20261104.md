# Auxiliary inner product and exterior product normalization

4 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance from **gpt-6-astra (Codex), reasoning effort xhigh**, recorded for this turn. Thread `01a1a9d4-3d44-7472-ae0f-54705423d86b`, MC11 history0002. This explanatory note specifies the existing Hilbert-space metric and wedge convention. It retains [Note03's distinction](03_MC11_THERMAL_PARAMETER_AND_ORBITAL_TERMINOLOGY_20261104.md) between auxiliary source functions and physical single-particle states; no new estimate or E04 assessment is made.

## The base inner product

At a fixed filter setting s, the auxiliary space is
\[
\mathcal H=L^2((0,\infty),du;\mathbb C),\qquad
\langle a,b\rangle_{\mathcal H}=\int_0^\infty\overline{a(u)}b(u)\,du.
\]
This convention is conjugate-linear in the first argument and linear in the second. The source functions used here are real. The measure is ordinary du; there is no additional Phi_s weight. The source factors have already been placed inside f_i and g_j. The metric is fixed as s varies; the vectors change.

With u=log(beta)/4, the same metric is
\[
\langle a,b\rangle=\int_1^\infty
\overline{a(\tfrac14\log\beta)}b(\tfrac14\log\beta)
\frac{d\beta}{4\beta}.
\]
This change of variable specifies the mathematical weighting across inverse temperatures, not a physical Born-rule interpretation for temperature.

## Realization of the exterior power

The qth Hilbert exterior power can be realized as the antisymmetric subspace of L²((0,infinity)^q,du_1...du_q). In the convention used by the [original source-pairing note](../../../02_fermionic_correlators/notes/01_THETA_ORBITAL_COMPARISON_RETURN_20261101.md), a wedge of orthonormal vectors has norm one. Its coordinate realization is
\[
(a_1\wedge\cdots\wedge a_q)(u_1,\ldots,u_q)
=\frac1{\sqrt{q!}}\det[a_i(u_j)]_{i,j=1}^q.
\]
This normalization is fixed; it does not normalize arbitrary wedges. If the a_i are not orthonormal, their Gram determinant supplies the squared norm.

The inner product in this antisymmetric subspace is the inherited product-measure integral:
\[
\langle A,B\rangle_{\wedge^q\mathcal H}
=\int_{(0,\infty)^q}\overline{A(u_1,\ldots,u_q)}
B(u_1,\ldots,u_q)\,du_1\cdots du_q.
\]
The variables u_1,...,u_q are independent copies of the integration variable. A wedge is not a product of all the functions evaluated at one common u.

Expanding the two determinants and integrating gives
\[
\frac1{q!}\int_{(0,\infty)^q}
\overline{\det[a_i(u_j)]}\det[b_i(u_j)]\,d\mathbf u
=\det\!\left[\int_0^\infty\overline{a_i(u)}b_j(u)\,du\right].
\]
Each product integral factors into one-variable pairings; grouping the two permutation sums leaves q! identical contributions, canceling the displayed factor. Absolute integrability of each factor follows from Cauchy-Schwarz for L² vectors. Hence
\[
\boxed{\langle a_1\wedge\cdots\wedge a_q,
 b_1\wedge\cdots\wedge b_q\rangle
=\det[\langle a_i,b_j\rangle].}
\]
An unscaled determinant in coordinates would instead produce an extra factor q! under the same product-measure inner product. The coordinate normalization and the wedge metric must be kept consistent.

## The MC11 source functions

Suppress s in the notation. The real functions are
\[
f_i=\frac{\Phi^{(2i)}}{\sqrt\Phi},\qquad
g_\ell=\frac{u^{2\ell}}{(2\ell)!}\sqrt\Phi.
\]
Their ordinary L² pairing is
\[
\langle f_i,g_\ell\rangle
=\int_0^\infty\Phi^{(2i)}(u)\frac{u^{2\ell}}{(2\ell)!}\,du.
\]
For the diagonal block 0<=i<q and q<=ell<2q, integration by parts 2i times gives
\[
\langle f_i,g_\ell\rangle
=\int_0^\infty\Phi(u)\frac{u^{2(\ell-i)}}{(2(\ell-i))!}\,du
=c_{\ell-i}.
\]
The sign is positive because 2i is even. The polynomial and the derivatives needed in the boundary terms vanish at the origin for this index range, while the source decay handles infinity. This is the filtered diagonal identity; it is not an assertion that arbitrary filtered blocks have the same endpoint cancellation. [MC11 overview](../../research-overview/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_OVERVIEW_20261104.md)

Consequently,
\[
F_q=f_0\wedge\cdots\wedge f_{q-1},\qquad
G_q=g_q\wedge\cdots\wedge g_{2q-1},
\]
\[
\boxed{\langle F_q,G_q\rangle
=\det[c_{q+j-i}]_{i,j=0}^{q-1}=D_q.}
\]
For q=2 this reads
\[
\langle f_0\wedge f_1,g_2\wedge g_3\rangle
=\langle f_0,g_2\rangle\langle f_1,g_3\rangle
-\langle f_0,g_3\rangle\langle f_1,g_2\rangle
=c_2^2-c_1c_3.
\]

## Positivity and normalization

For F=a_1 wedge ... wedge a_q,
\[
\|F\|^2=\det[\langle a_i,a_j\rangle]\ge0.
\]
This is a Gram determinant. A cross-pairing between two different wedges may be negative even though the Hilbert metric is positive definite. Whenever F_q and G_q are nonzero, their normalized pairing is
\[
\frac{D_q}{\sqrt{\det[\langle f_i,f_j\rangle]_{i,j=0}^{q-1}
\det[\langle g_{q+i},g_{q+j}\rangle]_{i,j=0}^{q-1}}}.
\]
MC11's reported response concerns D_q itself. The source vectors are not assumed orthonormal, and their individual Gram matrices cannot be replaced by identity.

These definitions explain the determinant representation without adding a physical state interpretation or a sign theorem. For repository context, see the [result index](../../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [patterns index](../../../../../../../../avoid/README.md), and [re-realizations caution](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md).
