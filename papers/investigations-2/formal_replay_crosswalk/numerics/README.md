# Formal replay records and scripts

Initialized 12 October 2026; updated 13 October 2026. Prepared for Edward
Baker with substantial LLM assistance. Model: GPT-6 (Codex), inherited
session configuration; exact serving variant and reasoning effort are not
exposed and are not inferred.

Linux operational setup is complete. The first guarded zeta attempt is
running from `rh-replay.pre-math-replay-20261013`; no mathematical target
outcome is available yet. Dirichlet and Hecke have not run.

- [Replay guide](REPLAY_GUIDE.md): exact pins, tested Linux setup, direct Lean tool paths, guarded invocation and baseline restoration protocol.
- [Linux environment record](linux_vm_environment_20261013.json) and [note](../notes/4_LINUX_REPLAY_ENVIRONMENT_20261013.md): VM/baseline identity and bindings to the preparation records.
- [Linux tool build](linux_tool_build_20261013.json), [dependency preparation](linux_dependencies_20261013.json), [isolation controls](linux_isolation_20261013.json), [trusted Mathlib cache](trusted_mathlib_cache_20261013.json), and [comparator integration](comparator_smoke_20261013.json): distinct evidence for the completed operational checkpoint.
- [Guarded target runner](run_guarded_comparator.py): requires a fresh mathematical baseline, checks inputs and tool hashes, and records target status and raw-log identities. A running record carries no acceptance result.
- [Tool bootstrap](bootstrap_linux_tools.py), [source materialization](prepare_math_sources.py), [dependency preparation](prepare_pinned_dependencies.py), [cache preparation](prepare_trusted_mathlib_cache.py), [isolation runner](check_linux_isolation.py), [integration runner](run_comparator_smoke.py), and [VM package configuration](cloud-init.yaml): reproducible preparation inputs; full execution logs remain external.

The historical 12 October source milestone consists of:

- [Source preflight script](check_replay_inputs.py) and [source inventory](source_inventory_20261012.json): read-only local source graph, deterministic evidence and external-manifest identity checks. Ten small controls passed; the script does not check proofs.
- [Native environment record](replay_environment_20261012.json): isolated Lean 4.34.1 and Mac auxiliary-tool builds, with target execution, kernel and axiom results unset at that date.
- [Statement contracts](formal_statement_contracts_20261012.json): written target signatures and Hecke bridge declaration/source identities.
- [Arithmetic declaration inventory](arithmetic_crosswalk_20261012.json): 26 source declarations and explicit unresolved applications.

Comparator acceptance concerns statement comparison, allowed-axiom
compliance and default-kernel replay. Its unchanged pinned implementation
does not emit the exact used-axiom set or accepted-export digest. Do not
substitute the permitted list for actual usage or treat a later export as
byte-identical to the accepted one.

Preserve completed attempt records, full raw logs and their hashes before
stopping or restoring the VM. The full source manifest and large logs are
external; see [ARCHIVES.md](../ARCHIVES.md), using normal
`numerics-archives/` lookup followed by `FORMAL_REPLAY_ARCHIVES`. Follow
[LARGE_FILES.md](../../../../LARGE_FILES.md) and [lane scope](../README.md).

The [queue launch checkpoint](replay_queue_launch_20261013.json) records the running one-off sequence and points to live state. [Queue guide](REPLAY_QUEUE_GUIDE.md), [runner](run_replay_queue.py), [34-control record](replay_queue_controls_20261013.json), [separate 20-control record](queue_scope_controls_20261013.json) and [scope review](../reviews/REPLAY_QUEUE_SCOPE_REVIEW_20261013.md) document preservation, fresh baselines and the strict timeout-only retry. Mutable progress is not final theorem evidence.
