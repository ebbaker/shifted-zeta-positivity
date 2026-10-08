# A uniform primitive-kernel bound and a larger controlled overlap sector

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is a same-model derivation for review, not independent specialist
validation or a replay of the imported analytic source.

## Result and scope

The complete transformed row kernel has a uniform bound at every scale:

\[
 |\mathcal K_f(m_1,m_2)|\ll_\Phi
 \tau(\mathfrak g)\sqrt Q,\qquad
 \mathfrak g=(m_1,m_2),\quad
 Q=N(m_1m_2)/N(\mathfrak g)^2,\quad m_1\ne m_2.
\tag{1}
\]

Combining it with counting by the common factor gives, for a dyadic block
\(Nb\asymp B,Nf\asymp F,N\mathfrak g\asymp G\),

\[
 |\mathfrak S^\circ_{\xi;B,F,G}|
 \ll_\varepsilon D^\varepsilon
 \min\left\{\frac{D^2}{B^2FG},
                 \frac{HD}{BF^2G^2}\right\}.
\tag{2}
\]

In particular, the union of dyadic blocks with
\(BF^2G^2\ge D^{1-a}\) contributes
\(O_\varepsilon(D^{h+a+\varepsilon})\), when \(H=D^h\).
This controls an additional overlap sector below the earlier rapid-decay
threshold \((Nf)^2N\mathfrak g\ge HD^{2\eta}\). It does not estimate
the low-overlap core, and it does not establish a new signed saving there.

## Source conventions and the actual kernel

Use the setting of
[the corrected small-cofactor note](SHORT_FAMILY_SMALL_COFACTOR_20261008.md), equations (2)--(8),
with the source's exact conjugations. The October 5 source PDF has SHA-256
`f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18`.
Rendered pages 13 and 16 were inspected. They give

\[
 a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n),\qquad
 W_0(t)=t^{-1/2}\overline{W(t)},\qquad
 \overline{\nu(t)}G(t^{-1})=\sum_\xi c_\xi\xi(t).
\tag{3}
\]

The transformed profile is
\(W_0(N(bfm_1)/D)\overline{W_0(N(bfm_2)/D)}\), as in source
equation (4.16). The displayed unbarred \(\alpha\) and unbarred \(W\)
in the earlier repository note have been corrected; see the
[source audit](SHORT_FAMILY_CORE_INVOLUTION_20261008.md). The bound here uses only \(|a_\xi|=1\)
on its actual squarefree support and the bounded profile, so it is
unaffected numerically by those corrections.

With all original masks retained, the actual kernel is

\[
 \mathcal K_f(m_1,m_2)=\sum_{k\in\mathcal O\setminus\{0\}}
 \chi_{m_1}(k)\overline{\chi_{m_2}(k)}
 \widehat\Phi\left(\frac{Nk}{R_{12}}\right),\qquad
 R_{12}=\frac{(Nf)^2Nm_1Nm_2}{H}.
\tag{4}
\]

Since the columns are squarefree and distinct, their ratio has a
nonprincipal primitive character \(\psi_{\mathfrak c}\) of conductor
\(\mathfrak c=m_1m_2/\mathfrak g^2\), prime to \(\mathfrak g\).
The exact identity is

\[
 \chi_{m_1}(k)\overline{\chi_{m_2}(k)}
 =\psi_{\mathfrak c}(k)\mathbf1_{(k,\mathfrak g)=1}.
\tag{5}
\]

The moving coprimality mask has not disappeared. The conductor statement
and the finite Gauss/reciprocity conventions are the same imported finite
arithmetic inputs used in the earlier note. The analytic step below is
the source's primitive Poisson formula, Lemma 4.2, valid for every
positive row scale; it does not invoke Proposition 5.1 outside its range.

## The uniform kernel estimate

Let \(\widetilde\Phi\) be the radial Fourier transform of
\(\widehat\Phi\). It is a fixed Schwartz function. There is a constant
depending on finitely many Schwartz seminorms such that

\[
 t\sum_{\ell\ne0}|\widetilde\Phi(tN\ell)|\ll_\Phi1
 \qquad(t>0).
\tag{6}
\]

For \(0<t\le1\), lattice counting and Schwartz decay bound the sum by
\(O(t^{-1})\). For \(t\ge1\), the positive shortest lattice norm and
Schwartz decay bound it by \(O_A(t^{-A})\) for any fixed \(A>1\).
This proves (6) without a restriction on \(t\).

Apply the masked primitive Poisson formula to (4). For each divisor
\(d\mid\mathfrak g\), the prefactor has magnitude
\(R_{12}/(Nd\sqrt Q)\), and the frequency scale is

\[
 t_d=\frac{R_{12}}{Nd\,Q}.
\tag{7}
\]

Every zero-frequency term vanishes because \(\psi_{\mathfrak c}\) is
nonprincipal. The normalized primitive Gauss factor has modulus one.
The term for \(d\) is consequently bounded by

\[
 \frac{R_{12}}{Nd\sqrt Q}
 \sum_{\ell\ne0}|\widetilde\Phi(t_dN\ell)|
 \ll_\Phi\frac{R_{12}}{Nd\sqrt Q}\,t_d^{-1}
 =O_\Phi(\sqrt Q).
\tag{8}
\]

Summing over divisors proves (1). This is a smooth two-dimensional
primitive-character completion bound. It is uniform even when the
smallest frequency scale is below one.

The original compact support of \(\widehat\Phi\) also gives
\(|\mathcal K_f|\ll_\Phi R_{12}\) by lattice counting. This holds
for every \(R_{12}>0\): if its support contains a nonzero lattice point,
then \(R_{12}\) is bounded below by a fixed positive constant; otherwise
the sum is zero. Therefore

\[
 |\mathcal K_f|\ll_{\Phi,\varepsilon}D^\varepsilon
 \min\{R_{12},\sqrt Q\}.
\tag{9}
\]

## Counting an overlap block

Use dyadic lower endpoints \(B,F,G\in\{1,2,4,\ldots\}\). Restrict to
\(B\le Nb<2B\), \(F\le Nf<2F\), and
\(G\le N(m_1,m_2)<2G\). The fixed original profile gives

\[
 Nm_j\asymp X=\frac D{BF},\qquad
 R_{12}\asymp\frac{D^2}{HB^2},\qquad
 \sqrt Q\asymp\frac XG.
\tag{10}
\]

For each possible common ideal \(\mathfrak g\) in its block, there are
\(O(X/G)\) choices for each quotient \(m_j/\mathfrak g\). There are
\(O(G)\) possible common ideals, hence

\[
 \#\{(m_1,m_2):Nm_j\asymp X,
                    G\le N(m_1,m_2)<2G\}\ll\frac{X^2}{G}.
\tag{11}
\]

Dropping squarefreeness, coprimality and the diagonal exclusion here only
enlarges the count. Fixed profile constants handle bounded nonempty
lengths; an impossible length block is empty.

The transformed exterior factor is \(HN b/D^2\). There are \(O(B)\)
choices of \(b\) and \(O(F)\) choices of \(f\). All Gauss coefficients,
characters and \(\mu_K(f)\) have modulus at most one. Thus the cost is

\[
 \frac{HB^2F}{D^2}\frac{X^2}{G}
 D^\varepsilon\min\left\{\frac{D^2}{HB^2},\frac XG\right\},
\tag{12}
\]

which is exactly (2). One allocates a smaller preliminary epsilon before
absorbing the divisor factors and the \(O((\log D)^3)\) possible blocks.

The bound also holds after **any additional selector on \(b,f,m_1,m_2\)**
that is independent of \(k\), since it bounds an absolute majorant after
the whole \(k\)-kernel has been assembled. It does not justify a sharp
selector inside that \(k\)-sum or an arbitrary enlargement of a signed
quadratic form.

## The additional removable region

Fix \(0<h<1\), \(a\ge0\), and \(H=D^h\). For every block satisfying

\[
 BF^2G^2\ge D^{1-a},
\tag{13}
\]

equation (2) is \(O_\varepsilon(D^{h+a+\varepsilon})\). Summing these
blocks keeps that estimate after epsilon reallocation. If a fixed
power reserve \(\kappa>0\) is useful, the buffered condition
\(BF^2G^2\ge D^{1-a+\kappa}\) instead saves \(D^\kappa\).

These are statements about dyadic lower endpoints, so there is no
unaccounted constant in the cutoff. If expressed in actual norms, every
term with \((Nb)(Nf)^2N(m_1,m_2)^2\ge32D^{1-a}\) belongs to a block
satisfying (13). Boundary blocks can simply remain in the residual.

Use the source's positive theorem on complete large-\(b\) blocks first,
as in the preceding note. Then remove its rapid-decay pair sector, and
finally apply (13) to the remaining pairs. This last step is permitted
by the selector observation after (12). The new sufficient residual
may be confined to

\[
 Nb<D^{1-h+\eta},\qquad
 (Nf)^2N(m_1,m_2)<HD^{2\eta},\qquad
 BF^2G^2<D^{1-a},\qquad m_1\ne m_2,
\tag{14}
\]

with the understood retained boundary blocks if the first condition is
implemented using dyadic cutoffs. The exact source coefficients, all
zero masks and complete smooth row kernels remain. The overall
decomposition is now an \(O(D^{h+a+\varepsilon})\) controlled part,
plus the signed residual (14), plus the already available rapid error.
No bound for that signed residual has been obtained.

Ignoring fixed buffers only to display exponents, in the \(b=f=1\)
block the two pair removals leave

\[
 G<\min\{D^h,D^{(1-a)/2}\}.
\tag{15}
\]

For \(a=0\), this is a genuine expansion of the controlled overlap
range for both \(h=8/9\) and \(h=2/3\): the old cutoffs were respectively
\(D^{8/9}\) and \(D^{2/3}\), whereas the new cutoff is \(D^{1/2}\).
At \(h=1/4\) it gives no additional removal in the \(b=f=1\) block,
although it can still help at larger \(b\). With a buffer \(\kappa\),
replace the new exponent by \((1-a+\kappa)/2\).

The complete block estimate has a second possible sufficient condition,
\(B^2FG\ge D^{2-h-a}\), from its trivial-kernel branch. The minimum in
(2) records both available bounds. On the ideal small-\(b\) range
\(B\le D^{1-h}\), the primitive-kernel branch is at least as strong,
since the ratio of the first bound to the second is
\(DFG/(HB)\ge1\).

## What this does not establish

At \(B=F=G=1\), the new generic estimate is only
\(O(D^{h+1+\varepsilon})\). It reaches \(D^{h+a}\) only if \(a\ge1\),
far outside the useful improvement range
\(a+5h/6<3/4\). The source-correct second Poisson transformation of the
summed-\(\xi\) coprime core returns the original coprime off-diagonal
Möbius form. It is not a new signed estimate for that form.

The [core-involution note](SHORT_FAMILY_CORE_INVOLUTION_20261008.md)
proves that the prime-selected part alone has size
\(\gg DH^{1/6}/(\log D)^2\) for a nonnegative profile and trivial
fixed twist. This exceeds every useful target by more than a quarter
power. A proof must preserve cancellation across column types; estimating
each prime/composite part separately by the desired budget cannot work.
The unrestricted signed form remains open.

The new contribution here is (1)--(14), a larger controlled overlap
sector. It is an absolute estimate of complete primitive row kernels,
not the missing signed low-overlap estimate or a new zero-free region.
