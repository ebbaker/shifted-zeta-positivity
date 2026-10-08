# Scoped review: fixed short-family extraction refinement

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed to this agent and are not inferred.
This is same-model internal cross-review, not independent specialist validation.

Reviewed: [1_SHORT_FAMILY_DESCENT_REFINEMENT_20261008.md](../short_families/notes/1_SHORT_FAMILY_DESCENT_REFINEMENT_20261008.md),
compared with Route B, equations (13)–(19), in the
[continuation](../notes/CODEX_CONTINUATION_20261008.md), and the
[earlier family transfer](../../quasi-rh-character-amplification/notes/CHARACTER_FAMILY_TRANSFER_20261008.md).
The source papers' deep analytic proofs and the short-family moment itself
were not independently verified. The source-range discussion is scoped as
conditional algebra using its displayed imported range formulas.

## 1. Accepted conditional extraction

The prime-deletion identity has the correct sign and scale:

\[
 A_1(L)=B_p(L)-\nu(p)B_p(L/Np),\qquad
 B_p(L)=\sum_{j\ge0}\nu(p)^jA_1(L/(Np)^j).
\]

Writing a squarefree ideal divisible by \(p\) as \(pm\), with \(p\nmid m\),
proves the first identity; the same fixed annular profile is retained.
Recursive substitution terminates by annular support. This explicitly
preserves the character zero extension instead of treating sixth-power
rows as exact unmasked copies.

For \(Np\asymp D^{h/6}\), a fixed-character bound \(P(t)\) controls the
mask error by \(D^{(1-h/6)(t+\varepsilon)}\). The number of eligible prime
rows is \(D^{h/6+o(1)}\). The hypothesized full moment therefore gives the
recurrence

\[
 t\longmapsto\max\{b,ct\},\qquad
 b=(1+a)/2+5h/12,\qquad c=1-h/6.
\]

For fixed \(0<h\le1\), \(b>0\), and \(b<1\), its iterate from the
unconditional ideal-counting bound \(t_0=1\) is exactly
\(t_j=\max\{b,c^j\}\). It reaches \(b\) at a finite stage. Every use of
the moment is the original same-scale assumption evaluated at the new
outer variable; it does not require a supremum over smaller scales or a
new conductor. The stronger bound from an earlier stage supplies the
smaller-scale mask control. The all-epsilon quantifier absorbs the finite
sequence of logarithms and losses. No uniform stage constant is needed.

Thus the advertised removal of the prime-mask *exponent loss* is correct.
It does not mean that the mask disappears from the exact identity. A fixed
positive \(h\) still leaves the floor \(b\ge1/2+5h/12\).

The chain \(1\to8/9\to64/81\to7/9\) for \(h=2/3,a=0\) is correct.
The strict improvement condition \(a+5h/6<3/4\) for beating \(7/8\) is
also correct, and imposes no lower bound such as \(h>3/4\).

## 2. Accepted repeated-row equivalence and endpoint scope

For the original fixed Möbius character coefficients and a fixed profile,

\[
 P(\beta)\quad\Longleftrightarrow\quad
 J(D)^{-1}\sum_{Np\asymp D^{h/6}}|B_p(D)|^2
 \ll_\varepsilon D^{2\beta+\varepsilon},\qquad 0<\beta\le1,
\]

is justified. The forward direction follows from the same geometric
completion; the reverse direction repeats the finite recurrence with floor
\(\beta\). The positivity assumption \(\beta>0\) matters for the finite
iteration and for uniform geometric control. No equivalence at \(\beta=0\)
is asserted.

The observation that moments at \(h_j,a_j\to0\) already reach the endpoint
via the row \(u=1\) is correct. Replication improves the finite-parameter
exponent; it does not make these arbitrarily short-family assumptions
logically weaker than their own single-row consequence. A hypothesis
conditional on a prior strip remains conditional until supplied at each
required stage.

The Mellin transform uses the correct \(D^{-s}dD/D\) convention. Smooth
annular support eliminates the small-scale endpoint, and a profile with
\(\widehat W(\rho)\ne0\) detects any fixed zero with real part beyond the
obtained exponent. The note correctly preserves the distinction between
one character, all Hecke characters, and a zeta-only strip.

## 3. Correction requested during review

The initial draft's unrestricted-column countercheck invoked its row
equivalence after changing the coefficients to the squarefree indicator.
That equivalence was stated and proved for the original Möbius character
coefficients. It should not be applied outside its stated coefficient
class without another proof.

The obstruction itself has a direct repair: with the permitted hypothetical
weight \(\mu_K(n)\overline{\nu(n)}\), a nonnegative nonzero fixed profile
makes the unmasked squarefree sum \(\asymp D\). Removing \(p\)-divisible
columns costs at most \(O(D/Np)\), uniformly for the primes in question.
Every such prime sixth-power row is therefore \(\gg D\). Their energy is
\(\gg D^{2+h/6}/\log D\); comparison with the proposed full bound forces
\(a+5h/6\ge1\). This supplies the stated coefficient-class obstruction
without misusing the fixed-coefficient equivalence. This correction was
sent to the author and has been incorporated in the final note.

The final note also incorporates the suggested wording correction: the
prime-row sum is a positive subsum of the full family. Its numerical value
need not be *strictly* smaller if all complementary summands happen to vanish.
No outstanding correction remains within this review's stated scope.

## 4. Source-range and numerical scope

Given the displayed imported relations
\(R\ll D^2/(HB^2)\), \(\Sigma=D/B\), and
\(R' < R(R/\Sigma)^2\), the ratio calculation and the small-\(B\)
obstruction to reusing the long-family induction are algebraically correct.
The range \(B\ge D^{1-h+\kappa'}\), with a fixed positive margin,
repairs only that ratio inequality, not all hypotheses of the imported
Poisson or induction statements. The note explicitly retains this limit.
This reviewer did not separately replay the source formulas or their proofs.

Ran the standard-library exact check script: five rational chains and twelve
finite masked-identity fixtures passed. These confirm algebra and a finite
integer analogue of the mask; they are not evidence for an asymptotic Hecke
moment estimate. No new RH claim follows from this review.
