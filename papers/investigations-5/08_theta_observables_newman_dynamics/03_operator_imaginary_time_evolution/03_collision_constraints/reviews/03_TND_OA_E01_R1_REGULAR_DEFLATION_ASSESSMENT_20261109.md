# E01 assessment of regular deflation and pair survival

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, OA chat0003. The registry exposes
neither actual model identifier nor reasoning effort. This is a separate-chat
internal analytical assessment with shared source premises.

**Disposition.** E01 r1 is complete. The conditional finite real-pair
theorem and its constants are accepted under the stated premises. Two
local conventions need explicit qualifications, and the quadratic check
needs its sharp initial bound and spatial hypotheses stated. The
[clarification note](../notes/04_TND_OA_E01_SCOPE_AND_BOX_SCREEN_20261109.md)
preserves the frozen proof and request. The theorem controls the
specified pair on a finite slab. A canonical application still requires
the full set of margins.

The assessment follows the [frozen request r1](../research-progress/handoffs/02_TND_OA_E01_REGULAR_DEFLATION_ASSESSMENT_REQUEST_20261109.md)
and [Note02](../notes/02_TND_OA_B01_REGULAR_DEFLATION_AND_FORCE_TRANSFER_20261109.md).
The [proof-author check](02_TND_OA_B01_ANALYTICAL_SELF_CHECK_20261109.md)
is prior context. The argument is a derivative-error estimate followed
by a finite sufficient survival test. The identities give diagnostics.
[Classification](../../../../../../avoid/01_restating_the_target.md).

## 1. Deflation at shared nodes — accepted with a confluent convention

For \(a\ne b\) and \(x\notin\{a,b\}\), integrating the simplex first in
\(t\) gives the difference of \(f'\) evaluated on the \(b\)-to-\(x\)
and \(a\)-to-\(x\) segments, divided by \(b-a\). Integration in \(s\)
gives \((f[b,x]-f[a,x])/(b-a)\). Multiplying by \((x-a)(x-b)\)
then gives \(f(x)-L_{a,b}f(x)\), where \(L_{a,b}\) interpolates the
values at \(a,b\). At \(x=a\) or \(b\) the regular expression is
the simplex limit. At \(a=b\) the affine term is instead the first
Taylor polynomial \(f(a)+f'(a)(x-a)\). It vanishes identically if
the confluent node is a double zero. At \(a=b=x\), evaluation
derivatives hold the first two nodes fixed. This is the second-order
case of the [Genocchi–Hermite formula, §9 (52)](https://arxiv.org/pdf/math/0502036v1).

Differentiating \(j\) times in \(x\) inserts \(s^j f^{(j+2)}\). Its
nonnegative weight has mass \(1/(j+1)-1/(j+2)\), giving \(1/2,1/6,1/12\).
Apply the same linear operation to \(\sigma(h-P)\) at the same
\(a,b,x\) to obtain (6). Affine terms cancel, including a constant
model offset, so the estimate uses derivative errors. For example,
a residual \(\epsilon\cos(\omega(x-x_0))\) has value error at most
\(\epsilon\) and deflation error \(\epsilon\omega^2/2\) in magnitude
at \(a=b=x=x_0\). Value error alone on the real interval therefore
cannot replace (6) for the general \(C^4\) transfer class. The
coincident-node values inserted into (5) give
\(h_{xxxx}/(6h_{xx})-h_{xxx}^2/(9h_{xx}^2)\) at a double event.

## 2. Force and signed averaging — accepted with sign convention

On the full box, \(U_0\ge V_0-e_0\ge m-e_0>0\). For \(i=1,2\),
\[
\frac{U_i}{U_0}-\frac{V_i}{V_0}
=\frac{U_i-V_i}{U_0}-\frac{V_i(U_0-V_0)}{U_0V_0}.
\]
This has absolute bound \((e_i+M_i e_0/m)/(m-e_0)\). At \(i=1\)
this is \(\alpha\). Multiplication by \(A+M_1/m\) bounds the
difference of squares. Adding the \(i=2\) bound gives exactly
\(\kappa\). The numerator triangle bounds give \(A\) for \(|g|\)
and \((M_2+e_2)/(m-e_0)+A^2=K\) for \(|g_z|\).

For \(d>0\), \(dx=d\,dv\), so the average over \([a,b]\) has weight
\(dv/2\). Its total mass one yields \(B\le b_P+\kappa\), with the
negative square kept in the model integral. The same formula is
continuous at \(d=0\) by the paid floor. Common rescaling by \(\rho\ne0\)
preserves the ratios if the sign choice changes to
\(\operatorname{sgn}(\rho)\sigma\). Then \(m,M_i,e_i\) scale by
\(|\rho|\), and \(b_P\) can be kept. The constants have no explicit
inverse gap. The floor \(m-e_0\) can still degrade with the chosen box.

## 3. Complete real-axis theta tails — accepted

For \(u\ge0,\ n\ge1\),
\(\Phi_n=\pi n^2 e^{5u}(2\pi n^2e^{4u}-3)e^{-\pi n^2e^{4u}}>0\).
On \(0\le u\le W\), bound the missing \(n\ge M=N+1\) using
\(2\pi^2e^{9u} n^4e^{-\pi n^2e^{4u}}\). The ratio of successive
\(n\)-terms is \((1+1/n)^4 e^{-\pi(2n+1)e^{4u}}\le r_M<1\).
The first term's remaining exponent has derivative
\(9-4\pi M^2e^{4u}<0\). The geometric sum, \(e^{LW^2}\), and
\(\int_0^W u^k du\) give precisely \(A_k\).

On \(u>W\) sum **all** indices, using the same ratio at \(n=1\) to
obtain \(C_\Phi=2\pi^2/(1-16e^{-3\pi})\). With
\(\psi(u)=k\log u+Lu^2+9u-\pi e^{4u}\), one has
\(\psi'(W)=-d_k(W,L)\), \(\psi''<0\), and
\(d_k(W,L)\ge4\pi e^{4W}-W-15>0\) for \(W\ge1\). Integrating
\(C_\Phi e^{\psi(W)-d_k(u-W)}\) gives \(T_k\).
The two regions cover the full remainder up to measure-zero endpoints.
Real cosine derivatives contribute at most \(u^k\). For complex \(x\)
the additional growth in \(|\operatorname{Im}x|\) requires its own
bound. The double-exponential decay also gives locally uniform
domination for the underlying entire function and for the time and
space derivatives used in the proof. The normalization and reversal
of the time variable agree with [Rodgers–Tao, equations (3)–(4) and
the following heat equation](https://arxiv.org/html/1801.05914v5).
For (14), the full source on \([0,1]\) uses \(e^{L-\pi}\) because
\(9-4\pi e^{4u}<0\); its remaining integral is \(T_k(1,L)\).

## 4. Parameter-cell allowances — accepted

With \(\xi=c+d\beta\) and \(\beta=-1+s+2t+sv\), the coefficient
\(\beta\) is a convex combination of \(-1,1,v\). Thus the
\(c,d\) derivatives cost at most one spatial derivative. The \(v\)
derivative costs \(ds\) and yields \(D/((j+2)(j+3))\) times the
next moment. At fixed \(c,d,v\), time differentiation inserts
\(-u^2\) in the transform. Equivalently \(\partial_\tau h=\partial_{xx}h\),
and the finite integral \(P\) also has this equality by direct
differentiation. The bound uses moment \(j+4\). Positivity of the
component measures makes (14) an upper allowance for the truncated
model too. Summing each derivative bound times the corresponding
cell radius is valid along coordinate segments inside the box.
An implementation must still enclose the cellwise rational model
curvature and its signed average, including quadrature and rounding.

## 5. Stopping time and strict endpoint — accepted

Take the two distinct simple real zeros at time zero as hypotheses.
Local implicit continuation gives real branches by real symmetry
and uniqueness. Continue only while they are simple, distinct and
inside the strict spatial bounds. On this interval differentiating
\(h(\tau,a)=h(\tau,b)=0\) gives \(a'=-2/(a-b)-2g(a)\),
\(b'=-2/(b-a)-2g(b)\). Consequently \(c'=-g(a)-g(b)\) and
\(q'=-8-4qB\), with \(q=(b-a)^2\). The bounds on \(g,g_z\) give
the midpoint and upper-gap estimates in (16). Write \(b_{\rm up}\)
for the constant \(b_P+\kappa\) denoted by \(b\) in (16).
Since \(q\ge0\) and \(B\le b_{\rm up}\), multiply
\(q'\ge-8-4b_{\rm up}q\) by \(e^{4b_{\rm up}\tau}\) to obtain (17).
\(E_{b_{\rm up}}\) is increasing for all real \(b_{\rm up}\). In
particular \(q\ge e^{-4\max(b_{\rm up},0)\Delta}\eta>0\) uniformly
on the continuation interval.

At a first candidate stopping time \(S\le\Delta\), \(c,q\) are
uniformly Lipschitz by the same ODE bounds and the upper gap bound.
They have limits. The endpoint positions \(c\pm\sqrt q/2\) converge
to distinct zeros by continuity of \(h\). The bound
\(\lvert h_x\rvert\ge\sqrt q(m-e_0)\) extends to both limits. Thus
an additional zero cannot join either endpoint at \(S\), since the
limiting zeros are simple. The two spatial inequalities keep the
limits strictly inside the box. The implicit function theorem
extends through \(S<\Delta\), and supplies simplicity at \(S=\Delta\).
This establishes the closed-interval claim without assuming pair
survival in advance. For this conclusion a complex zero count is
unnecessary. The real factor floor also excludes another real
zero on the segment. The result leaves other complex zeros outside
the specified pair unrestricted.

## 6. Controls and comparisons — accepted at the stated scope

The three polynomials solve the forward heat equation by
differentiation. The quadratic deflates to 1. With exact model,
\(Q_-=q(0)=8T\), and feasible initial and spatial data, the gap test
is exactly \(\Delta<T\). It fails by equality at \(T\). A conservative
\(Q_-\) can shorten that certified interval. For the cubic,
\(U_0=1+\alpha(a+b+x)\), \(U_1=\alpha\), \(U_2=0\). The average of
\(-\alpha^2/(1+3\alpha c+\alpha dv)^2\) gives the displayed
\(-\alpha^2/((1+3\alpha c)^2-\alpha^2d^2)\), including its continuous
limit. At the event the double zero is nondegenerate and
\(B_*=-\alpha^2\). Two local simple real roots on the pre-event side
follow by setting \(\tau=-s^2,\ z=sy\) and continuing the simple
roots \(y=\pm\sqrt{2}\) at \(s=0\). The quartic has \(h_{xx}=0\)
at the quadruple node, so a valid transfer there cannot have
\(m>e_0\). These are local heat-polynomial checks; they can be
translated in \(z,\tau\) for the local coordinates and carry no
theta-source premises.

The table below checks the premise in the *canonical acquisition*
that each family lacks. It does not assign a failed numerical
margin to a witness whose event class or location has not been
matched. [Control inventory and witness scope](../../../../../../result-summaries/12_collision_controls_and_screening.md),
[premise discipline](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

| Control | Failed canonical premise |
| --- | --- |
| Euler-factor | Unchanged unit theta coefficients and completion. The translated source needs its own tail payment. |
| Weighted-square | Complete unit weights and full normalized reflection, even when some endpoints match. |
| Reflected super-Gaussian | Integer-square theta expansion. Reflection and positivity leave the tail formula unjustified. |
| Smooth shape, positive primitive and earlier counter-kernels | Exact theta source. The retained shape or primitive conditions do not give its coefficients or the signed bound. |
| Finite-source and finite-prime orbit | Full unit theta expansion and normalized reflection. High-gap witnesses depend on time or source, so location needs its own check. |
| Fixed-event and finite-profile threshold families | Unchanged theta source, full profile and eventual simplicity. Finite observations leave the uniform floor and signed estimate unpaid. |
| RH-conditional normalized endpoint | Ordinary Dirichlet-series arithmetic. The added time-zero doubles escape to infinity, so a fixed box need not contain one. |
| Fixed amplitude with variable kernel | Literal cosine oscillator and physical heat equation. The raw mismatch witness does not itself define physical heat motion. |
| Actual-profile measure relaxation | An integer zero divisor of the physical theta field. Matching finitely many observations admits fractional slack. |

Reflection rigidity in its stated polynomially weighted square-comb
class explains why sharing only square support or only reflection is
insufficient. For any control with an actual real pair tending to a
nondegenerate double at \(T\le\Delta\), if the preceding floor,
confinement and signed \(B\le b\) are paid, integrate the *exact*
gap ODE to \(q(T)=0\). It yields
\(Q_-\le q(0)=8\int_0^T e^{4\int_0^s B(t)\,dt}ds\le8E_b(\Delta)\).
The strict survival margin then fails. This is a conditional screen
for a matched witness. A collision-free control box can pass.

The [contour transfer, RT Note02 §4](../../../../02_heat_flow_rh_applications/rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md)
also avoids inverse internal-gap loss. It pays for cluster
identification, a boundary floor and buffer, and either complex
first-jet errors or a complex value error for its logarithm. The
real-axis scheme pays for derivative errors and a uniform deflated
factor floor. Its model uses actual nodes with affine subtraction.
The contour method deflates the model by the model's own interior
divisor. The conditioning and inputs are different. For two roots and the
same true factor, RT Note02 §3 uses \(D_H=2g\) and the ordered
energy \(E=2/q\). Its exterior contribution in Newman time is
\(B_H=-8B/q\). This also follows from differentiating \(2/q\)
and reversing \(\tau=\lambda_s-\lambda\). Its derivative transfer
constant controls \((D_H-D_F)'\), which uses twice the curvature
normalization of (9) when comparing the same factors.

[RT Note03 §§4–5](../../../../02_heat_flow_rh_applications/rodgers_tao/notes/03_CANONICAL_TWO_ROOT_MARGINS_AND_FORCE_BUDGET_20261026.md)
reports a ratio of about 309.53 between two certified exterior
energy upper budgets on its one wide-gap slab. Its contour model
curvature payment dominated the source transfer error. Its direct
route used additional full-cell actual-root jets and positive slope
floors. This is neither a comparison with (16) nor a numerical
advantage for the present method. A future comparison should give
each route the same source, target pair and slab, charge for the
data each needs, and compare the same survival conclusion. On a
tracked critical curve \(h_x=0\), \(d h(\tau,x_c(\tau))/d\tau=h_{xx}\).
A negative initial minimum with \(v(0)+M_{xx}\Delta<0\) can support
a direct certificate when boundary signs, critical-curve continuation
and simplicity/identification of the two roots are also paid.
[Parent critical-curve and factor identities](../../notes/07_TND_O_B02_COLLISION_ANATOMY_20261106.md).

## Return

There is no new arithmetic input or canonical quantitative gain.
Still to acquire are a useful finite box and its initial simple-root
evidence, \(R_0,Q_-,Q_+\), certified source/evaluation errors,
\(m,M_1,M_2,b_P\) over the full box, and all three strict margins.
The signs and constants are reviewed, with the qualifications in
[Note04](../notes/04_TND_OA_E01_SCOPE_AND_BOX_SCREEN_20261109.md).
[Continuation05](../notes/05_TND_OA_AFTER_E01_CONTINUATION_AND_MODEL_CHANGE_20261109.md)
leaves the choice of box and equally informed comparison to B02.
