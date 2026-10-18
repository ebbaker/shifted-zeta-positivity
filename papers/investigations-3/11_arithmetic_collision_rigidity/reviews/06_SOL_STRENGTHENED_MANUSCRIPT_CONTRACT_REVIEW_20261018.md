# Sol review of the strengthened manuscript contracts

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. **GPT-6.1 Sol (`gpt-6.1-sol`), actual reasoning effort max**,
verified from this turn's metadata. This is same-assistant internal review;
it is not independent specialist review.

**Stage 0 disposition: gate passed for the stated auxiliary contracts.**
No blocking defect was found in the strengthened proof chain. All three
scalar programs reproduce their retained outputs byte for byte, and the
saved manuscript compiles successfully through the desktop compiler.
These checks establish no complete-field margin by themselves.

The controlling plan is [overview 02][plan]; ongoing decisions are in the
[progress tracker][progress]. Read the [result summaries][summaries] and
[patterns to avoid][avoid], particularly [collision controls][controls],
[target classification][target] and [separated estimates][separate].

## Version and scalar replay

The eight-file source set matches the [build record][build] exactly:
`f6cd484647ef328047e9ac51a577b8260e899aecbfdd5026e9e238079feb823f`.
The [fresh replay record][record] pins each source, Notes 05–06, Reviews
04–05 and overview 02. Review 04 concerns the earlier manuscript hash and
is used as historical assessment, not as a review of identical revised bytes.

`certify_manuscript_constants.py`, `certify_strip_carriers.py` and
`certify_updated_manuscript.py` all pass. Their fresh outputs match the
original JSON bytes, including all nine current table rows and eight current
headline bounds. The reused programs print their original authoring model
metadata; the wrapper records the actual Sol max replay separately.
The interval engine is reused, not independently implemented.

## Analytic checks

| Contract | Check and domain |
| --- | --- |
| Positive real part | For bounded nonnegative coefficients starting at m at least 2 and 0 to 1/2 heat time, the convex-kernel argument is strict for positive source coordinate, including the closed strip boundary. The endpoint at spectral coordinate zero is handled directly. |
| Schwarz budget | The map uses scale 4m squared. The second disk coefficient retains both slope and curvature deficits, giving the stated combined budget and E/64 payment. |
| Real remainder jets | The second quotient derivative retains the two squared slope terms; the factors are d_m and d_m squared. Absolute tolerances still depend on the original coefficient comparison. |
| Complex residual | The unit-strip lower bound for the real part of the carrier is explicit. The endpoint identity and weighted second-derivative mass give the stated complex relative estimate. |
| Complete contour shift | Source reflection is used before truncation, including the negative half-line. Remote contour sides decay. Individual finite modes cannot silently inherit the discarded vertical segment. |
| Derivatives and heat equation | The two factors are i(u+id) and -i(u-id). Both satisfy the heat equation with parameters fixed. A finite paired approximant need not be even. |
| Shifted tail | The positive linear rate, quadratic absorption and geometric ratio are explicit. Each fixed derivative is covered; the constants do not certify retained-mode integration. |
| Boundary approach | The power of x, ratio denominator and logarithmic factors agree with the stated asymptotic. Constants and effective onset remain unevaluated. |
| Collision normalization and controls | The curvature coefficient and stationary predecessor are retained. The reflection-rigidity argument and the fixed-coefficient orbit construction have their stated restricted scope. |

The primary [Polymath text](https://arxiv.org/html/1904.12438v2) was checked
for normalization in equations (1)–(4), the fixed-positive-time high-zero
input in Theorem 1.5 and Section 9, and the strip contraction in Theorem
3.2. These remain imported theorems. The published comparison bound in
[Platt–Trudgian, Section 3.4, Corollary 2](https://arxiv.org/pdf/2004.09765)
is used only as the plan's comparison baseline.

No manuscript repair was required. The next obligation was a complete
interval evaluator with retained-source, quadrature and whole-cell errors;
its new notes are housed in the user's requested
[overview 02 notes folder](../notes/02_updated_research_plan/README.md).

[plan]: ../research-overview/02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md
[progress]: ../research-progress/02_UPDATED_RESEARCH_PLAN_PROGRESS_20261018.md
[build]: ../manuscript/positive_arithmetic_packets/BUILD_RECORD.json
[record]: ../numerics/STRENGTHENED_MANUSCRIPT_REPLAY_20261018.json
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[target]: ../../../../avoid/01_restating_the_target.md
[separate]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
