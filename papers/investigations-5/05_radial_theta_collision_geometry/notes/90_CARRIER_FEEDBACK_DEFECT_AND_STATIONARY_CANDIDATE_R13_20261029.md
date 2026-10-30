# Carrier feedback defect and the unique stationary candidate

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), effort ultra**,
Investigation05 **chat0033**. Parent research synthesis with same-model contributing derivations
and checks; no independent specialist review.

**Status: proved in-note under the accepted R10–R12 prepared common-path
inputs; pending fixed E08 assessment.** The original feedback approaches
the scalar feedback ratio of the actual evolving carrier with an explicitly integrable defect. The
unbounded drift has a paid weak forcing norm using the existing carrier
second moment. The scalar carrier energy converges to a specified value
with finite total variation. There is a unique smooth radial stationary
candidate at that energy level. Convergence of the actual profile to that
candidate, convergence of either feedback coefficient, and nonlinear
shadowing remain unproved.

The domain, full source, physical mark (T,A)=(1/4,2), preparation, actual
jets, source operator, cutoff and feedback path remain those of
[Notes82][n82]–[83][n83], accepted in [Review43][r43]. The [R13 intake][intake]
selects this complete carrier/feedback comparison before analysis.
The companion full-balance calculation is [Note89][n89].

## 1. Paid inputs and a denominator that never vanishes

Use W=ah+e from R12, where a=(m0/M,m1/M), e=(e0,e1), M=int h>0 and
E0=||W(s)||2²>0 is the original conserved vector energy. Set
\[
 n=|a|^2=\frac{|(H,H_a)|^2}{M^2},\qquad
 n_*=(70/73)^2,\qquad n_*\le n\le1.                           \tag{1}
\]
The lower bound is exactly the accepted physical mass margin from R10;
the upper bound follows from |int W|<=M. No individual jet mass is in
a denominator, and none is assumed nonzero.

The original positive carrier obeys h0>=|W0|, hence positivity of the
common propagator gives h(s)>=|W(s)| pointwise. Define
\[
 E_h=\|h\|_2^2,\quad G_h=\|\nabla h\|_2^2,\quad
 D_h=\int d h^2,\quad d=\operatorname{div}v,\quad3\le d\le6.
\]
Then, at every auxiliary time,
\[
 \boxed{D_h\ge3E_h\ge3E_0>0,\qquad nD_h\ge3n_*E_0.}          \tag{2}
\]
This denominator payment uses carrier domination, not a new moment or
an unproved lower bound on h at a point.

Let \(L_\Sigma=L_0+L_1\) and \(T_\Sigma=T_0+T_1\) be the accepted
R12 error budgets. Throughout s>=0,
\[
 \|e(s)\|_2^2\le L_\Sigma e^{-B(s)/2},\qquad
 \|\nabla e(s)\|_2^2\le T_\Sigma e^{-B(s)/2},
\]
\[
 G_W=\|\nabla W\|_2^2\le KE_0,\qquad
 a_*\le\alpha\le\bar\alpha=2K/3,\qquad
 a_*=\frac15\left(\frac{6\pi^2E_0}{M^2}\right)^{2/3}.         \tag{3}
\]
The carrier budgets of Note82 are E_h<=M²D and G_h<=M²H, with D,H
completely paid there. These are inherited estimates for the same
carrier, not a new scalar evolution.

## 2. Exact feedback defect and all-time constants

For the actual carrier define the comparison functional
\[
 \alpha_h(s)=\frac{2G_h(s)}{D_h(s)}.                            \tag{4}
\]
It is well defined by (2). The original coefficient remains
alpha=2G_W/D_W, D_W=int d|W|². Put
\[
 \Delta G=G_W-nG_h
        =2\langle\nabla W,\nabla e\rangle-\|\nabla e\|_2^2,
\]
\[
 \Delta D=D_W-nD_h
        =2\langle dW,e\rangle-\int d|e|^2.                    \tag{5}
\]
Using alpha D_W=2G_W gives the **exact** identity
\[
 \boxed{\alpha-\alpha_h
          =\frac{2\Delta G-\alpha\Delta D}{nD_h}.}             \tag{6}
\]
The minus signs in (5) follow from ah=W−e and must be kept; the
coefficient in (6) is the original alpha.

Whole-space Cauchy–Schwarz, d<=6 and (3) yield
\[
 |\Delta G|\le2\sqrt{KE_0T_\Sigma}\,e^{-B/4}+T_\Sigma e^{-B/2},
\]
\[
 |\Delta D|\le12\sqrt{E_0L_\Sigma}\,e^{-B/4}+6L_\Sigma e^{-B/2}.             \tag{7}
\]
Define the fully paid constants
\[
 d_1=\frac{4\sqrt{KE_0T_\Sigma}
                     +12\bar\alpha\sqrt{E_0L_\Sigma}}{3n_*E_0},
 \qquad
 d_2=\frac{2T_\Sigma+6\bar\alpha L_\Sigma}{3n_*E_0}.                         \tag{8}
\]
Equations (2), (6), (7) prove
\[
 \boxed{|\alpha(s)-\alpha_h(s)|
                     \le d_1e^{-B(s)/4}+d_2e^{-B(s)/2}}
 \quad(s\ge0).                                                \tag{9}
\]
No early interval or small-error threshold is omitted. The same estimate
can use n instead of n_* when the actual vector mass is already given.

For t>=0 define
\[
 A(t)=4d_1e^{-B(t)/4}+2d_2e^{-B(t)/2}.
\]
Because B'=alpha and alpha>=a_*,
\[
 \boxed{\int_t^\infty\alpha|\alpha-\alpha_h|\,ds\le A(t),
 \qquad
 \int_t^\infty|\alpha-\alpha_h|\,ds\le A(t)/a_*.}             \tag{10}
\]
The first bound integrates exp(-B/4) and exp(-B/2) exactly; the second
uses ds<=dB/a_*. These are integrable defects, not finite total alpha.

For completeness alpha_h is uniformly nondegenerate as a functional
along this trajectory. Nash gives G_h>=c_N E_h^(5/3)M^(-4/3), with
c_N=(3/5)(6pi²)^(2/3), while D_h<=6E_h. Thus
\[
 \boxed{a_*\le\alpha_h(s)\le\frac{2M^2H}{3E_0}.}             \tag{11}
\]
The upper bound uses G_h<=M²H and (2). These inequalities do not define
or evolve a second path.

If B_h(s)=integral_0^s alpha_h(actual h(q))dq, then B−B_h has a finite
limit beta_infinity, and
\[
 |\beta_\infty-(B(t)-B_h(t))|\le A(t)/a_* .                    \tag{12}
\]
Both total compressions diverge at least linearly; their bounded difference says
nothing by itself about convergence of their instantaneous derivatives.

## 3. The unbounded drift has a paid dual-Lipschitz forcing norm

The existing positive carrier moment R_h=int |X|²h satisfies
R_h'<=6M−2alpha R_h. Consequently
\[
 R_h(s)\le\overline R:=\max\{R_0,3M/a_*\},                   \tag{13}
\]
where R0 already includes the complete +6M preparation cost. No new
source acquisition is needed. Since |v(X)|<=2|X|,
\[
 \int|v|h\le2\int|X|h\le2\sqrt{M\overline R}=:V_1.           \tag{14}
\]
For a distribution g define the explicit test seminorm
\[
 \|g\|_{\mathrm{Lip}^*}
   =\sup\{|\langle g,\varphi\rangle|:
       \varphi\in C_c^\infty(\mathbb R^3),\quad
                      \|\nabla\varphi\|_\infty\le1\}.
\]
It is finite for div(vh), since integration by parts and (14) give
\[
 |\langle\operatorname{div}(vh),\varphi\rangle|
       =\left|\int vh\cdot\nabla\varphi\right|
       \le V_1\|\nabla\varphi\|_\infty.                      \tag{15}
\]
This explicitly pays the spatially unbounded factor in v. It does not
assert an L2 bound on vh or an H^-1 bound on its divergence.

Define the actual defect forcing
\[
 \mathfrak f_s=(\alpha(s)-\alpha_h(s))\operatorname{div}(vh(s)).
\]
Then
\[
 \boxed{\|\mathfrak f_s\|_{\mathrm{Lip}^*}
             \le V_1(d_1e^{-B/4}+d_2e^{-B/2}),}
\]
\[
 \boxed{\int_t^\infty\|\mathfrak f_s\|_{\mathrm{Lip}^*}ds
                 \le(V_1/a_*)A(t),\qquad
 \int_t^\infty\alpha\|\mathfrak f_s\|_{\mathrm{Lip}^*}ds
                 \le V_1A(t).}                               \tag{16}
\]
All these bounds hold through the initial interval. Compactly supported
tests and the inherited decay justify the displayed integrations; no
boundary at r=1 or omission of the inner ball is made.

## 4. Exact scalar equation, scalar energy limit, and scope

For admissible positive h write the scalar nonlinear vector field
\[
 \mathcal N(h)=\Delta h+
       \frac{2\|\nabla h\|_2^2}{\int d h^2}\operatorname{div}(vh).
\]
The actual carrier obeys the **exact** equation
\[
 \boxed{\partial_sh=\mathcal N(h)+\mathfrak f_s.}              \tag{17}
\]
This is an identity on the original common-path solution. It is not a
silent replacement of alpha, and no independently evolved solution of
h_s=N(h) is introduced.

The vector field N is tangent to the scalar L2-energy surface:
2<h,N(h)>=−2G_h+alpha_h D_h=0. Thus the actual scalar energy satisfies
\[
 \boxed{E_h'=(\alpha-\alpha_h)D_h.}                            \tag{18}
\]
Since D_h<=6M²D, its total variation has the paid tail
\[
 \boxed{\int_t^\infty|E_h'|ds
                   \le\frac{6M^2D}{a_*}A(t).}                \tag{19}
\]
Here E_h itself is not constant. A second exact identity identifies its
limit without invoking a convergence theorem for profiles:
\[
 E_0-nE_h=2\langle W,e\rangle-\|e\|_2^2.
\]
Hence
\[
 \boxed{\left|E_h(s)-\frac{E_0}{n}\right|
    \le\frac{2\sqrt{E_0L_\Sigma}}n e^{-B(s)/4}
                           +\frac{L_\Sigma}{n} e^{-B(s)/2}.}            \tag{20}
\]
In particular E_h tends to E0/n>0; using n_* instead of n in the
upper allowance is permitted. This is scalar **energy** convergence,
not convergence of h in L2, convergence of its gradient norm, or a
stationary solution claim.

Equation (17) has an integrable forcing in the explicitly stated weak
test seminorm. Deriving nonlinear shadowing, convergence to an equilibrium,
or a stationary profile would additionally require a stability/compactness
and asymptotic argument suited to this topology and to N. None is proved
by (16), the L2-energy limit, or existence/uniqueness of possible equilibria.
The feedback defect tends to zero, but alpha and alpha_h are not thereby
proved to have limits. The common carrier continues to contain the
source, initial preparation and original feedback trajectory.

## 5. A unique stationary candidate at the identified energy level

The potential for the fixed radial drift is
\[
 V(X)=\frac{|X|^2}{2}+\frac12\log(1+|X|^2),\qquad \nabla V=v.
                                                               \tag{21}
\]
For lambda>0 define
\[
 Z(\lambda)=\int_{\mathbb R^3}e^{-\lambda V(X)}dX,\qquad
 h_\lambda(X)=\frac{M}{Z(\lambda)}e^{-\lambda V(X)}.
                                                               \tag{22}
\]
This is the classical fixed-potential Gibbs form; [Reference16][ref16]
records the checked classical attribution and its scope. The statements
needed here are derived directly, with no nonlinear convergence theorem
imported.

Each h_lambda is smooth, positive, radial and integrable, with mass M.
Its flux satisfies grad h_lambda+lambda v h_lambda=0. Integration of
its stationary equation against h_lambda gives
\[
 2\|\nabla h_\lambda\|_2^2
                  =\lambda\int d h_\lambda^2,
 \qquad \alpha_{h_\lambda}=\lambda.                           \tag{23}
\]
All boundary terms vanish by Gaussian decay. Thus h_lambda is also an
equilibrium of the scalar vector field N, for its own feedback value.

Conversely, let f be a nonnegative, nonzero, smooth radial equilibrium
of N with mass M, finite H1 norm and the stated integration domain.
Its scalar ratio lambda=2||grad f||2²/int d f² is positive: a nonzero
constant cannot be integrable on R³. The radial stationary equation is
\[
 \partial_r\{r^2[f'(r)+\lambda V'(r)f(r)]\}=0.
\]
Smoothness at the origin makes the constant radial flux zero. Hence
f'+lambda V'f=0, and mass normalization gives f=h_lambda. This is a
classification in the declared smooth radial stationary class; it is
not an attraction theorem.

Let
\[
 Q(\lambda)=\|h_\lambda\|_2^2
            =M^2\frac{Z(2\lambda)}{Z(\lambda)^2}.              \tag{24}
\]
Gaussian domination permits differentiation at every lambda>0. If
expectation with density exp(-lambda V)/Z(lambda) is denoted by
E_lambda, then
\[
 \frac{d}{d\lambda}\log Z(\lambda)=-\mathbb E_\lambda V,
 \qquad
 \frac{d}{d\lambda}\mathbb E_\lambda V
                     =-\operatorname{Var}_\lambda(V)<0.
\]
The variance is strictly positive because V is nonconstant and the
Gibbs density is positive everywhere. Therefore
\[
 \boxed{\frac{d}{d\lambda}\log Q(\lambda)
       =2(\mathbb E_\lambda V-\mathbb E_{2\lambda}V)
       =2\int_\lambda^{2\lambda}
                    \operatorname{Var}_t(V)dt>0.}              \tag{25}
\]
In particular Q is strictly increasing.

The elementary inequality 0<=log(1+r²)<=r² gives r²/2<=V<=r², so
\[
 (\pi/\lambda)^{3/2}\le Z(\lambda)
                       \le(2\pi/\lambda)^{3/2}.
\]
Apply both bounds separately to the numerator and denominator in (24):
\[
 \boxed{M^2(\lambda/(8\pi))^{3/2}
             \le Q(\lambda)\le M^2(\lambda/\pi)^{3/2}.}       \tag{26}
\]
Thus Q tends to zero as lambda decreases to zero, and to infinity as
lambda increases to infinity. Continuity and strict monotonicity prove
that there is exactly one lambda_star>0 with
\[
 Q(\lambda_*)=E_0/n.
\]
Writing mu=|(H,H_a)|=M sqrt(n)>0, (26) gives the completely analytical
bracket
\[
 \boxed{\pi(E_0/\mu^2)^{2/3}
                 \le\lambda_*\le8\pi(E_0/\mu^2)^{2/3}.}       \tag{27}
\]
No numerical value or source acquisition is claimed. The unique smooth
radial stationary **candidate** at the energy level identified in (20)
is h_(lambda_star). This statement alone does not identify the asymptotic
profile of the actual carrier.

## 6. The exact remaining convergence gap

R12's mixing proof compares two fields driven by the **same** coefficient
path alpha(s). The candidate h_(lambda_star) is stationary for the
constant path lambda_star. Applying that contraction argument to h and
h_(lambda_star) therefore introduces a difference of coefficient paths.
The paid defect alpha−alpha_h does not control the remaining difference
alpha_h−lambda_star. Identifying an energy level and its unique stationary
profile does not remove that unproved stability step. In particular,
common-path synchronization cannot be used as if it already compared the
actual carrier with this different-path equilibrium.

A conditional algebra diagnostic makes the same issue visible in the
classical fixed-potential free energy. For a positive sufficiently decaying
profile for which the displayed entropy, Fisher term and integrations by
parts are finite, set
\[
 \mathcal E_\lambda(h)=\int h\log h+\lambda\int Vh.
\]
Along a smooth path satisfying the original carrier equation,
\[
 \frac d{ds}\mathcal E_\lambda(h)
 =-\int h|\nabla\log h+\lambda v|^2
    +(\lambda-\alpha)
          \int h v\cdot(\nabla\log h+\lambda v).              \tag{28}
\]
Indeed differentiation and one integration by parts pair
−h(grad log h+alpha v) with grad log h+lambda v. Equation (28) is a
conditional algebra identity, not a new uniform actual-path
entropy/Fisher estimate. At lambda=lambda_star, the second coefficient
splits into the paid alpha−alpha_h and the unpaid alpha_h−lambda_star.
Thus this fixed-lambda entropy is not automatically a Lyapunov function
from the estimates proved here. This is not a no-go theorem for a
nonlinear Lyapunov or stability argument.

The equally informed direct method has all inputs used here and obtains
the same transfer. The positive mass margin in (1) and the upstream K
are unchanged. At an admitted zero-vector-mass collision n=0 and this
comparison loses its denominator premise; no exclusion is manufactured.
The remaining control scopes are those in [Review43][r43] and the
[control register][controls]. Primitive reconstruction remains available
to both comparators and supplies no additional sign in this argument.
The [result index][results] and [pattern index][avoid] govern the status.

[intake]: ../research-progress/handoffs/CTF-B02_COMPLETE_CARRIER_REDUCTION_R13_INTAKE_20261029.md
[n89]: 89_COMPLETE_CARRIER_PRODUCTION_TRANSFER_R13_20261029.md
[ref16]: ../references/16_FIXED_DRIFT_GIBBS_AND_FEEDBACK_SCOPE_20261029.md
[n67]: 67_UNIFORM_FEEDBACK_DIRECT_COMPARISON_B02_R10_20261029.md
[n76]: 76_UNIFORM_RESIDUAL_AND_FIXED_JET_CLOSURE_R11_20261029.md
[n82]: 82_COMMON_CARRIER_SYNCHRONIZATION_R12_20261029.md
[n83]: 83_FINITE_CENTERED_PRODUCTION_CORRECTION_R12_20261029.md
[r43]: ../reviews/43_COMMON_CARRIER_AND_PRODUCTION_E08_R12_ASSESSMENT_20261029.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
