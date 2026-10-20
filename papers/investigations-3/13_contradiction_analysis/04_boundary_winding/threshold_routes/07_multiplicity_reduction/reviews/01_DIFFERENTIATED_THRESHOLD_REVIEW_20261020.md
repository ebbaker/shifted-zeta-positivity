# Internal review of the differentiated threshold transfer

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Review by the parent **gpt-6-astra (Codex)**,
actual effort **ultra**, plus a separate same-model agent's analytic
check. This is internal LLM review, not independent specialist review.

**Assessment: the conditional reduction in [Note 02][note] is supported.**
The important assertion is equality of the transformed threshold, not
just preservation of a double zero. The proof establishes it without
applying a theorem about the unchanged theta source to a changed source.

The parent checked the full proof and replayed the [checker][checker]:
14 polynomial cases and 14 positive two-atom cases pass. The second
agent independently read the threshold and odd-source arguments and
reported no substantive defect; that agent did not replay the checker.
Finite controls check algebra and conventions, not the universal claims.

The decisive checks were:

- Paired-product polynomial approximations and Rolle/Hurwitz give
  differentiation closure. For any earlier all-real derivative slice,
  the operators (1-s∂²/n)^n preserve real zeros and converge to its
  forward heat flow by dominated convergence on the complete source.
  A surviving double event has nonreal immediate predecessors. These
  two facts prove that its all-real threshold is exactly T.
- The signs in the cosine/sine source and xi-derivative identities are
  correct. The odd case uses u coth(bu), with increasing tilt
  u^k tanh(bu) relative to the original cosh measure. Its permanent
  simple origin contributes 1/a² to the deflated sum and 1/b² to the
  imaginary-axis comparison; the difference is nonnegative for b>=a.
- The necessary bound and finite critical-value estimate really
  transfer. Original derivative orders extend through m+4. The
  generalized tail has the required negative tangent slope and
  concavity, and its two regions cover all omitted source contributions.
- The derivative jet is not a pointwise coordinate change of (H,Hx).
  Its degree -1 differs from the physical -floor(m/2) when m>=4;
  equality of those integers for m=3 proves no boundary homotopy.

The scope statement is essential: **“This is not a reduction of a proved
exclusion theorem: no such BW-01 theorem is available.”** Equality of
thresholds is conditional on the exact m-fold event that leaves a double
zero after m-2 derivatives. It is not asserted for arbitrary derivatives
without that surviving event. The full theta source changes, even though
the particular positive-source lower bound survives that change.

No numerical theta jets, new region, later contradiction or global
exclusion have been obtained. A useful continuation needs an opposing
arithmetic estimate on this derivative-weighted class, with its actual
source errors; repeating the necessary bound is not an induction.
This classification follows [target discipline][a01], [control
screening][controls] and [same-model review limits][a05].

[note]: ../notes/02_DIFFERENTIATED_THRESHOLD_TRANSFER_20261020.md
[checker]: ../numerics/check_differentiation_closure.py
[record]: ../numerics/DIFFERENTIATION_CLOSURE_CONTROLS_20261020.json
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
