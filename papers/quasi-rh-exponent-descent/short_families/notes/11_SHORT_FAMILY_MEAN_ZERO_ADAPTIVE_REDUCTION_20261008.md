# Zero integral profiles and a conductor dependent factorization cutoff

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Derivations and same-model reviews are internal checks, not independent
specialist validation or formal proof replay.

Based on commit 480581447dcd3e93c9c2f9c22a050d9c5100ff9d and the
working-tree [continuation in note 10](10_SHORT_FAMILY_FACTORIZATION_CONTINUATION_20261008.md).

## Result and scope

The principal correction in note 8 can be removed by a legitimate choice
of profile, without removing any row or any relevant Mellin detector.
Choose

\[
 W(t)=(1+t\partial_t)V(t),\qquad V\in C_c^\infty((0,\infty)).
\tag{1}
\]

Then \(\int W(t)\,dt=0\), and its Mellin transform is
\(\widehat W(s)=(1-s)\widehat V(s)\). This class detects every
\(\rho\ne1\), so it still suffices for the zero-free conclusion after
the conditional short-family extraction. No arithmetic moment is
proved by changing the profile.

There is also a sharper factorization cutoff. For each row \(u\ne0\),
let \(Q_u\) be the primitive conductor norm and \(E_u\) its extra
squarefree deletion ideal, as in note 8, and put

\[
 L_u=Q_uNE_u,\qquad Y_u=D^{1-\theta}/L_u,\qquad 0<\theta<1.
\tag{2}
\]

For the profiles (1), the part of the exact convolution with
\(Nd\le Y_u\) has normalized mean square \(O_N(D^{-N})\) for
every requested \(N>0\), with the original complete Schwartz row weight.
Thus the remaining target is an actual convolution tail, with no
principal correction:

\[
 \boxed{\frac1D\sum_{u\ne0}\Phi(Nu/D^h)|T_u^{\rm ad}(D)|^2
             \ll_\varepsilon D^{h+a+\varepsilon},\qquad
 T_u^{\rm ad}=-\sum_{Nd>Y_u}c_z(d)\lambda_u(d)S_u(D/Nd).}
\tag{3}
\]

The sum in (3) remains unproved. Its cutoff depends on the row; it is
legal here because the exact factorization and completion are applied
pointwise before the square is taken. It is not an arbitrary selector
inside the earlier transformed complete-row kernels.

## The profile class preserves detection

Integration by parts in (1), with zero endpoint terms, gives

\[
 \int_0^\infty W(t)\,dt=0,\qquad
 \widehat W(s)=\int_0^\infty W(t)t^s\,\frac{dt}{t}
              =(1-s)\widehat V(s).
\tag{4}
\]

For any fixed \(\rho\ne1\), take a nonzero nonnegative smooth
\(\phi\) supported in a fixed annulus and \(V(t)=t^{-\rho}\phi(t)\).
Then

\[
 \widehat W(\rho)=(1-\rho)\int_0^\infty\phi(t)\,\frac{dt}{t}\ne0.
\tag{5}
\]

Consequently the common Mellin zero of this profile class is exactly
\(s=1\). It removes no potential nontrivial zero with
\(1/2<\Re\rho<1\), nor any point \(1+it\) with \(t\ne0\).
The classical treatment at \(s=1\) is retained separately; this is not
a claim to detect a zero there with (1).

The finite prime-mask recurrence in note 1 uses the same profile at
each scale and works unchanged for these signed or complex profiles.
A bound (3) for every profile (1) would therefore give

\[
 |A_{1,W}(D)|\ll_\varepsilon
 D^{b+\varepsilon},\qquad
 b=\frac{1+a}{2}+\frac{5h}{12}.
\tag{6}
\]

The original scalar Mellin identity
\(\mathcal M_W(s)=\widehat W(s)/L_K^S(s,\nu)\), in the
[October 5 source](https://raw.githubusercontent.com/openai/math/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
Section 3, then excludes every zero \(\rho\ne1\) with
\(\Re\rho>b\). The Mellin identity and character presentation retain
their imported status; equations (4)--(5) establish the new profile
qualification. No contour hypothesis uniform in a changing conductor
has been substituted for a proved moment.

## Recovery of arbitrary profiles for sharp row moments

There is a stronger norm comparison in the useful range \(h+a<1\).
For this comparison only, use the classical fixed-character boundary
input

\[
 A_{u,V}(t)/t\longrightarrow0\quad(t\longrightarrow\infty)
 \quad\hbox{for each fixed }u\ne0.
\tag{B}
\]

Here \(A_{u,V}\) is the Möbius amplitude with profile \(V\).
The ordinary fixed-character Möbius prime number theorem supplies (B);
it is an explicitly retained analytic input, not a new conductor-uniform
estimate. The direct detector argument above does not need this recovery.

Differentiating the finite smooth sum gives
\[
 A_{u,W}(t)=(1-t\partial_t)A_{u,V}(t).
\]
Integration using (B) yields the exact identity

\[
 A_{u,V}(D)=D\int_D^\infty A_{u,W}(t)\,\frac{dt}{t^2}.
\tag{7}
\]

Suppose the sharp zero-integral moment holds for this \(W\):
\[
 \sum_{0<Nu\le t^h}|A_{u,W}(t)|^2
                \ll_\varepsilon t^{1+h+a+\varepsilon}.
\tag{8}
\]
For the finite fixed set \(0<Nu\le D^h\), Minkowski and positive
enlargement of the row set for \(t\ge D\) give

\[
 \begin{split}
 \left(\sum_{0<Nu\le D^h}|A_{u,V}(D)|^2\right)^{1/2}
 &\le D\int_D^\infty
       \left(\sum_{0<Nu\le t^h}|A_{u,W}(t)|^2\right)^{1/2}
                  \frac{dt}{t^2}\\
 &\ll_\varepsilon
       \frac{D^{(1+h+a+\varepsilon)/2}}
            {1-(1+h+a+\varepsilon)/2}.
 \end{split}
\tag{9}
\]

Choose a smaller preliminary epsilon so that \(h+a+\varepsilon<1\).
This proves the sharp moment for \(V\) with the same exponents.
No uniformity in the constants of (B) is needed: the boundary is used
only for the finite row set at the fixed \(D\), and (8) dominates the
integral. Thresholds on bounded \(t\) are absorbed in the usual constants.

Thus, subject to (B), the derivative-profile sharp moment and the
all-profile sharp moment are equivalent for \(h+a<1\). The reverse
implication is just restriction to the profile (1). This comparison
does not assert recovery of an arbitrary Schwartz-weighted all-row
moment; the hypothesis (3) nevertheless supplies (8), since
\(\Phi\ge1\) on its inner norm ball. If uniform profile seminorms are
claimed, the map (1) costs one additional derivative.

## The exact combined modulus and its weighted row mass

Let \(\operatorname{rad}_S(u)\) denote the product of the good primes
dividing \((u)\). At every such prime, a valuation nonzero modulo six
gives primitive conductor exponent one; a positive valuation zero modulo
six gives only a deletion prime. Therefore

\[
 N\operatorname{rad}_S(u)\le L_u
       \ll_{\nu,S}N\operatorname{rad}_S(u),\qquad Q_u\le L_u.
\tag{10}
\]

The fixed bad part belongs to a bounded finite family. These are the
same imported tame character and reciprocity inputs as in note 8.
Keeping the conductor and mask together avoids paying two copies of
the row modulus.

For every \(\delta>0\), an elementary ideal Euler product converges:
\[
 \sum_{\mathfrak n}
 \frac{4^{\omega(\operatorname{rad}_S\mathfrak n)}}
      {N\operatorname{rad}_S(\mathfrak n)(N\mathfrak n)^\delta}
 =
 \prod_{p\notin S}
 \left(1+\frac{4(Np)^{-1-\delta}}{1-(Np)^{-\delta}}\right)
 \prod_{p\in S}(1-(Np)^{-\delta})^{-1}<\infty.
\tag{11}
\]
The equality uses \(\operatorname{rad}_S\) in the denominator and
unit-free ideal counting. Lifting to elements pays only six units.
Since a fixed Schwartz function satisfies
\(\Phi(Nu/H)\ll_\delta H^\delta(Nu)^{-\delta}\), (10)--(11) imply

\[
 \sum_{u\ne0}\Phi(Nu/H)
       \frac{\tau(E_u)^2Q_u}{L_u^2}
                      \ll_{\nu,S,\Phi,\delta}H^\delta.
\tag{12}
\]

This is a small weighted mass, rather than a count of all rows.
For the sharp inner ball, (11) also gives
\(\sum_{0<Nu\le H}(N\operatorname{rad}_S(u))^{-1}\ll_\delta H^\delta\).
On rows with \(L_u\le R\), \(N\operatorname{rad}_S(u)\le R\), so
\(\#\{0<Nu\le H:L_u\le R\}\ll_\delta RH^\delta\).
This count uses (11) directly; (12) alone would not give it.
Neither bound deletes repeated rows or their character masks.

## Adaptive completion and the negligible small product

For general \(W\), put \(I_W=\int W(t)\,dt\). The refined pointwise
version of note 8's completion is

\[
 S_u(X)=\kappa_u X I_W+\mathcal V_u(X),\qquad
 |\mathcal V_u(X)|\ll_{A,W}
             \tau(E_u)\sqrt{Q_u}(L_u/X)^A,\quad X>0.
\tag{13}
\]

Indeed each divisor \(e\mid E_u\) has Poisson frequency scale
\(X/(NeQ_u)\); the full nonzero-frequency Schwartz sum costs
\(O_{A,W}(\sqrt{Q_u}(NeQ_u/X)^A)\). The principal zero frequency
is retained in \(\kappa_u XI_W\). We use \(\mathcal V_u=S_u-\kappa_u XI_W\)
to avoid changing any Fourier normalization.

Define
\[
 I_u^{\rm ad}=-\sum_{Nd\le Y_u}c_z(d)\lambda_u(d)S_u(D/Nd),
 \qquad
 P_u^{\rm ad}=-\kappa_u D I_W
       \sum_{Nd\le Y_u}\frac{c_z(d)\lambda_u(d)}{Nd}.
\tag{14}
\]
If \(Y_u<1\), both sums are empty. Otherwise
\(\sum_{Nd\le Y_u}|c_z(d)|\ll Y_u\log(2D)\), and (13) gives

\[
 |I_u^{\rm ad}-P_u^{\rm ad}|
 \ll_{A,W}
 \frac{D^{1-\theta}}{L_u}\log(2D)\tau(E_u)\sqrt{Q_u}D^{-A\theta}.
\tag{15}
\]

Combining (12) with (15) proves
\[
 \frac1D\sum_{u\ne0}\Phi(Nu/H)|I_u^{\rm ad}-P_u^{\rm ad}|^2
 \ll_{A,\delta}D^{1-2\theta-2A\theta}\log^2(2D)H^\delta.
\tag{16}
\]
For \(1\le H\le D\), choose \(A\) after \(\theta,\delta\) and the
requested error power. This gives arbitrary power decay without a
sharp row truncation. For (1), \(P_u^{\rm ad}=0\) identically, so
the discarded contribution is the actual small-product amplitude.
The two norm inequalities in note 8 establish (3) as the equivalent
zero-integral full-moment target.

For completeness, general profiles have an exact alternative main-term
recombination. With
\[
 M_z(u)=\sum_{Na\le z}\frac{\mu_K(a)\lambda_u(a)}{Na},
\]
finite convolution gives
\[
 T_u^{\rm ad}+P_u^{\rm ad}
 =-\kappa_u D I_W M_z(u)^2
   -\sum_{Nd>Y_u}c_z(d)\lambda_u(d)\mathcal V_u(D/Nd).
\tag{17}
\]
The square is an ordinary square, not an absolute square. This identity
retains all factorization coefficients; it estimates neither term.
For zero-integral profiles its first term vanishes.

## Short free factors on rows with small conductor

On the tail, write \(d=ab\) with \(Na,Nb\le z=(CD)^{1/2}\).
The exact support gives
\[
 Nm\ll_W D^\theta L_u,\qquad
 Na,Nb\gg_W D^{1/2-\theta}/L_u.
\tag{18}
\]
For a row \(u=\eta vr^6\), with \(v\) sixth-power-free,
\[
 L_u\ll_{\nu,S}(Nu)^{1/6}(Nv)^{5/6}.
\tag{19}
\]
Thus on the inner ball \(Nu\le H\), \(Nm\ll D^\theta
H^{1/6}(Nv)^{5/6}\). For the complete Schwartz moment, use (18)
pointwise or apply (19) separately on each row shell; there is no global
replacement of \(Nu\) by \(H\).

For coherent rows \(u=r^6\) in the inner ball:

| \(h\) | Lower bound for \(Y_u\) | Upper bound for \(Nm\) | Lower bound for each \(Na,Nb\) |
| --- | --- | --- | --- |
| \(4/5\) | \(D^{13/15-\theta}\) | \(D^{2/15+\theta}\) | \(D^{11/30-\theta}\) |
| \(8/9\) | \(D^{23/27-\theta}\) | \(D^{4/27+\theta}\) | \(D^{19/54-\theta}\) |

Fixed support and arithmetic constants are suppressed in this table.
The free factor is shorter, but the two Möbius factors still require
signed cancellation. [Note 12](12_SHORT_FAMILY_FACTOR_SELECTION_BARRIER_20261008.md)
shows that even a natural prime-by-prime part of the \(m=1\) tail is
too large to estimate separately by the useful budget.

The [scoped review](../../reviews/SHORT_FAMILY_MEAN_ZERO_REVIEW_20261008.md)
and [finite checker](../../numerics/check_short_family_mean_zero.py)
separate the profile and convolution algebra from the imported analytic
inputs. The new short-family estimate and a stronger zero-free boundary
remain open.
