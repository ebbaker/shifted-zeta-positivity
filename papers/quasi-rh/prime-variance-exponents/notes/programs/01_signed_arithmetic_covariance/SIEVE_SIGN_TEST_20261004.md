# Sign tests inside the actual smooth-cofactor scalar

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
reasoning effort are not inferred. This is an internal derivation, not an
independent specialist review. No new global prime-variance exponent or
priority claim is made.

## Result

The exact smooth-cofactor sector has substantial contributions of **both
scalar signs**, even after every factorization of an integer has been
combined into its actual coefficient. This can be proved inside the
particularly simple subfamily in which the outer factor is a product of
two comparable primes. A different subfamily of three comparable primes
also shows that the outer coefficient itself has no fixed sign.

More precisely, the positive and negative masses of the grouped
prime-inner scalar are each at least a positive constant times
\((\log X)^{-2}\), for every sufficiently large real \(X\). Therefore
the literal upper/lower bounds obtained by deleting terms of the favorable
sign fail the fixed-power target, even when the exact continuum
\(c_wM_1(U)\) is retained. The proof uses the signed kernel itself and
actual smooth coefficients; it does not reuse the previous semiprime
energy obstruction.

This rules out a specific pointwise positivity mechanism. It does not
rule out sieve identities that retain cancellation between the two kernel
lobes or the two arithmetic signs. The useful remaining requirement is a
quantitative signed comparison of those masses, with the continuum kept
in the same expression.

## 1. The scalar and the scope of the test

Use the fixed probe and exact cutoffs of the
[continuation](SIGNED_COVARIANCE_CONTINUATION_20261004.md):

\[
u=11/24,\quad U=X^u,\quad q_0=7/3,\quad
\ell(t)=\int_1^2 y\,w(t/y)\,dy,
\]
\[
A_U(m)=\sum_{d\mid m,\ d>U}\mu(d),\qquad
J_0(X)=c_wM_1(U)+\frac1{q_0X}
\sum_{\substack{m>U\\p>U}}A_U(m)(\log p)\ell(mp/X).
\tag{1}
\]

Here \(p\) is prime, \(\ell\) is supported on \([A,2B]\), and
\(A=e^{-1/4}, B=e^{1/4}\). All cutoffs are strict as written; \(X\)
is real. The probe satisfies

\[
\int_A^B w(t)\,dt=0,\qquad
c_w=\int_A^B w(t)\log t\,dt<0.
\tag{2}
\]

The small fixed value of \(c_w\) is never replaced by zero or made to
depend on \(X\). The test concerns either one-sided bound for (1),
for example \(J_0(X)\ll X^{-0.005+\varepsilon}\). The full scalar
criterion and the affordable inner-prime-power error are inherited from
the preceding notes, not proved anew here.

## 2. The short-cofactor identity retains both arithmetic signs

The divisor substitution \(k=m/d\) gives exactly

\[
A_U(m)=\sum_{\substack{k\mid m\\k<m/U}}\mu(m/k).
\tag{3}
\]

Let \(P^-(m)\) be the smallest prime factor of \(m>1\). If \(m>U\)
and \(P^-(m)\ge m/U\), the only admitted divisor \(k\) in (3)
is \(1\). Consequently

\[
\boxed{A_U(m)=\mu(m)\quad
       (m>U,\ P^-(m)\ge m/U).}
\tag{4}
\]

Equality is allowed in the roughness condition because the divisor cap
in (3) is strict. For example, \(U=7,m=35\) has
\(P^-(m)=m/U=5\); the divisor \(k=5\) is excluded and (4) gives
\(A_7(35)=1\). Repeated prime factors do not invalidate (4), although
they can make its value zero.

Fix an integer \(2\le r\le11\), and take distinct primes

\[
q_j\asymp X^{1/(2r)}\quad(1\le j\le r),\qquad
m=q_1\cdots q_r\asymp X^{1/2}.
\tag{5}
\]

Every implicit constant in this section is positive and independent of
\(X\). For all sufficiently large \(X\),

\[
m>U,\quad P^+(m)\le U,\quad
P^-(m)\asymp X^{1/(2r)}\gg X^{1/24}\asymp m/U.
\tag{6}
\]

The last strict exponent inequality holds precisely for \(r<12\).
Thus these are genuine **smooth outer factors** of the retained Vaughan
response, yet (4) says

\[
A_U(m)=(-1)^r.
\tag{7}
\]

In particular \(r=2\) gives positive and \(r=3\) gives negative
coefficients. Smoothness of the outer factor does not turn its coefficient
into a positive sieve weight. Equation (7) is a specific arithmetic
calculation, not an appeal to a general parity-barrier slogan.

## 3. The scalar kernel also has both signs

Fubini and \(t=s/y\) give the exact identities

\[
\int_0^\infty\ell(s)\,ds
=\int_1^2y^2\,dy\int_A^Bw(t)\,dt=0,
\]
\[
\int_0^\infty\ell(s)\log s\,ds
=\int_1^2y^2\,dy\int_A^Bw(t)\log t\,dt
=q_0c_w\ne0.
\tag{8}
\]

Thus \(\ell\) is not identically zero. Because it is continuous,
compactly supported, and has integral zero, it takes both positive and
negative values. There are closed intervals
\(I_+,I_-\subset(A,2B)\), each with nonempty interior, and fixed
\(\eta_+,\eta_->0\), such that

\[
\ell(s)\ge\eta_+\ (s\in I_+),\qquad
\ell(s)\le-\eta_-\ (s\in I_-).
\tag{9}
\]

No floating sign computation or claimed asymptotic onset is needed for
(9). In particular an argument that inserts a nonnegative kernel at
this step changes the target. The signs in (9) are the signs of the
actual shell-averaged probe.

## 4. Nonnegligible actual products in each lobe

Fix \(r\in\{2,\ldots,11\}\) and one of the intervals in (9).
Choose \(r\) pairwise-disjoint positive fixed-ratio intervals
\([a_j,b_j]\) and another interval \([a_0,b_0]\), sufficiently
narrow that

\[
[a_0\!\prod_{j=1}^r a_j,
 b_0\!\prod_{j=1}^r b_j]\subset\operatorname{int}(I_\pm).
\tag{10}
\]

Such choices exist around any positive interior point of \(I_\pm\):
choose distinct positive centers for the \(r\) outer intervals, fix
the inner-prime center to make their product the selected point, and
then narrow the intervals. Select primes

\[
p\in[a_0X^{1/2},b_0X^{1/2}],\qquad
q_j\in[a_jX^{1/(2r)},b_jX^{1/(2r)}].
\tag{11}
\]

Every product \(n=pq_1\cdots q_r\) then obeys all of the following,
for every sufficiently large real \(X\):

* \(p>U\), \(m=q_1\cdots q_r>U\), and \(m\) is \(U\)-smooth;
* the roughness condition (6), hence \(A_U(m)=(-1)^r\), holds;
* \(n/X\in I_\pm\), retaining the full product cap;
* \(p\) is the **only prime factor of \(n\) exceeding \(U\)**.

The last fact matters: these products cannot disappear through another
factorization after the sum is grouped by \(n\). Their exact grouped
coefficient is \((-1)^r\log p\). Nor can they coincide with the
semiprime sector, which has two prime factors above \(U\).
Disjoint outer intervals make the factorization enumeration injective.

Only the ordinary prime number theorem is needed to count these boxes.
In a fixed-ratio prime interval \([aX^\alpha,bX^\alpha]\), the count
is asymptotic to \((b-a)X^\alpha/(\alpha\log X)\), and its
\(\log p\)-weighted count is asymptotic to \((b-a)X^\alpha\).
These follow by subtracting the endpoint asymptotics for \(\pi\) and
\(\theta\). For the classical input, see
[Tao, Notes 2, prime number theorem and Corollary 39](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/).
The box construction and deductions below are internal derivations.

Multiplying the \(r\) outer counts and the weighted inner count gives

\[
\sum_{\substack{p,q_1,\ldots,q_r\ \text{in (11)}}}\log p
\sim C_r\frac{X}{(\log X)^r},\qquad C_r>0.
\tag{12}
\]

Equations (9) and (12), including the normalization \(1/(q_0X)\),
show that the absolute scalar mass of this box is at least

\[
c_r(\log X)^{-r},\qquad c_r>0,
\tag{13}
\]

and its scalar sign is exactly \((-1)^r\) times the lobe sign.
This is an all-sufficiently-large-real-\(X\) statement, not a
subsequence or an average over shells. The constants and the effective
onset are not evaluated here.

Already \(r=2\) supplies both scalar signs, of mass
\(\gg(\log X)^{-2}\), entirely inside the smooth-cofactor sector.
Taking \(r=3\) supplies the opposite arithmetic sign on each lobe,
of mass \(\gg(\log X)^{-3}\). Thus neither an arithmetic-sign rule
alone nor a kernel-lobe-sign rule alone gives a one-sided scalar bound.

## 5. Exact sign deletion still fails with the continuum retained

Group (1) by its product before taking any signs:

\[
b_X(n)=\sum_{\substack{pm=n\\p>U,\ m>U}}A_U(m)\log p,
\quad
P_X=\frac1{q_0X}\sum_n[b_X(n)\ell(n/X)]_+,
\quad
N_X=\frac1{q_0X}\sum_n[-b_X(n)\ell(n/X)]_+.
\tag{14}
\]

Here \([z]_+=\max(z,0)\), and all sums retain the exact support.
Then, identically,

\[
J_0=c_wM_1(U)+P_X-N_X.
\tag{15}
\]

The two \(r=2\) boxes above prove

\[
P_X\ge c_+(\log X)^{-2},\qquad
N_X\ge c_-(\log X)^{-2}
\tag{16}
\]

for some fixed positive constants. These lower bounds hold even if (14)
is restricted to smooth outer factors. Because each box has only one
admissible inner prime, (16) is not an artifact of taking absolute values
before divisor or prime-factor cancellations.

The previous
[arithmetic-overlap note, Section 6](ARITHMETIC_OVERLAP_20261004.md)
establishes the unconditional logarithmic-quality cancellation
\(J_0=O_M((\log X)^{-M})\) for every fixed \(M\). It combines
classical quantitative PNT with the already-proved polynomially smaller
Vaughan and inner-prime-power errors. Take \(M>2\). The literal
pointwise sign-deletion bounds are

\[
J_0\le U_X:=c_wM_1(U)+P_X=J_0+N_X,
\]
\[
J_0\ge L_X:=c_wM_1(U)-N_X=J_0-P_X.
\tag{17}
\]

Their actual values therefore satisfy, eventually,

\[
\boxed{U_X\ge\tfrac12c_-(\log X)^{-2},\qquad
       L_X\le-\tfrac12c_+(\log X)^{-2}.}
\tag{18}
\]

For every fixed \(a>0\), these bounds cannot deliver
\(J_0\le C X^{-a}\) or \(J_0\ge-C X^{-a}\), respectively.
In a subpower formulation, take any \(0<\varepsilon<a\); the same
comparison defeats \(X^{-a+\varepsilon}\).

The continuum in (17) is exact. No independent estimate of \(M_1(U)\)
or assumption on its sign has been inserted. Equation (18) thus closes
the potential loophole that a small fixed \(c_w\) might cancel the
positive majorant to power accuracy. Any still larger pointwise upper
majorant, or still smaller pointwise lower minorant, has the same failure.
The width \(P_X+N_X\gg(\log X)^{-2}\) already quantifies the lost
signed information before using the known estimate for \(J_0\).

### Extension to the narrower scalar cutoffs

The same obstruction applies to the new balanced scalar cutoff from the
[prime-discrepancy centering note](PRIME_DISCREPANCY_CENTERING_20261004.md),
\(U=X^u\) with \(u=1/2-\kappa/28\), \(0<\kappa<14/29\).
To check the range directly, keep the boxes (11), so that
\(m\asymp X^{1/2}\) and \(q_j\asymp X^{1/(2r)}\). Smoothness
requires \(u>1/(2r)\), the short-cofactor reduction requires
\(u>1/2-1/(2r)\), and both retained factors exceed \(U\) when
\(u<1/2\). Consequently the \(r=2\) construction works throughout
\(1/4<u<1/2\), and the \(r=3\) construction works throughout
\(1/3<u<1/2\). The new cutoff has \(14/29<u<1/2\), so both
constructions, including their unique-large-prime grouped coefficients,
remain valid. Their constants and onset may depend on the fixed \(u\).

The logarithmic bound used in (18) also survives without invoking the
older norm-cutoff comparison. The new scalar-only Vaughan comparison
gives

\[
J_0(X;X^u)=\lambda_V(X)
+O_w\!\left(X^{-7}\{X^{7u}(1+\log X)+X^{14u}\}
+X^{-u/2}\log X\right),
\tag{19}
\]

where \(\lambda_V=(q_0X)^{-1}\sum_n\Lambda(n)\ell(n/X)\) and the
last term removes inner higher prime powers. For every fixed
\(0<u<1/2\), each error is polynomially decreasing. Classical
quantitative PNT and \(\int\ell=0\) give
\(\lambda_V=O_M((\log X)^{-M})\), hence the same bound for this
\(J_0\), for every fixed \(M\). At the new cutoff the mixed Vaughan
error is \(O(X^{-\kappa/2})\), which is more than enough for this
logarithmic comparison; no new power estimate for \(\lambda_V\) is
assumed. Thus (16)–(18) hold for the new balanced scalar cutoff as well
as the original cutoff. Narrowing the retained factor range does not
make either literal sign-deletion bound adequate.

## 6. What remains viable, and exact finite checks

This test excludes termwise sign deletion, absolute kernel replacement,
and majorants whose last step reduces to (17). It does **not** prove
that every sieve method fails, nor that the desired one-sided bound is
false. The bound concerns the small difference in (15), and an argument
that retains that difference can escape the obstruction. The exact
short-cofactor identity may still be useful for such a comparison, but
its simplest rough-smooth subfamily preserves Möbius parity rather than
removing it.

The [exact checker](../../../numerics/01_signed_arithmetic_covariance/check_smooth_sign_obstruction.py)
and its [record](../../../numerics/01_signed_arithmetic_covariance/smooth_sign_obstruction_record_20261004.json)
verify **81,043 finite arithmetic comparisons**: 36,855 short-cofactor
identities, 35,453 complementary-divisor identities, 7,920 roughness/parity
identities, one strict-endpoint example, and 814 grouped coefficients with
a unique retained large prime. Rational cutoffs and the actual algebraic
\(U=X^{11/24}\) at two noninteger real shells are included; algebraic
comparisons are evaluated exactly by raising to the 24th power.
Prime logarithms are represented formally by integer coefficient
dictionaries.

Run from the project root:

```sh
python3 papers/prime-variance-exponents/numerics/01_signed_arithmetic_covariance/check_smooth_sign_obstruction.py
```

These checks concern finite coefficient bookkeeping. The kernel-lobe
existence and the asymptotic box counts have the analytic proofs above;
the checks do not certify an asymptotic threshold or a new exponent.
