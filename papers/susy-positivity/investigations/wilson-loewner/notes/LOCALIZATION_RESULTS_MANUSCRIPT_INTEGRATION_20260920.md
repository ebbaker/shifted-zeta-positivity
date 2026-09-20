# Predictive localization results in manuscript version 0.5

Date: 20 September 2026. Drafted for Edward Baker.
Model: OpenAI GPT-6 (Codex; developer-provided identity).
Effort setting: not exposed in this session; not inferred.
Status: editorial integration of internal research calculations, with build
and diagnostic checks; no independent specialist mathematical or physical review.

## What changed

The current manuscript pair is version 0.5. The standalone snapshot is
`drafts/2026-09-20-v05/`; versions 0.1--0.4 and the dated research notes are
preserved unchanged. The main exposition has 20 pages and the supplement
has 39 pages.

| Location | Addition |
|---|---|
| Main Section 5.4 | Predictive hemisphere gamma amplitude and actual scalar-pair state; fixed-representative spatial obstruction; the distinct canonical Hodge alternative and its missing elementary modes |
| SI S12.1--S12.2 | Charge and boundary conditions, auxiliary completion, vacuum transform, paired circle control, actual endpoint ordering and ordinary field-space adjoint |
| SI S12.3 | Centered stereographic frame and explicit non-closure witness for ordinary spatial dilation; scope of R compensation and moving-charge alternatives |
| SI S12.4--S12.5 | Canonical protected semigroup, exact omitted elementary covariance tower, and distinction between composite-state character and endpoint spectral weights |
| SI S12.6 | Conditional arithmetic parameter comparison and the still missing spatial-to-field-space dictionary |
| Main Section 8.4 / SI S9.5 | Separately established arithmetic EMA anchor and scalar-bound obstruction for the adjoining-window estimate |
| Main Section 9 / SI S13--S14 | Revised agenda, status ledger, separate localization controls and provenance |

The abstracts, reading maps, bibliographies and source records now reflect
these additions. Primary localization inputs are attributed to
Dedushenko--Pufu--Yacoby, arXiv:1610.00740v2, and Dedushenko's *Gluing II*,
arXiv:1807.04278v3. The derivations in the three dated localization notes
remain the research record. This integration adds no new numerical
positivity claim.

## Claims that must stay separate

The free hemisphere calculation derives a one-sided gamma amplitude from
specified boundary data. The separated scalar pair supplies the actual
insertion rather than an arithmetic polynomial chosen after the fact.
Its Mellin coordinate is boundary field magnitude, not spatial radius.

Ordinary spatial dilation fails to preserve arbitrary closed representatives
in the tested free Higgs sector. This does not forbid choosing canonical
Hodge representatives first: the kernel of `D-R_H` admits restricted
`exp(-u D)` evolution. For an elementary scalar that projection keeps only
angular degree zero. The omitted even-angular covariance is
`exp(-5u/2)/(1-exp(-2u))`; a composite-state character can reproduce its
ladder after extra selections, but an elementary endpoint does not excite
those states. No physical arithmetic transfer or positive storage identity
follows from either observation.

Independently, the arithmetic EMA calculation gives an all-input
fixed-window anchor. Its specialist review remains outstanding. In the
adjoining-window test, replacing both directional defects by the scalar
floor gives an estimate between 55 and 72, which cannot prove contraction.
The finite quotient near 0.802 is a diagnostic, not an all-input upper bound.
No auxiliary smoothing loss or averaging variance is credited as arithmetic
positivity, and no instantaneous operator lower bound is exponentiated
through the nonnormal evolution.

## Reproducibility and preservation

Both PDFs were rebuilt with pdfLaTeX/latexmk. The final build logs contain no
unresolved references, multiply defined labels or overfull boxes. Every
rendered page was inspected, with enlarged inspection of the new material;
the ledger heading and bibliography page breaks were adjusted. The final
page counts and hashes are in `BUILD_RECORD.json`.

The original four-program ledger remains 299 passing diagnostics. The three
additional localization programs were replayed separately and reproduced
their saved records exactly:

- hemisphere control at quadrature orders 24 and 40;
- radial-descent control: 83 passing cases (57 exact rational, 26 floating);
- Hodge channel: 25 protected-degree levels, 13 one-particle levels, six
  covariance comparisons, and an exact rational partial-sum/tail enclosure.

`BUILD.md` contains the commands. The version-0.5 build record hash-binds all
seven programs and their small records. The portable snapshot includes
them but does not relabel the three additional record formats as part of
the 299-case count. All saved files remain below the repository's 1 MiB
threshold. Hashes verify identity and finite replays verify their stated
checks; neither substitutes for specialist review of the physics or proofs.

## Next-session handoff

Start with main Section 5.4 and SI S12, then read
`HODGE_RADIAL_CHANNEL_AND_PROGRAM_ASSESSMENT_20260920.md` alongside
`SPATIAL_RADIAL_DESCENT_OBSTRUCTION_20260920.md`. Keep the Hodge qualification
when discussing the non-descent result. Do not resume the earlier
polynomial fit as if its spatial parameter map had been derived.

For the next localization calculation, choose a specific physical observable
or enlarged/interface sector *before* comparing its spectrum with arithmetic.
Derive the ordinary-adjoint endpoint matrix elements as well as energies.
A concrete bounded test is whether a prescribed boundary/interface coupling
can excite an infinite protected composite tower while retaining a defined
positive norm and independently determined weights. An arbitrary generating
function chosen to reproduce the target is not a predictive construction.
If no such independently motivated coupling is specified, the present free
control has reached its scoped conclusion; obtain specialist review rather
than fitting further constants.

The direct arithmetic continuation remains in `critical-path`: derive an
energy-weighted bound for the normalized cumulative append and both omitted
input spaces, preserving endpoint memory. Read the EMA anchor and append
notes cited in SI S9.5; retain their original normalization, signed poles,
reflection convention, and certificate/diagnostic distinction. The two
research directions inform one another but neither licenses the missing
steps of the other.
