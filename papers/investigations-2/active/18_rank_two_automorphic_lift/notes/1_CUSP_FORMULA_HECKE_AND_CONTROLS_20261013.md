# The insertion-transported rank-two lift: cusp formula, Newman time, Hecke at 2 and the control test

**Scope correction, 13 October 2026.** Prepared for Edward Baker with
substantial LLM assistance by `gpt-6-astra` (Codex), effort **ultra**.
Control summaries now distinguish tracked branch times from the global
constant and raw from normalized witness margins. The finite-prime
obstruction and A4 gate have their complete hypotheses stated. The
identities, original numerical records and Claude provenance are preserved.

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.

Internal research note for tasks A1–A3 of the
[program](INITIAL_RESEARCH_PROGRAM_20261013.md). Statements labelled
Theorem or Proposition have proofs here. Numerical statements come from the
[checker](../numerics/check_rank_two_lift_claude_20261013.py) and its
[record](../numerics/RANK_TWO_LIFT_RECORD_20261013.json): double-precision
quadrature, not interval certificates. No collision exclusion, zero-free
region or RH implication is claimed.

## Result and decision

1. **Cusp formula (Theorem 1).** For every shape \(r\) and complex
   spectral variable \(\kappa\), the volume transform of the theta pair
   source is a fourth-order operator applied to the cusp part of the
   completed Eisenstein series on the imaginary-axis geodesic. The physical
   insertion, in both variables, annihilates all four constant-term powers.
   (The insertion is \((\partial^2-1)/16\) acting on \(e^u\theta(e^{4u})\),
   equivalently \((\partial^2-1)/8\) on \(e^u\psi(e^{4u})\).) No
   renormalization or folding term remains.
2. **Newman time (Theorem 2).** At every \(t\ge0\), both Laguerre
   expressions \(\mathscr L_0=H_x^2-HH_{xx}\) and
   \(\mathscr L_1=H_{xx}^2-H_xH_{xxx}\) are folded moments of this cusp
   kernel. The Newman weight enters only through a Gaussian average of the
   spectral parameter and the geodesic weight \(e^{(t/8)(\log y)^2}\). The
   formula is explicit and absolutely convergent, and it agrees with direct
   computation to \(6\cdot10^{-15}\) relative at \((t,x)=(0,8)\),
   \((0.05,8)\) and \((0.05,28.27)\).
3. **Two-coset identity (Theorem 3).** Card 09's parity-coset identity with
   unequal-scale coupling is the Hecke correspondence at 2. It holds exactly
   at every Newman time. Its arithmetic content is the 2-adic
   self-similarity of \(\Phi\), the Euler factor at 2.
4. **Control test (Proposition 4).** Every Euler-factor control
   \(\Phi_{c,p}\) has the same cusp kernel, tested against translated
   weights, and satisfies the Hecke relation at every prime \(q\ne p\).
   Since \(\Lambda_{c,p}>0\), a finite set of these Hecke relations,
   together with other hypotheses also shared by the controls, cannot
   prove \(\Lambda\le0\).
5. **Diagnostics.** At the tested heights \(x\le42\) the first Whittaker
   mode carries \(\mathscr L_0\) to within 13%. From \(x\approx46\) the
   second mode is a quarter or more of \(\mathscr L_0\), and at \(x=100\)
   the first two modes are \(+1.85\) and \(-1.15\) times \(\mathscr L_0\).
   The folded kernel is positive in \(r\) for \(x\le22\) and changes sign
   from \(x\approx22.5\).

**Decision.** A1–A3 are complete as identities, and no sign has appeared.
By the stop rule, one bounded task remains (A4, §6). Stop with this note
as the identity record unless A4 supplies a new complete signed estimate,
justified positive structure or demonstrated quantitative saving.

## 1. Source, pair and the two Laguerre expressions

Write \(\varphi_n(u)=(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}\),
\(\Phi=\sum_{n\ge1}\varphi_n\), \(\psi(X)=\sum_{n\ge1}e^{-\pi n^2X}\) and
\(f(u)=e^u\psi(e^{4u})\). Then
\[
\Phi=\tfrac18\,(f''-f),
\tag{1.1}
\]
because \((\partial_u^2-1)[e^ue^{-Y}]=8(2Y^2-3Y)e^ue^{-Y}\) with
\(Y=\pi n^2e^{4u}\) (check E2). Let
\(H_t(x)=\tfrac12\int e^{tu^2+ixu}\Phi(u)\,du\). Expanding the products of
derivatives, symmetrizing in \((u_1,u_2)\) and substituting
\(u_{1,2}=s\pm r\) gives, for \(j=0,1\) (check E3),
\[
\mathscr L_j(H_t;x)=\iint r^2(r^2-s^2)^j\,e^{2t(s^2+r^2)}\,
\Phi(s+r)\Phi(s-r)\,e^{2ixs}\,ds\,dr .
\tag{1.2}
\]
The two stationary signs of the program are \(\mathscr L_0\ge0\) on
\(\{H_x=0\}\) and \(\mathscr L_1\ge0\) on \(\{H_{xx}=0\}\).

## 2. Theorem 1: the cusp formula

Set
\[
\mathcal D(\sigma,\rho)=\Bigl(\tfrac{(\sigma+\rho)^2}4-1\Bigr)\Bigl(\tfrac{(\sigma-\rho)^2}4-1\Bigr)
=\Bigl(\tfrac{\sigma^2}4-1\Bigr)^2-\Bigl(\tfrac{\sigma^2}8+\tfrac12\Bigr)\rho^2+\tfrac{\rho^4}{16},
\]
\(\lambda_w(n)=\sum_{ab=n}(a/b)^{w-1/2}\) and
\[
K_w(y)=4\sqrt y\sum_{n\ge1}\lambda_w(n)K_{w-1/2}(2\pi ny).
\]
For \(z=iy\) this is the non-constant part of
\(E^*(z,w)=\xi_c(2w)y^w+\xi_c(2w-1)y^{1-w}+4\sqrt y\sum_n\lambda_w(n)K_{w-1/2}(2\pi ny)\cos2\pi nx\),
with \(\xi_c(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\).

**Theorem 1.** For every \(r\in\mathbb R\) and \(\kappa\in\mathbb C\), with
\(w=\tfrac12+\kappa/4\),
\[
\boxed{\int_{\mathbb R}e^{\kappa s}\,\Phi(s+r)\Phi(s-r)\,ds
=\frac1{512}\,\bigl[\mathcal D(-\kappa,\partial_r)\,K_w(e^{4r})\bigr].}
\tag{2.1}
\]

*Proof (volume–shape swap).* Since \(\Phi\) is even,
\(\Phi(s-r)=\Phi(r-s)\), so the integrand is the pair at volume \(r\) and
shape \(s\). Put \(u_{1,2}=r\pm s\), so that
\(\partial_{u_{1,2}}=\tfrac12(\partial_r\pm\partial_s)\). By (1.1),
\(\Phi(u_1)\Phi(u_2)=\tfrac1{64}(\partial_{u_1}^2-1)(\partial_{u_2}^2-1)[f(u_1)f(u_2)]\)
with \(f(r+s)f(r-s)=e^{2r}\psi(e^{4r+4s})\psi(e^{4r-4s})\). For fixed \(r\),
this product and its derivatives decay superexponentially as
\(|s|\to\infty\): one factor is at most a constant times
\(\exp(-\pi e^{4r+4|s|})\), the other grows at most like \(e^{2|s|}\).
Integration by parts therefore replaces \(\partial_s\) by \(-\kappa\), and the
operator becomes \(\tfrac1{64}\mathcal D(-\kappa,\partial_r)\). With
\(v=4s\) and \(y=e^{4r}\),
\[
\int e^{\kappa s}e^{2r}\psi(e^{4r+4s})\psi(e^{4r-4s})\,ds
=\tfrac14\sqrt y\int e^{(w-1/2)v}\psi(ye^v)\psi(ye^{-v})\,dv
=\tfrac18K_w(y),
\]
where the last step expands
\(\psi(ye^v)\psi(ye^{-v})=\sum_{a,b}\exp\{-2\pi aby\cosh(v+\log\tfrac ab)\}\)
and uses \(\tfrac12\int e^{-X\cosh v+\nu v}dv=K_\nu(X)\). The factor is
\(\tfrac1{64}\cdot\tfrac18=\tfrac1{512}\). Every series and integral
converges absolutely for every complex \(\kappa\). \(\square\)

*Eisenstein reading.* For \(\operatorname{Re}w>1\),
\(\int e^{\kappa s}e^{2s}[\theta(e^{4s+4r})\theta(e^{4s-4r})-1]ds=\tfrac12E^*(ie^{4r},w)\),
the Epstein–Mellin identity. The insertion \(\mathcal D(-\kappa,\partial_r)\)
annihilates \(y^{w}\), \(y^{1-w}\), \(y^{-w}\) and \(y^{w-1}\) (check E1).
These are all four constant-term powers, including those seen through
\(E^*(i/y)=E^*(iy)\). Analytic continuation then gives (2.1) again. Thus
**the physical insertion is the annihilator of the Eisenstein constant
term on this geodesic.** This replaces the renormalized fold of review
§3.1, whose constant-term pieces came from the subtraction.

Two structural readings follow.

- The evenness of \(\Phi\), that is, the functional equation, is the
  **volume–shape swap** of the lift. It exchanges the Mellin-in-volume
  (Eisenstein) description with the Mellin-in-shape (Whittaker)
  description.
- The **fold at the CM point \(i\)** is needed for convergence. The
  integrand of (1.2) is even in \(r\), and the formula uses \(r\ge0\),
  that is \(y\ge1\). On \(r\ge0\) the mode \((a,b)\) is the folded swapped
  pair \(\varphi_a(r+s)\varphi_b(r-s)\). Over all \(r\), mode \((a,b)\)
  would instead be a Gamma-function Laguerre form of size about
  \((ab)^{-1/2}\), and the double series over \((a,b)\) would not converge
  absolutely.

## 3. Theorem 2: Newman time

Write \(e^{2ts^2}=\mathbb E\,e^{Vs}\) with \(V\sim N(0,4t)\). Fubini applies,
because \(\Phi(s+r)\Phi(s-r)\) decays superexponentially in both variables.

**Theorem 2.** For \(t\ge0\) and \(x\in\mathbb R\),
\[
\mathscr L_0(H_t;x)=\frac1{256}\int_0^\infty r^2e^{2tr^2}\,
\mathbb E_V\bigl[\mathcal D(-\kappa,\partial_r)K_{1/2+\kappa/4}(e^{4r})\bigr]_{\kappa=2ix+V}\,dr,
\tag{3.1}
\]
\[
\mathscr L_1(H_t;x)=\frac1{256}\int_0^\infty r^2e^{2tr^2}\,
\mathbb E_V\bigl[(r^2-\partial_\kappa^2)\,\mathcal D(-\kappa,\partial_r)K_{1/2+\kappa/4}(e^{4r})\bigr]_{\kappa=2ix+V}\,dr .
\tag{3.2}
\]

*Proof.* In (1.2) the factor \(s^{2j}\) becomes \(\partial_\kappa^{2j}\)
acting on \(e^{\kappa s}\). The integrand is even in \(r\), so
\(\int_{\mathbb R}dr=2\int_0^\infty dr\). Apply Theorem 1. \(\square\)

*Explicit form.* Let \(y=e^{4r}\), \(C=2\pi aby\cosh v\),
\(L=v+\log(a/b)\) and \(Z\sim N(0,4t)\). Define \(P_0=1\) and
\(P_{k+1}(z)=(2-4z)P_k(z)+4zP_k'(z)\), so that
\(\partial_r^k[\sqrt ye^{-cy}]=P_k(cy)\sqrt ye^{-cy}\). This gives
\(P_2=16z^2-32z+4\) and \(P_4=256z^4-2048z^3+3712z^2-1280z+16\). Gaussian
tilting (check E4) turns (3.1) into
\[
\mathscr L_0(H_t;x)=\frac1{128}\int_0^\infty dr\,r^2e^{2tr^2}e^{2r}
\sum_{a,b\ge1}\int_{\mathbb R}dv\;e^{-C+ixL/2+tL^2/8}\;
\mathbb E_Z\bigl[g(2ix+tL+Z;C)\bigr],
\tag{3.3}
\]
with
\(g(\kappa;C)=(\kappa^2/4-1)^2-(\kappa^2/8+\tfrac12)P_2(C)+P_4(C)/16\).
For \(\mathscr L_1\), replace \(g\) by
\(r^2g-\bigl[(L/4)^2g+(L/2)\partial_\kappa g+\partial_\kappa^2g\bigr]\).
The \(v\)-contour can be moved to \(\operatorname{Im}v=\theta\in(0,\pi/2)\);
this removes the oscillation and makes (3.3) usable at \(x=28\) and
beyond.

Three remarks.

- **Two identical Gaussian weights.** \(e^{2tr^2}=e^{(t/8)(\log y)^2}\)
  on the geodesic and \(e^{(t/8)(v+\log(a/b))^2}\) on the Whittaker
  variable. Both come from \(e^{2t(s^2+r^2)}\), which is symmetric under
  the swap.
- **Hecke eigenvalues are averaged, not preserved.** The spectral
  parameter \(w=\tfrac12+\tfrac{ix}2+\tfrac V4\) is Gaussian with variance
  \(t/4\).
- **The modular symmetry is exact on the integrand.** \(K_w\) is the cusp
  part of an \(\mathrm{SL}_2(\mathbb Z)\)-invariant eigenfunction for every
  \(w\). The Newman deformation acts only through the test function and the
  average over \(w\).

| \((t,x)\) | \(\mathscr L_0\) direct | \(\mathscr L_0\) by (3.3) | \(\mathscr L_1\) direct | \(\mathscr L_1\) by (3.2) | max rel. error |
| --- | --- | --- | --- | --- | --- |
| \((0,8)\) | \(2.29026684583\cdot10^{-5}\) | same | \(4.45809535321\cdot10^{-7}\) | same | \(2.7\cdot10^{-15}\) |
| \((0.05,8)\) | \(2.29397238278\cdot10^{-5}\) | same | \(4.4716011778\cdot10^{-7}\) | same | \(6.2\cdot10^{-15}\) |
| \((0.05,28.27)\) | \(7.44131936397\cdot10^{-9}\) | same | \(1.00349504841\cdot10^{-9}\) | same | \(5.8\cdot10^{-15}\) |

The fixed-\(r\) identity (2.1) agrees to \(1.6\cdot10^{-14}\) at five
points, including complex \(\kappa\) (record N1). A separate verification
pass (a Claude Opus 5.5 subagent writing its own mpmath code at 20–30
digits; scripts not retained) confirmed (1.2), Theorems 1–3 and
Proposition 4 to \(3\cdot10^{-25}\) or better
([verification pass](../reviews/1_VERIFICATION_PASS_CLAUDE_20261013.md)).

**Whittaker modes (diagnostic).** Group the terms of (3.3) by \(n=ab\).
Shares of \(\mathscr L_0\) at \(t=0\) (records N3, N3b):

| \(x\) | 4 | 8 | 12 | 20 | 28.27 | 42 | 46 | 54 | 80 | 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mode 1 | 0.999 | 1.006 | 1.004 | 0.984 | 1.072 | 1.130 | 1.369 | 0.723 | 1.287 | 1.849 |
| mode 2 | 0.001 | \(-0.006\) | \(-0.004\) | 0.016 | \(-0.071\) | \(-0.121\) | \(-0.414\) | 0.281 | \(-0.608\) | \(-1.154\) |
| mode 3 | \(<10^{-5}\) | \(<10^{-5}\) | \(<10^{-4}\) | \(<10^{-5}\) | \(-0.001\) | \(-0.009\) | 0.043 | \(-0.010\) | 0.246 | \(-0.022\) |

The values at \(t=0.05\) agree with these to three digits (for
\(x\le42\)). Below \(x\approx42\) the first mode carries
\(\mathscr L_0\). From about \(x\approx46\) several modes are comparable
and the shares oscillate, like the main sum of the Riemann–Siegel formula. (The share table of review §3.1 used the
renormalized fold and is superseded here.)

**Sign of the kernel (diagnostic).** At \(t=0\) the folded kernel
\(\int e^{2ixs}\Phi(s+r)\Phi(s-r)\,ds\) is positive for every grid point
\(r\in\{0,0.05,\dots,0.6\}\) when \(x\in\{8,16,22\}\). It is negative near
\(r=0\) for \(x=22.5\) and \(x=28.27\) (record N3c). Pointwise positivity
therefore ends below the first zero, \(x=28.27\).

## 4. Theorem 3: the two-coset identity is the Hecke correspondence at 2

Let \(\beta=\tfrac14\log2\). Since
\(\varphi_{2m}(u)=2^{-1/2}\varphi_m(u+\tfrac12\log2)\),
\[
\Phi_e:=\sum_{n\text{ even}}\varphi_n=2^{-1/2}\Phi(\cdot+2\beta),\qquad
\Phi_o:=\sum_{n\text{ odd}}\varphi_n=\Phi-\Phi_e .
\]

**Theorem 3.** For all real \(u_1,u_2\),
\[
\begin{aligned}
&\Phi(u_1+\beta)\Phi(u_2-\beta)+\Phi(u_1-\beta)\Phi(u_2+\beta)
+\sqrt2\bigl[\Phi_e(u_1-\beta)\Phi_e(u_2-\beta)+\Phi_o(u_1-\beta)\Phi_o(u_2-\beta)\bigr]\\
&\qquad=\sqrt2\bigl[\Phi(u_1-\beta)\Phi(u_2-\beta)+\Phi(u_1+\beta)\Phi(u_2+\beta)\bigr].
\end{aligned}
\tag{4.1}
\]
Consequently, for \(t\ge0\) and \(x\in\mathbb R\),
\[
\mathcal U_t(x)+\mathcal T_t(x)
=\sqrt2\,e^{2t\beta^2}\bigl[e^{2i\beta x}\mathscr L_0(H_t;x-2it\beta)
+e^{-2i\beta x}\mathscr L_0(H_t;x+2it\beta)\bigr],
\tag{4.2}
\]
where \(\mathcal U\) (unequal-scale channel) is the weight-\(r^2\) pair
transform of the first two terms on the left of (4.1), and \(\mathcal T\)
(two-coset, or twisted, channel) is that of
\(\sqrt2[\Phi_e\Phi_e+\Phi_o\Phi_o]\), the remaining term.

*Proof.* Substituting \(\Phi_e(u-\beta)=2^{-1/2}\Phi(u+\beta)\) makes
(4.1) a polynomial identity over \(\mathbb Q(\sqrt2)\) in four symbols
(check E6). For (4.2), integrate (4.1) against
\(\tfrac18(u_1-u_2)^2e^{t(u_1^2+u_2^2)+ix(u_1+u_2)}\) and translate the
volume variable; the translation becomes the complex shift
\(x\mp2it\beta\) by the dilation lemma (review §1.4). \(\square\)

*Lattice meaning.* With \(\Theta(V,y)=\theta(Vy)\theta(V/y)\), (4.1) is
the index-two sublattice count
\(\Theta(2V,2y)+\Theta(2V,y/2)+\theta_{\Lambda_3}(2V,y)=\Theta(V,y)+2\Theta(4V,y)\):
every nonzero vector of \(\mathbb Z^2\) lies in exactly one of the three
index-two sublattices unless it lies in \(2\mathbb Z^2\), when it lies in all
three (check E5). Here \(\Lambda_3=\{n\equiv m \bmod 2\}\) is card 09's
even–even parity coset. For the lattice of shape \(iy\) it has shape
\((1+iy)/2\). After the Mellin transform in volume, the identity reads
\[
E^*(2iy,w)+E^*(iy/2,w)+E^*(\tfrac12+\tfrac{iy}2,w)=\sqrt2\,\lambda_w(2)\,E^*(iy,w),
\]
relating the geodesics \(\operatorname{Re}z=0\) and
\(\operatorname{Re}z=\tfrac12\). The cusp parts agree to
\(4.4\cdot10^{-15}\) (record N4). The constant terms satisfy
\((2y)^w+2(y/2)^w=\sqrt2\lambda_w(2)y^w\). The coefficient identity behind
the cusp parts is \(\lambda(2)\lambda(m)=\lambda(2m)+\lambda(m/2)\), checked
exactly for \(m\le128\) (check E7).

*Status.* The identity is exact and linear in the pair source. As an
algebraic statement, (4.1) holds for any function once \(\Phi_e\) is
*defined* as \(2^{-1/2}\Phi(\cdot+2\beta)\). Its content is that this
function is the even-index sub-sum, so that the twisted channel is the
theta series of a sublattice. That is the Euler factor at 2:
\((1-2^{-s})\zeta(s)=\sum_{n\text{ odd}}n^{-s}\). It holds at
every Newman time because (4.1) is a pointwise identity of sources;
integrating it against the translated Gaussian weight produces the complex
shifts in (4.2). It supplies no sign. At \((t,x)=(0,8)\) the two channels are
\(\mathcal U=2.650\cdot10^{-4}\) and \(\mathcal T=-3.255\cdot10^{-4}\),
against \(\mathscr L_0(H_0;8)=2.29\cdot10^{-5}\) (record N5): large
cancelling pieces with no evident order.

## 5. Proposition 4: the control test

The controls of [direction 19](../../19_euler_factor_controls/README.md)
are \(\Phi_{c,p}=\Phi+\tfrac c2(\Phi(\cdot+a)+\Phi(\cdot-a))\),
\(a=\tfrac12\log p\), \(0<c<1\). Their pair source is
\(\sum_{j,k\in\{0,\pm1\}}c_jc_k\,\Pi(s+\alpha_{jk},r+\beta_{jk})\), with
\(\Pi(s,r)=\Phi(s+r)\Phi(s-r)\), \(c_0=1\), \(c_{\pm1}=c/2\),
\(\alpha_{jk}=(j+k)a/2\) and \(\beta_{jk}=(j-k)a/2\).

**Proposition 4.**

(a) With \(\mathcal K_\kappa(r)=\tfrac1{512}\mathcal D(-\kappa,\partial_r)K_{1/2+\kappa/4}(e^{4r})\),
\[
\mathscr L_0(H^{c,p}_t;x)=\sum_{j,k}c_jc_k\;\mathbb E_V\Bigl[e^{-\kappa\alpha_{jk}}
\int_{\mathbb R}(r-\beta_{jk})^2e^{2t(r-\beta_{jk})^2}\mathcal K_\kappa(r)\,dr\Bigr]_{\kappa=2ix+V}.
\]
Every control has the same cusp kernel as theta. Its test functions are
Gaussian weights translated along the geodesic to the Hecke points
\(ip^{\pm1}\) and \(ip^{\pm2}\), with volume phases.

(b) For a prime \(q\ne p\), \(\Phi_{c,p}\) satisfies the \(q\)-adic
self-similarity
\(\Phi_{c,p}-q^{-1/2}\Phi_{c,p}(\cdot+\tfrac12\log q)=\) (its part with
\(q\nmid n\)), and hence the \(q\)-analogue of (4.1). For \(q=p\) it fails.

(c) Every \(\Phi_{c,p}\) with \(0<c<1\) has \(\Lambda_{c,p}>0\). Consider
an argument whose arithmetic input is the Hecke relations at a finite set
\(P\) of primes, together with positivity, evenness, the Gaussian
structure and the same real zeros as theta at \(t=0\). Its hypotheses are
satisfied by \(\Phi_{c,p}\) for every \(p\notin P\), so it cannot prove
\(\Lambda\le0\).

*Proof.* (a) is the substitution of §3 applied to each translate; record
N7 reproduces direct control values to \(4\cdot10^{-12}\) or better at
\((p,c,t,x)=(3,\tfrac12,0.05,5)\), \((2,\tfrac12,0,9)\) and
\((5,0.7,0.1,3)\). At the second point \(\mathscr L_0<0\), as expected
next to an off-line zero. For (b),
\(\Phi_{c,p}=\sum_n\tfrac c2p^{-1/2}a_n\,(n/p)^{-1/2}\varphi_1(u+\tfrac12\log(n/p))\)
with \(a_n=1+(2\sqrt p/c)\mathbf 1_{p\mid n}+p\,\mathbf 1_{p^2\mid n}\), and
\(a_{qm}=a_m\) for all \(m\) exactly when \(q\ne p\) (check E8; numerical
replay N6, defect below \(10^{-15}\) for \(q\ne p\) and of order one for
\(q=p\)). For (c), \(\Phi_{c,p}\) has non-real zeros at \(t=0\) (review
§1.3), and it has the listed properties. \(\square\)

For intermediate targets the screen is quantitative. With \(c=\tfrac12\),
19 numerically tracks lowest-pair collision times \(T_0>0.2\) for primes
\(p\le41\), including \(T_0(1/2,41)\approx0.20011667246\). These are
numerical branch times, not certified values of the global constant
\(\Lambda_{c,p}\). A rigorously established branch gives
\(T_0\le\Lambda_{c,p}\); equality requires all other zeros to be real
by that time. A fixed outward negative Laguerre witness at \(t=0.2\)
would establish the desired lower bound directly, without global equality.

Any proposed genuine-theta bound must use an input that its relevant
countercontrols lack, such as a local factor or a quantitative genuine
low-height evaluation. No claim that all-prime relations are the only
possible useful input is made. Certification must resolve the raw witness
margin, which shrinks near an isolated pair collision even though the
normalized ratio grows. See the [corrected 19 note](../../19_euler_factor_controls/notes/1_EXACT_FLOW_WITNESSES_AND_ASYMPTOTICS_20261013.md).

## 6. What remains: A4

The stationary targets are now
\[
\text{(S0)}\ \ (3.1)\ge0\ \text{on}\ \{H_x=0\},\qquad
\text{(S1)}\ \ (3.2)\ge0\ \text{on}\ \{H_{xx}=0\}.
\]
This is the precise integral-kernel inequality that card 09 asked for. No
positive-definite structure is known for it.

- The kernel is real on the physical line, but it changes sign in \(r\)
  from \(x\approx22.5\) (§3).
- The Hecke relations are linear, and each is shared by controls at other
  primes (§5).
- The mode expansion is dominated by mode 1 only at low height (§3).

**A4 (final bounded task).**
(i) Decide the sign of the folded first mode,
\(2\int_0^\infty r^2\int e^{2ixs}\varphi_1(r+s)\varphi_1(r-s)\,ds\,dr\), for
all \(x\). It is positive at every height tested, but the fold prevents a
Gamma-function closed form.
(ii) Bound the higher modes at stationary points on a height range, and
compare the result with the main-sum and remainder structure of 01.
(iii) The review's calibration against Young's theorem concerns
\(|E^*|^2\) along this geodesic, not these signed moments; I now rank it
lowest.

A4 must specify its time-height domain and comparator, retain the complete
stationary constraints and both Laguerre obligations, and pay every omitted
mode and tail. A first-mode result alone does not give a complete sign.
Stop if (i)–(ii) give only the known main-term and remainder structure,
without a new complete estimate, justified positive structure or measured
saving. W1 stays deferred.

## 7. Checks

Run, from `numerics/`:

```sh
python3 -I check_rank_two_lift_claude_20261013.py --output RANK_TWO_LIFT_RECORD_20261013.json
```

Standard library only; about 45 seconds.

- **Part E, exact.**
  - E1: \(\mathcal D\) annihilates the four constant-term powers, and its
    expanded form.
  - E2: the insertion generates \(\varphi_n\).
  - E3: pair weights \(r^2\) and \(r^2(r^2-s^2)\).
  - E4: Gaussian tilting moments to order 8.
  - E5: index-two sublattice count and the rectangular coset identity.
  - E6: (4.1) over \(\mathbb Q(\sqrt2)\).
  - E7: Hecke multiplicativity at 2 as ratio multisets, \(m\le128\).
  - E8: the 2- and \(q\)-adic coefficient test for the controls.
- **Part N, double precision.**
  - N1: (2.1) at five points.
  - N2: Theorem 2 for \(\mathscr L_0\) and \(\mathscr L_1\).
  - N3/N3b: mode shares.
  - N3c: kernel sign.
  - N4: Hecke at 2 on two geodesics.
  - N5: (4.2) at three \((t,x)\).
  - N6: the control test.
  - N7: Proposition 4(a) against direct control values.
