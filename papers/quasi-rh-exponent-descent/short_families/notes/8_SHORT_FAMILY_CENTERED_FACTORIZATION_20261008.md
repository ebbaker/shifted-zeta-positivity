# Exact Möbius factorization and a controlled centered small product

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Derivations and separate same-model review are internal checks, not
independent specialist validation or formal proof replay.

Based on repository commit `480581447dcd3e93c9c2f9c22a050d9c5100ff9d`.
This continues [note 7](7_SHORT_FAMILY_CONTINUATION_20261008.md).

## Result and relation to the remaining core

An exact truncated Dirichlet-inverse identity preserves the Möbius
cancellation before the short-family square is expanded. In its two-factor
form, the part with small product of the two Möbius factors has a controlled
mean square **after its principal-character main term is subtracted**.
For a product cutoff \(Y\), every fixed \(A\ge0\) gives

\[
 \mathcal E_I(D,H;Y)\ll_\varepsilon
 D^\varepsilon\frac{H^2Y^2}{D}\left(\frac{HY}{D}\right)^{2A},\qquad 1\le H\le D.
\tag{1}
\]

In particular, fix \(0<\eta<1-h\). The choice

\[
 H=D^h,\qquad Y=D^{1-h-\eta}
\tag{2}
\]

makes this centered energy \(O_L(D^{-L})\) for every requested
\(L>0\), choosing the transform decay order first. The principal main
term has not been discarded. The weaker \(A=0\) bound also covers
the boundary range \(2y+h-1\le a\) without a strict separation.

The new sufficient target is the moment of the complementary convolution
sum **plus the explicitly retained principal main term**. Those terms must
remain together. No bound for that recombined target is proved here.
This is an alternative reduction of the original full moment; the product
cutoff is not a selector that can simply be inserted into the transformed
low-overlap residual of note 4.

## The exact ideal identity and its support boundary

All convolutions below are on integral ideals prime to the fixed set \(S\).
Write \(\delta\) for the identity of Dirichlet convolution, \(\mathbf1\)
for the constant-one function on this monoid, and

\[
 m_z(n)=\mu_K(n)\mathbf1_{Nn\le z},\qquad
 r_z=\delta-\mathbf1*m_z,\qquad z\ge1.
\]

Since \(\mathbf1*\mu_K=\delta\), every ideal in the support of \(r_z\)
has norm strictly greater than \(z\). Expanding a finite binomial gives

\[
 \mu_K=
 \sum_{j=1}^{J}(-1)^{j-1}\binom Jj
 m_z^{*j}*\mathbf1^{*(j-1)}
 +\mu_K*r_z^{*J}.
\tag{3}
\]

Every nonzero coefficient of the last term has norm strictly greater
than \(z^J\). Consequently the first sum equals \(\mu_K(n)\) for
**every \(Nn\le z^J\), including the endpoint**. This proof needs no
prime distribution theorem or zero-free region.

Fix \(\operatorname{supp}W\subset[c,C]\subset(0,\infty)\). The legal
profile choice is \(z^J\ge CD\); taking \(z=D^{1/J}\) without checking
\(C\le1\) would leave an uncovered part of the profile.

For \(u\ne0\), define on all good ideals

\[
 \lambda_u(n)=\nu(n)\chi_n(u).
\tag{4}
\]

The denominator symbol is extended multiplicatively, so \(\lambda_u\)
is completely multiplicative, including its zero values. In particular
\(\lambda_u(ab)=\lambda_u(a)\lambda_u(b)\) even when \(a,b\) share
primes, and it vanishes at primes dividing \(u\). Multiplication by
\(\lambda_u\) therefore commutes with all the convolutions in (3).
The source convention is the multiplicative denominator extension in
the [October 5 TeX source](https://raw.githubusercontent.com/openai/math/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
Section 2. We factor the original coefficients, not the differently
twisted Gauss coefficients \(a_\xi\).

There is no squarefree restriction on the individual free factors in
(3), and no extra pairwise coprimality restriction. The signed identity
itself makes the final coefficient zero at nonsquarefree ideals.
For example, in the two-factor identity at \(p^2\le z^2\), the three
divisor contributions \(1,-2,1\) sum to zero. Discarding their overlaps
destroys this cancellation.

## Two Möbius factors give an exact short-family amplitude

Take \(J=2\), \(z=(CD)^{1/2}\), and \(D\) sufficiently large that
\(cD>z\). Put \(c_z=m_z*m_z\). On the entire profile, \(m_z(n)=0\),
so (3) becomes

\[
 \mu_K(n)=-(c_z*\mathbf1)(n).
\tag{5}
\]

Let

\[
 S_u(L)=\sum_{(m,S)=1}\lambda_u(m)W(Nm/L).
\]

The original amplitude has the exact factorization

\[
 A_u(D)=-\sum_d c_z(d)\lambda_u(d)S_u(D/Nd).
\tag{6}
\]

All sums are finite. Only \(Nd\le CD\) can contribute, and
\(|c_z(d)|\le\tau(d)\). Split (6) as \(A_u=I_u+T_u\), where

\[
 I_u=-\sum_{Nd\le Y}c_z(d)\lambda_u(d)S_u(D/Nd),\qquad
 T_u=-\sum_{Nd>Y}c_z(d)\lambda_u(d)S_u(D/Nd).
\tag{7}
\]

For \(Y\le z\), the small-product coefficient simplifies further:
\(c_z(d)=(\mu_K*\mu_K)(d)\) for \(Nd\le Y\). No individual
factor cutoff remains in that part. The larger product retains both
conditions \(Na,Nb\le z\) in \(d=ab\).

## Completion with the principal main term retained

Reciprocity presents the column character \(\lambda_u\) as an induced
finite-order Hecke character, with primitive conductor \(\mathfrak q_u\)
and additional excluded primes. Its conductor norm satisfies

\[
 Q_u=N\mathfrak q_u\ll_{\nu,S}Nu.
\tag{8}
\]

At good primes, exponents of \(u\) are reduced modulo six: nonzero
exponents give conductor exponent one, and exponents divisible by six
leave a deletion mask. Factors at the fixed bad primes and supplementary
reciprocity factors have bounded conductor. The additional excluded
ideal \(E_u\), after primes already in the conductor are removed, is
squarefree. More precisely, its support is disjoint from the conductor,
and the combined modulus satisfies

\[
 Q_uNE_u\ll_{\nu,S}Nu.
\tag{8a}
\]

At good primes the conductor or the additional mask uses each prime
at most once; their product divides \(\operatorname{rad}(u)\).
The fixed bad part changes only the implied constant. This combined
bound, rather than the weaker two separate norm bounds, is essential
for rapid decay below.

Define \(\kappa_u\) as the residue at \(s=1\) of

\[
 \sum_{(m,S)=1}\frac{\lambda_u(m)}{(Nm)^s}.
\tag{9}
\]

It is zero unless the inducing Hecke character is principal. In that
case the character on good ideals is exactly the surviving-prime
indicator, and

\[
 \kappa_u=\operatorname*{res}_{s=1}\zeta_K(s)
 \prod_{p\mid S(u)}(1-(Np)^{-1}),
\tag{10}
\]

where the product is over the distinct primes in \(S\) or dividing
\((u)\). Set \(I_W=\int_0^\infty W(t)\,dt\), with no conjugation.
Primitive lattice Poisson, including its zero frequency, gives the
all-scale estimate

\[
 S_u(L)=\kappa_u L I_W+E_u(L),\qquad
 |E_u(L)|\ll_{\nu,S,W,A,\varepsilon}(Nu)^{1/2+\varepsilon}
              \left(\frac{Nu}{L}\right)^A
 \quad(L>0,\ A\ge0).
\tag{11}
\]

Here is the uniform completion argument. Lift the ideal character to
the Eisenstein lattice and divide by the six unit representatives;
the ideal character is trivial on units. Expand the extra zero mask by
divisors of \(E_u\). For each divisor \(e\), the nonzero-frequency
Poisson prefactor has size \(L/(Ne\sqrt{Q_u})\), and its norm frequency
scale is \(t=L/(NeQ_u)\). A fixed radial Schwartz transform satisfies

\[
 \sum_{k\ne0}|\widehat W(tNk)|\ll_W t^{-1}\qquad(t>0).
\tag{12}
\]

Thus each divisor costs \(O_W(\sqrt{Q_u})\), uniformly in \(L\).
For \(t\ge1\), Schwartz decay improves this to
\(O_{W,A}(\sqrt{Q_u}t^{-A})\); for \(t<1\), the same inequality
follows from \(t^{-A}\ge1\). Equation (8a) bounds
\(t^{-A}=(NeQ_u/L)^A\) by a fixed constant times \((Nu/L)^A\).
The number of divisors is \(O_\varepsilon((Nu)^\varepsilon)\).
The zero frequency is absent for a nonprincipal inducing character;
for the principal character it is exactly (10) times \(LI_W\).
This proves (11). The finite reciprocity and primitive Gauss/Poisson
formulas are imported arithmetic inputs, as in notes 2--4; the all-scale
estimate and the convolution reduction are deductions from them. The
source's Lemma 4.2 explicitly retains the principal zero frequency.

## The centered estimate and the new sufficient target

Keep the main term of \(I_u\) explicitly:

\[
 P_u=-\kappa_u D I_W
       \sum_{Nd\le Y}\frac{c_z(d)\lambda_u(d)}{Nd},\qquad
 I_u^c=I_u-P_u.
\tag{13}
\]

Equations (7) and (11), the divisor bound, and ideal counting give

\[
 |I_u^c|\ll_{A,\varepsilon}
 Y^{1+\varepsilon}(Nu)^{1/2+\varepsilon}
          \left(\frac{Nu\,Y}{D}\right)^A.
\tag{14}
\]

For the same fixed nonnegative Schwartz row weight as note 2,
lattice counting yields

\[
 \frac1D\sum_{u\ne0}\Phi(Nu/H)|I_u^c|^2
 \ll_{A,\varepsilon}D^{-1}Y^{2+\varepsilon}H^{2+\varepsilon}\left(\frac{HY}{D}\right)^{2A}.
\tag{15}
\]

This proves (1), reallocating epsilon and using \(Y\ll D\), \(H\le D\).
The zero row is omitted throughout; its original amplitude vanishes
for sufficiently large \(D\) because the unit column is off the profile.

Define the recombined residual by

\[
 R_u=T_u+P_u,\qquad A_u=I_u^c+R_u.
\tag{16}
\]

For \(Y\) chosen as in (2), or more generally
\(Y=D^y\) with \(2y+h-1\le a\), the elementary inequalities in both
directions, \( |A|^2\le2|I^c|^2+2|R|^2\) and
\(|R|^2\le2|A|^2+2|I^c|^2\), prove the equivalence

\[
 \boxed{
 \mathfrak M(D,D^h)\ll_\varepsilon D^{h+a+\varepsilon}
 \quad\Longleftrightarrow\quad
 \frac1D\sum_{u\ne0}\Phi(Nu/D^h)|R_u|^2
       \ll_\varepsilon D^{h+a+\varepsilon}.}
\tag{17}
\]

Both statements have the arbitrary-epsilon quantifier and the same fixed
arithmetic data and profile. The negligible-error cutoff and, separately,
the unbuffered lossless cutoff obtained with \(A=0\) are

| \(h\) | Negligible-error \(y=1-h-\eta\) | Lossless \(A=0\) boundary |
| --- | --- | --- |
| \(8/9\) | \(1/9-\eta\) | \(1/18\) |
| \(4/5\) | \(1/5-\eta\) | \(1/10\) |
| \(2/3\) | \(1/3-\eta\) | \(1/6\) |

For \(y=1-h-\eta\), the prefactor in (15) is
\(D^{1-2\eta+\varepsilon}\), and its decay factor is
\(D^{-2A\eta}\). This proves arbitrary power decay by choosing
\(A\) in terms of the requested error, \(\eta\), and a preliminary
epsilon. The higher moments of the fixed Schwartz row weight are
absorbed in the implied constant; no sharp truncation at \(Nu=H\)
is being made. The larger-product
sum still contains ranges with free factor of bounded length, including
\(m=1\). Equation (17) provides no bound for those ranges.

On principal-induced rows, \(T_u\) and \(P_u\) may be large separately.
The equivalence deliberately preserves their cancellation. Bounding
each by the desired moment, deleting nonsquarefree convolution products,
or treating the original transformed \(a_\xi\) as completely
multiplicative would require a different argument and is not licensed
by this reduction.

## Next estimate and verification

The bounded next analytic task is the full moment on the right of (17),
first at \(h=4/5\) with \(a<1/12\), taking
\(Y=D^{1/5-\eta}\), \(0<\eta<1/5\). It retains all overlapping factor
tuples, all column deletion masks, the smooth profile, and the principal
correction inside the square. It cannot be replaced by separately
estimating selected prime/composite pieces, which already fail the
obstruction in note 3. A direct proof of this full moment would bypass the need to
estimate each transformed \(b,f,G\) block separately.

The [exact checker](../../numerics/check_short_family_factorization.py)
tests finite ideal convolution, endpoint support, complex twists and
zero masks, nonsquarefree cancellation, principal centering, gcd
recombination, and rational budgets. The
[scoped review](../../reviews/SHORT_FAMILY_FACTORIZATION_REVIEW_20261008.md)
records the analytic and finite-check scope. Neither establishes the
moment in (17), a new zero-free boundary, or RH descent.
