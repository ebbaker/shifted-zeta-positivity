# Angular gluing and source rigidity review seeds

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6-astra` (Codex); reasoning effort **ultra**, verified from the
recorded session. Parallel internal assessments used the same configuration;
they are not independent specialist or formal validation.

This note sharpens the [initial program](INITIAL_RESEARCH_PROGRAM_20261013.md).
It derives a balanced angular lift, identifies a redundant low angular jet,
and isolates the role of exact lattice preparation. The formulas are internal
analytic derivations from classical theta identities. No new theta sign or
collision exclusion is obtained.

## An exact balanced lift

Use the entire angular theta series at positive real scale,
\[
\Theta(r,y)=\sum_{n\in\mathbb Z}e^{-\pi n^2r+2\pi iny},
\quad F(u,z)=e^{u+\pi z^2/2}\Theta(e^{4u},e^{2u}z),\quad u\in\mathbb R.
\]
[Jacobi inversion](https://dlmf.nist.gov/20.7.E32), in this convention, is
\[
\Theta(r,y)=r^{-1/2}e^{-\pi y^2/r}\Theta(r^{-1},-iy/r).
\]
Substitution gives \(F(u,z)=F(-u,-iz)\). Here \(z\) is a balanced angular
coordinate, not the spectral variable denoted by \(z\) in the initial note.
All \(u\)-derivatives below hold this new angular coordinate fixed.

Set
\[
M(u,z)=\frac{(\partial_u^2-1)F(u,z)}{16}.
\]
Then \(M(u,z)=M(-u,-iz)\). At \(z=0\), the difference between
\(F(u,0)\) and the old zero-subtracted \(k(u,0)\) is \(e^u\), which
is killed by the insertion. Thus \(M(u,0)=\Phi_e(u)\).

For \(u\to+\infty\) and \(|z|\le Z\), nonzero summands have absolute
exponential factor at most
\[
\exp(-\pi n^2 e^{4u}+2\pi |n|e^{2u}Z)
\le \exp(-\tfrac\pi2 n^2e^{4u})
\]
for all sufficiently large \(u\), uniformly for \(|n|\ge1\).
Differentiation adds polynomial factors in \(n,e^{2u},z\) that the
same type of decay absorbs. The zero-mode term \(e^{u+\pi z^2/2}\)
is annihilated exactly. Reflection supplies the negative tail with \(-iz\)
in the same compact disk. Hence
\[
K_t(x,z)=\frac12\int_{\mathbb R}e^{tu^2+ixu}M(u,z)\,du
\]
converges locally uniformly, together with every fixed derivative, for
complex \(t,x,z\). It is entire in those parameters and satisfies
\[
\partial_tK=-\partial_x^2K,\qquad K_t(x,0)=H_t(x),
\qquad K_t(x,z)=K_t(-x,-iz).
\]
The heat weight commutes with this reflection because \(u^2=(-u)^2\).
Ordinary Jacobi heat in scale and angle remains a different evolution.
No positivity for the inserted angular field \(M\) has been asserted.

## The first angular jet is not an anchor

Let \(h(u)=e^u\Theta(e^{4u},0)\). Direct termwise differentiation gives
\[
[z^2]F=\frac\pi2 h'(u),\qquad
[z^2]M=\frac\pi2\Phi_e'(u).
\]
Indeed the coefficient from the theta series is
\(-2\pi^2e^{5u}\sum n^2e^{-\pi n^2e^{4u}}\), and the gauge adds
\(\pi h/2\); their sum is \(\pi h'/2\).
Integration by parts, with both tails just established, now gives
\[
[z^2]K_t=\frac\pi4\int e^{tu^2+ixu}\Phi_e'(u)\,du
=\frac{i\pi}{2}(2tH_x-xH).
\]
This coefficient vanishes at a joint zero. Reflection symmetry by itself,
and this first angular Taylor coefficient, therefore do not provide the
independently nonzero source quantity sought in direction 03.

## Keep the elliptic lattice law

With \(\ell(u)=e^{-2u}\), the real angular period gives
\[
F(u,z+\ell(u))=
 e^{\pi\ell(u)z+\pi\ell(u)^2/2}F(u,z).
\]
Transporting this relation through \(\partial_u^2-1\) is a concrete next
task. It must include \(\ell'=-2\ell\), angular derivatives, and the
derivatives of the gauge. It cannot be obtained by treating the translating
period as constant. This law retains integer lattice information that is
absent from scalar reflection.

A complementary exact test uses the imaginary quasiperiod. Suppose
\(\Theta_c(r,y)=\sum_{n\in\mathbb Z}c_ne^{-\pi n^2r+2\pi iny}\)
converges normally at the arguments below. The
[classical elliptic law](https://dlmf.nist.gov/20.2.E8) has defect
\[
E_c(r,y)=e^{-\pi r}\{\Theta_c(r,y+ir)
-e^{\pi r-2\pi iy}\Theta_c(r,y)\}
=\sum_n(c_n-c_{n+1})e^{-\pi(n+1)^2r}e^{2\pi iny}.
\]
Fourier uniqueness shows that \(E_c\equiv0\) forces every \(c_n\)
to be the same. The anchor \(c_0=1\) selects actual theta. Parseval gives
\[
\int_0^1|E_c(r,y)|^2dy
=\sum_n|c_n-c_{n+1}|^2e^{-2\pi(n+1)^2r}.
\]
Exact rigidity and quantitative observation control are different. At one
fixed \(r\), this defect norm allows increasingly weak bounds on high-index
coefficient differences. An approximate-gluing certificate must pay those
weights, its cutoff and its angular continuation; a tiny residual alone
is not a uniform rigidity estimate.

## Nearby positive sources still permit distant collisions

This is a useful test of any proposed robust implication from positivity,
real-line closeness and scalar reflection alone. Fix \(T>0\), and write
\(H=H_T\) for the genuine source. Its positive density implies
\(H(0)>0\), \(H''(0)<0\). Choose small \(d>0\) so that
\(h=H(d)>0\) and \(p=H'(d)<0\). For large \(X>d\), consider
\[
\widetilde\Phi_X(u)=s_X\Phi_e(u)
\{1+a_X\cos((X-d)u)+b_X\cos((X+d)u)\}.
\]
Before the positive normalization \(s_X\), the value and slope at
\((T,X)\) vanish exactly when
\[
\frac12
\begin{pmatrix}
H(2X-d)+h&H(2X+d)+h\\
H'(2X-d)+p&H'(2X+d)-p
\end{pmatrix}
\binom{a_X}{b_X}=-\binom{H(X)}{H'(X)}.
\]
The heat-weighted theta density and its polynomial insertions are integrable,
so their Fourier transforms tend to zero along the real axis. The displayed
matrix tends to \(\tfrac12\left(\begin{smallmatrix}h&h\\p&-p\end{smallmatrix}\right)\),
whose determinant is \(-hp/2\ne0\). Thus for all sufficiently large \(X\)
the system has a solution with \(a_X,b_X\to0\). In particular
\(|a_X|+|b_X|<1\), ensuring strict positivity of the perturbed density.

Choose \(s_X>0\) to restore
\(\int_0^\infty\cosh u\,\widetilde\Phi_X(u)du=1/16\).
Then \(s_X\to1\), and the density converges to genuine theta in relative
supremum norm on the real \(u\) axis. Each perturbed density is even,
positive and admits every fixed Gaussian weight. Its heat transform is
entire, nonzero at \(x=0\), and has a finite-multiplicity joint zero at
\((T,X)\). Exact multiplicity two is not needed or claimed here.

The upstream [Green-kernel construction](../../../../quasi-rh-exponent-descent/newman_collisions/06_theta_lattice/notes/2_GREEN_KERNEL_ENDPOINT_EQUIVALENCE_AND_CONDITIONAL_JETS_20261010.md)
applied to \(\widetilde\Phi_X\) supplies all odd endpoint jets and scalar
reflection. These sources do **not** preserve the actual angular lattice
preparation, an all-real threshold, or the complete zeta counting law.
Nor is smallness claimed in a fixed complex-strip norm: rapidly oscillating
cosines behave differently off the real axis. This construction strengthens
the diagnostic that exact arithmetic/angular information, or a uniform
quantitative substitute, must enter any high-height exclusion argument.

## First continuation and stop rule

Derive the inserted variable-period law in the balanced chart and transform
it on a declared domain. Compare its information with the automatic scalar
jet hierarchy and with the positive deformations above. Continue for an
independent nonlocal source relation, a controlled angular positivity
statement, or a usable adjoint residual. If only scalar reflection,
source uniqueness, or the already redundant low jet remains, report that
bounded obstruction before extending the computation.

This note is a derivation and screening record. It performs no genuine-theta
numerical enclosure and proves no sign at a theta stationary point.
