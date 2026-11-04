# RGD-E03 r1 — two-case first-mode feasibility return

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded **gpt-6.1-sol (Codex),
reasoning effort ultra**, research chat0003, thread
`01a1a77f-2607-7832-9902-29399c58b442`, turn
`01a1a77f-28bf-7121-a260-46291cd2f2a4`.

**Disposition: completed bounded diagnostic; both k=1 and k=4 favorable.**
This is floating feasibility evidence plus exact rational algebra,
**not a certified positive bound**. No new coefficient range or determinant
positivity theorem is claimed. The [E04 assessment][review] accepted all
eight analytical obligations without correction before this run. The
author explicitly authorized E03 after that acceptance.

| k | q | R | L=q-R | S=q/R | (q-R)/(|q|+R) |
| --- | --- | --- | --- | --- | --- |
| 1 | 7.33359159023E-23 | 5.33106949211E-26 | 7.32826052074E-23 | 1.37563233814E+3 | 9.98547179269E-1 |
| 4 | 1.37870309759E-74 | 5.67423881281E-78 | 1.37813567371E-74 | 2.42975867437E+3 | 9.99177211617E-1 |

These are rounded displays of the final 120-digit pass, not enclosures.
The complete strings for both passes, eight shared moments, error estimates,
all E and B entries, and degree-by-degree residual payments are in the
[small execution record][record]. The code is the [fixed diagnostic][code].

## Fixed question, acquisition and scope

The unchanged [Packet01 r1][packet] asks only whether
P_k(1/16,x^[2])-R_k(x^[2],E+B(2)) has a stable positive floating margin
at exactly k=1,4. The canonical complete source, all negative-index
conventions, and exact common b=1/16 remain fixed. Source modes n>=2
are paid by Note01 (6); the entire first-mode spatial exterior u>2 is
paid by Note01 (18). No finite-domain Green identity is used.

The same moments 0,...,7 were acquired with mpmath **1.4.1**, Python
**3.12.14**, using tanh-sinh quadrature at breakpoints
[0,1/8,1/4,1/2,1,2], maxdegree=10. No library was installed.
Two passes, **80 and 120 decimal digits**, were performed. No 160-digit
trigger fired. There were no failed, capped or restarted attempts.
Total computation, including import and exact assembly: **1.676985417
seconds**. Total integrand evaluations: **46,056** (14,048 in the first
pass; 32,008 in the second), below 180 seconds and 250,000. Exact assembly
and checks took 0.114989542 seconds. These are measured local costs,
not a portable runtime claim or comparison with another method.

At 120 digits the acquired inputs were:

| j | x_j^[2] | E_j, complete n>=2 | B_j(2), entire u>2 | Quadrature absolute error estimate |
| --- | --- | --- | --- | --- |
| 0 | 3.59894511969E-4 | 8.84834245958E-9 | 1.75127978893E-4072 | 1.00000000000E-129 |
| 1 | 9.66094122200E-7 | 3.64566234438E-12 | 3.50265308336E-4072 | 1.00000000000E-131 |
| 2 | 1.62764484071E-9 | 1.50207273170E-15 | 1.16758219795E-4072 | 1.00000000000E-127 |
| 3 | 1.95111474490E-12 | 6.18878622916E-19 | 1.55681782638E-4073 | 1.00000000000E-130 |
| 4 | 1.78548808572E-15 | 2.54988151919E-22 | 1.11204242217E-4074 | 1.00000000000E-132 |
| 5 | 1.30527305773E-18 | 1.05059304379E-25 | 4.94254272357E-4076 | 1.00000000000E-134 |
| 6 | 7.86962726892E-22 | 4.32861580180E-29 | 1.49778020878E-4077 | 1.00000000000E-136 |
| 7 | 4.00674761722E-25 | 1.78346076726E-32 | 3.29191252841E-4079 | 1.00000000000E-138 |

**B is nonzero in the definition and separately computed and recorded.**
At both working precisions every E+B addition rounded back to E. Therefore
the floating R values do not outward-enclose even this addition. A rigorous
successor must add B outward. Its scale alone is not permission to omit it.
The quadrature error estimates likewise are estimates and are not included
as certified acquisition allowances in R. Numerical rounding remains
unbounded here; the analytical lower-bound theorem applies to exact x^[2]
and exact E+B, not automatically to these floating numbers.

## Algebra and numerical consistency

The script uses exact sparse integer/rational polynomial arithmetic,
then evaluates the collected Taylor coefficient polynomials. It does not
bound neighboring products separately and it does not take absolute
values before collecting each coefficient.

- k=1: the formal c polynomial has precisely the eight terms in Note01
  (16); its factorization agrees exactly. The C substitution has 85 terms,
  and translation has 111 monomials including the constant. Residual
  counts in degrees 1,...,6 are 5,12,19,23,25,26.
- k=4: the formal c polynomial has 27 terms and no c0, hence no b.
  The C substitution has 276 terms; translation has 881 monomials
  including the constant. Residual counts are 8,32,88,182,294,276.
- In both cases the assembled polynomial equals an independent
  permutation expansion of D4,k*D2,k in formal c variables. Each F3
  formula separately agrees with permutation expansion. Exact binomial
  translation is also checked at non-theta rational data; that latter
  finite check is a consistency check, not a substitute for the
  binomial construction. All nonzero coefficient polynomials through
  degree six are retained.

The maximum symmetric relative discrepancy over all eight moments is
**2.983e-67**. For q,R,S respectively it is
(5.071e-74, 6.670e-75, 4.404e-74) at k=1 and
(1.166e-67, 5.440e-68, 1.710e-67) at k=4 (rounded upward here for display).
These are far below the fixed 1e-30 consistency threshold. Each S is
well above 1+1e-20. Both cases meet exactly the packet's *favorable
diagnostic* guard. The largest reported absolute quadrature-error
estimate is about 2e-82 at 80 digits and 1e-127 at 120 digits; agreement
and estimates do not guarantee those errors.

The linear-degree payment dominates: about 5.33027e-26 of total
5.33107e-26 at k=1 and 5.67415e-78 of total 5.67424e-78 at k=4.
All higher degrees remain included. The specified conservative box
payment is comfortably affordable in these two floating cases. No
correlated residual improvement is needed to justify proceeding to a
rigorous acquisition of this same finite question.

## Evidence limits, controls and continuation

Read the [result index][results], especially [theta identities][theta]
and [collision controls][controls], and the [avoid index][avoid], especially
[target reformulation][a01], [joint payments][a12], [bounded numerics][a10]
and [precision versus evidence][a04]. The known PF44 baseline makes this
a quantitative method test. The exact determinant identity is not itself
a sign estimate. The measured q/R values are new feasibility information
for the frozen payment, not a proof of L>0.

The [E04 review][review] records the claim-specific collision premise
screen: weighted-square, Euler-factor, reflected and smooth positive
primitive controls do not supply the unchanged canonical unit-square
input and its bounds. No additional collision experiment was run or
uncalculated L failure claimed. A positive-time collision is consistent
with a time-zero finite-order comparison. The negative-result scope rule
[avoid/07][a07] continues to apply if a later acquisition fails.

The eight integrals are shared between the two cases; no extra k, cutoff,
mode truncation, parameter scan or certificate was computed. k=2,3, all
k>=5, uniform index estimates, higher orders and Mellin/Gaussian bounds
remain untreated. The inherited D2/D3 inputs retain their internal-review
status. Same-assistant implementation and record checks, plus a fresh
same-model read-only code/record check, are not independent specialist
review.

**Next: [E] RGD-E02 — Sol**, first freeze a rigorous acquisition packet
for these same two bounds, then execute it only under the author's next
request. E02 remains **unissued** at this return. It must rigorously
acquire the eight compact moments, enclose pi/exponentials, add complete
E+B outward, propagate input uncertainty through the collected Taylor
coefficients and the joint q-R expression, and publish positive lower
endpoints or the precise failed step. No larger scan is warranted.
B02 remains a conditional repair task; B03 is not enabled by this floating
pass. The [continuation/model-change note][continuation] gives the manual
handoff and the [sole register][progress] owns current readiness.

## Versions and replay

Assessed Note01: `556a97aa60f7a3448acbd00cf8bfa4c3e2916e428f67d03dbb97889077bc9847`.
Frozen Packet01: `da639d27f073b6ec4cf7291263da4756c1ccff7133fb7ccf6e47786928c9fd6a`.
E04 review, code and all diagnostic input hashes are recorded in the JSON.
Diagnostic code SHA-256: `a42db929d82eeeac3aef36b36290e003946c06e1505d81b76c119846576c1f09`.
Execution-record SHA-256: `932fa5164630bbf98c124e3d89d9f3c7501bfcef82d54d28245a72bc91f293b1`.
Hashes identify exact artifacts, not mathematical validity. The frozen
inputs and inherited returns are unchanged. The execution record is about
26 KB; no large data or manuscript snapshots were generated.

Run the installed script from any directory with a Python environment
containing mpmath, passing a fresh output path to preserve this return:

```text
python /absolute/path/to/10_radial_green_determinants/numerics/rgd_e03_firstmode_diagnostic.py --output /tmp/rgd-e03-replay.json
```

This is a regeneration instruction, not a request to spend the diagnostic
budget again. No replay was needed after the completed two-pass run.

[review]: ../reviews/01_RGD_E04_R1_BOUNDARY_PRESERVING_COMPARISON_ASSESSMENT_20261104.md
[packet]: ../research-progress/handoffs/01_RGD_E04_R1_AND_E03_R1_BOUNDARY_PRESERVING_COMPARISON_20261104.md
[record]: ../numerics/RGD_E03_R1_FIRSTMODE_DIAGNOSTIC_20261104.json
[code]: ../numerics/rgd_e03_firstmode_diagnostic.py
[continuation]: ../research-progress/handoffs/03_RGD_CONTINUATION_AFTER_FAVORABLE_E03_AND_MODEL_CHANGE_20261104.md
[progress]: ../research-progress/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_PROGRESS_20261104.md
[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[a04]: ../../../../../../../avoid/04_counts_and_precision_as_evidence.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
