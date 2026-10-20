# Boundary winding numerics

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model: **gpt-6-astra (Codex)**;
actual reasoning effort: **xhigh**, verified from the recorded turn metadata.

Reproducible computations and small execution records.

The [19 October control replay](THRESHOLD_CONTROL_REPLAY_20261019.json) records a fresh run of the inherited exact polynomial checker: degrees 2 through 16, 60 rectangle cases, and 1573 passing assertions. It checks existing winding controls and supplies no theta certificate or new arithmetic estimate. The record identifies the question, falsifying outcome, source, command, and actual execution configuration.

BW-01 now has its own [paired-face exact controls](../threshold_routes/01_local_double_winding/numerics/PAIRED_FACE_CONTROLS_20261019.json), with the contract and checker in that route. These are finite polynomial controls, not theta quadrature. Execution update, 19 October 2026: prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.

Before running a new diagnostic, specify the mathematical question, domain, source versions, comparator, and falsifying outcome. Keep scripts and small records here; follow the [large-file policy][large] for derived data. Label floating diagnostics separately from interval certificates and record every error and control contract.

[Parent index](../README.md).

[large]: ../../../../../LARGE_FILES.md
