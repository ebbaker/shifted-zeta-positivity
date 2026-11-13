# Riemann–Siegel source pointers

10 November 2026, America/New_York. Prepared for Edward Baker with substantial OpenAI Codex LLM assistance. Actual model and effort are unavailable in the founding chat capture metadata; recommendations are recorded separately.

The [parent catalog](../../references/README.md) owns shared branch-use records. Classical RS retains the [operator bibliography](../../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/references/riemann_siegel_sources.bib), [selected-passage record](../../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/references/18_TND_O_RIEMANN_SIEGEL_SADDLES_SOURCE_USE_20261110.md) and external-PDF receipts. Polymath v2 retains its [HDA record](../../../01_heat_density_asymptotics/references/references.bib). The [OG HDA/log transfer](../../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/01_green_potential_resolvent/notes/05_TND_OG_B03_HDA_HIERARCHY_LOG_TRANSFER_20261108.md) is the inherited consumer calculation.

The original child setup imported no new article. B02 adds the selected Shapiro lecture-note passages recorded below, with a [small child execution bibliography](riemann_siegel_execution_sources.bib); shared Arias/Polymath records remain in their canonical homes. Future work records exact additional checked passages, version, domain and consuming inequality. Follow [REFERENCE_WORKFLOW](../../../../../REFERENCE_WORKFLOW.md); reading copies stay external under [LARGE_FILES](../../../../../LARGE_FILES.md).

## Child overview inspection — 11 November 2026

Prepared for Edward Baker with substantial OpenAI Codex LLM assistance;
actual model/effort unavailable in chat0001 capture metadata.
The following **selected primary passages** were reopened in version-pinned
HTML for [GNP-RS-E02](../reviews/01_GNP_RS_OVERVIEW_COMPLETENESS_ASSESSMENT_20261111.md)
and the [revised overview](../research-overview/01_GNP_RS_RESEARCH_OVERVIEW_20261110.md).
This is not full-paper reading, a fresh proof audit, or a check of newer versions.
Canonical article/BibTeX ownership above is unchanged.

| Existing article/version | Passages inspected and consuming use | Retained limit |
| --- | --- | --- |
| J. Arias de Reyna, *Riemann's auxiliary function. Basic Results*, arXiv:2406.02403v1, 4 June 2024, [§3](https://arxiv.org/html/2406.02403v1#S3) | Definition 4, Theorem 5 and (7)–(10): contour, branch, conjugation and exact reflected identity; overview §3. | Identity/continuation, not nonvanishing. |
| J. Arias de Reyna, *Asymptotic Expansions of the auxiliary function*, arXiv:2406.04714v1, 7 June 2024, [§§2/8](https://arxiv.org/html/2406.04714v1) | (1)–(4), (78)–(81), including the square-root sectors and reflected expansion statement; overview §3. | No new zero-free-region theorem or growing-order error bound is imported from this paper. |
| D. H. J. Polymath, *Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant*, arXiv:1904.12438v2, 4 August 2019, [pinned HTML](https://arxiv.org/html/1904.12438v2) | (5), Theorem 1.3, Theorem 1.5 statement; §4 (35)–(41); Proposition 6.2 (48)–(57); corrected (69) versus (70). Overview §§4/6 use the domains, evolution and inherited remainder. | Theorem 1.3 states \(0<t\le1/2,\ 0\le y\le1,\ x\ge200\); wider strips require changed constants. In Proposition 6.2 the \(\sigma<0\) bound requires \(K+\sigma\ge2\); that restriction is absent at \(\sigma=1/2\). |

The overview's saddle differentiation, coordinate conversions and real-line
gamma cancellation were checked against the parent derivations. The
HDA recurrence/crossover statements are inherited through OG Note05 and
its exact source/review links; their underlying proofs were not re-audited.
The OA conditional survival/factor interfaces were read in their existing
manuscript §§2/4. Source counts and review labels remain inherited.

No new paper or PDF was acquired in this pass. Existing Arias/Siegel
external reading copies and hashes remain in the operator parent's
[receipt record](../../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/references/RS_SADDLES_PDF_RECEIPTS_20261110.json);
this inspection used primary HTML, not a newly downloaded copy.

## B01 input reuse — 11 November 2026

Prepared for Edward Baker with OpenAI Codex assistance; actual
model/effort unavailable in child chat0001 capture metadata.
[B01 Note01](../notes/01_GNP_RS_B01_TRANSITION_SCALE_GREEN_BASELINE_20261111.md)
uses the following exact local inputs. This is a bounded
selection/dependency check, not a fresh independent proof audit.

| Source inspected | Consuming use and retained evidence level |
| --- | --- |
| [HDA Ansatz Note03](../../../01_heat_density_asymptotics/ansatz/notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md), CB3–5 and CB26; [AN01 weight definitions](../../../01_heat_density_asymptotics/ansatz/research-progress/handoffs/HDA-A01-AN01.md) | Elementary arm normalization, weights and full arithmetic phase, including \(+\pi\lambda/8\). The earlier note's open complex remainder was superseded by Note04, not inferred from holomorphy alone. |
| [HDA Ansatz Note04](../../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md), §§1–6 and onset ledger; [Assessment03](../../../01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md) | CS3/CS6 supplies fixed-buffer fields, both arms, corrected cutoff and fully paid Gaussian exterior on \(\lvert\lambda\rvert L_X\le8\). Finite constants/onsets remain unevaluated; same-model internal assessment. This provider covers the wider Green lines, with fixed charts recentered pointwise. |
| [Earlier collision manuscript](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex), Proposition “Last-block absolute mass”; [S04 Note01](../../../../investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md), full-cutoff weights and phase | Inherited last-block exponent and growing-population warning. B01 specializes this to the chosen Green logarithmic allowance; it does not claim discovery of the coefficient-growth obstruction or transfer stronger unrelated signed obstructions. |
| [Parent source](../../manuscript/sections/02_source.tex), [Green](../../manuscript/sections/05_green.tex) and [prime](../../manuscript/sections/06_prime.tex) sections | Source/strip, unit-interval logarithmic bound, kernel masses/transform and defect margin. The new carrier has no interior divisor, so the parent's time-zero gamma-removal correction is not copied into its exact identity. |
| Polymath arXiv:1904.12438v2, linked above | Pinned primary HTML reopened to retain the published domain/evolved-RS comparison. No new claim is imported outside its printed narrow-strip domain. B01's wider-strip proof dependency is the separate local HDA result. |

The new harmonic-carrier argument is proved in B01 Note01 itself.
The shifted outer prime-baseline estimate is only the **E01 proof target**.
No new article, BibTeX entry or PDF reading copy was required.
The [B01 input record](../numerics/02_GNP_RS_B01_INPUTS_AND_HANDOFF_20261111.json)
pins local source bytes for the receiving model.

## E01 execution — 11 November 2026

Prepared for Edward Baker with OpenAI Codex assistance; actual
model/effort unavailable in chat0001 metadata. The
[E01 proof](../notes/03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_PROOF_20261111.md)
now establishes the former B01 proof target from the named inherited
inputs. Before execution, all 45 B01-recorded identities matched.

- Re-read HDA Note04 CS2–6, CS16–25 and §8, the exact weight/phase
  definitions in AN01/Note03, and Assessment03. The consumed result
  is the nonnegative-time field estimate on fixed \(r=1,b=9\)
  charts with its enlarged Gaussian buffers. The whole HDA proof
  was not independently re-audited; its review status is unchanged.
- Re-read the parent Green unit-log/tail identity and prime kernel
  transform. E01 derives its own normalized unit-log constant,
  complete outer field/log payments and shifted prime combination.
- Rechecked primary [DLMF 25.2.1](https://dlmf.nist.gov/25.2.E1),
  [25.2.6](https://dlmf.nist.gov/25.2.E6) and
  [25.2.11](https://dlmf.nist.gov/25.2.E11), retrieved 11 November
  2026, displayed DLMF version 1.2.8 (15 September 2026):
  the ordinary Dirichlet series, its derivative and Euler product
  for \(\Re s>1\). E01 uses them only for \(\Re s\ge5/2\).
  Canonical citation remains DLMFZetaOuter2026 in the linked
  [HDA bibliography](../../../01_heat_density_asymptotics/references/references.bib).
  The Euler-log prime-power formula is derived by absolutely
  convergent logarithmic expansion; no Euler product is assigned
  to the evolved field.

No new article, PDF copy or bibliography duplication was needed.
The [E01 input/check record](../numerics/03_GNP_RS_E01_INPUTS_AND_CHECKS_20261111.json)
pins the reused sources and separate return. The B01 source-use section
above is historical; its proposed-status wording is superseded by E01.

## B02 bounded comparison — 11 November 2026

Prepared for Edward Baker with OpenAI Codex assistance; actual model and
effort unavailable in chat0001 metadata. [B02 Note05](../notes/05_GNP_RS_B02_JENSEN_AND_SHIFTED_ZETA_COMPARISON_20261111.md)
reuses the full real HDA formula, E01's exact critical-log tail and prime
phase, and the parent paired-product Green proof. The affine-translation
radius check and pole/zero bookkeeping are derived in Note05 itself.
No underlying HDA proof is independently re-audited.

- The [OG hierarchy/log transfer](../../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/01_green_potential_resolvent/notes/05_TND_OG_B03_HDA_HIERARCHY_LOG_TRANSFER_20261108.md)
  and parent signed assembly were reread as acquisition interfaces.
  Neither supplies the favorable signed value.
- The earlier [OC signed-Jensen comparison](../../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/notes/04_TND_OC_B02_SIGNED_JENSEN_AND_HARMONIC_DISTANCE_20261107.md)
  was inspected to distinguish its two-dimensional Laplacian test and
  shrinking-depth obstruction from the present boundary/kernel recipe.
  Its result is not imported or claimed as this child's discovery.
- Joel H. Shapiro, *Notes on Oscillatory Integrals*, dated **9 February
  2012**, [author-hosted PDF](https://www.joelshapiro.org/Pubvit/Downloads/OscNotes/oscint.pdf),
  retrieved in the web reader 11 November 2026: selected §2 passages,
  Lemmas 2.1/2.3 and Theorems 2.5/2.6, printed pp.4–9.
  Checked first/second derivative assumptions, monotonicity for the first
  derivative, and amplitude payment by endpoint value plus variation.
  This supports E03's chosen elementary oscillatory method, not its
  unproved growing-mode estimates. The stated “sufficiently large”
  weighted second-derivative formulation is not silently imported with
  uniform constants for moving phases; E03 must derive the needed
  uniform version. This is selected-passage inspection, not full reading.
  Citation key: ShapiroOscillatory2012 in the child bibliography.
  The attempted external local reading-copy download failed with a
  hostname-resolution error; **no local PDF, size or hash is claimed**.
  The public PDF was accessible through the web reader. No third-party
  PDF was placed in the repository.

The [B02 record](../numerics/04_GNP_RS_B02_INPUTS_AND_HANDOFF_20261111.json)
pins local inputs and records this inspection/download limitation.
No literature-priority search or exhaustive source survey was performed.

## E03 execution — 11 November 2026

Prepared for Edward Baker with OpenAI Codex assistance; chat0002 records
no model or effort. [E03](../notes/07_GNP_RS_E03_COHERENT_JENSEN_OBSTRUCTION_20261111.md) uses the same HDA Note04
CS3/CS6 and CS25, its original Assessment03, the complete E01 E10–E11
real restriction and B02's prime/margin calculation. The inherited
provider's review scope is retained. The selected
[Shapiro §2 passage](https://www.joelshapiro.org/Pubvit/Downloads/OscNotes/oscint.pdf),
Theorems 2.5–2.6 on pp. 8–9, was rechecked in the author-hosted PDF
on 11 November. E03 derives its own partial-integral bounds uniformly
in all growing pairs and endpoints. No new source file or bibliography
entry was needed. See the [execution record](../numerics/05_GNP_RS_E03_INPUTS_AND_CHECKS_20261111.json).

## Critical-time clarification — 11 November 2026

Prepared for Edward Baker with Codex assistance; actual model/effort unavailable. [Note20](../notes/20_GNP_RS_GREEN_GEOMETRY_AND_CRITICAL_TIME_20261111.md) rechecks Polymath, arXiv:1904.12438v2 (4 August 2019), [Theorem 1.5(i)](https://arxiv.org/html/1904.12438v2#S1), Proposition 3.1 and [§4, (35)–(39)](https://arxiv.org/html/1904.12438v2#S4) in pinned primary HTML. The theorem's absolute positive-time height bound is used in a compactness proof of finite multiple-zero attainment conditional on Λ>0; (39) supplies the complete symmetric real-axis expression, including its remainder. This is a standard consequence and selected-passage inspection, not a new zero-exclusion estimate or full-paper review. The canonical HDA bibliography and existing reading-copy records remain in place; no new PDF copy was acquired.

## B07 localized tail input — 12 November 2026

The [source-use record](01_GNP_RS_B07_DISCRETE_DERIVATIVE_SOURCE_USE_20261112.md)
checks Elkies's discrete second/third-derivative estimates and records selected
Robert corroboration with an explicit extraction limitation. The
[download manifest](01_GNP_RS_B07_REFERENCE_DOWNLOADS_20261112.json) identifies
both public external reading copies. The child bibliography has the reusable
entries. This supports Note23's shifted-pair estimate; no independent theta
field theorem is imported. For Edward Baker with Codex assistance; actual
model/effort unavailable.

## B08 exponent-pair input — 12 November 2026

For Edward Baker with substantial OpenAI Codex assistance; actual model and
effort unavailable. The canonical [Robert record](01_GNP_RS_B07_DISCRETE_DERIVATIVE_SOURCE_USE_20261112.md#b08-later-use-of-robert--12-november-2026)
now includes a dated later-use section for Sections 5.1–5.2, equation (20),
and the A/B transformations, preserving its B07 history. The new
[Bourgain–Watt v1 record](02_GNP_RS_B08_EXPONENT_PAIR_SOURCE_USE_20261112.md)
checks the related shifted-logarithm estimate in (13.37) as corroboration.
Both are selected-passage uses for [Note25](../notes/25_GNP_RS_B08_EXPONENT_PAIR_LOCALIZATION_20261112.md),
not full-paper readings. The bibliography includes the pinned v1 entry;
the [new download manifest](02_GNP_RS_B08_REFERENCE_DOWNLOADS_20261112.json)
identifies its external PDF. Robert's existing copy and manifest are reused.

## B09 joint-theorem range screen — 12 November 2026

For Edward Baker with Codex assistance; actual model/effort unavailable.
The dated B09 addendum in the [existing Bourgain–Watt record](02_GNP_RS_B08_EXPONENT_PAIR_SOURCE_USE_20261112.md)
checks Theorem2(6.6),(6.11) and Remark(i), printed pp14–15. The direct
import fails necessary shift gates at the current consumer. Its omitted
case is a future source lead only. Original B08 bytes are preserved as
a prefix and the archived v1 PDF is unchanged; no new copy or theorem import.

- **B10, 12 November 2026:** the [Bourgain–Watt canonical source record](02_GNP_RS_B08_EXPONENT_PAIR_SOURCE_USE_20261112.md) now also records Theorem 4 and the earlier internal parameter restriction. This pass imports the cumulative mean-square theorem and proves its cutoff-arm transfer separately. For Edward Baker with Codex assistance; actual model/effort unavailable.

- **B10 audit, 12 November 2026.** The [Montgomery–Vaughan source record](03_GNP_RS_B10_EXPONENT_PAIR_AUDIT_SOURCE_20261112.md)
  gives an unambiguous reciprocal-phase citation for the same exponent pair.
  The [Bourgain–Watt record](02_GNP_RS_B08_EXPONENT_PAIR_SOURCE_USE_20261112.md)
  includes the journal metadata and the checked direction of the (7.3)
  parameter comparison. For Edward Baker with Codex assistance. Actual
  model and effort are unavailable.

## Lower transverse offset discussion — 13 November 2026

For Edward Baker with Codex assistance; actual model/effort unavailable.
[Brainstorm Note12](../brainstorm/notes/12_GNP_RS_LOWER_TRANSVERSE_OFFSET_AND_LOG_OBSERVATION_20261113.md)
rechecks Polymath, arXiv:1904.12438v2 (4 August 2019),
[primary HTML](https://arxiv.org/html/1904.12438v2#S1): (5), (11),
the caveat after (12), and Theorem 1.3 (13)–(24). This verifies the
near-axis finite-sum representation and normalization, not uniform
small-value control. Selected passages only; existing bibliography and
HDA/HDC external reading-copy provenance are reused. No new PDF acquired.

## Height and time dependent boundary discussion — 13 November 2026

For Edward Baker with substantial OpenAI Codex assistance; actual model
and effort unavailable. [Brainstorm Note13](../brainstorm/notes/13_GNP_RS_HEIGHT_AND_TIME_DEPENDENT_STRIP_BOOTSTRAP_20261113.md)
rechecks the same Polymath arXiv:1904.12438v2
[primary text](https://arxiv.org/html/1904.12438v2#S3):
Theorem 3.2 (global uniform strip contraction, in the normalization
\(\partial_t H=-H_{zz}\)); Theorem 1.2 and Proposition 3.3
(initial, final and intermediate barrier hypotheses); and Proposition 3.1,
especially (31)–(32) and the treatment of multiple zeros.
These are selected-passage checks. No arbitrary height-dependent
contraction theorem is imported. The same bibliography and external-copy
provenance are reused; no additional PDF acquired.
