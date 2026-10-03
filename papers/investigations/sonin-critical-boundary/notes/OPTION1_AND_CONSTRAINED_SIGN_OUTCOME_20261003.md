# First prime continuation outcome

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Exact serving variant and configured reasoning effort were not exposed and are not inferred. The calculation and analytic argument were checked by separate same-model agents and the lead agent; this is internal research, not independent specialist refereeing.
Repository baseline: `c943006b5003dad7ac48afc7689e7273f30c267a`. The earlier assessment file was already untracked when this continuation began.

The requested continuation had two parts: attempt a one-sided actual-Sonin trace certificate for the existing odd source, then investigate nonpositivity on the full prepared mean-zero class. The first part produced an inconclusive numerical pilot. The second produced an analytic obstruction: the constrained sign is false at the first-prime gate. The obstruction also excludes domination of this correction by any finite-rank nonnegative penalty.

The detailed proof is [First-prime translated resonance](FIRST_PRIME_TRANSLATED_RESONANCE_20261003.md), with a [separate proof audit](../reviews/FIRST_PRIME_RESONANCE_REVIEW_20261003.md). The result uses actual operators and an asymptotic source family; it does not depend on a numerical correction sign.

## The original odd source remains undecided

The [actual-Sonin pilot](../numerics/first_prime_actual_sonin_pilot_20261003/README.md) uses exact mathematical columns obtained from the archimedean projection and finite-place transport, and computes numerical proxies to their finite-output trace. It retains the identity complement of the prolate inverse and reduces the entire transported Gram to compact integrals.

Increasing the trial dimension through 160, 320, 640 and 1280 gave approximate traces 0.8783061, 0.9815153, 1.0210491 and 1.0314268. None exceeds the inherited arithmetic upper endpoint 1.047808594. A joint quadrature/rank/output-grid refinement changed the 640-dimensional value by about 1.68e-5; replacing its prolate inverse by the midpoint of the certified model changed it by about 2.21e-12. These sensitivities are not rigorous error bounds.

The arithmetic input bindings were verified, the prime correlation computation was replayed with Arb/Acb, and the inherited rank-32 prolate gap and inverse certificate were rebuilt. Their success does not enclose the pilot's remaining quadratures or floating arithmetic. No new certified trace lower endpoint or correction sign was obtained for the original broad odd bump. The tested trial family had no positive margin to certify, so the bounded pilot stopped before an expensive interval implementation.

## The constrained sign has an analytic obstruction

Set a=log 2, take a nonzero compact smooth real g with zero integral, and let epsilon=2 to the power minus N. Define

\[
h_\varepsilon(x)=\varepsilon g(x/\varepsilon),\qquad
H_\varepsilon(x)=h_\varepsilon(x+a/2)+h_\varepsilon(x-a/2),\qquad
F_\varepsilon=(-\partial_x^2+1/4)H_\varepsilon.
\]

For sufficiently small epsilon these sources lie strictly inside the length-one window. Their pole moments and ordinary mean vanish exactly. The proof establishes

\[
K_{\{2\},1/2}[F_{2^{-N}}]\longrightarrow\Lambda_2[g]>0.
\]

The first return has a translated resonance at separation log 2. Its full lacunary sinc profile yields a positive Fourier-average quadratic form. The self contributions vanish because the crossing interval shrinks at zero. Higher returns vanish because their fixed operator is trace class and the packet source multipliers converge strongly to zero. The proof keeps the log-periodic part of the profile; replacing it by an assumed continuous remainder would be unjustified.

Choosing odd or even mean-zero g gives either parity. Applying the same limiting form to any finite-dimensional profile space yields a positive correction subspace of that dimension for a common sufficiently small width. Hence the prepared mean-zero form has infinite positive index in both parity sectors. Any proposed finite-rank penalty vanishes on a nonzero vector in a sufficiently large such positive subspace, contradicting domination.

This retires the proposed mean-only upper bound and also the attempted repair by finitely many Mellin moments, already at L=1 and S={2}. The theorem does not specify a finite numerical threshold N. Its normalized positive corrections tend to zero, so numerical resolution can become difficult even though the existence proof is strict.

## What should follow this result

The result proves K>0, not K>B. The identity Q=B-K and the weaker comparison K at most B remain open; nothing here disproves Weil positivity or RH. It also leaves the earlier broad bump's sign unresolved.

The next bounded validation task is an explicit two-packet witness: derive quantitative remainder bounds, choose a finite width, and enclose the correction. A specialist review of the translated-resonance proof would independently test the central conclusion. Further work on the weaker comparison must account for an infinite family of positive correction directions; finite-rank penalties cannot remove them. This is a change in the viable research target, rather than a request for more unconstrained matrix sweeps.

No manuscript or historical research note was rewritten, no snapshot directory was created, and no commit or push was made. The investigation README is updated to distinguish the new obstruction from the older open-candidate status. Detailed numerical provenance and reproduction instructions remain beside the saved pilot records.
