# FCG-E01 R1: confirmed positive joint-jet coefficient on the frozen ball

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol**, reasoning effort **ultra**, existing Investigation05 **chat0047**, *Continue FCG-E02 R2 assessment*.

**Execution complete: degree \(N=8\) has a rigorously positive coefficient at both 256 and 384 bits.** The [frozen E01 R1 request][packet] was followed on its one ball; degrees 16 and 32 were not acquired, as the first confirmed positive degree ends the test. The [script][script] and [outward record][record] retain the complete signed source jets, separate quadrature/mode/source errors, tail guards, coefficients and comparisons. This is an internal interval certificate with an [execution self-check][self], pending the new [E02 R3 assessment][assessment]. [Progress06][progress] alone owns live status.

## 1. Fixed question and result

Keep [Note16][proof]'s complete theta source, literal cosine, original drift, unit preparation and full \(\mathbb R^3\). The ball is unchanged:
\[
 (\tau,a,r)=(1/4,882607/20000,1/64),\quad R=1/32,\qquad
 B=\{(T,A):(T-\tau)^2+(A-a)^2\le r^2\}.
\]
With complete center jets \(h_j\), \(b=h_2\), and the correlated allowance defined before acquisition,
\[
 D_0=h_1^2-2bh_0,\quad
 d_{B,8}=|D_0|-2b^2r-\Gamma_8,\quad
 c_{B,8}=\frac{d_{B,8}}{1+h_0^2+h_1^2+b^2},
\]
the outward enclosures prove
\[
 \boxed{d_{B,8}>5.07\,10^{-13},\qquad c_{B,8}>5.07\,10^{-13}.}
\]
The corresponding exact coefficient, rather than its rounded lower bound, is the coefficient in the spatial evolution below.

The following deliberately widened decimal intervals contain both precision stages. Full precision and binary midpoint/radius pairs remain in the record.

| Quantity | Outward enclosure at both precisions |
| --- | --- |
| \(D_0\) | [5.18467143, 5.18467144] × \(10^{-13}\) |
| \(2b^2r\) | [1.95740578, 1.95740579] × \(10^{-15}\) |
| Finite signed-coefficient absolute sum | [1.03607819, 1.03607820] × \(10^{-16}\) |
| \(M_G\) | [2.10826853, 2.10826854] × \(10^{-13}\) |
| \(M_G(8+3)/2^8\) | [9.05896634, 9.05896635] × \(10^{-15}\) |
| \(\Gamma_8\) | [9.16257416, 9.16257417] × \(10^{-15}\) |
| \(d_{B,8}\) | [5.07347163, 5.07347164] × \(10^{-13}\) |
| \(c_{B,8}\) | [5.07347163, 5.07347164] × \(10^{-13}\) |
| \(\Gamma_{\rm sep}\) | [8.08923331, 8.08923332] × \(10^{-14}\) |
| Independent-allowance margin | [4.35617404, 4.35617405] × \(10^{-13}\) |
| \(K_B\) | [5.01674762, 5.01674763] × \(10^{-7}\) |
| \(\mu_B\), also the direct uniform floor | [1.01130692, 1.01130693] × \(10^{-6}\) |

The complete positive moments and first three signed center jets are:

| Complete input | Outward enclosure at both precisions |
| --- | --- |
| \({\cal M}_3(R)\) | [1.21893826, 1.21893827] × \(10^{-4}\) |
| \({\cal M}_4(R)\) | [2.36386623, 2.36386624] × \(10^{-5}\) |
| \(h_0\) | [1.03403761, 1.03403762] × \(10^{-6}\) |
| \(h_1\) | [-2.96993926, -2.96993925] × \(10^{-8}\) |
| \(h_2\) | [-2.50273821, -2.50273820] × \(10^{-7}\) |

These are complete-source enclosures. Finite-integral midpoints alone were not substituted for \(h_j\).

## 2. Acquisition, full tails and arithmetic

Real-axis Arb quadrature integrated the exact sum of modes \(1,\ldots,8\) on \([0,1]\). Each signed \(h_j\), \(0\le j\le17\), retains its actual derivative cycle \(\cos,-\sin,-\cos,\sin\). Appendix A3 adds an omitted-mode error over the entire half-line; A4 separately pays \(u>1\) for every retained mode. Every actual interval guard was asserted. For the positive moments, the unacquired source part is added as a nonnegative interval; for signed jets it is symmetric. Lower and upper bounds for the exact \(\Gamma_8\) are preserved.

The two prescribed stages used:

| Precision | Absolute / relative tolerance | Acquisitions |
| --- | --- | --- |
| 256 bits | \(2^{-160}\), \(2^{-128}\) | Two positive moments, then \(h_0,\ldots,h_{17}\); positive \(d_{B,8}\) |
| 384 bits | \(2^{-224}\), \(2^{-192}\) | Entire same 20-input acquisition for confirmation, then four carrier integrals after positivity |

Every integral used maximum 200000 evaluations and depth 30. Runtime was Python 3.10.0, python-flint 0.9.0, FLINT 3.6.0; no package or backend was changed. All shared complete-input intervals and derived degree-8 margins overlap between precisions.

There were **24 distinct source integrands and 44 quadrature calls**, including the 20 confirmation repeats. The record's original field named “distinct_source_integrals” counts those 44 acquisitions; its added cost summary disambiguates the 24 mathematical inputs. Total callbacks were **21716**, with at most **546** per integral. Total acquisition wall time was **0.901154 seconds**, including approximately **0.749920 seconds** in the individual integral calls. These are local observed costs, not a speed comparison or complexity claim. The 20-minute cap was not approached.

The exact polynomial identity (8), coefficient rule (16), every listed low-order case (17), and the geometric sum (19) passed rational/symbolic checks before acquisition. The four specified \(q\)-coefficients are set exactly to zero. Zero-centered real-ball squaring reproduces the historical native NaN issue; the script uses explicit nonnegative square/absolute ranges, with Arb's nonnegative-part operation handling radius rounding. No source value was acquired during those arithmetic guards.

The largest retained-mode source-tail upper bound among the acquired jets/moments is below \(6\,10^{-71}\), and the omitted-mode error is below \(4\,10^{-109}\). Each exact separate error, rather than these reporting summaries, is paid in its own integral enclosure. Finite quadrature uncertainty dominates those tails. No source, mode, Taylor or spatial exterior is omitted.

## 3. Uniform first-jet and all-time spatial consequences

Note16's exact identity and its paid complete remainder give
\[
 |(H,H_A)|\ge\mu_B=\frac{d_{B,8}}{K_B},\qquad
 K_B=\sqrt{4b^2+(|h_1|+r|b|)^2}.
\]
The acquired intervals certify
\[
 \boxed{\mu_B>1.01\,10^{-6}\quad\text{on all of }B.}
\]
After confirmation, four positive source integrals at \(T_+=17/64\), \(j=0,1\), \(Y=0,4\) gave the carrier quantities in Note16(23). Conservative reporting bounds are
\[
 L<0.068,\quad R_2<0.101,\quad
 \overline N=\max\{R_2+6L,3L/c_{B,8}\}<4.01\,10^{11}.
\]
The record calculates this last upper bound from the tight carrier intervals and the tight lower endpoint of the exact \(c_{B,8}\), before widening the displayed bounds.

The accepted complete scalar-carrier argument then yields
\[
 \boxed{\quad
 E_{c_{B,8}}(s;p)\ge\delta_{B,8}
 =\frac{3\mu_B^2}{16\pi}
       \left(\frac{\mu_B}{2\overline N}\right)^{3/2}
 >8.6\,10^{-41}
 \quad(p\in B,\ s\ge0).\quad}
\]
The lower bound in the record is approximately \(8.6566450540\,10^{-41}\), obtained conservatively from lower \(c,\mu_B\) and upper carrier quantities. The defined \(c_{B,8}\) is small, so its second-moment ceiling is large and its energy floor is correspondingly small. No coefficient optimization or substitution was performed. The floor starts at \(s=0\) and uses no stationary convergence.

## 4. Matched direct and C01 comparisons

For the identical correlated scalar strip, the exact local distance is
\[
 \operatorname{dist}(0,\text{strip})
 =\frac{(|D_0+2b^2t|-\Gamma_8)_+}
        {\sqrt{4b^2+(h_1+bx)^2}},
\]
when the denominator is nonzero (the degenerate \(w=0\) case has distance zero). The same uniform certified floor is \(\mu_B>1.01\,10^{-6}\). The center-strip distance is approximately \(1.0157083663\,10^{-6}\). Thus the spatial construction gains no separation over the direct consumer of the same information.

The independent allowance from the very same positive moments also passes:
\[
 \Gamma_{\rm sep}\approx8.0892333151\,10^{-14},\qquad
 |D_0|-2b^2r-\Gamma_{\rm sep}>4.35\,10^{-13}.
\]
The correlated allowance is tighter, but correlation is not necessary to obtain a positive sufficient margin on this particular pilot. Note16's eventual high-frequency obstruction to the independent allowance is a different scoped statement; it did not predict failure on every finite pilot.

For C01, the same data give
\[
 B_2=|b|+r({\cal M}_3+{\cal M}_4),\qquad
 1+B_2^{\rm upper}/\mu_B^{\rm lower}<3.496.
\]
Consequently the simple fixed choice **\(C=4\)** satisfies
\[
 {\cal L}+4E_J\ge E_J\ge\mu_B^2.
\]
With spatial \(c=1\), the accepted compact-uniform derivative limit transfers this to eventual positivity of \(D_1+4E_1\), uniformly on \(B\). Its start time remains unspecified and depends on that accepted limit. No independent curvature estimate, flow simulation or earlier Poisson-budget repair is supplied.

## 5. Controls, scope and disposition

The Gaussian-polynomial control on its own event-centered radius-\(1/64\) ball has \(h_0=h_1=D_0=0\), \(b\ne0\), and strictly negative \(d_{B,N}\); it lacks the complete theta arithmetic source and fails the positive margin. The inherited three-positive-square event lies inside the present ball: its distance from the center frequency is less than \(1/20000<1/64\). Its own complete-source remainder must give \(d_{B,N}\le0\). This uses the existing event certificate cited by the [control register][controls], without numerical replay or borrowing theta tails.

Other controls retain Note16's source-specific screen: four-square and reflected/primitive controls use their own event balls and moment domains; high-gap existence does not place an event in this pilot; Euler-factor negative-Laguerre witnesses do not by themselves locate a collision; polynomial-observation controls fail the literal-cosine premise. No unverified domain is reported as passed. The weighted-square event is not an all-real threshold.

This completes the frozen sufficient coefficient test. It does not show that this ball contains a theta simple zero, establish broader coverage or an RH/Newman improvement, or demonstrate a cost/estimation advantage. The generic simple-zero capability and true-collision obstruction remain distinct from this acquired theta sign. E02 R1/R2 retain their original accepted scopes; neither had assessed Note16 or this acquisition.

**Next: [E] FCG-E02 R3 — Sol**, assess the complete conditional proof and actual interval evidence under the [new bounded request][assessment]. The [continuation/model-change note][next] preserves chat0047 and the subsequent scope. This execution uses three read-only same-Sol contributions for algebra, script and control checks, with shared premises, not specialist/formal independence. No manuscript, result-summary or milestone promotion is made.

Follow the [result index][results] and [avoid index][avoid], particularly [classification][a01], [scoped exclusions][a07], [bounded numerics][a10], [separate bounds][a12] and [noncircular coefficients][a14].

[packet]: ../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E01_R1_CORRELATED_JET_COEFFICIENT_20261030.md
[proof]: 16_QUADRATIC_HEAT_BEZOUT_COEFFICIENT_B03_R3_20261030.md
[script]: ../../numerics/fixed_coefficient_parameter_geometry/execute_fcg_e01_r1.py
[record]: ../../numerics/fixed_coefficient_parameter_geometry/fcg_e01_r1_joint_jet_coefficient_20261030.json
[self]: ../../reviews/fixed_coefficient_parameter_geometry/05_JOINT_JET_COEFFICIENT_E01_R1_SELF_CHECK_20261030.md
[assessment]: ../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R3_JOINT_JET_COEFFICIENT_ASSESSMENT_20261030.md
[progress]: ../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md
[next]: 19_CONTINUATION_FCG_E02_R3_AND_MODEL_HANDOFF_20261030.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a14]: ../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
