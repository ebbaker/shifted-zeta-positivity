# Confluent deflation and the box floor

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, OA chat0003. Actual model and
reasoning effort are unavailable in the registry.

E01 accepts the finite survival theorem in
[Note02](02_TND_OA_B01_REGULAR_DEFLATION_AND_FORCE_TRANSFER_20261109.md)
under its stated premises. The following qualifications apply to the
frozen text. [Claim-level assessment](../reviews/03_TND_OA_E01_R1_REGULAR_DEFLATION_ASSESSMENT_20261109.md).

- In §2, for \(a=b\) the affine interpolant of \(P\) means
  \(P(\tau,a)+(x-a)P_x(\tau,a)\). Evaluate at a repeated evaluation
  node by the simplex formula. This gives the continuous extension
  used by (6) over the closed box.
- In §3, when both fields are multiplied by a real \(\rho<0\),
  reverse \(\sigma\) to preserve the positive-floor convention.
  The signed derivatives and their error allowances then scale
  by \(|\rho|\). The logarithmic derivative and its curvature
  are scale invariant.
- In §6, the quadratic control with exact model gives
  \(A=K=b=0\). With \(Q_-=q(0)=8T\), its gap margin is positive
  precisely for \(\Delta<T\). The domain and the initial
  midpoint/upper-gap premises still apply. A weaker initial lower
  bound can certify a shorter interval.

## A necessary screen for the proposed box

In the fixed parameter box, the \(d=0\) slice has
\[
V_0(\tau,c,0,v)=\tfrac12\sigma P_{xx}(\tau,c),\qquad
U_0(\tau,c,0,v)=\tfrac12\sigma h_{xx}(\tau,c).
\]
Thus (6)–(7) require
\[
\sigma P_{xx}(\tau,c)\ge 2m,\qquad
\sigma h_{xx}(\tau,c)\ge 2(m-e_0)>0
\]
on the full time and **center** interval, \(|c-X|\le R\).
An actual zero or sign change of \(h_{xx}\) there rules out the
uniform floor on that specific box. This is a necessary screen
for the fixed box implementation. Passing it leaves all \(d>0\)
and \(v\) values, the signed average and the strict margins to
check. A rejected box can still contain a surviving pair. This
check has no canonical data attached to it. [Scope discipline](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
