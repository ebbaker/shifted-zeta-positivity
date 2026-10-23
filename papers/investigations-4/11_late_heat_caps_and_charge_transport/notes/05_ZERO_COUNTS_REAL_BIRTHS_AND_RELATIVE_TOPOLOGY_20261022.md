# All-zero cap balances, divisor transport, and the reciprocal double cover

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**.

**Status: proved in-note within the stated finite-domain contracts; consolidation and application of classical identities and established repository results, not a new topological invariant.** No endpoint simplicity or RH exclusion follows. The contribution is a precise reusable interface between ordinary zero counts, real births, complex event residues, and the reciprocal cover of Investigation 4/09.

Read the [result index][results], [avoid index][avoid], [heat-geometry summary][geometry], [collision controls][controls], and [target classification][classify]. The classification is an exact accounting lemma and a scoped diagnostic. A claim that its total collision count vanishes on an exhaustion would again be an RH-strength assertion; the identity itself supplies no new signed estimate.

## 1. The all-zero cap/birth balance already exists

The proposed principle has a precise real-time realization in Investigation 22: [spacetime-index Note 04][realindex], especially equations (5)–(6), and [moving-wall Note 06][wall], especially equations (1)–(4). It counts **every ordinary simple real root on each cap**, then cancels transported roots between caps. Retaining the full wall term leaves just the real-birth charge.

Let H be real analytic near a compact moving rectangle

\[
 \mathcal R=\{(t,x):a<t<b,\ \ell(t)<x<r(t)\},\qquad H_t=-H_{xx},
\]

with analytic walls, no identically zero spatial slice, nonzero first jet J=(H,H_x) on the full boundary, and H nonzero at all four corners. Cap roots are consequently simple. Let N_a,N_b count all real roots on the two caps. For a wall c(t), write F_c(t)=H(t,c(t)), and define its signed crossing number

\[
 Q_c=\sum_{F_c(t_j)=0}\operatorname{sgn}H_x(t_j,c(t_j))\,
 \frac{\operatorname{sgn}F_c(t_j+\epsilon)-\operatorname{sgn}F_c(t_j-\epsilon)}2.
\]

The small epsilon is chosen separately at each isolated wall zero. Even-order tangencies contribute zero; odd-order crossings contribute their signed local degree. Then

\[
 \boxed{N_b-N_a+Q_\ell-Q_r
 =2\sum_{(T,x_*)\in\mathcal R:\,H=H_x=0}
                \left\lfloor\frac{m(T,x_*)}{2}\right\rfloor.} \tag{1}
\]

Here m is the exact spatial multiplicity. This is the complete finite-domain all-zero transport lemma. If H has no zero on either wall, both Q's vanish. Wall flux cannot be dropped merely because the endpoint caps contain the same number of roots.

For a direct loop-integral form, orient the source by dt wedge dx and set

\[
 \beta=\frac{H_x\,dH-H\,dH_x}{2\pi(H^2+H_x^2)}.
\]

This is minus the normalized angular current of H+iH_x. Its integral around the positively oriented boundary is the positive sum on the right of (1), divided by two. For fixed walls and a regular cap put

\[
 B(t)=\int_{\ell}^{r}\frac{H_x^2-HH_{xx}}{2\pi(H^2+H_x^2)}\,dx,
 \qquad \theta_c(t)=\arctan\frac{H_x(t,c)}{H(t,c)}.
\]

If H is nonzero on the walls, the exact cap identity is

\[
 \boxed{ B(t)=\frac{N_t}{2}
                +\frac{\theta_\ell(t)-\theta_r(t)}{2\pi}.} \tag{2}
\]

Indeed the principal arctangent jumps upward by pi at every simple H-zero, whereas the continuous argument of H+iH_x passes clockwise through that crossing. The wall integrals cancel the endpoint arctangents in (2). Thus

\[
 B(b)-B(a)+\int_{\text{oriented walls}}\beta
      =\sum\lfloor m/2\rfloor.
\]

The heat equation fixes the local sign: at an m-fold real event, Hermite splitting gives m nearby real roots immediately after the event and m mod 2 immediately before it, so the jump is 2 floor(m/2). The cited notes supply the full isolation, homotopy, moving-wall, and finite-multiplicity proofs.

This validates the user's cancellation idea **for real births with the complete cap and wall accounting**. The ordinary zeros need not be assigned zero cap weight. But it does not imply that a cap consisting only of simple zeros has zero integral: its roots explicitly contribute N_t/2 in (2).

## 2. Complex zeros are conserved; complex events are a different residue

For H(t,z) holomorphic in z, continuous in real t, and nonzero on a fixed spatial boundary partial Omega throughout [a,b],

\[
 N_{\mathbb C}(t)=\frac1{2\pi i}\oint_{\partial\Omega}\frac{H_z}{H}\,dz
\]

is a continuous integer, hence constant, including through interior collisions. No heat equation is needed. An m-fold complex zero and its m simple descendants carry the same multiplicity count. If a moving spatial boundary permits crossings, the endpoint difference is its signed divisor flux, not an interior source term.

When H is holomorphic in complex (t,z), the corresponding standard current statement on that complex two-dimensional domain is

\[
 \mathcal J_H=\frac1{2\pi}d\,\operatorname{Im}(dH/H)=[\operatorname{div}H],
 \qquad d\mathcal J_H=0, \tag{3}
\]

interpreted distributionally, with multiplicities and the complex orientation. Equivalently use the normalized Poincare–Lelong current; [McMullen's notes, Theorems 2.10–2.11][pl] state this convention through ddc log|H|. Ordinary divisor slices count roots. Collisions may be singular points of the divisor, but are not endpoints of that closed current. A two-dimensional spatial cap pairs with this two-current; it is not the three-dimensional Chern–Hopf boundary form.

By contrast, for a proper finite cluster over a complex-time disk or rectangle D, let P(t,z) be its monic prepared polynomial. The established [BW12 foundation][bw12] gives

\[
 Q_{\mathbb C}=\frac1{2\pi i}\oint_{\partial D}d\log\Delta_P
 =\sum_{(t,z):H=H_z=0}\binom{m(t,z)}2,
 \qquad \Delta_P=\prod_{i<j}(z_i-z_j)^2. \tag{4}
\]

This is precisely the residue-like loop integral for **complex multiple-zero events**. It is not the ordinary zero count. The real weights floor(m/2) and complex weights binom(m,2) agree at a double but differ already at a triple.

Writing D=[a,b]+i[-Y,Y], define the forward vertical cap integral

\[
 C_t=\frac1{2\pi}\Delta_{s=-Y}^{Y}\arg\Delta_P(t+is),
\]

with continuous argument, and let S be the sum of the two horizontal-edge contributions with induced orientations. Then

\[
 \boxed{Q_{\mathbb C}=C_b-C_a+S.} \tag{5}
\]

Thus genuinely proved C_b→0 and S→0 would give C_a→−Q_C. This is a valid transport statement regardless of any RH consequence. Simplicity on the late cap only guarantees Delta_P is nonzero there; it does not force C_b=0. Formula (5) is the scalar version of the already established complete boundary charge, not a replacement for its missing face estimates. In LHCT Note 04 the shrinking late cap tends to zero while the two imaginary-time closures each retain half the event charge.

One may subtract dlog Delta_ref for any holomorphic nonvanishing reference on the whole closed D: its total loop integral is zero, so it reallocates face terms without changing Q_C. A reference that is singular, only locally defined, or mismatched across patches requires its own divisor and transition contributions.

## 3. What the reciprocal double cover counts

The reciprocal construction from [RHE Note 01][rhe1] is the spatial cover

\[
 X_t:\ w^2=H(t,z),\qquad \omega_t=dz/w.
\]

It is distinct from the time-parametrized spectral divisor H(t,z)=0. Let Omega be a disk, H holomorphic near its closure and nonzero on its boundary, and write its interior zero multiplicities as m_1,...,m_k. On the **normalization** of X_t the projection to Omega branches precisely at those roots whose multiplicity is odd. If

\[
 N=\sum_jm_j,\qquad B_{\rm odd}=\#\{j:m_j\ \text{odd}\},
\]

then the bordered Riemann–Hurwitz formula gives

\[
 \boxed{\chi(\widetilde X_t)=2-B_{\rm odd},\qquad
 \chi(\widetilde X_t)-(2-N)=2\sum_j\lfloor m_j/2\rfloor.} \tag{6}
\]

The formula includes a disconnected normalization when all multiplicities are even. It is proved directly by triangulating the disk with the odd roots among the vertices: edges and faces lift twice; every ramification vertex has one rather than two lifts. [Milnor, §5.1][rh] explicitly states the same Euler-characteristic formula and its extension to surfaces with boundary.

For a nearby regular fiber in the same proper cluster, every root is simple, so its Euler characteristic is 2−N. Both pre-event and post-event regular **complex** fibers have this same value. At an m-fold singular fiber the normalized Euler-characteristic excess is 2 floor(m/2). This is useful singular-fiber information, not a permanent change between regular cap topologies. The singular fiber itself and its normalization have different Euler characteristics; they must not be interchanged.

The reciprocal differential also records the singularity. Locally H=z^m g(z), g(0) nonzero. If m=2r, the normalization has two local sheets and omega has pole order r on each. If m=2r+1, use z=xi^2: omega=2 xi^(−2r) g(xi^2)^(−1/2) dxi, regular for m=1 and of pole order 2r otherwise. Hence a simple branch point is regular for omega, while a multiple zero is singular. The reciprocal area energy 2∫|H|^(−1)dA is locally finite at a simple root, logarithmically divergent at a double, and power-divergent at higher multiplicity. Finite energy on each regular late cap is therefore not a uniform limiting estimate as a collision is approached.

These reciprocal periods and residues are amplitude-dependent: at a pure double H=A z^2 the two local residues of omega are ±A^(−1/2). They are not the integer residue of dlog H or dlog Delta_P.

The derivative-weighted energy of [RHE Note 08][rhe8] instead uses

\[
 \eta=H_z\,dz/w=2dw,\qquad W(H;\Omega)=2\int_\Omega |H_z|^2/|H|\,dA.
\]

It is finite through every multiplicity and has no point-mass defect. Its count bound from [RHE Note 09][rhe9] is

\[
 \boxed{N\le W(H;\Omega)/(4\pi m_\partial),\qquad
                  m_\partial=\inf_{\partial\Omega}|H|>0.} \tag{7}
\]

Thus RHE provides a genuine analytic budget for an ordinary cap count, provided the boundary lower margin is paid. Equation (7) alone gives neither a signed cap surplus nor an event residue. For H=A z^2 on a radius-R disk it is sharp with N=2, explicitly allowing the double.

## 4. Endpoint and control screen

If the initial cap is t=0 and has a multiple root, the nonzero-boundary-jet hypothesis of (1) fails. One must start before zero or retain a specified endpoint indentation/link. Moreover an m-fold **real** zero counted with multiplicity at t=0 already contributes m, exactly as its m real descendants at positive time. An all-zero count difference therefore does not distinguish that endpoint multiplicity. Assigning a different endpoint weight changes the invariant and must be justified separately.

The exact heat double H=z^2−2t on a sufficiently wide spatial window has two complex zeros on both caps, zero versus two real roots, real birth charge one, complex event charge one, and reciprocal-cover Euler characteristic zero on both regular fibers. Its singular normalized cover has Euler characteristic two. All formulas above hold together; none excludes it. For the cubic H=z^3−6tz, the corresponding real counts are one and three, real charge one, and complex charge three. These controls prevent identifying the two event weights or deleting a cap solely because its roots are simple.

All of the identities use generic analytic/heat premises shared by applicable Euler-factor, weighted-square, reflected, and positive-primitive controls. **No such control is rejected by these identities.** The controls' distinct failures of full theta arithmetic, reflection, or unchanged canonical coefficients remain as listed in [the existing control register][controls]; none of those extra premises is used here. Consequently this note makes no theta exclusion claim and requires no fresh numerical scan. Its reusable deliverable is the exact choice of invariant, dimensions, endpoint conventions, and complete boundary contract.

[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[classify]: ../../../../avoid/01_restating_the_target.md
[realindex]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[wall]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[bw12]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/manuscript/foundations.tex
[rhe1]: ../../09_reciprocal_hodge_energy/notes/01_FINITE_COVER_CONTRACT_AND_ENERGY_ENCLOSURE_20261022.md
[rhe8]: ../../09_reciprocal_hodge_energy/notes/08_DERIVATIVE_WEIGHTED_ENERGY_AND_GLOBAL_STRIP_BOUND_20261022.md
[rhe9]: ../../09_reciprocal_hodge_energy/notes/09_SIGNED_LAGUERRE_TRANSFER_AND_COUNT_BOUND_20261022.md
[pl]: https://people.math.harvard.edu/~ctm/papers/home/text/class/notes/pn/course.pdf
[rh]: https://legacy-www.math.harvard.edu/archive/118r_spring_05/docs/milnor.pdf
