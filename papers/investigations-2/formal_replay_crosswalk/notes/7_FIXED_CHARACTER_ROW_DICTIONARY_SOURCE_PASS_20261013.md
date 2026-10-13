# Fixed-character row dictionary source pass

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration; exact serving variant
and reasoning effort are not exposed and are not inferred.

**Finding.** The inspected declarations give a concrete U1 dictionary,
conditional on the stated residue-character representation of the O5 input.
Take a genuine `HeckeFamily.Character eta`, put `f=1`, and let `m` carry the
declared fixed exclusions and the required bad primes. The exact row
specialization and sixth-power mask then give the centrally normalized O5
polynomial on every nonzero element row. This uses the original zero extension
of `eta`; it does not replace an imprimitive presentation by an unmasked
primitive lift. No new Lean construction, theorem application or compilation
has been performed here. The general classical-Hecke-character presentation
and the final generator/restricted-sum transports remain explicit application
obligations.

The pass used pure source reads and checked hashes against the preserved
source-closure manifest. It invoked no VM, Lean, Lake or comparator command,
and changed no research-repository file. All upstream references are to
`openai/math@fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.

## The input that is actually licensed

The source type is
`OAI.SevenEighths.HeckeFamily.Character`,
[Family.lean:22–29](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/Family.lean#L22-L29).
Its essential fields are a nonzero ideal `M`, a multiplicative residue
character `rho : MulChar (O/M) C`, and

\[
 \rho(\overline e)=1\quad\text{for every global unit }e\in O^\times.
\]

`Character.ofResidue`, [same file:31–45](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/Family.lean#L31-L45),
constructs the auxiliary positive period automatically; it imposes no bound
on the conductor, period or character order. Finiteness of the residue unit
group gives finite image in roots of unity, as used in
`IdealCharacter.norm_residue_le_one`,
[IdealCharacter.lean:111–125](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/IdealCharacter.lean#L111-L125).
This does not restrict the fixed input to cubic or sextic characters.

The unit condition is substantive. The permitted fixed element homomorphism
is `HeckeRowClosure.elementHom eta`, not an arbitrary function of type
`O ->* C`. The latter type alone does not make its value on a generator an
ideal invariant. The source contracts
`IdealCharacter.residue_eq_of_associated` and `ofResidue_span` use unit
triviality to remove the generator choice. At the Hecke interface,
`HeckeFamily.idealCoeff_span`,
[IdealBridge.lean:19–21](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/IdealBridge.lean#L19-L21),
states this equality for every nonzero generator, including a primary one.

The concrete ray family is also explicit:
`RayOrthogonality.globalUnits`, `rayCharacters` and `mem_rayCharacters_iff`,
[RayOrthogonality.lean:92–105](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/RayOrthogonality.lean#L92-L105),
represent residue characters trivial on the image of global units, and
`HeckeRayFamily.character` converts every such character to the above type.
Its ideal coefficient is definitionally the ray ideal character by
`HeckeRayFamily.idealCoeff_character`,
[RayFamily.lean:15–19](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/RayFamily.lean#L15-L19).

For a classical finite-order Hecke character `nu`, the existing Hecke-bridge
note explains the class-number-one/ray-class semantic identification. This
pass does not supply or locate a generic compiled equivalence from an abstract
idelic Hecke-character type into `Character`. The conditional input for the
dictionary below is precise: choose `eta` such that

\[
 \operatorname{idealCoeff}(\eta,I)=\nu(I)
 \quad\text{for every nonzero }I\text{ prime to the declared }S,
\]

with exactly the zero convention used for `nu` in the source family. This is
the representation equality to discharge, rather than an implicit claim
that any multiplicative element map is an admissible input.

## Declared exclusions and defining-modulus zeros

O5 [paper2.tex:663–678](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex#L663-L678)
declares a finite set `S` containing the primes above two and three and the
conductor primes of `nu`. Keep that set distinct from the zero support of a
particular residue presentation. A `MulChar (O/M) C` is zero on nonunits,
and `IdealCharacter.isUnit_mk_iff_isCoprime`,
[IdealCharacter.lean:28–48](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/IdealCharacter.lean#L28-L48),
identifies these zeros with ideals not coprime to **the defining modulus M**.

Thus the combined effective fixed zero support is

\[
 S_{\rm effective}=S\cup\{P:P\mid M\}.
\]

The construction below allows `eta` to supply its original zeros while `m`
supplies the declared `S`. If all defining-modulus primes already lie in `S`,
this union is simply `S`. If an imprimitive `nu` already vanishes at a
defining-modulus prime outside `S`, adding that prime to the fixed bookkeeping
set does not change any `A_u`: its original summands there were zero. That
statement requires the original zero extension; it is not permission to add
an arbitrary prime at which `nu` was nonzero.

In particular, the source's
`IdealCharacter.exists_primitive_associate`,
[IdealCharacter.lean:212–226](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/IdealCharacter.lean#L212-L226),
retains the **original M mask** even after exposing a primitive character of a
smaller modulus. Its equality has the form
`ofResidue(M,rho)(I)=1_(coprime(I,M))*ofResidue(K,phi)(I)`. Dropping that mask
can change the polynomial. `ofResidue_source_mask` and
`ofResidue_finite_deletion` make the same convention explicit. No primitive
replacement is needed for this U1 construction.

There are consequently two legitimate input situations, not one silently
merged convention. An intrinsic primitive finite-order character can be
represented at its conductor, yielding no extra presentation zeros. An
explicit imprimitive residue input must retain its original defining-modulus
zeros. The conditional representation equality above checks which situation
actually defines the supplied `nu`.

## A concrete RowData choice

Let `S` be the finite set of nonzero prime ideals in the declared exclusions.
For each `P in S`, choose the source's generator
`g_P=ConcretePrimeRowBridge.idealGenerator P`, with `(g_P)=P`. The source
provides `idealGenerator_ne_zero` for nonzero ideals in
[IdealGenerators.lean:60–65](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/PrimeRows/IdealGenerators.lean#L60-L65).
Here `lambda` denotes the source prime element `ConcretePrimeRowBridge.goodLambda`
used by `RowData`. Only its prime ideal above three and its divisibility are
used; no separate trace-normalizer equality is assumed. Take

\[
 q_S=\prod_{P\in S}g_P,\qquad
 m=\lambda\,2\,q_S,\qquad f=1.
\]

Every factor is nonzero. This directly supplies `m_ne_zero`, `f_ne_zero`,
`lambda_dvd` and `two_dvd` in
`HeckeInverseAmplification.RowData`,
[InverseAmplificationFamily.lean:12–19](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/InverseAmplificationFamily.lean#L12-L19).
The extra written factors `lambda` and `2` only repeat already excluded
primes; powers and generator units do not change the coprimality mask. `m`
need not itself be primary or squarefree, and `RowData` imposes neither
condition.

The principal ideal is
`(m)=(lambda)(2) product_(P in S) P`. Since the primes above two and three
are already included, its prime support is exactly the declared `S`.
Consequently, for nonzero ideals,

\[
 \operatorname{IsCoprime}(I,(m))
 \iff \forall P\in S,\ P\nmid I
 \iff (I,S)=1.
\]

The source prime criterion `HeckeInverseAmplification.prime_coprime_iff`,
[InverseAmplificationMask.lean:25–31](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/InverseAmplificationMask.lean#L25-L31),
and multiplicativity of ideal coprimality supply the exact finite-product
route. This support equivalence is part of the still-uncompiled finite-set
construction, not an equality asserted by the `RowData` structure itself.

For every nonzero element `u`, `RowData.character` chooses a character
`chi_u` and `RowData.character_spec` proves its element coefficient is

\[
 \operatorname{rowTwist}(\operatorname{elementHom}\eta,m,1,u)(n).
\]

Those declarations are at [InverseAmplificationFamily.lean:21–29](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/InverseAmplificationFamily.lean#L21-L29).
The existence theorem permits **every** nonzero `u`: it does not require
primary, squarefree, sixth-power-free or exclusion-coprime rows. The unit and
bad-prime parts of a moving row are retained by the periodic-row construction.

## Exact row coefficients and sextic masks

`HeckeRowClosure.idealCoeff_eq_row`,
[RowClosure.lean:236–250](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/RowClosure.lean#L236-L250),
transports `character_spec` to ideals:

\[
 \operatorname{idealCoeff}(\chi_u,I)
 =\operatorname{idealCoeff}(\eta,I)
   \operatorname{idealRowHom}(m^6u,I).
\]

On a `Supported` column, the exact sixth-power extraction is
`CanonicalRowCompletion.rowTwist_extract_sixth_mask`,
[PrimaryCompletions.lean:454–461](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/ChineseRemainder/PrimaryCompletions.lean#L454-L461).
Combining it with `idealCoeff_span` and the principal-ideal coprimality
criterion gives

\[
 \operatorname{idealCoeff}(\chi_u,I)
 =\operatorname{idealCoeff}(\eta,I)
   \mathbf1_{\operatorname{IsCoprime}(I,(m))}
   \operatorname{idealRowHom}(u,I).
\]

No squarefree hypothesis is needed for this coefficient identity. Its mask
comes from `idealRowHom_sixth_mask`,
[PrimaryCompletions.lean:427–446](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/ChineseRemainder/PrimaryCompletions.lean#L427-L446).
Locally,
`canonicalSextic_sixth_power_mask`,
[LocalProductAssembly.lean:542–551](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/GaussSum/LocalProductAssembly.lean#L542-L551),
states `canonicalSextic_P(m^6)=0` if `m in P`, and one otherwise. A sixth
power is therefore a coprimality mask, not the constant one on all residues.

The `Supported` convention is explicit at
[DivisorBlocks.lean:309–311](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/QuadraticSieve/DivisorBlocks.lean#L309-L311):
nonzero ideal, with no lambda prime factor and no residue characteristic two
factor. `supported_span_iff`, [TupleWeights.lean:382–415](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Fourier/TupleWeights.lean#L382-L415),
identifies this with `lambda` and `2` not dividing a generator.
Outside this domain, `rowTwist_zero_of_not_supported`,
[PeriodicRows.lean:92–100](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/RowCompletion/PeriodicRows.lean#L92-L100),
and `row_coeff_zero_unsupported`,
[InverseAmplificationMask.lean:12–23](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/InverseAmplificationMask.lean#L12-L23),
give zero. Those columns are already excluded by `S` in O5. They must not be
treated as additional surviving terms.

The local sextic convention also matches the O5 definition at
[paper2.tex:250–261](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex#L250-L261):

- `CompletedGauss.actualSextic` is definitionally
  `ActualEisensteinCubic.canonicalSextic`, [RowCaps.lean:204](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/CubicSieve/RowCaps.lean#L204).
- `canonicalSextic` is the fixed complex embedding of `sexticChar`,
  [EisensteinEmbedding.lean:461–463](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Arithmetic/EisensteinEmbedding.lean#L461-L463).
- `sexticChar_reduce_unit`, [FiniteFourier.lean:1337–1383](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/GaussSum/FiniteFourier.lean#L1337-L1383),
  gives exactly the congruence `x^((N(P)-1)/6)` for a residue unit away from
  characteristic two. `sexticChar_powers` gives the sixth-root property, and
  `sexticChar_zero_iff_mem`, [same file:1393–1399](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/GaussSum/FiniteFourier.lean#L1393-L1399),
  gives precisely zero at `u in P`.
- `idealRowHom_prime` and `idealRowHom_product`,
  [CompactEnergyFamilies.lean:489–512](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Eisenstein/CompactEnergyFamilies.lean#L489-L512),
  extend these local values multiplicatively to columns. On squarefree
  supported columns this is exactly the product defining `chi_n(u)`.
  Both ideal homomorphisms have value one at the unit ideal, agreeing with
  O5's empty-product convention.

For the polynomial, nonsquarefree columns have Möbius coefficient zero, so
the squarefree product interface is sufficient. The source likewise defines
the ideal row homomorphism multiplicatively on general supported ideals;
no new restriction to squarefree **rows** follows from this column argument.

The global-unit condition concerns changing the **column generator**. It
does not identify rows `u` and `e*u`. In particular, the source lemma
`rowTwist_unit` evaluates at a unit column; it is not a license to divide the
element-row moment by the six units. All nonzero element rows and their unit
factors remain present.

## Centrally normalized polynomial identity

`HeckeDetectorRowSpecialization.inverse_polynomial_original_row`,
[DetectorRowSpecialization.lean:11–25](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/DetectorRowSpecialization.lean#L11-L25),
already exposes the exact ideal sum after `character_spec`. With `f=1` and
zero analytic twists, it is

\[
 P_u(D)=D^{-1/2}
 \sum_{I\ne0}\mu(I)\operatorname{idealCoeff}(\eta,I)
      \operatorname{idealRowHom}(m^6u,I)
      W(N(I)/D).
\]

On columns prime to `S`, the previous mask is one, `eta` agrees with the
represented `nu`, and the local product is `chi_I(u)`. On other columns the
fixed mask is zero, or the unsupported-column declaration supplies zero.
Consequently the paper-level application is

\[
 \boxed{
 P_u(D)=D^{-1/2}
 \sum_{(I,S)=1}\mu(I)\nu(I)\chi_I(u)W(N(I)/D)
 =D^{-1/2}A_u(D),\qquad u\ne0,\ D>0.
 }
\]

The positivity of `D` identifies the source's complex-power normalizer with
the positive real square-root normalizer. `HeckeDyadic.norm` is the ideal
absolute norm, so the weight argument agrees. For compactly supported annular
`W`, finite ideal support licenses passing from the restricted infinite sum
to the O5 ideal sum; each nonzero ideal occurs once. O5's primary generator
notation chooses its representative, and `idealCoeff_span` removes that
choice for the fixed character. The local sextic convention is attached to
the ideal's residue field, so it supplies the same denominator convention.
There is no factor of six in this ideal-sum dictionary. The separate
one-sixth normalization of a lattice-series `LFunction` is unrelated here.

If a defining-modulus prime lies outside the declared `S`, it remains zero
through the **unmodified** `idealCoeff eta` in this equality. Rewriting with
`S_effective` is then legitimate only because those values of `nu` were
already zero; the displayed identity itself does not require changing `S`.

## What remains uncompiled

The useful bounded result is an explicit conditional dictionary and a
coefficient-by-coefficient derivation, with exact source entry points. Its
remaining Lean obligations are:

1. Construct or supply the residue presentation of the specific classical
   input, prove global-unit triviality, and prove the fixed-character
   coefficient agreement with its actual zero convention. The concrete ray
   input is directly accepted by the source; a generic classical idelic
   interface was not located in this pass.
2. Build `m` from the arbitrary finite exclusion set, prove its nonzero and
   divisibility fields, and prove its coprimality mask is exactly the declared
   `S` mask. Keep the defining-modulus mask distinct unless an explicit
   equality justifies combining bookkeeping sets.
3. Instantiate `character_spec`, the nonzero-generator ideal transport,
   supported/unsupported cases and local sextic product; assemble the
   restricted ideal sum and its primary-generator notation. The pinned
   declarations support these steps, but the new combined term has not been
   checked.

No reduction of arbitrary fixed ray-character order, arbitrary finite `S`,
nonprimitive zero support or arbitrary nonzero element rows was used. No
mathematical obstruction was found once the stated input representation is
available. This is not a claim that U1 has been formally replayed or that the
full O5 crosswalk is complete.

## Verified source identities

The following SHA-256 identities match the preserved closure manifest; paths
are relative to `lean/OAI/NumberTheory/DirichletL/`. The first source bundle
contained `Family`, `IdealBridge`, `RowClosure`, `RayFamily` and
`CompactEnergyFamilies`. Essential additional reads were the unit/zero
interfaces, finite-row specialization, sixth mask, support conventions and
the local sextic reduction listed below.

| Source | SHA-256 |
| --- | --- |
| `Hecke/Family.lean` | `9871d175749b34ec40cf66ccc14b4faa0a9ef08831cb3fa901c944e57c7b9ec6` |
| `Hecke/IdealBridge.lean` | `6c1fc33b7372108323bf3af3d4ab6f6e454ea9896b89e78964463a8e35df735f` |
| `Hecke/RowClosure.lean` | `de7e714eb48cc959993b8e58311cae6090e3258670a5c5618db6d98b19b986ea` |
| `Hecke/RayFamily.lean` | `86c80381f402618d744802694f1f09a9ab6a197d8730bcdd50d99a646c871c7e` |
| `Eisenstein/CompactEnergyFamilies.lean` | `895150367a2a113d4e16b072eddc9ef1ce7f3cf861fb891641101fdd9c6c6893` |
| `IdealCharacter.lean` | `ae9e08095d0eaa044a305e11db19c7d363302159897fcd54d07f65f952cc1f6e` |
| `RayOrthogonality.lean` | `85ff7487c61c123c298ed50f372be88338689a5d9d83ed4827bae30664243eed` |
| `Hecke/DetectorRowSpecialization.lean` | `cc461149e20ee542203ce8324c9255ee2b82d1cf06996d8176e94a324e096b3a` |
| `ChineseRemainder/PrimaryCompletions.lean` | `7f110a463e288c602fac99699d938f3744bbe198cf282e8b4ff67b5343e794bc` |
| `RowCompletion/PeriodicRows.lean` | `7306d53cc2364f05c53923d9db94cac9f28ab1a754fa0130c49b813dc69e7c8f` |
| `Arithmetic/EisensteinEmbedding.lean` | `ce0a59ae784c27a535e465b0cc6a112bef83435b66c3a9bcb274ac05dbb4febe` |
| `PrimeRows/IdealGenerators.lean` | `3c934cf47286a751655cc5aff2def2793e760f703c0cfd5048a0ed33ae69a533` |
| `GaussSum/LocalProductAssembly.lean` | `cda1a20b78d89a7d5c8c91ecae5f8ab2ee1d695d9a23394d3297404d63707d09` |
| `QuadraticSieve/DivisorBlocks.lean` | `48be5e32c0a93e4db774fb62cd825cba57c02074ed646a5bd8dbab81968d3f60` |
| `Fourier/TupleWeights.lean` | `3bf8c7fdf4ede391645c6244f113aa752c8b38831a843869dcc03afa1619840b` |
| `CubicSieve/RowCaps.lean` | `1ffb8b680360de85a1d968c7147aed82866a5f2547d375429f41c47a8eefd707` |
| `GaussSum/FiniteFourier.lean` | `0e8e4184de91161a75802e3a26abfd19a322dffa6441968bf9caeb25800b5d7c` |
| `Hecke/InverseAmplificationFamily.lean` | `9d1af7a50e0dcdda149b234c790aea46581a971ebb54f46881086ee986a097f4` |
| `Hecke/InverseAmplificationMask.lean` | `54f61f71149f0d32b6fd9ad5a285197b2a329494d5460e3e4c8c18b638dc4d47` |

The two amplification files were read from the separate source bundle and
also verified against the preserved manifest. The O5 source hash remains `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
