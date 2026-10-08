# Short families: a larger controlled sector and the remaining cancellation problem

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Derivations and separate same-model reviews are internal checks, not
independent specialist validation or formal proof replay.

Based on repository commit `00119da502ed019798e9b164e8342ea0e2df6d02`.
This continuation follows the [strategic review](../../reviews/STRATEGIC_REVIEW_20261008.md)
and [small-cofactor reduction](SHORT_FAMILY_SMALL_COFACTOR_20261008.md).

## What changed

The short-family route now has a larger controlled overlap sector and a
more precise obstruction in its coprime core. The core still needs a new
signed estimate. Its prime-selected part is provably too large to meet
the desired budget, so a successful argument must preserve compensating
terms across column types. Neither repeated Poisson summation nor the
generic sextic large sieve supplies that cancellation.

Two missing conjugations in the earlier small-cofactor note have also
been corrected. The original source-normalization review missed them;
plain PDF extraction had dropped the overbars. A comparison with the
TeX source and rendered PDF verifies

\[
a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n),\qquad
W_0(t)=t^{-1/2}\overline{W(t)}.
\]

The exact transformed identity needs both corrections. Earlier bounds
that use coefficient moduli, masks, and profile seminorms survive.
The [source audit](SHORT_FAMILY_CORE_INVOLUTION_20261008.md) records
the conventions, including the exterior finite-character coefficients.

## A larger controlled overlap sector

Keep the original moment, fixed twist, masks, and smooth profile:

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),\qquad
\mathfrak M(D,H)=D^{-1}\sum_u\Phi(Nu/H)|A_u(D)|^2,
\quad H=D^h,
\]

where \(0<h<1\). Write \(B,F,G\) for dyadic lower endpoints of
\(Nb,Nf,N(m_1,m_2)\) in the diagonal-subtracted transformed form.
Uniform primitive completion and counting by the common ideal give

\[
\boxed{
|\mathfrak S^\circ_{\xi;B,F,G}|
\ll_\varepsilon D^\varepsilon
\min\left\{\frac{D^2}{B^2FG},\frac{HD}{BF^2G^2}\right\}.
}
\]

Thus all blocks with \(BF^2G^2\ge D^{1-a}\) fit the proposed
\(D^{h+a+\varepsilon}\) budget. In the lossless \(b=f=1\) block,
this removes overlap norms \(G\ge D^{1/2}\), improving the previous
threshold for \(h>1/2\). The [proof](SHORT_FAMILY_HIGH_OVERLAP_20261008.md)
preserves the complete row kernel and explains dyadic boundary constants.

After first applying the imported positive theorem to complete large-
\(b\) blocks and then removing the rapid-decay sector, the remaining
obligation is confined to

\[
Nb<D^{1-h+\eta},\qquad
(Nf)^2G<HD^{2\eta},\qquad
BF^2G^2<D^{1-a},\qquad m_1\ne m_2,
\]

with the boundary convention specified in the proof. Its complete signed
combination must still be bounded by \(D^{h+a+\varepsilon}\).

## Why the coprime core cannot be split into separately affordable parts

For \(b=f=1\) and \((m_1,m_2)=1\), a second Poisson transform,
with the corrected coefficients, returns exactly the original coprime
off-diagonal Möbius form. This is an involution, not a contraction.

For trivial fixed twist and a nonnegative nonzero annular profile,
retain only distinct prime columns. The resulting core is a positive
prime-only moment minus its full diagonal. There are
\(\asymp H^{1/6}\) coherent rows \(u=r^6\), and all original
prime masks are one on those rows. The prime ideal theorem gives

\[
\mathcal C_{\rm prime}\gg
\frac{DH^{1/6}}{(\log D)^2}-O\!\left(\frac H{\log D}\right)
\gg\frac{D^{1+h/6}}{(\log D)^2}.
\]

Consequently a target-sized bound for every separately selected
prime/composite component would require \(a+5h/6\ge1\).
Every target that improves \(7/8\) instead has
\(a+5h/6<3/4\). This prime-selected component exceeds such a
target by more than a quarter power of \(D\), up to logarithms.

This is an obstruction to that decomposition method, not a lower bound
for the unrestricted Möbius moment. The [full derivation](SHORT_FAMILY_CORE_INVOLUTION_20261008.md)
retains the actual source coefficients and exterior character combination.

## Generic estimates and replication do not close the gap

The newly imported de Faveri preprint, [Theorem 1.1](https://arxiv.org/html/2610.04045v1),
allows sixth-power-free indices on both sides of its large sieve.
After checking the character presentation, retaining deletion masks,
and paying for all sixth-power multiplicities, it gives

\[
\mathfrak M(D,H)\ll_\varepsilon(DH)^\varepsilon
\left(H+DH^{1/6}+H^{5/6}D^{1/3}+H^{1/3}D^{5/6}\right).
\]

For \(1\le H\le D\), this is \(D^{1+\varepsilon}H^{1/6}\).
It matches the broad-coefficient lower bound in powers, but corresponds
to \(a=1-5h/6\) and extracts only exponent one. Its deep proof has
not been replayed. The [transfer and comparison](SHORT_FAMILY_SEXTIC_SIEVE_BARRIER_20261008.md)
separate that imported result from the new deductions here.

The [replication audit](SHORT_FAMILY_REPLICATION_LIMITS_20261008.md)
also shows that using every composite sixth power improves the prime-row
count only logarithmically; arbitrary row weights cannot improve the
replication power; and quadratic or cubic subfamilies inherited solely
from the same sextic moment give exactly the same extraction floor.
Additional power savings require additional arithmetic information.

## The next analytic target

The useful output exponent remains

\[
\beta_{\rm out}=\frac{1+a}{2}+\frac{5h}{12}.
\]

| Family exponent \(h\) | Required loss to improve \(7/8\) | Output if \(a=0\) |
| --- | --- | --- |
| \(8/9\) | \(a<1/108\) | \(47/54\) |
| \(4/5\) | \(a<1/12\) | \(5/6\) |
| \(2/3\) | \(a<7/36\) | \(7/9\) |

The next calculation should retain the full Möbius coefficients in the
low-overlap core and measure cancellation between factorization classes
before applying absolute bounds. A proposed factorization identity must
recombine its compensating terms before estimating them: the prime-only
test above is a concrete check against discarding that cancellation.
An estimate for the whole coprime core would still need extension to the
remaining \(b,f,G\) ranges and their original masks.

The \(h=8/9\) option minimizes the remaining large-cofactor range among
these examples but tolerates very little loss. The \(h=4/5\) option is
a useful parallel test because it permits loss below \(1/12\). This is
a tradeoff in the remaining analytic problem, not evidence that either
estimate is currently available. For a zero-free conclusion, the moment
must also cover a profile class with no common Mellin zero.

## Verification and present limits

The [scoped review](../../reviews/SHORT_FAMILY_CORE_AND_OVERLAP_REVIEW_20261008.md)
checks source corrections, the involution, the prime obstruction, the
overlap count, replication, and the new sieve transfer. The
[exact checker](../../numerics/check_short_family_continuation.py) and
[record](../../numerics/short_family_continuation_record_20261008.json)
contain 9,356 passing assertions: rational exponent budgets, complex
weight identities, a nonconstant Eisenstein angular-phase witness,
complex-profile orientation, and finite Gauss/Fourier identities.
The record replays byte-for-byte. These finite checks do not prove an
asymptotic arithmetic estimate or the imported number-field theorems.

The signed short-family remainder, a new zero-free boundary, and descent
to RH remain unproved. The progress is a smaller residual region and
sharper constraints on what a successful cancellation argument must do.
