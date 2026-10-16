# Complete block covariance and the first arithmetic test

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not inferred. These are new internal
derivations and floating checks, not independent specialist refereeing.
No new global exponent is proved.

Subsequent [continuation](SIGNED_COVARIANCE_CONTINUATION_20261004.md)
sharpens the global target: the complete scalar bound alone, even for one
sign, implies the energy bound for the actual arithmetic response on all
real shells. The two-piece identities below remain exact shellwise, but a
separate projected-Gram theorem is no longer an independent global requirement.

## Outcome

The charter's first algebraic deliverable is completed: a common physical
block-Gram formula treats both retained Möbius cofactors and balanced
Vaughan blocks, with terminal bands and the continuum retained. The new
prime-place identity below supplies an actual arithmetic relation to test,
but its complete fixed-prime version only removes prime powers. This
prevents mistaking a formal Euler decomposition for a contraction.

This remains the first choice for investigation because its exact open
inequality is now accessible without imposing separate Möbius power bounds.
The preliminary calculation does not supply that inequality.

## 1. One physical kernel, all caps included

Use the fixed probe and A, B from the [overview](../../PROJECT_OVERVIEW_20261004.md).
Let I_X contain the integers in [AX,2BX]. Define dimensionless kernels

\[
\Omega(u,v)=\int_1^2 w(u/y)w(v/y)\,dy,\qquad
\ell(u)=\int_1^2 y w(u/y)\,dy,\qquad q_0=7/3.
\]

Let a_j(n) be any finite real block coefficients supported on I_X, and set
R_j(x)=sum_n a_j(n)w(n/x). All quantities are exact for every real X>0.
Substitution x=Xy gives

\[
G_{ij}=\langle R_i,R_j\rangle
=X\sum_{n,m\in I_X}a_i(n)a_j(m)\Omega(n/X,m/X),                 \tag{1}
\]
\[
s_j=\sum_{n\in I_X}a_j(n)\ell(n/X),\quad
\lambda_j=\frac{s_j}{q_0X},\quad
G^\perp_{ij}=G_{ij}-\frac X{q_0}s_is_j.                         \tag{2}
\]

Indeed <R_j,x>=X²s_j and ||x||²=q_0X³. Both G and G-perp are
positive semidefinite Gram matrices. Their entries can have either sign.
For every real continuum coefficient c,

\[
\boxed{\quad
\left\|\sum_j R_j+cx\right\|_2^2
=\mathbf1^TG^\perp\mathbf1
+q_0X^3\left(c+\sum_j\lambda_j\right)^2.
\quad}                                                       \tag{3}
\]

This follows by orthogonality, including all cross terms. It is not an
entrywise majorization. Thus the exact first-saving gate is

\[
\mathbf1^TG^\perp\mathbf1\ll X^{3-\kappa+o(1)},\qquad
\left|c+\sum_j\lambda_j\right|\ll X^{-\kappa/2+o(1)}.           \tag{4}
\]

Both are required. A small projected fluctuation alone does not control
the scalar mismatch. Bounds for the largest eigenvalue or the trace would
be stronger sufficient substitutes and must not be silently assumed.

### Cofactor specialization

Fix D=X^(9/10), N=floor(2BX), and K=floor(N/(floor(D)+1)). Partition the
integers 1,...,K into disjoint dyadic blocks I_j, including the last partial
block. The complete coefficients are

\[
a_j(n)=-\sum_{\substack{k\in I_j,\ k\mid n\\n/k>D}}
\mu(n/k)\log(n/k).                                           \tag{5}
\]

No condition is dropped when k is near K. Then sum_j R_j=R_X exactly
and c=0. The [proved reduction](../../MOBIUS_AND_BALANCED_VAUGHAN_REDUCTIONS_20261004.md)
gives ||V_g-R_X||=O(X^(9/10)log X)=o(X). Equation (4) is therefore
equivalent to the conditional first-saving target, using the overview's
endpoint recovery for subpower factors. The physical kernel retains every
Mellin frequency and needs no extra low-frequency exception.

### Vaughan specialization

Take U=V=X^(11/24), A_U(m)=sum_{d|m,d>U}mu(d). Partition m into
disjoint blocks J_j intersected with U<m<=2BX/V. Set

\[
b_j(r)=\sum_{\substack{m\in J_j,\ mn=r\\m>U,\ n>V}}
A_U(m)\Lambda(n),\qquad
c=c_wM_1(U).                                                  \tag{6}
\]

Use b_j in (1)–(4). The resulting response is exactly B_(U,V)+cx.
All prime powers in the inner Lambda remain. The parent norm error is
O(X); this is enough for every 0<kappa<=1. The identity convention is
also consistent with [Tao's Vaughan identity, Lemma 18](https://terrytao.wordpress.com/2015/01/10/254a-notes-3-the-large-sieve-and-the-bombieri-vinogradov-theorem/);
no distribution theorem from that source is being imported.

### Comparing the two coordinate systems

Let T_X=B_(U,V)+cx. The two established reductions imply
||R_X-T_X||=O(X). Orthogonal projection is contractive, hence

\[
\|P_{x^\perp}(R_X-T_X)\|=O(X),\qquad
|\lambda(R_X)-\lambda(T_X)|=O(X^{-1/2}).                        \tag{7}
\]

Here lambda(T_X)=sum_j lambda_j+c. The scalar error is within every
budget X^(-kappa/2), kappa<=1. Thus neither coordinate system can evade
the scalar obligation; it can only expose different arithmetic structure.
Individual block matrices in the two systems need not resemble each other.

## 2. Exact prime-place identity, and what it fails to prove

For a prime p, define

\[
C_k(D;x)=\sum_{d>D}\mu(d)\log d\,w(dk/x),
\]
\[
C_k^{(p)}(D;x)=\sum_{\substack{d>D\\p\nmid d}}\mu(d)\log d\,w(dk/x),
\qquad
M_k^{(p)}(D;x)=\sum_{\substack{d>D\\p\nmid d}}\mu(d)w(dk/x).
\]

Splitting d into p-coprime and p-divisible parts, using
mu(pe)=-mu(e) for p not dividing e and mu(pe)=0 when p divides e,
gives the exact relation

\[
\boxed{\quad C_k(D;x)=C_k^{(p)}(D;x)
-C_{pk}^{(p)}(D/p;x)-(\log p)M_{pk}^{(p)}(D/p;x).\quad}           \tag{8}
\]

If a comparison requires the same D on both sides, the complete annulus
D/p<e<=D must be restored. Its signed coefficient is
-mu(e)log(pe); it is not negligible by declaration. Every sum in (8) is
finite on the shell, with the product support supplying its own cap.

The following exact computation limits the most obvious use of (8).
With the full divisor sum (no D cutoff), restricting BOTH divisor and
cofactor to be coprime to p gives

\[
-\sum_{\substack{k,d\ge1\\p\nmid k d}}
\mu(d)\log d\,w(dk/x)
=V_g(x)-\sum_{a\ge1}(\log p)w(p^a/x).                         \tag{9}
\]

For p not dividing n the divisor identity is unchanged. Among n divisible
by p, Lambda(n) is nonzero only for n=p^a. On the whole shell the last sum
has at most 1+log(2B/A)/log p terms. For a fixed p it has O_{p,w}(1)
amplitude and O_{p,w}(sqrt X) shell norm. Excluding any fixed finite set
of primes likewise preserves every admissible superquadratic exponent.

This is a bookkeeping barrier, not a theorem excluding all prime-place
methods: complete removal of finitely many Euler places does not itself
produce a smaller retained energy. A useful application of (8) must
control a growing set of arithmetic overlaps or a genuinely signed
cross term, with the annuli and log-p terms charged. Simply iterating
the identity with triangle inequalities offers no contraction.

## 3. Finite diagnostic and effective-scale warning

The [support-program script](../../../numerics/10_finite_certificates_support/block_gram_preflight.py)
assembles (5), (6), their projected Gram summaries and (8), on real
shells X=1000.25 and 10000.5, at 128/256 quadrature nodes. The maximum
divisor-coefficient residual is 7.11e-15 and the maximum normalized
orthogonal-split residual is 2.29e-14. These are floating checks.

At 256 nodes, the Vaughan shape/scalar energies divided by X² are
respectively (1.79151,0.0212603) and (2.39159,0.00685392). This confirms
the relevance of recording both pieces; it does not establish their
asymptotic behavior.

The pure D=X^(9/10) cutoff discards energies about 30.66 X² and
127.40 X² on these two modest shells. The asymptotic o(X²) theorem has
large probe constants and does not promise small errors here. The earlier
pilot used a smaller cutoff prefactor. Neither the present finite growth
nor the earlier signed/trace ratios support an asymptotic exponent fit.

## 4. Targeted next investigation

Focus on (4) in the Vaughan coordinates, using (5)/(8) to expose the
Möbius arithmetic behind selected block cross terms. Use kappa=0.01 as
a concrete audit budget, not as a conjectured achievable value:

\[
\mathbf1^TG^\perp\mathbf1\ll X^{2.99+o(1)},\qquad
|c_wM_1(U)+\sum_j\lambda_j|\ll X^{-0.005+o(1)}.
\]

First derive one exact overlap identity after projection and its full
cutoff-annulus cost. Then determine whether its signed total offers any
positive saving beyond the generic cubic estimate. The acceptance gate
is an explicit all-real-X arithmetic inequality with one fixed positive
saving; a reduction to a separated power Mertens hypothesis, uncharged
scalar mismatch, or finite signed/trace ratio fails the gate. Stop and
record the obstruction if the identity only reconstructs (9).

The kappa value may be weakened; it may not drift to zero with X.
This bounded next investigation is more informative than a larger
unmotivated numerical sweep.
