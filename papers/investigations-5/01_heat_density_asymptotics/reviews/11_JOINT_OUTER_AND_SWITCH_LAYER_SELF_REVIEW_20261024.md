# Joint outer range and regulator layer: same-assistant review

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from the session metadata. This is the same assistant that
derived and wrote [Note 28][note]. It is not independent specialist
review and does not complete HDA-20. No numerical, exact-arithmetic or
machine-symbolic execution was performed.

**Disposition:** retain the results as **proved in-note, same-assistant
review only**. HDA-19 advances within Partial: static density comparison
now crosses t=64 and has a joint time/height range. Static averaged
potential and filtered-w derivatives through order four are also paid.
The new range is exponentially far from the inner window at large time,
so HDA-18 remains gated. The continuation remains Analytical — Astra;
there is no pending Sol assignment.

## 1. Time-dependent field error

I checked the time factors against the exact convolution normalization.
The real Gaussian has variance t/2 and mean t Re(alpha)/2. Dividing its
absolute integral by the modulus of the complex integral costs
`exp(t (Im alpha)^2/4)`. Note 28 bounds this by exp(t), using the
uniform eventual bound |Im alpha|<=2. Its local gamma error is therefore
`C exp(t)(t+t^2 log^2 X)/X`, not a compact-time O-term asserted to be
uniform in t.

On `32<=t<=(log X)/4`, this gives the displayed X^-3/4 log^4 X rate.
The full arithmetic tail gives X^(-t log(2)/8), after constants linear
in t in its exponent are absorbed by a fixed fraction of t log X.
The lower linearized tail and the bounded middle strip have
`X^(C_Y) exp(-t log^2 X/128)` bounds. The positive infinite tails use a
horizontal-ray gamma bound valid beyond bounded real parts and a
Gaussian bound uniform because X^(1/3) dominates log^2 X. The
conservative last term in JT11 is sufficient. Every term is uniformly
small in the stated range.

For a fixed `[32,T]` the exp(t) factor is bounded and the stronger
O_T(log^2 X/X) rate follows from the same proof. Neither argument imports
Polymath's small-time high-zero theorem above its range. The lower time
32 is a chosen proof convenience, not a certified onset or a new
physical transition. The upper time (log X)/4 is sufficient, not proved
necessary or optimal.

## 2. The arbitrary-positive-q local lemma

The new transfer is conditional on already proved simple-root geometry,
not merely on small absolute field error. Both H/A and P/A have one
simple root in each phase-scaled disk, their root shift is O(e), and
their zero-free analytic units differ by O(e). The unit estimate follows
on the boundary by division and then throughout the disk by the maximum
principle; its removable points are filled before applying that principle.

For fixed Q(u)>0, change the analytic unit first, then translate the root
while holding Q(u) fixed. The logarithmic derivative is bounded by
`2|e_0|/|u-se_0|`, and the w derivative by
`|e_0|/(2|u-se_0|)`. Both are integrable with respect to planar area.
No derivative or lower bound of Q is required. After restoring the
omega^-2 area factor and summing O(omega) disks, the full L1 error is
O(e), including the exterior complement. The two fields share precisely
the same q/|A|^2; no unacknowledged normalization of the physical density
occurs.

Subtracting the two exact weak adaptive identities retains the gradient
and Laplacian of r and the w(1-w) term. Their difference has the required
Lipschitz bound on [0,1]. This proves the O(e) density transfer when
beta X is bounded. It cannot be applied with an unbounded spatial-r
constant and then declared uniform; the separate resolved-regulator
argument supplies the other regime.

The same L1 result directly gives the **physical averaged potential**
and filtered-w spatial-jet comparison: transfer derivatives through order
four to K. The kernel is C3 and has bounded weak fourth derivatives;
there is no boundary delta at this order. This is a static potential
comparison with its additive normalization retained. It does not estimate
squares of unfiltered gradients, potential time derivatives or covariance.

## 3. Regulator bounds in the joint range

The split is beta X<=pi versus beta X>pi. In the first regime the spatial
log-regulator derivatives are bounded, regardless of epsilon/A_X. In
the second regime the collar logarithmic bias is exponentially small.
For bounded times through 128, the quadratic exponent and beta X>pi
pay the carrier's exp(-pi X/8) scale on the full horizontal buffer.

For growing t, the saddle equation proves
`L<=C log(2+t)` and `ct<=kappa<=Ct log(2+t)`. The strict lower bound
L(64)>1/4 and L'>0 supply the lower kappa bound. Substitution into the
explicit regulator amplitude gives
`|log E_0|<=Ct log^2(2+t)`. For t>=128 and t<=(log X)/4,
beta is at least c/[log X log(2+log X)]. Its regulator exponent dominates
all carrier and regulator-amplitude growth. Thus lambda_X decays
exponentially uniformly, while the weak-test factors grow only
polynomially in X. Root displacement then finishes the density transfer.

This verifies a genuinely joint static range and a compact-time estimate
crossing 64. It does not yield a uniform bound on all positive t at fixed
X, and it does not connect to the inner large-time window.

## 4. Layer shape, center and width

The layer approximation keeps the logarithmic ratio
`b=log(epsilon_g/A_X)`, with d=b_+/omega. In the bounded-beta-X regime,
that ratio varies only O(1) across the fixed averaging buffer. The
potential of the cosine pair differs in L1 by O(1) from
`2log|A|+2 max(b,omega |v|)`. Away from zeros this follows from the
cosine/cosh comparison; at zeros the logarithm is integrable on phase
collars. The carrier logarithm is harmonic and the adaptive corrections
are O(1). The transverse second derivative of the maximum produces two
layers with weight omega/(2pi), merging to omega/pi at d=0. The horizontal
kernel still contributes its exact unit integral.

This establishes O(1) absolute error for the elementary layer profile,
not the vanishing absolute error of the more detailed gamma-field model.
Its O(1/log X) normalized error is stated separately. The off-axis
layers describe the rationally regularized density, not nonreal zeros.

The actual smooth switch has
`log beta=-64/Delta+1-log kappa(64)+O(Delta)`.
At the gamma-defined center, beta=pi/(4X)+O(log^2 X/X^2), hence the
constant in the denominator of the location expansion is
`c_0=log(4e/(pi kappa(64)))`. I checked its sign by solving the two
logarithmic equations before expanding the reciprocal.

The center derivative is
`b_t=-(pi/512)X log^2 X (1+O(1/log X))`; dividing by
omega~log X/4 gives the time scale 128/(pi X log X). This checks both
the 512 and 128 factors and the direction: earlier times correspond to
positive tau and separated regularized layers. The bound for b_tt comes
from the explicit switch derivatives, not differentiation of the center
asymptotic. It pays the Taylor remainder uniformly on bounded tau ranges.

The exact implicit center must remain in JT32--JT33. An inverse-logarithm
location expansion has an error much larger than the inverse-X width.
Replacing the center by a leading estimate would invalidate the resolved
profile even though that estimate is a valid coarse location asymptotic.
No chosen-height center has been numerically computed or certified.

## 5. Residual, scope and next action

With D_t=(log G_t)', the heat residual is exactly
`(1/4) sum G_t(alpha^2-D_t^2-D_t')`. Expanding D_t gives all four terms
in JT35 and the joint bound in JT36. The two compositions each contribute
-1/4 to the second z derivative. This residual is not zero and has not
been propagated to an evolution error theorem. Current, density/potential
time derivatives, forcing and actual Q/Delta Q remain open.

At a fixed large t the new joint outer range starts at exp(4t), whereas
the proved inner window has polynomial size kappa^(1/3). Placing these
theorems together therefore leaves a large spatial gap. This is a scope
statement about their proved sufficient domains, not a demonstration
that either approximation must fail in that gap.

The unchanged complete xi identity and full arithmetic source are the
same distinguishing inputs as in Note 27's control screen. The local
positive-q lemma can hold for a control on a simple-root subdomain and
is not a global collision exclusion. No RH conclusion is made.

**Next: Analytical — Astra.** Replace the absolute Gaussian integration
loss using a paid complex-contour/saddle analysis, state the improved
joint range, and compare it honestly with the inner domain. The next
session's exact entry points and stop rules are in [Note 29][next].
An independent audit remains separately open under HDA-20.

[note]: ../notes/28_JOINT_OUTER_REGULATOR_TRANSFER_AND_SWITCH_LAYER_20261024.md
[next]: ../notes/29_CONTINUATION_JOINT_OUTER_TO_INNER_MATCHING_20261024.md
