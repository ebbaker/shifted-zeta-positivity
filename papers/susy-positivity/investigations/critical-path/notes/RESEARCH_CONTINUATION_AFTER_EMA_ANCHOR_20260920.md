# Continuation after the arithmetic EMA anchor

20 September 2026. Prepared for Edward Baker.

**Model:** OpenAI GPT-6 (Codex; system-provided identity).
**Reasoning effort:** not exposed in this reviewing session.
The preceding audited task used Extra High according to Baker.

## What is now established in this investigation

Read these in order:

1. [Review of the completed adaptive-EMA work](../reviews/ADAPTIVE_EMA_REVIEW_20260920.md).
2. [All-input original-transfer anchor](EMA_TOWER_ORIGINAL_TRANSFER_ANCHOR_20260920.md),
   especially Sections 2--5 and 7.
3. [Previous audit and pilot](ADAPTIVE_EMA_AUDIT_AND_PILOT_20260920.md)
   for the smoothing comparisons and limiting lemmas.
4. [Cumulative storage and depth continuation](../../wilson-loewner/notes/SHIFT_FLOW_CUMULATIVE_STORAGE_AND_CRITICAL_PATH_20260919.md)
   and Wilson--Loewner SI continuation for the triangular depth identity.

The new certificate proves
\[
 Q_{0,1/2}\succeq I/40,\qquad
 D_{10^{-3},1/2}\succeq0.000049998\,I
\]
on all inputs. In fact contraction holds for every
\(0<\omega\le10^{-3}\) at this window.
The proof uses a finite part of the **fixed arithmetic EMA tower**
as a lower operator, retains its endpoint response and both pole
terms, and bounds the whole complementary input space. It then
integrates a bounded \(O(\omega^2)\) generator perturbation.
The 40- and 60-digit outward rational certificates agree on their
rounded bounds.

The prior pilot's omitted-input gap at the designated anchor is
therefore closed. This is a methodological result on a window well
inside the project's previously certified range, not a new
positivity horizon. Additional output smoothing did not provide
the certified margin. Input smoothing preserves the same bound
relative to \(S_\ell^*S_\ell\); no efficiency advantage is established.

## Recommended next bounded investigation

Study the **normalized cumulative depth coupling** for
\[
 L=\tfrac12,\qquad h=\tfrac1{20},\qquad
 L+h=\tfrac{11}{20}<\log2,\qquad\omega=10^{-3}.
\]
Write the original transfer as
\[
 V_{\omega,L+h}=\begin{pmatrix}X&0\\Y&Z\end{pmatrix}
\]
and analyze
\[
 \mathcal C=(I-ZZ^*)^{-1/2}Y(I-X^*X)^{-1/2}.
\]
The diagonal defects are strictly positive by the new anchor
and restriction to shorter windows. Establish a rigorous bound
on \(\|\mathcal C\|\), or a precisely quantified obstruction for
the chosen bound.

Start with these concrete steps:

1. Derive the append response \(Y\) from the complete prime-free
   kernel. Carry the fixed EMA memory and the signed pole states
   across the join, checking reflection and the output defect
   \(I-ZZ^*\). An artificial reset of these states changes the
   problem.
2. Measure the finite-input cumulative coupling using complete
   output integrals and compare it with the instantaneous central
   coupling. Use the comparison to identify which weak directions
   and endpoint terms matter. Label it diagnostic until both
   input complements and numerical errors are bounded.
3. Test whether the new finite-tower/endpoint decomposition helps
   enclose the cumulative mixed block. Do not assume that an
   operator lower bound for \(Q_0\) can simply be exponentiated
   through a nonnormal flow. The scalar anchor bound alone may
   be much too coarse after defect normalization; quantify that
   loss before increasing the numerical dimension.
4. If feasible, certify \(\|\mathcal C\|<1\). Otherwise record the
   exact missing bound with numerical scales and a reproducible
   calculation. A proof that independently certifies the larger
   central form would validate the test window but would not,
   by itself, solve the requested cumulative coupling estimate.

This append is a controlled proof-method experiment before a
prime threshold. Only after it is understood should the same
method be tested across \(\log2\), with the exact prime delay
included. No statement about arbitrarily large depth follows
from finitely many successful appends.

## Constraints and pitfalls to preserve

- The research target is cumulative positivity of the original
  arithmetic transfer. Instantaneous positivity is sufficient
  where proved, but is not a necessary condition for the program.
- Preserve identity initial normalization, causal support, the
  fixed local coefficient, and exact pole cancellation.
- The gamma-tail proof used **positive-form order**, not a
  uniform operator-norm tail estimate. Its derivative-dependent
  bound cannot be applied to arbitrary omitted inputs.
- Output-filter storage and path-average variance cannot be
  counted as arithmetic positivity. Two-sided input smoothing
  uses the metric \(S_\ell^*S_\ell\).
- The earlier audit's claim that its estimate necessarily needs
  \(N\ell\omega\to\infty\) is weakened by the review: a sufficiently
  large constant can suffice. Fixed dimension still fails for
  that old estimate.
- No arithmetic Loewner driver, localizing supercharge, physical
  Wilson norm identity, or all-depth path exists in the results
  established here. The localization proposal remains a separate
  possible explanation of the prescribed spectrum/cancellation.

## Deliverables and preservation

Save the calculation or scoped obstruction in a new research
note; put code and small certificate records in the numerics folder.
State the actual exposed model identity and effort information.
Preserve earlier dated notes, provenance, and manuscript snapshots.
The current manuscript pair is v0.4; these EMA developments have
not yet been integrated into a new manuscript version.

Useful replay commands are in Section 8 of the anchor note.
The [review/anchor provenance record](../numerics/records/ema-review-anchor-provenance-20260920.json)
identifies the files and verification results. Standard-library
arithmetic suffices for the anchor certificate; NumPy is used
only by its separate diagnostic checker and the older pilot.
