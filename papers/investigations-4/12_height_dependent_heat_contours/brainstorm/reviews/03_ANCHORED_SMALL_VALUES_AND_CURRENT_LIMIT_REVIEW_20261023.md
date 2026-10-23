# Internal review of anchored small values and exact current convergence

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. This record synthesizes a separate reviewing agent's audit, two contributing agents' derivations/checks, and the primary assistant's reconciliation. All used the same model. It is **not independent specialist review**, cross-model review, formal verification, or a numerical certificate.

Source: [Note 08][note], continuing [Note 07][previous] and the [OBF register][progress]. Read under the [result index][results], [control register][controls], and [avoid index][avoid]. The relevant scope rules are [target classification][a01], [same-model review][a05], [scoped claims][a07], and [coupled estimates][a12].

**Disposition: the stated finite analytical results are supported, conditional on the explicitly imported polynomial-root theorem.** The note proves fixed-field current convergence and a finite anchored source-dependent bound. The theta application supplies its anchor and upper source moments, but does not demonstrate a useful high-height allowance. The earlier nonreal population, improved backward width, and global conclusions remain unproved.

## Mathematical checks

1. **Exact transported field.** For f=H/B the numerator is −f_t=\mathcal T_Bf, including both the carrier drift and zeroth-order term. At a shifted level f=w its velocity is −f_t/f_z. Replacing this with f_zz/f_z would be wrong for general B. The note retains the full field throughout.

2. **Area formula.** The spatial Jacobian |f_z|² cancels the corresponding factor in the product-weighted density. This gives the target-plane integrals in (4), with regular preimages and almost-everywhere qualifications. Critical points have zero original product density. Fubini handles exceptional (t,w) pairs; the proof does not divide at persistent critical fibers or require every shifted family to have finitely many events.

3. **Imported regularity theorem.** The published [Parusiński–Rainer paper][pr], Theorem 1 (1.2), was checked. The allowed exponent is strictly below n/(n−1), and the coefficients must have C^{n−1,1} regularity. Normalization to the unit interval removes its displayed interval-size factor. The proposed p_N=1+1/(2N) works for every 2≤n≤N. Degree one is elementary. Equivalent coefficient-norm conventions are absorbed by the universal constant.

4. **Polynomial charts.** Uniform complex-time circle clearance fixes the degree of f−w and makes its symmetric root coefficients holomorphic in time and target. Root containment gives binomial coefficient bounds; Cauchy gives the displayed derivative/Lipschitz norm. No descendant root separation or H_z floor is used. Each chart has its own fixed degree; the proof sums estimates rather than putting a changing degree into an evolution equation.

5. **Time scaling.** The L¹ root path-length bound contains nR and no interval-length factor. Physical-time Lᵖ estimates used for uniform integrability must contain |J|^{1/p−1}; Note 08 (15) does. Short intervals therefore cannot be counted as free uniform Lᵖ control. The chart family is finite and all overlaps are paid.

6. **Finite cover.** Local isolating charts cover the compact zero set by interiors. Lowering the target radius below the positive minimum on the compact uncovered remainder makes them cover all small values on the weighted support. This existence argument is distinct from the acquired anchor bound. It requires the no-identically-zero-slice assumption and actual holomorphy in a complex time neighborhood.

7. **Anchor circle lemma.** Jensen bounds the strict-interior zero count by N. Removing the interior zeros with the finite disk Blaschke product leaves a zero-free interior factor bounded above by M and anchored below by m. Harnack gives the lower bound on the smaller disk. Radial avoidance removes no more than half of the allowed radius interval. Zeros on the factorization circle are harmless boundary zeros of the remaining factor. Multiplicities are included in N and in the product. An actual spatial anchor is present; it is not inferred from upper derivative budgets.

8. **Time extension of the circles.** For intervals of length at most ℓ and a collar of radius ℓ/2, every complex time is at distance at most ℓ from the interval midpoint. The derivative bound pays at most η/8. Subtracting the target allowance η/4 leaves at least 5η/8. The chosen ℓ also stays inside the original complex-time tube. The normalized Cauchy radius 1/4 is strictly smaller than the available 1/2 collar. Degree-zero charts contribute no level roots.

9. **Regulator limit.** Away from the finitely many zero-level multiple times, weighted root velocities converge by the implicit function theorem. Uniform Lᵖ control for p>1 supplies uniform integrability across those times. The support boundary is harmless because ∇ψ extends continuously by zero. The resulting essential target-plane limit is enough for the approximate identity. The far-target tail is paid by the finite total weighted product mass. This supports equality in (17), strengthening Note 07's Fatou-only inequality at the stated fixed-field scope. The same argument identifies the limiting quadratic coefficient of W(r).

10. **Complete theta source.** Positivity gives the uniform anchor at zero on [−ε,0]. The complete source integrals in (19) bound the field and its time derivative throughout the larger complex-time/spatial domain. Super-exponential decay pays their convergence. Formula (20) follows by retaining the n=1 source term on [0,1/10], including its full exponential damping. Formula (21) is a direct complex Taylor remainder, not an unsupported continuation of a positive- or negative-real-time error theorem. No high-height efficiency is implied by these absolute estimates.

11. **Collision check.** For the quadratic control the summed level-root speed is 2/|2t+w|^{1/2}. The substitution u=2t+Re w gives the bound 4√ε, including an interval crossing the singularity. Thus the weighted sublevel estimate allows a real collision. The cubic still supplies the inherited sharp factor 3/2; the new bound does not alter the endpoint multiplicity argument.

12. **Near-real improvement.** For a real heat event, real type and the square-root analytic parametrization give x even and y odd in q=√(t_e−t). A y-even C² window therefore cancels the singular vertical velocity, so the directional window derivative is bounded. The omitted strip lasts at most 4δ²/c_e² per incoming branch. This supports (23), with explicit local constants and the stated clearance condition. It does not improve the absolute-speed functional's strip cost to O(δ²), and it does not remove the strip at finite δ.

## Scope corrections retained in the final statement

- The bound is for smooth positive variation, not sharp-wall gross entry. The all-root estimate still overpays real trajectories. A drifting real-root example can have zero nonreal inflow and nonzero all-root current.
- Auxiliary local circle margins are lower information. They permit physical-window crossings and can vary between short time intervals, but they are not a free disappearance of boundary conditioning. The anchor theorem acquires them at an explicit cost.
- The universal C(n,p) is not numerically supplied here. The note gives a finite analytic source-dependent allowance with declared dependence, **not a certified numerical allowance**.
- Current convergence is fixed-field and has no acquired rate. It does not justify using one finite regulator without a bias error, or keeping a fixed approximation error as ρ→0.
- Scaling f by c scales m,M,T,η and r₀ by |c| while leaving the anchored path-length allowance unchanged. Its regulator threshold shrinks. This matches, rather than contradicts, Note 07's amplitude counterexample.
- The registered positive-source controls can share the anchor and upper moments. They are not rejected by this generic finite theorem. Their failures of the unchanged theta arithmetic are recorded separately; no unproved theta-sized quantitative separation is assigned to them.
- The source-at-zero construction can become extremely expensive when the buffer lies at large height. A useful carrier-normalized local source bound is still missing. No claim about the optimal possible estimate or a universal obstruction is made.

## Status recommendation

Record the structural regulator-removal part of OBF-02 as proved at the finite analytic scope, with an anchored quantitative small-value theorem. Record OBF-03 as partial: a coarse finite complete-source allowance is obtained, but useful band/growing-height size is open. OBF-04, OBF-05 and OBF-06 do not advance. Preserve Note 07 and its earlier review as the historical opening record, adding a forward pointer rather than rewriting their original claims.

No numerical experiment was needed to decide this analytical step. The next research target is quantitative economy from genuinely local normalized source data or a sharper directional estimate, with its required size specified by the intended consumer in advance.

[note]: ../notes/08_ANCHORED_SMALL_VALUES_AND_EXACT_CURRENT_LIMIT_20261023.md
[previous]: ../notes/07_NONREAL_WINDOW_TRANSPORT_AND_REGULARIZED_CURRENT_20261023.md
[progress]: ../research-progress/01_OPEN_BOUNDARY_FLUX_PROGRESS_20261023.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a05]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[pr]: https://math.univ-cotedazur.fr/~parus/publis/ens.pdf
