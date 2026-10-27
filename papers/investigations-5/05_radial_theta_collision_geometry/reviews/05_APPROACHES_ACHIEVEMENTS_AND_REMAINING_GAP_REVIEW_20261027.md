# Review of radial theta collision approaches and remaining gaps

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Research conversation: **Review radial theta collision work**, Investigation05 chat0002, thread 01a17ee9-ed08-7271-9f66-04ac5ee516b8.

**Assessment:** the investigation has established useful exact representations and specific reasons several proposed collision arguments fail. It has not obtained a canonical collision exclusion, a newly covered physical region, an improved Newman bound, or endpoint simplicity. The principal remaining difficulty is transferring information about the complete theta source into a signed statement about its oscillatory physical observation.

This is a fresh-session internal review using the same model as the original derivations. It is not independent specialist or cross-model review. The reviewed scope is the overview, progress register, Notes01–05, Reviews01–04, their exact records, and selected primary-source formulas.

## What each approach achieved

| Approach | Intended collision mechanism | Established outcome | Remaining gap or scoped stop |
| --- | --- | --- | --- |
| Radial and Kelvin geometry, Note01 | Use the source's geometric structure to obtain a boundary or oscillation theorem | Exact three-dimensional radial dictionary, time-dependent potential, origin charge and physical observation | Positivity and inversion do not determine the sign or multiplicity of the Mellin/cosine transform |
| Forced boundary equation, Note01 | Make physical zeros characteristic zeros and invoke spectral simplicity | Exact B=-8H, complete Wronskian identity, compatible response evolution and multiplicity hierarchy | The equation remains forced; an explicit positive source and positive response have a double boundary zero |
| Circle heat lift, Note03 | Retain square arithmetic through a transverse heat equation and transfer its structure to the response | Complete two-channel circle system, exact nonzero commutator and boundary residual, finite linear transverse obstruction | A physical zero is a zero at one circle point, not a homogeneous condition on the whole circle |
| Gaussian deformation, Note04 | Deform to a positive transform and transport zero degree backward | Exact heat symmetry, finite positive anchor, all-multiplicity transport and complete event trajectories | Collisions exit through boundary faces; the limiting global cap is singular |
| Modular Wronskian weight, Note05 | Use theta's nonlinear modular equations to give the current a favorable sign | Finite nonlinear source description, invariant complete integral, rational endpoint bound and actual canonical integrand sign change | The proposed pointwise positivity is false in the eventual large-frequency regime; signed comparisons remain unproved |

The [overview](../research-overview/01_RADIAL_THETA_COLLISION_RESEARCH_OVERVIEW_20261027.md) and [progress register](../research-progress/01_RADIAL_THETA_COLLISION_RESEARCH_PROGRESS_20261027.md) correctly preserve these distinctions. The older task table in Note02 is explicitly historical and superseded by its continuation update.

## The radial construction fixes the objects but does not supply an eigenvalue problem

[Note01](../notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md) identifies the natural radius as r=exp(2u), with

\[
\Phi(u)=\tfrac14r^{5/2}\Delta_3\Theta(r).
\]

The dimension three is selected by the source's Gaussian differential coefficients. The integer-square sum itself remains one-dimensional; replacing it with a three-dimensional lattice would change the problem. The evolved source has an explicit Kelvin-symmetric potential whose constant at infinity and charge at the origin both equal M_t=16H(t,i). Retaining these terms prevents a false conservation or boundary cancellation argument.

The physical source evolves by multiplication by exp(t log²r/4), rather than radial diffusion. H is a spectral coefficient of a fixed half-line operator, so simplicity of that operator's spectrum does not imply simplicity of the zeros of H. The positive primitive is similarly an auxiliary observation with a generic positivity property; it supplies no sign for H.

These are reusable structural results. Their present value is a precise dictionary and a correct account of the generator and boundaries. Basic Kelvin covariance is shared by suitably decaying even controls, so that covariance alone does not isolate the canonical arithmetic.

## The forced Wronskian reveals the decisive cancellation

The exact boundary construction is

\[
Y_{xx}+\lambda Y=g_t,\qquad B=Y_x(0)=-8H(t,2\sqrt\lambda),
\]

\[
Y(0)B_\lambda-BY_\lambda(0)
=\underbrace{\int_0^\infty Y^2dx}_{N}
+\underbrace{\int_0^\infty g_tY_\lambda dx}_{C}.
\]

At a double event, B=B_lambda=0 and therefore C=-N. The extra pairing C is precisely what prevents importing the usual homogeneous Sturm simplicity argument.

The control is unusually informative because it defeats an apparently stronger premise as well: both g_*=(16x⁴+24)exp(-x²) and Y_*=(4x²+4)exp(-x²) are positive, yet Y_lambda=-exp(-x²) at lambda=6, and N=27I0, C=-27I0. Thus positivity of the response as well as the source leaves exact cancellation possible.

This control lacks theta's complete arithmetic and tails. It closes the generic positivity argument for this forced realization, not every theta-specific relation or every spectral construction. Writing C>-N without independently proving it from additional source information would simply state the desired contradiction. The exact third-order spatial homogenization also remains generic and does not become a self-adjoint second-order eigenproblem.

## The circle construction preserves arithmetic but changes the observation

[Note03](../notes/03_CIRCLE_HEAT_LIFT_AND_BOUNDARY_TRANSFER_OBSTRUCTION_20261027.md) successfully retains every square mode. Its two channels are functions of a circle variable; they are not two scalar states. The proof excluding finite invariant linear transverse spaces is sound in its stated class: an annihilating polynomial would have to vanish at infinitely many distinct circle eigenvalues.

The important failure occurs when this source system is passed through the Volterra response. The resulting commutator is nonzero for the canonical response. Its observed residual and lower-end terms cannot be removed by the physical event conditions.

Moreover, the lifted boundary function beta is never identically zero as a circle function, although its physical value beta(0)=B can vanish. Averaging over the circle discards cross-mode terms that the physical evaluation retains. Consequently an averaged positive quantity is not automatically an event-vanishing quantity. The full modular transform also sends the real auxiliary argument to an imaginary one, as in [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32); it does not preserve the same real-circle positivity problem.

The obstruction leaves nonlinear theta identities, scalar restrictions, and nonlocal estimates open. Note05 demonstrates why that qualification matters: a finite nonlinear source system does exist. What remains unavailable is a useful closed system or inequality for the physical spectral response.

## Gaussian relaxation moves the events rather than excluding them

The useful achievement in [Note04](../notes/04_GAUSSIAN_SOURCE_DEFORMATION_AND_COLLISION_INDEX_TRANSPORT_20261027.md) is its exact observation formula:

\[
F_\rho(t,a)=W\,H\!\left(
\frac{\rho^2t}{\Delta},\frac{\rho a}{\Delta}\right),
\qquad
\Delta=1-(1-\rho^2)t,\quad W>0.
\]

For rho>0, the coordinate map preserves orientation and the physical jet changes by a positive-diagonal triangular matrix. Thus multiplicities and negative local collision indices survive. The endpoint is positive on a fixed finite rectangle because the corresponding original region contracts toward the known positive point (0,0).

The positive endpoint is real progress in understanding the deformation, but it is compatible with original collisions leaving the rectangle. The explicit control changes degree from -1 to 0 through the upper time face at rho²=5/9 while both frequency walls remain positive. On the full open slab, hypothetical events approach (1,0), where the endpoint Gaussian transform is singular. Following the event with moving side walls retains the temporal obstruction.

This is the strongest reason to stop this particular homotopy inference: it is already an exact symmetry of the physical heat equation and preserves the events one hoped to eliminate. A different deformation could be investigated, but its existence is presently a research option, not a developed construction or acquired boundary estimate.

## The modular return is a canonical obstruction

[Note05](../notes/05_MODULAR_WRONSKIAN_WEIGHT_AND_CANONICAL_SIGN_OBSTRUCTION_20261027.md) uses the classical finite nonlinear equations for theta constants, with the canonical initial data retained. The underlying differential identities and E2 normalization agree with [Brezhnev, Lyakhovich and Sharapov, equations 6 and 8](https://arxiv.org/pdf/1012.1429v4). These describe source-coordinate evolution, not physical heat or a finite closure of spectral jets.

For the proposed normalized scalar weight w, the complete integrand is

\[
\mathscr I_w=wY^2+wg_tY_\lambda-w_x
(YY_{\lambda x}-Y_xY_\lambda)
=-\partial_x(wW_{\!Y}).
\]

Here W_Y denotes the response Wronskian, to distinguish it from the Gaussian prefactor above. Since w(0)=1, the integrated current remains exactly the original boundary residual. The derivative of the weight is essential. The square-root conjugation retains forcing and restores the same Green form with its natural integrating factor.

Integral invariance alone would not show that weighting is useless: a different presentation can make an estimate easier. The stronger result is that the actual canonical integrand takes both signs for all sufficiently large lambda, uniformly for 0<=t<=1/2. Its endpoint coefficient satisfies

\[
g_t''(0)^2-g_t(0)g_t^{(4)}(0)
\le-\tfrac{5936}{5}K_*^2<0,
\]

while the leading coefficient integrates to zero and must be positive somewhere else. This rules out unconditional pointwise positivity for the displayed integrand. It leaves signed integration, restricted domains, and arguments using extra event information open. No numerical onset or collision exclusion follows.

## Why additional local asymptotic orders are not yet a sign estimate

An interpretive consequence of the existing source assumptions sharpens the scale issue. For g=g_t even and with all derivatives integrable, repeated integration by parts gives, for every integer j>=0 and lambda>=1,

\[
|B(t,\lambda)|\le\lambda^{-j}\|g^{(2j)}\|_1,\qquad
|B_\lambda(t,\lambda)|
\le\tfrac12\lambda^{-j-1/2}\|(xg)^{(2j)}\|_1.
\]

All endpoint terms vanish by parity. The bounds are uniform in compact real time intervals. The Volterra bounds for Y(0) and Y_lambda(0) then show that the complete boundary residual decays faster than every inverse power of lambda.

This explains why a local integrand can have a nonzero lambda^(-4) term while its integrated leading term cancels. A finite algebraic expansion, by itself, does not determine the much smaller signed residual. This observation does not preclude a controlled signed remainder, exponentially accurate analysis, or a different current; it explains why merely adding more local orders is not yet the missing physical estimate.

## Research judgment and next discussion

The largest gains are the explicit forcing cancellation, the canonical circle boundary mismatch, the complete Gaussian crossing mechanism, and the actual canonical sign obstruction. They eliminate specific tempting shortcuts while retaining exact tools that another argument could use.

The shared unresolved step is source-to-observation control. Identifying theta through complete arithmetic, reflection, or a finite nonlinear trajectory does not itself bound the signed response. This distinction follows the [result index](../../../../result-summaries/README.md), particularly the [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md) and [local index results](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), and the [avoid index](../../../../avoid/README.md), especially [target restatements](../../../../avoid/01_restating_the_target.md), [coordinate lifts](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

A continuation should identify one concrete current, signed comparison, or boundary construction and explain the additional information it provides before expanding the machinery. Its first deliverable should be a stated domain and an independently established restriction on the response or complete boundary, with the relevant colliding controls screened against the premises actually used. For a finite computational comparison, the target quantity and direct comparator should be fixed first.

The current RTC statuses are appropriate: RTC-01 and RTC-02 are complete within their diagnostic scope; the broader RTC-03 and RTC-05 questions remain open after specific failed constructions; RTC-04 lacks a characteristic candidate; RTC-06 is reasonably deferred; RTC-07 has transport without exclusion. No status upgrade follows from this review.

## Verification record

All four existing exact-algebra programs were copied unchanged to a temporary directory and replayed successfully. Each regenerated JSON record was byte-identical to its saved counterpart. The [replay receipt](../numerics/05_REVIEW_REPLAY_RECORD_20261027.json) records source hashes, outputs and comparisons. The original programs and records were not overwritten.

The review also checked the central Wronskian signs, Gaussian coordinate and jet transformations, scope of the transverse polynomial obstruction, and the endpoint/asymptotic mechanism in Note05. Selected primary checks covered the [theta heat normalization](https://dlmf.nist.gov/20.13), [modular inversion](https://dlmf.nist.gov/20.7.E32), and the nonlinear source equations cited above. These support the stated scoped results; finite replay does not independently certify convergence arguments, inherited index theorems, or a physical theta sign.
