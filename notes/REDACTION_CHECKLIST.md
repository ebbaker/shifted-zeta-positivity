# Redaction checklist for the research log

The notes were written as session reports inside a private project. Before
any of them is committed to a public repository — and certainly before a
release tag archives them permanently on Zenodo — each file goes through this
list. Tick the file off in the table at the bottom.

## What to remove or rewrite

1. **Draft correspondence.** Letters or messages to named people, sent or
   unsent. Replace with one line: "A letter was sent to ⟨name⟩ on ⟨date⟩
   asking ⟨topic⟩" — or remove entirely.
   - Known instance: `PROGRESS_psi_omega_next_steps.md` §4b (draft letter to Suzuki).
2. **Outreach shortlists and personal characterizations of named people.**
   Lists of who to contact, how the author knows them, how they might react,
   what they lead. Remove; a public repo can say "specialist review has been
   sought" without names.
   - Known instance: `ROUND19_endpoint_length_and_freeze.md` §5 (shortlist with
     characterizations; "the user knows him obliquely").
3. **Negative verdicts on named authors' papers phrased as instructions.**
   "Fatally flawed, do not cite" about a specific paper is a legitimate
   scholarly judgment in private notes; in a public archive it reads as an
   attack. Either remove, or restate neutrally with the specific technical
   reason ("the quaternionic content plays no role in the argument") and
   without the imperative.
   - Known instance: `BRIEF_three_live_routes.md` §3.5 (Tang, MDPI *Symmetry* 2025).
4. **Third-person references to the author.** The notes say "the user";
   replace with "the author" or first person, or leave and let the preface
   explain (see below). Decide once and apply uniformly.
5. **Internal paths and tooling.** `claude/…` paths, "session workspace",
   "agent-run", retrieval-attempt logs of specific web tools. Replace paths
   with repository paths (`notes/…`, `code/…`); keep the *lesson* of the
   retrieval failures (it is a house rule) but drop the tool-by-tool list.
   - Known instance: `ROUND11_freeboson_and_positivity.md` §7 (retrieval note lists ~15 services).
6. **User-supplied memos referenced by filename.** `Variants_of_data.md`,
   `Round5.md`, `ROUND6_manuscript.md` are private inputs. Either add them
   (redacted) to `notes/` or describe them in a sentence.
   - Known instances: `NOTE_variation_axes.md` §3 header; `LAB_ihara_round5.md` header; `ROUND6_closeout.md` header.
7. **Extended verbatim quotation from sources under copyright.** Short quotes
   with attribution are fine. Anything that reads as a transcription of a
   page (the Suzuki PDF text pasted in a note, long Connes/Burnol passages)
   should be cut to the sentence actually relied on, with a citation.
8. **Email addresses and contact details of anyone but the author.**
9. **Claims later retracted or corrected.** Do *not* silently fix them — the
   record is the point. Instead add a one-line header pointing to the
   correction: "Superseded in part by `ROUND12` §6; see corrections table there."
   - Known instances: `NOTE_connes_weil_dirichlet_form.md` (novelty withdrawn);
     `NOTE_n4_reformulation.md` v1 constants; `ROUND10` items corrected in `ROUND11` §5.

## What to add

- **Preface** at the top of `notes/README.md` (already drafted there): the
  notes are round reports written by a language model under the author's
  direction, exploratory, containing closed routes and corrected claims; not
  peer-reviewed; the papers and `verification/` are the reliable layer.
- **Per-file header** (three lines): date; thread; status (*live / closed /
  superseded by …*).

## Search aids

```bash
grep -rn -i -E "dear |letter|shortlist|knows him|knows her|do not cite|fatally|the user|claude/|session workspace|agent-run|@" notes/
```

Expect hits for "the user" in nearly every file; decide the convention in item 4 first.

## Tracking

| File | Reviewed by | Date | Items applied | Cleared for public |
|---|---|---|---|---|
| `PROGRESS_psi_omega_next_steps.md` | | | 1, 4, 5 | |
| `ROUND19_endpoint_length_and_freeze.md` | | | 2, 4, 5 | |
| `BRIEF_three_live_routes.md` | | | 3, 4 | |
| `ROUND11_freeboson_and_positivity.md` | | | 5, 7 | |
| `ROUND12_execution_and_a_retraction.md` | | | 4, 5, 9 | |
| `NOTE_variation_axes.md` | | | 4, 6 | |
| `LAB_ihara_round5.md`, `ROUND6_closeout.md` | | | 6 | |
| `NOTE_connes_weil_dirichlet_form.md`, `NOTE_n4_reformulation.md`, `ROUND10_boundary_data.md` | | | 9 | |
| all remaining notes | | | 4, 5, 7 as found | |
