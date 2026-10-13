# Cross-family review of the completed replays and source passes 4–8

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the
serving model may differ), Anthropic, Claude Cowork; reasoning effort max.
This is the review the lane README asks for under its next bounded tasks 1
and 3: the completed replay records and the work added since the first
milestone. It is an internal model review, not independent mathematical
validation. No Lean code was built and no comparator was run.

**Reviewed**, at commit `d377347`:

- notes 4–8;
- the three replay records, the completion checkpoint and the launch record;
- the Linux preparation records and scripts, read but not executed;
- `REPLAY_GUIDE.md`, `REPLAY_QUEUE_GUIDE.md`, `ARCHIVES.md` and the READMEs;
- the six same-family scope reviews of 13 October;
- the lane's chat registry.

Notes 1–3 were covered by the
[first cross-family review](CROSS_FAMILY_REVIEW_OF_FIRST_MILESTONE_CLAUDE_20261013.md).
Section 5 records the status of its points.

**Companion check program.** It is
[`…_checks.py`](CROSS_FAMILY_REVIEW_OF_REPLAYS_AND_SOURCE_PASSES_CLAUDE_20261013_checks.py),
with record
[`…_checks.json`](CROSS_FAMILY_REVIEW_OF_REPLAYS_AND_SOURCE_PASSES_CLAUDE_20261013_checks.json).
It is standard-library Python with deterministic output. It sits beside this
review because the lane's `numerics/` folder belongs to its owner, who may
move it.

Labels:

- **[read]**: a lane file read in full.
- **[source]**: a pinned upstream file read directly. The pins are openai/math
  `fd4aeeb2…`, comparator `d03acab1…` and lean4export `076e8e57…`. Each was
  fetched in the cloud workspace and its commit verified.
- **[checked]**: recomputed by the companion program, or re-derived by hand
  where stated.
- **[judgement]**: my assessment.

## 1. Verdict

The replays are sound and carefully recorded. Notes 5–8 are correct as
conditional paper-level derivations. I found no mathematical error and no
error in the evidence bindings.

Under the recorded trust assumptions, the three acceptances establish the
following from `propext`, `Quot.sound` and `Classical.choice`:

- `riemannZeta s ≠ 0` for `Re s > 7/8`;
- Mathlib's Dirichlet `L`-functions are nonzero there, apart from the
  principal pole;
- the bespoke finite-order Hecke `L`-functions over `Q(√−3)` are nonzero there.

This is the strongest evidence the program now holds for the
quasi-RH strip. The lane's wording of it is accurate.

I would change six things.

1. **The cache-trust statement can be made sharper.** The kernel replay
   re-checks every Mathlib proof the theorems use. What still depends on the
   cache is that its `.olean` files are well formed and that the definitions
   giving the statements their meaning match Mathlib source (§2.2).
2. **Several crosswalk contracts are proved inside the accepted replays.**
   Explicit invocation chains put `raw_reference_moment`,
   `rawMoment_reference`, `eventually_fixed_ray_amplification`,
   `canonical_marked_energy_exists`, `canonical_clipped_energy` and others on
   the proof path of the accepted Hecke target. The notes call them "read".
   They should be called replay-checked, after one Lean query confirms it
   (§3.6).
3. **Comparator assumption 1 covers the Lake configuration code, and no
   reading of that code is recorded.** Note 1 lists the requirement. The root
   lakefile runs git at configuration time, and ten dependency packages use
   executable `lakefile.lean` configurations (§2.3).
4. **U2 and U4 are not on the terminal path.** Note 6 lists U2 as a
   remaining input to the extraction. Fixed-weight raw moments come directly
   from two theorems on the replay path (§3.7).
5. **The first cross-family review has not been integrated.** Four of its
   five requested changes are open, and so is its point about U2. The lane
   README still says a Claude review is outstanding (§5).
6. **The next crosswalk pass should be U6, with U5, not compilation of
   U1–U4.** The 7/8 replay already implies the October 5 conclusion. U6 is
   the link the small-cofactor branch needs (§4).

Smaller housekeeping items are in §6.

## 2. The replays

### 2.1 Bindings re-verified [checked]

- **Pinned sources.** Each record's `configuration` equals the pinned JSON.
  The configuration, challenge and solution files match a fresh fetch at
  `fd4aeeb2` in bytes, SHA-256 and Git blob SHA-1.
- **Written contracts.** Each one occurs verbatim in its solution file, at
  lines 29 (zeta), 19 (Dirichlet) and 13 (Hecke).
- **Preparation context.** In each record, all ten context bindings match the
  committed lane files: by stored hash, and also by canonical hash for the
  JSON files.
- **Completion checkpoint.** Its bindings of the three records match.
- **Durations.** 4,715.6 s, 4,258.7 s and 3,518.7 s, with 3 h 30 min 49 s of
  total wall time, as stated.
- **Module counts.** The guest counted 2,924, 2,924 and 2,925 compiled OAI
  `.olean` files after each run (`run_replay_queue.py`, line 89). These
  counts equal the per-target closure sizes predicted by note 1's static
  inventory.
- **Guard.** The command is the comparator README's `systemd-run`
  invocation, plus a unit name, a runtime bound and `ELAN_TOOLCHAIN`. The
  README says the Landrun weakness that this AF_UNIX guard covers will be
  fixed in Linux 7.1. The VM kernel is 7.0.0, so the guard was needed, and it
  was used.

### 2.2 What an acceptance establishes for this comparator [source]

The pinned comparator does five things. `"Your solution is okay!"` is
printed only after all five succeed.

1. It builds the challenge and solution modules inside Landrun.
2. It exports each module with `lean4export <module> -- <targets>`. The
   targets are the theorem names, the permitted axioms, the kernel primitives
   and the quotient builtins; the configured definition holes would be added,
   but here there are none. lean4export dumps each named constant after
   recursively dumping every constant in its type and value. The export is
   therefore the full dependency closure of the nominated theorem.
3. It compares the theorem types. It then compares every constant used in
   the statement, recursively, by equality of the whole constant record,
   which includes definition bodies. With `definition_names: []`, the
   bespoke Hecke definitions are therefore term-identical in challenge and
   solution. This covers `Character`, the theta pairs and `LFunction`.
4. It checks every axiom reachable from the theorem's type and proof against
   the permitted list.
5. It replays the solution's whole exported closure into a fresh Lean kernel
   environment.

Four consequences follow.

**The cache trust can be stated more sharply.** The records trust "cache
artifact contents … to match their source inputs". The kernel replay
re-checks every Mathlib declaration in the theorem's closure, so a cached
proof on the path that is wrong but well formed would be rejected. Two
things remain trusted.

- **Well-formed files.** Lake and lean4export load the cached `.olean`
  files, and the comparator README treats loading `.olean` files as an
  attack surface.
- **Faithful definitions.** The replay cannot detect a cached definition
  that differs from Mathlib source, because challenge and solution read the
  same cache. The comparator README gives exactly this as its example of
  cache tampering. The definitions concerned are those in each statement's
  cone: `riemannZeta`, `DirichletCharacter.LFunction` and what they unfold
  to, and for Hecke the Mathlib constants its bespoke definitions use
  (`CyclotomicField`, the Hurwitz functional-equation pairs, `WeakFEPair`).

That is a smaller and clearer assumption than trusting all cache contents,
and the records should state it.

**Declarations off the proof path are not covered.** Lake compiled
everything else in the 2,924 or 2,925 modules, but the comparator's axiom
check and replay never reach it. An off-path `sorry` would compile with only a warning.
This matters for the crosswalk (§3.6).

**One proof core, three statements.** Explicit invocations (chains J and J1)
take the zeta solution through the following steps:

- `zeta_nonzero`;
- `zeta_of_certified`;
- `zeta_of_chosen_moments`;
- `zeta_of_common_probe`;
- `zeta_seven_eighths_of_hecke`;
- `dirichlet_seven_eighths_of_hecke`;
- `LFunction_eq_dirichlet_product`.

The Dirichlet solution follows the parallel `dirichlet_…` steps to the same
`dirichlet_seven_eighths_of_hecke` (chain K). Both `zeta_of_certified` and
`dirichlet_of_certified` call the same `chosen_moments_of_certified` as the
Hecke target (chains J1 and K1). So the three acceptances check three
statements derived from one shared proof, which is to be expected. The
records should not read as three independent proofs.

**The Hecke semantic bridge is partly machine-checked now.** The accepted
Hecke path uses the following (chains H and I):

- `LFunction_eq_series`;
- `LFunction_eq_ideal_tsum`;
- `continuedLattice_eq_six_ideal_tsum`, the one-sixth chain of note 3;
- `exists_primitive_character`.

The accepted zeta and Dirichlet paths use the base-change identity
`LFunction_eq_dirichlet_product`.

`LFunction_eq_dirichlet_product` in turn invokes the analyticity lemma
`LFunction_differentiableAt` (chain J2).

Inside the accepted replays, the kernel has therefore checked three things.

- For `Re s > 1` the bespoke `L`-function equals the ideal Dirichlet series
  of the zero-extended residue character.
- It is differentiable away from `0` and `1`, so it is the analytic
  continuation of that series.
- On norm lifts it equals a product of Mathlib Dirichlet `L`-functions.

Its meaning is therefore fixed except for the class-field-theory step: that
unit-trivial residue characters exhaust the finite-order Hecke characters of
`Q(√−3)`. That step remains a reading.

### 2.3 Gaps in the recorded trust base [source, read]

**Lake configuration (assumption 1).** The comparator assumes a trustworthy
Lake configuration, and note 1 records that requirement. What is missing is
a reading of the configuration code. Lake runs the root and package
configurations, or loads a cached elaboration of them, for every build,
including the challenge build. The root `lean/lakefile.lean` has two pieces
of code that run git through `IO.Process`:

- a configuration-time `run_cmd`;
- a `post_update` hook.

The `run_cmd` checks the pinned commit, origin and patch state of 11
packages. It clones any of them that is absent and patches any that is
unpatched. The hook re-checks those 11, then checks and applies the patches
for 12 more. I read the root configuration, and it does nothing else.

Ten of the 42 packages also use executable `lakefile.lean` configurations:
LeanArchitect, MD4Lean, UnicodeBasic, Zeta3Irrational, checkdecls,
leansqlite, mathlib, proofwidgets, doc-gen4 and rellich-kondrachov. I did not
read those. The dependency record's `rellich_configuration_audit` concerns
which libraries are declared, not configuration code. Record a reading of
the ten package files and the root, or record them as trusted.

**Unguarded configuration run.** `prepare_trusted_mathlib_cache.py` runs
`lake exe cache get` at the project root, outside the guard, so the root
configuration code ran unguarded at least once. Its cached elaboration may
then have been reused by the guarded builds. That is consistent with
assumption 1, once the configuration is recorded as trusted.

**Fresh environment (assumption 2).** The guarded runner checks only that
the OAI and challenge build trees are absent. The dependency record shows
that no build directory existed for any of the 42 packages at 03:47 UTC, so
before the cache step. That was not re-checked when the baseline was saved.
Add it to the next baseline check.

**Optional strengthening.** `enable_nanoda` is false, so the Lean kernel is
the only checker. A supplementary run with an external kernel would remove
the single-kernel assumption. It changes the configuration, so it must be
labelled supplementary. An exact axiom list can come from a separate,
non-adversarial `#print axioms` session. By step 4 above it is a subset of
the three permitted axioms.

**Evidence copies.** Outside the VM, the preserved raw attempt evidence
exists in one place, the local archive under `/Users/Shared/szp-archive`.
Its three comparator logs total about 9.9 MB. The outcome can be
regenerated, but these exact logs cannot. Keep a second copy before any
manuscript cites them.

## 3. Source passes 5–8

### 3.1 Identity and citation checks [checked]

- **Hash tables.** All 7 hashes in note 5's table and all 19 in note 7's
  match a fresh fetch.
- **Source-contract record.** The canonical-energy record's 38 files match in
  bytes, SHA-256 and blob SHA-1. Its 43 anchor excerpts match by SHA-256.
  The two TeX sources and its binding of note 8 match in bytes and SHA-256.
- **Line ranges.** Notes 5–8 link 86 pinned Lean line ranges. Of these, 34
  are attached to a back-ticked declaration name on the same line, and every
  one of the 34 contains that declaration.
- **Bare locators.** I checked note 6's bare `File:line` locators by hand.
  They are accurate, except that `prime_column_energy` is declared at
  `InverseAmplificationEnergy.lean:11`. The cited lines 18–29 are its
  coefficient bound inside the proof.

### 3.2 Note 5 (U2) [checked by hand; source]

- **Lean statements.**
  - `raw_reference_moment` gives `∃J ∀data ∃C>0 ∀t`, with growth
    `C(1+|t|)^{2J}`.
  - `rawMoment_reference` transfers this with the same `J` and the constant
    `C·B_J(W)²`, under Mathlib's `2π` Fourier convention.
  - `inverse_polynomial_bound` and `nonzero_element_rows_card` are as quoted.
  - `positive_cutoff(1/2, 2)` is one on `[1/2, 2]` with support in `[1/4, 3]`.
- **Derivations redone.**
  - the bound on `B_J` with `m = J+2`;
  - the Stirling-number chain rule;
  - the partition, which works because the dilates of `[3/4, 3/2]` tile
    `(0, ∞)`, so the sum `Q` is positive;
  - the `√λ_j` scale identity from central normalization;
  - the threshold `D_0` with `c_0 = c/2`;
  - the finite Cauchy–Schwarz constant;
  - the bounded-scale bound `128³·max(1,b)²·M_k(W)²·H·D`;
  - the quantifier order: `k = J+2` is fixed before `I`, the data and `W`.
- **No defect.**

### 3.3 Note 6 (U3) [checked; source]

- **Statements as quoted.**
  - `eventually_fixed_ray_amplification`: there is `c>0` such that the
    following holds eventually in `x`. Take any data, any finite set of
    sixth-power-free rows of norm at most `U`, any smooth `W` supported in
    `[wa, wb]` with `wa > 0`, and any `D > 0` and `E`. If the raw scale
    energies of `W` and `scaleProfile W` are bounded by `E`, then the sum
    over the rows of `‖polynomial‖²` is at most
    `4(1+2 log(xb))·E·log x/(cx)`.
  - `RawMoment.scaleEnergy` matches its quoted form.
- **Substitution.** Take `U = 1`, `q = (1+c)/6`, `V = D^q` and `x = V/b`.
  Then `N = D^{1+c}` and `E = C·D^{1+c+κ(2+c)}`, and the boxed bound
  follows. The exponents `5(1+c)/6 + κ(2+c)` and
  `11/12 + 5c/12 + κ(2+c)/2 + η/2` and the `ε/3` budget were checked in
  exact arithmetic.
- **Scale profile.** The derivative formula for `scaleProfile` is right.
- **Relation to the first Claude review.** Note 6 was committed in
  `2bf3fe3` at 01:30, before that review was committed in `c50e4d9` at
  07:48, so it could not cite it. Its warning about `U = 1` restates note 2's
  own caution and is correct.
- **The review's alternative route.** That route used rows `{1}`, a fixed
  `R ≥ 1` and `U = D^{1/R}` in `no_slot_endpoint`, which needs only
  `N(u) ≤ U`. It is also valid, giving `11/12 + (1+6ε)/(12R)` without
  setting `U = 1` [checked]. Note 6's route is better, because it keeps
  `c = θ` and gives the O5 exponent `(11+5θ)/12` directly. The ledger can
  simply record both.

### 3.4 Note 7 (U1) [checked; source]

- **Statements.** The `RowData` fields, `RowData.character_spec` and
  `inverse_polynomial_original_row` are as quoted.
- **Sextic orientation.** The orientation matches exactly, not up to
  conjugation. O5 fixes `ω = e^{2πi/3}` (`paper2.tex:186`). In Lean,
  `omega3 = (−1+√3·i)/2 = e^{2πi/3}` (`Arithmetic/EisensteinEmbedding.lean:32`).
  `eisEmbedding` is built from `omega3` (`:153`), and `canonicalSextic` is
  `sexticChar` composed with `eisEmbedding` (`:461–463`).
- **Exclusion support.** `m = λ·2·∏ g_P` has prime support exactly `S` once
  `S` contains the primes above 2 and 3.
- **Conditional input.** The dictionary is conditional on presenting `ν` as a
  `HeckeFamily.Character` with its original zeros, as the note says.
- **No defect.**

### 3.5 Note 8 (U4) [checked; source]

- **Statements as quoted.**
  - the quantifier order of `CanonicalEnergyExists`;
  - `CanonicalRankMoments` and `CanonicalMargins`;
  - `normalizedColumnEnergy`, with a single `Z^{−F/2}` inside the square;
  - `secondLabelWeight K = (#divisors)^{9+4K}`;
  - `energy_range_weight_le`;
  - `canonical_clipped_energy`: at dilation 1 and shift 0 the clipped test
    is `W`;
  - the CRT law `columnCoefficient_union_row_four`.
- **Derivations redone.**
  - the factor four at the dyadic endpoint;
  - domination of unit label weights;
  - the margins after dilation, `F_0 − M ≥ κ + log_Z(2a_j) ≥ κ/2` and
    `4F_0 − 3M ≥ 2κ`;
  - the small-column bound `2·128⁴·max(1,hi)²·H·X`;
  - the bound for bounded `Z`.
- **The restoration step.** Note 8 cites O5's `lem:remove-exclusions`
  (`paper2.tex:962`) only to contrast the direction. Its own argument is
  that lemma's mechanism reversed. It uses the same CRT law `eq:crt-a`
  (line 851), the same injective label map `f ↦ δf` and the same invariance
  `X′F′ = XF`, without the Möbius inclusion–exclusion. Saying so in the note
  would make the step quicker to audit.
- **No defect.**

### 3.6 Contracts already checked inside the accepted replays [source; checked textually]

In each chain below, every declaration's proof invokes the next one
explicitly. The invocations take the forms `obtain`, `exact`, `apply`,
`rw`, `have`, `filter_upwards`, `simpa … using` and plain term
application. The companion program verifies every link, and I read each
one. In every one of these forms, a proof that compiles keeps the invoked
constant in its term. Each constant below is therefore in the closure that
the comparator checked for axioms and replayed in the kernel.

| Constant | Notes | Chain from an accepted target |
| --- | --- | --- |
| `raw_reference_moment` | 2, 5 | A: Hecke target → certified bands → … → `fixed_raw_profiles` (8 links) |
| `rawMoment_reference` | 2, 5 | B: `fixed_raw_profiles` → `raw_pair_height_uniform` → … (4 links) |
| `inverse_polynomial_bound` | 5 | F: `raw_reference_moment` → `rawMoment_of_large_rows_ge_one` → … (4 links) |
| `no_slot_endpoint`, `eventually_fixed_ray_amplification`, `averaged_energy` | 2, 6 | C: `chosen_moments_of_certified` → … → `no_slot_rowwise_endpoint` → … (11 links) |
| `RawMoment.scaleEnergy` | 5, 6 | C1: called twice in `no_slot_endpoint` |
| `RowData.character_spec` | 2, 7 | G: `source_moments` → … → `momentData_plain_pair_norm` (5 links) |
| `canonical_marked_energy_exists` | 2, 8 | D: `raw_reference_moment` → `raw_reference_large` → … → `retained_physical_bound` (8 links) |
| `canonical_clipped_energy` | 8 | E: `retained_physical_bound` → … → `canonical_clipped_uniform` (4 links) |
| `LFunction_eq_ideal_tsum`, `continuedLattice_eq_six_ideal_tsum` | 3 | H (8 links) |
| `exists_primitive_character` | 3 | I (4 links) |
| `LFunction_eq_dirichlet_product` | 3 | J and K, on the zeta and Dirichlet paths (7 and 6 links) |
| `LFunction_differentiableAt` | 3 | J2: invoked in `LFunction_eq_dirichlet_product` |

So notes 5–8 rest on Lean theorems that the accepted replays machine-checked,
not on theorems that were only read. Note 2's status
vocabulary should gain a third level, such as "replay-checked contract".

One Lean query in the VM would make this definitive. In a supplementary
session, not presented as the accepted export, collect the constants in the
closure of the accepted theorem and intersect them with the crosswalk's
constants. For any cited constant outside the closure, run `#print axioms`.

My chains do not cover the following, so I make no claim about them either
way: `positive_cutoff`, `uniform_fourier_one_plus_moment`,
`idealCoeff_eq_row`, `rowTwist_extract_sixth_mask`,
`inverse_polynomial_original_row`, `columnCoefficient_union_row_four`,
`finiteCanonicalMarkedRow_complete_global`, `energy_range_weight_le`,
`normalization_change` and `canonical_original_completed_energy`.

### 3.7 What the terminal chain needs, and what U2 and U4 are for [judgement; source]

**No new conclusion from compiling U1–U4.** The accepted 7/8 targets imply
the October 5 conclusion, `Re s > 11/12`, for the same families. Compiled
U1–U4 applications would add no new conclusion. Their value is the
dictionary between O5's mechanism and the formal library.

**The terminal chain itself needs only five things:**

- U1;
- U3;
- fixed-weight raw moments;
- the Mellin step;
- the base change.

O5's Mellin weight `y^{−ϱ}φ(y)` is one fixed smooth `W` supported in
`[wa, wb]`. For such a `W`, apply `raw_reference_moment` to
`positive_cutoff(wa, wb)`. Then `rawMoment_reference` gives `RawMoment` for
`W` and for `scaleProfile W`, which has the same support and is smooth. Each
comes with a constant `C·B_J(·)²` [source].

Note 6's remaining item 3, "discharge U2's uniform seminorm input", is
therefore not needed for the extraction. U2 is needed only to reproduce
`thm:ms` with its stated uniformity. The first review's §3.2 made the same
point.

**U4 serves research, not the conclusion.** U4 is an input to O5's own proof
of `thm:ms`, which U1–U3 bypass. Note 8 shows that O5's positive gap
`H ≤ ΣD^{−κ}` is exactly the formal `CanonicalMargins` at `Q = z = 0`, where
the second inequality is then automatic. It is used with margin `κ/2` to
absorb dilation and restoration. The formal theorem requires a strictly
positive margin. This locates the boundary the small-cofactor branch has to
cross. Note 8 should say so, since it is the most useful thing the U4 pass
can give the small-cofactor obligation statement (plan item A6).

## 4. Where the crosswalk should go next [judgement]

**Where the mechanism lives.** O5's mechanism is carried by U5–U7:

- U5: the all-row completed bound `prop:R`;
- U6: exclusion removal and the two-Poisson transfer, with its child ranges
  and termination;
- U7: the theta dictionary.

The small-cofactor branch needs U6 specifically.

**Candidate starting points for U6.** I found two formal counterparts to
start from [source; not analysed].

- The canonical rank induction, in `Descent/CanonicalRankExistenceInduction.lean`,
  with its caps in `CanonicalRankExistenceData.lean`. Its child step,
  `canonical_rank_moments_children` in `Descent/CanonicalRankMoments.lean`,
  requires `cutoff ≤ ell + V`. It passes to the children a margin of
  `c − 7η` and a row cap lowered by `3·cutoff/2`.
- The terminal estimate `canonical_original_completed_energy`, in
  `Reflection/OriginalCompletedEnergy.lean`. It saves `Z^{−cstar/32}`. It
  requires `CanonicalMargins` with margin at least `cstar/2`, and small label
  and completion heights: `V ≤ d ≤ cstar/200` and `hhat ≤ d + η`.

If O5's small cofactor shells correspond to this terminal regime, the formal
route covers them only under a positive margin. That would agree with the
return-ledger diagnosis `H′/Σ′ = H/(ΣFR)`. This is a hypothesis for the U6
pass, not a finding.

**The missing Mellin row.** Two candidates are worth checking.
`Hecke/DyadicMellin.lean`'s `polynomial_mellin` expresses the polynomial
through `mellin W` times the inverse series. `Mellin/CompactWeights.lean`'s
`weight ρ` and `weight_mellin_ne_zero` match O5's `W(y) = y^{−ϱ}φ(y)` and
its nonvanishing `Ŵ(ϱ) ≠ 0`. The `FiniteDeletion` masks supply `L^S`.

**Compiling U1–U4.** I would not compile the U1–U4 applications unless the
small-cofactor branch needs their Lean form.

## 5. Status of the first cross-family review [read]

| Point in the first review | Status at `d377347` |
| --- | --- |
| U3 overstated (§3.1) | Resolved by note 6, which was written in parallel and takes a different route. No response note. |
| Mellin deduction and base change missing from the ledger (§3.3) | Open. The base change is now replay-checked (chains J and K); Mellin candidates are in §4. |
| Zeta and Dirichlet proved through the Hecke norm lift (§2.2) | Open in the lane's notes. Verified in §2.2 above. |
| The `…_of_hecke` theorems are implications from a Hecke hypothesis (§2.3) | Open. |
| `lean/docs/003.md` names two papers and four challenges, including `SiegelZeros` (§3.4) | Open. |
| U2 not on the terminal path (§3.2) | Open. Note 6's remaining item 3 repeats the dependency. |

The lane README still says "a Claude review remains outstanding" and asks
for one under next task 3. At `d377347` the reviews folder held eight
reviews, and `reviews/README.md` lists two of them. It omits the first
Claude review and five same-family reviews, and now this one as well. Both
indexes are the owner's to update.

The same scope document lists a fourth challenge, `SiegelZeros.lean`, for a
uniform exclusion of Landau–Siegel zeros. The lane did not nominate it.
Like Liu's verifier, it is a separate optional target.

## 6. Housekeeping [read]

- **No outcome note.** No dated note records the replay outcomes; they live
  only in the README, `ARCHIVES.md` and the JSON records. A short note 9
  could cover the outcomes, the comparator semantics of §2.2, the trust base
  of §2.3 and the closure status of §3.6.
- **Stale replay guide.** The opening paragraph of `REPLAY_GUIDE.md` still
  says that zeta is running and that Dirichlet and Hecke have not run.
- **Model attribution.** The notes say "GPT-6 (Codex) … not exposed".
  The lane's only registered chat records model `gpt-6.1-sol`, reasoning
  effort `ultra`. By its README, that chat covers the lane's creation, the
  crosswalk through U4 and the replays. Use the recorded configuration from
  now on, or explain the difference once.
- **Portfolio integration.** This belongs to the single integration writer,
  not this lane. The investigations-2 README still describes the 7/8 theorem
  without the replay. The dated clarification proposed by the priority
  review is now due: it would revise the "assumption" and "independent
  validation outstanding" labels on the 7/8 conclusion.
- **Plan items.** Three other ChatGPT items from the amended plan have not
  started:
  - A3, closing the amplification lane;
  - A6, the small-cofactor obligation statement;
  - A4, the review of Claude's Newman supplier report.

  The README's next task 3 tracks only the last.

## 7. Method and limits

**Read.** Every file listed under "Reviewed" above, and the investigations-2
README. Also the brainstorm handoff stack, which consists of:

- the priority review;
- Codex's response;
- the Claude review of that response;
- Codex's strategy and layout review.

**Source.**

- The comparator's `README.md`, `Main.lean`, `Compare.lean` and `Axioms.lean`.
- lean4export's `Main.lean` and `Export.lean`.
- From openai/math, the lakefile, the three challenges and their JSON files,
  and every Lean declaration quoted above.
- O5 `paper2.tex`, lines 186, 236–261, 655–771, 790–822, 930–1000 and
  1255–1280.

**Checked.** The companion program and its record cover the following.

- record and source identities against a fresh fetch;
- the hash tables;
- the line ranges;
- the invocation chains;
- exact-rational checks of the exponent substitutions in notes 2, 5, 6 and 8,
  and of the first review's U3 route;
- string checks of the comparator and lean4export behaviour in §2.2.

All checks pass, and the output is byte-identical across two runs. To find
candidate chains, I first built a heuristic graph by textual name resolution
over the 2,926 `DirichletL` files. Every chain reported here was then
verified link by link, by the program and by reading.

A same-session Claude subagent then fact-checked the draft against the same
sources and re-extracted all 74 chain links on its own. I verified its
corrections and incorporated them. Those corrections were about precision;
it found no mathematical or binding error. Its check is also same-family.

**Not done.**

- No Lean build, Lean dependency query or `#print axioms`.
- The ten dependency `lakefile.lean` files were not read.
- U5–U7 were not compared.
- The Linux and queue scripts were read for what they assert and record,
  but not executed.
- Their offline controls were not rerun.
- Notes 1–3 were not re-reviewed beyond §5.

The reviewer is a model from the other family, which does not make this an
independent review.
