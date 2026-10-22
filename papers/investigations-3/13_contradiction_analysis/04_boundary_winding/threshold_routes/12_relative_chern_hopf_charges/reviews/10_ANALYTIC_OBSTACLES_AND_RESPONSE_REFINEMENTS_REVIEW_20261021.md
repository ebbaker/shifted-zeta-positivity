# Review of the analytic obstacle assessment and response refinements

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**. Separate agents of the same model assessed
the signed-source and coverage questions and checked the refinements;
the producing assistant reconciled their findings. This is internal
LLM review, not independent specialist validation.

The [assessment in Note 10][note] correctly identifies the distinguishing
theta sign as the immediate obstacle. Pointwise event geometry is already
paid; all-height signed error control and exclusion of higher multiplicity
remain open. Its preference for the fixed-time endpoint response is a
research judgment based on fewer additional hypotheses than the event
homotopy route, not a theorem that this method will succeed.

## Mathematical checks

1. Expanding log(1+e) through its quadratic term gives the signed correction
   Q=2I[(z−c)e²]−(I[e])² and remainder
   4R(R+r)l_3+R²(2ρl_2+l_2²). The logarithmic-series bounds and the
   difference-of-squares estimate prove the stated O(ρ³) error. Q has
   no general sign and includes complete-residual cross terms. The
   note does not claim that it improves every finite-ρ enclosure.
2. Integrating interval bounds for C_K against the actual canonical
   probability law gives the mass-weighted enclosure. Exact masses make
   refinement nested. The last unbounded interval and its probability
   are retained. The warning about negative integrands and interval-valued
   mass errors is necessary. A narrower interval supplies no sign itself.
3. For a fixed m-root cluster, δS_1=−I[ℓ] and δS_2=−2I[(z−a)ℓ]
   give the exact centered-variance response, including the coefficient
   1/m in its square. Its first-order allowance and the full-birth residue
   −2∂_z^(m−2)(E/U)/(m−2)! are correct. This retains the exterior unit.
   A positive V excludes only full coalescence of all retained roots.
   The cubic control with roots (−2,1,1) has V=6 despite a partial collision.
4. The canonical linear expectation representation extends to the variance
   kernel under the displayed source and contour bounds. The specifically
   two-root kernel-oscillation theorem does not automatically extend; the
   note states this limitation.
5. The head–tail cancellation statement follows directly from Δ_H=0
   and the response enclosure. It explains why tail convergence does not
   create a signed surplus. No assertion of a true theta double is made.

The integrated-note review corrected scope phrases before installation:
the strict matched-envelope gain requires both reference roots in Re z>0;
and a positive endpoint lower bound must be tested against a control at
that same endpoint with the relevant vanishing observable. An allowed
negative-time event does not invalidate a positive endpoint discriminant.
It also made the full-birth premise explicit next to the discriminant
asymptotic and specified reality for both the reference and final fields.

## Control replay and evidence

The existing standard-library [exact control program][script] was replayed.
All checks passed and its parsed output exactly matched the [saved
receipt][receipt]: seven Hermite multiplicities, five exterior-forcing
clusters, three cubic identities, three quadratic responses and the
boundary-paid homotopy controls. This replay supports the existing
controls; the new response refinements are proved algebraically in
Note 10. No new theta-source acquisition was performed.

The primary [Rodgers–Tao statement][rt] was checked for the threshold and
nonnegativity claim. It prohibits a common negative all-real time slice,
not cluster-dependent negative caps. Height bounds in the assessment
are upper bounds for the manuscript's chosen window prescription, not
necessary scales or lower bounds for unknown root gaps.

## Status

The assessment and elementary estimating refinements do not change the
main task statuses. ECE-01 retains its parameterized completion;
ECE-02, the signed part of ECE-04 and higher-multiplicity exclusion in
ECE-05 remain open. ECE-03 and ECE-06 remain gated. No positive theta
margin, endpoint exclusion, or manuscript revision is asserted.

This assessment follows the [result index][results], [control register][controls]
and [avoid index][avoid], especially [scoped exclusions][scope] and
[coupled estimates][coupled].

[note]: ../notes/10_ANALYTIC_OBSTACLES_AND_ESTIMATION_PRIORITIES_20261021.md
[script]: ../numerics/ece_exact_controls.py
[receipt]: ../numerics/ECE_EXACT_CONTROLS_20261021.json
[rt]: https://arxiv.org/abs/1801.05914v5
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[coupled]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
