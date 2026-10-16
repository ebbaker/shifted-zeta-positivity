# Preliminary investigation: an exact six-factor response

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Internal mathematical work and exact finite checks, not independent
specialist review. No new global exponent is proved.

## Outcome and scope

The first algebraic deliverable is available: a finite Heath–Brown identity
on the complete product band, a nonzero continuum term, and an explicit
centered response differing from the prime response by much less than the
quadratic norm allowance. The remaining problem is still a signed
arithmetic estimate. Three short Möbius factors do not by themselves
create cancellation. This makes program 05 a useful structural scout,
behind the three established arithmetic/Sonin/pair programs.

We use the [overview's probe](../../PROJECT_OVERVIEW_20261004.md) and the
[proved lattice lemma](../../MOBIUS_AND_BALANCED_VAUGHAN_REDUCTIONS_20261004.md),
which states

\[
\sum_{m\ge1}(\log m)w(m/y)=c_wy+O_g((1+|\log y|)y^{-5}),
\quad c_w=\int w(t)\log t\,dt\ne0. \tag{1}
\]

The primary source [Heath–Brown, *Sieve identities and gaps between primes*,
Lemma 1 and pp. 61–62](https://www.numdam.org/item/AST_1982__94__61_0.pdf)
supplies the finite Dirichlet-series identity and its coefficient expansion.
The cutoff and continuum calculation below is our application, with no
prime-gap estimate imported from that source.

## Fresh derivation: exact cutoff, signs, and product caps

Let \(\epsilon\) be the convolution identity, \(\mathbf1(n)=1\),
\(\mu_Y=\mu\mathbf1_{n\le Y}\), and
\(r_Y=\epsilon-\mathbf1*\mu_Y\). Since r_Y vanishes for every
integer n<=Y, the convolution binomial identity and
\(\Lambda*\mathbf1=\log\) give exactly

\[
\Lambda=
\sum_{j=1}^{K}(-1)^{j-1}\binom Kj
\mu_Y^{*j}*\mathbf1^{*(j-1)}*\log
+\Lambda*r_Y^{*K}. \tag{2}
\]

This follows by multiplying
\(\epsilon-r_Y^{*K}=\sum_{j=1}^{K}(-1)^{j-1}\binom Kj
(\mathbf1*\mu_Y)^{*j}\) by Lambda. In particular, there are j
Möbius variables, j-1 unrestricted unit variables, and one logarithmic
variable: 2j factors, not 2j+1.

Fix \(K=3\) and \(Y=(2BX)^{1/3}\). Every nonzero coefficient of
\(r_Y^{*3}\) is supported at
\(n\ge(\lfloor Y\rfloor+1)^3>2BX\). The remainder in (2)
therefore vanishes on the entire real shell product band. Define

\[
H_j(x)=
\sum_{\substack{d_1,\ldots,d_j\le Y\\ d_i\ge1}}
\mu(d_1)\cdots\mu(d_j)
\sum_{m_1,\ldots,m_j\ge1}(\log m_1)
w\!\left(\frac{d_1\cdots d_jm_1\cdots m_j}{x}\right).
\]

All sums are finite after the weight is applied. For X<=x<=2X,

\[
V_g(x)=3H_1(x)-3H_2(x)+H_3(x). \tag{3}
\]

Every tuple is restricted by
\(Ax\le d_1\cdots d_jm_1\cdots m_j\le Bx\).
Equivalently, the shell union lies in [AX,2BX], retaining the original
weight inside that band. Endpoint terms are zero. A decomposition into
dyadic boxes must keep this product condition in every terminal box;
its Dirichlet polynomial is not an unrestricted product of factor
polynomials. The identity applies to every real X; floor changes in Y
create no gap.

## Fresh derivation: retain the first continuum, discard only its error

Applying (1) with y=x/d gives

\[
H_1(x)=c_wxM_1(Y)+E_1(x),\qquad
M_1(Y)=\sum_{d\le Y}\frac{\mu(d)}d,
\]
\[
|E_1(x)|\ll_g X^{-5}\log X\sum_{d\le Y}d^5
\ll_g X^{-5}Y^6\log X\ll_g X^{-3}\log X.
\]

Consequently the complete retained response

\[
T_X(x):=H_3(x)-3H_2(x)+3c_wM_1(Y)x \tag{4}
\]

satisfies
\(\|V_g-T_X\|_{L^2(X,2X)}\ll_g X^{-5/2}\log X\).
This is an unconditional new reduction from the cited identity and the
inherited lattice lemma. No other continuum moment or multilinear sector
has been discarded: H_2 and H_3 retain all of theirs exactly.

By the triangle inequality, V_g and T_X have the same admissible shell
energy exponents in [2,3]. A proposed estimate
\(\|T_X\|_2^2\ll X^{3-\kappa+o(1)}\) still needs proof. The overview's
endpoint-transfer result then removes the subpower loss for V_g; it
does not generate a positive kappa.

Here is a fully explicit scalar/cross-term gate. Set
\(U_X=H_3-3H_2\),
\(\lambda_X=\langle U_X,x\rangle/\|x\|_2^2\), with
\(\|x\|_2^2=7X^3/3\). Orthogonality gives

\[
\|T_X\|_2^2=
\|U_X-\lambda_Xx\|_2^2+
\frac73X^3|\lambda_X+3c_wM_1(Y)|^2. \tag{5}
\]

Thus the two exact sufficient and necessary gates for this retained
response are

\[
\|U_X-\lambda_Xx\|_2^2\ll X^{3-\kappa+o(1)},\qquad
|\lambda_X+3c_wM_1(Y)|\ll X^{-\kappa/2+o(1)}. \tag{6}
\]

Within the first term,
\(\|U_X\|^2=\|H_3\|^2+9\|H_2\|^2-6\langle H_3,H_2\rangle\).
These signs and the scalar mismatch are part of the target. Dropping the
continuum or bounding the two H_j separately changes it.

## Exact diagnostic and source gate

The accompanying
[standard-library check](../../../numerics/05_higher_multilinear_identities/check_heath_brown_identity.py)
verifies (2) coefficient by coefficient using integer vectors of prime
logarithms. It tests both capped cases with zero remainder and deliberately
uncapped cases with a nonzero remainder; floating comparisons cannot hide
a sign or cutoff mistake. It is an algebra check, not a variance experiment
or an arithmetic certificate at unbounded X. Run it from the repository
root with Python 3; no generated large data are needed.

The recorded run passed 8,888 coefficient comparisons: (cap,Y,K) equal
to (256,16,2), (4096,16,3), (3000,10,3), (512,3,2), and (1024,5,4).
The third and fourth cases have a nonzero residual; the other three have
zero residual. All calculations use integers, with no symbolic-library
dependency or floating arithmetic.

The inspected [Type II source audit](../../BILINEAR_INPUT_SOURCE_AUDIT_20261004.md)
does not give a power estimate for this six-factor signed response.
For a new candidate theorem, the required interface is (6), including the
actual truncated Möbius variables, m_1's logarithm, full product caps,
and all low frequencies. A result for divisor coefficients after removing
the Möbius signs is insufficient. Termwise divisor bounds give
H_j=O(X^{1+o(1)}) and energy X^{3+o(1)}, recovering the original barrier.

Recommended bounded continuation: classify the K=3 product boxes by the
sizes of the unrestricted m_i, extract only sectors covered by the lattice
lemma, and determine whether the remaining cross-Gram matrix has a new
arithmetic relation absent from the balanced Vaughan form. Stop before
large computation if the only proposed input is a separated power Mertens
estimate or a theorem with incompatible coefficients. The identity is now
ready for that test, but does not yet justify promoting this branch into
the top three.
