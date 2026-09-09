# Verification

This directory is the audit trail. It answers, for each manuscript: what has
been checked, by what means, by whom, and what has not. The project's working
rule is that machine checking is not sufficient verification; the point of
publishing these records is to let human readers see exactly where the human
checks still have to happen.

```
verification/
├── README.md                 this file
└── first-slab/
    ├── CHECKLIST.md          what to verify, how, and what failure would look like — for volunteers
    ├── PROTOCOL_C1_C2.md     hand protocol for the two premise checks: normalization against Suzuki [1], originality search
    ├── CERTIFICATE_RERUN_20260909.md   clean pinned rerun of the (not yet public) certificate code; byte-identical tables
    ├── reviews/              the two adversarial referee-round reports (LLM-generated, recomputed)
    └── scripts/              recomputation scripts: two historical (referee round 1; preprint prep) and
                              one current executable diagnostic (9 Sept; run by CI) — see its README
```

The four working drafts under `papers/` do not have verification folders yet;
each draft's `STATUS.md` carries its result-by-result verification record and
its review history until it is released and gets a `blueprint/` entry and a
folder here.

The authoritative current status of the first-slab preprint is
`papers/first-slab-positivity/VERIFICATION_STATUS.md`; `CHECKLIST.md` here is
the how-to that goes with it.

## Method used so far

Each manuscript went through referee-style review rounds in which every
reported constant was recomputed from the printed definitions, without access
to the primary code, and every analytic identity was re-derived. Corrections
were re-verified by recomputation, not accepted on assertion. For the
first-slab certificate there is in addition a clean-room reimplementation of
the whole interval computation (Section 7.6 of the preprint).

That apparatus is strong against implementation error and blind to premise
error, because every round shares the premises. `first-slab/PROTOCOL_C1_C2.md`
is written for exactly the two premises it cannot test: that the operator
certified is the first slab of Suzuki's system (C1), and that the two central
identities are new (C2). It asks the checker to read Suzuki's paper before the
preprint, not after.

Three standing methodological rules, adopted after specific failures in the
research log (see `notes/ROUND5_state_of_play.md` §"Method note" and
`notes/ROUND12_execution_and_a_retraction.md` §4.5):

1. For every claim of the form "X cannot happen", run the control that would
   show X happening in a case where it does.
2. For every claim of the form "X is new", run the search that would show X is
   old — before publishing.
3. Read the printed PDF; never build on a paraphrase of a display equation.

## How to contribute a check

Pick an open item from a `VERIFICATION_STATUS.md`, do it, and open an issue
with the **Verification report** template (`.github/ISSUE_TEMPLATE/`). Report
negative results too. If you find an error, use the **Possible error**
template; a reproducible counterexample or a specific line reference is worth
more than a general concern.
