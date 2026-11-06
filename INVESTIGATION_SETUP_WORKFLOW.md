# Setting up investigations and research branches

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort ultra**. Investigation08 chat0003.

**Standing setup guidance requested by Edward Baker.** Apply this workflow whenever creating a new investigation, whether it is one folder at a specified location or several numbered branches beneath an existing investigation. The same scientific, reference, progress and continuation requirements apply in both cases.

This document governs organization and handoff. [AGENTS.md](AGENTS.md), [GPT_RESEARCH_MODEL_WORKFLOW.md](GPT_RESEARCH_MODEL_WORKFLOW.md), [REFERENCE_WORKFLOW.md](REFERENCE_WORKFLOW.md), [LARGE_FILES.md](LARGE_FILES.md) and [tools/CHAT_HISTORY.md](tools/CHAT_HISTORY.md) remain authoritative for their respective subjects. Do not edit generated AGENTS.md files or synced sources while setting up an investigation.

## 1. Establish the destination and scope

Read the applicable instructions, the parent README/overview/progress files, relevant existing research, the [result index](result-summaries/README.md) and the [patterns index](avoid/README.md). Identify the actual scientific question, inherited results and their evidence levels before writing a plan. Reuse established formats and sources in place.

For **several branches**, use the next available two-digit numbers within the requested parent, such as 01_direct_newman_realization and 02_hamiltonian_auxiliary_dynamics. Check existing folders, reserved numbers and historical names. Do not renumber an existing branch to make a new sequence look tidy. Each branch should have a distinct question or consumer; common foundations belong at the parent.

For **one new investigation at a specified location**, make that location the investigation root and apply this same workflow once. Do not insert an unnecessary intermediate branch folder or force numbering onto an explicitly supplied path. If only a parent is specified, follow its existing naming and numbering conventions.

Inspect an existing destination before writing. Continue its established documents and identities rather than overwriting them or creating competing overviews/registers. Ask only if the destination or scientific scope is materially ambiguous and cannot be resolved from the request and repository.

Creating folders and plans does not activate their research, run numerics, create new chats, or change other investigations' statuses. Apply any separate execution authorization the author actually gives.

## 2. Use the standard folder structure

For each new investigation or branch, prepare this structure. The numbered/date-bearing filenames should follow the destination's conventions.

    investigation_or_branch/
      README.md
      DRAFT_HISTORY.md
      research-overview/
        01_<TOPIC>_RESEARCH_OVERVIEW_<DATE>.md
      research-plan/
        01_<TOPIC>_RESEARCH_PLAN_<DATE>.md
      research-progress/
        01_<TOPIC>_RESEARCH_PROGRESS_<DATE>.md
        handoffs/
      notes/
      numerics/
      reviews/
      brainstorm/
        notes/
      references/
        README.md
      chat-histories/
        README.md

Use short purpose/pointer READMEs to retain initially empty working directories when needed. Do not invent research notes, reviews, computations or chat registrations just to populate a folder. A bibliography is maintained locally or linked explicitly to its canonical existing home, as described below. Add a compact source catalog/download manifest when the reference collection warrants it.

Do not create a manuscript, generated PDF or snapshot folder as part of routine setup. A later authorized manuscript names Edward Baker or says it was drafted for him, acknowledges LLM assistance, and follows LARGE_FILES.md for its output location.

The roles are:

| Location | Purpose |
| --- | --- |
| README | Short purpose, current entry points, parent/sibling links and ownership |
| research-overview | Scientific background, question, inherited evidence, mechanisms and unresolved premises |
| research-plan | Bounded task specifications and dependencies |
| research-progress | Sole live task-status register for its declared task family |
| research-progress/handoffs | Issued requests, exact input versions, returns and model-change packets |
| notes | Incremental derivations, research records and continuation notes |
| brainstorm/notes | Consequential conceptual choices and mechanism/goal decisions |
| numerics | Authorized code and small execution records; large derived data remain external |
| reviews | Assessments with actual reviewer/model and shared-premise scope |
| references | Canonical article records or explicit pointers, bibliography and branch-use/inspection notes |
| chat-histories | The tool-managed public conversation archive and its provenance guide |
| DRAFT_HISTORY | Concise notable milestones with date, investigation, artifact/commit/tag, reason and supporting links |

For a multi-branch parent, keep shared notes, reference records and cross-branch history there. Link to shared material from each branch rather than moving it or duplicating its evidence. Existing arrangements with an integrated overview/plan can be retained; new investigations normally get the separate overview and plan shown above.

## 3. Write a substantive overview and bounded plan

An overview should identify the concrete question, fixed objects and normalization, relevant parameter/index domains, known baseline, what is inherited or conditional, candidate mechanisms, and the precise unresolved decisions. Separate a physical interpretation, representation identity, diagnostic, intermediate estimate and target-equivalent reformulation. Explain the intended consequence without asserting an unproved gain.

Cite the [result index](result-summaries/README.md) and [avoid index](avoid/README.md), with the specific applicable entries. For theta/Newman work, carry the [collision controls](result-summaries/12_collision_controls_and_screening.md), [target-classification rule](avoid/01_restating_the_target.md), [control-premise rule](avoid/02_shape_only_arguments_and_the_controls.md), [coordinate-realization caution](avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [scoped-exclusion rule](avoid/07_scoped_exclusions_read_as_universal.md). Preserve the source's evidence words and quantifiers.

Classify tasks **before execution**, following GPT_RESEARCH_MODEL_WORKFLOW.md. Every task needs:

- A stable ID and B/E type, recommended model and task-specific reason.
- Readiness, exact dependencies and what remains undecided.
- Concrete deliverable, evidence standard and completion condition, including a possible scoped failure.
- A finite work limit, permitted routine choices and named conceptual escalation trigger.
- The source, equation, observation, domain, inputs and proof/computation method whenever an executable request is issued.

Use **B / Astra** for consequential choices of mechanism, physical construction or target; use **E / Sol** for a fixed derivation, implementation, calculation or assessment. Record actual model/effort from metadata, separately from recommendations; mark unavailable settings as unavailable. The author chooses model, effort and continuation order.

Do not manufacture an executable packet while its source, generator, observable or success test remains open. Reserve the E task and name the B decision it needs. A plan can stop after one useful result; do not pad it with a compulsory sequence of future research.

## 4. Give every task one live status owner

Each new investigation/branch normally receives its own progress file, explicitly designated the **sole current register for its task family**. Use distinct task prefixes for branches. The parent owns only shared tasks and links to branch registers; it must not maintain a second live copy of their rows.

At setup, state whether tasks are ready and unactivated, reserved, or dependent on a named input. “Ready” does not mean proved. Read the live entry again before later edits and retain other chats' updates. Assign one writer to each shared artifact.

When branching an existing plan, include a dated crosswalk: which completed identities and issued requests remain unchanged, which unissued slots are superseded, which unresolved questions move to new branch IDs, and which assessment or tool is shared. Keep historical evidence and failed attempts. A superseded placeholder is not a completed theorem.

For a single new investigation, its register owns its one task family; no parent/shared ledger is needed unless actual shared work exists. If replacing a register, designate the new owner and mark the previous one historical instead of leaving two competing status sources.

## 5. Apply REFERENCE_WORKFLOW.md from the start

**Read and follow [REFERENCE_WORKFLOW.md](REFERENCE_WORKFLOW.md) at setup and during research. This is an active part of the workflow, not a bibliography task deferred until manuscript preparation.** The author has requested closer adherence from this point forward. Backfill references as work is resumed, starting with sources already used in current notes and manuscripts; describe the actual bounded backfill, not a repository-wide audit.

The application within a branch is:

1. **Record a relevant article when found.** Add it to the affiliated references/ index, or link an existing canonical record and record this branch's use. Search parent/sibling catalogs first. Maintain one canonical article record within an investigation; across investigations, link rather than duplicate annotations unnecessarily.
2. **Choose and state the canonical home.** Shared articles normally live in the parent catalog with branch-use links. A branch-specific collection may live in that branch. Every branch references/README.md states this ownership and links the reusable BibTeX bibliography. An explicit pointer to an existing bibliography is preferable to a competing copy. A standalone investigation uses its own references/ unless it is reusing a named existing canonical record.
3. **Cite at the point of use.** In a research note, review, overview or manuscript, attach the source to the actual imported claim, name the theorem/equation/section/page, and preserve the hypotheses, normalization, quantifiers and regime being used. Cite the internal derivation/assessment as well when the claim is inherited through repository work. A bibliography alone does not show which claim depends on which source.
4. **Record what was inspected.** Include authors, exact title, publication/preprint identifier, version/date, retrieval/inspection date, stable primary link, relevance and consuming note/section. Distinguish discovery, abstract-only inspection, checked passages and full reading. Check the primary source before newly importing a theorem. Reusing an inherited checked passage is not a fresh full-paper check.
5. **Retain limitations and provenance.** Record corrections, withdrawals, extra hypotheses, normalization changes and unexamined newer versions. Update newly checked passages or versions without silently erasing earlier provenance. Attribute an existing argument even if a similar calculation was first derived locally.
6. **Store reading copies correctly.** Follow LARGE_FILES.md: third-party PDFs stay outside Git regardless of size, normally in the external archive. Record stable source URL, retrieval date, archive location, byte size and SHA-256; verify the response is a PDF. Never bypass access controls or silently replace a different version. If retrieval fails, record that fact and continue unaffected work. A file hash establishes identity, not mathematical validity. Online sources may use section links and retrieval dates without artificial PDF copies.

Use short original annotations, not copied abstracts or substantial article text. Do not invent citations, checked passages, retrieval dates or download records to make a scaffold look complete. A reference index may accurately say that it currently contains inherited pointers only. See also [unchecked imports](avoid/16_unchecked_imports_and_novelty_claims.md).

## 6. Preserve chat history and evidence

Follow tools/CHAT_HISTORY.md at the start and end of the reply. A new branch-only conversation registers at that branch; a new single-investigation conversation registers at its specified root; a shared setup conversation stays at the parent. An already registered conversation keeps its unique existing home, number, filename and provenance unless the author requests relocation. Creating folders alone is not relocation authorization.

Use the recorder, its locks and its integrity checks. Do not hand-edit registered JSON, duplicate a chat in each branch or place raw transcripts in Git. Arrange the bounded exact-turn final capture until native hook activation is verified. Do not claim the unsent final message has already been archived.

Preserve input/source versions and all issued packets. Notes and reviews state date, intended author, LLM assistance, actual model/effort and evidence level. Keep DRAFT_HISTORY concise; detail belongs in linked notes/reviews. New milestones point to artifacts or commits/tags, not new manuscript snapshot folders.

## 7. Finish every setup with a continuation note and pasteable prompts

**After creating branching subfolders—or one new investigation—save a continuation note with a self-contained pasteable prompt for every new branch/investigation. This is part of completing setup.**

For several branches, a shared continuation note in the parent's notes/ can cover all of them; link it from every branch README and progress file. For a single investigation, put it in that investigation's notes/. Avoid competing copies; refresh the canonical note when a later handoff warrants it and retain dated history.

The continuation note must contain:

- A brief outcome and unresolved question for each branch, with its current evidence level.
- A routing table near the start: task ID, B/E type, recommended model/reason, readiness/dependencies and expected output. The live register remains authoritative; date the note as a handoff snapshot.
- Links to the exact destination, overview, plan, sole progress register, source/return records, reference index and relevant controls.
- One pasteable prompt per branch, naming its repository-relative path, next task and scope, inputs, output location, success/stop condition, reference workflow and chat-history destination rules.
- Any shared dependency, status-ownership boundary and execution limits. Say whether the task may execute now or merely decide/freeze a request.

Prompts should stand alone in a new chat, without relying on “the folder above” or inaccessible conversation context. Use the chosen task IDs and current specifications; do not activate later tasks by wording a continuation prompt. Include a default next task only when priority is settled; otherwise preserve the author's choice among branches.

## 8. Check and link the completed setup

Check local links, task-ID ownership, dependency consistency, input provenance and file sizes. Verify that no source, issued request or existing chat identity was silently changed. No mathematical tests or numerical runs are required merely for directory/document setup.

Link the new location from its parent/index, and link this workflow when helpful for future sessions. Record a concise setup milestone and provide the user with links to the new entry points and continuation note. Report any incomplete reference backfill accurately. Leave all unactivated research tasks unactivated.

## Reusable setup request

> Read AGENTS.md, INVESTIGATION_SETUP_WORKFLOW.md, GPT_RESEARCH_MODEL_WORKFLOW.md, REFERENCE_WORKFLOW.md, LARGE_FILES.md and tools/CHAT_HISTORY.md. Create [the named numbered branches under PARENT / one new investigation at EXACT_LOCATION], using the stated scientific questions and inherited evidence. Prepare the standard folder structure, substantive overview, bounded B/E research plan and sole progress register for each task family, with parent navigation and a dated task crosswalk where needed. Establish reference ownership and point-of-use citation practice, reusing canonical records and backfilling only the sources actually needed. Preserve evidence, issued requests and existing chat identities. Finish with a saved continuation note containing a self-contained pasteable prompt for each new branch/investigation. Record actual model/effort, check links and file sizes, and continue chat-history capture. Setup alone must not execute research or numerics or alter external statuses.
