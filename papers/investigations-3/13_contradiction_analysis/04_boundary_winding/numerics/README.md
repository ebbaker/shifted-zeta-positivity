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

20 October 2026 — Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, actual effort ultra**. [Round-three starting source receipt](ROUND_THREE_SOURCE_VERSIONS_20261020.json) and [review/replay receipt](ROUND_THREE_REVIEW_RECORD_20261020.json) bind the fourth-order and actual-profile work. Detailed acquisitions remain in their canonical Project 11, threshold-sign and BW-08 numerics folders.

20 October 2026 — Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra (Codex), actual reasoning effort max**.
[Profile witness topology diagnostic](PROFILE_WITNESS_TOPOLOGICAL_SCREEN_20261020.json)
and its [exact checker](check_profile_witness_topology.py) support the
[boundary-information brainstorm](../brainstorm/03_TOPOLOGICAL_BOUNDARY_DATA_AND_PROFILE_WITNESSES_20261020.md).
The three slack residues are uniformly noninteger. The checker performs
201 rational checks, including the boundary-harmonic and discriminant
factors, and binds a fresh 88-domain inherited wall-flux replay. This is
a self-checked diagnosis of one relaxed witness, not a new theta
acquisition or an exclusion of every integer replacement.

Run from the repository root, keeping replay outputs outside the tree:

```sh
python3 -B papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_spacetime_wall_flux.py --output /tmp/bw_wall_flux.json
python3 -B papers/investigations-3/13_contradiction_analysis/04_boundary_winding/numerics/check_profile_witness_topology.py --repo-root . --wall-replay /tmp/bw_wall_flux.json --output /tmp/bw_profile_topology.json
```

The inherited replay embeds its original 15 October header; the new
record separately identifies this 20 October replay and its actual model
and effort. Mathematical values and source hashes, rather than the fresh
capture timestamp, are the replay comparison.

20 October 2026 — Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra (Codex), actual reasoning effort max**.
[Direct-winding relative-phase checks](DIRECT_WINDING_RELATIVE_PHASE_20261020.json)
and their [exact checker](check_direct_winding_relative_phase.py) support
[Note 03](../notes/03_DIRECT_PHYSICAL_WINDING_RELATIVE_PHASE_AND_WALLS_20261020.md).
The finite heat-polynomial controls retain both wall transports; a pair
of ordinary double events has positive paired-face dot product and
winding −2. The record also checks the local error constants, sixteen
positive-atom kernel identities and the existing GEO-T1 boundary receipt.
These are author self-checks, with no new theta quadrature or coverage.

```sh
python3 -B papers/investigations-3/13_contradiction_analysis/04_boundary_winding/numerics/check_direct_winding_relative_phase.py --repo-root . --output /tmp/bw_direct_relative_phase.json
```
