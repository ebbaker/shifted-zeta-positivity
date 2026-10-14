# First research pass on the prioritized lifted theta directions

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: `gpt-6-astra` (Codex); reasoning effort **ultra**, read from
the actual session configuration. Three parallel agents inherited that
configuration. Their derivations and the integrating agent's checks are
internal model review, not independent specialist or formal validation.

## Outcome and allocation

The [earlier assessment](ACTIVE_DIRECTIONS_REVIEW_CODEX_20261013.md) gives
the right order for bounded discovery. This pass executes its proposed
allocation: **02 angular gluing and 01 complete cutoff reflection**, with
**17 boundary winding** as a small comparison. It reviews the initial
programs for all 17 active directions, rather than beginning 17 campaigns.

The strongest new analytic result is a complete moving-period angular
identity with a convergent, piecewise choice of period. It also identifies
why the simplest positive-kernel interpretation fails. The reflection
calculation retains an endpoint term that the proposed pairing does not
cancel. The genuine-theta boundary certificate passes, but its matched
interior comparison is cheaper. These are completed first tests with
specific consequences for the next allocation; none supplies a new global
theta sign, moment saving, zero-free region or RH result.

## What the originating discussion asks us to preserve

The [13 October conversation](../../chat-histories/0002_2026-10-13T12-54-02Z_review-newman-certificate-audit.json)
began with possible theta reflection identities, then explicitly redirected
the search toward higher-dimensional lifts and coordinate changes that
had simplified apparent singularities. The research question is whether
the genuinely prepared lifted source exposes a usable constraint on the
physical observations. A successful coordinate change need not itself be
an excluding inequality to be useful, but its source and projection must
remain visible in the eventual argument.

The older [strategy conversation](../../chat-histories/0003_2026-10-12T21-32-30Z_review-claude-s-priority-changes.json)
and [formal replay conversation](../../formal_replay_crosswalk/chat-histories/0001_2026-10-13T01-50-44Z_review-investigation-brainstorm.json)
keep the audit lanes separate. Their current records report three accepted
pinned Lean replays, with new arithmetic applications still uncompiled,
and substantial Newman supplier audits, with producer and coverage work
remaining. This pass reads those statuses; it does not independently
replay or validate those theorem chains. Their standing next tasks remain
in the [formal](../../formal_replay_crosswalk/README.md) and
[Newman](../../newman_certificate_audit/README.md) investigations.

The original program notes preserve their initialization status and the
proposed Claude review. The current user request starts the bounded work
reported here. It does not turn these internal assessments into that
cross-family review.

## 02: complete elliptic transport, with its convergence cost

The [angular derivation](../../active/02_angular_jacobi_gluing/notes/ELLIPTIC_INSERTION_TRANSPORT_AND_HEAT_OBSTRUCTIONS_20261013.md)
now transports the classical elliptic laws through the actual insertion.
Write
\[
F=e^{u+\pi z^2/2}\Theta(e^{4u},e^{2u}z),\qquad
M=(\partial_u^2-1)F/16.
\]
For a real period use \(p=e^{-2u},\ \kappa=\pi\); for an imaginary
quasiperiod use \(p=\pm i e^{2u},\ \kappa=-\pi\). Set
\(q=\kappa(pz+p^2/2)\) and \(B=\partial_z-\kappa z\). The exact
transport is
\[
e^{-q}M(u,z+p)=M(u,z)+
\frac{-2p'BF_u-p''BF+(p')^2B^2F}{16}.
\]
These connection terms cannot be omitted. The classical input is the
[theta quasiperiod law](https://dlmf.nist.gov/20.2.E8); the insertion and
heat-transform consequences are derived in the new research note.

Using either single period on the whole real source line creates an
exponentially growing term on one tail. Its positive-time heat integral
therefore fails already at angular coordinate zero. Choosing the short
real period on the positive half-line and the short imaginary period on
the negative half-line fixes this convergence problem. Symmetrizing the
two signs of each short period gives a complete identity involving
half-line transforms at spectral shifts \(x+4i\) and \(-x+4i\), with
the zero mode removed before transformation. The unsymmetrized version
has an explicit origin term after integration by parts.

This repair does not produce a positive auxiliary kernel. At angular
coordinate zero its symmetrized source is
\[
\mathcal A(u,0)=\Phi_e(u)-2\pi^2e^{|u|}
\sum_{n\ge1}n^2e^{-\pi n^2e^{4|u|}},
\]
which is negative at \(u=0\). The splice also introduces a cusp at
zero, whose Fourier tail must remain in the error or source relation.
That auxiliary tail cannot be treated as an independently visible
physical observation after dropping the corresponding correction.

A second result settles the finite angular-jet bookkeeping. Direct
differentiation of the defining series gives
\[
M_{zz}=\pi M_u+\pi^2z^2M,
\qquad
K_{zz}=\pi i(2t\partial_x-x)K+\pi^2z^2K.
\]
Consequently every Taylor coefficient is an explicit scalar differential
operator:
\[
[z^{2j}]K_t=Q_j\big(i(2t\partial_x-x)\big)H_t,
\quad Q_0=1,\quad Q_{-1}=0,
\]
\[
Q_{j+1}(D)=\frac{\pi DQ_j(D)+\pi^2Q_{j-1}(D)}{(2j+2)(2j+1)}.
\]
Operator powers retain the noncommutation of multiplication by \(x\)
with differentiation. This is stronger than merely identifying the first
redundant coefficient. It does **not** say that all angular coefficients
vanish at a collision: at an ordinary double zero with \(t>0\),
\([z^4]K=-\pi^2t^2H_{xx}/6\) is nonzero. It says that a new finite
coefficient calculation alone supplies a derivative dictionary rather
than the missing source estimate.

**Decision.** Keep the complete short-period identity as a legitimate
source relation. Further work should name a bound on its complete shifted
channels, with the origin contribution, that could improve a prescribed
adjoint residual or one of the paired signs. Do not expand angular-jet
tables or infer positivity from the new representation. Exact arithmetic
checks support the operator algebra; floating theta checks are explicitly
diagnostic and are not global numerical enclosures.

## 01: the reflected shared endpoint survives

The [cutoff derivation](../../active/01_complete_cutoff_reflection/notes/COMPLETE_REFLECTED_BLOCK_AND_ENDPOINT_OBSTRUCTION_20261013.md)
takes a literal reciprocal pair \([N/2,N]\), \([N,2N]\) at
\(P=N^2\). Both blocks retain the same finite Poisson ceiling and their
remaining Fourier tails. The note retains half-weight endpoints, the
actual coefficient amplitude and carrier, physical derivative terms and
the adjacent-cutoff correction ledger.

For ordinary adjacent-block gluing, the common endpoint cancels in the
oriented boundary terms. For the conjugated reflection comparison, it
instead appears as
\[
E_I(N)+e^{i\Theta}\overline{E_E(N)}.
\]
The new calculation proves its magnitude exceeds \(w_N/20\) for even
\(N\ge4\) at the prescribed reciprocal centers, with the note's
amplitude mismatch \(|\delta|\le1/2\). Thus the complete retained
modes must cancel or pay it; the reflection does not remove it for free.
This is an obstruction to that endpoint-cancellation argument, not to
every possible complete reflection identity.

The bounded diagnostics compare paired tails with the sum of the
separate actual tail magnitudes. The retained ratios range from about
0.957 to 0.991, showing little special reflection saving at these points.
A large apparent gain against a much looser absolute
envelope would not establish new signed structure. These finite chirp
calculations are not certificates of the full physical \((H,H_x)\),
and the note keeps the high-height approximation hypotheses separate
from its small-cutoff algebra diagnostics.

**Decision.** Retain the complete formula and stop the automatic shared
endpoint-cancellation ansatz. Reopen it only with a relation controlling
the endpoint together with the retained saddle modes and the physical
remainder. It is not ready to supply a paid observability certificate
to direction 03.

## 17: an actual certificate and a negative cost comparison

The [genuine-theta pilot](../../inactive/17_spacetime_collision_degree/notes/1_GENUINE_THETA_BOUNDARY_PILOT_20261013.md)
uses the compact rectangle
\[
[0,0.05]\times[8,12]
\]
and the full physical theta integral. The evaluator uses 60-digit outward
Decimal arithmetic, 512 source cells, explicit geometric bounds for
theta indices \(n\ge4\), and an analytic bound for \(u\ge1\).
It encloses complete parameter intervals, rather than interpolating
sampled angles. No height-dependent cutoff or carrier occurs here.

All four boundary sides lie in the lower half-plane of \(H+iH_x\),
so straight homotopy to \(-i\) proves winding zero. The previously
derived analytic heat index theorem then excludes all finite-multiplicity
collisions in the rectangle. Its higher-multiplicity argument was also
checked for the assumptions actually used by this pilot.

The matched interior calculation is stronger and cheaper on this easy
rectangle: one full interval box gives
\[
H>0.0223323,\qquad H_x<-0.00253515.
\]
The boundary test uses four pair integrations and three distinct heat
weight builds; the interior test uses one of each. Both use the same
source, arithmetic and infinite-tail bounds. The earlier atlas's finer
stationary-jet certificate is not used as an artificially expensive
baseline for this simpler joint-zero problem.

**Decision.** No expansion of the winding campaign on this evidence.
Reopen for a demonstrably difficult cell, or an independently justified
boundary homotopy that saves work. A low-height calibration neither
measures asymptotic cost nor supplies unbounded-height coverage.

## Remaining active directions and next choice

| Direction | Assessment after this pass |
| --- | --- |
| 03 Anchored observability | A downstream target; wait for a relation with a paid residual rather than optimize the same exact finite constraints again. |
| 04 Chord closure | Support 02 or 06 with one independent transverse correlation estimate; the current scalar dictionary remains insufficient. |
| 05 Metaplectic atlas | Build only a chart serving a named identity or measured conditioning improvement. |
| 06 Paired factorization | Retain both derivative-level kernels and their complete stationary conditions. No factorization emerged in this pass. |
| 07 Divisor transport | Keep the six-term algebra check capped; divisor exchange already belongs to the complete pair sum. |
| 08 Cusp unit sector | A separate arithmetic priority if the work turns to moments; the unit branch still needs a saving before positive enlargement. |
| 09 Rank two addition | Best next distinct identity calculation. Transport the actual differential insertions into both unequal-scale parity cosets before testing a sign. |
| 10 Gaussian Hermite | Use as a comparison or transfer of an actual source relation, not another coefficient survey. |
| 11 Stein/SUSY | Require a named nonlocal theta restriction on the stationary products. |
| 12 Canonical boundary | Longer-term; construct the source map and its heat defect in the known admissible regime first. |
| 13 Stability preparation | Longer-term; one admissible preparation operation or a precise obstruction, with no assumed stable theta input. |
| 14 Volterra | Keep capped until a theta restriction beyond generic moment integration by parts is specified. |
| 15 Adelic compatibility | A supporting source-selection framework; common-exponent consistency alone gives no physical observation bound. |
| 16 Radial geometry | One source-conditioned signed relation including its nonlocal generator; further dimension classification has no demonstrated benefit yet. |

The next allocation should be **one quantitative continuation of 02 only
if a specific complete-channel inequality is proposed, and otherwise the
bounded 09-to-06 calculation**. Neither the present 01 endpoint test nor
the 17 calibration warrants a larger campaign. This preserves the lift
as a discovery tool while making the next missing estimate explicit.

The [execution and input record](../numerics/PRIORITY_RESEARCH_FIRST_PASS_RECORD_20261013.json)
binds the reviewed sources and retained outputs. Program notes give the
derivations, numerical scopes and reproduction commands. No manuscript
snapshot or large generated dataset was created.
