# A uniform outer-cusp four-jet asymptotic and strict Laguerre signs

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded current-turn model: **gpt-6-astra (Codex)**; reasoning effort
**ultra**, verified from the local turn metadata. Parallel analytic,
geometric, computational, and independent internal review work supported
this continuation.

This continues the all-height target from
[Note 16](16_THETA_CENTERED_RESIDUAL_AND_SHARED_ARITHMETIC_20261014.md).
It proves the required signs on an unbounded outer part of the small-time
region, while identifying why the inner part still needs cancellation
after integration. The [internal review](../reviews/12_UNIFORM_OUTER_CUSP_INTERNAL_REVIEW_20261014.md)
records the independent proof check and diagnostic replay.

## 1. Result and scope

Write

\[
 h_k(t,x)=\partial_x^k H_t(x),\qquad
 L=\log\frac{x}{4\pi},\quad \theta=tL,\quad \omega=\frac L4,
\]

and

\[
 \mathcal L_0=h_1^2-h_0h_2,\qquad
 \mathcal L_1=h_2^2-h_1h_3.
\]

**Proposition.** For each fixed \(\varepsilon>0\), there is
\(X_\varepsilon<\infty\) such that, uniformly on

\[
 x\ge X_\varepsilon,\qquad 0<t\le\tfrac12,
 \qquad t\log(x/(4\pi))\ge4+\varepsilon,
 \tag{1}
\]

there is an explicitly defined nonzero complex carrier \(Q=Q_t(x)\) with
phase \(\phi=\arg Q\), for which

\[
 \frac{1}{2|Q|}
 \left(h_0,\frac{h_1}{\omega},\frac{h_2}{\omega^2},
                  \frac{h_3}{\omega^3}\right)
 = (\cos\phi,-\sin\phi,-\cos\phi,\sin\phi)
       +O_\varepsilon(L^{-1}).
 \tag{2}
\]

Consequently, uniformly in the whole region (1),

\[
 \begin{aligned}
 h_0^2+(h_1/\omega)^2
   &=4|Q|^2\bigl(1+O_\varepsilon(L^{-1})\bigr),\\
 \mathcal L_0
   &=4|Q|^2\omega^2\bigl(1+O_\varepsilon(L^{-1})\bigr),\\
 \mathcal L_1
   &=4|Q|^2\omega^4\bigl(1+O_\varepsilon(L^{-1})\bigr).
 \end{aligned}
 \tag{3}
\]

In particular both Laguerre quantities are strictly positive everywhere
in (1), after increasing \(X_\varepsilon\). No stationary-set hypothesis
is needed. This implies the required strict stationary signs, and excludes
\(h_0=h_1=0\), throughout this outer region.

This is an explicit consequence developed here from the effective
Riemann–Siegel estimate in D. H. J. Polymath,
[Theorem 1.3, equations (6)–(24)](https://arxiv.org/html/1904.12438v2#S1).
There is no priority claim. The theorem covers an unbounded region but
does not settle the remaining small-time cusp \(tL\le4+o(1)\).

## 2. Analytic carrier and imported estimate

Use the principal logarithm, and define

\[
 \begin{aligned}
 M_0(s)&=\frac{s(s-1)}{16}\pi^{-s/2}\sqrt{2\pi}
  \exp\left(\left(\frac s2-\frac12\right)\operatorname{Log}\frac s2
                  -\frac s2\right),\\
 \alpha(s)&=\frac{M_0'(s)}{M_0(s)}
       =\frac{1}{2s}+\frac{1}{s-1}
                      +\frac12\operatorname{Log}\frac{s}{2\pi},\\
 M_t(s)&=M_0(s)\exp\left(\frac t4\alpha(s)^2\right),\\
 s_\pm(z)&=\frac{1\pm iz}{2},\qquad
 w_\pm(z)=s_\pm(z)+\frac t2\alpha(s_\pm(z)),\\
 Q_\pm(z)&=M_t(s_\pm(z))\zeta(w_\pm(z)),\qquad
 \mathcal A_t(z)=Q_+(z)+Q_-(z).
 \end{aligned}
 \tag{4}
\]

The branches in (4) are analytic in all discs used below; their arguments
stay at imaginary part approximately \(\pm x/2\), away from the branch
cut. For real \(x\), set \(Q=Q_+(x)\). Schwarz symmetry gives
\(Q_-(x)=\overline Q\).

For \(z=u+iv\), \(u\ge200\), \(0\le v\le1\), set

\[
 N=N(u,t)=\left\lfloor\sqrt{\frac{u}{4\pi}+\frac{t}{16}}\right\rfloor,
 \quad
 S_{t,N}(w)=\sum_{n\le N}e^{t\log^2 n/4}n^{-w}.
\]

Theorem 1.3 of the cited paper implies

\[
 H_t(z)=M_t(s_-(z))S_{t,N}(w_-(z))
       +M_t(s_+(z))S_{t,N}(w_+(z))+\mathcal E_{RS}(z),
 \tag{5}
\]

with
\(|\mathcal E_{RS}|\le |M_t(s_-)|(e_A+e_B+e_{C,0})\),
where its explicit error estimates (23)–(24) will be bounded in Section 4.
Formula (5) is exactly the paper's two branches, not a new asymptotic
identification: its \(s_*\) is \(w_-\), and its second exponent satisfies
\(\overline{s_*}+\kappa-v=w_+\).

We apply this estimate pointwise even where \(N\) changes. **No derivative
of \(N\), or of the discontinuous finite-sum approximation, is taken.**
Only the analytic difference \(H_t-\mathcal A_t\) is differentiated later.

## 3. Uniform conversion of the weighted sum into zeta

Fix a real pair \((t,x)\) satisfying (1), with \(x\) sufficiently large
depending on \(\varepsilon\). Throughout the disc

\[
 D_x=\{z:|z-x|\le L^{-1}\},
 \tag{6}
\]

put \(L_u=\log(u/(4\pi))\) and \(\theta_u=tL_u\). Then

\[
 L_u=L+O((xL)^{-1}),\qquad
 \theta_u\ge4+\varepsilon/2,
 \qquad |v|\le L^{-1},
 \tag{7}
\]

once \(x\) is large enough. All subsequent constants may depend on
\(\varepsilon\), but never on \(t\), \(x\), or \(\theta_u\) within these
ranges.

Directly from (4), uniformly on (6),

\[
 \operatorname{Re}w_\pm(z)
 \ge\frac12-\frac{|v|}{2}+\frac{\theta_u}{4}-O(t/u),
 \qquad
 \log N\le\frac{L_u}{2}+O(u^{-1}).
 \tag{8}
\]

Thus, for \(1\le n\le N\),

\[
 e^{t\log^2n/4}n^{-\operatorname{Re}w_\pm(z)}
 \le n^{-p},\qquad
 p=\frac12+\frac{\theta_u}{8}-\delta_x,
 \tag{9}
\]

where \(\delta_x=|v|/2+O(u^{-1})\) may be chosen nonnegative, uniformly
tending to zero. Increase the lower threshold for \(x\) until
\(\delta_x\le\varepsilon/32\). Set \(\theta_0=4+\varepsilon/2\). Then

\[
 p\ge1+\frac{\varepsilon}{32}
                    +\frac{\theta_u-\theta_0}{8}.
 \tag{10}
\]

In particular, all weighted absolute sums in (9) are uniformly bounded.
Also (8) gives \(\operatorname{Re}w_\pm\ge5/4\), with room to spare.

For \(q\ge0\), \(e^q-1\le q e^q\). Therefore

\[
 \begin{aligned}
 |S_{t,N}(w)-\zeta(w)|
 &\le\frac t4\sum_{n=2}^{N}(\log n)^2
                      e^{t\log^2n/4}n^{-\operatorname{Re}w}
                  +\sum_{n>N}n^{-\operatorname{Re}w}\\
 &\le\frac t4\sum_{n=2}^{\infty}(\log n)^2n^{-p}
                   +\frac{N^{1-\operatorname{Re}w}}
                                {\operatorname{Re}w-1}.
 \end{aligned}
 \tag{11}
\]

This estimate needs uniformity when \(\theta_u\) grows, and not only when
\(t=\theta/L\) with a fixed \(\theta\). To see that uniformity explicitly,
write \(s=\theta_u-\theta_0\ge0\) and set

\[
 D_\varepsilon=\sum_{n=2}^{\infty}
       (\log n)^2 n^{-1-\varepsilon/32}<\infty.
\]

Then the first term of (11) is at most

\[
 \frac{D_\varepsilon}{4L_u}(\theta_0+s)2^{-s/8}
       =O_\varepsilon(L^{-1}),
 \tag{12}
\]

because the function of \(s\) in the numerator is bounded on
\([0,\infty)\). The second term of (11) is
\(O(N^{-1/4})=O(x^{-1/8})\). This deliberately conservative bound is
sufficient. We have proved the uniform estimate

\[
 S_{t,N}(w_\pm(z))-\zeta(w_\pm(z))
                 =O_\varepsilon(L^{-1})\quad(z\in D_x).
 \tag{13}
\]

The constant 4 arises here from the endpoint exponent
\(1/2+\theta/8>1\). It is a sufficient threshold for this absolute-sum
argument; no optimality claim is made.

## 4. The Riemann–Siegel errors and the complex disc

For the upper half of \(D_x\), the paper's error bound (23) contains
weighted sums bounded by (9)–(10). More explicitly, its weights are

\[
 (1+|\gamma|N^{|\kappa|}n^v)
       e^{t\log^2n/4}n^{-\operatorname{Re}w_-}.
\]

The estimates \(|\gamma|\le e^{0.02v}(u/(4\pi))^{-v/2}\) and
\(|\kappa|\le tv/(2(u-6))\) make their extra constant factors uniformly
bounded. The factor \(n^v\) changes the lower bound in (8) from
\((1+v)/2\) to \((1-v)/2\), which is already included in (9).
Moreover, for \(n\le N\),

\[
 \left|\log\frac{u}{4\pi n^2}\right|\le L_u+O(u^{-1}).
\]

Its exponential error multiplier is therefore
\(O((1+\theta_u^2)/u)\), uniformly, since
\(\theta_u\le L_u/2\). In particular,

\[
 e_A+e_B=O_\varepsilon(L^2/x).
 \tag{14}
\]

The paper's (24) gives, using (7),

\[
 e_{C,0}
 \le C\exp\left(-\frac{L_u}{4}
                   -\frac{\theta_u L_u}{16}\right)
 \le C_\varepsilon x^{-1/2}.
 \tag{15}
\]

The remaining factors in that formula are bounded uniformly: \(v\le1/L\),
\(N\asymp\sqrt x\), and its explicit correction exponent tends to zero.
There is no omitted source remainder in (14)–(15); these bounds include
all three errors from Theorem 1.3.

Let \(\Gamma=|M_t(s_+(x))|\). On \(D_x\),

\[
 |M_t(s_\pm(z))|\asymp\Gamma.
 \tag{16}
\]

Indeed the logarithmic derivative with respect to \(z\) is \(O(L)\),
uniformly for \(0<t\le1/2\), and the disc radius is \(1/L\). This is why
the shrinking disc (6) is used. On a fixed-radius disc, one must not
silently replace these gamma magnitudes by a constant multiple of
\(\Gamma\).

Combining (5), (13), (14), (15), and (16), on the upper half-disc gives

\[
 H_t(z)-\mathcal A_t(z)=O_\varepsilon(\Gamma/L).
 \tag{17}
\]

Both \(H_t\) and \(\mathcal A_t\) obey Schwarz symmetry, so (17) holds on
the lower half-disc as well. No extension of the paper's hypothesis
\(v\ge0\) is being assumed.

On the whole disc \(\operatorname{Re}w_\pm\ge5/4\). Absolute convergence
of the Dirichlet series for \(\zeta\) and \(1/\zeta\) gives

\[
 |\zeta(w_\pm)|\le\zeta(5/4),\qquad
 |\zeta(w_\pm)|\ge\zeta(5/4)^{-1}>0.
 \tag{18}
\]

Thus \(Q\ne0\) and \(|Q|\asymp\Gamma\), with absolute constants after
the lower threshold in \(x\) is imposed. This lower bound comes from a
zeta Euler/Dirichlet-series half-plane; it assumes nothing about a norm
of \(H_t\) or a collision gap.

The function \(H_t-\mathcal A_t\) is analytic on a neighborhood of
\(D_x\). Cauchy's formula applied to (17) now gives, with \(t\) held fixed,

\[
 \partial_x^k(H_t-\mathcal A_t)(x)
       =O_{\varepsilon,k}(|Q|L^{k-1}),
       \qquad k=0,1,2,3.
 \tag{19}
\]

At \(k=0\), this notation means \(O_\varepsilon(|Q|/L)\). The moving
cutoff has already disappeared into the uniform pointwise estimate (17),
so its jumps create no differentiation issue.

## 5. Four jets of the analytic carrier

At the real center, elementary differentiation of (4) yields

\[
 \alpha(s_+(x))=\frac L2+\frac{i\pi}{4}+O(x^{-1}),\qquad
 \alpha^{(r)}(s_+(x))=O_r(x^{-r})\quad(r\ge1).
 \tag{20}
\]

All fixed derivatives of \(\log\zeta(w)\) are uniformly bounded in
\(\operatorname{Re}w\ge5/4\): this follows either from its absolutely
convergent prime-power series or from derivatives of its Dirichlet
series together with (18). A local logarithm of \(Q_+\) therefore satisfies

\[
 \begin{aligned}
 (\log Q_+)'(x)
 &=\frac i2\left[
    \alpha+\frac t2\alpha\alpha'
    +\left(1+\frac t2\alpha'\right)
          \frac{\zeta'(w_+)}{\zeta(w_+)}\right]\\
 &=i\omega+O_\varepsilon(1),\\
 (\log Q_+)''(x)&=O_\varepsilon(1),\qquad
 (\log Q_+)'''(x)=O_\varepsilon(1).
 \end{aligned}
 \tag{21}
\]

All \(\alpha\)'s in the first line are evaluated at \(s_+(x)\).
For example, the gamma part of the second derivative is
\(O(x^{-1}+tL/x^2)\); the bounded zeta logarithmic derivatives dominate
the coarse bounds shown. These bounds are uniform when \(\theta\) is
unbounded as well, since \(t\le1/2\).

The usual formulas for derivatives of an exponential then give

\[
 Q_+^{(k)}(x)
   =Q\left((i\omega)^k+O_\varepsilon(L^{k-1})\right),
            \qquad k=1,2,3.
 \tag{22}
\]

The assertion for \(k=0\) is exact without an error. Since the derivatives
of \(Q_-\) along the real axis are conjugates of those of \(Q_+\),
(19) and (22) prove (2).

## 6. Quadratic signs and consequences

Put
\(P_k=h_k/(2|Q|\omega^k)\). Then (2) gives

\[
 (P_0,P_1,P_2,P_3)
 =(c,-s,-c,s)+O_\varepsilon(L^{-1}),\quad c^2+s^2=1.
\]

The errors are uniform in phase, including where individual leading jets
vanish. Therefore

\[
 P_0^2+P_1^2=1+O_\varepsilon(L^{-1}),\quad
 P_1^2-P_0P_2=1+O_\varepsilon(L^{-1}),\quad
 P_2^2-P_1P_3=1+O_\varepsilon(L^{-1}),
\]

which proves (3). This phase-independent computation is stronger than
separately restricting to \(h_1=0\) or \(h_2=0\).

At a stationary point \(h_1=0\), it follows that
\(-h_0h_2>0\); at a stationary point \(h_2=0\), it follows that
\(-h_1h_3>0\). There is no common zero \(h_0=h_1=0\) in (1).

If a sequence of positive-time real double zeros \((T_m,a_m)\) has
\(0<T_m\le1/2\) and \(a_m\to\infty\), then this proposition implies

\[
 \limsup_{m\to\infty}T_m\log\frac{a_m}{4\pi}\le4.
 \tag{23}
\]

Equivalently, for every fixed \(\varepsilon>0\), sufficiently high
positive-time collisions are confined to the inner cusp
\(t\log(x/(4\pi))<4+\varepsilon\). Evenness gives the analogous statement
at negative real heights with \(|x|\).

The cutoff \(X_\varepsilon\) has not been made numerical here. Its
existence follows from explicit primary estimates and the elementary
uniform bounds above. The proof neither settles the inner cusp nor
asserts positivity of \(\partial_t(h_0^2+h_1^2)\) everywhere. It proves
precisely the two signed Laguerre estimates and the balanced norm estimate.

## 7. Quantitative algebra and the octonionic target

The last step can be made explicit without yet evaluating the analytic
height cutoff. Suppose each error in the normalized four-jet vector (2)
is at most \(\delta\). Direct expansion, using \(|c|,|s|\le1\), gives

\[
 P_0^2+P_1^2\ge1-4\delta,\qquad
 P_1^2-P_0P_2\ge1-4\delta-\delta^2,\qquad
 P_2^2-P_1P_3\ge1-4\delta-\delta^2.
 \tag{24}
\]

For example,
\(({-s}+e_1)^2-(c+e_0)({-c}+e_2)
=1-2se_1+e_1^2-ce_2+ce_0-e_0e_2\).
Keep the nonnegative square, bound the linear terms by \(4\delta\),
and pay the remaining product by \(\delta^2\). The second form has
exactly the same structure. At \(\delta=1/8\), the norm lower bound is
\(1/2\) and both signed lower bounds are \(31/64\). Thus a numerical
choice of \(X_\varepsilon\) can eventually be based on this concrete
error target, rather than an unspecified sign test.

In [Note 15's conventions](15_OCTONIONIC_LIFT_AND_ASSOCIATOR_SIGN_TARGET_20261014.md),
\(\mathcal A_j=2\mathbf u\mathcal L_j\) for the fixed oriented octonionic
unit \(\mathbf u=\ell\mathbf j\). The theorem puts both associators
strictly on their prescribed positive ray throughout (1). In particular
\(\mathcal A_t=\mathbf u E_t\) has the required positive orientation
on the genuine stationary union. The arithmetic estimate supplies the
sign information; the octonionic representation preserves its geometric
meaning. No order on all octonions is being introduced.

The normalized four jets in (2) are, to controlled error, determined by
one complex phase and one amplitude. Keeping the common phase is what
makes both quadratic signs reduce to \(\cos^2\phi+\sin^2\phi\). The
argument does not divide by any physical jet, which may vanish.

## 8. What must be retained in the inner region

The constant 4 is the threshold of the absolute summability argument in
(9), not an asserted intrinsic boundary. Below it, the exact arithmetic
carrier of Note 16 retains phase correlations that a termwise modulus
bound can lose. The following finite diagnostics make this distinction
concrete.

At a fixed common-carrier coordinate \(v=b\), set

\[
 d_n=\tfrac12\log n,\quad
 D_j=\sum_{n\le e^{2b}}A_n(t,x;b)[-a+i(b-d_n)]^j,
 \quad j=0,1,2,3,
\]

with exactly Note 16's weights, and write the unit phase of the common
carrier \(e^{t(b+ia)^2}\phi_1(b+ia)e^{ixb}\) as \(U\). For the
pointwise real integrand jets \(p_j=\operatorname{Re}(UD_j)\), define

\[
 \mathfrak H_j=|D_{j+1}|^2-\operatorname{Re}(D_j\overline{D_{j+2}}),
 \qquad \mathfrak W_j=D_{j+1}^2-D_jD_{j+2}.
\]

The exact identity is

\[
 2(p_{j+1}^2-p_jp_{j+2})
   =\mathfrak H_j+\operatorname{Re}(U^2\mathfrak W_j).
 \tag{25}
\]

Thus positivity for every possible phase would require
\(\mathfrak H_j\ge|\mathfrak W_j|\). The retained Arb/Acb record
rigorously rejects that stronger condition at two points with
\(a=\pi/16\) and the prescribed
\(b=\tfrac14\log((x+2ta)/(4\pi\sin4a))\):

- \(x=211,\ t=1/\log211\):
  \(\mathfrak H_0-|\mathfrak W_0|\approx-0.0277198\).
- \(x=4898.7,\ t=2/\log4898.7\):
  \(\mathfrak H_0-|\mathfrak W_0|\approx-1.26105\).

At the second point, even the actual carrier phase yields
\(p_1^2-p_0p_2\approx-0.01099197\). These are exact finite-sum
integrand objects enclosed by ball arithmetic. They are not the
Laguerre forms of the integrated theta function. The counterexample
therefore rules out a proposed pointwise positive-integrand proof in
that region, while leaving integration-level signed cancellation viable.
The record uses the parameter \(t\log x=1\) or \(2\), stated explicitly;
these points are outside the outer theorem's domain.

There is a second reason to keep a one-sided target. The elementary
backward heat solution

\[
 P(t,y)=y^2-d^2-2t\qquad(d\ge0)
\]

has real zeros and \(\mathcal L_0=2y^2+2d^2+4t>0\),
\(\mathcal L_1=4\) for \(t>0\). At \(y=0\), let \(D=d^2+2t\).
Then \(P=-D,\ P_y=0,\ E=D^2\), while the centered residuals are
\(C_0=-2+\mu D\), \(C_1=-4a\). Any two-component relative cone must
therefore pay

\[
 \eta\ge\frac{\sqrt{(2-\mu D)^2+16a^2}}{D}.
 \tag{26}
\]

For bounded prescribed \(a,\mu\), this can become large as the pair
closes, even though the necessary negative loss is zero. This is a
control example, not a counterexample for theta. Growth as \(t\downarrow0\)
also does not contradict local boundedness at every positive time.
It demonstrates why a small relative cone can demand unnecessary control
of favorable curvature.

The preferred unresolved target remains

\[
 \boxed{h_jC_j\ge-\mu h_j^2-K_j E
 \quad\text{on }h_{j+1}=0,\quad j=0,1,}
 \tag{27}
\]

with \(K_j\ge0\) locally bounded through each candidate positive-time
collision and the full source and integration errors retained. This is
exactly the sufficient lower bound \(\mathcal L_j\ge-K_jE\).
The strong relative cone remains an available sufficient certificate
where its slack can be verified.

## 9. Remaining work and reproducible checks

For a fixed \(\varepsilon>0\), the currently unresolved domain consists
of the finite transition strip \(104<|x|<X_\varepsilon\), together with
the high-height inner region
\(0<t\le1/2,\ |x|\ge X_\varepsilon,\quad
 t\log(|x|/(4\pi))<4+\varepsilon\).
The previous physical gap through height 104 remains the finite baseline;
no new finite cover is asserted here.

Two concrete next steps follow. First, turn the uniform bounds above into
an explicit, preferably usable, value of \(X_\varepsilon\). Second,
replace the absolute arithmetic bound at the transition scale with
controlled oscillatory sums, retaining their logarithmic moments and
integration cross terms. The latter may lower the threshold 4, but that
improvement and the full one-sided inner-region estimate are not proved
in this note. Setting \(\varepsilon=0\) in the existing argument is not
justified: its summable majorant and constants depend on a positive gap.

The [diagnostic driver](../numerics/check_outer_cusp_and_phase_obstructions.py)
and [small record](../numerics/OUTER_CUSP_AND_PHASE_OBSTRUCTION_CHECKS_20261014.json)
retain the exact perturbation algebra, the finite-sum counterexamples,
selected complete-source point enclosures, and staircase identities.
The record binds its producing source and the imported complete-source
contour checker. With python-flint available, from the numerics folder:

```sh
python3 check_outer_cusp_and_phase_obstructions.py --output /tmp/outer-cusp-checks.json
```

The point diagnostics neither assert stationarity at their selected
points nor establish a whole-cell or all-height numerical certificate.
The uniform theorem rests on Sections 2–6 and the cited primary estimate.
The [independent internal review](../reviews/12_UNIFORM_OUTER_CUSP_INTERNAL_REVIEW_20261014.md)
separates that analytic proof from the diagnostic replay. No manuscript
revision, numerical finite-height extension, or RH conclusion is claimed.
