# MC07-E01 separate fixed review: Donaldson Witten assessment

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **E — fixed analytical checking**, request R1; reviewer **gpt-6.1-sol / ultra**, independently read from the reviewer's actual rollout turn metadata. Reviewer thread `01a19a87-f894-7a33-8595-6bcd2617192c`, turn `01a19a87-f89c-7772-9ec7-d3857e5eb0ce`; parent author **gpt-6-astra / ultra**. This is separate cross-model internal LLM checking with shared inputs, not independent specialist human review.

**Disposition: accept the complete-source flux-response identity, the scoped CP2 protected-correlator mismatch, and the projected K3 Gaussian comparison, with the two minor clarifications in Section 6.** No substantive correction to equations (3)–(14) or their main mathematical conclusions is needed. The frozen return and source note were hash-verified before checking and remain unchanged.

## 1 Scope, input binding and primary passages

The [frozen return](../notes/01_DONALDSON_WITTEN_FEASIBILITY_RETURN_20261101.md) has SHA-256 `e2308c6a3d9b1d758ac85758fb18f88fb9f0e6229678d355c8f4d9417f9b9383`; the [source note](../../../../references/08_DONALDSON_WITTEN_ASSESSMENT_SOURCES_20261101.md) has SHA-256 `25b6e76fbeca37e0dfc3110b33283a8047b35c5297e2c0cb3d64d0295a0d6ea0`. The [review record](../numerics/MC07_E01_REVIEW_RECORD_20261101.json) also binds the request, checker, primary archived PDFs and this review.

One analytical pass covered exactly the issued claims. I read Moore–Witten (1.2)–(1.8), (2.26), (3.18)–(3.21), Section 3.2, (4.6), (9.24), and Appendix A, checking printed pp.30–31 visually for overbars and superscripts. I checked Witten (2.8)–(2.11), (3.13), and the descent/Donaldson interpretation; printed p.366 was visually inspected. I checked Kronheimer–Mrowka Definition 1.4, (1.5), admissibility/Theorem 1.7, K3 Example 1, and the distinction expressed by (1.10); the definition and K3 example were also inspected visually. Primary PDFs were read from the supplied archives and the corresponding primary URLs were opened. This is not a full-paper or novelty review.

## 2 Genuine protected candidate and the degree obstruction

The CP2 data are consistent: complex orientation gives intersection form `[1]`, so the unit period is H, all harmonic two-forms are self-dual, and the stated Betti numbers, Euler characteristic and signature follow. Fixing the SU(2), equivalently SO(3) zero-w2 sector, fixes the bundle parity while summing instanton numbers. No simple-type theorem for b+>1 is used. The selected metric/chamber and the vanishing SW contribution agree with the specialization used in [Moore–Witten, Section 9](https://arxiv.org/pdf/hep-th/9709193v2).

By descent, the surface class is Q-closed. Consequently the literal insertion `I(H) exp(z I(H))`, with the usual gauge-invariant cohomological interpretation of Q, is Q-closed coefficientwise. Its expectation is exactly the derivative at **p=0** in (3), with no extra point projection. The fact that the exponential mixes degrees does not defeat closure; the grading selects the nonzero coefficients.

Independently applying degree matching to the formal index gives

\[
2N+4m=8k-6,\qquad m=0\Longrightarrow N=4k-3\equiv1\pmod4.
\]

Thus differentiating the surface series leaves powers z^(4j), and `[z²] C_D=0`. This uses only the full instanton grading in the stated SU(2) convention, consistent with [Witten (3.13)](https://www.ias.edu/sites/default/files/sns/%5B109%5DCommMathPhys117-1988.pdf). It does not identify Witten's instanton symbol with the modern adjoint Pontryagin number. For theta, every summand in (1) is positive at beta>=1, since `2 pi beta n²>3` for n>=1; convergence and positivity give c0,c1>0. The coefficient gap therefore proves the failure under the declared nonzero overall factor and nonzero linear rescaling through zero, even if the rescaling is complex. It makes no statement about an affine shift, nonlinear change, other source or insertion.

The published low-degree convention is essential: the linear coefficient is present. Using the factorial convention in the cited (1.3) and the polynomial coefficients of (9.24), differentiating and multiplying by -2/3 gives exactly

\[
\mathcal C_D(z)=1-\frac{z^4}{36}-\frac{z^8}{20160}+\cdots.
\]

This is the published convention, not a new direct construction of the low-dimensional moduli-space invariant. In particular d1=0, d2=-1/36, and the stated rank-two minor is +1/36. Its sign cannot fix the failed rank-one coefficient identity.

## 3 Flux response, phases and the complete theta source

The direct specialization of (3.18) has lambda=nH, lambda0=0 and no half-shift. Its characteristic factor is (-1)^n; S_-=lambda_-=0 and the other flux-independent factor is 1. Visual inspection confirms **unbarred J=du/da** in the insertion and **barred tau** on lambda_+². The n term pairs to zero. What remains is precisely the return's

\[
\Psi(\tau,t)=\frac{itJ(\tau)}{4\pi y}
\sum_{n\in\mathbb Z}(-1)^n e^{-i\pi\bar\tau n^2}.
\]

On tau=1+i beta, the residual phase is (-1)^(n+n²)=1. The declared normalization cancels the entire prefactor, so R(beta)=theta(beta) for **every beta>0**, retaining the zero mode and both signs of every nonzero mode. The product expansions of theta2 and theta3 have nonzero factors with a locally uniformly convergent product in H; hence their product, and the reciprocal J=2/(theta2 theta3), have no interior zero or singularity. The normalization is therefore defined on the entire chosen line.

The Gaussian summands and their fixed beta derivatives converge normally on compact subintervals of beta>0. Differentiating the **whole normalized response** gives (7), removes the zero mode, and yields `(2 pi² beta² n⁴ - 3 pi beta n²) exp(-pi beta n²)` for each positive n. The source, multiplicity and negative first-derivative contribution are all retained. Freezing beta/J when differentiating would fail this identity. These conclusions are algebraic consequences of the specified integrand extraction; they do not make that extraction a protected invariant.

## 4 Full modular expression and contact derivative

Equations (8)–(9) retain the correct source contact term and the measure specialized to sigma=1, with the source's branch convention. Gamma^0(4), defined by the **upper-right** entry condition, is the required group. The regularization is coefficientwise in p,t, with the real cusp coordinate integrated before the height cutoff is removed; cusp width is 4 at infinity and 1 at the other two cusps. This does not assert absolute convergence of the unexpanded expression.

After the flux pairing, the t dependence in the integrand is `t exp(t² T_hat)`. Its derivative is exactly `(1+2t² T_hat) exp(t² T_hat)`. This is a coefficientwise formal differentiation, so it requires no unproved interchange with a globally convergent unexpanded generating integral. The contact derivative cannot be discarded. Neither the complex measure nor the fixed-line response establishes positivity of the full modular integral.

## 5 K3, determinant bookkeeping and controls

The [Kronheimer–Mrowka definition and K3 example](https://people.math.harvard.edu/~kronheim/structhm.pdf) give precisely the **projected** series with factor `(1+point/2)`, and sign +1 for w=0 with the stated homology orientation. It is not the p=0 pure-surface generating function. Independently, integrating `C exp(-a x²) cosh(zx)` over the half-line gives the normalized factor `exp(z²/(4a))`. Taking a positive real homology ray with Q(S)=1/(2a) gives the return's identity. No assertion about integral classes of arbitrary norm is required. For its normalized coefficients, the rank-two formula follows directly from `d_(k-1)d_(k+1)=k d_k²/(k+1)`; k=0 is covered by d_-1=0.

The source-side identities D1,k=c_k, D2,0=c0² and D2,k=c_k²-c_(k-1)c_(k+1) have the right determinant orientation and factorials. The fixed rational checker was replayed once and returned d0=1, d1=0, d2=-1/36, d4=-1/20160 and D2,1=1/36. This checks imported-coefficient arithmetic, not the literature or the degree-selection proof.

The controls are appropriately scoped against the [control screen](../../../../../../../result-summaries/12_collision_controls_and_screening.md), [result index](../../../../../../../result-summaries/README.md) and [avoid index](../../../../../../../avoid/README.md), especially [factor versus target](../../../../../../../avoid/13_a_factor_is_not_the_target.md) and [shared-premise reviews](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md). Changing the weights or square support changes the selected exact flux dictionary. Other control response signs have not been assigned. No control has passed a new theta-specific inequality. In contrast with the accepted MC06 circle assessment, (3) is already Q-closed; the failure here is its coefficient match. The exact pre-integration response remains distinct from it.

## 6 Clarifications and final disposition

1. Equation (9) contains the typesetting string `-4\sqrt2,i`. Read this as `-4\sqrt2\,i`, the multiplicative imaginary unit in the primary formula. The comma is punctuation, not part of a new measure convention.
2. The control-table row “any nonzero positive source with finite first moments” needs precise scope: a nonnegative density, or a nonnegative measure with positive mass on x>0, and finite moments through x². Then c1>0. Finiteness of only the first power moment does not guarantee a finite c1, and a point mass at zero has c1=0. The canonical source satisfies the stronger conditions, so the selected obstruction is unchanged.

**Accepted with these minor clarifications:** equations (3)–(14) at their declared scope, the complete source recovery, the missing z² coefficient of the selected protected correlator, and the projected K3 comparator. No new Mellin bound, determinant sign theorem, Gaussian comparison interval, RH formulation by a protected Donaldson invariant, broad simple-type no-go, or universal TQFT exclusion follows. There is no unresolved import blocking this scoped acceptance. The fixed E check is complete; shared status and synthesis integration belong to the coordinator. No alternative model or numerical campaign was launched.
