# E03 r2: a compact-source control for parity monotonicity

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Explicit helper dispatch **gpt-6.2-sol /
ultra**. Independent serving-model and effort metadata are unavailable.
Execution proof with internal algebraic checking.
[B03 decision](../brainstorm/notes/04_AGC_JH_B03_PARITY_CONTROL_20261119.md)
and [immutable E03 r2 request](../research-progress/handoffs/AGC_JH_E03_REQUEST_R2_20261119.md).

For the continuous probability density in §4, both the even and odd
Jacobi degree subsequences have infinitely many increases and decreases
of the counted discriminant \(D_N\). The bounds are positive constants
on the signed limsup and negative constants on the liminf after
normalizing by the leading error scale. This is a class-specific
counterexample to eventual parity monotonicity at time zero. The
classification and premise comparison use the
[result index](../../../../../result-summaries/README.md),
[patterns index](../../../../../avoid/README.md),
[control screen](../../../../../result-summaries/12_collision_controls_and_screening.md),
[criterion classification](../../../../../avoid/01_restating_the_target.md),
[shared-premise controls](../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scope](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

**Correction to the frozen request.** The inherited convention is
\(F-G_N=L_NE_N\). The simple-root displacement has leading term
\(+L_N(\zeta)/F'(\zeta)\). Consequently \(D_N-D\) has the **negative**
leading sinusoid and \(D_{N+2}-D_N\) has the **positive** one in the
general formula below. The sign correction preserves both oscillation
bounds.

## 1. Compact-source error on fixed complex disks

Let \(\mu\) be an even positive probability measure with infinite
support in \([-K,K]\) for some \(K>0\). Let \(F(z)=\int e^{izu}\,d\mu(u)\),
the cosine observation by evenness, and let \(G_N\) be the canonical
\(N\)-site Jacobi readout. Each moment Gram matrix is positive
definite because a nonzero polynomial cannot vanish on the infinite
support. Thus \(h_N=\prod_{j=1}^N\beta_j>0\).
The Jacobi matrix is that of multiplication by \(u\) in the
orthonormal polynomial basis. Its finite compressions, the Gauss
nodes, and individual off-diagonal entries give
\[
 \|J_N\|\le K,\qquad |x_{j,N}|\le K,\qquad
 \sqrt{\beta_j}=|\langle u q_{j-1},q_j\rangle|\le K,\qquad
 h_N\le K^{2N}.
\]
[VCD finite readouts](../../../03_volterra_coefficient_dynamics/manuscript/sections/readouts.tex).

Apply the
[VCD complete error law](../../../03_volterra_coefficient_dynamics/manuscript/sections/error_law.tex),
equations error-factorization and error-moments, with
\[
 F-G_N=L_NE_N,\qquad
 L_N(z)=(-1)^N\frac{h_Nz^{2N}}{(2N)!},\qquad
 E_N(z)=\mathbb E e^{izX_N}.
\]
The confluent interpolation proof needs all moments and integrability
of the exponential remainder, both supplied here by compact support.
The error variable \(X_N\) is a simplex convex combination of a point
\(U\) from \(P_N^2\,d\mu/h_N\) and the doubled Gauss nodes. Its law is
symmetric and \(|X_N|\le K\). The exact variance gives
\[
 \sigma_N^2=\frac{2(\mathbb E U^2+\operatorname{tr}J_N^2)}
                  {(2N+1)(2N+2)}
            \le \frac{K^2}{2N+1}.
\]
Taylor's integral formula bounds
\(\left|e^{izX_N}-1-izX_N\right|
 \le \tfrac12 |z|^2 X_N^2e^{K|\operatorname{Im}z|}\).
With \(\mathbb E X_N=0\),
\[
 |E_N(z)-1|
 \le \frac{K^2|z|^2 e^{K|\operatorname{Im}z|}}{2(2N+1)} . \tag{1}
\]
Also \(|E_N(z)|\le e^{K|\operatorname{Im}z|}\), so for every fixed
\(R>0\)
\[
 \sup_{|z|\le R}|F(z)-G_N(z)|
 \le U_N(R):=\frac{e^{KR} h_NR^{2N}}{(2N)!}\ \longrightarrow 0.
 \tag{2}
\]
The bound retains the actual \(h_N\).

## 2. Root and discriminant displacements

Assume \(F\) has an isolated simple pair
\(\zeta=x+iy,\bar\zeta\) with \(x,y>0\), and choose the fixed
conjugation-symmetric counted circle of the request. Take disjoint
closed isolating disks about its two roots inside this circle, mapped
to each other by conjugation. Choose \(R\) so the circle, its
interior, the disks and a fixed positive margin \(\eta\) outside the
disks lie in \(|z|\le R\). Equation (2) and the positive minimum of
\(|F|\) on the three boundaries give the respective counts \(2,1,1\)
for \(G_N\) by Rouché for all sufficiently large \(N\). The same
uniform convergence on a narrower fixed closed collar free of
\(F\)-zeros gives a common open cleared collar for all these fields.
The \(G_N\) pair is \(\zeta_N,\bar\zeta_N\) by conjugation, with
\(\zeta_N\) in the upper root disk. These are the fixed-contour
discriminant's two occurrences. This is the fixed-cluster argument
from [VCD degree geometry](../../../03_volterra_coefficient_dynamics/manuscript/sections/zero_geometry.tex)
on separate nonreal root disks.

Write \(d_N=\zeta_N-\zeta\). The factor \(F(z)/(z-\zeta)\) is
nonzero on the closed upper disk, with a strictly positive modulus
minimum \(m\). Since \(G_N(\zeta_N)=0\), (2) gives
\(|d_N|\le U_N(R)/m\). Taylor expansion of \(F\) gives
\[
 F(\zeta_N)=F'(\zeta)d_N+O(|d_N|^2).
\]
Cauchy's derivative estimate for \(F-G_N\) on the root disk gives
a bound \(U_N(R)/\eta\). Integrating that derivative along the
segment from \(\zeta\) to \(\zeta_N\) yields
\[
 F(\zeta_N)=(F-G_N)(\zeta_N)
       =L_N(\zeta)E_N(\zeta)+O(U_N(R)|d_N|).
\]
Therefore \(F'(\zeta)d_N=L_N(\zeta)E_N(\zeta)+O(U_N(R)^2)\).
These constants depend on the fixed disks and \(F\).

Set \(A_N=h_N|\zeta|^{2N}/(2N)!\) and \(\theta=\arg\zeta\).
The normalized perturbation error is controlled without a lower
asymptotic bound for \(h_N\):
\[
 \frac{U_N(R)^2}{A_N}
 =\frac{e^{2KR}h_N}{(2N)!}
           \left(\frac{R^2}{|\zeta|}\right)^{2N}
 \le \frac{e^{2KR}}{(2N)!}
           \left(\frac{KR^2}{|\zeta|}\right)^{2N}
 \longrightarrow 0 .
\]
Equation (1) now gives
\[
 \zeta_N-\zeta=\frac{L_N(\zeta)}{F'(\zeta)}+o(A_N).
 \tag{3}
\]
The positive sign also follows directly from
\(G_N(\zeta)=-L_N(\zeta)E_N(\zeta)\) and moving from that value to
\(G_N(\zeta_N)=0\), as in VCD's fixed-real-zero displacement proof.

The discriminant conventions are \(D=-y^2\) and
\(D_N=-(y+\operatorname{Im}d_N)^2\). Since \(A_N\to0\), the
square of the displacement is \(o(A_N)\). With
\(L_N(\zeta)=(-1)^N A_N e^{2iN\theta}\), equation (3) gives
\[
 D_N-D=-2y(-1)^N A_N
       \operatorname{Im}\!\left(\frac{e^{2iN\theta}}{F'(\zeta)}\right)
       +o(A_N).
 \tag{4}
\]
The two additional links satisfy
\[
 \frac{A_{N+2}}{A_N}
 =\frac{\beta_{N+1}\beta_{N+2}|\zeta|^4}
        {(2N+1)(2N+2)(2N+3)(2N+4)}
 \le\frac{K^4|\zeta|^4}{(2N+1)(2N+2)(2N+3)(2N+4)}
 \longrightarrow0 .
\]
Inserting (4) at degree \(N+2\) then subtracting the degree \(N\)
value yields
\[
 \frac{D_{N+2}-D_N}{A_N}
 =2y(-1)^N
      \operatorname{Im}\!\left(\frac{e^{2iN\theta}}{F'(\zeta)}\right)
      +o(1).
 \tag{5}
\]

## 3. Explicit oscillation bounds on each parity

Write \(C=2y/|F'(\zeta)|>0\). On \(N=p+2j\), \(p\in\{0,1\}\),
the right side of (5) divided by \(C\) has the form
\(a_j+o(1)\), \(a_j=\sin(\omega j+\varphi_p)\),
\(\omega=4\theta\). The fixed factor \((-1)^p\) is included in
\(\varphi_p\). When \(\omega\) is neither \(0\) nor \(\pi\) modulo
\(2\pi\), the finite geometric sums at frequencies \(\omega\)
and \(2\omega\), divided by their length, tend to zero. Thus the
Cesàro mean of \(a_j\) is zero and the mean of \(a_j^2\) is \(1/2\).

Let \(b=\limsup a_j\). For each \(\epsilon>0\),
\(-1\le a_j\le b+\epsilon\) eventually, so
\((a_j+1)(b+\epsilon-a_j)\ge0\), or
\[
 a_j^2\le b+\epsilon+(b+\epsilon-1)a_j .
\]
Taking Cesàro means gives \(1/2\le b+\epsilon\). Apply the same
argument to \(-a_j\) and pass to \(\epsilon\downarrow0\). It follows
on **each** parity that
\[
 \limsup\frac{D_{N+2}-D_N}{A_N}\ge\frac{y}{|F'(\zeta)|},\qquad
 \liminf\frac{D_{N+2}-D_N}{A_N}\le-\frac{y}{|F'(\zeta)|}.
 \tag{6}
\]
The argument uses finite geometric sums for both rational and
irrational rotation angles satisfying the two frequency conditions.

## 4. The continuous triangular-density control

Take
\[
 T(v)=(1-|v|)_+,\qquad
 d\mu(v)=\frac{T(v)+[T(v-1)+T(v+1)]/4}{3/2}\,dv .
\]
The density is even, continuous, nonnegative everywhere, and strictly
positive throughout \((-2,2)\). The three tents each have integral
\(1\), so the displayed denominator gives total mass \(1\). Its
support is \([-2,2]\) and is infinite. The cosine transform of the
central tent is \(2(1-\cos z)/z^2=[\sin(z/2)/(z/2)]^2\) with the
removable value at zero. The two shifts give factors \(e^{iz}\) and
\(e^{-iz}\), so the literal Fourier observation is
\[
 F(z)=\left[\frac{\sin(z/2)}{z/2}\right]^2
             \frac{1+\cos(z)/2}{3/2}.
\]
Let \(a=\operatorname{arcosh}2\) and \(\zeta=\pi+ia\). The nonzero
sinc zeros lie at \(2k\pi\), \(k\in\mathbb Z\setminus\{0\}\). The
cosine factor has zeros exactly at \((2k+1)\pi\pm ia\):
writing \(z=u+iv\), \(\cos z=-2\) forces \(v\ne0\),
\(\sin u=0\) and \(\cos u=-1\), hence \(\cosh v=2\).
These zeros are simple. The inequality
\(\cosh(3/2)>1+(3/2)^2/2>2\) gives \(0<a<3/2\).
The two occurrences \(\pi\pm ia\) therefore lie strictly inside
\(|z-\pi|=3/2\). Every sinc zero has distance at least \(\pi\)
from the center, and each other cosine-factor zero has horizontal
distance at least \(2\pi\). Thus the count is exactly two and
the circle has a cleared collar. Since \(a<3/2<\pi\),
\(0<4\theta=4\arctan(a/\pi)<\pi\).

At the upper zero, \(\sin\zeta=-i\sqrt3\) and
\(\sin(\zeta/2)=\cosh(a/2)\), with
\(\cosh^2(a/2)=3/2\). Differentiating the product at the vanishing
cosine factor gives
\[
 F'(\zeta)=\frac{2i\sqrt3}{\zeta^2},\qquad
 |F'(\zeta)|=\frac{2\sqrt3}{\pi^2+a^2}.
\]
In this example (5) reads
\[
 \frac{D_{N+2}-D_N}{A_N}
 =-(-1)^N\frac{a(\pi^2+a^2)}{\sqrt3}
             \cos\bigl(2(N+1)\theta\bigr)+o(1).
\]
Consequently for \(p=0,1\),
\[
 \boxed{\quad
 \limsup_{N\equiv p\ (2)}\frac{D_{N+2}-D_N}{A_N}
 \ge\frac{a(\pi^2+a^2)}{2\sqrt3},\qquad
 \liminf_{N\equiv p\ (2)}\frac{D_{N+2}-D_N}{A_N}
 \le-\frac{a(\pi^2+a^2)}{2\sqrt3}.
 \quad}
\]
The scale \(A_N\) is positive. Both signs of the degree increment
therefore occur infinitely often on each parity.

## 5. Scope of the control

The compact control shares positive even source, literal cosine
observation, infinite Jacobi chain, simplex quadrature error and
a cleared count-two chart. Its continuous tent density has compact
support and lacks the full theta profile and square arithmetic.
It excludes eventual two-degree monotonicity inferred solely for
this continuous compact positive-source class. Theta-specific
arithmetic and more flexible induction, including estimates with
a separately paid defect, remain outside the exclusion. The control
is at fixed physical time zero. No positive-time collision or finite
all-real threshold is asserted. The signed remainder proof of E03 r1
serves a separate quantitative comparison.
