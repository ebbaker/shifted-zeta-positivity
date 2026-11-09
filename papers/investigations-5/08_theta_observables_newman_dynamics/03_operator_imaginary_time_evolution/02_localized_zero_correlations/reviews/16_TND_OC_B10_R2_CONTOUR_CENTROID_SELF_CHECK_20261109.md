# B10 r2 contour-centroid theorem: proof-author self-check

9 November 2026, America/New_York. Prepared for Edward Baker with
substantial OpenAI Codex assistance, OC chat0009. Recorded current thread
settings gpt-6-astra/max; per-turn backend configuration unavailable.
Same proof author, no delegation, independent assessment or specialist review.

**Disposition:** [Note20](../notes/20_TND_OC_B10_R2_CONTOUR_CENTROIDS_AND_GAUSSIAN_ESTIMATE_20261109.md) retained as **proved
in-note, proof-author checked**, with conditional numerical gates.
B10 r2 is complete at design/contract scope. E13 execution and all
canonical data remain unacquired.

| Check | Finding |
| --- | --- |
| Added information | Counts plus first complex moments yield exact unweighted centroids. The latter cancel both real linear Taylor components, including when internal zeros are complex or multiple. B07's counting method is credited. |
| Complete source | In the fixed high-real-coordinate rectangle, zeta(s(z)) and H0 differ by a nonzero holomorphic factor. Their contour counts and weighted first residues agree. No pole, trivial zero or spurious completion zero is enclosed. |
| Global tail | Positive complete theta source gives M<7 and H0(0)>1/7290. Jensen gives the global disk and slab counts. Shells for x beyond [988,2012] start at distance 12 for every allowed center. The explicit weight tail is <2^-44; pair tail is <2^-32 when the complete count N≤1024. |
| Kernel | Note19's gap coefficients 1/4 and 4/9 sum to 25/36; both transverse factors and finite erf edges remain. The self factor is e^(-4/17-16y²/17), with coefficient n_C. |
| Derivatives | Gaussian factor derivatives give K gradient components 6/T,3/T and Hessian entries 12/T,6/T,3/T. Diagonal bounds give Hessian entries 8/T,2/T,4/T. The row-sum operator bounds 18/T and 10/T are valid globally. |
| Cluster transport | Each raw-variable replacement costs 9NS2/T; self replacement costs 5S2/T. Approximate centroids add (18N²+4N)sigma/T. No extra mixed moment or hidden minimum gap enters. |
| Moments and quadrature | Centered residue integral is exact. The midpoint error is L³ sup|G''|/24 for complex straight segments. Cubic Z series suffice for G''; whole-segment denominator nonvanishing and all arithmetic radii remain mandatory. |
| Numeric comparison | Exact-rational bookkeeping verifies analytic error <1/400 at r=2^-12, sigma=2^-24, N≤1024, T=1000. Adding a certified 1/400 arithmetic radius gives <1/200. This is not an observed canonical enclosure. |
| Scope and caps | The new packet has one fixed method, three precisions, finite subdivision/evaluation limits and an external 30-minute cap. The real count and all moments may fail those gates. No actual cost advantage, universal availability or correlation asymptotic is claimed. |
| Controls | Generic contour/Taylor methods accommodate double and complex pairs. Only actual source evaluations can supply a canonical value; passing the generic lemma is not collision exclusion. |

The [exact record](../numerics/16_TND_OC_B10_R2_EXACT_CONSTANTS_20261109.json)
checks constant arithmetic, not analytic premises. The default interpreter
preflight found no flint/mpmath/sympy; no canonical numerical experiment
was run. A distinct fixed proof check is included before E13 computation.

One analytical mechanism and one author check were used. No manuscript
or root result-summary promotion. [Continuation23](../continuation-notes/23_TND_OC_AFTER_B10_R2_CLUSTER_MOMENTS_AND_MODEL_CHANGE_20261109.md)
recommends Sol for the fixed execution rather than more conceptual work.

