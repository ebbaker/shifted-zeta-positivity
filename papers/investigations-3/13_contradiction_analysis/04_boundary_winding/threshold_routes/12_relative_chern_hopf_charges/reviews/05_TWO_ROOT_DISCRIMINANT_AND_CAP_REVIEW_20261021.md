# Review of the two-root discriminant and real-cap reduction

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6-astra (Codex)**,
recorded reasoning effort **max**. Self-review by the producing assistant;
no independent specialist validation.

**Source:** [Note 05][note]. **Assessment:** proved in-note under the
explicit two-root isolation and phase assumptions. The complete-theta
strip formula is a sufficient implication from proved real-time wall
floors; those floors and the cap signs have not been established for a
new theta region here. The previous numerical receipts are unaffected.

## Mathematical audit

1. **Coefficient and normalization.** With q=U_z/U, the two root speeds
   are plus/minus 2/(z_1−z_2), plus 2q at each root. Their squared
   difference therefore satisfies Delta'=8+4Delta(q_1−q_2)/(z_1−z_2).
   The coefficient 4 agrees with the contour formula for A. The formula
   using b=2q would have coefficient 2 on its divided difference.
2. **Regularity at collisions.** A is defined by a spatial contour on
   which both H and P are nonzero. The exact identity
   integral(P_z/P^2)=0 removes the cluster contribution. No inverse
   discriminant or inverse internal gap is assumed bounded. An
   identically repeated quadratic factor is ruled out by the heat
   equation itself; analytic continuation then proves the ODE at every
   collision. There Delta'=8, so the charge is one.
3. **Complete exterior retained.** U includes the rest of the function.
   The contour formula does not discard its logarithmic derivative.
   Its real specialization agrees with the already recorded adjacent
   pair equation in BW10 Note 03; this inherited equation is not claimed
   as new. The scalar subtraction in (10) is permitted because
   integral(1/P)=0 for a monic quadratic, including a repeated root.
4. **Phase and reality.** Real spatial center, conjugation-invariant
   contour and the reality symmetry of H imply the same symmetry for P
   and A. With a real primitive base point, J is real on the real axis.
   Its imaginary part is precisely the vertical integral of Re A.
   Thus K tau<pi/2 controls phase without a factor for the real length.
   K and the wall hypotheses nevertheless cover that full length.
5. **Injectivity and boundary.** The time rectangle is convex. The
   average of mu along every straight segment has positive real part,
   proving injectivity on its closure. Conjugation excludes nonreal
   discriminant zeros, and the real quadratic places a repeated root on
   the real spatial axis. Nonzero real cap discriminants consequently
   exclude every time-boundary event. Whole-cap nonvanishing is derived,
   not assumed in addition to the two signs.
6. **Charge decision.** On real time, mu>0 and (mu Delta)'=8mu>0.
   Equal nonzero cap signs give zero events; negative followed by
   positive gives one; the reverse order is impossible. The three
   quadratic controls check both zero-charge sign cases and the
   one-charge case exactly. The cubic controls fail the root-count
   hypothesis and cannot be excluded by this theorem.
7. **Theta thickness.** Positivity and full decay of Phi justify the
   cosh moment majorants. A purely imaginary time lift costs tau M_2,
   not an additional real heat weight. Both circles need count two at
   the anchor; otherwise an extra root in the collar would invalidate
   the zero-free unit. Both spatial floors propagate to the strip.
   Rearranging K tau<pi/2 gives exactly the denominator
   B_R+8RL/(pi(R−r)^2) in (24). The internal separation never enters.
8. **What is not paid.** Defining d_r or d_R as unknown positive minima
   would not establish (22). They are explicitly required inputs. The
   positive source upper moments do not give those lower bounds or the
   real cap signs. The BW14 strict tail comparison has a real-parameter
   contract, so its improvement is not assumed on the complex wall.
9. **No zero-charge upgrade.** A half-plane bound for Psi' gives
   injectivity, not omission of the target value in (12). The collision
   model satisfies A=0 and still has Q=1. The source controls may
   satisfy all local continuation hypotheses while failing the same-sign
   cap case. This is the exact distinction between this analytical
   milestone and the still-open arithmetic endpoint exclusion.

## Remaining review and research

An additional algebraic check avoids moving root labels. Write
P=z^2−s z+p and let the remainder of q=U_z/U modulo P be q_0+q_1 z.
Reducing H_t+H_zz=0 modulo P gives
\[
 s'=4q_0+2s q_1,\qquad p'=-2+2s q_0+4p q_1.
\]
Consequently (s^2−4p)'=8+4q_1(s^2−4p), agreeing with the contour
coefficient A=4q_1. The analytic division remainder is well-defined even
at a repeated root. At an event the complex jet Jacobian is
−H_zz^2, which is nonzero for a double spatial root and gives local
holomorphic degree one.

No experimental validation is needed for these finite algebraic controls;
their formulas are checked directly in the note. Independent review of
the holomorphic factorization, contour cancellation, closed-boundary
injectivity and source domination remains desirable. No optimality claim
is made for pi/2 or for the moment-based strip width.

The next research task is an actual complete-source lower/phase/sign
estimate on a declared window. Increasing moment accuracy alone cannot
determine the sign of 2S_2−S_1^2. A unique negative-time collision must
also be distinguished from a time-zero event before drawing a physical
endpoint conclusion.

[note]: ../notes/05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md
