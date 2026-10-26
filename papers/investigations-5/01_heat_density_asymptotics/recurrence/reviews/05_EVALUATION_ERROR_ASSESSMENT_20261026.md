# Internal assessment: coefficient, rounding and retained RS quadrature

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, actual **gpt-6.1-sol (Codex), ultra**, verified
from the exact turn metadata. Recurrence chat0001, thread
`01a17690-2e5f-77b1-a3a4-9c31f72c117d`.

**Reviewed:** [Note06](../notes/06_COEFFICIENT_ROUNDING_AND_RS_QUADRATURE_20261026.md),
HDA-R05-AN02 r1; final file identity is recorded in the
[work record](../notes/06_EVALUATION_ERROR_WORK_RECORD_20261026.json).
This is a **same-model internal analytical assessment**, including three
read-only parallel checks of coefficient/rounding, quadrature/geometry
and source/RS-coefficient arguments. It is not independent specialist
validation, a verified implementation or a numerical certificate.

**Verdict:** accept the proved deterministic bounds and the conditional
accuracy specification on the stated full buffers, p=floor(L/2),K=2p,
1<=T<=2, with every arithmetic mode and the bounded RS integral retained.
The conditional total outer-envelope error is <=e^-L²/4 after the common
onset and all finite input/geometry/rounding inequalities are met. Close
the bounded audit; leave broad R05 **Partial** at the provider/evaluator
certification step.

The decisive checks and limits are:

| Item | Check and assessment |
| --- | --- |
| Target conversion and allocation, E4--5 | The center-normalized evaluation budget is c_o/(2C_chi) e^-3L²/8. Half the outer target is reserved for Note05 truncation by its enlarged onset. Five evaluation allowances of epsilon_X/20, multiplied by at most2, plus scale error epsilon_X/2 fit epsilon_X exactly. |
| All-mode coefficient conditioning, E6--11 | The finite coefficient derivative identity gives a positive, explicit condition sum. Changing beta first avoids using the unperturbed polynomial majorant for perturbed coefficients. The slope neighborhood pays real Gaussian sensitivity without a spurious e^+L² carrier loss. The full X^1/4 population, moment degrees and large phase costs remain. A0 now uses 2V B_loc, an explicit full integrand bound, rather than an unnamed constant. |
| RS regularity, E12--17 | Apparent half-integer poles are removable in the same complex normalization. Weighted e_j^k=(3k-2j)!d_j^k gives the stated interior/positive-even endpoint recurrence. Its positive majorant 8^k(k!)² and the rectangle Cauchy bounds yield the displayed D_k with O(Klog K) logarithmic cost. Only the specified exact identities are imported. |
| Analytic outer quadrature, E18--21 | Fixed real branches have a finite holomorphic extension via A(u)+conjugate(A(conjugate u)); no complex RS remainder theorem is inferred. The actual complex-kernel and direct-time ellipse costs remain. Positivity and degree2n-1 exactness of Gauss rules, plus the derived Chebyshev remainder, give 16V B_E4^-n and n=O(L²) per branch, at most two branches. |
| RS data and geometry, E22--25 | The product-sum data error, real shifted nodes, fixed branch labels, weight errors and omitted boundary strips inside the fixed branches are separately paid. Rules extending outside the original window require a new length/ellipse allocation. Local strip bounds have logarithmic cost O(L+Klog K), preventing the large ellipse bound from inflating the real-node precision leading term. Explicit V>=3, epsilon_u<=1/4 and epsilon_b<=1/4 guards keep displacements in the proved neighborhoods. |
| Pole-safe coefficient provider option, E26--28 | The contour-to-chi distance is >=1/4, quotient denominator >=1, and the explicit numerator bound is valid. The four-edge Gauss error includes total contour length12 and 1/(2pi), yielding 24/pi. Normalized jets cancel the factorials in the weighted coefficient sum. Primitive/node/weight errors remain named contracts. |
| Rounding and precision, E29--31 | Real-component updates are valid in the declared relative-roundoff model with sufficient exponent range. Nonlinear primitives and separated reciprocals require their own certified error. The complex-exponential allowance explicitly uses u<=1/16. The actual finite recurrence, with a small-accumulation guard, is the operative test. Real-node positive path bounds, all N modes and polynomial node counts justify a sufficient requested accuracy 3L²/(8log2)+O(Llog L) bits under these contracts. |
| Actual costs and residuals | Formal arithmetic O(p³+Np) and RS-only O(L^5) exclude provider bit cost and are not runtime certificates. Exact and structured frozen models solve heat exactly; independently rounded T and zz outputs have only their paid defect allowance. A residual_z output needs an extra mixed channel. |

The source audit records a selected reading of Arias PartII v1, not its
full preliminary precision proof. PartI's PDF was inaccessible; its
proof was not read. PartII's unproved Section3.10 inequalities and
blanket implementation conclusions are excluded. The current Gauss
facts were checked at DLMF3.5(v). A retrieved PDF's hash identifies the
reading copy and does not validate the mathematical inputs.

Corrections from this assessment were incorporated before acceptance:
the explicit A0 integral bound; small-u and small-accumulation guards;
real approximate nodes and bounded omitted strips within frozen branches; and four malformed
LaTeX control sequences. These change no leading rate or operation count.

**Precise unpaid step:** instantiate certified gamma/log/phase, scale,
reciprocal, Gauss-node/weight and frozen descriptor/boundary providers,
and prove that their delivered errors satisfy E5,E9,E22--29. The note
does not certify a concrete library, its internal precision, runtime or
an arbitrary-real floor decision near a cutoff. Query coordinate error
requires an additional allocation. No dependent implementation begins.

Preserved failures are correctly scoped: real size alone does not give
quadrature regularity; removable poles do not make a naive quotient
stable; operation count does not pay roundoff; bounded exponent formats
can destroy the normalization; rounded floor tests are not certified;
zero exact residual does not validate separately rounded channels.
None is presented as an impossibility theorem for certified evaluation.
The old order-growth absorption failure in Note05 is untouched.

This is an approximation/evaluation result, not an RH criterion. The
[result index](../../../../../result-summaries/README.md),
[heat cluster](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../../avoid/README.md) apply. Euler-factor
controls fail the full canonical coefficients; weighted-square/cutoff
controls fail the full xi/RS completion; reflected/smooth/positive-
primitive controls lack the same complete gamma/arithmetic identity.
Exact heat structure itself remains shared by suitable controls. No
physical transfer, endpoint extension, collision exclusion or parent
research-status promotion follows.

**Disposition:** HDA-R05-AN02 r1 CLOSED, bounded analytical audit Complete;
broad R05 Partial. HDA-A02 Partial, HDA-17 Partial, HDA-18 Gated and
HDA-20 unfulfilled unchanged. No manuscript, numerical/symbolic campaign,
field sampling or software certificate. Recommended next owner remains
**Analysis — Sol**, a new bounded provider-algorithm audit, not executed.
