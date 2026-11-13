# B07 discrete derivative estimates: source-use record

12 November 2026, America/New_York. Prepared for Edward Baker with substantial
OpenAI Codex assistance. Actual model/effort unavailable in chat0006; helper
settings are not inferred. This is selected-source verification, not a
literature-priority review or a new audit of the inherited field theorem.

The consuming proof is [Note23](../notes/23_GNP_RS_B07_LOCALIZED_TAIL_AND_EXACT_BOUNDARY_20261112.md).

- **Noam Elkies, *Exponential sums III: the van der Corput inequalities*.**
  Undated Math 229 course handout at the author’s M229.09 URL; no publication
  date is inferred. [Author-hosted PDF](https://people.math.harvard.edu/~elkies/M229.09/vdc.pdf),
  retrieved 12 November 2026. All three pages were read: inequalities II–III
  on page 1 and their proofs on pages 2–3. The consumed input is the discrete
  third-derivative estimate, with fixed-sign derivative and fixed comparability
  constants. Its trivial parameter regimes and translated subinterval use
  were checked. Note23 reproduces a short derivation and pays its application
  to the actual shifted logarithmic phase; the source supplies no theta
  residual estimate. Citation key: ElkiesVdCHandout.
- **Olivier Robert, *On van der Corput’s k-th derivative test for exponential
  sums*.** Author-hosted manuscript headed “To appear in Indagationes
  Mathematicae (2015)”. [PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf),
  retrieved 12 November 2026. Selected inspection of Section 3.3/Theorem 2
  and its surrounding proof corroborates the derivative-test setting;
  full-paper reading is not claimed. The extracted theorem-hypothesis
  derivative order is ambiguous; this is **not** the formal source used for
  the hypothesis. The unambiguous Elkies statement and reproduced derivation
  govern the application. No later version or final publication metadata was
  verified. Citation key: RobertDerivative2015AuthorCopy.

Public reading copies were retained outside the repository. The
[manifest](01_GNP_RS_B07_REFERENCE_DOWNLOADS_20261112.json) records exact
URLs, paths, byte sizes and hashes. These identify the retrieved files;
they do not validate any mathematical claim. Follow the
[reference workflow](../../../../../REFERENCE_WORKFLOW.md) and
[large-file rules](../../../../../LARGE_FILES.md). No third-party PDF is
stored in this repository.

## B08 later use of Robert — 12 November 2026

Prepared for Edward Baker with substantial OpenAI Codex assistance; actual
model and effort remain unavailable. This is an intentional later-use
addition to the canonical record. The B07 inspection and its derivative-order
extraction limitation above are preserved, not silently revised.

For [Note25](../notes/25_GNP_RS_B08_EXPONENT_PAIR_LOCALIZATION_20261112.md),
selected passages in the **same archived author manuscript**, Sections
5.1–5.2, printed pages 11–12, were checked: the semimonomial class
\(F(N,Q,\alpha,T,\epsilon)\), equation (20), its interval domain, and the
displayed A/B transformations. The bound includes both
\((T/N)^kN^l\) and \(N/T\). Its fixed finite derivative order, relative
derivative-error requirement and dependence on the fixed exponent pair and
\(\alpha\) are retained. B08 uses \(\alpha=-1\) and
\(BAAB(0,1)=(2/7,4/7)\); Note25 verifies the small-shift derivative
gate and pays the complementary shifts. These passages, rather than the
ambiguous extracted Theorem 2 hypothesis, supply this later input.

This is selected-passage checking, not full-paper reading, an audit of
the A/B-process proofs, or verification of a later publication. The original
[download manifest](01_GNP_RS_B07_REFERENCE_DOWNLOADS_20261112.json) still
identifies the unchanged reading copy. The separate
[Bourgain–Watt record](02_GNP_RS_B08_EXPONENT_PAIR_SOURCE_USE_20261112.md)
provides corroboration for a related shifted logarithmic phase.

The Section5.1 positive-alpha parameter list is internally inconsistent
with its preceding real-alpha<1 definition and Section5.2 quantifier. B08
states this issue explicitly and uses the consistent alpha<1 convention;
the separate Bourgain–Watt application corroborates the reciprocal-type
phase setting. This is not a correction silently applied to the source.
