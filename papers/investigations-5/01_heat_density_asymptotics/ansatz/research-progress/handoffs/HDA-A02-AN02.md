# HDA-A02-AN02 r1 — bridge the shrinking and fixed negative-time windows

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
ansatz chat0001, thread `01a175aa-a487-79a1-85a8-6f465fdb36bf`.

Parent task **HDA-A02**. Next owner **Analysis — Sol**. Prepared,
not dispatched. The [ansatz register](../01_HIGH_HEIGHT_ANSATZ_RESEARCH_PROGRESS_20261025.md)
owns live status. [AN01 r1](HDA-A02-AN01.md) closes only the fixed
`1<=T<=2` representation request; the parent remains Partial.

## Read first

Follow repository AGENTS.md, LARGE_FILES.md, GPT_RESEARCH_MODEL_WORKFLOW.md
and tools/CHAT_HISTORY.md. Read [Note04](../../notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md),
[Note05](../../notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md),
their same-model assessments, the maintained manuscript, overview and
live progress entry. Pin the input versions actually consumed. Read the
[result index](../../../../../../result-summaries/README.md) and
[avoid index](../../../../../../avoid/README.md), especially the heat-flow
and collision-control clusters and the patterns concerning separate
absolute bounds, normalization and status stronger than evidence.

Use Note05's rechecked real Riemann--Siegel coefficient/remainder input
and exact gamma parameters. Any new classical input must be checked in
its primary source and recorded. Neither an evolved positive-time RS
estimate nor an unqualified extension of Note05's fixed-time constants
is an input for the new lower time endpoint.

## Frozen bounded request

Prove the bridge only on

    t=-T, 4/L_X<=T<=2, L_X=log(X/(4pi)), X>=X0,

then join it to Note04 through zero on their overlap

    4<=T L_X<=8,

to obtain a paid chartwise field representation on the single negative
interval `-2<=t<=0`. The bridge lower endpoint tends to zero with X;
this dependence is the new estimate to prove, not an already accepted
compact-time theorem.

Keep the complete canonical source

    H_t=-H_zz, H(0,z)=xi((1+iz)/2)/8,

the physical `q=epsilon_g^2`, fixed physical `K=k_ell k_h`, unnormalized
observables and actual signed covariance. Target the full physical strip
`|y|<=1`, averaging supports, fixed collar margin and analytic buffer:
as in Notes04--05 take `r=ell+2`, `b=1+h+2` and reserve one further
analytic unit. No root collar, reality or simplicity hypothesis may
replace a field estimate. Physical observable transfer is outside this
packet.

### A. Pay the finite representation down to T=4/L_X

Start with Note05 FN25, retaining its complete main arithmetic
population, real high-order RS correction integral and exact adjacent
cutoff transfer. Freeze `X,N,K,J,V,R` at the real chart center in both
space and time. Here `K` denotes the RS order, separately from the fixed
physical kernel K. Candidate choices are

    N=floor sqrt(X/(4pi)), K=ceil L_X, J=ceil(3L_X),
    V=8L_X, R=X^(1/3).

They may be adjusted by routine analytical choice if their full error
ledger is preserved. Do not replace the exact mode gamma curvature by
its first linearization, discard modes near N, or replace the exact
cutoff transfer by a lower-order mismatch bound.

The exact real-initial-value identity is

    H(-T,z)=(4pi T)^(-1/2) integral_R
              exp(-(z-u)^2/(4T)) H(0,u) du.

Its complex kernel costs `exp(y^2/(4T))`, now as large as a fixed
power of X on the buffered chart. Explicitly retain this factor, the
normalization `T^-1/2`, and all inverse-time factors in spatial
derivatives through order three and a first time derivative. Uniform
Gaussian moment estimates, rescaling and polynomial factors are
delegated to Sol; no factor may be declared bounded merely because it
was bounded on Note05's old `[1,2]` interval.

Pay separately and then combine:

- the real high-order RS remainder, including Gamma(K/2) growth;
- the common analytic gamma-curvature Taylor remainder with constants
  uniform in J and the entire arithmetic population;
- both genuine source tails, retaining the height exponential before
  switching to the global source bound;
- both artificial polynomial-Gaussian tails;
- the complete complex buffers and every derivative factor.

The candidate target is, uniformly on the declared buffered chart,

    |partial_z^j(H-Fhat_X)(-T,z)|
        <= C_j E_o(-T,z) exp(-c L_X^2),  j=0,1,2,3,
    |partial_t(H-Fhat_X)(-T,z)|
        <= C E_o(-T,z) exp(-c L_X^2),

for one fixed `c>0`, preferably `c=1/4` if the paid ledger permits it.
State the actual c, constants and onset dependence on the fixed buffers.
E_o is the positive sum of the elementary outer arm moduli, not the
true field or a vanishing cosine. A weaker proved bound must be reported
at its actual scale rather than silently relabeled as this target.

Note05's finite representation solves `partial_T Fhat=Fhat_zz` exactly
with all chart parameters frozen. Re-establish the relevant regularity
on this moving lower-time domain before using that identity to consume
the spatial error for the direct first time derivative. A zero residual
does not substitute for a field comparison.

### B. Join on the paid overlap and compute the actual residual

Let `F_cross` be exactly Note04 CS4 and its proved estimates; do not
upgrade its outer allowance or use Note05's natural-scale theorem as
an outer-scale theorem. Choose a smooth fixed scalar function chi(s)
equal to zero for `s<=4` and one for `s>=8`, and consider

    F_join(-T,z)=(1-chi(T L_X))F_cross(-T,z)
                   +chi(T L_X)Fhat_X(-T,z).

The cutoff is time-only on each frozen chart: `L_X` depends on its
center X, not on z or `Re z`. Its first time derivative is O(L_X).
Specify the sign on returning from T to t. The overlap is genuinely
paid by both representations; no interpolation across an unpaid gap
is allowed.

Prove the full field, spatial j=0,1,2,3 and direct first time errors
uniformly for `0<=T<=2`, including T=0 from Note04. In the overlap,
bound `Fhat_X-F_cross` through their comparisons with the same H.
Retain the derivative-of-chi term in the direct time comparison.

Compute and bound the actual signed heat residual

    (partial_t+partial_zz)F_join

using the known crossover residual, the exact finite-representation
residual and the derivative-of-chi times the difference of models.
State its support and bound; do not set it to zero or confuse it with
a spatial joining defect. The only join requested here is this
time-only chartwise join. Any claim about overlapping spatial charts
must retain the parent physical joining obligations.

A useful candidate summary is an error tending to zero relative to
E_o throughout `[-2,0]`, with the actual logarithmic factors for each
jet and time derivative stated, and the stronger exponential-in-L_X^2
bound away from the crossover. Derive the actual rates from the two
inputs and the chosen chi rather than assigning them in advance.

## Evidence standard and stop rule

Analytical only: no samples, numerical fits, machine-symbolic expansion,
exact-arithmetic checks or interval campaign. Housekeeping and manuscript
production are permitted. Routine order/window selection, kernel
partitions, Gaussian moments, analytic margins, cutoff transfers and
finite onset gates are delegated to Sol.

Stop after this bridge and the resulting `[-2,0]` chartwise theorem, or
at the first precise unpaid estimate after a focused attempt. Return
its expression, attempted bound, time regime, comparison envelope and
the exact derivative or tail that remains unpaid. No `T>2`, T growing
with X, arbitrary compact-time family, negative infinite-time overlap,
regulator layer, physical covariance transfer, provider precision or
runtime/quadrature theorem is included.

Do not change models or dispatch another chat automatically. A specific
resistant analytical mechanism may justify a prepared Astra handoff,
but the shrinking lower time endpoint alone does not justify escalation.

## Outputs and continuation

Save new research in ansatz/notes/, the assessment in ansatz/reviews/,
and small analytical input records in ansatz/numerics/. Append the
return/disposition here, update the sole progress register, overview
and maintained manuscript at the actual evidence status, and refresh
the unique ansatz chat history. Preserve earlier failures, source
versions and same-model review limitations. No snapshots or duplicate
chat registration.

## Return / disposition

Pending. HDA-A02 remains Partial. Note05's fixed `1<=T<=2` theorems and
Note04's signed shrinking-time theorem retain their separate proved
scopes and same-model internal assessment only. Parent HDA-17 Partial,
HDA-18 Gated and HDA-20 unfulfilled remain.

## Executed return — 25 October 2026

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, recorded effort ultra**, ansatz chat0001,
thread `01a175aa-a487-79a1-85a8-6f465fdb36bf`. Executed r1 without
changing its contract. The [input manifest](../../notes/06_NEGATIVE_BRIDGE_INPUTS_20261025.json)
pins opening versions. [Note06](../../notes/06_NEGATIVE_BRIDGE_AND_TIME_JOIN_20261025.md)
and [Assessment05](../../reviews/05_NEGATIVE_BRIDGE_AND_TIME_JOIN_ASSESSMENT_20261025.md)
contain the complete proof, gates and same-model acceptance.

NB16--17 extend Note05 FN25 unchanged to 4/L_X<=T<=2 with
C E_o exp(-L_X^2/4) field, spatial j<=3 and first time errors,
and exact model heat residual zero. The full complex kernel and
inverse-time losses are retained before absorption. Both orders, all
mode populations, cutoff transfers and all tails remain paid.

NB19 defines a piecewise time-only join to Note04, avoiding the
undefined T=0 finite formula. NB20--24 pay the entire [-2,0] chartwise
field/jet/time comparison and the actual signed joined heat residual,
including -L_X chi'(T L_X)(F_b-F_c). The total residual also includes
the crossover residual near zero; it vanishes for T L_X>=8.
No physical spatial join, observable transfer or all-time claim follows.

### Disposition — Analysis, Sol

**CLOSED** at the frozen bounded bridge-and-join analytical scope.
Accept NB16--17 and NB20--24, same-model internal assessment only.
HDA-A02 remains **Partial** for the wider compact-negative-time and
short-formula program. Numerical onset, provider/runtime and independent
specialist review remain absent. No numerical or symbolic research was
executed. [Small analytical return](../../numerics/A02_AN02_ANALYTICAL_RETURN_20261025.json)
records scope and output identity; [Note07](../../notes/07_CHAT0001_RESEARCH_SUMMARY_20261025.md)
summarizes all progress in this chat at the author's request.

Next **Analysis — Sol**, [HDA-A03-AN01 r1](HDA-A03-AN01.md), is prepared,
not dispatched. It addresses the distinct regulator one-arm/center
comparison, retaining the actual physical protocol and sensitivity.
No resistant mechanism here warrants Astra escalation. Parent statuses
remain unchanged.
