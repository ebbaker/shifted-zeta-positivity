# The physical generator on a cleared spatial split

20 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex LLM assistance. Executor dispatched as gpt-6.2-sol, effort ultra. Serving configuration has no separate attestation. AGC-ST-E01 r1, proof on the stated chart, pending separate assessment.

The source is the literal theta field \(H\) of [AGC §1](../../manuscript/sections/01_source.tex), with \(H_t=-H_{zz}\) in forward physical time. The chosen state and comparison come from the [B01 decision](../brainstorm/notes/01_AGC_ST_B01_SPLIT_DECISION_20261120.md) and [frozen request](../research-progress/handoffs/AGC_ST_E01_REQUEST_R1_20261120.md). The local deflation and Burgers laws are inherited from [AGC §2](../../manuscript/sections/02_pair_chain.tex) and [§3](../../manuscript/sections/03_hierarchy.tex). The calculation below proves the compatibility of the finite spatial assembly in both polynomial and contour coordinates.

## Chart and physical coefficient velocity

Use one compact real-time interval \(I\) with a finite rectangular parent \(P\), split by a vertical wall into \(L,R\). A second wall in one child will give the three-leaf check. The outer boundary and every chosen wall stay zero-free on \(I\). For instance, at a fixed slice one can choose a bounded rectangle and two cuts avoiding the finitely many zero locations in a larger box, then take a sufficiently short compact interval about that slice. A rectangle symmetric about the real line and its vertical subdivisions are conjugation-invariant. We also allow piecewise smooth deformations on which the boundaries stay cleared and the children partition the parent with one common oriented wall. All zero counts include occurrences with their multiplicities. Zeros can merge in a cell interior.

For a cell \(K\) of count \(m_K\), put
\[
 P_K(t,z)=\prod_{\rho\in K(t)}(z-\rho),\qquad
 A_K=H/P_K,\qquad R_K=(A_K)_z/A_K .
\]
The monic divisor has analytic coefficients on a fixed-count chart. Indeed, locally in time the contour can be held fixed in its cleared collar, including for a small complex-time neighborhood by continuity of \(H\). The polynomially weighted integrals of \(B=H_z/H\) give analytic power sums there, and the Newton recursion below gives the coefficients. For each time \(H/P_K\) has removable singularities at the counted roots and has no zeros in the cell or its cleared collar. Joint holomorphy in the interior follows by applying the Cauchy formula to \(H/P_K\) on the fixed contour. The local proofs overlap for a deforming cleared chart. For real time the coefficients are real whenever \(K\) is conjugation-invariant.

For an analytic function \(F\) at the roots of a monic polynomial \(p\), write \(\operatorname{rem}_{p}F\) for the unique polynomial of degree less than \(\deg p\) matching the Taylor data of \(F\) at each root through one less than its multiplicity. This is ordinary remainder for a polynomial and Hermite interpolation for an analytic germ. Define \(\operatorname{rem}_1 F=0\). At fixed physical \(z\), differentiating \(H=P_KA_K\) gives
\[
 (P_K)_t+(P_K)_{zz}+2R_K(P_K)_z
   =-P_K\,\frac{(A_K)_t+(A_K)_{zz}}{A_K}.
\]
The right-hand side is divisible by \(P_K\) at full multiplicity. Monicity keeps \((P_K)_t\) in degree less than \(m_K\), so its complete instantaneous value is
\[
 V_K=(P_K)_t=-\operatorname{rem}_{P_K}
       \big((P_K)_{zz}+2R_K(P_K)_z\big).                         \tag{1}
\]
An empty cell has \(P_K=1\) and \(V_K=0\).

For a differentiable real origin \(o_K(t)\) let \(u=z-o_K(t)\) and \(\widetilde P_K(t,u)=P_K(t,u+o_K(t))\). Holding \(u\) fixed gives
\[
 (\widetilde P_K)_t(t,u)=V_K(t,u+o_K(t))+o_K'(t)(\widetilde P_K)_u(t,u).
                                                                    \tag{2}
\]
Thus the remainder formula in \(u\) has \(-o_K'(\widetilde P_K)_u\) *inside* the outer minus sign, and \(\widetilde R_K(t,u)=R_K(t,u+o_K(t))\). To bring a child's polynomial to the parent origin, substitute \(u_K=u_P+o_P-o_K\). Differentiating the substitution adds \((o_P'-o_K')(\widetilde P_K)_u\) to (2), giving the child's fixed-\(z\) velocity plus the parent's \(+o_P'(\widetilde P_K)_u\). This is the same change of coordinates whether made before or after multiplying.

## Product and sibling response

Upward multiplication gives \(P_P=P_LP_R\). In monomial coordinates this is coefficient convolution after translating to a common origin. Downward, \(A_L=P_R A_P\) and \(A_R=P_L A_P\). Consequently
\[
 R_L=R_P+\frac{(P_R)_z}{P_R}\quad\text{near the roots of }P_L,
 \qquad
 R_R=R_P+\frac{(P_L)_z}{P_L}\quad\text{near the roots of }P_R.        \tag{3}
\]
Each sibling is nonvanishing on the neighborhoods where its logarithmic derivative is used.

Set \(W=V_LP_R+P_LV_R\). The product rule and (3) give the following identity near the left roots:
\[
\begin{split}
 W+(P_P)_{zz}+2R_P(P_P)_z
 &=P_R\big(V_L+(P_L)_{zz}+2R_L(P_L)_z\big)\\
 &\quad +P_L\big(V_R+(P_R)_{zz}+2R_P(P_R)_z\big).
\end{split}                                                       \tag{4}
\]
The cross term \(2(P_L)_z(P_R)_z\) is paid by the left sibling response. The right-hand side is divisible by \(P_L\) at every left root. Using the exchanged identity on the right pays the same cross term through \(R_R\) and gives divisibility by \(P_R\) there. The two divisors are coprime, even with internal multiplicities, because the wall is cleared. The two sets of congruences give divisibility by \(P_P\) and \(\deg W<m_L+m_R\) when \(m_L+m_R>0\). Thus \(W=V_P\) by uniqueness in (1). If one child is empty, its congruence is vacuous and its sibling correction is zero. If both are empty, each velocity is zero.

### Samples at repeated roots

At a distinct root \(r\) of multiplicity \(q\), write \(P_K=(z-r)^q U_r(z)\) with \(U_r(r)\ne0\). Then
\[
 R_K(P_K)_z\equiv qU_r(r)R_K(r)(z-r)^{q-1}
                         \pmod{(z-r)^q}.                          \tag{5}
\]
The \(q-1\) lower coefficients of the exterior term vanish and all spatial derivatives of \(R_K\) of order at least one are killed by the modulus. The values \(R_K(r)\), one at each distinct complex root, suffice for (1). In fact each is recoverable from \(V_K\) and \(P_K\) as the coefficient of \((z-r)^{q-1}\) in \(V_K+(P_K)_{zz}\), divided by \(-2qU_r(r)\). Thus the instantaneous velocity detects exactly these values of the germ for fixed divisor. With conjugation symmetry one needs one representative of each nonreal conjugate pair, whose other value is obtained by conjugation. For an empty divisor there are no samples. A common full boundary trace supplies each sample by the Cauchy formula for \(B-(P_K)_z/P_K\) in the cell.

The time law for the germ itself has extra spatial data. The same factorization gives
\[
 (R_K)_t=-\partial_z\!\left[
 \frac{V_K+(P_K)_{zz}+2R_K(P_K)_z}{P_K}+(R_K)_z+R_K^2
 \right] ,                                                       \tag{6}
\]
where the quotient extends across the roots. In particular for \(P_K=z-a(t)\), (1) gives \(a'=2R_K(a)\) and the quotient is \(2(R_K(z)-R_K(a))/(z-a)\). Differentiating in \(z\) at \(a\), then adding \(a'(R_K)_z(a)\) for the motion of \(a\), gives
\[
 \frac{d}{dt}R_K(t,a(t))=-2(R_K)_{zz}(t,a(t)).
\]
The second spatial derivative is absent from the retained value at the root. The finite instantaneous data supply a coefficient velocity, while time propagation of those data requires more of the exterior field. The full germ remains the input of the proposed interface.

## Independent contour balance

Let \(\mathcal I_K f=(2\pi i)^{-1}\oint_{\partial K(t)}f\,dz\) with the positive orientation, and write \(w_{K,k}(t,z)=(z-o_K(t))^k\) for an integer \(k\ge0\). The count moment is \(U_k(K)=\mathcal I_K(w_{K,k}B)\). The residue of \(B\) at a root is its multiplicity, so \(U_k(K)\) is the sum over occurrences including nonreal ones.

If a contour arc is parametrized by \(z=\gamma(t,s)\), differentiating the integral of \(f(t,z)\,dz\) gives the integral of \(f_t\,dz\) plus
\[
 \int \partial_s(f(t,\gamma(t,s))\,\gamma_t(t,s))\,ds .
\]
Here \(f\) is holomorphic in a cleared collar, and \(f_t\) holds \(z\) fixed. The endpoints of the latter integral cancel on the oriented closed contour, including corners with common endpoint velocities. Individual open arcs have the indicated endpoint terms. From the physical heat equation,
\[
 B_t=-\partial_z(B_z+B^2).
\]
Differentiating \(\mathcal I_K(w_{K,k}B)\) and integrating by parts on the closed contour first moves a derivative to \(w_{K,k}\), and then moves the derivative in \((w_{K,k})_zB_z\) back to the weight. Writing \(w=w_{K,k}\) gives
\[
 \dot U_k(K)
 =\mathcal I_K\big(w_t B+w_z(B_z+B^2)\big)
 =\mathcal I_K\big((w_t-w_{zz})B+w_zB^2\big),
 \qquad w_t=-o_K' w_z.                                          \tag{7}
\]
This gives \(\dot U_0(K)=0\), and the \(k=1\) origin contribution is \(-o_K'm_K\), the sign for the sum of the translated roots.

For \(K=L,R\) let \(\delta_K=o_K-o_P\). The binomial coefficients in
\[
 w_{P,k}=\sum_{j=0}^k \binom{k}{j}\delta_K^{\,k-j}w_{K,j}          \tag{8}
\]
translate the child moments to the parent origin. Differentiating the *whole* translated sum uses the derivatives of its coefficients through \(\delta_K'=o_K'-o_P'\). Together with the child's \(w_{K,j,t}\) terms these give exactly \(w_{P,k,t}=-o_P' w_{P,k,z}\). The two spatial derivatives in (7) act through (8) with the coefficients held at the current time, giving \(w_{P,k,z}\) and \(w_{P,k,zz}\). Each child contribution therefore has the same physical flux on the shared wall, namely the integrand of (7) with \(w=w_{P,k}\) and the **single full trace** \(B=H_z/H\). In polynomial coordinates this trace is \((P_K)_z/P_K+R_K\) on either side and equals \((P_P)_z/P_P+R_P\) there. The opposite wall orientations cancel the full integrand, including \(w_{P,k,z}B^2\), leaving the direct parent boundary. The same cancellation without differentiation gives the moment merge (8).

This argument applies on cleared collars. At a wall-crossing time the child contour through the zero is undefined. On subsequent cleared intervals use the newly counted child divisors or a verified overlap assigning the same occurrences. For an isolated crossing time \(t_*\) with common limiting origins on both sides, the one-sided jump of a child's \(k\)-th moment is the sum of \((\rho_*-o_K(t_*))^k\) times the signed change of its interior occurrence count at each crossing location \(\rho_*\). This follows by taking limits in the finite residue sums, grouping by limiting location to include multiple roots. In divisor coordinates the factors at the crossing location are transferred with those counts. With a clear parent outer boundary, the internal transfers cancel after translation, and the parent divisor and its moments continue analytically. A crossing of the outer boundary requires a new cleared parent chart and recount unless an overlapping contour preserves the selection. A double formed in a single cleared child needs no reset. A collision through the cut must be handled in one enclosing cleared cell until a new split is verified.

## Newton identities and a repeated split

For a cell of count \(m\), at its chosen origin write
\[
 \widetilde P_K(u)=u^m-e_1u^{m-1}+\cdots+(-1)^m e_m,\qquad
 ke_k=\sum_{j=1}^k(-1)^{j-1}e_{k-j}U_j(K),\quad e_0=1,
 \quad 1\le k\le m .                                             \tag{9}
\]
The recursion and its derivative are triangular in the coefficients and their velocities. This links the first \(m\) polynomial moments and their derivatives to the monic divisor and its velocity, with the count known. The count-zero recursion is empty.

To check that the two time laws give the same derivative, use the factorization and (1) in the first form of (7). The two identities on the cell are
\[
 B=\frac{(P_K)_z}{P_K}+R_K,\qquad
 B_z+B^2=-\frac{V_K}{P_K}+
 \left(\frac{(P_K)_{zz}+2R_K(P_K)_z+V_K}{P_K}
                               +(R_K)_z+R_K^2\right).
\]
The parenthesized term is holomorphic in the cell and on its cleared collar. Its integral against \(w_z\), and the integral of \(w_t R_K\), vanish. Therefore (7) gives exactly
\[
 \dot U_k(K)=\mathcal I_K\left(w_t\frac{(P_K)_z}{P_K}
                                      -w_z\frac{V_K}{P_K}\right).
\]
This is the derivative of the count integral of \((P_K)_z/P_K\) under coefficient velocity \(V_K\), since at fixed \(z\) the derivative of the logarithmic trace is \(\partial_z(V_K/P_K)\). It agrees with (9) and with (2) when taking coefficients about a moving origin.

For the one repeated split label the three ordered leaves \(1,2,3\). Under either \((1,(2,3))\) or \(((1,2),3)\) the upward state in physical coordinates is \(P_P=P_1P_2P_3\). Downward the leaf input in both assemblies is \(R_i=R_P+\sum_{j\ne i}(P_j)_z/P_j\) near its roots. Applying (4) twice gives, in either assembly, the direct parent velocity \(\sum_{i=1}^3 V_i\prod_{j\ne i}P_j\). Translating twice with displacements \(\delta_1,\delta_2\) is translation by \(\delta_1+\delta_2\) on polynomial weights, and differentiating this identity preserves the translated time law. In the contour assembly both shared walls cancel against the translated flux in (7). All of these comparisons use the same full \(H\) trace and the same final parent divisor as the direct evaluation.

## Polynomial heat control and scope

At \(t=0\) initialize the two exact polynomial heat solutions in the [branch overview](../research-overview/01_AGC_ST_RESEARCH_OVERVIEW_20261119.md) by \(p_1(z)=z^2-s^2\) and \(p_2(z)=(z^2-s^2)(z^2-b^2)\), with \(0<s<b\). The solutions are the finite heat sums \(\sum_{j\ge0}(-t)^jp_i^{(2j)}(z)/j!\). A symmetric target box containing \(-s,s\) and excluding \(-b,b\) is cleared on a short chart about \(0\) for both solutions. At \(0\) the target divisor is the same in both cases, hence so are all its count moments. Their exterior germs are \(R_1=0\) and \(R_2=2z/(z^2-b^2)\). Formula (1) gives
\[
 V_1=-2,\qquad
 V_2=-2+\frac{8s^2}{b^2-s^2},
\]
since the remainder of \(2R_2(P_K)_z\) equals \(8s^2/(s^2-b^2)\). The target divisors stay even on the local chart, so the corresponding \(D'\) values are \(2\) and \(2-8s^2/(b^2-s^2)\). This excludes an autonomous velocity from the interior divisor alone in this class of exact polynomial heat solutions. The example meets the heat law and local clearance and fails the literal theta source premise.

This is an exact local assembly and an information requirement for a specified finite state. The registered controls explain why the generic assembly carries no theta separation estimate. Euler-factor sources change the full analytic exterior despite matching the real zeros at time zero. Weighted squares and finite-source changes alter the theta coefficients, and finite-prime orbit controls fail full reflection. Reflected super-Gaussian and smooth positive-primitive controls lack the theta square expansion. Fixed-event atoms and finite-profile controls lack the full theta profile or eventual simplicity at the event, and the RH-conditional endpoint family fails ordinary Dirichlet arithmetic. The fixed-amplitude kernel relaxation fails the physical cosine heat law. Any genuine counted double in a cleared cell is retained with its multiplicity, including those in the three-atom control. These are premise checks using the existing records, with the polynomial heat comparison above the single explicit control calculation. [Collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Overview premise screen](../research-overview/01_AGC_ST_RESEARCH_OVERVIEW_20261119.md#tests-and-ownership)

The direct parent and assembled state give identical results when supplied the same divisor and trace. An advantage in precision, cost or signed error would require an additional comparison with controlled exterior acquisition or compression. E02 remains reserved in the frozen packet. [Results index](../../../../../result-summaries/README.md) · [Patterns index](../../../../../avoid/README.md) · [Classification](../../../../../avoid/01_restating_the_target.md) · [Scope of exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
