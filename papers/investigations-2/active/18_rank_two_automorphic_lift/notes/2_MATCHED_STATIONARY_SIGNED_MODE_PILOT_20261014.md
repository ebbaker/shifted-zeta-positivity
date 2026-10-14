# Matched stationary signed-mode pilot: complete tails, failed cost gate

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: `gpt-6-astra` (Codex), reasoning effort **ultra**.
Internal analytic derivation and Arb/ACB computation; not independent external
validation. Original direction-18 identities and their Claude provenance
remain in [note 1](1_CUSP_FORMULA_HECKE_AND_CONTROLS_20261013.md).

## Outcome and scope

The selected grouped-mode implementation does **not** pass A4. Its complete
omitted-mode and domain tails fit below the requested error target, but its
validated finite double integral exhausts the common one-million-primitive
budget on each cell. The remaining certified intervals contain both signs.
The [direct-source baseline](../../../brainstorm/numerics/MATCHED_STATIONARY_BASELINE_RECORD_20261014.json)
certifies the two stationary signs for far less work. This pilot supplies
neither a new stationary sign mechanism nor a demonstrated cost saving.
Pause this continuation unless a materially different complete inequality
or a justified reduction of the finite integration cost is proposed.

This is a failure of the specified implementation and budget, not a theorem
that every automorphic representation must be inefficient. No first-mode
positivity assertion is needed or established. The test is at one exact
time and two stationary cells, not a positive-time interval or all heights.

The shared specification is:

| Obligation | Time | Initial real cell | Certified stationary constraint |
| --- | --- | --- | --- |
| j=0 | 1/20 | [204.087, 204.089] | H_x=0 |
| j=1 | 1/20 | [205.556, 205.558] | H_xx=0 |

The baseline certifies one unique stationary root in each initial cell and
provides narrow rational brackets. The mode integration takes the entire
corresponding bracket as a real ball; it does not substitute its midpoint
for the stationary point. Both cells use at most 256 bits, one million
primitive evaluations and 60 seconds per cell. The requested numerical
width of a complete Laguerre enclosure is at most 10^-72. A primitive here
means one divisor phase/heat evaluation or one mode polynomial/exponential
evaluation; it is a declared reproducible cost proxy, not a processor
instruction. Runtime also matters when comparing different formulas.

## 1. Direct insertion before the contour shift

Use the normalization of note 1,

\[
\varphi_a(u)=e^u(2Y_a(u)^2-3Y_a(u))e^{-Y_a(u)},\qquad
Y_a(u)=\pi a^2e^{4u},\qquad \Phi=\sum_{a\ge1}\varphi_a.
\]

Its pair identity, evenness of the full source, and the fold in r give

\[
\mathscr L_j(H_t;x)=2\int_0^\infty\!\int_{\mathbb R}
 r^2(r^2-s^2)^j e^{2t(r^2+s^2)}
 \sum_{a,b\ge1}\varphi_a(r+s)\varphi_b(r-s)e^{2ixs}\,ds\,dr,
 \quad j=0,1.
\tag{1}
\]

For one pair let n=ab, ell=log(a/b), Z=pi*n*exp(4r), and change variables
z=4s+ell. Then Y_a=Z exp(z), Y_b=Z exp(-z), and their insertion polynomial is

\[
P(Z,z)=(2Y_a^2-3Y_a)(2Y_b^2-3Y_b)
      =4Z^4-12Z^3\cosh z+9Z^2.
\tag{2}
\]

For 0<theta<pi/2 move z to v+i*theta and put w=v-ell+i*theta. The exact
folded-mode identity becomes

\[
\boxed{\displaystyle
\mathscr L_j(H_t;x)=\frac12\int_0^\infty r^2e^{2r+2tr^2}
 \sum_{n\ge1}\sum_{ab=n}\int_{\mathbb R}
 P(Z,v+i\theta)e^{-2Z\cosh(v+i\theta)}
 e^{tw^2/8+ixw/2}\left(r^2-\frac{w^2}{16}\right)^j\,dv\,dr .}
\tag{3}
\]

The factor 1/2 is the fold factor 2 times ds=dv/4. In particular, j=1
retains its full complex insertion r^2-w^2/16. This is the inserted source
version of the same rank-two modes as note 1, not a new positivity identity.
It avoids the Gaussian spectral average and fourth derivatives by expanding
the physical insertion first. The finite implementation sums all divisor
terms and all retained modes with their signs before evaluating the outer
integral.

For each fixed pair the integrand is entire and the vertical end pieces
vanish uniformly for 0<=Im(z)<=theta, because cos(Im(z))>=cos(theta)>0
gives superexponential decay in |Re(z)|. The
absolute majorants below are summable in n and integrable in r and v; they
also justify the expansion and interchange after the shift. The fold
r>=0 is essential to these particular uniform estimates.

## 2. Complete analytic payments

The fixed choices are

\[
T=t=1/20,\quad\theta=13/10,\quad N=32,\quad R=3/2,\quad V=6,
\quad b=2\pi\cos\theta>0.
\]

Use X for the lower endpoint of the initial x cell, and put

\[
A_n=4\pi^4n^4+12\pi^3n^3+9\pi^2n^2.
\]

For r>=0 and real v, |ell|<=log n gives

\[
\begin{aligned}
|P(Z,v+i\theta)|&\le A_ne^{16r}\cosh v,\\
|e^{tw^2/8+ixw/2}|&\le
 e^{-X\theta/2}e^{Tv^2/4+T(\log n)^2/4},\\
\left|r^2-w^2/16\right|&\le
 r^2+v^2/8+(\log n)^2/8+\theta^2/16.
\end{aligned}
\tag{4}
\]

The second inequality discards the favorable -t*theta^2/8 and uses
(v-ell)^2<=2v^2+2ell^2. The same upper bounds are valid for 0<=t<=T,
although the finite computation and stationary targets here use only t=T.
Next,

\[
e^{4r}\cosh v\ge1+8r^2+v^2/2.
\tag{5}
\]

Define a_r=8bn-2T and a_v=bn/2-T/4. Both are positive at n=1. Complete
the remaining linear envelopes as

\[
18r\le a_rr^2/2+162/a_r,\qquad
\cosh v\le e^{|v|}\le e^{a_vv^2/2+1/(2a_v)}.
\tag{6}
\]

Let

\[
R_k(q)=\int_0^\infty r^k e^{-qr^2}\,dr,\qquad
V_k(q)=\int_{\mathbb R} v^k e^{-qv^2}\,dv
\]

for k=0,2,4 as needed. These are the usual elementary Gaussian moments;
all evaluations in the checker are outward Arb balls. With the arguments
a_r/2 and a_v/2 suppressed, set

\[
M_0(n)=R_2V_0,\qquad
M_1(n)=R_4V_0+R_2V_2/8+
 R_2V_0\bigl((\log n)^2/8+\theta^2/16\bigr),
\quad c(n)=e^{162/a_r+1/(2a_v)}.
\tag{7}
\]

Equations (4)-(7) bound the complete nth grouped mode in absolute value by

\[
B_{n,j}=\frac12e^{-X\theta/2}d(n)A_n
 e^{-bn+T(\log n)^2/4}c(n)M_j(n).
\tag{8}
\]

This is a full folded integral bound. It does not assume stationarity,
positive modes or any cancellation between omitted terms.

### Omitted modes n>N

Write n0=N+1>=3 and A0=4pi^4+12pi^3+9pi^2. Use d(n)<=n and
A_n<=A0*n^4. The Gaussian factors and c(n) decrease. Since log(n)/n
decreases for n>=n0>=e,

\[
M_0(n)\le M_0(n0),\qquad
M_1(n)\le(n/n0)^2M_1(n0).
\]

The derivative of T(log n)^2/4 is T log(n)/(2n), also decreasing here.
Thus consecutive terms of this envelope have ratio at most

\[
q_j=(1+1/n0)^{5+2j}\exp\{-b+T\log(n0)/(2n0)\}<1.
\]

The checker verifies q_j<1 as an Arb inequality. The complete omitted-mode
payment is

\[
E_{n,j}=\frac{e^{-X\theta/2}}2\,
 \frac{A0\,n0^5e^{-bn0+T(\log n0)^2/4}c(n0)M_j(n0)}{1-q_j}.
\tag{9}
\]

The replay rejects N<2, outside this decreasing-log proof domain.

### Radial and contour ends of retained modes

On r>=R, split the exponential using

\[
e^{4r}\cosh v\ge\tfrac12e^{4R}
 +\tfrac12(1+8r^2+v^2/2).
\tag{10}
\]

Use a_r=4bn-2T and a_v=bn/4-T/4 in (6)-(7), and replace -bn in (8)
by -bn(e^(4R)+1)/2. Integrating this majorant over the whole r>=0,
v in R domain only enlarges the tail. Sum the resulting bounds for
n<=N with the exact divisor counts.

For |v|>=V the same construction follows from

\[
e^{4r}\cosh v\ge\tfrac12\cosh V
 +\tfrac12(1+8r^2+v^2/2),
\tag{11}
\]

and replaces -bn by -bn(cosh V+1)/2. The union bound may count a corner
twice, safely. Together, (9)-(11) cover every omitted term and domain end.
There is no unrecorded exponential cutoff inside the retained rectangle.
Finally, sum (8) through N and add (9) for a complete absolute fallback
bound A_j on |L_j|, valid uniformly on the initial cell.

## 3. Execution and comparison

The [checker](../numerics/check_rank_two_matched_pilot_20261014.py) uses
python-flint 0.9.0 at 256 bits. The finite region is r in [0,1.5] and
v in [-6,6]. Nested ACB quadrature retains complex parameter balls;
all finite integrands are entire. Divisor sums are cached only when their
full exact ball representations agree. A shared budget stop flag returns
a nonfinite ball rather than a partial integral whenever either cap is
reached. Consequently a stopped or nonfinite run cannot certify a sign.
The [small execution record](../numerics/RANK_TWO_MATCHED_PILOT_RECORD_20261014.json)
contains the bounds, target brackets, operation counts and provenance.

Rounded **upward** summaries of the paid tails and complete fallback are:

| Quantity | j=0 cell | j=1 cell |
| --- | --- | --- |
| All modes n>32 | <4.629e-76 | <2.982e-76 |
| Retained modes, r>1.5 | <1.069e-192 | <3.558e-193 |
| Retained modes, abs(v)>6 | <4.444e-119 | <1.480e-119 |
| Complete absolute fallback A_j | <4.696e-52 | <8.695e-53 |
| Mode kernel evaluations | 214,124 | 214,124 |
| Divisor phase/heat evaluations | 785,876 | 785,876 |
| Total counted primitives | 1,000,000 | 1,000,000 |
| Elapsed seconds, this run | 3.243 | 4.041 |
| Finite retained integral | Not completed | Not completed |
| Certified positive sign from this method | No | No |

The tails fit the 10^-72 numerical-width target. The current cost failure
is in validating the finite signed integral, not in paying those tails.
A full fallback interval [-A_j,A_j] is nevertheless established. Its radius
is roughly 4.1e12 or 4.2e12 times the actual stationary value respectively,
so this absolute estimate supplies no useful local sign.

The matched direct-source baseline gives

\[
\mathscr L_0=[1.15071737608519\cdot10^{-64}\ \mathord{+/-}\ 4.61\cdot10^{-79}],
\qquad
\mathscr L_1=[2.08000102453508\cdot10^{-65}\ \mathord{+/-}\ 5.21\cdot10^{-80}],
\]

at the certified roots. It uses 24,000 ACB callbacks, each evaluating eight
source terms: 192,000 source-term primitives **for both cells together**,
and less than one second in that run. Its root existence, uniqueness and
stationary conditional products are certified independently of the lift
pilot. The methods count different elementary blocks, so the counts alone
are not a machine-independent complexity theorem; the observed runtime and
completed certificate strengthen the practical comparison.

The lift evaluator encloses the full L_j on the narrow root bracket. It
retains the target's stationarity through that certified bracket, but it
has no additional multiplier or algebraic projection enforcing H_(j+1)=0
inside the double integral. In particular, no improvement is attributed
to a stationary-conditioned signed-remainder inequality that has not
actually been proved.

## 4. Replay, provenance and stop decision

From the investigation's numerics directory, with python-flint 0.9.0
installed in the selected Python environment:

```sh
python3 -B check_rank_two_matched_pilot_20261014.py \
  --record /tmp/rank-two-matched-replay.json
```

The normal input is the retained baseline under
`investigations-2/brainstorm/numerics/`. If absent, the checker tries the
same relative `brainstorm/numerics/` path under `MATCHED_STATIONARY_ARCHIVES`.
An explicit `--baseline PATH` is also supported. Every input path must match
SHA-256 `e98a91f7c3abe8e8e9302ca3cf4c372329ec84d8668a5777eaf68bf86e0a0e47`;
a missing or mismatched baseline fails closed. That hash binds the selected
brackets and comparator, not the truth of their proof. Rebuilding the
baseline may change runtime metadata and therefore its file hash; a new
matched record requires explicit review and rebinding, not silent acceptance.

`--tail-only` recomputes the analytic bounds without the finite integral.
`--cell j0` or `--cell j1` selects one obligation. The original caps cannot
be increased through this matched-pilot command. Other allowed cutoffs
must still pass the proved ratio and positivity checks.

An initial invalid attempt raised a Python budget exception inside nested
ACB callbacks and produced a Cython callback error. No numerical certificate
from it is retained or used. The repaired run uses the shared stop flag and
completed normally with the recorded analytic fallbacks. Final input hardening added the baseline hash pin, default lookup, parameter
guards and explicit checks that remain active under Python optimization.
The final delivered checker was rerun under the same caps, and the retained
record binds that exact source hash. Its diagnostic history records the
previous callback failure and successful pre-hardening bounded attempt;
no result from the invalid attempt is treated as evidence.

This bounded A4 continuation ends at its stop gate. Reopening requires a
specific new complete estimate or implementation change with a reason to
beat this comparator. Increasing precision, dropping a tail, assuming
first-mode positivity, or moving to easier cells would not discharge the
matched task recorded here.
