# Independent contributing-agent check of HDC Note 08

23 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Separate same-model contributing-agent mathematical review; not specialist or cross-model review.

Reviewed HDC Note 08, **Curved common-time transport, wall stability and height-graph corrections**, against its written formulas. No blocking mathematical issue found in the checked finite statements. The claimed theta application data remain explicitly unpaid.

The following potentially delicate details were checked directly:

- The moving-wall power-sum derivative has the positive sign shown in (2.1), because the integration-by-parts minus sign cancels the heat-equation minus sign. The normalized version (2.4) has the correct single factor `1/r` in its contour term and both coordinate-motion corrections.
- A relative-value wall error less than one gives a single-valued logarithm on a collar, without requiring its ratio to be holomorphic throughout the interior. This suffices for (3.2). The generating-function coefficient majorant (3.4) needs only the first N power-sum errors and remains valid at internal collisions.
- Each coefficient error occurs in N−1 polynomial rows and N derivative rows of the Sylvester matrix, with derivative multiplier N−j. This verifies (4.2). The determinant Lipschitz bound remains valid at a singular intermediate matrix.
- The complex edge-weight error (5.3) follows from the exact reciprocal-square difference; symmetry makes the absolute row and column norm bounds agree. The resolvent identity gives both denominator factors in (5.5). The whole-cluster wall does not provide those factors by itself.
- For the graph, `d(z^k dF/F) = -2ik z^(k−1)(F_bar/F) dA`. Removing small disks and orienting the inner boundaries therefore gives the **positive** area-correction sign in (6.5). Transversality makes the local area integrand integrable. The Jacobian in (6.4) equals `|H_z|²(1−h' Re v)`; its negative-orientation and tangency controls have the stated signs.
- The branch map `u -> h(Re z_i(u))` maps the full closed interval into itself under the stated domain hypothesis. Its derivative bound is (7.1), so contraction gives one and only one graph intersection per branch and the error factor `1/(1−kappa_i)` in (7.2). Simplicity at each common time alone does not give this contraction; the note correctly keeps it as an additional assumption.

The distinction between smooth prepared-coefficient transport and singular root/resolvent reconstruction is maintained. The information comparison in Section 8 is restricted to an identical analytic error model and does not claim that all curved source estimates have equal quality. The physical-cap product retains its unit factor. These are essential scope conditions, not optional application details.

No numerical source wall, onset, resolvent floor, or growing-height estimate was independently certified in this review. The note appropriately states that it has obtained a conditional finite interface rather than a new theta simplicity bound.
