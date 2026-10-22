# Internal review: paired theta residual and matched direct comparison

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring and reviewing configuration:
**gpt-6.1-sol (Codex), reasoning effort ultra**, as recorded for the active
turn. Two contributing agents checked complementary parts; this is
same-model internal review, not independent specialist or cross-model review.

**Disposition: passes in the stated analytic and estimator scopes.**
Reviewed [Note 02](../notes/02_PAIRED_THETA_RESIDUAL_AND_MATCHED_DIRECT_COMPARISON_20261022.md),
its [exact replay](../numerics/check_wgi_paired_residual.py),
[receipt](../numerics/WGI_PAIRED_RESIDUAL_CHECKS_20261022.json), and the
inherited BW14 source law, reflection/connector identities and S01 paired
baseline linked in the note.

The paired transform is applied to the complete reflected source first.
The subsequent head/tail/Laplace decomposition is linear in that transform;
it does not assume a finite source or each mixture component is even.
The source shift 1/16 keeps the mixture growth exponent below 1/32, while
the available exponential moment has exponent gamma/2>1/4. Complete
double-exponential source-ray majorants justify the sums, absolute Fubini
and physical derivatives through order two. No individual connector,
source mode, ray tail or negative lower-order source monomial is omitted.

The main quantitative improvement is correct. Subtracting the exact
lowest atom before estimating yields
M_kappa=2B_k+sum_{n>k}(A_n+2B_n)exp(kappa delta_n), and the all-mode cap
Mhat=2B_k+A(1+6/D)r/(1−r). The geometric ratio argument gives
Mhat<(4177/1967)A<3A and coarse-minus-new gap>(1724/1967)A.
The stronger inherited BW14 strip cap is also granted: its difference
from Mhat is exactly 6A alpha/(D beta)>0. Thus this is not merely a
comparison with the coarse constant four. The new cap divided by the
remaining source mass tends to two; the old strip and coarse budgets
have the distinct asymptotics stated in the note. No optimal exact-moment
or measured physical-error claim follows.

The reference energy floor and complete cubic payment are paid. From
the actual conditional floor and eta<=sqrt(e)/17, both the reference
and the full real homotopy have positive first-jet norm; rho<=1/16 follows.
The complex-root factorization of the energy ratio proves the uniform
log cubic bound. Its signed Green allowance is exactly at most 1/6480.
The correction contains one- and two-residual-source terms, with the
same measure and its product law. This counts algebraic order, not
acquisition work or cost superiority.

The signed finite dual is valid weak duality. Its two event coordinates
and one source-reflection coordinate are real. A positive exponential
moment multiplier makes the supremum finite, since its penalty grows
strictly faster than the response kernels. At fixed multipliers the
improved moment cap produces the stated exact strict endpoint decrease;
no uniform strict gain after multiplier optimization is proved. The
finite reflection sample is not presented as the entire reflection law.

The decisive fair comparison is also correct. On the paid regular
homotopy, exact Green identity can be differentiated twice under the
integrals. Direct weighted-density evaluation has the identical signed
linear and quadratic corrections, including their full mixed terms.
With the same feasible residual class, base mass and cubic payment,
its upper certificate is identical to the candidate's. Canonical-source,
event, reflection, moment and covariance constraints improve both sides.
This closes the superiority claim for the declared estimator class,
not every weighted method, different error payment or possible resource
comparison. No complete WGI-versus-direct advantage has been established.

Three precision clarifications were incorporated: V_s is defined as a
time-dependent field before its event values are used; the common feasible
class is restricted to the paid regularity/residual contract; and a
numerical reference cannot silently replace exact holomorphic F. A real
replacement must have certified holomorphic jets, including order two
for the density identity. Evaluation errors can instead be paid separately.

The reviewer independently re-executed the finite replay during audit.
The root regenerated the receipt after final text clarifications and the
stronger strip-comparison algebra checks. The replay checks rational
constants and local density/log variation coefficients through quadratic
order on three polynomial cases. These finite cases do not prove the
integrated or all-mode theorems; their written arguments carry those claims.
No theta values, source optimizer or actual weighted mass were computed.

The [progress register](../research-progress/01_WEIGHTED_GREEN_INTEGRALS_PROGRESS_20261022.md)
correctly keeps WGI-01–03 partial overall and WGI-04 gated. Controls retain
their distinct failed canonical premises; no unproved match to the sharper
new moment cap is assigned to a colliding control. The completed endpoint
atom is retained, and no endpoint-uniform, all-height or simplicity result
is claimed. Apply the [result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md), especially
[review independence](../../../../avoid/05_same_model_reviews_and_shared_premises.md),
[scoped conclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [complete coupled estimates](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
