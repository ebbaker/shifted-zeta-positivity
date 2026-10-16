# Continuation after the cumulative append obstruction

20 September 2026. Prepared for Edward Baker.

**Model:** OpenAI GPT-6 (Codex; developer-provided identity).
**Reasoning effort:** not exposed in this session; no setting is inferred.

Read [CUMULATIVE_APPEND_SCALAR_OBSTRUCTION_20260920.md](CUMULATIVE_APPEND_SCALAR_OBSTRUCTION_20260920.md)
first, then its linked anchor and review as needed. The anchor remains
subject to specialist review and was replayed at 40 and 60 digits.

## Established in the new calculation

At \(L=1/2,h=1/20,w=10^{-3}\), the anchor gives
\(E=I-X^*X,F=I-ZZ^*\succeq\delta I\),
\(\delta=0.000049998\). The exact append response is
\[
Yf(t)=\int_0^Lk_w(t+r)f(L-r)\,dr.
\]
Both signed pole states and the complete beta history cross the join.
The new-output defect is obtained by reflecting the short-window input
defect; do not replace it without reflection.

Exact rational checks and the note's analytic inequalities prove
\[
55<\|Y\|/\delta<72.
\]
This is a failure of the scalar sufficient estimate, **not** a lower
bound above one for the actual normalized coupling. The stronger exact
lower/upper displays are 55.9758151914 and 71.9031622484.

For 32 cosine modes on each side, the raw complement/complement block
satisfies
\[
\|(I-P_h)Y(I-P_L)\|/\delta>46.
\]
Its witness is logarithmically spread in an extremely small neighborhood
of the join; it lies mostly outside both finite cosine spaces. Raising
quadrature order cannot remove this omitted-space obstruction.

For the central generator, the omitted arithmetic EMA mixed kernel is
\(-2e^{-(2M+1/2)(t+r)}/(1-e^{-2(t+r)})\). Its norm is \(\pi\)
for every finite \(M\), even after any fixed finite-rank projections on
both sides. The corresponding central-form block has norm \(\pi/2\).
Thus positive-form truncation of diagonal gamma energy does not furnish
a small absolute mixed-block remainder. At positive shift the actual
mixed transfer is Hilbert--Schmidt; do not import the central
noncompactness claim into the positive-shift operator.

## Diagnostic evidence, not a certificate

The complete-output finite-input coupling quotients are approximately
0.798419915, 0.801276004, and 0.801830639 at 8, 16, and 32 cosine modes
per interval. The 32-mode instantaneous central quotient is 0.801829271.
The cumulative quotient changes by about \(1.9\,10^{-12}\) on its last
quadrature refinement. These are floating diagnostics and, in exact
arithmetic, finite quotients would be **lower** bounds on \(\|\mathcal C\|\).
No all-input upper bound below one has been proved.

The recorded weak finite pair has old defect about 0.0001276692,
new-output defect about 0.0034944355, and mixed pairing about
0.0005355675 for unit ordinary norms. The short-window directional
storage is much larger than the scalar anchor floor.

## Next bounded task

Keep this same append, shift and normalization. Develop an all-input
**energy-weighted** bound for the three blocks involving a complement,
rather than raising raw matrix resolution or crossing \(\log2\).

1. Choose explicit computable lower metrics for \(E\) and \(F\) that
   preserve the join-direction energy. A valid starting inequality is
   \[
   D_{w,\ell}\succeq2\int_0^w
   V_{s,\ell}^*(T_{M,\ell}-s^2I/8)V_{s,\ell}\,ds,
   \qquad\ell=L,h,
   \]
   with reflection on the output side. This identity retains the actual
   flow and is not an operator exponential of \(T_M\). Assess coercivity
   and high frequencies; a bounded finite tower alone may be weak there.
2. Use an explicit energy-orthogonal head/complement split, or retain
   the nonzero metric cross blocks in an ordinary cosine split. Bound
   all four normalized mixed blocks. A certified two-by-two matrix of
   their norms with norm below one would close this test.
3. Retain both endpoint/pole memories and the prescribed local
   coefficient. If using Cayley coordinates, use the proved unitary
   equivalence of normalized coupling and keep the full cumulative
   metrics. Central finite-test approximations are not uniform operator
   bounds.
4. If the method still fails, give its quantitative obstruction and
   identify exactly which energy-weighted block remains uncontrolled.
   Do not replace the target with an independent central certificate
   for \(L+h\).

No auxiliary filter loss or averaging variance has contributed to the
present result. Instantaneous positivity is sufficient where available
but is not required throughout the intended program. There is no new
all-depth theorem, arithmetic Loewner driver, physical Wilson norm
identity, or localization construction.

## Files and replay

- [Research calculation](CUMULATIVE_APPEND_SCALAR_OBSTRUCTION_20260920.md)
- [Exact checker](../numerics/certify_cumulative_scalar_obstruction.py)
- [Exact record](../numerics/records/cumulative-scalar-obstruction-20260920.json)
- [Diagnostic code](../numerics/diagnose_cumulative_append.py)
- [Diagnostic record](../numerics/records/cumulative-append-diagnostics-20260920.json)
- [Provenance](../numerics/records/cumulative-append-provenance-20260920.json)

Replay commands are in Section 8 of the calculation. Use temporary
outputs to preserve dated records. The previous notes, pre-existing
index changes and v0.4 manuscript snapshots have not been modified.
All new files fit the repository's small-file policy.
