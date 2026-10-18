# Current-results manuscript integration review

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6-astra**, reasoning effort
**max**, verified from the authoring turn metadata. This is internal
integration review by the contributing assistant. No independent specialist
review or independent arithmetic implementation is claimed.

## Version and disposition

**Current results incorporated; document and scoped numerical checks pass.**
The [canonical manuscript](../manuscript/positive_arithmetic_packets/main.tex)
has twelve TeX files, eleven numbered sections and 45 pages. Its source-set
SHA-256 is `2690c3052927702a7f25d7e0519cc8ae10abfd202ac891bb8c06208eaa9a7b0c`.
The [build record](../manuscript/positive_arithmetic_packets/BUILD_RECORD.json)
gives individual hashes and preserves the full preceding eight-file record.
The previous source set was
`f6cd484647ef328047e9ac51a577b8260e899aecbfdd5026e9e238079feb823f`.
No manuscript snapshot or Git commit was created for this integration.

The [round summary](../research-progress/03_OVERVIEW02_ROUND_SUMMARY_20261018.md),
Notes 07–14, Reviews 06–12, their numerical contracts, and the relevant
published inputs were compared with the revised exposition. The governing
status references are [result-summary 14](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md),
[cancellation scope](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [status synchronization](../../../../avoid/19_status_files_that_lag_the_findings.md).

## What changed

| Source material | Current manuscript | Disposition |
| --- | --- | --- |
| Existing packet, carrier, modular and finite-prime proofs | Sections 1–6 | Retained; roadmap and historical onset wording updated |
| Note 11 and Note 14 contour estimates | Section 7 | Full nonstationary proof, effective logarithmic onset and constant-distance theorem with all constants |
| Notes 07–09 and 12 finite computations | Section 8.1–8.2 | Complete retained-source and whole-cell contract; signed certificates on D0 and D1 |
| Note 13 finite wall and propagation | Section 8.3–8.4 | Seven-cell wall, finite propagation proof including multiple initial zeros, and named published imports |
| Note 12 comparison and adversarial screening | Section 8.5 | Original failed factor-two gate preserved; control premises identified |
| Note 14 exterior reduction and the earlier fixed-cutoff derivation | Section 9 | Complete analytic contract and proof included in-paper, then explicit exp(20/epsilon) theorem |
| Numerical provenance | Section 10 | Scalar table retained; replay entry points and full error evidence distinguished |
| Notes 10 and 14 global scope | Section 11 | Exact coverage table, scoped cost and moment obstructions, conditional canopy contract and exact remote polynomial control |

The abstract, subtitle, dependencies, acknowledgements and bibliography now
match these results. The added exposition imports only named published
theorems; numerical certificate claims remain explicitly computer assisted.

## Mathematical scope checks

The finite proof separates the wall on **0<=t<=1/5** from the signed
rectangle on **1/100<=t<=1/5**. It uses the zeta-to-heat height factor two
and only initial zeta height 500. The Hermite splitting argument handles
arbitrary finite multiplicity at t=0 without assuming initial simplicity.
The signed D1 rectangle overlaps the finite-height region at [999,1000].

The exterior proof reproduces the fixed-cutoff disk contract, normalizer,
reflection and Cauchy derivative payment before applying the explicit
constants. Its conclusion is a real first-jet bound. It is not substituted
for the complex nonvanishing hypothesis of the canopy theorem. The example
Lambda<=0.18 is explicitly conditional on the entire stated final-time
complex exterior.

All implementation exclusions name the class actually excluded: explicit
mode enumeration, the present absolute retained-source payment and a fixed
degree/midpoint Taylor majorant. The remote L=2000 polynomial preserves the
finite-wall, strip and all-real-baseline premises but fails the stronger
D1 signed inequality. It is not treated as a theta counterexample or a
universal obstruction to signed information.

The current abstract states: **“The bridge 1001<|x|<e^2000 remains open on
the stated slab.”** This supersedes the earlier manuscript's absence of
finite exclusion, while retaining its warning that an accurate auxiliary
approximation is not a physical lower bound. The exact current claim is
E>0 on [1/100,1/5] × [-1001,1001] and for epsilon<=t<=1/2,
|x|>=exp(20/epsilon), with no new Newman bound.

## Fresh computational checks

The [integration replay manifest](../numerics/MANUSCRIPT_INTEGRATION_REPLAY_20261018.json)
binds all twelve current sources, generator identities, observed outcomes
and hashes of fresh outputs. The [regeneration guide](../numerics/manuscript_integration_20261018/README.md)
uses the unchanged existing generators. Large or duplicate generated cell
records were not added to the repository; original records remain intact.

- Exact-rational checker: all nine printed rows, eight headline bounds and original checks pass.
- Effective-tail checker: three parameter cases and four invalid-contract rejections pass.
- D0: all 314 signed strips and 128 first-jet cells recalculated at 256 bits; minimum signed excess exceeds 4.60260e-16; fifteen failure/regression tests pass.
- D1: regenerated setup binds the current manuscript; 40 signed cells pass at production precision and fresh 256-bit replay, with signed excess above 8.26087e-5 G*².
- Wall: seven cells cover the complete stated time/imaginary-height rectangle, including seams and endpoints; selected coordinate margin exceeds 0.00425150082920 G*.
- Separate 768-bit real-source evaluation reproduces the high signed and wall conclusions; ten malformed-input, strictness and event controls reject.
- Source-specific screening rejects five collision-event boxes plus the Euler-factor negative-Laguerre witness, using each source's own errors.
- Analytic continuation: 25 strict outer scalar checks, 26 overlaps at 192/256 bits, five rejected parameter cases, two constant-distance parameter sets and the exact remote polynomial checks pass.

The D0 validation input is the unchanged historical record. The pilot and
its control receipts were regenerated before its 256-bit replayer ran.
An initial attempt against the old directory stopped because the Euler
receipt was absent; regeneration resolved this input failure without
bypassing a guard. The historical replayer still emits its older exp(6400)
budget. That generated budget is not promoted to current status; Section 11
and the integration manifest use exp(2000).

The scalar checker's embedded author metadata is historical; the manifest
records this turn's actual execution model/effort separately. The analytic
replayer's inherited finite-coverage wording is also distinguished from the
fresh high-height recomputation performed here. The manuscript keeps the
original matched timing 7.590 s versus 11.236 s (ratio 1.480), with its
failed factor-two gate. The fresh timing is verification metadata only.

## Document checks and remaining obligations

Terminal and built-in editor compilation succeed without LaTeX warnings,
overfull/underfull boxes or unresolved references. All 179 internal labels
are unique and every internal reference resolves. All 45 pages contain text;
every page was rendered and inspected, including readable checks of the new
proof pages and the repaired final bibliography. Automated glyph bounds
find no text outside a relaxed page interior.

The source SHA, numerical replay manifest, build record, reading-copy PDF,
READMEs, progress tracker and draft history are reconciled in this milestone.
Historical notes, numerical records and reviews retain their old hashes.
The research gap and failed speed gate remain unchanged. Global real
coverage or the full conditional complex exterior still requires new work.
