# GNP-RS-E03 r1 — coherent quadratic-Jensen obstruction

11 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Issuing chat0001 has no actual
model identifier or effort recorded in its capture metadata.

**Type E; recommended GPT-6.1 Sol.** B02 has fixed the moment, proof
route and comparison margin. This is a bounded analytical derivation,
not a request to choose or solve a new signed-log mechanism.
**Frozen request; ready, unactivated at issue.** Preserve this revision
and write a separate return. Issuing it changes no model settings.
E02 already denotes the overview assessment; this task is E03.

Owner: [sole GNP-RS register](../01_GNP_RS_RESEARCH_PROGRESS_20261110.md).
Dependencies: [B02 Note05][b02], [decision][decision], E01
[proof][e01] and [self-check][e01-review], and their named HDA inputs.
The [B02 identity record][record] pins the actual source/request bytes.
Verify them before reuse and report any drift. Existing E01 r1,
B01/E01 mathematical notes, earlier records and source proofs are
historical evidence, not editable execution templates.

## Fixed question and why either outcome matters

Does the exact coherent quadratic moment already make the localized
Jensen allowance fail at arbitrarily high centers, even with all
same-arm and reflected cross terms retained?

Prove the moment limit (E03a) and its consequence (E03b) below, or
return the precise first unsupported step of this fixed derivation.
Success closes this **particular quadratic-Jensen recipe** as an
eventual every-center method for the frozen defect margin.
It would leave direct signed-log estimates, estimates subtracting a
proved Jensen gap, and other coupled comparisons open.
A failed derivation is not evidence that the recipe succeeds.

Keep the complete theta source, \(\partial_\lambda H=-H_{zz}\),
E01's exact carrier \(C_-\), \(V_\lambda=H_\lambda/C_-\), strip
\(0<y<8\), center \(X+4i\), and kernel
\(K(t)=1/[16\cosh(\pi t/8)]\). Retain E01's \(I,P,C_*,D_V\) and
all inherited fixed-buffer/onset conditions.
\[
 L_X=\log(X/(4\pi)),\quad R_X=(32/\pi)\log X,\quad
 q_X=\int_{-R_X}^{R_X}K(t)\,dt,\quad
 T_X=D_VX^{-3}\log^2X.
\]
The original domain remains \(c\in[1/2,1]\), \(\lambda=c/L_X\),
every sufficiently large \(X\), with \(d=1/2,r=1\).
This task tests **only \(c=1\)**, a subfamily sufficient to refute
every-center success on that whole band. It does not claim a moment
law uniform in all \(c\), a fixed-positive-time result, or time zero.

## Statements and evidence standard

For the exact moment
\[
 M(X,1)=\int_{|x-X|\le R_X}K(x-X)|V_{1/L_X}(x)|^2\,dx,
\]
prove
\[
 \boxed{\lim_{T\to\infty}\frac1T\int_T^{2T}M(X,1)\,dX
                  =\zeta(3/2).}
 \tag{E03a}
\]
The time \(1/L_X\) stays **fixed** within each defining \(x\) integral.
The intermediate function \(v(u)=V_{1/L_u}(u)\) is only a proof
device; a justified uniform comparison must connect it to \(M\).

For
\[
 \mathcal B_J(X,1)=
 \frac{q_X}{2}\log\frac{M(X,1)}{q_X}
 -P_{1,1/L_X}(X)+T_X+\frac{C_*}{L_X},\qquad
 m_*=\frac{\sin(\pi/8)}{2\cosh(\pi/8)},
\]
prove the precise failure statement
\[
 \boxed{\text{For every }A\text{ sufficiently large, some }X\ge A
                      \text{ has }\mathcal B_J(X,1)\ge m_*.}
 \tag{E03b}
\]
The same follows for any valid replacement \(M^\#\ge M\) in this
recipe. It does not follow for a different logarithmic method or
one retaining an independently controlled Jensen-gap subtraction.
This is a failure of an **upper allowance**, never a lower bound
on the actual Green potential or evidence for off-line zeros.

Use an analytical proof with finite constants and onsets whose
dependencies are explicit; numerical instantiation is unnecessary.
An \(o(1)\) remainder is acceptable only after every contributing
term has a justified vanishing bound. No height samples, interval
certificates, experimental averages or zero census are requested.

## Four fixed proof groups

1. **Complete real-field reduction and diagonal.**
   Reuse HDA Ansatz Note04 CS3/CS6, \(r=1,b=9\) and its enlarged
   buffers, on pointwise recentered real charts. Use E01's complete
   formula (E10), correction (E11) and original provider assessment.
   At the centered time \(1/L_u\), write the two finite arms with
   \[
   N_u=\lfloor\sqrt{u/(4\pi)}\rfloor,\quad
   w_n(u)=n^{-3/4}e^{(\log n)^2/(4L_u)}\le n^{-5/8},
   \]
   \[
   \nu(u)=u/2+\pi/(8L_u),\quad
   \Theta(u)=u(L_u-1)/4+\pi/16+7\pi/8.
   \]
   Prove the correction/residual can be removed at an \(o(1)\)
   cost in the **averaged squared modulus**, paying both
   cross-error and error-square terms. A sufficient route is
   normalized correction \(O(u^{-1/4})\), residual \(O(u^{-3/4})\),
   and arm bound \(O(u^{3/16})\); verify these from the named
   inputs with constants uniform through every fractional cutoff.
   Prove \(2\sum_{n\le N_u}w_n(u)^2\to2\zeta(3/2)\) by summable
   domination \(n^{-5/4}\), including uniformity on dyadic windows.

2. **All oscillatory cross terms.**
   For each same-arm pair \(m\ne n\), integrate on its actual
   active interval
   \([T,2T]\cap[4\pi\max(m,n)^2,\infty)\).
   Pay endpoints and amplitude variation; use
   \(|\nu'(u)\log(n/m)|\gg|\log(n/m)|\).
   Sum through the full cutoff. A sufficient summation bound is
   \[
   \sum_{m<n\le N}\frac{(mn)^{-5/8}}{\log(n/m)}
                      \ll N^{3/4}(1+\log N).
   \]
   For all cross-arm pairs, including \(m=n\), use
   \(\phi_{mn}(u)=2\Theta(u)-\nu(u)\log(mn)\) and prove
   \(|\phi''_{mn}(u)|\asymp T^{-1}\) on their active intervals.
   Derive a first/second derivative integral bound uniform in
   these pairs and endpoints, with amplitude paid by its supremum
   plus total variation. The expected sufficient cross-arm cost
   after division by \(T\) is
   \(O(T^{-1/2}(\sum_{n\ll\sqrt T}n^{-5/8})^2)=O(T^{-1/8})\).
   These are proposed estimates to prove, not accepted outcomes.
   Do not differentiate the global floor or assume phase
   equidistribution or a pointwise cancellation theorem.
   Conclude \(T^{-1}\int_T^{2T}|v(u)|^2du\to2\zeta(3/2)\).

3. **Original time and convolution.**
   Prove, uniformly for \(|x-X|\le R_X\),
   \[
   |1/L_X-1/L_x|=O(R_X/(XL_X^2)).
   \]
   Compare normalized two-arm formulas at those two times;
   pay heat-weight and phase changes and all correction/residual
   terms. A permitted coarse route is to use
   \((L_x/L_X)\ge1/2\) eventually, giving
   \(w_n(1/L_X,x)\le n^{-9/16}\) on the actual cutoff.
   Then both arm sums are \(O(x^{7/32})\), so two separate
   \(O(x^{-1/4})\) correction bounds still give vanishing
   squared-modulus costs. A more precise carrier comparison is
   permitted but is not required if the coarse costs vanish.
   Establish the resulting \(o(1)\) comparison of local moments.
   Use Fubini to average the \(K\)-convolution; justify truncation
   from variable \(R_X\), both edges of \([T,2T]\), and the exact
   kernel mass \(1/2\). A crude squared-field bound \(O(T^{1/2})\)
   and \(O(\log T)\) edge widths suffice if proved and applied on
   the enlarged interval. Conclude (E03a); no unpriced extension
   of a local approximant to the whole real line is allowed.

4. **Margin and scope.**
   Check B02 (B13)'s analytical rational bounds
   \(m_*<9/50,\ |P_{1,\lambda}|<23/100,\
   \zeta(3/2)>13/5,\ e^{41/25}<26/5\).
   Verify the prime-power multiplicities, integer tail and
   kernel-mass factors. If \(\mathcal B_J<m_*\) eventually, then
   \[
   M(X,1)\le q_X\exp\{(41/50)/q_X\}
       \longrightarrow \tfrac12e^{41/25}<13/5,
   \]
   contradicting (E03a). Prove (E03b) with the correct quantifiers.
   A mean is used to contradict an eventual **upper bound on
   the allowance**, never to infer pointwise smallness of \(J\).

## Limits, permissions and return

One proof/failed-step note, one same-assistant check, one compact
source/check record and one model-change continuation; at most one
bounded correction pass. Routine choices of sufficiently large gates,
summation splits, finite constants, integrable majorants and elementary
oscillatory lemmas are allowed within the four groups. Preserve the
source, clock, carrier, kernel, cutoff, exact moment and target.

A changed moment, cancellation premise, uncontrolled buffer/time
comparison, phase sum requiring a new mechanism, or failure of the
fixed numerical comparison is a **B02 revision-2 escalation**,
recommended GPT-6 Astra. Retain everything proved and identify the
failed step; do not silently expand the task. Do not execute the
shifted-zeta route, a direct logarithmic route, a numerical campaign,
another moment order, or a uniform-in-\(c\) generalization.

Save notes, reviews and small records in the child's established
folders. Update the sole register, plan/overview navigation,
DRAFT_HISTORY, references and canonical continuation with the actual
result. Preserve frozen packets and input evidence. Apply the
[result index][results], [cluster11][r11], [controls12][controls],
[avoidance index][avoid], particularly [scope07][a07] and
[separate bounds12][a12]. The B02 control screen explains why this
negative certificate result is not a positive exclusion of controls.
Inherited HDA review status stays unchanged.

Record actual configuration only when available. The author chooses
the actual model and effort. Refresh the uniquely registered chat,
and arrange the bounded exact-turn final capture as the last tool
action before replying. Return the disposition, proof paths, complete
error accounting, any deviation and the next task/type/model.
Success does not automatically activate a new conceptual task.

[b02]: ../../notes/05_GNP_RS_B02_JENSEN_AND_SHIFTED_ZETA_COMPARISON_20261111.md
[decision]: ../../brainstorm/notes/03_GNP_RS_B02_DECISION_20261111.md
[e01]: ../../notes/03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_PROOF_20261111.md
[e01-review]: ../../reviews/03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_SELF_CHECK_20261111.md
[record]: ../../numerics/04_GNP_RS_B02_INPUTS_AND_HANDOFF_20261111.json
[results]: ../../../../../../result-summaries/README.md
[r11]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
