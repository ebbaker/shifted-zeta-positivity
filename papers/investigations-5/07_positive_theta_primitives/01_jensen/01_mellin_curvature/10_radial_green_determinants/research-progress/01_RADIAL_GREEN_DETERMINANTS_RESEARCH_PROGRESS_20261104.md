# Radial Green determinants research progress

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex),
effort xhigh**, chat 01a1a749-3920-78b1-a660-223790a78876, turn
01a1a753-26b4-79e3-93d5-b03b12432bc5.

**This is the sole live register for RGD tasks.** The
[overview's research plan r2][plan] owns their mathematical specifications.
No earlier local progress register exists. The parent Jensen J register
and all MC registers keep their existing task identities and ownership;
RGD tasks are new local work, not renamed or completed parent tasks.

## Current state

**Current priority: [B] RGD-B03 r2 — Astra, ready for investigation.**
The author redirected the program toward the overall induction argument
and complete-error control as the coefficient index increases. [Plan r2][plan]
and [Packet10][packet10] supersede the earlier default sequence of further
finite-case execution/assessment before B03. The conceptual task is now
ready; no induction theorem or uniform index bound is claimed. This turn
revises documentation only; the new mechanism attempt has not been run.

The next analytical return must state a noncircular quantitative H_r,
attempt its propagation to H_(r+1), and compare margin decay with complete
error growth over small k, k near r and unbounded k. Any split at K(r)
must expose its order dependence and an analytical argument for the
portion below the split. The fixed entry-relative envelope's nonuniformity
is an input to this investigation, not a reason to postpone it.

**Numerical policy:** future numerical work only tests a predeclared
hypothesis about that mechanism or its error control, with finite cases,
predictions, complete error accounting, a cap and a decision for every
outcome. No new numerical task is issued. E02 r2 remains completed;
E04 r3 remains an available, optional assessment of existing evidence and
is not a prerequisite for B03. Previous returns and their review levels
are preserved below. Planning revision: Astra/max, 4 November 2026.

### Retained evidence

The inherited Green identities retain their analytical and 25-case exact
algebra status. **RGD-B01 and RGD-E04 r1 are complete**: [Note01][note01]
proves the boundary-preserving primitive-moment and joint-residual estimates;
[Review01][review01] accepts all eight analytical checks without correction.
The assessment is different-model internal review (Astra/max to Sol/ultra),
with shared premises, not independent specialist review.

**RGD-E03 r1 is complete — both fixed cases are favorable floating
diagnostics.** [Note02][note02] and its [execution record][record03] report
q/R about 1375.6323 at k=1 and 2429.7587 at k=4. The 80/120-digit passes
agree within 2.983e-67 over the tested quantities; no 160-digit pass was
triggered. One bounded run used 46,056 evaluations and 1.677 seconds.
Exact polynomial checks passed. These are not certified positive bounds;
quadrature and rounding remain unenclosed, and nonzero B additions rounded
to E. No new positivity range, Mellin/Gaussian bound or order theorem follows.

**RGD-E02 r1 is complete — both lower allowances certified.**
[Note03][note03], [certificate][cert02] and [Self-assessment02][self02]
record Q3,1>=L1,2>7e-23 and Q3,4>=L4,2>1e-74 for the fixed complete
time-zero source. A single 384-bit Arb/FLINT acquisition used 4,546
callbacks and 0.714 seconds; exact saved-record verification passed.
No refinement, extra index or acquisition replay occurred. The E03 stage
remains floating evidence; its acquisition/rounding gap is resolved by
this separate rigorous return. E02 currently has author/self-checks with
fresh same-model contributions, not separate specialist review.

**RGD-E04 r2 is complete — accepted without correction.**
[Review03][review03] accepts all eight checks and both exact rational
lower bounds. The unchanged standard-library record verifier passed in
0.741 seconds; direct Fraction checks confirm complete outward E+B and
both dyadic/rational witnesses. No integration replay or new index was
acquired. This is same-assistant/same-model assessment with one fresh
contributing analytical check, not independent specialist review.

**RGD-B03 preparation is complete as a bounded analytical return.**
[Note05][note05], actual Astra/max, supplies the conditional (4,1) norm/
margin lemma and scoped failure of a uniformly small entry-relative
envelope. Its full-degree error estimate has now passed the E02 r2
analytical and exact input checks. k=2,3,4, the k=5 pure-volume triple
and uniform index/order conditioning are not covered by that application.
These are missing domains in the overall argument, not a prescribed
queue of numerical checks or a gate on the new B03 mechanism investigation.

**RGD-E02 r2 is complete — the fixed existing-data application passes.**
[Note06][note06], [exact record][recordr2] and [Review04][review04] establish
R4,1/q4,1*<1/15 and Q4,1>=L4,1>7/3000^9>3e-31, with all degree-eight
and complete E+B terms paid. All coarse coefficient/ratio/tail premises
and formal identities pass. One Python-standard-library run used
0.023964500 seconds and zero integrand evaluations; no correction,
new moment or old integration/verifier replay occurred. The matched
<1/120 and <1/15 ceilings are conservative analytical bounds, not
measured error growth. Inherited actual D3,1>0 supplies the D5 consumer.

The current E02 r2 evidence has different-model internal analytical
checking of Astra plus author checks of Sol code, with shared accepted
acquisition/library premises. [Packet09][packet09] retains its frozen
E04 r3 assessment contract, now optional and nonblocking under plan r2.
No specialist independence or all-order conclusion is claimed.

**Next: [B] RGD-B03 r2 — Astra**, under [Packet10][packet10]: investigate
the induction mechanism and index-dependent error control. B02 is
conditional on a specific obstruction requiring redesign. Earlier
requests, sources and records remain unchanged; no new computation is
part of this planning revision.

Model recommendations follow [GPT_RESEARCH_MODEL_WORKFLOW.md][workflow].
Edward Baker chooses the actual model, effort and chat. A B task can
produce a proof or decision; a fixed proof route is E and recommended
for Sol. Readiness is a workflow status, not a mathematical claim.

## Task register

The linked specification for each task contains its deliverable, evidence
standard, completion test, finite scope and conceptual escalation rule.
Those requirements are part of this register's task entries.

| ID and specification | Type | Recommended model and reason | Current status | Dependencies and expected output |
| --- | --- | --- | --- | --- |
| RGD-E01 — plan and register | E | **Sol**: documentation and consistency checking | **r1/r2 completed — documentation only, 4 Nov 2026** | r2 implements the author's induction/index-error focus. Actual revision Astra/max; no new mathematical claim or numerical task. |
| [RGD-B03][b03] — induction and index growth | B | **Astra**: the quantitative invariant, margin propagation and error control are unresolved | **r2 ready — default next; mechanism attempt unstarted** | [Packet10][packet10]: one worked overall induction attempt with explicit r/k dependence and a proved step, exact open estimate or scoped obstruction. Earlier preparation and E02 r2 retained; further low-order checks are not prerequisites. |
| [RGD-B01][b01] — select joint comparison | B | **Astra**: selecting a theta-specific input that controls signed cancellation | **Completed — bounded return, 4 Nov 2026** | [Note01][note01]: first-mode comparison and complete joint residual, accepted by E04 Review01. A candidate input to B03, not an established induction mechanism. |
| [RGD-E02][e02] — derive a specified comparison/lemma | E | **Sol**: execute a fixed analytical route and error accounting | **r1 accepted; r2 completed; further revision conditional and unissued** | [Note06][note06] and [record][recordr2] retain the fixed (4,1) result. New work requires a B03/B02 general-lemma contract; any numerical component follows the hypothesis-only rule. |
| [RGD-E03][e03] — bounded hypothesis test | E | **Sol**: fixed implementation to discriminate a stated mechanism hypothesis | **r1 completed; further tests conditional and unissued** | Earlier [Note02][note02]/[record][record03] remain floating evidence. New tests need a prediction, finite cases, error standard, cap and decision; no certificate campaign. |
| [RGD-E04][e04] — assess and integrate | E | **Sol**: check one stated argument against its contract | **r1/r2 accepted; r3 available, optional, unstarted** | [Packet09][packet09] remains frozen. Its finite-application assessment is nonblocking for B03; no new acquisition. Future assessments address the specific mechanism/lemma returned. |
| [RGD-B02][b02] — repair or stop mechanism | B | **Astra**: a named mathematical premise or strategy must change | **Conditional; inactive** | A specific obstruction from B03 or another return; one bounded repair decision or scoped stop, preserving prior evidence. |

B01 was started and completed under the author's research request in
chat0002, **gpt-6-astra / max**, thread
01a1a75a-0fb3-7e02-a1a5-092d309ba58a, turn
01a1a75a-1205-71a1-a2ed-5a1cfd44d617. One primary candidate was assessed;
no optional alternative, new numerical implementation or model dispatch
was performed. The frozen E04/E03 contracts specify exact inputs,
permitted files, acceptance tests and stopping rules. E02 was subsequently
issued as Packet04 after favorable E03 evidence and is now complete.
E04 r2 has now accepted its fixed return.

## Issued requests and returns

Entries below retain their status at issue/return. Plan r2's later
priority revision is recorded at the end; current readiness is above.

| Date | Task / revision | Request, return and consequence |
| --- | --- | --- |
| 4 Nov 2026 | RGD-E01 / planning r1 | Author requested a plan section and matching progress file under the root model workflow. Completed the overview addition and navigation; checked links, task correspondence, unchanged inherited equations (1)–(18), formatting and file sizes. Same-assistant documentation checks only. No substantive research executed. |
| 4 Nov 2026 | RGD-B01 / r1 | [Issued conceptual specification][b01]: one primary comparison, at most one alternative, one worked attempt, k=1 and k=4 structural cases. Request preserved; completed return recorded below. |
| 4 Nov 2026 | RGD-B01 / r1 return | [Note01][note01] completes one worked attempt, with explicit moment and joint-residual estimates and an unmeasured two-case sufficient test. Proof-author checks only; no new positive determinant bound. |
| 4 Nov 2026 | RGD-E04 / r1 request | [Packet01][packet01] freezes eight analytical checks of B01; at issue ready and unstarted; recommended Sol. |
| 4 Nov 2026 | RGD-E03 / r1 request | [Packet01][packet01] freezes the exact k=1,4 feasibility question, all mode/spatial payments, arithmetic, caps and outcomes; gated on E04. No implementation or return at issue. |
| 4 Nov 2026 | RGD-E04 / r1 return | [Review01][review01], actual Sol/ultra, chat0003: all eight analytical checks accepted without correction; author explicitly authorized E03 after acceptance. |
| 4 Nov 2026 | RGD-E03 / r1 return | [Note02][note02] and [record][record03], actual Sol/ultra: both k=1,4 favorable, 80/120 digits consistent, no 160 trigger; 46,056 evaluations, 1.677 s. Floating evidence only; E02 recommended, unissued at that return. |
| 4 Nov 2026 | RGD-E02 / r1 request | [Packet04][packet04] frozen before acquisition under the author's explicit continuation request: rigorous eight-moment/two-case acquisition, outward full tails, 384/conditional 512 bits, 180 s and 200,000 callbacks. |
| 4 Nov 2026 | RGD-E02 / r1 return | [Note03][note03], [certificate][cert02], [Self-assessment02][self02], actual Sol/ultra: both exact weaker rational floors certified; one 384-bit pass, 4,546 callbacks, 0.714 s; standard-library record verification passed in 0.749 s. Author checking with shared premises. |
| 4 Nov 2026 | RGD-E04 / r2 request | [Packet05][packet05] freezes eight checks of E02's certificate and consequence; ready for separate internal assessment, recommended Sol; no new integration. |
| 4 Nov 2026 | RGD-E04 / r2 return | [Review03][review03], actual Sol/ultra, same-assistant assessment with fresh same-model contributor: all eight checks accepted without correction; exact record verification passed, no integration repeated. |
| 4 Nov 2026 | RGD-B03 / preparation suggestion | Author requested an Astra task to run in parallel. [Brief06][brief06] proposes eligibility/order-dependence work within B03, without executing it or releasing the full extension gate. |
| 4 Nov 2026 | RGD-B03 / preparatory return | Author requested preparation alongside assessment. [Scope07][scope07] and [Note05][note05], Astra/max: one conditional (4,1) lemma, relative payment <1/15, matched old-order <1/120, and scoped nonuniformity of the entrywise envelope. No numerical implementation or new acquisition. Full B03 remains gated. |
| 4 Nov 2026 | RGD-E02 / r2 request | [Packet08][packet08] freezes exact verification from six saved moment/tail inputs and the conditional >3e-31 witness at (4,1). At issue ready/unstarted; no new integration, indices or precision. |
| 4 Nov 2026 | RGD-E02 / r2 return | [Note06][note06], [record][recordr2], [Review04][review04], actual Sol/ultra, chat0003: fixed box, formal identities and full-degree closure pass. Q4,1>=L4,1>3e-31; one 0.023964500 s exact run, zero integrand evaluations; no correction or acquisition. |
| 4 Nov 2026 | RGD-E04 / r3 request | [Packet09][packet09] freezes eight assessment checks of the new existing-data return and Note05 lemma; ready for Sol, unstarted; full B03 stays gated. |
| 4 Nov 2026 | RGD-E01 / planning r2 | Author requested emphasis on the overall induction mechanism and error control as k grows, with numerics only for hypothesis tests. Updated plan, register and navigation after Sol finished; all completed evidence and frozen requests preserved. Actual Astra/max, chat0002; documentation only. |
| 4 Nov 2026 | RGD-B03 / r2 priority and contract | [Plan r2][plan] and [Packet10][packet10] make the bounded induction/index-error investigation ready and the default next task. Earlier workflow gating is superseded; no induction theorem is claimed. E04 r3 becomes optional and nonblocking; no new E02/E03 test is issued. |

All issued requests are frozen; append dated returns without rewriting
their original questions or adverse evidence.
No automatic research, model change or other-chat dispatch is scheduled.

## Evidence and ownership

The [inherited derivation][n06], [exact checker][checker] and
[original record][record] stay at their existing locations and review
status. [Result summaries][results], especially [theta identities][theta]
and [collision controls][controls], and [patterns to avoid][avoid],
especially [target reformulations][a01] and [joint signed estimates][a12],
govern the research claims. A positive-time collision alone is not a
counterexample to a time-zero finite-order inequality.

Each return must record actual date, model/effort, request revision,
inputs, outcome, domain, errors, deviations, unresolved premises and
next declared B/E task. Exact algebra, floating diagnostics, interval
certificates and general proofs remain distinct. A failure can complete
a task within its stated scope; it cannot authorize a larger campaign.

One current writer owns this file. Reread the live entries before editing
and preserve other chats' results. New task IDs or reclassifications need
a dated reason; retain earlier identities and evidence. Parent and sibling
register updates require coordinated ownership and are outside this
local plan. Use `notes/`, `numerics/` and `reviews/` for their respective
research outputs; create no draft snapshot folders. The [local history
guide](../chat-histories/README.md) preserves unique chat registrations.

## Continuation prompt

> Read plan r2, the sole register, Packet10 and the existing source/notes.
> Investigate **[B] RGD-B03 r2 — Astra**: state the overall implication
> chain and a noncircular quantitative H_r, attempt H_r => H_(r+1), and
> control complete error against a justified determinant margin as k
> increases, with r-dependence explicit. Cover small indices, the moving
> boundary transition and unbounded indices analytically. Return a worked
> step, exact unresolved estimate or scoped obstruction. Further low-order
> certificates are not prerequisites. Numerical checks may only test a
> predeclared discriminating hypothesis under a separate bounded E packet.
> Preserve all completed evidence, actual review levels and unique chat
> histories; freeze routine analytical follow-through for Sol when ready.

4 November 2026 preparatory revision: prepared for Edward Baker with
substantial LLM assistance, **gpt-6-astra / max**, chat0002, turn
01a1a798-eb9d-7293-ac50-736a92e31a8e. Sol's E04 r2 completed before this
integration; its accepted assessment and prior inputs were preserved.

[plan]: ../research-overview/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_OVERVIEW_20261104.md#research-plan--revision-r2-4-november-2026
[b01]: ../research-overview/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_OVERVIEW_20261104.md#rgd-b01
[e02]: ../research-overview/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_OVERVIEW_20261104.md#current-task-routing-under-r2
[e03]: ../research-overview/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_OVERVIEW_20261104.md#current-task-routing-under-r2
[e04]: ../research-overview/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_OVERVIEW_20261104.md#current-task-routing-under-r2
[b02]: ../research-overview/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_OVERVIEW_20261104.md#current-task-routing-under-r2
[b03]: ../research-overview/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_OVERVIEW_20261104.md#rgd-b03--induction-and-index-growth-r2
[workflow]: ../../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[n06]: ../../brainstorm/notes/06_RADIAL_GREEN_DETERMINANT_DERIVATION_20261104.md
[checker]: ../../brainstorm/numerics/radial_green_determinant_check.py
[record]: ../../brainstorm/numerics/RADIAL_GREEN_DETERMINANT_CHECK_20261104.json
[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

[note01]: ../notes/01_BOUNDARY_PRESERVING_FIRST_MODE_COMPARISON_20261104.md
[packet01]: handoffs/01_RGD_E04_R1_AND_E03_R1_BOUNDARY_PRESERVING_COMPARISON_20261104.md
[continuation02]: handoffs/02_RGD_CONTINUATION_AND_MODEL_CHANGE_20261104.md

4 November 2026 E04/E03 revision: prepared for Edward Baker with substantial
LLM assistance, **gpt-6.1-sol / ultra**, chat0003. E04 accepted; both E03
cases favorable floating. One coordinator owns this register; read-only
same-model contributing checks wrote no artifacts. No commits or parent/
sibling/global register changes were made by this return.

[review01]: ../reviews/01_RGD_E04_R1_BOUNDARY_PRESERVING_COMPARISON_ASSESSMENT_20261104.md
[note02]: ../notes/02_RGD_E03_R1_TWO_CASE_FIRST_MODE_DIAGNOSTIC_RETURN_20261104.md
[record03]: ../numerics/RGD_E03_R1_FIRSTMODE_DIAGNOSTIC_20261104.json
[continuation03]: handoffs/03_RGD_CONTINUATION_AFTER_FAVORABLE_E03_AND_MODEL_CHANGE_20261104.md

[packet04]: handoffs/04_RGD_E02_R1_RIGOROUS_TWO_CASE_ACQUISITION_20261104.md

4 November 2026 E02 revision: prepared for Edward Baker with substantial
LLM assistance, **gpt-6.1-sol / ultra**, same chat0003. E02 r1 complete;
E04 r2 ready. Source inputs and earlier returns remain unchanged. No
commit, manuscript milestone or parent/sibling/global update was made.

[note03]: ../notes/03_RGD_E02_R1_RIGOROUS_TWO_CASE_BOUND_RETURN_20261104.md
[cert02]: ../numerics/RGD_E02_R1_TWO_CASE_CERTIFICATE_20261104.json
[self02]: ../reviews/02_RGD_E02_R1_CERTIFICATE_SELF_ASSESSMENT_20261104.md
[packet05]: handoffs/05_RGD_E04_R2_AND_MODEL_CHANGE_AFTER_E02_20261104.md

4 November 2026 E04 r2 revision: prepared for Edward Baker with substantial
LLM assistance, **gpt-6.1-sol / ultra**, same chat0003. E04 r2 accepted;
B03 preparation suggested in response to the author, not executed.
The full B03 gate is preserved. No parent/sibling/global changes or commit.

[review03]: ../reviews/03_RGD_E04_R2_TWO_CASE_CERTIFICATE_ASSESSMENT_20261104.md
[note04]: ../notes/04_ACCEPTED_PILOT_AND_PARALLEL_ASTRA_PREPARATION_20261104.md
[brief06]: handoffs/06_RGD_CONTINUATION_AND_ASTRA_B03_PREPARATION_20261104.md

[scope07]: handoffs/07_RGD_B03_PREPARATORY_SCOPE_20261104.md

[note05]: ../notes/05_RGD_B03_PREPARATORY_ORDER_DEPENDENCE_20261104.md
[packet08]: handoffs/08_RGD_E02_R2_EXISTING_DATA_NEXT_ORDER_AND_MODEL_CHANGE_20261104.md

4 November 2026 E02 r2 revision: prepared for Edward Baker with substantial
LLM assistance, actual **gpt-6.1-sol / ultra**, chat0003, turn
01a1a7ac-1448-7770-b86d-3264bc4b53e2. The user's request assigned this
bounded execution to this chat; the coordinator wrote only its new
outputs and local status/navigation. Earlier Astra and Sol artifacts,
parent/sibling/global indexes and source files were preserved. No commit.

[note06]: ../notes/06_RGD_E02_R2_FIRST_NEXT_ORDER_RETURN_20261104.md
[recordr2]: ../numerics/RGD_E02_R2_NEXT_ORDER_EXISTING_DATA_20261104.json
[review04]: ../reviews/04_RGD_E02_R2_ANALYTICAL_ASSESSMENT_AND_AUTHOR_CHECKS_20261104.md
[packet09]: handoffs/09_RGD_E04_R3_NEXT_ORDER_ASSESSMENT_AND_MODEL_CHANGE_20261104.md

4 November 2026 plan r2 revision: prepared for Edward Baker with
substantial LLM assistance, actual **gpt-6-astra / max**, chat0002, turn
01a1a7b4-0874-7401-9d01-11bf9930cad0. Sol's E02 r2 turn had completed;
this writer reread its final register before changing priorities. Source
notes, code, records, assessments and frozen handoffs were preserved.
The former B03 gate and E04 r3 default remain historical, not current
routing. No commit, manuscript milestone or mathematical execution.

[packet10]: handoffs/10_RGD_B03_R2_INDUCTION_INDEX_ERROR_AND_MODEL_CONTINUATION_20261104.md
