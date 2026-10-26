# Arbitrary fixed order of the unconditional full-gamma saddle

26 October2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
verified from session metadata. Ansatz chat0005, thread
`01a178fa-8a72-7f23-9a7f-47e284eab9a3`, turn
`01a17917-3a6f-7600-8fed-0a290e3c243c`.

**Status: proved in-note from named inputs; same-model internal assessment
only.** This executes [AN03 r1][packet] and closes LT-03 at the arbitrary
fixed-order scope. [Notes17][n17]–[18][n18] are the first two worked orders.
The general finite remainder, complete source payments and exact residual
recurrence are proved here. Each order is fixed before the sufficient
onset and constants are chosen. No convergence, growing-order or optimal
truncation theorem is claimed. No numerical/symbolic/sampling campaign
was performed; provenance hashes are administrative.

Read [the result index][results], [heat-flow cluster][heat], [controls12][controls]
and [avoid index][avoid], particularly [classification][a01], [scope][a07],
[complete payments][a12] and [same-model limits][a05]. This is a quantitative
approximation theorem, not an RH criterion. No RH, initial all-real-zero
hypothesis, assumed Lambda, selected zero data or fitted carrier is used.
[Note20][bridge] separately starts the regional field bridge; neither
result supplies physical transfer or all-time/all-height assembly.

## 1. Quantifiers, source and theorem

Fix an integer J>=0 and fixed finite observation widths H0,Y0 and
analytic margin b>0. The field domain is
|Re z-x|<=H0+2b, |Im z|<=Y0+2b, for every real center x.
Spatial/time estimates are reported on the smaller rectangles with b
in place of2b. Keep the full canonical theta source and
\[
H_t=-H_{zz},\qquad H(0,z)=\xi((1+iz)/2)/8.
\]
Put
\[
X=|x|,\quad R=2+t+X,\quad L=\log R,\quad N=1+X+tL,
\quad n=2J+2,\quad s=(1+iz)/2.
\tag{FO1}
\]
For w=s,1-s retain precisely the branch from parent Note30 and
Notes17–18:
\[
M(p)=\frac{p(p-1)}{16}\pi^{-p/2}\Gamma(p/2),\quad
\alpha=(\log M)',\quad p=w+\frac t2\alpha(p),
\quad B=1-\frac t2\alpha'(p),
\]
\[
S=\mathcal S_t(w)=M(p)e^{-(p-w)^2/t}B^{-1/2},\quad
\mathcal A(t,z)=|\mathcal S_t(s)|+|\mathcal S_t(1-s)|>0.
\tag{FO2}
\]
The logarithm is real on p>1, and B^{-1/2} is near1. At a sufficient
onset, a=Re(p-w)>=tL/5, m=|p|≈N, |Im(p-w)|<=t,
|B-1|<=1/4 and m>=t. These facts hold uniformly on all fixed buffers,
including x=0, by contraction in a fixed right-half-plane sector.
They depend on no zero hypothesis.

The finite coefficients C2j are defined in Section2. Set
\[
P_{2J}(t,z)=\sum_{w=s,1-s}\mathcal S_t(w)
                  \sum_{j=0}^JC_{2j}(t,w),\qquad C_0=1,
\]
\[
b_J=e_n=\sum_{k=1}^{n}\frac{t^{n/2+k}}{N^{n+k}},\quad
\delta_J=b_J/t
 =\sum_{h=J+1}^{3J+2}\frac{t^h}{N^{h+J+2}},
\]
\[
A_{\rm ar}=R^{-\kappa t},\quad\kappa=\log2/8,\qquad
A_{\rm ct}=R^{b_0}e^{-ctL^2},\quad E_J=b_J+A_{\rm ar}+A_{\rm ct}.
\tag{FO3}
\]
Here b0 is a fixed middle-strip growth exponent. The fixed positive
contour rate c may be decreased to at most1/400. It can be chosen
independently of J; the finite polynomial-tail prefactor depends on J.

**Fixed-order theorem.** For each fixed J and the stated buffers there
are finite constants C_(J,d),Ct,J,Cr,J and R0,J such that, for every
t>=32 and R>=R0,J,
\[
|\partial_z^d(H-P_{2J})|\le C_{J,d}L^dE_J\mathcal A,
\qquad0\le d\le3,
\tag{FO4}
\]
\[
|(H-P_{2J})_t|\le C_{t,J}(L^2E_J+\delta_J)\mathcal A,
\quad |(\partial_t+\partial_{zz})P_{2J}|
                  \le C_{r,J}\delta_J\mathcal A.
\tag{FO5}
\]
The d=0 bound holds on the full larger domain. Real mixed spatial
derivatives have the same total-order bound by holomorphy. The constants
are specified by finite constructions below and named inherited source
constants; they have not been numerically instantiated.

There is a sufficient t_*,J, depending on J and the fixed buffers, for
which both omitted budgets are absorbable into bJ for all real x.
After enlarging constants for the finite n-term sums, for t>=t_*,J,
\[
\boxed{\sup_{x,z}\frac{|\partial_z^d(H-P_{2J})|}{\mathcal A}
 \le\frac{C_{J,d}}{t^{J+1}\log^{2J+3-d}(2+t)},\quad0\le d\le3,}
\]
\[
\boxed{\sup_{x,z}\frac{|(H-P_{2J})_t|}{\mathcal A}
 \le\frac{C_{t,J}}{t^{J+1}\log^{2J+1}(2+t)},\qquad
\sup_{x,z}\frac{|(\partial_t+\partial_{zz})P_{2J}|}{\mathcal A}
 \le\frac{C_{r,J}}{t^{J+2}\log^{2J+3}(2+t)}.}
\tag{FO6}
\]
Suprema use the declared fixed rectangles. They divide by a positive
amplitude envelope, never H or a signed model at its zeros. The logical
order is **for every fixed J, there exist constants and an onset**;
these statements cannot be used with J=J(t) without new estimates.

## 2. Finite partition formula and recurrence

Let f=log M, a_r=alpha^{(r)}(p), and
beta_r=a_(r+1)/(r+2)!, r>=1. For a nonnegative integer ell define
\[
\mathcal P_\ell=\{\nu=(\nu_1,\ldots,\nu_\ell)\in\mathbb Z_{\ge0}^{\ell}:
                  \sum r\nu_r=\ell\},\quad k=|\nu|=\sum\nu_r.
\]
The empty partition is P0, with k=0. Coefficient extraction of a
finite formal exponential gives
\[
A_\ell(u)=\sum_{\nu\in\mathcal P_\ell}
       u^{\ell+2k}\prod_r\frac{\beta_r^{\nu_r}}{\nu_r!},
\qquad
\ell A_\ell=\sum_{r=1}^{\ell}r\beta_ru^{r+2}A_{\ell-r}.
\tag{FO7}
\]
Each Aell is finite and has parity ell. With (-1)!!=1, its normalized
complex Gaussian moment is zero for odd ell, while
\[
\boxed{C_{2j}=
\sum_{\nu\in\mathcal P_{2j}}
 \frac{(2j+2k-1)!!}{2^{j+k}}
 \left(\frac tB\right)^{j+k}
 \prod_r\frac{a_{r+1}^{\nu_r}}{(r+2)!^{\nu_r}\nu_r!}.}
\tag{FO8}
\]
This includes C0=1. The first two nonconstant instances are exactly
C2 and C4 in Notes17–18. Formula FO8 defines each finite approximation;
it does not assert a convergent infinite sum of corrections.

## 3. Indexed finite remainder constants

Take a fixed larger exterior sector containing the right half-plane
segments used below. The classical [DLMF5.11][gamma] sectorial remainder
and Cauchy's formula provide
\[
|\alpha^{(r)}(q)|\le K_r|q|^{-r},\quad1\le r\le n+1.
\tag{FO9}
\]
For example, if alpha(q)=Log(q/(2pi))/2+g(q), |g(q)|<=G/|q|,
use disks of radius |q|/4 in the larger sector. Once all their points
are in |q|>=m0, the finite sufficient choice
\[
K_r=\tfrac12(r-1)!+\tfrac43G\,4^rr!/m_0
\tag{FO10}
\]
follows from |g^(r)(q)|<=(4G/3)4^r r!|q|^{-r-1}. All quantities
needed for a fixed J are finite. Exposing this family does not supply
an optimal or useful growing-order theorem.

On the actual horizontal central segment U=[-a/2,a/2], enlarge the
onset so |p+r lambda u|>=m/3 for 0<=r,lambda<=1. Introduce
\[
E_\lambda(u)=u^2\int_0^1(1-r)
       [f''(p+r\lambda u)-f''(p)]dr.
\tag{FO11}
\]
At lambda=1 it is the exact nonquadratic exponent from the shifted
canonical gamma arm, and at lambda=0 it vanishes. Its derivatives at
zero give exactly FO7. For 1<=r<=n,
\[
|\partial_\lambda^rE_\lambda|
 \le d_r\frac{|u|^{r+2}}{m^{r+1}},\qquad
 d_r=\frac{3^{r+1}K_{r+1}}{(r+1)(r+2)}.
\tag{FO12}
\]
Moreover
\[
-\frac{Bu^2}{t}+E_\lambda
=-\frac{u^2}{t}+u^2\int_0^1(1-r)f''(p+r\lambda u)dr.
\]
The sufficient condition 3K1 t/(2m)<=1/2 therefore gives
\[
|e^{-Bu^2/t+E_\lambda}|\le e^{-u^2/(2t)}
\tag{FO13}
\]
for every lambda in[0,1]. This bounds the exponential factor in the
Taylor remainder without assuming E is small on all of U.

Define the finite positive Bell constants
\[
D_{n,k}=\sum_{\substack{\nu\in\mathcal P_n\\|\nu|=k}}
           \prod_{r=1}^{n}\frac{(d_r/r!)^{\nu_r}}{\nu_r!},
\quad1\le k\le n.
\tag{FO14}
\]
Real Taylor's theorem for exp(E_lambda) through degree n-1, with
its nth-derivative integral remainder, now proves
\[
\left|e^{-Bu^2/t}
 \left(e^{E_1}-\sum_{\ell=0}^{n-1}A_\ell\right)\right|
\le e^{-u^2/(2t)}\sum_{k=1}^{n}D_{n,k}
                       \frac{|u|^{n+2k}}{m^{n+k}}.
\tag{FO15}
\]
Indeed each Bell monomial with k factors and total derivative order n
has these powers; the n! in that polynomial cancels the Taylor n!
denominator. All differentiation is finite. Only alpha derivatives
through n+1=2J+3 are required.

With
\[
G_v(\eta)=\frac{(2v-1)!!}{2^v\eta^{v+1/2}},\qquad
(\pi t)^{-1/2}\int_{\mathbb R}u^{2v}e^{-\eta u^2/t}du
=G_v(\eta)t^v,
\]
and m>=c_m N, one sufficient local per-arm constant is
\[
C_{{\rm loc},J}=\max_{1\le k\le n}
 \sqrt{5/4}\,D_{n,k}G_{n/2+k}(1/2)c_m^{-n-k}.
\tag{FO16}
\]
Thus the central remainder divided by |S| is at most C_loc,J bJ.
The square-root factor converts the saddle prefactor to S.

Odd grades cancel exactly on the actual symmetric U. Only the retained
even polynomials A0,A2,...,A2J are extended to full Gaussian moments.
Their maximum degree is6J. Put b_r=K_(r+1)/(r+2)! and
\[
Q_J=\sum_{j=0}^{J}\sum_{\nu\in\mathcal P_{2j}}
       G_{j+k}(3/8)\prod_r\frac{b_r^{\nu_r}}{\nu_r!}.
\tag{FO17}
\]
Since Re B>=3/4 and m>=t>=1, their total omitted tails, relative to
|S|, are at most
\[
\sqrt{5/4}\,Q_Je^{-3a^2/(32t)}
 \le\sqrt{5/4}\,Q_Je^{-tL^2/400}.
\tag{FO18}
\]
Split the Gaussian into two equal factors; one pays |u|>=a/2 and
the other pays the full finite moments. Each remaining factor
 t^(j+k)/m^(2j+k) is<=1. No actual gamma integrand is extended past
its allowed contour or through its poles. The true noncentral pieces
are paid next, independently of parity.

## 4. Complete canonical source and order-dependent onset

The unconditional exact anchor, [Polymath v2 equation35][poly], is
\[
H(t,z)=(\pi t)^{-1/2}\int_{\mathbb R}
 e^{-v^2/t}\xi(s+v)/8\,dv.
\tag{FO19}
\]
The normalization xi/8=M zeta is exact. Split at Re(s+v)=2,-1,
reflect the left arm using xi(w)=xi(1-w), and keep the bounded middle.
Shift each right arm to Im v=Im(p-w), with its oriented connector.
Every shifted ray and connector stays in Re(w+v)>=2, where the
full ordinary Dirichlet series converges. No pole is crossed. The
finite far-right face vanishes before the infinite ray is asserted;
the reflected ray pays the other original infinite end.

These are the unchanged complete payments from Note17 Sections4–5
and Note18 Section4:

| Piece | Bound relative to its own arm |
| --- | --- |
| Central local truncation | C_loc,J bJ, by FO15–16 |
| Retained even-polynomial moment tails | Explicit FO17–18 |
| Actual infinite right ray outside the central segment | C exp(-c tL²), by the whole-ray quadratic gamma majorant |
| Remaining left horizontal segment | C exp(-c tL²), from exp(-d²/t+C Re p), d>=a/2 |
| Each connector, including length and the collapsed case | C exp(-c tL²), retaining its exp(Ct) gamma motion |
| Full n>=2 ordinary Dirichlet remainder on the central/right ray | C_ar R^(-kappa t) |
| All arithmetic on remaining segments/connectors | Included using bounded zeta on Re>=2 |
| Original bounded middle | C R^b0 exp(-c tL²), retaining fixed-strip growth and compact bounded-height behavior |

The local whole-ray Gaussian estimate uses the quadratic log-gamma
integral bound, not a cubic Taylor approximation at arbitrarily large u.
The left comparison loses only C Re p, dominated by tL²; connector
motion costs exp(Ct). Middle compactness avoids using high-height
Stirling at x=0. None of those estimates depends on J. The only new
noncentral prefactor is the finite QJ. An explicit prefactor for the full Dirichlet tail on the central/right
portion, for Re w>=-Sigma, is
C_ar=3·2^Sigma sqrt(5/2), after including L>=20log2/3 in the onset,
by Note18 SC22. This pays every omitted n>=2, not a finite selection.
Summing both arms and the middle proves FO4 at d=0 with all three
budgets visible. Generic simple-saddle expansion citations do not replace
these canonical payments.

To absorb the two omitted budgets, use N<=C_N R L and choose L0,J
beyond all fixed branch/sector/buffer conditions, m>=t, FO13 and the
finite polynomial-tail thresholds. Increase it past turning points so,
for every L>=L0,J,
\[
C_N^{n+1}L^{n+1}e^{-L}\le1,\qquad
C_N^{n+1}L^{n+1}e^{(b_0+n+1)L-32cL^2}\le1.
\tag{FO20}
\]
A sufficient symbolic choice is
\[
t_{*,J}\ge\max\{32,(n+2)/\kappa,e^{L_{0,J}}\}.
\tag{FO21}
\]
Then kappa t>=n+2 and bJ>=t^(n/2+1)/N^(n+1) give
\[
A_{\rm ar}/b_J\le C_N^{n+1}t^{-n/2-1}
                  L^{n+1}R^{n+1-\kappa t}\le1,
\]
\[
A_{\rm ct}/b_J\le C_N^{n+1}t^{-n/2-1}L^{n+1}
             e^{(b_0+n+1)L-ctL^2}\le1.
\tag{FO22}
\]
Their fixed prefactors stay in the final constant, or can instead be
included in FO20. No displayed arithmetic floor is a numerical onset.
For the joint t>=32 theorem retain both budgets rather than incorrectly
absorb them at arbitrary order. This is a limitation of that coarse
upper bound at smaller fixed times, not a true-error lower bound.
The compact-time refinement in Note20 changes this payment on its
own fixed domain; it does not silently alter FO21's global quantifiers.

## 5. Finite formal proof of the exact residual recurrence

The moving-saddle product identity from Note18 is
\[
S^{-1}(\partial_t-\tfrac14\partial_{ww})(SF)
=(\partial_t|_p-Q)F,
\]
\[
Q=\frac1{4B^2}\partial_{pp}
 +\frac{t a_2}{4B^3}\partial_p+k_0,\qquad
k_0=\frac{t a_3}{16B^3}+\frac{5t^2a_2^2}{64B^4}.
\tag{FO23}
\]
It follows directly from p_w=B^{-1}, p_t=alpha/(2B) and
(log S)_w=alpha+t a2/(4B²). No finite truncation solves heat
merely by its definition.

We prove the coefficient identity, rather than extrapolate it from C2,C4.
Let rho=t/B and define the polynomial Gaussian functional
\[
\mathcal G_\rho[u^{2v}]=(2v-1)!!(\rho/2)^v,
\qquad \mathcal G_\rho[u^{2v+1}]=0.
\]
For polynomials F, finite moment identities give
\[
\mathcal G_\rho(uF)=\tfrac\rho2\mathcal G_\rho(F_u),\quad
\mathcal G_\rho(u^2F)=\tfrac\rho2\mathcal G_\rho F
                    +\tfrac{\rho^2}4\mathcal G_\rho(F_{uu}),
\]
\[
\partial_\rho\mathcal G_\rho F
                         =\tfrac14\mathcal G_\rho(F_{uu})
\quad\text{when F is rho-independent}.
\tag{FO24}
\]
They may be checked monomial by monomial. No integration of an
uncontrolled infinite gamma expansion occurs.

Use a formal variable lambda and write, coefficientwise,
\[
g_\lambda(u)=\exp\left(\sum_{r\ge1}
       \frac{a_{r+1}u^{r+2}}{(r+2)!}\lambda^r\right),\quad
\mathcal C_\lambda=\mathcal G_\rho g_\lambda
                         =\sum_{j\ge0}C_{2j}\lambda^{2j}.
\tag{FO25}
\]
Every lambda coefficient is a finite polynomial. For any particular
identity read these expressions modulo a sufficiently high finite power
of lambda; convergence at lambda=1 is not an assumption.
The coefficient identities
\[
g_{\lambda,u}=\lambda g_{\lambda,p}
                  +\lambda a_2u^2g_\lambda/2,
\quad \rho_p=a_2\rho^2/2,\quad \rho_t|_p=B^{-2}
\tag{FO26}
\]
are exact. The p derivative of the Gaussian functional includes its
rho dependence; this is essential. Put h=rho a2/4. Applying FO24
and cancelling the rho_p term gives
\[
\mathcal G_\rho(g_{\lambda,u})
       =\lambda(\mathcal C_{\lambda,p}+h\mathcal C_\lambda).
\tag{FO27}
\]
Differentiate FO26 in u and apply the same finite moment identities:
\[
\mathcal G_\rho(g_{\lambda,uu})
=\lambda\partial_p\mathcal G_\rho(g_{\lambda,u})
 +3\lambda h\mathcal G_\rho(g_{\lambda,u})
\]
\[
=\lambda^2\{\mathcal C_{\lambda,pp}
 +4h\mathcal C_{\lambda,p}+(h_p+3h^2)\mathcal C_\lambda\},
\quad h_p+3h^2=\rho a_3/4+5\rho^2a_2^2/16.
\tag{FO28}
\]
At fixed p, g_lambda is t-independent, so FO24 and rho_t give
\[
\boxed{\partial_t|_p\mathcal C_\lambda=\lambda^2Q\mathcal C_\lambda,
\qquad \partial_t|_p C_{2j+2}=QC_{2j}.}
\tag{FO29}
\]
Only finitely many coefficients are involved at any extracted degree.
For FJ=sum_(j=0..J)C2j, finite telescoping in FO23 yields
\[
\boxed{(\partial_t+\partial_{zz})P_{2J}
            =-\sum_{w=s,1-s}\mathcal S_t(w)QC_{2J}.}
\tag{FO30}
\]
Both affine w(z) arms have (w_z)²=-1/4. FO29 is an exact
coefficient identity; FO30 is the actual residual of the finite analytic
model, not a statement about an infinite formal heat solution.

## 6. Indexed residual majorants and derivatives

Group FO8 at j=J as
\[
C_{2J}=\sum_\nu t^\nu B^{-\nu}U_{J,\nu}(a_2,a_3,\ldots),
\]
\[
U_{J,\nu}=\sum_{\substack{\ell\in\mathcal P_{2J}\\|\ell|=\nu-J}}
 \frac{(2\nu-1)!!}{2^\nu}
 \prod_r\frac{a_{r+1}^{\ell_r}}{(r+2)!^{\ell_r}\ell_r!}.
\tag{FO31}
\]
For J>=1 the index range is J+1<=nu<=3J; U0,0=1 and all
other out-of-range U are zero. These are finite positive-coefficient
polynomials, homogeneous of weight nu+J when a_r has weight r.
Let mathfrak d be the finite jet derivation d a_r=a_(r+1). Direct
product rules with B_p=-t a2/2 give
\[
\begin{split}
Q[t^\nu B^{-\nu}U]={}&\frac{t^\nu\mathfrak d^2U}{4B^{\nu+2}}
 +\frac{(\nu+1)t^{\nu+1}a_2\mathfrak dU}{4B^{\nu+3}}\\
 &+\frac{(2\nu+1)t^{\nu+1}a_3U}{16B^{\nu+3}}
 +\frac{(2\nu+1)(2\nu+5)t^{\nu+2}a_2^2U}{64B^{\nu+4}}.
\end{split}
\tag{FO32}
\]
This generalizes the explicit finite C2/C4 residual calculations without
needing a new expanded list at every order.

Put Khat_r=K_r c_m^{-r}, beta=4/3, so |a_r|<=Khat_r N^{-r}
and |B^{-1}|<=beta. For J+1<=q<=3J+2 define the finite constants
\[
\begin{split}
V_{J,q}=\beta^{q+2}\{&\tfrac14(\mathfrak d^2U_{J,q})(\widehat K)
 +\tfrac q4\widehat K_2(\mathfrak dU_{J,q-1})(\widehat K)\\
 &+\tfrac{2q-1}{16}\widehat K_3U_{J,q-1}(\widehat K)
 +\tfrac{(2q-3)(2q+1)}{64}\widehat K_2^2U_{J,q-2}(\widehat K)\}.
\end{split}
\tag{FO33}
\]
Positivity of the polynomial coefficients and their weights show that
QC2J is bounded by sum_q V_(J,q)t^q/N^(q+J+2).
Thus Cr0,J=max_q V_(J,q) suffices for the deltaJ bound in FO5;
a factor at most n suffices when converting that finite sum to the
supremum in FO6 for L>=1. Only K through2J+3 are needed. J=0
also works: U0,0=1 supplies the two terms of k0. This pays the
actual residual independently of the field proof.

For each fixed J the residual is nonzero eventually at x=z=0.
By FO29 and the single-factor leading coefficient of C2J+2, QC2J
has the positive leading term
\[
\frac{t^{J+1}\alpha^{(2J+3)}(p)}
 {4^{J+2}(J+1)!B^{J+3}}
=\frac{(2J+2)!}{2\,4^{J+2}(J+1)!}
 \frac{t^{J+1}}{p^{2J+3}}\{1+o(1)\}.
\tag{FO34}
\]
Here p and S are positive real at zero, so the two residual arms do
not cancel. A smaller residual is not used as a stability theorem.

For spatial derivatives, apply Cauchy to the complete holomorphic
field difference on disks of radius c_d/L within the paid buffers.
Each carrier modulus and error scale changes by a fixed factor on
these disks, because |(log S)_w|<=C L. This gives the L^d losses
in FO4; no real-axis O estimate is differentiated. The exact original
convolution gives H_t=-H_zz by local kernel differentiation and two
integrations by parts. Consequently
\[
(H-P_{2J})_t=-(H-P_{2J})_{zz}
                         -(\partial_t+\partial_{zz})P_{2J}.
\tag{FO35}
\]
FO4 with d=2 and the computed residual prove FO5. Artificial moving
split/saddle/localization endpoints are absent because the original
fixed contour is differentiated before splitting. Odd local moments
are not incorrectly discarded under a time-kernel multiplier. No
arbitrary-data backward-heat contraction or field-error propagation
from the residual is used.

Finally bJ<=n t^(-J-1)L^(-2J-3) and deltaJ<=n t^(-J-2)L^(-2J-3)
for L>=1, by N>=tL. The exponents d-2J-3 are nonpositive for
J>=0,d<=3. Monotonicity in L>=log(2+t) proves all uniform
suprema in FO6 with the stated finite-sum enlargement.

## 7. Fixed-height limits, balances and scope

For each fixed j>=1, the single-factor partition in FO8 dominates:
\[
C_{2j}=\frac{(2j)!}{2^{2j+3}(j+1)!}
 \frac{t^{j+1}}{p^{2j+1}}
 \{1+O_j(t/m+m^{-1})\}.
\tag{FO36}
\]
This uses alpha^(2j+1)=(2j)!/(2p^(2j+1))+O_j(m^(-2j-2));
other partitions carry extra t/m factors. At fixed x and bounded
transverse coordinate, p=(t/4)log t·(1+o(1)), so
\[
C_{2j}=\frac{2^{2j-1}(2j)!}{(j+1)!}
       t^{-j}\log^{-2j-1}t\,(1+o(1)).
\tag{FO37}
\]
This recovers2 and32 for the first two fixed-height coefficients.
It describes an arm coefficient, not the signed two-arm field error.

| Balance | Error allowance bJ | Direct-time allowance | Residual allowance |
| --- | --- | --- | --- |
| X much smaller than tL, or comparable with fixed comparison constants | t^(-J-1)L^(-2J-3) | t^(-J-1)L^(-2J-1) | t^(-J-2)L^(-2J-3) |
| X much larger than tL | t^(J+2)/X^(2J+3) | t^(J+2)L²/X^(2J+3) | t^(J+1)/X^(2J+3) |

Spatial order d adds L^d. Fixed-height statements and all-height
suprema are distinct, and both are proved. For fixed J, successive
complete allowances after their own absorptions improve by
\[
b_{J+1}/b_J\le C_J t/N^2
                    \le C_J/[t\log^2(2+t)]\longrightarrow0.
\tag{FO38}
\]
J=0 is also new quantitative information: the leading full saddle
alone has a paid parity-improved allowance t²/N³+t³/N⁴, giving
O(t^-1 log^-3 t) uniformly in height. This strengthens Note30's
valid but coarser absolute-cubic bound. J=1 and2 recover Notes17–18.
None of these estimates is relative error divided by H at zeros.

The canonical-control premise screen is unchanged: Euler-factor controls
alter ordinary arithmetic/completion; weighted-square/finite-tail controls
lack the same complete xi identity; reflected/smooth/positive-primitive
controls lack the canonical M times ordinary-zeta source; finite-prime
controls lack full canonical reflection/arithmetic; atomic/finite-profile,
counter-kernel and two-channel controls lack the complete theta source;
RH-conditional normalized-endpoint perturbations lack unaltered Dirichlet
arithmetic. Generic Gaussian recurrence and heat structure exclude none
of them. No collision or RH conclusion follows from this approximation.

[Input record][inputs] and [Assessment14][review] retain working-tree
provenance and same-model review limits. **AN03 r1 CLOSED; LT-03 Complete
at arbitrary fixed order.** Broad HDA-A04 remains Partial because regional
coverage and physical consumers remain. LT-04 growing/optimal order stays
open and was not executed. [Note20][bridge] records the first actual
compact-positive field bridge and its remaining core/physical gaps.

[packet]: ../research-progress/handoffs/HDA-A04-AN03.md
[overview]: ../research-overview/03_LARGE_POSITIVE_TIME_HIERARCHY_RESEARCH_OVERVIEW_20261026.md
[progress]: ../research-progress/03_LARGE_POSITIVE_TIME_HIERARCHY_RESEARCH_PROGRESS_20261026.md
[n17]: 17_FIRST_CORRECTED_LARGE_POSITIVE_TIME_20261026.md
[n18]: 18_SECOND_CORRECTED_LARGE_POSITIVE_TIME_20261026.md
[bridge]: 20_COMPACT_POSITIVE_FIELD_BRIDGE_20261026.md
[inputs]: 19_FIXED_ORDER_AND_BRIDGE_INPUTS_20261026.json
[review]: ../reviews/14_ARBITRARY_FIXED_ORDER_ASSESSMENT_20261026.md
[poly]: https://arxiv.org/html/1904.12438v2#S4
[gamma]: https://dlmf.nist.gov/5.11
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a05]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
