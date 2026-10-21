# Differentiated saddle estimates and eventual gap shrinkage

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. Status: **proved in-note; same-assistant
self-review only**. No specialist review or simplicity exclusion.

For every fixed finite set of positive root labels, the proposed HMC-02
velocity asymptotics hold. In particular every fixed adjacent gap is
eventually strictly decreasing. The proof differentiates the complete
source integral and cancels its leading covariance against motion of the
rescaling. It does not differentiate an uncontrolled location remainder.
Explicit finite moment bounds below make the error and a sufficient
shrinkage test computable; no numerical onset has been certified.

This continues [Note 19][n19] and the [program][program]. The
[result index][results], [heat geometry][geometry] and [avoid index][avoid]
apply, especially [target classification][a01], [control premises][a02]
and [scoped conclusions][a07]. Root motion is a quantitative milestone;
eventual shrinkage is compatible with a multiple endpoint.

## 1. The complete source and the result

Use exactly \(H_t=-H_{xx}\) and the theta source of Note 19. As in
the [BW09 manuscript's complete theta section][bw09], write
\[
e^{tu^2}\Phi(u)=2\pi^2e^{q_t(u)}b(u),\qquad
q_t(u)=tu^2+9u-\pi e^{4u},
\]
\[
b(u)=\sum_{n\ge1}\left(n^4-\frac{3n^2e^{-4u}}{2\pi}\right)
 e^{-\pi(n^2-1)e^{4u}}.
\tag{DS1}
\]
All summands are positive on \(u\ge0\), and
\(1-3/(2\pi)\le b\le C_b^*=1/(1-16e^{-3\pi})\).
Let \(L=L_t\) be the large stationary point and put
\[
4\pi e^{4L}=2tL+9,\quad \kappa=8tL-2t+36>0,
\quad L'=2L/\kappa.
\tag{DS2}
\]
The inherited limits \(L\sim(\log t)/4\), \(\kappa\sim8tL\)
will also follow from this equation in the range used below.
Define the complete probability law and real profile
\[
d\mu_t(u)=\frac{e^{tu^2}\Phi(u)}{H(t,0)}\,du,
\quad F(t,z)=\mathbb E_t\cos(zU/L).
\]
Fix \(K\), let \(s_j=(j-1/2)\pi\), and let \(x_j(t)\) be the
first \(K\) positive roots at large time. Then
\[
x_j'=-s_j\frac{L'}{L^2}
 +O_K\!\left(\frac1{L\kappa^{5/4}}\right),\qquad 1\le j\le K.
\tag{DS3}
\]
In particular, for each fixed \(k\),
\[
g_k'=-\pi\frac{L'}{L^2}
 +O_k\!\left(\frac1{L\kappa^{5/4}}\right),\qquad
c_k'=-k\pi\frac{L'}{L^2}
 +O_k\!\left(\frac1{L\kappa^{5/4}}\right).
\tag{DS4}
\]
The error is smaller than the leading scale \(L'/L^2=2/(\kappa L)\).
The late-time existence, simplicity, rank identification and estimates
are unconditional for these first finitely many roots. **RH is used
when identifying them with the fixed positive root walls continued
from a hypothetical multiple zero at time zero.** No assertion is
uniform over growing labels or growing event heights.

## 2. Exact differentiation and the cancellation

Put \(V=U-L\), \(m_p=\mathbb E|V|^p\), and
\(v_2=\operatorname{Var}(V)\). All the following estimates are for
real \(|z|\le Z\), with fixed \(Z\). Complete source decay justifies
differentiation under both the numerator and normalization integrals on
each compact heat-time interval. The exact identity is
\[
\partial_tF=\operatorname{Cov}(U^2,\cos(zU/L))
 +\frac{zL'}{L^2}\mathbb E[U\sin(zU/L)].
\tag{DS5}
\]
The second term is essential. Taylor expansion of the observable, with
global real remainder,
\[
\cos(z+zV/L)=\cos z-(z/L)\sin z\,V+\mathcal R,
\qquad |\mathcal R|\le z^2V^2/(2L^2),
\]
gives
\[
\operatorname{Cov}(U^2,V)=2Lv_2+
\mathbb E V^3-\mathbb E V^2\mathbb E V.
\]
The leading covariance is therefore \(-2z\sin z\,v_2\).
The leading rescaling term is \(z\sin z\,L'/L=2z\sin z/\kappa\).
Their cancellation yields the finite bound
\[
|\partial_tF(t,z)|\le\mathcal D_Z(t):=
2Z|v_2-\kappa^{-1}|
+\frac{Z(1+Z)}L(m_3+m_1m_2)
+\frac{Z^2}{2L^2}(m_4+m_2^2)
+\frac{2Z(1+Z)}{\kappa L}m_1.
\tag{DS6}
\]
To verify every remainder, use
\[
|\operatorname{Cov}(U^2,\mathcal R)|\le
\frac{Z^2}{2L^2}\{2L(m_3+m_1m_2)+m_4+m_2^2\},
\]
and
\( |\mathbb E[U\sin(zU/L)]-L\sin z|\le(1+Z)m_1\).
Thus no derivative of a probabilistic error estimate has been assumed.
The inherited all-moment Gaussian limit already implies
\(\mathcal D_Z=o(\kappa^{-1})\). The next section gives a finite,
explicit version, and the coarse rate used in DS3.

## 3. Explicit moment and variance errors for all source tails

The purpose here is an effective sufficient bound, not an optimized
Laplace expansion. Set
\[
\delta=1/4,\quad c=1/(4e),\quad h=\kappa^{1/12},
\]
and require the finite conditions
\[
L\ge\delta,\quad\kappa\ge32,\quad t/\kappa\le1/(4e),
\quad q_t(L-\delta)\ge q_t(0).
\tag{DS7}
\]
They hold for all sufficiently large \(t\). Define
\[
Q=16\exp[-3\pi e^{4(L-\delta)}],\quad
d_L=\frac3{2\pi}e^{-4(L-\delta)}+\frac Q{1-Q},
\]
\[
\eta=\frac{4e}{3}\kappa^{-1/4},\qquad
\varepsilon=e^\eta(1+d_L)-1,
\quad G_p=\int_{\mathbb R}|w|^pe^{-w^2/2}\,dw.
\]
Here \(Q<1\) follows already from \(L\ge\delta\). For
\(p=0,1,2,3,4\), define the entirely explicit error allowance
\[
\begin{split}
\Delta_p={}&\varepsilon G_p+
\int_{|w|>h}|w|^p
 \left(C_b^*e^{-cw^2}+e^{-w^2/2}\right)dw\\
&+C_b^*(L\sqrt\kappa)^{p+1}e^{-c\kappa\delta^2}.
\end{split}
\tag{DS8}
\]
The one-dimensional Gaussian tails can equivalently be written using
incomplete gamma functions. They are not truncated theta integrals.

If \(\Delta_0<G_0=\sqrt{2\pi}\), set
\[
M_p=\kappa^{-p/2}\frac{G_p+\Delta_p}{G_0-\Delta_0}
\quad(p=1,2,3,4),
\]
\[
\nu=\frac{\Delta_2+\Delta_0}{G_0-\Delta_0}
+\left(\frac{\Delta_1}{G_0-\Delta_0}\right)^2.
\tag{DS9}
\]
Then
\[
m_p\le M_p,\qquad |\kappa v_2-1|\le\nu.
\tag{DS10}
\]
Substitute \(M_p\) for \(m_p\) and \(\nu/\kappa\) for
\(|v_2-1/\kappa|\) in DS6 to obtain the computable bound
\(\widehat{\mathcal D}_Z\).

**Proof of the complete allowances.** With \(A=\pi e^{4L}\),
\[
q_t(L+v)-q_t(L)=tv^2-A(e^{4v}-1-4v).
\tag{DS11}
\]
On \(v\ge0\) this is at most \(-\kappa v^2/2\). On
\(-\delta\le v\le0\), it is at most \(-c\kappa v^2\): use
\(e^{4v}-1-4v\ge8e^{-1}v^2\),
\(8A=(\kappa+2t)/2\), and DS7. On \([0,L-\delta]\),
\(q_t\) has no interior maximum: its derivative has at most a
local-minimum zero before the selected maximum at \(L\), since
\(q_t''\) strictly decreases. DS7 then bounds this whole region by
\(q_t(L-\delta)\le q_t(L)-c\kappa\delta^2\).

On the central region \(|w|\le h\), \(v=w/\sqrt\kappa\) obeys
\(|v|\le\delta\). Taylor's third-order remainder and
\(A\le\kappa/8\) give
\[
\left|q_t(L+w/\sqrt\kappa)-q_t(L)+w^2/2\right|
\le\frac{4e}{3}\frac{|w|^3}{\sqrt\kappa}\le\eta.
\]
The full source series DS1 satisfies \(|b(u)-1|\le d_L\) for
\(u\ge L-\delta\): retain the first-mode correction, and bound
every \(n\ge2\) term by the geometric series with ratio \(Q\).
It follows that the rescaled unnormalized density
\[
B_t(w)=e^{q_t(L+w/\sqrt\kappa)-q_t(L)}
b(L+w/\sqrt\kappa)\,\mathbf1_{w\ge-L\sqrt\kappa}
\]
differs from \(e^{-w^2/2}\) by at most
\(\varepsilon e^{-w^2/2}\) centrally. The remaining near/right
region has bound \(C_b^*e^{-cw^2}\); the far-left region has
length at most \(L\sqrt\kappa\) and the exponential bound above.
These are precisely the three terms in DS8, including the Gaussian
mass outside the source's half-line. Thus both absolute moment
integrals and signed moment integrals differ from their Gaussian
values by at most \(\Delta_p\).

The normalization is at least \(G_0-\Delta_0\). Gaussian odd
mean zero gives \(|\mathbb Ew|\le\Delta_1/(G_0-\Delta_0)\);
Gaussian second moment \(G_2=G_0\) gives
\(|\mathbb Ew^2-1|\le(\Delta_2+\Delta_0)/(G_0-\Delta_0)\).
Subtract the squared mean to prove DS10.

Finally \(d_L=O(\kappa^{-1})\), since DS2 gives
\(e^{-4L}=16\pi/(\kappa+2t)\). Gaussian tails at
\(h=\kappa^{1/12}\) and the far-left exponential dominate the fixed
moment powers. Hence
\[
\Delta_p=O_p(\kappa^{-1/4}),\quad
M_p=O_p(\kappa^{-p/2}),\quad\nu=O(\kappa^{-1/4}),\quad
\widehat{\mathcal D}_Z=O_Z(\kappa^{-5/4}).
\tag{DS12}
\]
This bound retains every theta index, both source tails, and the
normalization error. No analytic result from the manuscript's Gevrey
approximation or normalized arithmetic heat sections is used.

## 4. Spatial enclosures and differentiated root estimates

The complete real estimates are
\[
|F-\cos z|\le\epsilon_0:=ZM_1/L,\qquad
|F_z+\sin z|\le\epsilon_1:=(1+Z)M_1/L,
\]
\[
|F_{zz}+\cos z|\le\epsilon_2:=(2+Z)M_1/L+M_2/L^2.
\tag{DS13}
\]
Fix \(0<\beta<\pi/4\), choose \(Z=s_K+\beta\), and require
\(\epsilon_0<\sin\beta\), \(\epsilon_1<\cos\beta\), in
addition to DS7 and \(\Delta_0<G_0\). On every interval
\([s_j-\beta,s_j+\beta]\) the endpoint signs and a derivative
floor give exactly one simple root \(z_j=Lx_j\). The intervening
compact intervals from zero through \(s_K+\beta\) contain no roots,
because \(|\cos z|\ge\sin\beta\) there. This proves the ranks.
Moreover, with \(d=\cos\beta-\epsilon_1>0\),
\[
|z_j-s_j|\le\arcsin\epsilon_0,\qquad
|z_j'|\le\widehat{\mathcal D}_Z/d.
\]
Implicit differentiation, at the actual root, now gives the finite error
\[
\left|x_j'+s_j\frac{L'}{L^2}\right|\le
\mathcal E_K(t):=\frac{L'}{L^2}\arcsin\epsilon_0
+\frac{\widehat{\mathcal D}_Z}{Ld}.
\tag{DS14}
\]
For a pair use \(K=k+1\). Its gap-velocity error is at most
\(2\mathcal E_K\); its center-velocity error is at most
\(\mathcal E_K\). Equations DS12–DS14 prove DS3–DS4.
A sufficient finite test for strict gap shrinkage is
\[
2\arcsin\epsilon_0+\frac{\kappa\widehat{\mathcal D}_Z}{d}<\pi.
\tag{DS15}
\]
All quantities in this test are explicit functions of \(t,L_t\) and
the chosen finite label range. A certified numerical onset would need
outward evaluation of these conditions; none is claimed here.

## 5. Consequences and control comparison

Under RH, a hypothetical double-born positive adjacent pair opens as
\(g\sim\sqrt{8t}\), stays positive at every finite positive time,
and is strictly decreasing after a sufficiently large time with
\(g\sim\pi/L_t\). This is a consistent trajectory. DS4 does not
force a finite collision, a phase surplus, or a regular limiting jet.
For a higher-order birth, every selected fixed adjacent pair has the
same late-time conclusions, but Note 19's singular cluster terms must
be retained near zero. The outer cluster has the sum of its adjacent
widths and leading velocity \(-(m-1)\pi L'/L^2\).

The [control register][controls] applies separately to each assertion:

| Control | Relevant response |
| --- | --- |
| Quadratic/Hermite heat polynomials | Their roots grow like \(\sqrt t\). They fail the complete continuous theta saddle hypotheses, and check only the local dynamics and normalization. |
| \(1+e^t\cos x\) | Its gap increases to \(\pi\). Its source is atomic and has no moving theta saddle, so it does not contradict DS4. |
| Euler factor \(c=1\) | Its shifted source changes DS1 and its numerical allowances. Generic root motion still survives; no unchanged-source claim is assigned to it. |
| Weighted-square/finite-prime controls | They fail full reflection and do not supply all-real root continuation. Finite-source mass also has different late-time concentration. |
| Reflected/positive-primitive controls | The original theta series and the specific bounds DS7–DS10 are absent. The heat covariance identity itself remains generic. |
| Note 05's close positive endpoint controls | Their preserved leading tail can give the same qualitative saddle concentration and covariance cancellation, using bounds for their own source. They retain multiple endpoints. Thus eventual shrinking is not a separating arithmetic estimate. They fail ordinary Dirichlet arithmetic. |

HMC-02's differentiated fixed-label theorem and finite error bounds are
complete at this internal checkpoint. HMC-03 has Note 19's finite-time
width estimate, but no enclosed turning time or sharp maximum-gap
estimate. HMC-04's moving geometric trace and HMC-05's additional signed
theta estimate remain open. The [review][review] checks these distinctions.

[n19]: 19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[program]: ../research-overview/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRAM_20261021.md
[bw09]: ../../09_expanding_contour_later_collision/manuscript/main.tex
[review]: ../reviews/19_ROOT_MOTION_AND_DIFFERENTIATED_SADDLE_REVIEW_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[geometry]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
