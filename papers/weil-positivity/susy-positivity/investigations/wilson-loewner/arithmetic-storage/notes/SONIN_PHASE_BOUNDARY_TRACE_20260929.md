# Sonin phase trace and boundary resolvent

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Separate same-model derivations and a
[critical review](../reviews/SONIN_PHASE_BOUNDARY_TRACE_REVIEW_20260929.md)
check this research note; they are not independent specialist refereeing.

**Later continuation:** the [critical-limit synthesis](SONIN_CRITICAL_LIMIT_STATUS_20260929.md)
and its companion proofs now establish full phase-trace finiteness and
uniform source-weighted frequency tails, complete the crossing calculation,
and localize the remaining return defect at cutoff spectral value 1.
Statements below that trace finiteness or tails are unproved describe the
stage at which this representation was derived; those gaps are now closed.
The exact critical projection limit and arithmetic identification remain open.

## Result and scope

This completes the bounded trace-representation assignment in the
[continuation note](SONIN_DIRECT_LIMIT_CONTINUATION_20260929.md).
For the actual regularized Sonin projection and every compact smooth source,
the following identity holds for sigma greater than 1:

\[
\boxed{B_\sigma[F]=\Gamma[F]-W_\sigma[F]+K_\sigma[F].}
\tag{1}
\]

The new correction is an explicit trace across the logarithmic cutoff,
with a compressed resolvent. It is derived from the two cutoff constraints,
not defined by subtracting the arithmetic expression from the positive
trace. In the notation below its particularly short form is

\[
\boxed{K_\sigma[F]
=2\Re\operatorname{Tr}_{\chi\mathcal H}
\left(C_\sigma(I-C_\sigma^2)^{-1}T_\sigma
       a_{F,e}(D)\chi\right).}
\tag{2}
\]

Here \(a_{F,e}(t)=(|\widehat F(t)|^2+|\widehat F(-t)|^2)/2\).
The crossing operator \(P a_{F,e}(D)\chi\) has the explicit kernel
\(1_{x>0>y}\kappa_{F,e}(x-y)\), supported in a finite strip when
\(F\) is compactly supported. The inverse in (2) is essential.
The correction tends to the existing, generally nonzero
\(E_\infty[F]\) as sigma tends to infinity.

A second representation, using bounded Abel resolvents, continues to every
fixed \(\sigma>1/2\) on compact frequency windows. It proves local
finiteness of the positive frequency measure without a zero-free assumption.
Full source-weighted frequency tails and the boundary limit at the critical
line remain unproved. The phase bulk alone concentrates locally on zeros
on the critical line; that fact does not identify the complete arithmetic
form. No RH result, full critical trace limit, or new numerical certificate
is claimed.

## 1 Conventions and the actual projection

Use \(\mathcal H=L^2(\mathbb R,dx)\), inner products antilinear in
the first variable, and

\[
\widehat F(t)=\int F(x)e^{-itx}dx,\quad
F(x)=\int\widehat F(t)e^{itx}\frac{dt}{2\pi},\quad
U_a h(x)=h(x-a).
\tag{3}
\]

The notation \(b(D)\) means the Fourier multiplier by \(b(t)\);
it is unrelated to the transport \(D_\sigma\). Convolution \(C_F\)
is the multiplier \(\widehat F\). Set \(P=1_{(0,\infty)}\) and
\(\chi=I-P\). Endpoint values at zero do not matter. The physical
positive-axis cutoff is 1; source support does not move that cutoff.
The logarithmic cosine involution has multiplier-reflection form

\[
\mathcal F_\infty=\mathscr I V_\infty,\qquad
v_\infty(t)=e^{2i\theta(t)},\qquad
\theta(t)=\Im\log\Gamma(1/4+it/2)-(t/2)\log\pi,
\tag{4}
\]

where \(\mathscr I h(x)=h(-x)\). For fixed real \(\sigma\), put

\[
v_\sigma(t)=e^{2i\theta(t)}
 \frac{\zeta(\sigma+it)}{\zeta(\sigma-it)},\quad
V_\sigma=v_\sigma(D),\quad
\mathcal F_\sigma=\mathscr I V_\sigma.
\tag{5}
\]

The unit-modulus ratio is defined almost everywhere. At any zero or pole
on the chosen line its real-parameter singularity is removable: numerator
and denominator have the same order. Thus it has a smooth extension on
each compact real frequency interval. No half-plane innerness is asserted.
Equation (5) is the phase family from the
[regularization note](SONIN_REGULARIZED_POSITIVE_FAMILY_20260929.md).
It is a selfadjoint unitary involution, and its orthogonal Sonin projection is

\[
\Pi_\sigma=\operatorname{proj}
 \{h\in P\mathcal H:T_\sigma h=0\},\qquad
C_\sigma=\chi\mathcal F_\sigma\chi,\quad
T_\sigma=\chi\mathcal F_\sigma P.
\tag{6}
\]

Operators on cutoff subspaces are extended by zero when used on
\(\mathcal H\). In particular
\(T_\sigma T_\sigma^*=I_\chi-C_\sigma^2\).

For \(\sigma>1\), the bounded causal transport and its inverse are

\[
D_\sigma=\sum_{n\ge1}\mu(n)n^{-\sigma}U_{\log n},\qquad
D_\sigma^{-1}=\sum_{n\ge1}n^{-\sigma}U_{\log n}.
\tag{7}
\]

Both series converge absolutely in operator norm. Set
\(\ell_\sigma=1/\zeta(\sigma)\),
\(u_\sigma=\zeta(\sigma)/\zeta(2\sigma)\), and
\(c_0=\|\chi\mathcal F_\infty\chi\|<1\).
Let \(D_+=D_\sigma|_{P\mathcal H}\) and
\(D_-=\chi D_\sigma\chi|_{\chi\mathcal H}\).
Causality gives bounded inverses on both spaces and

\[
T_\sigma=D_-T_\infty D_+^{-1},\qquad
I_\chi-C_\sigma^2\ge
g_\sigma I_\chi,\quad
g_\sigma=(\ell_\sigma/u_\sigma)^2(1-c_0^2)>0.
\tag{8}
\]

Indeed \(\|D_+\|\le u_\sigma\),
\(\|D_-^{-1}\|\le\ell_\sigma^{-1}\), and
\(T_\infty T_\infty^*\ge(1-c_0^2)I_\chi\).
No compactness or nuclearity of \(C_\sigma\) is needed for (8).
Consequently the kernel projection is exactly

\[
\Pi_\sigma=P-T_\sigma^*M_\sigma T_\sigma,\qquad
M_\sigma=(I_\chi-C_\sigma^2)^{-1}.
\tag{9}
\]

This is the same projection as
\(D_\sigma\Pi_\infty A_\sigma^{-1}\Pi_\infty D_\sigma^*\),
where \(A_\sigma=\Pi_\infty D_\sigma^*D_\sigma\Pi_\infty\)
acts on the original Sonin space. Both project onto \(D_\sigma\mathcal K\).
Equation (9) therefore retains the actual orthogonal metric; it does not
replace the transported projection by an unnormalized transport.

## 2 The phase trace and its prime coefficients

Define the bounded selfadjoint difference of projections

\[
\mathcal Q_\sigma=V_\sigma^*PV_\sigma-P
=\mathcal F_\sigma\chi\mathcal F_\sigma-P.
\tag{10}
\]

This \(\mathcal Q_\sigma\) is not the arithmetic Weil form \(Q[F]\).
For a Schwartz multiplier \(a\) such that \(a v_\sigma\) is Schwartz,

\[
a(D)\mathcal Q_\sigma
=V_\sigma^*\left([P,(a v_\sigma)(D)]-[P,a(D)]V_\sigma\right)
\in\mathfrak S_1.
\tag{11}
\]

To check the ideal statement, each off-diagonal half-line block of
\([P,b(D)]\), after reflection, has kernel \(\check b(x+y)\)
on \(x,y\ge0\). Multiplying its extension by smooth cutoffs which
vanish below \(-1\) makes a Schwartz kernel on \(\mathbb R^2\).
Powers of the harmonic oscillator give rapid singular-value decay.
This also proves continuity from Schwartz seminorms to trace norm. This is
the smoothing argument of
[Connes and Consani, Appendix D](https://arxiv.org/html/2006.13771v1#A4),
with the normalization checked directly here.

On Fourier space with measure \(dt/(2\pi)\), the kernel of \(P\) is
\(\pi\delta(t-s)-i\operatorname{pv}(t-s)^{-1}\). Hence the kernel
of (10), with its removable diagonal filled in, is

\[
-i\frac{\overline{v_\sigma(t)}v_\sigma(s)-1}{t-s},\qquad
\mathcal Q_\sigma(t,t)=i\overline v_\sigma(t)v_\sigma'(t)
=-\phi_\sigma'(t),
\tag{12}
\]

where \(\phi_\sigma\) is any local phase. For \(\sigma>1\),
all derivatives of the zeta ratio are bounded at each fixed order;
gamma-ratio derivatives grow at most polynomially. Thus (11) applies to
every Schwartz \(a\), and

\[
-\operatorname{Tr}(a(D)\mathcal Q_\sigma)
=\int a(t)\phi_\sigma'(t)\frac{dt}{2\pi},
\qquad
\phi_\sigma'=\gamma(t)+2\Re\frac{\zeta'}{\zeta}(\sigma+it),
\tag{13}
\]
\[
\gamma(t)=\Re\psi(1/4+it/2)-\log\pi.
\]

For rigor in taking the diagonal trace, first multiply on both frequency
sides by a smooth compact cutoff. The resulting smooth compact kernel is
nuclear, and its trace is the diagonal integral. These cutoffs tend strongly
to the identity, so the sandwiched trace-class operator converges in trace
norm. The diagonal converges by the Schwartz decay and the stated derivative
bounds. This does not assign separate traces to the two projections in (10).

Now set \(a=|\widehat F|^2\) and
\(\kappa_F(x)=\int\overline{F(y)}F(y+x)dy\). Absolute convergence
of the differentiated Euler series, for \(\sigma>1\), gives

\[
\phi_\sigma'(t)=\gamma(t)
-2\sum_{p,m\ge1}(\log p)p^{-m\sigma}\cos(mt\log p).
\tag{14}
\]

The absolute coefficient sum and integrability of \(a\) justify
termwise integration. If \(\operatorname{supp}F\subset(-L/2,L/2)\),
(13) is precisely

\[
\Gamma[F]-W_\sigma[F],\qquad
\Gamma[F]=\int\gamma(t)|\widehat F(t)|^2\frac{dt}{2\pi},
\tag{15}
\]
\[
W_\sigma[F]=\sum_{m\log p<L}(\log p)p^{-m\sigma}
\{\kappa_F(m\log p)+\kappa_F(-m\log p)\}.
\]

All active prime powers are present. At equality \(m\log p=L\) the
correlation vanishes. The contact normalization is already in \(\gamma\);
no extra scalar contact is added. Equation (1) actually holds before source
preparation. For the target comparison we restrict to
\(F=(-\partial_x^2+1/4)h\), \(h\in C_c^\infty\), so both pole
moments vanish. The artificial deformation (15) is not the full shifted
completed-zeta form.

## 3 An independently represented boundary correction

Suppress sigma temporarily. In blocks \(P\mathcal H\oplus\chi\mathcal H\),
put \(L=P-T^*T=P\mathcal F P\mathcal F P\). Equations (6) and (10)
give the exact bounded operator identity

\[
\mathcal Q=
\begin{pmatrix}-L&T^*C\\ CT&C^2\end{pmatrix},\qquad
\Pi=L-H,\quad H=T^*C^2(I-C^2)^{-1}T\ge0.
\tag{16}
\]

Thus \(\Pi=-\mathcal Q+Z\), where the independently specified boundary
operator is

\[
Z=C^2+CT+T^*C-H.
\tag{17}
\]

The notation in (17) includes the cutoff embeddings. It comprises the
small-cutoff diagonal block, the two crossing blocks, and a return through
the compressed resolvent. In particular neither \(L\) nor the phase
derivative alone is the orthogonal projection.

Every trace used next is justified after smoothing. Equation (11) with
\(a=\widehat F\), together with \([C_F,P]\in\mathfrak S_1\),
implies that \(C_F\) times every cutoff block of \(\mathcal Q\)
is trace class. In particular
\(C_F L=-C_F P\mathcal Q P\in\mathfrak S_1\).
Since \(0\le\Pi,H\le L\), the sandwiches
\(C_F\Pi C_F^*\) and \(C_F H C_F^*\) are positive trace class.
The return trace is also the explicitly finite squared norm

\[
\operatorname{Tr}(C_F H C_F^*)
=\|C(I-C^2)^{-1/2}T C_F^*\|_{\rm HS}^2.
\tag{18}
\]

Consequently a first usable version of the correction is

\[
K_\sigma[F]=\operatorname{Tr}(C_F C^2 C_F^*)
 +2\Re\operatorname{Tr}(C_F CT C_F^*)
 -\|C(I-C^2)^{-1/2}T C_F^*\|_{\rm HS}^2.
\tag{19}
\]

Combining (13), (15), and (16) proves (1), including its signs.

There is a more economical form which exposes finite boundary support.
The involution and its Sonin projection preserve real functions, so the
frequency measure of \(\Pi\) is even. The phase density is even too.
We can therefore replace \(a=|\widehat F|^2\) by its even part
\(a_e\) in these scalar traces. The selfadjoint operator \(a_e(D)\)
commutes with \(\mathcal F\).

Let \(s=(I-C^2)^{1/2}\) and \(J=T^*s^{-1}\). This is an isometry
from \(\chi\mathcal H\) onto \((P-\Pi)\mathcal H\).
In coordinates \(J\chi\mathcal H\oplus\chi\mathcal H\),

\[
\mathcal F=\begin{pmatrix}-C&s\\s&C\end{pmatrix},\qquad
Z=\begin{pmatrix}-C^2&sC\\Cs&C^2\end{pmatrix}.
\tag{20}
\]

Write the corresponding compression of \(a_e(D)\) as
\(\begin{pmatrix}A&B\\B^*&D_0\end{pmatrix}\). Commutation gives
\(sD_0-As=CB+BC\). The crossing block
\(B=J^*a_e(D)\chi=s^{-1}T a_e(D)\chi\) is trace class, because
\(P a_e(D)\chi\) is a Schwartz Hankel block. The diagonal products
with \(C^2\) are trace class by (11), (20), and this crossing bound.
Explicitly, the two compressions of \(a_e(D)\mathcal Q\) are
\(-AC^2+BCs\) and \(B^*sC+D_0C^2\), so both diagonal products are
trace class before any cyclic rearrangement.
Multiplying the commutation identity by \(C^2s^{-1}\) and taking traces
therefore gives

\[
\operatorname{Tr}(C^2D_0-C^2A)
=2\operatorname{Tr}(C^3s^{-1}B).
\]

Adding the two crossing traces in (20) reduces (19) to
\(2\Re\operatorname{Tr}(Cs^{-1}B)\), which is (2).
This cancellation uses the even multiplier and the bounded inverse;
it is not an assertion that each boundary contribution vanishes.
The resulting useful estimate is

\[
|K_\sigma[F]|\le
2\|C_\sigma(I-C_\sigma^2)^{-1}T_\sigma\|
 \|P a_{F,e}(D)\chi\|_1.
\tag{21}
\]

Its deterioration near a closing cutoff gap identifies where finer signed
or source-weighted control is needed. No sign of (2) is asserted.

There is also a norm-convergent return expansion. With
\(X_F=P a_{F,e}(D)\chi\) and \(c_\sigma=\|C_\sigma\|<1\),

\[
K_\sigma[F]=2\Re\sum_{n\ge0}
 \operatorname{Tr}(C_\sigma^{2n+1}T_\sigma X_F).
\tag{21a}
\]

Truncating after \(n=N\) has error at most

\[
\frac{2c_\sigma^{2N+3}}{\sqrt{1-c_\sigma^2}}\|X_F\|_1.
\tag{21b}
\]

Indeed the omitted bounded factor is
\(C^{2N+3}(I-C^2)^{-1}T\); multiplying it by its adjoint and using
\(TT^*=I-C^2\) proves the displayed norm bound. This makes (2) an
approximable boundary formula at every fixed \(\sigma>1\), without
an eigenbasis for the deformed cutoff.

## 4 Archimedean calibration

As \(\sigma\to\infty\), \(D_\sigma\to I\) and
\(D_\sigma^{-1}\to I\) in norm. Thus \(C_\sigma,T_\sigma\)
converge in norm to their archimedean values, and (8) gives a uniform
positive gap for sufficiently large sigma. The crossing operator in (2)
is fixed and trace class. Formula (2) consequently converges directly to
the same boundary formula at \(\mathcal F_\infty\).

To identify it, take a real orthonormal basis
\(C_\infty\xi_n=\lambda_n\xi_n\), and set
\(\zeta_n=T_\infty^*\xi_n/\sqrt{1-\lambda_n^2}\).
The base cutoff is nuclear, and \(\|C_\infty\|<1\), as proved in
the [canonical audit](SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md).
Then (2) reads

\[
2\Re\sum_n\frac{\lambda_n}{\sqrt{1-\lambda_n^2}}
 \langle\zeta_n,a_{F,e}(D)\xi_n\rangle
=\int\kappa_F(t)e(t)dt=E_\infty[F],
\tag{22}
\]

where, for \(t\ge0\),
\(e(t)=\sum_n\lambda_n(1-\lambda_n^2)^{-1/2}
\langle\xi_n,U_{-t}\zeta_n\rangle\), extended evenly.
Vectors here are already in logarithmic coordinates. Absolute summability
of the coefficients justifies interchange with the compact correlation
integral. This matches
[Connes and Consani, Theorem 7](https://arxiv.org/html/2006.13771v1#S4)
under the repository's audited conventions.

Since the fixed-source prime sum is finite and tends to zero,
\(B_\sigma[F]\to\Gamma[F]+E_\infty[F]\).
Thus the correction has the required nonzero calibration, obtained from its
boundary expression rather than imposed as a definition.

## 5 What continues without a cutoff gap

At an arbitrary fixed \(\sigma>1/2\), (6), (10), and the block identity
for \(\mathcal Q\) still hold. For \(0\le r<1\), define

\[
\Pi_{\sigma,r}=P-T^*(I-rC^2)^{-1}T=L-H_r,\qquad
H_r=rT^*C^2(I-rC^2)^{-1}T.
\tag{23}
\]

Spectral calculus for \(T^*T\) shows

\[
0\le\Pi_\sigma\le\Pi_{\sigma,r}\le L,\quad
\Pi_{\sigma,r}\downarrow\Pi_\sigma\text{ strongly},\quad
H_r\uparrow L-\Pi_\sigma\text{ strongly as }r\uparrow1.
\tag{24}
\]

For example, at a spectral value \(\alpha\) of \(T^*T\), the
multiplier of (23) is
\((1-r)(1-\alpha)/(1-r+r\alpha)\), equal to 1 at \(\alpha=0\)
and tending to zero at every \(\alpha>0\). These are positive
contractions, usually not projections.

Let \(b\in C_c^\infty(\mathbb R_t)\) be a compact **frequency**
multiplier, not a compact position source. The removable singularities
discussed after (5) give \(bv_\sigma\in C_c^\infty\). Equation (11)
and its cutoff-block argument apply, and
\(b(D)Lb(D)^*\) is positive trace class. Domination in (24) proves

\[
\int|b(t)|^2d\nu_\sigma(t)
=\operatorname{Tr}(b(D)\Pi_\sigma b(D)^*)<\infty,
\tag{25}
\]

where \(\nu_\sigma(J)=\operatorname{Tr}(\Pi_\sigma E_J\Pi_\sigma)\).
Choosing \(b=1\) on any prescribed compact interval proves that
\(\nu_\sigma\) is locally finite. It is absolutely continuous at
each fixed sigma by the orthonormal-basis/Tonelli representation.
In fact the stronger statement \(b(D)\Pi_\sigma\in\mathfrak S_1\)
follows from \(L\Pi_\sigma=\Pi_\sigma\) and
\(b(D)L\in\mathfrak S_1\).

Equations (16)--(19) extend on these frequency tests by replacing the last
term of (19) with

\[
\lim_{r\uparrow1}\operatorname{Tr}(b(D)H_r b(D)^*).
\tag{26}
\]

This limit is finite by monotone convergence and domination by
\(b(D)Lb(D)^*\). The bulk term is
\(\int|b|^2\phi_\sigma'\,dt/(2\pi)\), with the phase derivative
interpreted through its removable extension. Thus there is an unconditional
local frequency representation of the actual projection, beyond the
absolute-convergence region. Formula (2), with a bounded inverse, is not
asserted there.

For a compact position source, \(\widehat F\) is Schwartz but is not
compactly supported. No global derivative or weighted tail estimate has
been proved here which would justify the same argument for
\(1/2<\sigma\le1\). A sufficient smoothing condition is
\(\widehat Fv_\sigma\in\mathcal S\); a sufficient frequency condition
is \(\int|\widehat F|^2d\nu_\sigma<\infty\). Neither follows from
local finiteness alone. Gap loss blocks the bounded inverse proof, but
(23)--(26) show that gap loss alone is not a trace impossibility theorem.

The original finite-rank forms always survive:
\(\|C_F\Pi_\sigma E_N\|_{\rm HS}^2\) is finite and positive for
fixed finite-rank \(E_N\). Strong convergence in (24) gives
\(C_F\Pi_{\sigma,r}E_N\to C_F\Pi_\sigma E_N\) in Hilbert--Schmidt
norm. The forms still tend to zero at fixed \(N\) when
\(\sigma\downarrow1/2\). When using (25)--(26), do not replace
\(\operatorname{Tr}(b\Pi_{\sigma,r}b^*)\) by
\(\|b\Pi_{\sigma,r}\|_{\rm HS}^2\): the approximant is not idempotent.

Local finiteness supplies another positive family. Fix an even smooth
\(b\), equal to 1 on \([-1,1]\), zero outside \([-2,2]\), and
nonincreasing in \(|t|\), with \(0\le b\le1\). Set
\(b_N(t)=b(t/N)\), independent of the source and sigma. Then

\[
\widetilde P_{\sigma,N}[F]
=\|(\widehat F b_N)(D)\Pi_\sigma\|_{\rm HS}^2
=\int|\widehat F(t)|^2b_N(t)^2d\nu_\sigma(t)
\tag{26a}
\]

is always finite and positive. At fixed sigma it increases to the full
trace, which may be infinite. A compact frequency window is an infinite-rank
cutoff and can retain concentrated trace mass even though
\(\Pi_\sigma\to0\) strongly. Thus the fixed-\(N\) zero-limit theorem
for ambient finite-rank \(E_N\) does not apply to (26a). This family
separates the local boundary limit from the remaining frequency-tail problem;
no arithmetic limit for it is established.

## 6 Local concentration and the arithmetic obstruction

There is an elementary unconditional concentration statement for the bulk:
as \(\sigma\downarrow1/2\),

\[
\frac{\phi_\sigma'(t)}{2\pi}\,dt
\longrightarrow
\sum_{\rho=1/2+i\gamma}m_\rho\delta_\gamma
\quad\text{as distributions on compact frequency tests}.
\tag{27}
\]

On a fixed compact frequency window, finitely many zeros are involved;
one can choose a narrow rectangle about the critical line with no off-line
zeros in it. Factor out each critical-line zero. Its contribution, with
\(\epsilon=\sigma-1/2>0\), is
\(2m_\rho\epsilon/(\epsilon^2+(t-\gamma)^2)\).
The remaining smooth contribution tends locally uniformly to zero: away
from these zeros the functional equation says \(v_{1/2}=1\), and the
factored singular contributions vanish pointwise there. The Poisson kernel
integrals prove (27), including multiplicities and normalization.
At the endpoint itself the phase derivative is zero; (27) is a one-sided
distributional limit, not differentiation of a continuous endpoint trace.

Equation (27) is not a concentration theorem for \(\nu_\sigma\).
The full boundary contribution (19), with the return limit (26), has not
been shown to vanish, or even
converge, on these windows. Moreover \(\Gamma-W_\sigma\) in (15)
equals the phase bulk only in the region proved in Section 2. Below 1,
the Euler expansion is unavailable and shifting the logarithmic-derivative
contour requires pole and zero residues. For example, near \(\sigma=1\)
the zeta pole contributes

\[
-\frac{2(\sigma-1)}{(\sigma-1)^2+t^2}.
\tag{28}
\]

Its pairing with \(a(t)dt/(2\pi)\) jumps by \(+2a(0)\) from the
right-hand to the left-hand limit. The finite prime deformation is
continuous in sigma. Pole neutrality at \(\widehat F(\pm i/2)=0\)
does not imply \(a(0)=0\). Hence even excellent trace control would not
justify carrying (15) through the pole unchanged.

Off-line zero crossings likewise cannot be discarded. In particular the
measure in (27) counts only critical-line zeros and cannot be identified
with the complete Weil form without addressing the remaining contributions.
For a continued trace decomposition, the discrepancy to control is the
independently represented boundary term **together with** the difference
between the analytically continued phase bulk and the artificial arithmetic
deformation. A conjecture that only \(K_\sigma\to0\) is insufficient
as an unconditional arithmetic-identification argument.

## 7 A quantitative next estimate

The Abel representation isolates a specific cutoff spectral tail. Write
the polar decomposition
\(T=(I-C^2)^{1/2}V\), where \(V:P\mathcal H\to\chi\mathcal H\)
is a partial isometry with final space
\(\ker(I-C^2)^\perp\). For a compact spectral \(b\), the measure

\[
\eta_{\sigma,b}(E)=\operatorname{Tr}
 \bigl(b(D)V^*C^2 1_E(C^2)Vb(D)^*\bigr)
\tag{29}
\]

is finite and positive on \([0,1]\). Its mass is the full return trace,
bounded by \(\operatorname{Tr}(b(D)Lb(D)^*)\), and
\(\eta_{\sigma,b}(\{1\})=0\). Spectral calculus gives the exact
error and a useful bound, for \(0<\delta<1\):

\[
\begin{split}
\operatorname{Tr}\bigl(b(D)(\Pi_{\sigma,r}-\Pi_\sigma)b(D)^*\bigr)
&=\int_{[0,1]}\frac{1-r}{1-r\lambda}\,d\eta_{\sigma,b}(\lambda)\\
&\le\frac{1-r}{1-r+r\delta}\eta_{\sigma,b}([0,1])
 +\eta_{\sigma,b}((1-\delta,1)).
\end{split}
\tag{30}
\]

This is a proved error lemma, not a uniform critical estimate. Its
fixed-sigma error tends to zero. The next bounded assignment is to establish
or refute a useful joint estimate for the mass in
\((1-\delta,1)\) as \(\sigma\downarrow1/2\), with the remaining
small-cutoff and crossing terms in (19) retained, on compact frequency
windows. In particular (29) does not measure the possible subspace
\(\ker(I-C_\sigma^2)\), the negative-half-line intersection; any
contribution from that subspace remains in the small-cutoff term of (19).
The quantity is
specified directly by the cutoff operator and source multiplier; it does
not fit the already-known arithmetic answer. Strong convergence
\(C_\sigma\to0\) does not control this moving spectral mass.

After that local estimate, full compact-source convergence would still
require source-weighted frequency tails and an arithmetic comparison that
includes the crossing residues described in Section 6. If the boundary
limit produces the wrong local measure, revise this candidate or its
cutoff. The raw critical prime-cutoff family remains a distinct candidate;
none of these statements identifies its limit with the phase path.

No new numerical run is warranted before this spectral-tail or boundary
claim has a discriminating formulation. The existing even and odd source
certificates remain available for subsequent calibration. Direct positive
approximation remains the objective; finite-stage domination is not a new
prerequisite.
