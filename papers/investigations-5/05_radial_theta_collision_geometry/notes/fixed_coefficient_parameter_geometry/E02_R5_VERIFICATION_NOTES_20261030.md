# Verification notes for FCG-E02 R5

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6.1-sol / ultra**, existing Investigation05 **chat0047**. These notes support the [nine-obligation assessment][assessment]; they are internal shared-premise checking, not independent specialist or formal verification.

**All nine obligations are accepted without mathematical correction.** The [source-free checker][checker] and [record][record] preserve the detailed input identity and arithmetic coverage. The 20 frozen source hashes and issued packet match. No source acquisition, control replay or manuscript/DRAFT_HISTORY edit was performed.

## 1. IBP, complex neighborhoods and the primitive

For \(F_j(u)=u^je^{(\tau+t)u^2}\Phi(u)\), \(\partial_A^jH=\int F_j\cos(Au+j\pi/2)du\). Since \(\partial_u\sin(Au+\phi)=A\cos(Au+\phi)\), IBP has the positive finite boundary and **negative** derivative integral in Note26(10). Orders 3/4 kill the lower endpoint. Complete superexponential theta decay kills the upper endpoint for every allowed complex parameter. \(|A|\ge a-R\) is a coordinate bound, without division by a physical field.

The derivative of \(e^{tu^2}u^je^{\tau u^2}\Phi\) separates into the signed center derivative plus \(2tu^{j+1}e^{\tau u^2}\Phi\). Bounding only after this separation gives the stated B majorant. For \(|x|\le R\), the power series give \(|\cos(xu)|\le\cosh(Ru)\), \(|\sin(xu)|\le\sinh(Ru)\). These establish the actual S/C phase weights. At a center sine zero the neighborhood boundary is bounded by \(\sinh(RU)\), and cannot be set to zero.

The residual's constant coefficient in u is zero. Its quadratic coefficient is
\[
 t-(a+x)^2/2+a^2/2+ax+x^2/2-t=0.
\]
The same holds after differentiating in x; both residuals are even and \(O(u^4)\). Hence the combined kernel has zero value and derivative at zero. For \(\Phi=(\psi''-\psi)/8\), double IBP leaves no lower endpoint for G, while a finite U retains \((\psi'K-\psi K')/8\) and the original complete exterior. This does not discard the \(1/16\) needed for H alone. The primitive identity was checked analytically; no second integration algorithm was substituted.

## 2. Taylor allowance and sharp radius

There are k+1 two-variable monomials of total degree k. Summing \(\sum_{k>N}(k+1)q^k\) gives the issued \(T_N(q)\); at q=1/2 it is \((N+3)/2^N\). Signed finite coefficients retain \(g_{10}=-h_1h_3\). All terms in \(\Gamma_N\) are nondecreasing in r. The exact Cauchy coefficient bound makes \(\Gamma_N-\Gamma_{N+1}\ge0\). These are exact mathematical comparisons; independent interval widths need not be monotone.

For q≤1/2, \(T_1(q)\le8q^2\), so the degree-one payment is at most \(L_0r+8Mr^2/R^2\). Setting it to D/2 and rationalizing the positive root gives
\[
 r_0=\frac{D}{L_0+\sqrt{L_0^2+16MD/R^2}}.
\]
The formula remains \(D/(2L_0)\) if M=0,L0>0, and the general both-zero case is handled by the stated infinite third cap. For the actual theta bounds, D>0 forces a nonzero row and M>0. The caps R/2 and τ/2 keep every geometric and time-domain premise. Rescaling the source by a positive amplitude multiplies D,L0,M by its square, leaving r0 unchanged. The older added-unit rule is valid and is not silently rewritten.

Saved-input exact arithmetic reproduces both B/C enclosures, checks their strict separation and confirms overlap across precisions:

| Quantity | Conservative enclosure including both stages |
| --- | --- |
| D | \([1.9058,1.9059]\,10^{-19}\) |
| B sharp radius | \([8.4593,8.4594]\,10^{-5}\) |
| C sharp radius | \([2.3160,2.6591]\,10^{-4}\) |

The declared rounding means the largest radius of form \(2^k\) no greater than the confirmed C lower endpoint. It gives 1/8192; the next power 1/4096 exceeds that endpoint. This convention is explicit, since “dyadic” alone would not specify a largest rational of arbitrary binary denominator. On that single ball, actual \(d_1>1.80\,10^{-19}\) and \(d_1-D/2>0\). It is a data-derived certificate, not an optimized or independently predeclared radius.

## 3. Analytic source and complete complements

The finite integrand is exactly
\[
 e^{Tu^2+(1+Y)u}u^j\sum_{n=1}^8
 (2\lambda_n^2e^{8u}-3\lambda_ne^{4u})e^{-\lambda_ne^{4u}},
 \qquad\lambda_n=\pi n^2.
\]
For jets, multiplication by the cycle cos,−sin,−cos,+sin at 64u supplies the signed derivative. Each stage's first six moments have \((T,Y)=(\tau+\rho,\rho)\), orders 3/4, at \(\rho=1/32,1/64,1/128\); the next 18 inputs are complete h0 through h17 at the center. Degree8 needs no higher jet.

For a tail component \(C\lambda^p e^{q_0u-\lambda e^{4u}}\), \(e^{4u}\ge1+4u+8u^2\) and \(T\le8\pi m^2\) give the issued factorial/beta mode integral. Its geometric ratios decrease with n. Beyond U, the positive tangent denominator and \(16\lambda e^{4U}>2T\) make the logarithm concave and give the retained exterior bound. Every recorded mode beta, ratio, time guard, eight source denominators and minimum concavity has the required strict or weak sign. The derivative tail uses all three coefficients 30,−15,−8, with absolute magnitudes only in the tail majorant.

The checker verifies all 52 complete binary intervals contain the finite analytic interval plus both complete complements: symmetric for signed jets and nonnegative for positive moments. The 24 common source intervals overlap across precisions. Inspection confirms 256/384 bits, the prescribed tolerance pairs, depth 30, evaluation limit 200000, Python 3.10.0, python-flint 0.9.0 and FLINT 3.6.0. Those versions describe acquisition; the assessment checker uses only standard-library rational arithmetic.

## 4. Real panels, absolute values and minimum

Each of the 1024 closed v ranges covers its entire subinterval of [0,1]; multiplying by U and dividing by the panel count keeps the Jacobian. For u≥0 each retained source mode is positive because \(2\lambda_ne^{4u}-3>0\), which justifies clipping only the known nonnegative source range. The signed derivative expression is combined before applying a safe interval absolute value. Zero-containing absolute values and squares have zero lower endpoint. The recorded D ranges cross zero on 11 panels for order 3 and 14 for order 4, at both precisions; no analyticity is assumed across those crossings.

For complete and finite derivatives, \(\big||D|-|D_8|\big|\le|D-D_8|\); thus the core mode correction is symmetric. Whole-line I adds a retained exterior and a second whole-mode payment. This duplicate is harmless conservative overpayment, not an equality to the smallest available envelope. W retains the signed finite endpoint source plus omitted endpoint modes, its full neighborhood boundary, a symmetric core correction and the original-form exterior. Replacing the exterior phase weight by its valid \(e^{Ru}\) majorant is conservative.

From binary aggregate panel sums and the recorded complementary bounds, the checker reconstructs all four I/W envelopes and the interval minimum \([\min l_i,\min u_i]\). It confirms W<I<M for both derivatives at both precisions and the reported ratios below 0.134 and 0.140. All fixed margins and improvement questions are decided without 2048 panels. The audit inspects the range algorithm and recomputes aggregate arithmetic; it does not regenerate individual panel source ranges or treat their digest as a mathematical proof.

## 5. All rows and matched consumers

The independent rational implementation reconstructs every finite coefficient sum and all displayed row quantities from the complete binary jets and selected bounds. All 72 rows are contained in their saved enclosures, including Gamma,d,c,K,mu and both scalar floors. It checks endpoint statuses and the least passing choices among1/2/4/8. Shared-input linear remainder gaps are strictly positive for all twelve (r,N) pairs per precision. Shared source, selected-envelope and all Gamma/d/c intervals overlap across precisions.

The representative's negative component floors are failures of those particular sufficient tests. They prove neither H=0 nor H_A=0 anywhere. Smaller positive C cases and the derived ball already have a positive H floor. The exact row strip receives the same information and yields at least d/K. All improvement is in the source allowance/radius/degree comparison; the spatial realization adds no source separation.

## 6. Representative and exact-coefficient energy

The prescribed rule selects C,r=1/128,N=8. Inspection confirms that two-stage confirmation precedes its four carrier integrals. The exact coefficient and mu intervals give c>1.78e−19 and mu>4.25e−10. Using the same source data, B2=|b|+r(U3+U4) satisfies \(1+B_2^{upper}/\mu^{lower}<361\). This supplies eventual C01 positivity at spatial coefficient 1 under the accepted compact-uniform derivative limit, without a numerical start time.

The carrier sums at T=17/64, orders 0/1 and Y=0/4 enclose complete L and R2. Unit Gaussian preparation contributes 6L. Consequently
\[
 L<0.068,\quad R_2<0.101,\quad
 \overline N=\max\{R_2+6L,3L/c\}<1.14\,10^{18}.
\]
The conservative reporting floor is verified without evaluating a fractional power numerically:
\[
 \frac{9(4.25\,10^{-10})^7}
 {2048(22/7)^2(1.14\,10^{18})^3}>(2.7\,10^{-62})^2.
\]
The accepted carrier theorem therefore gives the stated lower energy bound at every s≥0 for the exact defined coefficient. Rounded lower bounds are used for reporting, not substituted into the equation. This all-time result does not require the eventual C01 convergence theorem.

## 7. Controls, cost and provenance

The [control register][controls] is applied to actual event-containing domains with each control's own valid source bounds. Weighted-square collisions near 44.13 are not placed in the frequency 64 ball; a negative-Laguerre witness and a relaxed profile are not event locations. Shrinking away from a collision removes that test. Literal cosine/heat reconstruction, full theta arithmetic, moment domains, reflection/growth failures and conditional endpoint qualifications are retained. Atomic sources are not presumed differentiable for IBP. These controls limit universal interpretation without requiring a replay in this fixed assessment.

The acquisition recount is 28 distinct integrands, 52 calls, 31700 callbacks, maximum 732 per integral, 4 blocks/4096 panel ranges. Recorded timing sums are 1.0793884135782719 seconds analytic and 0.18771749886218458 seconds for the panel component, inside total 1.43011012498755 seconds. No replay or refinement was needed. A smaller bound and lower issued degree are established; comparative runtime savings are not.

The assessment preserves all original proof, acquisition and request bytes and the separate identities of proof/manuscript chat0048 and acquisition/assessment chat0047. Three read-only same-Sol contributions checked proof/radius, panels/margins and consumers/scope; the parent reconciled the complete record with a saved standard-library checker. These are internal shared-premise checks, with no independence implied by delegation or model change. No manuscript or integration source was edited.

This is a sufficient local mechanism and finite allowance comparison, consistent with [the result index][results], [avoid index][avoid], [shared-premise review][a05], [scoped exclusions][a07], [separate-bound accounting][a12] and [noncircular constants][a14]. It is not a proof of a uniform theta discriminant sign or an efficient coverage schedule. [The continuation][next] closes the execution and describes the optional B03/Astra decision.

[assessment]: ../../reviews/fixed_coefficient_parameter_geometry/E02_R5_ADAPTIVE_RADIUS_IBP_ASSESSMENT_20261030.md
[checker]: ../../numerics/fixed_coefficient_parameter_geometry/verify_fcg_e02_r5.py
[record]: ../../numerics/fixed_coefficient_parameter_geometry/fcg_e02_r5_exact_assessment_20261030.json
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[a05]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a14]: ../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
[next]: E02_R5_CONTINUATION_AND_MODEL_HANDOFF_20261030.md
