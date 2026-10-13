# Assessment of the amended research plan and parallel work layout

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration. Exact serving variant
and configured reasoning effort are not exposed and are not inferred.
Two parallel internal model assessments assisted this review; they are not
independent mathematical validation. This is a strategy assessment, not a
Lean replay, a completed supplier audit, or a new arithmetic or Newman bound.

## Recommended next work

I agree with the core of
[Claude's latest amended plan](REVIEW_OF_CODEX_RESPONSE_AND_PARALLEL_PLAN_CLAUDE_20261012.md),
especially its parallel assignment of formal replay and statement scope to
ChatGPT and Newman supplier checking to Claude. It supersedes the original
priority review's audit-order rationale and its proposal to drop producer
coverage. The best immediate outputs are a pinned formal replay and an
arithmetic contract crosswalk on one side, and a tail partition audit with
the uniform approximation-error map on the other. Each output should then
receive a review from the other model family.

| ChatGPT lane | Claude lane | Completion condition |
| --- | --- | --- |
| Check the replay environment; run the three pinned comparator targets; record statements, axioms, dependencies, patches, and outcomes | Audit the tail partition and the status of `OV`, together with the uniform `E_max` gates | Each checked assertion has a source, domain, and execution or argument record; operational failures remain distinguished from mathematical failures |
| Build the October 5 to September 30 to Lean crosswalk while replay infrastructure or compilation runs | Audit barrier derivative majorants and interpolation, including normalization, cutoff, nonvanishing denominator, and time endpoints | Every application is identical, a justified specialization, or explicitly unresolved |
| Write the amplification-parameter closure assessment; review Claude's first supplier report | Parse complete certificate coverage, then audit the amortized producer and its remainder bounds; review the arithmetic contracts | Sampled rows are not promoted to full coverage; further parameter tuning stays closed unless the estimate changes |
| Compare certificate methods before any substantial sharp-weight campaign | Consolidate the audited suppliers and remaining gaps | A proposed improvement has a complete transfer and tail contract plus a credible computation cost |

This is an order of deliverables, not a promise that a build or analytic
audit finishes in one session. The small-cofactor obligation statement can
be written now; substantial probes wait for the crosswalk and a named new
input that pays for the unit sector. The other exploratory projects remain
parked until their existing reopening conditions are met.

## Arithmetic agreement and qualifications

The source repository's
[pinned formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/003.md)
lists the seven-eighths conclusions for zeta, Dirichlet characters and
finite-order Hecke characters over the Eisenstein field. A replay is
therefore a more concrete next confidence check than another general prose
audit. The bespoke Hecke definition still requires a semantic bridge to
the intended family, including the unit quotient, ideal characters,
Euler factors, and normalization. A successful check of the conclusion
does not certify the October 5 proof route or every later application.

The two terminal correspondences identified by Claude are useful. In the
[September 30 source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`eq:raw-moment`, with `H = D^(1+theta)` and `c = theta`, yields the
[October 5 main moment](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex)
after undoing the `D^(-1/2)` normalization. The first assertion of
`lem:inverse-amplification`, at `U = 1`, yields the extraction exponent
`(11+5*theta)/12`, with the usual epsilon adjustment. These statement
specializations make the crosswalk worthwhile. They leave the completion
argument, admissible smooth profiles, sign, exclusions, deletion zeros,
uniformity and exact Lean constants to check. Membership in an import
closure alone cannot discharge an application contract.

Claude's stored record reports 2,925 identical source-module blobs at the
two upstream pins and identical challenge, manifest and toolchain files.
That supports planning one upstream replay after checking its full inputs.
It establishes source identity, not identical compiled proof objects or a
successful build. Liu's extension remains a separately labelled optional
verification target.

For the claimed comparator guarantee, use a Linux VM or a suitably
configured Linux host. A container qualifies only if its actual sandbox
and user-service configuration meet the
[comparator's requirements](https://github.com/leanprover/comparator#readme).
Working `landrun`, compatible `lean4export`, the prescribed `systemd-run`
guard, an unprivileged user, and a clean checking environment matter. Do
not first perform an unrestricted solution build in that environment and
then describe its comparator run as satisfying the clean-environment
condition. The macOS development substitution carries weaker isolation
assumptions. Pin the checking tools as well as the mathematical sources.

I also agree with withdrawing the earlier Dunn–Radziwill contradiction
argument. [Theorem 1.4](https://arxiv.org/html/2109.07463v3#S1.SS4)
concerns a squarefree cubic-symbol operator norm. In the square-row
comparison, `A = D^((1+theta)/2)` and `B = D` give lower-bound exponent
`1+theta/3` per unit coefficient energy, below the proposed `1+theta`
allowance. This comparison establishes neither a contradiction nor a
general sextic estimate. The actual special coefficient family must still
remain visible throughout the application.

Close the existing amplification parameter exercise while retaining its
unproved restricted mixed-moment target. The return ledger's
`H'/Sigma' = H/(Sigma F R)` explains why `F = R = 1` needs a new paid
saving. A changed parameter or a saving confined to nonunit descendants
does not supply that input.

## Newman agreement and qualifications

The amended order correctly distinguishes approximation allowances from
derivative and contraction slack. Recalculating the recorded numerical
inputs gives:

| Quantity | Value from the stored inputs | Consequence |
| --- | --- | --- |
| Tail contraction reserve `1-D` | `0.0002790906112505` | Check partition, overlaps, and uniform gates early |
| Reserve if `OV` is proved removable padding | `0.03952177182142735` | Its larger size is conditional on the partition argument |
| Binding row floor divided by `E_max` | `3.389224894969161` | Check the complete uniform error derivation alongside the tail |
| Binding prism joint derivative multiplier | `1.4969097175723887` | The earlier `416x` approximation ratio does not describe derivative tolerance |

Inputs are in
[Claude's small check record](../numerics/PRIORITY_RESPONSE_REVIEW_CHECKS_20261012.json).
These are sensitivity calculations with other suppliers held fixed, not
probabilities of error or proofs of the supplier inequalities. The tight
finite-floor cancellation also supports retaining producer correctness and
complete coverage checks. Parsing all shards is a useful first bounded
check; a full independent regeneration of every row need not be the next
task.

The certificate-method comparison should precede a large sharp-weight
campaign. Compare complete criteria, assumptions, domains, available
artifacts and replay cost. A smaller public numerical claim does not by
itself establish stronger verified evidence. A replayable sharp-weight
certificate can remain a useful goal, conditional on its tail and height
transfer closing at acceptable cost. Four floating samples establish no
such certificate.

## Separate ChatGPT work folder

Use a dedicated topic folder owned by the ChatGPT lane:

```text
papers/investigations-2/formal_replay_crosswalk/
  README.md
  notes/
  numerics/
  reviews/
  chat-histories/
```

This fits the existing investigation layout and separates new formal
verification work from the historical prose audit. The name describes the
scientific task; the README records ChatGPT ownership. Claude continues in
`newman_certificate_audit/`. Both lanes cite the existing arithmetic audit
rather than copying or moving its records. A later substantial method
comparison belongs in a separately scoped topic folder; a short comparison
can remain a new Newman review with a unique filename.

Separate folders prevent overlapping research-file edits. They do not
isolate a shared Git checkout's branch, index, or working tree. Use separate
clones or Git worktrees when both workers perform Git operations, and
integrate only each lane's owned paths. Allocate distinct filenames for
cross-reviews, write them in the reviewed project's `reviews/`, and leave
that project's indexes to its owner. One integration writer updates the
portfolio README, brainstorm indexes and base chat-history registry.
Project-specific chat histories have one recorder at a time.

Keep third-party clones, dependency caches and full build logs outside the
repository. Track small replay records, source hashes, parameters and a
replay guide, following [LARGE_FILES.md](../../../../LARGE_FILES.md). Add an
archive guide and lookup convention when the first large artifact exists.
Your instructions in this conversation explicitly specify
`DRAFT_HISTOR.md`; use that spelling for future manuscript milestones.
No manuscript snapshot is needed for this assessment.

## Review scope

The four strategy files and brainstorm numerical record and checker were
read, together with the portfolio conventions and relevant audit context.
Primary source checks covered the formalization scope, comparator
requirements, the cubic operator-norm theorem, and the two terminal TeX
specializations. The displayed tolerance arithmetic was recalculated from
stored values. No Lean build, comparator execution, full closure refetch,
Newman supplier proof audit or full certificate regeneration was performed.
The new lane is initialized for the next research session; its verification
status remains unstarted.
