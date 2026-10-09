# Scoped review of the organized short-family manuscript

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
The coordinating review and three parallel audits are same-model internal
checks, not independent specialist validation or formal proof replay.

Reviewed manuscript:
[Short sextic character families](../short_families/short_family_reductions.tex).

This review describes the initial assembly from notes 1–13. The
[cancellation addition review](SHORT_FAMILY_CANCELLATION_MANUSCRIPT_REVIEW_20261008.md)
records the later incorporation of note 15, updated source hash and
successful native compilation.

## Scope and organization

The manuscript consolidates useful results from short-family notes 1–13.
Its main route is conditional extraction followed by the zero-integral
adaptive factorization. Signed gcd truncation and transformed overlap
control remain explicit alternative reductions. Generic sieve and
actual selected-component obstructions constrain the remaining estimate.

The new reductions have proofs. The native character/Poisson package,
finite transformed representation and positive valid-range dual bound
are stated as imported inputs with their permitted scope. The generic
sextic large sieve and the quantitative fixed-field prime ideal theorem
are cited to primary sources. Lengthy ray-group calculations are
referred to the notes rather than silently used or copied.

Replication variants, unit splitting, unrestricted positive long-row
extension, triangle bounds on positive gcd moments, and repeated Poisson
without a new signed estimate are summarized as routes that give no
additional power gain, with note references.

## Coverage of the main results

| Notes | Manuscript treatment |
| --- | --- |
| 1 | Complete finite prime-mask extraction proof, prime-row equivalence, Mellin zero detection and improvement thresholds |
| 2–4 | Full original diagonal removal; actual transformed representation; exact corrected second-Poisson involution; all-scale primitive kernel; rapid sector and high-overlap block bounds; valid-range ordering and signed residual |
| 5–7 | Replication limits summarized; imported sixth-order operator and full physical-row transfer proved from it, with masks and multiplicities paid |
| 8 | General truncated Dirichlet inverse with endpoint support; exact two-factor convolution; all-scale completion; uniform centered cutoff and retained principal correction |
| 9 | Exact signed divisor recombination; high-gcd truncation including its diagonal; unchanged row scale and circular positive triangle bound |
| 10 | Conditional low-core estimate and its conductor-constant cost; complementary-core generic estimate and its remaining upper-bound terms |
| 11 | Sufficient derivative profiles; sharp-profile recovery with fixed-row boundary; combined radical modulus; weighted row mass; adaptive negligible actual sector; ordinary main square and coherent support ranges |
| 12–13 | Original prime-core and actual prime-by-prime tail obstructions; generic bilinear and maximal-threshold calculation; explicit unproved tail target and endpoint scope |

## Mathematical audit

Three parallel readings checked separate portions of the assembled source:

- Extraction and generic baseline: arbitrary-epsilon quantifiers, finite reuse,
  same profile and character, Mellin detection, native-family compatibility,
  physical row multiplicities and the general sixth-power-free column operator.
- Factorization, recovery and gcd: cutoff endpoints, overlapping factors,
  deletion zeros, principal residue, complete Schwartz weight, fixed-row
  boundary, original-row gcd normalization and conditional core constants.
- Transformed and selected-factor sections: corrected complex conjugation,
  exact exterior finite combination, complete kernels, source range,
  dyadic lower endpoints, prime ideal asymptotic and bilinear normalization.

No unresolved substantive error was found within the stated inputs.
The review clarified that the auxiliary convolution for the mean of
\(F_\beta(r)^2\) is over all integral row ideals, including primes in \(S\);
coefficient convolutions remain on the good-ideal monoid.

A new explicit general physical-operator corollary covers all
sixth-power-free coefficient vectors. It justifies using cube-free
\(c_z(d)\) columns in the grouped bilinear diagnostic; this is not inferred
from a theorem restricted only to squarefree columns.

The sharp-profile recovery uses only fixed-character \(o(t)\) for each
fixed row and \(h+a<1\). It does not introduce conductor uniformity or
recover arbitrary Schwartz all-row moments. The direct detector argument
already suffices without this optional recovery.

The prime-selected and prime-by-prime lower bounds concern selected
components in the legal specialization \(\nu=1\). They do not lower-bound
the full tail, full \(m=1\) sector or unrestricted Möbius energy.

## Source and compilation verification

The primary statements were inspected at:

- [October 5 OpenAI source archive](https://github.com/openai/math/tree/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026),
  retaining the conventions and source-scoped qualifications documented in
  notes 2–4 and their reviews.
- [De Faveri, arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1),
  Theorem 1.1 and the sixth-power-free index convention.
- [Das–Kadiri–Ng, arXiv:2508.09480v1](https://arxiv.org/html/2508.09480v1),
  Corollary 1.4, for the quantitative fixed-field prime ideal input.

The standalone source uses one TeX file, an embedded bibliography,
and standard packages. It needs no auxiliary project files.
The built-in desktop LaTeX compiler successfully compiled the final source.
A failed intermediate compilation caused by a notation replacement in a
bibliographic surname was corrected; the final surname and compilation
were rechecked. Two long displays were also reformatted.

Static checks found all 93 labels unique, all 74 internal references
resolved in the source, and all 41 citation occurrences covered by
16 bibliography entries. Local note links were checked against the
repository. The source is under 1 MiB.

The existing exact finite records are described with their limited scope.
They are not presented as proof of the imported infinite analytic theorems
or of the new short-family moment. No new large derived dataset,
third-party PDF or manuscript snapshot was created.

## Open obligation

The adaptive signed tail moment at \(h=4/5\), \(0\le a<1/12\), for every
derivative profile remains unproved, as does the alternative at \(h=8/9\),
\(a<1/108\). The manuscript proves reductions and obstructions under its
recorded inputs. It does not establish a stronger zero-free boundary,
quasi-RH-to-RH implication or RH.
