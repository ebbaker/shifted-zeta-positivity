# HDA-A04-AN01 r1: first corrected positive-time estimate

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
ansatz chat0005, thread `01a178fa-8a72-7f23-9a7f-47e284eab9a3`.

**Disposition: accept at the bounded requested scope; proved in-note
from named inputs, same-model internal assessment only.** [Note17][note]
executes [AN01 r1][packet]. The local remainder, global contour budget
and residual were separately derived in parallel analytical subtasks;
the assembled note received focused same-model rereadings in those
three areas. This is not independent specialist or cross-model validation.
The parent Note30--31 and their assessments remain shared inputs.
No numerical, machine-symbolic, exact-arithmetic or sampling campaign
was performed, and no numerical onset is certified.

## Evidence checked and quantitative gain

With X=|x|, R=2+t+X, L=log R, N=1+X+tL, the model is
P2=sum S(1+C2) using exactly Note30's two selected implicit full-gamma
saddles, canonical xi/8 normalization and B^{-1/2} branch.
The correction coefficients1/32 and5/192 agree with independent
finite Gaussian-moment algebra. The formal recurrence P6--P7 needs
no correction; no convergent formal infinite series is assumed.

The complete field error is bounded by the unchanged positive carrier
sum times
\[
C\{e_4+R^{-t\log2/8}+R^{b_0}e^{-ctL^2}\},\qquad
e_4=t^3/N^5+t^4/N^6+t^5/N^7+t^6/N^8.
\]
This closes the proposed local next-order rate and leaves each nonlocal
payment visible until its eventual absorption is proved. For a symbolic
sufficient t_* and every real x, the complete envelope error is
O(t^{-2}log^{-5}t). The improvement over Note30's t^{3/2}/N² bound
is uniform, by the ratio O(t^{3/2}/N³)<=O(t^{-3/2}log^{-3}t).
This is a gain in a proved bound, not a measurement of actual error.

## Local parity and all noncentral pieces

LT17--18 use Taylor's integral remainder through degree5 in the
local exponent and through cubic order in its exponential. The
weighted remainder is a Gaussian times the four monomials
u^6/m^5,u^8/m^6,u^10/m^7,u^12/m^8. Both exponentials, including
that in the exponential remainder's max factor, have paid Gaussian
majorants. No smallness of the cubic remainder over an infinite ray
is assumed.

The odd terms cancel only on the genuine symmetric horizontal
subsegment [-a/2,a/2], where a=Re(p-w). The full contour is asymmetric.
Only a finite even polynomial times a Gaussian is extended to the full
line for moment evaluation; its tails are separately bounded. The actual
right infinite ray, remaining left segment, both connectors, original
middle and reflected infinite end retain their own payments. This
avoids a parity assertion on a contour where it would be false.

LT20--24 retain exact reflection, xi/8=M zeta and the entire ordinary
Dirichlet tail n>=2 in Re>=2. Neither a zeta pole nor a gamma
singularity is crossed. The far vertical face vanishes after finite
closure, and the eventual uniform tail follows from the explicit
Gaussian estimate. The bounded-height middle uses compactness,
not large-height Stirling at zero. The connector at zero height
collapses without a singular estimate.

## The rejected absorption shortcut and supported onset

The old t>=32 absorption used only an arithmetic power greater than2.
It cannot be copied at the new X^{-5} local scale: the inherited
R^{-t log2/8} bound has power below5 for some allowed fixed t.
This rejects that estimating shortcut, not the actual arithmetic
remainder or the canonical model on that domain.

LT12 chooses kappa t>=6, kappa=log2/8, together with a single
symbolic L0 paying branch contraction, fixed sectors, Gaussian rates,
noncentral exponent losses, analytic disks and both absorption
inequalities. The sufficient choice t_*>=max(32,48/log2,exp L0)
therefore covers all real heights. This is not an instantiated onset
at48/log2 or a statement about the physical regulator switch near64.
The full three-part bound remains valid for t>=32 and sufficiently
large R without the invalid absorption.

## Derivatives, direct time and actual residual

LT25--28 compute the actual residual algebraically. Holding p fixed,
C2_t=k exactly, where the leading-arm residual is -kS. The remaining
corrected-arm residual is
\[
S\{-kC_2-C_{2,pp}/(4B^2)-t\alpha''C_{2,p}/(4B^3)\}.
\]
All five expanded coefficients and signs in LT28 were rechecked by
ordinary differentiation; its allowance is exactly delta2=e4/t.
The corrected model is not an exact heat solution. This residual is
not used to propagate arbitrary data or to replace a field comparison.

For spatial j<=3, Cauchy's formula applies to the holomorphic complete
difference on full buffered disks of radius c/L. The carrier is
comparable on each disk, giving the stated L^j loss and uniform
O(t^{-2}log^{j-5}t) normalized suprema. No derivative of an
uncontrolled real-axis O statement is taken.

The original fixed-contour convolution supplies H_t=-H_zz directly,
by kernel differentiation and two justified integrations by parts.
Then (H-P2)_t=-(H-P2)_zz-Res(P2) gives the direct first-time bound
O(t^{-2}log^{-3}t); the residual is O(t^{-3}log^{-5}t). Artificial
moving contour/localization endpoints are absent in this operation.
A time-kernel multiplier would destroy some local odd cancellations;
the note explicitly avoids pretending otherwise and instead uses the
exact comparison identity with the independently computed residual.

## Scope, controls and remaining work

The proof uses no RH, initial all-real-zero assumption, selected root
data or assumed Lambda value. The controls12 premise screen names
which canonical-source/arithmetic identities each control lacks.
The generic recurrence/Cauchy/heat mechanisms themselves exclude no
control. As required by [avoid01][a01] and [avoid07][a07], this is a
quantitative approximation result, not an RH reformulation, a zero
exclusion theorem or a universal obstruction to other methods.
Read [the result index][results] and [avoid index][avoid], especially
[complete payments][a12] and [same-model limits][a05].

The fixed-height and all-height conclusions are separately stated;
the three X versus t log R balances have the expected correction,
field, time and residual rates. In all of them the first term of e4
dominates the allowance, with successive ratios O(1/L). This is not
an asymptotic equivalent of the signed two-arm field error.

**AN01 r1 CLOSED; LT-01 audited and LT-02 complete at this bounded
scope.** HDA-A04 remains Partial as a hierarchy program. No physical
observable transfer, regulator64 refinement, small-positive or through-zero
bridge, higher-order theorem, manuscript revision, numerical onset or
independent specialist review is supplied. Existing packets/results
for those subjects remain unchanged.

**Next owner: Analysis — Sol.** Prepare a bounded LT-03 fixed-order
request that specifies finite Taylor/sector/moment constants, the
arithmetic floor, full buffers and residual at that order; do not
infer order-uniform constants or start growing-order work from AN01.
This is a next deliverable, not a dispatch or automatic execution.

[note]: ../notes/17_FIRST_CORRECTED_LARGE_POSITIVE_TIME_20261026.md
[packet]: ../research-progress/handoffs/HDA-A04-AN01.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a05]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
