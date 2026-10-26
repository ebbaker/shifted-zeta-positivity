# HDA-A01-AN01 r1 — large-height calibration and the zero-time arithmetic bridge

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
chat0022, thread 01a17572-5411-7f32-9a12-7d1ba46ad679.

Parent branch task **HDA-A01**, supporting parent HDA-18.
Next owner **Analysis — Sol**; preparation phase READY_FOR_SOL,
unexecuted. The [ansatz register](../01_HIGH_HEIGHT_ANSATZ_RESEARCH_PROGRESS_20261025.md)
owns live phase/status. The author prioritizes very large height for
all real times, permits piecewise regimes and complicated remainders,
and wants the asymptotics, amplitude and phase correct.

## Read first

Follow the repository AGENTS.md, LARGE_FILES.md,
[model workflow](../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md)
and chat-history instructions. Read:

- [Overview](../../research-overview/01_HIGH_HEIGHT_ANSATZ_RESEARCH_OVERVIEW_20261025.md),
  [working manuscript](../../manuscript/main.tex), and
  [Note02](../../notes/02_HIGH_HEIGHT_PRIORITY_AND_DRAFT_SCOPE_20261025.md).
- Parent manuscript 01, 10–13, 14, 22–24; parent Notes27–31,
  Note60, and [Summary62](../../../notes/62_CHAT0021_RESEARCH_SUMMARY_20261025.md).
- [References](../../references/README.md): DLMF 5.11 and 25.10;
  Polymath arXiv:1904.12438v2 definitions, Theorem1.3, retained correction,
  Gaussian representation and Proposition9.1. Recheck the actual domains
  and the distinction between exact gamma and Stirling gamma.
- [Result index](../../../../../../result-summaries/README.md),
  particularly [11](../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
  and [12](../../../../../../result-summaries/12_collision_controls_and_screening.md);
  [avoid index](../../../../../../avoid/README.md), particularly
  01/02/05/07/08/12/16/19.

Save an input manifest before research. Keep the canonical source,
H_t=-H_zz, H(0,z)=xi((1+iz)/2)/8, physical q and fixed K.
No positivity/RH/simplicity assumption may replace a missing estimate.

## Frozen bounded request

Produce one analytical note, an assessment and a disposition for the
following connected task. Routine derivations, contour partitions,
branch choices, constants and finite onsets are delegated to Sol.

### A. Pin the outer carrier before seeking a uniform extension

With X=|x| and ell=log(X/(4pi)), verify the normalization and branches of

    A_o = pi^(1/4) X^(7/4)/16
          * exp[-pi X/8 + t(ell^2-pi^2/4)/16],
    Theta_o = X(ell-1)/4 + pi t ell/16 + 7pi/8.

Work first on the concrete compact interval 32<=t<=33 and the physical
strip |y|<=1, with all fixed buffers actually used. Derive a
carrier-scaled field comparison and its holomorphic jets j=0,1,2,3,
plus a directly justified first time derivative and the model's heat
residual. Expand the actual gamma heat carrier to its first nontrivial
correction, explicitly accounting for saddle curvature and determinant
as well as Stirling. The formal checkpoint in manuscript equation
formal-correction is to be checked, not assumed.

Separate the full cosine amplitude from one arm, reconcile x with
zeta height x/2, and preserve the unwrapped phase. Do not infer a
true H correction smaller than an unpaid arithmetic contribution.

### B. Establish one bounded bridge through zero time

Investigate the domain X>=X0 with ell>0 and

    |t| ell <= 8,    |y|<=1,

with the full declared fixed averaging and analytic buffers. X0 is
to be derived; 8 is a work boundary, not a critical constant.

Use the exact zero-time Riemann–Siegel anchor and candidate real-axis
weights/phase

    w_n = n^(-1/2) exp{t[(log n)^2-ell log n]/4},
    phi_n = Theta_o - (X/2+pi t/8) log n.

Determine a correct finite-sum field and cutoff/boundary correction,
or state exactly where the reduction fails. Retain the Riemann–Siegel
correction as part of the model whenever the requested error requires it.
Do not discard it or import the positive-time theorem at negative t.
For t<0, the exact starting identity is

    H(-T,z)=(4pi T)^(-1/2)
      integral_R exp[-v^2/(4T)] H(0,z-v) dv.

Pay the full integration window and tails. On complex charts use a
fixed cutoff or a corrected analytic representation across cutoff
changes. Account for the growing mode population; the fixed-n limit
w_n -> n^(-1/2-tau/4) alone is insufficient.

Aim first for field and buffered spatial-jet errors and state the
time-derivative status separately. A scoped negative-time obstruction
or an exact unpaid correction is a valid bounded outcome. This packet
does not require a full all-real-time theorem, a useful runtime theorem,
or the complete physical covariance transfer.

## Evidence standard and limits

Analytical only. No numerical fitting, source/field samples,
machine-symbolic expansion, exact-arithmetic checks or interval campaign
are authorized by this packet. Housekeeping and manuscript production
are allowed. Derive formulas by analysis and preserve failures.

Use a positive carrier envelope; never normalize by a vanishing cosine.
A complete result states domain, branch, constants/onset or their exact
remaining status, all arithmetic/contour/tail errors, cutoff handling,
jet/time scope and compatibility with the existing parent inputs.
Keep inherited results, new proofs and formal candidates distinct.

Stop after the calibration plus one bounded crossover argument, or at
the first precise unpaid signed-time/contour/cutoff estimate. Record
its expression, attempted bound and regime. Escalate to Astra only if
that specific mechanism remains resistant after a focused Sol attempt;
the fact that the larger objective is all-time does not itself require
Astra. Do not expand to global negative-time scales or regulator-layer
optimization within this packet.

## Outputs and continuation

Save the analysis in ansatz/notes/, assessment in ansatz/reviews/ and
any small analytical-only record in ansatz/numerics/. Append the return
and named disposition here, with actual model/effort, thread, input
versions, corrections, limits and evidence paths. Update the ansatz
register and unique chat history. Update the maintained manuscript only
with the result's actual status. No snapshot or automatic dispatch.

This high-height packet is the next task; the earlier Gaussian-polynomial
core packet HDA-18-AN09 remains preserved and deprioritized.

## Return / disposition

Pending. No new uniform crossover theorem or negative-time asymptotic
has been accepted. Parent HDA-17 Partial, HDA-18 Gated and HDA-20
unfulfilled remain.


### Return — Analysis, Sol, 25 October 2026

Executed r1 analytically with **gpt-6.1-sol (Codex), actual effort ultra**,
ansatz chat0001, thread `01a175aa-a487-79a1-85a8-6f465fdb36bf`.
The [input manifest](../../notes/03_CALIBRATION_BRIDGE_INPUTS_20261025.json)
pins the input versions. No numerical, machine-symbolic, exact-arithmetic
or interval research was executed.

[Note03](../../notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md)
proves the normalization, actual gamma-heat first correction (including
curvature and determinant), full-buffer compact-positive jets j=0..3,
direct time bounds and exact elementary/corrected residual on [32,33].
It also proves a corrected **signed real-axis field** bridge for
abs(t) log(X/(4pi))<=8 with O(A_o X^-1/4) error, complete Gaussian
window/tails, all modes and analytic fixed-cutoff correction. Constants
and onset gates are finite but unevaluated.

The required full-strip signed-time remainder CB28 remains open. The
naive real-initial-value complex Gaussian bound incurs
exp[(abs(y)-T log(X/(4pi))/2)^2/(4T)], so it does not close uniformly
through zero. This is a scoped failed route, not an impossibility theorem.
No signed buffered jets/time derivative or physical covariance transfer
is claimed. The maintained manuscript was updated at these actual statuses.

### Disposition — Analysis, Sol

Accept the bounded results and limitations in
[Assessment02](../../reviews/02_CALIBRATION_AND_REAL_BRIDGE_ASSESSMENT_20261025.md),
with same-model internal review only. Close AN01 at its permitted bounded
partial-return scope; keep HDA-A01 **Partial**. The opening polynomial
bound for a narrow middle strip was enlarged to a buffer-dependent power
for the fixed contour endpoints; the results are unchanged.

Next **Analysis — Sol**, [AN02 r1](HDA-A01-AN02.md): prove the fixed-cutoff
complex remainder or a sufficient specified epsilon-loss version, then
pay its full buffered signed-time consumers. Prepared, not dispatched;
no Astra escalation is justified by the current routine gap alone.
Parent HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled remain.
