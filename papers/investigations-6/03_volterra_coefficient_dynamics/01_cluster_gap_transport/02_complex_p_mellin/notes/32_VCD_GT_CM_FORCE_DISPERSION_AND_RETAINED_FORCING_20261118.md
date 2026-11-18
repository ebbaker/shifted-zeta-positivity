# B08 r2 — Force dispersion and a retained-forcing comparison

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model and effort are unavailable in
the guarded chat0004 registry; conceptual advisers inherited settings.
This is a lead-authored analytical decision with two read-only advisers.
Separate assessment is E29; the [sole register][register] owns its verdict.

**Status: proved in-note identities, two scoped allowance screens and a
conditional finite-time comparison; no new canonical acquisition.**
Retaining a physical forcing floor `F>=3/10` would pay the frozen .1003
descent with strict squared-gap margin greater than .00006246. That floor,
the extended contour and the time-wide coordinate bounds are **unacquired**.
The equally informed direct D/M method gives exactly the same comparison.

Read [result summaries][results], particularly [cluster18][cluster] and
[collision controls12][controls], and [avoid][avoid], particularly
[classification01][class], [premises02][premises], [coordinate changes03][coordinates],
[scope07][scope] and [joint bounds12][joint]. The starting point is
[Continuation31][prior] and the assessed manuscript lattice section.
Under avoid01 these are local representations, conditional consumers and
finite numerical allowance screens, not RH-equivalent reformulations or
an acquired collision exclusion. We compare exactly two quantities:
the dispersion of common node forces, and the retained transient of the
regular pair system. The constant-K calculation below screens a reduction
of the second candidate; it is not a third proposed source mechanism.

## 1. Fixed source, target and the source boundary

Use the complete canonical field `H_t=-H_zz`, `B=H_z/H`, physical backward
time `u=.1-t`, and the counted Lehmer pair centered near `a=140101/10`.
The unchanged finite target is

    0<=u<=Delta=1003/10000,  t_end=-3/10000,
    d_stop=1/10000,  r=9/10,  C=1/10,  Dmax=1/5.

[Note27][compact] supplies the exact provenance of the inherited bounds

    d=0.1787368 <= D(0) <= d+=0.1787369,
    b=0.6037742 <= M(0) <= b+=0.6037744,
    V=1-2DM,   V(0)<=v=1-2db=0.78416666313888.

Here `D=g^2/4`, `M=S1`, `F=12S2+16DS3`, and `K=2D^2 F`.
The old GT record's field named K is `-M`, not this K.
The known count-two annulus `3/4<=|z-a|<=21/20` is certified only for
`0<=t<=.1`. Its boundaries leave radial buffers .15 on either side of
the selected circle. All real trial coordinates `|c-a|<=C`,
`d_stop<=D<=Dmax` put both trial roots inside that circle and give
`|Q|>=q=(r-C)^2-Dmax=11/25`, where `Q=(z-c)^2-D`.

On the new negative-time part, boundary clearance, count two and the
unconditional coordinate bounds `|c-a|<=C`, `D<=Dmax` still need proof.
They may not be acquired by assuming the sought positive D. The contour
coordinates allow negative D and a conjugate pair. The complete exterior
may be nonreal, with every occurrence and integer multiplicity retained.
No global all-real assumption or high-exterior theorem pays this compact
extension. Consequently no source-acquisition execution is issued here.

## 2. Candidate A: common-force dispersion and its exact sign

Consider N consecutive real simple nodes in a finite block I, before its
first internal gap stop or loss of outer contour/buffer clearance. Set

    U_i=H_zz(x_i)/(2H_z(x_i)),   x_i,u=-2U_i,
    R(z,u)=B(z,u)-sum_{j in I}1/(z-x_j(u)),
    f_i=(R_u-2U_i R_z)(x_i,u),
    P=Id-(1/N)11^T,   E=|PU|^2/2,   r_U=|PU|.

R is the whole-block deflation; all other zeros, genus regularizers and
the complete source are included in R. On a cleared common block tube it
is analytic near every retained node. Its derivatives are fixed-coordinate
derivatives before substitution. This avoids assigning independent edge
tails or using a nonabsolute first-power sum.

Taking the finite part at x_i gives
`U_i=sum_{j in I,j!=i}1/(x_i-x_j)+R(x_i)`. Differentiate along the node:

    U_i,u=2 sum_{j!=i}(U_i-U_j)/(x_i-x_j)^2 + f_i.             (1)
    E_u=2 sum_{i<j}(U_i-U_j)^2/(x_i-x_j)^2 + (PU) dot (Pf).  (2)

The internal contribution is nonnegative in backward time. To prove (2),
pair the i,j terms in `(PU) dot U_u`; mean subtraction cancels because
each pair contributes zero to the node sum. This exact anti-dissipative
sign is not a theorem of growth of the complete E: the signed exterior
term may cancel it.

Let L be the weighted graph Laplacian with weights `(x_i-x_j)^(-2)`.
Since L annihilates constants, (1) and Cauchy--Schwarz imply, in the upper
Dini sense also at r_U=0,

    (r_U)_u <= 2 lambda_max(L) r_U + |Pf|.                    (3)

Every retained gap satisfies the common-label identity and bound

    g_i(u)=g_i(0)-2 integral_0^u (U_(i+1)-U_i) ds,
    min_i g_i(u) >= min_i g_i(0)-2 sqrt(2) integral_0^u r_U ds. (4)

The last inequality holds simultaneously for every edge, so it does not
assume a fixed minimizing index. Outer-edge exits and exterior entry must
still be excluded independently; a merging edge's regular pair chart
does not make its neighbors regular.

### Frozen scalar compression fails the compact target

The particular tested consumer replaces every adjacent gap denominator
by the uniform stop `s=2sqrt(d_stop)=1/50` and replaces `Pf` by an
independent nonnegative norm allowance. For the two-node block,
`lambda_max(L)=2/g^2<=2/s^2`, so its scalar upper envelope has

    R_U,u=10000 R_U+F_ext(u),   F_ext>=0,
    R_U(0)>=r_U(0),   R_U(u)>=r_U(0) exp(10000u).             (5)

The last inequality concerns the **comparison envelope**, not the actual
canonical force dispersion. Even zero exterior allowance and zero added
errors cannot make this consumer pay the requested interval. Indeed,
the inherited upper anchor bounds give `g0<423/500=.846`, `M0<151/250`,
and the exact edge identity gives

    U_1-U_0=2/g0-g0 M0
       >1000/423-(423/500)(151/250)>37/20.

For two nodes `2sqrt(2)r_U(0)=2|U_1-U_0|>37/10`. Equations (4)--(5)
therefore require, even in this favorable zero-error case,

    Delta <10^-4 log(1+10000(.846-.02)/3.7)
          =10^-4 log(82637/37) < .0008.                     (6)

The last strict inequality follows without floating arithmetic from
`exp(8)>sum_{k=0}^{10}8^k/k!=3830591/1575>82637/37`.
This is far shorter than .1003. It rejects only the fixed-stop-denominator,
unsigned-exterior scalar compression (3)--(5), not state-dependent
denominators, signed exterior correlations, refreshed anchors or the
canonical dynamics. It does not prove an obstruction for every larger
block or every force functional.

### What its source/error contract would cost

One common source enclosure must pay H_z,H_zz at the uncertain nodes and
a nonzero H_z denominator, or equivalent whole-block contour finite parts.
For approximants h1,h2 with errors e1,e2, `|h1|>=b1>e1`, `|h2|<=b2`,

    |U-h2/(2h1)| <= e2/[2(b1-e1)]
                     + b2 e1/[2b1(b1-e1)].                (7)

Root-location errors require source spatial derivatives on the same
cleared regions. Bounds for f require R_u and R_z jointly, hence time
jets or the heat equation with spatial jets and remainder. If inverse
square distances are approximated, two positive distances >=s with
error e have reciprocal-square error at most `2e/s^3`; the corresponding
finite Laplacian norm error must be added to (3). With node errors the
distance error is at most the sum of the two endpoint errors.
Boundary and complete exterior effects are in f, not zero. Whole-time
source, quadrature, tail, arithmetic and interpolation errors are required.
The same direct node evolution has all this information and retains the
signed differences in (4), so the norm compression supplies no dominance
over it. No favorable f bound has been acquired here.

## 3. Candidate B: retain the regular pair's transient

The complete contour passage of Note27 gives on a stopped positive pair

    D_u=-2+4DM,   M_u=-2M^2+F,
    V_u=(1-V^2-K)/D,   D_u=-2V.                             (8)

This candidate concerns the transient of this joint system, not another
independently evolved lattice row. Its exact identity

    A=(1-V^2)/D=4M(1-DM),   A_u=4VF=-2F D_u                 (9)

shows where a signed physical forcing enters. We do not divide a signed
integral by an uncertain minimum weight or assume monotonic D to use it.
The comparison below uses (8) directly and requires neither V>=0 nor
monotonicity of the actual gap.

### Keeping the transient still does not repair a constant K floor

For `g=2sqrt(D)`, (8) gives `g_uu=16(K-1)/g^3`. For a constant
`K>=kappa<=1`, the scalar comparison starting from `D0=d0`, `V0=v0`
has the explicit solution, until its first zero,

    d_kappa(u)=d0-2v0u+[(v0^2+kappa-1)/d0]u^2.             (10)

To verify it, differentiate `2sqrt(d_kappa)` twice. The system
`g_u=w, w_u=16(kappa-1)/g^3` is cooperative on g>0 because the second
right side is increasing in g. Thus initial lower g and lower w give a
lower solution; exact actual initial values in (10) give the sharp
constant-floor model. This comparison keeps the initial transient that
Note27's one constant-v consumer discarded.

Nevertheless Note27 proves at the included canonical slice t=0 that
`K<kappa*=1057/375000`. Give (10) the favorable values
`d0=d+`, `v0=v-=1-2d+ b+`, and `kappa=kappa*`. These maximize initial g
and initial velocity among the allowed anchor data; cooperative comparison
also makes the resulting model most favorable before a zero. Exact
rational evaluation yields

    d_kappa*(Delta)<-0.00008239.                            (11)

It has already reached zero before Delta. In contrast the required
constant floor even with these favorable anchor values is

    1-v-^2+(d+/Delta^2)(d_stop-d++2v- Delta)>0.00605917,

larger than kappa*. This is a new screen of the **sharp constant-K
second-order comparison from this anchor**, not of time-varying K or
constant physical F. The old constant-v rejection remains correct and
historical; (11) strengthens its consumer class without universalizing it.

### A constant physical F floor has a strictly positive conditional margin

Suppose instead that the **complete signed** forcing satisfies `F>=f=3/10`
through the stopped trial region. Define `lambda=sqrt(2f)`,

    S(u)=sinh(lambda u)/lambda,
    W(u)=cosh(lambda u)+2b S(u),
    m(u)=W'(u)/(2W(u)),
    d_f(u)=W(u)[d W(u)-2S(u)].                              (12)

Then `m_u=f-2m^2`, `m(0)=b`, and `d_f,u=-2+4m d_f`, `d_f(0)=d`.
The scalar Riccati difference satisfies
`(M-m)_u>=-2(M+m)(M-m)`, hence M>=m. On the stopped positive-D interval,

    (D-d_f)_u=4m(D-d_f)+4D(M-m)>=4m(D-d_f),

and D>=d_f follows by an integrating factor. Formula (12) uses
`integral_0^u W^-2=S(u)/W(u)`, proved by differentiation.
All of this works for nonreal exterior zeros when the signed complete
F floor is acquired; no positive-tail omission is used.

For the frozen rational d,b,Delta, a rational Taylor enclosure proves

    d_f(Delta)>0.00016246,
    d_f(Delta)-d_stop>0.00006246.                           (13)

Here is a reproducible exact enclosure, with no source samples. Put
`w=4lambda^2 Delta^2`, `v=1-2db` and
`J=d/2+(2db^2-2b)/lambda^2<0`. Algebra gives

    d_f(Delta)=d+J[cosh(2lambda Delta)-1]
                    -v sinh(2lambda Delta)/lambda.

Upper-bound cosh by
`sum_{j=0}^4 w^j/(2j)! + (w^5/10!)/(1-w/(12*11))`, and
`sinh/lambda` by
`2Delta[sum_{j=0}^4 w^j/(2j+1)! + (w^5/11!)/(1-w/(13*12))]`.
Every omitted successive-term ratio is bounded by the displayed geometric
ratio. Because J<0 and v>0, substitution gives a rational lower bound;
comparison to `16246/10^8` proves (13).

This endpoint bound is a whole-interval comparison: W>0 and
`d_f/W^2=d-2S/W` decreases, so positivity at Delta gives positivity
throughout. Also `0<m<=b` because `b>sqrt(f/2)`. The scalar d_f cannot
cross its initial upper barrier d, since `4bd<2`. Therefore
`d_f,u<=-2+4bd<0` on this positive interval, and its minimum is at Delta.
At a hypothetical first lower exit D=d_stop, D>=d_f>d_stop is a
contradiction. The other contour and coordinate exits require the
independent acquisitions specified in Section 1.

The improvement is an explicit **conditional** margin over the two
constant-K reductions, not a canonical certificate. Small K=2D^2 F at
t=0 is compatible with F>=.3, so the included-slice screen does not reject
this input. It does not establish that input either.

## 4. Source acquisition, errors and direct comparator for B

On the count-two circle and arbitrary allowed trial Q, the complete field
acquires the combined signed forcing by

    F_Gamma=-(1/(2pi i)) integral_Gamma
                   B(12/Q^2+16D/Q^3) dz.                  (14)

When the cleared annular log L of Note27 is available, its equivalent
kernel is `-integral L Q'(24/Q^3+48D/Q^4)/(2pi i)`.
These identities keep all exterior occurrences; there is no independently
discarded zero tail. A finite source evaluation must itself pay the full
theta/xi and Gaussian/source tails on the extended physical domain.

For uniform source error eB on the circle the contribution to the
forcing error is at most

    E_F,source <= r eB(12/q^2+16Dmax/q^3).                  (15)

For a log error eL it is at most
`r eL 2(r+C)(24/q^3+48Dmax/q^4)`. Note27's quotient bound pays eB from
field/first-jet errors and a positive contour denominator. If the trial
parameters are approximated rather than interval-covered, add at most

    r Bmax { (48(r+C)/q^3+96Dmax(r+C)/q^4) e_c
                   +(40/q^3+48Dmax/q^4) e_D }.              (16)

This follows by differentiating the combined kernel with respect to c,D
on the whole connecting parameter segments; Bmax bounds the exact B.
Add quadrature, outward arithmetic, reconstruction and whole-cell time
errors. A cleared angular strip with modulus A_s pays trapezoidal error
`2A_s/(exp(Ns)-1)` for the parametrized integrand; both the field and Q
must be cleared on that strip. The heat identity
`partial_t^j H=(-1)^j partial_z^(2j)H` needs an explicit Taylor remainder
for genuine time-uniformity. Values at sample times are insufficient.

The required acquisition is explicitly

    lower(Fhat_Gamma)-E_source-E_parameter-E_quadrature
        -E_arithmetic-E_time-E_reconstruction >=3/10        (17)

on a proved stopped reachable region or the full stated trial box.
The anchor intervals already include their old source/arithmetic error;
new ones must not be silently added without reducing d or b. Uniform
trial evaluation avoids divisions by the target gap: q stays 11/25.
If source jets at simple roots replace it, the H_z and root-reciprocal
errors of (7) and the applicable positive stop must be paid separately.
The contour, label and spatial-boundary counts remain independent gates.

The inherited annular log bound supplies an absolute F bound, not the
signed lower bound (17). The old source oracle's nonnegative-time domain
does not automatically extend to t<0. No favorable head, negative-time
source error, time-wide trial/coordinate bound or total error in (17) is
claimed. The trial floor may itself fail. This is the exact missing
source estimate, rather than a new hypothesis asserted equal to the goal.

Give direct regular D/M evolution the same initial intervals, physical
duration, complete F floor, all errors and count/coordinate payments.
It produces (12) exactly. Direct contour discriminant acquisition also
gets the same field and should be tested if that field is ever acquired.
There is no demonstrated lattice advantage in duration, margin, cost or
coverage over these equally informed comparators. No source campaign is
justified merely by the change of coordinates.

## 5. Collision controls and the bounded decision

The [control catalog][controls] is screened analytically at premises,
without numerical reruns. Generic heat identities (1)--(14) are not
supposed to reject physical collision controls. Their quantitative floors
and source-specific data, when used, are separate premises.

| Control | Premise or payment it does not supply |
| --- | --- |
| Quadratic/quartic heat fields | Complete canonical theta source and growing population; the quadratic has F=0 and cannot meet the selected .3 floor. Generic block identities remain valid before its collision. |
| Stationary cosine / cosine plus a constant | Canonical source/count profile absent. A colliding cosine-plus-constant field need not fail every positive F floor, but cannot satisfy the **whole** start, duration, clearance and strict-margin contract across its collision. No generic assertion F vanishes at collision is made. |
| Euler-factor translates, for every parameter/prime in the catalog | Exact normalized theta arithmetic/source equality fails; shared positivity, heat flow, symmetry and some counts do not acquire (17). |
| Weighted squares; finite-tail/score and finite-prime orbit controls | Full reflected unit-weight theta source equality fails; documented endpoint-defective subclasses additionally fail the strip. These are distinct failed premises, not one universal strip assertion. |
| Reflected super-Gaussian; smooth shape/positive-primitive controls; earlier counter-kernels | The former fails the canonical order-one class; the latter families change exact theta arithmetic/source and do not supply the complete canonical strip/count/contour transfer. Shape and positivity do not sign (17). |
| Atomic/fixed-profile threshold controls | Complete theta profile and canonical population are missing; local heat profiles and finite moments do not pay the retained forcing bound. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet arithmetic fails and RH remains an input; the corresponding source is not substituted for the canonical one. |
| Changed observations; fractional profiles | The physical cosine/Newman readout or integer divisor multiplicity premise fails, respectively. |
| Static divisor surgery or scalar weighted-energy examples | No established common canonical heat tube, or no claimed divisor realization. They do not disprove (17) for theta. |

**B08 r2 selects the retained-F comparison as a quantified source target,
but closes without a ready acquisition packet.** Candidate A's particular
unsigned compression is rejected by (6); a sharper constant-K reduction
of candidate B is rejected by (11). Candidate B with F>=.3 has the strict
conditional margin (13), while its actual source acquisition and any gain
over direct D/M remain unpaid. These are separate findings.

A further conceptual pass must decide whether a signed complete contour
estimate can acquire (17) and the independent new-domain clearances at a
credible cost, compared with direct discriminant/D/M evaluation. Its
output must be a genuinely ready, finite source contract or a scoped
disposition, not another time-envelope identity. E29 checks this note and
its finite arithmetic only. E16 r3 stays independently optional and
unexecuted. No manuscript integration, new zero coverage, Lambda bound,
stable finite closure or larger numerical campaign is asserted.

[register]: ../research-progress/01_VCD_GT_CM_RESEARCH_PROGRESS_20261117.md
[prior]: 31_VCD_GT_CM_COUPLED_LATTICE_MANUSCRIPT_CONTINUATION_20261118.md
[compact]: 27_VCD_GT_CM_COMPACT_CONTOUR_SELECTION_AND_FLOOR_SCREEN_20261118.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[coordinates]: ../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
