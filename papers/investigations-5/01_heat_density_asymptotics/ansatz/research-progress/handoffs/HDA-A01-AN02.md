# HDA-A01-AN02 r1 — fixed-cutoff complex remainder and buffered crossover

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**.
Ansatz chat0001, thread `01a175aa-a487-79a1-85a8-6f465fdb36bf`.

Parent task **HDA-A01**. Next owner **Analysis — Sol**. Prepared, not
dispatched. The [ansatz progress register](../01_HIGH_HEIGHT_ANSATZ_RESEARCH_PROGRESS_20261025.md)
owns live phase/status. AN01 r1 is preserved with its appended return.

## Read first and input scope

Follow repository AGENTS.md, LARGE_FILES.md, GPT_RESEARCH_MODEL_WORKFLOW.md
and tools/CHAT_HISTORY.md. Read the
[overview](../../research-overview/01_HIGH_HEIGHT_ANSATZ_RESEARCH_OVERVIEW_20261025.md),
[Note03](../../notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md),
its [assessment](../../reviews/02_CALIBRATION_AND_REAL_BRIDGE_ASSESSMENT_20261025.md),
and [AN01 return](HDA-A01-AN01.md). Preserve actual source versions with
an opening input manifest. Recheck primary RS contour definitions in
Polymath equations (36)--(38), its corrected equation (69), DLMF25.10,
and the exact domains of any imported estimate.

The compact outer task on `[32,33]` is completed at its in-note/same-model
status. The zero-time/signed real-axis finite-sum bridge is proved at
`O(A_o X^-1/4)`, with a retained correction. The next work is the
complex estimate, rather than redoing the outer normalization or
launching a numerical campaign. No independent specialist review has
been obtained.

## Frozen bounded request

Keep the canonical complete `H_t=-H_zz`, `H(0,z)=xi((1+iz)/2)/8`,
the physical `q=epsilon_g^2`, and fixed `K=k_ell k_h`. Do not assume
RH, positivity of an unknown remainder, real zeros, or simplicity.

Let `s=(1+iz)/2`, `a=sqrt(z/(4pi))`, and choose
`N=floor sqrt(X/(4pi))` **once per chart**, not as an analytic function.
Use the exact gamma factor and analytic branch

    M(w)=w(w-1) pi^(-w/2) Gamma(w/2)/16,
    G(z)=sqrt(M(s) M(1-s)), positive on the real segment,
    C(p)=cos(2pi(p^2-p)-pi/8)/cos(2pi p),
    R_N(z)=(-1)^N G(z) a(z)^(-1/2) C(a(z)-N),
    S_N(z)=sum_{n<=N}[M(s)n^(-s)+M(1-s)n^(-(1-s))],
    E_N(z)=H(0,z)-S_N(z)-R_N(z).

Every apparent pole of C is removable. Its exact recurrence
`C(p)+C(p-1)=2cos(2pi(p-1)^2-pi/8)` pays the adjacent cutoff mode
on real fixed charts within the existing `O(G X^-3/4)` remainder.
That real-axis result is not an off-axis error theorem.

### A. Prove the missing complex estimate or return its exact failure

For `R=ell+2`, `B=1+h+2`, target Note03 CB28:

    |E_N(z)| <= C_{B,R} X^(-3/4) [|M(s)|+|M(1-s)|],
    |Re z-X|<=R+17, |Im z|<=B+1,

uniformly in large X, every fractional cutoff position and adjacent
threshold. A proved `X^epsilon` loss, for one specified
`0<epsilon<1/4`, is sufficient for this bounded continuation. Give
the actual constants/onset status and any restriction on fixed widths.

Routine contour choices, branch definitions, strip partitions and finite
onset gates are delegated to Sol. Possible routes include the exact
fixed-cutoff RS contour or a local three-lines argument: a real rectangle
of width about `log^2 X`, real-edge corrected RS estimate, an independently
paid upper edge on a larger fixed strip, and exponentially suppressed
vertical edges. This is a suggested route, not an inherited theorem.

Do not attempt to deduce the estimate from real values plus holomorphy
alone. The naive real-initial-value Gaussian bound has the factor

    exp[y^2/(4T)+T L^2/16-|y| L/4]
      =exp[(|y|-T L/2)^2/(4T)],  L=log(X/(4pi)),

which is not uniform as `T L` tends to zero. Note03 preserves this failed
route without claiming an obstruction to all complex methods.

### B. Consume the estimate within the same bounded time window

If A succeeds, propagate it through the exact **negative-time** real
Gaussian convolution for `0<=T L<=8`. Reuse the `|v|<=16` local window,
gamma-envelope near tails up to `|v|=X/2`, and the distant complete-source
bound; enlarge windows only with a recorded new fixed constant and paid
tail budget. Include the full mode count and the retained correction.
The target is the holomorphic version of

    F_N(t,z)=A_o(t,z) sum_{n<=N} w_n(t,z) cos(phi_n(t,z))
                     +exp(-pi^2 t/64) R_N(z),

with carrier-envelope error `O(X^-1/4+epsilon)` and spatial jets
`j=0,1,2,3` on all of the physical/averaging/analytic buffers. Obtain
jets on `1/log X` disks, with their log factors, rather than losing
height powers through fixed-radius Cauchy bounds.

State the small-positive-time buffer status separately: the inspected
Theorem1.3 domain `0<=y<=1` cannot pay arbitrary fixed averaging margins
by assertion. Use its justified larger-domain contour variant or return
that exact unpaid extension. Do not replace it by the eventual
two-carrier theorem when `t L` remains bounded.

For the first time derivative, either derive a direct uniform bound
using an analytic remainder/heat identity and the model residual, or
explicitly leave it open. Differentiating the Gaussian remainder bound
naively costs `1/T` and does not pay the zero-time endpoint.

## Limits and stop rule

Analytical only: no numerical fits, field samples, symbolic expansion,
exact-arithmetic checks or interval campaign. Housekeeping, hashes and
manuscript production are permitted. Stop after this buffered crossover
comparison, or at a precise unpaid contour/interpolation/cutoff term
after a focused attempt. Preserve its expression, proposed bound and
regime. Do not expand to global negative times, regulator layers,
Lambert W, runtime or full physical covariance transfer.

Escalate to **Analytical — Astra** only if a specific mechanism remains
resistant after that focused attempt. The broad all-time objective is
not itself an escalation reason.

## Outputs and disposition

Save the proof/scoped failed route in ansatz/notes/, an assessment in
ansatz/reviews/, and any small analytical record in ansatz/numerics/.
Append a return and named disposition here; update the sole ansatz
progress register, maintained manuscript only at actual evidence status,
and this chat's unique ansatz/chat-histories registration. No snapshots,
automatic dispatch or model changes.

## Return / disposition

Pending. The signed real-axis result of Note03 is retained; the full
buffered signed-time field/jet theorem is open. Parent HDA-17 Partial,
HDA-18 Gated and HDA-20 unfulfilled remain.


### Return — Analysis, Sol, 25 October 2026

Executed r1 with **gpt-6.1-sol (Codex), actual effort ultra**, verified
from current turn metadata; ansatz chat0001, thread
`01a175aa-a487-79a1-85a8-6f465fdb36bf`. The
[opening manifest](../../notes/04_COMPLEX_STRIP_INPUTS_20261025.json)
records the inputs. Analytical only; no numerical, symbolic,
exact-arithmetic or interval research was executed.

[Note04](../../notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md)
proves the exact CB28 complex remainder, with no epsilon loss, by a
fully paid rectangle/maximum-principle argument. The upper edge retains
the ordinary Dirichlet tail. A separate published-contour check agrees.
The same fixed-N model has full buffered signed-time field, j=0..3
spatial jets and direct first time derivative on |t| log(X/(4pi))<=8.
Its field allowance is delta=X^-3/4 exp(t_- L_X^2/16), at most
C X^-1/4, and X^-3/4 for nonnegative times.

Both Gaussian identities, the full mode count, retained correction,
arbitrary fixed buffers, and all tails are paid. The window16 was
enlarged to a fixed V_b chosen from frozen source/ray constants,
with its larger initial charts explicitly included. Constants and
finite onset gates are not numerically instantiated. Time is bounded
via the exact heat identity and actual model residual, with no 1/T loss.

### Disposition — Analysis, Sol

Accept the results at their proved-in-note, **same-model internal
assessment only** status; see
[Assessment03](../../reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md).
Close AN02 r1 and the combined AN01--AN02 bounded scope of HDA-A01.
The maintained draft and current status documents were synchronized.
No independent specialist review, physical observable transfer,
useful runtime, all-time union or RH/simplicity conclusion follows.
Parent HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled remain.

Next **Analysis — Sol**, [HDA-A02-AN01 r1](HDA-A02-AN01.md): one fixed
negative-time window 1<=T<=2, paying growing-order/contour and mode-heat
curvature errors instead of substituting into this shrinking-time budget.
Prepared, not dispatched. No exceptional Astra escalation is warranted
without a focused attempt at that specific next estimate.
