# AGC-E12 r2: complete corrected-reference comparison

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Explicit retained helper dispatch:
**gpt-6.1-sol / ultra**; actual serving-backend model and effort were not
independently available to this helper. Python **3.10.0**, python-flint
**0.9.0**, **192-bit** Arb/Acb. One full run, no implementation repair,
geometry refinement or source/parameter search. The measured program
runtime was **84.05456337495707 seconds**; this is the program runtime,
not a separately measured total packet wall time.

**Result.** On the previous fixed cell, the accepted holomorphic correction
improves a complete all-time lower allowance, after reacquiring the new
reference's count, denominator, center, discriminant and source error:

    D_H(t) > .1493308659,  for every .09 <= t <= .1.           (1)

The previous P33 refined allowance was uniformly >.005414730535.
The new Q33 lower allowance exceeds the corresponding previous P33 lower
allowance on every one of the same 64 time cells. This is a paid finite
gain from retaining new correction information, inside already known
coverage. It is available to equally informed direct Q evaluation and
does not establish a transport representation or cost advantage.

This executes the [frozen r2 request](../research-progress/handoffs/AGC-E12-r2-request.md)
after the lead relayed the accepted analytical gate and after the author
read [Review05](../reviews/05_AGC_CORRECTED_REFERENCE_ASSESSMENT_20261119.md).
The [result index](../../../../result-summaries/README.md), particularly
[Cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md)
and [Controls12](../../../../result-summaries/12_collision_controls_and_screening.md),
and [patterns index](../../../../avoid/README.md), particularly
[01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[04](../../../../avoid/04_counts_and_precision_as_evidence.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md),
[12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and
[13](../../../../avoid/13_a_factor_is_not_the_target.md), govern the scope.
Classification: a fixed finite source-acquisition and complete-margin
comparison, not an RH-equivalent reformulation or a new coverage claim.

## 1. Frozen fields, one geometry and implementation provenance

Keep H, P33 and [Note10](10_AGC_E13_R2_HOLOMORPHIC_CORRECTION_20261119.md)'s
accepted Q33=P33−C_hol, with

    X=140101/10, A=2, h=1, r=9/10, N=33,
    9/100 <= t <= 1/10,
    fixed scale S=exp(πX/8).

The same constant scale multiplies H,P,Q,error and defect, preserving
the physical unit-coefficient heat equation. The natural-cutoff
inequalities are rechecked. The only geometry is **64 closed rational
time cells and 512 closed angular arcs**, on radii **4/5,9/10,1**.
There is no initial coarse grid or automatic refinement.

The [new script](../numerics/agc_corrected_reference_comparison.py) imports
the unchanged r1 program for its fixed constants, physical P/defect and
elementary kernel-free numerical primitives; it does not call r1's main
routine or write an r1 output. Both the base program and
[Record03](../numerics/03_AGC_FIXED_CELL_COMPARISON_20261119.json) are
hash-checked before use:

    base program: 9c6b6fd6f19cd716582f1569cea0d38ba0da3c7a3a2a4847bac78242d3160cda
    Record03:     6f97ba677fd59382dae07ef185e6ab51352a1aae952c761c230a918b3628fb05

They remain byte-for-byte unchanged. The sole new run produced
[Record05](../numerics/05_AGC_CORRECTED_REFERENCE_COMPARISON_20261119.json).
Its source manifest pins the new implementation, both r1 scientific files,
the accepted source/consumer notes, Review05 and frozen r2 contracts.
All source hashes stayed unchanged during the run. For a separate sole
scratch replay use the new script's `--output` option with a path under
`/private/tmp`; no mathematical input changes.

The new script and Record05 were frozen before separate numerical
assessment was requested:

    new script: 3a072c16aa929f6344a779d2bcb487898b27ba3d000a5a8c30b6b845d3e81166
    Record05:   d15913856684a5ebf2d85134585da371b70b84e3113a327c342f17ad2f21dba1

## 2. Correction, full source and complete defect payment

With k=π/8, w=z/2+kt, p=67−2sqrt(w/(2π)), the code evaluates exactly
the accepted finite formulas for C(p), C^sharp(p), A33(w) and
C_hol=J A33(w). The sharp function is evaluated as its analytic formula
with conjugated coefficients, not by conjugating the input p. The scaled
factor is evaluated stably as

    J_scaled=(-1)^34 sqrt(π)/4 exp[k(X−z)−k²t].

Every evaluated time/space box verifies the accepted local patch
9/50<Re p<6/25, |Im p|<1/400 and |2cos(πp)|>7/5. Principal square roots
are those of the positive-axis patch. The whole-rectangle holomorphy,
conjugation and derivative bounds are the accepted Note10/Review05
inputs; no global assertion about C's remote apparent poles is used.

At each closed r=.9 arc the complete physical source allowance is

    V_Q = S_term + L(δ_-+δ_+) + 12000 |J| |y|,                (2)

all multiplied by S. Both 33-term replacement sums remain. The delta
remainder is the **entire retained-correction remainder** of the accepted
source input. The full mismatch constant 12000 is used without derivative
optimization. The smaller allowance is assigned only to Q's newly
acquired coordinates and denominator, never to P's old center.

For bookkeeping the uniform scaled component maxima are bounded by

    term replacements <723.845528,
    retained remainder <15725.842534,
    vertical mismatch <5029.656218.

Their separate maxima need not occur on one arc; the recorded total
upper is the maximum of the complete arcwise sum (2), rather than an
unpaid subtraction from the old source envelope. On every time cell,
q_Q=max_arc(V_Q,arc/m_Q,arc), retaining the same local carrier profile.
The looser global-supremum/global-infimum ratio is retained only as context.

The exact physical corrected defect is

    R_Q=R_P−J A33''(w)/4.

The run deliberately acquires the permitted **conservative bound**

    |R_Q,scaled| <= |R_P,scaled|+350|J_scaled|,               (3)

using the accepted full-rectangle |A33''|<1400. It does not compute or
claim an exact signed complex enclosure of R_Q. On Γ, (3) is uniformly
<357.797450. A full **h=1 rectangle** bound also follows without another
source evaluation: the pinned old Record03 full-rectangle R_P bound plus
the accepted |J_scaled|<1 gives <26508.082276. This is a coarse global
triangle allowance, not a favorable cancellation or a heat-propagation
gain. The source-to-gap comparison below is an endpoint value consumer;
no scalar heat campaign or time-drift integral is run.

## 3. Direct corrected count, logarithm and reference moments

All three circles are checked directly with the new Q:

    Re[Q_scaled/(z−X)²] > 0

on every closed arc and time cell. This establishes count two on Γ by
winding. Positivity on both annulus boundaries propagates through the
annulus by the harmonic minimum principle and gives a principal
holomorphic logarithm there. The new calculation does not merely import
the analytic P-to-Q count transfer from Note10.

The 512-point Laurent trapezoid uses this Q logarithm. For k=1,2 its
two-sided alias payment is exactly

    M_out R_out^k (r/R_out)^512/[1−(r/R_out)^512]
     +M_in R_in^k (R_in/r)^512/[1−(R_in/r)^512],             (4)

with R_in=.8 and R_out=1. Both tails, arithmetic error and the whole
time-cell variation at every quadrature node are included. Each complex
alias disk is enclosed in a coordinate rectangle, a safe overpayment.
Both coefficient-alias bounds are <5.79e−23 on every time cell. There
is no unpaid spatial or time interpolation.

The Q Laurent coefficients give Q's **own** center and discriminant:

    c_Q−X=−a_-1/2,       D_Q=−a_-2−a_-1²/4.

The full complex square and its arithmetic uncertainty remain. Exact
conjugation symmetry and count two make D_Q real; the recorded imaginary
inclusions contain zero. The reference lower endpoints therefore already
pay moment evaluation, time variation and aliases.

## 4. Complete all-time results and the matched comparisons

The following strict outward summaries were checked against the actual
parsed endpoint fields on **all 64 final rows**, using 192-bit Arb and
the displayed terminating decimals as exact rationals. No further source
evaluation or geometry was used to prepare these summaries.

| Uniform paid quantity | Bound |
| --- | ---: |
| inf_Γ \|Q_scaled\| | >941112.530891 |
| sup_Γ V_Q,scaled | <21410.475449 |
| local q_Q | <.015234762 |
| \|c_Q−X\| | <.061075184 |
| D_Q | >.1617006119 |
| strongest E10 Q transfer allowance | <.012511448 |
| refined Q transfer allowance | <.012369746 |
| strongest E10 Q complete D_H lower allowance | >.1491891639 |
| refined Q complete D_H lower allowance | >.1493308659 |

All Q count/annulus/clearance gates pass. Since q_Q<1, Rouché gives
Count(H)=2 on every slice. Exact physical conjugation then makes (1)
a real distinct pair in Γ throughout the entire time interval. It is
not merely an endpoint statement.

For the **same Q inputs**, put d_Q=|c_Q−X|/r, λ_Q=−log(1−q_Q) and
η_Q=atanh q_Q. The two complete transfer allowances are

    B_E10,Q=r²[λ_Q sqrt(1+d_Q²)+λ_Q²/4],
    B_ref,Q=r² min{η_Q sqrt(1+d_Q²)+η_Q²/4,
                          η_Q+η_Q d_Q²/(2−η_Q)}.            (5)

The parabolic branch is used only with verified η_Q<2. The same Q
discriminant enclosure pays all common reference uncertainties on both
sides of (5). Strict refinement holds on every time cell; here both
complete Q lower allowances are positive. No pilot percentage is inferred
from two upper bounds or from E13's unrelated symbolic q=1/2 example.

The **new-source comparison** is separate. The accepted P pilot's best
refined uniform lower allowance is >.005414730535. The new refined Q lower
allowance is >.1493308659, and each new recorded lower envelope exceeds
the corresponding prior P recorded lower envelope. Q has its own paid
denominator, center and discriminant; the comparison therefore does not
spend a smaller error at P's coordinates. It establishes improvement of
the displayed complete lower allowances after new correction information
was acquired. It does not assert that the actual H discriminant changed.
An equally informed direct Q consumer receives precisely this correction,
source, count and refined estimator. No representation superiority or
total-runtime gain is claimed.

## 5. Work limits, controls and assessment boundary

One full 64×512/192-bit run took 84.055 seconds of recorded program
runtime, below the frozen 900-second runtime cap. No optional code repair,
failed geometry, extra numerical question, derivative-constant tuning,
new height/time or package installation was used. The new record is small;
no archive or manuscript snapshot was created. The r1 scientific files
remain pinned and untouched.

The [Note10/Review05](../reviews/05_AGC_CORRECTED_REFERENCE_ASSESSMENT_20261119.md)
controls remain applicable. The exact quadratic H=Q=(z−X)²−2(t−T) has
zero error and defect yet D_Q=0 at the event; the strict complete margin
fails. The unchanged theta retained budget is not assigned to Euler-factor,
weighted-square, finite-prime, finite-profile, reflected or primitive
controls. Their source-identification failures are separate from a
quantitative rejection. Finite-source lack of a global all-real anchor,
RH-conditional escaping-event scope and changed-kernel physical forcing
remain as stated in Controls12 and the accepted analytical screen.

This note reports a fixed complete allowance gain in known coverage.
It supplies no new Newman bound, no all-height or time-zero passage and
no universal claim about corrected references. The source theorem is an
accepted import; this implementation does not independently replay its
proof. Separate nonauthor code assessment and one scratch replay own the
numerical acceptance; none is claimed merely from this author's run.
