# Founding radial theta analytical self assessment

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

**Scope:** same-assistant analytical checking of [Note01][note] and its small exact control replay. This is not an independent review, numerical theta acquisition, or a proof of any proposed collision mechanism.

## Identities and boundary payments checked

- The Gaussian radial Laplacian has second coefficient -2d pi n^2, selecting d=3 in Phi=(1/2)r^(5/2)Delta A. Passing to the complete theta gives Phi=(1/4)r^(5/2)Q. The full Mellin observation has factor 1/16 and the exterior cosine observation 1/8.
- The origin singularity is retained. Q has radial mass one at t=0. For evolved Q_t, substitution r=exp(2u) and evenness give M_t=16H(t,i). The separate identity integral sQ_t=integral s^2Q_t follows from weight-five inversion, not an ordinary probability-measure symmetry.
- Differentiating the explicit potential yields r^2 T'_t=-integral_r^infinity s^2Q_t and Delta T_t=Q_t. Its specified tail removes both radial harmonic ambiguities. The coefficients M_t at infinity and M_t/r at zero match Kelvin symmetry, and the distributional contact term is -4 pi M_t delta_0.
- The time-adapted primitive has derivative -M_t/2 at u=0, giving J_t=8(H(t,i)-H(t,z))/(1+z^2). It differs from the earlier exp(tu^2)psi primitive. Its real-axis positivity is generic and supplies no sign for H.
- The half-line source g_t=4exp(tx^2/4)Phi(x/2), x=2u, gives B=-8H. For lambda=a^2/4 and a>0, B_lambda=-16H_a/a. Multiplicity is preserved under this local coordinate change.
- The Volterra solution satisfies Y_xx+lambda Y=g_t. Parameter differentiation keeps g_t fixed. The Wronskian derivative is -Y^2-g_tY_lambda, giving the sign and both boundary terms in Note01 (18). Super-exponential tails justify the outer limit and all stated differentiations.
- The closed spatial system retains its forcing channel. The third-order homogenization is not the scalar self-adjoint second-order eigenproblem. The response time identity was checked by applying partial_x^2+lambda to each term; at x=0 it yields B_t=-lambda B_lambdalambda-B_lambda/2, matching H_t=-H_aa.
- The Gaussian control uses a fixed source while differentiating lambda. Its response is positive, but Y_lambda=-exp(-x^2), so the forcing pairing exactly cancels the positive norm. Its local heat embedding has the explicitly stated finite time domain and is not a canonical global-threshold example.

## Exact replay

The [checker][checker] ran successfully and wrote [the record][record]. It uses exact rational polynomial differentiation and Gaussian even-moment ratios. It confirms the source polynomial 16x^4+24, response polynomial 4x^2+4, the differentiated forced equation, both zero boundary derivatives, and the coefficients +27 and -27 multiplying I0=sqrt(pi)/(2sqrt(2)). No floating-point maximum, theta integral, interval certificate or all-height inference is involved.

The replay is narrower than the proofs above. It does not independently validate the infinite source manipulations, the whole operator framework or the proposed research program.

## Claim classification and remaining risks

The radial dictionary, potential and exact boundary dynamics are faithful diagnostics. The generic forcing control is a proved in-note scoped obstruction: positivity of the forcing and response cannot remove the extra term in this realization. The existence of a useful theta-specific current, a homogeneous characteristic realization, or a source-derived zero boundary degree remains open. No global no-go conclusion is drawn from the control.

All-multiplicity collision theory and the canonical finite-event reduction are inherited at their source scope. The new note provides a derivative hierarchy, not an all-multiplicity exclusion theorem. Bounds on an arbitrary finite pilot would not establish every positive threshold or endpoint simplicity.

The next review should challenge any proposed closure where the source amplitude, boundary term, parameter dependence or residual is suppressed. It should also check that a claimed theta distinction actually uses a premise absent from the relevant colliding controls. The [progress register][progress] retains RTC-03 and RTC-05 as ready research tasks, not completed mechanisms.

[note]: ../notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[checker]: ../numerics/01_check_forced_wronskian_control_20261027.py
[record]: ../numerics/01_FORCED_WRONSKIAN_CONTROL_CHECKS_20261027.json
[progress]: ../research-progress/01_RADIAL_THETA_COLLISION_RESEARCH_PROGRESS_20261027.md
