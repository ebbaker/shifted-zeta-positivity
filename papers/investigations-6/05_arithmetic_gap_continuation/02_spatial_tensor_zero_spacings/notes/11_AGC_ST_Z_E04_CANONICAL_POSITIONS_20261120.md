# Predicting both canonical positions from the time-zero anchor

20 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex LLM assistance. AGC-ST-Z-E04 r1 execution dispatched as gpt-6.2-sol, effort ultra. Serving configuration has no separate attestation. Outward Arb computation on the declared finite slab, pending separate assessment. [Frozen request](../research-progress/handoffs/AGC_ST_Z_E04_REQUEST_R1_20261120.md) · [B03 choice](../brainstorm/notes/07_AGC_ST_Z_B03_CANONICAL_POSITION_TEST_20261120.md) · [Outward record](../numerics/02_AGC_ST_Z_E04_CANONICAL_POSITIONS_20261120.json)

The two marked roots and their center move left from \(t=0\) to physical \(T=10^{-4}\). The predicted endpoint widths are below \(2.094637\,10^{-12}\) and \(5.797961\,10^{-12}\) in Newman height, and the signed center displacement width is below \(3.946299\,10^{-12}\). These clear the three predeclared \(10^{-10}\) width gates. Both endpoint tangent defects and their center average are positive. Later direct terminal brackets have width \(2^{-54}\) each and lie strictly inside their respective predictions. The equally informed singleton transport has exactly the predictor widths, and the matched direct terminal solve is substantially narrower.

## Inputs and source allowance

The complete HDC wall and count identify two occurrences inside \([26,46]+i[-2,2]\) throughout the declared slab, with inherited full-field wall floor above \(4.94199065\,10^{-7}\) in its certificate normalization. The only refined positions used by the predictor are the accepted physical \(t=0\) E07 \(\texttt{F\_real\_brackets}\), inside \([28,29]\) and \([42,43]\), with widths below \(7.524\,10^{-37}\) each. Their certification and the HDC count together identify the positive real pair. The coarse intervals are also the starting points of the direct terminal comparison. The frozen input table binds the count and anchor records and their replay sources. It also binds the evaluator and coefficient generator code. The source constructor executes afresh in each executable phase and both copies have the same certified coefficient-interval digest. The digest is a provenance check. The signs and interval comparisons are decided by interval arithmetic. [HDC wall and count](../../../../investigations-4/12_height_dependent_heat_contours/numerics/07_COMPLETE_THETA_WALL_CERTIFICATE_20261023.json) · [Time-zero brackets](../../01_jacobi_integer_hierarchy/numerics/05_AGC_JH_E07_CERTIFICATE_20261119.json)

Use \(F(t,z)=H(t,z)/H(t,0)\) with the full theta field, \(s=t/T\), and \(w=z-36\). The generator encloses the coefficients through time order 10 and spatial powers 0 to 143 at 768 bits. The underlying tilt and the source normalization are paid on \(|t|\le1/20,\ |w|\le24\). The radius-15 replay evaluator charges the complete value tail on \(|t|\le T,\ |w|\le15\). Its time and spatial parts are below \(4.750\,10^{-29}\) and \(2.501\,10^{-28}\), with combined upper bound \(2.976\,10^{-28}\). The coefficient radii are carried through the polynomial evaluation, and their weighted sum at radius 15 is below \(3.101\,10^{-175}\). Each spatial derivative of order \(j=1,2,3,4\) pays \(j!\) times the analytic value tail by Cauchy's formula on a unit circle and is evaluated with its whole circle inside radius 15. The corresponding analytic allowances are below \(2.976\,10^{-28},\,5.951\,10^{-28},\,1.786\,10^{-27},\,7.141\,10^{-27}\). The evaluator also pays its fourth-order local polynomial Taylor remainder on each interval, using the absolute coefficient majorant of derivative order \(j+4\). The stored slope, velocity and acceleration intervals already include these errors. All spatial ratios used at roots are unchanged by the time-only normalization. [Complete source construction](../../01_jacobi_integer_hierarchy/numerics/e08_source.py) · [Complete radius-15 evaluator](../numerics/certify_st_e06.py)

## Prediction before terminal evaluations

Let \(X_i\) be the time-zero interval of the marked root \(i\in\{a,b\}\), increasing in height. On \(X_i+[-2T,2T]\) for the whole slab, the complete derivative bounds give \(|F_1|\) above \(0.00139053\) and \(0.0000178492\), respectively, where \(F_j=\partial_z^jF\). For \(|F_2/F_1|\) the upper bounds are \(0.579751\) and \(0.755200\), below 2. No repair was used. If a continuation first reached its box wall, its displacement from its own initial point would be at least \(2T\), whereas integrating the strict speed bound to that time pays less than \(2T\). The slope and real symmetry continue the simple branches on these intervals, and the two paths exhaust the HDC count.

With \(v_i=F_2/F_1\) at the root, use \(x_i''=-F_4/F_1+2v_iF_3/F_1-v_i^3\). On each corresponding path box, the saved acceleration enclosures include the weighted mean \(u_i=(2/T^2)\int_0^T(T-t)x_i''(t)\,dt\). The interval prediction is built from
\[
 y_i=x_i(0)+T\,v_i(0)+\frac{T^2}{2}u_i,\qquad
 (c(T),s(T))=\left(\frac{y_a+y_b}{2},\,\frac{y_b-y_a}{2}\right),\qquad
 D(T)=s(T)^2 .
\]
The anchor velocity is evaluated only on \(X_i\) at \(t=0\). The weights are exactly \(T=1/10000\) and \(T^2/2=1/200000000\). Reconstruction with the same variables gives \(c-s=y_a\) and \(c+s=y_b\). The center displacement keeps the initial anchors shared before subtraction. [Acceleration and first-exit proof](09_AGC_ST_Z_E02_CENTER_ACCELERATION_20261120.md) · [Correlated recovery proof](10_AGC_ST_Z_E03_ROOT_RECOVERY_20261120.md)

The table rounds enclosures outwards for display. Width bounds use the saved outward endpoints.

| Quantity at \(T\) | Outward enclosure | Width below |
| --- | --- | --- |
| \(a(T)\) | \([28.26939232043258545,\ 28.26939232043468010]\) | \(2.094637\,10^{-12}\) |
| \(b(T)\) | \([42.04400377806595431,\ 42.04400377807175228]\) | \(5.797961\,10^{-12}\) |
| \(c(T)\) | \([35.15669804924926988,\ 35.15669804925321619]\) | \(3.946299\,10^{-12}\) |
| \(s(T)\) | \([6.88730572881563711,\ 6.88730572881958341]\) | \(3.946299\,10^{-12}\) |
| \(D(T)\) | \([47.43498020217669427,\ 47.43498020223105301]\) | \(5.435874\,10^{-11}\) |
| \(a(T)-a(0)\) | \([-0.000057963036802122,\ -0.000057963034707484]\) | \(2.094637\,10^{-12}\) |
| \(b(T)-b(0)\) | \([-0.000075499477155669,\ -0.000075499471357707]\) | \(5.797961\,10^{-12}\) |
| \(c(T)-c(0)\) | \([-0.000066731256978895,\ -0.000066731253032596]\) | \(3.946299\,10^{-12}\) |

The lower and upper endpoint tangent defects are enclosed by \([2.0945666707,2.3040303415]10^{-11}\) and \([7.2648457778,7.8446418591]10^{-11}\). The center tangent defect lies in \([4.6797062242,5.0743361003]10^{-11}\). These strict signs use the full accelerations on the enclosed paths. Independently boxing \(c,D\) from the same positive half-gap projection gives both endpoints widths below \(7.892598\,10^{-12}\). Its loss is the other endpoint's width before serialization, as in E03. The older \(7.5\,10^{-9}\) center-displacement width used previously acquired full-slab root tubes. It is a separate benchmark with a different acquisition path. [Earlier acquired-tube comparison](../reviews/04_AGC_ST_FINITE_CURVATURE_ASSESSMENT_20261120.md#reproduction-and-comparison)

## Matched terminal comparison and replay

The predictor phase made 4 anchor derivative calls and 8 slab derivative calls at one source level. It made zero terminal value calls. It serialized its complete scientific prediction before a separate comparator process, which verified the saved prediction SHA-256 and regenerated the same bound source before doing any terminal evaluation. A fresh replay uses the commands below from this branch's numerics directory with python-flint available. Use fresh output paths.

    prediction_sha=$(python certify_st_z_e04.py predict --output /tmp/agc-st-z-e04-predict.json)
    python certify_st_z_e04.py compare \
      --prediction /tmp/agc-st-z-e04-predict.json \
      --prediction-sha256 "$prediction_sha" \
      --output /tmp/agc-st-z-e04-comparison.json

The recorded predictor digest is \(\texttt{a7bc5d89ca96650d0d7c58f54e71d09df34d39b6892c25cf9c5ab076ce9d640f}\). The comparator measured the endpoint signs afresh and bisected from each integer interval. There were 54 midpoint tests and two initial sign calls per root, 112 source value calls in all, with neither ambiguous signs nor exhausted budgets. The terminal intervals are enclosed by \([28.269392320433630039,\ 28.269392320433630095]\) and \([42.044003778068840537,\ 42.044003778068840594]\) for display. Their certified exact dyadic widths are \(2^{-54}<5.552\,10^{-17}\). Exact rational comparisons of the saved outward endpoints put each bracket strictly inside its prediction. Call counts distinguish derivative and value evaluations. The enclosure comparison makes no claim about equal runtime cost.

This is a verified finite position enclosure for the two specified roots of the complete source. The unchanged arithmetic source, count and first-exit slope inputs delimit the application. A genuine counted double fails the singleton slope premise and goes to the joint coefficient transfer in E03. Euler-factor controls can keep the real anchors while changing the complete analytic field and its jets, and the other catalogue cases fail the source or heat-law premises named in E01. [E01 premise screen](08_AGC_ST_Z_E01_ORIENTED_TRACE_20261120.md#source-screen-and-the-input-for-a-time-bound) · [Results index](../../../../../result-summaries/README.md) · [Collision catalogue](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Patterns index](../../../../../avoid/README.md) · [Target classification](../../../../../avoid/01_restating_the_target.md) · [Scope rule](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
