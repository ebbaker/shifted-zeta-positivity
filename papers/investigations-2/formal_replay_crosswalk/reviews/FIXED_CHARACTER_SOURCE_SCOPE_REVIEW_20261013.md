# Fixed-character dictionary source scope review

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
reasoning effort are not exposed and are not inferred.

Reviewed `7_FIXED_CHARACTER_ROW_DICTIONARY_SOURCE_PASS_20261013.md` against
the available pinned source files and bundles. This is a same-family source
review, not external independent validation. No VM, network, Lean build or
research-repository mutation was used. The new combined applications remain
uncompiled.

**Finding: no concrete defect found in the conditional coefficient dictionary.**
The source-level conclusion is properly conditional on supplying an admissible
`HeckeFamily.Character eta` with global-unit triviality and coefficient
agreement with the actual O5 input on ideals prime to the declared `S`.
Agreement on that domain is sufficient: the fixed row mask kills all other
columns. The note does not claim a compiled generic idelic-to-residue bridge.

- `m = lambda * 2 * product(g_P)` and `f = 1` supply the required nonzero and
  divisibility data. Exact prime support `S` follows once the stated
  generators and the primes above two and three are transported into the
  finite ideal product; that combined construction is explicitly pending.
- The sixth-power factor is a coprimality indicator on supported columns,
  rather than an everywhere-one factor. Unsupported columns vanish by the
  separate row theorem and already belong to the exclusions. The original
  defining-modulus zeros stay in `idealCoeff eta`. Removing an imprimitive
  modulus mask would change the sum, and the note correctly rejects that
  replacement.
- `sexticChar_reduce_unit` gives the positive exponent
  `(N(P)-1)/6`, matching the O5 orientation. Its zero theorem and the complex
  embedding agree with the stated local convention. Multiplication in the
  denominator gives the squarefree-column product needed after Möbius
  weighting; it imposes no squarefree condition on element rows.
- `idealCoeff_span` uses global-unit triviality to remove the column
  generator choice. Each ideal is counted once, so the polynomial dictionary
  has no factor of six. Unit multiples of element rows remain distinct rows;
  a unit-column lemma does not justify dividing their moment by six.
- The specialization theorem has precisely the complex prefactor
  `(D : C)^(-1/2)` and, at zero analytic twists, no further weight factor.
  For positive `D` this is `D^(-1/2)`; the ideal absolute norm supplies the
  same argument of `W`. Finite-support and primary-generator transports are
  still application obligations, as the note states.

All nineteen Lean-source hashes listed in the note match both the available
bytes and the preserved source-closure manifest. The checked declarations
support the paper-level conditional identity
`P_u(D) = D^(-1/2) A_u(D)` for every nonzero element row and positive `D`.
This review does not close the remaining Lean obligations, the classical
presentation obligation, or the full O5 crosswalk.
