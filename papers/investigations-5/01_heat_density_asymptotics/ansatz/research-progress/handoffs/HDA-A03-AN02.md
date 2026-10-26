# HDA-A03-AN02 r1 — fixed P4 physical tuple through the switch

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, base chat0025, thread `01a179ab-8856-7ba0-89a2-500b2d854c80`.
Parent HDA-A03; **next owner: Analysis — Sol**. The sole live execution
record is ansatz Progress02; positive Progress03 LT-06 routes here.
**Frozen request r1; READY_FOR_SOL, prepared and not executed.**

## Read first, inputs and permitted outputs

Follow root AGENTS.md, GPT_RESEARCH_MODEL_WORKFLOW.md, LARGE_FILES.md and
tools/CHAT_HISTORY.md. Read result-summaries/README.md, avoid/README.md,
clusters11--12 and avoid01/02/07/12/19/20. Read the actual working-tree
versions of Ansatz Notes18--20 and Note22/Assessment16; parent
Notes19--20,28,30--31,42 and58--61, including the general full-tuple
definitions in Note42 and Note59's inventory. The opening record for
this request is [Inputs22](../../notes/22_NAMED_SWITCH_CENTERS_INPUTS_20261026.json),
with the additional physical sources separately pinned in
[Consumer inputs](../../notes/22_CORRECTED_PHYSICAL_CONSUMER_INPUTS_20261026.json).
Execution must re-pin actual inputs before opening ANALYSIS.

Write research in ansatz/notes/, assessment in ansatz/reviews/, and
small input/work records in ansatz/numerics/ as needed. Append a return
and disposition here; update Progress02 and its overviews, with LT-06
a pointer only. Coordinate any manuscript edit with the current
production owner and re-read its changed source. Preserve unique chat
registrations; do not relocate base chat0025 to the ansatz archive.

## Frozen domain, model and gain

Fix ell,h,eta>0, 63<=t<=65, X=|x|>=X0, physical |y|<=1, with
r=ell+2, b=1+h+2 and one further analytic unit. Keep the full canonical
H, H_t=-H_zz, H(0,z)=xi((1+iz)/2)/8. Retain exact physical
q=epsilon_g² of parent Note20, fixed K=k_ell k_h, unnormalized
observables, original potential offsets and actual signed covariance.
Use exactly the compact model

\[
P_4(t,z)=\sum_{w=s,1-s}S_t(w)(1+C_2+C_4)(t,w),
\quad s=(1+iz)/2,
\]

with Note19's chosen saddle branch and finite coefficients. There is
no optional F1 splice in this request. Set e=X^-7, Lambda=1+logX.
The *input* is compact Note20 RB5: field/jets0--3 at
C A Lambda^d e; direct first time at C A Lambda²e; and exact residual

\[
E_4=(\partial_t+\partial_{zz})P_4
       =-\sum_{w=s,1-s}S_t(w)\mathscr Q C_4(t,w),
\quad |E_4|\le C A e,
\]

where mathscr Q is Note19 FO23 and the exact identity is FO30.
This is the actual compact theorem, not t=64 inserted into an unknown
eventual onset. A is a positive arm envelope, never |P4| or |H|.

The **requested output rates, not established results**, are absolute
differences between the actual observables of H and P4:

| Outputs | Spatial multi-index orders | Requested bound |
| --- | --- | --- |
| U,W | <=4 | C e |
| R, K*C_reg | <=2 | C e |
| J, actual Q, including Delta Q | <=2 | C e Lambda² |
| J needed internally for source balance | <=3 | C e Lambda² |
| U_t,W_t,R_t,K*(C_reg)_t,K*(b_reg w),K*mathcal S | <=2 | C e X Lambda² = C X^-6 Lambda² |
| Retained heat-potential, current/density equation residual corrections | orders needed by the equations, total kernel order <=4 | C e |

Here all symbols are the original physical definitions of parent
Note31 PE3--5, with b_reg=r_t+(r_xx+r_x²)/2, r=log q; b_reg is
distinct from the transverse buffer b and gamma determinant B.
For example Q=K*(S_x²-S_y²)-(U_x²-U_y²) is the actual covariance.
Compared with the inherited PE44 theorem these targets improve the
main output rates by five height powers and the old X^-3 residual
corrections by four powers. Proving these rows, or locating their
first precise unpaid estimate, is the measurable decision.

## Required payments

1. **Corrected phase, collars and units.** Prove both P4 arms nonzero,
   their corrected phase omega4 comparable to Lambda, bounded amplitude
   logarithmic derivative and bounded current residues on the full
   buffers. Acquire every intersecting simple collar and enlarged disk,
   exterior carrier-sum floor, root displacement O(e/omega4), residue
   difference O(e omega4), and regular-part difference O(e omega4²).
   Establish analytic-unit difference O(e) by removable-singularity and
   maximum-principle arguments. The leading S-model collars alone do
   not prove these facts for the corrected P4 model.
2. **Weak pole and residual transfer.** Reprove the corrected analogues
   of Note28 JT14--18a and Note31 PE13--17, including
   ||delta S||_1+||delta w||_1<=Ce,
   ||delta V_m||_1<=Ce Lambda² and ||Z_m||_1<=Ce for m=0,1,2.
   Keep the logarithmic translation payment
   e(1+|log e|)=O(e Lambda). Avoid an inverse minimum regulator floor.
   Use the exact E4 separately from the direct field-time estimate.
3. **Actual flat switch and derivatives.** Retain r=a(t)-beta(t)x²,
   beta=chi_reg/kappa, and the exact chi_reg. Keep r_x=-2beta x,
   r_xx=-2beta, r_t=a'-beta'x², r_xt=-2beta'x and r_xxt=-2beta'.
   Likewise q_t=q r_t, q_x=q r_x,
   q_xx=q(r_xx+r_x²), q_xt=q(r_xt+r_x r_t).
   For beta X<=B0 (fixed sufficiently large threshold), prove spatial
   coefficient bounds and |r_t|+|b_reg|<=C X Lambda²,
   |r_xt|<=C Lambda², |r_xxt|<=C Lambda²/X. For beta X>B0,
   prove epsilon_g/A4<=C exp(-cX) on the whole support and pay every
   polynomial regulator coefficient using individual weighted-pole
   estimates. These are estimate regimes, not field partitions.
4. **Actual means, covariance and time/source identities.** Use signed
   Note31 PE28 before absolute values. Subtract the actual full filtered
   mean products, prove the needed mean derivatives through three are
   O(Lambda), and retain their O(e Lambda) product-difference payment.
   Pay both curvature derivatives, direct R_t, actual signed source,
   E4 and its weak density correction. No fifth kernel derivative is
   permitted: the fixed k has bounded weak fourth derivative only.
5. **Full tuple inventory.** Under this unjoined holomorphic P4 model
   the compatibility variable partial_bar P4 is exactly zero; the
   general-tuple T_C,(T_C)_t,T_J,Xi,D_B vanish for that stated reason.
   C_tot=C_reg. T_U=2Re Z0 and D_E remain and must be paid in their
   actual signed weak form. There is no spatial, moving or temporal
   field join here. Any proof-local test partition must nevertheless
   retain its derivative terms. State which general tuple components
   are nonzero, compared, or identically zero before claiming closure.

Routine analytical choices, fixed finite constants/onset gates and
same-source comparisons are delegated to Sol. No numerical research is
needed or authorized by this analytical packet. Hashes and file checks
are housekeeping. A numerical request, if later useful, needs its own
finite question, arithmetic, work cap and stop condition.

## Acceptance, scope and stop

Accept only after all declared rows and exact defects have written
proofs with complete buffers, constants/onset dependencies, direct-time
and residual distinctions, regulator terms, means and source budgets.
Alternatively stop at one named unpaid estimate, record its attempted
bound and affected rows, and leave those rows Open. Do not silently
weaken requested rates or hide a field gain below an unpaid consumer.

Do not extend the time interval, change q/K, insert a coarse time splice,
claim a new simplified-layer accuracy from improved centering, infer an
evaluator height-cost theorem, or claim all-time/RH closure. Parent
JT24's O(1) absolute and JT33's O(1/logX) normalized layer statuses
remain. Keep HDA-A03 Partial until the broader stated obligations are
actually met; parent HDA-17 Partial, HDA-18 Gated, HDA-20 unfulfilled.
Name the complete canonical source/arithmetic premises missing in the
collision controls; a generic local pole lemma rejects none by itself.

## Return and disposition

Pending. This packet freezes a concrete corrected physical consumer
after A03-AN01, as requested by base Note64. It supplies no new physical
estimate. **Analysis — Sol** is the default next owner; no resistant
mechanism requiring an Astra handoff has yet been identified.


## RETURN — r1, 26 October 2026, base chat0025

**gpt-6.1-sol (Codex), actual recorded effort ultra**, same thread
`01a179ab-8856-7ba0-89a2-500b2d854c80`, turn
`01a179ec-1178-7b91-a108-042fe3108232`. The author explicitly requested
execution. [Inputs23](../../notes/23_FIXED_P4_PHYSICAL_TUPLE_INPUTS_20261026.json)
re-pins actual versions; all prepared source hashes matched.

[Note23](../../notes/23_FIXED_P4_PHYSICAL_TUPLE_20261026.md) proves every
frozen requested rate on[63,65], X>=X0, fixed complete buffers and exact
q/K. PT4--10 acquires corrected phase/collars/units/poles and regulator-
uniform L1 consumers; PT11--18 pays exact flat-switch coefficients and
direct time/curvature; PT19--22 pays current, full actual covariance,
actual signed source and residual corrections. PT23 and the order
inventory retain all equations/defects with at most K4. No requested
row remains unpaid. Constants and onset are finite but uninstantiated.

The completed main bounds are static X^-7, current/covariance
X^-7 Lambda², time/source X^-6 Lambda² and residual corrections X^-7,
with the exact derivative orders in the frozen table. The named center,
simple-layer law, canonical source, physical q/K and model are unchanged.
No numerical/symbolic campaign or manuscript edit was performed.

[Assessment17](../../reviews/17_FIXED_P4_PHYSICAL_TUPLE_ASSESSMENT_20261026.md)
records same-model checks and one repaired onset-summary quantifier;
the beta X<=B0 estimate regime was not imposed globally. The
[work record](../../numerics/A03_AN02_ANALYTICAL_WORK_RECORD_20261026.json)
binds outputs and original request/source preservation. These are
internal analytical checks, not independent specialist validation.

## DISPOSITION — Analysis, Sol, 26 October 2026

**AN02 r1 Complete/CLOSED at its frozen high-height physical scope.**
This supersedes the pending checkpoint and READY notice, not the frozen
request. HDA-A03 remains Partial for wider sharper-layer/core/assembly
work; LT-06 points to this completed bounded consumer. Parent HDA-17
Partial, HDA-18 Gated and HDA-20 unfulfilled remain. Uniform evaluator
height cost and the independent full-chain audit are not supplied.

Next **Analysis — Sol**, existing [A08-AN01 r1](HDA-A08-AN01.md),
prepared READY_FOR_SOL in Progress02, first small-positive slab[1/2,1].

> Execute HDA-A08-AN01 r1. Prove its canonical comparison on[1/2,1]
> with full buffers, spatial0--3, direct first time and actual residual,
> or identify the first precise unpaid estimate. Preserve source/q/K.

The same public conversation remains uniquely base chat0025; routine
refresh and exact-turn final capture use its original identity. This
research return makes no manuscript-build or specialist-review claim.
