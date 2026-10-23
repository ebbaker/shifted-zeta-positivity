# Internal review of finite tubes, canonical late caps and complete closures

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**, verified from the active parent-turn metadata.

**Verdict: accept Notes 01–04 as proved in-note within their explicit conditional and fixed-finite-rank scopes. No strict complete-charge exclusion bound is proved.** Three contributing agents cross-checked notes they did not primarily draft, and the parent agent checked the derivations and integration. All used the same model and shared the project assumptions. This is internal LLM review, not independent specialist mathematical validation. No numerical theta certificate, literature-priority claim or formal proof verification is asserted.

The reviewed final claims are [finite and growing-interval geometry][n1], [complete-source complex-time caps][n2], [fixed-rank pair cancellation][n3], and [complete closure concentration][n4]. The actual differentiated-saddle proof was read, including its full source density and tail bounds; the review did not infer complex estimates from a real-axis clock limit. Apply the [result index][results], [avoid index][avoid], [collision controls][controls], [scope rule][scope] and [coupled-error discipline][coupled].

## 1. Boundary construction and continuation

Note 01 names RH and a hypothetical endpoint event separately. RH supplies simplicity at positive real times. Fixed-rank continuation and compactness prove the finite minima of derivative magnitude and pair gap positive; these are exact unacquired quantities, not numerical certificates or assumptions of endpoint simplicity. The complete M_1,M_2,M_3 moments bound all derivatives used on the stated region.

The sufficient constants check explicitly: the Rouché remainder on the radius-rho/2 circle is at most (1+4+9)m rho/64=14m rho/64<m rho/2. On the larger disk, |H_z-A_j|<=3m/16 and |(H-qH_z)_z-A_j|<=13m/64 give the claimed floors 13m/16 and 51m/64. Strict containment and uniqueness patch the local inverses holomorphically. The inverse derivative Z_q=H_z/(H_z-qH_zz) is nonzero, distinct q values cannot coincide spatially, and the disks are disjoint and attach strictly inside the local core.

Every face is present: early and late caps, the joining complement, local outer wall, projective sides, and local/tube imaginary-time faces. The ambient orientation dt ds dx dy gives the late sign +, top-imaginary sign −, and bottom-imaginary sign +. Reentrant gluing is handled on piecewise smooth pieces; common attachment disks cancel with opposite orientations. A rounded replacement must retain its collar. No normalization is attempted at the interior joint zero.

The higher finite-multiplicity core uses Weierstrass preparation, an analytic discriminant not identically zero, and the inherited charge binom(m,2). It does not reuse the ordinary-double critical-point chart or its quantitative constants. Evenness reduces negative real heights; H(t,0)>0 excludes zero height in the canonical application. Every individual candidate has a finite set of ranks. No uniform bound in height, multiplicity or growing rank is claimed.

The new fixed-width continuation in Note 01 §7 also checks. The late source theorem holds for all real t beyond a sufficiently large threshold, on a fixed bounded imaginary strip. Freezing epsilon_T=r_0/L_T on the entire finite interval gives epsilon_T L_t<=r_0 because L_t increases. The compact initial segment supplies a positive common width and radius; its inverses agree with the late ones by uniqueness and the identity theorem. This creates no unestimated transition wall. It is a family of finite tubes of decreasing radius, not one tapered infinite side to which zero curvature could incorrectly be assigned.

## 2. Complete source, physical jet and integrated cap error

Note 02 retains every theta index in b(u), the near/right Gaussian tail, the entire far-left interval, the exponential complex-spatial weight, and a positive explicit normalization lower bound N_T. Its weighted source moments W_k are complete. The B_j decomposition first removes R^j−1, then spatial displacement, then common phase; it therefore needs only W_1,W_2,W_3, without omitted higher moments. The exact equations F_eta=−iF_2 and (F_1)_eta=−iF_3 preserve the backward-heat sign.

The physical jet is A_T(F,L F_1). Both the L in its derivative component and the common phase e^{i eta} remain. The Rouché lower bound sqrt(1−r_1^2)(2rho−sinh rho), the reference inverse w=s_j+arctan v, and the separate F_1 floor are valid. The actual cap is an embedded regular inverse disk; the raw equation containing joint zeros is not treated as its boundary contract. Its forward Jacobian is L^−4|w_v|^2, with the correct imaginary-time scaling.

The near-one logarithm controls the full normalized jet and all three first tangential derivatives. The spare v radius pays its Cauchy derivative. The heat derivative identities retain F_2+F_0 and F_3+F_1 together, and the denominator (1+v^2)F_1−v(F_2+F_0) has the claimed lower bound. Bounds are explicitly in eta,v coordinates; physical s derivatives carry L^2.

Radial harmonic averaging gives the exact physical cap flux gamma/(2pi) times the continuously lifted phase increment of H_z at the central root. The reference is gamma S_T/pi, not zero. At that root,

\[
 \partial_\eta\log F_1-i=-i(F_3+F_1)/F_1+i(F_2/F_1)^2,
\]

which verifies the phase-rate error D. The complete integrated remainder is

\[
 |I-I^{\rm ref}|\le\gamma\min(S_TD,b)/\pi.
\]

The endpoint alternative uses the same near-one logarithm at both endpoints and cannot lose phase windings. It is uniform when radius or width tends to zero. Substitution S(T)=Y_max L_T^2 in the finite bounds, rather than their fixed-S big-O statement, proves B_j=O(L_T/sqrt(kappa_T)). Thus fixed-width actual theta caps tend to r_0^2Y/pi, with error O(L_T^−2+1/(L_T sqrt(kappa_T))). Both the vanishing shrinking-width regime and the nonzero fixed-width regime are proved; neither estimates a growing population.

## 3. Complete closure and optional pair route

For Note 04 the Hopf form has radial comass at most D^3/(2pi^2 b^3). The two fixed-time faces have total measure 4pi R^2Y and the local spatial wall has measure 4pi R(d+t_0)Y, exactly giving the stated B. Deleting attachment disks decreases that area bound. Simultaneous conjugation of tau and z preserves ambient orientation and C, so the two outward imaginary-face integrals are equal. Degree q then gives |J_±−q/2|<=BY/2 on the local core.

The exact tube top and bottom contributions are each gamma/(2pi)[theta(t_0,Y)−theta(T,Y)]. The factors for two or m tubes check. In the shrinking-width family, all other contributions vanish and the two full imaginary faces tend to q/2. At fixed Y, the signed local remainder R_0 includes the FULL initial attachment level, while the exposed joining sum is R_0−I_b. Thus each complete imaginary face equals (q−R_0)/2+(I_b−I_T)/2. This proves the nonzero-cap cancellation and every limit in Note 04, with the stated error and no dropped closure. These are conditional charge-allocation theorems, not theta exclusion.

Note 03's finite pair constants also check. For m fixed adjacent ranks,

\[
 \Delta'/\Delta=-2m(m-1)/\kappa+O(\kappa^{-5/4}),\qquad
 8\sum_{i<j}(x_i-x_j)^{-2}\sim(8A_m/\pi^2)L^2.
\]

The exterior unit cancels the positive order-L^2 term to the negative order-1/kappa remainder. The finite error follows from established root velocities, not differentiation of a location remainder. The conditioning statement is correctly restricted to independent symmetric perturbations about the exact two terms; it is not a necessary width condition for all possible one-sided enclosures. No growing-population uniform integrability or complex-cap bridge is claimed. The direct source route bypasses it.

The quadratic inverse z=q±sqrt(q^2+2tau), its two-cap value gamma arctan(Y/T)/pi, and its backward disk pinch at tau=epsilon^2/2 have the correct factors. The pinch concerns fiberwise univalent disks; q_tau remains nonzero there, so the note does not wrongly declare the entire projective level hypersurface singular.

## 4. Corrections, controls and disposition

Review prompted three refinements before acceptance: a definable least-admissible-integer terminal replaces an uncomputed “permanent onset” description; the pair conditioning conclusion is restricted to its actual error interface; and the complete gluing is described as piecewise smooth with retained reentrant attachments. The fixed-width extension and its stronger endpoint allowance received subsequent cross-checks, so the final review includes them.

The quadratic double retains charge one; the cosine cap retains common phase and can be nonzero with simple clock roots; the projective shell retains its inner closure. The broader register's Euler-factor, weighted-square, finite-prime, reflected, primitive and close endpoint controls retain their distinct arithmetic/reflection failures. No new late statistical theorem is assigned to a control. The geometric identities are generic, and close endpoint controls can share analogous source concentration; the actual theta cap theorem is not advertised as an arithmetic discriminator.

Accept LHCT-01–03 for the stated finite-rank geometries and both width regimes. Record the proved finite-rank statistic under the optional LHCT-04 route, without claiming its missing statistical-to-cap bridge. LHCT-05 has a complete closure allocation and a scoped failure of the selected exclusion payment; the requested opposing signed estimate remains unpaid. LHCT-06 and the exclusion portion of LHCT-07 remain open. The finite-height/multiplicity geometric corollary is not simplicity coverage. LHCT-08 is satisfied for this package and remains an ongoing requirement.

No additional numerical campaign is needed for these analytic results. The next missing mathematical input is a theta-specific complete signed estimate that conflicts with the retained conditional charge, or a new fully paid boundary construction with such an estimate. More precise late-root sampling does not supply it by itself.

[n1]: ../notes/01_FINITE_PROJECTIVE_TUBES_AND_COMPLETE_ATTACHMENTS_20261022.md
[n2]: ../notes/02_COMPLEX_TIME_THETA_JETS_AND_LATE_CAPS_20261022.md
[n3]: ../notes/03_FIXED_RANK_PAIR_CANCELLATION_AND_TUBE_CONTROLS_20261022.md
[n4]: ../notes/04_IMAGINARY_TIME_CLOSURE_CONCENTRATION_20261022.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[coupled]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

Repository integration checks: local Markdown destinations in this home resolve, reference keys are unique, all saved files stay below 1 MiB, and the repository whitespace check passes. These are document-integrity checks, not additional mathematical evidence. The source history is refreshed only through the registered capture tool.
