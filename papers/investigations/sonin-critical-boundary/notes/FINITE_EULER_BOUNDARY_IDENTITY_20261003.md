# Finite Euler boundary identity and a fixed-place sign obstruction

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the exact serving variant and configured reasoning
effort are not exposed and are not inferred. Three parallel same-model
checks examined transport, boundary algebra, and the earlier comparison.
This is an internal derivation, not independent specialist refereeing.
Repository baseline: `2e84e2cb516067b949eb976aad9b1b2db4d38756`.

This completes the first identity audit requested in the
[continuation](FINITE_EULER_WEIL_COMPARISON_CONTINUATION_20261003.md).
For every fixed finite prime set and every positive exponent, including
one half, the proposed identity holds. The proof reuses the manuscript's
bounded-transport and smoothed boundary arguments. A new observation in
this continuation is that the strong correction sign fails on expanding
prepared sources for **every fixed finite prime set**. Neither result
settles the support-adapted comparison. The subsequent manuscript integration
is recorded in the [draft history](../DRAFT_HISTORY.md).
The companion [adversarial audit](../reviews/FINITE_EULER_BOUNDARY_AUDIT_20261003.md)
records the checks and remaining claim.

## 1. Statement, conventions, and quantifiers

Work on \(\mathcal H=L^2(\mathbb R,dx)\), with
\(\widehat f(t)=\int f(x)e^{-itx}dx\), inverse measure \(dt/(2\pi)\),
\(P=1_{(0,\infty)}\), \(\chi=1-P\), \(\mathcal Jf(x)=f(-x)\),
and \(D=-i\partial_x\). Inner products are antilinear in their first
variable. The reflection is linear. For a finite prime set \(S\) and
\(\sigma>0\), put
\[
v=v_\infty\frac{\zeta_S(\sigma+it)}{\zeta_S(\sigma-it)},\qquad
v_\infty(t)=\pi^{-it}
\frac{\Gamma(1/4+it/2)}{\Gamma(1/4-it/2)},\qquad
\mathcal F=\mathcal Jv(D),\quad V=v(D).
\]
Then \(\mathcal F\) is a real, selfadjoint unitary involution. Define
\[
T=\chi\mathcal FP,\quad C=\chi\mathcal F\chi,\quad
L=P V^*\chi V P=P-T^*T,\quad
\Pi=\operatorname{proj}_{\ker(T|_{P\mathcal H})}.
\]
All cutoff operators are extended by zero outside their indicated spaces.
Let \(F\in C_c^\infty(\mathbb R;\mathbb C)\), let \(C_F\) be convolution
by \(F\), and set
\[
\kappa_F(u)=\int\overline{F(x)}F(x+u)dx,\quad
a=|\widehat F|^2,\quad a_e(t)=\tfrac12(a(t)+a(-t)),\quad
X=Pa_e(D)\chi.
\]
For every such \(S,\sigma,F\),
\[
\boxed{B_{S,\sigma}[F]:=\|C_F\Pi\|_{\mathrm{HS}}^2
=\Gamma[F]-W_{S,\sigma}[F]+K_{S,\sigma}[F],}
\tag{1}
\]
where all terms are finite and
\[
\Gamma[F]=\int\gamma_\infty(t)a(t)\frac{dt}{2\pi},\quad
\gamma_\infty(t)=\Re\psi(1/4+it/2)-\log\pi,
\]
\[
W_{S,\sigma}[F]=\sum_{p\in S}\sum_{m\ge1}
(\log p)p^{-m\sigma}
\{\kappa_F(m\log p)+\kappa_F(-m\log p)\},
\]
\[
\boxed{K_{S,\sigma}[F]
=2\Re\operatorname{Tr}_{\chi\mathcal H}
\bigl(C(I_\chi-C^2)^{-1}TX\bigr).}
\tag{2}
\]
In particular (2) defines the correction independently of arithmetic
subtraction. Preparation is unnecessary for (1); it is needed to identify
its bulk with the pole-neutral arithmetic target in Section 5.
No estimate here is uniform as \(S\) grows or \(\sigma\) approaches zero.

## 2. Transport, gap, and the actual metric

Write \(U_af(x)=f(x-a)\) and distinguish the transport from \(D\):
\[
\mathscr D=\prod_{p\in S}(I-p^{-\sigma}U_{\log p}),\quad
d(t)=\prod_{p\in S}(1-p^{-\sigma-it})=\zeta_S(\sigma+it)^{-1}.
\]
Both \(\mathscr D\) and its inverse preserve \(P\mathcal H\). Indeed
\[
\mathscr D^{-1}=\sum_{n\in\mathbb N_S}n^{-\sigma}U_{\log n}
\]
converges absolutely in operator norm; \(\mathbb N_S\) denotes the positive
integers whose prime divisors belong to \(S\). With
\(\ell=\prod_{p\in S}(1-p^{-\sigma})\) and
\(u=\prod_{p\in S}(1+p^{-\sigma})\),
\[
\ell\|z\|\le\|\mathscr Dz\|\le u\|z\|.
\tag{3}
\]
The orientation check is explicit:
\[
\mathscr D\mathcal F_\infty\mathscr D^{-1}
=\mathcal J\left(v_\infty(t)\frac{d(-t)}{d(t)}\right)(D)
=\mathcal F.
\tag{4}
\]
Here \(d(-t)=\overline{d(t)}\); the ratio has modulus one, even though
\(\mathscr D\) itself is not unitary.

Let \(\mathscr D_+=\mathscr D|_{P\mathcal H}\) and
\(\mathscr D_-=\chi\mathscr D\chi|_{\chi\mathcal H}\).
Triangularity gives \(\mathscr D_-^{-1}=\chi\mathscr D^{-1}\chi\) and
\[
T=\mathscr D_-T_\infty\mathscr D_+^{-1},\qquad
TT^*=I_\chi-C^2\ge g I_\chi,\qquad
g=(\ell/u)^2(1-\|C_\infty\|^2)>0.
\tag{5}
\]
For example
\(\|T^*y\|\ge u^{-1}\|T_\infty^*\mathscr D_-^*y\|
\ge (\ell/u)\sqrt{1-\|C_\infty\|^2}\|y\|\).
The strict archimedean gap follows from the compact cosine kernel on
\((0,1)^2\) and analytic continuation excluding a norm-one extremal vector.
Thus \(T\) is onto, \(c:=\|C\|<1\), and
\[
\Pi=P-T^*(I_\chi-C^2)^{-1}T.
\tag{6}
\]
Its range is \(\mathscr D\mathcal K_\infty\), where
\(\mathcal K_\infty=\operatorname{Ran}\Pi_\infty\). Consequently
\[
M=\left.\Pi_\infty\mathscr D^*\mathscr D\Pi_\infty
\right|_{\mathcal K_\infty},\quad \ell^2I\le M\le u^2I,
\qquad
\boxed{\Pi=\mathscr D\Pi_\infty M^{-1}\Pi_\infty\mathscr D^*.}
\tag{7}
\]
The inverse acts on \(\mathcal K_\infty\). Formula (7) is the ordinary
orthogonal projection, not a transported unweighted quadratic form.

For completeness, \(C\) is compact: expand (4) into the absolutely
norm-convergent sum of
\(\mu(d)d^{-\sigma}n^{-\sigma}\chi U_{\log(d/n)}\mathcal F_\infty\chi\),
where \(d\mid\prod_{p\in S}p\) and \(n\in\mathbb N_S\).
In physical positive-axis coordinates each fixed summand has smooth kernel
\(2e^{-a/2}\cos(2\pi e^{-a}xy)\) on \((0,1)^2\), with
\(a=\log(d/n)\), hence is compact. Compactness is not needed to deduce
the transported gap. Nor does it imply \(C\) is Hilbert--Schmidt: the
one-prime critical example in the
[place-addition note, Section 9](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md)
is not. No trace of unsmoothed \(C^2\) is taken below.

## 3. Trace ideals and the arithmetic bulk

For every Schwartz multiplier \(q\), both \(q\) and \(qv\) are Schwartz.
The finite Euler factors and all their derivatives are bounded for fixed
\(S,\sigma\); the gamma phase derivatives have at most polynomial growth.
The manuscript's cutoff lemma follows by extending the reflected Hankel
kernel \(\check q(x+y)\), \(x,y>0\), to a Schwartz kernel on the plane.
It gives \([P,q(D)]\in\mathfrak S_1\), continuously in Schwartz seminorms.
For \(\mathcal Q=V^*PV-P\), the identity
\[
q(D)\mathcal Q
=V^*\bigl([P,(qv)(D)]-[P,q(D)]V\bigr)\in\mathfrak S_1
\tag{8}
\]
therefore applies. Moving \(q(D)\) past a cutoff adds only a trace-class
commutator. In the decomposition \(P\mathcal H\oplus\chi\mathcal H\),
\[
\mathcal Q=\begin{pmatrix}-L&T^*C\\CT&C^2\end{pmatrix}.
\tag{9}
\]
Thus \(q(D)\) times each extended block is trace class. In particular
the source sandwiches of \(L,C^2\) are trace class, and
\(0\le\Pi\le L\) proves \(B_{S,\sigma}[F]<\infty\) **before**
any arithmetic trace identity is used. Alternatively, with
\(J_S=\mathscr D\Pi_\infty M^{-1/2}\),
\(C_FJ_S=\mathscr D(C_F|_{\mathcal K_\infty})M^{-1/2}\)
propagates archimedean Hilbert--Schmidt smoothing using bounded factors.

If \(v'=i\phi'v\), the frequency kernel of \(\mathcal Q\) is
\(-i(\overline{v(t)}v(s)-1)/(t-s)\); its diagonal is \(-\phi'(t)\).
For compact smooth frequency multipliers the sandwich has a smooth compact
kernel, so its trace is its diagonal integral. Approximate any Schwartz
multiplier in Schwartz seminorms and apply (8) to pass in trace norm.
For \(b=\widehat F\), this yields
\[
-\operatorname{Tr}(b(D)\mathcal Q b(D)^*)
=\int a(t)\phi'(t)\frac{dt}{2\pi}.
\tag{10}
\]
The differentiated finite Euler series converges absolutely and uniformly:
\[
\phi'(t)=\gamma_\infty(t)
-\sum_{p\in S,m\ge1}(\log p)p^{-m\sigma}
\bigl(e^{itm\log p}+e^{-itm\log p}\bigr).
\tag{11}
\]
Since \(\check a=\kappa_F\), (10) equals \(\Gamma[F]-W_{S,\sigma}[F]\).
This uses only the finite Euler product, with no global zeta continuation
or sum over zeros. One must never split (10) into traces of
\(a(D)V^*PV\) and \(a(D)P\): neither separate trace is justified.

## 4. The independently represented correction

Set \(s=(I_\chi-C^2)^{1/2}\) and
\(H=T^*C^2s^{-2}T=L-\Pi\ge0\). Taking the already smoothed block traces
in (9) gives (1) initially with
\[
K=\operatorname{Tr}(C_FC^2C_F^*)
-\operatorname{Tr}(C_FHC_F^*)
+2\Re\operatorname{Tr}_{\chi\mathcal H}(CTPa(D)\chi).
\tag{12}
\]
All three terms exist: \(H\le L\), and the crossing block is trace class.

Real conjugation fixes \(\Pi\) and sends \(D\) to \(-D\), so its positive
frequency measure is even. The bulk derivative is also even. Thus the
right side of (12) may be replaced by its average under \(t\mapsto-t\),
using \(a_e\). This is not a parity condition on \(F\). In particular
\(\check a_e=\Re\kappa_F\), and both additive parity sectors and all complex
sources remain admitted. The even multiplier \(a_e(D)\) commutes with
\(\mathcal F\).

The isometry \(U=T^*s^{-1}\) has range \((P-\Pi)\mathcal H\), with
\(H=UC^2U^*\). The space
\(\mathcal M=U\chi\mathcal H\oplus\chi\mathcal H\)
reduces \(\mathcal F\) and \(\mathcal Q\): the Sonin space reduces
\(\mathcal F\), and \(\mathcal Q\Pi=-\Pi\). In these coordinates,
\[
\mathcal F|_{\mathcal M}=\begin{pmatrix}-C&s\\s&C\end{pmatrix},\qquad
(\Pi+\mathcal Q)|_{\mathcal M}
=\begin{pmatrix}-C^2&sC\\Cs&C^2\end{pmatrix}.
\]
Write the compression of \(a_e(D)\) as
\(\begin{pmatrix}A_{++}&A_{+-}\\A_{+-}^*&A_{--}\end{pmatrix}\).
It commutes with the displayed involution even if \(a_e(D)\) does not
preserve \(\mathcal M\). In particular
\[
sA_{--}-A_{++}s=CA_{+-}+A_{+-}C,\qquad
A_{+-}=s^{-1}TX\in\mathfrak S_1.
\tag{13}
\]
Compressing \(a_e(D)\mathcal Q\in\mathfrak S_1\) shows that
\(A_{++}C^2\) and \(A_{--}C^2\) are trace class; the other terms in its
diagonal blocks already contain \(A_{+-}\). The positive return trace
is \(\operatorname{Tr}(CA_{++}C)=\operatorname{Tr}(A_{++}C^2)\).
For example, use the spectral cutoffs \(1_{\{|C|\ge1/n\}}\), cycle with
the bounded inverse of \(C\) on each cutoff, and pass using positive
monotone convergence and trace-norm convergence of the other product.

Multiply (13) on the right by \(C^2s^{-1}\), then take traces. Each term
is a bounded factor times one of the trace-class products just established.
Cyclicity gives
\[
\operatorname{Tr}(C^2A_{--}-C^2A_{++})
=2\operatorname{Tr}(C^3s^{-1}A_{+-}).
\]
Combining this with the two crossing traces in (12) and
\(C^2+s^2=I_\chi\) gives
\(K=2\Re\operatorname{Tr}(Cs^{-1}A_{+-})\), which is (2).

If \(\operatorname{diam}(\operatorname{supp}F)\le L_0\), the kernel of
\(X\) is supported in the finite crossing triangle
\[
-L_0<y<0<x<L_0,\qquad x-y<L_0.
\tag{14}
\]
Neither half-line is replaced by an infinite separately traced bulk.
The return series also survives:
\[
K=2\Re\sum_{n\ge0}\operatorname{Tr}(C^{2n+1}TX),\quad
\left|K-2\Re\sum_{n=0}^{N}\operatorname{Tr}(C^{2n+1}TX)\right|
\le\frac{2c^{2N+3}}{\sqrt{1-c^2}}\|X\|_1.
\tag{15}
\]
Indeed the omitted bounded factor is \(C^{2N+3}s^{-2}T\), whose product
with its adjoint is \(C^{4N+6}s^{-2}\). This is a fixed-place bound,
not a useful uniform estimate for growing sets of primes.

## 5. Complete residual and the support-adapted comparison

At \(\sigma=1/2\), take \(F=(-\partial_x^2+1/4)h\),
\(h\in C_c^\infty(\mathbb R;\mathbb C)\). Integration by parts gives
\(\widehat F(\pm i/2)=0\); the canonical audit proves this preparation
is onto the pole-neutral class without enlarging support. If
\(S\supseteq S_{L_0}=\{p:p\le e^{L_0}\}\), every active prime is present,
and all active powers of those primes occur in (11). The correlation is
zero at the endpoints of its support. Hence
\[
W_{S,1/2}[F]=W_{1/2}[F],\qquad
\boxed{Q[F]=B_{S,1/2}[F]-K_{S,1/2}[F].}
\tag{16}
\]
No identification of the finite symbol with the constant global endpoint
symbol is made; a finite Euler product has no such functional equation.

To reconcile with the
[canonical audit, Sections 4--6](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md),
put \(G_S=\mathscr D^*\mathscr D\), \(A_F=C_F^*C_F\), and
\[
\Delta_S[F]=\operatorname{Tr}_{\mathcal K_\infty}
\bigl(M^{-1}\Pi_\infty G_S(I-\Pi_\infty)A_F\Pi_\infty\bigr).
\]
The compressed factor is trace class by the source-smoothed factorization
in that audit. Its established calibration is
\(B_\infty=\Gamma+E_\infty\) and \(B_S=B_\infty+\Delta_S\).
Here subscript \(\infty\) means archimedean, equivalently \(S=\varnothing\),
not an infinite-place limit. Comparing with (1) gives
\[
\boxed{K_{S,1/2}=E_\infty+\Delta_S+W_{S,1/2}.}
\tag{17}
\]
The old **complete** residual, on prepared sources, is
\(\mathcal R_{S,L_0}=-E_\infty-\Delta_S-W_{1/2}\).
It equals \(-K_{S,1/2}\) only after active primes are captured. Before
capture it equals \(-K_{S,1/2}-(W_{1/2}-W_{S,1/2})\).
Thus for a new prime \(p\), the increment of \(K\) is
\(\Delta_p B+W_{\{p\},1/2}\), whereas the increment of the complete
residual is \(-\Delta_p B\). An inactive prime can change \(B\) and
\(K\) equally. Equation (17) is consistency with the old comparison,
not a new positivity theorem.

## 6. Analytic obstruction to a fixed-place all-support correction sign

Choose any nonzero \(\eta\in C_c^\infty(\mathbb R)\), and define
\[
h_R(x)=R^{-1/2}\eta(x/R),\qquad
F_R=(-\partial_x^2+1/4)h_R,\qquad R\longrightarrow\infty.
\]
These sources are exactly pole neutral for every \(R\); preparation
does not impose zero mean. Rescaling Fourier variables yields
\[
\Gamma[F_R]=\int\gamma_\infty(u/R)
\bigl(u^2/R^2+1/4\bigr)^2|\widehat\eta(u)|^2\frac{du}{2\pi}
\longrightarrow\frac{\|\eta\|_2^2}{16}\gamma_\infty(0).
\tag{18}
\]
Dominated convergence follows from the logarithmic growth of
\(\gamma_\infty\) and Schwartz decay of \(\widehat\eta\).
For every fixed shift \(a\),
\(\kappa_{F_R}(a)\to\|\eta\|_2^2/16\), by continuity of translations
of \(\eta\) and the \(O(R^{-2})\) derivative correction. The uniform bound
\(|\kappa_{F_R}(a)|\le\|F_R\|_2^2\) permits summation against the
absolutely summable prime-power coefficients for **fixed finite** \(S\).
Therefore
\[
\Gamma[F_R]-W_{S,\sigma}[F_R]
\longrightarrow\frac{\|\eta\|_2^2}{16}
\left(\gamma_\infty(0)
-2\sum_{p\in S}(\log p)\frac{p^{-\sigma}}{1-p^{-\sigma}}\right)<0.
\tag{19}
\]
The sign uses
\(\gamma_\infty(0)=-\gamma_{\rm E}-\pi/2-3\log2-\log\pi<0\),
from the digamma reflection and duplication identities.
Since \(B_{S,\sigma}\ge0\), (1) implies
\[
\liminf_{R\to\infty}K_{S,\sigma}[F_R]
\ge-\frac{\|\eta\|_2^2}{16}\phi'_{S,\sigma}(0)>0.
\tag{20}
\]
Thus \(K_{S,\sigma}\le0\) is false on the all-support prepared class
for every fixed finite \(S\), including the empty set. This is an analytic
counterexample family, not a numerical sign experiment. It does not address
\(S=S_{L_0}\) as the support grows: that set changes with \(R\), and the
fixed-\(S\) dominated-convergence argument cannot be used on that diagonal.
In particular it neither refutes (16)'s weaker comparison nor implies a
negative complete Weil form.

## 7. One next inequality: domination by the mean functional

The mean-only proposal and its mixed-term obligation already appear in
the [finite Mellin-defect note, Sections 3--4](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_FINITE_MELLIN_DEFECT_20260929.md).
The formulation here connects that existing target to the newly audited
finite Euler boundary representation; it is not a new comparison conjecture.

The identity alone does not sign the mixed trace. A concrete next candidate
is the following **unproved structured estimate**, formulated entirely with
the actual finite-place boundary operators. Put
\(I_{L_0}=(-L_0/2,L_0/2)\),
\(\mathcal A=-\partial_x^2+1/4\), and use the minimal safe place set
\(S_{L_0}=\{p:p\le e^{L_0}\}\). Investigate whether, for each \(L_0>0\),
there is a finite \(c_{L_0}\ge0\) such that
\[
\boxed{
2\Re\operatorname{Tr}_{\chi\mathcal H}
\left(C_{S_{L_0}}(I-C_{S_{L_0}}^2)^{-1}
T_{S_{L_0}}X_{\mathcal A h,e}\right)
\le \frac{c_{L_0}}{16}\left|\int h(x)dx\right|^2,
\quad h\in C_c^\infty(I_{L_0};\mathbb C).
}
\tag{21}
\]
All operators in (21) have exponent \(1/2\), and
\[
X_{\mathcal A h,e}=P\left[
(t^2+1/4)^2\frac{|\widehat h(t)|^2+|\widehat h(-t)|^2}{2}
\right](D)\chi.
\]
Thus (21) is domination of a specified Hermitian quadratic form by the
rank-one mean form, not the assertion \(K\le B\) under another name.
It claims substantially more structure: the correction is nonpositive
on the fixed codimension-one mean-zero subspace, with all remaining
positive contributions controlled by that one functional. Interpret the
comparison on the displayed smooth core; no bounded operator realization
of the prepared form on ordinary \(L^2(I_{L_0})\) is assumed.

The motivation is the archimedean bound
\(K_\infty[F]\le c|\widehat F(0)|^2\) for source length \(\log2\)
from Connes--Consani, Theorem 6.11. Their Theorem 4.6 gives the plus-sign
calibration; the short-support theorem does not give a sign without its
mean term. [2021 author version](https://alainconnes.org/wp-content/uploads/Selecta.pdf).
Under \(F=\mathcal A h\), \(\widehat F(0)=\tfrac14\int h\), explaining
the factor \(1/16\) in (21). This motivates the shape of the candidate,
not its extension to additional primes or larger supports. The fixed-place
obstruction above persists if \(\int\eta=0\); consequently the changing
place set in (21) is essential even on the mean-zero sector.

If (21) held for every \(L_0\), then for all prepared sources with
\(\widehat F(0)=0\), (16) would give \(Q[F]\ge B_{S_{L_0}}[F]\ge0\).
The extra condition is sufficient for the eventual Weil criterion:
Appendix C, Proposition C.1 allows the fixed prescribed Mellin zeros
\(\{0,1,1/2\}\). The additional point is not a zeta zero; for example
the alternating Dirichlet series is positive at \(1/2\), while its
factor \(1-2^{1-s}\) is negative there.
[Same author version, Appendix C](https://alainconnes.org/wp-content/uploads/Selecta.pdf).
Thus the criterion would give RH and consequently positivity on the full
pole-neutral class. This is the **conditional criterion implication**;
(21) itself gives no direct nonzero-mean comparison with \(B\). No source
condition is added silently to (1) or (16), and no fixed support substitutes
for all \(L_0\).

The next bounded task is to prove or falsify (21) first at
\(L_0=1\), \(S_{L_0}=\{2\}\), using the actual transported cosine
kernel, its inverse compressed metric, and the prepared finite crossing
triangle (14). A positive correction on a **mean-zero** prepared source
would already falsify this candidate; positivity on a nonzero-mean source
would not. The first analytic check should identify the positive directions
of this prepared boundary form and whether the mean functional controls
them. Counting one positive direction, or proving a sign on the mean-zero
subspace alone, is insufficient: mixed terms with the mean direction must
also admit the finite bound in (21), including near-null directions of the
negative form. Both additive parity sectors and complex polarization must remain.
Any numerical falsification needs complete error and tail bounds; no such
calculation is claimed here. A proof at this one support would be a local
result only. Failure would reject (21), not the weaker comparison or RH.

The [quasi-inner framework](https://arxiv.org/abs/2008.10974) establishes
compact off-diagonal structure for finite local-factor products; compactness
alone supplies no correction sign. The
[semilocal transport, Sections 4.6--4.8](https://arxiv.org/html/2310.18423v2#S4.SS6)
supplies the multiplier orientation and bounded invertible transport while
retaining a place-dependent metric. Neither result proves (21).
Generic Gram positivity and place monotonicity are insufficient, as the
earlier finite-dimensional signed-increment control already shows. A proof
must use the actual cosine/Euler kernel and preparation to establish this
additional rank-one control. It has not been derived in this session.

The follow-up investigation supplies [residual error estimates](FINITE_EULER_BOUNDARY_RESIDUAL_CERTIFICATE_20261003.md),
[full spatial leakage Grams](FINITE_EULER_RANK_ONE_ANALYSIS_20261003.md), and
an [exploratory first-prime diagnostic](../numerics/finite_euler_first_prime_DIAGNOSTIC_20261003.md).
The diagnostic has no certified correction sign; the comparison remains open.

## 8. Reused, new in this continuation, and unresolved

- **Reused:** the archimedean gap and preparation theorem; the exact
  transported inverse metric; Schwartz cutoff smoothing; the manuscript's
  boundary block algebra; the canonical complete residual.
- **Established here as an adaptation:** their hypotheses hold for every
  finite Euler product at every \(\sigma>0\), giving (1)--(2) at the
  critical exponent with full complex sources. Equations (16)--(17)
  reconcile this with the old arithmetic comparison.
- **New observation in this continuation:** the explicit expanding-source
  obstruction (18)--(20) to every fixed-place all-support strong sign.
  This wording makes no claim of priority in the literature.
- **Unresolved:** the candidate rank-one bound (21), a signed comparison
  for the support-adapted family, or an independently identified positive
  arithmetic limit. The proved identity supplies none of these. No numerical
  enclosure, growing-place convergence, or proof of RH is claimed.

The calculations above contain no sums over zeta zeros. Only after a valid
all-support comparison is proved would the pole-neutral Weil criterion
give the eventual RH implication. The earlier
[moving-tail criteria](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_DIRECT_PLACE_TAIL_CRITERIA_20260929.md)
still require estimates along the growing family; the older
[direct-limit continuation](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_DIRECT_LIMIT_CONTINUATION_20260929.md)
is historical, including its then-open trace-finiteness question.
