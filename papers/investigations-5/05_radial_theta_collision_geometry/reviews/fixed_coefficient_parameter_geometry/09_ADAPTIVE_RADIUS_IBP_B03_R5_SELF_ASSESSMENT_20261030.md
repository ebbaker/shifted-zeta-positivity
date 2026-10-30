# Self-assessment of adaptive radius and phase-aligned IBP

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra**, reasoning effort **max**, existing Investigation05 **chat0048**. This is the proof author's self-check of [Note26][proof]; no subagent, numerical acquisition, independent implementation or specialist/formal review contributed.

**Disposition:** B03 R5's bounded conceptual task is complete. C04 R3 supplies an explicit adaptive sufficient certificate, uniform complete-source derivative envelopes and a fixed comparison question. Numerical benefit is unmeasured. [E01 R2/Sol][packet] is ready; no E02 acceptance is claimed.

| Obligation | Self-check and retained scope |
| --- | --- |
| Separate analytic and certified radii | All complex Taylor paths stay in \(|t|,|x|\le R\); the real ball is enclosed by \(|t|,|x|\le r\le R/2\). Keeping R fixed is permitted by the original proof and is a declared coefficient revision. |
| Full signed derivative envelope | Differentiating \(e^{tu^2}u^jf\) gives \(e^{tu^2}(D_j+2tu^{j+1}f)\). Its bound is exactly (4), with the signed complete D_j formed before absolute value. No unknown supremum or physical-jet division. |
| Whole-line IBP | Integrating cosine to sine gives the negative integral in (6). The zero endpoint vanishes for j=3,4 and full source decay pays infinity. \(|a+x|\ge a-R>0\) holds on the complex disk. |
| Finite phase boundary | The selected phases are exactly 22pi and 23pi. Center cancellation does not imply neighborhood cancellation: sinh(RU) pays the latter. The source exterior remains present in (10)–(11). Complex sine/cosine bounds follow from absolute power series. |
| Cauchy sum and monotonicity | Summing k+1 monomials of degree k gives (14), recovering the old factor at q=1/2. Coefficientwise Cauchy bounds prove (18); positive powers prove radius monotonicity with fixed outer envelope. This concerns exact quantities, not arbitrary interval widths. |
| Degree-one radius | The sole nonzero total-degree-one coefficient is g10=-h1h3. For q<=1/2, (3-2q)/(1-q)^2<=8. The two restrictions in (19) pay at most D/4 each, leaving d1>=D/2. D>0 is an explicit center condition; D=0 remains a failure even at some noncolliding centers. |
| Primitive remainder | Expanding the kernel at u=0 cancels constants and u squared; the even kernel is O(u^4). Both lower Green terms vanish in the combined remainder. The upper finite boundary and complete exterior in (22) retain their signs; phase alignment alone does not kill them. |
| Generalized tail route | Powers p=1,2,3 and exponents 5,9,13 cover the derivative terms. The same quadratic exponential lower bound and logarithmic tangent argument give (26)–(27), with every guard explicit. Mode and retained-mode exterior payments are distinguished. |
| Comparisons and physical transfer | The direct strip receives the same information and is at least as strong. Scalar floors are reported rather than ignored. C01 still imports uniform derivative convergence; the all-time carrier retains exact coefficient, 6L and spatial exterior. |
| Controls and finite scope | Event-containing balls reject for the same exact row reason. Shrinking a ball away from an event is not a passed event control. Atomic-source IBP applicability is not presumed; other registered premise failures are retained. No actual theta positivity or global covering schedule is acquired. |

The main unresolved issues are quantitative: whether the IBP envelope is smaller at the fixed test point, whether another constraint dominates after the tail decreases, and whether certified radii are useful for coverage. The phase-cutoff bound can be conservative; its complete core still contains oscillations. The primitive identity is a potentially useful simplification but has no proved improved remainder payment in this return.

The exact radius rule and Gaussian example demonstrate local capability without a source minimum. They do not prove that every theta center has a nonzero quadratic discriminant, nor eliminate the need for full theta information. Further degree/radius adaptation is outside the frozen finite experiment unless a later contract specifies it.

The [continuation][next] supplies the model handoff. [Progress06][progress] owns live status. No manuscript, result-summary or milestone promotion is made. Hash and link checks identify files only; no algebra count is treated as a mathematical independence claim.

[proof]: ../../notes/fixed_coefficient_parameter_geometry/26_ADAPTIVE_RADIUS_AND_PHASE_ALIGNED_IBP_B03_R5_20261030.md
[packet]: ../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E01_R2_ADAPTIVE_RADIUS_IBP_COMPARISON_20261030.md
[next]: ../../notes/fixed_coefficient_parameter_geometry/27_CONTINUATION_ADAPTIVE_RADIUS_IBP_AND_MODEL_HANDOFF_20261030.md
[progress]: ../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md
