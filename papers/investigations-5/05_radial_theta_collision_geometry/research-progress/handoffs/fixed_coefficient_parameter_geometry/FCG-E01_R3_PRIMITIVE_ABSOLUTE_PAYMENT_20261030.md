# FCG-E01 R3: fixed lower-cost test of the primitive absolute payment

30 October 2026. Prepared for Edward Baker with substantial LLM assistance. Issuer gpt-6-astra / ultra, Investigation05 chat0049. **E — execution; recommended Sol**, because every formula, comparison and stopping rule is fixed. Parent B03 R6. Ready on issue; the author explicitly authorized independent Sol execution. Progress06 alone owns status.

## Frozen question

Using the parent note's equations (5)/(6), decide whether L_I > M_G^IBP at the unchanged center (1/4,64), outer radius R=1/32. The target is a necessary cost of absolute primitive payment, not an upper bound on G. No new source jets or full source quadrature are required. All h1,b and baseline M_G inputs must be decoded from the complete binary saved intervals at both existing precisions in E01 R2. Use rule C, fixed outer radius, whose M_G is common to its cases. Cross-check that common value across all rule-C rows.

## Fixed calculation and evidence

1. I=[1/32,1/4]; Q=(6u−8187u³/2+u⁵/4)sin(64u)+(384u²+64u⁴)cos(64u). Integrand exp(u+u²/4−pi exp(4u))|Q|. Use outward python-flint/Arb real interval panels, with pi enclosed by Arb. Do not use analytic Acb quadrature through absolute values.
2. Precisions exactly 256 and 384 bits. Uniform panel counts 256,512,1024; start 256 at each precision and refine only if L_lower > M_upper is not decided. Maximum 120 seconds total arithmetic work and 3584 range evaluations over both stages (sum of all allowed counts); no parameter/grid/search extension. No sampling can supply a bound.
3. On each panel evaluate the complete signed Q before abs; multiply positive exponent interval by abs(Q), times exact panel width, and sum. Preserve binary midpoint/radius intervals plus human-readable values. Report a certified integral enclosure, L_I enclosure, accepted M_G enclosure, difference, ratio if denominator is positive, and actual evaluated panel count/runtime at both precisions. The omitted positive primitive modes and outside-I contribution need no upper payment for this lower-bound witness; explain that distinction explicitly.
4. If comparison succeeds at both precisions, return certified domination of this class, and compute lower bounds for (L_lower−M_upper)T_N(r/R) for the existing radii 1/64,1/128,1/256 and N=1,2,4,8. These are margin-cost comparisons, not newly acquired physical margins. Check cross-precision overlaps for J_I and L_I; disjoint enclosures are an implementation failure.
5. If the cap is reached without deciding strict domination, return unresolved for this witness. Do not infer benefit or search a new interval. A detected formula error is a B03 return; routine parsing/rounding corrections stay in E.

No need to compute a complete primitive upper allowance, its upper tails, new direct/scalar/carrier inputs, or an energy floor: if domination holds, the matched direct/C01 consumers simply retain R5. No global covering or theta-zero claim follows.

## Permitted outputs and provenance

Write only `numerics/fixed_coefficient_parameter_geometry/execute_fcg_e01_r3.py`, `numerics/fixed_coefficient_parameter_geometry/fcg_e01_r3_primitive_absolute_payment_20261030.json`, and `notes/fixed_coefficient_parameter_geometry/E01_R3_PRIMITIVE_ABSOLUTE_PAYMENT_RETURN_20261030.md`. Do not modify frozen inputs, progress, history, manuscript, summary indexes or DRAFT_HISTORY. Parent is sole shared-file writer. Record actual model/effort from available metadata, tool versions, hashes, finite cases, true error enclosure, runtime and precise scope; one small record under 1 MiB. Use the existing `/private/tmp/hcb-endpoint-venv/bin/python` if available. No package installation is required.

Completion: a certified domination or unresolved return with runnable code, saved evidence and limitations; stop at this boundary. Next fixed task E02 R6/Sol will assess the issued proof and return; no larger numerical campaign is authorized.

## Frozen source identities

Hashes identify inputs, not mathematical validity.

| Repository-relative path | SHA-256 |
| --- | --- |
| `papers/investigations-5/05_radial_theta_collision_geometry/notes/fixed_coefficient_parameter_geometry/B03_R6_PRIMITIVE_ABSOLUTE_PAYMENT_OBSTRUCTION_20261030.md` | `bbe0230b0e07c8a70f9f56af4fbda1985555aa6b14f0676d95c48488e0120a1e` |
| `papers/investigations-5/05_radial_theta_collision_geometry/notes/fixed_coefficient_parameter_geometry/26_ADAPTIVE_RADIUS_AND_PHASE_ALIGNED_IBP_B03_R5_20261030.md` | `d450a8ccb05ce40e8e567a9585002d047406698775140f18606def71b31fa56b` |
| `papers/investigations-5/05_radial_theta_collision_geometry/notes/fixed_coefficient_parameter_geometry/28_SHARP_QUADRATIC_RADIUS_PAYMENT_B03_R5_20261030.md` | `054f7663c9d9fcb49168ded71fc0813495c3d9927df41b462ca15206ade30aca` |
| `papers/investigations-5/05_radial_theta_collision_geometry/numerics/fixed_coefficient_parameter_geometry/fcg_e01_r2_adaptive_ibp_20261030.json` | `557c57e420534e4db949e3d019d5d40077a1df8f055f6634bd2f657c4f87392c` |
| `papers/investigations-5/05_radial_theta_collision_geometry/reviews/fixed_coefficient_parameter_geometry/E02_R5_ADAPTIVE_RADIUS_IBP_ASSESSMENT_20261030.md` | `e7cc379644196226aa4c45af959fe182ee8da8995d32470fa411655514ff8af3` |
