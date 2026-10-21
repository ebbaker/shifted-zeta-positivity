# Moving product tube and physical trace review

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. This is a **same-assistant self-review**, not
independent model or specialist validation.

**Assessment:** [Note 21][note] completes HMC-04 on its declared compact
positive-time product tubes. Its exact moving transport, complete face
accounting and quantitative physical trace payment are proved in-note.
The matched construction reduces exactly to a planar transverse average;
under RH it adds a nonnegative excess to the inherited cap phase. This
is no new signed theta gain and leaves HMC-05/06 open.

The review follows the [result index][results], [geometry summary][geometry]
and [avoid index][avoid]. The work is classified as exact transport,
a quantitative compact trace estimate, and a scoped comparison. It is
not an RH-equivalent criterion supported by finite checks.

## 1. Geometry and derivative audit

The orientation is \(dx\wedge dv\wedge dp\wedge dq\). Expanding
\(\beta_f\wedge\alpha_g\) gives
\((-\operatorname{Im}(P_f\bar g)dx+
\operatorname{Re}(P_f\bar g)dv)\wedge dp\wedge dq/2\).
This verifies the coefficient and sign in MT6. Both endpoint faces and
both transverse faces are retained in MT8. Each of the four auxiliary
faces has zero pulled-back \(dp\wedge dq\), rather than an omitted
flux. Their common area cancels after normalization.

The physical denominator is \(E(t,x)\), fixed along the transverse
fibers. In the original polarized primitive, differentiation introduces
\(W_x\mathsf B\), with the correction subtracted in MT8. The exact
gauge identity \(\theta=-G_vdx/2+d\psi\) cancels this term against
the boundary of \(W\,d\psi\); this accounts for its disappearance
in MT10. It does not assert that the original uncorrected flux equals
the weighted observation. A primitive constant changes the individual
terms but not the corrected sum.

The phase signs in MT3 follow directly from \(H_t=-H_{xx}\).
At a simple root, \(\rho=1\), \(\omega=H_{xx}/H_x=r'\), so the
moving endpoint terms cancel. The imaginary derivative of the pulled-back
physical jet includes \(-g'K_y/g^2\). Dropping it would give a different
density and time current. No assumption that the midpoint is stationary
is used; no circle radius or stationary-point condition is hidden.

MT13 retains the derivative of the thickness normalization as well as
the two transverse-face velocities. For a non-even comparison model,
the normalized primitive has \(P_t=-h_1+h_1(t,0)\); the note explicitly
retains this distinction. The scalar Reynolds formula does not depend
on a special primitive choice.

## 2. Constants, tails and scope

Differentiating the full Hermitian numerator twice transversely gives
the coefficients \((3,-4,1)\), and then in heat time gives
\((4,-7,4,-1)\). Together with \(|E_t|\le L_t\), these verify MT11.
The signed Taylor kernel in MT12 has integral \(\eta^2/6\). The
transverse boundary-minus-average payment in MT14 is
\(\eta|\eta'|D_0/3\), not twice that coefficient. The remaining
terms are \(gD_1\eta^2/6\) and the two endpoint speeds times
\(D_0\eta^2/6\). The endpoint bound
\(2M_2/\sqrt{e_*}\) follows from the same physical floor.

All constants retain their dependence on \(\epsilon,T,A,\eta_*\),
the complete source moments and the physical energy floor. MT18's
logarithmic majorant is concave on its stated tail; MT19's ratio bound
pays every omitted theta index on the finite source interval. Neither
is an unrecorded finite-support replacement. Finite quadrature errors
would still have to be certified in an actual evaluation.

The grid rule MT20 is a valid compact floor certificate when its displayed
number is positive. Its existence follows under RH on positive compact
time intervals, but this round did not compute a grid or a numerical
floor. No value, run time or uniform estimate down to time zero is claimed.
This dependence is material: MT23 gives an explicit double-zero model
where the unpaid trace loss persists even at thickness proportional to
the square root of time.

## 3. Matched planar comparison and control response

The comparison is exact for the fixed domain, weight and Hermitian
extension, not a benchmark between numerical implementations.
The nonnegative transverse coefficients are already generalized Laguerre
positivity. Note 21 provides the needed paired-product proof and checks
the primary Csordas–Vishnyakova source, Theorem 1.2 and equation (1).
No new positivity or literature-priority claim is justified.

Thus \(\pi\le I_\eta\le\pi+g\eta^2D_0/6\); the excess is
nondecreasing in thickness. These facts hold for the appropriate all-real
comparison models as well. The positive atomic and RH-conditional
Euler/close-source endpoint controls pass the generic compact geometry
and trace statements while retaining multiple endpoints. Their failure
is the original normalized theta arithmetic, not the new geometric
identities. Weighted-square/finite-prime controls lack an all-real heat
slice, so their entire spectra are not used in this positivity argument.
Reflected and positive-primitive controls are used only in the local
scope stated in the note. The polynomial witness lacks the theta source;
it closes only a generic unpaid uniform-recovery assertion.

MT21 exposes a complete two-source correlation payment with the
\((u+v)^2\) and \((u-v)^2\) factors and both oscillating phases.
Separate positivity of the source and the hyperbolic multiplier is not
a sign proof for its terms. Any HMC-05 continuation must specify a new
bound, its endpoint scale and the premise failed by the controls.
Another evaluation of the already known cap phase is insufficient.

## 4. Verification and decision

The [standard-library replay][script] passed its frozen exact polynomial
identities for heat degrees 2, 3, 4 and 6; nonconstant weighted boundary
and correction terms; the primitive change; the phase conservation law;
the two transverse derivative formulas; and a moving rectangle with
nonzero endpoint and thickness speeds. Separate rational fixtures check
the physical derivative scale and two-source frequency coefficients.
The [small receipt][replay] records the script hash and arithmetic scope.
These checks do not prove the infinite-product limit, certify a theta
floor, or replace the written analytical proof.

No discrepancy remains in this bounded self-review. HMC-04 is marked
complete **for MT2**, with a scoped absence of geometric gain. Different
domains and source-correlated estimates remain open. The requested
progress file and program are updated; the canonical manuscript and
parent simplicity status are unchanged. No commit, tag or draft snapshot
was created.

[note]: ../notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md
[script]: ../numerics/check_hmc_moving_tube_algebra.py
[replay]: ../numerics/HMC_MOVING_TUBE_ALGEBRA_REPLAY_20261021.json
[results]: ../../../../../../../result-summaries/README.md
[geometry]: ../../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[avoid]: ../../../../../../../avoid/README.md
