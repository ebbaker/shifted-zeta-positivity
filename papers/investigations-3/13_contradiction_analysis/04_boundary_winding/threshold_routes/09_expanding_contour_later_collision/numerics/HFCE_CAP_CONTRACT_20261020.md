# Frozen fixed-scale Gaussian cap comparison

20 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Same-model delegated research; parent will record its verified model/effort metadata.

This contract is written before the theta comparison is evaluated. It is a separate same-data cost comparison if the direct baseline excludes the box; no new energy coverage is claimed in that case.

- Initial closed box B=[109999/1000000,110001/1000000] × [4005/4,2003/2].
- Fixed s=1/1000000 and L=1/10; fixed positive A*=1000^(7/4) exp(-125 pi), never differentiated.
- Full cap interval x=[20023/20,5008/5]=[1001.15,1001.6]; cap time [11/100,55001/500000]=[.11,.110002].
- Import exactly pinned 160-bit source cache via BW09 pin_sources; re-evaluate at 192 and 256 bits; use fixed spatial degree24/time degree12 Taylor polynomials and complete physical orders0,1 tails from tail_bounds.
- One interval image for the whole cap, no spatial/time subdivisions, no quadrature, no adaptive changes. Whole-run wall budget300 seconds.
- Finite-cap raw deficit image is [s P1^2-P0^2] erf(50), with product error paid separately by erf(50) times [s(2|P1|e1+e1^2)+2|P0|e0+e0^2].
- Complete spatial tails are asymmetric [-p,+s p]/A*^2, p=erfc(50), using the separately proved global physical bounds |H|,|Hx|<=1 for t<=1/5. Contract fails if no valid global-bound proof is supplied.
- Direct Gaussian moments use the same cap component interval times erf(50), plus symmetric tails p/A* for each component. Compare their coordinate-energy lower bound with the strongest independently supplied same-cache initial-box baseline; no manufactured weakening.
- Record raw and complete deficit, product/component/source/spatial errors, direct Gaussian-moment bounds, energy exclusion and improvement, source acquisition cost and consumer cost.
- Controls: exact rational Gaussian integrals for quadratic, cubic, multiplicity-four heat polynomial, two-event quartic (both overall signs), at s in {1/1000000,1/4,1}; positive atomic threshold closed formula at the same scales with rigorous Arb positivity; do not use theta normalization or theta errors on controls.
- Refusals: missing spatial tails or positive global bounds, invalid scale/width, event/cap outside authorized time and source-tail domains, missing derivative cache, and insufficient ordinary-event curvature when contour eligibility is considered. No control claims validate all-real threshold for the two-event first event.

Source provenance and wrapper hash will be serialized. The parent baseline contract is /private/tmp/hfce_baseline_contract.md. Any substantive change requires a new explicit contract, not an invisible retry.
