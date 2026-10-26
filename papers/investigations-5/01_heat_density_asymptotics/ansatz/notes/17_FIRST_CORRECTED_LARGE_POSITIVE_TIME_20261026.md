# First corrected full gamma saddle at large positive time

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
verified in the current session metadata. Ansatz chat0005, thread
`01a178fa-8a72-7f23-9a7f-47e284eab9a3`.

**Status: proved in-note from named inputs; same-model internal assessment
only.** This executes [HDA-A04-AN01 r1][packet] under [Overview03][overview]
and [Progress03][progress]. The proposed first correction and local next
remainder are valid. All source, arithmetic, contour, buffered spatial
jet and first-time payments are retained below. The actual corrected heat
residual is computed independently. The sufficient onset is symbolic;
no numerical onset or independent specialist validation is claimed.
There was no numerical, machine-symbolic, exact-arithmetic or sampling
campaign. File hashes and history checks are administrative provenance.

Read [the result index][results], [heat-flow cluster][heat], [controls12][controls]
and [avoid index][avoid]. This is a quantitative approximation milestone
under [avoid01][a01], with the scope discipline of [avoid07][a07] and the
complete-payment discipline of [avoid12][a12]. No RH, initial all-real-zero
hypothesis or assumed value of Lambda is used. Regional bridges, physical
observable transfer, higher-order execution and manuscript integration
remain outside this return.

## 1. Exact contract, buffers and theorem

Keep the complete theta source and the exact identities
\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad H_t=-H_{zz},\quad H(0,z)=\xi((1+iz)/2)/8.
\tag{LT1}
\]
The normalization and full source are those of [parent Note30][n30].
The exact convolution is [Polymath v2, equation35][poly], checked again
in Section4 of that source; its derivation uses the Gaussian identity
and Fubini, without RH. The restricted evolved approximation theorems
elsewhere in that paper are not used here.

Fix arbitrary finite observation widths H0,Y0, and an analytic buffer
b>0. Prove the field bound on the larger rectangles
\[
|\Re z-x|\le H_0+2b,\qquad |\Im z|\le Y_0+2b
\]
for every real center x. Report derivatives on the rectangles with b
in place of 2b. For the parent notation one may take H0=ell+2 and
Y0=Y+h+2, and add the displayed buffer. Constants may depend on these
fixed widths and b, but not on t or x. Bounded changes of center only
change the scales below by constant factors. There is no q or K in the
field proof; if physical transfer is later performed, their parent
values must be preserved.

Set
\[
X=|x|,\quad R=2+t+X,\quad \mathcal L=\log R,\quad
\mathcal N=1+X+t\mathcal L.
\tag{LT2}
\]
With s=(1+iz)/2, use each w=s,1-s and exactly Note30's selected
right-half-plane branch
\[
\mathcal M(p)=\frac{p(p-1)}{16}\pi^{-p/2}\Gamma(p/2),\quad
\alpha=(\log\mathcal M)',\quad p=w+\tfrac t2\alpha(p),
\]
\[
B=1-\tfrac t2\alpha'(p),\qquad
S=\mathcal S_t(w)=\mathcal M(p)e^{-(p-w)^2/t}B^{-1/2}.
\tag{LT3}
\]
The logarithm of M is real on p>1 and holomorphic in Re p>1;
B^{-1/2} uses the branch near1. Let
\[
C(t,w)=\frac{t^2\alpha'''(p)}{32B^2}
       +\frac{5t^3(\alpha''(p))^2}{192B^3},\quad
P_2(t,z)=\sum_{w=s,1-s}\mathcal S_t(w)(1+C(t,w)),
\]
\[
\mathcal A(t,z)=|\mathcal S_t(s)|+|\mathcal S_t(1-s)|>0.
\tag{LT4}
\]
The envelope is the leading two-arm amplitude sum, not H or P2 at
possible zeros. Eventually |C|<1/2, so a corrected-arm amplitude sum
would also be comparable; it is not needed to define the norm.

Define separate positive allowances
\[
e_4=\frac{t^3}{\mathcal N^5}+\frac{t^4}{\mathcal N^6}
    +\frac{t^5}{\mathcal N^7}+\frac{t^6}{\mathcal N^8},\qquad
\delta_2=\frac{e_4}{t},
\]
\[
A_{\rm ar}=R^{-\kappa t},\quad\kappa=\frac{\log2}{8},\qquad
A_{\rm ct}=R^{b_0}e^{-ct\mathcal L^2},\qquad
E=e_4+A_{\rm ar}+A_{\rm ct}.
\tag{LT5}
\]
Here b0 is a fixed finite middle-strip polynomial exponent and c>0
is fixed, decreased when necessary to cover all tails. They depend
only on the declared fixed domains and gamma/source estimates.

**Complete first-correction theorem.** There are Cj,Ct,Cr and a
sufficient onset R0, independent of t and x, such that for t>=32 and
R>=R0 the field and jets on their stated buffered domains satisfy
\[
|\partial_z^j(H-P_2)|\le C_j\mathcal L^j E\,\mathcal A,
\qquad 0\le j\le3,
\tag{LT6}
\]
\[
|(H-P_2)_t|\le C_t(\mathcal L^2E+\delta_2)\mathcal A,
\qquad |(\partial_t+\partial_{zz})P_2|\le C_r\delta_2\mathcal A.
\tag{LT7}
\]
The field bound j=0 holds on the full larger domain. The same jet
bounds hold for real mixed spatial derivatives of total order j,
because the difference is holomorphic. These are absolute envelope
bounds, including x=0 and negative heights by reflection/conjugation.

There is a single eventual t_*>=32, depending only on these fixed
data, for which A_ar+A_ct<=C e4 for all real x. Hence for t>=t_*
replace E by e4 in LT6--7. In particular
\[
\boxed{\sup_{x,\ z\text{ in its observation rectangle}}
 \frac{|\partial_z^j(H-P_2)|}{\mathcal A(t,z)}
 \le\frac{C_j}{t^2\log^{5-j}(2+t)},\quad 0\le j\le3,}
\tag{LT8}
\]
\[
\boxed{\sup_{x,z}\frac{|(H-P_2)_t|}{\mathcal A}
 \le\frac{C_t}{t^2\log^3(2+t)},\qquad
\sup_{x,z}\frac{|(\partial_t+\partial_{zz})P_2|}{\mathcal A}
 \le\frac{C_r}{t^3\log^5(2+t)}.}
\tag{LT9}
\]
The suprema use the same fixed domains. For positive log powers the
maximal bounds follow from monotonicity of L^{j-5} and N>=tL,
not from freezing log R at its value at zero when its exponent is positive.
P2 is a moving-saddle approximation with a nonzero heat residual.

## 2. Baseline audit and precise sufficient-onset dependencies

The reusable branch proof is Note30 FS8--FS10, not a hypothesis about
zeros. Sectorial log-Gamma/digamma estimates [DLMF5.11][gamma] give, on
a fixed larger sector,
\[
\alpha(p)=\tfrac12\Log(p/(2\pi))+O(m^{-1}),\qquad
|\alpha^{(r)}(p)|\le K_r m^{-r},\quad m=|p|,\quad 1\le r\le5.
\tag{LT10}
\]
The finite derivative bounds follow by Cauchy on the holomorphic
sectorial remainder. One more derivative is available by the same
argument if a larger Cauchy domain is desired. The sector margin is
fixed, not shrinking as t or X grows. For the local Taylor remainder
below, r=5 suffices, since (log M)^{(6)}=alpha^{(5)}.

For w=sigma+i tau0, tau0>=0 and sigma in its fixed real buffer,
the map p->w+(t/2)alpha(p) is a contraction on
\[
\sigma+t\mathcal L/8\le\Re p\le\sigma+t\mathcal L,
\quad \tau_0\le\Im p\le\tau_0+t.
\]
Its real increment is tL/4+O(t log L), imaginary increment is in
[0,t] eventually, and derivative is O(t/N)=O(1/L). Near tau=0,
Re alpha'(A+i tau)>0 for 0<=tau<=A; farther up the half-argument
term makes Im alpha nonnegative. This supplies the sign, including
the real saddle at tau0=0. Conjugation covers tau0<0. Consequently
\[
a=\Re(p-w)\asymp t\mathcal L,\quad
m\asymp\mathcal N,\quad |h|=|\Im(p-w)|\le t,\quad
|B-1|\le C/\mathcal L,
\tag{LT11}
\]
and a>=tL/5 after a uniform onset. The branch is holomorphic by
uniqueness and B!=0, including across tau0=0. M is zero-free there.
All fixed horizontal/transverse enlargements are made before this onset.

A sufficient t_* can be specified as follows, without pretending it
has a numerical value. Obtain the fixed gamma constants K_r on the
selected enlarged sectors and the fixed constants in LT11 and in the
contour payments of Section5. Increase L0 until:

1. The branch rectangle maps into itself, the contraction constant is
   at most1/2, |B-1|<=1/4, Re p>2, and a/2 exceeds every bounded
   left endpoint. All local segments retain a fixed sector margin.
2. The constants in |Gamma_p(u)|<=C u²/m imply Ct/m<=1/4;
   thus the exact and quadratic exponents have a common positive
   Gaussian rate. The same bounds hold on all analytic buffers.
3. The losses C Re p and C|h| in the left segment/connector estimates
   are absorbed by a fixed fraction of a²/t. Choose the final c>0
   after these absorptions and polynomial Gaussian-tail payments.
4. With N<=C_N R L, require for all L>=L0
   C_N^5 L^5 e^{-L}<=1, and
   C_N^5 L^5 exp((b0+5)L-32c L²)<=1.
   Such an L0 exists; enlarge beyond the turning points of these
   elementary functions so the conditions persist.
5. Include the constants needed for |C|<=1/2, disk radius c1/L<b,
   carrier comparability on those disks and local scale comparability.

Then it suffices to take
\[
t_*\ge\max\{32,\ 48/\log2,\ e^{L_0}\}.
\tag{LT12}
\]
Indeed kappa t>=6, and R>=t>=exp L0, so
\[
\frac{A_{\rm ar}}{e_4}
\le\frac{C_N^5}{t^3}R^{5-\kappa t}\mathcal L^5\le1,
\quad
\frac{A_{\rm ct}}{e_4}
\le\frac{C_N^5}{t^3}
 R^{b_0+5}\mathcal L^5e^{-ct\mathcal L^2}\le1.
\tag{LT13}
\]
The floor48/log2 is just a convenient strict arithmetic power margin.
The dominant unspecified condition is exp L0; these inequalities do
not certify an onset at any displayed small time. In particular, no
claim at t=64, or refinement of the regulator switch, is made.

For a joint theorem retaining every t>=32 the budgets in LT5 remain
visible: the inherited A_ar has power32 log2/8<5, so that *bound*
cannot be absorbed into t³/N⁵ as X tends to infinity at t=32.
This is a limitation of that arithmetic upper bound, not a lower bound
on the true canonical error or an obstruction to a sharper arithmetic
analysis. It does not affect the eventual large-t theorem.

## 3. Recurrence and the first correction

This independently checks [Brainstorm03 P5--P9][discussion]. Let
f=log M and beta_r=f^{(r+2)}(p)/(r+2)!. In formal lambda,
\[
\exp\bigl(\sum_{r\ge1}\beta_r u^{r+2}\lambda^r\bigr)
=\sum_{j\ge0}A_j(u)\lambda^j,
\quad jA_j=\sum_{r=1}^j r\beta_r u^{r+2}A_{j-r},\quad A_0=1.
\tag{LT14}
\]
This is finite polynomial coefficient algebra at each j. Every monomial
in Aj has parity j: its degree is j plus twice its number of factors.
Thus odd j have zero full-line even-Gaussian moment. For Re B>0,
normalized moments are
\[
\mu_{2k}=\frac{(2k-1)!!}{2^k}(t/B)^k,\quad \mu_{2k+1}=0.
\]
Since A2=alpha''' u⁴/24+(alpha'')²u⁶/72, its moment gives precisely
LT4, with coefficients1/32 and5/192. P6--P7 require no algebraic
correction. [DLMF2.4(iv)][saddles] supplies the standard simple-saddle
context, not the moving-parameter complete remainder theorem here.
The required contour and parity justification follows next; a formal
lambda series at1 is not being asserted to converge.

## 4. Local remainder on the actual contour

For one arm write v=p-w+u with real u. On u>=-a/2,
\[
\Gamma_p(u)=f(p+u)-f(p)-\alpha(p)u,\quad
E_p(u)=\Gamma_p(u)-\tfrac12\alpha'(p)u^2,
\]
\[
\frac{e^{-(p-w+u)^2/t}\mathcal M(p+u)}
 {e^{-(p-w)^2/t}\mathcal M(p)}
=e^{-Bu^2/t+E_p(u)}.
\tag{LT15}
\]
The segment joining p and p+u stays in Re>1 and has modulus>=c0m.
For u>=0 its modulus only increases. The integral Taylor estimates
|Gamma_p(u)|<=C u²/m and |E_p(u)|<=C|u|³/m² therefore apply on
this entire half-line, even for arbitrarily large positive u. Independently,
\[
|e^{-Bu^2/t+E_p(u)}|+|e^{-Bu^2/t}|
\le2e^{-c_0u^2/t}.
\tag{LT16}
\]
This follows from the quadratic bound for Gamma_p, Re B>=3/4 and
Ct/m small. It does not assume a cubic perturbation is small over an
infinite ray.

Use only the symmetric actual subsegment J=[-a/2,a/2] for parity.
There |u|/m is bounded by a fixed number less than1 after onset.
With g_j=f^{(j)}(p)u^j/j!, j=3,4,5, Taylor's integral remainder gives
\[
E_p=g_3+g_4+g_5+r_6,\quad |r_6|\le C|u|^6/m^5,
\]
\[
|E_p|\le C|u|^3/m^2,\quad
|E_p-g_3|\le C|u|^4/m^3,\quad
|E_p-g_3-g_4|\le C|u|^5/m^4.
\tag{LT17}
\]
Consequently
\[
|E_p^2-g_3^2-2g_3g_4|\le C|u|^8/m^6,\qquad
|E_p^3-g_3^3|\le C|u|^{10}/m^7.
\]
Taylor's formula with its integral remainder gives
\[
|e^{E_p}-1-E_p-E_p^2/2-E_p^3/6|
\le |E_p|^4\max(1,e^{\Re E_p})/24.
\]
Multiply by the Gaussian and use LT16 for both members of the max.
For
\[
T=1+g_3+g_4+g_5+g_3^2/2+g_3g_4+g_3^3/6
\]
one obtains the pointwise *weighted* remainder
\[
|e^{-Bu^2/t}(e^{E_p}-T)|
\le Ce^{-c_1u^2/t}
 \left(\frac{|u|^6}{m^5}+\frac{|u|^8}{m^6}
       +\frac{|u|^{10}}{m^7}+\frac{|u|^{12}}{m^8}\right).
\tag{LT18}
\]
No unweighted uniform smallness of E is needed. Since
(πt)^{-1/2} integral_R |u|^{2k}e^{-c1u²/t}du=C_k t^k,
the normalized integral of LT18 is at most C e4 using m≈N.

The terms g3,g5,g3g4,g3³ are odd in real u and integrate to zero
on J against the even, generally complex Gaussian. This cancellation
is exact. Extend only the remaining finite polynomial
1+g4+g3²/2 from J to the full real line. For each fixed monomial,
splitting the Gaussian into two factors bounds its omitted tails by
\[
Ce^{-c_2a^2/t}(1+t^2/m^3+t^3/m^4)
\le Ce^{-c_3t\mathcal L^2}.
\tag{LT19}
\]
The Gaussian moments now give B^{-1/2}(1+C). The extra factor from
the original saddle normalization is precisely S in LT3. The actual
integrand was never extended through gamma poles into a fictitious
negative half-line. The genuine ray outside J is paid separately below.

The gain over an absolute cubic-moment estimate does use parity.
Without cancelling g3 and the grade3 odd terms, one would pay larger
absolute moments rather than the e4 scale. Symmetry is asserted only
on J, and every part omitted to create J has its own bound.

## 5. Complete source, noncentral contours and arithmetic

The following rechecks Note30 FS11--FS20 at the improved target scale.
Write the exact convolution with its original, fixed contour:
\[
H(t,z)=\frac1{\sqrt{\pi t}}\int_{\mathbb R}
 e^{-v^2/t}\frac{\xi(s+v)}8\,dv.
\tag{LT20}
\]
Split at Re(s+v)=2 and -1. Reflection xi(w)=xi(1-w) and v->-v
make the two arms
\[
I_w=\frac1{\sqrt{\pi t}}\int_{v_0}^\infty
 e^{-v^2/t}\mathcal M(w+v)\zeta(w+v)\,dv,
\quad v_0=2-\Re w,
\tag{LT21}
\]
plus a bounded middle interval. The gamma normalization satisfies
xi/8=M zeta exactly. Both arms and the middle are retained.

For tau0>=0 shift each arm to v=r+ih, h=Im(p-w), r>=v0,
including the oriented connector v0->v0+ih; negative tau0 uses h<0.
All rays/connectors have Re(w+v)>=2, so there is no crossed gamma
singularity or zeta pole, and the full ordinary Dirichlet series is
valid throughout. First close a finite rectangle on the right. Its
far vertical face tends to zero by
exp(-r²/t+O(r log(r+2))) for each fixed t,z. Uniform infinite-tail
bounds follow from LT16, not from an unquantified finite cutoff.

The complete one-arm error consists of:

| Piece | Payment relative to its own nonzero S |
| --- | --- |
| Exact M integral on J minus its even correction moments | C e4 by LT18--19 |
| Actual M ray u>=a/2, including its infinite right end | C exp(-c tL²), by LT16 |
| Remaining shifted horizontal segment v0<=r<=a/2 | C exp(-c tL²), by the integrated gamma comparison below |
| Its original vertical connector, including its length | C exp(-c tL²) |
| All omitted ordinary Dirichlet modes on r>=a/2 | C R^{-kappa t} |
| All arithmetic on the remaining horizontal segment/connector | Already included by zeta bounded on Re>=2 |
| Bounded middle interval from the original full convolution | C R^{b0}exp(-c tL²) |
| Finite Gaussian-polynomial tails used in moment replacement | C exp(-c tL²) by LT19 |

For completeness, let A=Re p=a+Re w and d=a-r>=a/2 on the
remaining left segment. Integrating the real part of alpha horizontally,
\[
\int_{A-d}^A\Re\alpha(v+i\Im p)dv
\ge d\Re\alpha(p)-CA.
\]
Indeed |v+i tau|/|A+i tau|>=v/A for 2<=v<=A, and the total
logarithmic loss is at most (1/2) integral_0^A -log(v/A)dv=A/2;
the bounded remainders add O(A). Since Re alpha(p)=2a/t, the ratio
of integrands to the saddle modulus is bounded by
\[
\exp(-d^2/t+CA)\le\exp(-ct\mathcal L^2).
\tag{LT22}
\]
Its length/sqrt(t) is absorbed by decreasing c. This comparison is
uniform at tau=0 and at tau much larger than A.

At the connector's top use LT22 down to Re(w+v)=2. On that line
|Im alpha| is uniformly bounded even at bounded height; moving the
imaginary coordinate by at most |h|<=t costs exp(Ct). The Gaussian
modulus does not increase when |Im v| decreases from |h|. Its
length/sqrt(t) is harmless after reducing c. A collapsed connector
has exactly zero contribution, so x=0 is covered.

On the original middle strip -1<=b<=2, Euler summation, reflection
and bounded-real-part Stirling give for some fixed finite b0
\[
\sup_b|\xi(b+i\tau_0)/8|
\le C(1+|\tau_0|)^{b_0}|\mathcal M(2+i\tau_0)|.
\tag{LT23}
\]
At bounded height use compactness: xi is entire and M(2+i tau0)
never vanishes. The endpoint-to-saddle comparison above, including
moving back along the connector, pays the whole bounded middle by
R^{b0}exp(-ctL²). No high-height estimate is applied at height zero.

Finally, on Re(w+v)>=2 the *complete* series gives
|zeta(w+v)-1|<=3·2^{-Re(w+v)}. On r=a+u>=a/2, use LT16 and the
tilted Gaussian to obtain
\[
C e^{-a\log2}\frac1{\sqrt{\pi t}}
 \int_{\mathbb R}e^{-u^2/(2t)-u\log2}du
\le C e^{-a\log2+t(\log2)^2/2}\le C R^{-\kappa t}.
\tag{LT24}
\]
Enlarge the single eventual onset to justify the last inequality from
a>=tL/5. This uses every omitted n>=2, not a chosen finite mode
set. Their other contour pieces were already paid with |zeta|<=zeta(2).
The same decomposition applies to the reflected arm. Sum both one-arm
bounds, add the middle and divide by A to prove LT6 at j=0 with
all three terms of E present.

The artificial endpoints v0, a/2 and the saddle displacement vary
with the estimating parameters. No derivative is inferred from the
separately bounded pieces. Section7 starts from the globally
holomorphic difference and the exact original fixed-contour identity;
this is what pays endpoint differentiation without discarded terms.

## 6. Actual residual, including its first exact cancellation

Here subscripts p mean derivatives holding t fixed; a t derivative
at fixed p is explicitly marked. Put
\[
k=\frac{t\alpha'''}{16B^3}
  +\frac{5t^2(\alpha'')^2}{64B^4},\quad
D=(\log S)_w=\alpha+\frac{t\alpha''}{4B^2},\quad
\mathscr D=\partial_t-\tfrac14\partial_{ww}.
\]
The implicit equation gives p_w=1/B and p_t=alpha/(2B). Directly,
\[
(\log S)_t=\frac{\alpha^2}4+\frac{\alpha'}{4B}
 +\frac{t\alpha\alpha''}{8B^2},\qquad
D_w=\frac{\alpha'}B+\frac{t\alpha'''}{4B^3}
 +\frac{t^2(\alpha'')^2}{4B^4}.
\]
Subtracting (D²+D_w)/4 from (log S)_t cancels the alpha²,
alpha'/B and t alpha alpha'' terms, giving \(\mathscr D S=-kS\),
consistent with Note30 FS33. For C in LT4, holding p fixed gives exactly
\[
\left.\partial_t C\right|_p=k,
\quad\text{since } B_t|_p=-\alpha'/2\text{ and }B+t\alpha'/2=1.
\tag{LT25}
\]
The product rule and chain rule therefore yield the compact exact
corrected residual per arm
\[
\boxed{\frac{\mathscr D[S(1+C)]}{S}
 =-kC-\frac{C_{pp}}{4B^2}-\frac{t\alpha''C_p}{4B^3}.}
\tag{LT26}
\]
There is no division by1+C or a sum that might vanish.
For a check of every coefficient,
\[
C_p=\frac{t^2\alpha^{(4)}}{32B^2}
 +\frac{t^3\alpha''\alpha'''}{12B^3}
 +\frac{5t^4(\alpha'')^3}{128B^4},
\]
\[
C_{pp}=\frac{t^2\alpha^{(5)}}{32B^2}
 +\frac{t^3(\alpha''')^2}{12B^3}
 +\frac{11t^3\alpha''\alpha^{(4)}}{96B^3}
 +\frac{31t^4(\alpha'')^2\alpha'''}{128B^4}
 +\frac{5t^5(\alpha'')^4}{64B^5}.
\tag{LT27}
\]
Thus, with all alpha derivatives evaluated at the appropriate arm's p,
\[
\begin{split}
(\partial_t+\partial_{zz})P_2
=-\sum_{w=s,1-s}\mathcal S_t(w)\bigg\{
&\frac{t^2\alpha^{(5)}}{128B^4}
 +\frac{35t^3(\alpha''')^2}{1536B^5}
 +\frac{7t^3\alpha''\alpha^{(4)}}{192B^5}\\
&+\frac{175t^4(\alpha'')^2\alpha'''}{2048B^6}
 +\frac{385t^5(\alpha'')^4}{12288B^7}\bigg\}.
\end{split}
\tag{LT28}
\]
Both w(z) choices have (w_z)²=-1/4. Applying LT10 to each
monomial proves the residual bound Cr delta2 A in LT7, since its
four scales are t²/N⁵,t³/N⁶,t⁴/N⁷,t⁵/N⁸. This improved residual
was not used to infer a field comparison; Section5 proved that
comparison directly from the complete source.

## 7. Buffered spatial derivatives and direct first-time comparison

The exact difference F=H-P2 is holomorphic on the larger domains.
From LT3 and LT10--11, |(log S)_w|<=C L. Each arm's modulus changes
by at most a constant factor on a disk |z-z0|<=c1/L. The scales
R,L,N and E at neighboring centers are comparable. The disk fits
inside the specified analytic buffer after the chosen onset.
Cauchy's formula applied to the *complete* field inequality on that
circle therefore gives C_j L^j E A for j<=3. The same reasoning
bounds the model's own jth derivatives by C_j L^j A. This is a
bound on derivatives of a holomorphic function from its circle norm,
not differentiation of an uncontrolled big-O assertion.

For the time derivative, start from the exact original convolution
LT20, locally in positive t. Differentiating its kernel gives
\[
\partial_t K_t(v)=(v^2/t^2-1/(2t))K_t(v)
                 =\tfrac14\partial_{vv}K_t(v),\quad
K_t(v)=(\pi t)^{-1/2}e^{-v^2/t}.
\tag{LT29}
\]
Gaussian decay versus exp(O(|v|log(|v|+2))) justifies domination and
two integrations by parts on the original entire-xi contour. Both
infinite endpoint terms vanish. Thus H_t=-H_zz holds directly with
this normalization, without differentiating a deformed contour.
Together with the *computed* residual E2=(partial_t+partial_zz)P2,
it gives the exact comparison identity
\[
\boxed{(H-P_2)_t=-(H-P_2)_{zz}-E_2.}
\tag{LT30}
\]
The j=2 circle bound and LT28 prove LT7. This is an immediate
identity at the same time, not a backward-heat stability/propagation
claim or differentiation of LT6 with respect to t.

This route also accounts for all moving endpoints: LT29 is taken
before splitting, so there are no finite artificial endpoints in the
operation; their terms would cancel if the full deformed decomposition
were differentiated. In particular one must not reuse odd local
cancellation after inserting the time-kernel multiplier, whose linear
u term can turn an odd polynomial into an even one. LT25--30 retain
those contributions exactly through the model derivative and residual.
Arithmetic, connectors, middle and noncentral pieces have already been
included in the circle norm; their derivative payment in the time
bound is L²(A_ar+A_ct). No isolated piece or endpoint is omitted.

## 8. Height balances, fixed height and quantitative gain

From LT10 and the finite differentiated leading digamma term,
\[
\alpha'''(p)=p^{-3}+O(m^{-4}),\quad
\alpha''(p)=-\tfrac12p^{-2}+O(m^{-3}),\quad
C=\frac{t^2}{32p^3}\{1+O(t/m+m^{-1})\}.
\tag{LT31}
\]
The braces describe a complex relative remainder of the nonzero leading
arm correction. Because t/m=O(1/L), it follows that |C|≈t²/N³
at the eventual onset. For the error *allowance*, not a signed error
asymptotic equivalent,
\[
e_4\asymp t^3/\mathcal N^5,
\quad \delta_2\asymp t^2/\mathcal N^5,
\quad \frac{e_4}{t^{3/2}/\mathcal N^2}
\le\frac{C t^{3/2}}{\mathcal N^3}
\le\frac{C}{t^{3/2}\log^3(2+t)}\longrightarrow0.
\tag{LT32}
\]
This last comparison is uniform over real x, and the complete error
has the same improvement once LT13 has paid the arithmetic/contours.

| Balance | Dominant arm-correction size | Dominant local field allowance | First-time allowance | Residual allowance |
| --- | --- | --- | --- | --- |
| X much smaller than tL | 1/(tL³) | 1/(t²L⁵) | 1/(t²L³) | 1/(t³L⁵) |
| X comparable to tL | Same powers, constants depend on the fixed comparison bounds | 1/(t²L⁵) | 1/(t²L³) | 1/(t³L⁵) |
| X much larger than tL | t²/X³ | t³/X⁵ | t³L²/X⁵ | t²/X⁵ |

Spatial order j contributes L^j to the field column. Within e4,
the first term dominates in every balance: successive ratios are
O(t/N)=O(1/L). Within C, the quartic moment dominates its squared
cubic companion by the same factor. These are smooth balances of the
implicit saddle, not new phase transitions. A two-arm sum may have
additional cancellation; none is used in this envelope theorem.

For each fixed x (and bounded fixed transverse coordinate),
p=(t/4)log t·(1+o(1)) on both arms, so each C is
2/(t log³t)·(1+o(1)). LT8--9 give the separate fixed-x field/jet/time
limits. The all-x assertion is stronger: its normalized suprema tend
to zero at the displayed rates while x may depend arbitrarily on t,
including the comparable and height-dominated regions. Neither
statement divides by H or P2, or gives relative error at a field zero.

## 9. Controls, evidence and next bounded deliverable

The recurrence and simple-saddle mechanism alone exclude no collision
control. The application uses the unchanged complete source identity
xi/8=M zeta, exact reflection and the full ordinary Dirichlet series.
The controls12 premise screen is:

| Control class | Premise not shared with this canonical application |
| --- | --- |
| Euler-factor controls | Unchanged ordinary-zeta coefficients/completed source |
| Weighted-square or finite-tail controls | The same full xi identity and arithmetic completion |
| Reflected, smooth-density, positive-primitive controls | The same canonical gamma-times-ordinary-zeta source |
| Finite-prime orbit controls | Full canonical source reflection/arithmetic identity |
| Atomic or finite-profile controls, including generic counter-kernels/two-channel constructions | The complete canonical theta profile and its exact completed identity |
| RH-conditional normalized-endpoint perturbations | Ordinary unaltered Dirichlet-series arithmetic |

This is an analytic applicability screen, not sampling or a new zero
exclusion. Generic Gaussian recurrences, holomorphic Cauchy estimates
and heat identities can hold for controls too. No RH conclusion or
universal exclusion follows from the gained approximation.

[Input record][inputs] pins the actual input bytes and repository HEAD;
the execution used an already modified working tree. [Assessment12][review]
is same-model internal checking, including parallel local/global/residual
subtasks with a single file writer. It is not an independent specialist
review. The parent Note30--31 assessments remain named shared inputs;
no retrospective upgrade of their status is intended.

**Disposition:** the bounded AN01 r1 closes at its requested eventual
all-height field/jet/first-time/residual scope. HDA-A04 as a hierarchy
program remains Partial. No source, normalization or frozen request
changed; the larger time onset is allowed by its eventual-t contract.
No resistant unpaid estimate arose. The t=32 arithmetic absorption
shortcut was rejected and replaced by LT5 plus the explicit LT12--13
payment. A smaller residual alone would not have closed this task.

**Next owner: Analysis — Sol.** The next deliverable is to prepare a
bounded LT-03 fixed-higher-order request, with finite Taylor degree,
polynomial parity, required sectorial derivative constants, Gaussian
moment/tail constants, arithmetic power floor, buffers and exact residual
specified for that order. AN01 proves only this first correction; it
establishes no uniform growth law for those constants and no convergent
or growing-order hierarchy. Higher-order execution and all regional
bridges remain for later authorized stages. There is no numerical
question or specifically resistant mechanism requiring Astra in this return.

[packet]: ../research-progress/handoffs/HDA-A04-AN01.md
[overview]: ../research-overview/03_LARGE_POSITIVE_TIME_HIERARCHY_RESEARCH_OVERVIEW_20261026.md
[progress]: ../research-progress/03_LARGE_POSITIVE_TIME_HIERARCHY_RESEARCH_PROGRESS_20261026.md
[n30]: ../../notes/30_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_20261024.md
[n31]: ../../notes/31_POSITIVE_ALL_HEIGHT_EVOLUTION_AND_COVARIANCE_20261024.md
[discussion]: ../../recurrence/brainstorm/03_POSITIVE_TIME_HIERARCHIES_AND_BRIDGES_20261026.md
[review]: ../reviews/12_FIRST_CORRECTED_LARGE_POSITIVE_TIME_ASSESSMENT_20261026.md
[inputs]: 17_FIRST_CORRECTED_POSITIVE_TIME_INPUTS_20261026.json
[poly]: https://arxiv.org/html/1904.12438v2#S4
[saddles]: https://dlmf.nist.gov/2.4#iv
[gamma]: https://dlmf.nist.gov/5.11
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
