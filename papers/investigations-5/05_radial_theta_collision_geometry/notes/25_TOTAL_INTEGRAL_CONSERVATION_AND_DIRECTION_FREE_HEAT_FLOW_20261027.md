# Total integral conservation and a direction independent heat flow

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, chat0008.

**Status: conservation, direct theta application, and the stated diffusion asymptotics are proved in-note using the explicit Gaussian kernel; same-assistant assessment.** Edward Baker has relaxed the earlier requirement: the three-dimensional integrand may change, including its radial average, provided its entire integral remains H(t,a). This note gives an actual local flow under that weaker requirement. Its collision diagnostic is a faster decay of two spectral-jet components. It is not a growing instability, a theta-specific separating estimate, or a collision exclusion.

This supersedes radial-integrand preservation as the *general requirement*, not the statements of [Notes20](20_AUXILIARY_ANGULAR_FLOWS_AND_COLLISION_LOCALIZATION_20261027.md), [22](22_STEERED_TUBE_GREEN_IDENTITY_AND_MATCHED_COMPARISON_20261027.md), and [23](23_PROJECTED_ANNULAR_FLOW_RESPONSE_AND_LOCAL_ADJOINT_20261027.md), which remain stronger special cases. [Note24](24_EXPLICIT_THETA_FLOW_AND_COLLISION_MAGNIFICATION_SCOPE_20261027.md) explains the projected flow's notation and explicit theta input. The [result index](../../../../result-summaries/README.md), [avoid index](../../../../avoid/README.md), [controls](../../../../result-summaries/12_collision_controls_and_screening.md), [target classification](../../../../avoid/01_restating_the_target.md), and [scope rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md) govern interpretation. The return is a concrete representation and quantified diagnostic, not evidence for a new final-strength criterion.

## 1. Conservation replaces the pointwise radial constraint

Write j_s(t,a;X) for the **full signed density with respect to Euclidean volume**, so the new requirement is

\[
\boxed{\int_{\Omega}j_s(t,a;X)\,dX=H(t,a).}
\tag{1}
\]

Preservation is required as a sufficiently differentiable family in a, not just at one nominated frequency, if its derivative is to retain the physical collision condition. A local conservation equation is

\[
\boxed{\partial_s j_s+\nabla\cdot J_s=0.}
\tag{2}
\]

For a smooth bounded region, the derivative of (1) is minus the total outward flux. On an exterior or whole-space domain the outer limit must also vanish. No-flux boundary conditions suffice; more general boundaries can be used if their net flux is explicitly accounted for. The integral over a *subregion* changes by its boundary flux. Thus radial and angular localization can change without an unrecorded loss.

The choice J_s=-ε∇j_s, ε>0, gives ordinary heat flow. It requires no preferred spatial direction, prescribed target cap, or angular averaging term. Other conservative fluxes remain available, but (2) alone is not an existence theorem for an arbitrary nonlinear choice.

There is a factorization issue. If one insists that a source F_s(r,ω) be independent of a and keeps the old kernel, then invariance for **every** real a gives

\[
\int_1^\infty r^{3/2}[PF_s(r)-Q_t(r)]
                \cos(a\log r/2)\,dr=0\quad(a\in\mathbb R).
\tag{3}
\]

Assuming the bracketed weighted difference is integrable, changing variables r=e^{2u} identifies its cosine transform. Its even extension is an L¹ function with zero Fourier transform, and is therefore zero: PF_s=Q_t almost everywhere. One elementary uniqueness proof convolves the even extension with a Gaussian. The Gaussian's integrable Fourier representation and Fubini make every such convolution zero; Gaussian approximate-identity convergence in L¹ then gives the claim. Thus (3) does not produce the desired extra freedom within that fixed factorization. This is a scoped observation, not an obstruction to (1): evolve the full a-dependent density, or evolve the source and testing kernel together.

For example, smooth transport with velocity v, tangent to any finite boundary, can use

\[
\partial_s\rho+\nabla\cdot(\rho v)=0,\qquad
\partial_s\ell+v\cdot\nabla\ell=0,\qquad j_s=\rho_s\cos(a\ell_s).
\tag{4}
\]

Then j_s satisfies (2) with J_s=vj_s. The initial values are
ρ_0=Q_t/(32π\sqrt r), ℓ_0=(\log r)/2 on r≥1. A complete smooth flow and the required tail flux bounds are assumptions for this transport example. Changing the phase ℓ accounts for moving radii. Pure transport alone is a change of representation, with no collision amplification law supplied.

## 2. A fully specified heat evolution from the theta sum

For a concrete construction without artificial radial faces, take Ω=R³ and set

\[
j_0(t,a;X)=
\begin{cases}
\dfrac{Q_t(r)}{32\pi\sqrt r}\cos(a\log r/2),&r=|X|\ge1,\\[4pt]
0,&r<1.
\end{cases}
\tag{5}
\]
\[
Q_t(r)=4\pi e^{t(\log r)^2/4}
       \sum_{n\ge1}n^2(2\pi n^2r^2-3)e^{-\pi n^2r^2}.
\tag{6}
\]

The factor 32π is fixed by spherical volume: integrating (5) gives
H(t,a)=(1/8)∫_1^∞r^{3/2}Q_t(r)cos(a log r/2)dr. The initially empty ball is part of the auxiliary domain; positive auxiliary time may carry density into it. This is **not** an additional inverted theta integral or a second copy of the original source.

Put
\[
K_{\varepsilon s}(X)=(4\pi\varepsilon s)^{-3/2}
                  e^{-|X|^2/(4\varepsilon s)},\qquad
\boxed{j_s=K_{\varepsilon s}*j_0,\quad
       \partial_sj_s=\varepsilon\Delta j_s.}
\tag{7}
\]

The complete theta tails imply j_0∈L¹∩L²∩L∞, with all finite spatial absolute moments and all finite physical parameter derivatives on compact parameter sets. It has a possible jump at r=1; no classical initial boundary compatibility is asserted. The Gaussian kernel gives the L¹-continuous mild solution, smooth for s>0, with the initial datum recovered in L¹. Direct differentiation proves its equation. L¹ uniqueness in the continuous mild class follows from the heat semigroup. These standard inputs are also recorded in Hunter, Section5.1, equations(5.5)–(5.6), Theorem5.5; see [reference annotation10](../references/10_PROJECTED_EVOLUTION_AND_ELLIPTIC_RESPONSE_20261027.md).

Since K≥0 and ∫K=1, Fubini proves

\[
\int_{\mathbb R^3}j_s\,dX=H(t,a),\qquad
\|j_s\|_1\le\|j_0\|_1.
\tag{8}
\]

These equalities include any flux across r=1. Keeping only the exterior integral at positive s would omit that flux and would not be the construction. On the fixed exterior one can instead prescribe a conservative boundary condition, but its heat kernel would be different.

The operator in (7) is independent of t and a. Dominated differentiation therefore gives

\[
\int\partial_a^k j_s\,dX=\partial_a^kH(t,a),\qquad
\partial_tj_s=-\partial_a^2j_s
\tag{9}
\]

for every finite k, with the same physical heat law as the original family. This supplies the full parameter accounting, not merely a single preserved number.

The theta sum can be passed through (7) in L¹. Indeed its positive summands Q_{t,n} satisfy

\[
\sum_{n\ge1}\|j_{0,n}\|_1
\le\frac18\int_1^\infty r^{3/2}Q_t(r)\,dr=H(t,0)<\infty.
\]

For a partial source Q_{t,N} and its evolved density j_s^{(N)},

\[
\|j_s-j_s^{(N)}\|_1\le
B_N(t):=\frac18\int_1^\infty r^{3/2}(Q_t-Q_{t,N})\,dr,
\]
\[
\|j_s-j_s^{(N)}\|_\infty\le(4\pi\varepsilon s)^{-3/2}B_N(t).
\tag{10}
\]

Both bounds are uniform in real a. Replacing the integrand by u^k times its positive majorant yields the corresponding spectral derivative bounds. The full infinite sum has exactly the original observation; a finite truncation has its own observation and requires this tail payment.

For radial evaluation, at radius R≥0,

\[
j_s(R)=\frac{(4\pi\varepsilon s)^{-3/2}}8
 \int_1^\infty r^{3/2}Q_t(r)\cos(a\log r/2)
 e^{-(R^2+r^2)/(4\varepsilon s)}
 \frac{\sinh(Rr/(2\varepsilon s))}{Rr/(2\varepsilon s)}\,dr.
\tag{11}
\]

The ratio is one at zero. This follows by integrating the Gaussian over the sphere and is a direct one-dimensional formula for the full three-dimensional flow. No PDE discretization or selected angular penalty is needed.

## 3. What a collision does to this flow

For k≥0 define the signed and absolute moments

\[
M_{2,k}=\int |X|^2\partial_a^k j_0\,dX,\qquad
A_{m,k}=\int |X|^m|\partial_a^k j_0|\,dX.
\]

They are finite by the theta tails. At the spatial origin the exact heat formula yields

\[
(4\pi\varepsilon s)^{3/2}\partial_a^k j_s(0)
=\partial_a^kH(t,a)-\frac{M_{2,k}}{4\varepsilon s}
+\mathcal R_{s,k},
\quad
|\mathcal R_{s,k}|\le\frac{A_{4,k}}{32\varepsilon^2s^2}.
\tag{12}
\]

This uses |e^{-x}-1+x|≤x²/2 for x≥0. The simpler bound

\[
\left|(4\pi\varepsilon s)^{3/2}\partial_a^k j_s(0)
-\partial_a^kH(t,a)\right|
\le\frac{A_{2,k}}{4\varepsilon s}
\tag{13}
\]

follows from |e^{-x}-1|≤x. These are explicit inequalities for every s>0, not just formal expansions. All absolute moment constants can be bounded by the positive full theta sum.

At a collision H(T,a)=H_a(T,a)=0, both j_s(T,a;0) and ∂_a j_s(T,a;0) are O(s^{-5/2}). A nonzero conserved component instead has leading order s^{-3/2} with its actual nonzero coefficient from (12). At a simple zero, only the first component has the extra cancellation. Higher multiplicities remove the leading mode in each corresponding spectral derivative.

This detects collision degeneracy through simultaneous loss of the leading diffusion mode. It is not a growing amplitude or concentration instability. The conclusion is at the stated central observation; no uniform all-space or all-height asymptotic estimate is inferred. Inverting a vanishing signal or merely rescaling it would not provide a new source estimate.

The initial data are radial and the heat operator is rotation invariant, so the evolution remains radial. This is allowed under (1), and it is nontrivial because the radial integrand may now change. The earlier zero-start stationary statement concerned a perturbation G under the stronger PF=Q constraint, not this full-density flow.

## 4. Controls and the next mathematical question

For the exact control Φ_*(u)=(64u⁴+6)e^{-(4+T_c)u²}, the event at (T_c,2√6) has both conserved masses zero. Formula(5) with Q_t=4r^{-5/2}e^{tu²}Φ_*(u) has every spatial moment on t<T_c+4. Thus (12)–(13) give the same extra decay at its real collision. The control fails the complete theta-source premise, but **no premise of this generic heat theorem fails**.

The smooth Euler-factor, weighted-square, finite-prime, reflected super-Gaussian, and positive-primitive controls likewise satisfy the conservation construction on their stated convergence domains whenever the displayed absolute moments are finite. Their failed theta inputs are those in the registered [control screen](../../../../result-summaries/12_collision_controls_and_screening.md): modified coefficients/reflection for square controls, incomplete arithmetic square sources for reflected/primitive controls, and modified arithmetic factors for Euler controls. None is excluded by positivity, diffusion or total-mass conservation. Atomic sources are outside the L¹-density formulation stated here.

The current next question is whether a conservative local evolution, possibly coupled to a response or spectral-jet field, yields a collision-sensitive growth or concentration law **and** a canonical theta estimate that makes that behavior quantitatively useful. Total-integral conservation is sufficient; fixed radial marginals and prescribed directions are not requirements. The proved heat example supplies a simple baseline and an exact decay diagnostic. [Review14](../reviews/14_PROJECTED_FLOW_MANUSCRIPT_AND_COLLISION_SCOPE_20261027.md) assesses both this result and the integration of the projected-flow results into the manuscript.
