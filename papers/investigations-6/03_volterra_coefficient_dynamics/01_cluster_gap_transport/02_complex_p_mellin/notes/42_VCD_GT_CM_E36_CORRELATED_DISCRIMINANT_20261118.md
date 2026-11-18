# E36 — A narrower discriminant enclosure from shared contour errors

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual serving model and reasoning effort
unavailable; helper settings inherited. The proof and implementation have
the same author. Separate nonauthor assessment is E37; the
[sole progress register][register] owns live acceptance status.

**Status: proved in-note support comparison and completed interval
calculation, pending separate E37 assessment.** Keeping one logarithm
error in the two contour moments gives a **6.4031% narrower enclosure**
than their sharp independent-moment Cartesian relaxation on the fixed
pilot. It also improves the lower endpoint. The result improves the direct
contour estimator itself. A direct calculation allowed the same centered
kernel reproduces it; no recursive superiority, new zero coverage,
convergence rate or equal-total-cost advantage is claimed.

Read [result summaries][results] and [avoid][avoid], especially
[cluster18][cluster], [controls12][controls], [classification01][class],
[premises02][premises], [scope07][scope] and [joint12][joint]. Under avoid01
this is a finite enclosure-width milestone, judged by the measured and
outward-certified width ratio below. [Selection41][selection], the
[E36 request][request] and its [28-file manifest][pins] freeze the
representations, comparator, 1% gate, source budgets and timing schedule.
All pins matched before execution.

## 1. Same source and same whole-path statistic

The physical field, two-occurrence population, contours and source record
are exactly those of [Note39][n39] and [Record16][oldrecord]:

    a=140101/10,  I=[-3/10000,1/10],
    r_-=3/4,  rho=9/10,  r_+=21/20,
    33-by-128 fine source archive, degree32 in space and time, 224 bits.

The independently counted tube permits either sign of D before its
source conclusion. E34 already paid `D_t>1.5072` throughout I, from
`0<M<.616`, `D<.2` and the collision-regular complete pair law. Both
methods receive this identical premise. Hence their common statistic is

    Q=min_(t in I) D(t)=D(-3/10000).                         (1)

A sharper enclosure of this endpoint narrows an enclosure of the
whole-path minimum. It does not enlarge I, establish a new monotonicity
theorem, or infer whole-path coverage from endpoint samples. The old
512-cell complete forcing audit is inherited and is not rerun.

The unchanged field error is `E<0.528676064`. The source polynomial,
16-by-64 geometry, principal logarithm branch and annular moment tails
are reconstructed with the same arithmetic as E34. The full geometry
record and the high-precision direct endpoint bounds reproduce exactly.
No improved field majorant, extra time cells, contour nodes or xi calls
are introduced. Every source, reconstruction, time-extension, arithmetic
and angular-tail payment of E34 remains in force.

## 2. A precise common error set and the sharp separate baseline

Let `w_j=rho exp(2pi i j/128)`, `0<=j<=64`, with weight one at
`j=0,64` and two otherwise. The real part of the weighted mean represents
the complete circle by exact source conjugation. From the actual E34
endpoint complex logarithm rectangles extract their exact dyadic
midpoints `ell_j` and component radii `a_j,b_j`. Write

    L_j=ell_j+e_j,
    |Re e_j|<=a_j,  |Im e_j|<=b_j.                          (2)

Arb exposes these midpoints and radii as exact representable numbers.
There is no box-conversion enlargement. The [new record][record] stores
their exact rational values and a canonical serialization hash, so both
assemblies consume demonstrably identical rectangles. Source errors
across nodes need not be independent: allowing their components to vary
independently defines an outer relaxation containing the one true source.
The proposed improvement retains an additional dependency **between
the two moments of these same node errors**.

For any complex kernel K define the exact support value of this box:

    S(K)=sum_j weight_j (|Re K_j|a_j+|Im K_j|b_j)/128.       (3)

This is the supremum of the absolute real weighted sum `Re<K e>`.
To prove sharpness, choose each real and imaginary component of e at the
endpoint with the sign of its coefficient in that real sum. Reversing
the signs attains its negative. This is a statement about the specified
rectangular relaxation, not a claimed physical theta perturbation.

Let `epsilon1,epsilon2` be the unchanged chosen positive annular-tail
allowances, as exact representable upper bounds. The contour formulas give

    p1=-Re<w ell>-Re<w e>+eta1,
    p2/2=-Re<w^2 ell>-Re<w^2 e>+eta2/2,
    |eta1|<=epsilon1, |eta2|<=epsilon2.                     (4)

For both methods these two tail intervals remain independently selectable
outer allowances; no new tail correlation is assumed. Put

    gamma0=-Re<w ell>/2,     s20=-Re<w^2 ell>,
    r_gamma=(S(w)+epsilon1)/2,
    r2=S(w^2)+epsilon2/2.                                  (5)

The exact marginal projections of this error set are
`gamma=p1/2 in [gamma0-r_gamma,gamma0+r_gamma]` and
`p2/2 in [s20-r2,s20+r2]`. Their Cartesian product discards their
shared node-error dependency. On this canonical endpoint, the computation
verifies `gamma0>r_gamma>0`. The exact minimum, maximum and width of
`D=p2/2-gamma^2` on that Cartesian rectangle are therefore

    L_sep=s20-r2-(gamma0+r_gamma)^2,
    U_sep=s20+r2-(gamma0-r_gamma)^2,
    W_sep=2r2+4 gamma0 r_gamma.                             (6)

These extrema follow from monotonicity in the independent s20 and positive
gamma variables. Both individual moment supports are sharp; their
optimizers need not be simultaneously compatible. This is the precise
information loss being tested. The comparator is not an artificially
rounded implementation interval or the weaker raw whole-cell bound.

## 3. Combine the common error before the full quadratic remainder

Choose h by the frozen rule: take the exact representable midpoint of
the outward enclosure of nominal gamma0. It is not optimized or selected
by a scan. The exact identity is

    J_h=p2/2-h p1+h^2=D+(gamma-h)^2
       =-Re<w(w-h)L>+h^2+eta2/2-h eta1.                   (7)

Consequently the nominal value and source/tail support radius are

    J0=s20-2h gamma0+h^2,
    R_h=S(w(w-h))+epsilon2/2+|h|epsilon1.                  (8)

For any sound interval Gamma containing the actual gamma, let
`[q_lo,q_hi]` be the full real interval range of `(Gamma-h)^2`.
This gives the certified enclosure

    D in [J0-R_h-q_hi, J0+R_h-q_lo].                       (9)

The square is the complete nonlinear remainder. If Gamma-h contains
zero, its lower endpoint is zero and its upper endpoint is the larger
squared endpoint magnitude. If zero is absent, both endpoint magnitudes
enter the minimum as well. In particular the code does not treat two
occurrences of gamma as independent when squaring, discard the square,
or replace it by a signed linear error.

For the idealized exact choice `h=gamma0`, (9) has width
`2R_h+r_gamma^2`. Triangle inequality gives

    R_h<=r2+2|gamma0|r_gamma,

so a sufficient strict-width test is

    2(r2+2|gamma0|r_gamma-R_h)>r_gamma^2.                   (10)

This explains the mechanism, but the executed acceptance uses (9) with
its actual representable h, all nominal arithmetic, and the complete
outward square interval. The possible arithmetic displacement of h from
exact gamma0 is thereby paid, not declared zero.

This formula is also exactly direct extraction of the discriminant using
the centered contour kernel. It can be inserted into a recursive outer
enclosure, but the calculation itself proves neither a recursion rate nor
an advantage over a direct method allowed the same kernel. It does not
shrink the exact full source feasible set by a projection sweep.

## 4. Arithmetic comparison and frozen acceptance

The complex contour nodes are rigorously enclosed at 224 bits. Exact
log-box component radii and exact dyadic midpoints are retained. The
nominal moment centers and support radii in (5),(8) remain full Arb
enclosures, with **both lower and upper endpoints**. They are not first
rounded upward and then falsely described as an exact baseline width.

For the candidate, Gamma uses an outward radius enclosing r_gamma; the
complete shifted-square range and outward nominal/kernel arithmetic give
lower endpoint L_cor, upper endpoint U_cor and a width upper bound W_cor.
For the sharp comparator, (6) gives an enclosure of the exact rectangle
width and exact lower endpoint. The primary tests are

    upper(W_cor)<=.99 lower(W_sep),
    lower(L_cor)>upper(L_sep).                            (11)

The same tests are made against the **high-precision** `D_lower,D_upper`
fields in Record16, including their printing/reparse error, not its wider
short display string. Also require `L_cor>.00016246`. For the quadratic
collision control, gamma0 is near zero, so use the general Cartesian
real-square range rather than the positive-gamma formula (6). Its gain
gate is not required; containing its exact zero is required.

## 5. Completed finite result

All primary canonical gates passed on the first mathematical execution.
No design, source-error, precision, time, node or threshold adjustment
was made. The following table uses outward-rounded endpoint summaries;
the width column displays the scale of the high-precision certified
values, which own the gate comparisons in [Record19][record].

| Same-source representation | Lower endpoint | Upper endpoint | Width |
| --- | ---: | ---: | ---: |
| Inherited E34 direct | 0.00082146953121025 | 0.00082252496203211 | about `1.05543082185022e-6` |
| Sharp independent moments | 0.00082158054103489 | 0.00082241395211396 | about `8.33411079060667e-7` |
| Shared-error centered kernel | 0.00082160722313648 | 0.00082238727005913 | at most `7.800469227e-7` |

The exact outward comparison gives

    W_cor/W_sep < .935969,
    width reduction versus sharp separate moments >6.4031%,
    width reduction versus E34 direct >26.0920%.            (12)

The **6.4031%** number is the correlation-recovery milestone. The larger
secondary reduction also includes the removal of excess arithmetic
wrapping in the old general interval evaluation; all 26.0920% must not
be attributed to the shared-error mechanism.

For scale, `r_gamma` is about `2.16227702427e-7`, `r2` about
`3.89274768182e-7`, `R_h` about `3.90023437942e-7`, and the full square
upper payment is below `4.6754420e-14`. Both candidate and comparator
retain the same annular allowances `epsilon1<5.014e-9`,
`epsilon2<1.048e-8`. The square's small size is a computed budget,
not permission to omit it.

With the unchanged whole-path monotonicity input, the new conservative
direct conclusion is

    min_(t in I) D(t) > .00082160722,
    min_(t in I) D(t)-.0001 > .00072160722.                 (13)

Positivity on this tube was already established by E34. Equation (13)
improves its numerical enclosure, not its zero coverage. No probability
or statistical independence is inferred from an interval width.

## 6. Acquisition equality and measured assembly overhead

The fine archive is read and both hashes checked once per comparison.
The same source polynomial and error bound are reconstructed once. Both
methods share the counted geometry, 65 complex log evaluations representing
128 nodes, the nominal moments and the two annular tails. The canonical
log-box hash is
`057edfb7df54685317537095da02137040c6a30e95e2da7bd22d532174aa63e9`.
Their current-source budgets are identical and new xi calls are zero.
The earlier acquisition of the archive and the E34 512-cell monotonicity
certificate remain common paid inputs; their historical work is not zero.

The support assemblies each use two 65-term sums. The baseline uses w,w^2;
the candidate uses w,w^2-hw and adds its centered nominal expression and
shifted-square range. It therefore has additional arithmetic. After one
untimed warmup per method, exactly 21 alternating-order assembly pairs
were measured. The final run reported median times about

    separate assembly:   .1345 milliseconds,
    correlated assembly: .2288 milliseconds,
    ratio:                1.70.

The full common preparation, including archive verification, polynomial
and error reconstruction, field construction, geometry and endpoint/log
work, was about .269 seconds. Input-manifest validation is separately
recorded, about .00184 seconds. The complete recorded execution was about
.350 seconds, including both methods, the timing repetitions and control.
Python/library startup and import overhead not isolated by these timers
is shared overhead, not a zero-cost claim. The record gives individual
components and all 42 timed assembly samples. These measurements describe
one environment, not a general complexity theorem or stable speed ratio.

One bounded **accounting-only** repair added an explicitly timed field
construction interval to the full common-preparation total. The first
successful record, including its original timings, is retained outside
Git at `/private/tmp/vcd-gt-cm-E36-attempt1.json`, SHA-256
`9a8c311eb54d8d040d91465428bbe86b443fe9357a01fba8a11cb7549e536245`.
The final record binds that first run and its source hash. After the
repair the unchanged frozen execution was repeated once; all mathematical,
source-error, exact log-box, comparator, gate and control fields were
checked identical. There was no numerical or proof-design repair and no
timing optimization. This is one of the two allowed correctness repairs.

The result is thus width reduction at equal **source/node/log acquisition
budget**, with measured assembly overhead. It is not a cost saving,
identical-total-runtime result, or proof that recursive acquisition is
cheaper than direct extraction.

## 7. Controls and continuation scope

The exact quadratic `w^2-2(t-1/20)` uses its zero-error polynomial source
and the same fixed geometry/log/moment formulas at its collision `t=.05`.
Both boundaries retain count two and clearance; both old and centered
discriminant intervals contain zero. Their widths are about `9.4954e-9`.
The method therefore does not erase a collision admitted by its sound
input boxes. The quadratic has no canonical xi source, and its strict
positive-gap conclusion fails at that event.

For the other [catalog controls][controls], preserve the exact source
distinctions of [Note39][n39]: Euler-factor translates change literal theta
arithmetic; weighted-square and finite-tail/score/prime perturbations lack
the complete reflected unit-weight source; reflected super-Gaussians fail
the canonical order class. Smooth/positive-primitive, finite-profile and
atomic controls lack full canonical arithmetic/profile/count transfer.
RH-conditional endpoint controls retain RH and changed Dirichlet
arithmetic. Changed readouts and fractional profiles fail literal cosine
readout and integer multiplicity respectively. Quartic/cosine fields lack
the complete canonical source/population, and static surgery lacks a
common canonical heat tube. These are separate failed premises; the
generic shared-error identity is not claimed to reject every control.

No manuscript, old note, old certificate or E16 input is changed. The
next continuation should either identify a further **different** lost
dependency with a quantitative comparator, or pursue a separately frozen
source-accuracy/cost question. Merely applying the same centering again
does not compound the 6.4031% gain. A centered direct comparator must be
the baseline for any subsequent claim using these same log boxes.
The exact joint log-box discriminant range could still be narrower than
(9), which separately bounds J_h and its full square; that is an unproved
remaining optimization opportunity, not an already acquired gain.

## Replay

Use the recorded runtime with a new output path:

```sh
/private/tmp/vcd-gt-lehmer/venv/bin/python \
  papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/numerics/vcd_gt_cm_correlated_discriminant.py \
  --cache-dir /private/tmp/vcd-gt-lehmer \
  --output /private/tmp/vcd-gt-cm-E36-replay.json
```

Without `--cache-dir`, the inherited normal/environment archive lookup
is preserved. Missing or altered inputs fail closed. The temporary archive
and first-run paths are local reading copies, not permanence promises.
The [consumer][code] and [small record][record] retain the frozen hashes,
exact log boxes, source/error accounting, comparisons, timings and control.
These hashes identify data; E37 must assess the mathematics and replay.

[register]: ../research-progress/01_VCD_GT_CM_RESEARCH_PROGRESS_20261117.md
[selection]: 41_VCD_GT_CM_B10_R3_CORRELATION_SELECTION_20261118.md
[request]: ../research-progress/handoffs/VCD-GT-CM-E36-r1.md
[pins]: ../research-progress/handoffs/VCD-GT-CM-E36-inputs-r1.json
[n39]: 39_VCD_GT_CM_E34_EXTENDED_SOURCE_AND_FORCING_20261118.md
[oldrecord]: ../numerics/16_VCD_GT_CM_EXTENDED_SOURCE_CERTIFICATE_20261118.json
[record]: ../numerics/19_VCD_GT_CM_CORRELATED_DISCRIMINANT_20261118.json
[code]: ../numerics/vcd_gt_cm_correlated_discriminant.py
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
