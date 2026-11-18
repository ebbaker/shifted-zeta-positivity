# E23 — A joint forcing barrier and its canonical positive-time acquisition

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model/effort unavailable in registered
CM chat0003; advisory helpers inherited settings. The lead authors this
proof; E24 supplies a separate internal assessment.

**Status: proved in-note; assessment status belongs to E24 and the sole
register.** A joint-in-time comparison overcomes E21's shrinking allowance
on the canonical exterior of a fixed positive slab. Its source input
already guarantees exterior reality. This is a stronger acquired dynamical
comparison on that known region, not new zero coverage or a Lambda bound.

Read [result summaries][results], [cluster18][cluster], [controls12][controls],
[avoid][avoid], [classification01][class], [premises02][premises],
[scope07][scope] and [joint12][joint]. The finite conditional estimate below
is a quantitative milestone with a stated source acquisition, not an
RH-equivalent reformulation or a claimed sharp law. [E23 r1][request]
freezes the method. [Advice23][a23] screens the weaker ratio-forcing route;
[Advice24][a24] derives the same-source velocity alternative, attributing
it to Polymath Remark9.4. Those derivations are part of E24's assessment.

## 1. A joint variable retains the stabilizing part of the forcing

Use physical backward time u=t*−t on 0<=u<=Delta, with
0<t0=t*−Delta<=t*<=1/2 for the canonical application. The comparison
itself uses only the adjacent-pair equations on the globally real simple
stopped regime established in [Note17][comparison]:

    D_u=−2+4DM,       M_u=−2M²+F,
    F=12S2+16DS3,     D>0, M,S2,S3>=0.

All moments count the complete exterior occurrences. Strict isolation
suffices for these identities; no old strong-collar estimate is imported.
Define

    V=1−2DM,        K=2D²F=24D²S2+32D³S3.

Product differentiation, without differentiating a moment cutoff, gives

    D_u=−2V,
    V_u=(1−V²−K)/D.                                    (1)

Indeed V_u=−2(D_u M+D M_u)=4M−4DM²−2DF; substituting
2DM=1−V gives (1). K is dimensionless, while u is physical time.

**Joint barrier.** Suppose a paid estimate K(u)>=1−eta² holds throughout
the stipulated stopped interval, where eta>=0 is constant. Put

    v=max{V(0),eta}>=0.

Then

    V(u)<=v,          D(u)>=D(0)−2vu.                    (2)

For proof let w=V−v. Equation (1) gives

    w_u+[(V+v)/D] w <= (eta²−v²)/D <=0.

An integrating factor on each compact pre-collision interval proves
w<=0. Integrating D_u=−2V proves (2). No sign of V+v is needed.
If v>0 and 2v Delta<D(0), the selected pair cannot collide at a first
finite collision by Delta, provided all premises hold up to that event.
If v=0, D>=D(0) on the stated interval. No continuation beyond a separate
unprotected loss of exterior reality is asserted. Equality in the finite
margin is not an exclusion.

An explicit input target follows: for gaps with D(0) of order L^−2,
a bound V(0)_+=o(L^−2) and 1−K<=eta²=o(L^−4), uniformly in time,
make every fixed admissible Delta pass eventually. These are sufficient
rates for this barrier, not necessary rates for actual collision avoidance.
Section 3 acquires them from canonical source localization; merely assuming
them would not complete the task.

## 2. Exact positive forcing from a finite neighboring head

For an equally spaced real divisor with gap g and D=g²/4, keep J exterior
zeros on each side. The mth left/right exterior denominators equal
m(m+1)g². Their combined K contribution is

    3/[m²(m+1)²] + 1/[m³(m+1)³]
       = 1/m³−1/(m+1)³.

Thus, exactly,

    K_J=1−(J+1)^−3.                                    (3)

All omitted forcing terms are positive in the all-real regime. Consequently
(3) is a lower bound for full K whenever those exact head locations occur,
with no subtraction of an uncomputed tail. It is not a finite closure:
the actual head is acquired at each time, not evolved independently.

For an approximate head suppose, with d>0 and 0<=E small,

    (x_(j+k)−x_j)/d=k+e_k,   |e_k|<=C E,
    k=−J,...,J+1,          e_0=0.                        (4)

Then g/d=1+O(E). For each exterior label its denominator divided by d²
is (k+e_k)(k−1+e_k−e_1). Both reference factors are nonzero integers.
Each summand in K is therefore its lattice value times 1+O(E), uniformly
in k. The sum of the positive lattice summands is at most one. Hence

    K >= 1−(J+1)^−3−C1 E.                              (5)

This estimate preserves the combined second/third-moment weights before
summing; treating their favorable relation as unrelated error boxes is
unnecessary. The associated finite lower bound for initial M alone also
gives V(0)<=1/(J+1)+O(E). We next retain a two-sided complete-M estimate
as well, so its exterior error is not hidden in the comparison with E21.

## 3. Canonical acquisition on a logarithmically growing head

Fix 0<t0<=t*<=1/2. Use the unchanged complete theta source and the
[checked Polymath v2 input][source], Theorem1.5(i)–(iv), with its uniform
positive-time constant convention. Write q_n(t) for the clock solution

    G(q_n(t),t)=n,
    G(x,t)=x/(4π)log(x/(4π))−x/(4π)+11/8+(t/16)log(x/(4π)).

Source localization gives actual real simple zeros x_n(t) near q_n(t)
with error O(q_n(t)^(−ct)), exhaustively and with occurrence counts,
after both the height and index onsets. Choose a common sufficiently high
cutoff for the entire slab. Its numerical value is not extracted here.
Uniformity in t follows as in E21, rather than taking a different
uncontrolled cutoff at every time. No estimate at t0=0 is used.

Fix a high index n and set X=q_n(t*), L=log(X/(4π)), R=L². All constants
below are independent of X and t in this fixed slab. At most they depend
on the fixed slab and the already chosen source constants. For large X,
R=o(X). Direct implicit differentiation of the explicit clock, not of its
error term, gives

    q_n'(t)=−(π/4) log(q_n/(4π)) /
                  [log(q_n/(4π))+πt/(4q_n)],
    |q_n'(t)|<=π/4.                                    (6)

Thus the clock pair and its actual localized zeros remain in X+O(1)
over this slab, and in [X/2,2X] for X sufficiently large. Its disks remain
separated; uniqueness and the implicit-function theorem make the same
clock labels continuously differentiable branches. The following head
estimates do not differentiate the moving set of included labels.

Set a=x_n(t), b=x_(n+1)(t), g=b−a and d=1/G_x(a,t). For every actual
neighbor with |x_(n+k)(t)−a|<=2R, the source error in G is
O(L X^(−ct0)). Taylor's theorem has G_xx=O(1/X) in this larger window,
so after subtracting the equation at a it gives

    (x_(n+k)−a)/d=k+O(E_X),
    E_X=L X^(−ct0)+L^4/X.                               (7)

This is an absolute error in the normalized position, uniform in the
whole head. It is not obtained by differentiating an O term. The
O(R²/X)=O(L^4/X) curvature cost is retained. In particular

    g=d(1+O(E_X)),      d~4π/L,
    D=g²/4~4π²/L²,                                     (8)

uniformly in the slab. The growing physical head R, not just a fixed
unit radius, is essential for the rates below.

Choose the fixed integer

    J=floor(R L/(64π)).                                 (9)

For large X it is positive and comparable to L³. There are at least J+1
actual neighbors on either side in the radius-R neighborhood at every
time: G_x>=L/(8π) there, so the clock's index increase across R is at
least RL/(8π), well above the chosen J. The source displacements are
o(1), and the unused buffer absorbs them and the one-label asymmetry.
The left clock indices stay above the source onset because J=O(L³)
is negligible compared with n of order X L. Thus (4) holds for this
same finite label head throughout the slab. No window-entry labels or
multiplicities are dropped. Other possible low-height pairs are not
covered by this construction.

On the globally real stopped part of the interval, exterior Q>0. Apply
(5) and (7)–(9), and omit the remaining positive K summands:

    K(u)>=1−C_K(E_X+L^−9).                              (10)

There is no unpaid upper-tail estimate in this lower bound. This is a
pointwise-in-time source acquisition of an actual complete-field forcing
lower bound, not an independent finite-moment dynamics approximation.
The positive omission uses the real stopped regime; it is not asserted
for an arbitrary low-height nonreal divisor.

For complete M, split at |rho−a|=R, assigning the boundary to the far
set. In the near set, the index interval has endpoints comparable to
RL, and (7) gives

    d² M_near=2+O(E_X+(RL)^−1).

This uses the exact lattice sum Σ_(k≠0,1)1/[k(k−1)]=2. For the far set,
|Q|>=r²/2 with r=|rho−a|>=R. The complete unit count yields

    |M_far|<=C Σ_(j>=floor(R)−1) log(3+X+j)/j²
           <= C'[L+log(R+1)+1]/R <= C'' L/R.             (11)

For the middle inequality, comparison with the integrals of j^−2 and
(log j)j^−2 bounds respectively 1/R and (log R+1)/R. Negative zeros,
all low-height occurrences and every unbounded shell are included.
Multiplication by d² makes the error O((RL)^−1)=O(L^−3). Hence

    2DM=1+O(E_X+L^−3),
    |V|<=C_M(E_X+L^−3).                                 (12)

The full-time estimate (12) is available on the same stopped regime;
only its initial value is required by the joint K barrier. The source
also supplies (12) directly at each time. We distinguish these two uses
when comparing methods below.

## 4. The shrinking allowance is overcome on the known positive-time exterior

Choose paid symbolic constants in (10),(12), and put

    eta_X=sqrt(C_K(E_X+L^−9)),
    v_X=max{C_M(E_X+L^−3),eta_X}.

Using this upper bound for V(0) rather than its exact value is legitimate
in (2). We obtain the uniform-in-time lower comparison

    D(u)>=D(0)−2v_X u,
    v_X=O(L^−3+sqrt(E_X)).                              (13)

At fixed t0>0, E_X decays faster than any fixed negative power of L.
Therefore v_X=O(L^−3) and D(0)~4π²/L². In particular

    (2v_X Delta)/D(0)=O(Delta/L) →0                      (14)

for every fixed Delta within the stipulated slab. The algebraic duration
budget D(0)/(2v_X) is at least a constant times L for sufficiently large
X, when v_X>0. This is a budget of the bound, not a claim of backward
evolution for that many time units: all inputs are established only on
the fixed 0<t0<=t<=t*<=1/2 slab. On that slab the comparison pays the
entire fixed Delta at sufficiently high labels.

E21, even with exact initial M, has duration asymptotic g²/4=O(L^−2)
and rejects every fixed Delta at sufficiently high labels. Equations
(10)–(14) explain precisely what additional information removes that
limitation: a full-time lower bound for the combined normalized forcing,
retaining the neighbor geometry. It is not obtained from initial M alone.
No numerical cutoff or certified finite threshold is stated; C_K,C_M
and the source onset constants have not been extracted numerically.

## 5. Same-information comparison and noncircular scope

The acquired bound is useful as a dynamical interface, but its acquisition
uses the published common-time exterior clock theorem. That theorem already
puts the high zeros on the real axis and makes them simple throughout the
slab, without a global low-height reality assumption. The present argument
therefore does not enlarge the known canonical zero-free or real-zero
region, and is not an independent proof of that source theorem. Applying
it to an unprotected compact region would require new K and initial-defect
data, not a reuse of the exterior asymptotic outside its domain.

An equally informed direct comparison receives the same source. Clock
localization already bounds the consecutive gaps at every time. Further,
(12) itself gives |D_u|<=2C_M(E_X+L^−3) wherever the pair law applies,
without the K barrier's square-root error. [Advice24][a24] uses an analytic
local source residual and Cauchy bounds to derive the still sharper
published velocity consequence, and consequently a squared half-gap D variation bound
of order Delta[X^(−ct0)+L/X]. E24 assesses that derivation separately.
No superiority over either same-source direct estimate is claimed.

The reason to retain (2) is its weaker data interface: a full-time lower
bound for K plus initial V, rather than a full-time estimate of V or all
individual trajectories. It could apply to a new canonical information
class where those combined moment data are cheaper. No such cost advantage
or compact source acquisition is demonstrated here.

For the weaker ratio condition F>=2(1−epsilon)M², [Advice23][a23] shows
that small initial defect can still be amplified on the backward scale
M^−1~L^−2. The K lower bound is correlated with D and genuinely stronger
in the relevant direction; it must not be replaced by that ratio floor.
The exact cosine-plus-constant heat control there reaches a real collision
and fails the required near-unit K payment as that event is approached.
It tests the distinction with an actual noncanonical heat flow, not an
arbitrary unconstrained scalar function.

## 6. Collision-control premises and disposition

The analytical control replay uses [controls12][controls] and E21's
[family table][e21], not rerun floating witnesses. The local joint identity
and conditional barrier may hold for noncanonical heat fields. The missing
premises are the actual K payment and the unchanged canonical source
used to acquire it, not generic positivity or evenness.

- Euler-factor translates, weighted-square and finite-source/score changes
  alter the unchanged complete theta function; endpoint-defective finite
  subclasses also lack the all-real start. Their preserved finite data
  do not import the uniform canonical clock.
- Finite-prime orbit controls fail complete reflection/unchanged arithmetic.
  Reflected super-Gaussians fail the theta square expansion; their canonical
  clock input is unacquired. Smooth shape/positive-primitive controls also
  change the source, with canonical strip/count/clock transfer unpaid.
- Atomic and finite-profile controls fail the complete canonical population
  and source; RH-conditional close-source mergers keep altered arithmetic
  and their conditional premise. None is an unconditional theta input.
- Changed readout kernels fail the physical cosine/Newman equation;
  fractional measures fail integer divisor realization; static surgery
  lacks a common canonical heat evolution.
- The stationary cosine field has K=1 and V=0, so (2) correctly preserves
  its gap without the old artificial deadline. A quadratic heat collision
  has K=0 and V=1, so its admissible eta is at least one and (2) reproduces
  the exact gap-only lifetime. The cosine-plus-constant flow in Advice23
  loses its near-unit K premise. These controls lack theta arithmetic and
  do not contradict the canonical positive-slab acquisition.

This completes the selected joint-in-time mechanism and its source-based
positive-slab demonstration, subject to E24's assessment. No stronger
compact statistical law, numerical Lambda bound, t0=0 extension, finite
BBGKY closure or E16 theorem is obtained. A future useful extension needs
new paid compact/near-threshold forcing information or an actually cheaper
source consumer, not another derivation of the same high exterior.

[request]: ../research-progress/handoffs/VCD-GT-CM-E23-r1.md
[comparison]: 17_VCD_GT_CM_B07_REGIONAL_GAP_STATISTICS_AND_BACKWARD_COMPARISON_20261118.md
[e21]: 21_VCD_GT_CM_E21_CANONICAL_HEIGHT_HORIZON_20261118.md
[a23]: 23_VCD_GT_CM_B07_R3_RETAINED_FORCING_ADVICE_20261118.md
[a24]: 24_VCD_GT_CM_B07_R3_COMMON_TIME_CLOCK_ADVICE_20261118.md
[source]: ../references/04_VCD_GT_CM_POSITIVE_TIME_SOURCE_AUDIT_20261118.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
