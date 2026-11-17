# VCD-GT-E18 r1 — Source and isolated-pair assessment

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Separate assessor dispatch
**gpt-6.1-sol / ultra**. Actual serving-model and reasoning-effort
metadata were unavailable. The assessor authored none of the
batch. This is a separate internal assessment with shared source
premises and model family, without specialist independence or a
literature-priority finding.

**Accepted within scope without required correction.** The accepted
outputs are E16's scoped lower-allowance failure, E17's unconditioned
mean bound and collar-conditional pointwise identity, E19's two
fixed-time isolated-pair counts, and revised Synthesis39. The
quantitative gains concern normalized collar radius and counts at a
fixed time. The [result index][results], [controls12][controls] and
[avoid index][avoid] govern the classification and scope. See
[classification01][class], [premises02][premises], [shared review05][shared]
and [scope07][scope].

## 1. Inputs and sequence

The [issued request][request] and its ten Stage A pins matched when
read, including the original Synthesis39. At Stage A I checked the
completed E16 and E17 proofs and derived the E19 route independently
of its proof output. The [frozen addendum][addendum] and all three
Stage B pins matched before final review. Its revised Synthesis39
supersedes the Stage A synthesis for this assessment. Its source
status wording, density band, $b=1/4$ example, $TL$ normalization,
and stronger Note34 control paragraph were all rechecked. The six
inputs pinned by the E19 request also matched, including Note34 and
the inherited TND-O Note21 and Assessment07.

| Reviewed input | SHA-256 |
| --- | --- |
| [E18 r1 request][request] | 855efeebc178b9e6eb047772161ab358f53dfd9bf439de03b11b6b0a1b0bc6a7 |
| [Note36][e16] | fa31227bc57ed8aa78fbec5231cabefb6c0508de80e6e6462a3ea2bfa5a589d4 |
| [E16 return][r16] | 77cb42ed38e2f563f572b61f532cc2b2025097ddf638f6b993ccdecdbbc1d91e |
| [Note37][e17] | 8b78a4fc25dc8e671238210a61ea359c764427cd72a12f48ae2a38e1723f923b |
| [E17 return][r17] | 87449f2410dc73c0a16e6239283182038ad1c241c609d69fa7043aee2cd0058f |
| [Decision17][b09] | 2f207ecc12dd3e9c14c06b0bb9be352b5471532c4d90e07e2b29436702df7585 |
| [Decision18][b10] | 0e88dcbf430414681687fc71b3d6e73b8113c7178b2921cb155d7a3c3af005fb |
| [E19 r1 request][q19] | 836772f122a86caee26a9998b65113cf6edd1ad9611e847383da1774c82b492b |
| Original Synthesis39, retained in the Stage A pin | 4cad24a331a19c28ba7ad25180e09017bc35132c993f355fb33136f85ded3505 |
| [Source-use06][source] | 2484cb1535de12848598be67ac66db6bb4a5e1f16934d9741d2c6320b679f92e |
| [Predecessor audit16][audit] | 6bb3866c12598769a5e203ce97fd680b62b5ef865d4f66acba706228b524fbc9 |
| [E18 Stage B addendum][addendum] | 69a55faf8563fdc52300cb44cdec27106682aa5b728c56fadbb8ed0e8974cbde |
| [Note38][e19] | c1614650cb46dbc19062746d5e2115aa233a1b1d37bc991b6aaae9f42d0b1485 |
| [E19 return][r19] | 8d772c001058eb1c3b0b728baf56860751725f57b888090e8f2368b6b1783040 |
| Revised Synthesis39 as assessed | a275280664f8603e0a20b7be88c9f33fa168ae551b7bb4448f8d4a0fb2dc34bc |

The lead subsequently updated the [live synthesis][s39] to record this
disposition and route B11. The integrated file SHA-256 is
c78928797aa19ba4eb962b8395aa3ed8923fb90c54a19bbca26e0d7643573f35.
Reversing only its status and routing prose and its review link
reconstructed the assessed Stage B hash.

## 2. E16 — Complete-source phase allowance

The literal theta primitive $p$ has $p(-u)-p(u)=\sinh u$ and
$p'(0)=-1/2$. Applying $\partial_u^2-1$ to the reflection and
differentiating the complete series give
$\Phi=(p''-p)/8$ as a smooth even density across the origin.
Each derivative on the half-line is a convergent sum of
$e^u Q_j(r_m)e^{-r_m}$ with $r_m=\pi m^2e^{4u}$ and
$\deg Q_j\le j+2$. The uniform majorant in (1) survives
$e^{tu^2}$, polynomial weights and $t=0,1/2$. The physical
$H_t$ uses one half of the full integral, so the normalized
$F_t$ uses $f_t=\Phi e^{tu^2}/Z_t$ with $Z_t=2H_t(0)$.
This agrees with the time-zero $\xi((1+iz)/2)/8$ normalization
and the physical heat sign. [Note36 §1][e16] · [Note12 §1][oracle]

In the Fourier product $i^3i^3=-1$ and $i^2i^4=-1$.
Symmetrizing $3u^2v^4-2u^3v^3$ gives the nonnegative weight
$u^2v^2(3u^2-4uv+3v^2)/2$. Its pushforward has
$\nu_t=3(a_4*a_2)-2(a_3*a_3)$, is even, and has mass
$T_t=3m_2m_4$ because the odd moment vanishes.
Uniform $\|\nu_t'\|_1$ and $\|\nu_t''\|_\infty$ and the decay
at each end follow by differentiating the decaying bounded
first convolution factors against the integrable second ones.
At zero, the odd factor reverses sign, yielding
$\nu_t(0)=5\int u^6 f_t(u)^2\,du$. This is the anti-diagonal
density value with zero mass assigned to the line itself. [Note36 §2][e16]

The allowance increases when another favorable phase is retained.
Retaining the entire allowed set maximizes it and gives the
periodic multiplier of mean $1/\pi-1/2$. Integration by parts
against its bounded primitive gives a uniform $C/c$ error.
The positive mass floor makes the optimal allowance eventually
strictly negative. For the first band $[-a/c,a/c]$, the even
density has zero first derivative at zero, so the constant term
of the Taylor expansion gives $2(a+\sin a)\nu_t(0)/c$ above
$-T_t$, and the second-derivative bound gives the stated
$O_a(c^{-3})$ remainder. Averaging lower allowances against a
nonnegative normalized measure preserves the high-center failure
for this class. At a nondegenerate real double the ratios of
deflated jets give $M=P_t/(18F_t''(c)^2)$, so this negative lower
allowance fails to certify the sign. The calculation leaves
the signs of the actual numerator and interaction undetermined,
and joint signed groupings of negative phases fall outside the
tested class. On a counted heat tube $D'=2-4MD$, hence $D'=2$
at $D=0$. A persistent interval of double slices cannot support a
time-average argument for $M$. [Note36 §§3–4][e16] · [Note24][jet]

## 3. E17 — Mean and signed radial bridge

The source inputs in [TND-O Note21 (2), (7)–(9)][density] and
[Assessment07 §5][inherited] are for the complete multiplicity
divisor on $0\le t\le1/2$, with closed real endpoints and a
strict transverse tail cutoff. The H-coordinate satisfies
$x=2\gamma$ and $y=-2(\beta_{\zeta}-1/2)$. The accepted transfer
fixes $0<b<1/2$ with a constant depending on $b$ and gives
the second-moment constant $C_b^{\rm moment}=2B_b/b^2$.
It provides no conditioned moment. I checked the source identity,
coordinate normalization and relevant statement against the
existing primary-source receipt. The inherited heat-time transport
chain was used in its reviewed scope. [Source-use06][source]

For $0<|y|<r_0$, integrating the two tails gives
$r_0^{-1}(\arcsin s-s\sqrt{1-s^2})/s$, with $s=|y|/r_0$.
The ratio of the numerator to $s^3$ increases up to $\pi/2$.
The full-line case $|y|\ge r_0$ equals $\pi/(2|y|)$, including
equality at $|y|=r_0$. The real-zero case contributes zero.
Thus the one-zero kernel has upper bound
$(\pi/2)\min(1/r_0,y^2/r_0^3)$. The real support condition
restricts contributing ordinates to $[T/2,5T/2]$, covered
by the three closed bands with scales $T/2,T,2T$.
The moment costs are $2/3,1,2$ times $C_b^{\rm moment}T/L$.
With $r_0=a\ell$, Tonelli gives constants
$C_s=11\pi C_b^{\rm moment}/6$ and $C_0=3\pi A$ for the
source $a^{-3}$ and the matched $a^{-1}$ mean bounds respectively.
At a fixed normalized collar both are constant-order allowances.
Markov bounds ordinary center measure on the band. [Note37 §§1–2,4][e17]

The exact radial subtraction uses
$|w^2-D|^2=(r^2-D)^2+4Dy^2$. The collar gives
$|w^2-D|\ge(1-\delta)r^2$ and $r^2\pm D\ge(1-\delta)r^2$
for either sign of $D$, where $\delta=d/a^2<1$.
The correction subtracted from $(r^2-D)^{-1}$ is nonnegative
and at most $2(1+\delta)(1-\delta)^{-3}y^2/r^4$.
The target occurrences are strictly inside the radial cutoff,
so the transverse sum at the selected center has exactly the
needed exterior occurrences. This comparison uses the actual
$\Xi$ at that center and the paid collar. It leaves the radial
lower mass, a fixed-collar selected-pair $o(1)$ correction and a
full sign open. [Note37 §§3–4][e17]

## 4. E19 — Fixed-time isolated-pair counts

Every target lies within $r_0/4$ of the real center.
If distinct pairs share an occurrence, the second pair's extra
occurrence lies within $3r_0/4$ of the first center, contradicting
its exterior cutoff. This uses occurrences and applies to an exact
double. Disjoint pairs then have center separation at
least $(a-\sqrt d)\ell\ge3r_0/4$, yielding
$1+4TL/(3a)$. The intervals of length $r_0/2$ are disjoint.
[Note38 §§1–2][e19]

The full geometry is $T\ge16$, $\max(2,4\sqrt d)\le a\le L$,
$3\le R\le T/4$, $c\in[T,2T]$, $|D|\le d\ell^2$, and an
exterior cutoff $r_0=a\ell$. Moving the center by at most
$r_0/4$ preserves each original term under the shifted radial
cutoff $r_0/2$ and horizontal cutoff $R+r_0/4$. The distance
increases by at most a factor $5/4$. This pays
$\beta=(4/5)^4$ even at originally closed cutoff boundaries.
The padded integration interval costs a zero-band padding of
$r_0/2$ beyond $[T-R,2T+R]$, still inside $[T/2,5T/2]$.
Reintegrating the same kernel costs $8C_sT/a^3$ or
$2C_0T/a$. Division by $\beta h\,r_0/2$ gives
$16C_sTL/(\beta a^4h)$ or $4C_0TL/(\beta a^2h)$ for
$\Xi\ge h>0$. The bound $C_\delta\le8704/3375$ for
$\delta\le1/16$ gives the strong-negative threshold
$h=\epsilon/(8704/3375)$ for $\ell^2S_R\le-\epsilon$.
The separate pointwise count and strip comparison costs
$O(L/a^2)$ on $|x|\le1$ and $O(1/L)$ on the inverse-fourth
shells beyond. It already excludes fixed $h$ when
$a/\sqrt L\to\infty$. The power-law comparison for fixed
$h$ is used at $a=L^\eta$, $0<\eta<1/2$. [Note38 §§4–5][e19]

For the signed estimate the same three bands make the enlarged
density constant $B_b^*=5B_b$. The relative costs are at
most $2^{b-1},1,3$ and the transverse condition is strictly
$|y|>v$. A negative individual $q$ gives
$y^2>(r^2-D)/2\ge(15/32)r_0^2$, hence
$|y|>v_0=2r_0/3$. For the contributing zero the negative
numerator also gives $|x|<\sqrt{y^2+D}\le |y|+r_0/4$.
Packing in this window gives at most $5/3+8|y|/(3r_0)$
incident eligible centers. Summing over occurrences and using
$v_0N(v_0)+\int_{v_0}^1N(v)\,dv$ for the height sum gives
the stated factor $31/9+8/(3ab)$. The boundary at $v_0$ is
excluded and a mark at $1$ is covered by thresholds below $1$.
For $|x|>R$, the strip and $|D|\le1/16$ give
$x^2-y^2-D>0$. The divisor sum converges absolutely by the
unit count against inverse-square shells. Therefore $M\ge S_R$,
so the near count bounds the full negative count, including the
one-way strong-threshold implication used above. [Note38 §§1,3–4][e19]

The signed count is at most $C_b'TL e^{-2ba/3}$ for fixed $b$.
The $b=1/4$ example gives $C T\log(T)e^{-a/6}$ with an unevaluated
constant. Relative to the packing allowance $O(TL/a)$, the
source bound gains an exponential rate for $a=L^\eta$,
$0<\eta<1$, and counts even arbitrarily small negative values.
The $TL$ normalization is separate from the eligible-pair
population. The stated upper allowance grows even at $a=L$,
so it leaves room for one exception. Both E19 outputs concern
one time slice and assume their collar. [Note38 §§3,5][e19] · [Synthesis39 §3][s39]

## 5. Controls, synthesis and continuation

The documented collision screen in Decisions17–18 and Notes36–38
identifies the failed premise family by family. Positive
Euler-factor translates can share E16's smooth allowance
failure while changing the literal square source and canonical
endpoint count discrepancy. Weighted-square and finite-source,
score or prime controls lack the full reflected unit-weight
source, with the fixed-strip failure retained for the
documented endpoint-defective classes. The reflected
super-Gaussian retains reflection and fails the order premise.
Smooth shape and positive-primitive constructions change arithmetic.
Atomic sources fail absolute continuity for E16, and finite
profiles fail the stated growing count law in the strip.
RH-conditional mergers retain their hypothesis and change
ordinary Dirichlet arithmetic. Variable kernels and fractional
profiles fail the literal readout or integer divisor respectively.
The finite polynomial sign examples lack the canonical growing
population and can pass upper bounds or local geometry. None of
these documentary checks infers failure of an upper density or
moment estimate from a changed source alone. [Controls12][controls] ·
[Decision17 §5][b09] · [Decision18 §5][b10]

The stronger Note34 check is supported explicitly. Deletion
only lowers the local population. The added nonreal group at
positive real part has two marks of size
$2\sqrt3/\log c$, costing at most $24/(\log c)^2\le3/2$
in a positive dyadic band. If it enters the transverse tail
for $[U,2U]$, then $U\le c+2/\log c$ and
$v<2\sqrt3/\log c$. Thus $bv\log U\le5\sqrt3 b/2$,
and the two occurrences are absorbed by adding
$2e^{5\sqrt3 b/2}/(8\log8)$ to the density constant.
With $T=c,a=2,d=D=0,R=3$ the closed exterior cutoff admits
both designated doubles, including equality at the inserted
real exterior group. Their exact near values after multiplying
by $\ell^2$ are $1/2$ and $-1/16$. These fixed slices share
the upper moment and density bounds and can retain opposite
signs. The modified fields supply no common physical heat tube
or unchanged theta source. [Note34][control] · [Note37 §5][e17] ·
[Note38 §6][e19]

Synthesis39 keeps the established far-tail result and the finite
local certificate in their separate scopes. Predecessor audit16
does not pay the missing selected-pair signed input through its
covariance, Ward, marked-pair evolution or all-order transverse
moment comparisons. The direct evaluator gets the same source,
counts, moments, density, geometry, signed identities and any
independently paid anchor. No cost advantage is established. The
batch supplies neither a growing count-two collar nor selected-pair
reality, a time-event count, an incoming anchor, a signed cost
bound, a one-exception exclusion or a new Newman bound.
[Synthesis39 §§4–5][s39] · [Predecessor audit16][audit]

**Next declared task is [B] VCD-GT-B11 — Astra/ultra.** The
remaining conceptual decision is to identify an additional
source quantity with a fixed-microscopic-collar selected-pair
success test, or stronger visibility/conditioning sufficient
to resolve one exception. Synthesis39 leaves that mechanism
unselected and gives no new execution contract. No numerical
experiment, proof-source edit or shared-status edit was
required in this assessment.

[request]: ../research-progress/handoffs/VCD-GT-E18-r1.md
[addendum]: ../research-progress/handoffs/VCD-GT-E18-r1-input-addendum.md
[e16]: ../notes/36_VCD_GT_E16_COMPLETE_SOURCE_PHASE_ALLOWANCE_20261117.md
[e17]: ../notes/37_VCD_GT_E17_AVERAGED_TRANSVERSE_CORRECTION_20261117.md
[e19]: ../notes/38_VCD_GT_E19_ISOLATED_PAIR_EXCEPTION_COUNT_20261117.md
[r16]: ../research-progress/handoffs/VCD-GT-E16-r1-return.md
[r17]: ../research-progress/handoffs/VCD-GT-E17-r1-return.md
[r19]: ../research-progress/handoffs/VCD-GT-E19-r1-return.md
[q19]: ../research-progress/handoffs/VCD-GT-E19-r1.md
[b09]: ../brainstorm/notes/17_VCD_GT_B09_SOURCE_NEAR_FIELD_DECISION_20261117.md
[b10]: ../brainstorm/notes/18_VCD_GT_B10_ISOLATED_PAIR_VISIBILITY_DECISION_20261117.md
[s39]: ../notes/39_VCD_GT_B09_B10_SOURCE_ESTIMATE_SYNTHESIS_20261117.md
[oracle]: ../notes/12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md
[jet]: ../notes/24_VCD_GT_FOURIER_GROUPING_AND_DEFLATED_CURVATURE_20261116.md
[control]: ../notes/34_VCD_GT_E15_IDENTICAL_COUNTS_OPPOSITE_SIGNS_20261117.md
[source]: ../references/06_VCD_GT_TRANSVERSE_MOMENT_SOURCE_USE_20261117.md
[audit]: 16_VCD_GT_B09_PREDECESSOR_RATE_AUDIT_20261117.md
[density]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/21_TND_O_E11_BROAD_WINDOW_TRANSVERSE_DENSITY_20261107.md
[inherited]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/reviews/07_TND_O_E13_ASSEMBLED_LOCALIZATION_ASSESSMENT_20261107.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[class]: ../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[shared]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
