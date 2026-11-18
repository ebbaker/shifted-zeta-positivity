# B09 r1 — Forward statistics from time zero and the backward return

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model and effort unavailable in the
guarded chat0004 registry; conceptual helpers inherited settings.
This responds to the author's proposal to use known t=0 information to
improve positive-time statistics before attempting backward propagation.
The [sole register][register] owns status; E30 separately assesses this note.

**Status: proved in-note finite-census inference, conditional forward
estimates and a scoped exact round-trip limitation; no new time-wide
source acquisition.** Forward propagation is a legitimate acquisition
direction. The backward use must retain what the forward step learned.
In particular, the unchanged exact-initial-M Riccati horizon cannot improve
its reached negative endpoint by first propagating forward when F>=0.
This does not exclude the retained-F consumer of [Note32][note32].

Read [result summaries][results], particularly [cluster18][cluster] and
[collision controls12][controls], and [avoid][avoid], specifically
[classification01][class], [premises02][premises], [scope07][scope] and
[joint12][joint]. Reuse [Note17][stats], [Note20][audit] and the complete
source/lattice conventions of Note32. Classify the forward formulas as
conditional finite estimates, the census consequence as a deduction from
an existing finite certificate, and the round-trip result as a limitation
of one precisely stated consumer. None is an RH-equivalent criterion or
a new all-height zero-exception theorem.

## 1. An actually available time-zero starting population

[OC Note22][census] records an accepted complete winding census of the
conjugation-invariant rectangle

    (988,2012)+i(-3/2,3/2)

at t=0: 388 occupied singleton cells, counting multiplicity, with pairwise
disjoint horizontal projections. Its exact bounds include horizontal
width at most 5/32768 and separation of successive horizontal intervals
at least 5085/8192. Its imaginary cells are asymmetric intervals, not
point values zero. The numerical source census is reused at its recorded
complete winding/count scope; it is not rerun or independently certified
by this note.

Nevertheless **all 388 zeros are real and simple** at that inherited scope.
For a zero rho in one occupied cell, its conjugate is in the symmetric
outer rectangle and must therefore occur in the complete census. Its
real coordinate is identical. Disjoint horizontal projections force the
conjugate into the same occupied cell; count one including multiplicity
then gives rho=conjugate(rho) and multiplicity one. This argument uses
completeness and conjugation, not replacement of an imaginary interval by
its midpoint. Without complete coverage or singleton counts the deduction
would fail.

Ordering these zeros gives 387 consecutive internal gaps, all at least
`s0=5085/8192`, and 385 edges have both neighboring gaps inside the
census. Consequently the full-block initial squared-gap minimum satisfies

    q(0)>=q0=s0^2/4=25857225/268435456.                      (1)

This supplies deterministic finite gap and three-gap enclosures. It is
stronger input for this purpose than the one previously evaluated blurred
scalar P_1000. It supplies no positive-time labels/counts, source jets,
complete exterior interaction or uniform-height distribution. It does
not establish global reality at t=0. Statistical averages alone would
not replace its complete-count premise.

## 2. The common forward domain must be acquired independently

Let N>=2 real simple initial nodes be the complete contents of a cleared
conjugation-invariant contour. Assume an independent count-N and boundary
clearance certificate persists on 0<=t<=s, with spatial buffers. The
remaining complete divisor may be nonreal. On compact pre-collision
subintervals use common labels, the complete B=H_z/H and the whole-block
deflation

    R=B-sum_{j=1}^N 1/(z-x_j),
    U_i=sum_{j!=i}1/(x_i-x_j)+R(x_i),   x_i,t=2U_i.          (2)

The contour excludes exterior entry. Its source/product and time bounds
are new hypotheses on this forward interval, not consequences of the
time-zero root-cell list.

Under these hypotheses the initially real simple population remains real
and simple forward. Here is a local proof that does not assume global RH.
At a hypothetical first collision, isolate one cluster of k>=2 real
roots; the other zeros are separated from its limit point. Deflate this
cluster, with analytic regular part R_cl, and put
`V_cl=sum_i(x_i-mean x)^2`. Pairing internal reciprocal forces gives

    (V_cl)_t=2k(k-1)+4 sum_i (x_i-mean x) R_cl(x_i).         (3)

The second term tends to zero at the hypothetical cluster collapse:
R_cl is uniformly bounded nearby and all centered coordinates vanish.
Thus V_cl,t is strictly positive sufficiently near that time, whereas
V_cl>=0 would be tending to zero from the left. This is impossible.
An initially simple real zero also cannot become nonreal before a
collision, by conjugation and local uniqueness. Compact contour clearance
excludes escaping labels and external entries. This proves local forward
preservation once the complete time-wide count/clearance has been paid;
it does not acquire that certificate.

## 3. Candidate A: forward contraction of force dispersion

Reverse the time orientation in Note32. Define the positive weighted
graph Laplacian `L_ij` by weights `(x_i-x_j)^(-2)`,
`P=Id-11^T/N`, `a=PU`, `r_U=|a|`, and
`h_i=(R_t+2U_i R_z)(x_i)`. Direct differentiation gives

    U_t=-2LU+h,
    (|a|^2/2)_t=-2 sum_{i<j}(U_i-U_j)^2/(x_i-x_j)^2+a dot Ph. (4)

If the independent spatial enclosure gives diameter at most Lmax, then
all internal weights are at least Lmax^-2 and
`sum_{i<j}(a_i-a_j)^2=N|a|^2`. Hence

    (r_U)_t<=-gamma r_U+J(t),
    gamma=2N/Lmax^2,   J(t)>=|Ph(t)|,
    r_U(s)<=exp(-gamma s)r_U(0)
                 +integral_0^s exp(-gamma(s-t))J(t)dt.       (5)

The norm inequality holds in the upper-Dini sense at zero. The internal
sign is now dissipative. An acquired remainder J can therefore give a
genuine forward force/velocity-dispersion bound. A constant J improves
the homogeneous initial norm only when its floor J/gamma is sufficiently
small. Source time/spatial jets, full exterior terms, node-location and
arithmetic errors remain payable as in Note32; boundary forces do not
vanish upon removing the mean.

This is a velocity statistic. Without additional initial geometry it is
not a nearest-neighbor gap distribution: a small force dispersion can
coexist with a nonuniform gap profile balanced by the exterior. The
direct gap integral keeps signed force differences and is at least as
informative as replacing them by sqrt(2)r_U.

For the entire census, confinement to its original rectangle would give
Lmax=1024 and gamma=97/131072. Even with J=0, the reduction supplied by
this particular conservative envelope at s=.1 is less than
`97/1310720`, about .0074 percent. This is the reduction *in that envelope*,
not a cap on the actual contraction. Shorter blocks might give stronger
rates but incur their own exterior/boundary payments. Neither positive-
time confinement nor J=0 is asserted for the census.

## 4. Candidate B: a forward lower-tail transport for block minima

This candidate uses actual initial gap geometry rather than force jets.
Let `g_i=x_(i+1)-x_i`, `D_i=g_i^2/4`, and `q=min_i D_i` over **all**
N-1 edges of the chosen block. Decompose each complete interaction into
its internal real nodes and the exterior represented by R. Assume

    M_ext,i=-(R(x_(i+1))-R(x_i))/g_i <= C,   C>=0,            (6)

uniformly on the forward domain, including both block-end edges.
An independently paid `|R_z|<=C` along all connecting real segments is
sufficient. This is a complete signed exterior bound and does not assume
that exterior zeros are real.

At an active minimizing edge, all block gaps are at least g_i. Number
the edge by i=1,...,N-1. The mth exterior internal node on either side
is at least m*g_i from its nearer target. The positive real terms obey

    M_int,i <= g_i^-2 [sum_{m=1}^{i-1}1/(m(m+1))
                        +sum_{m=1}^{N-1-i}1/(m(m+1))]
             =g_i^-2 [2-1/i-1/(N-i)].                      (7)

Apply `D_i,t=2-4D_i M_i` and (6). At almost every time an active
minimizer differentiates q; ties do not change the a.e. envelope law.
Therefore

    q_t >= a_N-4Cq,
    a_N=min_i[1/i+1/(N-i)]=N/[floor(N/2)ceil(N/2)],
    q(s)>=exp(-4Cs)q(0)+a_N(1-exp(-4Cs))/(4C),              (8)

with the continuous C=0 interpretation `q(s)>=q(0)+a_N s`.
The bound is positive on every finite interval when q(0)>0; it can
also serve as a first-lower-exit proof on the independently acquired
outer domain. Internal label switching causes no extra loss.

For the 388-node census, `a_N=1/97` and (1) is acquired at the inherited
scope. The scalar lower bound improves this initial q0 precisely when

    C < a_N/(4q0)=268435456/10032603300.                     (9)

No such time-wide C is currently acquired. For example, C=0 would yield
the illustrative increase s/97, but is not canonical exterior data.
The 12-unit buffer of the smaller observation window [1000,2000] cannot
be applied to the outermost census nodes without checking their actual
buffers. Nor may one silently minimize over only interior eligible edges
and still use (7): an excluded boundary gap could be smaller than the
chosen minimum. Use the complete block minimum, or derive and pay a
different boundary comparison.

For finitely many blocks with the same N and paid C, sample their index
uniformly only as bookkeeping. Formula (8) gives the distributional bound

    P(q_X(s)<=r) <= P(q_X(0)<=exp(4Cs)r
                                  -a_N(exp(4Cs)-1)/(4C)),  (10)

and the shift is r-a_N s for C=0. There is no independence or random-matrix
assumption. Different N,C use their individual monotone transforms. All
eligible and boundary-crossing gaps must still be covered if one wants
zero exceptions. A small averaged bad-block rate is not zero unless its
paid upper bound crosses the finite integer threshold of Note17.

## 5. What survives an equally informed backward return

Better positive-time minima alone do not supply the complete interaction
needed by the backward consumer. Formula (7) is an **upper** M estimate;
backward gap protection uses a **lower** M or F estimate. They cannot be
exchanged. A two-sided exterior C bound alone would give M>=-C and the
coarse backward comparison `D_u>=-2-4CD`. Combining this with (8) over
equal durations s, and writing z=exp(-4Cs), gives only

    q_return >= z^2 q(0)+(1-z)(a_N z-2)/(4C),               (11)

as a lower allowance. Its right side is at most q(0), since a_N<=2.
For C=0 it becomes q(0)+(a_N-2)s, also no improvement. This limits that
composition of two scalar allowances, not the actual return trajectory
or stronger joint information. The quadratic N=2,C=0 saturates the
loss-free return; it gives no extension past its original collision.

There is a sharper exact screen for the **unchanged complete-initial-M
Riccati backward consumer**. On a forward local trajectory with
`D>0`, `M>=0`, `y=1-DM>0` and complete `F>=0`, put

    h=D/[2(1-DM)].                                         (12)

This is the exact-input backward horizon from Note17, not actual time
remaining to a collision. The forward pair laws are
`D_t=2-4DM`, `M_t=2M^2-F`. Thus

    y_t=-2My+DF,
    h_t=1-2Fh^2,
    h(s)-s=h(0)-2 integral_0^s F(t)h(t)^2 dt <=h(0).        (13)

The first equation and an integrating factor preserve y>0 from y(0)>0
on such a positive-D interval, so no unmentioned horizon pole crossing
is used. M>=0 and the other stated source/domain conditions are required
where this inherited consumer is used; they are not inferred globally
from the finite t=0 census. The last identity is exact differentiation,
not an asymptotic or sampled statement.

Starting at t=s, this consumer reaches only times greater than `s-h(s)`.
Equation (13) says `s-h(s)>=-h(0)`: **forward propagation cannot improve
the reached endpoint of the unchanged exact-initial-M consumer when
F>=0 on the forward interval.** For persistent finite labels, each
`h_j(t)-t` is nonincreasing. Their block minimum and their probabilities
of exceeding a fixed negative-deadline allowance therefore cannot improve
under this same consumer. This includes any valid nonnegative two-neighbor
lower estimate b3(s)<=M(s), with the omitted exterior paid (for example,
under Note17's original complete all-real hypotheses), only in comparison
with the **complete** initial-M allowance at t=0: its horizon is then at
most h(s). Nonnegative complete M alone does not make a real-neighbor
subsum a lower bound when the remaining exterior may be nonreal. This
does not deny improvements over a deliberately weaker or uncertain
time-zero lower estimate.

The quadratic has F=0 and saturates (13). The stationary cosine has
positive F and constant h, so h-s decreases even though its true divisor
does not move. These controls screen the consumer, not canonical dynamics.
The precise negative class is (12) with its stated positive-D/F and
common-label domains. Signed F, time-dependent retained forcing, regular
joint D/M propagation, new source information or measured acquisition
costs are outside that exclusion.

## 6. Consequence for the author's proposal

The useful strategy is **forward acquisition of joint information**, then
a backward consumer that keeps it. Two concrete items now exist:

- Finite certified t=0 root geometry supplies actual labels and gap data;
  the earlier scalar OC projection is not the only usable source output.
  Paid whole-time exterior bounds would turn it into the forward lower-
  tail transport (8)--(10).
- Forward force dissipation provides (5) when its complete source remainder
  is paid. Its strongest possible use is correlated force/environment
  information, not simply a smaller marginal variance.

For backward use, retain the joint neighboring geometry or complete
time-dependent physical forcing. Note32 identifies one finite target:
`F>=.3` on its stopped Lehmer interval would give a strict margin greater
than .00006246. That is a different height/population from the OC census
and must not receive its numerical constants. A fresh bounded decision
must select **one** common source/window/time domain and compare direct
joint propagation on that same information. The .1 forward duration in
the census discussion is illustrative and has no acquired forward tube.

The catalogued collision controls retain their source equality/reflection,
order/count, physical readout and multiplicity failures from Note32's
table. The local forward theorem legitimately applies to changed-source
real-rooted fields on a cleared tube; their collisions can be at its
backward endpoint or involve missing exterior/count conditions. Neither
forward smoothing nor exact theta source identity alone signs the required
backward forcing. Pair averages and finite-profile controls still cannot
supply an all-height zero-exception statement.

**Decision:** preserve B08's retained-F target and record B09 as a useful
conditional forward route, with the specific initial-M round-trip screen.
No new source computation is ready: source/time/count/outer-force errors
are unacquired, and the useful joint statistic must be selected before
execution. Do not rerun forward data merely to feed the screened horizon.
E30 assesses this derivation and finite-census inference; E16 remains
independently optional. No new Lambda bound, global t=0 reality, positive-
time statistical certificate or manuscript integration is claimed.

[register]: ../research-progress/01_VCD_GT_CM_RESEARCH_PROGRESS_20261117.md
[note32]: 32_VCD_GT_CM_FORCE_DISPERSION_AND_RETAINED_FORCING_20261118.md
[stats]: 17_VCD_GT_CM_B07_REGIONAL_GAP_STATISTICS_AND_BACKWARD_COMPARISON_20261118.md
[audit]: 20_VCD_GT_CM_OC_ACQUISITION_INTERFACE_AUDIT_20261118.md
[census]: ../../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/notes/22_TND_OC_B10_R3_CELL_RANGES_AND_GAUSSIAN_WIDTH_20261109.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
