# Buffered conductor cutoffs and a further selector-preserving sector

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant
and configured reasoning effort are not exposed and are not inferred.
The computations and deductions below are not independent specialist
validation of the imported analytic statements.

**Result.** The sharper full-bin count and tapered target give a rigorous
operational total-conductor cutoff between approximately `U^0.903444`
and `U^1.071249` on an explicitly buffered application region. More
substantively, a count-sensitive bound on the **positive selected inverse
mass** removes an additional plain-conductor sector from the actual
signed residual. On a nonempty subregion its plain-cutoff exponent
increases by `1/12500`, beyond the taper/count refinement alone.
This is a conditional sector estimate, not the missing full mixed bound.
No new zero-free boundary, exponent descent, or RH implication follows.

The inputs are the current
[amplification manuscript](../../quasi-rh-character-amplification/manuscript.tex),
[two-ratio reduction](../../quasi-rh-character-amplification/notes/SELECTOR_PRESERVING_PLAIN_CONDUCTOR_20261008.md),
[proved mixed subcases](../../quasi-rh-character-amplification/notes/SELECTOR_PRESERVING_SUBCASES_20261008.md),
[energy localization](../../quasi-rh-character-amplification/notes/SELECTOR_ENERGY_LOCALIZATION_20261008.md),
and [scoped review](../../quasi-rh-character-amplification/reviews/SELECTOR_PRESERVING_REVIEW_20261008.md).
This implements Route A of the
[continuation](CODEX_CONTINUATION_20261008.md).

## 1. Dependency and quantifier ledger

| Item | Status used here |
| --- | --- |
| Marked inverse second moment, buffered conductor-sensitive plain bound, full-bin exponent `R*` | Imported analytic inputs, conditional here |
| Pointwise inverse envelope and the envelope for the original physical prime sums | Additional imported inputs, as in the energy note |
| Ratio identity with canceled-phase zero masks; ideal-pair count | Existing elementary lemmas, used with their original coefficients |
| Buffered cutoff identities and continuous rational bounds below | New deductions; arithmetic certificate supplied |
| Smaller positive selected inverse mass and its enlarged plain-conductor sector | New conditional selector-preserving estimate |
| Signed residual beyond both enlarged cutoffs | Unproved |

The September 30 source theorem, detector, and moments are not revalidated
here, and no Lean replay is claimed. In particular zeta-only quasi-RH
does not supply these family inputs. The source's global family theorem
and pointwise physical-profile hypotheses must retain their original
logical status.

Use `d` for the amplification bin parameter, `d in [9/25,21/50]`,
and `x in [49/100,1/2]`. The factors `M_r,S_m,Q_I`, their normalized
annuli, actual ideal Möbius coefficients, truncated inverse cutoff,
fixed ray presentation, common orientation, disjoint whole physical
prime slots, fixed exclusions, and every zero extension are unchanged.
In particular, this note does not delete primes from a physical annulus.
The selected physical row set is exactly the original full buffered bin
`C`, fixed before selecting the current witness pair. Set

    C+ = {u in C : Q_(psi_u) > U^(2m-1/1000)},
    H = 1+T_1,  eta = 1/5000,  gamma = 1/6250.

Work first at common fixed separating parameters. All bounds intended
for the application must be uniform for the source's derivative-profile
families, before its positive-norm Sobolev argument handles rowwise
heights. Polynomial height costs and arbitrary small analytic losses
are retained as `H^A U^epsilon`. A scalar estimate at one profile is
not silently promoted to derivative uniformity.

## 2. An operational version of the tapered cutoff

Retain the continuation's notation

    alpha=5/6, a=alpha-d,
    B=2-8x/9, D=3-17x/9, P=B(1-x), J=aD+dP,
    R*=1-d+a d P/(2J), F=aB/J,
    r_new=1-F/2-(1-F) eta/[d(1-x)],
    m_new=1/2-(a/J)[(1-x)/2-eta/d].

Write `a_r=r-r_new`, `b_m=m_new-m` and
`s_0=eta-d(1-x)a_r`. Take the concrete small loss budget

    ell=1/1000000.

This is a sufficient budget, not an assertion that arbitrary source
parameter choices attain it. Require that `ell` dominates each of the
two marginal count-exponent losses and the detector support loss; assume
the full-bin count available for the chosen setup is

    #C << U^(R*+ell+epsilon) H^A.                         (1)

Also require that the **actual** simultaneous-witness and selected-prime
amplitude bookkeeping needs at most `s_0+ell` saving. The latter condition
includes the slot-capacity loss, whole-slot rounding, and amplitude-bin
losses. It must be checked from `s_actual` in the continuation; it does
not follow merely from the support inequalities below. These fixed small
losses must fit inside the existing conditional payoff reserve.

The operational region left by the old marginal counts satisfies

    a_r < (eta+ell)/[d(1-x)],
    b_m > -ell/(dB),
    b_m <= a_r+ell.                                     (2)

Define

    s = s_0+ell,
    gamma_ell = gamma-3ell = 157/1000000,
    K_s = 1+dm-s,
    v = 2(dm-s-gamma_ell),
    tau = 2(1+dm-s-gamma_ell-R*-ell).                    (3)

The lower bound `a_r>-(39/14)ell`, already proved in the energy
note, gives

    0 < s < eta+2ell,
    d/1000-s-gamma_ell >= ell.                          (4)

Indeed `d(1-x) <= 1071/5000` and
`(1071/5000)(39/14)<1`. The low primitive-row-conductor term is therefore
at most `U^(K_s-gamma_ell-ell+epsilon)H^A`; the old threshold
`U^(2m-1/1000)` is retained. The other identities are exactly

    1+v/2 = K_s-gamma_ell,
    R*+ell+tau/2 = K_s-gamma_ell.                        (5)

The operational region stays inside

    0.70571698 < r < 0.72957194,
    0.40398543 < m < 0.41232277.

These decimal enclosures are backed by rational inequalities in the
record below; in particular all lengths remain inside the original
source rectangle, and `v>7/25>0`.

Let `T(tau,v)` denote exactly the continuation's signed tuple sum, but
with its two restrictions replaced by

    N f(n(t),n(t')) > U^tau,
    N f_plain(k,k') > U^v.                              (6)

The tuple coefficient `b(t)`, normalization `X_col^-1`, original physical
row selector `C+`, ratio phase `chi_c`, and canceled-phase mask
`1_((u,E)=1)` are unchanged. The same ordered proof gives

    sum_(u in C) |M_r S_m Q_I|^2
       = Re T(tau,v) + O(U^(K_s-gamma_ell+epsilon)H^A).   (7)

First remove low primitive row conductors. On `C+`, expand only the
plain factor, retaining the positive weight `|M_r Q_I|^2`, and remove
small plain-ratio conductor using the marked inverse mass `U^(1+epsilon)`.
Only then expand the other factors and remove small total conductor by
the absolute tuple majorant and (1). This proof never puts a total-ratio
restriction inside a purported positive inverse norm.

## 3. Continuous cutoff certificate and the actual improvement

For fixed `(d,x)`, put

    tau_A=2(1+d m_new-eta-gamma-R*).

Substitution in (3) gives the useful affine identity

    tau = tau_A + 2d[(1-x)a_r-b_m] + 2ell.               (8)

Optimizing the affine term on the closure of (2) gives

    tau_L = tau_A - 2x(eta+ell)/(1-x) - 2d ell + 2ell,
    tau_H = tau_A + 2eta + 4ell + 2ell/B,
    tau_L <= tau <= tau_H.                             (9)

Both bounding functions increase with `d` and `x` on the entire box.
The resulting exact continuous infimum and supremum on the buffered
region are

    822322221061601/910208262500000 <= tau
       <= 2977001009/2779000000,

    0.9034440302738967... <= tau <= 1.0712490136739834.... (10)

Strict boundaries in (2) mean limiting corner values, rather than a
claim that these endpoints occur at a permitted selected rectangle.

This is not a floating scan. The standard-library script
[check_mixed_conductor_refinement.py](../numerics/check_mixed_conductor_refinement.py)
uses automatic differentiation in rational interval arithmetic on
`32 x 32` closed cells covering the whole `(d,x)` rectangle. Its
division operation fails if a denominator interval contains zero.
The exact interval rules and derivative product/reciprocal rules
enclose each derivative everywhere in its cell. The script certifies,
for example,

    partial_d tau_L, partial_d tau_H >= 13517/5000,
    partial_x tau_L >= 1723/10000,
    partial_x tau_H >= 1739/10000.                      (11)

Thus corner evaluation in (10) follows from a continuous sign proof.
The deliberately coarse rational bounds (11) are below the exact
interval lower bounds. This is a reproducible finite arithmetic
certificate, not a formal proof-assistant verification.

For comparison, let

    R0=9/8-23d/20,
    tau_old=2(1+dm-eta-gamma-R0).

The same continuous certificate proves `R0-R*` decreases with `d`
and increases with `x`, giving

    3951043/1006206500 <= R0-R* <= 61273/3383000.         (12)

Moreover

    tau-tau_old = 2(R0-R*)+2d(1-x)a_r+2ell,

and its final two terms have positive sum throughout (2). Hence the
total cutoff exponent increases by at least

    3951043/503103250 = 0.00785334421910413... .           (13)

This quantifies a uniform gain over the old coarse cutoff even after
the displayed operational losses. Likewise `v` is larger than the
old `2dm-2(eta+gamma)` throughout (2). These are gains in the amount
of residual that can be discarded; they are not gains in the still
unproved bound on its complement.

## 4. A new positive-mass refinement of the plain sector

The following step uses the pointwise **physical-profile** inputs in
addition to the three inputs of the elementary two-ratio reduction.
Suppose, uniformly on the bin and required derivative families,

    |M_r(u)|^2 << U^(dr+epsilon)H^A,
    |Q_I(u)|^2 << U^(Gamma_I+epsilon)H^A.                (14)

For the original physical prime sums one may use `Gamma_I=dz`, with
`z <= (1-r)/2` and the original strict inverse capacities. An improved
profile-specific `Gamma_I` is permissible only with the necessary
uniformity. Arbitrary prime subsets are not justified by (14).

Define

    mu_C = max(0, 1-R*-ell-dr-Gamma_I).

Then the **same selected positive inverse mass** satisfies

    A_C := sum_(u in C+) |M_r(u)Q_I(u)|^2
      << U^(1-mu_C+epsilon)H^A.                         (15)

Proof: the marked inverse input gives exponent `1`; counting rows with
(1) and (14) gives exponent `R*+ell+dr+Gamma_I`. Take their minimum.
No signed kernel is enlarged and no rowwise coefficient is changed.

For every `V>=1`, the exact weighted plain-ratio expansion consequently
satisfies

    N^-1 sum_(N f_plain(k,k') <= V)
       |a(k) conjugate(a(k')) K_w_plain(k,k')|
       << U^(1-mu_C+epsilon) V^(1/2+epsilon) H^A,        (16)

where `w(u)=1_(C+)(u)|M_r(u)Q_I(u)|^2`. The kernel in (16)
retains `chi_(c_plain)(u)` and the entire canceled-phase mask
`1_((u,E_plain)=1)`. Equation (16) follows from the already proved
ideal-pair count and `|K_w_plain|<=A_C`. It is absolute only after
the whole inverse/prime polynomial has been assembled into `w`.

Set

    v_dagger = v+2mu_C.                                (17)

Equations (15)--(17) give `1-mu_C+v_dagger/2=K_s-gamma_ell`.
Therefore (7) holds with `T(tau,v_dagger)` in place of `T(tau,v)`.
This proves a new selector-preserving sector estimate:

    |T(tau,v)-T(tau,v_dagger)|
      << U^(K_s-gamma_ell+epsilon)H^A.                  (18)

For clarity about the intersection in (18), first assemble the plain
annulus `U^v < N f_plain <= U^v_dagger` against the positive weight
`w`; its whole signed contribution is bounded by (16). Subtract its
low-total-conductor portion, which is bounded by the same absolute
tuple majorant used in (5). The difference is exactly the high-total-
conductor portion in (18). One must not put that total-conductor cutoff
into `w` before invoking (15). All masks and cross terms survive this
subtraction.

## 5. A nonempty buffered subregion with a fixed extra removal

Use the universal physical envelope `Gamma_I=dz` and its worst allowed
value `z=(1-r)/2` in estimating (15). On the operational region, the
following subregion gives an explicit gain:

    4999/10000 <= x <= 1/2,
    a_r <= 1/10000.                                    (19)

Negative `a_r` allowed by the outer buffer are included. The exact
rebalance identity gives

    1-R*-ell-d(r+(1-r)/2)
       = (1-F)eta - (d/2)a_r
         -d(1/2-x)(1-r_new) - ell.                     (20)

The earlier continuous bounds `F<=1988/3383` and
`r_new>=47749/67660`, with `d<=21/50`, imply throughout (19)

    mu_C >= (1-1988/3383)/5000
       -(21/50)/(2*10000)
       -(21/50)(1-47749/67660)/10000 - ell
       = 1627609/33830000000
       > 1/25000.                                     (21)

This proves that one may uniformly take

    v_dagger = v+1/12500                               (22)

in (18) on (19), under the stated physical inputs. A positive fixed
decrement from `(1-r)/2`, as required by the strict inverse capacities,
only improves (20); no endpoint moment theorem is being used.

For a concrete interior example take

    d=9/25, x=1/2, a_r=1/20000, b_m=1/40000.

The certificate gives

    s=3/15625 = 0.000192,
    mu_C >= 24517/338300000 = 0.0000724711794...,
    tau=1531921103/1691500000 = 0.90565835235...,
    v=246482243/845750000 = 0.291436290866...,
    v+1/12500=246549903/845750000 = 0.291516290866....

The complete-moment count estimate at this example saves only `mu_C`,
strictly less than the required `s`. Thus the result is a genuine
additional conductor-sector removal at a point not already covered by
that positive count estimate, rather than a disguised full-moment claim.

## 6. What remains, and the next useful test

The remaining exact tuple sum has both

    N f_total > U^tau,   N f_plain > U^(v+2mu_C),

with the original coefficients, row selector and masks. It still needs
the signed upper bound at exponent `1+dm-s`. Neither thinness of the
application triangle nor the increase of either cutoff proves that
bound. No general relation between the two ratio conductors is assumed.
The primitive conductor of a row is a third different quantity.

The new estimate suggests a more precise next target than another
unqualified moment interpolation: seek an arithmetic bound for the
weighted plain kernel on **large** plain-ratio conductors, exploiting
the already assembled inverse mass in (15), or prove a stronger
conductor-resolved localization of that mass. A valid result must
control its distribution among ratio phases, not merely its total
mass. An arbitrary high-conductor restriction cannot be passed through
the positive factorization without the explicit intersection treatment.

Alternatively, an arithmetic decomposition of the plain coefficient
could remove a further sector, but it must improve on the existing
all-cofactor cost while preserving the annulus, inverse cutoff and
full signal. The present note does not repeat the complete-row Poisson
or inadmissible transformed-width attempts already audited elsewhere.

The two original limitations remain: this local mixed program targets
a fixed small boundary improvement, and it provides no RH iteration.
The short-family and alternative-endpoint programs should continue in
parallel.

Reproduce the small record with

```sh
python3 papers/quasi-rh-exponent-descent/numerics/check_mixed_conductor_refinement.py
```

The saved output is
[mixed_conductor_refinement_certificate_20261008.json](../numerics/mixed_conductor_refinement_certificate_20261008.json).
It certifies continuous finite-parameter algebra and the stated rational
inequalities, not the unproved mixed arithmetic estimate. All generated
files are small; no manuscript, historical note, or third-party PDF
has been changed by this lane.
