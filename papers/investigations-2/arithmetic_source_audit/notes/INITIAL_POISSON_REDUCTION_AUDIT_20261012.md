# Initial Poisson reduction and dual range audit

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration. The serving variant
and configured reasoning effort are not exposed and are not inferred.
Internal mathematical review; not independent specialist validation or
formal verification.

## Source and conclusion

Pinned [October 5 source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex):
`paper2.tex` at openai/math commit
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, manuscript date
5 October 2026, SHA-256
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
Source bytes were rehashed for this audit. Physical line numbers below
refer to that exact source.

I inspected the full proof of `prop:poisson-reduction`, lines 1000–1255,
together with `lem:poisson`, `lem:remove-exclusions`,
`lem:smooth-mean-square`, and the initial positive-gap argument, lines
1613–1629. The paired Gauss conversion is checked algebraically
conditional on the stated arithmetic lemma; the arithmetic lemma itself
is checked in the [companion arithmetic audit](INITIAL_ARITHMETIC_CONVERSION_AUDIT_20261012.md).

**Scoped finding:** no unresolved defect was established in the initial
Poisson reduction. The conductor, complete diagonal, shared column
factors, residual masks, smooth norms, Cauchy losses, and dual ranges are
consistent. In particular, a common factor in the columns does not create
a new primitive conductor that is then silently discarded: it is removed
by finite Möbius inversion *after* Poisson, and its exact effects are
retained until the bijective change of variables. This result remains
conditional on the auxiliary energy estimate and its upstream analytic
proof.

## Primitive conductor and the diagonal

After writing `n_j=g z_j`, both residual columns are squarefree and
`(z_1,z_2)=(z_1 z_2,g)=1`. The primitive character is

\[
\chi=\overline{\chi_{z_1}}\chi_{z_2}.
\]

Every prime dividing either residual column carries a nontrivial local
sextic character (or its inverse), so the primitive conductor is exactly
`z_1 z_2`. Outside the fixed excluded primes above 2 and 3, the
finite residue fields contain the sixth roots of unity and the local
sextic character has order six. Coprimality of the residual columns
precludes local cancellation. Thus no missing conductor-lowering factor
is present at this stage.

The identity

\[
\overline{\chi_{g z_1}(u)}\chi_{g z_2}(u)
=\mathbf1_{(u,g)=1}\overline{\chi_{z_1}(u)}\chi_{z_2}(u)
\]

retains the shared column factor as a row exclusion. Since this
exclusion is disjoint from the primitive conductor, its inclusion–
exclusion coefficient is `mu(e) chi(e)/N(e)`, not `mu(e)`
alone.

The primitive character is principal exactly when `z_1=z_2=1`.
Its zero Fourier coefficient gives the full diagonal

\[
Z={H\over D}\widehat\Phi(0)
\sum_g^* |W(N(g)/D)|^2
\prod_{p\mid g}(1-N(p)^{-1}).
\]

There are `O_I(D)` supported ideals `g`, so
`Z <<_{I,Phi} H ||W||_infinity^2`. This uses only ideal counting.
The source explicitly retains every nonzero frequency in this principal
case. Discarding its nonzero frequencies would change the exact identity;
the source retains them.

The original sum is over nonzero rows. Its nonnegative majorant includes
`u=0`, which is harmless: all terms are nonnegative before square
expansion, so this is an upper bound. The principal conductor-one
Poisson convention has `chi(0)=1`; nonprincipal primitive characters
have `chi(0)=0`. These conventions account for the zero mode above.

## Poisson normalization

The additive pairing `e(z w)` with
`e(z)=exp(4 pi i Im(z)/sqrt(3))` makes `O=Z[omega]`
self-dual under the measure `(2/sqrt(3)) dx dy`. Summing on residue
classes modulo a generator `m` gives

\[
\sum_\ell\chi(\ell)\Phi(N(\ell)/T)
={T\gamma(\chi)\over\sqrt{N(m)}}
 \sum_h\overline{\chi(h)}\,
 \widehat\Phi(TN(h)/N(m)).
\]

Setting `u=e ell` replaces `T` by `H/N(e)`, giving
exactly the denominator and Fourier argument displayed in
`eq:initial-poisson-rows`.

A nonnegative radial Schwartz majorant with compactly supported Fourier
transform exists. For example, take a real radial inverse transform of
a smooth even bump supported in a sufficiently small frequency ball,
choose the ball small enough that this inverse transform is positive
on the unit spatial ball, square it, and multiply by a fixed scalar.
The square is nonnegative and Schwartz; its Fourier transform is a
compactly supported convolution. Thus the compact dual cutoff is an
exact cutoff, and the proof has no omitted high-frequency tail.

## Paired Gauss conversion and the factor N(g)

By CRT,

\[
\gamma(\overline{\chi_{z_1}}\chi_{z_2})
=\gamma_{-1}(z_1)\gamma_1(z_2)\,
  \overline{\chi_{z_1}(z_2)}\chi_{z_2}(z_1).
\]

The last two characters give the reciprocity sign
`R(z_1,z_2)`. Combining `eq:convert1`,
`eq:convert2`, and `eq:quotient` gives

\[
\mu(z_1)\mu(z_2)\overline{\nu(z_1)}\nu(z_2)
\gamma(\overline{\chi_{z_1}}\chi_{z_2})
=a_0(z_1)\overline{a_0(z_2)}\,
 \overline{\nu(t)}G(t^{-1}),\quad t=z_1 z_2^{-1},
\]

where `a_0=overline(alpha) gamma_2`. Expanding the fixed
ray-class function in characters therefore yields the source's
`a_xi(z_1) overline(a_xi(z_2))` with the stated orientation.

Let `W_0(x)=x^{-1/2} overline(W(x))`. Its paired product is

\[
W_0(N(gz_1)/D)\overline{W_0(N(gz_2)/D)}
={D\over N(g)\sqrt{N(z_1)N(z_2)}}
 \overline{W(N(gz_1)/D)}W(N(gz_2)/D).
\]

Hence the exterior coefficient `H N(g)/(D^2 N(e))`
recovers exactly `H/(D N(e) sqrt(N(z_1)N(z_2)))`,
including the original normalization `1/D`. The shared column
factor costs neither an extra `N(g)` nor its reciprocal.

## Removing residual column coprimality

The paired Gauss formula is only asserted on coprime residual columns.
That is sufficient. The source first has an expression with those
columns restricted to be coprime, then extends its explicitly defined
`a_xi` expression off the coprime locus while multiplying by

\[
\mathbf1_{(z_1,z_2)=1}
=\sum_{v\mid z_1,\,v\mid z_2}\mu(v).
\]

One does not need the primitive Gauss identity to continue to hold for
the artificially introduced noncoprime pairs.

Putting `z_j=v m_j` retains
`(m_1 m_2,g v)=1`, while `(m_1,m_2)` becomes unrestricted.
The coefficient identity and character multiplicativity yield

\[
a_\xi(vm)=a_\xi(v)a_\xi(m)\chi_m(v)^4,
\qquad
|a_\xi(v)\chi_v(h e^5)|^2=\mathbf1_{(v,h)=1},
\]

because `(v,e)=1`. This mask is essential. It is carried forward
and later determines the inverse mapping.

The change of variables

\[
b=g/e,\quad f=e v,\quad k=e h
\]

is bijective from the displayed original domain to coprime squarefree
`b,f` and arbitrary nonzero `k`. Indeed, in the forward
direction `(v,h)=1` and squarefreeness of `f` force
`e=gcd(f,k)`. Conversely, define

\[
e=\gcd(f,k),\quad v=f/e,\quad g=b e,\quad h=k/e.
\]

The squarefree factorization of `f` gives `(v,h)=1`,
and `(b,f)=1` gives every remaining required coprimality.
Here gcd ideals use their fixed primary generators; products of
primary generators remain primary, so no untracked unit enters.

All identities needed for this substitution are exact:

\[
g v=b f,\quad h e^5 v^4=k f^4,\quad
\mu(e)\mu(v)=\mu(f),\quad N(g)/N(e)=N(b),
\]

and

\[
{H N(h)\over N(e)N(v)^2N(m_1)N(m_2)}
={H N(k)\over N(f)^2N(m_1)N(m_2)}.
\]

The column condition `(m_j,f)=1` is enforced by the zero
extension of `chi_{m_j}(f)^4`; the explicit remaining condition
is precisely `(m_j,b)=1`. No squarefree common column factor or
row mask is suppressed.

## Exclusion removal and the Cauchy factors

For fixed `b`, inclusion–exclusion on `(n,b)=1` writes the
column sum as a divisor sum indexed by squarefree `d|b`.
Terms with `(d,f) !=1` vanish. For the surviving terms,
`n=d m` gives

\[
a_\xi(dm)\chi_{dm}(k)\chi_{dm}(f)^4
=a_\xi(d)\chi_d(k)\chi_d(f)^4\,
 a_\xi(m)\chi_m(k)\chi_m(d f)^4.
\]

The right-hand character mask also enforces `(m,d)=1`.
Every exterior coefficient has modulus at most one. Cauchy in the
divisor index contributes `tau_div(b)`; enlarging the injective
image `f -> d f` contributes no multiplicity. The image is
squarefree because `(d,f)=1`.

The scales change to

\[
(X,F)\longmapsto(X/N(d),F N(d)).
\]

Both `X F` and the initial `B` remain fixed, so the initial
row bound and the equation `X=D/(B F)` are preserved. The
second divisor count in summing the energy comparisons gives at most
`tau_div(b)^2`. Since `N(b)<<_I D`, this is absorbed by the
reserved arbitrarily small power of `D`.

The resulting common-test bound is

\[
\sum_{f,k}|S_U(b,f,k)|^2
\ll D^{\varepsilon/2}(X F)^2\|U\|_{C^J}^2.
\]

The square of `XF` is correct: one factor comes from undoing
the energy normalization, the other from the assumed target
`E << D^epsilon XF`. No further Cauchy factor in `f`
or `k` is taken.

## Smooth weights and initial ranges

For a dyadic block `B<=N(b)<2B`, `F<=N(f)<2F`, let
`X=D/(B F)`. The kernel is

\[
\mathcal K_{b,f,k}(x_1,x_2)
=W_0(r x_1)\overline{W_0(r x_2)}
\widehat\Phi(a/(x_1 x_2)),
\]

with `1<=r<4` and
`0<a=H N(k)/(N(f)^2 X^2)<=C_{I,Phi}`.
Its support lies in `[a_0/4,b_0]^2`, away from zero, and
the chain rule gives a uniform `C^q` bound by
`C_{I,Phi,q} ||W||_{C^q}^2`.

The row-dependent kernel cannot be replaced by an arbitrary individual
test in each row using the common-test estimate alone.
`lem:smooth-mean-square` correctly supplies the missing step:
its Mellin coefficients have a common pointwise decay bound, and
Cauchy in the rows is applied only after taking that common bound.
The integral

\[
\iint {(1+|s|)^J(1+|t|)^J\over
 (1+|s|+|t|)^{2J+4}}\,ds\,dt
\]

converges. Thus the required derivative order is `q=2J+4`.
The coefficient `mu(f) 1_{(f,b)=1}` has modulus at most one,
so this application loses no row count.

Support yields

\[
N(b)N(f)\le b_0 D,\qquad
0<N(k)\le C_\Phi b_0^2 D^2/(H N(b)^2).
\]

There are only `O_I((log D)^2)` nonempty dyadic blocks.
The exterior `b` count is `O(B)`, and therefore

\[
{H\over D^2}\sum_{N(b)\asymp B}N(b)(XF)^2
\ll {H\over D^2} B^2(D/B)^2=H.
\]

This is the precise cancellation of the common-column-factor cost.
It uses only ideal counting and the energy bound for each fixed
exclusion ideal.

Finally,

\[
\mathcal H\le C D^{1-\vartheta}/B^2,
\quad\Sigma=XF=D/B,
\quad{\mathcal H\over\Sigma}
\le C D^{-\vartheta}/B\le C D^{-\vartheta}.
\]

For sufficiently large `D`, this supplies
`kappa=vartheta/2`; `Sigma<=D` is within `C_0=2`.
If `mathcal H<1`, the row sum is empty. If `X<1` and
the columns are nonempty, `N(n)>=1` and upper support give
`X>=1/b_0`, so only `O_I(1)` columns occur; direct counting
gives `E<<_I mathcal H ||W||_infinity^2<<Sigma||W||_infinity^2`.
The large-`D` threshold may depend on the fixed support constant
and fixed `C`, as allowed. Bounded `D` is covered by counting.

The same endpoint argument applies after every divisor shift:
`X'=X/N(d)`, `F'=F N(d)`, and `Sigma'=X'F'=Sigma`.
If `X'<1` but the shifted column sum is nonempty, then
`X'>=1/b_0` for the relevant fixed test interval. There are
`O_I(1)` columns, `O(F')` auxiliary ideals, and `O(mathcal H)`
element rows; dividing by `X'F'` gives the same bound
`E<<_I mathcal H ||U||_infinity^2`. Thus divisor removal does
not leave an untreated small-column range.

## Remaining obligation

The scoped initial reduction closes conditional on
`eq:auxiliary-target` and the classical imports identified in the
[arithmetic audit](INITIAL_ARITHMETIC_CONVERSION_AUDIT_20261012.md).
It does not establish `prop:R`, the two-Poisson return transfer,
the canonical energy estimate, the original mean square, or the claimed
zero-free theorem. The next bounded source target is the complete uniform `prop:R` ledger,
including its quadratic sieve hypotheses and every exceptional and general
row branch. The [combined review](../reviews/INITIAL_POISSON_AND_ARITHMETIC_REVIEW_20261012.md)
records that target and the scope of the new finite checks. The initial
reduction itself supplies no independent cancellation estimate.
