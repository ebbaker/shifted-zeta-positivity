# FCG-E02 R2 verification notes

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol**, reasoning effort **ultra**, Investigation05 **chat0047**, *Continue FCG-E02 R2 assessment*.

The [seven-check assessment][review] accepts [Note12][source] without mathematical correction under the [frozen request][packet]. These are supporting derivations, not a new coefficient construction. The source, radius-\(1/16\) ball, literal cosine, original drift, unit preparation and full spatial domain remain those of Note12. Three read-only same-Sol contributions checked moments, flow dependencies, and controls/scope; the parent reconciled them. All share inherited premises. No specialist or formal independence is claimed.

## 1. Complete source and exact comparisons

Write \(q=\pi n^2e^{4u}\). Each physical source summand is
\[
 \Phi_n(u)=e^u q(2q-3)e^{-q}>0\quad(u\ge0).
\]
The double-exponential tail dominates \(u^j e^{tu^2+bu}\) for every fixed finite \(t,b,j\), after complete index summation. This supplies the complete parameter and spatial moments used below. For \(\psi_n=e^u e^{-q}\),
\[
 \psi_n''-\psi_n=e^u(16q^2-24q)e^{-q}=8\Phi_n.
\]
The complete modular-even \(P=e^u+2\psi\) has \(P'(0)=0\), hence \(\psi'(0)=-1/2\). Only decaying \(\psi\) is integrated. Its upper derivative and value vanish, yielding
\[
 M_0(0)=\frac1{16}-\frac18\int_0^\infty\psi.
\]
The \(1/16\) is a retained boundary contribution.

For \(n\ge1\), \(n^2\ge1+3(n-1)\). Thus the complete positive series satisfies
\[
 \mathcal S=\sum_{n\ge1}n e^{-\pi n^2}
 \le\frac{e^{-\pi}}{(1-e^{-3\pi})^2}<\frac1{21}.
\]
The usual elementary bounds \(31/10<\pi<22/7\), the finite exponential partial sum, and positive exponential remainders justify every strict comparison; there is no decimal approximation to the source.

The second-moment Gaussian step is
\[
 2\pi^2n^4\int_0^\infty u^2
 e^{-(8\pi-5/16)n^2u^2}\,du
 =\frac{\pi^{5/2}}{2(8\pi-5/16)^{3/2}}n.
\]
Here the negative source term was dropped only in an upper bound, and the linear decreasing exponential was bounded by one. Tonelli applies to the full nonnegative majorant.

Selected exact comparisons in the [bounded replay][script] and [record][record]:

| Comparison | Exact value or positive gap |
| --- | --- |
| \(\sum_{k=0}^{8}3^k/k!\) | \(89641/4480>20\) |
| \(1/21-(1/22)/(1-22^{-3})^2\) | \(244397/113358609\) |
| \(1/16-1/1848-3/50\) | \(181/92400\) |
| \(8(31/10)-5/16-24\) | \(39/80\) |
| \(18/[2\cdot24\cdot(24/5)]\) | \(5/64\) |
| \(3/800-5/1344\) | \(1/33600\) |
| \(1-25(3/800)/(2(3/50))\) | \(7/32\) |
| \((3/50)(7/32)\) | \(21/1600\) |

The exact script checks algebra and frozen bytes. It does not evaluate theta, prove modularity or certify the analytic semigroup arguments.

## 2. Carrier normalization, cutoffs and all-time floor

Since \(\sqrt{\cos^2(Au)+u^2\sin^2(Au)}\le1+u\) and \(T\le T_+\), the positive common scalar kernel gives
\[
 |W_0(p)|\le G_B,\qquad |P_s^cW_0(p)|\le P_s^cG_B=\Sigma_c(s).
\]
For the radial source,
\[
 \frac{4\pi r^2\,dr}{8\pi r^3}=\frac{dr}{2r}=du.
\]
Thus the raw carrier has mass \(L\) and second moment \(R_2\). Centered \(K_1\) has covariance \(2I_3\), so preparation gives exactly \(N_c(0)=R_2+6L\).

For completeness, localize with \(f_R(X)=|X|^2\chi(X/R)\), where \(\chi\) is smooth, equals one on the unit ball and vanishes outside radius two. On the cutoff annulus,
\[
 |\Delta f_R|+|v\cdot\nabla f_R|\le C(1+|X|^2),
\]
uniformly in \(R\). The globally Lipschitz linear-growth drift and initial finite moments give finite moments on every bounded time interval, by the same localized generator estimates and Gronwall (or the nonexplosive diffusion construction). This supplies an integrable domination for removing cutoffs in the time-integrated identity. No unproved whole-time moment bound is assumed to prove itself. Removing \(R\) first gives
\[
 N_c'=6L-2c\int X\cdot v\,\Sigma_c
 \le6L-2cN_c\quad(c>0).
\]
Consequently
\[
 N_c(s)\le e^{-2cs}N_c(0)+(3L/c)(1-e^{-2cs})
 \le\overline N_c.
\]
All of \(\mathbb R^3\) is retained; the raw cutoff at \(r=1\) is not a spatial boundary condition.

Put \(R_X^2=2\overline N_c/m_B\). Markov's second-moment inequality pays the complete exterior:
\[
 \int_{|X|>R_X}\Sigma_c\le m_B/2.
\]
Conservation of vector mass and the triangle inequality then give
\[
 m_B/2\le |B_{R_X}|^{1/2}\|W_c(s;p)\|_2.
\]
Squaring and using \(|B_{R_X}|=4\pi R_X^3/3\) yields Note12(14), including \(3/(16\pi)\). This establishes \(S_B=0\) independently of stationary convergence.

## 3. Strict control signs and ordinary zeros

Let \(g(x)=\cos x-1+x^2/2\). It is even, \(g(0)=g'(0)=0\), and \(g''=1-\cos x\ge0\). Integration shows \(g(x)>0\) for every \(x\ne0\). A source with positive mass at \(u>0\) therefore has
\[
 H(T_0,A_0)>M_0(T_0)-\tfrac12A_0^2M_2(T_0)\quad(A_0\ne0).
\]
At any zero the right side is strictly negative. Monotonicity makes every admissible containing-ball margin no larger, hence \(c_B<0\). This includes simple zeros with \(H_A\ne0\); no derivative premise was used.

For the Gaussian control at \(T=1/4\), the effective source is \((64u^4+6)e^{-4u^2}\). With \(I_j=\int_0^\infty u^j e^{-4u^2}\,du\),
\[
 (I_0,I_2,I_4,I_6)/\sqrt\pi
 =(1/4,1/32,3/256,15/2048).
\]
This gives \(M_0=9\sqrt\pi/4\), \(M_2=21\sqrt\pi/32\), \(M_2/M_0=7/24\) and the center coefficient \(-5/2\). The containing-ball coefficient is strictly smaller; its moment domain remains \(T<17/4\).

The three-positive-square source has complete moments at every finite real \(T\). Its event bracket lies within \(1/20000\) of \(44.13035\), inside its own radius-\(1/16\) ball. Its negative coefficient follows analytically from strictness, with no certificate replay. Unit coefficients and full reflection fail; the event is not promoted to an all-real threshold. Other registered controls retain their actual domains and failed premises.

## 4. Imported zero-mass decay and compact-uniform derivatives

The [fixed-flow proof][fixed], not the all-time floor, supplies the two convergence-dependent conclusions. For prepared zero-mass \(f\), let \(\ell=\|f(0)\|_1\), \(P=\int |X||f(0,X)|\,dX\), \(E=\|f\|_2^2\), \(G=\|\nabla f\|_2^2\). If \(\ell=0\), \(f=0\). Otherwise its actual estimates give
\[
 G\ge c_NE^{5/3}\ell^{-4/3},\quad
 E\le\overline E,\quad
 G'\le-2G^2/\overline E+10cG+30c\overline E,
\]
\[
 \overline E=\max\{E(0),(3c/c_N)^{3/2}\ell^2\},\quad
 \overline G=\max\{G(0),\overline E(5c+\sqrt{25c^2+60c})/2\}.
\]
The Nash constant is consistent with the Fourier inequality
\[
 k^2E-G\le\ell^2k^5/(15\pi^2),
\]
optimized at \(k^3=6\pi^2E/\ell^2\). The inherited drift bounds give the displayed gradient barrier after retaining diffusion.

Synchronous contraction at \(\kappa=7/8\), zero mass and the first absolute moment imply
\[
 |\widehat f_s(\xi)|\le|\xi|Pe^{-\kappa cs},\quad
 E(s)\le\frac{P^2e^{-2\kappa cs}R^5}{10\pi^2}
          +\overline G/R^2.
\]
Choosing \(R=e^{2\kappa cs/7}\) gives squared-\(L^2\) decay at \(e^{-cs/2}\), exactly as imported. This uses no physical mass lower bound.

For each required parameter derivative, subtract its own stationary mass multiple of \(p_c\). The complete source tail and Gaussian preparation bound its \(L^1,H^1\) and first absolute moment uniformly on \(B\). The formulas for \(\overline E,\overline G,P\) stay bounded even when the subtracted field vanishes. Thus the [family note][family] gives compact-uniform \(L^2\) convergence of \(U,U_A,U_{AA}\). Uniform norm bounds and Cauchy–Schwarz transfer it to \(E_1,D_1\).

The three prepared frequencies in Note12 have distinct positive squares; Gaussian injectivity and the \(0,2,4\) derivative Vandermonde test establish independence. A nonzero element of their three-dimensional span has zero two-component mass. Its decay contradicts both boundedness and coercive nondecrease of the proposed common quadratic form. It is an arbitrary linear combination, not one physical cosine mark.

For C01,
\[
 M_2/m_B<2/7,\quad
 -HH_{AA}\ge-HM_2\ge-(M_2/m_B)H^2,
\]
so
\[
 \mathcal L+(9/7)E_J\ge H^2+(16/7)H_A^2\ge E_J\ge m_B^2.
\]
With spatial \(c=1\), the uniform limit is bounded below by \(Q(1)m_B^2>0\). This gives one uniform sufficiently late time, without an effective time value. The direct source floor is the identical information in both comparisons.

## 5. Consequence and continuation boundary

All seven checks are accepted. The coefficient is a sufficient scalar-\(H\) certificate, and its all-time flow consequence is proved in the stated ball. Its failure at simple zeros and the separate whole-span quadratic obstruction have different scopes. Neither excludes a joint-jet C04 mechanism.

E02 R1 retains its frozen six-check acceptance. Note07's subsequent regrouping was explicitly not part of that R1 assessment; it retains its original same-assistant derivation status. No source or issued packet is edited, no broader Poisson bound is supplied, and no manuscript/result-summary/milestone promotion is made.

The [continuation and model-change note][next] routes the open joint-jet design to **[B] FCG-B03 R3 — Astra**. Follow the [result index][results] and [avoid index][avoid], especially [classification][a01], [control premises][a02], [scope][a07], [separate bounds][a12] and [noncircular constants][a14].

[review]: ../../reviews/fixed_coefficient_parameter_geometry/03_FCG_E02_R2_REGIONAL_COEFFICIENT_ASSESSMENT_20261030.md
[source]: 12_REGIONAL_MOMENT_COEFFICIENT_AND_COMMON_FLOW_LIMITS_B03_R2_20261030.md
[packet]: ../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R2_REGIONAL_COEFFICIENT_ASSESSMENT_20261030.md
[script]: ../../numerics/fixed_coefficient_parameter_geometry/verify_fcg_e02_r2.py
[record]: ../../numerics/fixed_coefficient_parameter_geometry/fcg_e02_r2_exact_check_20261030.json
[fixed]: ../CHAT0042_FIXED_COMPRESSION_AND_NORMALIZATION_COMPARISON_20261030.md
[family]: ../CHAT0042_FIXED_FLOW_PARAMETER_FAMILY_AND_COLLISION_INDEX_20261030.md
[next]: 15_CONTINUATION_FCG_B03_R3_AND_MODEL_HANDOFF_20261030.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a14]: ../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
