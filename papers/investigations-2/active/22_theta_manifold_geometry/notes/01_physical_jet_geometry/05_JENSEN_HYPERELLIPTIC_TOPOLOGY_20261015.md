# Compact real surfaces and a topological criterion for RH

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata. The strict Jensen argument and compact-surface equivalence received independent internal mathematical review. This is a synthesis of classical ingredients; no novelty or publication-priority claim is made.

## Statement

Use the manuscript normalization

\[
H(0,z)=\int_0^\infty\Phi(u)\cos(zu)\,du
=\frac18\xi\!\left(\frac12+\frac{iz}{2}\right).
\]

The functional equation makes \(w\mapsto\xi(1/2+w)\) even entire. Consequently

\[
f(z):=\xi(1/2+\sqrt z)=\sum_{k=0}^{\infty}\frac{\gamma_k}{k!}z^k
\]

means its single-valued entire power series, not a choice of square-root branch. Its coefficients have the positive theta-source formula

\[
\boxed{\quad
\gamma_k=\frac{8\,k!\,4^k}{(2k)!}
\int_0^\infty u^{2k}\Phi(u)\,du>0.
\quad}
\tag{1}
\]

Define the unshifted Jensen polynomials

\[
J_d(X)=\sum_{k=0}^d\binom{d}{k}\gamma_kX^k.
\tag{2}
\]

For each integer \(g\ge1\), let \(C_g\) be the smooth projective normalization over \(\mathbb R\) of

\[
\boxed{\qquad y^2=J_{2g+1}(x).\qquad}
\tag{3}
\]

Normalization is part of the definition even when the displayed affine model is singular. Odd degree ensures that \(J_{2g+1}\) is not a square in \(\mathbb C(x)\), so its function field defines a connected smooth projective curve. Its complex points form a compact connected oriented surface, equipped with the antiholomorphic involution \(\sigma_g\) induced by complex conjugation. Write \(b_0(C_g(\mathbb R))\) for the number of connected components of its fixed set.

**Theorem.** The following are equivalent:

1. The Riemann hypothesis holds.
2. For every integer \(g\ge1\),
   \[
   b_0(C_g(\mathbb R))=g+1.
   \tag{4}
   \]
3. For every integer \(g\ge1\), \(C_g\) has genus exactly \(g\) and has the maximal possible number \(g+1\) of real components.

Thus RH is equivalent to the assertion that this explicitly defined countable family of compact surfaces **with real involutions** has the expected maximal fixed-set topology. The construction uses finitely many complete theta moments for each surface and no previously located zeta zeros. No auxiliary strictification polynomial is needed.

**Essential qualification.** In (4), the number is the specified \(g+1\), where \(2g+1\) is the original Jensen degree. Replacing it by “maximal for the actual genus of the normalization” would weaken the condition: a singular affine model can normalize to a smaller-genus maximal real curve.

## Proof

### 1. Source normalization and growth below order one

Substitute \(z=-2iw\) in the normalization of \(H\). Then

\[
\xi(1/2+w)=8\int_0^\infty\Phi(u)\cosh(2wu)\,du.
\]

Termwise expansion is valid locally uniformly by superexponential decay of \(\Phi\), giving (1). Thus \(f(0)>0\), \(f(x)>0\) for \(x\ge0\), and \(f\) is not a polynomial because all its Taylor coefficients are strictly positive.

For completeness the manuscript's elementary source bound

\[
0<\Phi(u)<4\pi^2e^{9u-\pi e^{4u}}
\]

also gives the requisite order bound directly. For \(|z|\le R\),

\[
\begin{aligned}
|f(z)|
&\le32\pi^2\int_0^\infty
e^{(9+2\sqrt R)u-\pi e^{4u}}\,du\\
&=8\pi^2\int_1^\infty v^{\beta-1}e^{-\pi v}\,dv
\le8\pi^2\pi^{-\beta}\Gamma(\beta),
\qquad \beta=\frac{9+2\sqrt R}{4}.
\end{aligned}
\tag{5}
\]

Stirling's bound yields \(\log M_f(R)=O(\sqrt R\log R)\), hence order at most \(1/2<1\). The exact order \(1/2\) is also recorded in O'Sullivan's paper, Introduction, but the upper bound suffices here.

Under RH, all zeros of \(f\) are negative real. By the standard Hadamard factorization theorem for an entire function of order below one,

\[
f(z)=f(0)\prod_{n\ge1}(1+a_nz),
\qquad a_n>0,
\qquad \sum_{n\ge1}a_n<\infty,
\tag{6}
\]

locally uniformly, with zeros and factors counted with multiplicity. There are infinitely many factors: otherwise Hadamard factorization would make \(f\) a polynomial, contrary to (1). No simplicity assumption about the zeros of \(\xi\) has been made.

### 2. Strict Jensen hyperbolicity follows from the infinite product

We give the strictness argument because merely importing non-strict Jensen hyperbolicity would not establish that (3) has the expected genus.

**Elementary lemma.** If \(p\) is a real-rooted polynomial of degree \(d\ge1\) and \(a>0\), then \(p+ap'\) is real-rooted of degree \(d\). Each old root of multiplicity \(m\) has multiplicity \(m-1\) in \(p+ap'\), and every new root is simple. Applying any \(d\) operators \(1+a_iD\), with all \(a_i>0\), therefore gives a polynomial with distinct real roots.

**Proof.** If the distinct roots of \(p\) are \(r_1<\cdots<r_s\) with multiplicities \(m_i\), then off those roots

\[
\frac{p+ap'}p=1+a\sum_i\frac{m_i}{X-r_i}=:R(X),
\qquad
R'(X)=-a\sum_i\frac{m_i}{(X-r_i)^2}<0.
\]

There is exactly one simple zero of \(R\) between consecutive roots, exactly one on \((-\infty,r_1)\), and none on \((r_s,\infty)\). A local factorization at each \(r_i\) shows that its multiplicity drops by one. These roots account for all \(d\) roots, and the leading coefficient is unchanged. Each application decreases every multiplicity greater than one, while all new roots are simple. At most \(d-1\) applications suffice, so \(d\) suffice. ∎

For any entire function \(F(z)=\sum_{k\ge0}c_kz^k/k!\), its action \(F(D)\) on a degree-\(d\) polynomial is the finite sum \(\sum_{k=0}^dc_kD^k/k!\). In particular

\[
f(D)X^d=\sum_{k=0}^d\binom dk\gamma_kX^{d-k}
=X^dJ_d(1/X).
\tag{7}
\]

Fix \(d\), and peel any \(d\) factors from (6):

\[
f(z)=P(z)G(z),\qquad
P(z)=\prod_{i=1}^d(1+a_iz),\qquad
G(z)=f(0)\prod_{n>d}(1+a_nz).
\]

The polynomial \(G(D)X^d\) has degree \(d\), leading coefficient \(G(0)=f(0)>0\), and only real roots. To prove this without a separate Jensen input, truncate the product defining \(G\). Each finite truncation acts on \(X^d\) by a finite sequence of operators \(1+a_nD\), and hence gives a real-rooted polynomial by the lemma. Local uniform convergence of the products gives convergence of the first \(d\) Taylor coefficients; therefore these polynomials converge coefficientwise to \(G(D)X^d\). Since their degree and leading coefficient are fixed, the limit is real-rooted as well.

The operator product identity is exact on degree-\(d\) polynomials, since all series terminate modulo \(D^{d+1}\). Thus

\[
f(D)X^d=\prod_{i=1}^d(1+a_iD)\bigl(G(D)X^d\bigr).
\tag{8}
\]

The final \(d\) positive first-order factors and the lemma make every root in (8) simple and real. Its constant coefficient is \(\gamma_d>0\), so none of its roots is zero. By (7), reciprocation proves that \(J_d\) has \(d\) distinct real roots. All coefficients of \(J_d\) are positive, so these roots are negative.

We have proved

\[
\boxed{\quad\mathrm{RH}\Longrightarrow
J_d\text{ has }d\text{ distinct negative roots for every }d\ge1.\quad}
\tag{9}
\]

This does not assume simple zeta zeros: repetition among the \(a_n\) is explicitly permitted.

### 3. Normalization, genus and fixed-set topology

For any real degree-\(2g+1\) polynomial \(Q\) with positive leading coefficient, write

\[
Q=cA^2B,\qquad c>0,
\]

with \(B\) real, monic and squarefree. Its degree is odd, say \(2h+1\), with \(h\le g\). The smooth normalization of \(y^2=Q(x)\) has the same function field as \(v^2=cB(x)\), by \(v=y/A\). The latter double cover has \(2h+1\) simple finite branch points and a simple branch point at infinity. Riemann–Hurwitz gives genus \(h\). Equality \(h=g\) holds if and only if \(Q\) was squarefree.

Harnack's inequality now gives

\[
b_0(C(\mathbb R))\le h+1\le g+1.
\tag{10}
\]

If the number of real components is \(g+1\), both inequalities in (10) are equalities. This forces \(h=g\), so \(Q\) is squarefree. Thus the proposed criterion detects possible loss of genus under normalization; it does not assume singularities away.

For squarefree odd-degree \(Q\), let \(r\) be the number of its real finite roots. This number is odd. Between the ordered real roots, the sign of \(Q\) alternates. Each bounded positive-sign interval contributes one oval. The positive unbounded interval, closed through the unique real point at infinity, contributes one more component. Therefore

\[
\boxed{\quad b_0(C(\mathbb R))=\frac{r+1}{2}.\quad}
\tag{11}
\]

Equivalently, the real double cover has \(r+1\) real branch points after infinity is included. Combining (10) and (11), even when the initial affine model might have been singular,

\[
b_0(C(\mathbb R))=g+1
\Longleftrightarrow
Q\text{ has }2g+1\text{ distinct real roots}.
\tag{12}
\]

Applying (12) to \(Q=J_{2g+1}\) establishes (2) \(\Longleftrightarrow\) (3), and (9) proves RH \(\Longrightarrow\) (2).

### 4. Odd Jensen degrees recover the entire function

The scaled polynomials satisfy

\[
J_d(z/d)
=\sum_{k=0}^d\frac{(d)_k}{d^k}\frac{\gamma_k}{k!}z^k
\longrightarrow f(z)
\tag{13}
\]

locally uniformly, where \((d)_k=d(d-1)\cdots(d-k+1)\). Indeed \(0\le(d)_k/d^k\le1\), this ratio tends to one for each fixed \(k\), and the Taylor series for \(f\) is absolutely convergent on every fixed disk. This convergence holds along odd degrees as well.

If (2) holds, (12) says that every \(J_{2g+1}\) has only real roots. Their scaled versions are consequently nonvanishing on either open half-plane. Hurwitz's theorem and the nonzero limit \(f\) imply that \(f\) has no nonreal zeros. Formula (1) excludes all zeros on \([0,\infty)\), so its zeros are negative real.

For every zero \(s\) of \(\xi\), the identity \(\xi(s)=f((s-1/2)^2)\) implies that \((s-1/2)^2\) is negative real. Hence \(s-1/2\) is purely imaginary and \(\Re s=1/2\). This proves RH. ∎

## Why the odd degree and real involution matter

Odd degree is a deliberate safeguard. For even-degree models, maximal real topology need not imply all finite branch points are real in low genus: the smooth compactification of \(y^2=x^4+1\) has genus one and two real components although it has no real finite branch points. Odd degree forces a real branch point at infinity and yields the exact count (11).

The unmarked complex surface generally has genus \(g\) whether a squarefree \(J_{2g+1}\) has real or nonreal roots. The distinguishing information is the pair \((C_g,\sigma_g)\), or equivalently its real fixed locus inside the surface. Under (4) that locus is a union of \(g+1\) circles and its complement has two components. The quotient by conjugation is a sphere with \(g+1\) open disks removed, and the compact surface is its double; thus the two halves are planar surfaces with the specified boundary circles. The theorem is an equivariant-topology/real-algebraic-geometry reformulation, not a claim that unmarked genus detects RH.

The fixed expected value \(g+1\) must not be dropped. For example, an odd-degree polynomial with repeated square factors can define a singular model whose normalization has smaller genus and is maximal relative to that smaller genus, while failing (4).

## Relation to the current investigations and publication scope

Formula (1) ties these surfaces directly to the complete theta source. Each is a genuine compact surface constructed from finitely many source moments. This gives a clean answer to whether one can formulate RH as a property of manifold topology: yes, provided the natural real involution is retained.

The criterion is independent of the missing all-event signed boundary estimate in Investigation 22. Establishing (4) for every \(g\) would prove RH; the equivalence itself does not establish (4). Positivity of source moments alone does not imply Jensen hyperbolicity. No choice of a zero or data-fitted deformation enters (3).

This is a synthesis of established Jensen–Pólya theory, elementary real-rootedness-preserving differential operators, Hadamard factorization, and classical topology of real hyperelliptic curves. A publication claim needs fuller literature comparison and likely a further substantive result: a new theta-specific control of the real loci, a useful relation to periods or divisors, or a demonstrated certification advantage. No such extra result is asserted here.

## Verified primary sources and bounded search

1. Cormac O'Sullivan, *Zeros of Jensen polynomials and asymptotics for the Riemann xi function*, [arXiv:2007.13582](https://arxiv.org/abs/2007.13582), [author's revised paper](https://fsw01.bcc.cuny.edu/cormac.osullivan/Research/xi-revised.pdf). The Introduction, equations (1.1)–(1.2), uses exactly \(\Theta(z)=\xi(1/2+\sqrt z)\), records its order \(1/2\), and gives the coefficient normalization used here. Section 3 defines reciprocal Jensen polynomials and proves the operator route \(\Phi(D)X^d\). Our elementary argument supplies the strictness needed to control genus.
2. Michael Griffin, Ken Ono, Larry Rolen and Don Zagier, *Jensen polynomials for the Riemann zeta function and other sequences*, PNAS **116** (2019), 11103–11110; [arXiv:1902.07321](https://arxiv.org/abs/1902.07321), [HTML Introduction](https://arxiv.org/html/1902.07321). Equations (1)–(2) and the following paragraph state the classical Jensen–Pólya RH criterion and sufficiency of unshifted polynomials. Their generating function is \((4w^2-1)\Lambda(1/2+w)=8\xi(1/2+w)\); their coefficient sequence is eight times ours, with identical Jensen roots.
3. Benedict H. Gross and Joe Harris, *Real algebraic curves*, Annales scientifiques de l'École Normale Supérieure, series 4, **14** (1981), 157–182; [original paper](https://www.numdam.org/item/10.24033/asens.1401.pdf). Section 6, especially Proposition 6.3 and printed pp. 171–172, treats real hyperelliptic topology and the distinction between all-real branching and the exception with no real branch points. The odd-degree count is proved directly here by signs and the point at infinity.
4. Sigurd Angenent, *Inflection Points, Extatic Points and Curve Shortening*, proceedings of the S'Agaró 1995 meeting, published in *Hamiltonian Systems with Three or More Degrees of Freedom*, NATO ASI Series C **533** (1999), 3–10; [author's preprint](https://people.math.wisc.edu/~angenent/preprints/extatic.pdf). Section 3, preprint pp. 7–8, already relates zero-number variation to the winding degree of \((u_x,u)\) and proves the same-sign local-degree mechanism for parabolic equations. This is the direct classical comparator for Investigation 22's separate spacetime jet-phase proposal.

A bounded web search on 15 October 2026 used the exact combinations “Riemann hypothesis” + “Jensen” + “hyperelliptic”, “Riemann hypothesis” + “M-curves”, “Jensen polynomials” + “real algebraic curves”, and “Riemann hypothesis” + “maximal” + “real curves”. No direct matching publication of this precise surface family was found. This limited negative search does **not** establish novelty or justify a priority claim. Much search noise concerns RH for function fields, which differs from classical RH.

## Internal verification scope

The positive moment factor \(8k!4^k/(2k)!\), gamma-integral growth bound (5), degree preservation in \(1+aD\), strictness with repeated zeros of \(f\) allowed, reciprocal identity (7), finite-order operator factorization (8), normalization genus bound, odd-degree component count, and Jensen scaling limit (13) have been checked analytically. No numerical check substitutes for these proofs. No new theta hyperbolicity range has been computed.

See also the [spacetime winding formulation](04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md) and the [combined geometric review](../../reviews/13_GEOMETRIC_SIMPLIFICATION_AND_TOPOLOGICAL_RH_REVIEW_20261015.md).
