# Current summary: heat-flow bounds and RH applications

Updated 26 October 2026, America/New_York. Prepared for **Edward Baker**
with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded
effort max**. Maintained summary, updated for the Rodgers–Tao subfolder;
exploratory, with no new
Newman bound or zero-exclusion theorem claimed.
Rodgers–Tao r1/r2 results and high-level bound priorities updated
26 October 2026 for Edward Baker with
substantial LLM assistance, **gpt-6.1-sol, actual recorded effort ultra**;
same-model internal assessment only.

This preserves the ideas in
[Brainstorm 01](../notes/01_HEAT_FLOW_RH_APPLICATIONS_BRAINSTORM_20261026.md).
[Note 02](../notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md) develops
the author's follow-up about assuming \(\Lambda>0\).
The [Rodgers–Tao branch](../rodgers_tao/README.md) now owns the focused
[overview](../rodgers_tao/research-overview/01_RODGERS_TAO_RESEARCH_OVERVIEW_20261026.md)
and [progress register](../rodgers_tao/research-progress/01_RODGERS_TAO_RESEARCH_PROGRESS_20261026.md);
its bounded audit in
[Note02](../rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md)
now has an instantiated canonical finite-family return in
[Note03](../rodgers_tao/notes/03_CANONICAL_TWO_ROOT_MARGINS_AND_FORCE_BUDGET_20261026.md).
The immediate preference is Rodgers–Tao, while the investigation stays
flexible. **Identifying the bounds an application would need is a coequal
goal:** these specifications should guide the intermediate estimates still
being developed.

## 1. Best ideas to retain

| ID | Idea and current priority | First useful outcome |
| --- | --- | --- |
| I1 | **Rodgers–Tao dynamics and energy: lead direction.** Study the complete interaction of a local zero block with its exterior. | Match one corrected energy/boundary term to a field-and-derivative bound; identify a quantitative gain or the exact missing estimate. |
| I2 | **Assume \(\Lambda>0\): current follow-up.** Investigate a possible finite collision at the threshold, using I1's methods. | Specify an estimate that prevents local energy concentration, or a complete first-jet margin on a declared positive-time slab. No such exclusion is proved here. |
| I3 | **Lower a specified positive Newman upper bound.** Use a complete existing certificate as the consumer. | Improve its total margin, covered parameter, onset, or certified cost; retain all initial, barrier, and exterior obligations. |
| I4 | **RH implies simple zeros.** Connect to the existing BW-10 endpoint program. | Identify a theta-specific estimate that beats the multiple-root endpoint behavior; preserve the distinction between this target and I2. |
| I5 | **Effective negative-time witnesses.** Quantify where a nonreal zero can be found. | A certified search region or cost as time approaches zero, compared with existing negative-time results. |
| I6 | **Moving-time zero geometry, counts, and certification.** Retain useful outcomes short of RH. | A new uniformity range, sharper complete count or interaction estimate, or an objective reduction in certificate cost. |
| I7 | **Aspirational bound design.** This accompanies every direction above. | A precise domain, norm, margin, parameter dependence, and consumer implication before committing to proving the estimate. |

For I3, \(0.2\) is the brainstorm's published comparison baseline, **not a
current-record claim**. The Gomila candidate and later conditional claims
retain their audit/hypothesis qualifications in the
[reference guide](../references/README.md).

## 2. The Rodgers–Tao sign question

The convention is \(H_t=-H_{zz}\), with all zeros real exactly for
\(t\ge\Lambda\). RH means \(\Lambda\le0\); Rodgers–Tao gives
\(\Lambda\ge0\). Assuming \(\Lambda>0\) for contradiction is therefore a
legitimate RH strategy.

The original argument uses a negative all-real interval to force regular
spacing at the zeta slice \(t=0\), contradicting its known spacing
information. With a positive threshold, that slice precedes the all-real
interval. Regular spacing at a later positive time supplies no analogous
contradiction. See [Note 02](../notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md)
for the source check and the time-shift issue.

The useful alternative is local: a positive threshold entails a finite
multiple-zero event, even though sufficiently high zeros at each fixed
positive time are already regular. A bulk asymptotic can miss that event.
The exact heat model \(F(t,z)=z^2-2(t-T)\) has a positive threshold \(T\),
and its post-threshold squared gap is \(8(t-T)\). Thus forward repulsion
and later simplicity permit a collision at the earlier endpoint.

I2 asks what extra canonical-theta estimate prevents that concentration.
I4 asks the corresponding endpoint question at zero time **under RH**.
The same local heat obstruction is relevant, but the hypotheses and
conclusions differ.

## 3. What the bounds supply, and their limits

The [Book review](../reviews/01_BOOK_APPLICATION_REVIEW_20261026.md) and
Brainstorm 01 §2 give the source inventory and exact rates:

- Negative-time hierarchies supply accurate complete arithmetic field and
  derivative data. The strongest moving-endpoint result in that inventory
  stops at \(-t\asymp1/\log X\).
- The signed crossover includes \(t=0\) and the microscopic scale
  \(|t|\asymp(\log X)^{-2}\), but supplies no automatic root-separation or
  nonvanishing floor.
- The Book's positive hierarchy and physical clock give late-time
  geometry. Its fixed-order analytic range starts at \(t\ge32\);
  adding orders there does not create a small-time theorem.
- The all-time physical construction has fixed smoothing/regulation.
  Its spatial joins are nonholomorphic. Weak density accuracy alone
  cannot distinguish a double zero from a nearby pair.
- Finite-source evaluation supports fixed-data accuracy. Uniform,
  practical cost as height grows, time shrinks, or a margin vanishes is
  a separate obligation.

**Parent-status update, separate from the brainstorm's frozen baseline:**
Ansatz Notes 24–25 first supplied buffered high-height coverage on
\([1/2,1]\) and \([3/4,33]\). The subsequent
[Note 26](../../01_heat_density_asymptotics/ansatz/notes/26_RETAINED_ARITHMETIC_MOVING_POSITIVE_BAND_20261026.md)
and [Assessment 20](../../01_heat_density_asymptotics/ansatz/reviews/20_RETAINED_ARITHMETIC_MOVING_BAND_ASSESSMENT_20261026.md)
report complete retained-arithmetic field/jets on \(4/L\le t\le1\),
with normalized allowance \((1+\log X)^2X^{-3/4}\), and its crossover overlap gives coverage on \(0\le t\le1\). Thus the formerly missing high-height
positive-time field coverage is now reported closed at this allowance.
Source status is **proved in-note from named inputs; same-model internal
assessment only**, with uninstantiated constants/onsets. The theorem,
union, scope, and assessment were inspected for this update; the full proof
was not independently audited. Lower root/first-jet margins beyond the
compact pilot below, the remaining finite-height core, transfer as
resolution shrinks, and useful joint cost remain separate obligations. The
[Rodgers–Tao initial note](../rodgers_tao/notes/01_INITIAL_RESULTS_AND_BOUND_REQUIREMENTS_20261026.md)
records the exact input contract and inspection limits.

### Newest Rodgers–Tao results and their implication

The bounded audit of the corrected proof identifies the bounds an energy argument
actually needs: control of interactions with zeros outside a chosen
block, suitable separating gaps, and the full boundary and reference
energy payments. The contour method can compare exterior forces without
tracking individual interior zeros, provided an independent contour
margin is available. This is a transfer estimate; the original proof's
negative-time interval and zeta endpoint remain separate inputs. See
[Note02](../rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md).

The subsequent canonical two-root pilot **acquires actual instances of
B3–B5** on \(t\in[1/20000,1/10000]\), in the fixed rectangle
\([26,46]+i[-2,2]\): a contour floor above \(4.94\times10^{-7}\),
two simple real roots with certified initial and whole-slab enclosures,
and a complete exterior-force budget. The direct root-derivative method
bounds the integrated exterior term by \(3.566\times10^{-8}\), against
\(1.104\times10^{-5}\) for the contour method, about **309 times smaller**.
These compare certified upper budgets, not runtime or the true errors.
[Note03](../rodgers_tao/notes/03_CANONICAL_TWO_ROOT_MARGINS_AND_FORCE_BUDGET_20261026.md)
gives the exact family, constants, certificate and replay;
[Assessment02](../rodgers_tao/reviews/02_CANONICAL_TWO_ROOT_ACQUISITION_ASSESSMENT_20261026.md)
records the same-model review limits. The region was already covered;
this is a finite acquisition and comparison result, with no new Newman
bound or endpoint exclusion.

The practical lesson is that **extra field accuracy is not the next
priority on this pilot**. Approximation error is already negligible;
the dominant loss is the contour method's estimate of the exterior
force. Pairing the drift errors also gives a larger allowance than
separate estimates on this wide-gap family. Preserve these comparisons
and stop seeking a contour advantage on the frozen box.

The desired next bounds must work on a materially different family or
scale: usable margins for growing or microscopic zero blocks, sharper
relative exterior-force estimates, and a complete corrected energy
balance after all boundary and summation costs. They must be compared
with the direct method using the same available information. Actual
compact margins do not supply uniform high-height, shrinking-resolution
or threshold estimates. The
[progress register](../rodgers_tao/research-progress/01_RODGERS_TAO_RESEARCH_PROGRESS_20261026.md)
owns the detailed task status and next research question.

## 4. The eight desired bounds

These retain the stable B1–B8 agenda from Brainstorm 01, updated for the
new results. Each is a broader requirement: acquiring one finite example
does not establish its uniform version. At height X, “microscopic” means
spatial distances of order \(1/\log X\) and times of order
\(1/(\log X)^2\).

| ID | Desired bound, at a high level | Present position and use |
| --- | --- | --- |
| B1 | Complete field and derivative errors at small positive time, retaining all arithmetic terms and giving usable constants and starting heights | High-height field coverage is reported available. Consumer margins, the remaining finite core and effective onsets still need their own bounds. |
| B2 | Accurate microscopic comparisons that remain useful as the number of zeros in a block grows | Crossover estimates provide a baseline. Block-size, narrow-buffer and short-time losses must be paid together before applying them to energy. |
| B3 | Lower contour, root-derivative or first-jet margins strong enough to dominate the complete error | Acquired on the r2 compact family. Desired next: independent margins on growing/high-height families or the precise positive-time region needed by an application. |
| B4 | Control of the relative force exerted by zeros outside a block, including its variation and the complete exterior contribution | Paid for r2's finite block. Desired next: a sharper estimate useful at the new scale, with an advantage over the direct method demonstrated rather than assumed. |
| B5 | A complete localized energy balance, including exterior forces, changing boundaries, cutoffs and reference-energy corrections | The raw two-root balance is calibrated. The corrected renormalized block and dyadic-boundary assembly remain open. |
| B6 | Stable transfer as spatial smoothing and regulator widths shrink, retaining derivative and localization costs | Fixed-resolution results do not supply this uniformity. Resolving near-collision geometry requires its own quantitative budget. |
| B7 | Under RH, a theta-specific arithmetic endpoint bound stronger than the universal multiple-root collision behavior | Still a final-strength simplicity target, coordinated with BW-10; no such discriminator is acquired by the compact pilot. |
| B8 | A joint effective bound on the total work needed for a complete application as height grows, time shrinks and margins deteriorate | Include source acquisition, all modes, working precision, starting heights and coverage. A finite replay or a fixed-data accuracy bound is not the full cost comparison. |

The immediate emphasis is **B3–B5 at a new scale**, supported by B2, B6
and B8 where the chosen family requires them. Detailed formulas and
required error sizes belong in
[Note02](../rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md)
and [Note03](../rodgers_tao/notes/03_CANONICAL_TWO_ROOT_MARGINS_AND_FORCE_BUDGET_20261026.md).

I2 adds a **positive-threshold application of B3–B5**, without replacing
B7. One diagnostic target is that local inverse-square pair energy grow
more slowly than \(1/(t-T)\) at a hypothetical positive threshold \(T\).
Note 02 explains its strength, required uniformity, and failure on
collision controls. Naming that estimate is planning progress, not a
weaker proof of RH.

## 5. What to do next

1. **Choose a useful new consumer.** Specify a growing or microscopic
   family, or a corrected dyadic boundary term, where the available root
   information differs materially from the completed compact pilot.
   State the conclusion that a successful bound would buy before more
   numerical work.
2. **Acquire the actual margins and complete force/energy payment.**
   Retain the dependence on block size, separation, buffers, time and
   all boundary sums. Compare with the direct method using the same
   information. Do not add approximation orders to the closed r2 pilot.
3. **For a smaller positive Newman bound, complete the global consumer.**
   Combine the finite-region margins with the required initial,
   exterior and barrier conditions, using a documented baseline.
   A better isolated block estimate alone does not lower that bound.
4. **Keep the endpoint question separate.** A positive-threshold
   contradiction still needs new canonical arithmetic information
   uniform toward a possible collision. RH-conditional simplicity has
   its distinct time-zero premise and remains coordinated with BW-10.
5. **Retain the other useful routes.** Effective negative-time witnesses
   and moving-time geometry remain alternatives. For negative
   microscopic time, pay the narrow transverse buffers and derivative
   losses while preserving arithmetic cancellation.

See the [Rodgers–Tao progress register](../rodgers_tao/research-progress/01_RODGERS_TAO_RESEARCH_PROGRESS_20261026.md)
for detailed dependencies and the next bounded question. This summary
states the application priorities rather than duplicating that register.

Every continuation should label its conclusion as an available theorem,
a quantitative milestone, an aspirational specification, or a scoped
obstruction. Keep the full control screen in Brainstorm 01 §8:
Euler-factor, weighted-square, reflected, smooth/primitive, finite-prime,
counter-kernel, finite-profile, normalized endpoint, and polynomial/Hermite
families. State which actual premise fails; failing the theta identity
does not automatically mean failing an inequality derived from it.

The [result index](../../../../result-summaries/README.md), especially
[11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[12](../../../../result-summaries/12_collision_controls_and_screening.md),
and [13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
and the [avoid index](../../../../avoid/README.md), especially
[target classification](../../../../avoid/01_restating_the_target.md),
[control screening](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
and [scoped conclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
remain the shared research memory. The proposed direction is not ruled
out by the limitations of the direct sign reversal.
