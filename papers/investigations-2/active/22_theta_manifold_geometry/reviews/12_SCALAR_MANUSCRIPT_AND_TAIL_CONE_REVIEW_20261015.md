# Scalar manuscript integration and positive tail review

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata. These are internal mathematical and numerical assessments, not external refereeing or formal verification.

## Manuscript integration

The [revised manuscript](../manuscript/theta_manifold_geometry.tex) incorporates physical-jet Notes 02–03 and joint-current Note 09. It proves the complete local backward stationary-set classification and one analytic first-jet factor, records joint currents with all boundaries, combines their lower fluxes into one gauge-invariant trace, gives the exact signed quotient cost, and states scalar cone transfer with fixed-cone mixed-error exclusion. Its final arithmetic target is

\[
WB_\partial\le C W^2+\varepsilon|W|.
\]

All 40 pre-existing formal statements remain unchanged. The new results retain their assumptions: analyticity and the backward heat equation, finite collision multiplicity, a strictly positive prescribed cone width, nonnegative mixed errors, and the original endpoint-interval and uniform-error requirements. The analytic trace criterion explicitly uses its first nonzero coefficient. The polynomial source obstruction remains restricted to its declared pointwise finite-range real-frequency polynomial class. Gauge changes require the stated integrable weighted bounds and absolute upper-flux decay.

The source editor compiler and the PDF export compiler both succeeded. The 49-page reading copy was checked page by page; the contents entry that initially spilled onto the opening page of the text was repaired, and the final render was checked again. There are no remaining compiler warnings, unresolved references, duplicate labels, clipped equations or overlapping elements. The final [build record](../manuscript/BUILD_RECORD.json) identifies the source and PDF. Two relevant exact checkers were replayed: 3,803 joint-current assertions and 1,291 scalar/gauge assertions, totaling **5,094**; both receipts match their earlier records byte for byte. These finite identities do not replace the analytic proofs.

## Next phase analytic result

The separate [positive-tail note](../notes/03_theta_bundles_and_connections/10_POSITIVE_TAIL_CONE_AND_FINITE_BOX_CERTIFICATE_20261015.md) derives explicit \(O(n^{-4})\) rectangles for the complete normalized vectors \((H_n,H_{n,x})/\beta_n\), including their limit \((1/8,0)\). The closed convex hull of the union of the finite rectangles, the infinite-tail rectangle and the limit point encloses the normalized tail hull. Independent derivations checked the integration-by-parts identity and all signs. The primitive envelope \(p_ne^{Tu^2}/\beta_n\le e^{-d_nu}/d_n\), where \(d_n=4\pi n^2-1\), bounds every required moment. Convexity of \((1+z)^{-3/4}\) supplies the lower primitive mass.

Combining these inequalities proves

\[
-H_{n,x}/\beta_n>x/[40(4\pi n^2-1)^2]>0
\]

for every \(n\ge2\), \(0\le t\le1/2\), \(0<x\le30\). The rational threshold at \(d=47\) was checked exactly. The proof uses \(\cos(xu)\ge1-x^2u^2/2\) and \(|\sin(xu)|\le xu\), so it makes no assumption that the oscillatory integrand has one sign everywhere.

## Validated finite pilot

With the prescribed separator \((0,-1)\), the complete normalized tail has infimum zero at its included limit. The checker certifies a strictly negative first-mode derivative throughout \([0.009,0.011]\times[28.2,28.4]\). Hence the complete field cannot collide there, even for every convergent nonnegative tail with first coefficient one. Additional complete endpoint enclosures show exactly one theta zero in the spectral bracket for each time; no claim that it is globally the first zero is used.

The final [checker](../numerics/check_positive_tail_cone.py) passes **52 exact or validated assertions**, using 32 Arb/Acb integrals at 160 bits. Its source tail covers moments through order five. The two-parameter Taylor bound covers the whole box and uses the correct heat-time derivative and Hessian orders. Finite modes plus the explicit uniform infinite-mode rectangle cover the complete tail. An independent replay matches the mathematical receipt after removing exactly three runtime timing fields; the [manifest](../numerics/SCALAR_MANUSCRIPT_AND_TAIL_CONE_CHECKS_20261015.json) records those identities.

Both ordinary directional and coarser radial cutoff comparisons already pass using the same head enclosure. Thus this pilot demonstrates neither a computational advantage nor theta-specific arithmetic discrimination: positivity and the fixed first mode suffice for its sign. It supplies an oriented-tail lemma and a finite control certificate, while the all-event scalar boundary estimate remains open. The next step should use arithmetic coupling where this componentwise positive-mixture argument fails, rather than scale a cone optimization that this pilot does not require.
