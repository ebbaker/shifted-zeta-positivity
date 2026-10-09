# Review of further bounds for the signed form

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
reasoning effort are not exposed and are not inferred. Three parallel
same-model derivations and audits are internal checks, not independent
specialist validation or formal proof verification.

[Note 29](../mixed_character_families/notes/29_SIGNED_FORM_SECTORS_AND_SIXTHPOWER_TAIL_20261009.md)
bounds three further parts of the exact signed residual from
[Note 28](../mixed_character_families/notes/28_SIGNED_HIGH_CONDUCTOR_SUPPORT_AND_DEFECT_20261009.md).
The bounds and their proofs are incorporated into the existing
[manuscript](../mixed_character_families/mixed_character_reductions.tex),
section “Further bounds for the remaining signed form.”
The full correlation with saving 1/700 remains open.

## Completed bounds and scope

| Part of the form | Estimate | Required scope |
| --- | --- | --- |
| Small primitive full-column quotient conductor | f≤B², saving 1/500 | Elementary ideal count, divisor coefficient bound and physical row mass |
| Additional higher-defect rows | κ+[η+(ℓ_M−2α)_+]/10≤κ_sf, saving 11/6250 | Original marked columns, full native sixth-order sieve and global growth |
| At least one column sixth-power factor exceeding U^(1/10) | Complete signed interaction saves 1/500 | Native arbitrary-vector sieve after exact extraction; includes head/tail cross terms |
| Optional larger removed column class, cutoff U^(2/25) | Same saving | Additional original source scalar coefficient, mesh, nonexceptional, profile/height and capacity hypotheses |
| Remaining exact form | Both exclusive supports>B, quotient radical>B², column sixth-power factors≤U^(1/10), row outside the complete core frontier | New one-sided correlation bound is unproved |

The quotient count is at most X√V U^ε for f≤V. Its proof uses the
ordinary gcd only as a counting map, followed by sixth-power extraction
of both coprime quotients. It leaves the full exclusive parts in the
signed pair selector unchanged. The convergent sums have weights
(Ns Nt)^−3; local residual allocations cost at most 10^ω(f).
The primitive conductor comparison retains fixed bad factors and all
physical canceled-phase zeros. No row Poisson theorem is needed.

The full piecewise marked inverse mass pays the low-radius column term
of Θ₆ through (ℓ_M−2α)_+/6. This removes the earlier defect ceiling
without changing the actual squarefree row radius. The new row gate
contains Note 28's defect gate for sufficiently large U, and its
new part is intersected with the exact old residual before removal.
The physical predicate uses
Q[Nd max(1,L/(Na₁)²)]^(1/10)≤U^κ_sf; fixed conductor factors cost
constants. The same contour offset 0<v≤1/5000 leaves reserve 29/87500.

The tail proof extracts each complete centered column k=f₀t⁶ and
freezes t and the physical row sixth-power factor w. The columns f₀
and rows v are sixth-power-free at radii X/(Nt)⁶ and U/(Nw)⁶.
The normalized coefficient norm is at most (Nt)^−6 U^εH^b.
The original high-conductor gate gives Nw≪U^((1−κ1)/6) before
enlargement. The frozen w-deletion stays in the arbitrary coefficient
vector; the v,t row mask is removed only in a positive square.
Finite presentation phases and zero masks are handled once.

Weighted Cauchy with (Nt)^−2 proves
E_tail≤U T^−4+XU^ζT^−10+U^(5/6)X^(1/3)T^−6+
U^(1/3)X^(5/6)T^−9, up to the stated subpower and height factors.
The all-t version bounds the original full energy by the same expression
at unit cutoff. This uses arbitrary-vector native Θ₆, not a specialized
source moment for a truncated inverse or column head.
The exact common-measure full/head identity then bounds every cross
term. Full/head differences of both existing pair cuts are controlled
by their own elementary absolute counts, so their intersections do
not rely on positivity of a pair filter.

At the universal cutoff U^(1/10), the exact cross reserve beyond
saving 1/500 is at least 5519/135000. The smaller pair-correction
reserve is 1/1750. The optional U^(2/25) cross reserve is
84727/6750000, only where Note 27's original scalar scope holds.
The coarse box corner that attains this arithmetic reserve violates
the specialized source capacity; it is used as a conservative
arithmetic enclosure, not as evidence for the source hypotheses.

The [primary de Faveri theorem](https://arxiv.org/html/2610.04045v1)
was checked directly for its sixth-power-free domains, arbitrary
complex vector and fixed arithmetic data. Its native finite-ray
transfer remains an explicit imported input.
Global family growth and finite height degrees retain their earlier
conditional status. All fixed costs must fit the respective reserves.

## Audits and finite verification

Parallel analytic audits checked the full piecewise row mass,
actual-radius frontier, endpoint constants, native full/tail sieve
domains, original high-conductor w cutoff, common physical zero masks,
and the complete head/tail identity. The kernel audit checked the
quotient count, exact nested pair intersections and final partition.
The head coefficient still has the zero-slot prototype's full-size
square norm; its diagonal pairs are already removed from the signed
form, so that benchmark is not a lower bound on the remaining form.

The [checker](../numerics/check_signed_form_bound.py) passes
16,191 assertions and reproduces its
[record](../numerics/signed_form_bound_record_20261009.json)
byte for byte. It tests finite quotient/sixth-power maps, head/tail
and nested-cut identities with physical zeros, piecewise core branches,
the enlarged frontier, strict predicate boundaries, and exact rational
tail reserves. The native cross ledger checks all 16 branch pairs
at the 16 parameter corners. These multi-affine bounds certify the
displayed continuous arithmetic box; the synthetic character model
does not prove native transfer, global analytic envelopes, ideal
asymptotics, all-height propagation or the unbounded signed theorem.

Checker SHA-256: 68a8149c0feab4ff6f26a4b1280709fa3e81cf15ffe34b063e383efb9e04fd7c.
Record SHA-256: a10e0f78070a9a628f178467277724dff6c8fb8ecf200f22979fbc691101d932.
Manuscript SHA-256: ea6deabc7fb1e3c8f90ee5cbaca7db6af7015a6b6392764c0c8a724862d66d3e.
Native compilation: success with the desktop editor's compiler on 9 October 2026 using the existing open source. Static checks resolve 259 labels, 195 references and 28 bibliography items; all 430 local Markdown links checked before installation resolve.

## Remaining obligation

Note 29 (18) is a complete absolute comparison between the old and
new signed forms, with saving 11/6250. The new one-sided target (19)
therefore remains sufficient with saving 1/700. The native whole-vector
bound is above that target. Where the original scalar input is legal,
its previous worst-case deficit of at least 1627/7000 persists.
The remaining estimate must use the joint correlation on the explicitly
retained domain; these controlled parts do not prove that estimate.
The full mixed theorem, detector coverage, new family boundary and
RH descent remain unproved.
