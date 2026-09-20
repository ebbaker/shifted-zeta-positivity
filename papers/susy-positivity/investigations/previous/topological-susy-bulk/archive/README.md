# Historical archive

The historical notes, review, and provenance files listed below are preserved
byte for byte from the state immediately
before the manuscript reorganization on 12 September 2026. This includes the
existing uncommitted progress, not just the last Git commit. None of the three
working notes was rewritten, including its links, date, or headings.

## Latest superspace construction and boundary preparation

[Superspace action for the relative boundary pairing](notes/SUPERSPACE_RELATIVE_BOUNDARY_ACTION_20260913.md)
supplies a positive canonical Fock realization, explicit cohomological
superspace action, physical adjoint, and boundary Ward identity for the
relative complex. It derives a uniform infinite-tower preparation bound and
identifies the failure of naive finite-time boundary protection. The
first-prime arithmetic deformation changes the harmonic projection and
retains the known infinite-rank residual. Its classical counterpart,
full target comparison, and separate reproducible checks are included.

## Preceding covariance audit and finite-block obstruction

[Covariance audit and an obstruction for every finite replaced block](notes/QUANTUM_COVARIANCE_AUDIT_AND_FINITE_BLOCK_OBSTRUCTION_20260913.md)
independently checks the preceding quantum investigation and corrects its
cross-correlation wording and an unqualified continuum interpretation of the
displacement argument. It calculates larger-block moment certificates and
positive Gaussian responses, proves a general finite-block shifted-moment
obstruction, and separately proves an infinite-rank interval discrepancy for
the analytic finite-dimensional mass class. The classical counterparts and the
remaining complete Weil operator problem are included. Its new diagnostics
preserve all preceding notes and records.

## Preceding quantum investigation

[Quantum ground-state correlations](notes/QUANTUM_GROUND_STATE_CORRELATIONS_20260913.md)
records the subsequent investigation on 13 September 2026. It constructs
positive quantum covariance models for the gamma tower and coupled replacements
of its first two loop channels. Two fields cancel three leading error terms;
a third field cancels a fourth. Nonzero residuals remain. A shifted moment
determinant excludes matching five such terms in the stated positive mass
class, even with more auxiliary fields. The note includes the full responses,
positivity proofs, domain and locality qualifications, and separate reproducible
checks. These follow-up results have not been incorporated into the manuscript.

## Preceding operator discussion

[Operator formulation of the gamma tower and the full Weil target](notes/OPERATOR_PERSPECTIVE_20260913.md)
records the discussion of 13 September 2026. It identifies which operator
ingredients are already in the background and manuscript, assembles the full
finite-interval target and loop response, and derives a normalized compact
spectral comparison. It also explains the existing repair obstructions in
operator language and what a rigorous spectral calculation would need.
This is a new explanatory note, separate from the preserved historical files;
it does not report a proved positivity bound or a new manuscript draft.

## Preceding handoff

[Manuscript discussion preceding the shift-to-channel derivation](notes/CONTINUATION_MANUSCRIPT_DISCUSSION_20260912.md)
records the later discussion after the introductory revision and the move to
the investigations folder. It is separate from the three preserved original
working notes listed below. The missing bridge identified there is now included
in the current manuscript; the handoff itself remains unchanged.

## Manuscript drafts

The earlier 33-page PDF and LaTeX source are preserved in
[drafts/20260912-before-introduction](drafts/20260912-before-introduction/README.md),
with their original bytes and a snapshot hash record. The current 40-page
manuscript, including its six-page conceptual introduction, remains at the
investigation root.

## Notes and review

| Archived file | Original role |
| --- | --- |
| [notes/CONTINUATION_20260912.md](notes/CONTINUATION_20260912.md) | Initial program, loop evolution, residual, and continuation record |
| [notes/FIELD_MIXING_20260912.md](notes/FIELD_MIXING_20260912.md) | Positive low-mode field, exact elimination, and new obstruction proofs |
| [notes/CONTINUATION_FIELD_MIXING_20260912.md](notes/CONTINUATION_FIELD_MIXING_20260912.md) | Handoff after the field-mixing investigation |
| [reviews/EVALUATION.md](reviews/EVALUATION.md) | Review of the preceding scalar proposal |

Their conclusions are integrated into the [current manuscript](../manuscript.pdf).
The manuscript derives the needed background of this attempt within its own
text and cites only the shared SUSY-positivity background document.

## Provenance

- [provenance/README_before_manuscript.md](provenance/README_before_manuscript.md)
  is the preceding entry point.
- [provenance/package-record.json](provenance/package-record.json) and
  [provenance/field-mixing-pass-record.json](provenance/field-mixing-pass-record.json)
  record earlier package states. Their file paths and hashes describe those
  states, not the current package.
- [../REORGANIZATION_20260912.json](../REORGANIZATION_20260912.json) maps every
  original file to its preserved location and records its original SHA-256.

## Resolve historical paths

Relative links inside frozen notes were interpreted from their former locations
at the attempt root, or from the former `review/` directory. Moving the notes
without editing them means some such links no longer resolve directly. Use the
relocation map above. In particular, former `calculations/` programs are now in
`../numerics/`, former `results/` diagnostics are in `../numerics/records/`, and
the numerical parts of `review/` are also under `../numerics/`.

The original fixed-output finite-coupling script is preserved at
[../numerics/archive/check_finite_coupling_before_cli.py](../numerics/archive/check_finite_coupling_before_cli.py).
Use its current [command-line version](../numerics/check_finite_coupling.py)
for replay. The predecessor generator for the supplied-model diagnostics is
now included as a standalone current program; its provenance is recorded in
the relocation map. No external exploratory file is needed to run it.

The older loop-evolution diagnostic and its byte-identical replay are both
retained as historical records. New replays write outside the attempt and never
overwrite these records.
