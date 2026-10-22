# Continuation prompt: establish the Investigations 4 research program

21 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **max**.

This prompt continues the [opening brainstorm][brainstorm]. It is an
instruction for the next organization task; saving it does not create the
program files or complete any mathematical task. Copy the text below into
a new research chat, or ask a continuing chat to carry it out.

## Prompt

Work in `/Users/ebbaker/Documents/shifted-zeta-positivity`. Establish the
research program for `papers/investigations-4/` from its opening brainstorm,
`brainstorm/01_COMPACT_GEOMETRY_HEAT_TRANSPORT_AND_WEIL_POSITIVITY_20261021.md`.
The purpose is a clear, shallow home for the network of ideas connecting
theta geometry, parallel transport, heat evolution, topological invariants,
compact surfaces and finite-interval Weil positivity.

Read the repository `AGENTS.md`, `LARGE_FILES.md`, `tools/CHAT_HISTORY.md`,
root README, `result-summaries/README.md` and `avoid/README.md` first. Then
read the opening brainstorm and follow its links to the authoritative
sources and current progress files needed to specify each direction.
In particular, consult the finite-time signed reconstruction program and
progress file in BW12, Notes 16–19 there, the BW13–15 continuations, the
Jensen-surface notes, and the finite-horizon Weil and CCM sources. Preserve
the sources' exact status and scope when summaries disagree.

Inspect the existing Investigations 4 tree before writing. Complete or
reconcile existing files rather than overwriting unrelated work or
creating a new dated copy of an already established program. Earlier
research remains at its original paths and should be linked, not moved
or copied into a second historical record.

Create the following:

1. A root `README.md` explaining the motivation, distinct objectives,
   common source, six directions, recommended first task and reading path.
2. A substantive shared overview in `research-overview/`, named
   `01_COMPACT_GEOMETRY_HEAT_TRANSPORT_AND_WEIL_POSITIVITY_PROGRAM_YYYYMMDD.md`.
3. A matching shared register in `research-progress/`, named
   `01_COMPACT_GEOMETRY_HEAT_TRANSPORT_AND_WEIL_POSITIVITY_PROGRESS_YYYYMMDD.md`.
   Use the actual local creation date for `YYYYMMDD`; reuse existing
   matching program files if this task has already begun.
4. These six project homes, each with a focused `README.md` and
   `notes/`, `numerics/` and `reviews/` folders:

   - `01_compact_weil_positivity/`: compact approximations and positive
     energies faithfully representing the complete arithmetic Weil form.
   - `02_theta_source_constraints/`: canonical theta coefficients, full
     reflection identities and coupled source estimates.
   - `03_heat_transport_and_charges/`: physical jet connections, transport
     under heat flow, event charges and all boundary fluxes.
   - `04_spectral_covers_and_periods/`: spectral double covers, transported
     cycles, marked monodromy and quantitative period observations.
   - `05_compact_jensen_surfaces/`: sequences of compact real curves,
     canonical coefficients, degeneration and real-component topology.
   - `06_signed_reconstruction/`: finite-time signed transport, complete
     head-tail response and comparisons with direct endpoint methods.

Keep the layout shallow. Use small placeholders only where needed to
retain empty folders; do not fill them with invented results or redundant
programs. The shared progress register is the primary task ledger. Each
project README should identify its object, inherited evidence, exact
missing estimate, first bounded task, dependencies, comparison method,
relevant controls and stopping condition.

In the overview, explain the connections between the six directions and
give a dependency map. Distinguish RH via positivity of the complete Weil
form for every finite support length, RH via the prescribed topology of
all canonical Jensen curves, and the stronger question of zero simplicity.
Keep physical theta heat separate from auxiliary polynomial heat, and
keep heat time, support length, source cutoff, spectral resolution, zeta
shift and curve degree distinct.

Start the task register with stable identifiers, exact deliverables,
prerequisites, source links, current status and next action. Separate
inherited results from new work. Mark only completed organizational work
as complete; unperformed mathematics remains unstarted, conditional or
gated as appropriate. Preserve the existing FTSR, BW13–15 and CCM statuses.

Use the brainstorm's priorities: first specify a compact positive energy
with a justified one-sided comparison to the **complete** Weil form for
each fixed test function; next examine joint theta-source constraints for
a signed response. Period and Jensen tasks need a distinct estimating
objective beyond an already known identity or the same endpoint data.
Do not activate every direction merely because its folder now exists.

Carry forward the controls and scoped obstructions. Compactness does not
automatically remove signed seam terms, topological capping obstructions,
degenerations or limiting errors. Conserved charge is not itself a signed
endpoint estimate. Finite strict Jensen hyperbolicity does not establish
simplicity of a limiting entire function. Compare methods using the same
information and complete error budgets. Link the relevant result-summary
clusters and specific avoid-pattern files, particularly collision controls,
restating the target, geometric re-realizations, coupled estimates,
identification of the full target and scoped exclusions.

Follow the research chat-history workflow using this chat's actual
identity. Preserve any existing registration; do not re-register or
renumber the founding archive. Include the date, Edward Baker, LLM
assistance and the actual recorded model and effort in new documents.
Record the organizational milestone concisely in `DRAFT_HISTORY.md`, with
links to the new overview and progress register; create no manuscript
snapshots.

Validate local links, agreement between task IDs and statuses, and file
sizes. Finish by reporting the files created, the recommended first
bounded research task and any unresolved factual dependencies. Complete
the documentation and folder setup without routine confirmation. Do not
begin a new proof attempt or numerical campaign in this organization task.

## Source and workflow pointers

The [result summaries][results] and [avoid index][avoid] remain entry
points, with the source files authoritative. Particularly relevant are
[finite-horizon certificates][finite], [collision controls][controls],
[heat-flow geometry and equivalent criteria][geometry],
[restating the target][a01], [geometric re-realizations][a03],
[scoped exclusions][a07], [coupled estimates][a12] and
[identification of the full target][a13]. The opening brainstorm links the
specific investigations and manuscripts.

[brainstorm]: 01_COMPACT_GEOMETRY_HEAT_TRANSPORT_AND_WEIL_POSITIVITY_20261021.md
[results]: ../../../result-summaries/README.md
[avoid]: ../../../avoid/README.md
[finite]: ../../../result-summaries/02_finite_horizon_certificates.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[a01]: ../../../avoid/01_restating_the_target.md
[a03]: ../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a13]: ../../../avoid/13_a_factor_is_not_the_target.md
