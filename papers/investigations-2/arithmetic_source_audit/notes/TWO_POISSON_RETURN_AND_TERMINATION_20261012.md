# Two Poisson return scales and finite termination

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is an internal mathematical review, not independent specialist
validation or formal verification.

## Result and source

Every surviving branch in the pinned transfer proof returns to the
specified energy class with admissible lengths. Removing the remaining
column exclusion preserves the product scale and the positive gap.
Combined with cube inversion, each nonempty tail decreases the row range
by at least the squared gap ratio. The canonical induction consequently
terminates at a finite derivative order. No new hypothesis on a returned
coefficient profile or on the intermediate row scale is needed.

Source: the [October 5 manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
openai/math revision fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb,
SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d.
Physical source lines 1487–1609 state the transfer and canonical
induction; lines 2496–2683 prove the return bound. Cube inversion and its
short ranges are at 1335–1473, and exclusion removal at 962–994.
The [arithmetic](TWO_POISSON_ARITHMETIC_LEDGER_20261012.md) and
[smooth-weight](TWO_POISSON_SMOOTH_AND_SHORT_RANGES_20261012.md) notes
check the two transformations and their estimates. This note checks
their use in the child supremum and terminating recurrence.

## Hypotheses and energy class

In the transfer proposition,
\[
1\le H,L,F,\Sigma\le D^{C_0},\qquad
\max\{H,LF\}\le\Sigma,\qquad C_0\ge1.
\]
The target \(\Sigma\) is independent of \(LF\). The source's energy is
\[
\mathcal E(H,X,F;\xi,V)
=\frac1{XF}\sum_{\substack{F\le N(f)<2F\\f\ {\rm squarefree}}}
\sum_{0<N(k)\le H}
\left|\sum_n^*a_\xi(n)\chi_n(k)\chi_n(f)^4V(N(n)/X)\right|^2.
\]
All ideal indices are primary and prime to the fixed set \(S\);
the star makes the column squarefree. The row \(k\) is any nonzero
Eisenstein element. The coefficient family is
\(a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n)\), with \(\xi\)
in a fixed finite ray-character group. Characters retain their zero
extensions. A returned \(f'\) may divide \(k'\), and this is allowed
by the energy definition.

The second transformation gives
\[
r=tg/e,\qquad f'=Cew,\qquad k'=deh,\qquad
X'_0=\frac L{N(r)N(f')}.
\]
Here \(r,f'\) are coprime, squarefree, and prime to \(S\).
The row \(k'\) can have arbitrary valuations, unit factor, or primes
in \(S\). Its only additional restriction after the signed regrouping
is \(f'\mid k'\). The column is exactly
\[
a_{\xi'}(n)\mathbf1_{(n,r)=1}\chi_n(k')\chi_n(f')^4.
\]
Thus its sole extra feature is the displayed exclusion at \(r\);
the coefficient class itself has returned.

## Why every surviving child has length at least one

Fix dyadic blocks \(R\le N(r)<2R\) and \(F'\le N(f')<2F'\).
Define common scales
\[
X'=\frac L{RF'},\qquad \Sigma'=X'F'=\frac LR,\qquad
H'=\frac{HL}{\Sigma F R^2}.
\]
Retain only \(r\) for which a nonzero term exists in that block.
For each retained \(r\), a witnessing pair \(f',k'\) satisfies
\[
F'\le N(f')\le N(k')\le
\frac{HL}{\Sigma F N(r)^2}.
\]
This implication uses \(f'\mid k'\); it is unavailable before signed
regrouping. It gives \(H'\ge1\). Moreover, for every ideal divisor
\(j\mid r\),
\[
\frac{X'}{N(j)}
\ge\frac{\Sigma F N(r)^2}{H R N(j)}
\ge\frac{\Sigma F}{H}\ge1,
\]
since \(N(j)\le N(r)\) and \(R\le N(r)\).
The unit cases \(r=1\), \(f'=1\), and \(j=1\) are included.

Exclusion removal changes the child to
\[
\left(H',\,\frac{X'}{N(j)},\,F'N(j)\right).
\]
Its two column/twist lengths are at least one and their product remains
\(\Sigma'\). The common scales obey
\[
H'\le\frac{HL}{\Sigma F},\qquad
\frac{H'}{\Sigma'}=\frac{H}{\Sigma FR}\le\frac H\Sigma,\qquad
\Sigma'\le L.
\]
These inequalities survive exclusion removal exactly. They are the
defining restrictions of the transfer supremum. They also place each
individual child parameter in the original polynomial range:
\(X'/N(j),F'N(j)\le\Sigma'\le L\le D^{C_0}\), and
\(H'\le H\le D^{C_0}\).

The child supremum is finite even before using induction. For tests with
\(\|V\|_{C^m}\le1\), the triangle bound gives
\(\mathcal E(H',X',F')/\Sigma'\ll_{I'}H'/F'\le H\).
Thus using it to supply a finite common-test bound in the first-transfer
lemma introduces no recursive assumption about a finite operator norm.

The order of operations matters. Eligibility of \(r\) comes from an
actual surviving witness; only then are the \(f',k'\) ranges enlarged
by positivity. The latter enlargement is used in a mean-square bound,
not to introduce additional untested \(r\)'s into the child supremum.

## Smooth norms and block normalization

The exact-to-common scale ratio is
\[
1\le \frac{X'}{X'_0}
=\frac{N(r)}R\frac{N(f')}{F'}<4.
\]
The two column supports \([u/2,2v]\) therefore rescale into
\([u/8,2v]\), strictly inside the prescribed test interval
\(I'=[u/16,4v]\). The kernels have a common derivative bound
depending on the fixed support and the input test norm, rather than
on \(r,f',k'\) or the individual Poisson scales.

After exclusion removal, the common-test bound for a retained \(r\)
is \(D^\delta(\Sigma')^2S_m\|V\|_{C^m(I')}^2\), where \(S_m\)
is the normalized child supremum. There are \(O(R)\) choices of \(r\).
Their exterior coefficient is \(O(\Sigma R/L^2)\) up to divisor
losses. Consequently each dyadic block costs
\[
\frac{\Sigma R}{L^2}\,R\,(\Sigma')^2
=\frac{\Sigma R}{L^2}\,R\,\left(\frac LR\right)^2
=\Sigma.
\]
Both the factor \(R\) from ideal counting and the squared normalization
are necessary. The divisor factors and finitely many dyadic blocks are
absorbed in a reserved small power of \(D\).

The row-dependent smooth-kernel lemma needs \(2m+4\) derivatives at
the second transform, then \(2(2m+4)+4=4m+12\) at the first.
Its proof uses a common pointwise Mellin majorant before summing rows;
it does not select an arbitrary column coefficient sequence separately
for each row.

## All cube ranges and strict contraction

For the canonical argument, assume
\[
H,X,F\ge1,\qquad \Sigma=XF\le D^{C_0},\qquad
H/\Sigma\le D^{-\kappa},\qquad \kappa>0.
\]
Cube inversion uses
\[
H_c^3=\min(X,X^2/H^2),\qquad L_b=X/N(b)^3.
\]
The [completed mean-square review](../reviews/COMPLETED_MEAN_SQUARE_REVIEW_20261012.md)
supplies the short-cube bound. Its applicability follows from
\(X/N(h)^3\ge1\) for \(N(h)\le H_c\), and
\(H^2FH_c^3/X\le XF=\Sigma\). If \(H_c<1\), that sum is empty.
The source uses the completed estimate with range \(C_0+1\) to
cover the auxiliary shell \(N(f)<2F\le2D^{C_0}\).
The Möbius identity uses complete multiplicativity including zeros;
it imposes no coprimality between the cube and squarefree indices.

For long cubes with \(L_b\le1\), support either makes the column empty
or forces \(L_b\ge1/v\) and leaves \(O_I(1)\) columns. Ideal and row
counting then give \(\mathcal E(H,L_b,F)\ll_I H/L_b\le v\Sigma\)
times the squared sup norm. These terms are handled directly.
If \(H^2\le X\), then \(H_c^3=X\), so every long cube has
\(L_b<1\) and the transfer supremum is empty.

For any remaining cube, \(N(b)>H_c\) and \(L_b>1\) imply
\(H^2>X\) and \(H_c^3=X^2/H^2\). The transfer proposition applies
with column scale \(L_b\) and target \(\Sigma=XF\), since
\(L_bF\le XF\) and \(H\le\Sigma\). Every child consequently has
\[
\begin{aligned}
H'&\le\frac{HL_b}{\Sigma F}
 =\frac H{N(b)^3F^2}
 <H\left(\frac H\Sigma\right)^2
 \le D^{-2\kappa}H,\\
H'/\Sigma'&\le H/\Sigma\le D^{-\kappa},\qquad
\Sigma'\le L_b\le\Sigma\le D^{C_0}.
\end{aligned}
\]
The strict inequality follows from the strict cube cutoff. It holds
even when \(H_c<1\) and the unit cube belongs to the long range:
then \(X^2/H^2<1=N(1)^3\). The independent target scale is essential;
substituting the smaller target \(L_bF\) would lose this stated
contraction.
In this below-one cutoff case, every divisor qualifies in the long
Möbius sum, so its coefficient vanishes unless \(b=1\). The source's
larger long-cube supremum is still a valid upper bound.

## Finite induction and derivative order

Induct on \(j\ge0\), assuming in addition \(H\le D^{j\kappa}\).
For \(j=0\), \(H\le1\), the triangle bound and ideal counting give
\[
\mathcal E(H,X,F)\ll_I HX\|W\|_\infty^2
\le\Sigma\|W\|_\infty^2.
\]
Thus \(J_0=1\) is sufficient; no cancellation theorem is used in
this base case.

For \(H\le D^{(j+1)\kappa}\), the contracted child has
\(H'\le D^{(j-1)\kappa}\le D^{j\kappa}\), and keeps the positive
gap and polynomial product range. Its normalized \(C^m\) test is
covered by the induction hypothesis on the enlarged interval \(I'\).
Derivative order is independent of the support interval, while
constants may depend on that interval. Only finitely many enlargements
occur.
At the first induction step, the sharper bound is \(H'<1\) for
\(D>1\), so the child supremum is empty; there is no negative-level
induction call.

Choose the child exponent loss \(\varepsilon/3\), the transfer loss
\(\varepsilon/3\), and the cube-reduction loss \(\varepsilon/3\).
A sufficient recursive choice is
\[
J_{j+1}(\varepsilon)\ge
\max\!\left\{
J_{\rm cube}(\varepsilon/3,C_0),
4J_j(\varepsilon/3)+12
\right\}.
\]
This is finite at every fixed \(j,\kappa,C_0,\varepsilon\).
Taking \(j_*=\lceil C_0/\kappa\rceil\) covers all
\(H\le\Sigma\le D^{C_0}\). Empty child suprema contribute zero and
need no induction call.

This checks the canonical induction under the audited completed-sum
and transfer bounds. The transformations retain their stated arithmetic
and analytic imports; finite numerical checks do not establish them.
The final extraction and zero-free claim require their own end-to-end
source assessment.
