# Verification: first-slab positivity

This folder is the preprint's audit trail: what has been checked, by what
means, by whom, and what has not. The project's working rule is that machine
checking is not sufficient verification; the point of publishing these
records is to let human readers see exactly where the human checks still have
to happen.

```
verification/
├── README.md                     this file
├── CHECKLIST.md                  what to verify, how, and what failure would look like — for volunteers
├── PROTOCOL_C1_C2.md             hand protocol for the two premise checks: normalization against Suzuki [1], originality search
├── CERTIFICATE_RERUN_20260909.md clean pinned rerun of the (not yet public) certificate code; byte-identical tables
├── requirements.txt              pinned environment of the referee-round recomputations
├── reviews/                      the adversarial referee-round records (LLM-generated, recomputed): round 2
│                                 here, round 1 linked from the RH3 project files
├── scripts/                      recomputation scripts: two historical (referee round 1; preprint prep) and
│                                 one current executable diagnostic (9 Sept; run by CI) — see its README
└── repository-review-20260909/   the external review of the first repository commit and the author's response
```

The authoritative current status of the preprint is
[VERIFICATION_STATUS.md](../VERIFICATION_STATUS.md); `CHECKLIST.md` here is
the how-to that goes with it. The statement inventory is in
[../blueprint/](../blueprint/README.md) and the release gate of the
unreleased certificate code in [../CERTIFICATE_CODE.md](../CERTIFICATE_CODE.md).

The other manuscripts carry their result-by-result verification record and
review history in their own folders (`STATUS.md` or `VERIFICATION_STATUS.md`,
and `reviews/`) until they are released and get a verification folder of
their own. For the finite-horizon continuation, use the [Weil-depth status](../../weil-depth/STATUS.md)
and [storage-depth status](../../storage-depth/STATUS.md),
[claim records](../../storage-depth/CLAIMS.json) and
[closeout record](../../storage-depth/CLOSEOUT.md). Their review packets
remain with the papers under `archive/reviews/`.

Moved here on 16 October 2026 from the repository-root `verification/`
folder (its `first-slab/` subfolder, the root README and
`environment/requirements.txt`), with the 9 September repository review from
the former root `notes/`; see the
[relocation record](../../../../REORGANIZATION_20261016.md).

## Method used so far

Each manuscript went through referee-style review rounds in which every
reported constant was recomputed from the printed definitions, without access
to the primary code, and every analytic identity was re-derived. Corrections
were re-verified by recomputation, not accepted on assertion. For the
first-slab certificate there is in addition a clean-room reimplementation of
the whole interval computation (Section 7.6 of the preprint).

That apparatus is strong against implementation error and blind to premise
error, because every round shares the premises. [PROTOCOL_C1_C2.md](PROTOCOL_C1_C2.md)
is written for exactly the two premises it cannot test: that the operator
certified is the first slab of Suzuki's system (C1), and that the two central
identities are new (C2). It asks the checker to read Suzuki's paper before the
preprint, not after.

Three standing methodological rules, adopted after specific failures in the
research log (see [ROUND5_state_of_play.md](../../../../../early-chat-logs/initial-project-files/rh3/claude/ROUND5_state_of_play.md) §"Method note" and
[ROUND12_execution_and_a_retraction.md](../../../../../early-chat-logs/initial-project-files/rh3/claude/ROUND12_execution_and_a_retraction.md) §4.5):

1. For every claim of the form "X cannot happen", run the control that would
   show X happening in a case where it does.
2. For every claim of the form "X is new", run the search that would show X is
   old — before publishing.
3. Read the printed PDF; never build on a paraphrase of a display equation.

## How to contribute a check

Pick an open item from a `VERIFICATION_STATUS.md`, do it, and open an issue
with the **Verification report** template (`.github/ISSUE_TEMPLATE/` at the repository root). Report
negative results too. If you find an error, use the **Possible error**
template; a reproducible counterexample or a specific line reference is worth
more than a general concern.
