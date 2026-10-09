# Signed gcd recombination of the original coprime core

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Same-model derivation and review are internal checks, not independent
specialist validation or formal proof replay.

Based on repository commit `480581447dcd3e93c9c2f9c22a050d9c5100ff9d`.
This continues [note 7](7_SHORT_FAMILY_CONTINUATION_20261008.md) and gives
a second exact way to preserve its prime/composite compensation.

## Exact recombination and a quantitative truncation

The coprime off-diagonal Möbius core equals an alternating sum of positive
moments with divisor masks. Truncating that signed divisor sum at \(Nd\le T\)
has error

\[
 O_\varepsilon\!\left(D^\varepsilon
 \left[H+\min\{HD/T,D^2/T^2\}\right]\right).
\tag{1}
\]

The \(H\) term includes the truncated diagonal. At the original row
scale, the lossless useful gcd cutoff is \(T=D^{1-h/2}\), rather than
the \(D^{1/2}\) cutoff for the different transformed kernel in note 4.
The divisor-one term of the recombination is exactly the original full
moment, so triangle-bounding the positive moments does not prove a
smaller exponent. The new result is the exact signed target and its
controlled truncation, not a bound for that target.

## Divisor masks and the coprime identity

Keep the fixed data, profile and nonnegative row weight of note 2. Write

\[
 x_u(n)=\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\]

and define

\[
 B_d(D,H)=\frac1D\sum_{u\ne0}\Phi(Nu/H)
             \left|\sum_{d\mid n}x_u(n)\right|^2\ge0.
\tag{2}
\]

All column ideals are prime to \(S\); squarefreeness follows from
\(\mu_K(n)\). The original coprime off-diagonal form is

\[
 C(D,H)=\frac1D\sum_{u\ne0}\Phi(Nu/H)
       \sum_{\substack{n_1\ne n_2\\(n_1,n_2)=1}}
             x_u(n_1)\overline{x_u(n_2)}.
\tag{3}
\]

For sufficiently large \(D\), the unit column is absent. Inclusion--
exclusion gives the exact identity

\[
 \boxed{ C(D,H)=\sum_d\mu_K(d)B_d(D,H). }
\tag{4}
\]

Indeed the coefficient of each pair is
\(\sum_{d\mid(n_1,n_2)}\mu_K(d)=\mathbf1_{(n_1,n_2)=1}\).
A surviving diagonal would have \(n_1=n_2=1\), which is off the profile.
There is no absolute convergence issue: all divisors have \(Nd\le CD\),
where \([c,C]\) contains the profile support, and the row weight is
Schwartz.

For squarefree \(d\), multiplicativity gives

\[
 \sum_{d\mid n}x_u(n)=
 \mu_K(d)\nu(d)\chi_d(u)
 \sum_{(m,dS)=1}\mu_K(m)\nu(m)\chi_m(u)
                     W(Nm/(D/Nd)).
\tag{5}
\]

The column mask \((m,d)=1\) and the row mask
\(|\chi_d(u)|^2=\mathbf1_{(u,d)=1}\) are both retained.
For squarefree \(d\), if \(\mathfrak M_d(L,H)\) denotes the normalized moment of the inner
sum with that row mask and normalization \(1/L\), then

\[
 B_d(D,H)=\frac1{Nd}\mathfrak M_d(D/Nd,H).
\tag{6}
\]

The row parameter stays \(H\); it does not change to \((D/Nd)^h\).
An estimate at one fixed family exponent is therefore not automatically
an estimate for every moment on the right of (6).

## The original high-gcd tail

For distinct squarefree columns \(n_1,n_2\), put
\(g=(n_1,n_2)\), \(G=Ng\), and

\[
 \psi=\chi_{n_1/g}\overline{\chi_{n_2/g}},\qquad
 Q=N(n_1n_2)/G^2.
\]

The character \(\psi\) is nonprincipal primitive at the good conductor,
and the original row kernel is

\[
 K_H(n_1,n_2)=\sum_{u\ne0}\Phi(Nu/H)
                   \psi(u)\mathbf1_{(u,g)=1}.
\tag{7}
\]

The all-scale argument of note 4 now applies with row scale \(H\),
giving

\[
 |K_H(n_1,n_2)|\ll_\varepsilon
 D^\varepsilon\min\{H,\sqrt Q\}
 \ll_\varepsilon D^\varepsilon\min\{H,D/G\}.
\tag{8}
\]

The conductor and masked Poisson formulas are the same imported inputs
as in notes 2--4. Nonprincipality removes the zero frequency. Lattice
counting gives the \(H\) branch because \(H\ge1\); primitive completion
and a divisor expansion of the mask give the second branch.

For \(G\le Ng<2G\), ideal counting gives \(O(D^2/G)\) column pairs.
After division by \(D\), their full absolute contribution is at most

\[
 D^\varepsilon\min\{HD/G,D^2/G^2\}.
\tag{9}
\]

Any column-pair selector independent of \(u\), of size \(D^\varepsilon\),
can be inserted in (9) without altering its power budget. Summing
dyadic gcd blocks \(Ng>T\) gives the same expression with \(G=T\),
up to epsilon and fixed support constants.

## Truncation including its diagonal

For \(T\ge1\), set

\[
 S_T(D,H)=\sum_{Nd\le T}\mu_K(d)B_d(D,H),\qquad
 \sigma_T(g)=\sum_{\substack{d\mid g\\Nd\le T}}\mu_K(d).
\]

For \(Ng\le T\), \(\sigma_T(g)=\mathbf1_{g=1}\). For \(Ng>T\),
\(|\sigma_T(g)|\le\tau(g)\ll_\varepsilon D^\varepsilon\).
Therefore the off-diagonal difference \(S_T-C\) is bounded by the
tail (9). Its diagonal is

\[
 \frac1D\sum_n |\mu_K(n)\nu(n)W(Nn/D)|^2\sigma_T(n)
           \sum_{u\ne0}\Phi(Nu/H)\mathbf1_{(u,n)=1},
\]

which is \(O_\varepsilon(HD^\varepsilon)\) by ideal counting,
lattice counting and the divisor bound. It need not be zero when the
divisor sum is truncated. This proves (1).

In particular, with \(H=D^h\), \(0<h<1\), \(a\ge0\), either of

\[
 T\ge D^{1-a},\qquad
 T\ge D^{1-(h+a)/2}
\tag{10}
\]

is sufficient to put the error inside \(D^{h+a+\varepsilon}\).
When \(a<h\), the second is the smaller cutoff.
With \(a=0\), the exact exponents are

| \(h\) | Original gcd truncation exponent \(1-h/2\) |
| --- | --- |
| \(8/9\) | \(5/9\) |
| \(4/5\) | \(3/5\) |
| \(2/3\) | \(2/3\) |

For \(h>1/2\), truncating this original divisor recombination at
\(T=D^{1/2}\) gives only \(O(D^{1+\varepsilon})\) from (1).
It cannot inherit the transformed overlap threshold by changing the
name of the gcd variable.

## What the signed target requires

The \(d=1\) summand of (4) is \(B_1=\mathfrak M(D,H)\).
Consequently (4) is a useful preservation of compensation, but a
triangle bound containing \(B_1\) is circular. Neither positivity nor
the change of column scale in (6) removes that term.

There is also an exact local description of the compensation. Put
\(\lambda_u(n)=\nu(n)\chi_n(u)\) and \(a_p=\lambda_u(p)\). For \(\Re s,\Re t>1\),

\[
 \sum_{(m,n)=1}\frac{\mu_K(m)\mu_K(n)
                 \lambda_u(m)\overline{\lambda_u(n)}}{(Nm)^s(Nn)^t}
 =\prod_{p\notin S}(1-a_p(Np)^{-s}-\overline{a_p}(Np)^{-t}).
\tag{11}
\]

The absent local mixed term enforces coprimality, including every zero
at a prime dividing \(u\). This product is not a new estimate for
smooth sums outside its domain of absolute convergence.

As a finite exact diagnostic, let columns be all squarefree divisors
of a product of \(k\) primes, use \(W=1\), and require \(a_p=1\)
on those primes, as for a coherent row with trivial twist.
The coprime pair total, including its unit column and diagonal, is
\(\prod_{p}(1-1-1)=(-1)^k\). The distinct prime-only pair total is
\(k(k-1)\). This finite divisor test demonstrates compensation; it has
no annular support or asymptotic force and is not a model for prime
distribution.

The [factorization in note 8](8_SHORT_FAMILY_CENTERED_FACTORIZATION_20261008.md)
provides an actual centered sector estimate and a different residual
target. The gcd identity here supplies an exact comparison and a
cutoff check for candidate arguments. The unrestricted signed core,
its extension to all transformed cofactors, and a new short-family
moment remain open.

The [exact checker](../../numerics/check_short_family_factorization.py)
and [scoped review](../../reviews/SHORT_FAMILY_FACTORIZATION_REVIEW_20261008.md)
cover the finite recombination and exponent budgets, with the imported
analytic inputs and their limits explicitly separated.
