# Coordinate invariance and implicit heat folds

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort is unavailable to this session
and is not inferred. Derivations and parallel audits are internal LLM work,
not independent mathematical validation.

## 1. What a chart can change

The question is whether a coordinate system that sees a nonzero lifted
component can exclude a zero of the original value and physical slope.
For a passive state change \(\widetilde q=Tq\), the same observation is
\(\widetilde C=CT^{-1}\), so \(\widetilde C\widetilde q=Cq\).
If the slope is calculated by differentiating a position-dependent basis,
the derivative of \(T\) must also be included. Selecting a different
visible component is a different observation and requires a relation back
to \((H,H_x)\).

There is a corresponding geometric invariant. Consider an invertible
time-preserving local change \(s=\varphi(t)\), \(y=\psi(t,x)\), and a
nonzero scalar normalization \(a(t,x)\). With
\(G(s,y)=a(t,x)H(t,x)\),
\[
G=0,\qquad G_y=a x_y H_x=0
\]
at a joint zero. Multiplicity in a physical time slice is preserved. A
chart mixing time and height can give a nonzero new partial derivative,
but the physical vector \(\partial_x|_t\) transforms with that chart.
The statement \(H=\partial_x|_t H=0\) remains invariant.

These observations do not exclude a useful chart argument. They identify
its missing step: a theta-specific estimate must restrict the actual
observation, or the orientation of the zero set relative to the physical
time slices. An atlas in which some lifted component is visible does not
by itself provide that restriction.

## 2. The ordinary double is a regular fold

Let \(H_t=-H_{xx}\) be real analytic near \((T,a)\), and suppose
\(H=H_x=0\), \(A=H_{xx}\ne0\). All jets below are evaluated at that
point. Since \(H_t=-A\ne0\), the implicit function theorem gives the
zero set as \(t=T+\tau(x-a)\). Write
\(B=H_{xxx}\), \(C=H_{xxxx}\). Direct differentiation gives
\[
\tau(0)=\tau'(0)=0,\qquad
\tau''(0)=1,\qquad
\tau'''(0)=-2B/A,\qquad
\tau''''(0)=8(B/A)^2-2C/A.
\tag{1}
\]
Thus the zero set is already smooth in the time-height plane. Its
projection onto time has a nondegenerate fold, with leading equation
\(t-T=(x-a)^2/2\). The two zero trajectories have a square-root
singularity when parametrized by time. Straightening the zero curve
changes its description; it does not remove the tangency to a physical
time slice.

The map \(J=(H,H_x)\) has the full Jacobian, with columns \((t,x)\),
\[
DJ=\begin{pmatrix}-A&0\\-B&A\end{pmatrix},\qquad
\det DJ=-A^2\ne0.
\tag{2}
\]
The inverse function theorem therefore makes the joint zero isolated in
the plane. Invertibility of this full Jacobian is compatible with a joint
zero; it is not a nonvanishing theorem for either observation.

For completeness, formal heat Taylor expansion gives the next two jets,
with \(r_j=H_j/H_2\):
\[
\tau^{(5)}=-40r_3^3+10r_3r_4+6r_5,
\qquad
\tau^{(6)}=240r_3^4-20r_3^2r_4-116r_3r_5+16r_6.
\]
The formal calculation has been checked internally through degree six.
The manuscript only uses (1).

## 3. Recasting the existing threshold test

At a positive all-real ordinary-double threshold with \(a>0\), the
[parent deflated mirror inequality](../../newman_collision_reductions.tex)
is
\[
2B^2-3AC-gA^2\ge0,\qquad g=9/a^2.
\]
A stronger density input replaces \(g\) by its already established
larger coefficient. Equation (1) rewrites the same test as
\[
3\tau''''-5(\tau''')^2\ge2g.
\tag{3}
\]
Alternatively, let \(x=\chi(t)\) be the critical branch defined by
\(H_x(t,\chi(t))=0\), and let \(v(t)=H(t,\chi(t))\). Then
\[
\chi'=B/A,\quad v'=-A,\quad v''=C-B^2/A,
\qquad
\frac{v''}{v'}\ge\frac{(\chi')^2}{3}+\frac g3
\tag{4}
\]
at the threshold. A genuine theta upper bound strictly below (3) or (4)
would contradict an ordinary threshold collision. These are geometric
versions of the existing fourth-jet test. They neither remove its
fourth-derivative cost nor handle higher multiplicities automatically.
The ratios also require a lower bound for \(|A|\), which can worsen
numerical stability. The universal curvature \(\tau''=1\) contains no
theta-specific information.

Even a spatial Morse chart can make the zero graph exactly parabolic:
\(y=h\sqrt{2\tau(h)/h^2}\) gives \(t-T=y^2/2\). Its third and fourth
graph jets vanish. However, if \(y=f(x)\) and
\(\widetilde H(t,y)=H(t,x)\), its heat equation is
\[
\widetilde H_t=-\alpha\widetilde H_{yy}
 -\tfrac12\alpha_y\widetilde H_y,\qquad \alpha=f_x^2.
\]
The physical metric coefficients now retain the information removed from
the graph jets. Applying (3) in the new chart while discarding these
coefficients would create a spurious contradiction. Equation (3) is
written in the original physical height coordinate.

## 4. A collision survives small changes to the source

Suppose \(H_\varepsilon=H+\varepsilon V+O(\varepsilon^2)\) is a smooth
perturbation of the heat source. From (2), the ordinary collision persists
at \((T_\varepsilon,a_\varepsilon)\), with
\[
T_\varepsilon'|_0=V/A,\qquad
a_\varepsilon'|_0=BV/A^2-V_x/A.
\tag{5}
\]
For the manuscript's positive Gaussian control, take
\(\Phi_\varepsilon=\Phi_{\rm ctrl}(1+\varepsilon f)\), where \(f\)
is even, smooth and bounded with suitable bounded derivatives. For
\(|\varepsilon|\|f\|_\infty<1\), this is still a positive even density
with a positive smooth Schwartz square-root wavefunction on a fixed
bounded time interval. Its heat and chord identities persist, and (5)
retains a local real collision near \((1/40,\sqrt6)\). This does not
preserve genuine theta arithmetic preparation, or assert that an
all-real threshold persists under every perturbation. It shows that local
purity, positivity and smooth chart regularity do not obstruct collisions.

## 5. Exact controls and higher multiplicity

For \(\Phi_{\rm ctrl}(u)=(16u^4+24)e^{-(1+1/40)u^2}\), put
\(K=(\sqrt\pi/2)e^{-3/2}\). At \((1/40,\sqrt6)\),
\[
A=48K,\qquad B=-48\sqrt6K,\qquad C=24K.
\]
Consequently \(\tau'''=2\sqrt6\), \(\tau''''=47\), and
\(3\tau''''-5(\tau''')^2=21\), exceeding the necessary mirror bound
\(18/a^2=3\). Regularity and the necessary curvature sign are both
compatible with the collision.

A second positive density is
\[
\Phi_4(u)=R(u)e^{-(1+1/40)u^2},\quad
R=256u^8+4096u^6+42240u^4+245760u^2+646080.
\]
The identity \(R e^{-u^2}=(-\partial_u^2-30)^4e^{-u^2}\) gives the
slice at \(t=1/40\)
\[
2H=\sqrt\pi e^{-x^2/4}(x^2-30)^4.
\]
It has quadruple zeros at \(\pm\sqrt{30}\), with \(H_{xxxx}=345600K_4\),
\(K_4=(\sqrt\pi/2)e^{-15/2}\). The ordinary-double Jacobian degenerates.
The leading local heat polynomial is
\(14400K_4[h^4-12s h^2+12s^2]\), where \(s=t-1/40\).
It splits into four simple real branches for small \(s>0\) and has no
local real branches for small \(s<0\). This control has a positive pure
lift on a bounded time interval; no global all-time theta or threshold
claim is made.

Odd multiplicity is also compatible with a positive even density. Take
\[
\Phi_3(u)=R_3(u)e^{-(1+1/40)u^2},\quad
R_3=256u^8+4736u^6+51840u^4+317760u^2+871680.
\]
Here \(R_3e^{-u^2}=(-\partial_u^2-30)^3(-\partial_u^2-40)e^{-u^2}\),
so at \(t=1/40\)
\[
2H=\sqrt\pi e^{-x^2/4}(x^2-30)^3(x^2-40).
\]
The zeros at \(\pm\sqrt{30}\) are exact triples and those at
\(\pm\sqrt{40}\) are simple. This bounded-time positive pure control
violates the second stationary sign on an earlier critical branch of
\(H_x\). It makes no global threshold or theta claim.

For an exact multiplicity \(m\), the leading scaled local solution is
\[
H(T+\epsilon^2,a+\epsilon z)
=\epsilon^m\frac{H_m}{m!}P_m(z)+O(\epsilon^{m+1}),\qquad
P_m(z)=\sum_j\frac{(-1)^j m!z^{m-2j}}{j!(m-2j)!}.
\]
These are the Hermite splitting polynomials. Their simple real roots
give the standard positive-time splitting. Applying the ordinary chart
to \(\partial_x^{m-2}H\) resolves a derivative zero, rather than the
original zero set. Lower-jet constraints still matter.

The [exact checker](../numerics/check_heat_transversality.py) verifies the
Gaussian double/triple/quadruple controls, Jacobian and fold identities, and even/odd heat
polynomial tests. It does not prove a theta sign or a parameter cover.

## 6. The useful next condition

[Note 5](5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md) develops
a different consequence of the implicit function theorem. Just before
an even-multiplicity collision, a real critical branch necessarily has
\(H H_{xx}>0\); for odd multiplicity, the corresponding statement holds
for \(H_x\). Two signs on the stationary sets therefore exclude every
multiplicity. This gives a precise theta target involving derivatives
through order three, with predecessor coverage and complete error
payments. Those signs remain unproved for the genuine theta state.

Primary context: [Polymath, Proposition 3.1](https://arxiv.org/html/1904.12438v2#S3),
for zero dynamics and Hermite splitting;
[Angenent's implicit function theorem notes](https://people.math.wisc.edu/~angenent/519.2016s/notes/IFT.html);
[DLMF Hermite series](https://dlmf.nist.gov/18.5.E13).
The local calculations above are derived explicitly, without a claim of
literature novelty.
