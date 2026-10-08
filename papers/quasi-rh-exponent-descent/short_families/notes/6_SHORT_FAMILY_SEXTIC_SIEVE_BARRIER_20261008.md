# The generic sixth-order sieve reaches exactly the coherent-row barrier

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is a same-model source check and deduction. The imported large-sieve
theorem is not independently proved or formally verified here.

## A current primary-source theorem

Alexandre de Faveri's *Optimal large sieve for fixed order characters*,
arXiv:2610.04045v1, submitted 2 October 2026, states in Theorem 1.1,
page 2, the bound

\[
 \Theta_n(M,N)\ll_{\varepsilon,n,K,S}(MN)^\varepsilon
 \left(M+N+M^{1-1/n}N^{2/n}+M^{2/n}N^{1-1/n}\right).
\tag{1}
\]

Here both row and column indices are **n-th-power-free** ideals, and
the norm is the supremum over coefficient vectors of squared norm one.
The theorem is stronger than the older squarefree-index BGL bound used
in the neighboring source. Its displayed statement was inspected in
the [primary PDF](https://arxiv.org/pdf/2610.04045), pages 1--2.
It is used as a new imported theorem, not inferred from the source's
character-amplification moments.

For \(K=\mathbb Q(\sqrt{-3})\) and \(n=6\), (1) becomes

\[
 \Theta_6(M,N)\ll (MN)^\varepsilon
 \left(M+N+M^{5/6}N^{1/3}+M^{1/3}N^{5/6}\right).
\tag{2}
\]

## Transfer to all physical rows, with multiplicities paid

Consider the original source-compatible coefficients

\[
 A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D).
\tag{3}
\]

The same argument works for any bounded squarefree-supported column
coefficient in place of \(\mu_K\nu\). Write each nonzero physical
element uniquely as a unit times a chosen generator of an ideal
\(v r^6\), with \(v\) sixth-power-free. The exact character identity is

\[
 \chi_n(vr^6)=\chi_n(v)\mathbf1_{(n,r)=1}.
\tag{4}
\]

No multiplicity is dropped: there are finitely many unit choices, and
\(Nr\le H^{1/6}\). The part of \(v\) supported on the fixed set \(S\)
has exponents at most five, hence finitely many possibilities. Its
effect is a fixed column twist and a fixed scale factor. The good part
of \(v\) is sixth-power-free, with norm at most \(O(H/(Nr)^6)\).

Here is an explicit comparison with de Faveri's family, rather than an
assumption that every sextic presentation has the same coefficients.
Since the Eisenstein ring is a PID, choose the data in de Faveri's
Section 2.3 so that each representative ideal \(E\) has a fixed global
generator \(m_E\). Fix a good sixth-power-free ideal \(v\) and its
physical generator \(v_0\). Choose one construction decomposition

\[
 v=(x)E\mathfrak j^6,\qquad x\equiv1\pmod{\mathfrak c},
\]

and one generator \(j_0\) of \(\mathfrak j\). Equality of the generated
ideals gives

\[
 v_0=\epsilon_v x m_Ej_0^6,\qquad \epsilon_v\in\mu_6.
\tag{4a}
\]

For ideals \(n\) avoiding the finitely many primes of this particular
decomposition, the defining power-residue symbols give

\[
 \chi_n(v_0)=\chi_n(\epsilon_v)\,\chi_v^{\rm DF}(n).
\tag{4b}
\]

Here \(\chi_v^{\rm DF}\) denotes the Hecke family in Theorem 1.1.
The decomposition and \(\epsilon_v\) are fixed before the columns vary.
Equality away finitely many primes identifies the inducing Hecke
characters. De Faveri Section 2.3.4 defines the original zero extension
by \(\chi_v^{\rm DF}(n)=0\) if \((n,v\mathfrak c)\ne1\); Section
2.5.1 gives good conductor \(\operatorname{rad}(v)\) for sixth-power-free
\(v\). The native power-residue character has that same good conductor
and zero set. Therefore (4b) holds on every good column, not merely
those avoiding the temporary decomposition's primes. No temporary prime
has been added to the physical masks.

Partition the averaged rows into the at most six classes indexed by
\(\epsilon_v\). Within each class, \(\chi_n(\epsilon_v)\) is a fixed
column twist **independent of the averaged ideal \(v\)**. The exterior
physical unit and the fixed bad-prime sixth-power-free part also give
fixed column twists after finite splitting. The mask \((n,r)=1\) is
fixed for each application of the sieve. Positivity then permits
extending each such row subclass to all sixth-power-free good ideals
with the same coefficient vector. This proves the required transfer.
A conjugated common orientation is covered by conjugating the entire
column coefficient vector inside the absolute square.

For each fixed \(r\), the coefficients
\(\mu_K(n)\nu(n)W(Nn/D)\mathbf1_{(n,r)=1}\) have squared norm
\(O_W(D)\) by ideal counting, uniformly in \(r\), and their squarefree
support is a subset of the allowed sixth-power-free support. Thus (2)
gives, after dividing the moment by \(D\), a contribution bounded by

\[
 D^\varepsilon\left(
 \frac{H}{(Nr)^6}+D+
 \frac{H^{5/6}D^{1/3}}{(Nr)^5}+
 \frac{H^{1/3}D^{5/6}}{(Nr)^2}\right).
\tag{5}
\]

The sums of \((Nr)^{-6},(Nr)^{-5},(Nr)^{-2}\) converge, while the
number of ideals \(r\) with \(Nr\le H^{1/6}\) is \(O(H^{1/6})\).
Consequently

\[
 \boxed{
 D^{-1}\sum_{0<Nu\le H}|A_u(D)|^2
 \ll_\varepsilon (DH)^\varepsilon
 \left(H+D H^{1/6}+H^{5/6}D^{1/3}+H^{1/3}D^{5/6}\right).
 }
\tag{6}
\]

An arbitrary fixed Schwartz row weight is covered by dyadic row shells
and a sufficiently large decay exponent. The zero row contributes
nothing once the unit ideal lies outside the annular column support.
This gives the same estimate for the normalized smoothed moment.

For \(1\le H\le D\), all terms in (6) are at most \(D H^{1/6}\):

\[
 \frac{H^{5/6}D^{1/3}}{D H^{1/6}}=(H/D)^{2/3},\qquad
 \frac{H^{1/3}D^{5/6}}{D H^{1/6}}=(H/D)^{1/6}.
\]

Therefore the generic bound in the short-family range is

\[
 \mathfrak M(D,D^h)\ll_\varepsilon
 D^{1+h/6+\varepsilon},\qquad0<h<1.
\tag{7}
\]

## Exact exponent comparison and its interpretation

Writing (7) in the proposed form \(D^{h+a+\varepsilon}\) requires

\[
 a\ge1-\frac{5h}{6}.
\tag{8}
\]

At the boundary choice in (8), the extraction formula becomes

\[
 \beta_{\rm out}=\frac{1+a}{2}+\frac{5h}{12}=1.
\tag{9}
\]

The new generic theorem thus does not yield a quasi-RH improvement,
let alone RH descent. It pays exactly the coherent sixth-power-row
cost. For prime-only nonnegative coefficients, the rows \(u=r^6\)
with \(Nr\le H^{1/6}\) contribute
\(\gg D H^{1/6}/(\log D)^2\) to the normalized moment. So (7) is
sharp in powers for the broad bounded squarefree coefficient class.

The actual Möbius moment may be smaller; (2) does not use its signs.
The useful desired condition \(a+5h/6<3/4\) asks for more than a
quarter-power saving beyond the generic broad-coefficient barrier.
This identifies the precise role for a new actual-coefficient argument:
it must use cancellation between factorization classes, or a different
structural property that generic character orthogonality discards.

The new sieve should be retained as an optimal generic baseline and as
an input for auxiliary sectors. It cannot be inserted as the missing
short-family moment with \(a=0\), and merely restricting to a
sixth-power-free family would remove the replicated rows needed by
the extraction.
