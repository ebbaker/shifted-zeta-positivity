# Continuation after the cumulative-energy HS obstruction

20 September 2026. Prepared for Edward Baker.
Model: OpenAI GPT-6 (Codex; developer-provided identity).
Effort setting: not exposed in this session; not inferred.
Status: internal analytical calculation and exact rational scalar checks;
specialist review of the reduction and inherited anchor remains outstanding.

Read [CUMULATIVE_ENERGY_HS_OBSTRUCTION_20260920.md](CUMULATIVE_ENERGY_HS_OBSTRUCTION_20260920.md)
before resuming. The objective is still the **operator norm** of the complete
cumulative coupling at \(L=1/2,h=1/20,w=10^{-3}\). No upper bound below
one for that norm was obtained in this session.

## New results that constrain the next calculation

1. The Gaussian review's compactness observation was proved under the actual
   finite-window hypotheses. Positive-shift kernel continuity holds away
   from zero; a uniform Young bound below 1.01 handles zero independently
   of positivity, while the anchor improves it to 1. Every finite-tower
   \(K_M\) is compact. The actual defects are identity minus compact.
2. The lower metrics
   \[
   A=\theta_L\delta I+(1-\theta_L)K_{32,L},\qquad
   B=\theta_h\delta I+(1-\theta_h)J_hK_{32,h}J_h
   \]
   are legitimate for strictly positive weights, with \(A\preceq E\),
   \(B\preceq F\). They retain the actual cumulative finite-tower energy.
   Their caps are \(A\preceq.00664I\), \(B\preceq.00483I\).
   Do not replace this convex combination with a sum of lower bounds.
3. Put \(\mathcal B=B^{-1/2}YA^{-1/2}\). For **any rank-16 head on
   each normalized space**, including exactly energy-orthogonal logarithmic
   heads, the remaining block obeys
   \[
   \|P_{\rm new}^{\perp}\mathcal B P_{\rm old}^{\perp}\|_{\rm HS}^2
       \ge2.36932194232857\ldots>9/4.
   \]
   This is uniform over both positive convex weights. At weights one half
   its squared HS norm exceeds 9.31008499787307. Thus using HS as the
   last entry of the two-by-two comparison matrix cannot certify a norm
   below one, even if the other three entries were computed exactly.
   **This is not a lower bound above one for the operator norm.**
4. The explicit split uses 16 unit vectors proportional to \(r^{-1/2}\)
   on successive logarithmic bands \([he^{-4(j+1)},he^{-4j}]\), then
   forms heads through \(A^{1/2}\), \(B^{1/2}\). No metric cross block
   is dropped. The rank obstruction follows from the whole corner's HS
   mass and is independent of head design. It applies up to total rank
   35; the bound is inconclusive from rank 36. It says nothing adverse
   about the earlier 32-per-side finite diagnostic or an optimized
   operator-norm method at that rank.
5. There is a constructive exact-defect alternative: if \(\|V-W\|\le
   \varepsilon\), then \(D\succeq I-W^*W-(2\varepsilon+\varepsilon^2)I\).
   At \(\varepsilon=\delta/10\) the latter retains at least \(\delta I/2\).
   But simply cutting off delays \(u<10^{-p}\) cannot meet that transfer
   tolerance unless \(p>5296.682562\ldots\). The singular diagonal needs
   analytic treatment in that route. This is a cutoff-method obstruction,
   not a general finite-rank complexity lower bound.

## The unresolved block and a specific useful next test

The normalized **complement/complement operator norm** is the fatal missing
bound for the attempted method. All four operator blocks have valid but
loose bounds in the new note; neither one-sided complement has been shown
small enough to close the two-by-two test. Do not report them as certified
small, and do not mistake the HS obstruction for failure of the coupling.

The next useful calculation is a spectral-norm estimate in the logarithmic
corner variables, or an exact identity-minus-compact metric that keeps the
fractional diagonal analytically. The leading transformed kernel is
\[
 A_wh^w e^{-w(x+y)/2}[2\cosh((x-y)/2)]^{w-1}.
\]
The exact signed correction and the metric action must accompany it.
This formula exhibits a convolution-like transverse profile and a long
logarithmic envelope; counting the energy in every channel by HS is the
specific loss now quantified. A spectral Schur/Mellin estimate would need
to prove a bound for this operator in the cumulative metric and then bound
both one-sided blocks, rather than replacing the kernel by its central
zero-shift limit or increasing matrix resolution without a tail estimate.

If that estimate is attempted, produce either a closed bound with constants
or a quantified failure of that particular estimate. Do not substitute an
independent central-form certificate on the enlarged interval.

## Fixed conventions, evidence and replay

The complete beta history and both signed pole states cross the join.
The new-output defect is reflected, the local \(w_0\) is fixed, and the
shift integral follows the original nonnormal flow. No auxiliary smoothing
loss or averaging variance is arithmetic positivity. Stay below \(\log2\).
The EMA anchor \(Q_{0,1/2}\succeq I/40\), \(D_{w,1/2}\succeq\delta I\)
remains subject to specialist review. Its all-input pilot gap was closed
previously; no new positivity horizon is claimed here.

The new exact checks passed at 40 and 60 digits. The old anchor and scalar
obstruction were replayed; the old floating .802 quotient was not rerun and
remains a finite-input diagnostic, not an all-input upper bound. Reproduce
from the repository root, writing temporary outputs:

```sh
python3 -B papers/susy-positivity/investigations/critical-path/numerics/certify_cumulative_energy_hs_obstruction.py --output /tmp/cumulative-energy-hs-replay.json
python3 -B papers/susy-positivity/investigations/critical-path/numerics/certify_cumulative_energy_hs_obstruction.py --digits 60 --output /tmp/cumulative-energy-hs-replay-60.json
```

The [40-digit record](../numerics/records/cumulative-energy-hs-obstruction-20260920.json),
[60-digit record](../numerics/records/cumulative-energy-hs-obstruction-60digits-20260920.json)
and [provenance](../numerics/records/cumulative-energy-hs-provenance-20260920.json)
separate exact comparisons from decimal displays and analytic assumptions.

Preserve all historical files, existing uncommitted work, manuscript v0.5
and all snapshots. Follow LARGE_FILES.md; the calculation requires no
matrix archive. Record the actual model identity and only an exposed effort
setting. The Gaussian exclusion still concerns its specified nonlocal
preparation and endpoint; further physical work needs a new independently
specified action or observable.
