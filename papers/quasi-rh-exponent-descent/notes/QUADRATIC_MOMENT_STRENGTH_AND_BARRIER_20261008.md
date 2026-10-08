# Quadratic moment strength and the necessity of signed prime cancellation

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Same-model derivation and review are internal checks, not independent
specialist validation.

The localized quadratic moment from the
[integer-response lift](INTEGER_QUADRATIC_RESPONSE_LIFT_20261008.md)
has three further consequences for the research program.

1. Its proposed bound excludes forbidden zeros for every primitive quadratic
   character of odd conductor, using this same fixed probe, not just for zeta.
2. Prime powers and the prime diagonal already fit below its target. The
   remaining exact signed prime-pair form has an entrywise absolute
   majorant of order at least \(X^2\), which is too large for every
   \(1<h<2\). This is a proved obstruction for the actual coefficients.
3. Even granting a favorable uniform individual response bound at exponent
   \(B\), combining it with the quadratic large sieve cannot give descent.
   The bottleneck lies at conductors \(X^{2-2B}\). A sharp abstract response
   model shows that those two scalar envelopes alone cannot do better.

These statements change which estimates are worth pursuing. They prove
neither the desired signed moment nor a new zero-free region.

## 1. The target and its exact family strength

Fix \(1<h<2\), and write
\[
Q=X^{2-h},\qquad T=1+h/2,\qquad \beta_h=T/2=1/2+h/4.
\]

Here \(Q\) is the remaining conductor ceiling, distinct from the
full physical row range \(X^h\). For odd squarefree \(a\), let
\[
\chi_a(n)=(n/a),\qquad
S_a(X)=\sum_{n\ge2}\Lambda(n)\chi_a(n)\ell(n/X),\qquad
\mathcal W_h(X)=\sum_{\substack{a\le Q\\a\ {\rm odd\ squarefree}}}
a^{-1/2}|S_a(X)|^2.                                      \tag{1}
\]
The Jacobi symbols retain all nonunit zeros, and \(\chi_1=1\).
The previous note proves that
\[
\mathcal W_h(X)\ll_\varepsilon X^{T+\varepsilon}            \tag{2}
\]
is equivalent, up to the already controlled larger-conductor contribution
and the mask error, to the proposed full-row scalar moment.

The inherited probe has a stronger noncancellation property than merely
being nonzero at zeta zeros. If
\(\widehat\ell(s)=\int_0^\infty\ell(v)v^{s-1}\,dv\), its exact formula is
\[
\widehat\ell(s)=G(1/2-s)\frac{2^{s+2}-1}{s+2}.              \tag{3}
\]
The [parent manuscript](../../prime-variance-exponents/manuscript.tex),
Lemmas 2.1 and 2.2, gives
\(G(z)=z(z^2-1/4)H(z)/\sqrt\nu\), with every zero of \(H\) purely
imaginary. Hence
\[
\widehat\ell(s)\ne0\quad(1/2<\Re s<1),\qquad
\widehat\ell(1)=0.                                       \tag{4}
\]
The second factor in (3) has zeros only on \(\Re s=-2\); its value at
\(s=-2\) is interpreted by continuity. This argument applies to any point
of the stated strip, independently of which \(L\)-function has a zero there.

**Proposition 1.** If (2) holds for every positive epsilon and every
sufficiently large real \(X\), then every primitive quadratic
\(L(s,\chi)\) of odd conductor, including zeta at conductor one, has
no zero with real part greater than \(\beta_h\).

**Proof.** Fix an odd squarefree \(a\). It eventually belongs to (1), so
positivity gives
\[
|S_a(X)|\ll_{a,\varepsilon}X^{\beta_h+\varepsilon}.         \tag{5}
\]
The factor \(a^{1/4}\) from (1) is harmless for this fixed character.
The Euler product gives the true transform, initially for \(\Re s>1\),
\[
\int_0^\infty S_a(X)X^{-s}\,\frac{dX}{X}
=-\widehat\ell(s)\frac{L'}{L}(s,\chi_a).                  \tag{6}
\]
The standard analytic continuation and Euler product of Dirichlet
\(L\)-functions are recorded in
[DLMF 25.15(i)](https://dlmf.nist.gov/25.15#i).
The integral vanishes below a fixed positive \(X\); its compact initial
part is entire. Equation (5), with a sufficiently small epsilon on each
compact subset, makes the transform holomorphic on \(\Re s>\beta_h\).
A zero \(\rho\) in \(\beta_h<\Re\rho<1\), of multiplicity \(m_\rho\),
would give the nonzero residue
\(-m_\rho\widehat\ell(\rho)\), contrary to (4). The usual zero-free
line at one and half-plane to its right dispose of their boundary;
the principal pole at one is canceled by \(\widehat\ell(1)=0\).
Odd squarefree \(a\) gives a primitive character modulo \(a\), by CRT
from the primitive Legendre factors, and these exhaust the primitive
quadratic characters of odd conductor. \(\square\)

Thus the example \(h=7/5\), boundary \(17/20\), is a simultaneous
odd-quadratic-family target. It is not merely a new way to average an
already known zeta bound. No uniform height or conductor constant is
needed for this necessary fixed-character implication. A family bound
with sufficient uniformity would be needed in the opposite direction.
This proposition does not cover even-conductor twists absent from (1).

## 2. Higher powers and the diagonal are affordable

Put
\[
c_p(X)=\log p\,\ell(p/X),\qquad
P_a(X)=\sum_{p\ {\rm odd}}c_p(X)\chi_a(p),\qquad
R_a(X)=S_a(X)-P_a(X).
\]
All terms are retained in this definition. Elementary counting of higher
prime powers gives, uniformly in \(a\),
\[
|R_a(X)|\ll_\ell X^{1/2}\log^2(2X).
\]
The omitted prime 2 and all its powers are included in this bound.
Consequently
\[
\sum_{a\le Q}^{*}a^{-1/2}|R_a(X)|^2
\ll X\sqrt Q\log^4(2X)
=X^{2-h/2+o(1)}.                                        \tag{7}
\]
The star denotes odd squarefree integers throughout. Since
\(T-(2-h/2)=h-1>0\), the triangle inequality in the weighted row norm
shows that (2) is equivalent to
\[
\sum_{a\le Q}^{*}a^{-1/2}|P_a(X)|^2
\ll_\varepsilon X^{T+\varepsilon}.                       \tag{8}
\]
This is a norm comparison with a paid error, not a claim that the
prime-power cross terms vanish or are independently small at an
unproved response scale.

For sufficiently large \(X\), every prime in the fixed support of
\(\ell(p/X)\) exceeds \(Q\), because \(Q=X^{2-h}=o(X)\).
Define the exact kernel and total row weight
\[
J_Q(k)=\sum_{a\le Q}^{*}a^{-1/2}(k/a),\qquad
W_Q=\sum_{a\le Q}^{*}a^{-1/2}\ll\sqrt Q.
\]
Then \(J_Q(p^2)=W_Q\) on this prime support; at smaller scales the exact
diagonal is instead the masked sum over \(p\nmid a\).
Expanding (8) gives
\[
\sum_{a\le Q}^{*}a^{-1/2}|P_a|^2
=D_Q(X)+\mathcal O_Q(X),                                \tag{9}
\]
\[
D_Q=W_Q\sum_p|c_p|^2\ll X\sqrt Q\log^2(2X),\qquad
\mathcal O_Q=\sum_{\substack{p,q\ {\rm odd}\\p\ne q}}
c_p\overline{c_q}\,J_Q(pq).                             \tag{10}
\]
The diagonal has the same exponent margin \(h-1\) as (7).
The paired expression \(\mathcal O_Q\) is real, and positivity of
the left side of (9) implies \(\mathcal O_Q\ge-D_Q\).
Thus a one-sided upper bound for \(\mathcal O_Q\) at exponent \(T\),
or a modulus bound for the whole sum, suffices and is equivalent at
this exponent. No pairwise positivity follows.

An exact squarefree-removal formula, useful before attempting a
transform, is
\[
J_Q(k)=
\sum_{\substack{d\le\sqrt Q\\d\ {\rm odd}\\(d,k)=1}}
\frac{\mu(d)}d
\sum_{\substack{b\le Q/d^2\\b\ {\rm odd}}}
b^{-1/2}(k/b).                                          \tag{11}
\]
It follows from \(\mu^2(a)=\sum_{d^2\mid a}\mu(d)\).
There is no restriction \((b,d)=1\). The factor \((d,k)=1\)
is the canceled-phase zero mask and cannot be omitted.
For distinct odd primes \(p,q\), the character in the inner row
variable has conductor \(pq\) or \(4pq\), according to \(pq\bmod4\);
the row range is at most \(Q\ll X\), while \(pq\asymp X^2\).
Neither a complete-period estimate nor a replacement by independent
random characters is licensed by (11).

## 3. A lower bound rules out entrywise absolute estimation

**Proposition 2.** For this actual fixed nonzero probe and every fixed
\(1<h<2\),
\[
\mathcal A_Q(X):=
\sum_{\substack{p,q\ {\rm odd}\\p\ne q}}
|c_p c_q J_Q(pq)|\gg_\ell X^2
\quad\text{for all sufficiently large real }X.           \tag{12}
\]
In particular, \(\mathcal A_Q\) cannot satisfy the desired
\(X^{1+h/2+\varepsilon}\) bound for every epsilon.

**Proof.** Write \(b_p=|c_p|\). The complete kernel is a positive
Gram kernel, so
\[
\begin{split}
\sum_{p,q}b_pb_qJ_Q(pq)
&=\sum_{a\le Q}^{*}a^{-1/2}
\left|\sum_p b_p\chi_a(p)\right|^2\\
&\ge\left(\sum_p b_p\right)^2,                           \tag{13}
\end{split}
\]
using its actual \(a=1\) term. Subtract the diagonal, then bound a
signed sum by its entrywise modulus, to obtain
\[
\mathcal A_Q(X)\ge
\left(\sum_p|c_p|\right)^2-W_Q\sum_p|c_p|^2.              \tag{14}
\]
The [prime number theorem](https://dlmf.nist.gov/27.2#E3),
by partial summation for the fixed continuous compact profile, gives
\[
\sum_{p\ {\rm odd}}\log p\,|\ell(p/X)|
\sim X\int_0^\infty|\ell(v)|\,dv.
\]
The integral is positive. The second term of (14) is
\(O_\ell(X\sqrt Q\log^2(2X))=o(X^2)\). This proves (12).
\(\square\)

This is not an abstract coherent-mode countermodel: it concerns the
entrywise absolute majorant of the exact arithmetic sum (10).
It leaves open cancellation among the original signed profile weights
and character correlations. Removing the principal row from (13)
would remove this particular obstruction, but would also remove the
zeta response that the family lift was designed to bound.
The useful next estimate must retain signs across prime pairs or exploit
the full operator, rather than add individual pair moduli.

## 4. A favorable family envelope still does not give descent

For a separate method audit, explicitly grant a uniform response hypothesis
\[
|S_a(X)|\ll_\varepsilon X^{B+\varepsilon},
\quad 1/2<B<1,\quad a\le X^{2-h},                        \tag{15}
\]
with a constant independent of \(a\). Polynomially growing conductor
constants are not silently allowed. This is an additional favorable
assumption; zeta-only quasi-RH does not provide it. No reciprocal-growth
or uniform explicit-formula theorem is being inferred from a bare strip.

On a dyadic conductor block \(A<a\le2A\), \(A=X^\alpha\),
\(0\le\alpha\le2-h<1\), the individual envelope gives
\[
\sum_{a\asymp A}^{*}a^{-1/2}|S_a|^2
\ll X^{2B+\alpha/2+\varepsilon}.
\]
The squarefree quadratic large sieve, after the already paid
prime-power separation, gives
\[
\sum_{a\asymp A}^{*}a^{-1/2}|S_a|^2
\ll X^{2-\alpha/2+\varepsilon}.
\]
This is the same [source theorem and application](INTEGER_QUADRATIC_RESPONSE_LIFT_20261008.md#6-what-the-classical-squarefree-large-sieve-actually-gives)
as before. Taking the better bound and summing blocks yields exponent
\[
\mathfrak E(B,h)=
\max_{0\le\alpha\le2-h}
\min\{2B+\alpha/2,\;2-\alpha/2\}
=
\begin{cases}
1+B,&h\le2B,\\
1+2B-h/2,&h\ge2B.
\end{cases}                                             \tag{16}
\]
This is a continuous calculation: the two affine functions cross at
\(\alpha_*=2-2B\); the first increases and the second decreases.

The target is \(T=1+h/2\). Formula (16) fits it only when \(h\ge2B\).
But then the extracted boundary obeys
\(\beta_h\ge(1+B)/2>B\). Every choice that would strictly improve
the existing \(B\) must satisfy
\[
h<4B-2<2B,                                              \tag{17}
\]
so its bottleneck is \(X^{1+B}\), at conductors \(X^{2-2B}\).
The additional energy saving needed over these scalar envelopes is
\[
\mathfrak E(B,h)-T=B-h/2>1-B.                            \tag{18}
\]
This is a limitation of combining these estimates, not a lower bound
for the actual signed moment.

For \(B=7/8,h=7/5\), the bottleneck conductors are \(X^{1/4}\),
the available exponent is \(15/8\), the desired one is \(17/10\),
and the missing saving is \(7/40\). This is a much larger obligation
than a tiny perturbation of the current family strip.

There is a sharp abstract check. Put \(A_*=X^{2-2B}\), and set artificial
responses \(v_a=X^B\) on odd squarefree indices \(a\in[A_*,2A_*]\),
zero elsewhere. Their individual sizes satisfy (15). Their total
unweighted squared mass is \(O(A_*X^{2B})=O(X^2)\), so they satisfy
all the cumulative scalar bounds \(O(X(Y+X))\), \(a\le Y\), supplied
by this application of the large sieve. But their weighted energy is
\(\asymp X^{1+B}\). In the useful range (17), this block is contained
in \(a\le X^{2-h}\) for sufficiently large \(X\).
It can have \(v_1=0\), so removing just the principal response does not
repair this second, family-average obstruction. These arrays are not
claimed to arise from actual primes or one common character matrix:
they certify the exact limitation of the two scalar envelopes alone.

## 5. Changed next task and verification scope

The new arithmetic task is the complete signed off-diagonal form (10),
with kernel (11), at exponent \(1+h/2\). Its coefficientwise absolute
majorant is provably too large. A successful argument needs information
about correlations of the actual prime coefficients, beyond individual
character bounds and the scalar quadratic large-sieve envelope.

This route now has a more explicit cost comparison with the sextic
short-family lane. The quadratic moment would improve a whole odd
quadratic family, and its naive hybrid estimates lose a fixed amount
even for a tiny proposed boundary improvement. It remains a valid
alternative, but should not be described as an inexpensive consequence
of the existing zeta strip.

The [finite check](../numerics/check_quadratic_moment_barrier.py) verifies
the exact masked squarefree transform coefficient by coefficient,
the positive-Gram inequality behind (14), and rational instances of the
piecewise envelope and its sharp abstract model. Square-root weights
are kept symbolic as integer coefficient vectors in the transform check;
finite Gram inequalities use arbitrary positive rational row weights,
for which the same algebra holds. No floating prime asymptotic or new
zero-free estimate is certified.
