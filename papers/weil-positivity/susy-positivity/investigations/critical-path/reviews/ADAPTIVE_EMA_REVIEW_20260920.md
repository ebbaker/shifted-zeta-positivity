# Review of the adaptive-EMA audit and pilot

20 September 2026. Prepared for Edward Baker.

**Reviewer:** OpenAI GPT-6 (Codex; system-provided identity).
**Review effort:** not exposed in this session.
**Reviewed task:** “Audit adaptive EMA positivity,” reported by Baker as
having run at Extra High effort. The review does not infer its quality
from that setting and does not claim independent human or different-model
mathematical review.

## Assessment

The main conclusions of
[ADAPTIVE_EMA_AUDIT_AND_PILOT_20260920.md](../notes/ADAPTIVE_EMA_AUDIT_AND_PILOT_20260920.md)
survive this review. The larger output-smoothed margins are accounted
for by the filter's energy loss. Two-sided input smoothing has the
stated stronger limiting lemma, but fixed-shift positivity remains
equivalent to the original question. The pilot integrates complete
outputs on a finite input space and correctly refuses to treat its
positive matrices as all-input certificates.

One minor quantitative statement should be weakened, as recorded
below. No error found in this review invalidates the pilot's conclusion
or the exact certificate for its deliberately over-smoothed operator.
The useful continuation was to change the complement estimate,
not repeat the same smoothing optimization.

## Claims checked

1. **Complete arithmetic target.** Checked the absorbed beta/pole
   kernel and its symbol against the parent decomposition and the
   SI S10 response. Both pole contributions and the fixed local
   constant remain present. The inherited EMA rate is fixed by
   cancellation and is not a free smoothing parameter.
2. **Energy and endpoints.** Re-derived
   \(\|f\|^2-\|S_\ell f\|^2
   =\ell^2\|(S_\ell f)'\|^2+\ell|S_\ell f(L)|^2\).
   With nonzero incoming state, its energy belongs on the input
   side. The two missing mathematical plus signs in the original
   handoff are correctly identified by the audit.
3. **Output removal.** The audit's \(H^1\) hypothesis and initial
   trace control justify the stated estimate on fixed smooth tests.
   The distinction between \(\ell^2=o(\omega)\) for the real form
   and \(\ell=o(\omega)\) for the full first vector variation is
   necessary. No operator-norm convergence of the central generator
   follows.
4. **Input removal.** Causal convolution commutes with the EMA.
   Writing \((V_\omega-I)f/\omega\to Af\), strong convergence of
   \(S_\ell\) proves the two-sided fixed-test limit for every
   \(\ell\to0\). Dense range gives the stated fixed-shift equivalence
   of positivity, and the metric is \(S_\ell^*S_\ell\).
5. **Shift averaging.** Checked initialization, normalization by
   mean shift, the variance identity, and the condition excluding
   an old-history contribution comparable with the mean. The
   inverse-logarithmic high-frequency asymptotic for the indicated
   scale-invariant shift average is consistent with the prime-free
   symbol; averaging does not improve its decay.
6. **Pilot implementation.** The output functions are integrated
   before forming Gram matrices. The subtractive comparison removes
   the entire filter-loss matrix before diagonalizing. The parent
   central form and transfer assembler are separate evaluations.
   Quadrature refinement does not enclose all numerical errors, but
   the note consistently labels those results as diagnostics.
7. **All-input bounds.** Verified the reduced complete-kernel
   \(L^1\) majorant, EMA norm estimate, sine endpoint tail estimate,
   and the exact Fraction certificate at the broad smoothing point.
   The unresolved small-shift input complement is real for that
   particular estimate, even if the finite matrices were exact.
8. **Scope.** The audit does not assume a positive arithmetic
   Loewner driver, claim a physical realization, or infer a path
   reaching unbounded depth.

## Minor correction: resolution scaling in Section 8.2

After (8.6), the audit says that a margin of order \(\omega\)
“would require” the first complement term to be
\(o(\sqrt{\omega})\), and consequently
\(N\ell\omega\to\infty\).

For example, if
\[
 a_N^2\le1-c\omega+o(\omega),\qquad c>0,
\]
then (8.6) closes whenever \(t_N^2\le c'\omega\), with
\(c'<c\) and enough slack for the remainders. Thus
\(t_N=O(\sqrt{\omega})\) with a sufficiently small constant can
suffice. For the first term in (8.5), this allows \(N\ell\omega\)
to remain a sufficiently large positive constant. Divergence is
a sufficient requirement for an asymptotically negligible tail,
not a necessary one for that estimate to close.

This correction does not rescue fixed \(N\): under
\(\ell\to0,\ \omega\to0\), fixed \(N\) still fails badly.
It also does not establish a complexity lower bound for another
representation. The original dated audit is retained; this review
is its correction record.

## Replay and provenance

The repository was clean at the beginning of the review, at commit
227fab6. Every file hash listed under "current_files" and
"local_inputs" in the preceding audit provenance matched before
the present index updates.

- Replayed all three arithmetic pilot configurations. The pilot's
  acceptance checks passed. The largest normalized N=24 refinement
  difference remained \(2.382672642520234\,10^{-9}\).
- Replayed the exact coarse certificate. Its full JSON result
  matched the historical result, including
  \(987339385394/10^{12}<1\).
- Replayed all 57 inherited EMA controls; all passed.
- Compared the pilot's numerical payload with its saved run,
  excluding elapsed times. There were 589 changed numerical
  leaves; the largest absolute difference was
  \(1.1102230246251565\,10^{-11}\), in a small-shift toy quotient.
  This is a successful numerical replay, not a claim of bitwise
  reproducibility across numerical-library threading/configuration.
  No causal attribution for the last-bit differences was established.

Replay outputs were written to temporary files, preserving the
historical records. Source-authorship and effort fields emitted
by the old script describe its original task, not this review's
runtime settings.

## Continuation completed

The [new research note](../notes/EMA_TOWER_ORIGINAL_TRANSFER_ANCHOR_20260920.md)
proves a lower bound for the complete central form using 32
prescribed gamma EMA terms, a 16-mode cosine head that retains
endpoint values, and rigorous bounds on the entire input
complement. A bounded shift perturbation and the actual evolution
equation then give
\[
 I-V_{10^{-3},1/2}^*V_{10^{-3},1/2}
 \succeq0.000049998\,I .
\]
This closes the specific original-transfer anchor requested by the
audit. It uses instantaneous positivity as a sufficient tool at
this small window; it supplies neither a new known depth horizon
nor an all-depth continuation argument.

The new arithmetic certificate passes at 40 and 60 decimal places.
A separate direct-response calculation agrees with its matrix
reduction to \(3.7\,10^{-14}\), and 130 exact-arithmetic control
cases pass. Those checks and the analytic proof remain subject to
specialist review. The
[continuation handoff](../notes/RESEARCH_CONTINUATION_AFTER_EMA_ANCHOR_20260920.md)
now prioritizes normalized cumulative depth coupling.

The earlier audit, its provenance, and the Wilson--Loewner v0.4
manuscript/supplement snapshots remain unchanged.
