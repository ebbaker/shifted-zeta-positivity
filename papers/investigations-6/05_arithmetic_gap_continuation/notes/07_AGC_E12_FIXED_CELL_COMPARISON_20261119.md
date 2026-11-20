# AGC-E12: one fixed arithmetic cell and its complete allowances

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Packet/helper dispatch: **gpt-6.1-sol / ultra**;
actual serving-backend model and reasoning-effort attestation were not
available to this helper. Python 3.10.0, python-flint 0.9.0, 192-bit
Arb/Acb interval arithmetic; the record supplies the actual runtime
version and source/implementation SHA-256 hashes. Internal nonauthor
assessment is separate; no specialist review or new coverage is claimed.

**Result.** The final closed-cell interval calculation acquires count two,
contour clearance, the full canonical source ratio and reference moments
for the frozen P33. With the **same acquired inputs**, the strongest
E10 logarithm allowance does not protect the whole time interval, while
the E13 centered/coupled allowance gives

    D_H(t) > 0.005414730535,  for every 9/100 <= t <= 1/10.     (1)

The complete source error includes both term errors and the entire
unretained Riemann--Siegel remainder. This is an improvement of a shared
local estimator inside earlier canonical coverage. It is equally
available to the direct endpoint comparator and the complete transport
identity; it is not transport superiority, an extension of known coverage,
or evidence for RH.

The frozen inputs are [B01 r2](../brainstorm/notes/04_AGC_B01_FIXED_PILOT_ADDENDUM_20261119.md)
and [E12](../research-progress/handoffs/AGC-E12-r1-request.md).
The [result index](../../../../result-summaries/README.md), especially
[approximation cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md)
and [Controls12](../../../../result-summaries/12_collision_controls_and_screening.md),
and the [patterns index](../../../../avoid/README.md), especially
[01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[04](../../../../avoid/04_counts_and_precision_as_evidence.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md),
govern the scope. Classification: a finite, matched quantitative allowance
comparison, not an RH-equivalent reformulation. Grid counts describe its
domain partition; they are not mathematical evidence by themselves.

## 1. Exact domain, scale and replay

Keep the Section 5 physical P_N, theta H and Section 6 exact defect.
There is no new reference, source, correction center or equation:

    X=140101/10, A=2, h=1, r=9/10, N=33,
    t_* = 1/10, U=1/100, 9/100 <= t <= 1/10,
    Γ: |z-X|=9/10,
    C=exp(πX/8),  H_scaled=C H, P_scaled=C P, E_scaled=C E,
    R_scaled=C(P_t+P_zz).

The positive scale C is constant in t,z and preserves the physical
unit-coefficient heat equation. The record verifies both strict/non-strict
natural-cutoff inequalities of B01 over the closed rectangle; the cutoff
is 33 throughout. r<min(A,h) also holds. No earlier Lehmer-pair source
archive, zero count or localization is used as an acquisition substitute.

Implementation: [agc_fixed_cell_comparison.py](../numerics/agc_fixed_cell_comparison.py).
Small record: [Record03](../numerics/03_AGC_FIXED_CELL_COMPARISON_20261119.json).
Replay with the existing Python environment specified in the request.
The script writes its single small JSON record and does not create an
archive. For a read-only assessor replay, import the script using
`importlib.util`, assign its `OUT` to a JSON path under `/private/tmp`,
and call its `main()`; this changes only the output destination.

## 2. What every interval and moment payment covers

Each time cell is the closed interval with exact rational endpoints
9/100+j/(100 n_t), j=0,...,n_t. Each closed contour arc is represented
by θ in [2πk/M,2π(k+1)/M], followed by interval sin/cos and
z=X+ρ exp(iθ). The same covers are used on radii ρ=4/5,9/10,1.
Arb's outward balls may enlarge these boxes; no sampled-only sign is
used. The partition covers every physical time and contour point.

The code evaluates the actual complex finite P_N and finite defect before
taking their moduli. The source allowance is exactly [E11 Note06 (5)](06_AGC_E11_SOURCE_ALLOWANCE_20261119.md),
including all 66 term-error contributions and the full remainder factor
1+δ_-+δ_+. The reference is not correction-aware. The imported source
domain applies on the r=.9 circle. Annulus boundary calculations use P
alone, so they do not require a source allowance outside that circle.

For every closed r=.9 arc it acquires a source upper bound V_k and a
strict denominator lower bound m_k. The reported complete relative error
is the **local-profile-retaining** bound

    q = max_k (V_k/m_k),

on each full time cell. The looser (max_k V_k)/(min_k m_k) is also retained
in the record and is not used for either compared gap allowance.

The all-arc inequality Re(P_scaled/(z-X)²)>0 proves winding number two:
the quotient remains in the right half-plane, and (z-X)² winds twice.
Thus Count(P_N)=2 and there are no contour zeros. On both annulus
boundaries the same positivity proves, by the harmonic minimum principle,
that f=P_scaled/(z-X)² has positive real part on the entire annulus.
Consequently its principal logarithm is single-valued and holomorphic
there, for every time in the cell. No logarithm through the interior
zeros is taken.

For ℓ_P=log f, let a_-1,a_-2 be its Laurent coefficients at X. The
inherited log-contour formula gives exactly

    c_P-X = -a_-1/2,       D_P = -a_-2-a_-1²/4.               (2)

The M-point trapezoid at r=.9 estimates these coefficients. With uniform
log bounds M_in on R_in=.8 and M_out on R_out=1, its alias payment for
a_-k, k=1,2, is

    M_out R_out^k (r/R_out)^M/[1-(r/R_out)^M]
      + M_in R_in^k (R_in/r)^M/[1-(R_in/r)^M].                (3)

This follows by the Cauchy bounds for positive and negative Laurent
coefficients and summing the two geometric alias tails. The code adds
that disk payment as a containing coordinate rectangle, hence slightly
overpays it. Ball arithmetic pays sample evaluation and assembly error.
Every sample retains the entire time-cell interval, so there is no unpaid
time interpolation or time quadrature. The maximum coefficient-alias
payment at the final geometry is below 5.787e-23. Equation (2) retains
the full complex square. Taking its real-part lower endpoint is justified
by exact conjugation symmetry of P and the count two, which make D_P real;
the recorded imaginary enclosure includes zero.

## 3. Complete all-time comparison at the accepted final geometry

The final geometry is 64 closed time cells and 512 closed arcs, all at
192 bits. The following decimal bounds are rounded conservatively from
the recorded ball endpoints, uniformly over the whole time interval:

| Quantity | Paid bound |
| --- | ---: |
| inf_Γ \|P_scaled\| | >975763.321419 |
| sup_Γ V_scaled | <196587.864108 |
| local max-arc q | <0.166453170631 |
| global-sup/global-inf q, retained for context | <0.201431766361 |
| \|c_P-X\| | <0.064495015773 |
| D_P | >0.141889609834 |
| strongest E10 transfer allowance, uniform upper | <0.154563575878 |
| E13 transfer allowance, uniform upper | <0.136474879299 |
| strongest E10 complete D_H lower allowance | >−0.012673966045 |
| E13 complete D_H lower allowance | >0.005414730535 |

For short reusable outward statements, exact rational comparisons against
the parsed outward fields in Record03 verify on **every final saved row**:

    q < .166454,       D_P > .1418896,
    B_E10 < .1545636,  B_ref < .1364749,
    D_H > .0054147.                                         (5)

These were obtained after the run by parsing the actual recorded Arb
endpoint strings at 192 bits and comparing them to the exact rationals
166454/10^6, 1418896/10^7, 1545636/10^7, 1364749/10^7 and 54147/10^7,
respectively. All comparisons returned true for all 64 rows; no new field
evaluation, geometric refinement or full-script rerun was used for (5).
The tested fields are q_raw_upper, D_P_lower, raw_gap_allowance_upper,
refined_gap_allowance_upper and refined_complete_D_H_lower.

The table's positive conclusion is (1). The negative E10 lower allowance
means that this allowance does not certify the entire path; it is not
an assertion that the true D_H is negative. In fact the final time cell's
E10 lower allowance is positive, while its first cell's is negative.
The E13 lower allowance is positive on **all** 64 closed cells. Counts,
denominators, source and reference-coordinate/alias payments hold on all
of them as well, so no endpoint-only conclusion is promoted to a path.
Rouché gives Count(H)=2 since q<1. Exact H conjugation symmetry then
turns positive D_H into two distinct real zeros in this circle.

For precision about the comparator, set d=|c_P-X|/r using the paid center
upper enclosure, λ=−log(1−q), and η=atanh q. The script records the
older independent-moment allowance r²[(1+d)λ+λ²/4], but compares against
the **stronger** [E10](04_AGC_E10_CONTOUR_ENDPOINT_20261119.md) allowance

    B_E10 = r²[λ sqrt(1+d²)+λ²/4].

The [E13 Note08](08_AGC_E13_LOG_DISK_ALLOWANCE_20261119.md) estimate used is

    B_ref = r² min{η sqrt(1+d²)+η²/4,
                         η+η d²/(2−η)}.                    (4)

η<2 is verified by the actual interval calculation. No numerical scalar
search is used. The reference D_P enclosure already includes (2)'s
arithmetic, time and alias uncertainty, and exactly the same enclosure
is used in both D_P−B lower bounds. The shared q, radius, count, scale,
center and complete source data are unchanged. The code verifies strict
allowance improvement on every time cell.

A separate exact-endpoint summary check pays a percentage comparison of
the **largest evaluated outward allowance** across the saved time cells.
The maximum saved E10 envelope has a lower bound >.154563575877,
and the maximum saved refined envelope has an upper bound
<.136474879299. Parsing those outward fields and taking Arb maxima at
192 bits verifies `new_max.upper() < (89/100)*old_max.lower()`.
Thus the worst evaluated allowance is reduced by more than 11 percent.
This uses a paid lower bound for the old evaluated envelope, rather than
dividing two upper bounds. It concerns these matched numerical allowances,
not the actual source error, a sharp information-theoretic optimum, runtime,
or the separate symbolic centered q=1/2 example in E13.

The direct comparator receives the same source and may use (4) as well.
This is a successful comparison of local allowances, not a representation
advantage over the equally refined direct estimator. It provides no total
runtime comparison against that estimator and no canonical coverage beyond
the already protected region containing this pilot.

## 4. Bounded heat acquisition: a scoped scalar loss

For each horizontal line reaching Γ the initial and lateral value bounds
need only |y|<=r=.9. They are acquired on y in [0,.9] and extended to
negative heights by exact conjugation. The initial x interval is [X−2,X+2];
both lateral x values are X±2, over the full physical time interval. The
E11 closed defect bound is acquired on the larger **h=1** rectangle.
This separates the actual paid domains; the value boxes are not claimed
to cover every height up to h=1.

The conservative scaled data are

    ε0 <327394.727397,
    M_b <326293.669246,
    ρ_full <26158.082276,
    βΓ(U) <7.357847918e-15.

Since M_b<ε0 is certified, [E10 heat (14)](05_AGC_E10_BOUNDED_HEAT_20261119.md)
gives ε0 S+M_b(1−S)+∫ρS <= ε0+Uρ. The evaluated uniform heat allowance
is below 327656.308220, compared with the direct contour value allowance
below 196587.864108. It does **not** improve that direct allowance.
No quadrature is omitted: the constant full forcing is integrated by the
safe Uρ payment, and the actual lateral data are absorbed using their
certified M_b<ε0 relation and S+Q_-+Q_+=1. The very small boundary
probability cannot remove the larger paid initial-rectangle norm.

This loss concerns these uniform rectangle data and this conservative
positive-kernel reduction. It is not a lower bound for the true error,
an instability theorem, or an exclusion of spatially dependent,
signed, joint or more sharply acquired bounded-heat estimates. No extra
heat/domain campaign is started. The direct comparator receives the
minimum of every valid acquired envelope.

## 5. Bounded execution, controls and limitations

The initial 16×128 geometry failed count/q gates through interval wrapping;
no count, nonvanishing or gap certificate is attributed to that attempt.
The 32×256 refinement acquired count, clearance and finite q but both
complete gap allowances still failed at the beginning of the time interval.
The final permitted 64×512 geometry produced (1). Arithmetic precision
remained 192 bits because geometrical enclosure width dominated; there
was no 256-bit run, new domain, parameter scan or alternative source.

An immediate startup repair replaced an Arb interval-equality comparison
used to identify the central radius by its loop index, before any complete
attempt was recorded. A bounded final implementation pass then retained
local-arc q, the stronger E10 baseline and both explicit E13 bounds, and
replaced an unnecessary floating maximum selector by Arb's interval max.
The final saved run took 98.814 seconds; the preceding complete acquisition
took 23.694 seconds. These are measured script runtimes; total packet wall
time was not independently recorded.
No broad test suite or additional numerical question was run.

The analytical control screens of E10 Notes04–05 and E13 Note08 apply
unchanged. In particular H=P=(z−X)²−2(t−T) has q=0 and zero transfer
allowance but D_P=0 at its merger: the strict complete margin fails there.
The physical Cluster12 collision classes likewise cannot satisfy a valid
strict count-two gap margin at their event; their documented failures of
full arithmetic, profile, reflection or the physical equation are named in
those notes. This canonical calculation imports no unchanged source budget
for a modified control, and no new control replay is claimed.

What is established is the specified finite allowance comparison and
its already-covered local positive result. It supplies neither a global
source theorem, new high-height/low-time region, improved Newman bound,
an independent human assessment, nor a transport/direct cost comparison.
Nonauthor replay and assessment should check the source import, the closed
domain covers, principal annulus log, (3), both complete margins and these
scopes before manuscript integration.
