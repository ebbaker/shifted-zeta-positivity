# Vertical spectral paths as a positivity lead

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

Imaginary spectral displacement gives exact alternatives to the real
stationary signs. The potential lead is to exploit their forward-heat
form while retaining the theta arithmetic constraints.

## Equivalent complex plane conditions

Keep t real and set \(M(t,x,y)=|H(t,x+iy)|^2\). Each time slice H is
nonzero and real entire of order one. Its real-rootedness is equivalent
to vertical nondecrease, or equivalently vertical convexity:

\[
\partial_yM(t,x,y)\ge0\quad(x\in\mathbb R,\ y>0),
\qquad\text{or}\qquad
\partial_y^2M(t,x,y)\ge0\quad(x,y\in\mathbb R).
\]

At t=0 either condition is equivalent to RH. These are classical complex
Laguerre criteria; see [Csordas and Escassut, Theorems 2.3 and 2.4](https://www.numdam.org/item/AMBP_2005__12_2_331_0.pdf).
The explicit observations are

\[
\partial_yM=-2\operatorname{Im}(H_z\overline H),
\qquad
\frac12\partial_y^2M=|H_z|^2-\operatorname{Re}(H_{zz}\overline H).
\]

They exclude a nonreal zero because a nonnegative, nondecreasing vertical
modulus cannot return to zero. The curvature restricts to
\(\mathscr L_0=H_z^2-HH_{zz}\) on the real axis. More generally,

\[
|h_j(t,x+iy)|^2=h_j(t,x)^2+y^2\mathscr L_j(t,x)+O(y^4).
\]

The condition requires every translated vertical line. On the pure
imaginary axis, source positivity already gives
\(H(t,iy)=\int_0^\infty e^{tu^2}\Phi(u)\cosh(yu)\,du>0\) and increase
for y>0; those signs alone do not locate all the zeros.

## Forward heat and the remaining forcing

For \(F(t,x,y)=H(t,x+iy)\), holomorphy gives

\[
\partial_tF=\partial_y^2F,
\qquad
\partial_tM=\partial_y^2M-2|\partial_yF|^2.
\]

Consequently, \(W=\partial_yM\) satisfies

\[
\partial_tW=\partial_y^2W-2\partial_y|\partial_yF|^2.
\]

The forcing has no automatic sign. A possible task is a theta-specific
identity controlling this derivative or the complex curvature directly.
A forward-preservation theorem alone would still not recover t=0 from a
known real-rooted later slice.

The [full formula note](../notes/COMPLEX_LAGUERRE_AND_VERTICAL_PATH_CRITERIA_20261014.md)
contains the equivalence proof, logarithmic-derivative form, and exact
paired-source kernels. Those kernels retain an oscillatory cosine even
though their hyperbolic weights are nonnegative.
