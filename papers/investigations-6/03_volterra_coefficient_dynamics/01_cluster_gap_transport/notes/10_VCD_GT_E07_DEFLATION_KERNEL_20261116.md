# VCD-GT-E07 r1 — Deflated curvature at the collision scale

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Explicit helper dispatch
**gpt-6.1-sol / ultra**, as recorded in the frozen request. Separate
backend attestation and actual lead configuration are unavailable.

**Proved in-note for the local analytic model.** The physical corollary
is conditional on the fixed isolated event and the phase and norm
estimates of Notes03 and 06. This is an intermediate calculation of the
existing curvature functional under [pattern 01][a01].
[Frozen request][request] [B03 decision][decision] [Result index][results]
[Local collision geometry][geometry] [Control catalog][catalog]
[Avoid index][avoid] [Control screening][a02] [Scope][a07]
[Normalization][a08]

## 1. First variation at the moving pair

Fix real \(a\ne 0\), \(k=2/a\), and \(d^2=2s\). Write
\(Q_d(x)=x^2-d^2\), \(E(x)=e^{kx}\) and \(H_\epsilon=Q_d-\epsilon E\).
For \(|s|\le S\), choose two fixed radii \(R_0,R\) with
\(\sqrt{2S}<R_0<R\). On either circle \(Q_d\) has a uniform positive
modulus floor, so Rouché gives a common two-zero count inside both
for all sufficiently small complex \(\epsilon\). Let \(P_\epsilon\)
be the monic polynomial of the pair, \(U_\epsilon=H_\epsilon/P_\epsilon\),
and \(K_\epsilon\) the divided difference of \(U_\epsilon'/U_\epsilon\)
at this pair. Here primes on functions of \(x\) denote \(x\)-derivatives.
Write \(\oint_R^\ast=(2\pi i)^{-1}\oint_{|x|=R}\) with positive
orientation. The factorization and functional satisfy
\[
 m_j(\epsilon)=\oint_R^\ast x^j H_\epsilon'/H_\epsilon\,dx,\qquad
 P_\epsilon=x^2-m_1(\epsilon)x+\tfrac12(m_1(\epsilon)^2-m_2(\epsilon)),
 \qquad
 K_\epsilon=\oint_R^\ast \frac{U_\epsilon'/U_\epsilon}{P_\epsilon}\,dx .
 \tag{1}
\]
The moments make \(P_\epsilon\) holomorphic in \(\epsilon\), including
at double roots. In the last integral a double root evaluates the
derivative of \(U_\epsilon'/U_\epsilon\). Equivalently, \(H_\epsilon'/H_\epsilon\)
may be used as numerator, since \(P_\epsilon'/P_\epsilon^2\)
integrates to zero. These are the conventions of [Note04 §2][e02] and
[Note05 §3][e03].

At \(\epsilon=0\), \(P_0=Q_d\), \(U_0=1\), and \(m_1(0)=0\).
Differentiation and integration by parts give
\[
 \left.\partial_\epsilon m_j\right|_0
   =j\oint_R^\ast x^{j-1}\frac{E(x)}{Q_d(x)}\,dx,\qquad
 \left.\partial_\epsilon P_\epsilon\right|_0=-I_d(x),\qquad
 I_d(x)=\cosh(kd)+x\,\frac{\sinh(kd)}{d}.
 \tag{2}
\]
The residues are the interpolation coefficients for the values at
\(\pm d\). At \(d=0\) they give the Hermite interpolant \(1+kx\).
Set \(V_d=(E-I_d)/Q_d\), with its holomorphic values at the two
zeros. Differentiating the quotient on the circle yields
\(\left.\partial_\epsilon U_\epsilon\right|_0=-V_d\).
In (1) the zeroth-order \(x\)-logarithmic derivative vanishes, so
the first-order result is
\[
 \kappa_a(s):=\left.\partial_\epsilon K_\epsilon\right|_0
  =-\oint_R^\ast \frac{V_d'(x)}{Q_d(x)}\,dx .
 \tag{3}
\]
In particular, the perturbed two-zero factor contributes \(I_d\) to
the variation of the unit. Formula (3) evaluates that variation at
the unperturbed pair because the unperturbed unit is constant.

For \(d\ne0\), at a root \(r=\pm d\) the identity \(Q_d V_d=E-I_d\)
gives
\[
 V_d'(r)=\frac{E''(r)}{4r}
           -\frac{E'(r)-I_d'}{4r^2}.
\]
Taking the divided difference of these values cancels \(I_d'\).
Writing \(C_a(s)=\cosh(kd)\) and now using \(C_a'=dC_a/ds\) gives
\[
 \boxed{\displaystyle
  \kappa_a(s)=\frac{k\sinh(kd)/d-k^2\cosh(kd)}{4d^2}
             =\frac{C_a'(s)-k^2 C_a(s)}{8s}} \qquad (s\ne0).
 \tag{4}
\]
The square-root choice has no effect on this expression.

## 2. Entire extension and algebra checks

The exact contour form also gives an independent residue calculation.
Differentiate the integral in (1) with \(H_\epsilon'/H_\epsilon\)
as numerator. The term \(Q_d'I_d/Q_d^3\) is rational with all its
poles inside the circle and vanishes to order at least four at
infinity, giving zero integral. Integration by parts in the
remaining term gives
\[
 \begin{aligned}
 \kappa_a(s)&=-\oint_R^\ast \frac{(E/Q_d)'(x)}{Q_d(x)}\,dx
            =-\oint_R^\ast \frac{2x e^{kx}}{(x^2-2s)^3}\,dx\\
            &=-\sum_{j=0}^\infty
               \frac{(j+1)(j+2)(2s)^j\,k^{2j+4}}{(2j+4)!}.
 \end{aligned}
 \tag{5}
\]
For the residue expansion, \(|2s/x^2|\le 2S/R^2<1\) on the circle.
The series in (5) converges absolutely and uniformly on every compact
complex \(s\)-disk by the factorial denominator. In particular
\(\kappa_a(0)=-k^4/12=-4/(3a^4)\) and
\(8s\kappa_a(s)=C_a'(s)-k^2 C_a(s)\) holds at zero as well.
The fixed circles give common bounds for the \(H_\epsilon\) and
\(P_\epsilon\) denominators on \(|x|=R\), since the perturbed pair
lies in \(|x|<R_0\). Cauchy's estimate in \(\epsilon\) therefore gives
\(K_\epsilon=\epsilon\kappa_a(s)+O(|\epsilon|^2)\) uniformly for
\(|s|\le S\), through \(s=0\).

- For the exact quadratic \(Q_d\) the monic deflation gives \(U_0=1\)
  and \(K_0=0\). If the perturbation is any polynomial of degree at most
  two, the unit is the perturbed quadratic's leading coefficient, so
  the curvature is identically zero for all sufficiently small \(\epsilon\).
  For a constant perturbation \(b\), the new squared half-gap is
  \(d^2+\epsilon b\), and that curvature stays zero through coalescence.
- For the exponential at \(d=0\), \(V_0=(e^{kx}-1-kx)/x^2\), whose
  second derivative at zero is \(2k^4/4!=k^4/12\). The confluent
  divided difference in (3) gives the negative of this value, agreeing
  with the independent residue and the continuous extension of (4).
- For real \(s\ge0\), (5) gives \(\kappa_a(s)<0\). For \(s<0\), with
  \(u=|k|\sqrt{-2s}\), (4) yields
  \(\kappa_a(s)=k^4(\cos u-\sin u/u)/(4u^2)\).
  At \(u=m\pi\), \(m\ge1\), this has sign \((-1)^m\).

## 3. Conditional physical normalization and limit

Assume the event and fixed tube of [Note06 §1][e06], with real
\(a\ne0\), \(0<T<1/2\), \(F_T(z)=(z-a)^2 A_T(z)\) there, and
\(A_T(a)\ne0\). Use the literal normalized Fourier field and its
Jacobi model \(G_{N,t}\). Set \(t=T+s/N^2\), \(x=N(z-a)\), and
\[
 f_N(s,x)=\frac{N^2 F_t(a+x/N)}{A_T(a)},\qquad
 g_N(s,x)=\frac{N^2 G_{N,t}(a+x/N)}{A_T(a)},\qquad
 \epsilon_N=\frac{N^2 L_N(T,a)}{A_T(a)} .
 \tag{6}
\]
On any fixed bounded real \(s\)-interval and any fixed closed \(x\)-disk,
the normalized heat law gives \(f_N(s,x)\to x^2-2s\) uniformly.
Indeed \(\partial_t F_T(a)=-\partial_z^2 F_T(a)=-2A_T(a)\), since
the normalization term multiplies \(F_T(a)=0\).
The \(F_T\) term in (6) is \(x^2 A_T(a+x/N)/A_T(a)\).
The time increment contributes exactly
\[
 \frac{s}{A_T(a)}\int_0^1
   \partial_t F_{T+\theta s/N^2}(a+x/N)\,d\theta ,
\]
which tends uniformly to \(-2s\) by joint continuity from the
physical source domination. This also treats negative \(s\).

The exact signed error law and norm law give \(g_N=f_N-\epsilon_N b_N\),
where
\[
 b_N(s,x)=
 \frac{h_N^*(t)}{h_N^*(T)}
 \left(1+\frac{x}{aN}\right)^{2N} E_{N,t}(a+x/N).
 \tag{7}
\]
 [Note03 §2][e01] [Note06 §4][e06]

The logarithmic norm derivative is \(O(\log^2(N+1))\) on the fixed
event interval, so its ratio in (7) tends uniformly to one. The
monomial factor converges uniformly to \(e^{kx}\) by the Taylor
series for \(\log(1+x/(aN))\). The phase tends uniformly to one by
Note03 (7) on a fixed compact disk in the strip containing all the
arguments. Hence \(b_N\to E\) uniformly on any fixed closed
\(x\)-disk. Also \(\epsilon_N\ne0\) and \(\epsilon_N\to0\), since
the norms are positive and \(\sup_t h_N^*(t)/(2N)!\) has the
factorial-small envelope of [Note06 §1][e06].

To apply the curvature functional, use \(R_0,R\) as above and take
the uniform field convergence on a slightly larger \(x\)-disk so
that Cauchy's estimate gives uniform convergence of the \(x\)-derivatives
on the circles. For a sufficiently small fixed disk of complex
\(\lambda\), the fields \(f_N-\lambda b_N\) and \(Q_d-\lambda E\)
are uniformly close to \(Q_d\) on both circles, below half its
modulus floors there, for all sufficiently large \(N\).
Rouché gives two zeros inside \(R_0\), with the same count inside
\(R\). Their pair polynomials are the contour moment polynomials
in (1), with a common floor \((R-R_0)^2\) on \(R\). The field
values, their \(x\)-derivatives, the pair polynomials, and the
curvature integrals thus converge uniformly to those of
\(Q_d-\lambda E\), on a common closed \(\lambda\)-disk. The
curvature integral is holomorphic in \(\lambda\) on this disk.
Cauchy's formula gives uniform convergence of its first derivative
at zero to \(\kappa_a(s)\) and a uniform quadratic remainder.
It follows that
\[
 K_x(g_N)-K_x(f_N)=\epsilon_N\big(\kappa_a(s)+o(1)\big)
\]
uniformly in \(s\), where \(K_x\) uses the \(x\)-coordinate.
The scaled circles are inside the original fixed physical tube for
large \(N\). Their counts agree with the fixed tube's count for
both fields, so the curvature uses the original pair in new
coordinates.

Under the change \(x=N(z-a)\), the derivative of the logarithm of
the unit with respect to \(x\) supplies a factor \(1/N\), and the
divided difference contributes another \(1/N\), including for a
double root. Thus \(K_x(f_N)=K(t)/N^2\) and
\(K_x(g_N)=K_N(t)/N^2\). With \(e_N(T)=D(T)-D_N(T)\) one has
\(e_N(T)\sim-L_N(T,a)/A_T(a)\) by [Note06 §2][e06], so
\(-\epsilon_N/(N^2 e_N(T))\to1\). This gives the direct limit
\[
 \boxed{\displaystyle
 \frac{N^{-4}(K-K_N)(T+s/N^2)}{e_N(T)}
   \ \longrightarrow\ \kappa_a(s)}
 \tag{8}
\]
uniformly on bounded real \(s\)-intervals, including at zero and
through the model's double time. The derivation uses only spatial
contours and uniform approximation of the signed field error.

## 4. Premise screen

The quadratic and constant checks test the same functional through
both zero types, but the quadratic field lacks the infinite positive
Jacobi source for (7). The fixed three- and four-square controls
share the quantitative phase and norm premises at their catalog
events and so admit the same conditional limit. Their full
reflection and unchanged complete square coefficients fail, and
their events supply no finite all-real threshold.
[Note06 §5][e06] [Control catalog][catalog]

For the other controls the inherited screen applies. The tested
Euler member fails \(B_0\) at time zero. The reflected super-Gaussian
fails the inherited score confinement; smooth shape and primitive
controls lack the canonical summand score, with their weaker
quantitative envelopes untested. Finite-prime orbit events vary the
source and escape in height, while finite-head or finite-score
matches supply no fixed canonical event. Finite atomic chains
terminate, and the compact triangular extensions lack the global
positive-density premise of the score argument. The RH-conditional
normalized endpoint doubles retain RH and occur outside
\(0<T<1/2\). Changed observations fail the literal Fourier heat
law, and relaxed profile data lack a specified physical field with
a counted pair. [Note03 §6][e01] [Note06 §5][e06] [B03 decision][decision]

The corollary uses the stipulated event, with no acquisition of a
canonical collision, coefficient computation, or numerical replay.

[request]: ../research-progress/handoffs/VCD-GT-E07-r1.md
[decision]: ../brainstorm/notes/03_VCD_GT_B03_CRITICAL_SCALE_DECISION_20261116.md
[e01]: 03_VCD_GT_E01_PHYSICAL_TIME_SIGNED_ERROR_20261116.md
[e02]: 04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md
[e03]: 05_VCD_GT_E03_PHYSICAL_MODEL_DEFECT_20261116.md
[e06]: 06_VCD_GT_E03_FIXED_EVENT_DEFECT_20261116.md
[results]: ../../../../../result-summaries/README.md
[geometry]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[catalog]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../avoid/08_normalization_and_constant_slips.md
