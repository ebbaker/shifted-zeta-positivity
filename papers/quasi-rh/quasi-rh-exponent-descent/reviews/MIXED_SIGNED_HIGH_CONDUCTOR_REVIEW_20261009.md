# Review of signed support and conductor reductions

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
reasoning effort are not exposed and are not inferred. Three parallel
same-model derivations and audits are internal checks, not independent
specialist review or formal proof verification.

[Note 28](../mixed_character_families/notes/28_SIGNED_HIGH_CONDUCTOR_SUPPORT_AND_DEFECT_20261009.md)
continues the signed high-conductor estimate from
[Note 27](../mixed_character_families/notes/27_CENTERED_AUXILIARY_CONTROL_AND_SIGNED_REMAINDER_20261009.md).
Two additional sectors are controlled under the stated inputs, and their
complement is an exact real signed finishing theorem. The full centered
mixed estimate remains open. The deductions are incorporated into the
existing [manuscript](../mixed_character_families/mixed_character_reductions.tex),
section “Further signed support and auxiliary conductor reductions.”

## Controlled sectors and the remaining estimate

| Result | Scope and hypotheses | Saving and reserve |
| --- | --- | --- |
| Small exclusive full column support | Original centered coefficient and inverse, common physical kernel, divisor bound, elementary fixed-support ideal count and physical row count | With B_all=U^(dr−1/500), saving 1/500; reserve 1/1750 over 1/700 |
| Direct selected variant | Same pair identity and imported selected count U^R; B_sel=U^(1+dr−1/500−R) | Same saving; retains the sharp bin exactly |
| Auxiliary conductor extension | Original disjoint slots, marked inverse coefficient norm, native arbitrary-coefficient sixth-order sieve transfer, global premise β*≤7/8, actual squarefree core radius | Defect η≤3/20 and κ≤κ_sf−η/10; saving 11/6250, reserve 29/87500 after the literal v cost |
| Exact residual | Nonprincipal rows above κ1 outside the new defect frontier, both exclusive full column norms above B_all | Required real one-sided saving 1/700 is **unproved** |

The pair count controls all same-radical pairs, including different
valuations with nonprincipal sextic quotient. For k=p²q and k′=pq²,
the exclusive full column parts are both the unit; ordinary gcd quotients
would give p and q. Rankin's bound with fixed positive parameters proves
the uniform supported-ideal count, for all column powers in the original
coefficient. The pair sector is real but need not be positive.
Its absolute bound uses at most X B U^ε pairs and the row mass, with
the original X^−1 normalizer. No inverse pointwise bound is needed.

The auxiliary sieve uses only the marked inverse columns. Each has
valuation at most two, since the inverse is squarefree and the original
prime slots are disjoint. For u=a₁h w⁶, fixed h,w enter a bounded column
multiplier, retaining physical zeros. The row radius is Na₁=U^α with
α=κ−λ. Counting the frozen labels gives the exact extra mass
cost η/6, where η=Σ_(e=2)^5(5−e)log_U Na_e.

The frontier κ≤κ_sf−η/10 pays that cost because
(5/3)(−η/10)+η/6=0. Its uniform lower endpoint is
κ_D=κ_sf−3/200, improving κ1 by at least 2029/56250.
The actual core radius remains inside the dominant sieve branch,
with limiting lower margin 121/3600 and upper margin 11/5000.
A fresh fixed 0<v≤1/5000 costs at most 3/12500.
Source height degrees remain finite and symbolic; their conversion and
other fixed losses must fit within the printed reserve 29/87500.
Annular O(1/log U) endpoint errors cost constants and preserve the
strict branch margins for sufficiently large U.

This cutoff is below the original selected high-conductor gate.
It improves the auxiliary row problem. The direct selected pair removal
is a separate route and does not require the defect estimate.
Earlier inverse-variable gcd and cofactor cuts are different predicates;
any joint removal requires exact set differences or a tuple identity.

## Analytic audits and retained inputs

The [primary de Faveri theorem](https://arxiv.org/html/2610.04045v1)
was checked directly: its n=6 factor is
Θ₆(A,L)=A+L+A^(5/6)L^(1/3)+A^(1/3)L^(5/6).
Its fixed native presentation transfer remains the explicit imported
input in the manuscript. Growing h,w masks are in the arbitrary
coefficient vector; no new growing-twist theorem is asserted.
Global growth, deleted Euler factors and the specialized scalar bound
retain Note 27's source qualifications. No third-party PDF is retained.

The same-model analytic audits passed after clarifying the actual row
radius, naming the marked length exponent ℓ_M separately from the fixed
geometric buffer, retaining the fixed presentation multiplier once, and
including annular endpoint constants. A final audit passed the moving
frontier and its exact complementary predicate:
Q>U^κ1 and [Nd>U^(3/20) or Q(Nd)^(1/10)>U^κ_sf].

The kernel audit passed the full common-support count, selected/all-row
normalizations, symmetric signed cuts, exact complement, and physical
zeros. Sharp conductor and bin predicates are valid in the finite physical
kernel; they do not automatically inherit radial Poisson. No termwise
positivity or smoothing comparison is asserted.

Equal-product centering has a quadratic zero in the common Mellin
difference frequency for identical profiles on the same real line.
It cancels the common principal double residue but neither generic inverse
poles nor the independent inverse Mellin argument. The common aspect
derivative identity preserves both integrals and every cross term under
one pair cut, costing O(log⁴U). Both interfaces need a new correlation
estimate to produce a fixed power saving. Unequal individual extraction
children have no automatic exchange symmetry.

## Exact finite verification

The [checker](../numerics/check_signed_high_sectors.py) passes
7,021 assertions, and its
[record](../numerics/signed_high_sectors_record_20261009.json)
replays byte for byte. It uses a formal ideal monoid and a synthetic
multiplicative physical kernel. The retained cases include 42 marked
tuples, 21 columns, 27 rows, 20 selected rows, 355 physical zeros,
398 pairs with asymmetric common powers, and 382 pairs on which an
ordinary gcd quotient differs from the full-support split.

It checks full centered squares, cuts and complements, reversed real
pairs, four common-kernel rectangles, inverse-column valuation bounds,
exact rational core-radius and contour ledgers, and Mellin/derivative
diagnostics. Five defect values give 80 exact frontier cancellations
and 320 feasible core-radius cases; the residual tests include strict
boundary assignments. In the finite example, enlarging B from 1 to 7
adds pairs but decreases the signed sector.

These checks do not prove native reciprocity or transfer, source analytic
envelopes, asymptotic ideal counts, derivative propagation, row Poisson,
or the unbounded signed finishing theorem.

Checker SHA-256: f6b9f38c42ef8bba60c3c9d0fe9938ad1cacbae1633542532b65f89605c2b63d.
Record SHA-256: dd722f2245621b1f3b188cc5a3300db863e8100960539812000802d7cb7c233e.
Manuscript SHA-256: 6c69b3d9a4de34e254faee454b965e425d5b045cd3ea9df2a0b1a27c25e936e6.
Native compilation: success with the desktop editor's compiler on 9 October 2026, using the existing open source in place. Static checks resolve all 246 labels, 180 references and 27 bibliography items; all 419 local Markdown links checked before installation resolve.

## Next analytic obligation

The next estimate is Note 28 (27), or its selected counterpart (28),
with the exact row predicate, original centered inverse, large exclusive
supports on both sides, and physical zeros. The remaining legal scalar
supremum still misses by at least 1627/7000. Re-estimating the removed
same-support or low-defect sectors cannot supply that gain.
The centered Mellin and common aspect derivative formulas provide
precise interfaces for a new signed estimate; their cancellation must
remain inside the complete aggregate. The full mixed theorem, detector
coverage, family boundary improvement and descent from zeta-only
quasi-RH to RH remain unproved.
