# Scoped review: selected inverse distribution and the cubic target

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is same-model internal review, not independent specialist validation
of the source theorems or a formal proof replay.

Reviewed [2_SELECTED_INVERSE_DISTRIBUTION_20261008.md](../mixed_character_families/notes/2_SELECTED_INVERSE_DISTRIBUTION_20261008.md),
its exact script, and the operational region in the preceding
[mixed-conductor note](../mixed_character_families/notes/1_MIXED_CONDUCTOR_REFINEMENT_20261008.md).
The Gram normalization, legal transposition, conditional kernel bound,
finite-character example, trace expansion, and continuous exponent budgets
pass the stated checks. The actual primitive-character fiber audit resolves
the extra term initially left open in the working derivation. The remaining
pairwise-inequivalent cyclic sum is still unproved.

## 1. Positive frame and conductor-uniform kernel bound

With \(T_{u,k}=N^{-1/2}\psi_u(k)B(Nk/N)\), the vector of ones gives
exactly the original centrally normalized plain polynomial. Its support
contains \(O(N)\) columns, including any original zeros. Thus
\[
\|\operatorname{diag}(\sqrt w)T\mathbf1\|^2
\le L_N\|G\|\le L_N\operatorname{Tr}(G^3)^{1/3}.
\]
The kernel uses \(|B|^2\), not \(B\) or an independently selected
column profile. The selected-row indicator belongs to \(w\); it is not
inserted into the complete smooth column sum. Consequently this argument
does not apply a complete-sum theorem to an arbitrarily selected row set.

The product of the row phases is the inducing primitive character times
the union of both original zero masks. Canceling a phase never cancels a
nonunit zero. The possible primitive conductor \(O(U^2)\) and
polynomial deletion radical are both included in the contour estimate.
The previously defined high-column-ratio selector is not put into this
Gram matrix, which would in general destroy positivity.

The September 30 source text was inspected at Lemmas 4.9--4.10,
pages 22--23, against the hash identified in the note. Lemma 4.9 explicitly
includes an arbitrarily small power of conductor and height on a fixed
half-plane to the right of the global boundary. Lemma 4.10 treats the
polynomial-size deleted Euler factors. These statements, together with the
imported global boundary \(7/8\), justify a nonprincipal contour at
\(7/8+v\). Allocating the arbitrarily small losses gives
\(U^\varepsilon N^{-1/8}\) with the profile seminorm and height costs
retained. Principal row ratios are excluded from this argument. Their
possible main term is not estimated by a nonprincipal bound.

This check verifies the dependency and conductor bookkeeping, not the
proof of the source's global family theorem. The note correctly requires
uniformity for all profiles used by the eventual positive-norm argument.

## 2. Bounded actual primitive-character fibers

The source's equation (4.8), page 16, and its Section 8 description give
the exact local phase at each prime outside the fixed bad set \(S\).
For common orientation \(\varsigma=\pm1\), the ratio for rows \(u,v\)
has local exponent
\(\varsigma(v_{\mathfrak p}(u)-v_{\mathfrak p}(v))\) in a character of
exact order six. Fixed ray and unit phases are unramified there. A
principal inducing ratio therefore forces equality modulo six of the two
valuations. Since both rows are sixth-power-free, their valuations in
\(\{0,\ldots,5\}\) agree exactly. Equal local **orders** alone would
not justify this conclusion; the exact reciprocal phase identity does.

In the Eisenstein PID, the fixed outside-\(S\) ideal determines an element
up to its \(S\)-valuations and six units. Thus there are at most
\(6^{|S|+1}\) rows in a primitive-character fiber. For the source rows
coprime to \(S\), the bound is at most six. An annular or selected subset
can only reduce this count. This proves \(P\ll_S W\) for the actual
row set without identifying the masked kernels within a fiber.

The separate [local-character review](PRIMITIVE_CHARACTER_FIBER_REVIEW_20261008.md)
checks this arithmetic argument against the source. Neither argument
extends the assertion to unrestricted rows containing arbitrary sixth powers.

## 3. Trace expansion and controlled character coincidences

For positive semidefinite \(G\), the expansion
\[
\operatorname{Tr}(G^3)=\sum_{u,v,h}w_uw_vw_hK(u,v)K(v,h)K(h,u)
\]
is exact and retains every canceled-prime mask. The diagonal costs
\(AW^2\); two equal physical rows with a nonprincipal ratio cost
\(WA^2N^{-1/4}\). Equal-primitive-character fibers are now bounded.
More generally, all three characters equal costs at most \(AP^2\),
and exactly two equal costs at most \(A^2PN^{-1/4}\), using the two
nonprincipal cross-character kernels. Thus \(P\ll_S W\) controls
every repeated-character sector by the same two exponent budgets.
This estimate does not assume that a same-character masked kernel is one
or equal to a diagonal entry.

The target exponent is \(h_3=3[1-(1-d)m-s]\), because the column
count contributes \(U^m\) outside the cube root. The note's
\(147/12500\) lower margin comes from a rational interval enclosure on
1,024 closed cells, using valid upper bounds for \(r,m,s\) and
discarding only a favorable nonnegative mass saving. The all-identical
budget has margin \(154297/500000>3/10\). The interval operations
and sign of \(11/4-3d\) used in the substitutions were checked.

The remaining signed sum over three pairwise inequivalent primitive
characters is real after summing the reversed cyclic order. Only an upper
bound for that signed sum is required. No assertion that its individual
terms, or its total, are positive is needed. The target is sufficient for
the original energy; equivalence with that weaker fixed-vector target is
not claimed.

The rank inequality is also correct with \(Z=\operatorname{Tr}G\):
\(\operatorname{Tr}(G^k)\ge Z^k/L_N^{k-1}\). The note makes its
exponent interpretation conditional on the size of \(Z\), and does
not silently assume a uniform diagonal lower bound for arbitrary profiles.

## 4. Finite-character example and method limits

For fixed nonzero quadratic coefficient \(b\), additive orthogonality
makes the \(q\) rows indexed by \(a\) an orthonormal basis. Different
bases have inner products of modulus \(q^{-1/2}\), by the quadratic
Gauss identity in odd characteristic. This proves both the signed frame
norm \(B\) and the entrywise-modulus norm \(1+(B-1)\sqrt q\).
The trace formulas count ordered triples correctly. A nonzero triangle
with three distinct rows must use three distinct bases; their individual
moduli sum to \(q^{3/2}B(B-1)(B-2)\), while the signed total is
\(qB(B-1)(B-2)\). The all-ones column vector has energy exactly the
total row mass since every retained \(b\) is nonzero.

The finite-field script checks all 819 quadratic Gauss sums over fields
of orders 3, 9, and 27 using integer arithmetic in the cube roots of unity.
It verifies the quotient fields have no zero divisors and separately
checks the continuous parameter budgets. An additional 504 exact local
sextic phase/mask comparisons check the valuation-difference identity,
retained canceled-prime zeros, and an equal-order but unequal-character
example. The fields illustrate the loss
from discarding cyclic phases; they are not asserted to realize the actual
Eisenstein Möbius weights or prime annuli.

The absolute-Schur deficit concerns the available uniform entrywise
envelope. It is not a lower bound for actual mixed energy or a prohibition
on using stronger information about the distribution of its entries.
No complete arithmetic cubic-trace bound or zero-free improvement follows
from this review.
