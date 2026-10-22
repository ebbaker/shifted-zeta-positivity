# Self-review: full reflection adjoint and connector audit

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. This assessment is by the authoring assistant;
it is not independent or specialist review.

## Material and disposition

Reviewed [Note 02][note], its [checker][checker] and the
[192-bit execution record][record]. The result is an explicit audit of
the candidate selected in the progress register: complete reflection
adjoint subtraction for the physical first jet. The finite-source
connector and its payments are supplied; the reflection-only norm
comparison is equality. The known complete contour evaluator is not
presented as a new result. No theta exclusion or simplicity conclusion
is supported or claimed.

## Analytic checks

1. **Contour orientations.** The upper and lower half-line shifts have
   vertical contributions from 0 to +id and 0 to -id. Changing variable
   in the lower one gives A(v)-A(-v), with the positive prefactor i/2
   in the s-coordinate. Thus H_A=P_A+C_A; for complete theta, C=0.
   For a finite prefix the two residuals are H-P_N=P_tail and
   H-H_N=P_tail-C_N. The distinction is retained throughout the note.
2. **Complex parameters and derivatives.** The proof does not replace
   the paired integrands by a real part for complex t,z. All z-derivatives
   hold the contour fixed. The connector factor is (-s)^j; the shifted
   factors are (i(u+id))^j and (-i(u-id))^j. The normal-convergence and
   superexponential bounds justify the complete-source operations.
3. **Finite negative cusp.** An analytic mode has leading behavior
   -3 lambda_n exp(5u) as u tends to minus infinity; positive heat makes
   its separate full-line transform divergent. An even extension using
   |u| instead has a cusp. Neither is the analytic complete reflected
   source. The note does not integrate either as if the missing
   cancellation had occurred.
4. **Connector size and asymptotic.** The bound exp(T d^2) is valid for
   complex |t|<=T. Canonical prefix derivative a_N=sum_(n>N) gamma_n
   is positive for N>=1. Its leading connector term is
   (-1)^(j+1)(j+1)! a_N/x^(j+2). Taylor's bounded cubic remainder
   and a fixed-segment Laplace estimate give the stated error.
   No claim is made that height 30 is in this eventual-sign regime.
5. **Sharp norm comparison.** Pairing u and -u proves the directional
   lower bound for every odd adjoint kernel. Removing the odd part
   attains it. The measurable even extremizer rho sign(F_l) proves
   sharpness only for the explicitly relaxed pointwise error class.
   It is not asserted admissible in the analytic theta class. The
   coupled support function and convex-distance formula use the same
   data on both sides; no Cartesian-box disadvantage is charged only
   to the baseline.
6. **Complete shifted tail.** The complex-time estimate pays
   exp(T d^2), bounds both contour halves, sums every omitted mode
   through a geometric majorant, and integrates the entire source ray.
   Its numerical constants exclude retained quadrature error. The
   inherited nonstationary and S01 paired-tail improvements remain
   available; no superiority over them is claimed.

## Numerical checks and limits

The frozen diagnostic contains two finite-source cases, including one
with complex heat time and spectral coordinate, at d=pi/16. For value
and first derivative it acquires H_N, P_N and C_N independently. All
four residual balls for H_N-P_N-C_N contain zero and have absolute
upper bound below 1e-25. Each connector and each H_N-P_N ball excludes
zero, so omitting the connector fails the diagnostic.

The half-line integrals are not treated as finite integrals without
payment. The source cutoff U=1 is followed by the full tangent-majorant
exteriors of Note 02 (25)–(26). Positive decay slopes and log-concavity
conditions are checked by interval inequalities. The connector has no
unbounded exterior. Finite-source diagnostics do not need a fictitious
infinite mode tail; the separate complete-theta constants include all
modes n>=5.

The reflected control at t=1/4, x=pi/4 is integrated on both shifted
rays through U=8 with complete quartic exteriors for orders 0–2. Its
second derivative is strictly positive, enclosing
13.0469417294339317307841204705. Its exact double zero follows from
the analytic factorization F(x)(1+cos(4x)); the balls containing zero
are a regression check, not a proof of exact equality.

The receipt records Python 3.10.0, python-flint 0.9.0, 192-bit precision,
fixed inputs and the source-file SHA-256. The integration callbacks are
entire, so their analyticity contract does not rely on unsupported
conjugation or a branch choice. This is one implementation with analytic
tail proofs, not an independent numerical reproduction. No timing,
precision-cost, sign-region or coverage comparison was performed.

## Control matching and remaining gap

The reflected control passes the evenness, strip analyticity and
vanishing-connector hypotheses while colliding. It fails canonical
integer-square arithmetic. Euler-factor symmetric translates likewise
pass reflection but change arithmetic and numerical envelope constants.
Finite-prime and weighted-square controls can match finite endpoints
while failing full reflection. Smooth/primitive controls are not granted
unproved complex analyticity. The note preserves these distinctions
from the [control register][controls].

The exact no-gain statement concerns **odd reflection adjoints with the
same pointwise envelope and coupled observations**. It is not a universal
obstruction to modular geometry, contour shifts, arithmetic coupling or
analytic residual norms. Source rigidity still does not supply the
missing signed retained-core inequality. That limitation follows the
[classification][a01] and [scoped-stop][a07] rules in the
[avoid index][avoid], and the inherited identities retain their status
in the [result index][results].

**Disposition:** retain the connector identities and complex-time tail
payment as reusable components; stop the tested reflection-only
improvement. Require a concrete coefficient-coupled signed residual and
a same-information comparator before any theta pilot. TST-03 remains
open; TST-05 and the global simplicity bridge remain gated.

[note]: ../notes/02_FULL_REFLECTION_ADJOINT_AND_CONNECTOR_AUDIT_20261021.md
[checker]: ../numerics/check_reflection_adjoint.py
[record]: ../numerics/REFLECTION_ADJOINT_CHECK_192_20261021.json
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
