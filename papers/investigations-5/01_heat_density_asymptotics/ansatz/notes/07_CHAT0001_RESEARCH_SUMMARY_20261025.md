# Ansatz chat0001: results, dependencies and remaining work

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**.
This summarizes all four bounded research continuations in thread
`01a175aa-a487-79a1-85a8-6f465fdb36bf`, titled **Continue heat density
research**. It is a source-based summary, not another mathematical proof
or an independent review. The unique public [chat history][history]
preserves the actual conversation; the [sole progress ledger][ledger]
owns live status.

## 1. What this conversation established

Throughout, the field is the complete canonical theta heat field,
`H_t=-H_zz`, `H(0,z)=xi((1+iz)/2)/8`. Its physical regulator
`q=epsilon_g^2`, averaging kernel, unnormalized observable definitions
and actual signed covariance are unchanged. With `X` a frozen real
chart center, use

    L_X=log(X/(4pi)), Lambda_X=1+L_X,
    N=floor sqrt(X/(4pi)), E_o=|C_+|+|C_-|>0.

The positive envelope E_o is never replaced by a vanishing cosine or
the true field. Physical buffers include averaging and collar margins,
with an extra analytic unit. Every differentiation is on frozen-cutoff
holomorphic charts. The right tail reflects to the left tail.

| Completed packet | Domain and result | Evidence |
| --- | --- | --- |
| HDA-A01-AN01 | On 32<=t<=33, the first corrected outer carrier approximates the true H, including full buffered spatial jets j<=3 and direct first time error. A retained-RS corrected finite sum supplies a signed **real-axis field** bridge on abs(t)L_X<=8. | [Note03][n03], [Assessment02][r02]. |
| HDA-A01-AN02 | Fixed-cutoff complex RS remainder with exact X^-3/4 power, followed by full buffered field/jets/time on abs(t)L_X<=8. This closes the complex gap left by AN01. | [Note04][n04], [Assessment03][r03]. |
| HDA-A02-AN01 | On t=-T, 1<=T<=2, a short corrected formula at natural gamma scale, and a **distinct** finite growing-order representation at outer-carrier precision. | [Note05][n05], [Assessment04][r04]. |
| HDA-A02-AN02 | The same finite representation extends to 4/L_X<=T<=2. A time-only join to Note04 pays all field/jets/time and actual residual errors on the complete negative interval -2<=t<=0. | [Note06][n06], [Assessment05][r05]. |

All are **proved in-note from named classical inputs; same-model internal
assessment only**. These statuses do not supply independent specialist
validation. No numerical, symbolic, exact-arithmetic, sampling or interval
research was executed in this chat. Hashes, history capture, compilation
and rendered-page inspection are housekeeping and production checks.

## 2. Quantitative progress and why each step mattered

### Corrected compact-positive carrier

Note03 pins the full-cosine coefficient `pi^(1/4)/16`, one-arm factor
half that value, unwrapped phase constant `7pi/8`, and zeta height X/2.
It derives the `i/(24z)` gamma coefficient and includes determinant
and displaced-mean curvature contributions. The corrected field F1 has

    |partial_z^j(H-F1)| <= C_j E_o (1+log^(4+j)X)/X^2, j<=3,
    |partial_t(H-F1)| <= C E_o (1+log^6 X)/X^2,

on 32<=t<=33. The full arithmetic remainder, bounded middle and both
infinite tails lie below the stated allowance. This is a correction to
the true H, not just an expansion of an auxiliary gamma function.
The compact interval is essential to that ordering.

### Complex arithmetic crossover through zero

Note03's real-axis bridge retained an RS correction; its complex gap
was recorded explicitly. Note04 pays it by a rectangle argument: on
the top edge, grouping H/M_dom with its dominant finite sum as an
ordinary Dirichlet tail preserves X^-3/4. The bottom edge, both
vertical edges, analytic weight and frozen-cutoff crossings are paid.

For its short model F_cross, Note04 proves

    |partial_z^j(H-F_cross)| <= C_j E_o delta Lambda_X^j, j<=3,
    |partial_t(H-F_cross)| <= C E_o delta Lambda_X^2,
    |(partial_t+partial_zz)F_cross| <= C E_o delta Lambda_X,
    delta=X^-3/4 exp(t_- L_X^2/16), abs(t)L_X<=8.

Thus delta<=C X^-1/4 throughout the signed shrinking window, and
delta=X^-3/4 at nonnegative time, including zero. Exact Gaussian
identities handle both heat signs. Full mode populations and true and
artificial tails are retained. Time follows from a proved spatial error
and the actual model residual, without differentiating an allowance.

### Fixed negative times: two representations and two scales

Note05 first establishes the existing short model on 1<=T<=2 with
field, j<=3 and first time errors `O(|G|X^-3/4)`, where
`G=[M(s)M(1-s)]^(1/2)` is positive on the real axis. This is useful
relative to the natural positive correction envelope `|G|X^-1/4`.
It is not a lower bound on H or the retained correction.

At the outer scale that bound permits
`X^-3/4 exp(TL_X^2/16)`, which grows at fixed T. Note05 preserves
this failed allowance and constructs a different finite representation.
With frozen `K=ceil L_X`, `J=ceil(3L_X)`, `V=8L_X`, `R=X^(1/3)`,
it retains all arithmetic modes, K+1 classical RS terms, exact adjacent
cutoff transfer and one bounded correction integral. An n-independent
analytic gamma factor supplies the common degree-J curvature polynomial.
The actual Gamma(K/2) growth, full mode count and all tails are paid.
The model Fhat_X has

    |partial_z^j(H-Fhat_X)| <= C_j E_o exp(-L_X^2/4), j<=3,
    |partial_t(H-Fhat_X)| <= C E_o exp(-L_X^2/4),
    (partial_t+partial_zz)Fhat_X=0,

on 1<=T<=2. It is a finite representation with a correction integral,
not a short low-parameter elementary asymptotic or an evaluated cost theorem.

### The new bridge and complete negative interval

Note06 extends this **unchanged** model to 4/L_X<=T<=2. Complex
real-initial-value smoothing costs `exp(b^2/(4T))`, and j derivatives
cost `T^(-j/2)(1+B/sqrt T)^j`. Gaussian rescaling pays the original
T^-1/2 normalization. On the bridge these factors are at most
`exp(b^2 L_X/16) C Lambda_X^j`, so they do not consume the quadratic
log-height slack in the growing-order RS and curvature errors.
The same outer error `exp(-L_X^2/4)` and exact heat residual survive.

With a fixed smooth chi(TL_X), zero below4 and one above8, Note06
joins F_cross to Fhat_X on their paid overlap. The direct time error
retains the derivative-of-chi term. The actual residual is

    R_join=(1-chi)R_cross - L_X chi'(TL_X)(Fhat_X-F_cross).

It need not vanish near T=0 because the crossover residual remains.
It vanishes for TL_X>=8. Uniformly for -2<=t<=0, the joined model has

    |partial_z^j(H-F_join)| <= C_j E_o X^-1/4 Lambda_X^j, j<=3,
    |partial_t(H-F_join)| <= C E_o X^-1/4 Lambda_X^2,
    |R_join| <= C E_o X^-1/4 Lambda_X.

These relative errors all tend to zero. The weighted estimates in
Note06 NB20--23 are sharper near both ends of the crossover.

## 3. Failed routes and limitations retained

- Note03's naive absolute complex Gaussian route loses
  `exp(y^2/(4T))` as T tends to zero. Note04 bypasses it using a paid
  complex initial strip; Note06 uses it only on T>=4/L_X with its
  height cost explicitly retained.
- Fixed-order shrinking-time errors cannot simply be substituted at
  fixed negative T. The failure is of the allowance, not an actual
  error lower bound or a negative-time impossibility theorem.
- Raising only the initial RS order leaves arithmetic heat curvature
  unpaid. Note05 pays both orders separately.
- A small or zero heat residual alone does not propagate a field error.
  Each time estimate here consumes an independently proved spatial
  comparison. A time-dependent join has its own residual.
- A globally floor-valued formula is not differentiated. This chat pays
  fixed charts and a time-only join, not physical spatial assembly.

The [result index][results] and [avoid index][avoid] remain the short
repository-wide entry points, especially controls12 and patterns05,
07,08,12,16,19. The source-specific canonical arithmetic/completion
premises fail for the named collision controls; positivity, Gaussian
shape and symmetry alone supply none of these approximations.

## 4. Status and next deliverable

HDA-A01 is **Complete at its bounded AN01--AN02 analytical scope**.
Both HDA-A02 packets are **CLOSED at their bounded analytical scopes**,
and the branch now has a proved chartwise negative interval [-2,0].
HDA-A02 remains **Partial** as a broader compact-negative-time and
short-formula program. The positive fixed-time gaps, arbitrary compact
negative endpoints, growing-time limits, regulator-layer refinement,
physical observable transfer, full assembly, useful runtime and
independent specialist review remain open. No new RH, simplicity,
collision-exclusion or Newman-bound claim was made. Parent HDA-17
Partial, HDA-18 Gated and HDA-20 unfulfilled are unchanged.

The maintained manuscript incorporates these results in place; no
snapshots or commits were created. Generated reading PDFs live in the
ignored root output/pdf tree, with small build records in ansatz.
Notes03--06 and their input manifests/assessments retain the detailed
history. This chat keeps its unique original chat0001 registration.

Next **Analysis — Sol**, [HDA-A03-AN01 r1][next], is prepared, not
dispatched: corrected one-arm comparison in a bounded neighborhood of
the physical regulator switch, then an explicit comparison of named
centers at the inherited rounding scale. Static centering is separated
from any sharper density, time/current or covariance consumer. No
specific resistant estimate here requires an Astra assignment.

[history]: ../chat-histories/README.md
[ledger]: ../research-progress/01_HIGH_HEIGHT_ANSATZ_RESEARCH_PROGRESS_20261025.md
[n03]: 03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md
[n04]: 04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[n05]: 05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md
[n06]: 06_NEGATIVE_BRIDGE_AND_TIME_JOIN_20261025.md
[r02]: ../reviews/02_CALIBRATION_AND_REAL_BRIDGE_ASSESSMENT_20261025.md
[r03]: ../reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md
[r04]: ../reviews/04_FIXED_NEGATIVE_TIME_ASSESSMENT_20261025.md
[r05]: ../reviews/05_NEGATIVE_BRIDGE_AND_TIME_JOIN_ASSESSMENT_20261025.md
[next]: ../research-progress/handoffs/HDA-A03-AN01.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
