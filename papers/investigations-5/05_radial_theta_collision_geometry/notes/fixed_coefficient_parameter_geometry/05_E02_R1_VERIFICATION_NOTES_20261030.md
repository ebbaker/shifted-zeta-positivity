# FCG-E02 R1: normalization, strip estimates, and exact loss verification

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol**, reasoning effort **ultra**, Investigation05 **chat0044**, *Assess FCG-E02 R1 obligations*.

**Status: supporting analytical verification for the [six-check assessment][review]; no mathematical correction to B02 R1.** Keep FCG-C01 R1, c=1, K*=[1/8,3/8]×[4,45], unit preparation, original drift and literal cosine. This note supplies details behind acceptance, rather than a new signed mechanism. [Progress06][progress] alone owns live status. The [issued packet][packet] and [B02 proof][b02] remain unchanged.

## 1. Normalization and domination

The half-line quadrant maps to the cone z≥|w| under u=z+w, v=z−w, with absolute Jacobian 2. Symmetrizing the two source variables gives

\[
\Gamma=\tfrac12(u^2+v^2)\cos(Au)\cos(Av)+uv\sin(Au)\sin(Av),
\quad \eta=\cos(Au)\cos(Av)+uv\sin(Au)\sin(Av).
\]

The addition formulas give exactly B02's Γ and η in cone coordinates. With P=e^uΘ(e^{4u}), Φ=(P''−P)/16 and

\[
(\partial_u^2-1)(\partial_v^2-1)=\mathcal D/16,
\qquad \mathcal D\Pi=4096\Phi(u)\Phi(v).
\]

For G=(8π)^(−3/2), Gaussian convolution followed by spherical averaging gives

\[
B_0=G e^{-(r^2+t^2)/8}\frac{\sinh(rt/4)}{rt/4}
=\frac{2G}{rt}\left(e^{-(r-t)^2/8}-e^{-(r+t)^2/8}\right).
\]

Since rt=e^{4z}, B02(6) has the correct coefficient. For each mass-one seed g_s(u), preparation gives ||g_0(u)||₂²≤G. The imported energy/Nash inequality gives a whole-time bound by M=max{G,(3/c_N)^(3/2)}, independent of u. Cauchy–Schwarz yields 0≤B_s≤M. Each fixed seed has a finite first spatial moment, so the inherited fixed-flow convergence applies individually and B_s(u,v)→Q(1). Uniformity of that first moment over all u is unnecessary: the uniform B bound and complete source moments dominate the subsequent u,v integrals, even after taking the supremum over p∈K*.

Old Note42's joint derivative bound restricts legitimately to the cone. With |Ψ_C|≤(1+C)Ω+C, its majorant is a polynomial times exp(−εΩ²+2TΩ+18√Ω), integrable in every escape direction for ε≥ε₀>0. The window is outside D, and no integration by parts is performed. No boundary term or unwindowed interchange is being suppressed.

In particular,

\[
\mu_j^+=2\int_{\mathcal C}\Omega^j e^{2T\Omega}\Phi(z+w)\Phi(z-w)\,dz\,dw,
\quad
\mu_2^+=\frac{m_0m_4+m_2^2}{2},\quad
\mu_3^+=\frac{m_0m_6+3m_2m_4}{4}.
\]

The factor 2 is already absorbed by the coordinate change. Thus |R|≤Mε{(1+C)μ₃⁺+Cμ₂⁺}, using moments through order six. This is an absolute allowance; it has no energy denominator.

## 2. Explicit narrowing-strip bounds and rate

Write θ=tanh(4w) and q=1−θ². Acting on f(w)p(θ), differentiation becomes

\[
f^{-1}\partial_w(fp)=4(1-\theta^2)p'-2\theta p.
\]

Four applications and D=(∂_w²−4)² on z-independent functions give

\[
\mathcal Df/f=528-2208\theta^2+1680\theta^4
=48q(35q-24),\qquad \mathcal Df(0)=528/\sqrt2.
\]

For |w|≤δe^(−2z), z≥0,

\[
|r-t|\le4\delta\cosh(2\delta),\quad r+t\ge2e^{2z}.
\]

Put a_δ=exp(−2δ²cosh²(2δ))>0. After increasing z₀ so exp(−e^{4z}/2)≤a_δ/2, admissible comparison constants in B02(7) are b₋=Ga_δ and b₊=2G. Also

\[
\Psi_C\ge z^2-
\{2A^2z^2+1+C[A^2(1+z^2)+1]\}w^2\ge z^2/2
\]

for sufficiently large z₀, uniformly in bounded A,C. Positivity of Df persists there. The overlap costs e^(−4z), and the strip width costs e^(−2z); their product gives the positive-part lower integral ∫z²exp(2Tz²−6z)dz=∞. The constant kernel Q(1) leaves only the width cost. Neither argument assigns a value to the whole signed undamped integral.

For Z=√(T/ε), z∈[Z,Z+1], the penalty ε(Ω−T/ε)² is at most 4T+o(1). This proves B02's lower budget bound after absorbing bounded constants. For the upper bound, 18√Ω≤αΩ+81/α gives an exponential rate at most (T+α/2)². First take ε↓0 at fixed α>0, then α↓0. Hence ε log A_ε→T² at B₀ and Q(1), for fixed p,C. The complete-source absolute integral stays bounded. No intermediate-s lower rate or signed-source divergence follows.

## 3. Exact exterior loss and controls

For the complete positive measure dμ_s=2e^{2TΩ}B_sΦ(u)Φ(v) dzdw,

\[
M-\mathcal E=F-\int(1-\chi)(\Psi+|\Psi|)\,d\mu_s
=F-2\int(1-\chi)\Psi_+\,d\mu_s.
\]

At any z₀>0,w=0, Ψ_C≥z₀² uniformly in A∈[4,45]. At fixed finite C, continuity over the compact parameter range gives a common open patch inside the cone with Ψ_C≥z₀²/2. Complete source positivity, Q(1)>0 and 1−χ>0 give a strictly positive uniform limiting loss for fixed ε>0. This floor bounds the loss, not |J|. At a hypothetical theta double event F_s→0, so this lower bound tends to −Δ_∞<0, conditionally on that event. A new source-derived signed estimate could still exclude the event.

The generic loss applies without conditioning at the two admitted controls' actual events, using their own source products. The Gaussian-polynomial source has moment domain T<17/4; the finite positive-square source has double-exponential half-line tails. Both admit K* and the required prepared moments. Their failed premises remain, respectively, the full arithmetic source relation and unit coefficients/full reflection. No Poisson mode formula is assigned to them; the weighted-square event is not a finite all-real threshold. The sign-changing example B02(14) is valid inside the cone and defeats pointwise positivity alone.

The [exact replay][script] and [small record][record] check Df, the differential normalization, moment coefficients and the eight input hashes using standard-library rational arithmetic. They do not verify analytic tails or evaluate theta data. Three read-only Sol contributions assisted the analytical assessment; they share the coordinator's model and inherited premises. This is a different-model internal assessment of Astra's return, with no independent specialist or formal verification.

The [result index][results], [theta identities][identities], [controls][controls] and [avoid index][avoid] retain their source status words. In particular, [separate bounds][a12], [scoped negatives][a07] and [circular floors][a14] prevent promoting this failed estimating route to a universal C01 exclusion. No manuscript or result-summary milestone is asserted before B03 disposition. See the [continuation][continuation].

[review]: ../../reviews/fixed_coefficient_parameter_geometry/01_FCG_E02_R1_POISSON_LOCALIZATION_ASSESSMENT_20261030.md
[progress]: ../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md
[packet]: ../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R1_POISSON_LOCALIZATION_ASSESSMENT_20261030.md
[b02]: 03_POISSON_LOCALIZATION_AND_RELATIVE_LOSS_B02_20261030.md
[script]: ../../numerics/fixed_coefficient_parameter_geometry/verify_fcg_e02_r1.py
[record]: ../../numerics/fixed_coefficient_parameter_geometry/fcg_e02_r1_exact_check_20261030.json
[continuation]: 06_CONTINUATION_FCG_B03_AFTER_E02_20261030.md
[results]: ../../../../../result-summaries/README.md
[identities]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a14]: ../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
