# Review reconciliation and the sharp metric threshold

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort:
**ultra**. Two parallel same-model agents checked the endpoint analysis and
the perturbation algebra. These are internal checks. Baseline:
`e2e1e0e`; the [Claude review][review] is in commit `7e56ba2`.

**Status: proved in-note, with inherited Sonin inputs; round-two assessment
pending.** The review's four additional analytic claims are accepted, with
the scope correction in §5. The metric remainder is bounded exactly when
\(L\le a:=|\log(p/q)|\). Its boundary case is noncompact. More precisely,
after subtracting the explicit arithmetic form, its essential norm at
\(L=a\) is \(\pi\beta_p\beta_q/8\). Below that threshold the same
arithmetic-subtracted operator is compact. A second result gives an exact
return formula and an explicit cubic remainder for the leading mixed term.
Neither result signs the complete actual-Sonin response or improves a
positivity margin.

The [result index][results], [Sonin cluster 07][s07] and [avoid index][avoid]
govern this continuation, particularly [target reformulations][a01],
[scoped exclusions][a07] and [separate-sector bounds][a12]. The opening
phase passes its stated acceptance criterion and is closed after review.
This bounded second round completes the proposed reconciliation and
sharpens its endpoint; an estimate campaign still needs a named consumer.

## 1 Place changes and source changes

Retain [Notes 01–02][n02]: \(F=(-\partial_x^2+1/4)h\),
\(h\in C_c^\infty(I_L)\), \(I_L=(-L/2,L/2)\); fixed finite \(S\),
distinct \(p,q\notin S\), \(\beta_j=2\sqrt j/(j+1)\), and
\(a_+=\log(pq)>a\). All four corners use the same source.

For every fixed finite \(A\) disjoint from \(S\), the finite Euler identity
and Note 02's compact transfer give
\[
B_{S\cup A}-B_S=-(W_{S\cup A}-W_S)+(K_{S\cup A}-K_S).
\tag{1}
\]
This is a bounded source form on \(L^2(I_L)\): a finite sum of compressed
translations plus a compact form. Differences of order at least two cancel
the additive arithmetic sum and are compact. Consequently every fixed
finite linear combination of place traces with coefficient sum zero is
bounded. It cannot equal the full Weil form of a fixed nonzero finite
translate combination: on the prepared modulations of Note 01 §4 the
latter grows like a positive multiple of \(\log\tau\), while the former
stays bounded. This confirms the review's simpler proof of that obstruction.

For one prime with \(\log p<L\), choose real nonnegative \(h\) with
\(\kappa_h(\log p)>0\), and put
\(F_\tau=\tau^{-2}(-\partial_x^2+1/4)(e^{i\tau x}h)\).
The normalized transport \(J_p\) of Note 02 satisfies
\[
B_S[J_pF_\tau]-B_S[F_\tau]
=-\beta_p\kappa_h(\log p)\cos(\tau\log p)\log\tau+O(1).
\tag{2}
\]
Indeed its numerator difference is
\(-\beta_p\Re B_S(F_\tau,U_{\log p}F_\tau)\); polarize
\(B_S=\Gamma-W_S+K_S\) on the enlarged fixed support. The last two forms
are bounded, and the shifted gamma asymptotic is the calculation of Note
02 §3. Subtract (2) from the bounded place difference (1) to obtain
\[
Z_p[F_\tau]=\beta_p\kappa_h(\log p)
\cos(\tau\log p)\log\tau+O(1).
\tag{3}
\]
Thus the review's Proposition R1 holds on the prepared core, already at
first order. This is a consequence of the existing identities, rather than
an additional positivity mechanism.

## 2 Boundedness at and below the threshold

Write \(b=\beta_p\beta_q/2\). Note 02 (10) reads
\[
\mathcal R_{\rm met}=-\mathcal G_\Gamma+
\mathcal G_{W_S}+\mathcal C_L,\qquad
\mathcal C_L=\Delta_p\Delta_qK_S-\mathcal G_{K_S},
\tag{4}
\]
where \(\mathcal C_L\) is compact. Define
\(\mathcal A_L=\mathcal R_{\rm met}-\mathcal G_{W_S}\).
The subtraction is explicit arithmetic, independently defined in Note 02.

Taking the real part in [DLMF 5.9.16](https://dlmf.nist.gov/5.9.E16),
with \(z=1/4+it/2\), and taking the inverse Fourier transform away from
the diagonal gives
\[
g(u)=-\frac{e^{-|u|/2}}{1-e^{-2|u|}},\qquad
g(u)=-\frac1{2|u|}+r(|u|),\quad r(0)=-\frac14.
\tag{5}
\]
Here \(r\) extends continuously to zero. For normalization, the cosine
term is \(-e^{-v/4}\cos(tv/2)/(1-e^{-v})\); its inverse transform is
\(-\tfrac12[\delta(u-v/2)+\delta(u+v/2)]\) times the displayed weight.
The substitution \(v=2|u|\) gives (5), without an extra factor of two.
Terms supported at the diagonal do not contribute between disjoint
translated source intervals.

On \(I=(0,L)\), the Hermitian form
\(T_d[F]=\Re\Gamma(F,U_dF)\), for \(d\ge L\), has kernel
\[
t_d(x,y)=\tfrac12\{g(x-y-d)+g(x-y+d)\}.
\tag{6}
\]
It is smooth on the closed square if \(d>L\), hence Hilbert–Schmidt.
At \(d=L\), its only singularities are at the two opposite corners.
The kernel \(1/(x+y)\) on the positive half-line has norm at most \(\pi\):
weighted Schur with weight \(x^{-1/2}\) uses
\(\int_0^\infty y^{-1/2}/(x+y)\,dy=\pi x^{-1/2}\).
The integral follows directly by \(y=xt^2\). Reflection gives the same
bound for each corner of (6), uniformly as \(d\downarrow L\).

For an explicit bound set \(f(u)=e^{-u/2}/(1-e^{-2u})\).
Since \(f(u)\le 1+1/(2u)\),
\[
\|T_L\|\le\pi/2+L,\qquad
\|T_d\|\le Lf(d-L)\quad(d>L).
\]
Thus for \(L\le a\),
\[
\|\mathcal G_\Gamma\|
\le b\{\pi/2+L+Lf(a_+-L)\}<\infty.
\tag{7}
\]
Equations (4)–(7) prove boundedness of \(\mathcal R_{\rm met}\), including
equality. For \(L>a\), Note 02 (13) supplies normalized prepared sources
with arbitrarily large values of both signs. This proves the claimed
if and only if. The endpoint proof requires the corner estimate; it does
not assume a uniform positive gap between translated supports.

## 3 The endpoint is noncompact

At \(L=a\), let \((Rf)(x)=f(L-x)\) and
\((C_Lf)(x)=\int_0^L f(y)/(x+y)\,dy\). From (5)–(6),
\[
T_L=-\tfrac14(C_LR+RC_L)+\text{Hilbert–Schmidt},\qquad
\mathcal A_L=\frac{\beta_p\beta_q}{8}(C_LR+RC_L)+\text{compact}.
\tag{8}
\]
For \(0<d<L/2\), restrict to the two endpoint intervals of length \(d\)
and reflect the right one. Modulo a bounded square-integrable kernel,
\(C_LR+RC_L\) becomes
\(\left(\begin{smallmatrix}0&C_d\\C_d&0\end{smallmatrix}\right)\),
with a zero middle block. The omitted kernels have denominators bounded
away from zero.

Both the norm and essential norm of \(C_d\) are \(\pi\).
The upper bound is Schur's estimate above. For the lower bound, the unitary
change \(x=de^{-t}\), \(t>0\), turns its kernel into
\(k(t-s)=1/(2\cosh((t-s)/2))\). Normalized indicators of intervals
\([T,T+R]\) have Rayleigh quotient
\(\int_{-R}^R(1-|v|/R)k(v)\,dv\to\int_\mathbb R k=\pi\).
Taking \(R\to\infty\) and \(T\to\infty\) makes them weakly null;
every compact perturbation contributes zero. Therefore
\[
\boxed{\|\mathcal A_a\|_{\rm ess}=\frac{\pi\beta_p\beta_q}{8}>0.}
\tag{9}
\]
For \(L<a\), both kernels in \(\mathcal G_\Gamma\) are smooth, so
\(\mathcal A_L\) is compact. At equality the full metric remainder is
noncompact for every allowed \(S\): the finitely many shifts in
\(\mathcal G_{W_S}\) are none of \(0,\pm L\), by unique factorization
and \(p,q\notin S\). Their quadratic forms vanish on sufficiently small
paired endpoint supports. The symmetric and antisymmetric endpoint
sequences from (8) still give limits \(\pm\pi\beta_p\beta_q/8\).
In particular \(\|\mathcal R_{\rm met}\|_{\rm ess}\ge\pi\beta_p\beta_q/8\).

Below the threshold the full metric remainder need not be compact when
\(S\ne\varnothing\). For example take \(p=2,q=3,S=\{5\}\) and
\(\log(6/5)<L<\log(3/2)\). The arithmetic form has a nonzero compressed
translation by \(\log(6/5)\). A positive bump whose autocorrelation there
is nonzero, modulated to infinity, gives a nonzero finite trigonometric
polynomial of quadratic values. It cannot tend to zero, whereas the
compact terms do. Thus the compact statement below threshold belongs to
\(\mathcal A_L\), or to \(\mathcal R_{\rm met}\) when \(S\) is empty.

All boundedness, essential norm and noncompactness conclusions remain true
on the closed two-moment kernel. Its orthogonal projection differs from
the identity by rank two, so compression changes a bounded operator by
finite rank. Smooth prepared sources are dense there: correct any smooth
approximation with two fixed smooth bumps having independent moment
vectors, then use the canonical preparation characterization.

## 4 The leading return and a controlled remainder

Put \(x=\beta_p,y=\beta_q\), \(e_j=E_j/\beta_j\), and on
\(\mathcal K=\operatorname{Ran}P\) define
\[
A=Pe_pP,\ B=Pe_qP,\ C=Pe_pe_qP,\quad
\ell_p=N_p'-AN_0,\quad \ell_q=N_q'-BN_0,\quad
\ell_{pq}=N_{pq}'-CN_0,
\]
where \(N_j'=V^*e_jV\), \(N_{pq}'=V^*e_pe_qV\), and
\(B_0=\operatorname{Tr}N_0=B_S[F]\). Set
\(K_0=\ell_{pq}-B\ell_p-A\ell_q\) and
\(R=(I+xA+yB+xyC)^{-1}\). Note 01 (10) gives exactly
\[
\mathfrak M=xy\operatorname{Tr}R\left[
K_0-x(C-BA)(I+xA)^{-1}\ell_p
-y(C-AB)(I+yB)^{-1}\ell_q\right].
\tag{10}
\]
For instance
\((B+xC)(I+xA)^{-1}=B+x(C-BA)(I+xA)^{-1}\);
the order of factors is retained. Hence
\[
\mu_2=\operatorname{Tr}K_0
=\operatorname{Tr}\{Pe_q(I-P)e_p(I-P)A_FP
-(Pe_pP)(Pe_q(I-P)A_FP)\}.
\tag{11}
\]
The double-return term is trace class as
\(\ell_{pq}-B\ell_p\), not by assuming \(A_FP\) trace class.
The expression is symmetric in \(p,q\), as is \(K_0\).

Each defect has trace norm at most \(2B_0\), and
\(\|C-BA\|,\|C-AB\|\le1\). In fact \(\|K_0\|_1\le4B_0\): expand it as
\(N_{pq}'-BN_p'-AN_q'+(BA+AB-C)N_0\).
The first three terms cost \(B_0\) each; the final coefficient is a
selfadjoint contraction because
\[
\langle v,(BA+AB-C)v\rangle
=\Re\langle e_pv,(2P-I)e_qv\rangle.
\]
With \(g=(1-x)(1-y)\), \(\|R\|\le g^{-1}\) and
\(\|R-I\|\le(x+y-xy)/g\). Therefore
\[
\boxed{|\mathfrak M-xy\mu_2|
\le\frac{xyB_0}{g}\left[4(x+y-xy)+\frac{2x}{1-x}+\frac{2y}{1-y}\right].}
\tag{12}
\]
This gives the review's cubic expansion uniformly for any commuting
selfadjoint contractions \(e_p,e_q\). It is a small-weight expansion;
along actual growing primes the translations also change, and the
coefficient need not converge. The same calculation yields
\[
|\mathfrak M|\le\frac{2xy}{g}
\left(\frac1{1-x}+\frac1{1-y}\right)B_S[F].
\tag{13}
\]
This improves the review's leading generic constant from \(6xy\) to
\(4xy\). It still holds in the tilted two-dimensional sign control, so
it supplies no actual-Sonin sign premise. The balanced control has
\(\mu_2=0\); the tilted control has either sign as the review states.

## 5 Disposition and the next decision

The first-order statement, sharp threshold, original generic bound and
coefficient in the review are correct. Equations (9) and (12) sharpen the
endpoint and remainder. The original seven-section review program replays
with no failures; the [round-two exact check][checks] tests (10)–(13)
against direct finite-model corners, including a dropped-return control.
These finite models check algebra, not the actual Sonin projection.

The review's fixed-window argument establishes that the decomposition adds
no information by itself. It does **not** establish that every sharper
mixed estimate is useless. If a known bound for
\(K_S+\Delta_pK_S+\Delta_qK_S\) is \(r\), and a new signed actual-Sonin
bound is \(\mathfrak M\le m\), then \(r+m\) could improve an existing
bound for \(K_{S\cup\{p,q\}}\). No such improving pair \((r,m)\) is
supplied here. The review's numerical conditioning costs are costs of the
recorded gap bounds, not universal lower bounds on every method.

Accordingly the opening algebraic route is closed without a phase-three
enclosure campaign. Further developing work requires a declared residual
budget and a signed estimate that improves it, or an actual-Sonin return
cancellation absent from the tilted control. The all-support inequality
\(K_{S_L}\le B_{S_L}\) remains the original target ([avoid 01][a01]).
No universal exclusion of collective prime estimates follows.

The [collision screen][s12] has the same scope as in Note 01: the generic
control lacks the actual Sonin projection; Euler-factor controls change
the arithmetic family; weighted-square controls lack full reflection;
reflected controls lack integer-square support; smooth/primitive controls
lack the full theta arithmetic. None of the conclusions above asserts
heat-flow noncollision from their shared shape properties.

[review]: ../../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md
[n02]: ../round-1/02_CORRECTED_SIGNED_WEIL_GRAM_AND_MIXED_SOURCE_ESTIMATES_CODEX_20261017.md
[checks]: ../../numerics/round-2/README.md
[results]: ../../../../../result-summaries/README.md
[s07]: ../../../../../result-summaries/07_sonin_critical_boundary.md
[s12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
