# Contributing

This repository is organised around verification rather than feature work.
The most valuable contribution is a human check of something that has so far
only been checked by machine.

## Verifying something

1. Open the relevant `VERIFICATION_STATUS.md` (per paper) and the matching
   `CHECKLIST.md` under `verification/`. Pick an item marked ⬜ or 🔶.
2. Do the check against the **published sources**, not against this project's
   restatements of them. For a computation, work from the definitions printed
   in the paper, not from the project's code.
3. Open an issue with the **Verification report** template. Say what you
   checked, how, to what precision, and what you found — including "it holds".
   Negative results and "I could not complete this because …" are both useful.
4. If the check passes, the maintainer updates the status file and credits
   you there (opt out if you prefer).

## Formalizing something

`blueprint/<paper>/statements.md` lists every statement with a feasibility
estimate for a Lean 4 / Mathlib formalization, and the section "Where a
formalization effort would start" ranks the entry points. Issues labelled
`formalization` track them; `good-first-check` marks the elementary ones
(for the first slab: Lemma 7.1, the polynomial part of Lemma 6.1, the
modular-endpoint and Dirichlet-series identities).

1. Open a **Formalization** issue naming the statement id (e.g. `fs:S19`)
   before starting, so two people don't formalize the same lemma.
2. Formalize the statement *as printed*, in a standalone Lean file under
   `formal/<paper>/` (created on first contribution), with the statement id
   in a docstring. If the printed statement is wrong or under-specified, say
   so in the issue — that is a verification result in itself.
3. When a statement is formalized, its `formalization` field in the blueprint
   and `statements/ledger.yaml` gains `lean: <path>#<decl>`, and its
   `human_check` state becomes `done` with your name.
4. Certificate-type statements (the interval computations) are formalized by
   a verified checker over the stored certificate data, not by re-deriving
   the numbers; the certificate data are released under `code/certificates/`
   once their own gate (D1–D5) is passed.

The project uses leanblueprint conventions so that `blueprint/` can become a
real leanblueprint project without rewriting the statements.

## Reporting a possible error

Open an issue with the **Possible error** template. Give the paper, version,
section and equation number, the statement you believe is wrong, and — if you
can — a counterexample, a recomputation, or the line of the proof where it
breaks. A specific, reproducible objection will be acted on quickly; a general
concern will be discussed but may not be resolvable.

## House rules (learned the hard way)

These come from specific failures recorded in `notes/` and are applied to every
claim in this repository:

1. **Run the control.** For every claim "X cannot happen", run the control that
   shows X happening in a case where it does.
2. **Search before claiming novelty.** For every claim "X is new", run the
   search that would show X is old — before writing it down. One note here was
   retracted the day it was published because this was done in the wrong order.
3. **Read the printed PDF.** Never build on a paraphrase of a display equation.
   Automated readings of long PDFs have fabricated content in this project.
4. **Verify object type before building.** Lexical co-occurrence in a
   literature search is not structural relatedness.
5. **Say what was and was not checked.** Every note and paper carries its own
   status ledger. Keep it accurate when you change anything.

## Disclosure

Work in this repository was produced with substantial language-model
assistance. Contributions that use such tools are welcome; say so in the issue
or pull request, and apply the house rules above to the tool's output as you
would to your own.

## Licensing of contributions

Text contributions are accepted under CC BY 4.0, code under MIT (see the
dual-license notice in `LICENSE`).
