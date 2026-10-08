# Scoped review of the integer quadratic prime-response lift

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This separate same-model review is an internal check, not independent
specialist validation.

## Scope and finding

Reviewed [INTEGER_QUADRATIC_RESPONSE_LIFT_20261008.md](../notes/INTEGER_QUADRATIC_RESPONSE_LIFT_20261008.md),
including its conductor localization in Section 7, against the inherited
[scalar detector](../../prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/SCALAR_DETECTOR_20261004.md)
and [arithmetic feedback](../notes/ARITHMETIC_FEEDBACK_AND_RESONANCE_20261008.md)
normalizations. The classical quadratic large-sieve statement was checked
in the indexed primary-source text of Heath-Brown's
[Theorem 1, p. 237](https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf).
Direct web PDF retrieval returned HTTP 403; the primary PDF search
result supplied the theorem and the definition of its starred ranges.
Neither its proof nor the inherited fixed-probe theorem was replayed.

**Finding:** no blocking error found in the complete lift, zero masks,
prime-power deletion, exponent extraction, large-sieve application, or
conductor localization. The proposed useful moment remains explicitly
unproved. The note does not establish a new zero-free region.

## 1. Whole response and masks

For odd \(b\), the exact identity is

\[
\left(\frac n{b^2}\right)=\mathbf1_{(n,b)=1}.
\]

Since \(\Lambda\) is supported on prime powers, deleting the primes
dividing \(b\) removes exactly the terms displayed in note equation (3).
No prime-power tail is suppressed in this identity. In a multiplicative
window \([A_LX,C_LX]\), a fixed prime contributes at most
\(1+\log(C_L/A_L)/\log p\) powers. Summing their logarithmic weights
gives the stated uniform \(O_L(\log b)\) deletion error, including
boundary windows. The count of odd square roots in (5) is exact.

The Hilbert-space construction uses a common function \(F_X(y)\) for
all square rows, \(y\in[1,2]\), and only enlarges a positive sum of
entire row norms. The deletion estimate is uniform in \(y\), so the
direct-sum triangle inequality proves (6). The shell conversion is

\[
\mathcal V_g(X)=X\|F_X\|_2^2,
\]

with no missing factor of \(X\). For the scalar response,
\(S_1(X;\ell)=\int_1^2yF_X(y)\,dy=qX\lambda(X)\), so the norm
moment implies the scalar moment by Cauchy. The zero ordinary moment
of the inherited probe removes the continuous density term. It does
not remove the nonzero logarithmic continuum term when a later Vaughan
decomposition is used; the note preserves that distinction.

## 2. Conditional exponent and detector

Dividing the proposed moment \(X^{1+a+h+\varepsilon}\) by the number
of square rows \(X^{h/2}\) yields the squared response exponent
\(1+a+h/2+\varepsilon\). Multiplication by the shell factor \(X\)
therefore gives variance exponent \(2+a+h/2+\varepsilon\), hence

\[
\beta_{\rm out}=\frac12+\frac a2+\frac h4.
\]

The deletion energy \(X\log^2X\) is smaller throughout the stated
range. The passage from arbitrary positive epsilon to the exact closed
zero bound is valid by intersecting the resulting half-plane bounds.
It requires every sufficiently large real \(X\), which the moment
hypothesis explicitly supplies. No rightmost zero or bounded height is
assumed.

The scalar conclusion uses the inherited noncancellation of the fixed
Mellin probe at every forbidden zeta zero. It is not a generic
scalar-to-norm inequality. The fixed-delay formula (14) has the correct
factor \(c^{\beta-1}\); substitution in the Mellin integral gives the
stated multiplier \(1-rc^{\beta-z}\).

## 3. Grouping the primitive characters

The decomposition \(u=ab^2\) is unique with \(a\) squarefree; it imposes
no coprimality between \(a\) and \(b\). The example \(u=27,a=b=3\)
therefore belongs. At a prime shared by \(a,b\), both sides of

\[
\chi_{ab^2}(n)=\chi_a(n)\mathbf1_{(n,b)=1}
\]

retain the correct zero. The direct-sum norm error is at most
\(O_L(\sqrt H\log(2H))\), proving (11). In particular the principal
squarefree index \(a=1\) has weight \(R(H)\), so it cannot be removed
without losing the replicated target. For odd squarefree \(a\), the
Jacobi character in the numerator variable is primitive modulo \(a\),
with the conductor-one principal case at \(a=1\).

The signed Gram kernel includes all prime-power pairs and the exact
diagonal exclusion \(p\nmid u\). Positivity of the complete norm is not
used to claim positivity of each pair term.

## 4. Classical large sieve and the remaining conductor range

Heath-Brown's theorem restricts both indices to positive odd squarefree
integers. The note applies it to the odd-prime column contribution and
the primitive index \(a\), with \(b\) held fixed. Its mask
\(\mathbf1_{p\nmid b}\) is consequently independent of \(a\), as
required. Summing over \(b\le\sqrt H\) gives

\[
X\sum_b(H/b^2+X)\ll HX+X^2\sqrt H
\]

up to the explicitly allowed subpower factors. The uniformly estimated
higher powers contribute at most \(HX\log^4(2X)\). Their temporary
separation in this upper bound does not alter the exact family lift.
After extracting square rows, the \(X^2\sqrt H\) term still produces
a response bound of order \(X\); the note correctly rejects a power
improvement from this theorem alone.

For Section 7, a dyadic primitive block \(A<a\le2A\) contributes at
most

\[
(HX)^\varepsilon
\left(X\sqrt H\sqrt A+\frac{X^2\sqrt H}{\sqrt A}\right).
\]

Summing blocks above \(A_0=X^2/H\) gives
\(O((HX)^\varepsilon[HX+X^2\sqrt{H/A_0}])\), which is
\(O((HX)^{1+\varepsilon})\). This is useful exactly in the stated
range \(1<h<2\), where \(1<A_0<H\). Partial endpoint blocks are
handled by positive enlargement.

The comparability \(R(H/a)\asymp\sqrt{H/a}\), uniformly for
\(1\le a\le H\), proves both directions of the remaining-input
claim. A full energy \(\ll XH\) implies a low-conductor weighted
energy \(\ll X\sqrt H\); conversely that low-conductor estimate,
the high-conductor result just proved, and the \(O(H\log^2H)\)
grouping error recover the full target. These statements retain the
usual epsilon losses. At \(h=7/5\), the cutoff \(3/5\), weighted
energy exponent \(17/10\), and response boundary \(17/20\) are correct.

## 5. Finite checks and limitations

Reran [check_integer_quadratic_lift.py](../numerics/check_integer_quadratic_lift.py)
after the localization update: all checks passed. Its independent Jacobi
implementations, \(51{,}657\) mask comparisons, \(1{,}000\) root-count
checks, formal prime-power deletion, signed Gram identity, primitive
grouping, and rational exponent identities cover the advertised finite
algebra. Rational formal coefficients appropriately test the identities
without pretending to evaluate the asymptotic prime cancellation.

The imported fixed-probe equivalence and the classical large sieve
remain theorem inputs. The new localized low-conductor moment has not
been proved or numerically certified. Its \(a=1\) summand already has
the desired improved scalar strength, which the note explicitly says.
The review confirms the reduction and scope, not the missing estimate
or a proof of RH.
