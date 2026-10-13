# Formal statement contracts and the finite-order Hecke bridge

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration; exact serving variant
and reasoning effort are not exposed and are not inferred. This is a
source-inspection record, assisted by an LLM, not independent mathematical
validation or successful formal replay.

## Finding and evidence boundary

The three comparator targets have the expected universal seven-eighths
contracts. The bespoke Hecke definition has substantive source theorems
connecting its lattice continuation to the ideal series, ray characters,
unit quotient, and finite Euler corrections. The factor one-sixth is
justified by an explicit element-to-ideal reindexing theorem. I find no
statement restriction to primitive characters, bounded conductor, selected
height, or characters of order six in these targets.

The remaining checks are execution and the application crosswalk. No
solution was compiled or comparator run for this note, and no actual axiom
report was produced. All occurrences of “theorem” below identify a source
declaration and its written contract; acceptance by the pinned checker
remains unverified. Import-closure membership supplies none of these
application conclusions on its own.

The inspected checkout is openai/math
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, read under
`/private/tmp/formal-replay-crosswalk-20261012/upstream/openai-math`.
Its manifest pins Mathlib to
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Source-file hashes, exact target
contracts, and the distinction between nominated and reported axioms are
in [the accompanying small record](../numerics/formal_statement_contracts_20261012.json).
Third-party source files and build artifacts are not copied into this lane.

## 1. Exact comparator scope

The displayed OpenAI theorem names are rooted at `OAI`; library names are
retained as written, and `_root_` bypasses the local namespace.

| Target and exact name | Universally quantified inputs and hypotheses | Exact conclusion |
| --- | --- | --- |
| `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` | Every `s : ℂ`; `(7 / 8 : ℝ) < s.re` | `riemannZeta s ≠ 0` |
| `OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re` | Every `q : ℕ` with `[NeZero q]`, every `χ : DirichletCharacter ℂ q`, every `s : ℂ`; `(7 / 8 : ℝ) < s.re`; `¬ (χ = 1 ∧ s = 1)` | `_root_.DirichletCharacter.LFunction χ s ≠ 0` |
| `OAI.SevenEighths.HeckeFamily.LFunction_ne_zero_of_seven_eighths_lt_re` | Every `χ : HeckeFamily.Character`, every `s : ℂ`; `(7 / 8 : ℝ) < s.re`; `¬ (χ.residue = 1 ∧ s = 1)` | `HeckeFamily.LFunction χ s ≠ 0` |

The challenge sources are
[zeta](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/QuasiRiemannHypothesis.lean#L5),
[Dirichlet](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/DirichletSevenEighths.lean#L8), and
[Hecke](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/HeckeSevenEighths.lean#L237).
The corresponding solution declarations in
[Nonvanishing](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean#L19)
and
[Hecke.Nonvanishing](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/Nonvanishing.lean#L13)
have these same written signatures. Text inspection is weaker than the
comparator's environment and proof-object checks.

Each JSON nominates exactly its one displayed theorem, lists
`definition_names: []`, permits `propext`, `Quot.sound`, and
`Classical.choice`, and sets `enable_nanoda: false`. Zeta and Dirichlet
use solution module `OAI.NumberTheory.DirichletL.Nonvanishing`; Hecke uses
`OAI.NumberTheory.DirichletL.Hecke.Nonvanishing`. These are the requested
configuration fields, not an executed axiom-dependency result. Empty
`definition_names` means that no additional definition is separately
nominated; it is not evidence that definitions appearing in a theorem
contract have been bypassed or accepted.

The boundary `Re(s) = 7/8` is excluded in all three statements. Dirichlet
includes modulus one, principal and imprimitive characters, and both
parities. Its pole exception is only the conjunction of principal character
and `s = 1`. The Hecke exception uses the identity *residue character*,
which is the principal mask on the chosen modulus.

Zeta's signature deliberately has no pole-exclusion hypothesis. Mathlib
defines a total function with an assigned value at the analytic pole;
its pinned nonvanishing source explains that this value is nonzero. The
analytic interpretation is nonvanishing of the meromorphic function away
from its pole, plus a convention-specific assertion at one. See
[RiemannZeta](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/NumberTheory/LSeries/RiemannZeta.lean#L20)
and
[Mathlib Nonvanishing](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/NumberTheory/LSeries/Nonvanishing.lean#L18).
The upstream Hecke-to-zeta bridge explicitly uses
`riemannZeta_one_ne_zero` at `s = 1`.

## 2. Bespoke character and finite-order family

The challenge repeats the relevant definitions; the solution's canonical
definitions are in
[Hecke.Family](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/Family.lean#L13):

- `K := CyclotomicField 3 ℚ`, `O := NumberField.RingOfIntegers K`.
- `omega` is the integral primitive third root; `coordinateElement x y`
  is `x + y * omega` for integers `x,y`.
- `Character` carries a nonzero ideal `modulus`, a
  `residue : MulChar (O ⧸ modulus) ℂ`, and
  `unit_trivial : ∀ u : Oˣ, residue (Ideal.Quotient.mk modulus (u : O)) = 1`.
- It also carries `period : ℕ`, `period_pos : 0 < period`, and
  `period_mem : (period : O) ∈ modulus` for the periodic lattice construction.

The period is an auxiliary presentation, not a condition bounding the
conductor or order of the character. `Character.ofResidue` takes any
nonzero ideal, any residue multiplicative character, and unit triviality;
it constructs a permitted period using `Fintype.card (O ⧸ M)` and the
finite quotient's characteristic. Therefore the period field introduces
no family restriction. `elementCoeff_add_period_mul` and
`periodicCoeff_eq_elementCoeff` prove that the coordinate periodicity
agrees with the original residue coefficient.

Since the quotient by a nonzero ideal is finite, restriction to its unit
group has finite image in complex roots of unity. This is visible inside
`IdealCharacter.norm_residue_le_one`, which invokes
`MulChar.apply_mem_rootsOfUnity` on units. Nonunits map to zero by
`MulChar.map_nonunit`. Finite-order here applies to the character on
coprime ideals, before its zero extension; an ideal coefficient that is
zero is not itself a root of unity. The main theorem does not restrict the
order to two, three, or six.

The standard semantic identification is as follows. Milne's ray-class
exact sequence, together with class number one and no real places,
identifies the ray class group with the quotient of residue units by the
image of global units. Consequently characters of that quotient are
exactly residue characters trivial on global units. This use of
[Milne, *Class Field Theory*, Chapter V, Theorem 1.7](https://www.jmilne.org/math/CourseNotes/CFT.pdf#page=159)
is a classical inference from the stated exact sequence and the field's
properties. The source manuscript itself defines its family as ray
characters, extended by zero, at
[paper.tex lines 50–64](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L50).
The finite-order continuous character at the complex place is trivial
because the place's multiplicative group is connected.

The source makes the residue-to-ray interface explicit:

| Declaration | Contract or role |
| --- | --- |
| `SevenEighths.RayOrthogonality.globalUnits M` | Image of `Oˣ` inside `(O ⧸ M)ˣ` |
| `RayOrthogonality.rayCharacters M` | The subgroup of residue `MulChar`s trivial on `globalUnits M` |
| `RayOrthogonality.mem_rayCharacters_iff` | Membership is equivalent to `IdealCharacter.UnitInvariant M χ` |
| `RayOrthogonality.rayCard M` | `Nat.card ((O ⧸ M)ˣ ⧸ globalUnits M)`; `card_characters` identifies the cardinality of its character family |
| `HeckeRayFamily.character M χ` | Constructs `HeckeFamily.Character` from any member of `rayCharacters M` |
| `HeckeRayFamily.idealCoeff_character` | Its ideal coefficient is definitionally `RayOrthogonality.idealCharacter M χ` |
| `HeckeRayFamily.principal_iff` | `(character M χ).residue = 1 ↔ χ = 1` |
| `HeckeRayFamily.LFunction_ne_zero_of_seven_eighths_lt_re` | Every nonzero ideal `M`, every such ray character, every `s` with `Re(s)>7/8`, excluding exactly `χ=1 ∧ s=1` |

See
[RayOrthogonality](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/RayOrthogonality.lean#L89),
[RayFamily](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/RayFamily.lean#L11), and
[the ray nonvanishing corollary](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/Nonvanishing.lean#L30).
Both `RayFamily` and `IdealBridge` install
`IsCyclotomicExtension.Rat.three_pid K` as the principal-ideal-ring
instance. Thus the ideal class issue is explicitly addressed, not inferred
from the absence of real places.

The inspected modules provide these concrete residue, quotient, and ideal
interfaces. I did not identify a generic Lean equivalence from an abstract
idelic Hecke-character type onto this family. Accordingly the standard
idelic interpretation should be labelled a classical semantic bridge;
the concrete ray-family statement is an actual source corollary. The
residue-family coverage itself is fully explicit in the source.

## 3. Ideal coefficients, zero extension, and one-sixth normalization

`SevenEighths.IdealCharacter.ofResidue M χ hu` is a monoid-with-zero hom
`Ideal O →*₀ ℂ`: it assigns zero to the zero ideal and uses the residue
value of a generator on every nonzero ideal. The contract
`ofResidue_span` applies only to a nonzero generator. Its proof uses
`residue_eq_of_associated`, hence unit triviality, to eliminate the
generator choice. `isUnit_mk_iff_isCoprime` identifies residue units with
ideals coprime to the modulus. This supplies the standard zero extension;
`HeckeFamily.idealCoeff_source_mask` writes it explicitly as
`idealCoeff η I = if IsCoprime I η.modulus then idealCoeff η I else 0`.
For the principal character, `ofResidue_one` is the coprimality indicator
on nonzero ideals, and `ofResidue_one_top` is one on all nonzero ideals.
See
[IdealCharacter](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/IdealCharacter.lean#L17)
and
[ModulusRefinement](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/ModulusRefinement.lean#L22).

The normalization chain is concrete:

1. `HeckeTheta.theta` sums periodic coefficients times
   `exp(-π * normForm(x,y) * t)` over `ℤ × ℤ`. The completed function is
   `(pair w).Λ`, and `latticeL w s = π^s * (Gamma s)⁻¹ * completed w s`.
   `HeckeTheta.latticeL_hasSum` in `ThetaSeries`, for `1 < s.re`, gives the lattice
   Dirichlet series with denominator `normForm(x,y)^s`.
2. `HeckeFamily.coordinateEquiv` identifies integer coordinates with the
   ring of integers. `normForm_eq_absNorm_span` identifies the quadratic
   form `x² - xy + y²` with the absolute norm of the generated ideal.
3. `UnrestrictedIdealReindex.unitIdealEquiv` gives the bijection between
   nonzero elements and pairs of a unit and a nonzero ideal. Its
   `tsum_unit_invariant_of_zero` reindexes a summable unit-invariant
   function as six times its ideal sum, using
   `PrimaryIdealUnitReindex.card_units_eq_six`.
4. `HeckeFamily.continuedLattice_eq_six_ideal_tsum`, for `1 < s.re`, gives
   `continuedLattice χ s = 6 * ∑' I, idealTerm χ s I`.
5. `HeckeFamily.LFunction χ s := continuedLattice χ s / 6`, and
   `LFunction_eq_ideal_tsum` proves
   `LFunction χ s = ∑' I, idealCoeff χ I / (absNorm I)^s` for `1 < s.re`.

These declarations appear in
[Theta](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/Theta.lean#L61),
[ThetaSeries](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/ThetaSeries.lean#L55),
[the ideal bridge](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/IdealBridge.lean#L26), and
[the reindexing theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/CubicSieve/ResidualSectors.lean#L547).

The zero element must be distinguished from bad-prime zero extension.
At the unit modulus the residue quotient is the trivial ring, and the
principal coefficient at the zero element can be one. The theta Mellin
construction subtracts that constant term; the series term at zero is
zero for the relevant `s ≠ 0` by `elementTerm_zero`. Thus this case does
not add a spurious constant to the ideal series.

`LFunction_eq_series` in
[Hecke.Euler](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/Euler.lean#L11)
identifies the result with `IdealEuler.series (idealCoeff χ) s` for
`Re(s)>1`, and `inverseSeries_mul_LFunction` gives the Möbius inverse
identity there. Equality to the standard meromorphic continuation in
the remaining half-plane is justified by the series identity and analytic
continuation, not by substituting a divergent ideal sum. The source
provides `LFunction_differentiableAt` when `s ≠ 0` and either `s ≠ 1` or
the residue is nonprincipal, and `LFunction_entire_nonprincipal` globally.

## 4. Principal pole and primitive/imprimitive correction

The principal status is modulus-dependent as a zero-extended residue
mask. It must not be confused with a constant-one element coefficient
at every element of a nontrivial quotient. `HeckeOrigin.poleRemoved` is
entire, equals `(s-1) * LFunction χ s` away from zero and one, and has
nonzero value at one for principal residue. `HeckePrincipalResidue`
strengthens that value to a positive real residue. For nonprincipal
residue, `LFunction_entire_nonprincipal` supplies a meaningful analytic
value at one, which is included in the seven-eighths statement. See
[Origin](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/Origin.lean#L11)
and
[PrincipalResidue](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/PrincipalResidue.lean#L35).

`HeckeFamily.exists_primitive_character` supplies a `ψ` with
`χ.modulus ≤ ψ.modulus`, `FiniteFourier.IsPrimitiveOnIdeals ψ.residue`,
`absNorm ψ.modulus ≤ absNorm χ.modulus`, and the exact mask

`idealCoeff χ I = if IsCoprime I χ.modulus then idealCoeff ψ I else 0`

for every ideal `I`. Ideal containment is in the displayed direction:
the primitive conductor divides the chosen modulus. It is unsafe to
read the containment direction as an increase in conductor. This is a
primitive presentation with a norm bound; a claim of conductor minimality
requires its own contract. See
[IdealOperations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/IdealOperations.lean#L16).
The exact predicate in
[FiniteFourier](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/FiniteFourier.lean#L18)
is `∀ I : Ideal R, I ≠ ⊥ → ∃ u : Rˣ, (u : R) - 1 ∈ I ∧ χ (u : R) ≠ 1`
for the finite residue ring `R`. This expresses nontriviality on every
nonzero ideal congruence kernel in that ring; it is the predicate actually
required by the downstream theorems.

For a primitive character with principal ideal modulus `(c)`,
[`HeckePrimitive.completedL_eq_gamma_mul_LFunction`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/Primitive.lean#L149)
states that `completedL = scale(c)^(-s) * π^(-s) * Gamma(s) * LFunction`
when `s ≠ 0,1` and `Gamma(s) ≠ 0`. Here
`scale(c) = GaussianTheta.parameter c 1 = 2 / (sqrt(3) * |c|)`.
Using the source norm identity `|c|² = absNorm((c)) = Q`, its multiplier
is the conventional `(3Q)^(s/2) * (2π)^(-s) * Gamma(s)`.
This last algebraic comparison is a semantic normalization inference,
not a newly executed Lean theorem. The source functional equation is
written in the orientation
`completedL χ (1-s) = normalizedGauss χ * completedL χ⁻¹ s`,
under `s ≠ 0,1` and the displayed primitive and unit-invariance hypotheses.
Its exact orientation and hypotheses must be retained in any application.

[Hecke.FiniteDeletion](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/FiniteDeletion.lean#L12)
defines `factors M ψ` as the finite product over prime divisors of `M`
of `1 - idealCoeff ψ P * (NP)^(-s)`. This includes primes dividing the
primitive conductor; their coefficient is zero, so their factor is one.
The operative declarations are:

| Declaration | Exact domain and conclusion |
| --- | --- |
| `factors_ne_zero` | Every ideal `M`, every `ψ`, `0 < s.re`; product is nonzero, using `NP ≥ 2` and coefficient norm at most one |
| `LFunction_eq_of_mask_right` | Given the exact ideal mask above, `1 < s.re`; `LFunction χ s = LFunction ψ s * factors χ.modulus ψ s` |
| `regularizedL_eq_of_mask` | Given the mask, `0 < s.re`; same identity for the regularized functions |
| `LFunction_eq_of_mask` | Given the mask, `0 < s.re` and `s ≠ 1`; identity for the original functions |
| `principal_iff_of_mask` | Given the mask, `χ.residue = 1 ↔ ψ.residue = 1` |
| `LFunction_eq_of_mask_nonprincipal` | Given the mask, `χ.residue ≠ 1`, and `0 < s.re`; original-function identity also at `s = 1` |
| `LFunction_eq_of_mask_nonpole` | Given the mask, `0 < s.re` and `s ≠ 1 ∨ χ.residue ≠ 1`; original-function identity |
| `exists_primitive_same_zeros` | Finds a primitive presentation with no larger modulus norm, preserving zeros for `0 < s.re` and `s ≠ 1` |
| `exists_primitive_zero` | Transfers a zero in `0 < s.re`, excluding the principal pole, to a primitive character with the same nonpole condition |

The product nonvanishing contract has no claim on the line `Re(s)=0`.
Positive real part is enough for every seven-eighths use. The separately
named module `Hecke.FiniteEulerFactors` primarily supplies a norm-lift
and fixed-test restoration interface; its presence in `Foundation` is
not the justification for the primitive/imprimitive Hecke identity.

`Character.refineModulus` and `Character.excludePrimes` in
`ModulusRefinement` supply exact coefficient masks for enlarging a
modulus and adding a finite prime exclusion set. These are the right
interfaces for fixed primes above two and three or a fixed auxiliary
set in the October 5 argument. Their Euler corrections should be
applied through the mask theorem, retaining its domain and pole condition.

## 5. Relation to zeta/Dirichlet and next checks

There is also a direct norm-lift interface in
[Hecke.Dirichlet](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/Dirichlet.lean#L71).
For any positive modulus `q`, `HeckeDirichlet.character χ` uses ideal
modulus `(q)` and has `idealCoeff I = χ(absNorm I)` on nonzero ideals.
`LFunction_eq_dirichlet_product_right` identifies its series with the
product of `χ.LFunction` and `(ShortDraftHeckeBridge.baseChangeChar χ).LFunction`
for `Re(s)>1`; `LFunction_eq_dirichlet_product` extends this identity
away from `s=0,1`. `dirichlet_seven_eighths_of_hecke` handles `Re(s)≥1`
using Mathlib nonvanishing, and uses the product identity in
`7/8<Re(s)<1`; `zeta_seven_eighths_of_hecke` includes the assigned value
at one. These are named source contracts, so the norm-lift connection
need not be inferred from an import list.

The actual nominated zeta and Dirichlet solution declarations call
`ProbeFinalAssemblyUnconditional.zeta_nonzero` and `dirichlet_nonzero`.
The Hecke solution calls `LFunction_ne_zero_of_certified_bands` with
`ProbeFinalAssemblyUnconditional.detector_certified_bands`.
[`Foundation.lean`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Foundation.lean)
is an import hub; reading those imports is useful for navigation and does
not prove each manuscript application.

This closes the first semantic reading at the concrete residue/ray-family
level. The next deliverable must add successful comparator outcomes and
reported axioms in the specified checking environment. In parallel, each
October 5 application needs its own named Lean constant and a comparison
of assumptions, normalization, signs, masks, smooth-profile class,
parameter ranges, and uniformity. A successful replay of these three
universal conclusions will not by itself certify that entire proof route
or later applications.
