# A fixed short-family moment already removes its prime-mask error

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant
and configured reasoning effort are not exposed and are not inferred.
Same-model analysis and review are internal checks, not independent
specialist validation.

## Result and dependency ledger

The short-family estimate in Route B has a stronger consequence than the
one-step map previously recorded. **One fixed moment at one positive
length exponent can be reused finitely many times to remove the
prime-mask error entirely.** It gives the same extracted exponent as the
previously proposed scale-supremum hypothesis, without that stronger
hypothesis and without an initial zero strip.

This is a new deduction from elementary replication and the existing
mask identity, not a proof of a short-family moment or a new zero-free
region. It sharpens the analytic obligation for Route B. The
[earlier transfer note](../../quasi-rh-character-amplification/notes/CHARACTER_FAMILY_TRANSFER_20261008.md)
and [continuation](CODEX_CONTINUATION_20261008.md), equations (13)--(19),
are the starting records.

| Ingredient | Status used here |
| --- | --- |
| Sextic zero-extension convention; prime ideal counting; squarefree ideal Möbius multiplicativity | Standard arithmetic facts, also used in the cited source extraction |
| Mean square at a fixed short exponent \(h\) | Explicit new hypothesis; not established here |
| Removal of the prime-mask error by finite reuse of that one hypothesis | Proved below |
| Equivalence between a normalized moment on prime sixth-power rows and its target Möbius bound | Proved below |
| Source induction at dual row/column ratio \(<D^{-\kappa}\) | Imported statement; inspected, not independently verified |
| RH, or a stronger strip for the Hecke family | Not proved |

The [October 5 source](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf),
Proposition 3.1 and Sections 4--5, and the
[September 30 source](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
equations (17.87)--(17.90), were inspected in their actual local PDF text.
Their SHA-256 values are respectively
`f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18`
and `8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
No deep analytic proof was replayed and no Lean verification was run.

## 1. Fixed data, all losses, and the exact mask

Work over \(K=\mathbb Q(\sqrt{-3})\). Fix a finite-order Hecke
character \(\nu\), a finite excluded prime set \(S\) containing its
conductor and the primes above 6, and one fixed smooth annular profile

\[
W\in C_c^\infty((0,\infty)),\qquad
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D).
\tag{1}
\]

Rows are elements; ideals outside \(S\) have their fixed primary
generators. The character has its original zero extension. In particular,

\[
\chi_n(p^6)=\mathbf1_{p\nmid n},
\tag{2}
\]

not the constant one. The same argument works with the negative common
orientation because (2) is unchanged. Write \(B_p(L)=A_{p^6}(L)\),
\(q=Np\). Splitting squarefree ideals according to divisibility by \(p\)
gives, with the very same profile,

\[
A_1(L)=B_p(L)-\nu(p)B_p(L/q),\qquad
B_p(L)=\sum_{j\ge0}\nu(p)^jA_1(L/q^j).
\tag{3}
\]

The sum is finite by annular support. No varying-conductor hypothesis
is hidden here: all sums on the right concern the original fixed
character \(\nu\).

Let \(P_{\nu,W}(t)\), for \(t>0\), mean that for every \(\varepsilon>0\)

\[
|A_1(L)|\ll_{\nu,S,W,t,\varepsilon}L^{t+\varepsilon}
\quad(L\ge1).
\tag{4}
\]

Changing the constant handles all nonzero sums at smaller bounded
\(L\). Ideal counting supplies \(P_{\nu,W}(1)\) unconditionally.
From (3), if (4) holds, then uniformly for \(q\asymp D^{h/6}\),

\[
|A_1(D)-B_p(D)|
\ll_{\nu,S,W,t,\varepsilon}(D/q)^{t+\varepsilon}.
\tag{5}
\]

Indeed the geometric series in \(q^{-t-\varepsilon}\) is uniformly
bounded once \(q\ge2\). This proof retains every prime-deletion mask.

## 2. A single-scale hypothesis suffices

Fix \(0<h\le1\) and \(a\ge0\), and suppose that for every
\(\varepsilon>0\), at all sufficiently large \(D\),

\[
\sum_{0<Nu\le D^h}|A_u(D)|^2
\ll_{\nu,S,W,h,a,\varepsilon}D^{1+a+h+\varepsilon}.
\tag{M_{h,a}}
\]

Constants and thresholds may depend on the displayed fixed data.
There is no supremum over smaller column scales and no uniformity over
different \(h\)'s in this hypothesis. Put

\[
b=\frac{1+a}{2}+\frac{5h}{12},\qquad c=1-\frac h6.
\tag{6}
\]

**Proposition.** Hypothesis \((M)_{h,a}\) implies
\(P_{\nu,W}(b)\). In particular, if \(b<1\), its stated bound improves
on ideal counting without any previously assumed zero strip.

**Proof.** Let \(Q=D^{h/6}\), and average over good prime ideals with
\(Q/2<Np\le Q\). The prime ideal theorem for the fixed field, after
removing the finite set \(S\), gives

\[
J(D)\asymp Q/\log Q.
\tag{7}
\]

Their primary sixth powers are distinct element rows and have norm
at most \(D^h\). Thus \((M)_{h,a}\) yields

\[
\frac1{J(D)}\sum_{Q/2<Np\le Q}|B_p(D)|^2
\ll D^{2b+\varepsilon},
\tag{8}
\]

where the logarithm has been absorbed by choosing a smaller preliminary
loss. Applying (5), squaring and averaging proves the implication

\[
P_{\nu,W}(t)\Longrightarrow
P_{\nu,W}\!\left(\max\{b,ct\}\right).
\tag{9}
\]

The usual arbitrary-\(\varepsilon\) quantifier is essential: request a
smaller loss in (4) and \((M)_{h,a}\) before proving (9).

If \(b\ge1\), ideal counting already proves the result. Otherwise start
from \(t_0=1\) and reuse the **same** moment assumption in (9). Since
\(0<c<1\) and \(b>0\), induction gives

\[
t_n=\max\{b,c^n\}.
\tag{10}
\]

Choose any finite \(n\) with \(c^n\le b\). Then \(t_n=b\), proving the
claim. All applications use one character and one profile. The finite
number of new constants or thresholds can be combined; no estimate
uniform in \(n\) is needed. \(\square\)

This does not let a fixed positive \(h\) reach \(1/2\): its floor is
exactly \(b\ge1/2+5h/12\). It does show that the prior strip and the
all-scale supremum in continuation equation (19) are unnecessary for
extracting that floor. The original one-step map remains correct.

For example, \(h=2/3,a=0\) gives \(b=7/9,c=8/9\), and the entirely
conditional finite chain is

\[
1\longmapsto\frac89\longmapsto\frac{64}{81}
\longmapsto\frac79.
\tag{11}
\]

The imported \(7/8\) bound makes this a one-step extraction; it is not
needed for the conclusion. More generally, a single fixed moment beats
\(7/8\) whenever

\[
a+\frac{5h}{6}<\frac34.
\tag{12}
\]

There is no lower restriction such as \(h>3/4\) once the mask error is
handled in this way. Small \(h\) is analytically harder, not obstructed
by this extraction.

## 3. The exact strength of restricting to the repeated rows

For fixed \(0<h\le1\), define

\[
\mathcal R_h(D)=\frac1{J(D)}
\sum_{Q/2<Np\le Q}|A_{p^6}(D)|^2,
\qquad Q=D^{h/6}.
\tag{13}
\]

For every fixed \(0<\beta\le1\), the following are equivalent:

\[
P_{\nu,W}(\beta)
\quad\Longleftrightarrow\quad
\mathcal R_h(D)\ll_\varepsilon D^{2\beta+\varepsilon}
\text{ for every }\varepsilon>0.
\tag{14}
\]

For the forward direction, (3) bounds \(B_p(D)\) by a uniformly
convergent geometric multiple of \(D^{\beta+\varepsilon/2}\).
For the reverse direction, use (5) and the right side of (14) in place
of (8). Starting from \(P(1)\), the same finite iteration has floor
\(\beta>0\), hence proves \(P(\beta)\).

Consequently, an estimate only on prime sixth-power rows concerns a
positive subsum of the full-family obligation, and is sufficient,
but it is **equivalent to the target fixed-character Möbius bound**.
The repeated values do not create cancellation among independent
characters. This equivalence does not rule out proving such an estimate
by new methods; it prevents describing the restriction alone as an
analytic saving or an independent route around the target.

It also gives a sharp coefficient countercheck. If an arbitrary bounded
column weight were allowed, take it to be
\(\mu_K(n)\overline{\nu(n)}\) on squarefree support, with a nonnegative
nonzero profile. The selected coefficients are now the squarefree
indicator, whose unmasked sum is of order \(D\). Removing the multiples
of a prime with \(q\asymp D^{h/6}\) costs \(O(D/q)\) by ideal counting,
so every one of these masked prime sixth-power rows is also of order
\(D\). Their contribution is therefore \(\gg J(D)D^2\). A full-family
theorem in that coefficient class must consequently pay

\[
a+\frac{5h}{6}\ge1.
\tag{15}
\]

For \(a=0\), this is the previously identified obstruction \(h\ge6/5\).
The new deduction concerns the actual Möbius coefficients only.

## 4. Consequences for an RH program and Mellin detection

Suppose the moment is available for a set of fixed pairs \((h,a)\), for
every profile in a class with no common Mellin zero in \(\Re s>1/2\).
By Section 2, each such pair supplies its floor \(b(h,a)\).
If

\[
\inf_{(h,a)}\left(a+\frac{5h}{6}\right)=0,
\tag{16}
\]

then the fixed character has Möbius exponents arbitrarily close to
\(1/2\). This conclusion does not need an initial family strip. Since
\(a\ge0,h>0\), condition (16) is equivalent to having a sequence
\(h_j\to0,a_j\to0\). There is a simpler logical check: these same
full-family assumptions already give, just from the row \(u=1\),

\[
|A_1(D)|\ll D^{(1+a_j+h_j)/2+\varepsilon},
\tag{17}
\]

which itself approaches \(1/2\). Replication improves the finite-\(h\)
exponent, while the strength of unconditional arbitrarily short-family
inputs already contains the endpoint.

If instead a future theorem produces \((M)_{h,a}\) only **conditional
on** a prior bound \(P_\nu(\theta)\), that conditional production is
still the substantive step. At a fixed stage its already-established
moment can be reused as in Section 2; to approach \(1/2\), a new theorem
must supply smaller floors at subsequent stages. No zeta-only strip
provides the needed Hecke-family estimate automatically.

For completeness, fix a putative nontrivial zero \(\rho\), with
\(\Re\rho>\beta\), and a permitted profile satisfying
\(\widehat W(\rho)\ne0\). The Mellin transform

\[
\int_0^\infty A_1(D)D^{-s}\,\frac{dD}{D}
=\frac{\widehat W(s)}{L_K^S(s,\nu)}
\tag{18}
\]

holds first for \(\Re s>1\). A \(P_{\nu,W}(\beta)\) bound makes the
left side holomorphic for \(\Re s>\beta\); the small-\(D\) end vanishes.
Multiply by \(L_K^S\) and continue the identity meromorphically, allowing
the principal character's possible pole at \(s=1\). Evaluation at the
nontrivial zero \(\rho\ne1\) contradicts
\(\widehat W(\rho)\ne0\). The finitely omitted Euler factors are
nonzero for \(\Re s>0\). For a class of all smooth annular profiles,
one may take \(W(y)=y^{-\rho}\phi(y)\), with nonnegative nonzero
\(\phi\in C_c^\infty((1,2))\).

Each zero is fixed before its profile, loss, and sufficiently large
threshold are chosen. No uniformity in zero height or conductor is
required for this fixed-character contradiction. An all-character
conclusion requires the assumptions for each character. For
\(\nu=1\), zero-freeness of \(\zeta_K=\zeta L(\cdot,\chi_{-3})\)
to the right of \(1/2\) implies RH for zeta. A strip for zeta alone does
not give a starting strip for that product or moments for (1).

## 5. Where the source's long-family proof stops

The October 5 paper assumes \(H=D^{1+\vartheta}\) in Proposition 3.1.
Its Poisson reduction, equation (4.11), has dual row length \(R\) and
column product \(\Sigma=XF\) with

\[
R\ll\frac{D^2}{HB^2},\qquad \Sigma=\frac DB,
\qquad \frac R\Sigma\ll\frac D{HB}.
\tag{19}
\]

Here \(B\asymp N(b)\), where the proof sets \(b=g/e\),
\(g=(n_1,n_2)\), \(e\mid g\); it is not an independently disposable
selector. The induction of Proposition 5.1 needs
\(R/\Sigma\le D^{-\kappa}\), \(\kappa>0\). Its step uses

\[
R' < R(R/\Sigma)^2\le D^{-2\kappa}R.
\tag{20}
\]

Thus the long-family margin is precisely the shrinking dual-row
parameter. Merely substituting \(H=D^h\), \(h<1\), into the displayed
range formula leaves \(R/\Sigma\ll D^{1-h}/B\). In the small block
\(B=1\), neither the required ratio nor the contraction is supplied.
If a short-family extension of the Poisson reduction were otherwise
justified, only blocks

\[
B\ge D^{1-h+\kappa'}
\tag{21}
\]

with a fixed positive buffer \(\kappa'\) would automatically recover
this part of the old range, after absorbing its fixed constants and
checking the remaining length conditions. The block \(b=1\) actually
occurs and cannot be removed by declaring most rows nonprincipal.
No short-family extension of Proposition 4.5 is asserted here.

The September 30 version has the parallel explicit restriction:
the unmarked use of Lemma 17.1 requires \(r<m\) with a fixed strict
margin, which becomes \(H\ge D^{1+c}\) in (17.87). Its scale supremum
(17.89) is proved after imposing that restriction and does not remove it.

The next analytic task can therefore be stated more narrowly. Prove
the actual-coefficient short-family moment at **one** fixed useful
\(h<9/10\) and \(a<3/4-5h/6\), preserving the original smooth profiles
and zero extensions, by controlling the small-\(B\) dual blocks where
the existing induction does not shrink. For a route to RH, explain how
that control can continue to \(h\to0\) with \(a\to0\). A new estimate
for the long-dual-row regime, or an alternative signed transform that
avoids it with a paid error budget, is needed. Proving an all-scale
supremum or first obtaining another initial family strip is unnecessary
for the extraction proved here.

## Checks and limits

The exact exponent recurrence, the finite chains, the error map, and
the unrestricted-coefficient threshold are checked by
[check_short_family_refinement.py](../numerics/check_short_family_refinement.py),
with the small record
[short_family_refinement_check.json](../numerics/short_family_refinement_check.json).
These are algebraic checks, not asymptotic arithmetic evidence.

This note proves conditional extraction and an equivalence of obligations.
It does not establish the new short-family estimate, extend a source
theorem outside its stated range, prove reciprocal growth from a bare
zero strip, or validate the imported analytic machinery independently.
