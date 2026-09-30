# Critical boundary localization and a closing-gap countermodel

29 September 2026. Prepared for Edward Baker with substantial LLM
assistance. Model: GPT-6 (Codex); exact serving variant and configured
reasoning effort are not exposed and are not inferred. This is an internal
derivation, not independent specialist refereeing.

## Result and limits

For the actual zeta phase family of the
[phase-boundary note](SONIN_PHASE_BOUNDARY_TRACE_20260929.md), the small-cutoff
trace and crossing trace tend to zero on every compact smooth frequency
test as \(\sigma\downarrow1/2\). Consequently

\[
\limsup_{\sigma\downarrow1/2}\int |b|^2\,d\nu_\sigma
\le \sum_{\rho=1/2+i\gamma}m_\rho|b(\gamma)|^2,
\qquad b\in C_c^\infty(\mathbb R).
\tag{1}
\]

The return measure \(\eta_{\sigma,b}\) loses all its mass on every fixed
closed subinterval of \([0,1)\). Any remaining loss of the positive
projection trace therefore concentrates at the spectral endpoint
\(\lambda=1\). For every fixed Abel parameter \(r<1\), the positive
Abel approximant does converge locally to the critical-zero measure.

A completely explicit rational phase family shows why these results do
not prove equality in (1): it has exactly the same local critical-zero
factorization, smooth background convergence, strong endpoint collapse,
and a strictly positive cutoff gap at every prelimit parameter, but its
actual Sonin projection is identically zero. Its return measure puts
asymptotically unit mass at an eigenvalue tending to 1. This is a
counterexample to an inference from that local structure, **not** a
counterexample to a claim about the actual zeta phase.

## 1. Conventions and localized factorization

Use the Hilbert space, Fourier convention, and notation of the
[phase-boundary note](SONIN_PHASE_BOUNDARY_TRACE_20260929.md):

\[
\mathcal H=L^2(\mathbb R,dx),\quad P=1_{x>0},\quad\chi=I-P,
\quad \mathcal F_\sigma=\mathscr I V_\sigma,
\quad V_\sigma=v_\sigma(D),
\]
\[
C_\sigma=\chi\mathcal F_\sigma\chi,\quad
T_\sigma=\chi\mathcal F_\sigma P,\quad
L_\sigma=P-T_\sigma^*T_\sigma,
\quad 0\le\Pi_\sigma\le L_\sigma.
\tag{2}
\]

All compressed operators are extended by zero on the complementary
half-line. Write \(\epsilon=\sigma-1/2\). On a fixed compact interval
containing the support of \(b\), choose a slightly larger interval whose
endpoints are not critical-zero ordinates and a narrow complex rectangle
with no off-line zeros. Only finitely many critical zeros occur there.
Factoring them out gives, on a neighborhood of the support,

\[
v_{1/2+\epsilon}(t)=B_\epsilon(t)w_\epsilon(t),\qquad
B_\epsilon(t)=\prod_\gamma
 \left(\frac{t-\gamma-i\epsilon}{t-\gamma+i\epsilon}\right)^{m_\gamma},
\quad w_\epsilon\longrightarrow1\quad\hbox{in }C^\infty.
\tag{3}
\]

The product includes every critical zero in the chosen rectangle.
Division cancels its entire local singular factor before the limit is
taken. The remaining factors are smooth jointly in \(\epsilon,t\),
including at \(\epsilon=0\); the functional equation gives
\(w_0=1\). No assumption about zeros outside this rectangle is used.

The rational multiplier \(B_\epsilon\) has modulus one on the real axis,
has all its poles in the lower half-plane, and its inverse Fourier kernel
is supported in \(( -\infty,0]\). This last assertion follows directly
by partial fractions and contour integration, or by multiplying the
one-factor kernel computed in Section 5. Hence

\[
P B_\epsilon(D)\chi=0.
\tag{4}
\]

Both \(B_\epsilon(D)\) and \(V_{1/2+\epsilon}\) converge strongly to
the identity by bounded pointwise convergence almost everywhere. The
functional equation supplies the latter convergence independently of RH.

## 2. The small-cutoff and crossing traces vanish

For every \(b\in C_c^\infty\),

\[
\boxed{\|C_\sigma b(D)\|_{\rm HS}\longrightarrow0.}
\tag{5}
\]

Here is a proof that does not require global derivative estimates for
\(v_\sigma\). Set \(r_\epsilon=b(w_\epsilon-1)\), extending by zero
outside the neighborhood used in (3). This is a smooth compact multiplier
tending to zero in the Schwartz topology. Since
\(v_\sigma b=B_\epsilon(b+r_\epsilon)\), (4) gives the exact identity

\[
C_\sigma b(D)=\mathscr I\left\{
 P r_\epsilon(D)\chi B_\epsilon(D)\chi
 +P\bigl(B_\epsilon(D)-V_\sigma\bigr)[b(D),\chi]
\right\}.
\tag{6}
\]

Indeed \(C_\sigma=\mathscr I P V_\sigma\chi\); expanding
\(\chi b=b\chi-[b,\chi]\), and then using
\(PB_\epsilon\chi=0\), proves (6).
For any Schwartz multiplier \(r\),

\[
\|P r(D)\chi\|_{\rm HS}^2
=\int_0^\infty x|\check r(x)|^2\,dx,
\tag{7}
\]

and \([b(D),\chi]\) is Hilbert--Schmidt. The first term of (6)
therefore tends to zero in that ideal. The second does also: a uniformly
bounded strongly null operator times a fixed Hilbert--Schmidt operator
converges in Hilbert--Schmidt norm, as follows by finite-rank
approximation. This proves (5).

It follows immediately that

\[
\operatorname{Tr}\bigl(b(D)C_\sigma^2 b(D)^*\bigr)
=\|C_\sigma b(D)^*\|_{\rm HS}^2\longrightarrow0.
\tag{8}
\]

Put \(a=|b|^2\). The crossing block
\(X_a=P a(D)\chi\) is trace class by the smooth Hankel-kernel argument
in the phase-boundary note. The strong convergence
\(C_\sigma T_\sigma\to0\) and uniform boundedness give

\[
\operatorname{Tr}\bigl(b(D)C_\sigma T_\sigma b(D)^*\bigr)
=\operatorname{Tr}(C_\sigma T_\sigma X_a)\longrightarrow0.
\tag{9}
\]

The trace identity is justified by the already established smoothed
cutoff-block trace-class statements. Convergence follows by trace-class
finite-rank approximation, not by estimating either diagonal projection
separately. No parity assumption on \(b\) is needed.

## 3. A sharp local upper bound for the actual projection

The phase-boundary block identity gives

\[
\operatorname{Tr}(b L_\sigma b^*)=
\int |b(t)|^2\phi_\sigma'(t)\frac{dt}{2\pi}
+\operatorname{Tr}(b C_\sigma^2 b^*)
+2\Re\operatorname{Tr}(b C_\sigma T_\sigma b^*).
\tag{10}
\]

Here and below an isolated \(b\) inside an operator formula denotes
\(b(D)\). The known local phase concentration and (8)--(9) yield

\[
\boxed{\operatorname{Tr}(b L_\sigma b^*)\longrightarrow
\mu_{\rm crit}(|b|^2),\qquad
\mu_{\rm crit}=\sum_{\rho=1/2+i\gamma}m_\rho\delta_\gamma.}
\tag{11}
\]

Positivity and \(\Pi_\sigma\le L_\sigma\) now prove (1).
The measures \(\nu_\sigma\) are uniformly bounded on each compact
interval near the endpoint: choose a smooth \(b=1\) there and apply
(11). Every sequence approaching the endpoint has vaguely convergent
subsequences, and every such limit has the form

\[
\nu_* =\sum_\gamma c_\gamma\delta_\gamma,
\qquad 0\le c_\gamma\le m_\gamma.
\tag{12}
\]

This follows by testing (1) first on intervals containing no zero, and
then on successively smaller neighborhoods of individual zeros. In
particular the actual positive frequency measure vanishes locally away
from critical zeros. Equality of the coefficients in (12) remains open.

The independently defined boundary correction on these tests is
\(K_\sigma[b]=\operatorname{Tr}(b C_\sigma^2b^*)+
2\Re\operatorname{Tr}(b C_\sigma T_\sigma b^*)-
\operatorname{Tr}(b H_\sigma b^*)\), with
\(H_\sigma=L_\sigma-\Pi_\sigma\). Thus

\[
K_\sigma[b]=-\operatorname{Tr}(b H_\sigma b^*)+o(1).
\tag{13}
\]

Along a subsequence with limit (12), its limit on \(|b|^2\) is exactly
\(-\sum_\gamma(m_\gamma-c_\gamma)|b(\gamma)|^2\).
The possible boundary limit is therefore a deficit on critical zeros,
not an arbitrary extra local measure.

## 4. All remaining return mass moves to the spectral endpoint

Use the polar decomposition and measure already defined in the
phase-boundary note,

\[
T_\sigma=(I-C_\sigma^2)^{1/2}V_\sigma^{\rm pol},\qquad
\eta_{\sigma,b}(E)=\operatorname{Tr}
\bigl(b(V_\sigma^{\rm pol})^*C_\sigma^2
1_E(C_\sigma^2)V_\sigma^{\rm pol}b^*\bigr).
\tag{14}
\]

The superscript distinguishes this partial isometry from the phase
multiplier. Its total mass is \(\operatorname{Tr}(bH_\sigma b^*)\).
For each fixed \(0<\delta<1\),

\[
\boxed{\eta_{\sigma,b}([0,1-\delta])
\le \delta^{-1}\|C_\sigma T_\sigma b^*\|_{\rm HS}^2
\longrightarrow0.}
\tag{15}
\]

To verify the last limit, write \(b^\sharp(t)=\overline{b(-t)}\).
The identity \(\mathcal F_\sigma b^*=b^\sharp(D)\mathcal F_\sigma\)
gives

\[
C_\sigma T_\sigma b^*
=C_\sigma b^\sharp(D)\mathcal F_\sigma P
 +C_\sigma\mathcal F_\sigma[P,b^*].
\tag{16}
\]

The first term is Hilbert--Schmidt small by (5), and the second by the
strong convergence \(C_\sigma\mathcal F_\sigma\to0\) and the fixed
Hilbert--Schmidt commutator. On \([0,1-\delta]\), spectral calculus
rewrites the operator in (14) as
\(T_\sigma^*C_\sigma^2(I-C_\sigma^2)^{-1}
1_{[0,1-\delta]}(C_\sigma^2)T_\sigma\); bounding the inverse there
by \(\delta^{-1}\) proves the inequality in (15).

In particular, the joint measures can only accumulate return mass at
\(\lambda=1\). This statement allows nonzero total return mass and is
not uniform integrability at that endpoint.

There is a useful positive limit before removing the Abel parameter. For
the operators \(\Pi_{\sigma,r}=L_\sigma-H_{\sigma,r}\) of the
phase-boundary note,

\[
0\le\operatorname{Tr}(bH_{\sigma,r}b^*)
\le\frac{r}{1-r}\|C_\sigma T_\sigma b^*\|_{\rm HS}^2,
\quad 0\le r<1.
\tag{17}
\]

Consequently

\[
\boxed{\lim_{\sigma\downarrow1/2}
\operatorname{Tr}(b\Pi_{\sigma,r}b^*)=
\mu_{\rm crit}(|b|^2)\quad\hbox{for each fixed }r<1.}
\tag{18}
\]

A joint choice \(r=r(\sigma)\uparrow1\) has the same conclusion if
\(\|C_\sigma T_\sigma b^*\|_{\rm HS}^2/(1-r(\sigma))\to0\).
This is a sufficient source-dependent estimate, not a proved universal
rate or an identification with the complete arithmetic form. The Abel
operators are positive contractions, generally not projections, and the
trace in (18) cannot be replaced by \(\|b\Pi_{\sigma,r}\|_{\rm HS}^2\).

## 5. Exact rational countermodel with a prelimit cutoff gap

This section concerns a separate model, not the zeta phase. Take
\(0<\epsilon<1\), set \(R=\epsilon^{-1}\), and define

\[
B_h(t)=\frac{t-ih}{t+ih},\qquad
v_\epsilon^{\rm mod}(t)=-\frac{B_\epsilon(t)}{B_R(t)},\qquad
q=\frac{R-\epsilon}{R+\epsilon}
=\frac{1-\epsilon^2}{1+\epsilon^2}.
\tag{19}
\]

This multiplier has modulus one and satisfies
\(v(-t)=\overline{v(t)}\), so \(\mathcal F^{\rm mod}=\mathscr I v(D)\)
is a selfadjoint unitary involution. On every compact interval it has the
factorization \(v_\epsilon^{\rm mod}=B_\epsilon w_\epsilon\), where
\(w_\epsilon=-B_R^{-1}\to1\) in \(C^\infty\). It converges pointwise
almost everywhere to 1, and its phase density satisfies

\[
(\phi_\epsilon^{\rm mod})'(t)
=\frac{2\epsilon}{t^2+\epsilon^2}
-\frac{2R}{t^2+R^2},\qquad
\frac{(\phi_\epsilon^{\rm mod})'}{2\pi}\,dt
\longrightarrow\delta_0
\quad\hbox{locally}.
\tag{20}
\]

Partial fractions give the full inverse Fourier kernel, including its
delta term:

\[
\check v_\epsilon^{\rm mod}(x)
=-\delta_0(x)-2\epsilon q e^{\epsilon x}1_{x<0}
 +2Rq e^{-Rx}1_{x>0}.
\tag{21}
\]

For example \(\check B_h=\delta_0-2h e^{hx}1_{x<0}\), which fixes the
Fourier orientation in (3)--(4). Let the unit vectors

\[
u_\epsilon(x)=\sqrt{2\epsilon}\,e^{-\epsilon x}1_{x>0},\qquad
\xi_R(x)=\sqrt{2R}\,e^{Rx}1_{x<0}.
\tag{22}
\]

Since the kernel of \(\mathcal F\) is \(\check v(-x-y)\), (21)
immediately yields the two diagonal cutoff blocks

\[
A:=P\mathcal F^{\rm mod}P=-q\,|u_\epsilon\rangle\langle u_\epsilon|,
\qquad
C:=\chi\mathcal F^{\rm mod}\chi=q\,|\xi_R\rangle\langle\xi_R|.
\tag{23}
\]

Here \(|u\rangle\langle u|\) is the orthogonal rank-one projection.
Thus \(\|C\|=q<1\), and there is no subspace
\(\ker(I-C^2)\). The cutoff gap is genuinely positive at each parameter,
although

\[
1-q^2=\frac{4\epsilon^2}{(1+\epsilon^2)^2}\longrightarrow0.
\tag{24}
\]

Because \(L=A^2=q^2|u_\epsilon\rangle\langle u_\epsilon|\) and
\(\Pi\le L\), an orthogonal projection \(\Pi\) must be zero:
\(\|L\|=q^2<1\). Hence

\[
\Pi_\epsilon^{\rm mod}=0,\qquad
H_\epsilon^{\rm mod}=L_\epsilon^{\rm mod}
=q^2|u_\epsilon\rangle\langle u_\epsilon|.
\tag{25}
\]

One may verify the polar pair directly. Equations (21)--(22) give
\(T u_\epsilon=-\sqrt{1-q^2}\,\xi_R\); the minus sign can be absorbed
into \(\xi_R\). In either convention, \(C^2\xi_R=q^2\xi_R\), so

\[
\eta_{\epsilon,b}^{\rm mod}
=q^2\|b(D)u_\epsilon\|_2^2\,\delta_{q^2},\qquad
\|b(D)u_\epsilon\|_2^2
=\int |b(t)|^2\frac{2\epsilon}{\epsilon^2+t^2}\frac{dt}{2\pi}
\longrightarrow |b(0)|^2.
\tag{26}
\]

Thus for every fixed \(\delta>0\),

\[
\lim_{\epsilon\downarrow0}
\eta_{\epsilon,b}^{\rm mod}((1-\delta,1))=|b(0)|^2.
\tag{27}
\]

The local small-cutoff and crossing traces still tend to zero by
Section 2, while the return trace tends to \(|b(0)|^2\). The full local
boundary correction therefore tends to \(-|b(0)|^2\) and exactly
cancels the phase bulk. In particular a vanishing small-cutoff trace
does not force a vanishing return trace.

The Abel crossover is also explicit:

\[
\Pi_{\epsilon,r}^{\rm mod}
=\frac{q^2(1-r)}{1-rq^2}
 |u_\epsilon\rangle\langle u_\epsilon|.
\tag{28}
\]

In this model the numerator in the general estimate (17) is exactly
\(\|CTb^*\|_{\rm HS}^2=q^2(1-q^2)\|b u_\epsilon\|_2^2\),
which is asymptotic to \(4\epsilon^2|b(0)|^2\) when \(b(0)\ne0\).

Writing \(d=1-r\), its smoothed trace tends to \(|b(0)|^2\) if
\(d/\epsilon^2\to\infty\), to zero if
\(d/\epsilon^2\to0\), and to
\(c(c+4)^{-1}|b(0)|^2\) if \(d/\epsilon^2\to c\in(0,\infty)\).
This demonstrates the failure of interchange of the two limits within
a completely solvable closing-gap family.

## 6. Compact-source corollary and the next actual-zeta step

The companion [frequency-tail theorem](SONIN_PHASE_FREQUENCY_TAILS_20260929.md)
supplies uniform unit-window bounds of order \(1+\log^2(2+|j|)\) for the
positive measures obtained by smoothing \(L_\sigma\) and \(C_\sigma^2\).
Consequently (8), (11), and (18) extend from compact-frequency \(b\) to
\(b=\widehat F\), for every \(F\in C_c^\infty\), by a compact frequency
cutoff followed by the uniform Schwartz-weighted tail bound. The crossing
term extends directly: \(P|\widehat F|^2(D)\chi\) is trace class and
\(C_\sigma T_\sigma\to0\) strongly. Therefore, writing

\[
Z_{\rm crit}[F]=\sum_{\rho=1/2+i\gamma}
 m_\rho|\widehat F(\gamma)|^2,
\]

one obtains

\[
\operatorname{Tr}(C_F L_\sigma C_F^*)\longrightarrow Z_{\rm crit}[F],
\qquad
\limsup_{\sigma\downarrow1/2}B_\sigma[F]\le Z_{\rm crit}[F],
\tag{29}
\]
\[
B_\sigma[F]=Z_{\rm crit}[F]
-\operatorname{Tr}(C_F H_\sigma C_F^*)+o(1),\qquad
K_\sigma[F]=-\operatorname{Tr}(C_F H_\sigma C_F^*)+o(1),
\tag{30}
\]
\[
\lim_{\sigma\downarrow1/2}
\operatorname{Tr}(C_F\Pi_{\sigma,r}C_F^*)=Z_{\rm crit}[F]
\quad\text{for each fixed }r<1.
\tag{31}
\]

For (31), it is enough to pass the local limit through tails using
\(0\le\Pi_{\sigma,r}\le L_\sigma\); no global rate for (17) is needed.
The series defining \(Z_{\rm crit}\) converges by the same window bounds.
These are consequences of the companion theorem, not of local finiteness
alone.

The unresolved local claim is now precise: prove, or disprove for the
actual zeta phase, that

\[
\eta_{\sigma,b}([0,1])\longrightarrow0,
\tag{32}
\]

equivalently that the upper bound (1) is attained on each compact smooth
frequency test. Equation (15) settles every fixed portion of the spectrum
away from 1; only mass approaching 1 remains. The rational model proves
that smooth local factorization, the strong endpoint limit, and even a
prelimit cutoff gap do not establish equality in the upper bound (29).
An additional property of the
actual global zeta phase is required.

The frequency-tail theorem supplies compact-position-source finiteness
and the upper bounds above. Arithmetic identification additionally
requires the pole and off-line-zero crossing terms of the
[arithmetic continuation note](SONIN_PHASE_ARITHMETIC_CROSSINGS_20260929.md).
The critical-zero measure alone does not contain those terms. Nothing
here proves RH or identifies a positive critical limit with the complete
Weil form.
