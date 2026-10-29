# Continuation: a signed arithmetic test after the exterior stop

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort xhigh**.

**Status: HCB-05 round 2 prepared, not started.** This is the executable
analytical handoff for [Overview02][overview] and the sole current
[Register02][progress]. It incorporates [Note10][n10] and [Review06][review]
without upgrading their proof/review status. No new arithmetic estimate,
source evaluation or numerical protocol is supplied here.

## 1. Starting position

Note10 acquired the eventual normalized physical-jet floor \(1/384\) on
\(6\le tL\le8\), \(|u|\le1\), after uninstantiated finite gates. It is
classical exterior calibration. The tested weighted \(n=1\) absolute-sum
budget fails near \(tL=4\), even with zero source error. That variant is
stopped; the time-zero HCB-05 target remains open.

The next question is whether **a specific estimate retaining cancellation
between distinct arithmetic modes** gives useful control of the joint
field and physical derivative. Do not restart by adjusting the weights
of the same sum of individual norms, or by increasing source accuracy.

Read the [result index][results], [heat-flow cluster][r11],
[collision controls][controls] and [avoid index][avoid], especially
[target classification][a01], [scoped failures][a07] and
[complete signed estimates][a12]. Then read Note10 §§1–8, Review06,
[crossover Note04, CS2–CS7][crossover], and the
[earlier outer budget, §§1–2][outer58] with its linked Note43. The latter
already has the asymptotic scale \(tL\ge61/24\), with its own imported
arithmetic package, time domain and unevaluated onset. This is the
comparison baseline, not the stopped \(tL\ge6\) calibration alone.

## 2. Frozen first benchmark

Use the canonical normalization \(H_t=-H_{zz}\),
\(H(0,z)=\xi((1+iz)/2)/8\), and
\[
L=\log(X/(4\pi)),\quad N=\lfloor e^{L/2}\rfloor,\quad
z=X+u/L,\quad |u|\le1,\quad \sigma=tL=2,
\tag{1}
\]
as \(X\to\infty\). Reserve \(|u|\le2\) and the upstream fixed complex
buffers. Freeze \(X,L,N\) and \(A=\mathcal E_o(t,X)>0\) in spatial
differentiation. The target vector is
\[
V_H=(H/A,H_z/(LA)),\qquad V_F=(F_N/A,F_{N,z}/(LA)).
\tag{2}
\]
Here \(\sigma=tL\); it is not HCB-02's microscopic time \(tL^2\).
No RH assumption is needed for the inherited field approximation.

This benchmark is below the recorded \(61/24\) constant and remains
inside the positive crossover theorem. It is a diagnostic choice, not a
claim that a positive margin exists or can presently be proved. If another
domain is needed, justify and freeze it before changing the task; retain
the original benchmark and the reason it was unsuitable.

## 3. Keep the signed object visible

One exact starting notation, directly grouping Note10(3), is
\[
U_N(t,z)=\sum_{n=1}^{N}w_n(t,z)
 e^{-i(z/2+\pi t/8)\log n},\qquad
w_n=n^{-1/2}e^{t((\log n)^2-\lambda\log n)/4},
\quad \lambda=\log(z/(4\pi)).
\tag{3}
\]
On the real core, with Note10's \(E,\Theta,\rho=E_z/E\) and
\(R_c=e^{-\pi^2t/64}\mathcal R_N\),
\[
F_N=E\operatorname{Re}(e^{i\Theta}U_N)+R_c,
\]
\[
F_{N,z}=E\operatorname{Re}\!left[
 e^{i\Theta}\{(\rho+i\Theta_z)U_N+\partial_zU_N\}\right]
 +\partial_zR_c.
\tag{4}
\]
These identities only specify the existing full arithmetic object; their
derivation is not a new result. They show why a scalar upper bound for
\(U_N\), or a lower bound for its modulus alone, is not automatically a
joint physical-jet lower bound. Preserve the correlation with its
derivative. Do not divide by \(U_N\), \(H\), \(F_N\) or the completion
without a separately established nonvanishing premise.

## 4. Work order and required return

1. **Select one signed estimate.** State the exact theorem or proposed
   bounded lemma, block decomposition and parameters. Identify the
   arithmetic phase relation it uses that Note10's absolute sum discarded.
   Check its hypotheses against the actual quadratic heat weights and
   physical derivative. Begin with the earlier outer package and its
   source references before importing or rederiving an estimate.
2. **Apply it to the complete quantity.** Account for every omitted block,
   cutoff endpoint and derivative. If using a shifted Dirichlet series or
   Euler product, prove the replacement error for (3); the heat weight
   cannot be silently dropped. Retain cross terms in a squared expansion.
   A height average needs an additional argument before it can exclude an
   exceptional point.
3. **Pay the physical comparison.** Report the model jet margin or exact
   obstruction. Add completion/value/derivative errors separately, then
   combine them with any norm condition number. Use CS6's positive-time
   crossover allowance \(O(X^{-3/4})\) on this domain. Recheck all carrier
   and completion bounds used outside Note10's proved band. A time-evolution
   argument must also retain the model's actual nonzero heat residual.
4. **Compare and decide.** State the resulting domain, constants/onsets and
   full net margin, and compare with the earlier \(61/24\) budget under
   matched hypotheses. Distinguish an asymptotic gain from an effective
   finite onset or cost improvement. Return either an actual quantitative
   estimate or the first precisely failed inequality, with its required
   size and the information that is missing.

A complete signed-sum estimate weaker than global noncollision can be a
useful intermediate result; specify its number and consumer. Conversely,
assuming joint nonvanishing or the desired lower margin merely restates
the target. Do not count that assumption, (3)–(4), or a classical-range
recovery as new collision exclusion.

**Stop this attempt** if the chosen estimate is inapplicable, its remainder
erases the margin, it uses only the stopped absolute-sum information, or
it reproduces the inherited result without a demonstrated quantitative
benefit. Keep the failed calculation and its exact scope. One such failure
does not close J, and it does not automatically activate P. A P continuation
still needs a specific integrated arithmetic quantity, complete population
and an absolute error budget below one event.

## 5. Controls, application scope and delivery

Use Note10 §8 and [cluster12][controls] to name the premise each relevant
control fails. The distinctions concern unchanged canonical arithmetic,
full reflection and the actual approximation/bound, not the choice of
norm. Euler-factor sources alter the factors; weighted-square controls
lack full reflection and an all-real heat time; reflected/primitive
controls lack canonical square arithmetic; finite-prime and close-source
controls do not preserve the full required arithmetic data. A new estimate
must show the corresponding failed premise or quantitative payment at an
event in its domain. No new control test has been performed for this plan.

A result only on (1) proves neither RH nor time-zero simplicity. The
former requires the complete positive-threshold/height argument; the
latter requires the original time-zero J bound, all high charts and the
bounded remainder under RH. Keep these applications distinct.

Save the return in `notes/`, review in `reviews/`, and update HCB-05 round 2
and HCB-09 in Register02. Do not edit the historical register as a second
live list. No numerical sweep, finite source case, higher-order expansion
campaign, manuscript snapshot or new chat is launched by this note.
Register a future research chat uniquely in Investigation03; this planning
chat retains its existing Investigation05/chat0016 identity.

**Suggested opening request:** Continue HCB-05 round 2 from Note11 and
Overview02. On the proposed tL=2 benchmark, test one named signed arithmetic
estimate against the complete paired sum and physical derivative. Retain
all weights, complementary blocks, completion and source errors; compare
with the earlier 61/24 outer budget. Return a quantitative gain or a
precisely scoped failure, without restarting the stopped absolute-sum
variant or launching a numerical sweep.

[overview]: ../research-overview/02_POST_CALIBRATION_RESEARCH_OVERVIEW_20261028.md
[progress]: ../research-progress/02_POST_CALIBRATION_RESEARCH_PROGRESS_20261028.md
[n10]: 10_DIRECT_ARITHMETIC_JET_CALIBRATION_AND_STOP_20261028.md
[review]: ../reviews/06_DIRECT_ARITHMETIC_JET_INTERNAL_REVIEW_20261028.md
[crossover]: ../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[outer58]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/01_weighted_outer_remainders/58_EXPLICIT_CARRIER_PHASE_AND_CONDITIONAL_HEIGHT_20261015.md
[results]: ../../../../result-summaries/README.md
[r11]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
