# Results assessment and research paths after height 112

> **Chat-history routing update, 17 October 2026.** Current histories: [Chat 14 — Review quaternion theta handoff](../chat-histories/0014_2026-10-15T02-29-33Z_review-quaternion-theta-handoff.json), [Chat 13 — Continue quaternion theta geometry](../chat-histories/0013_2026-10-15T00-47-29Z_continue-quaternion-theta-geometry.json). Use this investigation’s [local registry](../chat-histories/index.json) and [relocation receipt](../CHAT_HISTORY_RELOCATION_20261017.json) for current numbers and preserved provenance; this supersedes the routing and numbering below. All future investigation 21 chats belong in this investigation’s `chat-histories/` folder.

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model **gpt-6-astra**, reasoning effort **ultra**, verified from
this conversation's turn metadata. This is a synthesis and proposed research
program, with a conditional local calculation; it establishes no new theta
sign theorem or numerical certificate. Parallel internal LLM readings
checked the result boundaries and proposed directions.

The finite certificate now reaches height 112, and a prescribed delay has a
valid comparison theorem in part of the known outer region. The principal
unresolved task is a theta-specific signed inequality at the physical energy
scale in the unbounded small-time cusp. Further absolute approximation or
another exact representation will help only if it supplies that inequality.

The starting sources are [Handoff 26](26_CONTINUATION_AND_CHAT_HISTORY_HANDOFF_20261014.md),
[Note 25](25_PHASE_CONTROLLED_DELAY_AND_CUSP_EXTENSION_20261014.md),
[Review 19](../reviews/19_PHASE_CONTROLLED_DELAY_AND_CUSP_EXTENSION_REVIEW_20261014.md),
[Note 24](24_PROPORTIONAL_DELAY_PHASE_OBSTRUCTION_AND_CONTINUATION_20261014.md),
[Note 21](21_ONE_SIDED_STATIONARY_ESTIMATES_AND_THETA_PILOT_20261014.md), and
[Note 19](19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md).

## Established results and their scope

Write h_k=partial_x^k H, E=h_0^2+h_1^2, and
L_j=h_{j+1}^2-h_j h_{j+2}, j=0,1. Put
L=log(x/(4 pi)) and theta=tL for positive x>4 pi.

| Result | Established domain and conclusion | Remaining limitation |
| --- | --- | --- |
| Finite certificate | 0<=t<=1/2, abs(x)<=112: sqrt(E)>1e-17 and h_{j+1}=0 implies L_j>0 for both j | Stationary implications do not assert positivity of both forms at every nonstationary point |
| Earlier-time products | On the genuine positive-height branches in 104<=x<=112, the retained and absorption products are positive for every 0<=s<=t | No extension of that delayed-product statement to every older band or unchanged-drift reflection |
| Full outer signs | For each fixed epsilon>0, E>0 and both full forms are positive at sufficiently large abs(x) if theta>=3+epsilon | The height cutoff is unevaluated |
| Smooth-delay comparison | With delta=t/[2(1+t log(1+x^2))], both P_j,Q_j>0 at current stationarity for sufficiently large abs(x) and theta>=13/4 | This lies inside previously established sign coverage |
| Explicit outer theorem | theta>=5, abs(x)>=4 pi exp(10^9) | Gives neither a practical bridge from 112 nor coverage of the inner cusp |

The newest bands comprise 64 closed cells and 128 stationary observations.
The actual new branches are h_1=0 in 107<x<108 and h_2=0 in 109<x<110,
with exactly one regular stationary point at every time in each window.
The source records retain the failures of the stronger uniform residual-cone
enclosures; these are not negative physical signs.

Note 24 proves a useful negative result about the method: every fixed
proportional delay produces adverse retained products on genuine stationary
points at arbitrarily large height on a fixed positive-time slice. The
height-dependent rule in Note 25 repairs that outer comparison by controlling
both gamma and zeta phase. It does not lower the full-sign threshold three.

Review 19 records 21 exact symbolic checks, 1,321 exact finite audit checks,
and fresh 192-bit quadrature replays. Those checks were not rerun for this
assessment. They support the recorded calculation and its stated scope;
the internal reviews are not external peer review or formal verification.

## The precise missing estimate

Keep a=pi/16, b=1/4, mu=a^2+b^2, and

\[
 C_j=-h_{j+2}-2ah_{j+1}-\mu h_j,\quad
 \tau=t-\delta,\quad
 P_j=h_jC_j(\tau,x),\quad
 Q_j=h_j\{C_j(t,x)-C_j(\tau,x)/2\}.
\]

On the current stationary set h_{j+1}=0,

\[
 \mathcal L_j=\mu h_j^2+\tfrac12P_j+Q_j.
\]

A sufficient target is P_j>=0 and Q_j>=-K_j E, with prescribed losses
locally bounded through each possible positive-time collision. More
flexibly, one may prove P_j>=-A_j E and Q_j>=-B_j E, or directly

\[
 \tfrac12P_j+Q_j\ge-K_jE.
\]

The direct combination equals h_j C_j(t,x) identically. Thus delay can
organize an estimate, but it does not change the total expression being
bounded. Separate bounds can discard cancellation and impose a needlessly
strong requirement.

On h_1=0, E=h_0^2, whereas Q_0=h_0 times an earlier/current residual
bracket. An ordinary absolute bound for that bracket yields an error of
order abs(h_0), rather than h_0^2. A favorable sign or additional
cancellation is essential. The same difficulty appears for the derivative
branch relevant to higher-order collisions. Absolute source-tail payments
and finite energy floors do not supply this relative estimate.

Local boundedness permits K_j(t,x) to grow with height or as t tends to
zero. It requires boundedness in a neighborhood of each finite candidate
(T,x_*) with T>0. A growing sampled quotient along x tending to infinity
therefore refutes only a specified growth-rate or uniform-loss proposal,
not the entire locally bounded-loss program. The coefficient must be
prescribed or derived from the source, not fitted by division by E.

## A conditional collision test for proposed inequalities

Suppose, conditionally, that H(T,x_*)=H_x(T,x_*)=0 at T>0 and
c=H_xx(T,x_*) is nonzero. The implicit-function theorem gives the local
current stationary branch x=xi(t). From H_t=-H_xx and H_x=0 on this
branch, with epsilon=T-t>0,

\[
 h_0(t,\xi(t))=c\varepsilon+O(\varepsilon^2),\quad
 h_2(t,\xi(t))=c+O(\varepsilon),
\]
\[
 E=c^2\varepsilon^2+O(\varepsilon^3),\quad
 \mathcal L_0=-c^2\varepsilon+O(\varepsilon^2),\quad
 \frac{\mathcal L_0}{E}=-\varepsilon^{-1}+O(1).
\]

For the smooth prescribed delay, put g=C_0(tau(T,x_*),x_*). Smoothness
of this earlier-time field gives

\[
 P_0=cg\varepsilon+O(\varepsilon^2),\qquad
 Q_0=-c(c+g/2)\varepsilon+O(\varepsilon^2).
\]

The linear terms in P_0/2+Q_0 sum to -c^2 epsilon independently of g.
This is a conditional test, not evidence of an actual theta collision.
It explains why adjusting the delay alone cannot defeat the generic
collision geometry. A successful theta-specific estimate must exclude
that geometry. The cubic control in Note 21 likewise explains the need
to retain the second stationary set; the calculation above does not
analyze every higher multiplicity.

## Priority one is a signed estimate on an unbounded inner subdomain

Prescribe a domain before testing, for example

\[
 x\ge X_0>112,\quad 0<t\le1/2,\quad
 \theta_0\le t\log(x/(4\pi))\le3+\eta,
\]

with fixed theta_0>0 and eta>0. The region still has t tending to zero
as x grows. Success leaves both 0<theta<theta_0 and the finite transition
112<x<X_0 explicit.

An especially useful first strip lies just below three while theta>2
has a fixed positive margin. The nominal current zeta-carrier argument
has real part 1/2+theta/4, so its elementary nonvanishing argument remains
available there, although the weighted-sum approximation needed for the
existing theorem has not been proved in that strip. If an earlier zeta
carrier is used, its own condition tau L>2 with a fixed margin must also
be verified. Alternatively estimate the combined source kernel without
requiring a separate earlier carrier.

Use the existing common-carrier staircase domain and dyadic arithmetic
blocks, retaining both source coordinates and every index pair. For the
absorption field, combine current and earlier coefficients using

\[
 (y^2-b^2)\{1-\tfrac12e^{-\delta(y+ia)^2}\}
\]

before taking absolute values. Seek a lower bound for the actual theta
block-pair sum, possibly by retaining a prescribed set of interacting
pairs and controlling the rest one-sidedly by physical E. A bound by the
sum of absolute block energies is insufficient unless a valid comparison
to physical E is proved near candidate collisions.

Current stationarity applies to the full sum. It cannot be imposed on
individual blocks. A universally positive matrix for arbitrary block
amplitudes is too strong: Note 21 proves that the arbitrary-jet stationary
forms are indefinite for every finite K. The proof must exploit the
specific theta coefficients and their relations.

Both Hermitian and bilinear terms, the conjugated second multiplier,
all omitted-pair sectors and staircase entry terms remain mandatory.
The entry phases cancel in physical x, so those contributions cannot
be bounded using invented oscillation in x. If transport is used, the
moving-delay derivatives and singular-branch obligations also remain.

## Priority two is a diagnostic pilot in the shrinking-time scaling

Design a small pilot to identify which block pairs create the sign. For
selected fixed values of theta, locate genuine stationary roots satisfying
t=theta/log(x/(4 pi)) at increasing heights. These are roots of the
physical partial derivative h_{j+1}; they are not stationary points of
the composite function H(theta/L(x),x). For a fixed theta, root certification
of the composite derivative observation uses

\[
 \frac{d}{dx}h_{j+1}(\theta/L(x),x)
 =h_{j+2}+\frac{\theta}{xL(x)^2}h_{j+3},
\]

with all jets evaluated at (theta/L(x),x). Using only h_{j+2} would
incorrectly freeze time. Retain the full source error budget.

A lower-cost assembly can integrate complex moment arrays once per
retained block. With

\[
 U_{r,j}=\int_{\Omega_r}Wq^j\,d\nu,\qquad
 V_{r,j}=\int_{\Omega_r}Wq^jk^Q\,d\nu,
\]

the retained absorption product is exactly

\[
 Q_j^A=\frac{e^{-2ax}}4\Re\sum_{r,s}
 \left[V_{r,j}\overline{U_{s,j}}+U_{r,j}\overline{V_{s,j}}
       +V_{r,j}U_{s,j}+U_{r,j}V_{s,j}\right].
\]

This is product-integral assembly with independent source variables;
it does not identify coordinates or keep only diagonal blocks. Assemble
all pairs algebraically instead of separately integrating a double
integral. Add the full retained/omitted, omitted/retained and
omitted/omitted payments and all parameter and quadrature errors.

Record the full combined sign, the retained-product sign, the signed
contribution of a predeclared pair subset, the remaining cross terms,
and the error budget. Test a predeclared loss directly through Q_j+K_j E
or the combined inequality. Exploratory quotients may be displayed as
diagnostics but cannot define the certified loss.

A certified violation at a genuine theta stationary point refutes the
specified inequality. A negative free-amplitude eigenvector only refutes
that relaxation. An undecided interval enclosure is neither kind of
counterexample. Favorable finite samples guide a lemma; they do not
prove the unbounded-domain assertion.

## Supporting work and priorities to defer

Use the coefficient combination that resolved the eight finite absorption
cases as a guide to correlation-preserving estimates. Its shared variable
is the physical observation displacement; independent integration
coordinates stay independent. The finite all-earlier-time success is a
useful diagnostic, but requiring every earlier time in the unbounded
region is stronger than needed. Start with one prescribed comparison.

Keep finite bridging as a separate computational task. Extending beyond
112 is useful when it tests an identified mechanism or reaches an evaluated
analytic cutoff. Repeated bounded extensions alone do not address the
unbounded cusp. A better explicit outer cutoff would assist this bridge,
while leaving the deeper small-time problem in place.

Improved arithmetic-block bounds that lower the full-sign threshold three
would add real coverage. They are a reasonable secondary analytic project,
but they should be judged by an actual new domain. Improving the smooth
delay only within already favorable outer signs has lower priority.

Near theta=0 the shifted zeta argument approaches the critical line.
Continuing the outer phase argument by assuming a nonvanishing zeta factor
or a controlled zeta'/zeta there would assume the needed arithmetic input.
The direct paired products avoid introducing that denominator.

The recommended next deliverable is a predeclared block-pair inequality
on one unbounded inner strip, supported by a small stationary-root pilot
that can distinguish a false target from a weak enclosure. New kernel
identities, another hypercomplex lift, or blanket positivity for arbitrary
sources would not satisfy that deliverable.

## Repository and archive status

This assessment uses the stable repository manuscript and research notes;
Notes 24 and 25 remain outside the manuscript integration identified by
Handoff 26. The current checkout HEAD is
`d48a69cc0f1761f52ff190e256cccc6ba9e403d7`, read on this turn; the older
HEAD named by the handoff describes its own historical state. No manuscript,
commit, tag or snapshot folder is created here. This note stays below
1 MiB and does not constitute a new proved milestone.

The actual new chat is `01a13d64-ba41-7362-acfe-bf5978c84d11`, titled
**Review quaternion theta handoff**, registered as number **11** in the
explicitly required formal replay lane. It has a distinct identity from
the preceding handoff chat number 10. The authorized recorder preserves
that earlier registration and this chat's own identity; the bounded exact-turn
follow-up captures the real final reply after completion.
