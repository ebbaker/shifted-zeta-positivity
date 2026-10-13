# Initial arithmetic conversion and coefficient class audit

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration. The exact serving
variant and configured reasoning effort are not exposed and
are not inferred. This is an internal mathematical read-through, not
independent specialist validation or formal verification.

## Scope and finding

The pinned [October 5 source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex)
is `paper2.tex` at openai/math revision
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. Its SHA-256 was
rechecked as
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
Physical-line references below refer to those exact bytes. This audit reads
`lem:arithmetic` (lines 823–862), its Appendix A proof (2689–2873), and the
arithmetic part of `prop:poisson-reduction` (1039–1186), together with
`lem:remove-exclusions` (962–991).

**Scoped result:** the conversion identities, finite ray-class expansion,
and the initial shared-column reindexing close under the stated classical
inputs. The same fixed coefficient family
\(a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n)\) occurs in both
columns. The moving common factors introduce the permitted auxiliary
sextic twist and an exclusion mask; they do not introduce an arbitrary
moving column profile. No substantive arithmetic defect was established.

The [companion Poisson audit](INITIAL_POISSON_REDUCTION_AUDIT_20261012.md)
checks the analytic kernel separation and full initial energy ranges.
These audits do not prove the canonical energy estimate, the theta or quadratic sieve inputs, or the full claimed
zero-free theorem.

## Definitions and nonvanishing needed by the algebra

Let \(\mathcal O=\mathbb Z[\omega]\), \(\omega=e^{2\pi i/3}\),
\(N(c)=|c|^2\), and \(e(z)=\exp(4\pi i\operatorname{Im}(z)/\sqrt3)\).
Primary means congruent to 1 modulo 3, and ideals prime to 3 have unique
primary generators. All starred columns are squarefree and prime to the
fixed set \(S\), which contains primes over 2 and 3 and the conductor of
the finite-order Hecke twist \(\nu\). Divisors are represented by their
unique primary generators.

For a prime \(p\notin S\), \(\chi_p\) has exact order 6 in the finite
field \(\mathcal O/(p)\). All \(\chi_p^j\) for \(j=\pm1,2,3,4\) are
nonprincipal and primitive. A squarefree product has nontrivial local
character at every prime of its modulus, so these product characters are
primitive. Their normalized Gauss sums have modulus 1. In particular,
every division or cancellation of \(\gamma_j\) in the Appendix proof is
legitimate. Also \(|a_\xi(n)|=1\) for all admissible squarefree \(n\).
At the unit ideal all these factors equal 1 by the source's convention.

The primitive character used in the initial Poisson step is
\(\overline{\chi_{z_1}}\chi_{z_2}\), where \((z_1,z_2)=1\). Its
conductor is exactly \(z_1z_2\). It is principal only when
\(z_1=z_2=1\); an empty local modulus is allowed. A sixth power in a row
variable does not reduce this conductor as a *character of the row*.

## 1. The prime cubic Jacobi evaluation

Write \(q=N(p)\), \(\psi=\chi_p^2\), and
\(J(A,B)=\sum_xA(x)B(1-x)\), with nonprincipal multiplicative characters
extended by zero at 0. The source uses classical Gauss–Jacobi and
inverse-character identities and the resulting norm
\(|J(\psi,\psi)|^2=q\). The remaining unit evaluation is supplied in the
source rather than merely quoted:

1. Reducing \(\psi(x)\) modulo \(p\) gives \(x^{(q-1)/3}\).
   Expanding \((1-x)^{(q-1)/3}\), every power of \(x\) lies strictly
   between 0 and \(q-1\). Its sum over the field is zero. Hence
   \(p\mid J(\psi,\psi)\).
2. Both \(J\) and \(p\) have norm \(q\). Thus \(J/p\) is a unit in
   \(\mathcal O\). This reasoning also covers inert primes, whose residue
   field has \(q=\ell^2\); it does not silently assume \(q\) is a
   rational prime.
3. Write \(\psi(x(1-x))=\omega^{j_x}\) for \(x\ne0,1\). The product
   of all \(x(1-x)\) is 1, because each of \(\prod x\) and
   \(\prod(1-x)\) over that set is \(-1\). Therefore
   \(\sum j_x\equiv0\pmod3\).
4. Modulo \((3)=(\omega-1)^2\), expanding \(\omega^{j_x}\) yields
   \(J\equiv(q-2)+(\omega-1)\sum j_x\equiv-1\pmod3\).
   Since \(p\equiv1\pmod3\), the unit multiplier is \(-1\). The six
   units have distinct reductions among the six units modulo 3, so this
   indeed selects a unique unit.

Thus \(J(\psi,\psi)=-p\). The inverse-character Gauss identity gives
\(\gamma_2(p)\gamma_4(p)=\chi_p(-1)^2=1\), and hence

\[
\gamma_2(p)^3
=\frac{\gamma_2(p)^2}{\gamma_4(p)}
=\frac{J(\psi,\psi)}{\sqrt q}
=-\alpha(p).
\]

The sign is tied to the primary generator and to the source's chosen
additive character. Replacing either convention without carrying its
correction would change this identity.

For the second prime identity, counting the two roots of
\(u^2=1-y\), with the quadratic character taking value 0 at 0, proves

\[
\chi_p(4)J(\chi_p,\chi_p)=J(\chi_p,\chi_p^3).
\]

The Gauss–Jacobi relations therefore give

\[
\gamma_1(p)\gamma_2(p)
=\overline{\chi_p(4)}\gamma_3(p)\gamma_2(p)^3
=-\alpha(p)G(p).
\]

The substitutions here preserve the zeros at 0 and 1. The character
orders ensure that all Gauss–Jacobi formulas being divided through have
nonprincipal product character.

## 2. The quadratic phase and finite reciprocity classes

The source derives the quadratic phase by Gaussian Poisson, rather than
assuming a formula uniform in changing primes. Define

\[
\Gamma(c)=|c|^{-1}\sum_{x\bmod c}e(x^2/c).
\]

For \((c,2)=1\), its claimed formula is
\(\Gamma(c)=\frac12\sum_{y\bmod2\mathcal O}e(-cy^2/4)\).
The finite phase \(e(-cy^2/4)\) is periodic modulo \(2\mathcal O\),
because replacing \(y\) by \(y+2z\) changes the exponent's argument by
an element of \(\mathcal O\).

For completeness, the limiting normalization in lines 2793–2813 works as
follows. With \(M_\eta=\sum_ze^{-\pi\eta|z|^2}\), the left side of
Gaussian Poisson, divided by \(M_\eta\), tends to
\(N(c)^{-1}\sum_{x\bmod c}e(x^2/c)\). The transform is

\[
\frac{|c|}{2\sqrt{r_\eta}}
e^{-\pi\eta N(c)|y|^2/(4r_\eta)}e(-cy^2/(4r_\eta)),
\qquad r_\eta=1+3N(c)\eta^2/16.
\]

Replacing \(r_\eta\) by 1 has unnormalized error
\(O_c(\eta^2\sum_y|y|^2e^{-C_c\eta|y|^2})=O_c(1)\);
normalization costs \(M_\eta\asymp\eta^{-1}\), making that error
\(O_c(\eta)\). Each of the four residue classes modulo 2 contributes
asymptotically the same Gaussian mass, and the total transformed Gaussian
mass is \((4/N(c))M_\eta\). Thus the normalized right side tends to
\((2|c|)^{-1}\sum_{y\bmod2\mathcal O}e(-cy^2/4)\). Multiplying by
\(|c|\) gives exactly the asserted formula. The errors need be uniform
only for each fixed \(c\) during this evaluation; the resulting finite
formula is exact for every odd \(c\).

For \(c=a+b\omega\), direct evaluation yields

\[
\Gamma(c)=\frac{1+i^{-b}+i^a+i^{b-a}}2.
\]

It depends only on \(c\bmod4\mathcal O\) and is invariant under
multiplication by squares. The four square classes, with
\(\lambda=1+2\omega\), give
\(\Gamma(1)=\Gamma(-1)=1\), \(\Gamma(\lambda)=i\), and
\(\Gamma(-\lambda)=-i\). The quotient

\[
\mathcal R(c,d)=\frac{\Gamma(cd)}{\Gamma(c)\Gamma(d)}
\]

is the symmetric bicharacter
\(\mathcal R((-1)^e\lambda^f,(-1)^g\lambda^h)
=(-1)^{eh+fg+fh}\).

At a prime, grouping \(x\) by \(x^2\) proves
\(\Gamma(p)=\gamma_3(p)\); the additive character's trivial sum over
the field vanishes. CRT extends this equality to squarefree moduli.
For coprime primes, quadratic CRT identifies \(\mathcal R\) with the
quadratic reciprocity quotient. Cubic reciprocity says the sextic
quotient's square is 1; its cube is exactly the quadratic quotient.
Therefore

\[
\chi_b(a)=\mathcal R(a,b)\chi_a(b).
\]

Multiplicativity of both the symbols and the finite bicharacter extends
this relation to coprime primary \(a,b\) with arbitrary prime powers.
One must not instead assert \(\Gamma(c)=\gamma_3(c)\) for an arbitrary
nonsquarefree \(c\), because \(\gamma_3(c)\), defined by the imprimitive
quadratic character, need not have that value. The source restricts this
particular equality to squarefree \(c\), as needed.

Finally, cubic reciprocity gives
\(\chi_c(4)=(-2/c)_3=(c/(-2))_3\), a character modulo 2 for primary
\(c\). Consequently
\(G(c)=\overline{\chi_c(4)}\Gamma(c)\) depends only on a fixed
residue class modulo 4, together with the primary convention modulo 3.
A fixed ray modulus containing these factors and the conductor of \(\nu\)
is sufficient. There is no need to enlarge it with a moving prime.

## 3. CRT, conversions, and the quotient identity

For coprime squarefree primary \(a,b\), the general CRT factor is

\[
\gamma_j(ab)=\gamma_j(a)\gamma_j(b)
\chi_a(b)^j\chi_b(a)^j.
\]

Cubing the \(j=2\) identity removes its local twist, giving
\(\gamma_2(n)^3=\mu(n)\alpha(n)\) at squarefree \(n\).
For the product \(\gamma_1\gamma_2\), the local twist is
\(\chi_a(b)^3\chi_b(a)^3=\mathcal R(a,b)\), exactly matching
\(G(ab)=G(a)G(b)\mathcal R(a,b)\). Hence

\[
\gamma_1(n)\gamma_2(n)=\mu(n)\alpha(n)G(n),\qquad
\gamma_1(n)\gamma_{-1}(n)=\chi_n(-1).
\]

These give both conversion directions:

\[
\overline{\alpha(n)}\gamma_2(n)\gamma_1(n)=\mu(n)G(n),
\quad
\mu(n)\gamma_{-1}(n)=\chi_n(-1)G(n)^{-1}
\overline{\alpha(n)}\gamma_2(n).
\]

Cubic reciprocity also reduces the \(j=2\) CRT twist to
\(\chi_b(a)^4\), giving
\(a_\xi(ab)=a_\xi(a)a_\xi(b)\chi_b(a)^4\).

On the fixed ray group, \(\mathcal R(a,a)=\chi_a(-1)\), which also
follows directly from the four-class table. Because \(G(1)=1\),

\[
G(a^{-1})=\chi_a(-1)\overline{G(a)},\qquad
G(ba^{-1})=\chi_a(-1)\overline{G(a)}G(b)\mathcal R(a,b).
\]

The inverse here is a ray-group inverse, not the primary generator of an
integral ideal of reciprocal norm. This distinction is essential to
interpreting the finite Fourier expansion.

## 4. Why the initial paired Gauss sum produces the same fixed profile

Set \(A(n)=\overline{\alpha(n)}\gamma_2(n)\). Extracting
\(g=(n_1,n_2)\) before the Poisson step gives \(n_j=gz_j\), with
\((z_1,z_2)=(z_1z_2,g)=1\). The common coefficient factors cancel:
\(\mu(g)^2=1\) and \(\overline{\nu(g)}\nu(g)=1\). The common
sextic factors yield precisely

\[
\overline{\chi_{n_1}(u)}\chi_{n_2}(u)
=\mathbf1_{(u,g)=1}\overline{\chi_{z_1}(u)}\chi_{z_2}(u).
\]

For \(\chi=\overline{\chi_{z_1}}\chi_{z_2}\), CRT gives

\[
\gamma(\chi)
=\gamma_{-1}(z_1)\gamma_1(z_2)
\overline{\chi_{z_1}(z_2)}\chi_{z_2}(z_1)
=\gamma_{-1}(z_1)\gamma_1(z_2)\mathcal R(z_1,z_2).
\]

Let \(t=z_1z_2^{-1}\) in the ray group. The two conversion directions
and \(|A(z_2)|=1\) therefore yield

\[
\begin{aligned}
&\mu(z_1)\mu(z_2)\overline{\nu(z_1)}\nu(z_2)\gamma(\chi)\\
&\quad=A(z_1)\overline{A(z_2)}
\overline{\nu(t)}\,
\chi_{z_1}(-1)\overline{G(z_1)}G(z_2)\mathcal R(z_1,z_2)\\
&\quad=A(z_1)\overline{A(z_2)}\overline{\nu(t)}G(t^{-1}).
\end{aligned}
\]

Expand the *fixed* function
\(\overline{\nu(t)}G(t^{-1})=\sum_\xi c_\xi\xi(t)\) on the finite
ray group. Since \(\xi(t)=\xi(z_1)\overline{\xi(z_2)}\), this is
exactly

\[
\sum_\xi c_\xi a_\xi(z_1)\overline{a_\xi(z_2)}.
\]

Both columns have the same \(\xi\). The coefficients \(c_\xi\) and
number of characters depend only on the fixed modulus and twist. No
dependence on \(g,e,h\), or the dyadic scales enters the column profile.
Applying the one-column conversion to each side while omitting the CRT
reciprocity phase would fail to justify this paired identity.

The zero frequency is present only for \(z_1=z_2=1\), and gives the
displayed diagonal with factor
\(\prod_{p\mid g}(1-N(p)^{-1})\). The nonzero frequencies for those
same diagonal indices must still be retained; the source does so.

## 5. Shared columns and all zero-extension masks

After Poisson and the preceding conversion, removing
\((z_1,z_2)=1\) uses the exact ideal identity
\(\mathbf1_{(z_1,z_2)=1}=\sum_{v\mid z_1,z_2}\mu(v)\).
Set \(z_j=vm_j\). Squarefreeness forces
\((m_1m_2,gv)=1\), and \((g,v)=1\). The common column factor is

\[
|a_\xi(v)\chi_v(he^5)|^2=\mathbf1_{(v,h)=1},
\]

because \(e\mid g\) is already coprime to \(v\). The remaining
factors are
\(\chi_{m_1}(he^5v^4)\overline{\chi_{m_2}(he^5v^4)}\). There is
no residual \((m_1,m_2)=1\) condition: keeping it after Möbius inversion
would be an incorrect restriction.

The full variable change is

\[
b=g/e,\qquad f=ev,\qquad k=eh.
\]

Its inverse is \(e=(f,k)\), \(v=f/e\), \(g=be\), \(h=k/e\).
Indeed, \(f=ev\) is squarefree, \((e,v)=1\), and \((h,v)=1\);
therefore \((f,k)=e\), regardless of whether \((e,h)=1\). Conversely,
for arbitrary \(k\ne0\) and coprime squarefree \(b,f\), these inverse
formulas give every original restriction. This is a bijection of ideals
for the divisors and of actual lattice elements for \(h,k\), since the
divisor generator is fixed primary. It does not identify unit associates
of the row variables.

Under this change,

\[
gv=bf,\quad he^5v^4=kf^4,\quad
\mu(e)\mu(v)=\mu(f),\quad N(g)/N(e)=N(b),
\]

and

\[
\frac{HN(h)}{N(e)N(v)^2N(m_1)N(m_2)}
=\frac{HN(k)}{N(f)^2N(m_1)N(m_2)}.
\]

The surviving column exclusion \((m_j,f)=1\) is exactly enforced by
the zero-extended factor \(\chi_{m_j}(f)^4\); the exclusion
\((m_j,b)=1\) remains explicit. Thus the columns are the allowed
energy class with auxiliary \(f\) and exclusion \(b\), not a larger
coefficient class. A fourth power of a zero-extended character still
vanishes at nonunits. No factor is replaced by 1 on those columns.

The factor \(N(g)/D^2\) after introducing
\(W_0(x)=x^{-1/2}\overline W(x)\) is also correct: writing
\(x_j=N(gz_j)/D\),
\(\sqrt{N(z_1)N(z_2)}=(D/N(g))\sqrt{x_1x_2}\).
This accounts for both the Poisson denominator and the initial \(1/D\)
normalization, producing the prefactor \(H/D^2\) and the eventual
\(N(b)\) in `eq:initial-column-output`.

## 6. The exclusion-removal identity stays in the class

For \(r_0\) the radical of an exclusion ideal away from \(S\), Möbius
inversion and \(n=dm\) give

\[
C_{\mathfrak r}(X;k,f)
=\sum_{\substack{d\mid r_0\\(d,f)=1}}
\mu(d)a_\xi(d)\chi_d(k)\chi_d(f)^4
C_1(X/N(d);k,df).
\]

The CRT factor \(\chi_m(d)^4\) simultaneously restores
\((m,d)=1\) and combines with \(\chi_m(f)^4\). Terms with
\((d,f)\ne1\) vanish in the original sum. Each exterior coefficient
has modulus at most 1. Cauchy–Schwarz in \(d\), then the injective map
\(f\mapsto df\) for each fixed \(d\), produce the stated comparison
of excluded to unexcluded energies. Squarefreeness of \(df\) follows
from \((d,f)=1\). The product scale is unchanged:
\((X/N(d))(FN(d))=XF\). Both the ray character and the smooth profile
remain the same. The dyadic scale of \(f\) becomes \(FN(d)\), which
need not be a power of 2; the energy definition permits real scales.

## Imports and exact remaining obligations

The arithmetic audit uses classical lattice Poisson, Gauss–Jacobi and
primitive/inverse-character Gauss identities, cubic reciprocity for
primary Eisenstein integers, and finite-group character orthogonality.
These are imports. The Appendix's cubic Jacobi sign, the quadratic
four-class table, the paired conversion, and the mask-preserving
reindexing have been checked directly above. No theta estimate or
large-sieve inequality is needed to establish these arithmetic
identities.

The [companion Poisson audit](INITIAL_POISSON_REDUCTION_AUDIT_20261012.md)
checks uniform smooth separation, the compact dual cutoff, the initial
positive gap and small ranges, and the dyadic and divisor losses. The
[combined review](../reviews/INITIAL_POISSON_AND_ARITHMETIC_REVIEW_20261012.md)
records finite verification and the remaining completed-family and transfer
obligations. These arithmetic identities do not supply a power saving
without the auxiliary energy estimate.

Useful clarifications for a source rewrite, without altering its result:

- Spell out the CRT phase in the paired Gauss identity and the ray-group
  quotient \(t=z_1z_2^{-1}\).
- Show the factors in the Gaussian-mass limit, so the factor \(1/2\)
  is visibly compatible with the normalized measure.
- Restrict \(\Gamma(c)=\gamma_3(c)\) explicitly to squarefree \(c\),
  as the source presently does, and explain multiplicativity when
  extending the reciprocity law to general coprime primary elements.
- State that \((e,h)\) may be nontrivial in the reindexing, while
  \((v,h)=1\) is exactly the mask needed for \(e=(f,k)\).

These are expansions of steps that close under the existing hypotheses,
not established proof defects or new cancellation assumptions.
