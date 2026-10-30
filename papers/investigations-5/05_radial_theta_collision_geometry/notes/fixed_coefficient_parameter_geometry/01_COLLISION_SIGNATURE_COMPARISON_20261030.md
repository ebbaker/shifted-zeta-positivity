# FCG-B01: three collision signatures and one provisional selection

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra**, reasoning effort **xhigh**. Investigation05 **chat0043**, *Compare FCG-B01 collision signatures*.

**Return: B01 complete as a bounded conceptual comparison. Select FCG-C01 R1, relative signed frequency curvature, for B02.** The collision calculations and common-kernel formulas below have same-assistant derivations/checks only. The theta restriction is **unproved**. No numerical work, new PDE, exclusion, coverage gain, or independent assessment is claimed.

| Rank / persistent candidate | Collision signature, initially for a nondegenerate double | Preliminary complete-theta connection | Disposition |
| --- | --- | --- | --- |
| **1. FCG-C01 R1** | The limiting signed frequency curvature divided by jet energy has a negative pole on the stationary predecessor | Exact two-source-point formula with the complete parity–Poisson product, retaining the actual prepared/evolved overlap kernel | **Select provisionally:** a concrete signed consumer; useful source estimate and propagation remain open |
| **2. FCG-C02 R1** | Relative physical-parameter response becomes unbounded at the collision as auxiliary time tends to infinity | Complete theta primitive identity applied to the derivative-weighted transported tests | Inactive: absolute derivative estimates do not supply the required reverse norm comparison |
| **3. FCG-C03 R1** | A small oriented physical loop has jet winding −1 | Full theta primitive evaluation of a bounded spatial observation on the loop | Inactive: an independent zero-degree estimate and boundary control are missing |

These are different observations of the same physical jet; they are not three independent reasons for exclusion. C01 is chosen because its arithmetic consumer is an explicit signed bilinear expression. It has no demonstrated advantage over direct analysis of that expression. Its credibility is the source-to-observable interface, not evidence that the missing inequality is true.

## 1. Fixed family, provenance, and scope

Use [Overview06][overview], [the fixed-flow derivation][fixed], and [the parameter-family note][family]. For physical parameters p=(T,A), auxiliary time s≥0, and one finite c>0 fixed throughout a compact physical region K,

\[
 H=\int_0^\infty e^{Tu^2}\Phi(u)\cos(Au)\,du,\quad H_T=-H_{AA},
 \qquad W_c=(U_c,U_{c,A}),\quad \partial_sW_c=\Delta W_c+c\operatorname{div}(vW_c),
\]
\[
 v(X)=X+X/(1+|X|^2),\qquad
 W_c(0)=K_1*[\rho_T(\cos Au,-u\sin Au)],
 \quad \rho_T=\mathbf1_{|X|\ge1}e^{Tu^2}\Phi(u)/(8\pi|X|^3),
 \quad u=\tfrac12\log|X|.
\]

Write J=(H,H_A), p_c=Z(c)^{-1}e^{-c(|X|^2+\log(1+|X|^2))/2}, and Q(c)=||p_c||₂²>0. The inherited fixed-flow argument gives, for every required finite parameter derivative, compact-uniform L² convergence

\[
 \partial_p^\nu W_c(s;p)\longrightarrow(\partial_p^\nu J(p))p_c,
 \qquad \sup_{p\in K}||\partial_p^\nu(W_c-Jp_c)||_2^2
 \le C_{K,\nu,c}e^{-cs/2}. \tag{1}
\]

This argument uses complete moment and preparation budgets, not a positive physical-mass floor. It remains a same-assistant inherited result; its uses below must be checked in an eventual E assessment. All derivatives refer to the common fixed-c family. No derivative of a fitted coefficient is suppressed.

Here K is compact and convex with nonempty interior in T>0. The initial collision class is an **interior nondegenerate double**, H(p₀)=H_A(p₀)=0, b=H_AA(p₀)≠0. Gaussian-control regions additionally stay in their moment domain. Higher multiplicity and transfer to an RH-related domain are not established by this return. A boundary event can be made interior to a larger compact region in T>0; this matters for C01 and C03. No claim about a one-sided boundary event on the original K is inferred.

Classification follows the [result index][results], [local geometry cluster][geometry], [control register][controls], and [avoid index][avoid], particularly [target reformulations][a01], [shared premises][a02], [scoped exclusions][a07], [lost cancellation][a12], and [circular constants][a14]. The known stationary pole and local index are reused, not claimed as discoveries.

## 2. FCG-C01 R1: relative signed frequency curvature

Define the real quadratic observations

\[
 E_c=||U_c||_2^2+||U_{c,A}||_2^2,
 \qquad D_c=||U_{c,A}||_2^2-\langle U_c,U_{c,AA}\rangle. \tag{2}
\]

D_c is a signed frequency-curvature expression, **not** the curvature of a metric or a scalar-energy Hessian. It uses no normalization in its definition. By (1), uniformly on K,

\[
 E_c\to Q(c)E_J,\quad D_c\to Q(c)L,
 \qquad E_J=H^2+H_A^2,\quad L=H_A^2-HH_{AA}. \tag{3}
\]

**Collision law.** The implicit-function theorem gives a stationary branch A=a(T) through p₀ with H_A(T,a(T))=0. With h=T₀−T↓0,

\[
 H(T_0-h,a(T_0-h))=bh+O(h^2),\quad H_{AA}=b+O(h),
 \quad L=-b^2h+O(h^2),\quad E_J=b^2h^2+O(h^3).
\]

Thus L/E_J=−1/h+O(1), the inherited double-event pole. The raw fields stay regular; the pole comes from division by vanishing energy. It still yields a genuine obstruction to the **undivided** estimate

\[
 \mathsf X_1(K,c):\quad \exists C,S<\infty,\ C,S\ge0:\quad
 D_c(s;p)+C E_c(s;p)\ge0\quad(p\in K,\ s\ge S). \tag{4}
\]

At an interior double event, (4) fails for **every** finite c>0. For any proposed C choose a sufficiently close stationary predecessor in K with L+CE_J<0; then (3) makes D_c+CE_c<0 at sufficiently large s. The limit is taken at that fixed predecessor; no unjustified joint limit in h and s is needed.

Conversely, if J is nonzero on all of K, compactness and (1) give a positive late-time E_c floor and a uniform bound on |D_c|, so (4) holds. This proves an equivalence only in the restricted setting where all possible zeros on K are interior nondegenerate doubles; it is **not** an all-multiplicity, all-boundary characterization. The constant obtained from min_K|J| in this converse cannot prove the theta direction.

The proposed theta obligation is ∀K ∃ finite c_K,C_K,S_K such that (4) holds. One c_K serves all p and all auxiliary times in its stated range. Constants may differ between regions, but must be obtained without assuming nonvanishing. A bare lower bound D_c≥−B_K is insufficient: the negative pole is relative to E_c. Nonnegativity D_c≥0 would be stronger than necessary.

### The complete source reaches exactly this consumer

Let k_r(X)=(4π)^{-1}∫_{S²}K₁(X−rθ)dθ and

\[
 g_s^c(u)=P_s^c k_{e^{2u}},\quad
 B_s^c(u,v)=\langle g_s^c(u),g_s^c(v)\rangle,\quad
 f_T(u)=e^{Tu^2}\Phi(u).
\]

Both kernels g have mass one. B is symmetric, nonnegative pointwise, and positive semidefinite as an overlap kernel. Direct polar integration and differentiation in A give

\[
 D_c+CE_c=\int_0^\infty\!\int_0^\infty
 f_T(u)f_T(v)B_s^c(u,v)[\Gamma_A(u,v)+C\eta_A(u,v)]\,du\,dv, \tag{5}
\]
\[
 \Gamma_A=\tfrac14\{(u+v)^2\cos A(u-v)+(u-v)^2\cos A(u+v)\},
 \qquad \eta_A=\cos Au\cos Av+uv\sin Au\sin Av.
\]

For example, symmetrizing −⟨U,U_AA⟩ gives (u²+v²)cos(Au)cos(Av)/2; adding uv sin(Au)sin(Av) gives Γ. This checks the factor 1/4. Positivity of B alone gives no sign for (5).

The starting kernel is explicit. For r=e^{2u}, t=e^{2v},

\[
 B_0^c(u,v)=(8\pi)^{-3/2}e^{-(r^2+t^2)/8}
 \frac{\sinh(rt/4)}{rt/4}. \tag{6}
\]

This follows from Gaussian convolution K₁*K₁=K₂ and the spherical average of exp(rt cosθ/4). It includes the unit preparation and all of physical space; no exterior boundary condition has been inserted. It is independent of c at s=0.

For every fixed u,v, B_s^c→Q(c). This also passes through (5): the mass-one Nash estimate in [the fixed-flow proof][fixed] gives

\[
 0\le B_s^c(u,v)\le M_c:=\max\{(8\pi)^{-3/2},(3c/c_N)^{3/2}\},
 \quad c_N=\tfrac35(6\pi^2)^{2/3},
\]

uniformly in s,u,v. The complete theta tail dominates f_T(u)f_T(v) times the polynomial weights uniformly on K. Each seed has a finite first moment, so its individual convergence is legitimate even though that moment is not uniform in u. Dominated convergence, or directly (1), recovers (3). No positive mass of the **signed** field enters this transfer.

For an arithmetic connection, put z=(u+v)/2, w=(u−v)/2 and P(x)=e^xΘ(e^{4x}), with Θ(y)=∑_{n∈Z}e^{-πn²y}. [The complete parity–Poisson identity][poisson] gives

\[
 \Pi(z,w)=P(z+w)P(z-w)
 =\frac1{\sqrt{2\cosh4w}}\sum_{m,n\in\mathbb Z}
 e^{-\pi(e^{4z}m^2+e^{-4z}n^2)/(2\cosh4w)}
 (-1)^{mn}\cos(\pi mn\tanh4w),
\]
\[
 \Phi(z+w)\Phi(z-w)=\mathcal D\Pi/4096,
 \quad\mathcal D=(\partial_z^2-\partial_w^2)^2
                 -8(\partial_z^2+\partial_w^2)+16. \tag{7}
\]

In (5), the transformed domain is z≥|w|, the Jacobian is 2, and the heat weight is e^{2T(z²+w²)}. In particular Γ=z²cos(2Aw)+w²cos(2Az). The differential operator in (7) acts on the complete theta product; moving it to the overlap kernel would require all derivative and boundary terms. Ordinary same-nome addition formulas do not replace this two-independent-coordinate identity.

**Required gain:** use the full relation (7), with the literal cosine and the common B_s^c, to bound the signed integral (5) below by zero with finite C uniformly in its declared region and late-time range. This is a candidate connection, not a proved consequence of (7), reflection, or source uniqueness. The distinction from weighted squares is the complete unit-coefficient parity–Poisson relation; the distinction must survive into the inequality actually used.

**Propagation and first bounded test.** Formula (5) is valid at each s; it does not show that a sign at s=0 propagates. For example,

\[
 \partial_sD_c=-2||\nabla U_{c,A}||_2^2
 +2\langle\nabla U_c,\nabla U_{c,AA}\rangle
 +c\int\operatorname{div}v\,(U_{c,A}^2-U_cU_{c,AA}),
\]

which has no generic favorable sign. B02 should test **one** complete signed cancellation mechanism against the explicit B₀ and the limiting kernel Q, before demanding a theorem for all B_s. Fix c=1 for that structural pilot; this is not a proof that c=1 works for all regions. Keep the existing source and one declared compact K. No sampling of known noncolliding marks is part of the pilot.

[The old axis/mixed split][poisson] is not globally heat-integrable; [the windowed continuation][localized] restores integrability but not energy-relative control. Those results have their original full-plane weights. They do not automatically prove divergence for the new cone and B_s weight, nor do they license an undamped termwise interchange here. A future split must prove its own joint-tail integrability and signed payment. A fixed absolute O(ε) localization error cannot by itself control an energy that may tend to zero. No new localization parameter, numerical cutoff, or damping has been selected.

**Direct comparison.** At infinity B_s/Q→1, so the consumer is exactly L+CE_J≥0. Varying c does not change that limiting ratio. The criterion is a reformulation in its declared event class. Any useful gain must be a new signed estimate or a justified finite-time propagation mechanism; the common-kernel representation supplies neither by itself. An equally informed direct method may use (5)–(7). Selection authorizes testing that missing connection, not a new general theory of the fixed flow.

## 3. FCG-C02 R1: relative parameter response

Let N_c=||∂_TW_c||₂²+||∂_AW_c||₂². The proposed property is

\[
 \mathsf X_2(K,c):\ \exists C,S<\infty:\quad N_c(s;p)\le C E_c(s;p)
 \quad(p\in K,s\ge S). \tag{8}
\]

At a double collision, in coordinates (T,A),

\[
 DJ(p_0)=\begin{pmatrix}-b&0\\H_{AT}(p_0)&b\end{pmatrix},
 \quad \det DJ=-b^2,
 \quad N_c(s;p_0)\to Q(c)(2b^2+H_{AT}^2)>0,
 \quad E_c(s;p_0)\to0.
\]

Thus (8) fails for every finite c, including a double event on the boundary. Whenever E_c>0, the inherited exponential upper bound on E_c even gives an exponential lower bound on N_c/E_c at this mark. No division is needed to prove failure of (8). This is singular **relative sensitivity**, not a singularity of W or its unnormalized derivatives. Without collisions on compact K, (8) follows from the same compactness argument as C01. No extension to every higher multiplicity is made here.

The preliminary theta input is [the complete primitive transfer][primitive]: for ψ(u)=e^u∑_{n≥1}e^{-πn²e^{4u}},

\[
 \int_0^\infty\Phi f=\frac{f(0)}{16}
 +\frac{\psi(0)f'(0)}8+\frac18\int_0^\infty\psi(f''-f). \tag{9}
\]

Apply it to the transported spatial tests with weights e^{Tu²}, u² and the actual frequency derivatives. It evaluates the relevant parameter responses without replacing the theta coefficients. The needed gain is a **reverse** comparison with ||W_c||₂, uniformly through possible mass cancellation. The known absolute moment and primitive-test bounds do not do this. Initial derivative/trace costs and propagation must stay visible; [Note75][tests] shows why retaining the joint primitive identity alone reconstructs the same prepared source.

The first bounded test, if C02 is later activated, is whether the full ψ relation yields one noncircular reverse comparison for these fixed tests, rather than only an absolute derivative budget. Positive ψ and its normalized endpoint are shared by colliding controls after rescaling, so they are insufficient. Rank two: the geometric signature is sharp, but its present source consumer is less concrete than the signed bilinear target in C01.

## 4. FCG-C03 R1: local winding of a bounded observation

Set Y_c(s;p)=⟨p_c,W_c(s;p)⟩/Q(c), componentwise. This bounded L² observation tends to J in C¹(K) by (1). On a small positively oriented physical loop Γ enclosing only a double event,

\[
 \nu(J;\Gamma)=\frac1{2\pi}\oint_\Gamma
 \frac{H\,dH_A-H_A\,dH}{H^2+H_A^2}=-1,
\]

because det DJ=−b². For each such loop, δ_Γ=min_Γ|J|>0; if sup_Γ|Y_c−J|<δ_Γ, homotopy preserves that degree. This is a justified eventual transfer, not a theta estimate for δ_Γ. The angular form is locally closed away from the zero; its loop charge is not a nonzero smooth curvature density there.

The exclusion property would require zero degree on every admissible event-enclosing loop (with nonzero boundary) in K for all sufficiently large s at one c. A collision obstructs it for every c. Computing only degree on ∂K needs its own nonzero-boundary hypotheses and, beyond this double-event scope, the inherited negative-index theorem. No boundary-only requirement is imposed on the other candidates.

The preliminary theta connection again uses (9), now with the fixed terminal test p_c/Q(c) and transported/prepared test \(K_1(P_s^c)^*[p_c/Q(c)]\). The star denotes the spatial adjoint. This must retain the initial-sphere traces. It gives complete-source values of the two observed components. It does not determine their loop winding or pay an independent boundary margin. A future test would seek a signed zero-degree deformation with all boundary crossings controlled. Rank three: the same arithmetic cancellation must be settled and additional boundary geometry is required. The local index is inherited; no new topological restriction is claimed.

## 5. Collision controls and exact premise distinctions

The first two controls below are analytically screened at their **actual events** using the displayed local laws and inherited preparations. Their certificates are not numerically rerun. No floating test or automatic “passed control screen” is claimed.

| Control | What is shared / what happens | Failed theta premise or remaining qualification |
| --- | --- | --- |
| Gaussian-polynomial source Φ*=(64u⁴+6)e^{−(4+1/4)u²}, event (1/4,2√6), [Note28 §8][gaussian] | H*(1/4,A)=√π(A²/4−6)²e^{−A²/16}/16, hence a nondegenerate double. Unit preparation, fixed c, and all three collision signatures apply on nearby compact T<17/4. In this normalization b=(3√π/4)e^{−3/2}>0. | Fails the complete arithmetic square-source/Poisson-product premise (7). Evenness, smoothness, finite moments, positive source and a positive rescaled primitive are shared and cannot exclude it. |
| Three-positive-square source, event T=1/4, A*∈(44.1303,44.1304), [R16 §5][squares] | Inherited certified nondegenerate double; same unit preparation and finite moments. It has the negative C01 predecessor pole, the C02 late-time response divergence, and C03 index −1. Its kernel B_s is the same source-independent kernel. | Fails unit theta coefficients and full source reflection. Square support, positive weights, carrier domination and the first reflection endpoint remain shared. Its event is not claimed to be an all-real threshold. |
| Four-square / finite-prime controls in [the register][controls] | Additional finitely many endpoint or prime identities do not distinguish them; use only their recorded events and moment domains. | Full normalized theta reflection/product relation fails in the recorded classes. No common event mark or uniform extension is asserted. |
| Reflected super-Gaussian control, event (1/4,π/4), [register][controls] | Positive even source and a nondegenerate event share the local signature; preparation has the required moments near the event. | Fails the integer-square arithmetic representation. Full reflection or positive Fourier–Gram forms alone are insufficient. |
| Smooth shape / positive-primitive, Euler-factor and finite-profile controls, [register][controls] | Screen any proposal consuming only those families' recorded shape, endpoint, finite-measurement or deformation properties. | Preserve each family's distinct failed arithmetic, reflection, growth or threshold premise. No universal control with all properties is asserted. |
| Fixed theta amplitude with polynomial observation, [Note51][variable] | Important screen against using the amplitude identity alone. | Fails the literal cosine oscillator/Newman relation. It is outside the physical-cosine C01–C03 class; it is not a theta collision. |

The admitted controls **fail (4) and (8)** and have nonzero local degree; they do not fail generic flow regularity. No proposed theta *inequality* has yet been proved or shown to discriminate them. Merely observing that they fail a literal theta identity does not pay the inequality derived from it.

## 6. Disposition and bounded continuation

**FCG-C01 R1 retained provisionally for one source test; C02 and C03 inactive.** C01's signature and source representation are derived above; its source restriction remains a candidate, its absolute limit transfer is inherited/checked at the stated level, and its relative signed propagation is open. This completes B01's selection boundary.

**Next: [B] FCG-B02 — Astra.** Decide whether the complete parity–Poisson product can supply one signed estimate for (5) with a finite locally uniform energy coefficient, or a propagation mechanism whose limit pays that same estimate. At most two source connections may be compared; the optional second is the complete primitive transfer (9), not a new source. Use B₀ and the constant limiting kernel as early structural checks. Keep every error relative to the actual energy consumer and preserve the direct comparator. If a fixed method and acceptance test emerge, issue FCG-E01/Sol immediately. If the only surviving argument assumes the jet floor or restates L+CE_J≥0, return a scoped obstruction to B03. No numerical implementation or broad scan is authorized by this return.

The [continuation note](02_CONTINUATION_FCG_B02_20261030.md) supplies model-change guidance. [Progress06][progress] alone owns live status. This selection is not an assessed research milestone; result summaries and manuscript history are not upgraded.

[overview]: ../../research-overview/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_OVERVIEW_20261030.md
[progress]: ../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md
[fixed]: ../CHAT0042_FIXED_COMPRESSION_AND_NORMALIZATION_COMPARISON_20261030.md
[family]: ../CHAT0042_FIXED_FLOW_PARAMETER_FAMILY_AND_COLLISION_INDEX_20261030.md
[primitive]: ../73_BOOK_INTEGRATION_BY_PARTS_AND_FEEDBACK_PAIRINGS_20261029.md
[tests]: ../75_PRIMITIVE_TEST_COSTS_AND_SIGNED_COMPARISON_R11_20261029.md
[gaussian]: ../28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[squares]: ../101_MASS_FREE_FEEDBACK_DEFECT_AND_SLOPE_CLOSURE_TEST_R16_20261029.md
[variable]: ../51_ZERO_RAW_MISMATCH_KERNEL_FREEDOM_B02_R6_20261029.md
[poisson]: ../../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/38_POISSON_PARITY_CORRELATION_AND_HEAT_OBSTRUCTION_20261015.md
[localized]: ../../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/42_LOCALIZED_POISSON_MODE_OBSTRUCTIONS_20261015.md
[results]: ../../../../../result-summaries/README.md
[geometry]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a14]: ../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
