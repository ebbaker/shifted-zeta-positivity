# B02 line-logarithm proof-author check

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Exact backend identifier and reasoning
effort unavailable. **Same author and premises; not independent review.**

Scope: [Note04](../notes/04_TND_OG_B02_ONE_SIDED_BOUNDARY_LOG_ACQUISITION_20261108.md)
sections 1–3 and its B decision. Section 4's complete assembly is explicitly
an [E03 target](../research-progress/handoffs/09_TND_OG_E03_SIGNED_LOG_ACQUISITION_REQUEST_20261108.md),
not a theorem accepted by this check.

| Claim | Check and boundary |
| --- | --- |
| Disk and segment geometry | R0/rho=27/26; (rho+r0)/(rho-r0)=51; B=26/3. A real length-one segment below v+4i has maximum radius sqrt(65)/2<25/6. |
| Jensen count and factor removal | k counts every multiplicity inside the open rho disk; k<=n. Finite Blaschke factors are unit modulus on the outer circle. The quotient is zero-free only inside rho, exactly where Harnack is applied. Residual boundary zeros use an inner-radius limit. |
| Line estimate | A disk of radius b meets a horizontal line in length at most 2b. This replaces the sibling's area calculation; the area exponent is never used for a trace. For q<1 and k<=n, q^(1/k)<=q^(1/n); q>=1 is covered by the segment length. |
| Envelope sign | abs(f)<=abs(g)+epsilon<=abs(f)+2epsilon. Thus the pointwise upper log is valid without a lower real-boundary modulus or a nonvanishing approximant. |
| Integration constants | Splitting the exact kernel h/[t(t+h)] at h gives n and n/(n-1), whose sum is n^2/(n-1). n>=2 is necessary for this proof and deliberately imposed. Tonelli and the sublevel estimate pay logarithmic integrability. |
| Local absolute-log bound | abs(log abs(Mf))<=log M+log^-abs(f). Layer-cake gives Cn. This is a line bound, not an invented pointwise lower modulus. |
| Canonical pole and domain | Re(s)>=1/4 on every outer disk. The fractional-part representation cancels s=1; s=0 stays outside. The upper bound 2abs(v)+25 and safe anchor c0 hold for every real v. |
| Scaling | Dividing by M_v sends the field error to delta/M_v and the additive envelope to abs(g)+delta/M_v; logarithmic constants cancel exactly in (16). |
| Height and precision | A_v/n_v<=kappa bounds the exponential factor. n_v=O(log(2+abs(v))), so the power tends to zero with height. Equation (18) is sufficient local precision, not an efficient algorithm. |
| Double-zero check | Scaling and one real integration by parts give 2pi sqrt(delta). It verifies no fixed floor and warns against claiming Lipschitz behavior; it is not a theta control. |
| Green consumer boundary | Equations (20)–(21) are E03 targets. Exact prime baseline has one plus G(X,1) term. T and beta each require a factor two in an upper-approximation gap. The favorable value is still unpaid. |

**Disposition:** the written local proof passes this same-author check;
the finite-source/full-tail assembly is ready for ordinary execution,
not already assessed. No code, numerical constants or tests were run.
No theorem is promoted to an independently reviewed result.

The controls in Note04 are a premise screen, not validation by collision
counts. The selected route avoids the hypotheses of the *specific*
quadratic and zero-free harmonic recipes; this does not prove its canonical
value favorable. Generic defective fields remain defective under accurate
log acquisition. The source's literal arithmetic selects the field, while
the local analytic lemma alone selects no sign.

Keep the [target](../../../../../../avoid/01_restating_the_target.md),
[scope](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[shared-premise](../../../../../../avoid/05_same_model_reviews_and_shared_premises.md)
and [unchecked-import](../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md)
distinctions. No investigation closure or manuscript milestone occurred;
shared result-summary promotion is deferred to a later assessed assembly.
