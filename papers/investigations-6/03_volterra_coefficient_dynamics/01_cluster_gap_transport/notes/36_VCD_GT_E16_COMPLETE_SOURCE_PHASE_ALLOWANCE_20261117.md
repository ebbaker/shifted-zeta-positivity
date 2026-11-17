# VCD-GT-E16 — Complete-source favorable-phase allowance

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance, chat0006. Executor dispatch
**gpt-6.1-sol / ultra**. Separate serving-model and effort metadata and
the lead's actual settings are unavailable.

**Proved in-note, pending separate internal assessment.** This is a
quantitative allowance failure for the class specified in [E16 r1][request]
and [B09 Decision17, §2][decision]. It extends [Note28, (7)][earlier] from
the zero-frequency atom to every measurable selection of favorable
cosine phases, with the discarded cosine replaced by \(-1\). The
classification is a scoped estimate under [classification01][classification].
See the [result index][results], [avoid index][avoid],
[controls12][controls], [premises02][premises], [scope07][scope],
[normalization08][normalization] and [joint estimates12][joint].
The [proof return][return] records the verified input pins.

## 1. Complete density at both time endpoints and at the origin

Write \(I=[0,1/2]\). Use [Note12, §1][oracle] with
\[
 r_m(u)=\pi m^2 e^{4u},\qquad
 \Phi(u)=e^u\sum_{m\ge1}\bigl(2r_m(u)^2-3r_m(u)\bigr)e^{-r_m(u)}
 \quad(u\ge0),
\]
and its even extension. For \(u\ge0\), \(r_m(u)\ge\pi>3/2\), so every
summand is positive. On every compact real \(u\)-interval, the complete
theta primitive \(p(u)=e^u\sum_{m\ge1} e^{-r_m(u)}\) and each
termwise derivative converge uniformly. Each differentiated summand has
the form \(e^u\) times a polynomial in \(r_m(u)\) times \(e^{-r_m(u)}\),
and \(r_m(u)\) has a positive lower bound proportional to \(m^2\)
on that interval. Direct differentiation gives
\((p''-p)/8=\Phi\) on the nonnegative half-line. Apply
\(\partial_u^2-1\) to the complete reflection identity
\(p(-u)-p(u)=\sinh u\). It gives exact evenness of \((p''-p)/8\)
on the real line, so the smooth even extension is precisely that
formula, including at zero. In particular all odd derivatives there
vanish.

For \(j\ge0\) and \(u\ge0\), the \(j\)-th derivative of the source
summand is \(e^u Q_j(r_m(u))e^{-r_m(u)}\), with
\(Q_0(r)=2r^2-3r\) and \(Q_{j+1}=(1-4r)Q_j+4rQ_j'\).
Thus \(\deg Q_j\le j+2\), and \(|Q_j(r)|\le C_j r^{j+2}\)
for \(r\ge\pi\). Use
\(r_m(u)=\pi e^{4u}+\pi(m^2-1)e^{4u}\) and
\(e^{4u}\ge1\) to obtain
\[
 |\Phi^{(j)}(u)|\le C_j' e^{(9+4j)|u|} e^{-\pi e^{4|u|}},
 \qquad
 C_j'=C_j\pi^{j+2}\sum_{m\ge1}m^{2j+4}e^{-\pi(m^2-1)}<\infty .
 \tag{1}
\]
Reflection proves the same estimate for \(u<0\). The bound at zero
follows from the convergent series.

Put \(Z_t=\int_{\mathbb R}\Phi(u)e^{tu^2}\,du\),
\(f_t(u)=\Phi(u)e^{tu^2}/Z_t\), \(a_k(u)=u^k f_t(u)\), and
\(m_k=m_k(t)=\int u^k f_t(u)\,du\). Then
\(0< Z_0\le Z_t\le Z_{1/2}<\infty\). For \(j,k\ge0\), each term
in \(\partial_u^j a_k\) is \(Z_t^{-1}\) times a polynomial in
\((u,t)\) times \(e^{tu^2}\Phi^{(i)}(u)\) for some \(0\le i\le j\).
Equation (1) bounds it uniformly for \(t\in I\) by a finite sum of
polynomial factors times \(e^{u^2/2+(9+4j)|u|-\pi e^{4|u|}}\).
All polynomially weighted \(L^1\) and \(L^\infty\) norms of these
derivatives are therefore bounded uniformly on \(I\). These majorants
also imply continuity in \(t\) by dominated convergence. On compact
complex \(z\)-sets, the extra factor \(e^{|\Im z||u|}\) and the
powers from \(z\)- and \(t\)-differentiation are integrable against the
same double-exponential decay. In particular the physical field
\(H_t(z)=\tfrac12\int \Phi(u)e^{tu^2}e^{izu}\,du\) satisfies
\(\partial_t H_t=-H_t''\), with one-sided derivatives available at
the slab endpoints. We use \(F_t=H_t/H_t(0)=\int f_t(u)e^{izu}\,du\)
slice-wise.

## 2. Positive product density and its uniform norms

Primes on \(F_t\) indicate spatial derivatives. In
\(P_t=2(F_t''')^2-3F_t''F_t''''\), the Fourier products are
absolutely integrable by the moments above. Symmetrizing their joint
weight gives exactly
\[
 \tfrac12 u^2v^2(3u^2-4uv+3v^2)
 =\tfrac12 u^2v^2\bigl(u^2+v^2+2(u-v)^2\bigr)\ge0 .
\]
Pushing this weight times \(f_t(u)f_t(v)\,du\,dv\) to \(s=u+v\)
gives the pointwise nonnegative density
\[
 \nu_t=3(a_4*a_2)-2(a_3*a_3),\qquad
 P_t(c)=\int_{\mathbb R}\nu_t(s)\cos(cs)\,ds .
 \tag{2}
\]
Here \(a_k(-u)=(-1)^k a_k(u)\) makes each convolution even and the
sine integral zero. Parity and Tonelli for the joint nonnegative
weight, or Fubini for the two convolutions, give
\[
 T_t:=\int\nu_t=3m_2m_4\ge
 \tau:=\frac{3(\int u^2\Phi(u)\,du)(\int u^4\Phi(u)\,du)}
                 {Z_{1/2}^{\,2}}>0 .
 \tag{3}
\]
The same source bounds give \(\sup_I T_t<\infty\).

Differentiating in the first factor of each convolution gives
\[
 \begin{aligned}
 \|\nu_t'\|_1
   &\le 3\|a_4'\|_1\|a_2\|_1+2\|a_3'\|_1\|a_3\|_1,\\
 \|\nu_t''\|_\infty
   &\le 3\|a_4''\|_\infty\|a_2\|_1
          +2\|a_3''\|_\infty\|a_3\|_1 .
 \end{aligned}                                                   \tag{4}
\]
Differentiation under each integral follows from bounded continuous
derivatives of the first factor and the integrable second factor.
Equation (1) bounds both right sides uniformly. Each convolution
tends to zero at both infinities by dominated convergence, since its
first factor is bounded and decays there. The even \(C^2\) density
has \(\nu_t'(0)=0\), and at the anti-diagonal it has value
\[
 \nu_t(0)
 =3\int a_4(u)a_2(-u)\,du-2\int a_3(u)a_3(-u)\,du
 =5\int u^6 f_t(u)^2\,du>0 .
 \tag{5}
\]
The coefficient in (5) is a density value. The exact line \(u+v=0\)
has zero mass, as in [Note28][earlier].

## 3. Optimal allowance and anti-diagonal band

For \(c\ge1\), let \(E\) be any measurable subset of
\(\{s:\cos(cs)\ge0\}\). The lower allowance of the packet is
\[
 L_E=-T_t+\int_E (1+\cos(cs))\nu_t(s)\,ds\le P_t(c).
\]
The inequality uses \(\cos(cs)\ge-1\) on the discarded domain.
The integrand in the retained addition is nonnegative on the
allowed set. Taking the entire set therefore attains the maximum
\(U_t(c)=\int\nu_t(s)g(cs)\,ds\), where the \(2\pi\)-periodic
function \(g\) equals \(\cos\theta\) at nonnegative cosine and
\(-1\) at negative cosine. Its mean is
\[
 \mu=\frac{2-\pi}{2\pi}=\frac1\pi-\frac12<0 ,
\]
since the positive cosine integral over a period is \(2\) and the
negative domain has length \(\pi\). The phase endpoints satisfy the
specified nonnegative-cosine convention and form a null set.

Take \(J(\theta)=\int_0^\theta (g(v)-\mu)\,dv\), with oriented
integration for negative \(\theta\). The full-period integral is
zero, so \(J\) is \(2\pi\)-periodic, bounded and locally absolutely
continuous. Integration by parts on a finite interval followed by
both endpoint limits gives
\[
 U_t(c)-\mu T_t=-\frac1c\int_{\mathbb R}\nu_t'(s)J(cs)\,ds,\qquad
 |U_t(c)-\mu T_t|\le\frac{C}{c},\qquad
 C=\|J\|_\infty\sup_{t\in I}\|\nu_t'\|_1<\infty.
 \tag{6}
\]
Indeed \(J(cs)\) has derivative \(c(g(cs)-\mu)\) almost everywhere,
the boundary product tends to zero, and (2) and (4) give absolute
integrability on both sides. By (3), whenever
\(c\ge\max(1,2C/(|\mu|\tau))\), every allowance satisfies
\(L_E\le U_t(c)\le-|\mu|\tau/2\) uniformly in \(t\). The norm
constants are finite and have not been numerically enclosed.

For fixed \(0<a\le\pi/2\), take \(L_a=L_{[-a/c,a/c]}\), a permitted
band including the endpoints at \(\pm\pi/(2c)\) when \(a=\pi/2\).
Set \(x=cs\). Evenness and the second-derivative bound imply
\(\left|\nu_t(x/c)-\nu_t(0)\right|\le
 \|\nu_t''\|_\infty x^2/(2c^2)\). This proves
\[
 \begin{aligned}
 L_a&=-T_t+\frac{2(a+\sin a)\nu_t(0)}{c}+R_{t,c,a},\\
 |R_{t,c,a}|&\le
 \frac{\sup_{t\in I}\|\nu_t''\|_\infty}{2c^3}
       \int_{-a}^{a} x^2(1+\cos x)\,dx .
 \end{aligned}                                                     \tag{7}
\]
Equation (5) gives a strictly positive first-order coefficient, with
a uniform lower floor from \(f_t\ge\Phi/Z_{1/2}\). The vanishing
linear term of the density at zero removes the order \(c^{-2}\)
contribution. These bounds apply across the complete closed time slab.

## 4. Averaging and use at a double

Let \(\lambda\) be a nonnegative probability measure on \((t,c)\)
supported on \(t\in I\), \(c\ge c_0\ge1\). This includes a
normalized time average along a measurable center choice \(c(t)\).
For jointly measurable choices of the retained sets, (6) gives
\[
 \int L_{E(t,c)}\,d\lambda(t,c)
 \le \int U_t(c)\,d\lambda(t,c)
 \le \mu\int T_t\,d\lambda(t,c)+C/c_0
 \le-|\mu|\tau+C/c_0 .
 \tag{8}
\]
It follows that a nonnegative normalized average of these lower
allowances stays strictly negative for sufficiently large \(c_0\),
even when the phase selections and the averaging measure depend on
the centers.

At a stipulated nondegenerate real double, \(F_t(c)=F'_t(c)=0\)
and \(F_t''(c)\ne0\). Write \(A(z)=F_t(z)/(z-c)^2\) locally.
Taylor coefficients give \(A(c)=F_t''(c)/2\),
\(A'(c)=F_t'''(c)/6\), and \(A''(c)=F_t''''(c)/12\). Thus the
double-slice curvature in [Note24, (2) and (5)][fourier] is
\[
 M=-K=\frac{(A')^2-AA''}{A^2}(c)
     =\frac{P_t(c)}{18F_t''(c)^2}.                                  \tag{9}
\]
Dividing a strictly negative lower allowance by this positive
denominator cannot certify \(M\ge0\). A proposed full-domain
certificate based on this allowance cannot pay its required high-center
double slice. The result concerns the allowance alone. The signs of
\(P_t\) and \(M\) remain open in this calculation, as does the
existence of a theta event there. Joint estimates that retain signed
information from negative phases fall outside this class.

On a counted physical heat tube the regular law is \(D'=2-4MD\);
it gives \(D'=2\) at \(D=0\), as derived in [Note12, §5][oracle].
In particular \(D=0\) cannot persist on any time interval. Equation (8)
is averaging of lower allowances for the numerator alone. The
two-point divided difference governs \(D\ne0\), with the vertical
average of the deflated logarithmic curvature for a conjugate pair
in [Note24, (3)][fourier]. Equations (8)–(9) supply no averaged
\(M\), no transport cost and no transfer away from the double slice.
Direct evaluation receives the same complete source, moment and
derivative norms, full phase information, normalized jets and any
independently acquired \(t,c,D\), count, collar and nondegeneracy data.
It can use the same identities and allowances. The calculation
establishes neither a computational advantage nor new zero coverage.

## 5. Documentary collision-control replay

The premise screen uses [controls12][controls], [B09 Decision17, §5][decision],
[Note24, §3][fourier] and [Note28, §4][earlier]. Shared positivity and
evenness permit the product identity under its integrability hypotheses.
A changed source can share the allowance failure. Each verdict below
keeps the source, endpoint or readout failure attached to its class.

| Control | Relevant premise and outcome |
| --- | --- |
| Euler-factor translates | The positive, smooth, even translated sources retain the physical equation. Their finite translates have double-exponential bounds with a changed exponent constant, so the allowance proof applies with their own norms. The Euler factor changes the unchanged theta Dirichlet series and exact square source. |
| Weighted-square, finite-source changes and finite-score controls | The weighted-square endpoints do not give the full unit-weight reflected theta source. The finite-source changes lack the unchanged coefficient sequence. Exact finite-score matches do not restore full reflection in the stated endpoint-defective classes, whose zeros escape every fixed horizontal strip. |
| Finite-prime orbit controls | Finite selected-prime compatibility and matched scores survive. Full source reflection fails in the documented construction. No fixed event location is inherited from the high-gap construction. |
| Reflected super-Gaussian | Even smooth positivity and full reflection survive. Integer-square arithmetic is absent, and the documented transform fails order at most one. |
| Smooth shape and positive-primitive controls | Smoothness, positivity and the specified primitive data survive. The canonical square expansion is absent. Their common strip and the theta two-point magnitude stay untested here. |
| Fixed-event atom and compact-profile controls | Atomic sources fail the smooth absolutely continuous hypothesis and can retain an atom at frequency zero. The compact continuous extensions still lack complete theta coefficients and full profile, and require their own derivative-norm check for (6)–(7). |
| RH-conditional normalized endpoint mergers | The controls retain their RH assumption and change ordinary Dirichlet-series arithmetic. Their added doubles supply neither a canonical double nor a high-center bound on the theta curvature. |
| Fixed-amplitude variable observation kernel and fractional profile | The variable kernel fails the literal cosine/Newman readout. The relaxed fractional profile lacks a complete integer-multiplicity divisor of a specified field. |
| Quadratic, quartic and identical-count fixed-slice controls | The polynomial fields fail boundedness on the real axis required of a finite positive Fourier source. The identical-count pair changes the theta field. Its positive Fourier source and common physical heat tube remain unpaid. |
| Gaussian-factor heat examples | Their order-two growth fails the order-at-most-one premise. The cited local curvature constructions do not establish the smooth nonnegative Fourier density needed for (2), (6) and (7). |
| Five-atom readout of Note24 | At \(c=\pi\), \(F''=1/6\), \(F'''=0\), and \(F''''=5/6\) give \(P=-5/12\) despite the real double and positive even masses. It fails absolute continuity and its added roots have height \(\operatorname{arcosh}2>1\). |
| Four-atom readout of Note24 | Its positive even measure is atomic, and its positive first undeflated Laguerre expression coexists with nonreal zeros. It supplies neither the smooth density required in (6)–(7) nor an estimate for the deflated quotient in (9). |
| Earlier counter-kernels \(q,q_{T,a}\) | Their positive even kernels and physical heat evolution coexist with the documented positive thresholds. They use a different source from the literal theta square series. [Counter-kernel summary][counter] |

The signed negative-phase remainder and the selected-pair near-field sign
remain separate questions. The next declared task for this return is
**[E] VCD-GT-E18 — Sol**, the separate internal assessment.

[request]: ../research-progress/handoffs/VCD-GT-E16-r1.md
[return]: ../research-progress/handoffs/VCD-GT-E16-r1-return.md
[decision]: ../brainstorm/notes/17_VCD_GT_B09_SOURCE_NEAR_FIELD_DECISION_20261117.md
[oracle]: 12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md
[fourier]: 24_VCD_GT_FOURIER_GROUPING_AND_DEFLATED_CURVATURE_20261116.md
[earlier]: 28_VCD_GT_E03_FOURIER_GROUPING_SCREENS_20261116.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[counter]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[avoid]: ../../../../../avoid/README.md
[classification]: ../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[normalization]: ../../../../../avoid/08_normalization_and_constant_slips.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
