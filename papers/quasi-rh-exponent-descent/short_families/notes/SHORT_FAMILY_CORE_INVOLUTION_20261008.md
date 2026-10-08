# Short-family core: source corrections, exact involution, and a prime-column obstruction

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is a same-model scoped audit and derivation, not independent specialist
validation.

## Source and two corrections applied in this continuation

The primary [October 5 TeX source](https://raw.githubusercontent.com/openai/math/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
lines 738--800 and 991--1100, was checked against rendered PDF pages 13--17.
The PDF SHA-256 is
`f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18`.
Plain extraction of this PDF loses mathematical overbars and is inadequate
for checking these identities.

The [small-cofactor note](SHORT_FAMILY_SMALL_COFACTOR_20261008.md)
had two missing conjugations, now corrected:

1. Its equation (5) must use
   \[
   a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n),
   \qquad \alpha(n)=n/|n|.
   \]
   Source Lemma 4.1 equation (4.4) is
   \[
   \overline{\alpha(n)}\gamma_2(n)\gamma_1(n)=\mu_K(n)G(n).
   \]
   Replacing the conjugate by \(\alpha\) introduces a nonconstant factor
   \(\alpha(n)^2\). It is not a harmless scalar or fixed ray-class change.

2. The profile definition must be
   \[
   W_0(t)=t^{-1/2}\overline{W(t)}.
   \]
   With that definition, equation (7)'s existing factors
   \(W_0(N(bfm_1)/D)\overline{W_0(N(bfm_2)/D)}\) have the source's
   correct orientation. An equivalent repair keeps the old definition and
   conjugates the first physical factor instead of the second in (7).
   This distinction disappears for real profiles, but the note admits
   complex smooth profiles.

No conjugation of the exterior coefficients is required under this repair.
Their precise definition is the finite ray-group expansion
\[
\overline{\nu(t)}G(t^{-1})=\sum_\xi c_\xi\xi(t).
\tag{C1}
\]
Source (4.15), for coprime squarefree columns, reads
\[
\mu_1\mu_2\overline{\nu_1}\nu_2
\gamma(\overline{\chi_1}\chi_2)
=\sum_\xi c_\xi a_\xi(m_1)\overline{a_\xi(m_2)}.
\tag{C2}
\]
The [earlier review](../../reviews/SHORT_FAMILY_SMALL_COFACTOR_REVIEW_20261008.md)
has been amended to record its missed conjugations. The modulus estimates, conductor
calculations, and diagonal/cofactor bounds survive them: conjugation
preserves profile seminorms and every actual coefficient still has modulus
one. The exact transformed equality must use the corrected definitions.

## Exact second-Poisson involution in the coprime core

Take \(b=f=1\), squarefree \(m_1\ne m_2\), and
\((m_1,m_2)=1\), with all columns prime to \(S\). Put
\[
q=N(m_1m_2),\quad
\psi=\chi_{m_1}\overline{\chi_{m_2}},\quad
t=m_1m_2^{-1}
\]
where the last quotient is in the fixed ray group. The ratio \(\psi\) is
primitive and nonprincipal of conductor \(m_1m_2\). Its original zero
extension already retains all zeros at the column primes; there is no
shared-prime mask because the columns are coprime.

The complete kernel is
\[
K(m_1,m_2)=\sum_{k\ne0}\psi(k)\widehat\Phi(HNk/q).
\]
Lemma 4.2 at row scale \(q/H\), with excluded ideal one, gives
\[
K(m_1,m_2)=\frac{\sqrt q}{H}\gamma(\psi)
\sum_{u\ne0}\overline{\psi(u)}\Phi(Nu/H).
\tag{I1}
\]
Here Fourier inversion returns \(\Phi\): the source's Fourier transform
squares to reflection, and the weight is radial. The primitive zero
frequency vanishes. No row truncation, constant, or missing mask is hidden
in (I1).

For completeness, the actual coefficient cancellation can be checked
without concealing it inside (C2). The Chinese remainder theorem and
source reciprocity give
\[
\gamma(\psi)=\mathcal R(m_1,m_2)
\gamma_1(m_1)\gamma_{-1}(m_2).
\]
Use (4.4),
\(\gamma_{-1}(n)=\chi_n(-1)\overline{\gamma_1(n)}\), and source
(4.7), with \(a=m_2,b=m_1\). The result is
\[
a_\xi(m_1)\overline{a_\xi(m_2)}\gamma(\psi)
=\mu_1\mu_2\xi(t)G(t).
\tag{I2}
\]
The corrected physical profile supplies the normalization
\[
\frac{H}{D^2}\frac{\sqrt q}{H}
W_0(Nm_1/D)\overline{W_0(Nm_2/D)}
=\frac1D\overline{W(Nm_1/D)}W(Nm_2/D).
\tag{I3}
\]

Let \(S_{\xi,\mathrm{core}}\) mean equation (7) restricted to this core.
Equations (I1)--(I3) identify each individual \(\xi\) core with a finite
ray-group combination of coprime Moebius pair sums: expand the fixed
function \(\xi(t)G(t)\) in ray characters. In particular, after the
original exterior coefficients are restored,
\[
\begin{split}
\sum_\xi c_\xi S_{\xi,\mathrm{core}}
=\frac1D\sum_{\substack{m_1\ne m_2\ \,\mathrm{squarefree}\\
(m_1,m_2)=1}}^*
&\mu_1\mu_2\overline{\nu_1}\nu_2
\overline{W(Nm_1/D)}W(Nm_2/D)\\
&\times\sum_{u\ne0}
\overline{\chi_{m_1}(u)}\chi_{m_2}(u)\Phi(Nu/H).
\end{split}
\tag{I4}
\]
To see the last phase precisely, (C1) and (I2) give
\(G(t)G(t^{-1})=\psi(-1)\). This factor disappears from the complete
radial sum by replacing \(u\) with \(-u\); if the ratio is odd, that
sum is zero already. Thus (I4) is exactly the original coprime,
off-diagonal Moebius pair form. A second Poisson transform alone does not
shorten this core or create new cancellation.

There is an exact but finite-class simplification. Multiplication of the
row by any unit preserves its norm. Therefore the kernel vanishes unless
the restrictions of \(\chi_{m_1}\) and \(\chi_{m_2}\) to the six units
agree. This leaves at most six unit-character classes. It supplies no
power saving in \(D\).

## A genuine actual-coefficient obstruction from prime columns

Specialize to \(\nu=1\), take fixed nonnegative nonzero smooth annular
\(W\), and retain only distinct prime-ideal columns \(p_1,p_2\notin S\)
in this same \(b=f=(m_1,m_2)=1\) core. Define
\[
P_u(D)=\sum_{p\notin S}\chi_p(u)W(Np/D).
\]
Since \(\mu_K(p)=-1\), the signs cancel in every prime pair. Equation
(I4) is now exactly
\[
\mathcal C_{\mathrm{prime}}=
\frac1D\sum_u\Phi(Nu/H)|P_u(D)|^2
-\frac1D\sum_p W(Np/D)^2
\sum_u\Phi(Nu/H)\mathbf1_{(u,p)=1}.
\tag{P1}
\]
The first term is nonnegative. In fact, use all sixth-power rows
\(u=r^6\) with \(0<Nr\le H^{1/6}\), not just the unit row. There
are \(\asymp H^{1/6}\) distinct such rows: the map \(r\mapsto r^6\)
has exactly six preimages on its image, and lattice counting counts
\(r\) in the norm ball. The annular prime columns have \(Np\asymp D\).
For fixed \(h<1\), no such prime can divide these \(r\), once \(D\)
is large. Thus every original mask is one and
\(\chi_p(r^6)=1\). Also \(\Phi(N(r^6)/H)\ge1\).

By the prime ideal theorem, \(P_{r^6}(D)=\sum_p W(Np/D)\asymp
D/\log D\). The first term in (P1) is therefore
\(\gg D H^{1/6}/(\log D)^2\). Lattice counting and the prime ideal
upper count bound the second term by \(O(H/\log D)\).
Since \(D H^{-5/6}/\log D\to\infty\), for every fixed \(0<h<1\)
we obtain the stronger lower bound
\[
\mathcal C_{\mathrm{prime}}\gg
\frac{D H^{1/6}}{(\log D)^2}
=\frac{D^{1+h/6}}{(\log D)^2},
\qquad H=D^h,
\tag{P2}
\]
for all sufficiently large \(D\).

This uses the actual source coefficients and the actual exterior
combination, with a prime-column selector. A bound
\(O(D^{h+a+\varepsilon})\) for every selected piece of the core would
require
\[
a+5h/6\ge1.
\tag{P3}
\]
In particular, at least one member of the finite \(\xi\)
combination cannot obey such an absolute bound on this prime-selected
piece. A method that separately estimates every prime/composite sector
by the desired budget cannot work. The full signed form may cancel the
prime contribution against other column or cofactor sectors; (P2) does
not disprove the desired unrestricted arithmetic estimate.

Every parameter pair that beats \(7/8\) satisfies
\(a+5h/6<3/4\), so the prime-selected core exceeds its proposed budget
by strictly more than a quarter power of \(D\), up to logarithms.
All deletion masks are retained in this strengthening.

The [uniform overlap bound](SHORT_FAMILY_HIGH_OVERLAP_20261008.md)
controls a larger common-factor sector but leaves this coprime core.

## Next theorem and scope

The full signed remainder bound remains the decisive sufficient theorem.
The coprime core is a useful first analytic target only when its actual
Moebius cancellation across column types is preserved. The prime-selected
subcase is an obstruction test, not a subproblem that should satisfy the
same target. At \(h=8/9\), the full bound needs \(a<1/108\).
The all-scale gcd estimate removes another sector but gives no mechanism
for the coprime core. The source's deep dual mean-square and theta proofs
were not replayed; these deductions use its stated finite identities and
Poisson formula, plus ordinary lattice/prime ideal counting.
