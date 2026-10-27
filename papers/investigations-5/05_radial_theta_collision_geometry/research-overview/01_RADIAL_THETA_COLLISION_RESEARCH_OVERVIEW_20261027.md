# Radial theta collision research overview

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

**Current continuation:** [Note13](../notes/13_RADIAL_LAPLACIAN_CONTINUATION_20261027.md) returns to the standard three-dimensional radial Laplacian with the original one-dimensional theta sum. This supersedes the earlier priority of constructing a higher-rank lattice kernel. The next work reviews and develops radial source, flux, potential and observation identities, with all boundaries and physical time dependence retained. This is a planning update; the seven recorded RTC-03 returns retain their status.


The [spatial-sphere and spectral-mode return](../notes/07_SPATIAL_SPHERES_LOGARITHMIC_MODES_AND_PERIODIC_LATTICES_20261027.md) distinguishes the original radius r from the auxiliary radius |u|. It reconnects H to the earlier exact spherical Fourier representation, expresses z as a logarithmic radial mode in the original geometry, and proves that no fixed periodic field has nonzero integrable spherical mean. This excludes exact global spherical-mean recovery of A or Q from that periodic class; nonperiodic lattice constructions remain open. No collision-excluding estimate is obtained.

The [changed three-dimensional lattice definitions](../notes/08_GENUINE_THREE_DIMENSIONAL_LATTICE_SUMS_AND_THETA_RECOVERY_20261027.md) answer the clarified request to begin with different underlying sums. A Euclidean cubic-coset sum uses a parity sign and spherical averaging to recover the odd theta sector, then the complete primitive by an exact two-scale identity. A second positive sum over every point of Z^3 recovers Theta directly using the maximum-coordinate norm and a rational resolvent weight. These are exact source constructions with stated tradeoffs; no physical collision estimate is obtained.

The [flat Dirac continuation](../notes/12_FLAT_QUATERNION_DIRAC_AND_DYADIC_LATTICE_H_20261027.md) adds a single weighted cubic-lattice exponential field with actual r=|X|, both parameters inside the summand, and complete spatial H recovery. It retains dyadic parity and completion costs; quaternion noncommutativity and first-order Fueter evolution provide no established advantage. This seventh bounded RTC-03 return has a [same-assistant review](../reviews/07_FLAT_DIRAC_DYADIC_LATTICE_SELF_REVIEW_20261027.md) and [finite exact/floating record](../numerics/10_FLAT_DIRAC_DYADIC_LATTICE_CHECKS_20261027.json); the whole-formula simplicity objective remains open.

The [earlier complete observation](../notes/10_COMPLETE_THREE_DIMENSIONAL_GAUSSIAN_OBSERVATION_20261027.md) now meets both dimensional requirements: a native additive rank-three coset and a three-dimensional full-H integral with explicit all-time convergence. The [quaternionic comparison](../notes/11_HURWITZ_HOPF_AND_UNIT_QUATERNION_HEAT_REPRESENTATIONS_20261027.md) provides a full-time Hopf/Möbius construction and a simpler local unit-sphere operator, retaining their extra dimension or arithmetic costs. [Review06](../reviews/06_COMPLETE_OBSERVATION_AND_QUATERNION_SELF_REVIEW_20261027.md) is same-assistant.

## Purpose and intended outcomes

The immediate objective is to develop the useful standard-operator simplification Phi=(1/2)r^(5/2)Delta_3 A, keeping the original square arithmetic. The [current continuation program](../notes/13_RADIAL_LAPLACIAN_CONTINUATION_20261027.md) begins with the established radial, Kelvin and flux identities and asks what they simplify in the complete H observation. A higher-rank discrete lattice is no longer a design requirement. A clearer source representation is an admissible research outcome before it supplies a collision estimate. The longer-term structural question remains whether the resulting system supports a useful collision argument or signed estimate. This work does not take over the live approximation, Dobner, response or collision-energy tasks in sibling investigations.

The [initial note][initial] proves the radial/Kelvin dictionary, constructs a time-dependent potential with fixed boundary convention, and realizes H as the boundary derivative of an inhomogeneous differential equation. Its exact Wronskian identity exposes a forcing term that cancels the positive norm at a collision. A positive source and positive response control realize that cancellation. The RTC-03 question is whether the complete theta equations supply additional information that changes this implication.

The first bounded continuation, [Note03][circle], derives a full circle heat system and a precise obstruction to transferring it into a homogeneous physical boundary problem. Its response commutator is nonzero, finite invariant transverse linear closure fails, and a physical zero does not make the circle boundary function vanish. The source system alone is also shared by weighted-square controls. This closes only the selected transfer attempt; broader RTC-03 remains open.

The first RTC-05 return, [Note04][gaussian], tests positive Gaussian relaxation of the complete source. It proves an exact physical degree transport, a finite positive anchor and event orbits with every face and limiting cap retained. A positive-source control changes degree through the upper time face while the frequency walls remain positive. This closes only the inference from a positive Gaussian endpoint to zero original degree; the canonical global constraint remains open.

The second RTC-03 return, [Note05][modular], implements the proposed modular multiplier through a finite nonlinear theta system. Its complete weighted integral equals the original boundary residual, and its actual canonical integrand takes both signs at sufficiently large positive frequency, uniformly for 0<=t<=1/2. Exact rational source bounds prove the endpoint sign. This closes the selected unconditional pointwise positivity attempt while leaving signed cancellation and other currents open.

Possible outcomes are a useful theta-specific boundary/transfer relation, a new collision obstruction on a declared time-height domain, a global index constraint, an improved complete signed estimate, or a precise failure of a specified construction. A new RH formulation or another faithful coordinate lift alone is not an exclusion gain. The global homogeneous spectral realization remains an aspirational sufficient mechanism; no equivalence of that realization with RH is asserted.

Read the [result index][results], [local collision geometry][geometry], [theta arithmetic][arithmetic], [geometric realizations][lifts] and [control register][controls], with the [avoid index][avoid]. The especially relevant patterns are [target restatements][a01], [shape-only controls][a02], [coordinate lifts][a03], [scoped exclusions][a07], [coupled terms][a12], and [circular definitions][a14].

The user-requested [rank-three lattice test](../notes/06_RANK_THREE_LATTICE_REALIZATION_AND_PROJECTION_20261027.md) now distinguishes full-lattice equality from geometric recovery. A direct full-rank positive Gaussian trace cannot reproduce the exact profile; transverse averaging of the cubic torus kernel does recover it, and Z x 3Z x 3Z gives relative profile error below 9e-11 on r>=1. Neither the marginal nor this approximation provides an acquired physical sign or a characteristic operator. The source and observation must be specified separately in any continuation.

## Exact working objects and domains

Use H(t,z)=integral_0^infinity exp(tu^2)Phi(u)cos(zu)du and H_t=-H_zz, with the unchanged integer-square source from Note01. The three coordinates have distinct roles:

| Variable | Role |
| --- | --- |
| u | Original source coordinate |
| r=exp(2u) | Euclidean source radius for the Laplacian and Kelvin transformation |
| x=log(r)=2u | Logarithmic coordinate for the half-line boundary equation |
| a or z | Physical observation variable; a is real |
| lambda=a^2/4 | Spectral parameter for the forced half-line equation, locally nonsingular for a>0 |
| T,t | Candidate event time and genuine physical heat time |
| tau=t-T | Time relative to an event; it does not remove T from the source |
| m | Arbitrary finite spatial multiplicity; not restricted to two in an eventual exclusion theorem |

The exact baseline is

\[
Q=\Delta_3\Theta,\quad \Phi=\tfrac14r^{5/2}Q,\quad
Q_t=e^{(t/4)\log^2r}Q,\quad Q_t(r)=r^{-5}Q_t(1/r),
\]

\[
M_t=16H(t,i),\quad
\mathcal T_t(r)=M_t+\int_r^\infty(s^2/r-s)Q_t(s)ds,
\]

\[
g_t(x)=4e^{tx^2/4}\Phi(x/2),\quad
Y_{xx}+\lambda Y=g_t,\quad
Y,Y_x\longrightarrow0\text{ at infinity},\quad
B(t,\lambda)=Y_x(t,0;\lambda)=-8H(t,2\sqrt\lambda).
\]

The decay condition means the explicit Volterra solution in Note01, including its parameter derivatives. There is no boundary eigenfunction normalization hidden in Y. The collision equations are B=B_lambda=0 for a double event at a>0. At multiplicity m, B has the same multiplicity in lambda, with the forced derivative hierarchy from Note01.

Begin analytically with real t in a compact positive interval [b,B], 0<b<B, and a>0. These are parameters, not claimed covered regions. If a finite pilot is later needed, state its domain and purpose before evaluating it. Excluding a positive threshold requires all possible heights and multiplicities at that threshold, or an explicit reduction. Endpoint simplicity at t=0 is a separate stronger endpoint question. No all-height uniformity, zero-endpoint limit, or positive source lower bound for H is assumed.

## Longer-term mechanisms after source simplification

### Source-derived boundary and oscillation mechanism

The ordinary radial Sturm operator is unitarily the Neumann half-line operator -partial_x^2+1/4. H is its source spectral coefficient. Its eigenvalue simplicity does not constrain the zeros of that coefficient.

The forced realization is more informative: its complete boundary identity is

\[
Y(0)B_\lambda-BY_\lambda(0)
 =N_t(\lambda)+C_t(\lambda),\quad
N_t=\int Y^2dx,\quad C_t=\int g_tY_\lambda dx.
\]

At a double event C_t=-N_t. Both sides are already determined by the boundary residual; this identity is not an independent exclusion inequality. Note01 also gives the exact three-component spatial transfer system with q_t=partial_x log g_t and the compatible response evolution Y_t=x^2Y/4+x partial_x Y_lambda-3Y_lambda/2-lambda Y_lambdalambda. These generic closures retain the source channel. The structural question is whether canonical theta mode equations and full reflection yield an additional collision-relevant relation, a useful current, or a constraint on the forcing term. Keep the full coupled expression before majorization.

A successful homogeneous realization would need independently specified real coefficients, positive weight, a declared operator domain and boundary conditions, and an exact physical observation map. Any spectral dependence of the coefficients or boundaries adds derivative terms to the Wronskian identity. Defining an operator using the unknown physical zeros, assuming a positive first-jet floor, or suppressing a forcing channel would not meet this requirement.

### Global continuation and collision index mechanism

The inherited physical local index is negative for every event. Thus a zero global boundary degree could rule out all events in a region. Explore whether the canonical radial source supplies a continuation or current that constrains this boundary degree independently of assuming the desired interior nonvanishing.

Keep the physical (t,a) map, all boundary faces, wall tangencies, moving-domain derivatives, and the source's actual evolution. Kelvin symmetry by itself only restates reflection and does not cancel the equal indices at a and -a. A finite-box boundary argument should identify its information advantage over the already available direct first-jet or winding tests; an exact re-expression alone is insufficient.

### Coupled radial estimates where a consumer exists

If either structural route supplies a useful current or residual, examine complete signed Green estimates on inversion-paired annuli. Reuse the earlier Hodge, trace and inverse-marginal tools with their actual measures and generators. Compare against the one-dimensional consumer on the same domain. This route remains available but does not define the whole program.

## Tasks and dependencies

The [progress register][progress] is authoritative for these IDs and their status.

| ID | Task and deliverable | Dependency and decision |
| --- | --- | --- |
| RTC-01 | Exact radial/Kelvin dictionary, evolved potential, origin charge and physical readout | Complete in Note01 within its stated scope; maintain normalization |
| RTC-02 | Forced boundary equation, complete Wronskian current, and explicit generic cancellation control | Complete in Note01 for this realization; it identifies the remaining forcing term |
| RTC-03 | Native higher-dimensional representation and source structure | Notes10–11 provide a complete three-dimensional H baseline and quaternionic alternatives; reduce their remaining channel, scale or arithmetic-inversion costs. Note09 retains the abstract objective and earlier scoped results remain in Notes03 and05–08 |
| RTC-04 | Characteristic or nodal realization with a collision implication | Follow RTC-03 only if it gives a concrete candidate; specify coefficients, domains and every boundary derivative |
| RTC-05 | Source-derived global continuation or collision-index constraint | First Gaussian-deformation return complete in Note04 as exact transport and a scoped obstruction; a distinct construction or new canonical boundary information is still needed |
| RTC-06 | Improved correlated Green or trace estimate for an identified consumer | Defer numerical acquisition and optimization until a consumer/domain is fixed |
| RTC-07 | Multiplicity, threshold and parameter-range transfer | Exact derivative hierarchy and arbitrary-multiplicity Gaussian transport are available; no exclusion or threshold transfer follows yet |
| RTC-08 | Mathematical assessment, controls, provenance and integration | Continue with each return; initial checking is same-assistant only |

The earlier circle lift, Gaussian deformation and modular multiplier retain their scoped results. The current RTC-03 task may first deliver a materially simpler native representation of H; an immediate collision estimate is not a prerequisite for this requested exploration. Any later exclusion claim still needs independent signed information and the registered controls. These are research task states, not separate chat dispatches or scheduled jobs.

## Current RTC-03 continuation contract

Use [Note10](../notes/10_COMPLETE_THREE_DIMENSIONAL_GAUSSIAN_OBSERVATION_20261027.md) as the completed three-dimensional baseline and [Note11](../notes/11_HURWITZ_HOPF_AND_UNIT_QUATERNION_HEAT_REPRESENTATIONS_20261027.md) as the quaternionic comparison, under the objective of [Note09](../notes/09_SIMPLER_HIGHER_DIMENSIONAL_H_REPRESENTATION_CONTINUATION_20261027.md). A new candidate should remove a specified remaining operation, such as the Hopf divisor inverse or the separate sphere/scale integral, and be compared in full with these formulas. State the meaning of every radius and time, the z observation, and all recovery and boundary terms. It is permissible to change the intermediate target or symmetry when that simplifies the complete system. The earlier collision-focused contract below is retained as historical completed work.

## First bounded continuation contract — returned for the selected circle lift

1. Take Note01's exact g_t, Y, B, N_t and C_t. Keep t and lambda symbolic in a stated domain. Reconcile the normalizations before adding another state variable.
2. Apply the Gaussian mode equations (partial_r+2 pi n^2 r)exp(-pi n^2r^2)=0 to the prescribed theta source combination. Track the time multiplier, lattice summation, endpoint terms at r=1, and both inversion-related tails. If an auxiliary theta or bundle variable is used, give its exact physical restriction and all commutators.
3. Determine whether the resulting relation adds information beyond the generic three-component closure and its time compatibility, without using already evaluated H or its unknown zeros as defining data. If it leaves a forcing residual, display that residual and its whole observation cost. A fixed finite derivative list does not imply closure.
4. Apply the explicit Gaussian-polynomial control and the relevant registered controls. Identify the actual canonical premise each would fail. A calculation using only positivity, evenness, Kelvin covariance and the generic forced ODE must remain compatible with the control.
5. Return either a usable new relation with its collision implication and range, a concrete smaller unpaid arithmetic problem with a genuine information gain, or a scoped closure obstruction. Do not label the original boundary identity or an RH-equivalent target as that gain.

The work should remain analytical unless a specific finite computation resolves a stated uncertainty. Do not restart the old bounded energy correction or a broad theta sampling campaign by default.

## Completed bounded returns and next contract

[Note03][circle] meets the obstruction option of the preceding contract: it keeps the full square population, time multiplier, Jacobi argument transformation, both inversion tails, response commutator, physical first-jet residual and endpoint terms. Its [self-assessment][circle-review] and [exact record][circle-record] separate finite algebra from analytical proofs. The result is not an RH-equivalent criterion or a physical sign gain.

[Note04][gaussian] supplies the first RTC-05 return on 0<b<c<1/2 and finite frequency width: its Gaussian deformation is an exact heat symmetry, its event trajectories preserve every finite multiplicity, and its positive endpoint is separated from the initial field by explicit collision crossings. Its [self-assessment][gaussian-review] and [exact record][gaussian-record] include a control with both frequency walls positive and a nonzero upper-time crossing. This is no canonical sign gain.

[Note05][modular] completes the next RTC-03 multiplier test. It preserves the complete physical source and weight derivative, derives the finite nonlinear source equations, and proves an actual canonical sign obstruction with a rational endpoint bound. Its [self-assessment][modular-review] and [record][modular-record] retain the distinction between exact algebra and the analytical asymptotic proof. Future signed estimates must account for this cancellation; unconditional positivity of the selected integrand is unavailable on the whole stated regime.

For another RTC-05 construction, first declare a physical time-frequency region and one distinct source-derived current or deformation. Retain both time faces, both frequency walls, and every boundary crossing or tangency. Seek a constraint on the complete degree that is established from source information independently of the desired interior nonvanishing; alternatively prove the chosen construction's exact failure. Merely substituting a circle norm or Kelvin identity for the physical boundary data does not satisfy the contract. A formal identity alone does not justify a numerical campaign or all-height extrapolation.

## Validation and maintenance

Every nontrivial assertion keeps a written proof, inherited source link, or explicit conjectural status. The exact control checker verifies polynomial identities and the rational coefficients +27 and -27 multiplying the same Gaussian integral; it does not verify the whole analysis or evaluate theta. A subsequent independent review should check the potential boundary convention, all factors in B=-8H, the Wronskian sign, the forcing derivative, and the scope of any collision implication.

Save derivations in notes/, analytical assessments in reviews/, and any justified computations in numerics/. Update the progress register after each result, including a losing comparison. Keep primary-source records in references/ and large external material outside Git. The founding chat keeps its unique registration in Investigation04; future chats primarily about this program register in this investigation. No manuscript snapshots are created.

[initial]: ../notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[progress]: ../research-progress/01_RADIAL_THETA_COLLISION_RESEARCH_PROGRESS_20261027.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[arithmetic]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[lifts]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a14]: ../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md

[circle]: ../notes/03_CIRCLE_HEAT_LIFT_AND_BOUNDARY_TRANSFER_OBSTRUCTION_20261027.md
[circle-review]: ../reviews/02_CIRCLE_HEAT_LIFT_SELF_ASSESSMENT_20261027.md
[circle-record]: ../numerics/02_CIRCLE_HEAT_LIFT_CHECKS_20261027.json

[gaussian]: ../notes/04_GAUSSIAN_SOURCE_DEFORMATION_AND_COLLISION_INDEX_TRANSPORT_20261027.md
[gaussian-review]: ../reviews/03_GAUSSIAN_DEFORMATION_AND_INDEX_SELF_ASSESSMENT_20261027.md
[gaussian-record]: ../numerics/03_GAUSSIAN_INDEX_TRANSPORT_CHECKS_20261027.json

[modular]: ../notes/05_MODULAR_WRONSKIAN_WEIGHT_AND_CANONICAL_SIGN_OBSTRUCTION_20261027.md
[modular-review]: ../reviews/04_MODULAR_WRONSKIAN_SELF_ASSESSMENT_20261027.md
[modular-record]: ../numerics/04_MODULAR_WRONSKIAN_CHECKS_20261027.json
