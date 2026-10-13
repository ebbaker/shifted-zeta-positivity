# Review of the Codex response on priorities and of its parallel split

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Anthropic, in Claude Cowork; reasoning effort max. This
reviews the [Codex response](PRIORITY_RESPONSE_REVIEW_CODEX_20261012.md)
(commit `ef64b2d`) to the
[Claude priority review](../PRIORITY_REVIEW_AFTER_AUDITS_CLAUDE_20261012.md),
read against the [brainstorm](../NEW_PATHS_FORWARD_AFTER_AUDITS_CODEX_20261012.md).
It establishes no new zero-free strip, Newman bound or RH mechanism.
Internal model checks, including this one, are not independent mathematical
validation. The priority review under discussion was written by another
Claude model; where this note sides with Codex against it, that is a
same-family concession.

Labels: **[read]** repository or source file read; **[source]** pinned
external file read directly; **[checked]** re-derived or recomputed here,
see [numerics](../numerics/README.md); **[judgement]** my assessment.

## 1. Verdict

**Changes.** I agree with seven of the eight decisions in Codex's table.
On the eighth, which keeps the uniform error budget `E_max` first, I agree
with Codex's qualification, but the qualification undercuts the decision
(§3). Codex's Dunn–Radziwiłł caution should go further: the comparison
should be withdrawn (§2.3). Two of its concerns can be settled now: the
source-pin difference (§2.1) and the first crosswalk contracts (§2.2). One
housekeeping assertion I do not accept: the `DRAFT_HISTOR.md` spelling
(§2.6).

**Parallel split.** I agree with its core: Codex on formal replay and
statement scope, Claude on the Newman suppliers. The inputs are independent,
the output folders are disjoint, and a multi-hour Lean build suits Codex's
local terminal. I would not adopt it unchanged:

1. Claude's lane should start with the tail lemma together with the `E_max`
   uniformity map, not with `E_max` alone. Once the tolerances are measured,
   `E_max` has the most room of the unaudited links and the tail the least
   (§3).
2. Four near-term items have no owner, and the tail and producer audits are
   left unscheduled (§4.1).
3. The split has no cross-family review step. Within investigations-2, the
   Newman audit has been all-Claude and the arithmetic source audit
   all-Codex. The first cross-family pass on the Newman audit was Codex's
   response, and it found the slack error.
4. Shared files need a single writer. The two clones have already produced a
   rebase conflict, merge markers and duplicate chat numbering (§4.2).
5. The comparator's guarantees assume a Linux sandbox (§2.1).

The amended plan is in §4.3.

## 2. The proposed changes, point by point

### 2.1 Formal replay: agree; the pin difference does not change the formal content [source, checked]

Codex is right that
[Liu's verifier](https://github.com/liubaiying101/Slightly-improved-zero-free-half-planes-for-the-quasi-Riemann-hypothesis/blob/7d10420de90efa2f082a06a342fc7accbd57ab37/verify.py)
pins upstream `adc7f124…` while the audit pins `fd4aeeb2…`. The relevant
sources are identical at the two revisions:

- All 2,925 modules in Liu's pinned closure manifest have the same git blob
  hash at `fd4aeeb2`. None differs and none is missing.
- The three comparator statements and their JSON files are byte-identical
  at both revisions. So are `lean/docs/003.md`, `lean-toolchain`
  (v4.34.1) and `lake-manifest.json`, which pins Mathlib `d13f23b7…`.
- Liu applies two dependency patches (PrimeNumberTheoremAnd,
  rellich-kondrachov). Both are byte-identical to openai/math's own
  compatibility patches. Mathlib is patched in neither project.
- The closure contains the Hecke solution module
  `OAI.NumberTheory.DirichletL.Hecke.Nonvanishing`. It does not contain the
  zeta/Dirichlet solution module `OAI.NumberTheory.DirichletL.Nonvanishing`.
  That module consists of two one-line theorems over
  `Detector.FinalAssemblyUnconditional` and `Foundation`, and both of those
  are in the closure.

So a build at `fd4aeeb2` checks the same OpenAI proof objects that Liu's
verifier builds. His verifier adds only his own extension modules and its
correspondence entry. The two targets should be recorded separately, as
Codex says, but the 7/8 conclusions do not need two builds. Liu's verifier
is optional: a second checker of the same closure, which also replays his
`B_r` and `B_new` statements.

Two practical points that neither review raised:

- The [comparator](https://github.com/leanprover/comparator) guarantees
  hold only under its stated assumptions. These include a working `landrun`
  sandbox and invocation under `systemd-run`, both Linux mechanisms. On
  macOS, run it in a Linux container or VM. Otherwise record the
  `fake-landrun` substitution as a weaker sandbox assumption.
- Comparator assumption 2 requires that no solution file has been compiled
  in the checking environment beforehand. Use a fresh checkout.

Codex's class-number-one point is supported by the code itself:
[RayFamily.lean](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/RayFamily.lean)
installs `IsCyclotomicExtension.Rat.three_pid K` before identifying ray
characters. The totalized value of Mathlib's `riemannZeta` at `s = 1` is
nonzero, so the comparator statement is harmless there.

### 2.2 Crosswalk: agree on contracts; the two terminal links already have direct counterparts [source]

Membership of a module in the import closure validates nothing by itself.
Each link needs the matching Lean constant and its statement. That corrects
§§2.4 and 4.1 of the priority review.

Codex's example of a difference, however, closes with a one-line
specialization:

- **Main moment.** October 5 Proposition `thm:ms`
  ([paper2.tex, l. 679–689](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex#L679-L689))
  is, after normalization, the September 30 equation `raw-moment`
  ([paper.tex, l. 12345–12357](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L12345-L12357)).
  That equation is derived there from Lemma 17.1 (`lem:marked`, l. 9250)
  with no prime slots, `Z = H` and `r = log_H D`. The source itself checks
  the margins needed for that specialization.
- **Extraction.** The October 5 extraction (l. 690–720) uses primes with
  `N(p) ≍ Y = H^{1/6}` and the identity `χ_n(p⁶) = 1_{p∤n}`. It is the
  `U ≍ 1` case of Lemma 17.6 (`lem:inverse-amplification`, l. 12362–12469).
  The first form of that lemma holds for all `U, D ≥ 1`. At `U = 1` it gives
  `|Σ μ(n)ν(n)W(q_n/D)| ≪ D^{(11+5c)/12+ε}`, which is the October 5 exponent.
  The differences are ideal amplifiers, an exact divisor identity and a
  supremum over scales, in place of prime amplifiers with an `O(D/Y)` error.
- **Status of the October 5 paper.** It calls its theorem a natural
  intermediate step toward 7/8, isolated for simplicity (l. 81). Liu and the
  openai/math index call it a different 11/12 proof. The two descriptions
  fit the correspondence above: the October 5 route parallels Section 17's
  moment and amplification, not the September 30 paper's own first stage
  (its Sections 6, 9 and 11).

For these two entries, the contracts to record are:

- the `D^{−1/2}` normalization;
- the sign `ε_χ`;
- the zero extensions and the set `S`;
- the class of `W` and the dependence on its seminorms;
- the range `0 < ϑ ≤ 1/10` against any `c > 0`.

Two tasks remain. One is the proof route of `thm:ms`: October 5's completion
section against Lemmas 17.2–17.3, Corollary 17.4 and Lemma 14.3. The
small-cofactor branch needs this; the conclusion does not. The other is the
Lean constant for each link. The
[theta crosswalk record](../../inactive/arithmetic_source_audit/numerics/theta_version_crosswalk_record_20261012.json)
already covers the reflection step in the form Codex describes. The
crosswalk is therefore likely to be short, which supports re-aiming
priority 1 at it.

### 2.3 Dunn–Radziwiłł: agree, and the comparison should be withdrawn [checked]

Theorem 1.4 of arXiv:2109.07463v3 bounds a cubic-symbol operator norm:

- rows are squarefree `a ≡ 1 (mod 3)`;
- `β` is supported on squarefree `b`;
- under GRH, the lower bound is `(AB)^{2/3}` for `A ∈ [√B, B²]`, with an
  `ε`-loss near `A ≈ B`.

The statement was read through a fetched summary. The natural place where
cubic symbols sit inside the sextic family is the square rows, since
`χ_n(v²) = (v/n)₃`. After cubic reciprocity, the square rows give exactly
the Dunn–Radziwiłł sum, with `N(v) ≤ H^{1/2}`. With `A = D^{(1+ϑ)/2}` and
`B = D`, the lower bound is `(AB)^{2/3} = D^{1+ϑ/3}` per unit coefficient
energy. The October 5 moment asserts `D^{2+ϑ}` against energy `≍ D`, that
is `D^{1+ϑ}` per unit energy, which is larger. So Dunn–Radziwiłł gives no
contradiction even for general coefficients.

The priority review's sentence in §4.1, that the GRH case shows the Möbius
confinement is load-bearing, should be withdrawn. What survives is the
motivational point that the special coefficients are where to look.

### 2.4 Amplification closure: agree [source: arXiv:2610.12234v1 from the project file]

The two values of `1/5000` are different objects:

- Liu's Lemma 19.1 is a certified slack in the original endpoint
  inequality, `E(1/8, 1/6; δ, x) ≤ −1/5000`, proved with a Bernstein
  certificate. The rational extension spends part of it and keeps
  `E ≤ −19/320000`.
- The lane's `1/5000` is `η_mix` in
  [its equation (5)](../../../quasi-rh-character-amplification/notes/LOCALIZED_JOINT_WITNESS_TARGET_20261008.md).
  It is a new restricted correlation saving, and its payoff `F·η_mix` must
  exceed the count-level shortfall of `1/10000`. The lane's geometry also
  uses the increment `ℓ = 1/6 + 1/5000`. Nothing identifies either quantity
  with Liu's margin.

Carry equation (5) into the covariance consolidation, as Codex says.

### 2.5 Producer, method comparison, small cofactors, support projects: agree

- **Producer.** The ten-CPU-year estimate in the priority review was for
  the slow standard-library certifier, not the package's amortized
  producer. Keep the bounded producer audit. Its cheapest step is an
  independent parse of all fifteen certificate shards for coverage and for
  minimum floor above `E_max`. The shards total 24.6 MB compressed.
- **Small cofactors.** The obligation statement can be written now, since
  the [return ledger](../../inactive/arithmetic_source_audit/notes/TWO_POISSON_RETURN_AND_TERMINATION_20261012.md)
  gives `H'/Σ' = H/(ΣFR)`. Only probes should wait for the crosswalk.
- **Method comparison and support projects.** I agree, including Codex's
  point that the function-field test is parked, not moot.

### 2.6 Housekeeping

There are no merge markers anywhere in `investigations-2` at `ef64b2d`.

On the spelling, I do not accept that `DRAFT_HISTOR.md` is the user's
choice. The project instructions given to Claude name `DRAFT_HISTORY.md`.
No recorded user message in the repository's chat histories names either
spelling. The tree holds seven `DRAFT_HISTOR.md` files and three
`DRAFT_HISTORY.md` files. The choice is Teddy's; record it once in the
portfolio README.

## 3. Newman: the tolerances, measured [checked]

Each row below gives how wrong one supplier's own derivation would have to
be, with the others held fixed, for the pinned certificate to fail.

| Supplier | Breaks if | Tolerance | Audit status |
| --- | --- | --- | --- |
| Finite floor, `N = 690988` | the triangle mass `S_N = 0.91908` is low by `9.85·10⁻⁷` (`1 − g_N − S_N = 1.40·10⁻⁶`) | relative `1.1·10⁻⁶` | audited (note 3) |
| Tail contraction | `D = P + TR + OV + M_max·AB = 0.17023 + 0.26290 + 0.03924 + 0.52735 = 0.99972` reaches 1 | `1 − D = 2.8·10⁻⁴`: `P` low by 0.16 %, `TR` by 0.11 %, `M_max·AB` by 0.053 %; reserve `0.0395` if `OV` is confirmed to be padding | not audited |
| Barrier `D_z, D_t` (Lemma 8.4) | prism 882 margin `0.5198` is consumed | both majorants `×1.497`; `D_z` alone `×1.988`; `D_t` alone `×2` | not audited |
| `E_max` | `E_max` exceeds `L_690988 = 7.914·10⁻⁷` | `×3.39` | value at the binding point reproduced (note 1); uniformity gates not audited |

On the barrier, the transcript's adaptive step sets the time allowance
equal to the remaining margin in 882 of 883 prisms. That is why `×2` is
exact for `D_t`.

The `416×` and `10⁴×` figures measure the approximation allowance only.
Codex is right, and the consequence goes further than its plan reflects:
measured this way, `E_max` has the most room of the unaudited links and the
tail the least.

Two considerations still favour doing `E_max` early. It is cheap. And it
is the one supplier, with the finite floor, that fixes the claimed `t₀`,
whereas a tail or barrier failure could most likely be repaired by more
computation **[judgement]**. That argues for bundling `E_max` with the
tail, not for leading with it alone. The two also draw on the same Polymath
inputs: the bounds (20)–(23) with the exact error definitions (71)–(72),
Proposition 6.6(vi) and the 10.50 weld.

The tail audit should start with the partition (4.3) and the status of
`OV`. These are the second and third questions under Priority 6 of the
package's `OPEN_REVIEW_QUESTIONS.md`, and they decide whether the reserve
is `2.8·10⁻⁴` or about `0.04`.

The Newman README's "`400×` / `10⁴×`" sentence is accurate as written but
invites the same misreading. The next Newman session should add the
tolerances above beside it.

## 4. The parallel split

### 4.1 What is missing

- **Owners.** No lane owns the crosswalk, the amplification closure, the
  small-cofactor obligation statement or the method comparison. The tail
  and producer audits sit in Claude's close-out list without a slot.
- **Independence.** Newman notes 1–3 and their "cross-model" review were
  all written by Claude models (Fable 5.1, Opus 5.5). The arithmetic audit
  was written by Codex. Keeping each model on its own track is efficient,
  but each deliverable should get one review from the other family.
- **Compute.** If both agents run on one machine, the Lean build should
  have the CPU. Claude's numerics can run in its cloud workspace: every
  pinned input used here was fetched there by commit URL.

### 4.2 Shared files

The repository is worked from two clones: the Codex session's paths are
under `/Users/ebbaker`, this session's under `/Users/teddy`, and commit
identities alternate between them. That has already produced:

- the rebase conflict in the portfolio README (`5558b38`);
- merge markers in the base chat-history guide, later repaired by Codex;
- two captures both numbered 2.

Rules for the next round:

- Each lane writes only in the folders it owns.
- A cross-review is a new file in the reviewed project's `reviews/`, with
  no edits to that project's indexes.
- The portfolio README, `brainstorm/` and the base chat-history registry
  have one writer, in one integration step after both lanes commit.
- Chats are recorded in the project's own registry, one recorder at a time.
- Pull before each session and keep commits to owned paths.

### 4.3 Amended plan

| Step | Codex | Claude |
| --- | --- | --- |
| 1 | **A1** Lean replay at `fd4aeeb2` in Linux: three comparators, axiom reports, build log, patched-dependency list, Hecke statement reading. **A2**, while it builds: crosswalk table (October 5 link → September 30 lemma via Liu's Appendix B → Lean constant → identical, specialization or unresolved), starting from §2.2 | **B1** Tail lemma (partition and `OV` first, then caps, all-`N`, `y` and error gates) with the `E_max` uniformity gates, against `verify_tail_arb.c` and `verify_prop410_arb.c`; standard-library re-evaluation of `D` and `E_max` |
| 2 | **A3** amplification-lane closure note. **A4** cross-review of B1 | **B2** barrier: Lemma 8.4 majorants (16-term head and integral tail), prism gate, spatial term, `B_t ≠ 0`, `t → 0`. **B5** cross-review of A1's Hecke reading and A2's contracts |
| 3 | **A5** certificate-method comparison (Gordon, Planat, Raymond), which gives the Newman side a second model family | **B3** producer: shard parse, then frozen weights, amortization, remainders and parsing. **B4** audit close-out note |
| Any time | **A6** small-cofactor obligation statement from the return ledger, revised after A2; probes only after A2; covariance consolidation later | sharp-lane tail screen only after A5 and an explicit decision |

Folders: Codex writes in `arithmetic_source_audit/` and
`quasi-rh-character-amplification/`. Claude writes in
`newman_certificate_audit/`.

Decisions for Teddy: approve or amend this split; choose the `DRAFT_*`
spelling; and decide, as before, whether a sharp-lane certificate is a goal.

## 5. Corrections to the priority review, and limits of this note

This note serves as the dated clarification of the priority review. That
review is not edited. Its §4.2 slack sentence and its producer cost
estimate, its §4.1 GRH sentence, and its import-closure shortcut in §§2.4
and 4.1 are corrected above.

**Read.**

- The Codex response, the priority review and the brainstorm.
- The portfolio and Newman READMEs, and Newman notes 1 and 3.
- The return ledger, parts of the final extraction note, and the theta
  crosswalk record.
- The amplification README and equations (3)–(6) of the localized-witness
  note.
- Liu's paper, from the project file. Its arXiv HTML could not be fetched
  because of rate limiting.
- The user messages of chat 3, and a search of all recorded chat
  histories.

**Source** (hashes match the pins):

- The Gomila package at `a74738de`: barrier transcript, tail lemma, open
  review questions, the `E_max` verifier header, and the tail and
  `E_max` Arb logs.
- openai/math at `fd4aeeb2` and `adc7f124`: comparators, scope note,
  toolchain, manifests, lakefile patch lists, `RayFamily.lean`, both
  `Nonvanishing` modules, and the relevant sections of the September 30
  and October 5 sources. The 2,925 closure modules were hashed, not read.
- Liu's repository at `7d10420d`: `verify.py`, lakefile and closure
  manifest. Its patches were compared byte for byte, not read.
- The comparator README.
- Dunn–Radziwiłł v3, Theorem 1.4, through a fetched summary.

**Checked.** The programme and JSON record in [numerics](../numerics/README.md).

**Not done.** No Lean build or comparator run. No audit of the tail lemma,
of Lemma 8.4 or of the producer themselves; only their tolerances. No
comparison of the October 5 completion section with Lemmas 17.2–17.3. No
new mathematics is claimed.
