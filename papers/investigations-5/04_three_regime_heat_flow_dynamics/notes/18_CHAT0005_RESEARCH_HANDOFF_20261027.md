# Chat0005 research handoff: collision energy and source acquisition

27 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.
Source chat: **Continue heat-flow research**, thread
`01a17e41-99d3-79c1-b932-2bae84ad0d47`, uniquely registered as
[chat0005][chat]. This note summarizes both research returns in this chat.

**Current position.** The chat established conditional finite-time energy
lower bounds, removed exact low-moment inputs from a finite source
approximation, and completed a matched raw-versus-shifted source comparison.
On each fixed positive-time slab, a moving contour improves the declared
source-data ledger by one logarithm. No theta first-jet lower margin,
new covered slab, improved Newman upper bound, or endpoint simplicity
theorem was obtained. The energy's logarithmic coefficient is unchanged.

## Start here

The [CE progress register][progress] is authoritative for CE-01 through
CE-08. Read [Notes15–16][n15] for the latest analytical comparison and
[Review07][r07] for its checks; [Note17][n17] states the implementation
contract. [Notes12–13][n12] and [Review06][r06] contain the earlier return.
The individual notes hold the proofs and complete constants.

Follow repository [AGENTS.md][agents], [chat-history instructions][history],
[large-file policy][large], [result index][results], [control register][controls]
and [avoid index][avoid]. Especially preserve [target classification][a01],
[scoped exclusions][a07], and [matched coupled estimates][a12]. This handoff
adds no new mathematical claim or manuscript milestone.

## Inherited baseline versus this chat's work

The starting assignment was [Note08][n08], with the first return in
[Notes09–11][n09]. Notes09–11, Review05 and numerics01 belong to
**chat0004**, not this chat. They supply the complete source/discriminant
interface, static scaled-energy transfer, and

\[
 E(t_c+u)=\frac{\kappa_m}{u}-2\kappa_m\gamma+O(u),\qquad
 \kappa_m=\frac{m(m-1)}{16}.
\]

Their bounded exterior correction cannot save an order-one amount on each
logarithmic annulus. Its tested budget has zero strict margin. Improving
that local expansion alone was already closed as an exclusion mechanism.
The shifted contour and its sharp mode-tail theorem were also inherited
from [arithmetic-rigidity Note06][ar06]. This chat does not claim priority
for contour shifting or its previously recorded fixed-shift mode gain.

This chat produced **Notes12–17, Reviews06–07, and numerics02–03**.

## 1. Finite-time energy comparison — Note12

At a hypothetical all-real threshold t_c, fix an isolated real zero a of
finite multiplicity m>=2. On the right-time interval where its cluster
remains isolated, real and simple, with the order-one all-real exterior,
[Note12][n12] proves

\[
 E_{\rm cl}(t_c+u)\ge\frac{\kappa_m}{u}.
\]

The proof retains the full exterior velocity B_ext=2U_z/U. If
partial_x B_ext<=-lambda on the cluster hull throughout the interval,
then, with p=m(m-1)/2,

\[
 E_{\rm cl}(t_c+u)\ge
       \frac{p\lambda}{4(1-e^{-2\lambda u})}.
\]

Confinement |x_i-a|<=rho<|a| and evenness supply
lambda=m/[2(|a|+rho)^2] from the reflected cluster. Exact centered-variance
and nonnegative shape-defect identities underlie the comparison. This
strengthens the previous asymptotic lower statement to a finite-time
inequality. It supplies no excluding upper estimate; matching all-real
threshold controls also satisfy it.

## 2. Unconditioned source acquisition — Note13

[Note13][n13] constructs a finite source approximation without inserting
the exact low event moments. For a fixed event amplitude c!=0 and order N,
acquiring raw accuracy |c|r^(m+N+1) gives normalized O(r^(N+1)) errors,
including the declared scaled derivatives. The cutoff schedules are

\[
 V(r)=\tfrac14\log\log(1/r)+O(1),\qquad
 K(r)=O(\sqrt{\log(1/r)}).
\]

Both the retained-integral midpoint error and a faster analytic source
quadrature are paid. The latter has
O(log(1/r)log log(1/r)) derivative terms at fixed parameters. This counts
terms, excluding arithmetic precision and derivative-generation costs.
Source tails, finite theta-mode tails and fixed-coefficient errors are
explicitly charged.

The approximation no longer assumes exact low moments, but energy use
still needs the event's amplitude, count, wall and scaled conditioning
gates. Cutoffs are frozen per annulus. No holomorphic approximant family
in r is asserted. Static energy transfer adds a summable error and leaves
the coefficient kappa_m unchanged.

## 3. Matched raw/shifted first-jet budgets — Note15

[Note15][n15] compares the same physical (H,H_x) target on
[b,B] x [A,A+Delta]. The exact full even source is completed before
truncating either modes or frequency. Both shifted arms, the derivative
of exp(-sigma x), analytic source disks, quadrature, source-coefficient
allowances and final evaluation errors are retained. The raw comparator
uses the same sharp tail theorem at sigma=0.

There is a concrete error distinction: fixed raw theta-mode cutoffs have
an inverse-square endpoint tail, and a fixed raw frequency wall has a
first-jet signal of order 1/x. The correctly completed shifted truncations
retain exponential errors. The imaginary-axis and remote-wall seams
explain why shifting an already truncated raw integral while discarding
its seams is invalid.
These are fixed-cutoff calibrations, not necessary joint-growing
complexity bounds.

The comparison uses the explicit positive carrier

\[
 W_t(x)=x^{7/4}\exp[-\pi x/8+(t/16)\log^2(x/(4\pi))].
\]

W is a declared normalization, not a lower bound on H. Exact published
gamma-modulus comparisons require their actual ratio bounds. If F=H/P,
the physical vector divided by P uses F_x+(log P)_x F; an ordinary
normalized derivative needs its additional error payment.

## 4. Radius tradeoff and positive-slab gain — Note16

[Note16][n16] defines J as the number of source cells, q as the integrated
Taylor order, and K as retained theta modes. Jq counts paired derivative
entries; KJq counts their individual mode contributions before aggregation.

For fixed shifts, smaller q is offset by the smaller strip-safe source
radius. Optimizing the displayed ledger gives the same leading
(e/8)X log X for Jq in both raw and shifted methods. The inherited
constant improvement in K remains. Requested precision can change the
best shift; no shift dominates all same-K or all-precision comparisons.

For fixed 0<b<=B<=1/2, fixed box width Delta, fixed precision, and X to
infinity, select

\[
 g=\zeta\log^2X/X,\quad \sigma=\pi/8-g,\quad0<\zeta<b/16,
\]
\[
 K+1=\left\lceil\sqrt{Q/\cos(4\sigma)}\right\rceil,
 \qquad Q>\max\{9/(4\pi),B/(8\pi),2/\pi\}.
\]

With the complete frequency, quadrature and coefficient contracts paid,
the sufficient schedules have

\[
 K=O(\sqrt X/\log X),\quad Jq=O(X\log X),\quad
 KJq=O(X^{3/2}),
\]

versus O(X^(3/2)log X) for the matched raw sufficient ledger. The
positive-time carrier factor pays the mode error, whose normalized bound
is exp((zeta-b/16)log^2 X+O(log X)). The result also allows
log(epsilon^(-1))=o(log^2 X).

This is an analytical source-data improvement. Coefficient generation,
derivative convolution, arithmetic operations, precision and runtime
remain unmeasured. The constants and onset depend on fixed b>0; there
is no uniform b down to zero theorem or new exp(C/b) exterior coverage.
All selections are frozen using the box endpoint X during differentiation.

## Verification and current task status

[Review06][r06] records separate same-model checks of the first return;
[numerics02][num02] replays exact rational geometry, conservative source
budgets and quadrature polynomial exactness. [Review07][r07] assesses the
matched comparison; [numerics03][num03] encloses twelve scalar designs
using the reused Fraction interval engine with outward 2048-bit rounding.

The moving fixed-Q mode schedule misses its normalized target at the
smaller sample heights 2^16, 2^64 and 2^256, and passes at 2^512. Those
failures remain recorded. They establish neither a practical crossover
nor coverage between examples. The usable source-coefficient tolerance
is its recorded **lower** endpoint. No source coefficient, actual theta
field value, first-jet margin or runtime benchmark was evaluated.
Reviews are internal same-model checks, not cross-model or specialist
validation. Replays do not independently verify every analytic proof.

| CE task | Handoff disposition |
| --- | --- |
| CE-01, CE-03 | Conditional source/energy interfaces remain complete; no new exclusion is implied. |
| CE-02 | Partial: analytical acquisition/comparison advanced; coefficient implementation and effective conditioning remain. |
| CE-04 | Bounded-exterior saving remains a scoped failure; an excluding arithmetic estimate is open. |
| CE-05 | Tested energy budget retains zero strict margin. |
| CE-06 | Open; no new positive slab or Newman upper bound. |
| CE-07 | Partial: fixed-positive-slab schedule and dependency audit; no zero-endpoint theorem. |
| CE-08 | The two returns from this chat are assessed and integrated. |

Parent TRD statuses and chat0001's Dobner/chat0002's response ownership
are unchanged. Accurate source evaluation alone does not distinguish
theta from colliding controls by a derived excluding inequality.

## Next bounded task

Implement one paired reference from Note15, enclose its source-coefficient
generation and final summation separately, and compare identical physical
first-jet targets and precision with [HDC Note13][hdc13] and
[HDC Note15][hdc15]. Measure the costs hidden by KJq, including derivative
convolution. Keep the two arms, shared derivatives and every error budget.

**Domain clarification for Note17:** the existing HDC oracle also covers
negative and complex times and higher jets. Notes15–16 establish real
positive-time first-jet bounds. Use a common real positive subbox of the
HDC domain: x in [26,46], 0<b<=t<=B<=10^(-4). A comparison on the full
HDC complex-time rectangle or higher jets requires additional bounds.
This existing box is calibration only, not new coverage.
Choose parameters from the finite gates; the asymptotic moving schedule
is not assumed effective at this calibration height.

Advance beyond calibration only if a complete accuracy/cost advantage
or a positive first-jet margin survives coefficient evaluation. Reuse
the existing [positive-threshold Section 5A][jet] consumer. If no advantage
survives, record the measured complete failure and close that specific
implementation branch. Do not revive more bounded local energy orders
or the already screened homogeneous finite-Gram relaxation as new margins.

Keep research in notes/, computations in numerics/, assessments in reviews/
and task changes in research-progress/. Refresh this chat's existing
registration through the standing history tool. A new chat must register
its own actual identity; it must not reuse chat0005's number or thread id.
Raw session exports stay outside the repository; no new manuscript
snapshot folders or large derived data belong in Git.

[chat]: ../chat-histories/0005_2026-10-27T16-46-30Z_continue-heat-flow-research.json
[progress]: ../research-progress/02_COLLISION_ENERGY_RESEARCH_PROGRESS_20261027.md
[n08]: 08_COLLISION_ENERGY_CONTINUATION_20261027.md
[n09]: 09_COMPLETE_SOURCE_AND_SCALED_ENERGY_TRANSFER_20261027.md
[n12]: 12_FINITE_TIME_CLUSTER_ENERGY_COMPARISON_20261027.md
[n13]: 13_UNCONDITIONED_SOURCE_ACQUISITION_AT_COLLISION_SCALE_20261027.md
[n15]: 15_MATCHED_RAW_AND_SHIFTED_SOURCE_ERROR_BUDGET_20261027.md
[n16]: 16_STRIP_RADIUS_AND_POSITIVE_SLAB_COMPARISON_20261027.md
[n17]: 17_RAW_SHIFTED_RETURN_AND_IMPLEMENTATION_CONTRACT_20261027.md
[r06]: ../reviews/06_FINITE_TIME_COMPARISON_AND_SOURCE_ACQUISITION_REVIEW_20261027.md
[r07]: ../reviews/07_RAW_SHIFTED_SOURCE_COMPARISON_REVIEW_20261027.md
[num02]: ../numerics/02_FINITE_TIME_AND_SOURCE_ACQUISITION_CHECKS_20261027.json
[num03]: ../numerics/03_RAW_SHIFTED_COMPARISON_CHECKS_20261027.json
[ar06]: ../../../investigations-3/11_arithmetic_collision_rigidity/notes/06_CANCELLATION_PRESERVING_APPROXIMATION_AND_NEWMAN_ROADMAP_CODEX_20261018.md
[hdc13]: ../../../investigations-4/12_height_dependent_heat_contours/notes/13_COMPLETE_THETA_WALL_AND_COEFFICIENT_CERTIFICATE_20261023.md
[hdc15]: ../../../investigations-4/12_height_dependent_heat_contours/notes/15_COMPLETE_PHYSICAL_CAP_COMPARISON_20261023.md
[jet]: ../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[agents]: ../../../../AGENTS.md
[history]: ../../../../tools/CHAT_HISTORY.md
[large]: ../../../../LARGE_FILES.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
