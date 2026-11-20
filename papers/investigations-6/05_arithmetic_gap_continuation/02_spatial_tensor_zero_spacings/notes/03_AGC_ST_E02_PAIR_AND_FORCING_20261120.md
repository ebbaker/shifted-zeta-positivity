# Pair drift and forcing from the spatial split

20 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex LLM assistance. Executor dispatched as gpt-6.2-sol, effort ultra. Serving configuration has no separate attestation. AGC-ST-E02 r1, exact matching on the stated chart, pending separate assessment.

Use the literal theta field in forward physical time \(H_t=-H_{zz}\). The marked cell encloses two zero occurrences throughout a compact cleared chart. The contour is conjugation-invariant when real \(c,D\) are required. As in [AGC §6](../../manuscript/sections/06_residual_transport.tex), the count and boundary clearance hold throughout the chart. Use the complete even product and uniform count of [AGC §2](../../manuscript/sections/02_pair_chain.tex), with all exterior occurrences and their multiplicities included. The fixed comparison is the direct pair and moment readout on the same field and contour. [Frozen request](../research-progress/handoffs/AGC_ST_E02_REQUEST_R1_20261120.md) · [E01 split generator](02_AGC_ST_E01_SPLIT_GENERATOR_20261120.md)

## The counted quadratic

Let \(w=z-c\), \(P=w^2-D\), \(H=PA\), \(R=A_z/A\), and \(B=H_z/H\). Write \(s^2=D\), \(a=c-s\), \(b=c+s\). At a separated pair the remainder of \(R\) modulo \(P\) is \(\alpha+\beta w\), where
\[
 \alpha=\tfrac12\big(R(a)+R(b)\big),\qquad
 \beta=\frac{R(b)-R(a)}{b-a}.
\]
At a double this is the Hermite remainder with \(\alpha=R(c)\) and \(\beta=R_z(c)\). Both coefficients are analytic through \(D=0\), as the symmetric Taylor combinations at the two roots show. By E01, holding physical \(z\) fixed,
\[
 -2c_t w-D_t=P_t=-\operatorname{rem}_{P}\big(2+4wR\big)
                  =-4\alpha w-2-4D\beta .
\]
Thus
\[
 c_t=2\alpha,\qquad M=-\beta,\qquad D_t=2-4DM .                   \tag{1}
\]
At a double \(c_t=2R(c)\), \(D_t=2\), and \(M=-R_z(c)\). The slope drops out of \(D_t\) at that instant.

With \(\mathcal I f=(2\pi i)^{-1}\oint_\Gamma f\,dz\) the count gives \(c=\mathcal I(zB)/2\) and \(D=\mathcal I(z^2 B)/2-c^2\). From E01, \(H_{zz}/H=-P_t/P\) plus a holomorphic term in the cell. The direct §6 drift is \(\mathcal I(wH_{zz}/H)\). Since \(\mathcal I(w/P)=1\) and \(\mathcal I(w^2/P)=0\) by total residues at the two targets, this gives \(D_t\) in (1). Its corresponding center formula \(\tfrac12\mathcal I(H_{zz}/H)\) gives \(c_t\). These identities also hold when both poles coalesce. [AGC §2, pair law](../../manuscript/sections/02_pair_chain.tex) · [AGC §6, exact gap readout](../../manuscript/sections/06_residual_transport.tex)

## Complete moments from the same exterior input

For an exterior occurrence \(\rho\) put \(y_\rho=\rho-c\) and \(Q_\rho=y_\rho^2-D\). Define \(S_n=\sum_{\mathrm{ext}} Q_\rho^{-n}\) for \(n\ge1\), and \(T_n=\sum_{\mathrm{ext}} y_\rho Q_\rho^{-n}\) for \(n\ge2\). The log derivative of the even product can be taken in opposite pairs. For each occurrence the negative endpoint divided difference of its pole is \(Q_\rho^{-1}\); spatially constant regularizers vanish in the difference. The sum of these differences is absolute, so \(M=S_1\), including the Hermite value at the double. The fixed-order tails are \(O(R_0^{1-2n}\log R_0)\) and \(O(R_0^{2-2n}\log R_0)\), respectively, at exterior radius \(R_0\). These orders are summable by the uniform zero count. A cleared compact chart keeps the remaining exterior denominators bounded away from zero. Conjugate occurrences contribute conjugate summands on a real chart. Their sums are real under the conjugation symmetry, with no termwise positivity assumption for nonreal occurrences.

For the stated orders the readouts are
\[
 S_n=-\mathcal I(P^{-n} B)=-\mathcal I(P^{-n}R),\qquad
 T_n=-\mathcal I(wP^{-n} B)=-\mathcal I(wP^{-n}R).                \tag{2}
\]
For either weight \(k=P^{-n}\) or \(k=wP^{-n}\), the total target residue of \(kP_z/P\) is zero by its decay at infinity. The integral of \(k\) is also zero, so the spatially constant product regularizers make no contribution. For an exterior pole \(1/(z-\rho)\), the sum of the residues of \(k/(z-\rho)\) inside \(\Gamma\) equals \(-k(\rho)\). The complete product permits passage of these contour integrals from finite products. The same residue argument applies to multiple exterior occurrences by summing repeated poles with their multiplicity. [AGC §3, rational traces](../../manuscript/sections/03_hierarchy.tex)

In particular \(\mathcal F=12S_2+16DS_3\) is recovered in full by applying (2) to the single weight \(12P^{-2}+16DP^{-3}\). A finite exterior child contributes exactly the terms for its divisor, via the sibling logarithmic response of E01, and the remaining exterior germ supplies the rest. In the moment formula the weight and contour are common. The direct parent uses that same divisor, trace and weight.

The two E01 samples give \(\alpha,\beta\) on a separated chart. Higher residues need additional spatial data. With \(h=b-a\ne0\), for example,
\[
 S_2=\frac{2\beta-R_z(a)-R_z(b)}{h^2}.
\]
This follows by taking the two second-order pole residues in (2), and exhibits the dependence on slopes absent from the root values. At a double the single E01 sample gives the instantaneous quadratic velocity but leaves all of
\[
 M=-R_z(c),\qquad
 T_2=-R_{zz}(c)/2!,\qquad
 S_2=-R_{zzz}(c)/3!,\qquad
 S_3=-\partial_z^5 R(c)/5!
\]
as further data. At the double \(\mathcal F=12S_2\). Full exterior germs at the target roots supply the jets in (2). Equivalently the common boundary trace, together with the divisor, supplies the interior \(R\) by Cauchy's formula. This is an information statement about the quotient and residue maps on analytic germs. It makes no assertion about varying the canonical field while its root values are fixed.

## First regular time rows

Specialize the symmetric recurrences of [AGC §3](../../manuscript/sections/03_hierarchy.tex). In the \(S_n\) recurrence, \(n=1\) gives the product \(2S_1^2\) and diagonals \(-12S_2,-16DS_3\). At \(n=2\) the two first-sum terms give \(8MS_2\), and the single term in the second sum gives \(4T_2^2+4DS_2^2\). Its diagonals are \(-32S_3,-40DS_4\). In the \(T_2\) row the two sums give \(6MT_2\) and \(8DS_2T_2\); the diagonals give \(-20T_3,-40DT_4\). Hence the assembled readouts obey
\[
\begin{aligned}
 M_t&=2M^2-12S_2-16DS_3,\\
 (S_2)_t&=8MS_2+4DS_2^2+4T_2^2-32S_3-40DS_4,\\
 (T_2)_t&=6MT_2+8DS_2T_2-20T_3-40DT_4.                          \tag{3}
\end{aligned}
\]
In particular the first spatially odd moment enters the \(S_2\) row through \(+4T_2^2\). In backward time \(u=t_*-t\), \(c_u=-2\alpha\), \(D_u=-2+4DM\) and \(M_u=-2M^2+\mathcal F\). The right-hand sides of the \(S_2,T_2\) rows, including the mixed products, each change sign in full. The definition of \(\mathcal F\) at the sampled slice is the same in either time coordinate.

For the precise finite-to-complete passage, fix a physical slice. Truncate the complete opposite-paired product retaining the targets, all conjugates, ties and multiplicities, and initialize an exact finite polynomial heat solution at that slice from each truncation. Local uniform convergence of the paired products and Cauchy's formula give convergence of spatial jets through order three on the fixed cleared target contour. The first physical time jet of the trace follows there from \(B_t=-B_{zz}-2BB_z\), so it converges as well. The differentiated count moments give the first jets of \(c,D\), and consequently of the time-dependent kernels in (2) on the contour. This proves convergence of the first time derivatives of the finite trace readouts at the slice. A finite polynomial slice with multiple roots is obtained by perturbing its factors to simple roots inside disjoint cleared neighborhoods and taking the limit using the same contour readouts and time jets. In the finite simple algebra the first powers are used only before the cancellation. Once canceled in the symmetric recurrence, every entry and product in (3) has an absolute fixed-order limit. This argument is slice-wise on the physical chart and requires neither a common time interval for polynomial truncations nor uniform estimates with increasing moment order.

Equivalently, (2) differentiated on the cleared contour yields
\[
 \partial_t[-\mathcal I(kB)]
    =-\mathcal I\big((k_t-k_{zz})B+k_z B^2\big),                 \tag{4}
\]
using the same deformation and integration by parts as in E01. The weights may have poles inside, and the integrations by parts use their holomorphic restrictions to the collar. Formula (1) supplies the \(c_t,D_t\) in \(k_t\). Thus one exact trace at a slice also determines the first time rows directly with the given heat law. The few coefficient-velocity samples alone lack the higher spatial jets needed for these rows, and no finite closure of them was assumed.

### Products across the exterior split

For one exterior split write \(L\) for the neighboring block and \(R\) in the following subscripts for its complete complement. Each moment is the sum of its two indicated parts, for example \(M=M_L+M_R\). The forcing \(\mathcal F\) itself is linear in the contributions with the same \(D\). The mixed terms in (3) after assembling, beyond the terms with both factors in the same block, are

| Row | Mixed terms in forward physical time |
| --- | --- |
| \(M_t\) | \(4M_L M_R\) |
| \((S_2)_t\) | \(8(M_L S_{2,R}+M_R S_{2,L})+8D S_{2,L}S_{2,R}+8T_{2,L}T_{2,R}\) |
| \((T_2)_t\) | \(6(M_L T_{2,R}+M_R T_{2,L})+8D(S_{2,L}T_{2,R}+S_{2,R}T_{2,L})\) |

The linear diagonal terms split by ordinary summation. This expansion is of the full-source law, with the same \(c,D\) in both blocks. Its same-block terms are algebraic components of the complete row, not separate evolution equations for partial exterior sums. An evaluation that drops the product between blocks changes the parent time law.

## One adjacent pair of edges

For this readout take three consecutive real simple nodes \(x_0<x_1<x_2\) on a chart where each adjacent pair is separated from its own exterior. Put \(g_j=x_{j+1}-x_j\). In the parent convention \(P_{p,q}^{[j,j+1]}\) uses the power \(p\) at the right endpoint and the power \(q\) at the left. At the shared node both rows have exactly the same anchored power once the omitted neighbor is restored:
\[
 P_{r,0}^{[0,1]}+(-g_0)^{-r}
   = P_{0,r}^{[1,2]}+g_1^{-r}
   = \sum_{\rho\ne x_1}(\rho-x_1)^{-r},\qquad r\ge2 .             \tag{5}
\]
The sum counts occurrences and is absolute. The first-power node response is instead the finite part \(U_x=\lim_{z\to x}(B-1/(z-x))\), with the complete even pairing if it is expressed via the divisor. The law \(x_t=2U_x\) and \(g_{j,t}=4/g_j-2g_j M_j\) give \(g_jM_j=2/g_j-(U_{x_{j+1}}-U_{x_j})\). Hence
\[
 g_0M_0+g_1M_1=2(1/g_0+1/g_1)-(U_{x_2}-U_{x_0}),\qquad
 g_{0,t}+g_{1,t}=2(U_{x_2}-U_{x_0}).                             \tag{6}
\]
The identical shared-node response cancels. There is no use of independent unpaired first-power sums. The distinct real endpoints and adjacency are needed for the gap readout. A complete real exterior with no intervening root guarantees nonnegativity of each \(g_jM_j\) term by term. [AGC §2, block telescope](../../manuscript/sections/02_pair_chain.tex) · [AGC §3, anchored overlap](../../manuscript/sections/03_hierarchy.tex)

Consider one even polynomial heat family initialized by \((z^2-a^2)(z^2-b^2)\) with \(0<a<b=(r+1)a\), \(r>0\). Its exact evolution is the finite sum of iterated spatial derivatives with coefficients \((-t)^j/j!\). At the reference slice \(-a,a,b\) form the two-edge block and \(-b\) is the remaining occurrence outside it. For each parameter the real simple roots persist on a short cleared chart. The center and outer edges have respective gaps \(2a\) and \(ra\), and their complete moment responses at the reference slice are
\[
 M_{\rm center}=\frac{2}{b^2-a^2},\qquad
 M_{\rm outer}=\frac{1}{2a(a+b)}+\frac{1}{2b(a+b)}=\frac{1}{2ab}.
\]
Consequently the aggregate in (6) and the marked outer squared-gap drift are
\[
 A_0=g_{\rm center}M_{\rm center}+g_{\rm outer}M_{\rm outer}
     =\frac1a\left(\frac{4}{r(r+2)}+\frac{r}{2(r+1)}\right),
 \qquad (D_{\rm outer})_t=2-\frac{r^2}{2(r+1)}.
\]
Choosing \(a=(4/[r(r+2)]+r/[2(r+1)])/A_0\) fixes any \(A_0>0\). At \(r=1,6\) the marked drifts are \(7/4,-4/7\), so the same aggregate permits either sign within a bounded set of reference positions. As \(r\to\infty\) the drift tends to \(-\infty\) and the outer edge receives a fraction tending to one of \(A_0\). This last assertion allows increasing block diameter. The nonnegative response bound \(0\le g_jM_j\le A_0\) holds throughout this real slice class. In particular, a supplied upper bound \(g_j\le G\) gives \(D_{j,t}\ge2-GA_0\).

The same family also tests a sum of signed gap velocities. Equation (6) gives \(g_{{\rm center},t}+g_{{\rm outer},t}=[1+1/(r+1)+4/(r+2)]/a\). Scaling \(a\) to keep this sum fixed and positive as \(r\to0\) makes \(g_{{\rm outer},t}=4/(ra)-r/[a(r+1)]\) unbounded above, although the positions stay bounded. The gaps are positive for each parameter, and there is no uniform lower bound on the outer gap in this limit. Both calculations concern finite even polynomial heat fields with a completely real simple slice, not the literal theta source.

## Disposition

The pair, complete forcing and first regular time rows agree exactly with the direct parent. The every-occurrence product, trace and recurrence are inherited. The finite spatial split supplies a compatible way to assemble their inputs and makes the missing mixed terms and missing spatial jets explicit. The aggregate control delimits the information in the displayed telescope for its stated polynomial class. The [registered collision screen](../../../../../result-summaries/12_collision_controls_and_screening.md) applies as in [E01](02_AGC_ST_E01_SPLIT_GENERATOR_20261120.md#polynomial-heat-control-and-scope). The Euler, square-weight and primitive controls can obey this local algebra despite their changed exterior, coefficients or square expansion. The variable observation kernel fails the fixed heat law. A counted double is retained wherever the pair contour is cleared. This return establishes a representation and a scoped information obstruction. Quantitative improvement over the same direct evaluation remains open. [Results index](../../../../../result-summaries/README.md) · [Patterns index](../../../../../avoid/README.md) · [Coordinate changes](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) · [Scope of exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
