# E02 r1: claim-level assessment of the opening comparison

7 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. **Actual exact backend model/effort:
unavailable in the exposed session metadata.** The task recommends
Sol6.1/ultra; that is not asserted as an observed configuration. This is a
new-session internal LLM assessment, with three read-only inherited-model
scope checks and one root writer. It is not specialist or verified
cross-model review. The original proof author recorded Astra/max.

**Disposition: ACCEPT AFTER ONE BOUNDED HYPOTHESIS CORRECTION.**
Note01's count corollary requires supp w contained in [-1,1] and a positive
window width. These are now explicit. All its finite identities remain
valid for arbitrary compact support. Note02's mathematical claims and
constants are accepted without alteration; it already restricts w.

Sources: the immutable [E02 request r1](../research-progress/handoffs/02_TND_OC_E02_REQUEST_20261107.md),
[inputs02](../research-progress/handoffs/02_TND_OC_E02_INPUTS_20261107.json),
[E01 request](../research-progress/handoffs/01_TND_OC_E01_REQUEST_20261107.md),
[return01](../research-progress/handoffs/01_TND_OC_E01_RETURN_20261107.json),
Notes01--02, inherited canonical source/transverse sections and
[source receipts](../references/02_TND_OC_E02_SOURCE_USE_20261107.md).
All **9 primary and 19 inherited** input records matched their frozen
byte sizes and SHA-256 hashes before review. Hashes identify inputs;
they do not validate their claims. Author check01 was read as a claim
map and was not used as a proof premise. Issued requests, input manifests
and the historical E01 return remain byte-identical.

## Claim dispositions

| Claim and location | Disposition and independent check |
| --- | --- |
| Note01(1)--(3), odd moments and quadratic pairs | **Accept.** Conjugation cancels odd powers at each x before integration. A self-pair has zero difference, and even chi interchanges the square terms. Thus S2=2 integral (chi*q0)dq2, and chi=1 gives 2NQ. |
| Note01(4)--(6), multiplicities and all even orders | **Accept.** Two ordered conjugate directions give 8m^2w0^2d^2 and, at order 2k, 2^(2k+1)m^2w0^2d^(2k). Odd terms in the binomial expansion vanish. In the unit strip, absolute differences are at most two, proving (6). Geometrically coincident multiplicity copies have not been wrongly deleted. |
| Note01(7)--(9), deterministic configuration | **Accept.** Finite logarithmic differentiation gives Newton's recurrence with the displayed alternating signs. Concavity on [0,1] and log(1+t)<=t give log(1+eta)Q<=log Z<=eta Q. No ensemble or Fredholm formula is required. |
| Note01(10)--(11), factorial order | **Accept.** Expanding Q^k retains all distinct-index terms k!e_k. The tail is at most e^t*t^k/k!, k=K+1. The two conditions k>=2et and k>=(t+log(1/epsilon))/log2 pay both factors. t=0 is exact. |
| Count corollary after Note01(11) | **Correct, then accept.** The stated population cover was missing supp w contained in [-1,1]; h>0 is also now explicit. Parent unit counts include multiplicity and closed endpoints. A cover with at most ceil(2h)+1 unit intervals yields the unchanged allowance under that local support condition. The inherited absolute constant is not numerically evaluated. |
| Note01(12)--(13), log series and averages | **Accept.** The scalar series is used only within q=abs(eta)max a_j<1, with tail denominator 1-q. The change of variables in center averages retains h/T; the pair expression is its mutual contribution, not the full density-amplified total. |
| Note02(1)--(7), Jensen/Blaschke/Harnack | **Accept.** R/rho=27/26 and (rho+r)/(rho-r)=51. The quotient removes only inner zeros, stays bounded by one on the R-disk and has no zero inside rho. Its center modulus is at least m. The interior-radius Harnack limit handles zeros on the rho-circle. |
| Note02(8)--(9), sublevel area | **Accept.** For q<1 and 1<=k<=n, k*q^(2/k)<=n*q^(2/n). For k=0 the set is empty in this regime. For q>=1 the bound dominates the whole disk. Layer cake gives precisely n/2; multiplicities are retained in k. |
| Note02(3)--(4), comparison split | **Accept.** At tau=epsilon^(n/(n+2)), the high-modulus cost is pi*r^2*epsilon/tau. On the complementary set both moduli are below 2tau. Two applications of (9) give the second term in C_n, with the same exponent 2/(n+2). |
| Note02(10)--(15), canonical geometry and anchor | **Accept from stated canonical inputs.** Xi reflection and H0=xi(s)/8 give the factor16 in D. The disk has Re s in [1/4,19/4], so D has no zero/pole nearby. The fractional-part identity gives 1+(X/2+6)/(1/4)=2X+25. At sigma=5/2 the Euler-product lower bound is zeta(5)/zeta(5/2), multiplied by at least 3/5. |
| Note02(16)--(18), both normalized fields | **Accept.** Fhat has upper modulus <=M_X-1+delta<=M_X and center modulus >=c0/2. The common scale cancels in the log difference. A_X/n_X<=log(27/26) bounds the exponential factor, so C_X=O(log^2 X) and alpha_X is of order 1/log X. No height-uniform positive exponent is asserted. |
| Note02(19)--(25), weak tests and zero formula | **Accept.** The support buffer is positive because sqrt(17)<25/6. The value and first normal derivative vanish at y=0; no line delta appears. Mollification preserves bounded weak Laplacians and converges almost everywhere there; local log integrability and locally finite zero mass give (20). Factor two counts conjugate halves. Approximate zeros in 1<y<2 keep their weights. |
| Note02(26)--(30), complete arithmetic/radial tails | **Accept.** The canonical half-line cosine integral has no extra factor two. Omitted arithmetic terms cost 5C2(J)I_b, the complete radial tail costs B0*I_b^(>U), and abs(cos zu)<=exp(bu) for b=17/2. Consecutive arithmetic terms have ratio <=16exp(-pi(2J+3))<1 even at J=0. |
| Note02(31), gamma parameter | **Accept.** v=pi exp(4u) produces (1/4)pi^(-19/8)v^(27/8)exp(-v)dv, hence upper incomplete gamma parameter35/8. |
| Note02(32)--(34), enlarged-disk conversion | **Accept.** The reciprocal-gamma product yields abs(1/Gamma(w))<=abs(w)exp(gamma Re w+pi^2 abs(w)^2/12). Setting w=s/2 gives prefactor8/abs(s)<=32 and exponent pi^2(361+4V_X^2)/768, with the exact stated pi factor. This expensive bound is compact and height-dependent. |
| Note02(35)--(38), termination and consumer | **Accept.** Both independent tails tend to zero. Choosing them after the parameters to give delta<=delta_* yields E_phi<=e/2. A plateau pair forces Q>=2d^2 or log Z>=2log(1+eta d^2). The strict comparison excludes only the declared plateau/defect class. eta=0 has exact zero response. |
| Claimed scope and controls | **Accept with the stated limits.** The construction approximates the canonical complete field without giving the finite source an all-real-zero property, preserving all approximate collar zeros. It supplies no small signed statistic, practical-cost result, through-zero HDA extension, determinantal law, new Green bound or canonical exclusion. |

## Bounded correction pass and recheck

The allowed correction pass adds h>0 in Note01 section1 and the local
support restriction immediately before its count corollary. Earlier
finite algebra is explicitly left in the wider compact-support class.
No source, field, observable, time regime, exponent, constant or theorem
route changes. Note02 receives only a status amendment. [Note03](../notes/03_TND_OC_E02_VERIFIED_CONSUMER_20261107.md)
records the repaired cover and exact usable consumer. The post-correction
read-only check accepts this repair; final identities are bound in
[return02](../research-progress/handoffs/02_TND_OC_E02_RETURN_20261107.json).

No second repair, numerical sweep, new kernel or signed proof was needed
or attempted. The defective wide-support count wording is not promoted
to a negative result about localized statistics generally.

## Shared inherited premises and downstream boundary

The canonical source/xi normalization, conjugation and strip bound,
and the absolute unit-count estimate remain inherited canonical inputs.
Their point-of-use formulas were cross-checked; this is not a new full
proof audit of Polymath, the parent investigation, or every HDA note.
Jensen, Harnack, smoothed Jensen and the reciprocal-gamma product were
reopened in their primary online sources. The C^(1,1) extension and
quantitative constants are recalculated here. The HDA theorem is used
only to respect its negative-Newman-time domain, never at zero.

**First unpaid clause within E02 after correction: none found.**
**First unpaid downstream clause:** an independently tractable canonical
upper estimate on Qhat or Lhat below Note02(38)'s remaining defect margin.
Future numerical evaluation would separately owe observable integration
and rounding error; current values are exact integrable expressions.

[Controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md)
remain compatible with generic algebra and log stability. Note01 section5
names the literal canonical coefficient/normalization/conductor premises
their respective families fail; none is claimed excluded by the present
identities. See [avoid01](../../../../../../avoid/01_restating_the_target.md),
[avoid02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[avoid05](../../../../../../avoid/05_same_model_reviews_and_shared_premises.md),
and [avoid07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
No root summary, parent register or Green register was changed.

**Next: [B] TND-OC-B02 — Astra**, choose a signed source-sensitive comparison
or preserve a scoped failure. E02 completion does not create a ready
numerical or exclusion task.
