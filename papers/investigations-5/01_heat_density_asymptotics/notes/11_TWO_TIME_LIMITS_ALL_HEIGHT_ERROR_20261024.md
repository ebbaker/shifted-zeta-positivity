# Two heat-time limits: all-height error and stationary scaling

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.

**Status: estimates proved in-note; same-assistant review only.** The new
negative-time estimate is uniform over every real height. The positive-time
stationary clock, its growing height range and its Vandermonde error are in
[Note 12][positive]. Section 4 here also supplies a convergent analytic
positive-time approximation with an all-height absolute error budget; it
is a fallback hierarchy, not a simple asymptotic shape or an efficient
numerical algorithm. No reduced boundary evolution has been solved.

The author clarified the limits as t -> +/- infinity, suggested stationarity,
and directed attention to the sibling Vandermonde work. We keep the
**unnormalized** density and the same fixed epsilon > 0 throughout:

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad \rho_\epsilon[H]=
\frac{\epsilon^2|H_z|^2}{\pi(|H|^2+\epsilon^2)^2}.
\tag{1}
\]

Here z=x+iy; “all heights” means all real x, on the stated transverse
strip. A stationary shape after scaling is distinguished from an
unchanged physical density. These are approximation milestones under
[avoid 01][a01], not RH-equivalent criteria. See the [result index][results],
[avoid index][avoid], [controls][controls] and [self-review][review].

## 1. A complete-source derivative constant

Let phi_0=Phi(0)>0. The canonical source is even, so Phi'(0)=0.
An explicit finite constant B_2 >= sup_{u>=0}|Phi''(u)| is

\[
\begin{split}
S_p(a)&=(\max\{a,p\})^p e^{-\max\{a,p\}},\\
B_2&=\pi^{-1/4}\sum_{n\ge1}n^{-1/2}
\left[75S_{5/4}(\pi n^2)+330S_{9/4}(\pi n^2)
+224S_{13/4}(\pi n^2)+32S_{17/4}(\pi n^2)\right].
\end{split}\tag{2}
\]

This is an explicit rapidly convergent series, not a numerical supremum.
To check it, put a=pi n^2 e^(4u). Twice differentiating e^(bu-a) gives
the factor b^2-(8b+16)a+16a^2. Bound the two theta terms separately by
their absolute coefficient polynomials, and use
sup_{a>=a_0} a^p e^(-a)=S_p(a_0). This gives exactly (2).
All differentiated series converge uniformly on the positive half-line.

For a finite evaluation through n=N>=1, the remaining positive series
is at most its n=N+1 summand divided by 1-r_N, where

\[
r_N=\left(1+\frac1{N+1}\right)^8e^{-\pi(2N+3)}<1.
\tag{3}
\]

Indeed pi n^2>17/4 for every omitted n>=2, and each component has
the form constant times n^q exp(-pi n^2), with 2<=q<=8.
Equation (3) is an analytic tail bound; floating evaluation is not
outward-rounded certification. Taylor's theorem now gives the global
source inequality |Phi(u)-phi_0|<=B_2 u^2/2.

## 2. Negative time: a Gaussian with a uniform density error

Write t=-T, T>0, and set

\[
G_T(z)=\frac{\phi_0\sqrt\pi}{2\sqrt T}e^{-z^2/(4T)},
\quad C_T^2=\frac{\pi\phi_0^2}{4T},
\quad E_T(x,y)=e^{-(x^2-y^2)/(2T)}.
\]

The analytic approximate physical density is

\[
\boxed{\rho_{G,T}(x,y)=
\frac{\epsilon^2\phi_0^2(x^2+y^2)E_T(x,y)}
{16T^3\,[\epsilon^2+C_T^2E_T(x,y)]^2}.}
\tag{4}
\]

It retains the regulator crossover and the entire height dependence;
there is no Taylor expansion in x. For any fixed A>=0, the following
bound holds **for all x in R and |y|<=A sqrt(T)**. Define

\[
J_m(A)=\int_0^\infty v^m e^{-v^2+Av}\,dv,
\quad d_j=\frac{B_2 J_{j+2}(A)}{2T^{(j+3)/2}}\quad(j=0,1),
\]
\[
Q=\frac{\phi_0J_0(A)}{\sqrt T}+d_0,
\qquad P=\frac{\phi_0J_1(A)}T+d_1.
\]

Then

\[
\boxed{\sup_{x,\ |y|\le A\sqrt T}
|\rho_\epsilon(-T,x+iy)-\rho_{G,T}(x,y)|
\le \mathcal E_-(T,A):=
\frac{2P d_1}{\pi\epsilon^2}
+\frac{4QP^2d_0}{\pi\epsilon^4}=O_{A,\epsilon}(T^{-3}).}
\tag{5}
\]

All constants in (5) are specified. For evaluation,
J_0= sqrt(pi) exp(A^2/4) erfc(-A/2)/2,
J_1=(1+A J_0)/2, and
J_(m+1)=(m J_(m-1)+A J_m)/2 for m>=1.

**Proof.** Source Taylor and |partial_z^j cos(zu)|<=u^j e^(|y|u)
give |partial_z^j(H-G_T)|<=d_j, independently of x. Along the straight
segment between the two pairs (H,H_z) and (G_T,G_T'), the field and
derivative moduli are bounded by Q and P. As a real function of two
complex variables (h,p), the density has gradient norms at most
2P/(pi epsilon^2) in p and 4QP^2/(pi epsilon^4) in h. The mean value
theorem proves (5). It remains valid at zeros; no division by H is used.

For any positive normalized spatial average F whose support stays in
that transverse strip, define R_G=F rho_G. Positivity immediately gives
|F rho-R_G|<=E_-. The widths can depend on the observation height and
T. A time average has error bounded by the average of the corresponding
E_- values, with the strip condition checked at each constituent time.
This is a static approximation assertion. Differentiating a variable
filter in an evolution equation still requires its commutators.

### The stationary negative-time profile

For z=sqrt(T)(xi+i upsilon), put B=pi phi_0^2/(4 epsilon^2). Then

\[
\boxed{T^2\rho_\epsilon(-T,\sqrt T(\xi+i\upsilon))
\longrightarrow
F_-(\xi,\upsilon)=\frac{\phi_0^2}{16\epsilon^2}
(\xi^2+\upsilon^2)e^{-(\xi^2-\upsilon^2)/2}}
\tag{6}
\]

uniformly for xi in R and |upsilon|<=A, with error O_(A,epsilon)(1/T).
For an explicit allowance add T^2 E_- to
2B exp(A^2/2) M_A/T, where

\[
M_A=\frac{\phi_0^2e^{A^2/2}}{16\epsilon^2}
\begin{cases}2e^{-1+A^2/2},&A^2\le2,\\A^2,&A^2\ge2.
\end{cases}
\]

This bounds sup F_-; the additional term follows from
0<=1-(1+a)^(-2)<=2a. Fixed kernels in the scaled coordinates give
the corresponding averaged stationary profile. Height-dependent scaled
widths are allowed if the transverse support remains uniformly bounded.
At fixed physical x,y the density instead has the earlier T^(-3)
background. Both statements are compatible; neither counts zeros in a
zero-free compact region. This extends [Note 05][oldnegative].

## 3. What cannot be stationary uniformly over every height

For every fixed finite t and finite Y, the complete source and its
u-multiplied version are integrable with weight exp(Yu). Consequently
H(t,x+iy) and H_z(t,x+iy) tend to zero as |x| tends to infinity,
uniformly for |y|<=Y. One proof splits the Fourier integrals at a finite
u cutoff, approximates the remaining compact family of integrands in
L1 by finitely many step functions, and uses their explicit oscillatory
integrals; the uniform tail is bounded by the integrable majorant.
Thus, at the unchanged fixed regulator,

\[
\rho_\epsilon(t,x+iy)\longrightarrow0\quad(|x|\to\infty).
\tag{7}
\]

The same holds for positive normalized averages with bounded transverse
support and horizontal support satisfying |x|-ell(x,t)->infinity at
each fixed t. In particular ell=o(|x|) is allowed. Note 12 proves
R~L(t) k_h(y)/pi at every fixed height as t->+infinity, and uniformly
on explicitly growing windows. But whenever k_h(y)>0,

\[
\sup_{x\in\mathbb R}\left|\frac\pi{L(t)}R(t,x,y)-k_h(y)\right|
\ge k_h(y)\quad\hbox{for every finite }t.
\tag{8}
\]

Therefore that nonzero stationary profile cannot be a global uniform
limit for this averaging class. This is a fixed-regulator, bounded-
transverse-support statement. It does not exclude different transverse
scalings, nonlocal averages reaching the origin, changing epsilon, or
a more informative outer-height profile. No zero-counting theorem is
needed for this obstruction.

## 4. An analytic positive-time approximation with an all-height budget

There is a constructive global fallback if a formula valid at every
height, with a prescribed **absolute** tolerance, is needed now. Since
H(0,z)=xi(1/2+iz/2)/8, define, for t>=0,

\[
P_N(t,z)=\frac18\sum_{k=0}^N\frac{(t/4)^k}{k!}
\xi^{(2k)}(1/2+iz/2),\qquad R_N=F\rho_\epsilon[P_N].
\tag{9}
\]

These are finite analytic expressions in a standard entire function;
they use no theta roots. We give an explicit remainder so (9) is more
than an unquantified restatement of the heat operator. Put
C_b=(1-16e^(-3pi))^(-1). For s,Y>=0 define

\[
U=1+\log(s+Y+10),\qquad
\mathcal B_j(s,Y)=2\pi^2 C_b
\left[\frac{U^{j+1}}{j+1}e^{sU^2+(9+Y)U}
+\frac12\Gamma\left(\frac{j+1}2\right)\right],\quad j=0,1.
\tag{10}
\]

The complete-source bound Phi<=2pi^2 C_b exp(9u-pi e^(4u)) implies
M_j(s,Y):=integral u^j e^(su^2+Yu) Phi(u)du <= B_j(s,Y).
For u<=U discard the negative exponential in the exponent. For u>=U,
(s+1)u^2+(9+Y)u <= (pi/2)e^(4u), so the exponent is <=-u^2.
To verify the last inequality, let D=s+Y+10>=10: its left side is
<=D u^2 for u>=U; e^(4u)/u^2 is increasing there, and at U,
(pi/2)e^4 D^4>=D U^2 because U<=D. Integrating proves (10).

For a>=0, the exponential tail is bounded by
sum_(k>N) a^k/k! <= 2^(-N-1)e^(2a). Hence, uniformly on all real x
and |y|<=Y,

\[
|\partial_z^j(H-P_N)|\le2^{-N-1}\mathcal B_j(2t,Y),\quad j=0,1.
\tag{11}
\]

The positive source coefficients also give
|H_z|,|partial_z P_N|<=B_1(t,Y). The exact global maximum of the
gradient of epsilon^2/[pi(|h|^2+epsilon^2)^2] is
c_0/(pi epsilon^3), c_0=125/(54 sqrt(5)). Thus

\[
\boxed{|R-R_N|\le2^{-N-1}\mathcal A(t,Y,\epsilon),}
\tag{12}
\]
\[
\mathcal A=
\frac{2\mathcal B_1(t,Y)\mathcal B_1(2t,Y)}{\pi\epsilon^2}
+\frac{c_0\mathcal B_1(t,Y)^2\mathcal B_0(2t,Y)}{\pi\epsilon^3}.
\]

The filter may depend on height; its support must lie in |Im z|<=Y.
Choose
N=max{0, ceil(log_2 A + p log_2(1+t))-1} to get the all-height
error at most (1+t)^(-p). At fixed Y,epsilon,p this degree is
O(t log^2(t+10)). Evaluation error in the xi derivatives and subsequent
averaging must be added separately. No such high-degree numerical
evaluation is claimed here. This conservative hierarchy gives a genuine
all-height continuation and a vanishing absolute budget, but it is not
the desired simple global positive-time asymptotic profile. The useful
stationary inner profile and its much smaller input set are in Note 12.

## 5. Controls and remaining work

The density stability bound is generic and does not imply simplicity.
The negative-time theorem uses a smooth even source with the explicit
canonical B_2. Finite atomic collision controls fail that smooth-source
premise; smooth perturbed controls can have analogous Gaussian limits
and still collide. The four repository control families do not share
the unchanged canonical source used in (2), (9), and (10): Euler-factor
and primitive perturbations change its coefficients; weighted-square
controls change its reflected source structure; reflected controls do
not restore the exact canonical integer-square source. None is excluded
by a generic density error inequality. Hermite heat polynomials and the
stationary sine control remain compatible with their own stationary
scalings, as detailed in Note 12.

The open task is a useful positive-time **outer-height** formula with
relative or naturally scaled error through the fixed-regulator turnover,
plus derivative/current/covariance budgets suitable for a boundary solve.
The elementary global hierarchy is not reported as having solved those
tasks. Numerical checks are in the [round-three record][data].

[positive]: 12_GROWING_HEIGHT_STATIONARY_CLOCK_AND_VANDERMONDE_20261024.md
[oldnegative]: 05_ASYMPTOTIC_MEAN_SHAPES_AND_FLUCTUATIONS_20261024.md
[review]: ../reviews/03_TWO_TIME_LIMITS_AND_VANDERMONDE_SELF_REVIEW_20261024.md
[data]: ../numerics/TWO_TIME_LIMITS_ROUND3_20261024.json
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
