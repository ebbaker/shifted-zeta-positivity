# Positive loop evolution and field corrections

This attempt develops a positive relative bulk complex for the gamma kinetic
term, incorporates exact primitive-return coefficients through loop evolution,
and studies what still prevents its boundary response from being the full Weil
form. The latest positive field modification cancels the first cusp of the
error, but a third-derivative jump survives. The arithmetic completion remains
open.

The latest exploratory [superspace construction](archive/notes/SUPERSPACE_RELATIVE_BOUNDARY_ACTION_20260913.md)
gives the relative complex a canonical positive Fock Hamiltonian, an explicit
cohomological action, and a protected Hermitian ground-state boundary pairing.
A mass-dependent preparation rate gives a uniform bound for the infinite
gamma tower. Its first-prime response still has the earlier infinite-rank
residual: the Ward identity protects changes of massive bulk frequencies,
not changes of the arithmetic differential. The preceding
[covariance audit](archive/notes/QUANTUM_COVARIANCE_AUDIT_AND_FINITE_BLOCK_OBSTRUCTION_20260913.md)
addresses finite replacements in a different Gaussian mass-matrix class.
These follow-up results are separate from the manuscript.

Start with the **[manuscript](manuscript.pdf)** ([LaTeX source](manuscript.tex)).
It is a self-contained account of the work through 12 September 2026, including
the earlier models, exact constructions, obstruction proofs, numerical checks,
and the next mathematical requirements. Its sole project reference is the main
[SUSY-positivity background](../../background.pdf). It does not require the
working notes or any material from the exploratory folders.

The new opening section, **Introduction: purpose, progress, and physical
interpretation** (pages 4–9), explains the goal and the sequence of results before the
technical notation. It distinguishes the static positive response models from
a physical Hamiltonian theory, explains the auxiliary SUSY Hamiltonian and
boundary norm, and states why nonlinear bulk models remain possible. The
numbered sections, equations, and theorems retain their previous numbering.

The introduction now locates this investigation on the program's direct
zero-shift positivity route and distinguishes inherited ingredients from its
new constructions. Section 3.3 (pages 15–16) derives the gamma tower from the
shifted gamma ratio and separates the roles of the shift, channel index,
support length, and auxiliary coupling. The openings of Sections 4 and 6
(pages 17 and 21) derive the prime-delay data and explain why the logarithmic
gamma response motivates exponential loop coupling. References to the shared
background use its subsection titles and definitions, not its equation numbers.

## Contents

| Location | Purpose |
| --- | --- |
| [manuscript.pdf](manuscript.pdf), [manuscript.tex](manuscript.tex) | Current mathematical account; 40 pages in this snapshot |
| [STATUS.md](STATUS.md) | Results, limitations, and next investigation |
| [Operator perspective note](archive/notes/OPERATOR_PERSPECTIVE_20260913.md) | 13 September discussion: full Weil operator, Schur complements, normalized compact spectral comparison, and next steps |
| [Quantum ground-state investigation](archive/notes/QUANTUM_GROUND_STATE_CORRELATIONS_20260913.md) | New Gaussian covariance models cancel up to four leading residual terms; a positive-moment obstruction limits the specified mass class |
| [Covariance audit and finite-block obstruction](archive/notes/QUANTUM_COVARIANCE_AUDIT_AND_FINITE_BLOCK_OBSTRUCTION_20260913.md) | Independent audit, larger-block moment certificates, a general finite-block obstruction, and an interval infinite-rank theorem |
| [Superspace relative boundary action](archive/notes/SUPERSPACE_RELATIVE_BOUNDARY_ACTION_20260913.md) | Explicit action, physical adjoint and ground states, boundary Ward identity, uniform tower preparation bound, and first-prime limitation |
| [numerics/](numerics/README.md) | All numerical programs, historical diagnostic records, and replay instructions |
| [archive/notes/](archive/README.md) | Original continuation notes and field-mixing report, unchanged |
| [archive/reviews/EVALUATION.md](archive/reviews/EVALUATION.md) | Preserved review of the preceding scalar model |
| [archive/provenance/](archive/README.md) | Historical package records and preceding README |
| [REORGANIZATION_20260912.json](REORGANIZATION_20260912.json) | Original-to-current path map and preservation hashes |
| [manifest.json](manifest.json) | File sizes and hashes for this delivered snapshot |
| [validation/BUILD_RECORD.json](validation/BUILD_RECORD.json) | Compilation, visual inspection, and packaging record |

## Read the conclusions with their scope

The manuscript distinguishes analytic derivations from floating-point evidence.
The manuscript constructions specify static energies and an auxiliary Hilbert
complex. The later superspace note constructs a canonical bulk Hamiltonian
for that complex; a Hamiltonian boundary pairing reproducing the full Weil
form and an arithmetic selection principle remain open. Quadratic energies
are the class studied here, not a universal restriction on possible bulk theories.
Its nonexistence results concern specified rational-transfer, finite-rank,
unchanged-energy relaxation, and positive compliance-splitting models. They do
not exclude all positive bulk theories. Selected negative finite-frequency
defects have no interval sign certificate. No full Weil pairing or RH proof is
claimed.

Sections 1–4 establish the target, relative complex, endpoint terms, and primitive
returns. Sections 5–9 explain scalar failure, exact loop evolution, its residual,
and two kinds of completion obstruction. Sections 10–12 derive the positive
splitting field and the surviving obstruction. Sections 13–15 cover cutoff
compatibility, numerical evidence, and the next construction. The appendices
derive the asymptotic coefficients, retain the comparison models, and give a
result-by-result status ledger.

## Reproduce and verify

Python 3 with NumPy runs the numerical programs; no zero database or external
data file is needed. See [numerics/README.md](numerics/README.md) for individual
commands and the limits of replay agreement.

```sh
python3 numerics/replay.py --output-dir /tmp/topological-susy-bulk-replay
python3 validation/check_package.py
make pdf
```

The replay directory must be outside this attempt. `make pdf` uses `latexmk`
and writes a new build to `validation/build/`; it leaves the delivered PDF and
historical records intact. The source contains its own bibliography and has no
LaTeX input dependency on the background or archived notes. `make verify` checks
the delivered snapshot's manifest, relocation hashes, active links, and source
reference policy. It is an integrity check, not a proof checker.

The original notes were archived byte for byte. Their old relative links and provenance
paths are historical; use the [archive index](archive/README.md) and relocation
map instead of interpreting them as the current layout. All current numerical
entry points are under `numerics/`. No changes outside this attempt were needed.
