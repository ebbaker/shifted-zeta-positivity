# Chern--Simons/WZW as a natural setting for Loewner evolution

22 September 2026. Prepared for Edward Baker.

**Model:** GPT-6 (Codex; developer-provided identity).
**Effort:** not exposed in this session; not inferred.
**Status:** literature-grounded assessment and proposed pilot, prepared with LLM assistance. No arithmetic realization, new CFT theorem, or completed boundary construction is claimed.

## Research direction

Baker proposes looking for a theory in which the boundary, Wilson endpoints, and Loewner evolution arise together, before attempting the pending four-dimensional Yang--Mills closure calculation. Chern--Simons theory with specified conformal boundary data is a serious candidate. The immediate task should be to understand its native boundary observables and evolution, allowing the arithmetic comparison to follow that construction.

The present recommendation is to examine boundary WZW conformal blocks and their deterministic Loewner transport, keeping the Chern--Simons interpretation of endpoints and gluing explicit. The previously proposed source hierarchy and abstract boundary readout are not prerequisites. No existing manuscript or research result is superseded by a claimed construction here.

## What the correspondence supplies

For suitable compact gauge group and level, quantization of Chern--Simons theory on a surface produces spaces of WZW conformal blocks. Wilson representations label marked insertions. This is the relevant content of [Witten, Quantum field theory and the Jones polynomial, Sections 3 and 5](https://www.ias.edu/sites/default/files/sns/%5B115%5DCommMathPhys121-1989.pdf).

[Alekseev--Barmaz--Mnev](https://arxiv.org/abs/1212.6256) explicitly treat Wilson lines ending on the spacetime boundary and identify the resulting physical boundary-state space with WZW conformal blocks. This supplies a concrete source for endpoint data. It does not identify that space with L2(I_L).

Boundary conditions and a complex polarization must be specified. A general Chern--Simons boundary is not canonically the complex plane. To use half-plane boundary CFT, one also needs a compatible conformal boundary condition, defect construction, or appropriate chiral/antichiral pairing. [Cattaneo--Mnev--Wernli](https://arxiv.org/abs/2012.13983) give a boundary-polarization and cutting/gluing formulation on cylinders; this is useful for making these choices explicit.

The proposed physical advantage is that endpoint labels, permissible channels, and composition would be selected by a known state space and its gluing rules. They would not first be arbitrary kernel labels and an unspecified projection R.

## Where shape dependence lives

Bulk Chern--Simons amplitudes are topological, with framing and endpoint data retained. Smoothly changing an isolated bulk path at fixed endpoints, framing, and topology does not provide the desired generic geometric evolution. The relevant candidate is the conformal boundary amplitude, whose marked coordinates, local conformal frames, or slit domain change.

Likewise, a boundary Loewner interface must not simply be declared to be the identical geometric object as a bulk Wilson line. The relation between the bulk representation labels and boundary insertions is established structure; a particular interface observable still requires its own definition.

This makes the domain interpretation materially different from the current four-dimensional calculation: there the plane is an embedding for a probe in a fixed ambient spacetime. Here a slit can be part of the domain of a two-dimensional conformal boundary theory, with boundary conditions on its two sides. Conformal transport can therefore control its variation.

## A concrete deterministic equation to investigate

For a chosen collection of primary representations, let F(z_1,...,z_n) denote a vector of chiral conformal blocks. In the standard current-algebra normalization the KZ equation has the form

\[
 \partial_{z_i}F=A_i(z)F,\qquad
 A_i(z)=\frac{1}{k+h^\vee}
          \sum_{j\ne i}\frac{\Omega_{ij}}{z_i-z_j},
 \quad \Omega_{ij}=\sum_a t_i^a t_j^a.
\]

See [Alekseev--Bytsko--Izyurov, Section 3](https://arxiv.org/html/1012.3113). Mirror insertions, endpoint fields and invariant/fusion channels are part of the boundary formulation and must be included explicitly.

Now prescribe a sufficiently regular deterministic Loewner driver u(t). Spectator marked points transported by g_t satisfy

\[
 \dot z_i(t)=\frac{2}{z_i(t)-u(t)}.
\]

For any specified path of all marked coordinates away from collisions, the chain rule gives the exact pullback identity

\[
 \frac{d}{dt}F(z(t))=\sum_i\dot z_i(t)A_i(z(t))F(z(t)).
\]

This is a proposed calculation using a known closed system, not a derivation of a particular new slit observable. To identify it with a physical correlator one must include conformal Jacobians, the moving tip field, normalization and any anomaly/local-coordinate factors. For a chiral primary Jacobian J_i(t)^{h_i}, the spectator Loewner contribution is

\[
 \partial_t\log J_i(t)^{h_i}
 =-\frac{2h_i}{(z_i(t)-u(t))^2}.
\]

The corresponding infinitesimal conformal action is the Ward operator
sum_i [v(z_i) partial_(z_i) + h_i v'(z_i)], with v(z)=2/(z-u). At the functional level, shape variation is generated by the stress tensor; fixed insertions reduce that action to differential equations in marked coordinates. [Bauer--Bernard](https://arxiv.org/abs/hep-th/0210015) provides the CFT/Loewner framework.

The potential gain is an explicit evolution whose coefficients and allowed states follow from symmetry and representations. The generator acts on conformal blocks or boundary states; identifying an arithmetic response is a subsequent task.

## Existing stochastic precedent and its scope

[Bettelheim--Gruzberg--Ludwig--Wiegmann](https://arxiv.org/abs/hep-th/0503013) extend SLE to WZW systems with internal spin degrees of freedom and connect the evolution to KZ equations.

[Alekseev--Bytsko--Izyurov](https://arxiv.org/abs/1012.3113) analyze boundary correlators on a slit half-plane, with fields at the growing tip and a target. Their martingale construction uses Brownian driving and an additional internal group diffusion, together with a level-two null-vector condition. A finite target is also treated. These are not conclusions for an arbitrary deterministic driver.

Quantum averaging over the fixed theory and probability averaging over the driver are separate operations. The proposed first pilot retains deterministic driving. A stochastic law should be introduced only if the selected model supplies a reason to use it. Martingale conservation also does not establish the arithmetic transfer's L2 contraction.

## Proposed pilot

Choose a small SU(2)_k boundary WZW sector at integer k >= 2, with explicit compatible boundary conditions, endpoint representations and a nontrivial four-point block. An alternative following the slit-correlator literature is a pair of boundary-changing fields plus a bulk probe and its mirror insertion. The detailed choice should be made before asserting a particular block dimension or transfer interpretation.

The pilot should deliver:

1. The observable and the physical boundary/state space on which it acts.
2. The deterministic Loewner variation, including every endpoint and conformal factor.
3. Its reduction using Ward and KZ identities, with a specified initial block/state.
4. Its gluing or composition rule, including the pairing used to obtain scalar amplitudes if needed.
5. A statement of what spatial boundary smearing would mean, before naming the result an operator on L2(I_L).

A two-dimensional boundary CFT can be studied directly if the Loewner/interface question is primary. Retaining the WZW/Chern--Simons pair is preferable for this pilot if the Wilson-line interpretation and gauge representation labels are central. Neither choice requires a prior arithmetic match to make the physical calculation worthwhile.

## Later comparison, without building in the answer

Compact Chern--Simons theory with fixed topology and finitely many labeled punctures supplies finite-dimensional conformal-block spaces. This is useful for a pilot but is not already the infinite-dimensional arithmetic boundary-input space. Descendants, boundary smearing, or a different sector would require an explicit construction if used in that comparison.

The arithmetic generator's gamma contribution, fixed normalization, pole response and prime-power translations remain later tests. The sources examined do not supply the shifted-zeta quotient or its prime coefficients. The recommended reason to explore this setting is the natural joint occurrence of geometry, endpoints and differential identities.

Loewner capacity, endpoint-window length L and arithmetic shift omega also remain distinct. In particular a half-plane slit does not by itself enlarge a chosen interval on its real boundary.

Only this note was added; the Yang--Mills handoff was not executed, and no manuscript or snapshot was changed.
