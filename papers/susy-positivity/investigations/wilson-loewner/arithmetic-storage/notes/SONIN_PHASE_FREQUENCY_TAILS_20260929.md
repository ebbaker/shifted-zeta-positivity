# Uniform frequency tails for the Sonin phase family

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Parallel same-model derivations checked
the rational-factor energy and the cutoff factorization below. This is an
internal mathematical derivation, not independent specialist refereeing.

## Result

Use all conventions of the [phase trace note](SONIN_PHASE_BOUNDARY_TRACE_20260929.md).
The full source traces are finite near the critical boundary, and their
frequency tails are uniformly controlled. More precisely, there is a constant
independent of the integer j and of 1/2 < sigma <= 3/4 such that

\[
\nu_\sigma([j,j+1])\le C\log^2(2+|j|).
\tag{1}
\]

The same estimate holds for the positive, generally nonprojective majorant
\(L_\sigma=P-T_\sigma^*T_\sigma\) and for the small-cutoff square
\(C_\sigma^2\). Consequently, for every Schwartz
frequency multiplier f,

\[
\sup_{1/2<\sigma\le3/4}
 \operatorname{Tr}\bigl(f(D)L_\sigma f(D)^*\bigr)<\infty,
\tag{2}
\]

and the contribution from \(|t|>R\) tends to zero uniformly in sigma.
This proves the source-weighted tail obligation left open in Section 5 of
the phase trace note. It does not determine how much of the majorant's
critical mass survives in the exact kernel projection \(\Pi_\sigma\).
No zero-location hypothesis is used.

## 1 Local phase factorization with a uniform remainder

We use the classical local zero count

\[
\#\{\rho=\beta+i\gamma:|\gamma-j|\le5\}
 =O(\log(2+|j|)),
\tag{3}
\]

with multiplicity, and the local logarithmic-derivative expansion for zeta.
For primary expository derivations, see Propositions 16 and 19 of
[Tao's complex-analytic multiplicative number theory notes](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/).
The count for the full critical strip follows by reflection from a strip
bounded away from real part zero. The functional equation is recorded in
[DLMF Section 25.4](https://dlmf.nist.gov/25.4).

Fix j and put \(J_j=(j-3,j+3)\). List every nontrivial zero with
\(|\gamma-j|\le5\), repeating its entry according to multiplicity.
Let \(M_j\) be the length of this list. For each listed zero set
\(d_\rho=\sigma-\beta\) and

\[
B_{\rho,\sigma}(t)=
 \frac{t-\gamma-id_\rho}{t-\gamma+id_\rho}
\quad(d_\rho\ne0),\qquad
B_{\rho,\sigma}=1\quad(d_\rho=0).
\tag{4}
\]

These are unit-modulus rational factors. Negative d gives the conjugate
of the corresponding positive-width factor; no innerness of the product
or of the full phase is assumed. Define

\[
B_{j,\sigma}=\prod_\rho B_{\rho,\sigma},\qquad
w_{j,\sigma}=v_\sigma/B_{j,\sigma}\quad\hbox{on }J_j.
\tag{5}
\]

After removal of singularities, w is smooth on this interval, has modulus
one, and satisfies the uniform bound

\[
\sup_{J_j}|w_{j,\sigma}'|\le C\log(2+|j|).
\tag{6}
\]

Here is a direct justification that does not require a lower bound for the
distance of sigma from any zero. Apply the local logarithmic-derivative
formula in a fixed positive-real-part strip containing
\(1/2\le\Re s\le3/4\). It extracts every zero within a fixed small
distance of s and leaves an \(O(\log(2+|\Im s|))\) remainder, apart
from the zeta pole. Enlarge its extracted set to the fixed list above.
Every additional term is bounded in magnitude by a fixed constant because
it was outside the original small disk, and there are \(O(\log(2+|j|))\)
such terms. Thus, for \(s=\sigma+it\), \(t\in J_j\),

\[
\frac{\zeta'}{\zeta}(s)
 -\sum_{|\gamma-j|\le5}\frac{m_\rho}{s-\rho}
 =O(\log(2+|j|)).
\tag{7}
\]

The sum in (7) is over distinct zeros with their displayed multiplicities;
the product in (5) is over the repeated list.

The pole at s=1 is uniformly separated from this sigma interval and is
absorbed in the bound. The archimedean phase derivative is
\(O(\log(2+|t|))\). Taking twice the real part in (7), and using

\[
\frac{d}{dt}\arg B_{\rho,\sigma}(t)
 =\frac{2d_\rho}{d_\rho^2+(t-\gamma)^2},
\tag{8}
\]

proves (6). At d=0 the factor is constant and the real part of the
corresponding singular term is zero away from t=gamma; after subtraction,
the remainder extends smoothly there. This covers vertical lines containing
zeros as well as lines arbitrarily close to them. Bounded j causes no
problem: the same local formula applies, or one factors the finitely many
zeros in a fixed compact neighborhood.

## 2 The width-independent energy estimate

For a scalar function q define its homogeneous half-derivative energy by

\[
\mathcal E(q)=\iint_{\mathbb R^2}
 \frac{|q(t)-q(s)|^2}{(t-s)^2}\,dt\,ds.
\tag{9}
\]

An individual nonconstant factor in (4) has exactly

\[
\mathcal E(B_{\rho,\sigma})=4\pi^2.
\tag{10}
\]

Indeed its difference quotient squared is
\(4d_\rho^2/(((t-\gamma)^2+d_\rho^2)((s-\gamma)^2+d_\rho^2))\),
whose double integral is (10). The constant factor has energy zero.
Widths may therefore collapse, or change sign, without worsening this bound.

Choose a fixed real smooth cutoff b, equal to 1 on [0,1], with support in
(-2,2), and set \(b_j(t)=b(t-j)\). Extend w constantly outside J_j;
the resulting extension is continuous and Lipschitz. Put
\(f_{j,\sigma}=b_jw_{j,\sigma}\). Its compact support and (6) imply

\[
\mathcal E(f_{j,\sigma})
 \le C(\|f_{j,\sigma}\|_2^2+\|f_{j,\sigma}'\|_2^2)
 \le C\log^2(2+|j|).
\tag{11}
\]

For completeness, the first inequality follows by integrating the
translation bound
\(\|f(\cdot+h)-f\|_2\le |h|\|f'\|_2\) when \(|h|\le1\),
and \(\|f(\cdot+h)-f\|_2\le2\|f\|_2\) when \(|h|>1\),
against \(dh/h^2\).

Telescoping a product of M unit-modulus functions gives
\(|B(t)-B(s)|^2\le M\sum_{k=1}^M|B_k(t)-B_k(s)|^2\).
Combining this with

\[
|f(t)B(t)-f(s)B(s)|^2
 \le2|f(t)-f(s)|^2
 +2\|f\|_\infty^2|B(t)-B(s)|^2
\]

and (3), (10), (11) proves

\[
\boxed{\mathcal E(b_jv_\sigma)\le C\log^2(2+|j|).}
\tag{12}
\]

The equality \(b_jv_\sigma=f_{j,\sigma}B_{j,\sigma}\) is global,
since b_j is supported inside the interval where (5) holds. This is a
local factorization followed by an energy estimate; it is not an infinite
Blaschke factorization of the zeta phase.

## 3 The majorant's frequency measure

For the Fourier convention in the phase trace note,

\[
\|[P,q(D)]\|_{\rm HS}^2
 =\frac{\mathcal E(q)}{4\pi^2}.
\tag{13}
\]

This follows directly from the Fourier kernel
\(-i(q(s)-q(t))/(t-s)\), with measure \(dt/(2\pi)\).
Either off-diagonal half-line block has squared Hilbert--Schmidt norm at
most (13). The phase majorant has the exact factorization

\[
L_\sigma=P V_\sigma^*\chi V_\sigma P=A_\sigma^*A_\sigma,
\qquad A_\sigma=\chi V_\sigma P.
\tag{14}
\]

Here A is local notation for this factor, not the Gram operator in the
regularization note. Because V and frequency multipliers commute,

\[
A_\sigma b_j(D)^*
 =\chi(v_\sigma\overline{b_j})(D)P
  +\chi V_\sigma[P,b_j(D)^*].
\tag{15}
\]

Equations (12), (13), and the fixed energy of b_j show that

\[
\operatorname{Tr}\bigl(b_j(D)L_\sigma b_j(D)^*\bigr)
 =\|A_\sigma b_j(D)^*\|_{\rm HS}^2
 \le C\log^2(2+|j|).
\tag{16}
\]

Let \(\lambda_\sigma\) be the positive frequency measure of L, defined
by \(\lambda_\sigma(E)=\|1_E(D)L_\sigma^{1/2}\|_{\rm HS}^2\),
initially with value infinity allowed. Since b_j=1 on [j,j+1], (16)
proves local finiteness and

\[
0\le\nu_\sigma\le\lambda_\sigma,\qquad
\lambda_\sigma([j,j+1])\le C\log^2(2+|j|).
\tag{17}
\]

The first inequality uses \(0\le\Pi_\sigma\le L_\sigma\), not
idempotence of L or of an Abel approximant. Countable additivity and the
usual multiplier integral follow by an orthonormal-basis/Tonelli expansion.

The symmetric calculation also gives

\[
C_\sigma^2=\chi V_\sigma^*P V_\sigma\chi,\qquad
\operatorname{Tr}\bigl(b_j(D)C_\sigma^2b_j(D)^*\bigr)
 \le C\log^2(2+|j|).
\tag{17a}
\]

Indeed, factor its sandwich through \(P V_\sigma\chi b_j(D)^*\)
and commute b_j past chi. The first term is
\(P(v_\sigma\overline b_j)(D)\chi\); the second is bounded by
the Hilbert--Schmidt norm of \([\chi,b_j(D)^*]\). Equations (12)--(13)
apply unchanged. In particular any negative-half-line intersection contained
in the spectral value 1 of C squared is included in this estimate.

There is an independent check of the projection part. The difference of
projections \(\mathcal Q_\sigma=V_\sigma^*PV_\sigma-P\) satisfies
\(\mathcal Q_\sigma\Pi_\sigma=-\Pi_\sigma\), hence
\(\Pi_\sigma\le\mathcal Q_\sigma^2\). Its squared-kernel measure is

\[
d\nu_\sigma(t)\le
 \left(\int\frac{|v_\sigma(t)-v_\sigma(s)|^2}{(t-s)^2}
           \frac{ds}{2\pi}\right)\frac{dt}{2\pi}.
\tag{18}
\]

Integrating on a unit t interval, the nearby s contribution is bounded by
the same finite-factor estimate; the distant contribution is bounded by
\(4/(t-s)^2\). This recovers (1). Formula (16) is stronger because it
also bounds the entire majorant and its positive return term.

## 4 Full source traces and uniform tails

For every Schwartz f, (17) gives the explicit bound

\[
\int |f(t)|^2d\lambda_\sigma(t)
 \le C\sum_{j\in\mathbb Z}\log^2(2+|j|)
                \sup_{t\in[j,j+1]}|f(t)|^2<\infty.
\tag{19}
\]

Restricting this sum to intervals meeting \(|t|>R\) proves uniform tail
decay; it is enough to sum over \(|j|>R-2\). For any integer M>1 this
tail is \(O_{f,M}(R^{1-2M}\log^2(2+R))\), after bounding f by its
order-M Schwartz seminorm. In particular, for every compact smooth position
source F,

\[
B_\sigma[F]=\|C_F\Pi_\sigma\|_{\rm HS}^2
 =\int|\widehat F|^2d\nu_\sigma<\infty,
\tag{20}
\]

uniformly in \(1/2<\sigma\le3/4\). Also
\(C_F L_\sigma C_F^*\) and
\(C_F(L_\sigma-\Pi_\sigma)C_F^*\) are positive trace class, with
the same uniform source-tail bound. Monotone convergence of the Abel return
operators therefore applies to full Schwartz multipliers at each sigma.
This does not assert global Schwartz bounds for \(\widehat Fv_\sigma\),
or trace class of unsandwiched products.

## 5 A full-source scalar boundary formula

Let \(a=|\widehat F|^2\), \(H_\sigma=L_\sigma-\Pi_\sigma\),
and \(X_a=P a(D)\chi\). The latter is trace class by the Schwartz
Hankel-kernel argument in the phase trace note. Equations (17a), (19),
and \(0\le H_\sigma\le L_\sigma\) make both positive traces below
finite. The independently defined full-source boundary correction is

\[
\begin{split}
K_\sigma[F]={}&\operatorname{Tr}(C_F C_\sigma^2 C_F^*)
 -\operatorname{Tr}(C_F H_\sigma C_F^*)\\
&+2\Re\operatorname{Tr}_{\chi\mathcal H}
       (C_\sigma T_\sigma X_a).
\end{split}
\tag{21}
\]

The crossing term is represented directly by its trace-class product on
the negative half-line; it is bounded by
\(2\|C_\sigma T_\sigma\|\|X_a\|_1\le2\|X_a\|_1\).
No trace-class assertion about \(C_F C_\sigma T_\sigma C_F^*\)
on the entire Hilbert space is needed.

Apply the proved compact-frequency trace decomposition to
\(f_N=\widehat F b_N\). The positive terms converge by (19) and
(17a); the crossing terms converge because
\(a b_N^2\to a\) in Schwartz seminorms and hence
\(P(a b_N^2)(D)\chi\to X_a\) in trace norm. The phase integral
converges absolutely: factoring its derivative as in (7)--(8) gives a
uniform bound \(\int_j^{j+1}|\phi_\sigma'(t)|dt
\le C\log(2+|j|)\), because each rational-factor derivative has
absolute integral at most \(2\pi\) and the remainder is bounded by
(6). It follows that

\[
\boxed{B_\sigma[F]
 =\int |\widehat F(t)|^2\phi_\sigma'(t)\frac{dt}{2\pi}
   +K_\sigma[F],\qquad 1/2<\sigma\le3/4.}
\tag{22}
\]

Thus the full-source boundary decomposition extends to this critical
neighborhood with the Abel return interpretation; the arithmetic Euler
series identity from sigma greater than 1 still does not extend unchanged.
See the [crossing note](SONIN_PHASE_ARITHMETIC_CROSSINGS_20260929.md)
for its residue terms.

The compact-frequency forms of Section 5 in the phase trace note now
approximate (20) uniformly as their frequency cutoff tends to infinity,
for sigma in this interval. Thus a proved local limit for \(\nu_\sigma\)
would automatically extend to every compact smooth source. Uniform tails
alone do not prove existence of that local limit or identify its atom weights.
Any loss caused by the exact kernel/return term remains an independent
question. Pole and off-line-zero crossing residues also remain necessary
for arithmetic identification.

## 6 Extension to every bounded sigma strip

The near-critical theorem has a useful global-in-sigma corollary. For every
fixed finite S > 1/2, all the unit-window and Schwartz-tail bounds above
hold uniformly for \(1/2\le\sigma\le S\), with a constant depending
on S. In particular full-source phase traces are finite for every fixed
\(\sigma>1/2\), including sigma=1 under its removable real-parameter
phase convention.

To see this, retain the zero factors (4) and multiply the local product (5)
by the single inverse pole factor

\[
R_\sigma(t)=\frac{t+i(\sigma-1)}{t-i(\sigma-1)}
\quad(\sigma\ne1),\qquad R_1(t)=1.
\tag{23}
\]

It has modulus one and energy \(4\pi^2\) when nonconstant. Its phase
derivative is
\(-2(\sigma-1)/((\sigma-1)^2+t^2)\), precisely the zeta pole's
contribution. The local logarithmic-derivative formula used in (7), now
on a fixed strip containing \([1/2,S]\), gives

\[
\frac{\zeta'}{\zeta}(s)
 -\sum_{|\gamma-j|\le5}\frac{m_\rho}{s-\rho}
 +\frac1{s-1}
 =O_S(\log(2+|j|)).
\tag{24}
\]

As before, zeros added beyond the small disk in that formula contribute
only \(O_S(\log(2+|j|))\). With \(R_\sigma\) extracted, the
remainder's derivative therefore has the bound (6) with an S-dependent
constant, even when sigma approaches 1. At sigma=1 the singular term's
real part vanishes off t=0, the ratio has a smooth real-parameter extension,
and the residual estimate holds by removal of the local pole factor.
The energy proof adds at most one factor to \(M_j\), preserving its
\(O(\log(2+|j|))\) bound. All subsequent operator arguments are
unchanged. This extracts both signs of zero factors and the pole factor;
it assumes neither a zero-free half-plane nor global innerness of the phase.

The scalar identity (22), with its independently defined correction (21),
also extends throughout each such bounded strip. At crossing lines its
bulk derivative uses the removable extension itself; one-sided phase-trace
limits can differ because of concentration. These trace-finiteness and
tail estimates do not remove the arithmetic crossing terms.
