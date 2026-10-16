# Mixed fourth estimate: squarepart removal and the smooth obstruction

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
reasoning effort are not exposed and are not inferred. The parallel
reviews are same-model internal audits, not independent specialist review
or formal proof verification.

The next estimate following [Note 24](../mixed_character_families/notes/24_ADAPTIVE_COFACTOR_AND_DYADIC_KERNEL_20261009.md)
removes another sector of the original selected moment, including its
complete interaction with the remaining inverse. It also identifies a
rigorous obstruction to a broader proposed smooth estimate. Both results
are incorporated in [Note 25](../mixed_character_families/notes/25_SQUAREPART_REMOVAL_AND_SMOOTH_OBSTRUCTION_20261009.md)
and the same [stable manuscript](../mixed_character_families/mixed_character_reductions.tex).
The selected mixed fourth theorem with saving 1/700 remains unproved.

## New estimate and its scope

Write the exact truncated coefficient as
\(c_Z(g^2h)=\mu_F(h)d_{Z/\mathrm Ng}(h)\), with squarefree coprime
\(g,h\). This \(g\) is the common factor of the two truncated inverse
factors; it is distinct from the gcd of an original inverse pair or of
two full marked columns. Retain the original profiles, factor caps,
product cut, annulus, slots, selected weight and physical zeros.

Choose \(G=U^{(1-d)r/2+1/250}\). An absolute three-factor ideal count
bounds the part \(H_G\) with \(\mathrm Ng\ge G\) by
\(D^{1/2}G^{-1}U^\varepsilon\) on every row. The imported selected
fourth-mass bound and full inverse envelope then give:

| Deduction | Guaranteed saving relative to \(U^{1+dr}\) |
| --- | --- |
| Selected square of \(H_G\) | 1/125 |
| Complete difference after removing \(H_G\) | \(1/250-6re_{\rm src}\ge79927/20000000\) |
| Adaptive short-cofactor and common-factor removals together | 7979/2000000 |
| Combined reserve over the remaining 1/700 target | 35853/14000000 |

The cross estimate uses
\(|F_*-F_\dagger|\le2\sqrt{F_*F_G}+F_G\), rather than discarding
ordered cross terms. The source buffer remains capped at 1/1200000;
literal source, witness, profile and height costs retain their separate
budgets. The residual coefficient keeps \(\mathrm Ng<G\),
\((\mathrm Ng)^2\mathrm Nh>U^{r/2-1/4}\), both inverse-factor caps
and the arbitrary plain quotient. Its signed squarefree core
\(\mu_F(h)\) remains. Under those assumptions the smaller selected
target is equivalent, at the required exponent, to the original target.

The legal transferred sixth-order sieve supplies
\(L\Theta_6(U,AB)U^\varepsilon\) for an unweighted factor block.
After the baseline selected plain/slot envelope, its best endpoint
still misses the required exponent by at least 5423/52500. This is an
upper estimate, not the missing cancellation theorem. The coefficient
proof applies directly after imposing the residual gcd cut; a signed
block norm cannot be compared by positivity with its unsliced version.

## The broader smooth target fails in a specified class

The obstruction requires an actually admitted principal native/fixed-ray
presentation and inverse/plain profiles with nonzero principal means.
The zero-slot instance suffices. A full positive smooth row envelope
then includes auxiliary rows \(u=p^6\), whose character is the
coprimality indicator. These rows are excluded from the original
sixth-power-free, nonprincipal, high-conductor selected family.

For the unpunctured principal polynomial, elementary ideal counting
gives a short-cofactor main term involving
\(\sum_{\mathrm Nt\le U^{\alpha_*}}(\mu_F*\mu_F)(t)/\mathrm Nt\),
where \(\alpha_*=r/2-1/4\). Its Mellin transform has two distinct
zeta arguments. A hypothetical bound below
\(E_{\rm crit}=(r-\alpha_*)/2\) would force each zero \(\rho\)
with real part at least 1/2 to have a canceling zero at
\(1+(\alpha_*/r)(\rho-1)\). Iteration would produce zeros tending
to the isolated simple pole at one, a contradiction. The counting error
has Mellin transform holomorphic for \(\Re s>\alpha_*/2\), covering
every pole used in this argument. Profile numerator zeros cannot create
a canceling pole.

Prime-sixth rows transfer this oscillation uniformly: the deletion error
has exponent smaller by at least 131/1200. Along arbitrarily large
scales, their positive norm has exponent arbitrarily close to
\(E_{\rm low}=5/12+r/2+2m\). This exceeds the proposed exponent
\(1+dr-1/700\) by at least 1439/5250. The removed common-factor
amplitude is smaller than the principal obstruction by at least
157/1000, so the obstruction also applies to the residual polynomial.
Conditional on the imported smooth row-Poisson formula, the first zero
is too small to account for this contribution; the complete nonzero
first-frequency aggregate also fails the proposed bound in this class.

This is an oscillation along a sequence, not an all-scale lower bound.
It disproves the uniform unrestricted, uncentered all-row class theorem
covering this instance. It does not disprove the original selected
target, a genuinely nonprincipal fixed-ray version, arbitrary signed
slots, or a separately justified centered comparison.

The standard zeta and Dirichlet analytic facts were checked in the
primary [DLMF 25.10](https://dlmf.nist.gov/25.10) and
[DLMF 25.15](https://dlmf.nist.gov/25.15). The quadratic-field
factorization follows from its splitting Euler factors. A parallel
reviewer checked fixed-ray prime counting in
[Pollack–Troupe, Theorem 2.1, printed p. 4](https://www.pollack-math.net/irreddiv-bams.pdf).
The sieve formula and its scope were checked against
[de Faveri, Theorem 1.1](https://arxiv.org/html/2610.04045v1);
its native transfer retains its imported status. These source checks do
not replay the deep analytic input proofs. No third-party PDF was saved.

The exact sixth-power-free row mask is retained as a signed divisor sum.
Absolute summation restores the unwanted principal rows. A genuinely
smaller power cutoff has an inadequate crude tail bound; the full finite
cutoff has zero tail but leaves its entire signed aggregate to estimate.
The additional high primitive-conductor restriction is nonradial.

## Audits and verification

Three parallel read-only audits checked the common-factor split,
normalizers, complete Cauchy estimate, continuous rational budgets,
legal sieve application, principal Mellin continuation and pole
iteration, uniform prime deletion, and the exact row-mask interface.
Their scope corrections were incorporated: physical row radius in the
sieve sum, fixed annular constants in the length exponent, a direct
residual coefficient proof, dropping the nonnegative slot envelope in
the lower comparison, explicit oscillation quantifiers, and the full
finite-cutoff exception. No required mathematical correction remains
within the stated scope.

The new [checker](../numerics/check_mixed_squarepart_estimate.py) and
[record](../numerics/mixed_squarepart_estimate_record_20261009.json)
contain **725,761 exact assertions**. They test the literal split by
inverse-factor common part with both caps, finite complex profiles,
selected weights, both finite character orientations, physical zeros, original normalization,
complete ordered cross terms, sixth-power-free divisor projectors
through valuation twelve, and rational saving formulas. Formal rational
complex pole-map iterations test the affine scaling only; those points
are not asserted to be zeta zeros.

Two fresh checker runs were byte-identical, and a coordinating replay
matched the saved record. The record binds both checker and read-only
dependency hashes. Finite checks do not prove Mellin continuation,
the analytic obstruction, a derivative-uniform mixed moment, native
Poisson, selected bin populations or detector coverage.

Static checks passed: 224 unique labels, 158 references with existing
targets, 23 bibliography keys with resolved citations, balanced
environments and actual math control delimiters, and no external input,
image or bibliography dependency. The final standalone source compiled
successfully with the desktop editor's compiler. No exported PDF or
independent rendered-layout audit is claimed. Local note/index links
and whitespace checks passed.

Final manuscript: 193,667 bytes, 3,844 lines.
SHA-256: `76c95befc29059809197137cc8e5a83dfeef69307064a4e71bfa4c7a13f006c5`.
Checker SHA-256: `88086a0ac402de588587d6d46553dac3206a2880940e7a61f468d70f15c10e14`.
Record SHA-256: `d502669c675a2a0755210d94738a83c4a570bad7fc109d77a882f0f8a110eeff`.
The stable source and repository indexes were updated in place,
preserving existing working-tree material. No commit, tag or draft
snapshot was created.

The next proof obligation is the selected small-common-factor signed
correlation with its actual row restrictions, or a proved signed-mask
or centered comparison that preserves those restrictions. The new
controlled sector and smooth obstruction establish no full mixed
fourth theorem, boundary reuse or stronger zero-free strip.
