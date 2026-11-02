# MC01-E01: separate review of the frozen thermal-source return

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewer `/root/review_thermal_fermion`, actual recorded **gpt-6.1-sol (Codex), reasoning effort ultra**. Own rollout `01a19a53-8e12-7bd0-ae29-5de242d6c4b0`, turn `01a19a53-8e26-7d42-903c-91c9afc93375`, records that configuration. The author's specified rollout and turn were also checked and record **gpt-6-astra / ultra**. This is a separate **cross-model internal LLM review**, with shared canonical source, accepted baseline and research instructions; it is not independent specialist review.

**Disposition: accept the frozen identities and scoped obstruction without mathematical correction. MC01-E01's bounded review is complete.** The source has the stated positive filtered circle-thermal realization on the half-line, and the derivative determinant is the stated signed multi-copy observable. The fixed one-mode witness correctly defeats positivity-only pointwise transfer in its declared comparison class. The complete Mellin comparison remains unproved on every claimed range. No new theta sign, coefficient range or RH consequence is accepted.

## Frozen scope and evidence

The [request r1](../numerics/MC01_E01_REVIEW_REQUEST_R1_20261101.json) fixes one analytical pass and the one exact support replay. Its SHA-256 is `f34027a958188cd3a66e6f6daf144ee3a7f755ef2513f51f5557b12b3297ffa8`. Before opening the return, its bytes were checked against the contract:

- [Return01](../notes/01_THERMAL_SOURCE_IDENTITY_RETURN_20261101.md): `8f063727f1e56f36462e697bd42e27ea074a4af43f01d98227d33d6f500ca439` — match.
- [Exact support program](../numerics/mc01_b01_thermal_polynomial_check.py): `abe96a55339b3991168de243b691142c8b230fa99fab9157a49ca49d7982f2b6`.
- [Initial Mellin assessment](../../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md): `ee4280708b43d4d080fe98c128d58c0180f0ba0851b730bd859c2a899f84d9de` — the inherited consumer version.

The original return, checker and evidence were not edited. The checker was read before one replay, using Python `fractions.Fraction`; it performs polynomial/rational algebra, not theta truncation, quadrature or a numerical campaign. The accepted [J-E03 assessment](../../../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md) is an inherited premise for canonical monotonicity, not a certificate independently rerun in this review.

Read with the [result index](../../../../../../../result-summaries/README.md), particularly [physical channels](../../../../../../../result-summaries/06_physical_channels_wzw_ym_and_collar.md), [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md) and [theta identities](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and the [avoid index](../../../../../../../avoid/README.md), particularly [reformulations](../../../../../../../avoid/01_restating_the_target.md), [shared-premise review](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md), [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [normalization](../../../../../../../avoid/08_normalization_and_constant_slips.md).

## Reconstruction and response calculations

For the periodic circle basis, \(L\) has eigenvalues \(\pi n^2\), \(n\in\mathbb Z\). The trace of \(P_0(\beta L)e^{-\beta L}\) therefore has two copies of each positive-square contribution. Its zero mode vanishes because \(P_0(0)=0\). Multiplication by \(e^u/2\) yields exactly both terms of every canonical summand, including the coefficients 2 and -3 and the exponents 9u and 5u. There is no missing ground-state constant. On \(u\ge0\), nonzero \(x_n\ge\pi>3/2\), so the insertion is positive. Polynomial heat damping makes the normalized operator trace class. The claim is correctly limited to this filtered, temperature-dependent state; ordinary Gibbs susceptibility cannot be substituted.

Differentiating a summand uses \(x'=4x\), giving \(P_{m+1}=4xP_m'+(1-4x)P_m\). In addition to the printed P2 and P4, the intervening polynomials are
\[
P_1=-15x+30x^2-8x^3,\qquad
P_3=-375x+3270x^2-4232x^3+1440x^4-128x^5.
\]
These reconstruct all P0–P4. The fixed checker agrees exactly. Dividing complete sums by the positive source gives the stated expectations of P2/P0 and P4/P0. Multilinearity in the three determinant columns proves the independent-copy expectation in (8). It preserves the determinant orientation and every spectral occupation. Ordered temperatures do not order those occupations.

For \(a=u+\log P_0(x)-x\), direct differentiation gives
\[
a'=9-4x+12/(2x-3),\qquad a''=-16x-96x/(2x-3)^2.
\]
Differentiating normalized weights gives the displayed expectation derivative plus covariance. Repeated application yields all four logarithmic responses in (13), including the coefficients 3 in the third response and 4, 3, 6 in the fourth. In particular, the fourth mixed cumulant is retained, and the thermal variance has the opposite sign to the negative single-mode second logarithmic derivative. State positivity supplies no sign for the required combination.

## Witness, residual and curvature

The exact replay returned
\[
r(4)=-291/5,\quad r_x(4)=952/25,\quad r_{xx}(4)=4192/125,
\]
\[
z(4)=44021/5,\quad z_x(4)=-255952/25,\quad z_{xx}(4)=-1702592/125.
\]
Thus \((z_{xx}r_x-z_xr_{xx})/(2r_x^3)=-157375/99127\), as claimed. The factor 1/2 is the confluent second-divided-difference normalization. Since \(r_x(4)>0\), continuity supplies distinct nearby ordered u points with the same negative ratio. The energy distribution in this one-mode comparison has zero response fluctuations; the ± circle degeneracy does not alter that fact. This is a valid obstruction to pointwise inference from positive filtered states and single-mode log-concavity. It lacks full theta spectrum and reflection, so it supplies no negative canonical integral, canonical curvature counterexample, or integer endpoint identity.

The logarithmic derivative identities give precisely
\[
U=S-R^2=\ell_4+4\ell_1\ell_3+2\ell_2^2+4\ell_1^2\ell_2
=R''+2\ell_1R'.
\]
Using accepted \(R'>0\), the determinant quotient is the second divided difference of \(S(y)=y^2+U(y)\), hence \(h_3=1+U[y_1,y_2,y_3]\). For \(e^{-au^2}\), direct differentiation gives \(U=-8aR-8a^2\), confirming \(h_3=1\) without a missing constant.

Writing \(A=1+E_s\chi\), differentiating \(\log M=\log Z+\log A\) gives (17), including the centered-square covariance and the negative squared covariance term. Multiplication by positive \(A^2\) gives exactly (18), with the displayed signs. Its truth is neither implied nor tested by the fixed rational witness. The inherited integer factor is also correct: Andréief on the ordered chamber leaves \((2k)!(2k+2)!(2k+4)!\), with no extra 3!.

## Domains, physical scope and remaining obligation

The complete series differentiates termwise on the half-line. The degree m+2 response polynomial gives the stated \(e^{(4m+9)u}e^{-\pi e^{4u}}\) envelope after summing a convergent square tail. Full reflection, rather than a first mode, gives evenness and the origin derivative cancellations. Fixed log powers are integrable at zero for \(s\ge0\), and double-exponential decay handles infinity uniformly on compact s intervals. At node faces, using the undivided product of the two determinants avoids an unjustified quotient bound. These payments justify the representation and response identities; they do not compare the signed response with \(\kappa_3\) as s grows.

The control table keeps the right distinctions: modified square weights lose unchanged unit multiplicities/full reflection; reflected and shape/primitive controls lack the literal complete circle spectrum; modified Euler factors lose the exact arithmetic reconstruction. None is assigned an uncomputed curvature sign. A positive-time collision does not contradict a time-zero fixed-order statement. Gaussian equality checks normalization only.

**Classification:** (1)–(17) are exact identities or physical realizations under the stated baseline; (14) is a proved scoped obstruction; (18) is the unpaid target restated in those variables. The physical observable dictionary is useful and faithful. It carries no independently acquired estimate. No new external theorem was needed for these checks; the thermal/cumulant/exterior identities were derived directly. The common primary-source inspection limits remain unchanged.

**Corrections:** none required. **Unresolved issues in the fixed claimed identities/obstruction:** none identified. **Unproved research target:** the full Gaussian Mellin comparison, including s in [0,2] and the unbounded range. This review stops at MC01-E01; it issues no new E task or campaign. The coordinator alone integrates the disposition and shared records.
