# B04: a deterministic transfer for a marked pair test

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Authenticated chat0003, thread
01a1bbc2-ac28-71c1-8bf0-aefeb0b06ce8. Actual model and effort are unavailable
in the recorded source; no model switch or delegation occurred.

**Status: proved in-note from accepted E02; proof-author self-check only.**
This is an acquisition estimate, not a favorable canonical pair bound.
[Note05](05_TND_OC_B04_ARITHMETIC_RECONCILIATION_AND_ROUTE_COMPARISON_20261108.md)
owns B04's two-route decision and control screen;
[Review04](../reviews/04_TND_OC_B04_AUTHOR_SELF_CHECK_20261108.md) records
the checking scope. E03's pending assessment of B02 is not consumed.

The classification is a quantitative approximation milestone under
[avoid01](../../../../../../avoid/01_restating_the_target.md), with explicit
constant (15) below. Read the
[result index](../../../../../../result-summaries/README.md) and
[avoid index](../../../../../../avoid/README.md), especially
[controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
This note does not assign a probability law to canonical zeros.

## 1. Fix the time, coordinates and test

Time is **lambda=0** throughout, with
H_0(z)=xi((1+iz)/2)/8 and z=x+iy=2 gamma+i(1-2 beta).
The zero multiset has separate labels for multiplicity copies and is
invariant under conjugation. Use all zeros, including nonreal ones.

Define the fixed cutoff
\[
 p(t)=
 \begin{cases}
 1,&t\le0,\\
 1-10t^3+15t^4-6t^5,&0<t<1,\\
 0,&t\ge1,
 \end{cases}
 \qquad w(t)=p(2|t|-1),\qquad v(t)=t_+^2p(t-1).
 \tag{1}
\]
Thus w is one on [-1/2,1/2], zero off [-1,1], and lies in [0,1].
The transverse v equals t^2 on [0,1], is nonnegative, and is zero
outside [0,2]. These fixed piecewise polynomials have the needed bounded
weak second derivatives; v is C^{1,1}, not C-infinity. No smoothness
stronger than that is used.

For every X>=10 and 0<h,b<=1 set
\[
 a(z)=w((x-X)/h)v(y/b),\qquad
 c_h(u)=\frac{h^2}{u^2+h^2},\qquad K(z,z')=a(z)a(z')c_h(x-x').
 \tag{2}
\]
The full-plane weight is
q(z)=w((x-X)/h)v(|y|/b). The selected ordered statistic is
\[
 S_{X,h,b}(H)=\sum_{j\ne k}q(z_j)q(z_k)c_h(x_j-x_k).
 \tag{3}
\]
It is a test of the full marked factorial measure, with both transverse
magnitudes retained after the deliberate projection. No independence
of marks, stationarity, or nearest-neighbor interpretation is asserted.

The law of the center is the point mass at X: **no center averaging**.
The fixed default comparison family is
\[
 h=b=h_X=\min(1,4\pi/\log X).
 \tag{4}
\]
At large X this is the canonical leading mean-spacing scale in the
x=2 gamma coordinate. The logarithm in (4) is a definition, not an exact
spacing assertion. Horizontal window half-width is h, separation-kernel
width is h, and transverse cutoff scale is b. The theorem also permits
different declared h,b; no uniform cost as b decreases is asserted.

Every summand in (3) is nonnegative. A simple conjugate pair at
x_*+-id, |x_*-X|<=h/2, 0<d<=b, contributes exactly
\[
 2(d/b)^4.                                                   \tag{5}
\]
Its interactions with other zeros cannot subtract from this signal.
For m copies at each conjugate location, the within-pair population
contributes (4m^2-2m)(d/b)^4. Every all-real configuration, including
arbitrary real multiplicities, gives zero. In the default band
b/2<=d<=b, the simple-pair signal is at least 1/8. A fixed band does not
cover all transverse displacements.

## 2. The exact self-index correction

Use the E02 disk centered at c=X+4i, with
R=9/2, rho=13/3, r=25/6. The support of a lies in
|x-X|<=1, 0<=y<=2 and hence strictly inside D(c,r), since
sqrt(17)<r. Let mu_V be the zero counting measure of a nonzero
holomorphic V on the disk, counting multiplicities. Put
\[
 T_V(K)=\iint K\,d\mu_Vd\mu_V,\qquad D_V(a^2)=\int a^2\,d\mu_V.
\]
If V has the same local zeros as a conjugation-symmetric full field,
conjugate folding gives
\[
 \boxed{S(V)=4T_V(K)-2D_V(a^2).}                            \tag{6}
\]
Each positive-height label has two full-plane copies. The tensor square
therefore gives factor 4, and removing the self-index of each of the two
copies gives factor 2. Real-axis zeros have a=q=0. At an upper location
of multiplicity m, the tensor measure has mass m^2 and the subtraction
removes m, not m^2. In particular the two distinct conjugate partners
must not disappear when their upper-half-plane representatives coincide.

For L_V=log|V| and compact tests with these bounded weak derivatives,
\[
 T_V(K)=\frac1{4\pi^2}\iint L_V(z)L_V(z')
                 \Delta_z\Delta_{z'}K(z,z')\,dA\,dA',
\quad
 D_V(a^2)=\frac1{2\pi}\int L_V\Delta(a^2)\,dA.                \tag{7}
\]
This follows by applying the one-variable zero-measure identity in each
independent variable. Local logarithmic integrability gives product
integrability by Fubini on the product disk, even on its geometric
diagonal. Mollification inside the support buffer proves the identities
for (1): there is no boundary delta at y=0 because a and its first
y derivative vanish there. The same reasoning applies to a^2.

A constant or zero-free holomorphic multiplier only changes L_V by a
harmonic term. Integrating in the appropriate variable in (7) removes
that term, including its cross-products. No exterior zero divisor has
been silently discarded.

## 3. A two-variable acquisition lemma with only second-derivative cost

Let f,g be holomorphic near the closed R-disk, translated to c, and assume
\[
 |f|,|g|\le1,\quad |f(c)|,|g(c)|\ge m>0,\quad
 \int_{D(c,r)}|\log|f|-\log|g||\,dA\le E.
 \tag{8}
\]
Write
A=log(1/m), n=max(1,ceil(A/log(27/26))).
The accepted E02 Jensen argument gives at most n zeros of each function
in D(c,rho), including multiplicity. In particular it bounds each
population in the projections of the support of K.

For any real symmetric compact pair test K supported in D(c,r)^2 set
\[
 D_2\ge\max(\|\Delta_zK\|_\infty,\|\Delta_{z'}K\|_\infty),
 \qquad D_{\rm diag}\ge\|\Delta[K(z,z)]\|_\infty .
\]
Then the folded functional in (6), when applicable to the two full
fields, satisfies
\[
 \boxed{|S(f)-S(g)|
       \le \frac{E}{\pi}(4nD_2+D_{\rm diag}).}               \tag{9}
\]
The algebraic estimate for 4T-2D also holds without field symmetry;
symmetry is needed to identify it with the full statistic (3).

**Proof.** For every fixed z' in the relevant support, the one-variable
identity and (8) give
\[
 |(\mu_f-\mu_g)(K(\,\cdot\,,z'))|\le ED_2/(2\pi).
\]
Use the exact tensor telescoping
\[
 \mu_f\otimes\mu_f-\mu_g\otimes\mu_g
 =(\mu_f-\mu_g)\otimes\mu_f+\mu_g\otimes(\mu_f-\mu_g).
\]
Integrating the two uniform bounds against the positive zero measures
costs their two populations, at most 2n. Thus
|T_f-T_g|<=nED_2/pi. Also
|D_f-D_g|<=ED_diag/(2pi). Multiplication by 4 and 2 proves (9).
There is no root matching, simplicity premise, division by a root
derivative, or independence assumption. QED.

**Focused clarification.** A separate joint *accuracy* theorem is not
needed under these strong deterministic E02 inputs. The two functions
are compared on the same whole disk, and Jensen supplies the population
payment. A favorable value or a comparison in law with an independent
reference field is a different input and is not supplied by (9).

For comparison, Jensen's circular means also imply
\[
 \|\log|f|\|_{L^1(D_r)},\|\log|g|\|_{L^1(D_r)}
       \le M=\pi r^2 A .
\]
Indeed both logs are nonpositive, and their circular averages are at
least -A. Tensoring the log fields directly gives the valid alternative
\[
 |S(f)-S(g)|\le E\{2MD_4/\pi^2+D_{\rm diag}/\pi\},
 \quad D_4\ge\|\Delta_z\Delta_{z'}K\|_\infty .                \tag{10}
\]
This pays fourth spatial derivatives of K. Formula (9) is the selected
bound: it pays the finite population instead and needs only D_2. This is
a comparison of the displayed allowance rules, not an optimality theorem.

## 4. Explicit constants for the fixed test

Direct differentiation of p gives |p'|<=15/8 and
|p''|<=10/sqrt(3)<6. Consequently the following conservative bounds hold
almost everywhere:
\[
 \|w\|_\infty\le1,\quad\|w'\|_\infty\le15/4,\quad
 \|w''\|_\infty\le24,
\]
\[
 \|v\|_\infty\le4,\quad \|v'\|_\infty\le23/2,\quad
 \|v''\|_\infty\le41.
\]
For a in (2) set
\[
 A_0=4,\quad A_x=15/h,\quad A_y=23/(2b),\quad
 D=96/h^2+41/b^2 .
\]
These bound |a|, |a_x|, |a_y| and |Delta a| respectively.
The partial-fraction expression for c_h gives
|c_h^{(j)}|<=j!h^{-j}. Applying Delta_z to K yields
\[
 D_2=A_0D+2A_xA_0/h+2A_0^2/h^2
     =536/h^2+164/b^2,                                     \tag{11}
\]
and, since K(z,z)=a(z)^2,
\[
 D_{\rm diag}=2A_0D+2A_x^2+2A_y^2
             =1218/h^2+1185/(2b^2).                        \tag{12}
\]
For completeness one may use
D_4=D^2+76D/h^2+3624/h^4 in (10). Expansion differentiates each
a at most twice; no unproved fourth derivative of v is used.
The selected (9) is cheaper at small matched scales.

## 5. Canonical E02 specialization and all error terms

Use precisely [accepted Note02](02_TND_OC_LOCAL_LOG_TRANSFER_20261107.md)
(10)-(18),(26)-(34), not B02:
\[
 F=D(z)H_0(z)=\frac{s-1}{s}\zeta(s),\quad s=\frac12-\frac{iz}2,
 \quad M_X=2X+26,\quad
 c_0=\frac35\frac{\zeta(5)}{\zeta(5/2)},\quad
 m_X=c_0/(2M_X).
\]
Here the holomorphic zero-free multiplier D(z) is the one in E02;
it is unrelated to the derivative allowance D in section 4.
Set A_X=log(1/m_X), n_X=max(1,ceil(A_X/log(27/26))),
alpha_X=2/(n_X+2), and
\[
 C_X=\pi(25/6)^2+
 \pi(26/3)^2n_X^2e^{102A_X/n_X}2^{2/n_X}.
\]
For the exact finite-source integral Hhat_{J,U} in E02 (27), use
Fhat=D(z)Hhat and the *whole enlarged disk* error
\[
 \delta=\mathcal B_X[5C_2(J)I_{17/2}+B_0I_{17/2}^{>U}]
       \le\min(1,c_0/2),\quad \epsilon=\delta/M_X.             \tag{13}
\]
The arithmetic tail C_2(J), complete radial tail I^{>U}, constant B_0
and multiplier bound mathcal B_X are the explicit E02 (28)-(34)
quantities. These are two separate tails; neither is dropped. Their
proved majorants tend to zero. No numerical quadrature has been used.

Then f=F/M_X, g=Fhat/M_X satisfy (8) with
E_X=C_X epsilon^{alpha_X}. The truncated real cosine source is
conjugation symmetric, and its zeros in b<|y|<2b keep their actual
weights. No strip theorem for Hhat is presumed. Equations (9),(11),(12)
therefore give, for every declared X,h,b,
\[
 |S_{X,h,b}(H_0)-S_{X,h,b}(Hhat_{J,U})|
 \le E_{\rm pair}:=
 \frac{C_X\epsilon^{\alpha_X}}{\pi}
 \left[4n_X(536h^{-2}+164b^{-2})+
             1218h^{-2}+\frac{1185}{2}b^{-2}\right].          \tag{14}
\]
For the matched scales b=h the constant simplifies to
\[
 \boxed{E_{\rm pair}=
 \frac{2800n_X+3621/2}{\pi h^2}\,
       C_X(\delta/M_X)^{2/(n_X+2)}.}                         \tag{15}
\]
This is the numerical form of the acquisition milestone. At h=b=h_X,
its prefactor is O((log X)^5); the direct tensor-log rule (10) instead
has an O((log X)^7) allowance. These describe proved upper allowances,
not actual error asymptotics or complexity. Both retain the deteriorating
exponent alpha_X of order 1/log X and the expensive multiplier/source
cost in E02.

Let K_pair=(4n_XD_2+D_diag)/pi. Given any e>0, take
\[
 \delta_*=\min\{1,c_0/2,\,
 M_X(e/(2K_{\rm pair}C_X))^{1/\alpha_X}\},
\]
and choose J,U using E02's two separate tail inequalities with
delta_* in place of delta. Then E_pair<=e/2. This proves finite
acquisition precision at every declared X,h,b, with no exceptional
centers, but no uniform runtime or favorable value.

If a later evaluator returns qhat with
|qhat-S(Hhat)|<=E_eval, all evaluation, quadrature and rounding costs
belong in E_eval. An off-axis pair in the plateau with d_0<=d<=b
would contradict only the strictly paid inequality
\[
 qhat+E_{\rm eval}+E_{\rm pair}<2(d_0/b)^4.                 \tag{16}
\]
For (4) and d_0=b/2 the right side is 1/8. Neither qhat nor an
independent upper bound below the residual margin was acquired.
The exact integral (7) still has logarithmic singularities and is not
permission to use smooth quadrature without its own justification.

## 6. Comparison with the inherited methods and stopping point

With transverse marks replaced by one, a complete finite *real*
population and no horizontal window, c_h is exactly the HCB Poisson
pair kernel at observation height h/2. HCB Note01's identity and
transfer are therefore a concrete benchmark. Its denominator floor
|P(x+iy)|>=y^n assumes real true roots; a complex approximant did not
remove that premise. Equations (6)-(15) instead allow nonreal true
roots and pay disk normalization, logarithm accuracy, multiplicity
count and test derivatives. The inputs differ, so no matched cost
advantage over HCB is claimed; see Note05 for the predecessor links.

The Tao-Vu replacement theorem is not applied to H by calling a
truncation degree n_X. Its degree parameter and joint distributional
hypotheses are different; Hhat here is not a random polynomial.
The present deterministic tensor calculation is motivated by the weak
log-field architecture, and proved directly. A reference-process
comparison still needs a quantitatively verified joint input.

For example, replacing log products in (7) by products of averaged
one-point logs would discard their covariance. E02 does not justify
that operation. A sufficient additional input would be an independent
upper bound for the *combined* contraction
\[
 \frac1{\pi^2}\iint L_{\widehat F}(z)L_{\widehat F}(z')
                         \Delta_z\Delta_{z'}K\,dA\,dA'
 -\frac1\pi\int L_{\widehat F}\Delta(a^2)\,dA,
 \tag{17}
\]
with a remaining margin in (16). Merely renaming (17) as the required
joint estimate supplies no information and is not an execution task.

Time has not been evolved. No finite zero block is transported,
no wall is selected, and no RT exterior force or boundary energy is
estimated. A later dynamical consumer must retain the complete exterior
unit and all moving-window, higher-correlation and collision obligations.
The complete-source field in (13) pays this *fixed-slice* acquisition.

The normalized polynomial control in Note05 passes the generic
approximation hypotheses and still has S>0. Thus the passage to pairs
does not by itself create a favorable value. The scoped B04 conclusion
is: **the deterministic marked-pair acquisition is available in-note;
the inspected inputs do not supply its independent favorable canonical
value.** The larger localized-correlation investigation remains open.
