# Fixed-character extraction and Dirichlet norm-lift conclusion

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration. Exact serving variant
and configured reasoning effort are not exposed and are not inferred.
This is an internal mathematical audit, not independent specialist
validation or formal verification.

## Source, scope, and finding

The source is the [October 5 manuscript at openai/math revision
fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
read from `/private/tmp/arithmetic-source-audit-20261012/paper2.tex`.
Its SHA-256 is
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
All physical-line references use those exact bytes. The main theorem is at
lines 74–77; this audit covers fixed-character extraction, Mellin
continuation and the Dirichlet implication at 665–770. The earlier
dependency/extraction note was read within its expressly conditional
scope. This note does not reprove the family mean square or silently
promote its scoped audits to independent verification.

**Finding:** assuming the stated original mean-square proposition, the
coherent-row extraction gives the claimed bound for every fixed
finite-order Hecke character, including the principal character. The
Mellin argument then gives the common qualitative half-plane. The
Dirichlet conclusion follows for primitive and imprimitive characters
after explicitly distinguishing the norm lift's actual conductor from a
chosen modulus. The split, inert and ramified Euler factors match; finite
factor corrections cannot create or cancel a zero in positive real part.
No substantive extraction or base-change defect was found. The possible
pole cancellation at 1 closes in the two exceptional principal/quadratic
cases. This finding remains conditional on the mean square and the
classical continuation/prime-counting imports.

## Imported facts checked against outside sources

These sources were accessed directly on 12 October 2026. They support
standard imported facts, not the October 5 manuscript's new estimate.

- Alex Burgin, [*A New Elementary Proof of Landau's Prime Ideal Theorem,
  and Associated Results*, arXiv:2406.08565v1](https://arxiv.org/html/2406.08565v1),
  Theorem 1 and Lemma 1: the fixed-field prime ideal asymptotic is
  \(\pi_K(x)\sim x/\log x\). This external paper states the needed
  theorem; its full proof was not independently audited.
- Bjorn Poonen, [*Tate's thesis*, MIT 18.786 notes](https://math.mit.edu/~poonen/786/notes.pdf),
  Definition 5.11, Example 5.13, and Theorem 5.22, especially Section
  5.11: the global Hecke continuation theorem applies to finite-order
  characters. Its completed-function formulation has exceptional norm
  characters; for a finite-order character over this imaginary quadratic
  field, the only possible pole in \(\Re s>0\) is at 1 for the trivial
  character. This is an imported theorem, not newly proved here.
- [NIST DLMF Section 25.15](https://dlmf.nist.gov/25.15), including
  equation 25.15.9: Dirichlet \(L\)-functions are entire for nonprincipal
  characters; principal characters have a simple pole at 1; nonprincipal
  characters have nonzero value there.
- [NIST DLMF Section 27.8](https://dlmf.nist.gov/27.8), especially
  27.8.7–27.8.8: the primitive/induced-modulus distinction and the
  decomposition into a primitive character and a principal mask.

The estimates, parameter choices, ray-character construction and local
Euler calculations below are this audit's derivations. No third-party
full text or PDF is added to the repository.

## 1. Exact coherent rows, prime counts and uniform error

Fix a finite-order Hecke character \(\nu\) of
\(K=\mathbb Q(\sqrt{-3})\), and fix \(S\) containing primes above 2
and 3 and the conductor of \(\nu\). Set

\[
H=D^{1+\vartheta},\qquad
Y=H^{1/6}=D^{(1+\vartheta)/6},\qquad 0<\vartheta\le1/10.
\]

For every prime ideal \(\mathfrak p\notin S\) with
\(Y/2<N(\mathfrak p)\le Y\), let \(p\) be its primary generator.
The zero-extended sextic symbol satisfies exactly

\[
\chi_n(p^6)=\mathbf1_{\mathfrak p\nmid n}.
\]

On units modulo every prime of \(n\), this is the sixth power of a
sixth root of unity; on nonunits both sides vanish. Consequently these
rows are coherent with \(A_1\), while retaining the necessary exclusion
of \(\mathfrak p\)-divisible columns. Their norms obey
\(N(p^6)=N(p)^6\le Y^6=H\).

Distinct prime ideals give distinct element rows. Equality
\(p_1^6=p_2^6\) implies equality of the sixth-power prime ideals and
therefore \(\mathfrak p_1=\mathfrak p_2\). Their unique primary
generators are then equal. Thus no unit-associate multiplicity reduces
the extracted number of rows.

For support \(I=[a_0,b_0]\), write a multiple of \(\mathfrak p\) as
\(n=\mathfrak p m\). Ideal counting gives, uniformly in
\(\mathfrak p\),

\[
\#\{n:\mathfrak p\mid n,\ N(n)\in[a_0D,b_0D]\}
\le\#\{m:N(m)\le b_0D/N(\mathfrak p)\}
\ll_I D/Y.
\]

For this field the count \(\#\{m:N(m)\le R\}\ll 1+R\) follows
directly by counting lattice points in the disk \(|z|\le\sqrt R\)
and dividing by the six generators of every principal ideal. Since
\(D/Y=D^{(5-\vartheta)/6}\ge1\), its constant term is harmless.
Squarefreeness and the fixed \(S\)-exclusions only reduce this upper
bound. Since \(|\mu(n)\nu(n)|\le1\),

\[
|A_1(D)-A_{p^6}(D)|\ll_I\|W\|_\infty D/Y.
\]

The implicit constant is uniform over the selected moving primes. No
bound for a Möbius sum or prime in a varying ray class enters this error.

The imported fixed-field prime ideal theorem gives

\[
J=\#\{\mathfrak p\notin S:Y/2<N(\mathfrak p)\le Y\}
\sim\frac{Y}{2\log Y}.
\]

Removing finite \(S\) affects only a finite number of primes and the
threshold for the asymptotic. No uniformity in the conductor of \(\nu\)
is required: \(\nu,S\) are fixed before letting \(D\) grow. A fixed
bounded initial range is handled by enlarging the permitted constant.

## 2. Every exponent and the order of parameter choices

Let the loss in `thm:ms` be \(\eta>0\), and use a separate exponent
\(\lambda>0\) to absorb \(\log Y\ll_\lambda D^\lambda\).
For the derivative order \(k=k(\vartheta,\eta)\), positivity and the
coherent-row error imply

\[
\begin{aligned}
|A_1(D)|^2
&\le\frac2J\sum_p|A_{p^6}(D)|^2
+O_I(\|W\|_\infty^2D^2/Y^2)\\
&\ll_{\nu,S,I,\vartheta,\eta,\lambda}
\|W\|_{C^k(I)}^2
D^{11/6+5\vartheta/6+\eta+\lambda}
+\|W\|_\infty^2D^{5/3-\vartheta/3}.
\end{aligned}
\]

The first exponent is
\(2+\vartheta+\eta+\lambda-(1+\vartheta)/6\), and the second is
\(2-(1+\vartheta)/3\). Taking square roots gives the precise bound

\[
|A_1(D)|\ll_W
D^{11/12+5\vartheta/12+(\eta+\lambda)/2}
+D^{5/6-\vartheta/6}.
\]

For any requested \(\delta>0\), choose first
\(\vartheta=\min(1/10,3\delta/5)>0\), then
\(\eta=\lambda=\delta/2\). The additional exponent is at most
\(\delta/4+\delta/2=3\delta/4<\delta\), and the second term is
strictly below \(D^{11/12}\). The fixed moment derivative order is
then chosen with these parameters; it is finite for the smooth fixed
\(W\). This proves

\[
A_1(D)\ll_{\nu,S,W,\delta}D^{11/12+\delta}.
\]

There is no limiting application at \(\vartheta=0\), and no requirement
that \(k\) be bounded as \(\delta\downarrow0\). The manuscript's
renaming of exponent losses at lines 712–724 is legitimate, though the
separate \(\eta,\lambda\) ledger makes the choices transparent.

Exactly the same argument works for \(\nu=1\). The original mean
square permits it; the prime error bound uses only unit modulus. It is
the positive moment that supplies the principal Möbius estimate, not a
separate assumed principal cancellation theorem.

## 3. Mellin continuation interface

The [Mellin assembly note](FINAL_MELLIN_AND_ZERO_FREE_ASSEMBLY_20261012.md)
checks the complete continuation argument from this every-loss saving:
small-scale cutoff, compact-set uniform convergence, absolute Fubini on
real part greater than one, a smooth test fixed after an alleged zero,
and the meromorphic product identity including the principal pole.
Its test norms may depend on the alleged zero. Together these give the
qualitative Hecke conclusion used in the norm-lift calculation below.

## 4. Constructing the norm lift, without an unstated conductor claim

Let \(\chi\) be a Dirichlet character modulo \(q\), and define
\(\nu_\chi(\mathfrak a)=\chi(N(\mathfrak a))\) for integral ideals
prime to \(q\mathcal O\). Extend multiplicatively to the fractional
ideal group prime to that modulus, using the Dirichlet character on
positive rational \(q\)-units. This character has finite image.
If \(\beta\equiv1\pmod{q\mathcal O}\), then
\(N(\beta)\equiv1\pmod q\), so \(\nu_\chi((\beta))=1\).
Consequently it factors through the finite ray group modulo
\(q\mathcal O\). Its actual finite conductor divides
\(q\mathcal O\), and the infinity type is trivial. An odd Dirichlet
character causes no archimedean problem: the complex norm lands in
\(\mathbb R_{>0}\), where its sign character is trivial.

The actual conductor can be smaller. For example \(\chi_{-3}\)
pulls back to the trivial character away from 3: split prime norms
are 1 modulo 3 and inert prime norms are squares. Its primitive norm
lift has conductor 1. The source's qualification by finite Euler
factors is therefore necessary if \(L_K\) denotes the primitive
Hecke \(L\)-function rather than the ray-modulus Euler product.
Enlarging the fixed \(S\) to include primes over \(q\) is allowed;
the Hecke conclusion has already been proved for each fixed character.

## 5. Complete Euler-factor table

Write \(\Delta=\chi_{-3}\). For rational \(p\ne3\), the polynomial
\(x^2+x+1\) has roots modulo \(p\) exactly when \(p\equiv1\pmod3\),
giving the familiar split/inert alternatives. At 3,
\((3)=(\lambda)^2\), \(N(\lambda)=3\). For \(p\nmid q\), put
\(z=\chi(p)p^{-s}\). The local calculation is:

| Rational prime | Prime ideals and norm-lift values | \(K\)-Euler factor | Product of Dirichlet factors |
| --- | --- | --- | --- |
| \(p\equiv1\pmod3\) | Two primes of norm \(p\), both value \(\chi(p)\) | \((1-z)^{-2}\) | \((1-z)^{-1}(1-z)^{-1}\), since \(\Delta(p)=1\) |
| \(p\equiv2\pmod3\) | One prime of norm \(p^2\), value \(\chi(p)^2\) | \((1-z^2)^{-1}\) | \((1-z)^{-1}(1+z)^{-1}\), since \(\Delta(p)=-1\) |
| \(p=3\), \(3\nmid q\) | One ramified prime of norm 3, value \(\chi(3)\) | \((1-\chi(3)3^{-s})^{-1}\) | Same first factor; second is 1 because \(\Delta(3)=0\) |

The prime 2 belongs to the inert row; it is not omitted from the
full-Euler-product comparison merely because the proof's fixed set
\(S\) contains it. At \(p\mid q\), the modulus-\(q\mathcal O\)
product omits all primes above \(p\), while both Dirichlet characters
vanish there, so both local sides are 1. Passing to the actual conductor
of \(\nu_\chi\) may restore finitely many local factors. Each such
factor and its inverse is holomorphic and nonvanishing in
\(\Re s>0\), since its character value is zero or a root of unity.

Thus the exact modulus-product identity for \(\Re s>1\) gives, for
the primitive Hecke \(L\)-function,

\[
L_K(s,\nu_\chi)=E_q(s)L(s,\chi)L(s,\chi\Delta),
\]

with a finite correction \(E_q\) holomorphic and nonvanishing on
\(\Re s>0\). Meromorphic continuation extends the equality. The
displayed formula is derived here by Euler factors; invoking an
unexplained automorphic base-change theorem is unnecessary for this
one-dimensional norm lift.

## 6. Primitive, imprimitive and principal cases at 1

If \(\chi\) modulo \(q\) is induced by primitive \(\chi^*\) of
conductor \(q_0\mid q\), direct comparison of Euler products gives

\[
L(s,\chi)=L(s,\chi^*)
\prod_{\substack{p\mid q\\p\nmid q_0}}
(1-\chi^*(p)p^{-s}).
\]

The finite factors are nonzero in positive real part. The same
observation applies when the product character \(\chi\Delta\) is
imprimitive, with its natural modulus \(\operatorname{lcm}(q,3)\).
The norm-lift argument therefore applies to every Dirichlet character,
including induced principal characters, without altering the common
half-plane.

Away from 1, neither Dirichlet factor has a pole. If either has a
zero in \(\Re s>11/12\), its product with the other and \(E_q\)
vanishes, contradicting the Hecke conclusion.

At 1, possible pole cancellation requires one primitive factor to be
principal. There are precisely two cases:

- If \(\chi^*=1\), the other primitive factor is \(\Delta\).
- If the primitive factor inducing \(\chi\Delta\) is principal,
  then \(\chi^*=\Delta\), and the first primitive factor is
  \(\Delta\).

The quadratic factor is nonzero at 1 by the imported Dirichlet theorem.
In this particular case positivity can also be verified directly:

\[
L(1,\Delta)=\sum_{j\ge0}
\left(\frac1{3j+1}-\frac1{3j+2}\right)>0.
\]

The paired terms are positive and summable. Induced-modulus Euler
corrections remain nonzero at 1. Thus the nonprincipal factor cannot
cancel the principal pole. If neither factor is principal, both are
holomorphic at 1, so the already obtained Hecke nonvanishing excludes
any zero there directly. Both primitive factors cannot simultaneously
be principal because \(\Delta\) is nontrivial.

## Constant dependence and boundary of this result

The exponent \(11/12\) is common to all the characters. The original
moment's derivative order is \(k=k(\vartheta,\eta)\), independent of
its support interval and of the fixed character; it is selected before
using the moment. Constants and large-\(D\) thresholds may depend on
fixed \(\nu,S,I,\vartheta\) and the chosen losses. The fixed test's norms
may depend on the alleged zero. This is sufficient for the
qualitative assertion for every fixed character and every fixed zero.
It does not establish uniform conductor/height bounds, effective
prime-distribution errors, least nonresidue bounds, or the manuscript's
other quantitative corollaries. Those need their own explicit
quantitative arguments.

The downstream logical chain in lines 665–770 closes assuming
`thm:ms`. The [final moment ledger](FINAL_ORIGINAL_MOMENT_ASSEMBLY_20261012.md)
connects the earlier audited canonical energy bound to that original
moment, with matched parameters and constants. The classical prime ideal and Hecke continuation
theorems remain imports. No failure was established here, but a correct
extraction cannot independently validate the new mean square on which
it depends.
