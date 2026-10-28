# Assessment of the tube comparison and projected flow

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, chat0008. **Same-assistant internal assessment; not independent specialist review.**

The return comprises [Note22](../notes/22_STEERED_TUBE_GREEN_IDENTITY_AND_MATCHED_COMPARISON_20261027.md), [Note23](../notes/23_PROJECTED_ANNULAR_FLOW_RESPONSE_AND_LOCAL_ADJOINT_20261027.md), [reference annotation10](../references/10_PROJECTED_EVOLUTION_AND_ELLIPTIC_RESPONSE_20261027.md), and [check record14](../numerics/14_TUBE_AND_PROJECTED_FLOW_CHECKS_20261027.json). It completes the tested LOC-02 comparison and establishes the bounded LOC-03 prototype with an explicit exterior response. No theta collision is excluded.

## Tube calculation

The x=log r conversion was checked separately: ψ∂rζ−ζ∂rψ=r⁻²W, the divergence density is r⁻³K, and multiplication by r²dr gives K dx. The normalized angular convention is dΩ/(4π). The induced weight A⁻² cancels the profile in both the current and volume. In ordinary measure the same cap factor multiplies K and both face currents.

The outward side normal is −∇q/|∇q|. Direct surface parametrization agrees with dS=r²|∇q|dr dφ. The side flux is generally nonzero pointwise, but its signed angular integral vanishes at fixed cap width because n_r·n=0. The ordinary drift vanishes by the same rotational symmetry. The complete scalar potential, including n_rr, cancels in the polarized identity; it remains in the first Green identity. No steering term was silently dropped. At variable width the additional side term is +(1/2)∫A(c)²Wc' dr and need not vanish.

The comparison is stronger than recovery of H: the signed bulk, absolute bulk, each of its two radial summands, and matched radial-tail allowances all receive the same positive coefficient. Independent absolute lateral/drift bounds add cost. This conclusion is restricted to this current, the common multiplicative response, an axisymmetric profile depending on r only through its axis, constant angular width, and matched source information. It does not close other local signed estimates or deformations.

The full radial assembly includes both omitted intervals and the physical boundary at r=1. The artificial face currents are not zero at an event. The moment-tail bounds in Note22 follow directly from the sine kernel and its fixed-source λ derivative. The exact Gaussian-polynomial control has W=8xe⁻²ˣ² and K=8(4x²−1)e⁻²ˣ²: its collision coexists with strictly positive W at every artificial face x>0.

## Bounded evolution and exterior realization

The projected multiplication Πχ is self-adjoint only after restriction to the zero-average Hilbert space; Note23 makes that restriction. The projected Dirichlet Laplacian preserves the same space. The radial substitution rv and the first nonzero spherical eigenvalue give the stated coercivity constant γ. The semigroup formula gives the graph-continuous strong solution, its unique equilibrium, and exponential convergence. Expanding the quadratic energy checks the sign and factor1/2 in its exact decrease.

The strict source-cost decrease follows from total energy decrease and nonnegativity of the gradient penalty. It is not a monotonicity claim for the source term by itself. The variational lower bound requires a trial function in H¹₀; an interior bump times h supplies one even when h has nonzero boundary trace. No positivity of the evolved source is claimed.

Initial boundary compatibility is distinguished from positive auxiliary-time smoothing. Zero extension has the distributional Laplacian J_DΔG−(∂_NG)δ∂D; a global parabolic equation would need its compensating surface term. The response avoids this issue by solving one coercive exterior elliptic equation with the extended source itself. Its μ² term gives coercivity on the unbounded domain. Only local exterior H²/H³ regularity, including boundary collars and artificial joins, is asserted; the bounded-domain regularity theorem is not silently applied as a global exterior estimate.

The operator Δ+VP−μ²Π has the original radial channel and a separately selected zero-average channel. Its nonlocal angular projection is explicitly stated. The averaged physical boundary and all spectral observations are preserved. They need not vanish pointwise at an event: the zero-average response can have a nonzero angular normal derivative. Since the source flow is independent of running λ, ∂λf=ζ and ∂λL=r⁻²P. Replacing the differentiated forcing by −f/r² would be an error.

## Signed functional and adjoint

Re-expanding fΔζ−ζΔf gives the extra local term (V+μ²)ζU. It cancels only after a complete spherical average. Self-adjointness of the coercive inverse and the minus sign in δU=−K_μ⁻¹J_DδG give the adjoint formula in Note23(23). The final Π implements the zero-average constraint. The cutoff identity retains ∇η·j; a tube indicator retains its actual flux. Whole radial tests and physical B,B_λ have zero variation. The sharp energy-ball range is a Hilbert-space Cauchy–Schwarz statement, not a theta estimate.

The derivative −⟨k_η,e⁻ˢᴬh⟩ identifies what the source energy dissipation fails to sign. This is a concrete next comparison; a strict localization gain alone is compatible with a colliding source. The auxiliary evolution and the new current supply no physical exclusion without a further canonical estimate and complete complementary allowances.

## Verification and disposition

The checker uses exact integer polynomial arithmetic for the control ODEs, W, K, and boundary data. Its separate floating checks evaluate the conjugated Cartesian operator from finite differences of the actual fields, integrate normals from a direct surface parametrization, and differentiate a manufactured additive-response current. They are not interval certificates or a simulation of the projected PDE.

At the smaller Cartesian step, the maximum scaled conjugated-operator residual is about 7.4×10⁻⁹; halving the larger step reduces the residual consistently with the fourth-order stencil. Tube balance residuals are below 1.3×10⁻¹⁴ for the tested quadratures. The variable-width control has lateral flux about0.310; dropping it fails the balance. The additive-current residual is about9.6×10⁻¹² at the smaller step, while omitting its projected-potential term changes the scaled balance by about0.416. These figures describe sampled diagnostics only. The unsigned side integral at fixed width is nonzero; its displayed quadrature values are not certified enclosures.

All exact checks and specified diagnostic tolerances passed. Standard analytic inputs were checked in author-hosted sources and their public PDFs archived outside Git. New files are small. The working manuscript is unchanged and was not rebuilt. Existing pending program edits and prior chat identities are preserved; chat0008 has its own unique registration.

The generic theorems accept the smooth Gaussian, Euler-factor, weighted-square, finite-prime, reflected, shape and primitive controls on their stated domains. The missing canonical premises are listed in the notes; no control is said to fail a nonexistent separating estimate. Atomic and conditional controls retain their scope qualifications. Existing collision certificates were not rerun.

**Disposition:** retain the fixed-width multiplicative comparison as a completed scoped limitation, and retain the bounded projected evolution, strict source-cost reduction, complete weak exterior response and signed adjoint as proved in-note. Proceed to the actual local signed comparison using canonical data. LOC-04 and the positive-threshold application remain open; no independent review or RH progress claim is supplied by these diagnostics.
