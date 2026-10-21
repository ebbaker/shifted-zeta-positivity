# Analytic program for heat root motion and signed contours

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. Internal research planning; no specialist review.

Study the motion, size and phase distribution of a selected root cap,
then determine whether a signed contour identity supplies a quantitative
constraint specific to the complete theta source. The immediate objective
is an analytic estimate for root motion or boundary transport. The eventual
application is BW10's conditional simplicity problem.

This direction comes from the author's suggestions in
[brainstorm 03][discussion]. The [matching progress note][progress] tracks
**HMC-00–07** (heat motion and contours). It is a focused continuation within
the
[parent RH-to-simplicity program][parent], whose RHS task statuses remain
separate. The [canonical manuscript][manuscript] now includes Notes 17–18
in Sections 5–7; its approximation theorems are background, not automatic
estimates for the moving contour.

The [result index][results], [local heat geometry][heat-summary],
[hypercomplex constructions][geom-summary], and [avoid index][avoid]
govern the starting point. In particular, apply the rules on
[target reformulations][a01], [control premises][a02],
[coordinate lifts][a03], [scoped exclusions][a07], and
[complete signed estimates][a12].

## Scope and normalization

Retain the original theta family

\[
H(t,x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,
\qquad H_t=-H_{xx},\qquad
8H(0,x)=\xi\!\left(\frac12+\frac{ix}{2}\right).
\]

For the conditional endpoint problem, assume RH and a zero of exact
finite multiplicity `m>=2` at `(0,a_0)`, with `a_0>0`. RH supplies simple
all-real zeros at every positive time. Start the quantitative motion
calculation with an adjacent pair born from a double zero; extension to
arbitrary multiplicity is an explicit later task. A proof for that pair
alone would leave higher multiplicities unresolved.

Write the selected roots as `a(t)<b(t)`, their gap as `g=b-a`, and their
center as `c=(a+b)/2`. Distinguish the physical coordinate `x=2 gamma`,
heat time `t`, source coordinate `u`, and the large-time scale `L_t`.
No bounded event height, lower derivative bound, or uniform gap to the
other zeros is part of the hypothesis. A first estimate may cover a
specified finite range, with its parameter dependence recorded.

The cap is the finite interval `[a(t),b(t)]`. Increasing its heat time,
exhausting a source contour, and exhausting ordinate height in a norm
are different operations. Every limit must retain its own remainder.

## Established starting points

[Note 01, Section 2][n01] proves continuation of fixed positive root
labels under RH. The [BW09 manuscript][bw09] proves the complete-source
large-time cosine limit. Their combination in [brainstorm 03][discussion]
gives, for fixed adjacent labels `k,k+1`,

\[
g_k(t)=\frac{\pi+o(1)}{L_t},\qquad
c_k(t)=\frac{k\pi+o(1)}{L_t},\qquad
4\pi e^{4L_t}=2tL_t+9,
\]

with `L_t ~ (log t)/4`. This does not give uniformity in `k`, an explicit
onset time, or differentiated asymptotics. For a double birth,
`g(t) ~ 2 sqrt(2t)` near zero. These two regimes allow a positive gap
with a finite maximum and a limit of zero only at infinite time.

Brainstorm 03, Section 3 also gives the finite enclosure
`|g_k-pi/L_t| <= 2 arcsin(epsilon_0)/L_t`, with
`epsilon_0=Z E_mu|U-L_t|/L_t`, under its stated root-neighborhood,
derivative and rank-identification conditions. Thus the moment-to-width
comparison is already available. Effective uniform moment bounds and
heat-time differentiation remain additional work.

The paired product and the heat equation give the exact gap balance
recorded in the brainstorm:

\[
S_{\rm ext}(t)=\sum_{r\ne a,b}\frac1{(b-r)(a-r)},\qquad
g'=\frac4g-2gS_{\rm ext},\qquad
(g^2)'=8-4g^2S_{\rm ext}.
\tag{1}
\]

Here the sum includes all other signed real roots and is absolutely
convergent. It is nonnegative because the pair is adjacent. The center
velocity requires a consistently paired or principal-value sum. The
double-birth consequence `g(t)<=sqrt(8t)` is a baseline quantitative
bound compatible with a multiple endpoint.

For the physical jet `J=H+iH_x`, the cap-phase decrease is exactly `pi`
while the pair remains adjacent. The outer cap of an `m`-fold cluster
has baseline `(m-1)pi`. A strict finite surplus is the existing
contradiction target, not a new milestone. Likewise, by (1), making
`integral_0^t g^2 S_ext` reach `2t` at a finite time restates a
double-pair collision. Numerical checks of these reformulations do not
provide evidence for the missing estimate.

Investigation 21 provides two useful signed representations:
[Note 46's spectral-circle current][g46] and
[Note 50's closed-form Stokes flux][g50]. They retain the relevant
orientation but do not yet bound it at physical first-jet scale.
[Note 57][g57] quantifies the loss from paying positive and negative
boundary masses separately. These are existing inputs, not unfinished
constructions to be repeated.

## First analytic checkpoint

21 October 2026 — **gpt-6-astra, actual effort max**.
[Note 19][n19] proves HMC-01's explicit complete-root tail, paired center
and gap remainders, rank-dependent finite-time enclosure and moving
deflation. Its mirror-root comparison supplies a finite-interval width
bound for HMC-03. [Note 20][n20] proves the proposed differentiated
fixed-label asymptotics in (2), with explicit finite moment/error bounds
and a sufficient shrinkage test. Every fixed adjacent gap eventually
decreases; no numerical onset or multiple-zero exclusion is claimed.
[Review 19][review19] is a same-assistant self-review. That checkpoint
selected HMC-04 for continuation; its bounded result is recorded next.
The task definitions below retain their original completion requirements.

## Moving-tube checkpoint

21 October 2026 — **gpt-6-astra, actual effort max**.
[Note 21][n21] completes HMC-04 on bounded product tubes over the moving
cap, on compact positive-time intervals. It proves the full signed
transport, all-face Stokes formula, physical-weight correction and explicit
trace/time-derivative payments. An exact primitive change reduces the
construction to a planar transverse average. Under RH its value lies
between `pi` and `pi+g eta^2 D0/6`; generic all-real-product positivity
supplies the lower bound. The quadratic double model has trace error at
least `eta^2/(2t)`. Thus the selected tube supplies no new signed gain
or unpaid endpoint-uniform recovery. [Review 20][review20] is a
same-assistant self-review. HMC-05 now has an explicit complete two-source
residual to assess, but no separating theta estimate.

## First HMC-05 comparison

21 October 2026 — **gpt-6-astra, actual effort max**.
[Note 22][n22] analyzes that residual at `eta=r sqrt(2t)`. Conditional
on a fixed multiplicity event, it gives an explicit complete-source
`O(sqrt(t) log(1/t))` error around the Hermite tube profile, using the
exact physical phase measure. The double profile is `pi(1+r^2)`;
the outer profile is `pi[L_(m-1)^(1)(-r^2)-1]`, proved for every fixed
finite multiplicity. The error is uniform for bounded `r` and retains
event dependence. A separate local analytic version handles controls
without an all-real heat slice.

Matching controls share the leading profile. This completes a bounded
comparison and closes the proposed leading-profile discriminator, not
HMC-05's separating-estimate requirement. The next bounded question is
the first surviving nonuniversal correction, with its complete-source
payment and close-control comparison. [Review 21][review21] is a
same-assistant self-review; no endpoint exclusion follows.

## Surface curvature checkpoint

21 October 2026 — **gpt-6-astra, actual effort max**.
[Note 23](../notes/23_CAP_PHASE_CONCENTRATION_AND_FINITE_TIME_BASELINE_20261021.md)
separates coordinate cap shrinkage from image length and records the exact
finite-time quadratic tube baseline. Its correction already contains
`-r² sqrt(2t)`, so the leading Hermite profile alone is not the baseline
for a source-dependent correction.
[Note 24](../notes/24_GAUSS_AREA_CONCENTRATION_AND_CURVATURE_FLUX_20261021.md)
proves that the induced jet surface has local Gauss-area concentration
`pi(m−1)` at a multiplicity-m event, with an explicit fixed-boundary
error. The double control has finite total area `2pi` on both sides of
the event; the four-dimensional Ricci-form integral retains that
concentration times the transverse area. Thus bounded total curvature
does not imply endpoint regularity for this observation.

The [gate assessment](../reviews/22_HMC06_GATE_AND_ENDPOINT_LIMIT_REVIEW_20261021.md)
and [curvature review](../reviews/23_GAUSS_AREA_AND_CURVATURE_FLUX_REVIEW_20261021.md)
retain HMC-05 open and HMC-06 gated. These are internal same-model
assessments. The signed real-angle estimate remains absent; the
curvature calculation does not evaluate the original tube's first
source-dependent correction or exclude other geometric observations.


[Note 25](../notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md)
addresses the proposed multiplicity-selective refinement. The Gauss defect
already vanishes for simple zeros; Investigation 22's complex heat-jet
degree becomes a relative second Chern/Hopf number with weight binomial(m,2).
An explicit positive regularized curvature-square measure has precisely
that limiting mass. These are local section invariants, distinct from the
fixed arithmetic theta-bundle class and the hyperkähler tangent classes.
The double polynomial has charge one even on flat hyperkähler space.
No theta-specific upper bound is supplied, so HMC-05/06 statuses are unchanged.
The addendum to [Review 23](../reviews/23_GAUSS_AREA_AND_CURVATURE_FLUX_REVIEW_20261021.md)
checks the normalization and scope; it is a same-assistant assessment.

## Analytic tasks and completion requirements

### HMC-00 Record the contract and inherited results

Keep the normalization, selected root labels, multiplicity scope,
baseline cap phase, and source references together. Classify each new
claim as an identity, a quantitative estimate, a conditional criterion,
or a scoped obstruction. This planning task is complete in this note
and the progress register; it does not complete any of the estimates
below.

### HMC-01 Control the complete root equations

Establish the gap and center equations with consistent summation and
uniform remainder bounds on `epsilon<=t<=T`. Separate nearby roots from
the complete distant tail. Use the source growth bound and a zero-count
estimate with explicit parameter dependence to bound that tail; a
finite root list without this payment is insufficient.

An initial quantitative target is a distant contribution bounded by
`C_(epsilon,T,A) (1+log R)/R` when the endpoints satisfy `|a|,|b|<=A`
and `R>2A`. Prove the counting input and both summation conventions
before using this rate. State how the enclosure `A` is obtained and
where its root-label dependence enters.

Audit the equivalent deflation
`R_t(z)=H(t,z)/((z-a(t))(z-b(t)))`, with removable endpoint values,
as a way to relate exterior interactions to the complete function.
Retain the heat terms produced by moving the two factors. Division
near time zero must be checked separately for double and higher-order
births.

**Completion:** a proved tail inequality and a justified finite/complete
comparison for both velocities. Re-deriving (1) alone is insufficient.

### HMC-02 Differentiate the complete-source saddle estimates

Develop explicit bounds for the normalized profile
`F_t(z)=H(t,z/L_t)/H(t,0)`, its spatial derivatives, and its heat-time
derivative, using the existing moment-to-width comparison. Use the complete
probability law
`d mu_t=e^(t u^2) Phi(u) du/H(t,0)`; differentiation of a fixed observable
is governed by `Cov_mu(U^2, observable)`. Moving rescaled arguments also
contribute the `L_t'` term.

The exact saddle equation gives

\[
L_t'=\frac{2L_t}{8tL_t-2t+36}.
\]

A specific test is whether one can prove, for fixed labels,

\[
g_k'=-\frac{\pi L_t'}{L_t^2}
       +o\!\left(\frac{L_t'}{L_t^2}\right),\qquad
c_k'=-\frac{k\pi L_t'}{L_t^2}
       +o\!\left(\frac{L_t'}{L_t^2}\right).
\tag{2}
\]

Equation (2) was the proposed theorem and is now proved in
[Note 20][n20] by complete-source covariance cancellation, with an
explicit smaller-order remainder. It is not obtained by differentiating
the existing `o(1)` location error.
Retain all theta indices, remote source tails and normalization
derivatives. Give finite error bounds where possible, including the
root-neighborhood and derivative conditions needed for enclosure.

**Completion:** a controlled differentiated estimate, with a stated
range and constants or parameter dependence. Eventual shrinkage would
be a dynamical result; it would not itself exclude a multiple endpoint.

### HMC-03 Connect the birth and intermediate time regimes

Use the local Hermite expansion with explicit event-dependent remainders
near zero. On positive compact time intervals, combine HMC-01 with
complete-source information to bound the gap, center, and exterior
compression. Connect those intervals to the regime of HMC-02 without
losing the selected root labels.

Seek at least one effective estimate not supplied by continuity alone:
an enclosure for a turning time or maximum gap, a bound for accumulated
exterior compression, or an intermediate-time width enclosure with a
specified remainder. An estimate may be limited to declared event data;
the unresolved dependence on `a_0`, `m`, and local derivative ratios must
then remain visible. Existence of a maximum from the two limiting
regimes is already known and is not this task's completion.

**Completion:** one proved quantitative bound over a stated time range,
or a precise obstruction for the selected estimating class.

### HMC-04 Transport a signed contour observation with the cap

Use the fixed interval `-1/2<=y<=1/2` and
`K(t,y)=H(t,c(t)+g(t)y)`. The chain rule gives the starting identity

\[
K_t=-g^{-2}K_{yy}+\frac{c'+g'y}{g}K_y,
\qquad J=K+i g^{-1}K_y.
\tag{3}
\]

Derive the signed phase or boundary-current transport with every
moving-coordinate term retained. Replacing the physical derivative by
`K_y` changes the phase density even when it preserves total winding.
Keep that distinction in any comparison of concentration scales.

For the geometric calculation, first use the existing polarized
Stokes identity on a declared family of bounded four-dimensional
domains. Specify the physical trace, orientation, auxiliary thickness,
and all boundary faces. Derive the moving-domain terms and the estimate
needed to recover the physical line observation. These fixed-time
holomorphic-form domains are distinct from the Fueter lift's auxiliary
complex heat coordinates. An octonionic version must specify its
projection and multiplication order and justify its own trace.

At an interior stationary point one may also use Note 46's circle
identity, with its full stationary condition. This point is not
automatically the midpoint `c(t)`. Any rule locating it and any varying
radius must be included in the calculation.

**Completion:** a complete transport identity **and a quantitative
boundary/trace remainder estimate** for a declared domain class. Compare
the result with the planar calculation using the same source information.
If the construction only reproduces the existing cap budget, record
that scope without calling it a signed gain.

### HMC-05 Obtain an additional theta estimate

Choose the single term exposed by HMC-01–04 that still needs control.
Derive a bound from the unchanged theta arithmetic, retaining the
complete signed source before estimation. State the comparison constant,
rate, or strict margin that improves the existing bound, and identify
exactly where the control families cease to satisfy its hypotheses.

Possible inputs are the complete two-source covariance/current or the
theta jet-bundle structure in [Note 62][g62] and its
[continuation program][g63]. If the bundle is used,
establish its transition and connection terms for the chosen observable
and retain the physical weight `exp(t (log y)^2/16)` and Mellin phase.
The Jacobi heat equation is a different evolution. A new ambient metric
or cycle is useful here only if it supplies the stated estimate.

**Completion:** an independently proved quantitative gain at the
scale needed by the selected consumer, or a bounded-class obstruction.
Generic source positivity, separate Hodge norms, a renamed unknown sign,
or a count of successful numerical samples does not complete this task.
Notes 17–18's scoped arithmetic-transfer obstructions remain in force
if a changed heat normalization is introduced; they do not prohibit
geometric uses of the original heat flow.

### HMC-06 Apply the estimate with explicit endpoint coverage

Connect HMC-05 to the selected finite-contour contradiction or to a
direct exclusion of the original endpoint. Pay endpoint deficits,
continuation, source remainders, and any terminal-boundary regularity.
For `m>2`, retain the complete Hermite cluster: other members of the
birth cluster contribute singular terms to an adjacent pair's exterior
interaction near zero. A double-isolation bound cannot be reused without
those terms.

**Completion:** a theorem excluding an explicitly stated class of
multiple endpoints, or a complete all-height/all-multiplicity argument.
A finite-height or multiplicity-two conclusion must state its remaining
complement. The established cap phase and the putative contradiction
cannot both be treated as independent new information.

### HMC-07 Review the analytic argument and consolidate its result

Check normalization, summation, all parameter dependencies, limit order,
boundary orientation, and the control responses. Compare any geometric
estimate with its planar counterpart on the same information. Preserve
successful bounds and narrowly stated failures even if HMC-06 remains
open. Specialist review remains distinct from internal LLM checking.

**Completion:** a review tied to actual estimates and a concise update
of the progress register. Amend the manuscript and result indexes only
when a substantive result warrants it; do not create snapshot folders.

## Order of work

The initial work order began with HMC-01 and HMC-02; their declared
analytic estimates are now in Notes 19–20. HMC-03 has the finite-interval
width bound, with turning-time and maximum-gap refinements still open.
HMC-04 is complete for Note 21's declared product tubes, with no geometric
sign gain. Note 22 completes HMC-05's first bounded comparison: its paid
leading profile is shared by the controls. Next derive and screen the
first surviving nonuniversal correction, initially for a double event.
HMC-05 remains open and HMC-06 depends on a new separating estimate;
HMC-07 reviews each completed analytic unit and the eventual combined
argument.

This ordering gives useful quantitative outputs before the final
simplicity question is resolved. It does not require a numerical scan
to select the next analytic inequality.

## Control comparisons

Use the [collision-control register][controls] and the detailed
[brainstorm screen][discussion]. Apply each proposed estimate only where
the control satisfies its actual hypotheses.

| Control | Required comparison |
| --- | --- |
| Quadratic and Hermite heat polynomials | Recover local splitting and the gap balance exactly. They lack the unchanged infinite theta source; passing these identity checks is expected. |
| `1+e^t cos x` | Recover gap `2 arccos(e^-t)` and cap phase `pi`. Its atomic source lacks theta's large-time saddle law. |
| Euler-factor control with `c=1`, under RH | Retain its multiple endpoint and later simple all-real roots. A separating step must use the changed coefficients or completion quantitatively. |
| Weighted-square and finite-prime controls | Identify the failed full-reflection premise. Finite-source examples lack an all-real slice, so do not apply an all-real-root equation to them. |
| Reflected and positive-primitive controls | Their generic lifts and boundary identities survive; the original normalized integer-square expansion does not. |
| BW10's close positive-source endpoint controls | Preserve their leading-tail and completion data in the comparison. Their ordinary Dirichlet arithmetic fails; do not combine their properties with those of a different control. |

If a proposed exclusion uses only hypotheses shared by a colliding
control, narrow or replace that estimate. A failure of one domain, norm,
radius rule, or truncation class is not a prohibition on all contour
methods.

## Numerical support

Numerics support a named analytic task after its formula and domain are
fixed. They do not decide whether an equivalent simplicity criterion is
true. The useful supporting calculations are:

1. **Exact algebra:** check signs, factors and moving-coordinate terms on
   the quadratic, atomic and Hermite models. These checks support
   HMC-01 and HMC-04; they do not verify infinite tails.
2. **Bounded root and moment enclosures:** compare proved error bounds
   with actual theta data on a finite label/time range. Certify root
   membership and uniqueness using complete-function bounds, rather
   than relying solely on an ODE tracker. Use controls for hypothetical
   multiple births; do not invent an original theta double zero.
3. **Signed boundary evaluation:** evaluate the complete current on a
   fixed contour with certified source, quadrature, and boundary errors.
   Preserve cancellations before taking absolute values. A visual sign
   or small residual is supporting evidence only; an interval result
   proves only its stated finite claim.

Before a run, record the analytic question, fixed range, exact observable,
tail theorem, precision and truncation budget, and a stopping condition.
If the bound or enclosure cannot resolve the question within that
budget, report that limit rather than expanding the scan. A physical
energy denominator requires an independently certified nonzero lower
bound on the sampled domain; such a bound cannot be assumed near the
unknown endpoint in the analytic theorem.

Save derivations in `notes/`, supporting calculations and small execution
records in `numerics/`, and assessments in `reviews/`. Retain brainstorms
and the uniquely registered [chat 0005][history] at their existing homes.
Follow [LARGE_FILES.md][large] for any derived output. No numerical
campaign is launched by this planning note.

[progress]: ../research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[parent]: 01_RH_TO_SIMPLICITY_PROGRAM_20261020.md
[discussion]: ../brainstorm/03_HEAT_ROOT_MOTION_AND_HIGHER_DIMENSIONAL_CONTOURS_20261021.md
[manuscript]: ../manuscript/main.tex
[n01]: ../notes/01_FINITE_WALLS_ARITHMETIC_RESOLUTION_AND_GAUSSIAN_SCREEN_20261020.md
[bw09]: ../../09_expanding_contour_later_collision/manuscript/main.tex
[history]: ../chat-histories/0005_2026-10-21T04-09-04Z_review-threshold-route-manuscripts.json
[results]: ../../../../../../../result-summaries/README.md
[heat-summary]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[geom-summary]: ../../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[large]: ../../../../../../../LARGE_FILES.md
[g46]: ../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/02_signed_cusp_control/46_OCTONIONIC_BOUNDARY_CURRENT_AND_SIGNED_CUTOFF_TARGET_20261015.md
[g50]: ../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/04_octonionic_reductions/50_QUATERNION_FORMS_HODGE_PAIRING_AND_SOURCE_TARGET_20261015.md
[g57]: ../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/02_signed_cusp_control/57_CIRCLE_DEFECT_MULTIPLICITY_AND_RADIUS_20261015.md
[g62]: ../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/62_THETA_JET_BUNDLE_AND_SEMIFLAT_HYPERKAHLER_GEOMETRY_20261015.md
[g63]: ../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/00_research_coordination/63_MANIFOLD_GEOMETRY_AND_THETA_BUNDLE_CONTINUATION_20261015.md

[n19]: ../notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[n20]: ../notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[review19]: ../reviews/19_ROOT_MOTION_AND_DIFFERENTIATED_SADDLE_REVIEW_20261021.md

[n21]: ../notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md
[review20]: ../reviews/20_MOVING_TUBE_AND_TRACE_REVIEW_20261021.md

[n22]: ../notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md
[review21]: ../reviews/21_HEAT_SCALE_TRACE_AND_CONTROL_REVIEW_20261021.md
