# Priority review after the audits: where I agree, and what I would change

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: Claude Fable 5.1 (`claude-fable-5-1`), Anthropic, in Claude Cowork;
the session was configured as `claude-opus-5-5` and the serving model
identifies itself as Fable 5.1. Reasoning effort: not exposed in this
session and not inferred. This note reviews the
[12 October Codex brainstorm](NEW_PATHS_FORWARD_AFTER_AUDITS_CODEX_20261012.md)
and the [portfolio README](../README.md). It proposes a changed order of
work; it establishes no new zero-free strip, Newman bound, or RH mechanism.
Internal model checks, including this one, are not independent mathematical
validation.

Revision in the same session: after the first draft, the author supplied
arXiv:2610.12234v1 (B. Liu, 8 October 2026) as a PDF. It was read in full
and Sections 2.5, 4.1 and 4.7 and the order in Section 3 were revised
accordingly. The paper supersedes the repository's character-amplification
lane; see Section 4.7.

Labels used below: **[read]** a repository or source file read in full;
**[checked]** arithmetic or a statement re-derived here; **[source]** a
primary external file read directly; **[web, unverified]** a third-party
report found by web search and not verified; **[judgement]** my own
assessment.

## 1. Verdict

I agree with the brainstorm's three-part program and with nearly all of
its stop rules. In particular I agree that independent scrutiny of the
arithmetic argument outranks new arithmetic; that the corrected-interface
benchmark should stay closed; that the sharp-weight Newman lane is an option
and not a result, with the tail and the `y`-transfer as its only real
risks; that the quadratic covariance is a diagnostic and not a route; and
that the four scoped support projects should stay capped until they
identify information the two main routes lack. Where I checked the
brainstorm's arithmetic it is correct (Section 6).

I would change five things.

1. **Priority 1 is aimed at the wrong artifact.** The brainstorm asks for
   a specialist reconstruction package for the October 5 argument, which
   proves the half-plane `Re s > 11/12`. The same source repository marks
   the stronger September 30 theorem, `Re s > 7/8` for zeta, every
   Dirichlet `L`-function, and every finite-order Hecke `L`-function over
   `Q(√−3)`, as **formalized in Lean**, with comparator statements that
   use Mathlib's own `riemannZeta` and `DirichletCharacter.LFunction`.
   The repository has never replayed that formalization (its own
   amplification README says "No Lean proof was replayed") and continues
   to label the 7/8 theorem an assumption. Replaying the Lean build and
   reading the three formal statements is one session of mechanical work,
   and it dominates every prose audit as evidence for the conclusion: the
   11/12 strip is implied by the 7/8 strip. I would make this **priority
   0**. Section 2 gives the details and the caveats.
2. **Priority 1 should be re-aimed, not dropped.** Once the conclusion is
   settled by the formal artifact, the October 5 prose matters for its
   *mechanism*. Liu's Part I and Appendix B now supply, for the September
   30 argument, exactly the theorem-to-application index the brainstorm
   asked for, and they show that the architecture the arithmetic audit
   reconstructed for the October 5 chain (two-Poisson transfer, finite
   induction, sixth-power extraction) is the architecture of the September
   30 paper's Lemmas 17.1–17.6. The specialist deliverable becomes a
   crosswalk, not a reconstruction. That crosswalk is also the prerequisite
   for the brainstorm's item 3.
3. **The character-amplification lane is superseded and should be
   closed.** Liu varies the same two length parameters the lane varied,
   proves `B_new = 0.874957069799…` from the September 30 intermediate
   results, expects it to be optimal for that estimate system, and reports
   a Lean 4 formalization. The lane's own computed limit of its `b = 1/8`
   family, `0.8749572006`, lies `1.3·10^{−7}` above Liu's two-parameter
   optimum. Its conditional candidate `7/8 − 1/24000` is now dominated by a
   public, formalized result; its proposed next target `7/8 − 1/20000`
   lies beyond Liu's expected optimum and needs a new estimate, as the lane
   itself said. Section 4.7.
4. **The Newman order should follow the slack ratios, and the method
   comparison should precede any sharp-lane work.** The uniform error
   budget `E_max` is 29 % of the weakest row's certified value; the barrier
   has `400×` slack and the tail `10^4×`. So the `E_max` proof-to-code map,
   not Lemma 8.4, is the audit piece most able to change a conclusion. The
   full producer regeneration should be dropped as an audit target. And
   since the sharp lane's candidate `0.1745354` is numerically dominated by
   two public claims, the comparison of certificate methods, which the
   brainstorm discusses but leaves out of its ordered table, should be
   placed above the sharp-lane feasibility test.
5. **Item 3 should be gated, and its first deliverable changed.** The
   small-cofactor branch should start only after the crosswalk exists, and
   its first output should be the statement of the structural input that
   the small shells would need, not a probe.

The revised order is in Section 3.

## 2. The facts that change the arithmetic priorities

### 2.1 What the source repository states [source]

The audited source is `openai/math` at commit
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` (the same commit the
[final assembly review](../arithmetic_source_audit/reviews/FINAL_ASSEMBLY_REVIEW_20261012.md)
pins). I read, from a sparse clone of that commit on 12 October:

- `CONTENTS.md`, entry 003: the September 30 paper "proves that every
  Dirichlet `L`-function, including `ζ(s)`, is zero-free in `Re s > 7/8`
  … The same half-plane is zero-free for every finite-order Hecke
  `L`-function over `Q(√−3)`. A companion gives a different proof of the
  zero-free half-plane `Re s > 11/12`." The entry carries a Lean link;
  the companion does not.
- `lean/docs/003.md`, the formalization scope: "The formalization gives
  `θ = 7/8` for the Riemann zeta function and every Dirichlet
  `L`-function, uniformly over all positive moduli and all characters. It
  also establishes the same bound for finite-order Hecke `L`-functions over
  `Q(√−3)`. The principal-character poles at `s = 1` are excluded in the
  Dirichlet and Hecke statements. The paper's later applications are not
  included." The October 5 argument is not mentioned.
- `lean/ComparatorChallenges/QuasiRiemannHypothesis.lean`, the full
  comparator statement for zeta:

  ```lean
  theorem riemannZeta_ne_zero_of_seven_eighths_lt_re
      {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0
  ```

  Its JSON names the solution module
  `OAI.NumberTheory.DirichletL.Nonvanishing` and permits only the axioms
  `propext`, `Quot.sound`, `Classical.choice`.
- `DirichletSevenEighths.lean`: the same statement for
  `DirichletCharacter.LFunction χ s` with `χ : DirichletCharacter ℂ q`,
  `NeZero q`, and the hypothesis `¬ (χ = 1 ∧ s = 1)`.
- `HeckeSevenEighths.lean`: a bespoke construction, about two hundred
  lines including its helper lemmas.
  `K := CyclotomicField 3 ℚ`, `O` its ring of integers; a `Character` is a
  nonzero ideal `𝔪`, a `MulChar (O ⧸ 𝔪) ℂ` that is trivial on the image
  of `Oˣ`, and a period `N ∈ 𝔪`. The `L`-function is defined as
  `(1/6)·π^s·Γ(s)⁻¹·Λ(s)`, where `Λ` is the completed Mellin transform
  of a theta series assembled from products of two Hurwitz even
  functional-equation pairs with shifts `xShift`, `yShift` and scales
  `L²`, `3L²`. The statement is `LFunction χ s ≠ 0` for `Re s > 7/8`
  unless `χ.residue = 1 ∧ s = 1`. Solution module:
  `OAI.NumberTheory.DirichletL.Hecke.Nonvanishing`.
- `lean/ComparatorChallenges/README.md`: the verification recipe is
  `lake update`, `lake exe cache get`, then
  `lake env comparator ComparatorChallenges/<name>.json`, with
  `comparator`, `landrun` and `lean4export` on `PATH`. Toolchain
  `leanprover/lean4:v4.34.1`. The library has 913 `OAI` modules and about
  a dozen external Lean dependencies pinned by commit.

The challenge files themselves end in `sorry`; that is the comparator
design. The proofs live in the named solution modules, and the comparator
checks that a solution module proves the identical statement from the
permitted axioms.

### 2.2 What third parties report [web, unverified]

A public repository (`tomoto0/quasi-riemann-hypothesis-7-8-verification`,
dated 7 October) reports rebuilding the formalization, 2,924 modules with
no errors, and that the key theorems depend only on the three standard
axioms; it states that the Hecke challenge was **not** built. Coverage
pages report no identified error in either manuscript, quote Alex
Kontorovich calling the result a potential breakthrough, quote Jared
Lichtman that the cubic family of `L`-functions appears essential even for
the zeta corollary, and report a remark that the 7/8 method has a barrier
at `3/4`. None of this is peer review, and I have not verified any of it.

### 2.3 Where the repository stands [read]

The portfolio README states that for the arithmetic audit "Independent
mathematical validation remains outstanding." The arithmetic project's
README calls the audit "not independent mathematical validation or a newly
established zero-free result." The character-amplification README says
"The external reflection and moment proofs and the source's seven-eighths
theorem remain assumptions. No Lean proof was replayed." The 8 October
comparison note knew of the scope document and chose to audit the
October 5 argument instead.

### 2.4 Consequence [judgement]

The question the brainstorm's first priority is answering, whether the
quasi-RH strip is real, has a cheaper and stronger answer available than
any prose audit by any number of models. A compiled Lean proof from
standard axioms, with a statement that uses Mathlib's `riemannZeta`, is the
strongest form of verification this program can obtain, and 7/8 implies
11/12. Three model families have now audited the 11/12 prose and reached
"internal closure under imports"; a fourth audit would move the evidence
less than one `lake build`.

What the replay would and would not settle:

- It settles the **conclusion** at 7/8 for zeta and Dirichlet
  `L`-functions, provided the two Mathlib-based statements compile against
  their solution modules under the permitted axioms. Those two statements
  are transparent and need no interpretation.
- For the **Hecke family**, which is the hypothesis the repository's lanes
  actually use, the statement is bespoke and must be read as well as
  built. The checks are: that a unit-trivial `MulChar` on `O/𝔪` is exactly
  a ray-class character mod `𝔪` of trivial infinity type, hence that every
  finite-order Hecke character of `K` is a `Character` (the imaginary
  quadratic field has no real places, so this should be immediate); that
  the theta product with shifts `xShift`, `yShift` and scales `L²`, `3L²`
  encodes `N(x + yω) = x² − xy + y² = (x − y/2)² + 3y²/4` and that the
  normalization `π^s Γ(s)⁻¹` with weight `k = 1` yields
  `Σ_{z ≠ 0} χ(z) N(z)^{−s}` with coefficient exactly one, so that the
  factor `1/6` counts the units; that the resulting `L`-function is the
  imprimitive one (coefficients vanish off `(z, 𝔪) = 1`), whose
  nonvanishing for `Re s > 0` is equivalent to the primitive statement;
  and that `χ.residue = 1` is the trivial `MulChar`. This is one careful
  reading, not research.
- It does **not** settle the mechanism, the effective constants, the
  "later applications", or anything about the October 5 route as such.
  Whether the repository's imported lemmas are individually validated
  depends on whether they appear on the formal path; Section 2.5 says why
  the import closure of the Hecke module is worth listing for exactly
  this reason.
- If the build fails, the axioms are not the permitted ones, or the Hecke
  statement is not faithful, that is a finding of the first importance
  and the prose audit regains its urgency.

**Bounded deliverable (priority 0).** In
`arithmetic_source_audit/notes/`, a dated note recording the toolchain,
the commit, the exact commands, the build outcome for the two solution
modules, the `#print axioms` output for the three theorems, the list of
`OAI` modules in the import closure of
`OAI.NumberTheory.DirichletL.Hecke.Nonvanishing` with the ones that
correspond to the September 30 paper's Sections 5, 14 and 17 identified,
and the statement reading for the Hecke comparator with each of the checks
above marked passed, failed, or unresolved; a small JSON record in
`numerics/` with the module hashes and axiom lists. Keep the clone outside
the repository, consistent with `LARGE_FILES.md`. Expect hours of compute,
not days; the `tomoto0` figure of about 2,900 modules is consistent with a
Mathlib-dependent build with cache. If the Hecke module does not build in a
session, report that exactly; it is the one module no third party reports
having built, though Liu's verifier (Section 2.5) may have done so.

**Follow-on maintenance.** If the replay succeeds, the labels
"assumption" and "independent validation outstanding" attached to the 7/8
theorem across the repository should be revised in a dated clarification,
not by editing historical notes, in the same way the fact (D) correction
was handled. The arithmetic project's status line should then read: the
conclusion is dominated by a formally verified theorem; what remains
unvalidated is the October 5 route.

### 2.5 arXiv:2610.12234 (Liu, 8 October 2026) [source; read in full]

**What it is.** Baiying Liu (Purdue), "Slightly improved zero-free
half-planes for the quasi-Riemann hypothesis", 45 pages, dated 8 October.
The acknowledgments state that OpenAI Codex (GPT 6.1) assisted with
drafting, source checking and the search for improved bounds, and that
Claude (Opus 5.5) assisted with auditing. It follows the September 30
preprint, retains its numbering, and uses its proved intermediate results
throughout. Part I is a complete summary of the 7/8 proof with every input
indexed; Parts II and III vary the two length parameters `b = l_y − l_x`
and `ℓ` (the total selected prime length) of the modified average and
re-derive the exponent inequalities.

**What it proves.** Theorem 15.1: with `b = 1/8`, `ℓ = 1/6 + 1/10000`,
every finite-order Hecke `L`-function over `Q(√−3)` and every Dirichlet
`L`-function is zero-free in `Re s > B_r = 34999/40000 = 0.874975`.
Theorem 21.1: with
`b_new = −4/29 + 230√921/26709 ≈ 0.1234054`,
`ℓ_new = (33 + 8√921)/1653 ≈ 0.1668384`,
the same holds in `Re s > B_new = (1507 − 2√921)/1653 = 0.874957069799…`,
so `7/8 − B_new = 4.293·10^{−5}`. In both cases `B = 11/12 − ℓ/4`
**[checked]**. The algebraic values come from the critical zero class
`δ_c = (49 − √921)/48` at which the count exponent `R_* = 2/3` makes the
coefficient of `b` vanish; Proposition 25.1 proves `B ≥ B_new` for every
real choice of `M, ℓ` under three explicit affine constraints, and a
remark states the expectation that `B_new` is optimal for the full
estimate system with `3/4 ≤ κ ≤ 1`, `1 ≤ t ≤ 3/2`, while varying `κ`
beyond that range "may yield a further small improvement … by
`≈ 4.4799·10^{−8}`". The endpoint inequalities are proved by exact
polynomial identities (a Bernstein-basis certificate in Part II, an exact
discriminant identity in Part III) with an accompanying exact arithmetic
checker.

**Lean status, as stated by the paper.** Reference [15] is a GitHub
repository with Lean 4.34.1 formalizations of the zero-free conclusions
for both `B_r` and `B_new`, namespaces `RHZeroFreeExtension` and `RHV2`,
public conclusions `beta_star_le`, `hecke_nonzero`, `dirichlet_nonzero`,
`zeta_nonzero`, and a verifier `formalization/verify.py` that "builds the
complete import closure and replays the 22 correspondence theorems with
`-trust=0`", with transitive axioms `propext`, `Classical.choice`,
`Quot.sound`. I did not open that repository. If the import closure is the
`openai/math` library, this is a third party reporting a successful build
of the Hecke path; that is worth confirming as part of priority 0.

**What it says about the mechanism.** Liu's Section 1 states the engine
of the 7/8 proof in two sentences: one cubic-theta average is evaluated
two ways, directly by reflection (Kubota–Patterson automorphy, with the
completed theta mean square from the quadratic large sieve over number
fields and the additive large sieve), and by Poisson summation, which
isolates a principal Mellin integral containing `1/L_F(s, η)`; a
hypothetical zero makes two character polynomials simultaneously large,
and two moment estimates control the remaining nonprincipal terms. The
preliminary 11/12 stage (balanced scales `X = Y = Z^{1/2}`, direct bound
`Z^{1/4+ε}`, principal exponent `s − 2/3`) is load-bearing: the
character-count argument of the 7/8 stage needs `δ ≤ κ ≤ 5/6`, "so the
preliminary theorem cannot be omitted from this proof without replacing
that input". The two moments are the Möbius-weighted second moment
(Lemma 17.1 of the source, proved by an inverse-moment induction in which
"two finite Poisson transforms decrease `M` while preserving the common
character, coprimality condition and `4F_0 − 3M − 6z_cap` margin", with
the reflected mean square handling the terminal range) together with
sixth-power amplification (Lemma 17.6), and the unweighted fourth moment
(Lemma 18.1), whose decisive cancellation is
`(X_1X_2)^{1+it} − (Y_1Y_2)^{1+it} = 0` at equal products of scales. A
cubic-sieve term of Heath-Brown type enters twice: the sextic sieve
(Lemma 9.1 of the source, `(KN_s)^{2/3}`) in the preliminary character
count, and the quadratic–cubic sieve (Lemma 14.2, `(NL)^{2/3}`) behind the
divisibility-restricted theta mean square used by the modified average.
Where the chosen scales make those terms affordable is part of what the
crosswalk of Section 4.1 should record. Appendix B indexes every result of
the source used in Parts I–III.

## 3. Revised order

| Order | Deliverable | Brainstorm rank | Change | Continue when |
| --- | --- | --- | --- | --- |
| 0 | Lean replay and statement reading for the 7/8 theorems, with the import closure of the Hecke module listed against the source's Sections 5, 14, 17 (Section 2) | absent | new; one session | always worth finishing; a failure is itself the finding |
| 1 | Crosswalk of the audited October 5 chain to the September 30 paper's Lemmas 17.1–17.6 as indexed by Liu's Appendix B, stating where the Möbius and sextic structure is consumed (Section 4.1) | 1 | re-aimed from reconstruction to crosswalk; the full package follows only if the crosswalk fails | the crosswalk identifies the formalized lemma each audited link corresponds to, or names the link that has no counterpart |
| 2 | Close the character-amplification lane against Liu: dated closure note recording the parameter correspondence, the `1.3·10^{−7}` gap between the lane's `b = 1/8` limit and `B_new`, and the stop rule (Section 4.7) | absent | new; half a session | never reopened for parameter tuning; reopened only with a new estimate beyond Liu's system |
| 3 | Newman close-out: `E_max` proof-to-code map, then barrier Lemma 8.4 and the tail gates; write the audit as one reviewable note (Section 4.2) | 2 | reordered; producer regeneration dropped | every remaining supplier is checked from the pinned source or its gap is named |
| 4 | Certificate-method comparison: triangle lane against Gordon and Planat/Raymond (Section 4.3) | discussed, unranked | promoted above the sharp lane | a second method supplies a lever the triangle lane lacks, or the sharp lane is shown to be on the frontier |
| 5 | Small-cofactor short-moment branch (Section 4.4) | 3 | gated on item 1; first deliverable changed | a named analytic input produces a paid saving at small `B` without returning the unit sector at the same ratio |
| 6 | Sharp-lane tail and `y`-transfer screen | 4 | demoted; contingent on item 4 and on an explicit decision to pursue a replayable certificate contribution | tail start and sharp gate close with a credible full-lane cost |
| 7 | Covariance consolidation: one ledger, four-way classification, lanes closed with the problem stated | 5 | kept; framed as a close-out | a matched theorem beats the known envelopes on a surviving signed sector |
| parked | Function-field model; counterkernel construction; Weil two-packet comparison | 6, optional | parked with one-line reopen conditions in each README; no further README maintenance until reopened | the covariance ledger names a family (function fields); a proof actually uses a feature the counterkernel lacks; a finite detection target is declared |

Items 0, 1 and 2 are arithmetic and should run first and in that order;
items 3 and 4 are the Newman track and can interleave with them. Items 5
and 6 start only after their gates.

## 4. Reasoning for the individual changes

### 4.1 Re-aiming priority 1 at the mechanism [judgement, with checked arithmetic]

The audited chain gives, for `H = D^{1+ϑ}`,

```
Σ_{0 < N(u) ≤ D^{1+ϑ}} |A_u(D)|²  ≪  D^{2+ϑ+ε},
```

and the exponent `11/12 + 5ϑ/12` follows by pigeonholing on the
`≍ Y / log Y` sixth-power rows with `Y = D^{(1+ϑ)/6}`: `(2+ϑ) − (1+ϑ)/6`,
halved, is `(11 + 5ϑ)/12` **[checked]**. So `11/12` is `1 − 1/12`, the
price of extracting one row from a family of sixth powers; it has nothing
to do with any exponent inside the moment. The entire content of the
argument is the moment, and the moment sits exactly at the diagonal: the
family has `D^{1+ϑ}` members and the coefficient energy is `≍ D`
**[checked]**.

A diagonal-strength bound with family longer than the sum is an optimal
large sieve for this family. For cubic residue symbols the best general
bound is Heath-Brown's, with the extra term `(MN)^{2/3}`, and
Dunn–Radziwiłł, the very paper the audit uses as its primary theta source,
show that this cubic large sieve is sharp up to `X^{o(1)}` under the
Generalized Riemann Hypothesis (abstract of arXiv:2109.07463, fetched, one
sentence quoted verbatim **[source]**; their extremal coefficients are not
read here). With `M = D^{1+ϑ}` and `N = D` the general-coefficient cubic
bound is `D^{7/3 + 2ϑ/3}`, against the claimed `D^{2+ϑ}`; the claim beats
it by `D^{(1−ϑ)/3}` **[checked]**. The GRH condition does not weaken the
test: if the October 5 moment bound applied to the Dunn–Radziwiłł extremal
sequence, then under GRH it would be false; so the step that confines the
bound to the Möbius family is load-bearing, and an argument whose purpose
is a step toward RH cannot escape by denying GRH. The sextic symbol factors
as a quadratic times a cubic symbol, so the quadratic large sieve of
Goldmakher–Louvel can only account for the quadratic part. The audit
already says the argument "never enlarges the completed-family estimate to
arbitrary sextic coefficient sequences", and the brainstorm says the
quadratic large sieve "does not become an arbitrary sextic coefficient
estimate by changing notation". Both are the right caution. Neither names
the step.

Liu's Part I names it for the September 30 route (Section 2.5): the
Möbius-weighted moment is reduced by two finite Poisson transforms to the
completed theta coefficients, whose mean square comes from the theta
functional equation together with the quadratic large sieve and a
quadratic–cubic sieve, at scales chosen so that the cubic `2/3`-type term
is affordable. The arithmetic audit's own chain for the
October 5 argument (initial reduction, theta transformation, completed
mean square, two Poisson transfers, finite induction, sixth-power
extraction) is that architecture. The deliverable is therefore a
**crosswalk**: for each link of the audited October 5 chain, the lemma of
the September 30 paper, as indexed in Liu's Appendix B, that performs the
same step, with the differences in normalization, row length and loss
accounting noted. Where the crosswalk closes, the October 5 "imports" are
the same objects the September 30 formalization proves, and the question
"is this import validated" becomes "is this lemma in the formal import
closure", which priority 0 answers. Where it does not close, that link is
the one a specialist should read. This is a shorter and more decisive
deliverable than a reconstruction package, and I would write it before the
theorem-to-application contracts, not after.

The remaining parts of the brainstorm's priority 1 stand: the conjugated
cusp coefficients, nonunit frequencies, moving-row uniformity, exceptional
primes, and the common Mellin majorant are the right places to look if the
crosswalk leaves the theta step uncovered. The adversarial
reflection-identity diagnostic is a good idea only if both tails can be
bounded, as the brainstorm says.

### 4.2 Newman: order by what can change a conclusion [read, checked]

From [note 3](../newman_certificate_audit/notes/3_CERTIFIED_ROW_REPLAY_AND_FINITE_LANE_REDUCTIONS_20261012.md)
and the project README: the certified weakest row is
`L_690988 ≥ 7.9137·10^{−7}` against the package's `E_max = 2.33·10^{−7}`,
a ratio of `0.29` **[checked]**; the barrier's minimum margin `0.5198`
against the allowance `0.00125` is `416×`; the tail has `10^4×`. The
`E_max` budget is the only supplier whose error by a small factor would
flip the certificate. It is also the only finite-lane link that note 3 did
not re-audit. The brainstorm lists it second, after Lemma 8.4; I would
list it first. The Lemma 8.4 majorants are more intricate, but an error
there would have to be a factor of several hundred to matter.

The producer's full coverage should be removed from the audit list. The
standard-library certifier runs at about 100 s per row in the first leg and
about 125 µs per `m ≤ N` in general; over 3,149,013 rows that is of order
ten CPU-years **[checked, order of magnitude]**, and a hundredfold faster
implementation is still a CPU-month, for an unreviewed third-party claim
whose weakest rows are already independently certified. Record it as a
limitation of the audit, as note 3 already does.

With `E_max`, the barrier and the tail done, the audit is complete as a
deliverable: an independent replay of a public `Λ` certificate reporting
what was and was not verified. I would write that note and close the
project's audit phase before any new computation.

### 4.3 The method comparison belongs before the sharp lane [judgement]

The sharp lane's candidate objective `0.157 + 0.0350708/2 = 0.1745354`
**[checked]** is below Gomila's `0.1787854` and above Gordon's reported
`0.1576566…` and the reported Raymond claim `< 0.149396`, all at the same
verification height and all unreviewed. The brainstorm says this and
still ranks the sharp-lane screen at 4, with the comparison described in
prose but absent from the ordered table. I would invert that. The one
thing the comparison can produce that the sharp lane cannot is a *lever*:
if Gordon's method reaches `0.158` with a different finite-time criterion,
a phase-sensitive lower bound, or a different barrier, that is the
information worth having, and it decides whether a sharp triangle lane is
on the efficient frontier or a software exercise. The comparison is a
reading task against pinned sources and a table of criterion, inputs,
domains, proof-to-code obligations and availability.

On the sharp lane itself I agree with the brainstorm's analysis. The
first-row sharp value `+0.00178` at `t = 0.157` is almost four orders of
magnitude above the current `E_max` (which would itself be recomputed at
`t'`), so the finite-lane margin is not the risk; the `y`-transfer
for `U_g` with its absolute-value switch surfaces, and the tail with
contraction `0.99972` at a lower `σ`, are. If the lane is pursued, the
tail cost screen should come first, exactly as the brainstorm says. The
reason to pursue it is not the number; it is a certificate that others can
replay in the Polymath framework. That is a legitimate goal and it is the
author's decision, as notes 2 and 3 record.

### 4.4 Gating item 3 and changing its first deliverable [judgement]

The brainstorm's shorter-moment target `M_{h,a}` is, for `h < 1`, a bound
that beats the large sieve by a power on a family *shorter* than the
conductor, and on the coherent rows it is equivalent to the better strip
`b = (1+a)/2 + 5h/12`. Its own analysis shows that the positive-gap
geometry fails for `B ≤ D^{1−h}` and that the unit sector returns at the
same ratio. So the probe it proposes, retaining the signed return
restriction longer, can only succeed if some structural input acts at the
small shells. Which input that would be is what the crosswalk of item 1
identifies. Without it the probe is a search in the dark, and with it the
probe has a target. That is the gate.

Its first deliverable should therefore be a half-page statement, before
any computation: for the small shells `B ≤ D^{1−h}` including `B = 1`,
which of the inputs named in the crosswalk is still available, which is
lost, and what the lost one would have to be replaced by. If the answer is
"nothing is available at `B = 1` and the unit sector is the whole
obstruction", the brainstorm's own stop rule applies before a session is
spent. Liu's expected optimality of `B_new` for the September 30 estimate
system, and the reported `3/4` barrier for that method, are relevant
context: `h = 2/3, a = 0` would give `7/9`, which does not reach `3/4`, so
the sextic route is worth pursuing for descent only if its obstruction
structure differs from the September 30 method's. The crosswalk should say
whether it does.

### 4.5 The support projects [judgement]

The covariance consolidation is the honest close-out of the stalled lanes
and should be done once, as the brainstorm says. The function-field
project's original purpose, testing whether the descent reductions were
consistent with a known-RH world, is moot now that those reductions are
closed; its remaining purpose, an exact model for a chosen signed family,
cannot start until item 7 names the family. The counterkernel and Weil
tasks remain optional one-paragraph facts for the heat closure note. I
would mark all three as parked in their READMEs with a single reopen
condition each and suspend their README and chat-history maintenance
until then. Six open folders for one researcher and interleaved sessions
is an overhead the portfolio does not need.

### 4.6 Housekeeping [read]

- The brainstorm says the portfolio README "contains unresolved merge
  markers and overlapping status passages". The working tree at commit
  `94febc7` has no merge markers; the status passages read consistently.
  That item can be closed.
- The portfolio README and the arithmetic project use `DRAFT_HISTOR.md`;
  the Newman project and the project instructions use `DRAFT_HISTORY.md`.
  One spelling should be chosen.
- The README's background section should mention that the September 30
  theorem carries a Lean formalization at the pinned commit, with the
  replay status, and should cite Liu, so that future sessions do not
  re-derive the points of Section 2.

### 4.7 The character-amplification lane after Liu [read, checked, judgement]

The lane (`papers/quasi-rh-character-amplification`, 8–9 October) took
the September 30 geometry, kept `b = 1/8`, and lengthened the total prime
slot to `ℓ = 1/6 + e`. Its records **[read]**:

- `GEOMETRY_OPTIMIZATION_20261008.md`: `e = 1/6000`, so `ℓ = 1001/6000`,
  `l_x = 4249/12000`, `l_y = 5749/12000`, candidate boundary
  `σ = 11/12 − ℓ/4 = 20999/24000 = 7/8 − 1/24000`, exact polynomial
  certificate on the `(δ, x)` rectangle, `κ = 3/4` kept; and the limit of
  this `b = 1/8` family, where strict endpoint negativity fails at
  `e_* ≈ 0.0001711975385`, `δ_* ≈ 0.386688531`, boundary
  `≈ 0.8749572006154`.
- README: the candidate is conditional on the imported reflection and
  moment proofs and on the 7/8 theorem; "No Lean proof was replayed"; the
  next target `7/8 − 1/20000` "would suffice" given a new restricted
  mixed-moment saving of `1/5000`, which "remains unproved".

Liu's results in the same coordinates **[checked]**:

| Result | `b` | `ℓ` | Boundary | Status |
| --- | --- | --- | --- | --- |
| September 30 | `1/8` | `1/6` | `0.875` | formalized (openai/math) |
| Liu, rational `B_r` | `1/8` | `1/6 + 1/10000` | `0.874975` | proved; Lean per [15] |
| Lane candidate | `1/8` | `1/6 + 1/6000` | `0.8749583` | conditional; not formalized |
| Lane limit of the `b = 1/8` family | `1/8` | `1/6 + e_*` | `0.8749572006` | computed limit of the envelope |
| Liu, algebraic `B_new` | `0.1234054` | `0.1668384` | `0.8749570698` | proved; Lean per [15]; expected optimal for the system |
| Lane's proposed next target | — | — | `0.87495` | needs a new estimate; below `B_new` |

Three readings. First, the lane and Liu optimized the same two-parameter
family of the same estimate system; the lane went further than Liu's
rational choice along the `ℓ` axis and computed the `b = 1/8` limit, and
Liu optimized over `b` as well and attained a boundary `1.3·10^{−7}` below
the lane's limit, with a proof that the three affine constraints force
`B ≥ B_new` (Proposition 25.1) and an exact certificate on the full
rectangle (Lemma 24.1). The lane's stall was the real optimum of its
family, now established by a third party. Second, Liu's bound is
public, proved from the same intermediate results the lane imported, and
reported as Lean-formalized; the lane's candidate is weaker, private and
conditional. Third, the lane's own next target `7/8 − 1/20000 = 0.87495`
lies below `B_new`, consistent with Liu's remark that `B_new` is expected
to be optimal for the whole estimate system: the lane correctly identified
that a new estimate, not a parameter, is required, and Liu's expectation
that varying `κ` yields only `≈ 4.5·10^{−8}` more says the same.

The lane therefore has no further value as a parameter study and should
be closed with a dated note: the correspondence of parameters above, the
agreement of its limit computation with Liu's optimum, the statement that
its conditional candidate is superseded, and the stop rule that no further
geometry, including the `κ` extension, is worth a session. Its exact
polynomial certificate and its limit computation are a useful independent
corroboration of Liu's Lemma 19.1 and Proposition 25.1 and can be cited as
such. The lane's identified missing input, the restricted mixed-moment
saving on large-conductor rows (`T_joint` in the plain-ratio reduction),
remains the honest statement of what a further improvement needs; it
belongs in the covariance consolidation of item 7, not in a reopened lane.

One check worth a paragraph in the closure note: Liu's Lemma 19.1 bounds
the nonprincipal exponent at the original parameters by `−1/5000`, and the
lane's next target asks for a new saving of `1/5000`. Whether these are
the same quantity in different bookkeeping, or a coincidence of constants,
should be stated.

## 5. What I would not do

I would not commission a fourth model audit of the October 5 prose before
item 0. I would not reopen the amplification geometry, including the `κ`
extension. I would not start the sharp-lane sweep, the small-`B` probe, or
any function-field computation before their gates. I would not regenerate
the Gomila finite sweep. I would not treat any of the web-reported claims
in Section 2.2, including the clean rebuild and the `3/4` barrier, as
established until the repository has its own record, and I would treat
Liu's Lean claim the same way until his verifier has been run. And I would
keep the brainstorm's stop list intact: no heat lifts, no stationary-sign
recalibrations, no scalar moment rewritings, no amplification parameter
tuning until the missing source estimate has changed.

## 6. Checks performed and limits

- **[read]** The portfolio README; the Codex brainstorm; both active
  project READMEs; the final assembly review; Newman note 3 and the
  second-session summary; the three 11 October brainstorms; the
  chat-history user messages; the character-amplification README, its
  geometry-optimization note and the low-structural audit's exponent
  passage; the 8 October comparison note's Lean passage.
- **[checked]** The brainstorm's thresholds `a < 5(1−h)/6` and
  `a + 5h/6 < 3/4`; `h = 2/3, a = 0 ↦ 7/9`; `0.157 + y_0²/2 = 0.1745354`
  and `0.16125 + y_0²/2 = 0.1787854`; `√(1 − 2·0.157) = 0.82825`; the
  exponent `(11 + 5ϑ)/12`; the diagonal size of the sextic moment; the
  general-coefficient cubic bound `D^{7/3 + 2ϑ/3}` against `D^{2+ϑ}`; the
  `E_max`, barrier and tail slack ratios; the producer regeneration cost;
  Liu's `B_r`, `B_new`, `b_new`, `ℓ_new`, `δ_c` and `7/8 − B_new` from the
  stated closed forms; `B = 11/12 − ℓ/4` for Liu's two choices and the
  lane's candidate and limit; the ordering of the six boundaries in
  Section 4.7. All agree with the sources.
- **[source]** `openai/math` at `fd4aeeb2…`: `CONTENTS.md` entry 003,
  `lean/docs/003.md`, `lean/README.md`, `lean/ComparatorChallenges/README.md`,
  the four comparator `.lean` and `.json` files for result 003,
  `lean-toolchain`, `lakefile.lean`, and the `OAI.lean` import list; the
  abstract page of arXiv:2109.07463; arXiv:2610.12234v1 in full, from the
  PDF the author supplied. No Lean code was compiled, no solution module
  was read, and Liu's formalization repository was not opened.
- **[web, unverified]** The `tomoto0` verification README; two coverage
  pages summarizing expert remarks.
- **No new mathematics** is claimed. No manuscript, note, or review was
  edited. The grep for merge markers was run on the working tree.
