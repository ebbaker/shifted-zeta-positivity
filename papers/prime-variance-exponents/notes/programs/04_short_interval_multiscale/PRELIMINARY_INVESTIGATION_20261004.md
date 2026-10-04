# Preliminary investigation: long intervals, a common mode, and the exact covariance

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Internal analytic investigation, not independent specialist refereeing.
No new global exponent is proved.

The fixed-saving objective allows longer intervals than the previously
emphasized \(X^{11/12}\): sixth-order reconstruction permits
\(h=X^{1-\kappa/12}\) when the intended variance is
\(X^{3-\kappa}\). This is useful flexibility, but the three lengths
share an uncancelled coarse arithmetic mode. The exact decomposition below
shows what a proposed covariance contraction would have to control.

## 1. Inherited exact transfer and a sharper first-saving budget

Use the complete definitions of \(D_h,V_h,w,A,B\) in the
[higher-order reconstruction note](../../HIGHER_ORDER_SHORT_INTERVAL_RECONSTRUCTION_20261004.md).
For \(a=(1,1/2,1/4)\), \(c=(1,-20,64)/45\), put

\[
V_i=V_{a_i h},\qquad R_{6,h}=\sum_{i=0}^2c_iV_i.
\]

All functions below are in \(L^2([X,2X])\), with real sufficiently
large \(X\). The inherited complete-cap bound, using its stated
Montgomery--Vaughan sieve input, is

\[
\|R_{6,h}-V\|_2\ll_{w,\eta}X^{6\eta-9/2},
\qquad h=X^\eta,\quad 1/2<\eta<1.
\tag{1}
\]

For the first-saving target the error need only be at most
\(X^{(3-\kappa)/2}\), so (1) gives the fresh admissible range

\[
\boxed{\eta\le1-\kappa/12.}
\tag{2}
\]

The corresponding second- and fourth-order ranges follow from their
inherited norm errors \(h^2X^{-1/2}\) and \(h^4X^{-5/2}\):

| Reconstruction | Approximation energy | Maximum \(\eta\) at saving \(\kappa\) | At \(\kappa=1/100\) |
| --- | --- | --- | --- |
| One box \(V_h\) | \(X^{4\eta-1}\) | \(1-\kappa/4\) | \(399/400\) |
| Fourth order | \(X^{8\eta-5}\) | \(1-\kappa/8\) | \(799/800\) |
| Sixth order | \(X^{12\eta-9}\) | \(1-\kappa/12\) | \(1199/1200\) |

At any such fixed \(\eta\), the exact target
\(\|R_{6,h}\|_2^2=O(X^{3-\kappa})\) is equivalent to the same
target for \(V\), by the reverse triangle inequality. A bound with
\(X^{o(1)}\) losses also gives the exact final endpoint through the
overview's closed-strip argument. This supersedes the older
reconstruction note's endpoint caveat; it does not produce the bound.

The constants and starting threshold depend on the fixed \(\eta\).
At exponents close to one, \(h\le AX\) may start extremely late.
No uniform estimate as \(\eta\to1\), and no result at \(h\asymp X\),
is asserted by (1).

## 2. The full matrix and its coarse-mode coordinates

Let \(W_X(t,u)=\int_X^{2X}w(t/x)w(u/x)dx\). The exact matrix is

\[
H_{ij}(X,h)=\langle V_i,V_j\rangle
=\frac1{a_i a_jh^2}
\int_{AX}^{2BX}\!\int_{AX}^{2BX}
D_{a_i h}(t)D_{a_j h}(u)W_X(t,u)\,dt\,du.
\tag{3}
\]

It is a positive semidefinite Gram matrix, without any entrywise sign
assertion. Every coordinate cap, interval normalization, and terminal
prime band is inherited from the exact \(D_h\). Its required signed
scalar is \(c^THc\), not a diagonal or a sum of positive entries.

Set

\[
C=V_h,\quad d_1=V_{h/2}-V_h,\quad
d_2=V_{h/4}-V_{h/2},\quad
D=\frac{44}{45}d_1+\frac{64}{45}d_2.
\]

Exact arithmetic gives

\[
\boxed{R_{6,h}=C+D,\qquad
\|R_{6,h}\|^2=\|C\|^2+2\langle C,D\rangle+\|D\|^2.}
\tag{4}
\]

For \(\|C\|>0\), define
\(\lambda=\langle C,D\rangle/\|C\|^2\) and
\(D_\perp=D-\lambda C\). Then

\[
\boxed{\|R_{6,h}\|^2=(1+\lambda)^2\|C\|^2+\|D_\perp\|^2.}
\tag{5}
\]

Thus a large coarse response can be removed only by a quantitatively
negative aligned correction \(\lambda\approx-1\), with the
orthogonal residual also controlled. Small differences alone leave the
coarse response. If \(C=0\), the formula is simply \(\|D\|^2\).

Equivalently, any exactly common component \(L\) of the three
responses survives with coefficient \(\sum c_i=1\). The cancellation
conditions \(\sum c_i a_i^2=\sum c_i a_i^4=0\) remove smoothing
errors, not the common component itself.

## 3. Fresh check against a positive PNT slow-mode model

This is a structural diagnostic, not a model of the actual Euler product.
Choose fixed \(1/2<\beta<1\), \(\gamma\ne0\),
\(\rho=\beta+i\gamma\), and \(0<\epsilon<1\). On \(t\ge1\), take

\[
d\psi_{\rm mod}(t)=
[1+\epsilon t^{\beta-1}\cos(\gamma\log t)]dt.
\tag{6}
\]

This is positive and satisfies \(\psi_{\rm mod}(t)=t+O(t^\beta)\).
All caps lie above one for sufficiently large real \(X\). Because
\(\int w=0\), its complete response is exactly

\[
V_{\rm mod}(x)=\epsilon\operatorname{Re}[x^\rho W(\rho)],
\qquad W(s)=\int_A^B w(u)u^{s-1}du=G(1/2-s).
\tag{7}
\]

Here \(G(z)=\int g(t)e^{zt}dt\) uses the manuscript's plus-exponent
convention; the substitution \(u=e^{-t}\) fixes the displayed sign.
The inherited noncancellation theorem gives \(W(\rho)\ne0\).
For fixed \(\rho\), Taylor expansion of the density on the interval
gives, uniformly on the shell,

\[
\frac1h\int_{-h/2}^{h/2}(t+v)^{\rho-1}dv
=t^{\rho-1}
+\frac{(\rho-1)(\rho-2)}{24}h^2t^{\rho-3}
+O_\rho(h^4t^{\beta-5}).
\tag{8}
\]

Hence for every fixed \(\eta<1\),

\[
V_{a_i h,\rm mod}=V_{\rm mod}+O_{w,\rho}(X^{\beta+2\eta-2}),
\qquad
\|d_j\|_2=O(X^{\beta+1/2+2\eta-2}).
\tag{9}
\]

There are constants depending on \(\rho,w,\epsilon\) for which
\(\|V_{\rm mod}\|_2^2\asymp X^{2\beta+1}\). To check the lower
bound uniformly in the phase \(\gamma\log X\), integrate on
\([1,2]\): the Gram matrix of
\(u^\beta\cos(\gamma\log u)\) and
\(u^\beta\sin(\gamma\log u)\) is positive definite when
\(\gamma\ne0\). Thus the leading matrix in (3) is

\[
H_{ij,\rm mod}=\|V_{\rm mod}\|_2^2
+O(X^{2\beta+1+2\eta-2}),
\tag{10}
\]

a common rank-one mode. Since \(c^T(1,1,1)=1\), it survives with
the same leading energy. More precisely, expanding through sixth order
shows

\[
R_{6,h,\rm mod}-V_{\rm mod}
=\frac{h^6}{20643840}\epsilon\operatorname{Re}
\left[(\rho-1)\cdots(\rho-6)x^{\rho-6}W(\rho-6)\right]
+O_{w,\rho}(h^8X^{\beta-8}).
\tag{11}
\]

Here the smooth model permits the expansion; it does not improve the
sixth-derivative-measure estimate for actual prime atoms. In (5), this
model has \(\lambda\to0\), not \(-1\).

If \(\beta>1-\kappa/2\), its surviving energy exceeds
\(X^{3-\kappa}\). Positivity, PNT, exact reconstruction, and small
cross-length differences therefore do not imply the desired contraction.
An actual \(\Lambda\)-identity must supply the missing information.

## 4. A precise next gate and assessment

At \(h=X^\eta\), with (2), either of the following would suffice:

1. A direct signed bound \(c^TH(X,h)c\ll X^{3-\kappa+o(1)}\).
2. The stronger raw interval bound
   \(\int_{AX}^{2BX}|[D_h-40D_{h/2}+256D_{h/4}]/45|^2dt
   \ll Xh^2X^{-\kappa+o(1)}\).

The second gate includes the narrower interval normalizations. An
exceptional center set \(\mathcal E\) cannot be discarded: under the
available long-interval cap bound \(|D_{a_i h}|\ll_\eta h\), its
raw cost is \(O(h^2|\mathcal E|)\), so a sufficient exceptional-set
budget is \(|\mathcal E|\ll X^{1-\kappa+o(1)}\). A logarithmically
small exceptional fraction is insufficient for this crude treatment.

**Assessment:** useful supporting program, especially if an arithmetic
input becomes effective only at very long sublinear lengths. It is not
presently a top-three independent proof mechanism: the new length
flexibility leaves a precisely identified coarse arithmetic mode. Before
further computation, identify a source or \(\mu/\Lambda\) relation
that controls this mode or the signed scalar (3).

## Verification

Standard-library rational arithmetic checked
\(\sum c_i a_i^j=(1,0,0,1/64)\) for \(j=0,2,4,6\), the coefficient
\(1/20643840\), the change of coordinates \((1,44/45,64/45)\), and
the three \(\kappa=1/100\) table entries. Formulas (3)--(11) were
checked algebraically, retaining real-shell and endpoint conventions.
The sieve input and endpoint measure treatment are inherited from the
linked reconstruction note; no new numerical asymptotic or prime sample
is used.
A separate same-model agent checked the budget and covariance algebra;
parent review checked the displayed Mellin-transform sign convention.
