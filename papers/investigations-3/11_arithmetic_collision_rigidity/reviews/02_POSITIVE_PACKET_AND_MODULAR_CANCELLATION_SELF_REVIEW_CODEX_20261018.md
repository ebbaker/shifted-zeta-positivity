# Self review of positive packets and modular cancellation

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Reviewer **gpt-6-astra (Codex)**, reasoning effort **max**,
verified from the authoring turn metadata.

**Review type: self-review by the same assistant that derived the result and
wrote the checker.** No independent LLM or specialist review is claimed.
Disposition: the positivity, explicit relative estimates and bounded carrier
payment have written analytic proofs and the stated constant checks. The
signed residual estimate and theta collision exclusion remain open.

## Sources and versions

| Source | SHA-256 |
| --- | --- |
| [Note 04][note] | 350ee6391f9b44699a5d01361af3d1dc98da8cd24247056411998f772e565500 |
| [Checker][code] | 62dd5da6d1a834ae581149b863a511417f7c0246d9def06add00f2e9c2176e5a |
| [Execution record][record] | 3817380d1e171b29ec2bb38a8a1f76d69e4f57c8090d769273f5b0fd7ad9c264 |

The [result summaries][summaries] and [patterns to avoid][avoid] govern the
assessment, particularly [control premises][a02], [same-model limits][a05]
and [preserving the cancellation][a12]. This is a bounded research milestone,
not a manuscript or Newman-bound milestone.

## Analytic checks

1. **Which transform is positive.** Logarithmic differentiation of the
   physical mode, including its polynomial factor, gives the 9 and
   12/(2a-3) in Note 04 (1). For n>=2 and 0<=t<=1/2, the two source
   inequalities imply g''/g>=7a^2. The proof does not apply to n=1 or to
   the complete even source. Integration by parts yields the positive
   measure g''(u)du against (1-cos(xu))/x^2; x=0 is handled separately.
   Bounded nonnegative coefficients justify summation and differentiation.
2. **Packet identification.** Inclusion-exclusion makes G_2+G_3-G_6 the
   selector for indices divisible by 2 or 3, each with coefficient one.
   Those are the complete packets, so the shifted half-line prefactors,
   reflected signs and lower intervals established in Note 02 remain.
   Positivity has not been assigned to separately evaluated shifted terms.
3. **Uniform lower bound.** On [0,1/64], a<14 and log(g_2)' > -47.
   Hence g_2''>=336 phi_2(0). The elementary sinc inequality, integrated
   against this lower bound, gives kappa/(4096+x^2). This lower bound
   uses the included n=2 mode, so (5) and subsequent uniform constants
   require that P contain 2. No physical-jet nonvanishing is assumed.
4. **Tail comparison.** The quadratic term in e^(4u)>=1+4u+8u^2 absorbs
   the heat weight throughout [0,1/2]. Geometric majorants give S_m, Q_m
   and epsilon_j. Convexity gives the second, inverse-square bound for
   the tail; combining it with the absolute moment bound makes the
   relative estimate uniform in height. Absolute moment bounds alone
   would not establish this result.
5. **Derivative estimates.** The moments of g'' are -g'(0), g(0), and
   2 integral(g). Differentiating the positive representation gives (11).
   Splitting at |x|=64 yields (12), including the factors 8192, 1/8 and
   3/512. Applying the same bounds to A_P with m=2 and differentiating
   R_P/A_P gives (13)–(15). All assertions concern the real axis; complex
   nonvanishing of the carrier is not inferred.
6. **Energy payment.** In H=A_P q, the cross terms cancel exactly in
   H_x^2-H H_xx, leaving (18). The carrier payment is bounded by 117 H^2
   and therefore 117 E. The remaining A_P^2(q_x^2-q q_xx) is still signed.
   The transformed heat equation has the displayed minus drift sign.
7. **Full modular coupling.** The normalized theta inversion makes the
   complete weighted source even, so every odd source endpoint cancels.
   This gives (22) and the full hierarchy, not just the one checked
   endpoint. The individual positive packets have inverse-square tails;
   the complete physical field is rapidly decreasing. Thus the finite
   approximation H_1+A_P is eventually negative because it omits the
   strictly positive R_P. This conclusion is scoped to that truncation.

## Checks and their limits

The recorded run used Python 3.12.14, python-flint 0.9.0, and 384-bit Arb/Acb
arithmetic. It took approximately 0.023 seconds and used about 39 MB peak
resident memory. It certifies the constants, including rho_5<7.3e-25,
the first two quotient-derivative bounds, and B_2+B_1^2<117.

An endpoint sum through n=8 with a rigorous all-index tail from n=9 encloses
the first modular cancellation; it also encloses q_R/q_A>0 for P={2,3}.
Eight finite-interval integrations cover n=2,5, t=0,1/2 and x=32,128 with
upper endpoint 1/8. Their integration-by-parts residual enclosures contain
zero and are below 1e-90. Omitting the upper boundary fails each check.
These finite identities check implementation and normalization; the global
convexity and all-height estimates are proved by inequalities in the note.
The existing packet checker's shifted identities were not rerun or modified.

## Scope and continuation

The gain is concrete: positive complete arithmetic packets, a nonzero
carrier with uniform first and second logarithmic-derivative bounds, a
uniform relative two-prime remainder and a bounded carrier energy payment.
The convex-kernel method is classical and already used for the repository's
different positive primitive; no literature novelty is asserted.

Positive weighted-square and finite-prime orbit controls also possess the
new positivity property. They fail full modular reflection, not this
auxiliary estimate. Reflected smooth and Euler-factor controls fail the
unchanged normalized theta square data in the relevant ways recorded in
the source catalogue. No control is claimed to pass both full unchanged
arithmetic and normalized reflection.

The necessary collision band is not an excluding estimate: its limiting
value at high height lies inside the band. Likewise, the tiny but fixed
relative remainder is not small relative to a vanishing physical field.
The next substantive task is a signed estimate on the complete residual
with modular cancellation retained. A new norm for the same positive
carrier, or another rewriting of (18) without that estimate, would not
constitute further collision progress.

[note]: ../notes/04_POSITIVE_ARITHMETIC_PACKETS_AND_MODULAR_CANCELLATION_CODEX_20261018.md
[code]: ../numerics/check_positive_packets.py
[record]: ../numerics/POSITIVE_PACKET_BOUNDS_20261018.json
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a05]: ../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
