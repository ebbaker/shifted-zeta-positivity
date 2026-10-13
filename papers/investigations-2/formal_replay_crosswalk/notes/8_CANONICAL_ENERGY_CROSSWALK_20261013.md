# Canonical-energy crosswalk: U4 source pass

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration; exact serving variant
and reasoning effort are not exposed and are not inferred. Source analysis
and same-family parallel checks are not independent mathematical validation.

**Conclusion.** The pinned Lean source supplies a concrete conditional
paper-level route to October 5's canonical-energy estimate. Its column
polynomial, full element-row support and central normalization match under
the arithmetic dictionary in [notes 2](2_ARITHMETIC_APPLICATION_CROSSWALK_20261012.md)
and [7](7_FIXED_CHARACTER_ROW_DICTIONARY_SOURCE_PASS_20261013.md). The dyadic
label endpoint requires a factor four, unit label weights must be dominated
by the ninth-power divisor weight, and arbitrary original exclusions need
finite fixed-prime restoration. A fixed reference annulus makes the smooth
derivative order precede every support interval and fixed arithmetic input.
The new combined application has **not been compiled**. This is a source
crosswalk with explicit remaining proof terms, not formal closure of U4.

All source references use `openai/math` at
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. The
[small source-contract record](../numerics/canonical_energy_crosswalk_20261013.json)
identifies the inspected files and anchors. The preserved closure manifest
binds 2,926 OAI modules; all 2,926 copied source files were checked for byte
count, SHA-256 and Git blob SHA-1. The October 5 source SHA-256 is
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`;
September 30 is
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
Third-party trees and full manifests remain external. Source identity does
not verify proofs. No VM mutation or new mathematical compilation was used
for this source pass; the separately recorded comparator replay concerns
its nominated universal targets.

## 1. The target and its quantifiers

Write `H` for the paper's `mathcal H`, and `Z` for its physical outer `D`.
The [O5 energy definition](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex#L938-L953) is

\[
 E_S(H,X,F;\xi,W)=\frac1{XF}
 \sum_{\substack{f\ \mathrm{squarefree},\ (f,S)=1\\F\le Nf<2F}}
 \sum_{0<Nk\le H}
 \left|\sum_{\substack{n\ \mathrm{squarefree}\\(n,S)=1}}
 a_0(n)\xi(n)\chi_n(k)\chi_n(f)^4W(Nn/X)\right|^2,
 \qquad a_0(n)=\overline{\alpha(n)}\gamma_2(n).
\]

Both starred variables are nonzero ideals represented once by primary
generators. Rows are **all nonzero Eisenstein elements**, including their
six unit associates and arbitrary prime powers. There is no division by
six. The moving fourth-power label is `f`; U1's terminal specialization
`f=1` cannot replace this label family.

[O5 Proposition `prop:canonical`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex#L1260-L1277) asks, for fixed
`kappa>0`, `C0>=1` and every `epsilon>0`, for an integer
`k=k(kappa,C0,epsilon)>=1` such that

\[
 H,X,F\ge1,\quad \Sigma=XF\le Z^{C_0},\quad H\le\Sigma Z^{-\kappa}
 \quad\Longrightarrow\quad
 E_S\ll_{I,\nu,S,\kappa,C_0,\epsilon}
 \|W\|_{C^k(I)}^2 Z^\epsilon\Sigma.
\]

The integer precedes arbitrary compact positive intervals `I` and weights
supported there. Constants may depend on the fixed ray data and `I`.
The paper's preceding physical-scale convention is `Z>=2`; the argument
below also handles bounded `Z>=1` separately. It does not take logarithms
at `Z=1`.

O5 chooses one finite ray class group, with modulus supported on `S`,
through which `nu` and the fixed residue factors pass
([coefficient and modulus](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex#L794-L818)). Its finitely many `xi` may be
handled individually and their constants maximized. We assume a genuine
`HeckeFamily.Character eta_xi` presenting each supplied `xi`, unit triviality,
and agreement on the original `S`-coprime columns, with original defining
modulus zeros retained. This is the conditional classical-to-residue input
specified in note 7. Replacing it by a primitive character after dropping
imprimitive zeros would alter the target.

## 2. Exact canonical rank contract

The [September 30 canonical marked lemma](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L9296-L9349) is the intermediate paper contract: it uses a row exponent `M`, column exponent `N`, label exponent `V`, `F0=N+V`, a fixed zero-extended character, a fixed puncture, and bounded prime-slot marks. Its central column factor `Z^(-N/2)` and outer factor `Z^(-V)` together give `1/Z^(N+V)` after squaring. With no slots and unit puncture, its two displayed margins reduce to `cstar<=F0-M` and `cstar<=4F0-3M`. Its nonnegative label weight depends only on the label and is divisor bounded. The exact Lean predicate below supplies these margins, a concrete divisor weight, complete-pool and mode uniformity; it is read directly rather than inferred from the paper lemma's name.

The entry point is
[`canonical_marked_energy_exists`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/CanonicalRankExistence.lean#L32-L38).
For nonnegative `Mcap,Fcap`, positive `c,eps`, slot cap `K`, and one Schwartz
profile supported in a positive compact interval, it proves

`CanonicalEnergyExists Mcap Fcap c eps (Fcap+1) K W`.

Unfolding [the existence predicate](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/CanonicalEnergyExistenceData.lean#L13-L26)
gives the order

\[
 \exists J\in\mathbb N\;\exists B\ge1\;
 \forall q\in\mathbb N\setminus\{0\}\;
 \exists C>0\;\exists Z_0>1\;
 \forall Z\ge Z_0\;\forall P_{\rm cap}\in\mathbb N,
 \quad BZ^{F_{\rm cap}+1}\le P_{\rm cap}\;\Longrightarrow\cdots.
\]

The mode degree `J` and `B` precede `q`; `C,Z0` precede the natural pool cap,
slot data, admissible bases, labels, moving scales and Fourier mode.
`Pcap` is the source's natural parameter named `D`. It is **different
from O5's physical `D=Z`**. The pool is the complete squarefree ideal family
outside `S_q=reflectionExcludedPrimes q` up to `Pcap`, its prime-index subtype
and `poolPrimary` generators
([complete-pool predicate](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/CanonicalRankExistenceData.lean#L15-L25)).
It is permissible to enlarge `Pcap` without changing `C`.

The [rank moment predicate](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/CanonicalRankMoments.lean#L19-L30)
requires nonnegative `N,V,M,Qwidth`, `M<=Mcap`, `N+V<=Fcap`, and

\[
 c\le N+V-M-Qwidth-z,\qquad
 c\le4(N+V)-3M-6z.
\]

These are exactly [the canonical margins](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/Basic.lean#L13-L14).
The puncture has norm square `Z^Qwidth`; labels need only be
`CanonicalQuadraticSieve.Admissible` and have norm at most `Z^V`.
**Labels are not required to be coprime to `q` or to belong to the column
pool.** The conclusion bounds `normalizedColumnEnergy` on the full row
ball of radius `Z^M`, with `secondLabelWeight K` and `childLogTest W s`, by

\[
 C Z^{N+V+\epsilon}(1+|s|)^{2J}.
\]

For the intended no-mark application take `K=0`, type `Fin 0`, empty slots
and subslots, `z=0`, `m=1`, `Qwidth=0`, and `Psi=base`. All disjointness and
slot estimates are vacuous; the empty norm product is `1=Z^0`.
[`primeMark_empty`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/Marks.lean#L18-L24) is exactly one.
`IsBaseRayTwist base base` follows from the left alternative in
[its definition](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Eisenstein/CoordinateLaplacian.lean#L448-L449).
An arbitrary varying multiplicative phase is not justified by this step.

## 3. Column equality and full row support

For the moment suppose the fixed pool excludes exactly `S` and
`Pcap>=hi*X`, where `W` is supported below `hi`. Put
`Psi=HeckeRowClosure.elementHom eta_xi`. The finite marked row is the
powerset polynomial with summand

\[
 \operatorname{columnCoefficient}(U)\Psi(\textstyle\prod_{i\in U}p_i)
 \operatorname{rowCoprimeMask}(U,m)
 \chi_U(f)^4\chi_U(k)W(N(U)/X).
\]

See [the definition and actual-column equality](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/Canonical.lean#L16-L39)
and [the actual summand](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/CubicSieve/FirstPassage.lean#L544-L549).
At `m=1` the moving mask is one. Fixed exclusions remain in the pool.
`columnWeight` uses the squarefree coefficient
`star(angularFactor(primaryGenerator I))*gaussTwo I`
([ideal coefficient](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Arithmetic/IdealMobius.lean#L419-L434),
[Gauss product identity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/GaussSum/CompletedExpansion.lean#L329-L352)).
The trace and lambda transport in note 2 remains part of the dictionary;
we do not equate its additive characters merely from their names.

[`finiteCanonicalMarkedRow_complete_global`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/CompleteMarkedPool.lean#L40-L54)
identifies this with the global ideal sum at the exact fixed exclusions,
provided `hi*X<=Pcap`. At empty marks it is precisely the O5 inner sum
under the stated character and Gauss dictionaries. Its `excludedGenerator S`
sixth-power factor imposes the `S` mask, including unsupported-column zeros.
[`marked_weighted_column_tsum_eq`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/CompletePool.lean#L49-L61)
and [`selectedIdealTest_outside`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/MeanSquare/OutsideIdeals.lean#L139-L159)
show that adding an ambient pool beyond the weight support adds only zero
terms. There is no pool-cardinality loss.

[`nonzeroChildFrequencyBall`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/ChildCutoff.lean#L30-L42)
has exactly `k!=0` and `N(k)<=H`. A label generator change by a unit
reindexes rows by `k -> u^4 k`; this is a bijection of the full ball
([generator transport](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/GeneratorTransport.lean#L41-L46),
[energy equality](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/CanonicalLongNormalization.lean#L40-L57)).
It supplies no factor of six. The
[complete normalized generator-sum theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/CanonicalCompleteNormalized.lean#L15-L62)
is the available exact transport if an arbitrary ideal generator is used.

## 4. Normalizer, label weight and dyadic endpoint

[`normalizedColumnEnergy`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Inversion/InitialClippedColumns.lean#L199-L229)
puts **one** scalar `Z^(-(N+V)/2)` inside each norm square. Thus at
`X=Z^N`, `F=Z^V`, exact target label and row sets, empty marks and weight one,

\[
 E_S(H,X,F;\xi,W)=\operatorname{normalizedColumnEnergy}(\ldots,1,W,X,Z,N+V).
\]

This is the exact normalization identity before requesting a rank bound.
For the bound, dyadic labels extend to `<2F`, so use instead

\[
 V_+=\log_Z(2F),\qquad F_0=N+V_+=\log_Z(2XF).
\]

The same numerator then has normalizer `1/(2XF)`. Consequently
`E_S=2 E_Lean(unit weight)`. The source RHS at this exponent is
`C*2XF*Z^eps`, so the resulting target bound costs **four**, not two:

\[
 E_S\le4C\Sigma Z^\epsilon
\]

before smooth-profile factors. Both appearances of two are constants;
there is no epsilon loss. Source
[`normalization_change` and `initial_child_from_rank`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Inversion/InitialCanonicalEnergy.lean#L18-L77)
already express the corresponding enlarged-exponent transport.

Even at `K=0`, [the source label weight](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/SecondNormalizedEnergy.lean#L35)
is `card(idealDivisors f)^9`, not one. For every nonzero label its divisor
set contains the unit ideal by
[`mem_idealDivisors`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Arithmetic/IdealMobius.lean#L76-L88), so its
weight is at least one. The source
[`energy_range_weight_le`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Inversion/InitialCanonicalEnergy.lean#L33-L45)
therefore drops this nonnegative weight to one without a divisor estimate,
label-cardinality penalty or additional epsilon. The exact target label
set is the finite ideal norm range up to `2F`, filtered by squarefreeness,
`S`-coprimality and `F<=Nf<2F`.

[O5's fixed exclusions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex#L665-L670) include the primes above two and three. These imply
`CanonicalQuadraticSieve.Admissible` for its squarefree labels
([definition](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/QuadraticSieve/CoprimeBilinearBound.lean#L522-L524),
[outside-ideal admissibility](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/MeanSquare/OutsideIdeals.lean#L104-L118)).
The differently defined `CubicSieve.Admissible` used in Gauss coefficient
lemmas is not identified with this predicate by name; the corresponding
squarefree and nonzero-primary hypotheses must be transported separately.

## 5. Rational period and restoration of extra excluded primes

The existence theorem's exclusions are the prime ideals dividing `(2592q)`
([definition](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Cusp/StaticReflectionPhases.lean#L140-L143),
[`excluded_mem_iff`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Inversion/InitialExcludedPeriod.lean#L41-L50)).
Its base must factor modulo `(4q)`
([fixed conductor](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Eisenstein/CoordinateLaplacian.lean#L611-L622)).
A rational period can exclude both ideals above a split rational prime.
O5's specified `S` may contain only one. One cannot remove nonzero columns
inside a complex sum by a monotonicity claim.

Given the residue presentation above, a concrete choice is

\[
 q=\eta_\xi.\operatorname{period}\prod_{P\in S}N(P)>0.
\]

`Character.period_pos` and `period_mem` are
[fields of the genuine character](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/Family.lean#L22-L29).
`Ideal.absNorm_mem P` puts `N(P)` in each nonzero prime `P`; source uses
appear in [LocalEulerIdentities](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/LocalEulerIdentities.lean#L110-L118)
and [NormFiberCharacters](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/NormFiberCharacters.lean#L133-L135).
Hence `(4q)` is contained in `eta_xi.modulus`, and every `P in S` divides
`(2592q)`. The original element character has norm at most one and is
periodic modulo its defining modulus
([row character](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/RowClosure.lean#L86-L96)), so it satisfies the
base-period hypothesis for this `q`. Use this **original character** as
base; no extra arbitrary `S` mask is inserted into the character.
The column pool and the restoration below impose the original exclusions.
These period/enlargement terms remain uncompiled.

Put `T=S_q minus S`. It is fixed and finite. Split each original squarefree
column uniquely as `n=delta*j`, where `delta` is a product of a subset of
`T` and `j` lies outside `S_q`. There are `b=2^|T|` possible factors.
With all generators primary, the exact source CRT law is

\[
 a_0(j\delta)=a_0(j)a_0(\delta)\chi_j(\delta)^4,
\]

from
[`columnCoefficient_union_row_four`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Mellin/UniformKernelBounds.lean#L618-L637).
It requires disjoint squarefree prime sets, good primary generators and
`lambda^2 | p-1`. Retain those hypotheses. It gives the coefficientwise
finite decomposition

\[
 C_S(W;X,f,k)=
 \sum_{\delta\mid\prod T}
 a_0(\delta)\xi(\delta)\chi_\delta(k)\chi_\delta(f)^4
 C_{S_q}(W;X/N\delta,\delta f,k).
\]

Here `C` is the unnormalized inner column sum. The fourth-power CRT factor
combines with `chi_j(f)^4` into `chi_j(delta*f)^4`; it is not an arbitrary
bounded residual weight. Character multiplication and all zero extensions
are retained. The outside scalar has norm at most one, by
[the coefficient norm bound](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/CubicSieve/FirstPassage.lean#L378-L389)
and the character and sextic norm bounds.

If `delta` and `f` share a prime, `chi_delta(f)^4=0` and the entire branch
vanishes. For surviving labels, `f'=delta*f` is nonzero, squarefree and
avoids the bad primes, so it is admissible. The source uses precisely this
product-squarefreeness pattern in
[InitialPoissonBridge](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Inversion/InitialPoissonBridge.lean#L190-L195).
Multiplication by nonzero `delta` is injective on nonzero ideals
([source cancellation use](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Inversion/InitialOverlap.lean#L38-L40)).
The image label set therefore has no multiplicity weight and satisfies

\[
 N\delta\,F\le Nf'<2N\delta\,F,\qquad
 X'=X/N\delta,\quad F'=N\delta\,F,\quad X'F'=\Sigma.
\]

These image labels can contain primes from `S_q`, which the rank predicate
explicitly allows. The row set and its scale `H` are unchanged.
Cauchy--Schwarz gives a factor `b` followed by the sum of these branch
energies. Both the number and norms of the possible `delta` depend only
on fixed arithmetic data, never on moving scales. Thus the restoration
preserves the target constant dependencies.

This is an explicit assembled argument, not a located one-line restoration
theorem. O5's [`remove-exclusions` lemma](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex#L962-L996) bounds an
additionally deleted sum in terms of the original family; that direction
does not by itself restore columns removed by `S_q`.

## 6. Fixed annulus and the derivative-order quantifier

Applying `canonical_marked_energy_exists` separately to each arbitrary `W`
or support interval would allow its degree to depend on the input.
Instead choose once a smooth reference `R`, equal to one on `[1/2,2]`
and supported in `[1/4,3]`. The positive cutoff construction is available
in [SecondChildWindows](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Inversion/SecondChildWindows.lean#L14-L34).
Invoke the existence theorem only for this fixed `R`, with

\[
 M_{\rm cap}=C_0,\quad F_{\rm cap}=C_0+1,\quad
 c=\kappa/2,\quad \mathrm{eps}=\epsilon,\quad K=0.
\]

It chooses `J,B` before `q`, before `I` and before the target weight.
For every smooth `V` supported on `[1/2,2]`,
[`canonical_clipped_energy`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/ClippedEnergy.lean#L35-L86)
with `c_dilation=1`, `theta=0`, nonnegative label weights and fresh profile
`R` gives exactly

\[
 E_{\rm Lean}(V)\le C Z^{F_0+\epsilon}\mathcal B_J(V)^2,
 \quad
 \mathcal B_J(V)=\int_{\mathbb R}(1+|t|)^J
       |\widehat{\,u\mapsto V(e^u)\,}(t)|\,dt.
\]

Its reconstruction identity is
[`canonical_clipped_fourier`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Descent/ClippedFourier.lean#L91-L119).
The bound is homogeneous and quadratic; it has no additive `1+||V||` term.
On this fixed annulus, integration by parts through order `J+2` gives

\[
 \mathcal B_J(V)\le K_J M_{J+2}(V),\qquad
 M_k(V)=\max_{0\le r\le k}\sup_y|V^{(r)}(y)|.
\]

For `|t|<=1` use the compact-support L1 bound; above one the integrand
is bounded by a constant times `|t|^-2` after `J+2` derivatives. The chain
rule between ordinary and logarithmic derivatives has fixed annulus
constants. Note 5 supplies this argument and the alternative source
Fourier estimate in
[LogProfiles](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Mellin/LogProfiles.lean#L1123-L1186).
Its ordinary-derivative conversion is still a new application obligation.
Take `k=J+2>=1`; it depends only on `kappa,C0,epsilon` and fixed reference
choices, not on `I`, `S`, `nu`, `xi` or `q`.

For arbitrary positive compact `I`, fix a smooth dyadic partition `psi`
supported in `[1/2,2]` with `sum_j psi(2^-j*y)=1` on positive `y`.
Only finitely many `a_j=2^j` meet `I`. Set

\[
 V_j(y)=\psi(y)W(a_j y),\qquad
 C_S(W;X,f,k)=\sum_j C_S(V_j;a_jX,f,k).
\]

The column identity is exact and unnormalized. For the same chosen `k`,
`M_k(V_j)<=B_(psi,k)*max(1,a_j)^k*M_k(W)` by Leibniz and the chain rule.
The finite partition and its constants depend on `I`; its derivative
order does not. Extension of a smooth weight supported in `I` by zero is
understood as the paper's globally smooth compactly supported weight.

## 7. Moving-scale application after restoration and dilation

For each of the finitely many pairs `(j,delta)`, write `Delta=N(delta)`,

\[
 X_{j,\delta}=a_jX/\Delta,\qquad F_\delta=\Delta F,
 \qquad \Sigma_j=X_{j,\delta}F_\delta=a_j\Sigma.
\]

First suppose `X_(j,delta)>=1`. For sufficiently large fixed `Z`, choose

\[
 N=\log_Z X_{j,\delta},\quad V=\log_Z(2F_\delta),\quad
 M=\log_Z H,\quad F_0=N+V=\log_Z(2a_j\Sigma).
\]

All exponents are nonnegative. Enlarge the fixed threshold so, for every
partition scale, `2a_j<=Z` and `2a_j Z^(kappa/2)>=1`. Then

\[
 M\le C_0,\quad F_0\le C_0+1,\quad
 F_0-M\ge\kappa+\log_Z(2a_j)\ge\kappa/2,
\]

and `4F0-3M=M+4(F0-M)>=2kappa>=kappa/2`. Thus both canonical margins
hold at `Qwidth=z=0`. The fixed restoration factor cancels from `F0`.
Choose a natural pool cap at least

\[
 \left\lceil\max\left(BZ^{C_0+2},\;
 3\max_{j,\delta} X_{j,\delta}\right)\right\rceil_+.
\]

The factor three covers the reference support as well as `[1/2,2]`.
The existence contract is uniform in this pool cap. It bounds every mode
of `R`, and the clipped Fourier transfer bounds the weighted energy of
`V_j`; weight domination then gives the target branch with normalizer
`1/(X_(j,delta)*F_delta)`:

\[
 E_{j,\delta}\le4C a_j\Sigma Z^\epsilon K_J^2M_k(V_j)^2.
\]

The **original** outer energy has normalizer `1/Sigma`, rather than
`1/(a_j Sigma)`, so each branch pays one further `a_j`. Its contribution
is therefore bounded by `4C a_j^2 Sigma Z^epsilon K_J^2 M_k(V_j)^2`.
Finite Cauchy--Schwarz in the partition and restoration indices costs
only constants depending on `I` and fixed arithmetic data. No power of
`Z` is spent on these finite decompositions.

### Shifted columns below one

If `0<X_(j,delta)<1`, do not apply the rank predicate with negative `N`.
Use **unit label weights** directly. All actual column coefficients have
norm at most one. For support below `hi`,
[`norm_tsum_ideal_ball`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Moments/Counting.lean#L12-L49)
bounds the column amplitude by
`128*max(1,hi)*X_(j,delta)*M0(V_j)` for every positive column scale;
if the ideal norm cap is below one the support is empty.
The label image has at most `128*(2F_delta)` members by
[finite ideal counting](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Mellin/InverseContour.lean#L306-L320),
and the full element-row ball has at most `128*H` members by
[finite element counting](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/QuadraticSieve/GreenIntegrals.lean#L246-L261).
Squaring the amplitude and retaining both counting constants gives

\[
 E_{j,\delta}\le
 2\cdot128^4\max(1,hi)^2 H X_{j,\delta}M_0(V_j)^2.
\]

Since `X_(j,delta)<1` and `H<=Sigma Z^-kappa`, returning to the original
normalizer multiplies by `a_j` and gives at most a fixed constant times
`a_j Sigma Z^-kappa M0(V_j)^2`. This is within the desired
`Sigma Z^epsilon M_k(W)^2` bound. Here `hi=2` is fixed. No divisor-weight
upper bound is needed or claimed for this small-column calculation.

### Bounded outer scales

All previous thresholds depend only on the allowed fixed data. For
`1<=Z<=Z_*`, use the original unit-weight sum: amplitude
`<=128*max(1,hi_I)*X*M0(W)`, labels `<=256F`, rows `<=128H`.
Hence `E_S<=const_I H X M0(W)^2`. Since `X<=Sigma`, `H<=Z_*^C0`
and `Z^epsilon>=1`, this is `<=const_(I,Z_*) Sigma Z^epsilon M_k(W)^2`.
This also handles `Z=1` without logarithms.

Together these arguments give the conditional paper-level estimate in
section 1 with the required derivative-order quantifier.

## 8. Status and next formalization boundary

| Link | Source-pass classification | Remaining new application |
| --- | --- | --- |
| O5 coefficient and sextic orientation | Conditional exact dictionary from notes 2 and 7 | Supply the genuine input character and compile its coefficient agreement, including zeros and trace transport |
| Complete polynomial, ideal labels, full element rows | Exact source identities with support-sized pool | Instantiate finite/global transport for the target label set |
| Central normalizer and `<2F` label endpoint | Exact equality plus explicit factor four | Compile enlarged exponent and unit-weight domination |
| Arbitrary fixed `S` versus rational `S_q` | Explicit finite CRT restoration preserving `XF` | Compile primary-factor decomposition, label image/cancellation, zero branches and Cauchy--Schwarz |
| Uniform quadratic smooth-weight dependence | Exact canonical Fourier transfer plus fixed-annulus argument | Compile partition, ordinary/log derivatives, and seminorm conversion |
| Positive gaps, polynomial caps, shifted/bounded scales | Explicit paper-level substitutions above | Compile logarithmic exponent arithmetic and direct counting branches |

The source pass finds no missing counterpart for this conditional U4
route. It does not replace the paper's compressed transfer proof or
certify U5--U7; those remain separate crosswalk tasks. Successful replay
of a universal zeta, Dirichlet or Hecke target does not compile these new
O5 applications. A next formalization step should implement the exact
unit-weight, dyadic-label specialization first, then restoration and the
fixed-annulus profile conversion, in a separate application module without
changing the pinned upstream source or active replay.

The [same-family scope review](../reviews/CANONICAL_ENERGY_SOURCE_SCOPE_REVIEW_20261013.md)
records the checks and any corrections. A Claude or external mathematical
review remains useful before treating this source route as settled.
