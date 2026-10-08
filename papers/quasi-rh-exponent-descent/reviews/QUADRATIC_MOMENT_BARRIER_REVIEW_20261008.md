# Review of quadratic-family detection and the signed-moment barriers

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This separate same-model review is an internal check, not independent
specialist validation.

## Scope and finding

Reviewed [QUADRATIC_MOMENT_STRENGTH_AND_BARRIER_20261008.md](../notes/QUADRATIC_MOMENT_STRENGTH_AND_BARRIER_20261008.md)
and [check_quadratic_moment_barrier.py](../numerics/check_quadratic_moment_barrier.py).
The relevant probe construction was checked in the
[parent manuscript](../../prime-variance-exponents/manuscript.tex),
Lemmas 2.1--2.2, including the proof locating all zeros of \(H\) on
the imaginary axis. The existing scalar detector and integer quadratic
lift supply the normalization. The standard Dirichlet \(L\)-function
continuation and Euler product were checked against
[DLMF 25.15](https://dlmf.nist.gov/25.15); the cited prime number
theorem is recorded in [DLMF 27.2](https://dlmf.nist.gov/27.2#E3).
The classical quadratic large sieve is the same imported statement
already scoped in the [lift review](INTEGER_QUADRATIC_LIFT_REVIEW_20261008.md).

**Finding:** no blocking mathematical error found. The note proves
necessary family strength and two limitations of proposed estimation
methods. It does not claim the missing signed arithmetic estimate or
a new zero-free region.

## 1. The fixed probe detects the whole stated character family

The Mellin multiplier is

\[
\widehat\ell(s)=G(1/2-s)\frac{2^{s+2}-1}{s+2}.
\]

The manuscript proves
\(G(z)=z(z^2-1/4)H(z)/\sqrt\nu\), with every zero of \(H\)
nonzero and purely imaginary. Thus the first factor has no zero in
\(1/2<\Re s<1\); its possible zeros contributed by the displayed
polynomial occur at \(s=0,1/2,1\). The second factor has its
nonremovable zeros on \(\Re s=-2\). This verifies that the
noncancellation property used in Proposition 1 is not restricted to
points already known to be zeta zeros.

For each fixed odd squarefree \(a\), the conductor ceiling
\(Q=X^{2-h}\) eventually contains \(a\). Positivity of the moment
then gives the response exponent \(\beta_h\), with a harmless
factor \(a^{1/4}\). The Mellin identity with \(-L'/L\) retains
all prime powers and has no lower-end convergence problem. Arbitrary
positive epsilon makes the transform holomorphic strictly to the
right of \(\beta_h\). A zero there leaves a nonzero residue, while
the principal pole at one is canceled by the preparation zero.
The ordinary zero-free line at one handles that boundary separately.

For odd squarefree \(a\), the product of its primitive Legendre
characters is primitive modulo \(a\). Conversely, a primitive
quadratic character with odd conductor has exactly this form.
Both character parities occur; even-conductor characters do not.
The proposition's scope and fixed-character quantifiers are therefore
correct.

## 2. Remainders, diagonal, and the squarefree mask

Higher prime powers and the prime 2 contribute at most
\(X^{1/2}\log^2(2X)\) per row by counting, uniformly in \(a\).
The weighted squared norm is consequently

\[
O(X\sqrt Q\log^4(2X))=X^{2-h/2+o(1)}.
\]

Its gap below the target \(1+h/2\) is \(h-1>0\).
The weighted norm triangle inequality proves the equivalence of the
full and prime-only target without neglecting any cross terms.
The prime diagonal has this same permissible exponent.

For sufficiently large \(X\), all primes in the fixed annular support
exceed \(Q=o(X)\), so the diagonal kernel is exactly the total row
weight. Before that range the original zero mask is needed, as the
note states. The off-diagonal form is real by pairing \(p,q\), and
the full norm's positivity bounds its negative part by the already
controlled diagonal. Thus the one-sided upper estimate suffices.

In the squarefree removal \(a=d^2b\), the weight becomes
\(d^{-1}b^{-1/2}\), and the canceled quadratic phase is exactly
\(\mathbf1_{(d,k)=1}\). There is no reason to impose
\((b,d)=1\). Equation (11) retains both facts. For \(k=pq\)
with distinct odd primes, the character on odd \(b\) has primitive
conductor \(pq\) or \(4pq\), as stated; the short row range has not
become a complete character period.

## 3. Actual entrywise absolute obstruction

Replacing the signed coefficient \(c_p\) by \(|c_p|\) inside the
complete Gram form gives a positive sum of squared row responses.
Its \(a=1\) term is \((\sum_p|c_p|)^2\). Therefore

\[
\sum_{p\ne q}|c_pc_qJ_Q(pq)|
\ge \left(\sum_p|c_p|\right)^2
-W_Q\sum_p|c_p|^2.
\]

The fixed profile is continuous, nonzero, and compactly supported.
The prime number theorem gives a positive linear asymptotic for
\(\sum\log p\,|\ell(p/X)|\); the diagonal term is
\(O(X\sqrt Q\log^2X)=o(X^2)\). Proposition 2 consequently
applies to the actual prime coefficients for all sufficiently large
real \(X\). It is not a claim that the original signed form is
large, nor that every kernel entry is positive. The distinction
between an arithmetic absolute-majorant obstruction and the
separate abstract response model is maintained.

## 4. The hybrid-envelope limitation

With the explicitly additional conductor-uniform individual bound,
the two permitted block exponents are
\(2B+\alpha/2\) and \(2-\alpha/2\), on
\(0\le\alpha\le2-h\). The first increases and the second
decreases, so their crossing is \(\alpha_*=2-2B\).
This proves the piecewise expression in equation (16) continuously,
including the meeting point \(h=2B\).

The envelope fits the required exponent only for \(h\ge2B\).
Any strict improvement over \(B\) would require
\(h<4B-2<2B\). In that useful range the available exponent is
\(1+B\), the missing saving is \(B-h/2>1-B\), and the
bottleneck lies at conductor exponent \(2-2B\).
The example \(B=7/8,h=7/5\) has the correctly stated powers
\(15/8\), \(17/10\), and gap \(7/40\).

The artificial response array at \(a\asymp X^{2-2B}\) has
total unweighted squared mass \(O(X^2)\), so it obeys every
cumulative scalar large-sieve envelope \(O(X(Y+X))\).
Its weighted mass is of order \(X^{1+B}\), and its support
lies strictly inside the conductor ceiling in the proposed descent
range. It can have zero principal response. This establishes the
claimed sharp limitation in that range for those two scalar
envelopes alone. The note correctly avoids asserting that the
array comes from actual primes or respects all information in the
common character matrix.

## 5. Finite checks and limits

Reran the exact script successfully. It verifies \(13{,}065\)
coefficient identities in the squarefree removal, the canceled-phase
mask counterexample, three exact positive-Gram comparisons, and
twenty rational instances of the continuous piecewise envelope.
The script keeps square-root weights symbolic in the coefficient
identity and uses positive rational row weights where only Gram
positivity is tested. These substitutions preserve the algebra
being certified and are disclosed.

The noncancellation proof and the standard analytic inputs were
checked only to the scope above. No new asymptotic moment, uniform
explicit-formula estimate, or improvement of a zero-free strip
was proved by the numerical checks or by this review.
