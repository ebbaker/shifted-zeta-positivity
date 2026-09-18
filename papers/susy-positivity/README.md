# SUSY positivity research program

This program seeks an independently defined positive structure whose pairing
is the full central Weil quadratic form on every smooth compactly supported
input, at arbitrary support length. The shifted transfer family supplies a
related contraction route. **The all-length sign problem remains open; no RH
proof is claimed.**

## Start here

- [Mathematical background](background.pdf) and [program overview](PROGRAM_OVERVIEW.md): shared normalization, domains, goals, and the original research framework.
- [Inverse bulk realization](investigations/inverse-bulk-realization/README.md): the self-contained [working manuscript](investigations/inverse-bulk-realization/manuscript.pdf) collects sphere and Schur source calculations, an exact positive local prime norm, and domain and gluing restrictions. The complete Weil match remains open; [dated drafts](investigations/inverse-bulk-realization/drafts/README.md) preserve successive versions.
- [Research assessment, 14 September 2026](brainstorm/ASSESSMENT.md): compares the earlier proposals after the ground-state investigation and finite-response novelty review. Its later direction update moves the next task to exact bulk fitting.
- [Arithmetic ground-state geometry](investigations/arithmetic-ground-state-geometry/README.md): the investigation through note 20, including the finite-rank reduction and remaining arithmetic sign problem.
- [Boundary corrections and finite responses](manuscripts/finite-response-weil-positivity/README.md): a separate technical note with detailed derivations. Submission is deferred pending further work and reassessment; human mathematical review and novelty assessment remain necessary.

## Folder map

```text
susy-positivity/
  README.md
  PROGRAM_OVERVIEW.md
  background.tex                 # standalone wrapper and bibliography
  background_section.tex         # authoritative substantive background
  background.pdf                 # compiled reading copy
  brainstorm/                    # proposals, surveys, continuation context
    ASSESSMENT.md                # latest research-direction assessment
    candidate-bulk-theories/
    continuation-notes/
    theory-landscape-20260913/
  investigations/                # approach-specific research packages
    positive-factorizations/
    topological-susy-bulk/
    arithmetic-ground-state-geometry/
    inverse-bulk-realization/
    source-selection-rules/
    wilson-lines/
    loewner/
  manuscripts/                   # separate manuscripts drawn from the research
    finite-response-weil-positivity/
  archive/                       # historical reorganization record and path guide
  validation/                    # structure checker and historical relocation checks
```

The [brainstorm index](brainstorm/README.md) explains the dated proposals and
later reassessment. The [manuscript index](manuscripts/README.md) distinguishes
standalone notes from manuscripts retained within investigations.

## Investigations and current scope

| Investigation | Scope and status |
|---|---|
| [Inverse bulk realization](investigations/inverse-bulk-realization/README.md) · [PDF](investigations/inverse-bulk-realization/manuscript.pdf) · [drafts](investigations/inverse-bulk-realization/drafts/README.md) | Working manuscript 0.1: self-contained Weil normalization, sphere-sector pairings, a dressed Schur realization of the positive prime reference at one fixed quantization parameter, and magnetic-domain and mixed-return restrictions. Earlier gamma, gauge and rational-feedback tests are retained. The joint contact/pole match and all-support realization remain open. |
| [Source selection rules](investigations/source-selection-rules/README.md) · [PDF](investigations/source-selection-rules/manuscript.pdf) · [drafts](investigations/source-selection-rules/drafts/README.md) | Working manuscript 0.1, *A jump-process presentation of the localized Weil form*. A spin-off from inverse bulk realization that asks what the localized Weil form is rather than building a source: the archimedean symbol identified with the smooth zero density, the target presented as a single Lévy jump form whose atoms are the primes, the Perron--Frobenius structure and the rank-two pole term that breaks it, a necessary condition with a disproof test that found no violation, and nine selection rules. No source is constructed and no positivity is proved. |
| [Wilson lines](investigations/wilson-lines/README.md) · [PDF](investigations/wilson-lines/manuscript.pdf) · [drafts](investigations/wilson-lines/drafts/README.md) | Working manuscript 0.3, *Deformation flows for the shifted Weil family: the transfer as an all-pass filter*. Opened 17 September 2026 from a proposal that the shifted family is the deformation flow of a Wilson line. The transfer symbol is unimodular on the critical line, exactly and unconditionally, so the transfer is an all-pass filter; its phase derivative is the archimedean symbol, which explains the density identity; its phase jumps are resonances at the zeros, so the Weil form is a total resonant response; under RH it is inner and the contraction defect is the flux through the leading endpoint; and a filter that changes only phase is abelian, so the non-Abelian Stokes mechanism has nothing to act on along the shift. The contraction region is then settled: it is monotone in the length with supremum one or infinity, so contraction at every length is equivalent to the absence of zeros at distance more than the shift --- a graded criterion, with no critical path and only a disproof reading. What remains is the endpoint direction, where the algebra is triangular and flat. The form's exact symmetry group turns out to be the residual conformal group of a ray with one end pinned, so conformal symmetry is aligned with the target rather than in tension with it. No source is constructed and no positivity is proved. |
| [Loewner](investigations/loewner/README.md) · [manuscript](investigations/loewner/manuscript.pdf) · [notes](investigations/loewner/notes/README.md) | Opened 17 September 2026 from the Wilson-lines investigation, around a factorization of the shifted transfer: $K_\omega=B_b\widehat K_\omega$ with $B_b=\frac{p-b}{p+b}$ one first-order all-pass section at the pole of $\zeta$ ($b=\frac12+\omega$) and $\widehat K_\omega$ completely monotone, so the transfer kernel is an explicit positive measure --- a Beta-distributed archimedean delay (squared-Bessel additivity in dimensions $\frac12\mp\omega$) convolved with a multiplicative comb $\widetilde c_n=n^{\omega-\frac12}\prod_{p|n}(1-p^{-2\omega})$ at the integer ratios, with one further exponential smoothing --- minus twice its exponential moving average. The compressed transfer is thereby assembled exactly from elementary functions and the integers $n<e^L$. The comb is a Hecke/Bost--Connes semigroup structure and not a Loewner one; the correction is forced by the functional equation; at $\omega=\frac12$ the positive part is the Eisenstein scattering matrix of the modular surface. The compressed transfer built from the kernel alone is validated at $L=\log3$: a strict contraction whose defect reproduces the Weil-form margin in the same basis to $0.1\%$ at $\omega=0.01$, with the second-order defect $2\omega Q-\omega^2(2Q^2+[Q,A])$ and a zero-free closed form for the first-order tail. Manuscript *The Markov part of the shifted Weil transfer*, working draft 0.1 (25 pages), with a pedagogical introduction. No source is constructed and no positivity is proved. |
| [Positive factorizations](investigations/positive-factorizations/README.md) · [PDF](investigations/positive-factorizations/manuscript.pdf) · [status](investigations/positive-factorizations/STATUS.md) | Manuscript v0.2: short-window factors, gamma kinetic tower, restricted odd-sector factors, scoped obstructions, and a certified first-prime stabilization example. Separate round-4 reports extend the odd factor across shifts and isolate the remaining even scalar. A complete even factor, joint prime construction, and arbitrary-length mechanism remain open. |
| [Topological SUSY bulk](investigations/topological-susy-bulk/README.md) · [PDF](investigations/topological-susy-bulk/manuscript.pdf) · [status](investigations/topological-susy-bulk/STATUS.md) | Manuscript through 12 September: positive relative gamma complex, arithmetic loop responses, and correction obstructions. Separate 13 September notes construct a physical Fock realization and superspace boundary action and study finite-block restrictions. The full arithmetic norm remains open. |
| [Arithmetic ground-state geometry](investigations/arithmetic-ground-state-geometry/README.md) · [PDF](investigations/arithmetic-ground-state-geometry/manuscript.pdf) · [status](investigations/arithmetic-ground-state-geometry/STATUS.md) | Integrated manuscript through note 20: interacting local factors, physical caps, closed gamma source, pole gluing, prime returns, and a positive source equal to the full Weil form plus an explicit finite-rank positive error. The remaining finite response matrix is not proved positive. Includes the noncompact gamma boundary correction and residual estimates; an all-support physical source law remains open. |

The positive gamma kinetic construction is established within its stated
scope. Later constructions retain the normalization, poles, and primes in an
explicit signed remainder or finite-rank error; positivity of the auxiliary
source does not remove that error. Local results retain their support, shift,
and input restrictions. Internal checks do not replace specialist proof review.

## Standalone manuscript

[Boundary corrections and finite responses for the localized Weil form](manuscripts/finite-response-weil-positivity/README.md)
contains a [condensed note](manuscripts/finite-response-weil-positivity/manuscript.pdf),
[detailed derivations](manuscripts/finite-response-weil-positivity/derivations.pdf),
and its own review, build, provenance, and dated draft records. It develops
boundary corrections, truncation bounds, and finite-response enclosures from
the ground-state investigation. Its matrix conjecture remains unproved; the
numerical example is not a positivity certificate or demonstrated computational
advantage. See the [current evaluation](manuscripts/finite-response-weil-positivity/EVALUATION.md)
for the deferred publication status.

This folder moved from `papers/finite-response-weil-positivity/` to
`papers/susy-positivity/manuscripts/finite-response-weil-positivity/`.
The [review navigation guide](manuscripts/finite-response-weil-positivity/reviews/README.md)
maps preserved reviews to the drafts they assessed. Their old paths and line
numbers are historical references, not links to the current revision.

## Working conventions

Keep shared background at the program root. New approaches belong in
`investigations/<descriptive-name>/`, with a README stating their mechanism,
scope, status, and relation to the shared framework. Keep their working
manuscripts, notes, checks, and histories together. A separate manuscript
belongs in `manuscripts/<descriptive-name>/`, with an explicit source record,
review status, build instructions, and dated drafts. Exploratory proposals
and comparative assessments belong in `brainstorm/`.

Update this index when adding an investigation or manuscript. Distinguish
proved results, diagnostics, and proposals. Link to the shared background;
retain historical validation and snapshots under their original dates, and
refresh current file inventories explicitly after edits. The
[archive guide](archive/README.md) maps earlier layouts without rewriting
historical evidence. Follow the repository [large-file policy](../../LARGE_FILES.md).

## Build and verification

Run the structure check from this directory:

```sh
python3 validation/check_structure.py
python3 investigations/arithmetic-ground-state-geometry/validation/check_package.py --replay
python3 investigations/topological-susy-bulk/validation/check_package.py
```

The first checks current navigation, TeX dependencies, and selected current
file records while distinguishing historical links. The investigation checks
verify their complete package manifests; the ground-state replay also
reproduces 59 labelled exact-algebra checks. None is an analytical proof checker.

Build the shared background with a standard TeX distribution:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error background.tex
```

Use each package's build or replay guide for its outputs:

- [Positive factorizations](investigations/positive-factorizations/README.md): manuscript build and replay that preserves historical diagnostics.
- [Topological SUSY bulk](investigations/topological-susy-bulk/README.md): isolated build and numerical replay.
- [Arithmetic ground-state geometry](investigations/arithmetic-ground-state-geometry/BUILD.md): integrated manuscript build and package refresh procedure.
- [Finite-response note](manuscripts/finite-response-weil-positivity/BUILD.md): both document builds and review checks.
- [Candidate bulk theories](brainstorm/candidate-bulk-theories/REPRODUCE.md): model diagnostics and earlier certificate replay.

The [12 September verification record](validation/reorganization-20260912/VERIFICATION.json)
describes that reorganization, not a fresh build of later revisions.
