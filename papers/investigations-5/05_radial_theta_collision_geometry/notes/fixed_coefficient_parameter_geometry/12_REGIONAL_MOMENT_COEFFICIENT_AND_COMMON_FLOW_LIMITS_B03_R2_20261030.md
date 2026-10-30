# A regional moment coefficient and the limits of common flow propagation

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra**, reasoning effort **max**, Investigation05 **chat0046**, *Continue FCG-B03 R2 on C04*.

**FCG-B03 R2 return: complete bounded comparison.** C04 has an explicit finite source-derived coefficient whose sign is proved positive on one fixed ball. A complete-source carrier then gives an explicit energy floor for **all** auxiliary times. This is an elementary low-frequency calibration: the same information proves the stronger direct statement \(H>0\). It supplies no new advantage over direct theta analysis, and the coefficient cannot handle a ball containing a simple zero of \(H\). A second C04 sketch, propagation by a common coercive quadratic form on the family's linear span, fails in that explicitly enlarged class. C01 follows on the calibration ball from the same direct margin.

The derivations below have same-assistant checking only. **Next: [E] FCG-E02 R2 — Sol**, the bounded assessment in the [issued packet][packet]. The [continuation][next] distinguishes that ready assessment from a later conceptual decision about a two-component coefficient.

## 1. Fixed scope and the three sketches

Follow [Note11][request] and the sole live [Progress06][progress]. Keep the complete theta source, literal cosine, original drift, unit Gaussian preparation and all of \(\mathbb R^3\):

\[
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},\qquad
 H(T,A)=\int_0^\infty e^{Tu^2}\Phi(u)\cos(Au)\,du,
\]
\[
 W_c=(U_c,U_{c,A}),\quad \partial_sW_c=\Delta W_c+c\operatorname{div}(vW_c),\quad
 v(X)=X+X/(1+|X|^2),\quad \int W_c=(H,H_A).
 \tag{1}
\]

The raw radial data use \(u=\tfrac12\log|X|\) and density

\[
 \rho_T(X)=\mathbf1_{|X|\ge1}\frac{e^{Tu^2}\Phi(u)}{8\pi|X|^3},\qquad
 W_0=K_1*[\rho_T(\cos Au,-u\sin Au)],\quad
 K_1(X)=(4\pi)^{-3/2}e^{-|X|^2/4}.
 \tag{2}
\]

Fix the ball recorded at intake,

\[
 B=\{(T,A):(T-1/4)^2+(A-2\sqrt6)^2\le1/256\},\qquad r=1/16.
 \tag{3}
\]

Its center is the exact Gaussian-polynomial control event, not a mark selected by a theta jet evaluation. Put \(T_-=3/16\), \(T_+=5/16\), and \(a_+=2\sqrt6+1/16<5\). Thus \(B\subset K_*\). The inherited \(K_*=[1/8,3/8]\times[4,45]\), \(c=1\) C01 pilot remains historical context; the conclusions here concern only (3). No numerical acquisition or scan is used.

| Sketch | Mathematical object and source input | Result |
| --- | --- | --- |
| C04 moment coefficient | Two complete source moments; theta primitive endpoint and complete arithmetic tail | Positive on (3); all-time energy floor; identical direct \(H>0\) margin |
| C04 quadratic propagation on the linear span | One common bounded coercive quadratic functional for all linear combinations of the prepared family | Impossible in that enlarged class because it contains nonzero zero-mass fields |
| C01 comparator | \(D_c+CE_c\), evaluated with the same moment information | Works eventually on (3), \(c=1,C=9/7\), by the C04 mass margin; no new curvature estimate |

The regional target remains the [Note10][clarification] reformulation of compact jet nonvanishing under its convergence hypotheses. The first coefficient below is a **sufficient condition, not an equivalent criterion**: it excludes even ordinary zeros of \(H\). Its quantitative calibration and its limitation, rather than the equivalent target, are what this return establishes. See the [result index][results], [theta identities][identities] and [avoid index][avoid], particularly [target reformulations][a01], [scoped exclusions][a07], [separate bounds][a12] and [circular definitions][a14].

## 2. A finite real coefficient from complete moments

For a nonzero nonnegative source with the required moments, define

\[
 M_j(t)=\int_0^\infty u^j e^{tu^2}\Phi(u)\,du,\qquad
 c_B=1-\frac{a_+^2M_2(T_+)}{2M_0(T_-)},\qquad
 m_B=M_0(T_-)c_B.
 \tag{4}
\]

The denominator is positive by source positivity, independently of any physical jet. The expression is finite and real before its sign is known. It is one number for the entire ball, not (c(p)) or a stationary-energy matching coefficient. The dimensionless normalization in (4) is a design choice; the drift does not uniquely select it.

The elementary inequality \(\cos x\ge1-x^2/2\), source positivity, and monotonicity of the complete moments give

\[
 H(T,A)\ge M_0(T)-\tfrac12A^2M_2(T)
 \ge M_0(T_-)-\tfrac12a_+^2M_2(T_+)=m_B\qquad(p\in B).
 \tag{5}
\]

This uses the whole half-line and every source index. The sign of \(c_B\) therefore gives a uniform mass floor without defining a constant through \(\min_B|J|\). Equation (5) is also the exactly matched direct comparator: the fixed flow does not improve this source estimate.

## 3. Theta proves the coefficient positive on the selected ball

All inequalities in this section are analytic. The bounds are deliberately coarse; their purpose is to determine the sign with complete tails, not to approximate theta values.

Use the complete primitive relation from [Primitive Note52, Section 1][primitive]:

\[
 \psi(u)=e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}},\quad
 \Phi=(\psi''-\psi)/8,\quad \psi'(0)=-1/2.
 \tag{6}
\]

The endpoint follows from evenness of \(e^u\Theta(e^{4u})=e^u+2\psi(u)\). The decaying primitive, rather than the nonintegrable full \(P=e^u+2\psi\), is integrated below. Its upper derivative and value vanish, so

\[
 M_0(0)=\frac1{16}-\frac18\int_0^\infty\psi(u)\,du.
 \tag{7}
\]

First bound the complete arithmetic sum. Since \(n^2\ge1+3(n-1)\) for integer \(n\ge1\),

\[
 \mathcal S:=\sum_{n\ge1}n e^{-\pi n^2}
 \le\frac{e^{-\pi}}{(1-e^{-3\pi})^2}
 <\frac{1/22}{(1-22^{-3})^2}<\frac1{21}.
 \tag{8}
\]

For an elementary rational check of \(e^\pi>22\), use \(\pi>31/10\), \(e^3>\sum_{k=0}^8 3^k/k!=89641/4480>20\), and \(e^{1/10}>11/10\). No fitted decimal is involved.

From \(e^{4u}\ge1+4u\) and \(4\pi n^2-1>11\),

\[
 \int_0^\infty\psi(u)\,du
 \le\sum_{n\ge1}\frac{e^{-\pi n^2}}{4\pi n^2-1}
 <\frac1{11}\mathcal S<\frac1{231}.
\]

Consequently

\[
 M_0(T_-)\ge M_0(0)>\frac1{16}-\frac1{1848}>\frac3{50}.
 \tag{9}
\]

For the second moment, each physical source summand is positive on \(u\ge0\). Dropping its negative term is a valid upper bound. With \(e^{4u}\ge1+4u+8u^2\),

\[
 e^{T_+u^2}\Phi(u)
 \le2\pi^2\sum_{n\ge1}n^4e^{-\pi n^2}
 e^{-(4\pi n^2-9)u-(8\pi n^2-T_+)u^2}.
\]

Here \(4\pi n^2-9>0\) and \(8\pi n^2-T_+\ge n^2(8\pi-5/16)>24n^2\). Tonelli and the Gaussian second-moment integral give

\[
 M_2(T_+)
 \le\frac{\pi^{5/2}}{2(8\pi-5/16)^{3/2}}\mathcal S
 <\frac5{64}\mathcal S<\frac5{1344}<\frac3{800}.
 \tag{10}
\]

For the prefactor bound, \(\pi^2<10\), \(\sqrt\pi<9/5\), and \(\sqrt{24}>24/5\) suffice. Thus its numerator is below 18, while its denominator is above \(2\cdot24\cdot24/5\).

Combining \(a_+<5\), (9) and (10) yields

\[
 \boxed{\quad \frac7{32}<c_B<1,\qquad
 m_B>\frac{21}{1600},\qquad H(T,A)>\frac{21}{1600}\quad(p\in B).\quad}
 \tag{11}
\]

The full endpoint and complete series supply the theta evaluation of (4). The general theorem does not require every source to be theta: other sources can satisfy the same quantitative moment inequality. Conversely, the normalization or arithmetic support alone does not imply (9)–(11) for a control.

## 4. A complete all-time energy lower bound

This propagation step supplies the requested regional theorem with \(S_B=0\). It uses positivity and conservation of the fixed linear propagator, as constructed in [Note28][flow], and a paid spatial second moment. It does not need a stationary density, a convergence rate or an unknown minimum of energy.

Set

\[
 L=\int_0^\infty e^{T_+u^2}\Phi(u)(1+u)\,du,\qquad
 R_2=\int_0^\infty e^{T_+u^2+4u}\Phi(u)(1+u)\,du.
 \tag{12}
\]

Both constants are finite by the complete theta tail. Let

\[
 G_B=K_1*[\rho_{T_+}(1+u)],\qquad \Sigma_c(s)=P_s^cG_B.
\]

The pointwise vector norm obeys \(|W_0(p)|\le G_B\) and \(|W_c(s;p)|\le\Sigma_c(s)\), uniformly on \(B\). The latter follows from positivity of the **same scalar kernel** acting on both vector components. Exact polar integration in (2) gives \(\int\Sigma_c=L\). Since \(K_1\) has zero mean and second moment 6,

\[
 N_c(0):=\int |X|^2G_B(X)\,dX=R_2+6L.
\]

The full-space moment identity, justified first with spatial cutoffs and then by finite prepared moments, is

\[
 N_c'=6L-2c\int X\cdot v(X)\Sigma_c(X)\,dX
 \le6L-2cN_c\quad(c>0),
\]

because \(X\cdot v=|X|^2+|X|^2/(1+|X|^2)\ge|X|^2\). Thus, for every \(s\ge0\),

\[
 N_c(s)\le\overline N_c:=\max\{R_2+6L,3L/c\}.
 \tag{13}
\]

The source boundary \(|X|=1\) is included in the original radial measure and in \(R_2+6L\); it is not a boundary condition on the prepared full-space flow. The moment estimate retains all spatial exteriors.

Assume now \(c_B>0\), put \(c=c_B\), \(m=m_B>0\), and choose the **spatial** radius

\[
 R_X^2=2\overline N_c/m.
\]

At every physical mark and auxiliary time, mass conservation, the carrier tail estimate and Cauchy–Schwarz give

\[
 m\le |J(p)|
 \le\int_{|X|\le R_X}|W_c|+\int_{|X|>R_X}\Sigma_c
 \le\left(\frac{4\pi R_X^3}{3}\right)^{1/2}E_c(s;p)^{1/2}+\frac m2.
\]

Hence the explicit complete-source result is

\[
 \boxed{\ E_{c_B}(s;p)\ge\delta_B:=
 \frac{3m_B^2}{16\pi}
 \left(\frac{m_B}{2\overline N_{c_B}}\right)^{3/2}>0
 \quad(p\in B,\ s\ge0).\ }
 \tag{14}
\]

Every quantity in (14) is defined by finite source moments and the already signed coefficient. No spatial tail is omitted and no parameter-boundary estimate is substituted for a pointwise result. The same proof works for any fixed \(c>0\) once (5) is established. Choosing the source margin itself as the compression coefficient is valid, but does not make it a uniquely effective coefficient.

## 5. Control screen and the limitation at simple zeros

For \(A_0\ne0\) and a nonnegative source with positive mass at \(u>0\), the cosine inequality is strict after integration. If \(H(T_0,A_0)=0\), then

\[
 M_0(T_0)-\tfrac12A_0^2M_2(T_0)<0.
 \tag{15}
\]

For any containing ball, its \(T_-,T_+,a_+\) imply \(c_B<0\) by monotonicity. Thus the proposed sign certificate necessarily rejects every such collision on its own admissible domain. It also rejects **simple zeros of \(H\)**, although those can have \(|J|>0\). This is the decisive limitation: (4) cannot establish regional jet noncollapse across ordinary sign changes of \(H\).

| Control | Actual domain and consequence for this coefficient | Theta premise not available |
| --- | --- | --- |
| Gaussian polynomial \((64u^4+6)e^{-17u^2/4}\) | Ball (3) is within \(T<17/4\). At its event \(T_0=1/4,A_0=2\sqrt6\), \(M_0=9\sqrt\pi/4\), \(M_2=21\sqrt\pi/32\). The center coefficient is \(1-(24/2)(7/24)=-5/2\); the ball coefficient is strictly smaller. | Full theta source and normalized primitive endpoint evaluation used in (7)–(10) are not assigned to this source. Its quantitative sign test actually fails. |
| Three positive square weights | Use its own radius-\(1/16\) ball centered at \((1/4,44.13035)\), containing the certified event \(A_*\in(44.1303,44.1304)\). Its complete moments are finite; (15) proves \(c_B<0\) without replaying the event certificate. | Unit coefficients and full reflection fail; the theta moment estimates are not transferred. Its event is not asserted to be an all-real threshold. |
| Reflected, positive-primitive and finite-information positive controls | At a recorded nonzero-frequency event, (15) applies whenever the containing ball has the required moments. No common event or enlarged moment domain is imposed. | Their separate failed arithmetic, full-profile or reflection premises stay as in the [control register][controls]. A shared primitive shape does not imply (9)–(11). |
| Fixed theta amplitude with variable observation | The cosine inequality and (15) concern the literal oscillator; arbitrary polynomial observation is outside this implication. | Literal cosine/Newman observation fails. |

The coefficient is not required to be negative for a control on a different, collision-free region. These are analytical screens at the actual event domains, not new control computations.

## 6. Why a common quadratic propagation theorem on the whole span fails

The second C04 sketch would try to avoid the signed mass estimate by proving a common energy propagation inequality on the linear envelope of the prepared family. That strengthening fails even for the actual complete theta source.

Take three distinct frequencies \(A_i=2\sqrt6-1/32,2\sqrt6,2\sqrt6+1/32\), all at \(T=1/4\), and put \(F_i=W_0(T,A_i)\). They are linearly independent. Indeed, Gaussian convolution is injective (its Fourier multiplier is nowhere zero). A relation among the raw first components would imply \(\sum b_i\cos(A_iu)=0\) on \(u>0\), since the common radial source is positive there. Its derivatives of orders \(0,2,4\) give a Vandermonde matrix in the distinct \(A_i^2\), forcing all \(b_i=0\).

Their mass vectors \(J_i\in\mathbb R^2\) are linearly dependent. Thus some nonzero combination \(F=\sum b_iF_i\) has zero vector mass but is a nonzero prepared field. The [fixed-flow zero-mass estimate][fixed] applies for every finite \(c>0\):

\[
 \|P_s^cF\|_2\longrightarrow0.
 \tag{16}
\]

Suppose a time-independent common quadratic functional 

\[
 \mathscr Q_c(F)=\langle F,A_cF\rangle,\qquad
 a_c\|F\|_2^2\le\mathscr Q_c(F)\le b_c\|F\|_2^2,\qquad 0<a_c\le b_c<\infty
\]

were nondecreasing under the flow for every initial field in this linear span. Its value on the constructed \(F\) would stay at least \(\mathscr Q_c(F)>0\), while (16) and the upper bound force it to zero, a contradiction. A uniform positive reverse norm bound on that entire span fails for the same reason.

This rejects the **common bounded coercive quadratic, all-linear-combinations, all-time propagation class**. It does not reject parameter-specific estimates, a positive cone excluding those combinations, nonquadratic identities, correlated theta estimates, or the original C04 target. The massless combination is not a single literal-cosine mark; requiring the propagation inequality for it was the extra premise of this sketch. A shared operator alone does not license that strengthening.

## 7. C01 with the identical source information

On (3), \(H\ge m_B\), \(|H_{AA}|\le M_2(T_+)\), and (11) gives \(M_2(T_+)/m_B<2/7\). For \(E_J=H^2+H_A^2\), \(\mathcal L=H_A^2-HH_{AA}\), choose the **comparison coefficient** \(C=9/7\), distinct from the spatial coefficient \(c\). Then

\[
 \mathcal L+\frac97E_J
 \ge\left(\frac97-\frac{M_2(T_+)}{m_B}\right)H^2
       +\frac{16}{7}H_A^2\ge E_J\ge m_B^2.
 \tag{17}
\]

For the inherited baseline \(c=1\), compact-uniform convergence of \(U,U_A,U_{AA}\) in the [family note][family] gives

\[
 D_1(s;p)+\tfrac97E_1(s;p)
 \longrightarrow Q(1)(\mathcal L+\tfrac97E_J)
 \ge Q(1)m_B^2.
\]

It is therefore positive uniformly on this ball at all sufficiently large times. C01 is valid here because the same direct \(H\) floor has already been paid. This supplies no signed curvature mechanism on all of \(K_*\), near a possible double, or across simple zeros.

The [accepted E02 R1 assessment][review1] of the earlier Poisson calculation is preserved: undamped individual modes and the uniform absolute-mode budget fail in their stated endpoint classes; full regrouping restores integrability without supplying the desired signed estimate. The present low-frequency moment argument neither repairs nor contradicts those results. It avoids that decomposition by proving a stronger direct low-frequency bound.

## 8. Disposition and the remaining research decision

**Retain C04 R1 as a regional research target, with this moment construction recorded as a completed calibration and scoped insufficient lead for regions crossing simple zeros.** The coefficient, its theta positivity and its all-time implication are concrete; the direct comparison shows exactly where the sign information enters. The linear-span quadratic alternative is rejected only in Section 6's class. C01 remains the comparator, without a new independent signed mechanism.

After the fixed assessment, a genuinely different C04 continuation would seek a source coefficient using **both** \(H\) and \(H_A\), remaining capable of positivity on a prespecified region that may cross an ordinary simple zero. Its open obligation is to obtain a source-signed joint-jet bound without inserting the unknown jet minimum or replacing the physical family by its arbitrary linear span. No such formula or theta lemma is claimed here, and this unresolved design must stay **B — Astra**. Widening the present moment inequality or scanning its known calibration range is not the proposed continuation.

No manuscript, result-summary or milestone promotion is warranted by this unassessed calibration. The return and [self-assessment][self] are saved, the live register is updated, and the next fixed review is ready. There is no claim of a new literature-level zero-free region, RH consequence or exhaustive obstruction.

[request]: 11_CONTINUATION_FCG_B03_R2_REGIONAL_COEFFICIENT_POSITIVITY_20261030.md
[clarification]: 10_FIXED_FLOW_BOUNDEDNESS_AND_LOCAL_COLLISION_GEOMETRY_20261030.md
[progress]: ../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md
[next]: 13_CONTINUATION_FCG_E02_R2_AND_C04_MODEL_HANDOFF_20261030.md
[packet]: ../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R2_REGIONAL_COEFFICIENT_ASSESSMENT_20261030.md
[self]: ../../reviews/fixed_coefficient_parameter_geometry/02_REGIONAL_MOMENT_COEFFICIENT_B03_R2_SELF_ASSESSMENT_20261030.md
[primitive]: ../../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md
[flow]: ../28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[fixed]: ../CHAT0042_FIXED_COMPRESSION_AND_NORMALIZATION_COMPARISON_20261030.md
[family]: ../CHAT0042_FIXED_FLOW_PARAMETER_FAMILY_AND_COLLISION_INDEX_20261030.md
[review1]: ../../reviews/fixed_coefficient_parameter_geometry/01_FCG_E02_R1_POISSON_LOCALIZATION_ASSESSMENT_20261030.md
[results]: ../../../../../result-summaries/README.md
[identities]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a14]: ../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
