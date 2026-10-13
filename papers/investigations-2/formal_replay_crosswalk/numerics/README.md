# Formal replay records and scripts

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and effort are not exposed.

- [Portable replay guide](REPLAY_GUIDE.md): environment requirements, exact pins and guarded target invocation.
- [Source preflight script](check_replay_inputs.py) and [source inventory](source_inventory_20261012.json): read-only local source graph, deterministic evidence and external-manifest identity checks. Ten small controls pass; no proof checking occurs in this script.
- [Environment record](replay_environment_20261012.json): isolated Lean 4.34.1 and native auxiliary-tool builds; actual target execution, kernel and axiom results remain null.
- [Statement contracts](formal_statement_contracts_20261012.json): exact written target signatures and Hecke bridge declaration/source identities.
- [Arithmetic declaration inventory](arithmetic_crosswalk_20261012.json): 26 source declarations and explicit unresolved applications.

The full source manifest and tool logs remain external. See
[ARCHIVES.md](../ARCHIVES.md), with normal `numerics-archives/` lookup then
`FORMAL_REPLAY_ARCHIVES`. Follow [LARGE_FILES.md](../../../../LARGE_FILES.md)
and [lane scope](../README.md). No mathematical replay has run.
