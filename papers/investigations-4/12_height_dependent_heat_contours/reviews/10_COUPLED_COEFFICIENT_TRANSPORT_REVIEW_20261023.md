# Review of coupled coefficient backward transport and its wall support

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewer: a separate contributing agent using **gpt-6-astra (Codex)**, reasoning effort **ultra**. This is a separate same-model analytical review, not independent specialist validation.

**Disposition: accepted within the stated finite-population, fixed-wall scope, after the corrections recorded below.** The reviewed artifacts are [Note 12](../notes/12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md), including its coefficient-wall Appendix A, and the [exact-rational replay](../numerics/06_check_coefficient_transport_20261023.py). The reviewer reran the final replay: **PASS, 252 exact assertions**, matching the [execution record](../numerics/06_COEFFICIENT_TRANSPORT_CHECKS_20261023.json). These checks establish finite algebra and the displayed implications; they do not acquire canonical theta source data.

## Checked claims

1. **Complete prepared equation and source operator.** Analytic division gives the complete force \(\Psi=\mathcal T_P(bP_z)\) and \(P_t=-P_{zz}-2\Psi\), with the nonzero unit force retained. The source quotient \(Z_H=H_{zz}/H\) gives \(\mathcal A_HP=P_{zz}+2\Psi\) directly. This proof remains valid at repeated interior roots because it uses the complete prepared polynomial and analytic remainder, rather than division by individual root derivatives. Its paid denominator is the full-field wall floor; there is no hidden internal gap floor.

2. **Commuting source matrices and finite propagator.** For the fixed center and circle, \(\mathcal A_H=\sum_jM_{j-1}\mathsf S^j\), with the plain degree-lowering shift \(\mathsf S\), is correct. All source matrices commute, their exponential terminates, and the backward sign in \(\mathcal U_H(t,s)=\exp(\int_t^s\mathcal A_H)\) is correct. The exact weighted coefficient norm is the sum of absolute coefficients of its normalized shift polynomial. Its wall-only majorant \(\sum_{l=0}^n\binom nl V^l/l!\) follows from the coefficient sum of \(\exp(Vu/(1-u))\) through degree \(n\). No claim of a bound uniform in degree, time, or height follows from this finite-polynomial statement.

3. **Error residual and reference defect.** With \(d_*=P_{*,t}+\mathcal A_*P_*\), the difference equation is \(E'=-\mathcal A_HE-[(\mathcal A_H-\mathcal A_*)P_*+d_*]\). Its backward integral has a plus sign. The source residual is evaluated on the known reference polynomial, and its norm allowance \(\eta_ZW_R(P_*)+\eta_d\) has the correct circle normalization. The reference-defect contour formula correctly uses \((H_{*,t}+H_{*,zz})/H_*\); an approximate reference need not solve heat. The joint field numerator in the source-quotient difference and the explicit first-order fallback are algebraically correct.

4. **Source acquisition and logarithms.** Cauchy bounds for \((H-H_*)_{zz}\) are justified by analyticity and an absolute bound for \(H-H_*\) on the larger disk. A relative logarithm only on an annulus does not supply this missing interior hypothesis. The distinct logarithmic projection in Appendix A legitimately recovers the analytic-unit difference on an inner wall, provided the complete-population and nested-wall hypotheses hold. The endpoint moment formula has the correct minus sign and uses a continuous time lift of the wall logarithm; constant branch changes integrate to zero. Endpoint relative comparisons already consume early endpoint source information.

5. **Different perturbation models remain distinct.** For \(H=z^3-6tz\), the exact fixed-source operator is \(6\mathsf S^2\), giving a quadratic error a constant increment \(6(T-t)\). The free polynomial-heat operator gives \(2(T-t)\). Both are correct under their respective hypotheses, and comparing two different heat fields retains the source-quotient residual. The final note now states this explicitly. Its scalar feedback example now specifies a symmetric two-root cluster with fixed center zero; its closed residual reproduces \(\exp(4\int S)\), so the finite homogeneous propagator does not erase nonlinear source-feedback amplification.

6. **Wall support and controls.** Appendix A's remainder kernel, coupled-force numerator, reference-first split, coefficient-tube constants, nested-wall unit projection, and complete-source acquisition bounds were checked. Quadratic and cubic heat controls, a genuine constant-unit forcing example, and stationary sine cancellation require the full source unit and agree with the identities. The exact free-heat coefficient norm is sharp in the stated weighted norm. Internal collisions are allowed only while the fixed wall and declared source bounds survive.

## Corrections verified before acceptance

- The scalar feedback model now explicitly has a fixed center; no moving-frame drift is silently discarded.
- The cubic fixed-source/free-heat distinction is explicit, and the forest-note link uses its final `FILTER_ENCLOSURE` filename.
- A literal formfeed corrupting `\frac` in Appendix A's equation (S16) was replaced by the intended LaTeX command. A full control-character scan of the support file is now clean.

## Remaining boundary

The result is a useful coefficient error theorem and can feed [Note 11's forest-filter enclosure](../notes/11_FOREST_POLYNOMIAL_AND_GAP_FREE_FILTER_ENCLOSURE_20261023.md) without individual root disks. It does not provide a useful theta wall floor, an independently small complete-source quotient or integrated-moment error, a uniform growing-population budget, or the microscopic coefficient accuracy required by a heat-birth filter. All those source and scaling obligations remain explicit. If a residual is bounded only by the unknown coefficient error, closing that feedback may restore exponential amplification. The endpoint formulation has no uncharged advantage over equally informative direct endpoint source estimates. No simplicity or positive-proportion conclusion is established here.

## Separate contributing-agent controls and replay

23 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Separate same-model derivation and exact-rational replay; no specialist review or theta acquisition.

**Disposition: the complete finite coefficient equations, signed backward formulas and nilpotent source propagator pass the controls below.** Source/residual acquisition and growing-rank bounds remain separate hypotheses.

For H=UP and b=U_z/U, the monic prepared polynomial obeys

P_t=-P_zz-2 Psi,   Psi=Rem_P(bP_z).

The wall expression for Psi uses the polynomial kernel (P(w)-P(z))/(w-z) multiplying b(w)P_z(w)/P(w). Its residue at a root r of multiplicity m is m b(r)P(z)/(z-r). Exact long division agrees with the sum of these residues for both simple and repeated root populations. This verifies the sign, kernel order and multiplicity factors without using internal root gaps in the coefficient equation.

The backward Duhamel formula has the **positive** forcing sign:

P(t)=exp((T-t)partial_z^2)P(T)+2 integral_t^T exp((s-t)partial_z^2)Psi(s)ds.

For a monic difference of degree n=N-1, the fixed-center weighted coefficient norm has exact homogeneous amplification

C_n(h/R^2)=sum_k n! (h/R^2)^k/[k!(n-2k)!].

The highest-degree normalized monomial attains it. A positive constant-in-time monomial forcing also attains the integrated norm payment, so that payment is sharp within the independent absolute-error class. It does not supply the actual unknown joint residual Psi-Psi_*; Psi depends on both the source unit and the evolving polynomial.

The stronger complete-source equation is P_t=-A_H(t)P, with

A_H(t)=sum_{j>=1}M_{j-1}(t)S^j,
M_k=(2pi i)^(-1) integral_Gamma w^k H_ww/H dw,
S z^j=z^(j-1), S1=0.

These operators commute at different times because they are polynomials in the same nilpotent shift. The exact backward propagator is the finite exponential of the integrated moments. On degree n, if gamma_r are the coefficients through degree n of exp(sum_j J_j u^j), its induced weighted coefficient norm is exactly sum_r |gamma_r|/R^r. This is a polynomial dependence on the integrated moments at fixed rank, not automatically a polynomial bound in time or height.

**Do not interchange the two error generators.** For the exact cubic heat field H=z^3-6tz, A_H=6S^2. A terminal quadratic error z^2 propagated with this fixed exact source becomes z^2+6h. The unforced polynomial-heat error becomes z^2+2h. Both propagators recover the actual monic cubic, but they describe different hypotheses for perturbed coefficient data.

The stationary shifted-sine/cosine control with roots +/-1 has P=z^2-1. Its true exterior b agrees at those roots with -z/2, so Psi=-1: it exactly cancels P_zz=2. Dropping Psi incorrectly predicts P+2h. In the complete-source description H_ww/H is spatially constant, all M_k vanish, and P is stationary. The representative -z/2 is used only for the remainder; it is not a claim about the entire exterior unit.

The finite gain is real: quadratic and cubic constant coefficient errors have zero homogeneous amplification even near a collision, while resolving individual roots becomes singular. Nevertheless, with a=4t, a quadratic error epsilon=eta t gives q=2/(4-eta), and a centered cubic constant error eta t^(3/2) gives q=6048/(5184-27eta^2). Fixed normalized errors retain a nonzero filter bias. Coefficient propagation does not remove the source accuracy needed at microscopic time.

**Replay: 252 exact rational assertions, PASS.** The standard-library script checks remainder/residue identities, degree-2 through degree-8 heat matrices and sharp norms, eight forced Duhamel examples, stationary-source cancellation, and microscopic filter precision. It also independently derives Laurent moments of the actual complete fields H=exp(cz-c^2t)P, P=exp[-t(partial_z^2+2c partial_z)]P_0, integrates them exactly and recovers P(t) in 21 cases. Rational moment controls verify commutation, exponential composition and the exact weighted norm. JSON is emitted to stdout by default; optional file writing is explicit. These checks validate finite identities and sharp controls, not an acquired theta moment/residual budget or simplicity theorem.

Saved [replay script](../numerics/06_check_coefficient_transport_20261023.py) and [record](../numerics/06_COEFFICIENT_TRANSPORT_CHECKS_20261023.json).
