# E21 — Canonical high-height horizon of the initial-interaction comparison

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model and effort unavailable in the
registered CM chat0003. Advisory helpers inherited settings. The lead
writes this proof; a separate nonauthor E22 assessment is requested.

**Status: proved in-note; the E22 assessment and sole register record
acceptance status.** The result is a scoped
limitation of Note17's one-step scalar comparison, even with exact initial
canonical data. It is not a collision, a limitation of actual theta
dynamics, or an improved bound on Lambda. The positive-time exterior
coverage is imported from Polymath, not claimed as a new theorem.

Read [result summaries][results] and [avoid][avoid], particularly
[cluster18][cluster], [controls12][controls], [classification01][class],
[premises02][premises], [scope07][scope] and [joint12][joint]. This is a
quantitative consumer test with constants and a vanishing rate, not an
RH-equivalent reformulation. [E21 r1][request] freezes its method and limits;
[Note20][oc] and [source audit04][source] supply the two acquisition audits.

## 1. Inputs and a genuinely common positive-time cutoff

Keep the complete unchanged theta source, its occurrence multiplicities,
and physical H_t=-H_zz. Fix 0<t0<=t1<=1/2. In this note t is a slice time;
for a backward application set t=t* and u=t*−time. No normalized time is
substituted. The positive initial-interaction statements below concern
those slices in [t0,t1] at which the complete divisor is real and simple.
They are uniform over all such slices; they do not presume the entire slab
is all real. In particular t*=1/2 is an available classical all-real start.

[Polymath v2][poly], Theorem1.5 and its absolute-constant convention, supplies
a clock

    G(x,t)=x/(4π) log(x/(4π))−x/(4π)+11/8+(t/16)log(x/(4π)),
    G(q_n(t),t)=n,

and actual sufficiently high zeros ξ_n(t)=q_n(t)+O(q_n(t)^(-c t)).
Its high zeros are real and simple, with no other zeros in that region.
Its unit-window occurrence bound is O(log(2+|x|)), also on the negative
side by evenness. The constants C,c and the O constants are absolute,
independent of t. See the source audit for exact passages, the Rouché
multiplicity interpretation, and the parent checked count receipt.

Part (i) imposes a height onset exp(C/t); part (ii) an index onset
exp(C/t). Choose a larger absolute C1 and X0=exp(C1/t0), enlarging it
further if necessary. Since G(x,t) grows like x log x/(4π), every clock
index associated to x>=X0−2 meets both onsets for every t∈[t0,t1]. The
localization disks are disjoint for large height: their radius is c/log x,
where c can be chosen small, while clock separation is asymptotic to
4π/log x. Part (i) exhausts high zeros and part (ii) counts one occurrence
per disk. Thus labels are consecutive and the zeros simple. Reflection
provides the same result for x<=−X0. This proves the common exterior
coverage, including the endpoints of the fixed positive slab.

There is no numerical X0 here: no numerical C1 is extracted. This is a
uniform existence/asymptotic input, not a finite certificate. At t0=0 the
onset diverges and the localization error no longer decreases. Taking
t0↓0 in this argument supplies no time-zero tail theorem.

## 2. Local clock errors and the complete exterior tail

Let a=ξ_n(t), b=ξ_(n+1)(t), g=b−a, D=g²/4, with a→∞. Write

    L=log(a/(4π)),       d=1/G_x(a,t)=(L/(4π)+t/(16a))^(-1),
    η=L a^(-c t0)+1/a,  ε=1/L+L a^(-c t0).

All following constants are uniform in the real-simple slices of the
fixed slab. Their numerical values are not acquired. Increase X0 until
the finite factors below are separated from zero, g<1/4 and η is small.

For |ξ_(n+k)−a|<=2, source localization gives
G(ξ_(n+k),t)=n+k+O(L a^(-c t0)), uniformly in every such k.
Taylor's theorem, G_x(a,t)=1/d and G_xx(x,t)=O(1/a) in that neighborhood,
therefore gives

    (ξ_(n+k)−a)/d = k+e_k,       |e_k|<=Cη,       e_0=0.       (1)

Subtract the k=0 equation when obtaining (1); its error is included in
Cη. No derivative of a source remainder is taken. In particular

    g=d(1+O(η)),      h_L=d(1+O(η)),      h_R=d(1+O(η)).     (2)

Now define the *complete* positive exterior interaction

    M=Σ_(ρ≠a,b) 1/[(ρ−a)(ρ−b)].

Every exterior occurrence is retained, including negative zeros and the
bounded low-height population. Absolute convergence follows from the
unit-window count and inverse-square denominator. Split at |ρ−a|=1;
assign equality to the far set.

For the near terms put ρ=ξ_(n+k), k≠0,1. Equation (1) yields

    d²/[(ρ−a)(ρ−b)]
       =1/[(k+e_k)(k−1+e_k−e_1)]
       =(1+O(η))/[k(k−1)].                               (3)

The bound is uniform in k: both nonzero integer denominator factors
have magnitude at least one. Since all local zeros are consecutive, the
near index set is an interval with the target indices deleted. Its left
and right endpoints have magnitudes comparable to L, by (1) and d~4π/L.
The positive telescoping sum is

    Σ_(k∈Z\{0,1}) 1/[k(k−1)] = 2,

and either omitted index tail is O(1/L). Summing (3) gives

    d² M_near = 2+O(η+1/L).                              (4)

For the far set let r=|ρ−a|>=1. Since g<1/4,
|(ρ−a)(ρ−b)|>=(3/4)r². Split into shells j<=r<j+1, j>=1.
The two unit windows have at most C log(3+a+j) occurrences. Therefore

    |M_far| <= C Σ_(j>=1) log(3+a+j)/j² <= C' log(3+a).    (5)

For the last bound use log(3+a+j)<=log(3+a)+log(1+j) and the convergent
sum Σ log(1+j)/j². This pays the entire unbounded exterior; it is not an
unproved cutoff or a nearest-neighbor approximation. Since d²=O(L^−2),
its normalized payment is O(1/L). The split boundary at distance one
is accounted for by the near index tails and (5); no boundary zero is lost.
Combining (2), (4), (5) proves

    g=4π/L (1+O(η)),
    d²M=2+O(ε),          g²M=2+O(ε),
    DM=1/2+O(ε).                                        (6)

The replacement d=4π/L(1+O(1/(aL))) is absorbed in η.
For the two-neighbor lower bound

    b_3=1/[h_L(h_L+g)]+1/[h_R(h_R+g)],

(2) separately proves

    g² b_3=1+O(η),         D b_3=1/4+O(η).               (7)

These are canonical source consequences, with a written head/tail passage.
They are stronger evidence than a lattice example but do not describe a
new distribution law for the non-asymptotic, low-height divisor.

## 3. Exact quantitative limitation of the frozen consumer

[Note17][comparison], equations (6)–(11), supplies the strict score

    R(d0,b0;Δ)=d0(1+2b0Δ)−2Δ,
    0<d0<=D,  0<=b0<=M,  Δ>=0.                          (8)

Both partial derivatives in d0,b0 are nonnegative. Thus exact D,M maximize
the score over every certified initial lower pair in this information
class. A finite positive partial sum, a smaller gap enclosure or a more
accurate estimate of the same initial quantities cannot exceed this
maximum. At high height, DM<1 by (6); for the exact input, positivity of
(8) is equivalent to

    Δ < τ_full := D/[2(1−DM)].

Likewise define τ_3=D/[2(1−D b_3)], with denominator positive eventually.
The equality endpoints are excluded. Equations (6)–(7) prove

    τ_3   = (g²/6)(1+O(η))
          = (8π²/(3L²))(1+O(η)),
    τ_full= (g²/4)(1+O(ε))
          = (4π²/L²)(1+O(ε)),
    τ_full/τ_3 = 3/2+O(ε).                               (9)

The gap-only horizon is exactly g²/8. Thus two neighbors give asymptotic
factor 4/3 over gap-only; complete initial M gives factor 2 over gap-only,
or factor 3/2 over the two-neighbor allowance. These are improvements of
this comparison's admissible duration, not of a proved Lambda bound.

For every fixed positive Δ, at every sufficiently high initial canonical
pair on the stipulated real-simple slices, even the maximal score is
negative. More explicitly,

    R(D,M;Δ) = D−Δ+O(Δε) → −Δ,
    R(D,b_3;Δ) = D−3Δ/2+O(Δη) → −3Δ/2.                  (10)

The limits are uniform on the positive slab. Consequently any nonempty
finite block consisting only of sufficiently high eligible pairs is
conservatively bad for this fixed Δ. Its bad-block probability is one,
not a rare exceptional tail. Better acquisition of the same initial
lower data cannot make the unchanged score positive there.

**The limitation concerns only Note17's one-step Riccati lower envelope
from initial D,M; it does not concern the actual canonical evolution.**
It excludes neither a strengthened joint-in-time estimate nor renewed
anchors, divided steps, direct exterior simplicity, or a different
consumer. It does not show a collision or any dynamical instability.

## 4. Exact controls and why the discarded forcing matters

For an equally spaced bi-infinite divisor of gap g, the first n exterior
zeros on each side contribute

    b_n=(2/g²) Σ_(k=1)^n 1/[k(k+1)]
       =2n/[(n+1)g²],
    D b_n=n/[2(n+1)],
    τ_n=g²(n+1)/[4(n+2)].                                (11)

This gives g²/6 at n=1 and g²/4 as n→∞, in agreement with (9).
It is exact telescoping algebra, not a numerical approximation.

For a physical check use H(t,z)=exp(π²t/g²) cos(πz/g). It is even and
satisfies H_t=−H_zz. Its zeros have spacing g and are stationary; M=2/g²,
D=g²/4 and D_u=0. The Riccati-only envelope still decays and (8) still
stops at g²/4. The positive terms 12S2+16DS3 in M_u exactly balance
2M² here; dropping them causes the loss. This finite exponential-type
field is not theta and has linear, not X log X, zero population. It
checks the logic of the estimate without claiming the canonical field
is stationary. The quadratic control H(t,z)=z²−2(t−t_c) has M=0 and
collides exactly at Δ=t*−t_c; it retains the necessity of strictness.

Analytical replay of [controls12][controls], rather than new numerical
experiments, yields the following application-premise screen. The generic
local comparison need not fail for a control; the source-specific import
and final exclusion require the stated additional premises.

| Control family | Failed or unacquired premise in this canonical use |
| --- | --- |
| Euler-factor translates | Unchanged complete theta initial function fails; Polymath's canonical clock is not imported for the changed source. |
| Weighted-square and finite-source/score controls | Full reflected unit-weight theta identity fails; endpoint-defective finite-source subclasses have no all-real heat time, so also fail the start premise. |
| Finite-prime orbit controls | Full reflection/unchanged theta fails despite selected-prime identities; no canonical uniform clock follows from them. |
| Reflected super-Gaussian control | Theta square arithmetic fails; the canonical population/clock input is unacquired for this control. |
| Smooth shape and positive-primitive controls | Unchanged theta arithmetic fails; required uniform source localization is unacquired. |
| Fixed-event atoms and finite/compact-profile controls | Complete canonical source and X log X population fail; finite profiles do not supply clock localization. |
| RH-conditional close-source mergers | Changed arithmetic and conditional construction do not satisfy the unchanged unconditional source input. |
| Variable kernels with theta amplitude | Physical cosine/Newman readout fails. |
| Fractional count relaxations | Integer divisor/void realization fails, so cannot supply a bad-block zero-exception count. |
| Static divisor surgery | Common canonical heat evolution and unchanged source fail. |
| Cosine and polynomial checks above | Canonical source/population fail; they test the comparison's algebra and scope only. |

## 5. Disposition of the two acquisition mechanisms

**Neighbor/void mechanism.** Source localization does acquire deterministic
neighbor information uniformly in the eventual positive-time region. It
makes the unchanged fixed-Δ score negative there, rather than yielding a
favorable tail. In the complementary bounded region, an unrestricted
four-point marginal does not impose adjacency; void information or an
actual ordered divisor census remains necessary for three consecutive
gaps. [Note20][oc] records the existing finite OC scalar certificate and
its census, so we do not say that all canonical statistics are unacquired.
Those data are at a different time and for a fixed projection; no transfer
to the present positive-time three-gap score has been proved.

**Complete initial-interaction mechanism.** Equations (6) and (9) do acquire
its high-height size, with all exterior tails paid, and prove the best
possible gain under the frozen scalar consumer. Conditioning on a small
gap does not evade (10) for these high canonical pairs: all their raw gaps
are small. In the low-height regime a new conditioned source estimate
might still help. This note does not exclude it or any stronger integrated
interaction estimate.

For a fixed strictly positive target t0=t*−Δ, the independently imported
common exterior simplicity theorem can cover |Re z|>=X0 for the whole
slab. Then only a compact possible first-collision region remains.
A concrete application still needs the source constants or another
certified exterior cutoff, a complete finite pair-label cover (including
pairs crossing every chosen window edge), an independent all-real simple
start and positive margins or an integer bad-count bound below one.
Freezing labels does not authorize ignoring trajectories entering a window.
No compact statistical estimate, explicit computational height budget or
new bound on Lambda is obtained here.

This closes B07 r2 with a quantitative source-based consumer disposition.
No larger initial-statistics campaign is justified for the failed all-height
one-step objective. A future B decision would have to specify either a
bounded compact positive-time acquisition with every error paid, or a
stronger joint-in-time consumer. The independent E16 r2 approximation
contract remains ready and unexecuted; it is not a consequence of this note.

[request]: ../research-progress/handoffs/VCD-GT-CM-E21-r1.md
[comparison]: 17_VCD_GT_CM_B07_REGIONAL_GAP_STATISTICS_AND_BACKWARD_COMPARISON_20261118.md
[oc]: 20_VCD_GT_CM_OC_ACQUISITION_INTERFACE_AUDIT_20261118.md
[source]: ../references/04_VCD_GT_CM_POSITIVE_TIME_SOURCE_AUDIT_20261118.md
[poly]: https://arxiv.org/html/1904.12438v2#S1.Thmtheorem1.5
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
