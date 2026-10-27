# Continuation: a simpler higher-dimensional representation of H(t,z)

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Research conversation: **Review radial theta collision work**, Investigation05 chat0002, thread 01a17ee9-ed08-7271-9f66-04ac5ee516b8.

**Current priority superseded, 27 October 2026, chat0003.** Start with [Note13](13_RADIAL_LAPLACIAN_CONTINUATION_20261027.md). Edward Baker has chosen to retain the useful three-dimensional radial Laplacian while keeping the original one-dimensional theta sum. The rank-three lattice preference in the brief below is historical; the earlier identities and scope statements are retained.

**Current continuation brief.** Find a higher-dimensional system in which the complete function H(t,z) has a simpler native description. The preferred starting point is a function defined by a three-dimensional lattice sum and an observation expressed as a three-dimensional integral. Aim for a maximally simple summand and a simple complete observation, allowing the intermediate objects and geometry to change.

This note organizes the research program requested by Edward Baker. It supersedes the immediate research priorities in the earlier handoff, while retaining their proved identities and scoped obstructions. It does not announce another completed construction or select Note08's examples as final models.

**27 October, chat0003 clarification.** The preferred next direction uses the standard flat quaternion operator D=sum e_i partial_i, t as the real paravector coordinate, an exponential summand on the imaginary-unit lattice, and r=exp(2u) as an actual spatial radius, with z inside the summand. [Note12](12_FLAT_QUATERNION_DIRAC_AND_DYADIC_LATTICE_H_20261027.md) supplies one complete construction under that brief, retaining a dyadic parity rule. The remaining target is to explain or remove that rule or obtain a useful first-order completion; writing t+X alone does not establish Fueter regularity.

## 1. The objective, before choosing a representation

The question is whether the polynomial weights, logarithmic substitutions, completion factors and oscillatory observation in the usual formula are consequences of reducing a simpler higher-dimensional object.

A useful outcome would start with an independently specified lattice, kernel, geometry and evolution, then derive the canonical H. It could make the underlying equation easier to understand, replace a complicated summand by a standard heat or Green kernel, explain a normalization geometrically, or provide a more manageable object for later analysis.

The immediate objective is **representational simplification**. Exploration is worthwhile before it supplies a collision estimate. The eventual interest in zeros remains, but it should not force every candidate prematurely into a positivity or eigenvalue-simplicity argument. An exact reformulation is not itself a new RH result; a materially simpler full representation can still be a legitimate research deliverable.

There are three separate goals:

1. **A native higher-dimensional sum.** Begin with lattice labels n in a rank-three lattice or a clearly specified family of cosets. The summand should be defined without importing Phi, H, their zeros, or a fitted table of their coefficients.
2. **A native higher-dimensional observation.** Recover H through an integral over a three-dimensional space or manifold, with its measure, domain and boundary terms explicit. Merely making the lattice sum three-dimensional does not accomplish this.
3. **A simpler complete formula.** Judge the kernel, measure, observation, evolution and recovery together. Removing a polynomial from the summand by hiding it in a difficult observation may be useful, but the cost must be visible.

Three dimensions are the preferred experimental setting, motivated by the existing radial identities and the new lattice constructions. They are not an immutable axiom. A different dimension or geometry is worth considering if it produces a substantially simpler complete system; the change must be stated.

## 2. What remains fixed, and what may change

The canonical target is

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad \partial_tH=-\partial_z^2H.
\tag{1}
\]

For orientation, the present intermediate objects are

\[
A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\quad
\Theta=1+2A,\quad
\psi(u)=e^uA(e^{2u}),\quad
\Phi=\tfrac18(\partial_u^2-1)\psi.
\tag{2}
\]

These intermediates are useful reference points, not mandatory stages in the new construction. It may be simpler to recover H directly, or to introduce a different primitive or completed field, rather than reproduce A pointwise and follow exactly the old chain.

In particular, do not require every higher-dimensional shell to match an integer-square term before the final integral. Extra shells might disappear through a geometric observation, a symmetry, or the completion operation. A construction that simplifies the combined sum and integral could be better than one that reproduces A shell by shell.

| Choice | Freedom to explore | What must be retained |
| --- | --- | --- |
| Intermediate target | A, Theta, psi, Phi, a Green potential, a completed primitive, or a new field | An explicit recovery of the complete H |
| Geometry | Euclidean space, a torus with boundary phases, a radial manifold, or a polyhedral norm | Its actual dimension, measure and operator |
| Lattice | Z^3, another rank-three lattice, shifted cosets, or finitely many sectors | A simple independent rule for sites and weights |
| Kernel | Gaussian, wave, Green/resolvent, power kernel, or a small coupled system | Convergence or a specified regularization, and honest total complexity |
| Signs | Positive terms, periodic characters, or signed/complex interference | Cancellation must be controlled before any positivity claim |
| Symmetry | Radial at all times, radial only initially, or anisotropic | The exact symmetry of the observation and evolution |
| Parameters | Cartesian frequency, Mellin frequency, a boundary phase or spectral parameter | The precise map to t,z and the resulting evolution |
| Recovery | Direct equality, a known nonzero factor, or a short differential/integral reconstruction | All constants, inverse data, endpoints and derivative terms |

If a replacement is c(t,z)H with c holomorphic and nonzero on the stated domain, its zeros and multiplicities are preserved there. A primitive, derivative, additive completion or general observation does not automatically preserve them. Such a target is still admissible for this program, but its recovery map must be supplied.

## 3. A useful abstract template for the desired system

Write a native field as

\[
\mathcal F_t(X)=\sum_{n\in\Lambda}a(n)\,k_t(X,n),
\qquad X\in M^3,
\]
\[
H(t,z)=C\int_{M^3}\mathcal F_t(X)\mathcal O_z(X)\,d\mu(X).
\tag{3}
\]

This is a design template, not an established construction. Prefer an elementary or standard kernel k, a simple geometric weight a, and a familiar observation O. A finite number of sectors or a simple completion term can be allowed if the full expression is clearer. They must be included when comparing complexity.

The discrete dimension of Lambda and the continuous dimension of M are distinct requirements. A rank-three sum followed by a one-dimensional Mellin integral meets only the first. A three-dimensional integral of a density reconstructed from Phi meets only the second. Adding two independent normalized Gaussian factors or two unused angles gives no explanatory higher-dimensional structure.

A particularly clean possible target is

\[
\mathcal F_0(X)=\sum_{n\in\Lambda}a(n)k(X,n),\qquad
\boxed{H(t,z)=\frac12\int_{\mathbb R^3}
\mathcal F_0(X)e^{tX_1^2+izX_1}\,dX.}
\tag{4}
\]

Its verification condition is

\[
\int_{\mathbb R^2}\mathcal F_0(u,X_2,X_3)\,dX_2dX_3=\Phi(u).
\tag{5}
\]

Equation (5) is a condition to prove from the proposed lattice kernel, not permission to define that kernel circularly from Phi. Under absolute convergence and the needed moment bounds, Fubini and evenness of Phi prove (4). The time dependence is then the simple multiplication

\[
\mathcal F_t(X)=e^{tX_1^2}\mathcal F_0(X),\qquad
\partial_t\mathcal F_t=X_1^2\mathcal F_t,
\]

and differentiating the plane wave gives the exact backward heat equation for H.

This illustrates a potentially useful change of target: **do not insist that the evolving density remain radial.** Even if the initial field is radial, multiplication by exp(tX_1^2) selects the observation axis. Allowing this may be simpler than continually reconstructing a radial density with a nonlocal time generator. No native rank-three kernel satisfying (5) with the desired simplicity has yet been obtained.

A different natural template uses M^3=R x S^2: logarithmic scale supplies one coordinate and a genuine spherical observation supplies two. This fits the Euclidean lattice construction below. The angular dependence must come from the lattice field; it should not be a spectator factor. A conventional integral on R^3 may be obtainable by changing variables, but its Jacobian is part of the cost.

## 4. What has been tried

The earlier collision work supplies context rather than a fixed architecture for this search. The [founding analysis][initial] gave the radial source and forced boundary problem. The [circle lift][n03] retained a nonzero response commutator; the [Gaussian deformation][n04] transported candidate events rather than eliminating them; the [modular weight][n05] preserved the original boundary residual and had a sign-changing canonical integrand. These are exact dictionaries and scoped failures of particular collision arguments. Forcing terms, boundary contributions and signed cancellations cannot be discarded. They do not rule out a simpler native higher-dimensional source model.

| Attempt | What it accomplishes | What remains unsatisfactory for the present goal |
| --- | --- | --- |
| Radial Poisson/Kelvin representation, [Note01][initial] | Explains why the coefficients in Phi fit the three-dimensional radial Laplacian; gives exact source and Mellin observation | The original lattice index is still one-dimensional |
| Three-torus transverse marginal, [Note06][n06] | Starts with a genuine three-dimensional heat kernel and recovers the rank-one theta kernel exactly | Averaging removes every transverse Fourier mode; the recovered expression has little surviving higher-dimensional structure |
| Stretched lattice approximation, [Note06][n06] | A full-rank integer lattice approximates A on r>=1 with a proved relative profile bound | It changes the source; derivative, completion and H-error transfer have not been supplied |
| Inverse radial marginal, [Note07][n07] and its predecessor | Gives an exact three-dimensional Fourier integral for H, with a proven positive density on the inherited small-time interval | The density is constructed by differentiating Phi; it does not supply a new lattice origin |
| Original-radius logarithmic modes, [Note07][n07] | Places z into an inverse-square radial equation and gives a three-dimensional integral against Q_t | The source is still inherited from the original rank-one sum |
| Euclidean parity/sphere construction, [Note08][n08] | A changed rank-three lattice sum recovers the canonical primitive through exact shell cancellation and scale identities | Signed weights, a selected sphere and two-scale recovery remain; a simple full three-dimensional H integral has not been assembled |
| Positive cube-shell resolvent, [Note08][n08] | A positive sum over every point of Z^3 equals Theta exactly | It changes the norm and introduces a resolvent weight; the H observation and its time dependence still need simplification |

The main gap is now precise: **we have useful three-dimensional sums and useful three-dimensional integrals, but not yet a compelling single system that achieves both with a simpler complete description of H(t,z).**

### The Euclidean starting point to carry forward

Let v=(2a+1,2b,2c), R_v=|v| and define

\[
P(r)=\sum_{a,b,c\in\mathbb Z}
(-1)^c\frac{\sin(\pi R_v/2)}{2R_v}
e^{-\pi r^2R_v^2}.
\tag{6}
\]

The signed shell identity derived from Jacobi's derivative formula gives

\[
P(r)=\sum_{n\ge1,\ n\ {\rm odd}}e^{-\pi r^2n^2},
\qquad
A(r)=2P(r)+r^{-1}P(1/(2r))-\tfrac12.
\tag{7}
\]

The sine-over-distance factor is an ordinary spherical-average kernel. P is the selected spherical mean of a native three-dimensional parity heat field, rather than a density manufactured from Phi. Non-axial lattice points are essential to its coefficients.

Its present observation sphere has fixed radius 1/4, while r^2 is heat time. Combining that sphere with the original scale integral offers a three-dimensional continuous integration space. This is a concrete starting route, not yet evidence that the combined formula is simple.

Possible changes: incorporate the two scales into a single domain by inversion or unfolding; combine parity sectors as one small vector-valued field; move the completion derivatives to the observation; or choose a related lattice/kernel for which the spherical average already produces the desired completed source. Keep the constant -1/2 and every resulting boundary term.

### The positive starting point to carry forward

With M(v)=max(|v_1|,|v_2|,|v_3|),

\[
\mathcal C_\infty(r)=
\sum_{v\in\mathbb Z^3}
\frac{e^{-\pi r^2M(v)^2}}{1+12M(v)^2}
=\Theta(r).
\tag{8}
\]

The equality follows because a cubic shell has 24n^2+2 points. The denominator is a simple resolvent weight that compensates this multiplicity. Equivalently, it arises by an exponential integral of the unweighted maximum-norm heat trace.

Possible changes: realize the weight by a native Green operator, select a geometry with simpler multiplicities, or let the resolvent parameter become one of the continuous coordinates in the final observation. The last option must genuinely simplify the total integration space, not append an uncounted extra dimension. The maximum-norm operator is not the ordinary Euclidean Laplacian.

These two examples are benchmarks with complementary strengths. Neither should be treated as the only permitted model.

## 5. Where to look for a simpler full formula

**Redesign the sum and observation together.** Start from a candidate elementary kernel on the higher-dimensional system, then determine its natural integral. Do not first insist on reproducing A and only afterward force the old H integral onto it. Intermediate shell multiplicities or extra modes may be useful if the complete observation handles them naturally.

**Move the completion operation to a more natural place.** The n^4 and n^2 factors in Phi arise from applying a differential operator to the primitive. They might be represented by a Laplacian, a flux, a Green identity, or differentiation of the observation instead. This can simplify the summand, but integration by parts must retain the origin/contact and endpoint terms.

The existing primitive already shows the exact cost. If

\[
J(t,z)=\int_0^\infty e^{tu^2}\psi(u)\cos(zu)\,du,
\]

then [Note01][initial] gives

\[
8H=\tfrac12+(2t-z^2-1)J+4tzJ_z-4t^2J_{zz}.
\tag{9}
\]

This is a useful benchmark for any proposed primitive-based simplification. At t=0 the reconstruction is short; at nonzero t additional frequency derivatives appear. The constant is essential. A new geometry may package these terms more naturally, but it cannot simply omit them.

**Treat z as part of the system.** Try a Cartesian plane wave, a spherical wave, a Mellin power, a boundary phase or an operator spectral parameter. Angular averaging produces sinc rather than cosine, so its compensating derivative or density must be accounted for. A simple lattice power sum for H(0,z), as in Note08, requires analytic continuation outside its initial convergence half-plane; it is not yet a convergent representation at physical real z or a construction for nonzero t.

**Treat Newman time separately from lattice heat time.** The Gaussian parameter in a lattice heat kernel is not automatically t. A useful candidate should exhibit its exact t evolution early. Formula (4) suggests one uncomplicated possibility if anisotropy is allowed; the radial inverse-marginal construction instead has a nonlocal correction. Compare these choices rather than insisting simultaneously on rotational invariance and a local radial flow.

**Be willing to change the geometry or intermediate observable.** Shifted lattices, several parity sectors, a curved three-dimensional space, a non-Euclidean norm, or a resolvent may be simpler overall than a positive unweighted cubic Gaussian. A spectral triple of labels is not automatically an additive rank-three lattice; such a change must be described honestly. Likewise, a recoverable primitive is acceptable even though its zeros are not H's zeros.

## 6. How to judge simplicity and retain the limits of earlier results

For each candidate, write down the complete expression before simplifying it back to theta. Compare:

- the summand and the rule for its coefficients;
- the lattice, geometry and measure;
- the observation and any outer derivatives or finite sector combinations;
- the t evolution;
- the endpoint, contact, convergence and regularization terms.

Prefer fewer special-purpose choices, elementary kernels, standard operators, transparent symmetry and explicit recovery. Do not optimize summand length at the expense of an opaque measure or a coefficient defined using the answer. Signed terms, one rational weight or a small coupled system are not automatic failures; their value depends on the complete formula.

Several attractive requirements may conflict. A finite-mass, nonzero positive mixture of centered Gaussian densities, for example, has a strictly positive real Fourier transform: each transformed Gaussian is positive and so is their positive mixture. That restricted class cannot by itself model a transform with real zeros. Signs, shifts, a different kernel or a different observation must then enter. This is a reason to keep the design space flexible, not to abandon higher-dimensional systems.

The existing obstructions are narrower than this program:

- Note06 excludes direct equality in its specified positive Euclidean Gaussian-trace classes. It does not exclude signed characters, a changed norm, a resolvent, or a combined observation.
- Note07 excludes a nonzero integrable global spherical mean of one fixed periodic spatial field. It does not exclude varying the field's heat parameter at a fixed observation sphere, as Note08 does.
- Positivity of a radial density, Kelvin symmetry and an exact Fourier representation do not by themselves exclude collisions. Their registered controls remain applicable.

The [result index][results] and [avoid index][avoid] remain required reading, particularly [theta arithmetic][arithmetic], [geometric realizations][geometry], [coordinate lifts][lifts], [scoped conclusions][scope], [target restatements][targets], and the [control register][controls]. The controls must be applied to any later claimed collision mechanism, with the missing premise identified for each family. This continuation note proposes no such mechanism and requires no rerun of existing event certificates.

## 7. Next continuation session

1. **Write the complete baseline.** Combine one actual rank-three sum from Note08 with the H observation, retaining all scale, angular, time and completion terms. Determine the true continuous dimension. Its purpose is to expose the complexity that must be reduced.
2. **Explore a small number of genuinely different formulations.** Include a route that relaxes the demand to reproduce A first, and a route that relaxes either positivity, Euclidean geometry or radial evolution. Use (3)–(5) as possible templates, not mandatory answers.
3. **Simplify the whole representation.** Test integration by parts, modular unfolding, geometric measures, Green/resolvent formulas and finite coupled fields. Check whether these remove work or merely move it.
4. **Establish the full parameter dictionary.** A t=0 identity is a useful intermediate result. The next stage must supply actual Newman-time dependence on a declared interval and the physical z observation, with the required convergence and derivatives.
5. **Compare the resulting systems before choosing a direction.** Save the best explicit formula, what is simpler, what costs remain, and the exact reason any rejected model failed. Structural shell or normalization checks are appropriate once a candidate is specified; a broad numerical search is not the first step.

A strong next return is a simpler native lattice kernel and three-dimensional observation for H, or a well-defined partial construction that identifies the remaining operation precisely. It need not already be a collision theorem. Once a clear system exists, ask what analytical question becomes easier in it.

## 8. Reading order and continuation status

Start here, then read [Note08][n08] for the changed lattice definitions and proofs, [Note07][n07] for the distinct radii and exact three-dimensional observations, and [Note06][n06] for the earlier trace/marginal tests. Use [Note01][initial] for normalizations and the primitive reconstruction. [Note02][old-handoff] retains the original collision-focused handoff; the [progress register][progress] remains authoritative for RTC statuses.

The five existing bounded RTC-03 returns retain their status. This is a new continuation brief, not a sixth completed mathematical return. No new numerical experiment, external theorem, collision exclusion or manuscript milestone is claimed. Existing checks and references remain at their recorded scopes; all work here is same-assistant.

The chat's unique registration remains Investigation05 chat0002. Follow the repository history workflow at the start and end of future replies; do not create a duplicate registration or move it to a different research lane.

[initial]: 01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[old-handoff]: 02_CONTINUATION_AND_SESSION_HANDOFF_20261027.md
[n03]: 03_CIRCLE_HEAT_LIFT_AND_BOUNDARY_TRANSFER_OBSTRUCTION_20261027.md
[n04]: 04_GAUSSIAN_SOURCE_DEFORMATION_AND_COLLISION_INDEX_TRANSPORT_20261027.md
[n05]: 05_MODULAR_WRONSKIAN_WEIGHT_AND_CANONICAL_SIGN_OBSTRUCTION_20261027.md
[n06]: 06_RANK_THREE_LATTICE_REALIZATION_AND_PROJECTION_20261027.md
[n07]: 07_SPATIAL_SPHERES_LOGARITHMIC_MODES_AND_PERIODIC_LATTICES_20261027.md
[n08]: 08_GENUINE_THREE_DIMENSIONAL_LATTICE_SUMS_AND_THETA_RECOVERY_20261027.md
[progress]: ../research-progress/01_RADIAL_THETA_COLLISION_RESEARCH_PROGRESS_20261027.md
[results]: ../../../../result-summaries/README.md
[arithmetic]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[geometry]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[lifts]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[targets]: ../../../../avoid/01_restating_the_target.md
