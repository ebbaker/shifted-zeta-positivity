# Continuation after the all-input cumulative operator-coupling certificate

20 September 2026. Prepared for Edward Baker.
Model: OpenAI GPT-6 (Codex; developer-provided identity).
Effort setting: not exposed in this session; not inferred.
Status: internal computer-assisted proof with exact rational checks;
independent specialist review remains outstanding.

## Result to retain

Read [CUMULATIVE_OPERATOR_COUPLING_CERTIFICATE_20260920.md](CUMULATIVE_OPERATOR_COUPLING_CERTIFICATE_20260920.md).
At the original fixed test
\[
 L=1/2,\quad h=1/20,\quad w=10^{-3},\qquad
 E=I-X^*X,\quad F=I-ZZ^*,
\]
the new analytic reduction and rational certificate establish internally
\[
 \boxed{\|F^{-1/2}YE^{-1/2}\|<951/1000.}
\]
This closes the all-input coupling estimate for this append. It is not
a new positivity horizon, an all-depth theorem or a physical realization.
The inherited floor \(E,F\succeq\delta I\), \(\delta=.000049998\),
and its outstanding specialist-review status are unchanged.

The proof's new step is a forward/backward energy-transfer lemma. For the
original triangular generator with lower mixed block \(-2H_s\),
\[
 Y=2\int_0^w U_h(w,s)H_sV_{s,L}\,ds,
\]
\[
 E[f]=2\int_0^w Q_{s,L}[V_{s,L}f]ds,\qquad
 F[v]=2\int_0^w Q_{s,h}[U_h(w,s)^*v]ds.
\]
A uniform relative bound \(|\langle v,H_sf\rangle|\le
\kappa\sqrt{Q_{s,L}[f]Q_{s,h}[v]}\) yields the **same** upper bound
\(\kappa\) for the cumulative coupling. The backward output energy is
essential. No bounded inverse of \(V_s\), or operator exponential of a
lower metric, is used.

## Explicit constants and omitted-space control

The finite lower tower uses \(M=128\), with 32 endpoint-aware cosines on
each local window. All metric cross blocks are retained through certified
Young bounds with parameters \(1/40\) and \(1/200\). The resulting
complement metric floors are 2.78 and 3.6874. The four mixed operator blocks
are bounded by
\[
 \begin{pmatrix}.87&.265\\.081&.493\end{pmatrix},
 \qquad\|\cdot\|<.95.
\]
The full noncompact central gamma corner is bounded by the Carleman operator
norm \(\pi/2\), with the signed pole added explicitly. Both one-sided
complements include analytic tails beyond mode 2047. No corner HS norm is
used. The finite matrices do not alone imply the result.

The local shift perturbation is at most \(s^2/8\); the mixed perturbation
has norm below \(2.6516720750\,10^{-7}\). Together they give the uniform
relative bound below .950012797294, rounded outward to .951.

The actual defects are still identity minus compact. Finite integrated
lower energy forms can remain compact: the new proof uses them as storage
maps and never inverts them. This explains why the earlier compactness
audit and [HS obstruction](CUMULATIVE_ENERGY_HS_OBSTRUCTION_20260920.md)
remain valid and do not contradict the new result.

## Review priority and the next bounded research decision

The next review should audit the evolution-domain construction, the
forward/backward identity, all factors of two and reflections, and the
infinite-complement reduction in Sections 3--6 of the new note. The source
includes explicit rounding, Gram errors and positive-series controls;
replaying it is necessary but does not replace that mathematical review.
Do not mark specialist approval complete on the strength of another
same-model replay.

The all-input test at this \((L,h,w)\) no longer needs another resolution
sweep. If continuing the arithmetic research after review, the substantive
question is which constants and energy-transfer hypotheses persist under
a further append. The current proof depends on positive **local**
instantaneous forms; it does not handle their failure, establish a
nonaccumulating sequence of depths, or cross the first prime delay. Any
extension must retain the exact new delay terms when they enter. An
independent central certificate on a larger interval alone would not
establish such a continuation invariant.

Keep the complete beta history, both signed pole states, fixed local
coefficient, identity initial normalization and reflected new-output
defect. Auxiliary smoothing loss and averaging variance remain separate
from arithmetic positivity. The Gaussian physical branch is unchanged and
needs a new independently specified action or observable before resuming.

## Reproduction and preservation

The exact certificate passed at 40 and 60 digits; the rational comparison
matrix, its determinant slack and the small control matrix agree, and all
12 recorded interval enclosures are nested at the higher precision. Ten
digamma-based pure-series coefficients passed independent positive-series
and integral-tail enclosures. A separate physical-delay quadrature agrees
with the first 8-by-8 mixed block within \(5.016\,10^{-13}\). The latter
is a floating diagnostic, not a sign certificate.

From the repository root, preserving the saved records:

```sh
python3 -B papers/susy-positivity/investigations/critical-path/numerics/certify_cumulative_operator_coupling.py --output /tmp/cumulative-operator-replay.json
python3 -B papers/susy-positivity/investigations/critical-path/numerics/certify_cumulative_operator_coupling.py --digits 60 --output /tmp/cumulative-operator-replay-60.json
python3 -B papers/susy-positivity/investigations/critical-path/numerics/check_cumulative_operator_reduction.py --certificate /tmp/cumulative-operator-replay.json --output /tmp/cumulative-operator-reduction-replay.json
```

Saved records:

- [40-digit certificate](../numerics/records/cumulative-operator-coupling-20260920.json)
- [60-digit certificate](../numerics/records/cumulative-operator-coupling-60digits-20260920.json)
- [Independent reduction checks](../numerics/records/cumulative-operator-reduction-checks-20260920.json)
- [Provenance](../numerics/records/cumulative-operator-coupling-provenance-20260920.json)

Follow LARGE_FILES.md. Only code, notes and small records were added; no
matrix archive is needed. All 337 pre-existing files checked in critical-path
and wilson-loewner, including manuscript v0.5, snapshots, and uncommitted
research, were preserved. Record actual model identity and only an exposed
effort setting in subsequent notes. This research proof has not been
silently incorporated into a manuscript or treated as specialist-reviewed.
