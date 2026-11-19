# Research position and paths forward

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model and reasoning effort are
unavailable in this chat's recorded configuration; none is inferred.
Status: **expository synthesis and prospective brainstorm, with
same-assistant source and premise checking**. No new theorem, certificate,
manuscript milestone or research-task disposition is established here.

The current development has three distinct achievements: exact equations
for a pair and its entire environment; a finite model proved to follow
that environment over a fixed interval; and sharper error bounds for an
already acquired local calculation. The central open question is how to
turn these into useful bounds on complete gap paths and ultimately into
coverage of every possible collision.

This reading follows [Continuation55][n55], the [live register][register]
and the [107-page manuscript guide][guide]. [E47][assessment] records
internal acceptance within the fixed-input, counted-chart and
inherited-certificate scope, not specialist validation. The
[result index][results] and [avoid index][avoid] supply the wider context,
especially [Cluster18][cluster], [Controls12][controls],
[classification01][classification], [premises02][premises],
[scope07][scope], [joint bounds12][joint-bounds] and [volume20][volume].

## Background and the central equation

The Newman heat family changes the Riemann xi function continuously with
a parameter t. At t=0, reality of all its zeros is RH. The
de Bruijn–Newman constant Lambda is the threshold above which all zeros
are real; RH is equivalent to Lambda<=0. Rodgers and Tao proved
Lambda>=0. Their [paper abstract][rt], already cited in the shared
bibliography, confirms these background statements. The present project's
global aim is downward continuation from an established all-real time,
eventually improving an upper bound.

Write a counted conjugation-invariant pair as c±s and put D=s². For a
real pair, D is one quarter of the squared gap. D=0 is a merger; D<0
describes a nonreal conjugate pair. These symmetric coordinates remain
regular at a merger. A counted contour is a surrounding curve on which
the function is proved nonzero and which contains exactly the intended
number of zeros, including multiplicity.

[Manuscript §1][framework] derives the physical-time law

\[
 D'=2-4DM,\qquad
 M=\sum_{\rho\text{ exterior}}\frac{1}{(\rho-c)^2-D}.
\]

The constant 2 is the pair's intrinsic separation rate in increasing
time. M accounts for every other zero, including nonreal zeros. In
decreasing time an isolated pair's D falls toward zero, so controlling
the exterior interaction matters to downward continuation. At a merger
D'=2: regularity of the equation does not prevent the event.

The moments S_n and T_n record successively finer inverse-distance
information. M=S_1; its evolution involves S_2 and S_3, whose equations
need higher moments. The [integer hierarchy, §2][integer], closes as an
infinite system. The [coupled lattice, §4][lattice], imposes compatibility
between adjacent pairs sharing roots and the same exterior field.

The two poles also have separate exponents. [§3][split] defines
\(P_{p,q}=\sum_j(w_j-s)^{-p}(w_j+s)^{-q}\), where \(s=\sqrt D\)
and \(w_j=\rho_j-c\). Its proved recurrence uses nonnegative integer
p,q with p+q>=2. The complete S/T tower and this split-pole tower
are algebraically equivalent: S_n=P_{n,n}, while mixed entries supply
the odd information. Changing the sign of s exchanges the two indices;
regular symmetric combinations remove the labeling singularity at a
merger. Thus q and the square-root geometry are structural, not a minor
addition. The original conversational overview underemphasized them.

The complex-p construction in [§9][complex] extends the integer exponent
of the combined quadratic denominator to a complex moment exponent and
supplies contour representations. This is not yet a proved joint
complex-p,q hierarchy. [Discussion07][followup] explains the distinction,
the intended gap-error target and the author's localization suggestion. The
current manuscript is broader than that original direction. The
particular absolute contour estimates in [§11][bounds] do not beat the
equally informed grouped direct estimate; other joint signed estimates
remain outside that comparison.

## The recent developments

**One finite model now follows an entire interval.** [§6][common]
retains the complete initial zero divisor through radius N, including
opposite pairs, conjugates, ties and multiplicities, and evolves its
polynomial by the heat equation. The error is O(log N/N) at fixed height,
time interval and derivative order. [§7][transfer] transfers this to the
counted pair, every fixed complete exterior moment, forcing and transport,
with explicit error payments and matching across overlapping contours.

This is stronger than selecting a fresh approximation at every time.
It also preserves compatibility: all polynomial moments arise from one
divisor. Initial finite data, normalization and cleared contours remain
inputs. Practical acquisition and uniform control as height or moment
order grows remain open. The positive-time approximation theorem does
not inherit the separate local certificate's negative-time domain.

**The tested practical use of that theorem has been parked.** [§8][conditioning]
identifies the enormous loss in an origin-centered absolute estimate.
Centering near the pair and using one fixed calibration repairs that loss
while paying the entire Gaussian path. Nevertheless, the selected positive
absolute core estimate still makes the transport allowance too large.

The concrete consumer in [Appendix B][support] asks for logarithmic
transport error below 10^-6 on [0,1/1024]. The original allowance requires
log N>48,000,000 just for its first contour test. The centered replacement
is much better, but under N<=2^40 its resulting transport allowance,
when the transfer gates are available, still exceeds 7/65536, about
1.07×10^-4. This is a failure of the specified
absolute-envelope/count-tail/quotient allowance, not a lower bound on
actual error or on all finite methods. The register parks B05's tested
realization; increasing precision alone cannot remove these positive terms.

**The acquired direct calculation has become sharper.** [§20][correlated]
explains three distinct improvements, with comparisons in Appendix B:

| Improvement | Established change and comparison |
| --- | --- |
| Keep common logarithm errors in both moment readouts | More than 6.4031% narrower than the sharp independent-moment relaxation at the original source allowance. |
| Bound the actual interpolation operator | Replacing the old amplification allowance 1100 by a proved factor below 17 produces a centered interval more than 33.9494 times narrower than its preceding centered baseline. |
| Constrain annular Fourier errors jointly | At least 5% less annular allowance and more than 2.4% less complete outward-parsed endpoint width, with all other payments retained. The inequality is proved; the new endpoint serialization remains unexecuted. |

These have different baselines and cannot be combined into one percentage.
The first two are completed interval calculations. The third is the
accepted analytical basis for E44 and is available to an equally informed
direct method.

The earlier certified result covers one pair near x=14010.1 on
[-0.0003,0.1], with

\[
 \min_tD(t)=D(-0.0003)
 \in[0.00082198577,\ 0.00082200876].
\]

A derivative bound paid throughout the interval identifies the minimum;
endpoint samples alone would not. This is substantial local source
coverage. The pair was already securely separated before the newest
refinement. Narrower uncertainty does not protect another pair, extend
the physical interval or improve a global Newman bound. The separate
388-root census still needs its own forward source tube.

## Questions worth pursuing

Under [classification01][classification], these are prospective finite
quantitative milestones or research questions. No new global sign
criterion is asserted. Success must change a complete error bound,
covered region or measured cost with every error contribution retained.

1. **Finish the already justified endpoint refinement.** E44 can
   materialize the annular saving using exact rational arithmetic; E45
   must assess the artifact. Its frozen execution gate is a 2% total-width
   improvement. This is bounded completion work. It remains unexecuted as
   of this discussion.

2. **Estimate the final observable while retaining common errors.** This
   is my preferred conceptual question. A common multiplicative
   normalization disappears from H_z/H, while separate numerator and
   denominator error bounds can lose that cancellation. Can relative,
   derivative and time correlations survive the Gaussian evolution and
   contour transfer? The [complete adjoint identity in §19][two-sided]
   offers another existing way to weight errors by their effect on final
   D, retaining quadratic terms and anchor errors.

   Here “final observable” means D at a specified time, or the minimum
   of D over a specified interval when the claim concerns a full path.
   It does not mean that a positive endpoint alone protects the interval.
   The objective is to bound the error in that quantity while preserving
   dependencies among its inputs. Discussion07 gives a common-shift
   example and an exact quotient-error identity.

   A meaningful first target is the existing 10^-6 transport tolerance on
   the short tube at a declared feasible data budget, or a strictly larger
   certified time interval at the same source budget. Quotient cancellation
   is an identity, not yet that estimate. Work on zero-free contours and
   retain independent counts and floors. Compare against direct evaluation
   of the same observable with the same correlations.

3. **Test whether realizability makes a short hierarchy stable.** Specify
   a small state arising from one divisor or an admissible analytic
   exterior, using §4's shared-root relations. Keep the complete exterior
   of any small counted block. The missing result is a useful
   finite-duration error bound for unresolved rows, including their initial
   uncertainty. The compatible polynomial supplies the reference model.
   [§5][finite] shows why the particular independent positive absolute
   propagation allowance can diverge despite a small boundary residual;
   it does not prove instability of every constrained closure.

4. **Protect every eligible gap in a counted block.** Block length can
   remain controlled while one gap closes and others widen. A worthwhile
   geometric milestone would control the minimum or a complete failure
   count, paying both boundary forces and changes of chart. Symmetric
   block coordinates can survive an internal merger when adjacent-pair
   charts cease to apply. The conservation child offers exterior-flux
   identities, but a positive quartic invariant can coexist with collision.
   Its contribution must improve the full gap calculation, including the
   affine response, coordinates and time errors. A failure-count upper
   bound below one excludes failures only for a complete eligible population.

The [closing §21][discussion] identifies the eventual bridge: compact
and high-height regions must cover a common physical interval with cleared
interfaces and no omitted exits. Positive-time exterior estimates give no
automatic uniform passage to zero. This is the eventual coverage test;
another percentage improvement on one safe pair is an accuracy result.

My preference is to complete the endpoint artifact, then choose one
observable-specific correlation question with a fixed success measure.
Scale to blocks after that question changes a complete budget or coverage
claim. Repeated forward/backward sweeps with fixed exact relations do not
add information to the complete joint feasible set; §19 proves this.
Better dependency representation, new observations or sharper transition
bounds must supply any strict gain.

## Collision controls for these proposed uses

The [Controls12][controls] witnesses were screened analytically against
these uses and the manuscript's [E40 premise table][e40]. This is not a
new numerical replay of their certificates. No future estimate above is
already proved to distinguish theta from every colliding source. A
generic error theorem must preserve an eligible control's collision;
only a separately established canonical margin can exclude an event.

| Control class | Failed canonical premise or event that must remain |
| --- | --- |
| Quadratic and strong-collar quartic heat fields | Generic approximation inputs can hold with zero truncation error at a merger. Literal theta source equality fails. E40's exact quartic shows that compatibility and accurate approximation do not exclude collision. |
| Annular quadratic controls | A shifted double can pass the fractional-reduction geometry; retaining the entire square must still enclose D=0. The zero-centered inherited control fails the particular h/r guard and cannot receive the blanket 19/20 contraction. |
| Euler-factor translates | The unchanged normalized theta source fails. Generic count/product and error inequalities may survive. |
| Weighted-square, finite-source and finite-score perturbations | Full reflected unit-weight theta identification fails; documented endpoint-defective subclasses also lack the imported strip. Preserved finite moments or scores do not restore these premises. |
| Finite-prime orbit perturbations | Full reflection/source identity fails despite the stated finite-prime and measurement agreements. No obstruction to infinite assembly follows. |
| Reflected super-Gaussian | The particular order-one product premise and literal theta identification fail; local heat and contour identities can still preserve its event. |
| Smooth shape and positive-primitive sources | Complete theta arithmetic and transfer of the particular canonical source certificate are absent. Positivity or endpoint data alone gives no canonical margin. |
| Atomic thresholds and finite-profile constructions | Full theta/profile identity fails. Atomicity or lack of a lower count asymptotic is not itself a failed premise of the approximation theorem. |
| RH-conditional endpoint mergers | Ordinary Dirichlet arithmetic changes and RH is a construction premise. Fixed-compact approximation gives no escaping-height exclusion. |
| Changed observation kernels | The physical cosine/Newman readout fails. |
| Fractional-profile relaxations | Integer multiplicities and actual divisor realization fail. |
| Static divisor surgery or arbitrary scalar/moment states | A supplied common canonical heat path or divisor realization is absent. Slice agreement alone does not supply it. |

The required distinction is between a valid generic approximation and
a favorable actual-source estimate. No missing source identity is being
claimed to force failure of every coarse numerical majorant. All negative
conclusions above retain their stated estimate classes.

## Reading order

Read §1 for the pair law, then §§2–4 for the hierarchy and compatibility.
For the recent work, read §§5–8 in order: the independent-tail limitation,
compatible construction, observable transfer, and conditioning. Read §20
with Appendix B to distinguish the analytical refinements and numerical
comparators. §19 supplies the two-sided framework; §21 states the open
challenges. The [guide][guide] maps printed section numbers to historically
numbered source filenames.

[n55]: ../../notes/55_VCD_GT_CM_ANALYTICAL_MANUSCRIPT_CONTINUATION_20261118.md
[register]: ../../research-progress/01_VCD_GT_CM_RESEARCH_PROGRESS_20261117.md
[guide]: ../../manuscript/README.md
[assessment]: ../../reviews/26_VCD_GT_CM_E47_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261118.md
[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[cluster]: ../../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[classification]: ../../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint-bounds]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[volume]: ../../../../../../../avoid/20_volume_without_a_gain.md
[rt]: https://arxiv.org/abs/1801.05914v5
[framework]: ../../manuscript/sections/01_framework.tex
[integer]: ../../manuscript/sections/02_integer_hierarchy.tex
[split]: ../../manuscript/sections/03_split_poles.tex
[lattice]: ../../manuscript/sections/14_coupled_lattice.tex
[complex]: ../../manuscript/sections/04_complex_powers.tex
[bounds]: ../../manuscript/sections/06_bounds_transport.tex
[finite]: ../../manuscript/sections/10_finite_hierarchy.tex
[common]: ../../manuscript/sections/20_common_time_approximation.tex
[transfer]: ../../manuscript/sections/21_counted_transfer.tex
[conditioning]: ../../manuscript/sections/23_conditioning.tex
[correlated]: ../../manuscript/sections/22_correlated_enclosures.tex
[support]: ../../manuscript/sections/16_supporting_compact_example.tex
[two-sided]: ../../manuscript/sections/19_two_sided_refinement.tex
[discussion]: ../../manuscript/sections/07_discussion.tex
[e40]: ../../reviews/22_VCD_GT_CM_E40_COMMON_TIME_APPROXIMATION_ASSESSMENT_20261118.md
[followup]: 07_VCD_GT_CM_SPLIT_POLES_OBSERVABLES_AND_LOCALIZATION_20261118.md
