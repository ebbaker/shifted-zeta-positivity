# Cluster resolution and heat-collision assessment

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex LLM assistance. Actual model and reasoning effort unavailable.
Same assistant as the derivation; no independent specialist review.

**Status: same-assistant analytical check completed within the stated scope.**
Scope: manuscript §5.3 clarification and §10.4, Propositions 10.4–10.6;
see [discussion27](../notes/27_VCD_CLUSTER_RESOLUTION_AND_HEAT_COLLISIONS_20261116.md).

1. Uniform-in-time convergence: positivity gives Z_λ≥Z_(λ−), and the
   numerator moment is bounded at λ+. The resulting fixed endpoint
   cosh series is summable. No interchange of a moving-domain limit
   or unproved heat equation for G_(N,λ) is used.
2. Cluster coordinates: the residues give power sums with multiplicity.
   The center and D are symmetric, so labels are immaterial. Real-centered
   disks and real reflection make the two possible root configurations
   exactly a real pair or a conjugate pair, including a real double root.
3. Error estimate: the logarithm exists on a collar of the contour since
   the relative boundary error is strictly below one. Its power-series
   bound is −log(1−t), not t without a remainder. Integration by parts
   gives k ρ^k b. The two-root bound |p_1|≤2ρ gives |D_N−D|≤2ρ² b.
   The finite-data alternative uses log(F/G_N) and a known two-zero
   model count; it does not infer a limiting margin from error alone.
4. Heat normalization and sign: F_λ=−F_zz−m_2 F. At the double event
   F=(z−a)² A, the residue of (z−a)F_zz/F is 2, giving p_2'=4 and
   D'=2. The scalar normalization term has zero contour integral.
   The sign agrees with (z−a)²−2(λ−λ*), and reverses with τ=1/2−λ.
5. Event approximation: D'≥κ gives a local lower slope for D, which
   stays nonsingular at the collision. Uniform D_N convergence and
   opposite endpoint signs give at least one approximating double
   event. All such events in the chosen interval obey d_N/κ; neither
   uniqueness nor a global threshold is claimed. The unresolved band
   gives 2d_N/κ and spatial separation at most 2 sqrt(2d_N).
6. Scope/control screen: generic colliding heat fields share the local
   law. These results describe approximation of a stipulated fixed
   double event, not its existence or exclusion for theta. Higher
   multiplicities, growing regions and canonical margins remain open.

The classical source-polynomial phase is explicitly identified as counting
q_N zeros rather than F zeros. The physical contour count uses F directly.
The Rodgers–Tao citation retains its PDF numbering and stated simple-real
time range; no singular individual-root ODE is applied at collision.

The [build record14](../numerics/14_VCD_CLUSTER_RESOLUTION_MANUSCRIPT_BUILD_20261116.json)
records reference resolution and PDF inspection. No numerical experiment
or numerical premise was introduced. B07 remains unactivated/E25 unissued.
