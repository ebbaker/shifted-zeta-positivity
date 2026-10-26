# Second fixed full-gamma correction at large positive time

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
verified in current session metadata. Same ansatz chat0005, thread
`01a178fa-8a72-7f23-9a7f-47e284eab9a3`, turn
`01a17909-083b-7ee1-87cc-9f5b9d884c6e`.

**Status: proved in-note from named inputs; same-model internal assessment
only.** This executes [AN02 r1][packet] under [Overview03][overview] and
[Progress03][progress], following [Note17][n17]. One second fixed-order
correction closes with a complete smaller error. The finite constants,
all nonlocal payments, buffered derivatives, direct first-time comparison
and actual nonzero residual are specified below. Onset remains symbolic.
There is no numerical, machine-symbolic, exact-arithmetic or sampling
campaign; file hashes/history checks are administrative provenance.

Read [the result index][results], [heat-flow cluster][heat], [controls12][controls]
and [avoid index][avoid], specifically [avoid01][a01], [scope][a07],
[complete payments][a12] and [same-model limits][a05]. This is an
approximation milestone, not an RH criterion. No RH, initial all-real
zeros, assumed Lambda value, fitted carrier or selected root data is used.
Regional bridges and physical transfer remain deferred. The arbitrary
fixed-order theorem is still broader than the two worked corrections.

## 1. Contract and quantitative statement

Keep the exact complete theta source, H_t=-H_zz and
H(0,z)=xi((1+iz)/2)/8. Write
\[
X=|x|,\quad R=2+t+X,\quad L=\log R,\quad N=1+X+tL,
\quad s=(1+iz)/2.
\tag{SC1}
\]
Use precisely the same fixed observation widths and full analytic buffers
as Note17 Section1: field estimates on
|Re z-x|<=H0+2b, |Im z|<=Y0+2b, and derivatives on the smaller
rectangles with b in place of2b, for fixed finite H0,Y0 and b>0.
All constants depend only on these fixed data and the named finite
sectorial/source constants, not on t or x.

For w=s,1-s retain the selected large branch
\[
M(p)=\frac{p(p-1)}{16}\pi^{-p/2}\Gamma(p/2),\quad
\alpha=(\log M)',\quad p=w+\frac t2\alpha(p),\quad
B=1-\frac t2\alpha'(p),
\]
\[
S=\mathcal S_t(w)=M(p)e^{-(p-w)^2/t}B^{-1/2},\quad
\mathcal A(t,z)=|\mathcal S_t(s)|+|\mathcal S_t(1-s)|.
\tag{SC2}
\]
Log M is the branch real on p>1; B^{-1/2} is near1. Note17's
branch proof gives m=|p|≈N, a=Re(p-w)≈tL, a>=tL/5 and
|Im(p-w)|<=t. Include its sufficient onset so |B-1|<=1/4.
No change of source, branch, normalization or envelope is made.

Put a_j=alpha^{(j)}(p) for j>=1. Retain C2 from Note17 and set
\[
\boxed{\begin{split}
C_4={}&\frac{t^3a_5}{384B^3}
 +\frac{t^4}{B^4}\left(\frac{7a_2a_4}{768}
                       +\frac{35a_3^2}{6144}\right)\\
 &+\frac{35t^5a_2^2a_3}{2048B^5}
 +\frac{385t^6a_2^4}{73728B^6},\qquad
P_4(t,z)=\sum_{w=s,1-s}\mathcal S_t(w)(1+C_2+C_4).
\end{split}}
\tag{SC3}
\]
Define
\[
e_6=\sum_{k=1}^{6}\frac{t^{k+3}}{N^{k+6}},\qquad
\delta_4=e_6/t=\sum_{n=3}^{8}\frac{t^n}{N^{n+4}},
\]
\[
A_{\rm ar}=R^{-\kappa t},\quad\kappa=\log2/8,\qquad
A_{\rm ct}=R^{b_0}e^{-ctL^2},\quad E_6=e_6+A_{\rm ar}+A_{\rm ct}.
\tag{SC4}
\]
The fixed b0 and c>0 are the enlarged-domain middle exponent and
contour rate, decreased once if necessary for the finite polynomial tails.

**Second fixed-order theorem.** For t>=32 and R above one sufficient
symbolic R0, the complete field and its buffered derivatives obey
\[
|\partial_z^j(H-P_4)|\le C_j L^j E_6\mathcal A,
\quad 0\le j\le3,
\tag{SC5}
\]
\[
|(H-P_4)_t|\le C_t(L^2E_6+\delta_4)\mathcal A,\qquad
|(\partial_t+\partial_{zz})P_4|\le C_r\delta_4\mathcal A.
\tag{SC6}
\]
The j=0 field estimate holds on the full larger rectangle. Real mixed
spatial derivatives obey the same total-order bound by holomorphy.
The finite local and residual constants are given in Sections3 and5;
global source constants are inherited with every piece retained in Section4.

For a symbolic sufficient t_*, independent of real x, A_ar+A_ct
is absorbable into e6. For t>=t_*, uniformly over real centers x and
z in their respective fixed rectangles, after enlarging the reported
constants to convert the six-term sums to dominant powers,
\[
\sup_{x,z}\frac{|\partial_z^j(H-P_4)|}{\mathcal A}
 \le\frac{C_j}{t^3\log^{7-j}(2+t)},\quad0\le j\le3,
\]
\[
\boxed{\sup_{x,z}\frac{|(H-P_4)_t|}{\mathcal A}
 \le\frac{C_t}{t^3\log^5(2+t)},\qquad
\sup_{x,z}\frac{|(\partial_t+\partial_{zz})P_4|}{\mathcal A}
 \le\frac{C_r}{t^4\log^7(2+t)}.}
\tag{SC7}
\]
These are carrier-envelope bounds, including at zeros of H or P4.
P4 is not an exact heat solution. No physical observable theorem follows
here just by substituting the new field bound into an old observable rate.

## 2. Finite coefficient algebra

Let f=log M and beta_r=f^{(r+2)}(p)/(r+2)!. The finite recurrence
\[
A_0=1,\qquad jA_j=\sum_{r=1}^j r\beta_r u^{r+2}A_{j-r}
\tag{SC8}
\]
is Note17 LT14. Its grade4 polynomial is
\[
A_4=\beta_4u^6+(\beta_1\beta_3+\beta_2^2/2)u^8
 +\tfrac12\beta_1^2\beta_2u^{10}
 +\tfrac1{24}\beta_1^4u^{12}.
\tag{SC9}
\]
The normalized full-line complex Gaussian moments are
mu_{2k}=(2k-1)!!(t/B)^k/2^k, mu_{2k+1}=0. Substituting SC9
gives exactly the five monomials in SC3. The coefficients come from
the five partitions4,3+1,2+2,2+1+1,1+1+1+1. This is finite algebra;
there is no convergence claim for an infinite expansion. Odd Aj has
odd parity because every monomial has degree j plus twice its number
of factors. Its use on the actual contour is proved next.

## 3. Finite local constants and sixth-grade remainder

On the fixed larger sector let
\[
|\alpha^{(j)}(q)|\le K_j|q|^{-j},\quad1\le j\le7.
\tag{SC10}
\]
Only these seven finite constants are needed. [DLMF5.11][gamma] gives
the log-Gamma/digamma sectorial remainder; Cauchy on an enlarged
sector gives SC10. For an explicit way to expose this dependence,
write alpha(q)=Log(q/(2pi))/2+g(q), |g(q)|<=G/|q|. For large
q in the right half-plane, the disk of radius |q|/4 stays in a fixed
larger sector, away from the poles/zeros. If its points have modulus
at least m0, Cauchy gives the sufficient finite choice
\[
K_j=\tfrac12(j-1)!+\tfrac43G\,4^j j!/m_0,
\quad1\le j\le7.
\tag{SC11}
\]
Enlarge the branch onset so this exterior-sector condition holds on
all segments used below. This is a constructive choice in fixed input
constants, not a numerical certificate or a uniform-in-order theorem.

Use the actual shifted horizontal central segment
J=[-a/2,a/2], v=p-w+u with real u. Enlarge onset until
|p+r lambda u|>=m/3 for u in J and 0<=r,lambda<=1, and m>=t>=1.
Define the finite real-parameter interpolation
\[
E_\lambda(u)=u^2\int_0^1(1-r)
 [f''(p+r\lambda u)-f''(p)]dr,\quad0\le\lambda\le1.
\tag{SC12}
\]
At lambda=1 this is exactly the nonquadratic exponent E_p(u) of
Note17 LT15, and E0=0. More explicitly, the finite lambda derivatives
at zero give E_lambda=sum beta_r u^{r+2}lambda^r to each required
Taylor order. Thus the coefficients of exp(E_lambda) at zero are
precisely Aj in SC8, through j=5. A complex analytic continuation of
this interpolation parameter is not needed for the real Taylor theorem.

For 1<=j<=6,
\[
\partial_\lambda^jE_\lambda
 =u^{j+2}\int_0^1(1-r)r^j f^{(j+2)}(p+r\lambda u)dr,
\quad
|\partial_\lambda^jE_\lambda|
 \le d_j|u|^{j+2}/m^{j+1},
\]
\[
d_j=\frac{3^{j+1}K_{j+1}}{(j+1)(j+2)}.
\tag{SC13}
\]
The exponent itself has the exact quadratic-integral expression
\[
-\frac{Bu^2}{t}+E_\lambda
=-\frac{u^2}{t}+u^2\int_0^1(1-r)f''(p+r\lambda u)dr.
\]
Consequently the sufficient condition 3K1 t/(2m)<=1/2 implies
\[
|e^{-Bu^2/t+E_\lambda}|\le e^{-u^2/(2t)}
\quad(0\le\lambda\le1,u\in J).
\tag{SC14}
\]
This pays the full Taylor remainder's exponential factor uniformly.
It does not assume pointwise smallness of E on all of J.

The sixth derivative of exp(E_lambda) is its exponential times the
finite sixth Bell polynomial. Taylor's integral remainder through
lambda degree5 therefore gives the explicit weighted bound
\[
\left|e^{-Bu^2/t}\left(e^{E_1}-\sum_{j=0}^5A_j\right)\right|
\le e^{-u^2/(2t)}\sum_{k=1}^6D_k\frac{|u|^{6+2k}}{m^{6+k}},
\tag{SC15}
\]
where
\[
\begin{array}{ll}
D_1=d_6/720,&D_2=d_1d_5/120+d_2d_4/48+d_3^2/72,\\
D_3=d_1^2d_4/48+d_1d_2d_3/12+d_2^3/48,
&D_4=d_1^3d_3/36+d_1^2d_2^2/16,\\
D_5=d_1^4d_2/48,&D_6=d_1^6/720.
\end{array}
\tag{SC16}
\]
Indeed a partition of6 into k positive derivative orders contributes
exactly the power |u|^{6+2k}/m^{6+k}; the factorials in the Bell
polynomial cancel the1/6! in the Taylor remainder bound. SC16 lists
all eleven finite partition monomials. This argument bypasses the
uncontrolled high-degree products that would arise from expanding an
exponential without retaining its weighted remainder.

For eta>0 put
\[
G_n(\eta)=\frac{(2n-1)!!}{2^n\eta^{n+1/2}},\quad
\frac1{\sqrt{\pi t}}\int_{\mathbb R}u^{2n}e^{-\eta u^2/t}du
=G_n(\eta)t^n,
\tag{SC17}
\]
with (-1)!!=1. If m>=c_m N, the local integral divided by its own
|S| is bounded by
\[
\sum_{k=1}^6\sqrt{5/4}\,D_kG_{k+3}(1/2)c_m^{-k-6}
\frac{t^{k+3}}{N^{k+6}}\le C_{\rm loc}e_6,
\]
\[
C_{\rm loc}=\max_{1\le k\le6}
 \sqrt{5/4}\,D_kG_{k+3}(1/2)c_m^{-k-6}.
\tag{SC18}
\]
The square-root factor converts the original saddle prefactor to S.

The odd A1,A3,A5 vanish only on the actual symmetric J against its
even complex Gaussian. Extend only A0+A2+A4 to full-line moments;
their maximum polynomial degree is12. Here is a finite tail constant.
Let H_n=G_n(3/8) and use the same K_j at p. Since m>=t>=1 and
Re B>=3/4, the normalized omitted polynomial tails are at most
\[
\sqrt{5/4}\,Q_{\rm tail}e^{-3a^2/(32t)},
\tag{SC19}
\]
where
\[
\begin{split}
Q_{\rm tail}={}&H_0+\frac{K_3}{24}H_2
 +(\frac{K_2^2}{72}+\frac{K_5}{720})H_3\\
 &+(\frac{K_2K_4}{720}+\frac{K_3^2}{1152})H_4
 +\frac{K_2^2K_3}{1728}H_5+\frac{K_2^4}{31104}H_6.
\end{split}
\tag{SC20}
\]
Split exp(-3u²/(4t)) into two equal Gaussian factors, use
|u|>=a/2 in one and full moments for the other; each remaining
t^k/m^j factor is<=1. This proves SC19. Only finite Gaussian
polynomials have been extended past J. The actual gamma integrand
outside J is not extended into a region with poles.

## 4. Complete source and all nonlocal payments

Use the exact unconditional convolution
\[
H(t,z)=\frac1{\sqrt{\pi t}}\int_{\mathbb R}
 e^{-v^2/t}\frac{\xi(s+v)}8\,dv.
\tag{SC21}
\]
Its normalization was checked in [Polymath v2 equation35][poly] and
in Note17. Split at Re(s+v)=2,-1, reflect the left arm exactly, and
retain the bounded middle. Each arm is the integral of
exp(-v²/t)M(w+v)zeta(w+v), v>=2-Re w, divided by sqrt(pi t).
Shift to Im v=Im(p-w), retaining its oriented connector. Every
shifted ray and connector has Re(w+v)>=2. No gamma singularity
or zeta pole is crossed; first close a finite rectangle and then
let the far vertical face vanish. The reflected arm pays the other
original infinite end. These operations are unchanged by C4.

The complete contour ledger is:

| Piece | Bound relative to its own nonzero arm S |
| --- | --- |
| Actual central M integral minus its C0+C2+C4 moment model | C_loc e6 plus SC19 |
| True horizontal M tail to positive infinity outside J | C exp(-c tL²), using Note17's whole-ray quadratic Gaussian majorant |
| Left horizontal segment not in J | C exp(-c tL²), from exp(-d²/t+C Re p), d>=a/2 |
| Each oriented connector, including its length and the zero-length case | C exp(-c tL²), paying its exp(Ct) gamma motion |
| Bounded original middle | C R^b0 exp(-c tL²), via fixed-strip polynomial growth/reflection and bounded-height compactness |
| Full zeta-1 arithmetic on r>=a/2 | C_ar R^{-kappa t}, with every n>=2 included |
| Remaining arithmetic on left segments/connectors | Included in their preceding bounds with zeta bounded on Re>=2 |
| Finite even polynomial moment tails | Explicit SC19–20 |

The true whole-ray majorant, the integrated gamma comparison, connector
payment and middle comparison are Note17 LT15–16 and LT20–24, themselves
from parent Note30's complete source. None depends on truncation order.
The only additional nonlocal cost here is the finite polynomial-tail
constant SC20. Decrease c to at most min(c_parent,1/400) to cover
all Gaussian tails using a>=tL/5; retain finite inherited source
constants in C_ct. Summing two one-arm bounds against A pays both
reflected arms without dividing by a possibly cancelling field.

An explicit arithmetic prefactor is also available. If Re w>=-Sigma,
with Sigma>=0 fixed by the buffered strip, then
|zeta(w+v)-1|<=3·2^{-Re(w+v)} and the tilted Gaussian give
\[
\frac{\text{arithmetic arm error}}{|S|}
\le3\,2^{\Sigma}\sqrt{5/2}
 e^{-a\log2+t(\log2)^2/2}
\le C_{\rm ar}R^{-\kappa t},
\tag{SC22}
\]
where C_ar=3·2^Sigma sqrt(5/2). The last step follows from
a>=tL/5 whenever L>=20log2/3. This is a bound on the whole
ordinary Dirichlet remainder, not a finite-mode replacement.
Together SC18–22 prove SC5 at j=0 with the three error types
kept separate before any absorption.

To obtain an all-x eventual pure-e6 bound, use N<=C_N R L and
choose L0 to include the branch/buffer conditions, all seven fixed
sectorial constants, m>=t, |B-1|<=1/4, SC14, and L>=20log2/3.
Increase it so, persistently for L>=L0,
\[
C_N^7L^7e^{-L}\le1,\qquad
C_N^7L^7e^{(b_0+7)L-32cL^2}\le1.
\tag{SC23}
\]
Such an L0 exists; take it beyond the finite turning points. A
sufficient, uninstantiated choice is
\[
\boxed{t_*\ge\max\{32,64/\log2,e^{L_0}\}.}
\tag{SC24}
\]
Then kappa t>=8 and e6>=t⁴/N⁷ imply
\[
A_{\rm ar}/e_6\le C_N^7t^{-4}L^7R^{7-\kappa t}\le1,
\quad
A_{\rm ct}/e_6\le C_N^7t^{-4}L^7
 e^{(b_0+7)L-ctL^2}\le1.
\tag{SC25}
\]
The complete constant becomes C_loc+C_ar+C_ct after absorption.
The floor64/log2 is only an arithmetic power margin. The symbolic
exp L0 condition may be much larger; no numerical onset or switch64
claim follows. Retain the full SC4 bound for t>=32 rather than
pretend this coarse arithmetic allowance supplies X^{-7} there.
Failure of that absorption at smaller fixed t is only a limitation
of this upper bound, not a lower bound on the actual arithmetic error.

## 5. Actual residual and finite coefficient bounds

For an arm define
\[
\mathscr D=\partial_t-\tfrac14\partial_{ww},\qquad
k=\frac{t a_3}{16B^3}+\frac{5t^2a_2^2}{64B^4}.
\]
The exact implicit derivatives in Note17 give, for any coefficient
F(t,p),
\[
S^{-1}\mathscr D(SF)
 =\left.\partial_tF\right|_p-\frac{F_{pp}}{4B^2}
 -\frac{t a_2F_p}{4B^3}-kF.
\tag{SC26}
\]
This is a product/chain-rule identity, not an assumption that the
moving-saddle heat residual vanishes.

Write C4=sum_{n=3}^6 t^n B^{-n}U_n, with
\[
U_3=a_5/384,\quad U_4=7a_2a_4/768+35a_3^2/6144,
\quad U_5=35a_2^2a_3/2048,\quad U_6=385a_2^4/73728.
\]
Holding p fixed,
\[
\partial_t(t^nB^{-n})=nt^{n-1}B^{-n-1},
\tag{SC27}
\]
because B+t alpha'/2=1. Thus partial_t|p C4 is exactly the
positive bracket G4 in Note17 LT28, the negative of its P2 residual
per S. In particular 3/384=1/128, 4·7/768=7/192,
4·35/6144=35/1536, 5·35/2048=175/2048 and
6·385/73728=385/12288 are all required. These identities establish
actual cancellation of the previous residual, not just a size estimate.
Consequently
\[
\boxed{S^{-1}\mathscr D[S(1+C_2+C_4)]
 =-kC_4-\frac{C_{4,pp}}{4B^2}-\frac{t a_2C_{4,p}}{4B^3}.}
\tag{SC28}
\]

For a fully explicit residual write
\[
(\partial_t+\partial_{zz})P_4=-\sum_{w=s,1-s}\mathcal S_t(w)G_6,
\]
\[
\begin{split}
G_6={}&\frac{t^3a_7}{1536B^5}
 +\frac{t^4}{B^6}\left(\frac{5a_2a_6}{1024}
 +\frac{35a_3a_5}{4096}+\frac{21a_4^2}{4096}\right)\\
 &+\frac{t^5}{B^7}\left(\frac{77a_2^2a_5}{4096}
 +\frac{231a_2a_3a_4}{4096}+\frac{385a_3^3}{32768}\right)\\
 &+\frac{t^6}{B^8}\left(\frac{7007a_2^3a_4}{147456}
 +\frac{35035a_2^2a_3^2}{393216}\right)
 +\frac{25025t^7a_2^4a_3}{294912B^9}
 +\frac{85085t^8a_2^6}{4718592B^{10}}.
\end{split}
\tag{SC29}
\]
Both arms have (w_z)²=-1/4. One finite product-rule check for every
coefficient in SC29, using primes for p derivatives of U_n, is
\[
G_6=\sum_{n=3}^6\left\{
\frac{t^nU_n''}{4B^{n+2}}
+\frac{(n+1)t^{n+1}a_2U_n'}{4B^{n+3}}
+\frac{(2n+1)t^{n+1}a_3U_n}{16B^{n+3}}
+\frac{(2n+1)(2n+5)t^{n+2}a_2^2U_n}{64B^{n+4}}
\right\}.
\tag{SC30}
\]
This follows directly by differentiating B_p=-t a2/2 in SC28;
no new C6 model or higher-order theorem is invoked.

For a finite residual constant put Khat_j=K_j c_m^{-j}, beta=4/3,
so |a_j|<=Khat_j N^{-j}, |B^{-1}|<=beta. Let V_n be the positive
polynomial on the nth line/power t^n of SC29 with each a_j replaced
by Khat_j and B^{-n-2} replaced by beta^{n+2}. More explicitly,
\[
\begin{array}{ll}
V_3=\beta^5\widehat K_7/1536,&
V_4=\beta^6(5\widehat K_2\widehat K_6/1024
 +35\widehat K_3\widehat K_5/4096+21\widehat K_4^2/4096),\\
V_5=\beta^7(77\widehat K_2^2\widehat K_5/4096
 +231\widehat K_2\widehat K_3\widehat K_4/4096
 +385\widehat K_3^3/32768),&
V_6=\beta^8(7007\widehat K_2^3\widehat K_4/147456
 +35035\widehat K_2^2\widehat K_3^2/393216),\\
V_7=\beta^9\,25025\widehat K_2^4\widehat K_3/294912,&
V_8=\beta^{10}\,85085\widehat K_2^6/4718592.
\end{array}
\tag{SC31}
\]
Thus C_{r,0}=max(V3,...,V8) is sufficient for the delta4 bound
in SC6, since each line of SC29 has denominator scale N^{n+4}.
Taking C_r=6C_{r,0} suffices simultaneously in SC6 and the residual
supremum in SC7 when L>=1: the finite sum of successive L^{-1}
powers is at most6. Only derivatives through7 are used. At x=z=0 and sufficiently late time the leading term is
15t³/(64p⁷)>0 in G6, while the others are smaller by O(t/p).
S>0 there, so the actual summed residual is nonzero. Its improvement
is not a substitute for the separate field proof.

## 6. Buffered jets, direct first time and endpoint accounting

As in Note17 Section7, H-P4 is holomorphic on the larger buffers;
|(log S)_w|<=C L. On disks of radius r=c_d/L within those buffers,
each carrier modulus changes by a fixed factor C_env and the local
scales are comparable. Cauchy's formula applied to the *complete*
circle norm SC5 at j=0 gives the j<=3 bounds. For example, if
C_scale pays the variation of E6 over the disk, a sufficient finite
jet multiplier is j! c_d^{-j}C_env C_scale times the field constant.
No artificial contour endpoint is differentiated.

For the time derivative use the original fixed real contour SC21.
Differentiating its Gaussian kernel gives
partial_t K=(v²/t²-1/(2t))K=partial_vv K/4; local domination and
two integrations by parts with the entire xi source prove H_t=-H_zz.
Both infinite endpoint terms vanish. Together with the computed
E4=(partial_t+partial_zz)P4 this gives directly
\[
(H-P_4)_t=-(H-P_4)_{zz}-E_4.
\tag{SC32}
\]
The complete j=2 bound and SC29–31 prove SC6. This uses no time
derivative of an O estimate and no arbitrary-data backward-heat
contraction. All arithmetic and noncentral terms enter the complete
circle norm before this identity is used. A direct time-kernel
multiplier would turn some discarded odd moments into even ones;
SC26–32 retain the necessary contributions through exact identities.
Artificial moving split/saddle/localization endpoints cancel in the
unsplit integral and are not dropped from a differentiated decomposition.

Finally N>=tL gives L^j e6<=C t^{-3}L^{j-7} for j<=3,
and delta4<=C t^{-4}L^{-7}; monotonicity in L>=log(2+t)
proves SC7. The residual also lies below the direct-time allowance.

## 7. Height balances and what this fixed order establishes

Finite differentiated sectorial estimates yield
\[
\alpha^{(5)}(p)=12p^{-5}+O(m^{-6}),\quad
C_4=\frac{t^3}{32p^5}\{1+O(t/m+m^{-1})\}.
\tag{SC33}
\]
Thus |C4|≈t³/N⁵ and e6≈t⁴/N⁷, with successive error-scale
ratios O(t/N)=O(1/L). The dominant term of C4 is its single sixth
exponent-derivative moment, rather than its products of lower derivatives.
These are arm-correction sizes and error upper bounds; signed two-arm
cancellation is not used or asserted to have a fixed asymptotic equivalent.

| Balance | New C4 arm size | Field allowance | Direct-time allowance | Residual allowance |
| --- | --- | --- | --- | --- |
| X much smaller than tL | t^-2 L^-5 | t^-3 L^-7 | t^-3 L^-5 | t^-4 L^-7 |
| X comparable to tL | Same powers with fixed comparison constants | t^-3 L^-7 | t^-3 L^-5 | t^-4 L^-7 |
| X much larger than tL | t³/X⁵ | t⁴/X⁷ | t⁴L²/X⁷ | t³/X⁷ |

Spatial order j contributes L^j to the field column. For fixed x and
bounded transverse coordinate, p=(t/4)log t·(1+o(1)), hence
C4=32/(t²log⁵t)·(1+o(1)). This fixed-height statement is separate
from the all-x suprema SC7, which permit arbitrary height growth with t.

The complete field allowance improves Note17 uniformly:
\[
\frac{e_6}{e_4}\le\frac{Ct}{N^2}
 \le\frac{C}{t\log^2(2+t)}\longrightarrow0,
\tag{SC34}
\]
after both sources' eventual arithmetic/contour absorptions hold.
The same spatial/logarithmic and first-time losses retain that gain.
An improvement of local gamma order alone would not have justified
SC34 for the full canonical field without the new SC23–25 payment.

## 8. Controls, disposition and next deliverable

The canonical-source control screen is unchanged from Note17 Section9:
Euler-factor controls alter ordinary-zeta coefficients/completion;
weighted-square/finite-tail controls lack the unchanged full xi identity;
reflected/smooth/positive-primitive controls lack the same M times
ordinary-zeta source; finite-prime controls lack full canonical reflection
and arithmetic; atomic/finite-profile/counter-kernel/two-channel controls
lack the complete theta source; RH-conditional normalized-endpoint
perturbations lack unaltered Dirichlet arithmetic. Generic heat,
Gaussian recurrence and Cauchy structure exclude none of those controls.
This is an applicability screen, not a new collision/RH conclusion.

[Input record][inputs] pins the actual working-tree versions and the
pre-return r1 request. [Assessment13][review] checks the local finite
constants, global budgets and residual in the same model; parallel
read-only subtasks supplied internal checks with a single file writer.
No independent specialist validation or numerical onset is claimed.

**AN02 r1 CLOSED at this one fixed-order scope. LT-03 remains Partial**:
two worked corrections are not an arbitrary-fixed-order theorem.
Broad HDA-A04 also remains Partial. There was no resistant unpaid
estimate, no changed source or normalization, and no bridge/physical
transfer/manuscript execution. AN01 remains valid at its original scope.

**Next owner: Analysis — Sol.** The next concrete deliverable is a bounded
arbitrary-but-fixed-order statement with an order-indexed finite Bell
majorant, all coefficient/residual identities, and explicit order-dependent
arithmetic/onset constants. The present sixth-derivative interpolation
shows a route but proves only the order used here. It establishes no
uniformity as the order grows with t, no optimal truncation, and no
convergent infinite hierarchy. Once fixed-order understanding is assessed,
the separate regional bridges can be scoped; they remain unexecuted.

[packet]: ../research-progress/handoffs/HDA-A04-AN02.md
[overview]: ../research-overview/03_LARGE_POSITIVE_TIME_HIERARCHY_RESEARCH_OVERVIEW_20261026.md
[progress]: ../research-progress/03_LARGE_POSITIVE_TIME_HIERARCHY_RESEARCH_PROGRESS_20261026.md
[n17]: 17_FIRST_CORRECTED_LARGE_POSITIVE_TIME_20261026.md
[inputs]: 18_SECOND_CORRECTED_POSITIVE_TIME_INPUTS_20261026.json
[review]: ../reviews/13_SECOND_CORRECTED_LARGE_POSITIVE_TIME_ASSESSMENT_20261026.md
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
