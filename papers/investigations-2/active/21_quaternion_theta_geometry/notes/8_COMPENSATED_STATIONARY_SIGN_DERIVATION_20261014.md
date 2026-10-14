# Compensated stationary signs on a bounded theta rectangle

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

The K=2, N=3 construction from
[Note 7](7_CONTINUATION_AND_NEXT_SIGNED_ESTIMATE_20261014.md) now certifies
both genuine stationary signs on the entire closed padded rectangle

\[
R^+=[1/200,3/50]\times[7,41].
\]

The explicit strict margins are L_0(H)>5*10^(-10) where H_x=0 and
L_1(H)>10^(-11) where H_xx=0. The complete 34-cell cover leaves no
unresolved sign or branch-isolation cells. In particular H and H_x have
no joint zero in R+, or in its reflected negative-height rectangle.

This note supplies the complete-index payment, finite-channel heat
residual, and a separate analytic signed cross-term estimate on the
overlap band

\[
B=[1/200,3/50]\times[7,8]\subset R^+.
\]

The analytic signed estimate holds throughout B, whether or not a
stationary set meets it. Section 6 reports the completed independent
validated calculation on all of R+. No sampled sign, zero table, or
unproved relative error enters either proof. Its assessment is a separate
internal review.

## 1. Exact endpoint compensation and transport

Use the complete source and scalar normalization of the
[manuscript](../manuscript/quaternion_theta_geometry.tex):

\[
\phi_n(u)=(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\quad g_{n,t}=e^{tu^2}\phi_n,
\quad H(t,x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du.
\]

Put b_n=phi_n'(0), e_n=phi_n'''(0), and

\[
\beta_0=(u+u^3)e^{-u^2},\qquad \beta_1=u^3e^{-u^2}/6.
\]

Their first and third endpoint derivatives are respectively (1,0) and
(0,1). Thus

\[
\widetilde g_{n,t}=g_{n,t}-b_n\beta_0-(e_n+6tb_n)\beta_1
\]

has its first and third odd endpoint jets zero. Normal convergence and
Jacobi reflection give sum_n b_n=sum_n e_n=0; hence the compensation
changes no complete-source observation.

For B_k(x)=int_0^infinity beta_k(u)cos(xu)du and
G_n(t,x)=int_0^infinity g_{n,t}(u)cos(xu)du,

\[
a_n=G_n-b_nB_0-(e_n+6tb_n)B_1,
\quad
\partial_t a_n=\int_0^\infty u^2g_{n,t}\cos(xu)\,du-6b_nB_1,
\]
\[
(\partial_t+\partial_x^2)a_n
=-b_nB_0''-(e_n+6tb_n)B_1''-6b_nB_1.
\tag{1}
\]

For m>=2, partial_t^m a_n=int u^(2m)g_n cos(xu)du. Formula (1) is the
finite-channel heat residual. Only the complete sum cancels it. Transport
by the homogeneous heat equation is therefore legitimate for H, but
requires this residual for a_n or P_3. The adopted Fueter lift and real
external time are unchanged.

The Gaussian transforms can be evaluated without a Gaussian integration
cutoff. If D is Dawson's function, S(x)=D(x/2), then

\[
S'=\tfrac12-\tfrac{x}{2}S,
\quad
B_0=1-\tfrac{x^2}{8}+\tfrac{x(x^2-10)}8S,
\quad
B_1=\tfrac{4-x^2}{48}+\tfrac{x(x^2-6)}{48}S.
\tag{2}
\]

Indeed S=int_0^infinity e^(-u^2)sin(xu)du, its differential equation
follows by one integration by parts, and B_0=S'-S''' and B_1=-S'''/6.
Higher x derivatives follow exactly from the displayed differential
equation. Validated arithmetic must retain the cancellation in (2).

## 2. A rational complete-index payment for every physical jet

Let R_3=sum_(n>=4) tilde g_(n,t), r_j=int u^jR_3 cos(xu+j pi/2)du.
For j=0,1,2,3, four integrations by parts have no lower boundary terms
and give

\[
|r_j|\le x^{-4}\|(u^jR_3)^{(4)}\|_1.
\tag{3}
\]

The manuscript's coefficient majorant has

\[
Q_0=2q+3,\qquad
Q_{k+1}=(2u+5+4q)Q_k+\partial_uQ_k+4q\partial_qQ_k,
\]
\[
W_{2j}=\sum_{\ell=0}^{\min(j,4)}
\binom4\ell\frac{j!}{(j-\ell)!}u^{j-\ell}Q_{4-\ell}
=\sum_{a,b}\omega_{ab}u^aq^b.
\]

This majorizes the heated source for every 0<=t<=1, so in particular on
the requested padded rectangle. The endpoint coefficient polynomials are

\[
Q_1(0,q)=15+30q+8q^2,
\]
\[
Q_3(0,q)=465+3450q+4280q^2+1440q^3+128q^4.
\]

Gaussian differentiation and an absolute coefficient sum give the
following rigorous upper bounds for
B_(2jk)=||(u^j beta_k)^(4)||_1:

| j | k=0 | k=1 |
|---|---:|---:|
| 0 | 316 | 67 |
| 1 | 702 | 747/5 |
| 2 | 1566 | 328 |
| 3 | 18819/5 | 1539/2 |

To reproduce these bounds, differentiate the Gaussian polynomial with
the rule p -> p'-2up four times and sum absolute coefficients against
the half-line Gaussian moments. For odd powers use
int_0^infinity u^(2m+1)e^(-u^2)du=m!/2; for even powers use
(2m)! sqrt(pi)/(2*4^m*m!), with sqrt(pi)<9/5.

For A=16pi, the N=3 threshold A>=25 is satisfied. The manuscript's
complete geometric index tail is

\[
T_s(3)=\frac{A^se^{-A}}{1-e^{-5\pi}}.
\]

Using pi>25/8, pi<22/7, and e>8/3 gives the fully rational majorant

\[
T_s(3)<\widehat T_s:=
\frac{(3/8)^{50}}{1-(3/8)^{15}}
\begin{cases}(352/7)^s,&s\ge0,\\50^s,&s<0.\end{cases}
\tag{4}
\]

For each j, the rational quantity

\[
C_j=\sum_{a,b}\omega_{ab}\frac{a!}{3^{a+1}}\widehat T_{b-a}
+\sum_{k=0}^1 B_{2jk}\sum_b[q^b]Q_{2k+1}(0,q)\widehat T_{b+1}
\tag{5}
\]

includes every omitted index and the entire half-line source integral.
Its bounds are

\[
(C_0,C_1,C_2,C_3)
<(2,4,9,20)\,10^{-9}.
\]

Consequently on R+,

\[
|r_j|<\varepsilon_j(x):=(2,4,9,20)_j10^{-9}x^{-4},
\quad
|r_j|<(1,2,4,9)_j10^{-12}\qquad(x\ge7).
\tag{6}
\]

All comparisons in (4)--(6) are rational. The replay script checks the
tighter bounds C_j/7^4<(1,2,4,9)_j10^(-12), rather than obtaining them
solely from the rounded C_j bounds. These estimates pay the omitted
theta indices; they do not pay approximation errors in retained channel
quadrature, which must be added by the independent numerical certificate.

For a retained channel, an explicit integration payment is also available.
Set tau=3/50 and, for U>=1,

\[
L_n(U)=\tau U^2+9U-\alpha_ne^{4U},\quad
\lambda_n=4\alpha_ne^{4U}-9-2\tau U>0.
\]

Concavity of the exponent on u>=U gives, for any nonnegative integer j,

\[
\left|\int_U^\infty u^jg_{n,t}(u)\cos(xu+j\pi/2)\,du\right|
\le2\alpha_n^2e^{L_n(U)}
\sum_{\ell=0}^j\binom j\ell
U^{j-\ell}\frac{\ell!}{\lambda_n^{\ell+1}}.
\tag{7}
\]

This follows from dropping the negative summand in phi_n, not from
assigning a sign to the oscillatory integral. If the compensation is also
integrated with a cutoff, each Gaussian monomial satisfies

\[
\int_U^\infty u^me^{-u^2}\,du
\le e^{-U^2}\sum_{\ell=0}^m\binom m\ell
U^{m-\ell}\frac{\ell!}{(2U)^{\ell+1}}.
\tag{8}
\]

Using exact transforms (2) avoids that additional Gaussian cutoff.

## 3. A complete-source signed moment on the overlap band

For 0<=t<=3/50, write w_t=e^(tu^2)Phi and
M_j=int_0^infinity u^jw_t(u)du. The strengthened moment inequality is

\[
M_4-\frac{32}{3}M_6
>\frac{659107997}{1101004800000000}
>\frac1{2000000}.
\tag{9}
\]

Here is its complete arithmetic and integration payment. Put
g(q)=q(2q-3)e^(-q). Then phi_1=e^u g(pi e^(4u)), and
g'(q)=-(2q-1)(q-3)e^(-q)<0 for q>=pi. The earlier complete-source
core gives Phi>6/25 on [0,1/10]. In addition,

\[
\Phi>3/25\quad(0\le u\le3/20),
\qquad
\Phi>1/20\quad(0\le u\le1/5).
\tag{10}
\]

For the first extra bound, e^(3/5)<11/6 and pi<22/7 give
pi e^(4u)<6; therefore g(q)>g(6)>54(4/11)^6>3/25.
For the second, e^(4/5)<9/4 gives q<36/5, and e<11/4,
e^(1/5)<5/4 give

\[
g(q)>\frac{2052}{25}(4/11)^7(4/5)>1/20.
\]

Only strictly positive theta indices are discarded in these lower bounds.

For the full upper tail take b=3/10 and
L_t(u)=tu^2+9u-pi e^(4u). The elementary rational comparisons
e^(6/5)>83/25 and pi>25/8 imply

\[
L_t(b)<\frac{27}{10}+\frac{27}{5000}-\frac{83}{8}<-\frac{23}{3},
\quad L_t'(b)<9+\frac9{250}-\frac{83}{2}<-32.
\]

L_t''<0 on u>=b. Since e^(23/3)>2000 and 4pi^2<40, the complete
theta-index majorant from the manuscript therefore gives

\[
w_t(u)<\frac1{50}e^{-32(u-b)}\qquad(u\ge b).
\tag{11}
\]

The factor u^4(1-32u^2/3) is nonnegative on [0,b], and for u>=b
it is bounded below by -(32/3)u^4(u^2-b^2), since
1-(32/3)b^2=1/25. Applying the three lower bounds in (10) on their
successive subintervals and paying the complete negative tail gives

\[
M_4-\frac{32}{3}M_6>P-\frac{16}{75}I,
\]
\[
P=\frac6{25}\int_0^{1/10}f(u)\,du
+\frac3{25}\int_{1/10}^{3/20}f(u)\,du
+\frac1{20}\int_{3/20}^{1/5}f(u)\,du
=\frac{111799}{33600000000},
\quad f(u)=u^4(1-32u^2/3),
\]
\[
I=\int_b^\infty u^4(u^2-b^2)e^{-32(u-b)}\,du
=\frac{85837761}{6710886400000}.
\]

Their exact difference is the rational number in (9). The check script
verifies every elementary exponential comparison using rational Taylor
sums with explicit geometric remainder bounds.

The same moment threshold holds uniformly on the larger time range
0<=t<=1. For this extension use the slightly sharper classical bound
pi>333/106. It also follows from the rational alternating-series lower
bound in Machin's identity pi=16 arctan(1/5)-4 arctan(1/239), checked in
the replay. Then, at b=3/10,

\[
L_t(b)<\frac{279}{100}-\frac{333}{106}\frac{83}{25}
=-\frac{40491}{5300}<-\frac{38}{5},
\]
\[
L_t'(b)<\frac{48}{5}-4\frac{333}{106}\frac{83}{25}
=-\frac{42558}{1325}<-32.
\]

Since exp(38/5)>1960, the full upper envelope becomes
w_t(u)<(1/49)exp(-32(u-b)). Keeping the same positive core and exact
tail integral therefore yields, for every 0<=t<=1,

\[
M_4-\frac{32}{3}M_6
>P-\frac{32}{147}I
=\frac{2092283587}{3853516800000000}
>\frac1{2000000}.
\tag{9a}
\]

## 4. A nonvacuous signed cross-term estimate on B

The global inequality sin y>=y-y^3/6 for y>=0 and positivity of w give

\[
h_3(t,x)\ge x\left(M_4-\frac{x^2}{6}M_6\right)
>\frac{x}{2000000}\qquad(0<x\le8).
\]

Together with the manuscript's complete-source central slope
-h_1>x/120000, this proves throughout B

\[
\mathscr L_1(H)=h_2^2-h_1h_3
>\frac{x^2}{240000000000}
\ge\frac{49}{240000000000}.
\tag{12}
\]

This is a signed source estimate on the whole band, not a sampled sign
or a statement requiring the stationary set to be nonempty there.
Using (9a), the same sign L_1(H)>x^2/240000000000 holds on the whole
central domain 0<=t<=1, 0<|x|<=8. At x=0, h_2<0 excludes the second
stationary set. The first stationary set is exactly x=0 on |x|<=8,
where the established strict L_0 sign applies. Thus both central
stationary signs now extend to |x|<=8. This extension claims no larger
uniform norm gap than the already proved one.

Let P=P_3 and p_k=partial_x^k P. Define the exact retained diagonal and
cross terms D_1^3, X_1^3 as in Note 7, and put

\[
E_1=\varepsilon_2^2+|p_1|\varepsilon_3
+|p_3|\varepsilon_1+\varepsilon_1\varepsilon_3,
\tag{13}
\]

using the uniform choices (epsilon_0,...,epsilon_3)=(1,2,4,9)10^(-12).
The manuscript's genuine jet bounds |h_1|<=1/8 and |h_2|,|h_3|<=1/12
imply |p_k|<=|h_k|+epsilon_k. Hence E_1<13*10^(-13).
The general identity, valid without stationarity, is

\[
\mathscr L_1(H)-\mathscr L_1(P)
=2p_2r_2+r_2^2-p_1r_3-p_3r_1-r_1r_3.
\]

Its absolute value is at most

\[
E_{\rm all}=2|p_2|\varepsilon_2+E_1<2\,10^{-12}.
\]

Since D_1^3+X_1^3=mathscr L_1(P) exactly, (12) gives the concrete paid
cross-term inequality throughout B:

\[
\boxed{\quad
X_1^3>-D_1^3+E_1+10^{-10}.
\quad}
\tag{14}
\]

Indeed 49/240000000000-E_all-E_1>10^(-10), verified by exact rational
arithmetic. This proves the proposed sufficient cross-term target for
j=1 on B and supplies a strict surplus. On the genuine stationary set
h_2=0, p_2=-r_2 and the general identity reduces precisely to

\[
\mathscr L_1(H)=D_1^3+X_1^3-r_2^2-p_1r_3-p_3r_1-r_1r_3.
\]

The first stationary set is empty on B because h_1<0. Formula (14)
assigns no separate sign to D_1^3 or X_1^3. All retained arithmetic
cross terms are accounted for by their exact identity with the finite
Laguerre polynomial; none is dropped or replaced by a diagonal sign.

## 5. Controls and precise remaining claim

The decisive additional property used in (9)--(12) is the quantitative
positive complete theta source, including its specific core mass and
superexponential full tail. Fueter regularity, smooth endpoint gluing,
and the heat equation alone do not give (9). The shifted controls
Q_2=(x-24)^2-2(t-1/40) and
Q_3=(x-24)^3-6(t-1/40)(x-24) have predecessor stationary loss
1/(1/40-t). In particular, Q_3 has L_1=-36(1/40-t)<0 on x=24,
where Q_3,xx=0. They do not have the positive integrable theta source
or the moment gap just paid. No general regularity-to-sign implication
is being made.

The rational replay is
[check_compensated_tail_and_signed_overlap.py](../numerics/check_compensated_tail_and_signed_overlap.py),
with its small
[execution record](../numerics/COMPENSATED_TAIL_AND_SIGNED_OVERLAP_20261014.json).
It checks constants and exact identities; the proof of their application
to the infinite source is the analytic argument above.

## 6. Completed validated stationary certificate on R+

The independent calculation
[certify_compensated_stationary_theta.py](../numerics/certify_compensated_stationary_theta.py)
and its
[execution certificate](../numerics/COMPENSATED_STATIONARY_THETA_CERTIFICATE_20261014.json)
complete the proposed bounded construction. The recorded run uses
python-flint 0.9.0, 256-bit Arb/Acb arithmetic, K=2, N=3, source cutoff
U=1, space Taylor order 12, time Taylor order 5, and Gaussian transform
Taylor order 24. The exact time interval has center 13/400 and radius
11/400; the spatial cover consists of all 34 closed unit cells
[7,8],...,[40,41], without gaps.

The retained raw-source jets are enclosed by validated Acb integration,
with (7) paying the entire U=1 integration tail. The complete Gaussian
transforms and their derivative recurrence are evaluated in ball
arithmetic; their spatial Taylor remainders are bounded by exact
Gaussian moments. Raw channels are transported using their heat
equation and positive source moment remainders before applying the
explicit time-dependent compensation. This retains residual (1), rather
than treating a compensated channel as a heat solution. Every cell
carries its actual Taylor payments and four-jet index errors.

For clarity, the parameter transport used in that calculation has the
following explicit form. For a spatial cell with center x_0 and radius
rho_x=1/2, let tau=t-13/400, eta=x-x_0, and
J_(n,k)=partial_x^k G_n(13/400,x_0). The finite raw-source polynomial is

\[
T_{n,k}(\tau,\eta)=
\sum_{\ell=0}^4\sum_{m=0}^{11}
\frac{(-\tau)^\ell\eta^m}{\ell!m!}J_{n,k+2\ell+m}.
\]

Write M_(n,r)(tmax)=int_0^infinity u^r g_(n,tmax)(u)du, with tmax=3/50.
The whole-cell remainder is bounded absolutely by R_(n,k)^x+R_(n,k)^t,
where

\[
R_{n,k}^x=
\sum_{\ell=0}^4\frac{(11/400)^\ell}{\ell!}
\frac{\rho_x^{12}}{12!}M_{n,k+2\ell+12}(t_{\max}),
\quad
R_{n,k}^t=\frac{(11/400)^5}{5!}M_{n,k+10}(t_{\max}).
\tag{17}
\]

The time Taylor theorem is applied first to the raw heat solution at
fixed x; each retained derivative is then expanded spatially. Absolute
positivity of the source, monotonicity in time, and |sin|,|cos|<=1
justify all moment majorants in (17). The moment quadratures themselves
include their complete source-integration tails. No time Taylor theorem
is applied to the compensated heat residual as though it vanished.

For the Gaussian observations put
I_m(x)=int_0^infinity u^m exp(-u^2+ixu)du. The exact entire transform
and recurrence are

\[
I_0=\frac{\sqrt\pi}{2}e^{-x^2/4}(1+i\operatorname{erfi}(x/2)),
\quad I_1=\frac{1+ixI_0}{2},
\quad I_{m+1}=\frac{mI_{m-1}+ixI_m}{2}\quad(m\ge1).
\]

Thus B_0^(k)=Re[i^k(I_(k+1)+I_(k+3))] and
B_1^(k)=Re[i^k I_(k+3)/6]. Each is expanded at x_0 through order 23.
Its order-24 remainder is bounded by

\[
R_{0,k}^{\beta}=
\frac{\rho_x^{24}}{24!}
\left(\mu_{k+25}+\mu_{k+27}\right),
\quad
R_{1,k}^{\beta}=
\frac{\rho_x^{24}}{24!}\frac{\mu_{k+27}}6,
\quad
\mu_r=\frac12\Gamma\left(\frac{r+1}{2}\right).
\tag{18}
\]

These are complete half-line Gaussian moments, so no Gaussian cutoff is
implicit. The linear factor e_n+6tb_n is then evaluated on the full time
interval. For the aggregate P_3, the summed endpoint coefficients are
combined before interval evaluation to retain their cancellation; the
three individual channel enclosures remain available for the explicit
diagonal and cross-term records.

Evaluating the same complete-index polynomial formula with tighter
validated transcendental constants gives tail-norm upper enclosures
approximately

\[
(5.14668\,10^{-10},\ 1.10612\,10^{-9},\
2.46557\,10^{-9},\ 5.69580\,10^{-9}).
\]

The decimal displays are descriptions only; the record stores outward
dyadic endpoints and uses those endpoints for every decision. These
tighter constants are compatible with the deliberately coarser rational
bounds (4)--(6). In the recorded run the maximum returned source-jet
quadrature radius is below 2.43*10^(-63), and the maximum separately paid
source-integration tail is below 8.36*10^(-73).

For j=0, the full genuine stationary derivative h_1 is rigorously
excluded from zero on 33 cells. The remaining cell [31,32] has a unique
regular stationary branch, uniform across the entire time interval.
For j=1, h_2 is excluded from zero on 32 cells; [9,10] and [34,35]
each contain a unique regular stationary branch. Endpoint signs and
strict next-derivative enclosures give existence and uniqueness at each
time, followed by analytic implicit-function continuation. There are no
unresolved sign cells and no unresolved branch-isolation cells.

On each retained stationary cell, the certificate checks the exact
correlated identity D_j^3+X_j^3=p_(j+1)^2-p_jp_(j+2), retaining and
recording every individual diagonal and cross term. It subtracts the
full stationary payment from Note 7. The final explicit surplus bounds
are

\[
h_1=0\quad\Longrightarrow\quad
X_0^3>-D_0^3+E_0+\frac1{2000000000},
\]
\[
h_2=0\quad\Longrightarrow\quad
X_1^3>-D_1^3+E_1+\frac1{100000000000},
\tag{15}
\]

where on each cell
E_j=epsilon_(j+1)^2+|p_j|epsilon_(j+2)+|p_(j+2)|epsilon_j
+epsilon_j epsilon_(j+2), with that cell's paid four-jet errors.
The stationary identity then yields on the whole closed R+

\[
h_1=0\Rightarrow\mathscr L_0(H)>5\,10^{-10},
\qquad
h_2=0\Rightarrow\mathscr L_1(H)>10^{-11}.
\tag{16}
\]

In particular H and H_x have no joint zero anywhere in closed R+:
at a joint zero the first Laguerre form would be zero, contradicting
(16). Evenness gives the same conclusion on the reflected negative
height rectangle. This covers the proposed R and its predecessor
neighborhoods. Neither this finite cover nor the analytic central
extension covers arbitrary possible collision heights.

The next obligation is a source-specific stationary signed bound uniform
at arbitrary heights, or a moving-domain family with rigorous coverage
of every possible collision predecessor. A fixed K=2 absolute x^(-4)
error cannot become a relative estimate by dividing by an unproved norm:
the complete theta observation is Schwartz, so its norm may decrease
much faster than this absolute payment. Increasing compensation order,
theta cutoff, precision, or parameter subdivisions must preserve a
signed surplus against the complete source at every step.

Even within the possible positive-threshold time range 0<t<=1/2, the
new certificate covers only 1/200<=t<=3/50 and |x|<=41 together with
the previously central |x|<=8 result. The time ranges 0<t<1/200 and
3/50<t<=1/2 at larger heights remain open, as do |x|>41 in the
certified time band. A numerical finite cover of R+ supplies a bounded
collision exclusion, not a global RH conclusion.
