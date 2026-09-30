# Sonin canonical comparison: normalization, source class, and trace audit

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort are
not exposed. Three separate same-model readings checked the calibration,
source/transport conventions, and finite-place algebra. These are internal
mathematical checks, not independent human refereeing.

**Result.** The canonical comparison in the [28 September handoff](../../../../../investigations/program-meta-analysis/notes/SONIN_RESIDUAL_CONTINUATION_20260928.md)
passes on compact smooth inputs. No corrective sign, contact, pole, or
finite-place adjoint change is required. This note supplies the missing
repository-local derivation, including the compressed trace-class proof.
The stronger smooth trace assertion can also be proved. Positivity of the
complete residual is still open. The [continuation analysis](SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md)
derives a signed place-addition identity, a faster return expansion, and a
one-sided trace-approximation bound; it explains why an actual numerical
Sonin residual is not yet certified.

The audit uses the recovered 14 September comparison, SHA-256
`6c1d50c6b53e8f261efcb3d49e43dfa8e8affcb16e816964f054825487b3e12c`,
as a claim to check, not as authority. Repository baseline inspected:
`305806625d1659466f2ba7ff3fed9d496c1a1bc2`. The pre-existing modified
meta-analysis index and untracked continuation note are retained.

## 1. Full form and coordinate conventions

Let \(I_L=(-L/2,L/2)\), \(f,g\in C_c^\infty(I_L)\), with zero
extensions \(F,G\). Inner products are antilinear in their first slot. Set

\[
\widehat F(t)=\int F(x)e^{-itx}\,dx,\qquad
U_a v(x)=v(x-a),\qquad
\kappa_{f,g}(a)=\int\overline{F(x)}G(x+a)\,dx.
\tag{1}
\]

Thus \(C_F^*C_G=C_\kappa=:K_{f,g}\), with Fourier multiplier
\(\overline{\widehat F}\widehat G\). The full target is

\[
Q_L(f,g)=\Gamma_L(f,g)+P^{\rm pole}_L(f,g)-\mathcal W_L(f,g),
\tag{2}
\]
\[
\Gamma_L(f,g)=\int_{\mathbb R}
\bigl(\Re\psi(1/4+it/2)-\log\pi\bigr)
\overline{\widehat F(t)}\widehat G(t)\,\frac{dt}{2\pi},
\tag{3}
\]
\[
P^{\rm pole}_L(f,g)=2\overline{c(f)}c(g)-2\overline{s(f)}s(g),
\quad c(f)=\int F(x)\cosh(x/2)dx,\quad
s(f)=\int F(x)\sinh(x/2)dx,
\tag{4}
\]
\[
\mathcal W_L(f,g)=\sum_{m\log p<L}(\log p)p^{-m/2}
\{\kappa_{f,g}(m\log p)+\kappa_{f,g}(-m\log p)\}.
\tag{5}
\]

No scalar contact is added to (3). At \(m\log p=L\) the correlation
vanishes for these interior compact tests. The support parameter \(L\)
does not change the Sonin cutoff, which stays 1 throughout.

For the positive-axis state space define
\(Wh(x)=e^{x/2}h(e^x)\) and
\(\vartheta(\rho)h(y)=\rho^{-1/2}h(y/\rho)\).
Then \(W\vartheta(e^a)W^{-1}=U_a\), and a multiplicative kernel
\(q(e^a)=\kappa(a)\) gives \(W\vartheta(q)W^{-1}=C_\kappa\).
The even real-place space, with the paper's half-real-line norm, is
unitarily the positive-axis space. Its cosine transform is exactly
\(\mathcal F_\infty h(x)=2\int_0^\infty\cos(2\pi xy)h(y)dy\).
Physical evenness supplies no parity restriction on the logarithmic variable.

Writing
\(\theta(t)=\Im\log\Gamma(1/4+it/2)-(t/2)\log\pi\) gives
\(2\theta'(t)=\Re\psi(1/4+it/2)-\log\pi\).
This identifies \(W_\infty=-W_{\mathbb R}\) with (3), including its
contact. These conventions match Connes–Consani, [Appendices A, B, E](https://arxiv.org/html/2006.13771v1).

For an independent check of the poles and prime weights, set
\(v(u)=u^{-1/2}\kappa(\log u)\) and
\(M_\pm(F)=\int F(x)e^{\pm x/2}dx\). Then

\[
\widetilde v(1)=\overline{M_-(F)}M_+(G),\qquad
\widetilde v(0)=\overline{M_+(F)}M_-(G).
\tag{6}
\]

Their sum is (4). The local evaluation
\(v(p^m)+p^{-m}v(p^{-m})\) is
\(p^{-m/2}(\kappa(m\log p)+\kappa(-m\log p))\).
The poles belong to the global explicit formula, not to the archimedean
Sonin calibration.

## 2. The pole-neutral restriction is sufficient, with all-support quantifiers

Define
\[
\mathcal D_L^0=\{f\in C_c^\infty(I_L):M_+(F)=M_-(F)=0\}.
\tag{7}
\]
For \(g_0(u)=u^{-1/2}F(\log u)\), direct substitution yields
\[
M_{g_0}(s)=\int F(x)e^{(s-1/2)x}dx
=\widehat F(i(s-1/2)).
\tag{8}
\]
Hence the two moments in (7) are its Mellin values at 1 and 0.
The critical-line argument is \(\widehat F(-t)\), not
\(\widehat F(t)\). The gamma multiplier's evenness makes this consistent
with (3). Multiplicative convolution gives
\((g_0*\overline{g_0}^{\sharp})(e^a)=e^{-a/2}\kappa_{f,f}(a)\).

[Connes–Consani, Appendix C, Proposition 1](https://arxiv.org/html/2006.13771v1#A3)
therefore applies with prescribed Mellin zeros \(\{0,1\}\):
\[
\mathrm{RH}\ \Longleftrightarrow\
Q_L[f]\ge0\quad\text{for every }L>0,\ f\in\mathcal D_L^0.
\tag{9}
\]
Any nested \(L_j\to\infty\) suffices. A finite family at \(L=1\)
does not. The zero sum in the explicit formula is unconditionally a sum
of products \(M_{g_0}(\rho)\overline{M_{g_0}(1-\bar\rho)}\),
which cannot be replaced by absolute squares without RH.

The same-support preparation is exactly onto:
\[
\mathcal D_L^0=(-\partial_x^2+1/4)C_c^\infty(I_L).
\tag{10}
\]
The forward implication is integration by parts. For the converse use
\(h(x)=\int e^{-|x-y|/2}F(y)dy\). The Green kernel has derivative
jump \(-1\), so \((-\partial_x^2+1/4)h=F\).
Outside the convex hull of \(\operatorname{supp}F\), its tails are
\(e^{-x/2}M_+(F)\) and \(e^{x/2}M_-(F)\), both zero.
The ODE gives smoothness, proving (10) without enlarging support.

Optional zero mean adds the Mellin zero \(1/2\), which is allowed since
\(\zeta(1/2)\ne0\). Its same-support range is
\(\partial_x(-\partial_x^2+1/4)C_c^\infty(I_L)\).
No additional single parity restriction is used. Both additive parity
sectors must be retained unless a separate criterion proves otherwise.

## 3. Actual projection and finite-place metric

In \(L^2(0,\infty;dx)\), put \(\chi=1_{(0,1)}\),
\(R=I-\chi\), and \(C=\chi\mathcal F_\infty\chi\) on
\(L^2(0,1)\). This compact self-adjoint contraction has \(c=\|C\|<1\):
an extremal vector at norm 1 would have both itself and its Fourier
transform compactly supported, contradicting analytic continuation.
The orthogonal projection onto the cutoff-1 Sonin space is
\[
\Pi=R-R\mathcal F_\infty\chi(I-C^2)^{-1}
\chi\mathcal F_\infty R.
\tag{11}
\]
Indeed \(T_0=\chi\mathcal F_\infty R\) satisfies
\(T_0T_0^*=I-C^2\), and (11) is the kernel projection for \(T_0\)
inside \(R\mathcal H\). Conjugate all operators by \(W\) before
using logarithmic translations. Separate unsmoothed terms in (11) need
not have finite traces.

The semilocal transport is
\[
D_S=\prod_{p\in S_f}(I-p^{-1/2}U_{\log p}),\quad
G_S=D_S^*D_S,\quad A_S=(\Pi G_S\Pi)|_{\mathcal K},\quad
\mathcal K=\operatorname{Ran}\Pi.
\tag{12}
\]
[CCM v2, §4.6, (57)](https://arxiv.org/html/2310.18423v2#S4.SS6)
has multiplier \(\prod(1-p^{-1/2-it})\), verifying this orientation.
The other map is \(\eta_S=(D_S^*)^{-1}\).
[Theorem 4.6 and §4.8](https://arxiv.org/html/2310.18423v2#S4.SS7)
identify the invariant semilocal Sonin sector with \(D_S\mathcal K\)
and retain its changing metric. They do not assert isometry.

For fixed finite \(S\),
\[
\ell_S^2 I\le G_S,A_S\le u_S^2 I,\quad
\ell_S=\prod_{p\in S_f}(1-p^{-1/2}),\quad
u_S=\prod_{p\in S_f}(1+p^{-1/2}).
\tag{13}
\]
These constants are not uniform in all primes. The isometry and ordinary
orthogonal projection are
\[
J_S=D_S\Pi A_S^{-1/2}:\mathcal K\longrightarrow\mathcal H,
\qquad \Pi_S=J_SJ_S^*=D_S\Pi A_S^{-1}\Pi D_S^*.
\tag{14}
\]
Inverses act on \(\mathcal K\); the surrounding projections implement
zero extension. Omitting the inverse changes the object being traced.

## 4. Calibration and convergence of its error kernel

Take an orthonormal real eigenbasis \(C\xi_n=\lambda_n\xi_n\),
extend \(\xi_n\) by zero, and put
\(\zeta_n=R\mathcal F_\infty\xi_n/\sqrt{1-\lambda_n^2}\).
After applying \(W\) to both vectors, define, for \(t\ge0\),
\[
e(t)=\epsilon(e^t)=\sum_n
\frac{\lambda_n}{\sqrt{1-\lambda_n^2}}
\langle W\xi_n,U_{-t}W\zeta_n\rangle,\qquad e(-t)=e(t).
\tag{15}
\]
The sign and \(U_{-t}\) agree with [Connes–Consani, Theorem 7,
(83)–(84)](https://arxiv.org/html/2006.13771v1#S4).

Convergence follows directly from the nuclear Taylor expansion
\[
2\cos(2\pi xy)=\sum_{j\ge0}
\frac{2(-1)^j(2\pi)^{2j}}{(2j)!}x^{2j}y^{2j},\quad
\|C\|_1\le\sum_{j\ge0}
\frac{2(2\pi)^{2j}}{(2j)!(4j+1)}<\infty.
\tag{16}
\]
Consequently \(\sum |\lambda_n|/\sqrt{1-\lambda_n^2}
\le\|C\|_1/\sqrt{1-c^2}\). Formula (15) converges absolutely
and uniformly for all real \(t\). It is real, continuous and bounded,
and \(e(0)=0\). If ordered by decreasing eigenvalue magnitude,
\[
\|e-e_N\|_\infty\le
(1-c^2)^{-1/2}\sum_{n>N}|\lambda_n|.
\tag{17}
\]
This is an analytic bound. Its numerical use needs certified spectral
data and a quantified upper bound \(c<1\).

With \(V_F=C_F\Pi:\mathcal K\to\mathcal H\), the calibration is
\[
\mathcal B_\infty(f,g)=\operatorname{Tr}_{\mathcal K}(V_F^*V_G)
=\Gamma_L(f,g)+\mathcal E_\infty(f,g),\qquad
\mathcal E_\infty(f,g)=\int\kappa_{f,g}(t)e(t)dt.
\tag{18}
\]
The error has a **plus sign**. The pole term is absent from (18).
The published short-support dominance theorem does not extend (by this
identity alone) from source length \(\log2\) to length 1.

## 5. Trace existence, including a proof of the stronger smooth assertion

Here all convolution kernels are compact smooth. In logarithmic coordinates
write \(P_+=1_{(0,\infty)}\), let \(B\) be the unitary Fourier
multiplier \(u(t)=e^{2i\theta(t)}\), and let \(\mathscr I v(x)=v(-x)\).
The cosine involution is \(\mathscr I B\), so
\(\widehat P_+=B^*(1-P_+)B\). Set
\(Q_0=B^*P_+B-P_+\). Then
\[
L_0=P_+\widehat P_+P_+=-P_+Q_0P_+.
\tag{19}
\]
For every Schwartz multiplier \(a\), \([P_+,a(D)]\) is trace class.
Reflecting either off-diagonal quadrant gives a Hankel kernel \(k(x+y)\)
on \(x,y\ge0\). Choose a smooth function \(\eta\) that is zero below
\(-1\) and one above 0. The extension \(\eta(x)\eta(y)k(x+y)\)
is Schwartz on \(\mathbb R^2\); every power of the harmonic oscillator
acting on this extended kernel is bounded. Compress back to the quadrant.
This proves rapid singular-value decay. It is also the argument in
[Connes–Consani, Appendix D, Lemma 1](https://arxiv.org/html/2006.13771v1#A4).

For \(H\in C_c^\infty(\mathbb R)\), both \(\widehat H\) and
\(\widehat H u\) are Schwartz. The gamma-ratio derivatives have at most
polynomial/logarithmic growth. The identity
\[
C_H[P_+,B]=[P_+,C_HB]-[P_+,C_H]B
\tag{20}
\]
implies that \(C_HQ_0=B^*C_H[P_+,B]\) is trace class. Moving \(C_H\)
past the first \(P_+\) in (19) proves \(C_HL_0\) trace class.
The two-projection decomposition is
\[
L_0=\Pi+\sum_n\lambda_n^2
|W\zeta_n\rangle\langle W\zeta_n|.
\tag{21}
\]
The correction is trace class by \(\sum\lambda_n^2<\infty\).
Thus \(C_H\Pi\in\mathfrak S_1\), in particular
\(V_F\in\mathfrak S_2\) and \(K_{f,g}\Pi\in\mathfrak S_1\).
Only already smoothed trace-class operators were subtracted.
Theorem 7 then identifies the trace in (18); polarization handles complex
inputs. This establishes the stronger assertion by a separate proof,
rather than incorrectly inferring it from a Hilbert–Schmidt norm.

The simpler compressed proof suffices for all finite-place operations.
Convolution commutes with the bounded translation polynomial \(G_S\), hence
\[
\Pi G_SK_{f,g}\Pi=V_F^*G_SV_G,\quad
\Pi K_{f,g}\Pi=V_F^*V_G,
\]
\[
\Pi G_S(I-\Pi)K_{f,g}\Pi
=V_F^*G_SV_G-A_SV_F^*V_G\in\mathfrak S_1.
\tag{22}
\]
This explicitly justifies each compressed trace and its bounded-factor
cyclicity without requiring the stronger result.

## 6. Audited full comparison

Finite-place smoothing follows from
\(C_FJ_S=D_S V_F A_S^{-1/2}\). Define
\[
\mathcal B_S(f,g)=\langle C_FJ_S,C_GJ_S\rangle_{\rm HS},\qquad
\mathcal B_S[f]=\|C_F\Pi_S\|_{\rm HS}^2\ge0.
\tag{23}
\]
Using (22) in
\(\mathcal B_S=\operatorname{Tr}(A_S^{-1}V_F^*G_SV_G)\)
gives
\[
\mathcal B_S=\mathcal B_\infty+\Delta_S,\qquad
\Delta_S(f,g)=\operatorname{Tr}_{\mathcal K}
\bigl(A_S^{-1}\Pi G_S(I-\Pi)K_{f,g}\Pi\bigr).
\tag{24}
\]
Therefore, with every prime power from (5) retained,
\[
Q_L=\mathcal B_S+\mathcal R_{S,L},\qquad
\boxed{\mathcal R_{S,L}=P^{\rm pole}_L-\mathcal E_\infty
-\Delta_S-\mathcal W_L.}
\tag{25}
\]
All formulas hold on the stated smooth core for each finite \(S\).
The algebra in fact permits any finite \(S\), provided (5) remains
complete; including all active primes is the intended arithmetic comparison.
An inactive place changes (23) and (24) but leaves (2) unchanged.

For completeness, the natural fixed-support form norm is
\[
\|f\|_{\log}^2=\int(1+\log(2+|t|))|\widehat F(t)|^2\,\frac{dt}{2\pi}.
\tag{26}
\]
On the completion of the smooth core, (3) is continuous. The error kernel
is bounded, so \(|\mathcal E_\infty(f,g)|\le
L\|e\|_\infty\|f\|_2\|g\|_2\); the poles and finite prime sums
are also continuous. Furthermore
\[
\frac{\ell_S^2}{u_S^2}\mathcal B_\infty[f]
\le\mathcal B_S[f]\le
\frac{u_S^2}{\ell_S^2}\mathcal B_\infty[f].
\tag{27}
\]
The form identity extends continuously to this completion, and moment
constraints are closed there. No extension of every separate
\(\mathfrak S_1\) assertion or return-series trace is claimed by continuity.

## 7. Scope of what is settled

The audit settles normalization, the actual projection, adjoints and inverse
metric, trace existence, and the legitimate restricted-test RH implication.
It supplies no all-input residual inequality. The semilocal small-cutoff
operator's compactness does not replace smoothing; its first-prime
non-Hilbert–Schmidt calculation is checked separately in the continuation
analysis. No finite Weil certificate, manuscript, or CCM investigation
was reopened. The next numerical obligation is a computable error bound
for actual Sonin-projected sources, as specified in the companion note.
