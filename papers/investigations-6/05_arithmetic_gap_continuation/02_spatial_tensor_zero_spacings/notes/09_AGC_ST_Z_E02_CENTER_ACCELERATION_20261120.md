# Complete center acceleration and signed displacement

20 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex LLM assistance. AGC-ST-Z-E02 r1, execution dispatched as gpt-6.2-sol, effort ultra. No separate serving-backend attestation. Analytical bound on the stated premises, pending separate assessment. [Frozen request](../research-progress/handoffs/AGC_ST_Z_E02_REQUEST_R1_20261120.md) · [B01 chart and anchor](../brainstorm/notes/05_AGC_ST_Z_B01_ORIENTED_ANCHOR_20261120.md) · [B02 acquisition decision](../brainstorm/notes/06_AGC_ST_Z_B02_ODD_CUBIC_TRANSPORT_20261120.md)

Use the literal Newman field \(H_t=-H_{zz}\) on \(0\le t\le h\), with increasing physical height and time. Fix a positively oriented, conjugation-invariant contour \(\Gamma\) which stays clear and counts exactly two occurrences. Write \(P=(z-c)^2-D\) for their counted polynomial, \(a=c-s,\ b=c+s,\ s^2=D\), and \(H=PE\), with \(\mathcal R=E_z/E\) inside the contour. The arguments below use the complete even product and uniform radial count of AGC. Real \(c,D\) follow from conjugation invariance. This is a finite transport estimate in the sense of [pattern 01](../../../../../avoid/01_restating_the_target.md). Its quantitative test is whether the actual error budget resolves the signed displacement on a chosen slab. [AGC source](../../manuscript/sections/01_source.tex) · [AGC pair law and product](../../manuscript/sections/02_pair_chain.tex)

## The complete acceleration

At a simple root \(x(t)\), let \(H_j=\partial_z^j H\) and evaluate at \((t,x(t))\). Differentiating \(H(t,x(t))=0\) twice and using the physical heat equation gives
\[
 v=x'=\frac{H_2}{H_1},\qquad
 x''=-\frac{H_4}{H_1}+2v\frac{H_3}{H_1}-v^3.                 \tag{1}
\]
In fact \(H_{tt}=H_4\), \(H_{tz}=-H_3\), and the term from \(H_{zz}(x')^2/H_z\) is \(v^3\). At a fixed time factor \(H=(z-x)U\) and put \(q=U_z/U\). The product rule gives \(H_j(t,x)=j\,\partial_z^{j-1}U(t,x)\) for \(j\ge1\). Substituting \(U_{zz}/U=q_z+q^2\) and \(U_{zzz}/U=q_{zz}+3q q_z+q^3\) into (1) gives \(x''=-4q_{zz}(t,x)\). In the even product each opposite pair contributes the two logarithmic poles, and subtracting \(1/(z-x)\) removes the marked occurrence. The complete products converge locally uniformly by the uniform count. On a small cleared neighborhood of \(x\), the same holds after deflating this simple factor, and Cauchy's formula gives convergence of the needed spatial derivatives. Equivalently the differentiated pole series converges absolutely and locally uniformly away from its remaining poles by the cubic decay. Thus
\[
 x''=-8\sum_{\rho\ne x}(x-\rho)^{-3},                         \tag{2}
\]
where the sum excludes one marked occurrence. Only spatial derivatives of the product are used. The complete first-power trace needed for \(x'\) is the finite part of \(H_z/H\), or the pole sum with the even product grouping. [Assessed singleton acceleration](../reviews/04_AGC_ST_FINITE_CURVATURE_ASSESSMENT_20261120.md#exterior-occurrences-and-acceleration)

At a separated pair the mutual terms in \(a''+b''\) are opposite cubes. For each exterior occurrence set \(y_\rho=\rho-c,\ Q_\rho=y_\rho^2-D\), and \(T_j=\sum_{\rm ext}y_\rho Q_\rho^{-j}\) for \(j=2,3\). Then
\[
\begin{aligned}
 c''&=-4\sum_{\rm ext}\left[(a-\rho)^{-3}+(b-\rho)^{-3}\right]\\
     &=8T_2+32DT_3=8(T_2+4DT_3).                             \tag{3}
\end{aligned}
\]
The bracket equals \(-2y_\rho(y_\rho^2+3D)/Q_\rho^3\), and \(y_\rho^2+3D=Q_\rho+4D\). The sum includes all nonreal occurrences with multiplicity, including the reflected partners of targets whenever these partners lie in the exterior. Conjugate occurrences give conjugate contributions. For real time their complete sum is real.

For continuation, let \(\mathcal I f=(2\pi i)^{-1}\oint_\Gamma f(z)\,dz\). The existing moment readout \(T_j=-\mathcal I((z-c)P^{-j}H_z/H)\) is holomorphic in the time chart through a target double. Uniform clearance gives the requisite time neighborhood locally, and \(P\) has no root on \(\Gamma\). The moment formula counts exterior multiplicities and yields the absolutely convergent sums on every real slice, including at the double. The pair law gives \(D'=2\) at \(D=0\), so a target double is isolated locally. Equation (3) therefore continues through it. At \(D=0\), \(T_2=-\mathcal R_{zz}(t,c)/2\) and \(c''=-4\mathcal R_{zz}(t,c)\). [Moment readouts and multiplicities](03_AGC_ST_E02_PAIR_AND_FORCING_20261120.md#complete-moments-from-the-same-exterior-input)

There is an independent calculation on the fixed contour. Write
\[
 B=H_z/H,\qquad F=H_2/H,\qquad G=F^2-H_4/H .
\]
On its collar \(B_t=-F_z\) and \(F_t=G\). Differentiating \(c=\mathcal I(zB)/2\) and \(D=\mathcal I(z^2B)/2-c^2\), then integrating by parts on \(\Gamma\), gives
\[
\begin{aligned}
 c'&=\tfrac12\mathcal I F, & D'&=\mathcal I((z-c)F),\\
 c''&=\tfrac12\mathcal I G, &
 D''&=\mathcal I((z-c)G)-2(c')^2.                             \tag{4}
\end{aligned}
\]
The last term is the derivative payment for the moving center in the weight. On separated charts \(c\) is the mean of the same roots as in (1), so its differentiated contour evaluates (3). At an exact double put \(w=z-c\), \(\beta=E_{zz}/E\), \(\gamma=E_{zzz}/E\). Factoring \(H=w^2E\) gives the singular terms of \(G\) as
\[
 4w^{-4}+16\mathcal Rw^{-3}+(16\mathcal R^2-8\beta)w^{-2}
              +8(\mathcal R\beta-\gamma)w^{-1}.
\]
Using \(\beta=\mathcal R_z+\mathcal R^2\) and \(\gamma=\mathcal R_{zz}+3\mathcal R\mathcal R_z+\mathcal R^3\), their residue is \(-8\mathcal R_{zz}(t,c)\), which gives the same double value directly. All the spatial ratios in (1) and (4) are unchanged under multiplication by a nonzero time-only factor, in particular normalization by \(H(t,0)>0\). The derivation uses the heat equation for the physical field before substituting these equal ratios. For elapsed backward time the first derivatives have the opposite sign and the second derivatives have the same sign, with all fields sampled at the reversed physical time. [AGC contour readout](../../manuscript/sections/06_residual_transport.tex)

## Tail and time integration

Assume \(|a|,|b|\le A\) throughout the chart and the whole-divisor count \(n_t(u)\le C u\log(2+u)\) uniformly for \(u\ge R_0\). For a radius \(R\ge\max(2A,R_0,2)\), assign ties to the head, so the tail consists of \(|\rho|>R\). Each tail occurrence in (3) costs at most \(64|\rho|^{-3}\), since both endpoint distances are at least \(|\rho|/2\). Partial summation, counting occurrences rather than opposite pairs, gives
\[
\begin{aligned}
 \sum_{|\rho|>R}|\rho|^{-3}
 &= -\frac{n_t(R)}{R^3}+3\int_R^\infty \frac{n_t(u)}{u^4}\,du\\
 &\le 3C\int_R^\infty \frac{\log(2u)}{u^3}\,du
  = \frac{3C}{2R^2}\left(\log(2R)+\tfrac12\right).
\end{aligned}
\]
The count makes the endpoint at infinity vanish and \(u\ge2\) gives \(\log(2+u)\le\log(2u)\). The bound for the acceleration tail is therefore
\[
 \tau(R)=\frac{96C}{R^2}\left(\log(2R)+\tfrac12\right).        \tag{5}
\]
An enclosed signed head uses every actual exterior occurrence at radius at most \(R\) and pays its position and evaluation uncertainty. Without such a head enclosure (5) only pays the tail. Alternatively (1) or (4) with the complete source supplies the entire acceleration, including every exterior term.

For any integrable pointwise signed acceleration enclosure \([L(t),U(t)]\) and independently acquired \(c'(0)\in V_c^0\),
\[
 c(h)-c(0)
 \in h V_c^0+
 \left[\int_0^h(h-t)L(t)\,dt,\ \int_0^h(h-t)U(t)\,dt\right]. \tag{6}
\]
This follows by integrating \(c''\) twice. For a constant interval the weight is exactly \(h^2/2\). With a time-dependent central approximation and absolute error allowance \(e(t)\), integrate the approximation with weight \(h-t\) and add the radius \(\int_0^h(h-t)e(t)\,dt\). A partition into full time cells with interval bounds on each uses the exact nonnegative weight on each cell, including interval and source errors there. Pointwise samples alone require an additional bound over intervening times. For a fixed radial split, (5) costs at most \(h^2\tau(R)/2\), in addition to head error. A measurable moving \(R(t)\) satisfying the same threshold gives the integrated cost \(\int_0^h(h-t)\tau(R(t))\,dt\), provided the signed head enclosure follows actual membership at each time. This uses an instantaneous decomposition of \(c''\). A head kept frozen across unaccounted entries or exits does not represent that decomposition. Differentiating a cutoff-dependent partial trace would require a separate argument that accounts for membership changes. A moving cutoff supplies no error bound for a first-power velocity used at the anchor.

If \(c'(0)\) has error radius \(e_v\), the displacement pays \(h e_v\). An initial center error \(e_c\) further costs \(e_c\) for the absolute final location. Anchor localization affects the evaluation of \(V_c^0\) and the path enclosures as well. A signed claim follows if the interval in (6) lies wholly on one side of zero.

## Acquisition without target-time ordinates

For the separated real predictor, independently count and enclose the two simple real roots at \(t=0\) in intervals \(X_a,X_b\). Take disjoint compact real intervals \(B_a,B_b\), in that order and inside the cleared pair chart, with \(X_i\subset\operatorname{int}B_i\). Acquire the full source spatial jets through order four on \([0,h]\times B_i\). A sufficient first-exit condition for each \(i=a,b\) is
\[
 \inf_{[0,h]\times B_i}|H_1|\ \ge m_i>0,\qquad
 \sup_{[0,h]\times B_i}|H_2/H_1|\ \le U_i,\qquad
 \operatorname{dist}(X_i,\partial B_i)>hU_i.                 \tag{7}
\]
The real implicit root from \(X_i\) is simple while in \(B_i\), and its displacement up to a putative exit is at most \(tU_i\) by (1). A finite interior endpoint of continuation also has a limiting real root by the speed bound and \(H=0\), with nonzero slope by (7), so the implicit root extends there. This proves containment and simplicity throughout \([0,h]\). The narrower guaranteed tube on each time slice is \(X_i+[-tU_i,tU_i]\), still inside \(B_i\). Both real roots exhaust the fixed count. The proof uses the anchor and a source acquisition box declared before the terminal comparison.

For approximants \(\widehat H_j\) with certified absolute errors \(\epsilon_{ij}\) uniform on the acquisition box, one may take \(m_i=\inf|\widehat H_1|-\epsilon_{i1}>0\) and \(U_i=(\sup|\widehat H_2|+\epsilon_{i2})/m_i\) with bounds rounded outward. The same test applies to the normalized jets with their own error allowances. Enclose the full ratio at \(t=0,\ z\in X_i\) in \(V_i^0\). On the guaranteed tube, evaluate (1) on the jointly enclosed jet values, enlarging each approximation by its uniform error before taking ratios, and enclose the resulting acceleration in a signed interval \(I_i\). The denominator floor is that of the full \(H_1\). Each occurrence of \(H_2/H_1\) in (1) represents the same ratio. This procedure includes source, spatial evaluation and time coverage error in the jet enclosures. The uniform accelerations may instead be replaced by integrated cell enclosures as in (6). A lack of either a slope floor or a speed-versus-wall margin stops this particular first-exit certificate.

For \(h>0\), let \(\alpha_i=(2/h^2)\int_0^h(h-t)x_i''(t)\,dt\). Then \(\alpha_i\in I_i\), and define \(p_i=x_i(0)+hv_i^0+h^2\alpha_i/2\) using the true \(x_i(0)\in X_i,\ v_i^0\in V_i^0\). The center and positive half-gap have the simultaneous enclosure
\[
 (c(h),s(h))=\left(\frac{p_a+p_b}{2},\,\frac{p_b-p_a}{2}\right). \tag{8}
\]
An enclosure of the center **displacement** uses only the two velocity and acceleration terms in the first component, since the initial positions cancel. Absolute final enclosures keep both initial positions. A separately acquired signed exterior or contour bound (6) can be imposed as an additional constraint on the same variables if available. Keeping the anchor locations, velocities and weighted accelerations as shared variables in (8) gives exactly the direct Taylor enclosure on recovering \(c-s=p_a,\ c+s=p_b\), with the same joint input set. Independent interval projections of \(c\) and \(s\), or of \(c\) and \(D\), can enlarge the recovered location intervals. The direct calculation with the same source can also integrate singleton velocity enclosures over the guaranteed tubes, and can attempt a terminal source root solve after the prediction is fixed. These are legitimate comparators using the common acquired data.

For the signed discriminant on the separated real chart, map the joint enclosure to \((c,D)=(c,s^2)\) with the same \(s>0\) fixed by the ordered disjoint tubes. On any cleared chart containing a possible double, \(D=\mathcal I(z^2B)/2-c^2\) is real and signed. With sufficient complete-source bounds on the fixed contour, (4) supplies a second-order enclosure for \(D\) from its own anchored \(D(0),D'(0)\), with the same weight as in (6). Evaluating (4) quantitatively requires a positive modulus floor for \(H\) on the contour. Retain the count and joint center/discriminant information for E03's recovery of the possibly nonreal unordered pair.

## Scope and premise screen

The E01 even-polynomial control with equal anchored jets through order three has a \(-1134\) center acceleration difference in the order fixed by B02. It supplies the limitation for that compressed anchor information and fails the unchanged complete theta source. The identity and transport bound apply to other fields meeting their respective product, heat and clearance hypotheses. At a colliding occurrence the separated slope condition fails, while the fixed counted contour can survive. Euler-factor and RH-conditional endpoint controls fail ordinary xi arithmetic. Weighted-square, finite-source and finite-score perturbations change the full theta coefficients. The finite-prime orbit controls additionally lose complete reflection. Reflected, smooth-shape and primitive-compatible controls lack the canonical square expansion. Fixed-event atomic and finite-profile controls lack the full source profile and its eventual simplicity at threshold. The variable observation kernel fails the physical cosine/Newman evolution. The positive-measure relaxation lacks an integer zero divisor. No canonical slab estimates or resolution advantage follow without acquisition of the quantified inputs. [Results index](../../../../../result-summaries/README.md) · [Collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Patterns index](../../../../../avoid/README.md) · [Premise screening](../../../../../avoid/02_shape_only_arguments_and_the_controls.md) · [Scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)

## R2 addendum · pair the outer opposite occurrences

20 November 2026. Prepared for Edward Baker with OpenAI Codex LLM assistance. AGC-ST-Z-E02 r2, execution dispatched as gpt-6.2-sol, effort ultra. No separate serving-backend attestation. [Frozen r2 request](../research-progress/handoffs/AGC_ST_Z_E02_REQUEST_R2_20261120.md)

Use the hypotheses of (5). Every occurrence with \(|\rho|>R\) is exterior, and this radial cutoff puts \(\rho\) and \(-\rho\) in the same part. Evenness pairs them with equal multiplicity. The field has \(H(t,0)\ne0\), so the orbit has two locations, including when \(-\rho=\bar\rho\). A nonreal orbit contributes as a pair with its own multiplicity. Conjugation introduces no further division of the count. Within the head the reflected partner of a target stays in the exterior sum if it is exterior, even though the target itself has been removed.

At either endpoint \(x\in\{a,b\}\), take the signed sum before the absolute value:
\[
 K(x,\rho)=(x-\rho)^{-3}+(x+\rho)^{-3}
           =\frac{2x(x^2+3\rho^2)}{(x^2-\rho^2)^3}.
\]
Since \(|x|\le|\rho|/2\), \(|x^2+3\rho^2|\le(13/4)|\rho|^2\) and \(|x^2-\rho^2|\ge(3/4)|\rho|^2\) hold also for complex \(\rho\) or \(x\). Consequently \(|K(x,\rho)|\le(416/27)|x|\,|\rho|^{-4}\). The two endpoints and the coefficient \(-4\) of (3) cost at most \((3328/27)A|\rho|^{-4}\) per orbit counted with multiplicity. The weighted orbit sum is exactly half the corresponding whole occurrence sum. As in (5),
\[
\begin{aligned}
 \sum_{|\rho|>R}|\rho|^{-4}
 &= -\frac{n_t(R)}{R^4}+4\int_R^\infty\frac{n_t(u)}{u^5}\,du\\
 &\le \frac{4C}{3R^3}\left(\log(2R)+\tfrac13\right).
\end{aligned}
\]
Thus the uniform tail bound for the signed acceleration after grouping is
\[
 \tau_\pm(R)=\frac{6656}{81}\frac{AC}{R^3}
                       \left(\log(2R)+\tfrac13\right).        \tag{9}
\]
The signed head enclosure is enlarged by \([-\tau_\pm(R),\tau_\pm(R)]\). Formula (6) weights this allowance by \(h^2/2\) for fixed cutoff, or by \(\int_0^h(h-t)\tau_\pm(R(t))\,dt\) as a radius for a measurable moving cutoff with a head enclosure that follows actual orbit membership. The equally informed direct exterior computation can use the same \(K\), the same cutoff and the same occurrence count, including any unpaired exterior terms in the head. With complete source jets, the direct readout already contains the outer response. The improvement in (9) concerns the truncation allowance.
