# Cross-family review of the first formal-replay and crosswalk milestone

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the
serving model may differ), Anthropic, Cowork session; reasoning effort
max. This is step B5 of the parallel plan: the review from the other
model family that the lane README asks for. It is an internal model
review, not independent mathematical validation, and it does not replay
any Lean proof.

**Reviewed.** The lane's first milestone at commit `3c59f9a`:

- notes 1–3;
- the statement-contract and arithmetic-crosswalk records;
- the replay guide;
- Codex's own scope review.

**Not reviewed.** The source-inventory consumer `check_replay_inputs.py`
was not rerun. The lane's indexes are left to their owner.

## 1. Verdict

The milestone's factual claims hold.

- Every statement, declaration name and hypothesis I checked against the
  pinned source reads as the notes say. Line numbers drift by at most a
  few lines in a handful of places (§5).
- The evidence boundary is drawn correctly. No note claims a compiled
  proof, an axiom report or a comparator outcome.

I would change five things:

1. Gap U3 is overstated. The cited endpoint, instantiated differently,
   gives the October 5 extraction directly (§3.1).
2. The ledger omits two terminal steps of the October 5 argument: the
   Mellin deduction and the base change (§3.3).
3. Note 3 does not record that the zeta and Dirichlet solutions are
   proved *through* the Hecke norm-lift. This matters for the semantic
   bridge (§2.2).
4. Note 3 §5 calls `dirichlet_seven_eighths_of_hecke` and
   `zeta_seven_eighths_of_hecke` contracts. They are implications from a
   Hecke nonvanishing hypothesis, and the note should say so.
5. Note 2 describes the formalization scope `lean/docs/003.md`
   incompletely (§3.4).

None of these changes a status from "checked" to "failed".

## 2. Formal statements and the Hecke bridge (note 3)

### 2.1 Checked as stated [source]

The checks were made in a sparse checkout of `openai/math` whose HEAD was
verified as `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. `DL` below means
`lean/OAI/NumberTheory/DirichletL`.

**Records.**

- All 39 source hashes, byte counts and line counts in
  `formal_statement_contracts_20261012.json` match the checkout (scripted).
- All 26 constants in `arithmetic_crosswalk_20261012.json` exist at their
  declared lines under their stated fully qualified names (scripted).

**Comparator targets.**

- Challenge statements:
  - zeta: `QuasiRiemannHypothesis.lean:5–6`;
  - Dirichlet: `DirichletSevenEighths.lean:8–11`;
  - Hecke: `HeckeSevenEighths.lean:237–239`.
- Each JSON configuration nominates one theorem, sets
  `definition_names: []`, permits `propext`, `Quot.sound` and
  `Classical.choice`, sets `enable_nanoda: false`, and names the solution
  module as quoted.
- The solution signatures in `DL/Nonvanishing.lean:19–22, 29–30` and
  `DL/Hecke/Nonvanishing.lean:13–15` are identical to the challenges.
- Beyond the note's own check, every definition the Hecke challenge
  repeats matches the solution source text after whitespace
  normalization, in the same namespaces. This covers the theta pairs,
  `latticeL`, `K`, `O`, `omega`, `coordinateElement`, `Character`, the
  coefficients, `continuedLattice` and `LFunction`.

**The `Character` structure.**

- The fields are in `DL/Hecke/Family.lean:22–29`.
- `ofResidue` (`:31–44`) sets the period to `Fintype.card (O ⧸ M)` for
  any nonzero `M`, so the period field imposes no restriction.
- `three_pid` is installed in `RayFamily.lean:13` and
  `IdealBridge.lean:12`.
- `principal_iff` is at `RayFamily.lean:21–24`.
- The ray corollary is at `Hecke/Nonvanishing.lean:35–38`.

**The one-sixth chain.**

- In `IdealBridge.lean`: `LFunction := continuedLattice χ s / 6`
  (`:95`); `continuedLattice_eq_six_ideal_tsum` and
  `LFunction_eq_ideal_tsum` for `1 < Re s` (`:80–81`, `:97–98`); and
  `elementTerm_zero` for `s ≠ 0` (`:62–64`).
- `card_units_eq_six` is at `Reciprocity/RamifiedSymbol.lean:424`.

**Primitive presentation.**

- `exists_primitive_character` is at `Hecke/IdealOperations.lean:16–22`.
- Lean's ideal order `≤` is inclusion, so `ψ.modulus` is the larger ideal
  and divides `χ.modulus`. The note reads the direction correctly.
- `factors_ne_zero` requires `0 < Re s` (`Hecke/FiniteDeletion.lean:32`).

### 2.2 An addition that strengthens the semantic bridge [source]

The nominated zeta solution `zeta_nonzero` ends in the Hecke family. The
chain runs:

1. `zeta_nonzero` (`Detector/FinalAssemblyUnconditional.lean:43`);
2. `zeta_of_certified` (`FinalAssemblyCertifiedBands.lean:156`);
3. `zeta_of_chosen_moments` (`FinalAssemblyChosenData.lean:84`);
4. `HeckeCommonProbe.zeta_of_common_probe` (`Hecke/CommonProbe.lean:63`);
5. `HeckeDirichlet.zeta_seven_eighths_of_hecke` (`Hecke/Dirichlet.lean:171`),
   applied to `hecke_ne_zero_of_common_probe`.

The Dirichlet solution ends in `HeckeDirichlet.dirichlet_seven_eighths_of_hecke`
(`Hecke/Dirichlet.lean:158`) by the same route.

So both Mathlib-stated targets are proved from nonvanishing of the
bespoke Hecke `LFunction`, by way of the proved base-change product
identity `LFunction_eq_dirichlet_product`. A successful zeta or Dirichlet
comparator run would therefore also certify one thing about the bespoke
definition: on norm-lifted characters it agrees with Mathlib's `L`-series
products. That is a machine-checked partial validation of the
definition. It does not replace the note's reading for general ray
characters, but it is evidence the note should list.

### 2.3 Smaller points

- **Hypothesis of the base-change theorems.** Note 3 §5 should state that
  `dirichlet_seven_eighths_of_hecke` and `zeta_seven_eighths_of_hecke`
  take a Hecke nonvanishing hypothesis `hH`.
- **The conductor-minimality caution.** It is right at the Lean level,
  since no minimality lemma is stated. Mathematically it is
  over-conservative: primitivity together with the exact mask already
  makes `ψ.modulus` the conductor.
- **The Milne reference.** The ray-class identification cites Milne,
  *Class Field Theory*, Chapter V, Theorem 1.7, while the September 30
  source cites Chapter VI §1 (`paper.tex:57`). I did not check which is
  intended.

## 3. The arithmetic crosswalk (note 2)

### 3.1 U3 is a short corollary, not a missing mechanism [source; checked]

Note 2 T2 says that the Lean endpoint `no_slot_endpoint` is stated for
`D = U^r` with bounded `r` and only for large `U`, so setting `U = 1`
does not give arbitrary large `D`. That reading is literally correct
(`Hecke/InverseAmplificationEndpoint.lean:11–27`). The conclusion drawn
from it, that a new mechanism or a different declaration is needed, is
too strong.

The theorem requires only `absNorm(span{u}) ≤ U` for each row, not
`≍ U`. The unit is a `FreeRow`, since `SixthFree ⊤` holds
(`InverseAmplificationRows.lean:10, 38`). The direct route is then:

1. **Instantiate.** Take `rows = {1}`, a fixed `r = R ≥ 1` and
   `U = D^{1/R}`.
2. **The bound.** Since `sourceExponent R = (1 + 5R)/6`
   (`InverseAmplificationBudget.lean:10`), the endpoint gives, for all
   large `D`,
   `|D^{−1/2} A_1(D)|² ≤ C K D^{5/6 + (1 + 6ε)/(6R)}`.
   That is, `|A_1(D)| ≪_R D^{11/12 + (1 + 6ε)/(12R)}` **[checked]**.
3. **The limit.** Letting `R → ∞` gives the October 5 saving
   (`paper2.tex:722–723`), with a loss `η > 0` as small as wanted.

The two raw-moment hypotheses come from `raw_reference_moment` at
`t = 0`, applied to `W` and to `scaleProfile W`, for the `c` and `κ`
the endpoint chooses.

What remains is U1: constructing the October 5 data `ν` and `S` as a
`RowData`. U3 should be downgraded to a routine instantiation that
depends on U1. Only the intermediate bound indexed by `c` is not
exposed, and the October 5 terminal step does not use it.

### 3.2 U2 is a fidelity item, not on the terminal path [source]

U2 asks for an ordinary-seminorm conversion so that `k` is chosen before
the interval and `W`, as in `thm:ms`. That is right for reproducing the
proposition as stated. The October 5 extraction and the Mellin step,
however, use one fixed `W` (`paper2.tex:694–730`). So U2 is not needed
for the zero-free conclusion. The ledger should say this, so that U2 is
not read as blocking the terminal crosswalk.

### 3.3 Two terminal steps missing from the ledger [source]

1. **The Mellin deduction.** `paper2.tex:726–757` turns the saving for
   `A_1` into nonvanishing of `L_K^S`. Its Lean counterpart needs the
   identification of `L_K^S` with `HeckeFamily.LFunction` times the
   finite factors. The `FiniteDeletion` mask theorems in note 3 §4
   supply exactly this, but the crosswalk does not link it.
2. **The base change.** The final step to Dirichlet `L`-functions
   (`paper2.tex:759–771`) corresponds to
   `HeckeDirichlet.LFunction_eq_dirichlet_product` (`Hecke/Dirichlet.lean:128`).

Two further ledger rows, or a sentence under T2, would close the
terminal chain on the source side.

### 3.4 The formalization scope [source]

`lean/docs/003.md` names two papers: the September 30 paper and the
October 1 paper on uniform exclusion of Landau–Siegel zeros. It lists
four comparator challenges, the fourth being `SiegelZeros.lean`. Note 2
says only that the scope "names the September 30 paper". The material
point stands: the October 5 argument is not named.

### 3.5 What the crosswalk can and cannot deliver [judgement]

The October 5 theorem, `Re s > 11/12`, follows from the Hecke 7/8
target once that is replayed (`paper2.tex:81` calls October 5 an
intermediate step). The crosswalk therefore certifies the October 5
proof route, not its conclusion. The lane README says this, and that
priority is right: the route is what the small-cofactor branch needs.

The checked specializations are the following:

| Link | Check | Result |
| --- | --- | --- |
| T1 | `H = D^{1+θ}`, `c = θ`, `ε' = ε/(2+θ)` | `D·H(HD)^{ε'} = D^{2+θ+ε}` **[checked]** |
| T1 | margins of `lem:marked` at `m = 1`, `z = 0` | `c/(1+c)` and `3 − 2/(1+c)` **[checked]** |
| T2 | the `U = 1` arithmetic | `(11 + 5c)/12` **[checked]** |
| C2 | `CanonicalMargins` (`Descent/Basic.lean:13–14`) | exactly `c ≤ F − M − Q − z ∧ c ≤ 4F − 3M − 6z` |

## 4. The replay environment (note 1)

The environment note is accurate and appropriately cautious.

- The Mac lane has no Linux runtime. The comparator's stated guarantees
  need a Linux host that meets its sandbox assumptions.
- The cloud container this Claude session runs in is Linux (Ubuntu
  24.04, x86-64, root, 2 cores, 7 GB).
  - It could at most run an unguarded `lake build` and `#print axioms`.
    That is weaker evidence than the comparator.
  - It cannot satisfy the comparator's unprivileged-user and `systemd`
    requirements.
- I have not run anything in this lane. Whether to use such a build as an
  interim, explicitly weaker record is Teddy's and the lane owner's
  decision.

## 5. Line drift and minor items

- **Line drift.** The links in note 3 sit a few lines from the
  declarations:
  - the ray nonvanishing corollary is at `Hecke/Nonvanishing.lean:35`;
    the note links L30;
  - `globalUnits` is at `RayOrthogonality.lean:92`; the note links L89.

  In note 2, `raw_reference_moment` begins at `:132`, not `:131`. Every
  other cited range contains its declaration.
- **Module counts.** The figures 2,926 and 2,929 are consistent. The
  2,926 are the `DirichletL` files, 2,929 adds the three challenge
  modules, and `DirichletL` imports no other `OAI` module.

## 6. Method and limits

**Done.**

- A sparse partial clone of `openai/math` at the pin, made in the cloud
  workspace and kept out of the repository.
- Scripted identity checks of both small records.
- Reading of every declaration and TeX range cited above.

A same-session Claude subagent did most of the line-by-line reading, and
I re-read the U3 argument (§3.1) and the zeta solution chain (§2.2)
myself. Both are same-family steps, which do not make this review
independent.

**Not done.**

- No Lean code was compiled.
- No comparator or `lake` command was run.
- The 252-import external frontier was not expanded.
- The October 5 completion and two-Poisson sections (U5–U7) were not
  compared beyond confirming that the cited ranges contain the cited
  statements.
