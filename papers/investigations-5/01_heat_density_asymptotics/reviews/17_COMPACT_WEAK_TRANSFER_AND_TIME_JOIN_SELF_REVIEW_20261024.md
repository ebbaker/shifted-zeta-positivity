# Compact weak transfer and time join: same-assistant review

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort xhigh**,
verified from session metadata; chat 0010.

This is the author's assistant rereading its own [Note 34][note], not a
distinct-reviewer audit or HDA-20. No numerical, machine-symbolic or
exact-arithmetic execution was performed. Disposition: **compact transfer
and local time-joining estimates proved in-note; same-assistant review
only**. No instantiated cost, accepted finite core or global assembly.

## Checks that matter for the new estimate

1. **What two source orders mean.** The data are errors in F and F_zz,
   not the claim that F_z or F_zzz need not exist. The fields are analytic
   on the whole buffer. Weak spatial identities move their derivatives
   onto a fixed kernel. Pointwise density-time formulas still need F_zzz.
   The new norm includes only filtered quantities and their specified
   derivatives. Shrinking or moving the kernel would change the costs.
2. **Frozen constants.** CJ4 uses declared error caps before selecting
   mesh accuracy. P_2 and the mean-gradient majorants are fixed over those
   caps. Thus CJ20 really is linear in d_0,d_2,eta_E. The cap must be
   checked on every tile; changing it requires recomputing the table.
   The useful local amplitude denominator is retained. Its global fallback
   can be extremely expensive when the compact regulator floor is small.
3. **Curvature cancellation and time derivatives.** Subtracting the weak
   density identity from Delta S/(4pi) cancels the S term in C. Its time
   derivative has all four coefficient groups: grad r, grad r_t, Delta r,
   Delta r_t, plus the two terms from differentiating c_F|grad r|^2.
   CJ9 retains the last coefficient as T_h. CJ11 follows from the exact
   field equation and the 1-Lipschitz cubic on [0,1], not differentiating
   an allowance. The residual signs are + for S_t and - for w_t.
4. **Kernel orders.** R and R_t through spatial order two use fourth
   kernel derivatives. J through third order also uses four; that third
   order is needed internally for source derivatives through two.
   Q through two uses square K_alpha (order four) and U derivatives
   through three. The compact C3 kernel has integrable weak fourth
   derivatives with no boundary delta; no fifth derivative is invoked.
5. **Actual covariance.** CJ16 is a spatial identity before convolution.
   It keeps the signed gradient-square combination. CJ13 then pays the
   difference of the actual squared means using the full multi-index
   Leibniz sum. A convex blend of component covariances is not used.
6. **Residual and signed source.** Varying the weak identity with delta F=E
   holds q fixed, giving coefficients 2,-4,-2 in CJ18. Inserting the common
   bound z for Z_0,Z_1,Z_2 gives the factor 3R_1^2, rather than dropping Z_2.
   The actual signed source is defined before using current balance to
   estimate it. This removes an E_z input from the filtered estimate;
   it does not assert an E_z pointwise bound.
7. **Joining cost.** CJ23 contains the component residuals and
   theta'(F_2-F_1). The latter is bounded by field differences through H,
   not by already averaged observable errors. The local joined field
   remains holomorphic, so its actual tuple has compatible equations with
   the explicitly retained residual. There is no PDE stability argument.
8. **Cover and remaining failure.** The outer thresholds are uniform only
   after choosing the two fixed time slabs. PE44's onset/constants are
   still uninstantiated. A common finite source is compared only on the
   compact buffered core; its known positive-cutoff outer obstruction
   remains. CJ28 identifies the nonzero bar derivative from an uncorrected
   spatial field cutoff. The note neither repairs that term nor rules out
   other spatial constructions. HDA-18 therefore stays Gated.

## Hand controls and limits

For F=z and spatially constant q, V_m=0 and j=0; CJ16 gives the required
signed cancellation `S_x^2-S_y^2=-square S`. If F=z-a(t), its algebraic
current still vanishes, while E=-a' and CJ18 supplies the translating
density. A time blend of z and z-c is precisely this latter control with
a=c theta(t): omitting theta' would incorrectly give a static density.
For F=z^2-2t, E=0 and the formulas remain smooth at the double event for
q>0. These are direct hand substitutions, not evidence of a theta
collision exclusion. Changed-source controls can satisfy the generic
local theorem with their own constants; the canonical source constants
are not inherited automatically.

CJ21 is a sufficient source budget, not a measured feasible cost. Reducing
input orders can be offset by large kernel derivative norms or reciprocal
regulator factors. The [Sol request][packet] must preserve a losing
comparison. Finite sample success cannot accept a continuous core or
instantiate an eventual endpoint theorem. The same-assistant dependencies
in Notes 25/26/30/31 are not independently revalidated by this review.

## Disposition and routing

HDA-17: **Partial — compact analytical contract; no accepted finite core**.
HDA-18: **Gated**, with a proved symbolic compact time-join estimate and
unpaid spatial assembly/effective cost. HDA-20: unchanged. The manuscript
is unchanged and no numerical result is claimed.

The author's revised [workflow][workflow] makes routine coefficient work,
implementation, diagnostics and routine disposition Sol's responsibility.
The concrete next assignment is **Analysis and numerics — Sol**, packet
HDA-17-AN01 r1. Reserve Astra for the genuinely difficult spatial
compatibility or a comparably hard issue identified by Sol's evidence.

[note]: ../notes/34_COMPACT_WEAK_TRANSFER_AND_TIME_JOIN_20261024.md
[packet]: ../research-progress/handoffs/HDA-17-AN01.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
