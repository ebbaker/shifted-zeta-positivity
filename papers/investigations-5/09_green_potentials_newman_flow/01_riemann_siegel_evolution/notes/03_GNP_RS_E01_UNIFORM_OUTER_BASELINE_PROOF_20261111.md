# GNP-RS-E01 r1: uniform outer Green baseline

11 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual model identifier and
reasoning effort are unavailable in child chat0001 capture metadata.
Type **E**, recommended GPT-6.1 Sol; that recommendation is not provenance.

**Status: proved in-note from the named inherited inputs; same-assistant
internal self-check only.** This is the separate return to [frozen E01 r1][request].
The request and B01 evidence are unchanged. All 45 recorded input/document
identities matched before activation; see the [input/check record][record].
The [self-check][review] distinguishes this proof from a fresh independent
audit of the inherited HDA field theorem.

The result is an **acquisition estimate**, in the terminology of
[avoid01][a01]. It does not acquire a favorable signed critical-boundary
value. Read the [result index][results], [cluster11][r11],
[controls12][controls] and [avoidance index][avoid], particularly
[premise02][a02], [scope07][a07] and [separate bounds12][a12].
No numerical, machine-symbolic, exact-arithmetic or interval research
was executed. Constants are finite analytical constants; their numerical
values and the onset are not certified.

## 1. Statement and exact normalization

Keep the complete normalized theta source,
\[
 H_0(z)=\xi((1+iz)/2)/8,\qquad
 \partial_\lambda H_\lambda=-\partial_{zz}H_\lambda .
\]
Use the parent's strip \(0<\Im z<8\), center \(X+4i\), and
\[
 K(t)=\frac1{16\cosh(\pi t/8)},\qquad
 \int_{\mathbb R}K(t)\,dt=\frac12 .
\]
Write
\[
 L=L_X=\log(X/(4\pi)),\qquad \lambda=c/L,\qquad
 \frac12\le c\le1,\qquad R=R_X=\frac{32}{\pi}\log X .
 \tag{E1}
\]
Every conclusion below is uniform for **every** sufficiently large
\(X\) and every such \(c\), including exceptional centers. The value
\(\lambda=c/L_X\) stays fixed throughout each spatial integral.

Retain exactly [B01 Note01 (3)][b01]'s upper-half-plane branches:
\[
 L(z)=\Log(z/(4\pi)),\quad
 A(\lambda,z)=\frac{\pi^{1/4}}{16}z^{7/4}
 \exp\!\left[-\frac{\pi z}{8}
       +\frac{\lambda}{16}\left(L(z)^2-\frac{\pi^2}{4}\right)\right],
\]
\[
 \Theta(\lambda,z)=\frac z4(L(z)-1)+\frac{\pi\lambda L(z)}{16}
                  +\frac{7\pi}{8},\qquad
 C_\pm(\lambda,z)=\frac A2e^{\pm i\Theta},\qquad
 V_\lambda=H_\lambda/C_- .
 \tag{E2}
\]
Only \(C_-\) is used for the global normalization. Define boundary values
almost everywhere and
\[
 I_\lambda(X)=\int_{\mathbb R}K(x-X)\log|V_\lambda(x+i0)|\,dx,
\]
\[
 P_{c,\lambda}(X)=
 \sum_{n\ge2}\frac{\Lambda_{\rm vM}(n)}{\log n}
 \frac{n^{-5/2-c/4}}{1+n^{-4}}
 \cos\!\left[\left(\frac X2+\frac{\pi\lambda}{8}\right)\log n\right].
 \tag{E3}
\]

**Theorem.** There are finite constants \(C_*,X_*\), independent of
\(X,c\) in (E1), such that
\[
 \boxed{\left|J_{c/L_X}(X)-I_{c/L_X}(X)+P_{c,c/L_X}(X)\right|
             \le \frac{C_*}{L_X}\qquad(X\ge X_*).}
 \tag{E4}
\]
Section 6 specifies \(C_*\) and a finite onset ledger in terms of
the fixed inherited constants. For any integer \(Q\ge2\),
\[
 |P_{c,\lambda}-P_{c,\lambda,Q}|
 \le\frac{Q^{-3/2-c/4}}{3/2+c/4}
 \le\frac23Q^{-3/2}.
 \tag{E5}
\]
This is not an Euler product for \(H_\lambda\). The ordinary zeta
function enters as an approximation on the two outer lines.

## 2. Harmonic cancellation and complete logarithmic integrability

The explicit logarithm of \(C_-\) in (E2) is holomorphic on the open
strip. Its real part \(u_\lambda=\log|C_-|\) has no interior logarithmic
divisor. Near zero it is \(O(1+|\log|z||^2)\), with gradient
\(O((1+|\log|z||)/|z|)\), uniformly for \(0\le\lambda\le1/2\).
On far vertical sides of the strip it has at most linear plus
logarithmic-square growth. These are the hypotheses checked in
[B01's harmonic-cancellation lemma][b01].

For completeness, removing a small upper semicircle at zero in the
strip Green formula costs \(O(\epsilon(1+\log^2\epsilon))\):
the Green kernel vanishes linearly at the real boundary, its normal
derivative is bounded there, and the arc has length \(O(\epsilon)\).
The far-side terms vanish by exponential harmonic-measure decay.
Consequently \(\mathcal J[C_-]=0\). The exact real-boundary modulus is
\[
 |C_-(\lambda,x+i0)|=
 \frac{\pi^{1/4}}{32}|x|^{7/4}
 \exp\!\left[-\frac{\pi|x|}{8}
 +\frac{\lambda}{16}
       \left(\log^2(|x|/(4\pi))-\frac{\pi^2}{4}\right)\right],
 \quad x\ne0.
 \tag{E6}
\]
At negative \(x\), the upper branch has argument \(\pi\), and its phase
terms give exactly (E6). Both tails and the singularity at zero are retained.

Here is a useful uniform bound, also needed for the remote integral.
Set \(k=\pi^{1/4}/32\), \(\kappa_0=\log(4\pi)\), and
\[
 B_C=|\log k|+\frac{39}{4}+\frac{9\pi^2}{128}
       +\frac{3\pi}{8}+\frac74+2(1+\kappa_0)
       +\frac{(1+\kappa_0)^2}{16}.
\]
For every real \(v\), \(y=0,8\), \(Q_v=|v|+12\), and
\(0\le\lambda\le1/2\),
\[
 \int_v^{v+1}|u_\lambda(x+iy)|\,dx
       \le B_C Q_v\log^2(3Q_v).
 \tag{E7}
\]
To see this directly, put \(r=|z|\), \(\theta=\arg z\) and
\(\ell=\log(r/(4\pi))\). Taking the real part in (E2) gives
\[
 u_\lambda=\log k+\frac74\log r-\frac{\pi x}{8}
 +\frac{\lambda}{16}(\ell^2-\theta^2-\pi^2/4)
 +\frac{x\theta+y(\ell-1)}4+\frac{\pi\lambda\theta}{16}.
\]
On the unit interval, \(r\le Q_v\), \(|x|\le Q_v\), and
\(|\log r|\le\log Q_v+h(x)\), where
\(h(x)=\max(0,-\log|x|)\). This inequality is valid also at \(y=8\).
Use \(\int h\le2\), \(\int h^2\le4\), \(0\le\theta\le\pi\).
If \(B=\log Q_v+\kappa_0\), the integral is at most
\[
 |\log k|+\frac{39}{4}+\frac{9\pi^2}{128}
       +\frac{3\pi Q_v}{8}+\frac74\log Q_v+2B+\frac{B^2}{16}.
\]
Since \(Q_v\ge12\), this is bounded by (E7).

Let \(B_H\) be the constant in the parent's
[unit-interval logarithmic bound][green], renamed to avoid confusion
with the new \(C_*\). Then \(B_V=B_H+B_C\) gives (E7) for
\(|\log|V_\lambda||\) as well. Thus all required boundary integrals
converge absolutely. Subtracting the harmonic carrier from the parent's
complete Green identity yields the **exact** identity
\[
 J_\lambda(X)-I_\lambda(X)=
 \int_{\mathbb R}K(x-X)\log|V_\lambda(x+8i)|\,dx
        -\log|V_\lambda(X+4i)|.
 \tag{E8}
\]
The parent zero-strip input makes the center nonzero. No floor on the
real boundary has been used. There is no extra \(G(X,1)\) term: that
term belongs to the different time-zero gamma/zeta normalization.

## 3. Complete outer field comparison

### 3.1 Fixed provider, charts and retained terms

Use [HDA Ansatz Note04 CS3/CS6][hda04] and its
[Assessment03][hda-review], at their recorded same-model internal scope.
Choose fixed target \(r=1,b=9\). The source's tail constants \(c_9,P_9\)
are fixed before choosing
\[
 V_9\ge\max\{16,17,16c_9,8\sqrt{P_9+6}\}.
\]
Its enlarged initial charts have radius \(V_9+3\), height 10 for
negative smoothing, and radius 2, height \(10+2V_9\) for positive
smoothing. Retain their separate zero-time onsets and the local
gamma/Taylor and large-ray gates in Note04 §§5–8. We only consume the
nonnegative-time field part of CS6. Its whole Gaussian exterior has
already been included; no strip-only remainder is integrated over an
unbounded Gaussian line here.

Let \(U_0\ge4\pi e^{16}\) exceed these onsets and the fixed gamma and
correction onsets below. At each real \(x\ge U_0\), choose the fixed
chart centered at \(x\), with \(N=N_x=\lfloor\sqrt{x/(4\pi)}\rfloor\).
For \(z=x+iy\), \(y=4,8\), the provider says
\[
 |H_\lambda(z)-F_N(\lambda,z)|
       \le h_9 x^{-3/4}(|C_+|+|C_-|),\qquad
       0\le\lambda L_x\le8 ,
 \tag{E9}
\]
with a single finite \(h_9\). The complete approximant is
\[
 F_N=A\sum_{n\le N}w_n\cos(\Theta-\nu(z)\log n)
                   +e^{-\kappa\lambda}\mathcal R_N,\quad
 \kappa=\pi^2/64,\quad \nu(z)=z/2+\pi\lambda/8,
\]
\[
 w_n=n^{-1/2}\exp\{\lambda[(\log n)^2-L(z)\log n]/4\}.
 \tag{E10}
\]
These are [AN01's weights][hda-request] and [Note03 CB26][hda03].
The retained correction is precisely Note04 CS2:
\[
 \mathcal R_N=(-1)^NG(z)a(z)^{-1/2}\mathcal C(a(z)-N),\quad
 a(z)=\sqrt{z/(4\pi)},\quad
 G(z)=[M(s_+)M(s_-)]^{1/2},\quad s_\pm=(1\pm iz)/2,
\]
\[
 M(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)/16,\qquad
 \mathcal C(p)=\frac{\cos(2\pi(p^2-p)-\pi/8)}{\cos(2\pi p)} .
\]
The apparent poles of \(\mathcal C\) are removable.
Sectorial calibration [Note03 CB4][hda03] and Note04 CS25 give finite
\(g_9,f_9\) such that
\[
 |G(z)|\le g_9|A(0,z)|/2,\qquad
 |a(z)^{-1/2}\mathcal C(a(z)-N)|\le f_9 x^{-1/4}.
 \tag{E11}
\]
All constants are uniform in the fractional-cutoff position.

On \(|x-X|\le R\), the gates \(R+8\le X/2\), \(X\ge2U_0\) give
\[
 x\ge X/2\ge U_0,\quad
 |L(z)-L|\le 2(R+8)/X,\quad
 0<\lambda L_x\le1+\log(3/2)/L<2<8.
 \tag{E12}
\]
The logarithm bound follows by integrating \(1/z\) along the segment
from \(X\) to \(z\). Fixed charts are recentered pointwise; their
radius is never increased to \(R\). No floor is differentiated and no
smooth global floor-valued approximant is required.

### 3.2 Reflected population, correction and provider error

For \(x>0\), put \(\theta=\arctan(y/x)\) and \(\ell=\Re L(z)\).
Since \(x\theta\ge y-y^3/(3x^2)\) and \(\ell\ge L_x\),
\[
 \Im\Theta=\{x\theta+y(\ell-1)\}/4+\pi\lambda\theta/16
       \ge yL_x/4-y^3/(12x^2).
\]
Thus, for \(y=4,8\) and \(x\ge U_0\),
\[
 |e^{2i\Theta}|\le A_\rho x^{-y/2},\qquad
 A_\rho=e(4\pi)^4.
 \tag{E13}
\]
The same bound holds at \(\lambda=0\).
For every \(n\le N\), \(\log n\le L_x/2\le\Re L(z)\);
hence \(|w_n|\le n^{-1/2}\) at nonnegative time.
Writing \(p_y=(y+1)/2\), the **entire** reflected sum obeys
\[
 \left|e^{2i\Theta}\sum_{n\le N}w_ne^{-i\nu(z)\log n}\right|
 \le A_\rho x^{-y/2}\sum_{n\le N}n^{(y-1)/2}
 \le A_\rho B_{\rm pop}x^{(1-y)/4},
\]
\[
 B_{\rm pop}=\max_{y=4,8}\frac{2^{p_y}(4\pi)^{-p_y/2}}{p_y}.
 \tag{E14}
\]
Here \(\sum_{n\le N}n^{p_y-1}\le(N+1)^{p_y}/p_y\) and
\(N+1\le2\sqrt{x/(4\pi)}\). This is \(O(x^{-3/4})\) at height 4
and \(O(x^{-7/4})\) at height 8, without a fixed-mode approximation.

Also
\[
 \left|\frac{C_-(\lambda,z)}{C_-(0,z)}\right|
 =\exp\{\lambda[\ell^2-(\theta-\pi/2)^2]/16\}\ge1,
\]
because \(L_x\ge16>\pi/2\). Equations (E11) and (E13) therefore give
\[
 \left|\frac{e^{-\kappa\lambda}\mathcal R_N(z)}{C_-(\lambda,z)}\right|
 \le g_9 f_9\sqrt{A_\rho}\,x^{-(y+1)/4}.
 \tag{E15}
\]
The normalized correction is \(O(x^{-5/4})\) or smaller. From (E9),
the remaining normalized field error is at most
\(h_9(1+A_\rho)x^{-3/4}\). Both arms, every retained mode, the
correction and the full provider remainder have now been paid.

### 3.3 Dominant arithmetic weights, tail and center parameters

The dominant part of \(F_N/C_-\) is exactly
\[
 D_N(z)=\sum_{n\le N}n^{-s_\lambda(z)}
                       e^{\lambda(\log n)^2/4},\qquad
 s_\lambda(z)=s_-(z)+\lambda L(z)/4-i\pi\lambda/8.
\]
Let \(D_j=\sum_{n\ge2}n^{-5/2}(\log n)^j<\infty\), \(j=0,1,2\).
For \(u_n=\lambda(\log n)^2/4\), use
\(0\le e^{u_n}-1\le u_ne^{u_n}\) and
\(\log n\le\Re L(z)/2\). Since \(y\ge4\),
\[
 |n^{-s_\lambda(z)}e^{u_n}|
 \le n^{-(1+y)/2-\lambda\Re L(z)/8}\le n^{-5/2}.
\]
It follows that
\[
 \left|D_N-\sum_{n\le N}n^{-s_\lambda(z)}\right|
          \le\lambda D_2/4.
 \tag{E16}
\]
This inequality sums through the actual growing cutoff. It uses
absolute convergence on the outer lines; it does not apply on the
critical boundary.

The [ordinary Dirichlet series][dlmf-series] gives
\[
 \left|\zeta(s_\lambda(z))-\sum_{n\le N}n^{-s_\lambda(z)}\right|
 \le\frac23N^{-3/2}\le B_Nx^{-3/4},\quad
 B_N=\frac23\,2^{3/2}(4\pi)^{3/4},
\]
where \(N\ge\frac12\sqrt{x/(4\pi)}\).
Set
\[
 s^0_y(x)=\frac{1+y}{2}+\frac c4
               -i\left(\frac x2+\frac{\pi\lambda}{8}\right).
\]
Then \(s_\lambda-s^0_y=\lambda(L(z)-L)/4\). The segment joining
these two arguments has real part at least \(5/2\), so the
[differentiated Dirichlet series][dlmf-derivative] yields
\[
 |\zeta(s_\lambda)-\zeta(s^0_y)|
 \le D_1\lambda|L(z)-L|/4
 \le \frac{D_1\lambda(R+8)}{2X}.
 \tag{E17}
\]
This retains the phase \(+\pi\lambda/8\) and never replaces the
fixed time by \(c/L_x\) inside an integral.

Combining (E9)–(E17), define
\[
 A_F=B_N+A_\rho B_{\rm pop}+g_9f_9\sqrt{A_\rho}
                       +h_9(1+A_\rho),\qquad
 C_F=\frac{D_2}{4}+\frac{D_1}{2}+2^{3/4}A_F.
\]
After the additional gate \(L X^{-3/4}\le1\), we have
\[
 \boxed{|V_\lambda(x+iy)-\zeta(s^0_y(x))|
                  \le C_F/L,\quad y=4,8,\quad |x-X|\le R.}
 \tag{E18}
\]
These constants depend only on the fixed source/provider and buffers,
not on \(X,c\). The estimate is uniform through every cutoff crossing.

## 4. Safe-line logarithms and both remote directions

For \(\Re s\ge5/2\),
\[
 |\zeta(s)-1|\le D_0
 \le2^{-5/2}+\int_2^\infty u^{-5/2}\,du
 =\frac7{12\sqrt2}<\frac12.
\]
Choose the finite onset so that \(L>4C_F\). Then (E18) implies
\(|V_\lambda|>1/4\) on the stated outer windows and
\[
 \left|\log|V_\lambda(x+iy)|
             -\log|\zeta(s^0_y(x))|\right|
 \le4C_F/L.
 \tag{E19}
\]
This uses the real-log mean-value inequality with the minimum modulus
greater than \(1/4\). It is not a floor at \(y=0\).

For the exact remote upper boundary, apply (E7) for \(V\) to both
directions in unit shells. Put \(a=\pi/8\), \(q=e^{-a}\),
\(m=\lfloor R\rfloor\), \(S=X+13+m\), and
\[
 T_3(q)=\sum_{j\ge0}(j+1)^3q^j
             =\frac{1+4q+q^2}{(1-q)^4}.
\]
On either shell \(K(x-X)\le e^{-a(m+j)}/8\), and its unit-interval
parameter is at most \(S+j\). Since
\((S+j)\log^2(3(S+j))\le S\log^2(3S)(1+j)^3\),
\[
 \int_{|x-X|>R}K(x-X)|\log|V_\lambda(x+8i)||\,dx
 \le \frac{B_V}{4}e^{-am}S\log^2(3S)T_3(q)
 \le D_VX^{-3}\log^2X,
\]
\[
 D_V=2e^aB_VT_3(q).
 \tag{E20}
\]
For the last inequality use \(X\ge26\), \(R\le X/2\), hence
\(S\le2X\), \(\log(3S)\le2\log X\), and
\(e^{-am}\le e^aX^{-4}\). The same bound is valid at \(y=0\);
the unit interval containing zero was already paid in (E7).
No global use of the near-height approximant occurs in (E20).

The [Euler product][dlmf-euler] gives, on \(\Re s\ge5/2\), the
absolutely convergent logarithm with prime-power coefficients
\(\Lambda_{\rm vM}(n)/\log n\in[0,1]\). Thus
\(|\log|\zeta(s)||\le D_0\), and its corresponding remote tail is at most
\[
 D_ZX^{-4},\qquad D_Z=D_0/(4a),
 \tag{E21}
\]
using \(\int_{|t|>R}K(t)\,dt\le e^{-aR}/(4a)\).
The true logarithm and comparison logarithm have therefore each been
paid on the full exterior.

## 5. Prime combination, sign and uniform tail

Write \(\sigma_y=(1+y)/2+c/4\). Absolute convergence of the Euler
logarithm on both outer lines permits
\[
 \log|\zeta(s^0_y(x))|=
 \sum_{n\ge2}\frac{\Lambda_{\rm vM}(n)}{\log n}
 n^{-\sigma_y}\cos[(x/2+\pi\lambda/8)\log n].
\]
The parent's [kernel transform][prime] is
\[
 \widehat K(\omega)=\frac12\operatorname{sech}(4\omega),\qquad
 \widehat K((\log n)/2)=(n^2+n^{-2})^{-1}.
\]
Evenness of \(K\) retains the center phase in (E3). The coefficient
of upper boundary minus center is exactly
\[
 \frac{n^{-9/2-c/4}}{n^2+n^{-2}}-n^{-5/2-c/4}
       =-\frac{n^{-5/2-c/4}}{1+n^{-4}}.
\]
Therefore
\[
 \int_{\mathbb R}K(x-X)\log|\zeta(s^0_8(x))|\,dx
       -\log|\zeta(s^0_4(X))|=-P_{c,\lambda}(X).
 \tag{E22}
\]
The kernel mass \(1/2\) has not been replaced by one.
Finally, summing \(n^{-5/2-c/4}\) for integers \(n>Q\) and applying
the integral test proves (E5), uniformly in \(X,c\).

## 6. Assembly, constants and onset ledger

Use (E8), (E19) and (E22). The compact upper integral costs at most
\(2C_F/L\), and the center at most \(4C_F/L\). Equations (E20)–(E21)
give the stronger explicit bound
\[
 |J_\lambda-I_\lambda+P_{c,\lambda}|
 \le \frac{6C_F}{L}
           +D_VX^{-3}\log^2X+D_ZX^{-4}.
 \tag{E23}
\]
Set
\[
 C_*=6C_F+D_V+D_Z.
 \tag{E24}
\]
Choose one \(X_*\) beyond all the following eventual gates, so they
hold for every \(X\ge X_*\):

| Gate | Purpose |
| --- | --- |
| Freeze \(c_9,P_9,V_9\) and all fixed enlarged charts before their onsets | Pays the inherited Gaussian exterior and source remainders with their actual fixed-buffer constants. |
| \(X\ge\max(26,2U_0)\), with \(U_0\ge4\pi e^{16}\) and all provider/gamma/correction onsets | All recentered charts satisfy the inherited hypotheses; \(0<\lambda\le1/2\), \(N\ge a(x)/2\), and carrier ratios are controlled. |
| \(R_X+8\le X/2\) | Logarithm comparison, recentered time band and exterior simplification. |
| \(L_XX^{-3/4}\le1\) | Absorbs polynomial field errors into \(C_F/L_X\). |
| \(L_X>4C_F\) | Supplies the independent safe-line logarithmic floor. |
| \(L_XX^{-3}\log^2X\le1\) | Absorbs both remote logarithmic tails into (E24). |

Every gate is eventual; all constants were fixed first and are
independent of \(X,c\). This proves (E4). The constants depend on
\(h_9,g_9,f_9\), the inherited fixed-buffer/onset data, the parent
unit-log constant \(B_H\), and the displayed universal constants
\(D_j,B_C,A_\rho,B_N,B_{\rm pop}\). The finite onset is specified
analytically, not numerically evaluated.

For the frozen defect parameters \(d=1/2,r=1\), let
\[
 m_*=\frac{\sin(\pi/8)}{2\cosh(\pi/8)}.
\]
The additional gate \(L_X>4C_*/m_*\) makes the new allowance smaller
than \(m_*/4\). A source-acquired upper value \(U(X,c)\) for
\(I_\lambda-P_{c,\lambda}\) would exclude the specified defect only
if \(U(X,c)+C_*/L_X<m_*\). **No such favorable upper value is proved
here.** Positivity of \(J\) supplies the opposite lower comparison
\(I_\lambda-P_{c,\lambda}\ge-C_*/L_X\), not the needed upper bound.

## 7. Control screen, scope and return

The proof uses the complete arithmetic HDA provider, not just the
heat equation or source positivity. The [B01 control screen][b01]
and [overview table][overview] remain in force, checked at the actual
points of use:

- Euler/translated sources do not retain the unchanged completion and
  Dirichlet coefficients used in (E9)–(E17).
- Weighted-square, finite-prefix and finite-prime controls do not
  retain the complete normalized arithmetic/reflected expansion.
- Reflected super-Gaussian and smooth/positive-primitive controls
  lack the gamma-times-ordinary-zeta arithmetic used here.
- Counter-kernels \(q,q_{T,a}\), atomic and finite-profile controls
  lack the same completed field and full source/profile.
- RH-conditional endpoint controls lack the ordinary Dirichlet
  arithmetic; their conditional status is not changed.
- Variable theta readouts lack the literal cosine/Newman evolution;
  the three-profile relaxation lacks the full integer zero measure.

These are failed premises for unchanged use of this proof, not
assertions that every control violates its final approximation.
The harmonic normalization holds for eligible controls as well.
An outer-baseline identity is compatible with a positive Green value,
so it is not a collision discriminator. No finite control check has
been substituted for the uniform proof or an RH-equivalent claim.

All four request groups are complete at the stated inherited-input
and same-assistant checking scope. The separate-magnitude failure
from B01 remains a failure of that specified envelope; E01 does not
repair its lost phase information or turn it into a lower bound on \(H\).
No time-zero extension, other time band, shrinking defect depth,
finite initial-range certificate, collision survival or zero exclusion
is claimed.

The [continuation/model-change note][return] recommends **GPT-6 Astra**
for a bounded B decision on an independent phase-sensitive upper estimate
of the remaining \(I_\lambda-P_{c,\lambda}\). That task is not activated
by this E return. The parent retains its separate time-zero value question.

[request]: ../research-progress/handoffs/01_GNP_RS_E01_UNIFORM_OUTER_BASELINE_R1_20261111.md
[b01]: 01_GNP_RS_B01_TRANSITION_SCALE_GREEN_BASELINE_20261111.md
[review]: ../reviews/03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_SELF_CHECK_20261111.md
[record]: ../numerics/03_GNP_RS_E01_INPUTS_AND_CHECKS_20261111.json
[return]: 04_GNP_RS_E01_RETURN_AND_MODEL_CHANGE_20261111.md
[overview]: ../research-overview/01_GNP_RS_RESEARCH_OVERVIEW_20261110.md
[green]: ../../manuscript/sections/05_green.tex
[prime]: ../../manuscript/sections/06_prime.tex
[hda03]: ../../../01_heat_density_asymptotics/ansatz/notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md
[hda04]: ../../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[hda-review]: ../../../01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md
[hda-request]: ../../../01_heat_density_asymptotics/ansatz/research-progress/handoffs/HDA-A01-AN01.md
[dlmf-series]: https://dlmf.nist.gov/25.2.E1
[dlmf-derivative]: https://dlmf.nist.gov/25.2.E6
[dlmf-euler]: https://dlmf.nist.gov/25.2.E11
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
