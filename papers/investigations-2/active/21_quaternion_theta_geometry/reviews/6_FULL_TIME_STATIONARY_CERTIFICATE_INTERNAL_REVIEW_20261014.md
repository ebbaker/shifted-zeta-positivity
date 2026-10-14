# Internal review of the full-time bounded stationary certificate

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.
The parent session verified its actual current-turn configuration in the
recorded rollout; this reviewing subtask inherited that configuration.

This independent internal LLM review covers the
[full-time driver](../numerics/certify_compensated_stationary_time_extension.py),
its [execution record](../numerics/COMPENSATED_STATIONARY_TIME_EXTENSION_20261014.json),
the imported source reviewed in
[Review 5](5_COMPENSATED_STATIONARY_SIGN_INTERNAL_REVIEW_20261014.md),
and the central-moment and compensated-observation additions to the
[manuscript](../manuscript/quaternion_theta_geometry.tex).
It is not specialist refereeing or formal verification. The bounded
full-time claim passes; no unresolved mathematical or implementation
concern was identified within its declared domain.

## Time and source payments

The parameterized source explicitly sets the center, radius, and maximum
time of each slab before computing any moments or retained jets. All
three parameters propagate into the inherited source integration,
concavity tail, raw heat transport, and affine endpoint compensation.
The source moment majorant uses that slab's right endpoint. The
complete-index Q-polynomial bound already holds throughout 0<=t<=1,
so its unchanged use on 0<=t<=1/2 is justified. This was checked in
the source; it was not inferred from a changed domain label.

The inherited retained-source quadrature includes its returned ball
radius and the whole integration tail beyond u=1. Positive source
moments pay both the time and spatial Taylor remainders. The complete
Gaussian transforms and Gaussian moment remainders pay the separate
compensation integrals. Raw channels are transported by heat before
the explicit affine compensation is subtracted. No finite compensated
channel is treated as a homogeneous heat solution.

The decisions use the exact aggregate identity D+X=L(P), with all
retained diagonal and off-diagonal terms recorded where needed. At
genuine stationarity the square remainder is negative, and the full
payment in the imported source has the correct sign and indices.
The new manuscript's two-jet residual, rational index payments, central
fourth/sixth moment gap, and correlated stationary observation agree
with the derivations in Note 8 and the implementation.

## Exact cover and independent replay

The final calculation uses Python 3.10.0, python-flint 0.9.0, and
256-bit Arb/Acb arithmetic. It has K=2, N=3, cutoff u=1, spatial
Taylor order 12, time Taylor order 5, and Gaussian Taylor order 24.
The exact cover is the product of eight closed time slabs
[i/16,(i+1)/16], i=0,...,7, and 34 closed unit spatial cells
[k,k+1], k=7,...,40. All 272 cells remain at their initial subdivision
depths. Their shared boundaries, t=0, t=1/2, x=7, and x=41 are included.

The reviewer independently replayed the final driver outside the
repository. Its JSON equals the repository record after removing only
runtime.seconds. Both recorded source hashes match the inspected
driver and imported source. All 25 exact algebra and control checks
pass. A separate standard-library Fraction audit verified the exact
two-dimensional cover, all 544 observation classifications, every
signed surplus against its rational target, the shared payment
references, all 24 branch windows, and the independently recomputed
norm lower bound. The audit also recomputed the signed lower bounds
from the stored aggregate intervals and conservative index payments,
rather than merely trusting the stored positive surplus flags.

| Level | Stationarity excluded | Individually unique branch cells | Other signed cells |
|---|---:|---:|---:|
| j=0 | 263 | 7 | 2 |
| j=1 | 255 | 15 | 2 |

The four additional signed cells are not automatically interpreted as
individually isolated branches. Joining adjacent signed cells gives
one first-stationary branch and two second-stationary branches on each
time slab. Each resulting window has a uniformly strict next-derivative
sign and opposite strict outer endpoint signs. These facts prove one
and only one regular branch per window. All 24 windows pass; no sign
cell or branch window remains unresolved. Moving roots crossing unit
cell boundaries are therefore covered without an unsupported isolated
branch assertion for those individual cells.

## Certified conclusions and scope

The smallest recorded strict stationary surpluses are approximately
5.44724*10^(-10) and 1.44099*10^(-11). Their exact outward dyadic
lower endpoints exceed 1/2000000000 and 1/100000000000,
respectively. Thus throughout the full closed rectangle
0<=t<=1/2, 7<=x<=41,

\[
h_1=0\Longrightarrow\mathscr L_0(H)>5\,10^{-10},\qquad
h_2=0\Longrightarrow\mathscr L_1(H)>10^{-11}.
\]

Independently of stationarity, the genuine H and H_x interval distances
from zero give the uniform norm lower bound

\[
|F|\ge
\frac{321849425817089107558489508215301}
{170141183460469231731687303715884105728}
>\frac{189}{100000000}>\frac9{5000000}.
\]

The minimum cellwise squared bound is attained by the recorded cell
[7/16,1/2]x[40,41]. The displayed rational bound is a directed square
root below that exact minimum; its square and its comparison with
189/100000000 and 9/5000000 were checked using exact fractions. It is obtained directly
from paid genuine jets, without a norm division. Combining it with
the analytic central gap and evenness gives |F|>9/5000000 on
0<=t<=1/2, |x|<=41. The central signed estimates likewise join the
stationary signs across the overlapping spatial bands.

The record is 666674 bytes, below one MiB, and retains complete
genuine four-jet enclosures on every cell. Shared Taylor and index
payments are stored once with equality-checked references. The small
record can be replayed without any external large-data dependency.

These conclusions close the time gaps relevant to the positive
threshold criterion at heights |x|<=41. If RH fails, its positive
threshold collision must therefore occur at |a|>41. The theorem does
not provide an all-height relative sign or a globally covering family
of moving domains, and does not settle RH. Forward stationary collars
are assessed separately in
[Review 7](7_GUARDED_FORWARD_COLLARS_INTERNAL_REVIEW_20261014.md).
