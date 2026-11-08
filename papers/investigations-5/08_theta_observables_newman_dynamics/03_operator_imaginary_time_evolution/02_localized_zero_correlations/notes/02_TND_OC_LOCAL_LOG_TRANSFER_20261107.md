# An explicit time-zero source-to-logarithm-to-zero comparison

7 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**,
branch chat0001.

**Status: proved in-note from the named classical and inherited inputs;
separate internal [E02 assessment](../reviews/02_TND_OC_E02_CLAIM_LEVEL_ASSESSMENT_20261107.md) accepted the mathematical statements without changing their constants.**
This executes [E01 r1](../research-progress/handoffs/01_TND_OC_E01_REQUEST_20261107.md).
The result is a quantitative approximation theorem, not a signed
upper bound or an RH exclusion. There is no numerical implementation,
certificate, new manuscript, or literature novelty claim.

The gain over an unpaid logarithmic substitution is explicit: normalized
uniform field accuracy controls a compact zero statistic through
multiple zeros, with exponent \(2/(n_X+2)\), \(n_X=O(\log X)\).
There is no assumption that H is bounded away from zero throughout
the observation region. A safe anchor and a larger-disk upper bound
remain essential.

## 1. A local analytic lemma with all constants

Set
\[
 R=\frac92,\quad \rho=\frac{13}3,\quad r=\frac{25}6,\quad
 B=R+r=\frac{26}3,\quad \frac{\rho+r}{\rho-r}=51.
 \tag{1}
\]
Let f,g be holomorphic on a neighborhood of \(\overline D(0,R)\), with
\[
 |f|,|g|\le1,\quad |f(0)|,|g(0)|\ge m,\quad 0<m\le1,\quad
 \|f-g\|_\infty\le\epsilon\le1.
 \tag{2}
\]
Put
\[
 A=\log(1/m),\quad
 n=\max\left(1,\left\lceil\frac A{\log(27/26)}\right\rceil\right),
 \quad \alpha=\frac2{n+2},
\]
\[
 C_n=\pi r^2+\pi B^2n^2e^{102A/n}2^{2/n}.
 \tag{3}
\]
Then
\[
 \boxed{\int_{D_r}|\log|f|-\log|g||\,dA\le C_n\epsilon^\alpha.}
 \tag{4}
\]
All logarithms are log moduli, with their locally integrable values at
zeros. For \(\epsilon=0\) the claim is immediate.

### Proof: finite factor removal

Consider f. Jensen's formula, including multiplicities, bounds its
number k of zeros in \(D_\rho\) by
\[
 k\log(R/\rho)\le-\log|f(0)|\le A.
 \tag{5}
\]
Boundary zeros on \(|z|=R\) have zero Jensen weight; an interior-radius
limit gives the same inequality. This is the standard formula and
Blaschke construction in
[Tao, Theorem2 and its proof](https://terrytao.wordpress.com/2020/12/23/246b-notes-1-zeroes-poles-and-factorisation-of-meromorphic-functions/).

Write these k zeros as \(a_l\) and remove precisely them:
\[
 b_l(z)=\frac{R(z-a_l)}{R^2-\overline{a_l}z},\qquad
 h(z)=f(z)\big/\prod_{l=1}^k b_l(z).
 \tag{6}
\]
There is no zero at the center. The apparent singularities are
removable, each \(b_l\) has modulus one on \(|z|=R\), and the maximum
principle gives \(|h|\le1\) on \(D_R\). The function h is nonvanishing
on \(D_\rho\), and \(|h(0)|\ge|f(0)|\ge m\).
Thus \(-\log|h|\) is nonnegative harmonic there. The disk Harnack
inequality gives \(-\log|h(z)|\le51A\) on \(D_r\).
If h has a zero on the circle of radius \(\rho\), apply Harnack on
smaller circles and pass to the limit. The disk inequality is
[Tao, Exercise69](https://terrytao.wordpress.com/2016/10/18/246a-notes-5-conformal-mapping/);
its factor is exactly the ratio in (1).

For \(|z|\le r\),
\[
 |b_l(z)|\ge\frac{|z-a_l|}{R+r}=\frac{|z-a_l|}{B},\qquad
 |f(z)|\ge e^{-51A}\prod_{l=1}^k\frac{|z-a_l|}{B}.
 \tag{7}
\]
Each distance ratio is at most one, since \(r+\rho<B\).
If \(q=e^{51A}t<1\) and \(|f(z)|<t\), some distance is less than
\(Bq^{1/k}\). For k=0 this sublevel set is empty. For \(1\le k\le n\),
the union of these k disks has area at most
\(k\pi B^2q^{2/k}\le n\pi B^2q^{2/n}\).
If q>=1, the same bound dominates \(\pi r^2\) and is automatic.
Consequently, for every \(t>0\),
\[
 |\{z\in D_r:|f(z)|<t\}|
 \le n\pi B^2e^{102A/n}t^{2/n}.
 \tag{8}
\]
Layer-cake integration gives
\[
 \int_{\{|f|<t\}\cap D_r}\log\frac t{|f|}\,dA
 \le\frac{\pi B^2n^2}{2}e^{102A/n}t^{2/n}.
 \tag{9}
\]
The same statements hold for g with the same parameters.

### Proof: comparison across small values

For \(0<\epsilon\le1\), choose \(\tau=\epsilon^{n/(n+2)}\), so
\(\epsilon\le\tau\). Where both moduli are at least \(\tau\),
the real logarithm is \(1/\tau\)-Lipschitz, giving an integral
at most \(\pi r^2\epsilon/\tau\).
On the complement, the smaller modulus is below \(\tau\) and the larger
is below \(2\tau\). The log difference is bounded by
\(\log(2\tau/|f|)+\log(2\tau/|g|)\).
Apply (9) twice. Both powers become
\(\epsilon^{2/(n+2)}\), proving (4).
This proof supplies the sublevel payment instead of assuming a
pointwise lower modulus near zeros.

## 2. A canonical anchor and disk at Newman time zero

Fix \(X\ge10\) and
\[
 s(z)=\frac12-\frac{iz}{2},\quad c=X+4i,\quad
 F(z)=\frac{s(z)-1}{s(z)}\zeta(s(z)).
 \tag{10}
\]
The canonical normalization \(H_0(z)=\xi(s(z))/8\), using xi reflection,
gives
\[
 F(z)=D(z)H_0(z),\qquad
 D(z)=\frac{16\pi^{s(z)/2}}{s(z)^2\Gamma(s(z)/2)}.
 \tag{11}
\]
D is holomorphic and zero-free on a neighborhood of
\(\overline D(c,R)\): throughout the disk
\[
 \frac14\le\Re s\le\frac{19}4,\qquad
 |\Re z|\le X+\frac92.
 \tag{12}
\]
The point \(s=0\) and gamma's nonpositive-integer poles are outside;
the apparent pole of zeta at s=1 is cancelled in F. No multiplier
zero or pole is introduced in this disk.

For \(\Re s=\sigma>0\), the fractional-part continuation, inherited
from [parent Note28 §2](../../notes/28_TND_O_E20_PAID_QUADRATIC_GREEN_COMPARISON_20261107.md),
is
\[
 \frac{s-1}{s}\zeta(s)
 =1-(s-1)\int_1^\infty\{v\}v^{-s-1}\,dv.
 \tag{13}
\]
Partial summation proves it initially at \(\sigma>1\), and the integral
continues it to \(\sigma>0\). It follows that
\[
 |F(z)|\le1+\frac{|s-1|}{\sigma}\le2X+25=M_X-1,\quad
 M_X=2X+26.
 \tag{14}
\]
Indeed \(|s-1|\le15/4+(X+9/2)/2=X/2+6\) on the disk.
This recalculates the upper bound for its small extension below y=0.

At c, \(\Re s=5/2\). The absolutely convergent Euler product and
\(|(s-1)/s|\ge3/5\) give
\[
 |F(c)|\ge c_0:=\frac35\frac{\zeta(5)}{\zeta(5/2)}>0.
 \tag{15}
\]
The product lower bound is
\(\prod_p(1+p^{-5/2})^{-1}=\zeta(5)/\zeta(5/2)\).
This is a safe-line bound, not an RH premise. It is the Q-free version
of the same calculation in parent Note28.

Let \(\widehat F\) be holomorphic on a neighborhood of this disk and
\[
 \sup_{\overline D(c,R)}|F-\widehat F|\le\delta,\qquad
 0<\delta\le\min(1,c_0/2).
 \tag{16}
\]
Both \(f=F/M_X\) and \(g=\widehat F/M_X\), translated to c, satisfy
(2) with
\[
 m_X=\frac{c_0}{2M_X},\quad A_X=\log(2M_X/c_0),\quad
 n_X=\max(1,\lceil A_X/\log(27/26)\rceil),\quad
 \epsilon=\delta/M_X.
 \tag{17}
\]
Use (3) to define \(C_X,\alpha_X\). Then
\[
 \int_{D(c,r)}|\log|F|-\log|\widehat F||\,dA
 \le C_X(\delta/M_X)^{\alpha_X}.
 \tag{18}
\]
In particular \(n_X=O(\log X)\), \(C_X=O((\log X)^2)\), and
\(\alpha_X=2/(n_X+2)\) is of order \(1/\log X\). The constants in
these asymptotic descriptions are unnecessary for use: (3),(17)
are explicit. The exponent deteriorates with height; no fixed positive
Hölder exponent uniform in unbounded X is claimed.

## 3. Two nonholomorphic zero observables

Fix \(0<h\le1\), \(0\le w\le1\), \(w\in C_c^\infty(\mathbb R)\)
supported in [-1,1] and equal to one on [-1/2,1/2]. Choose a smooth
nonnegative cutoff \(\kappa\), equal to one on [0,1], at most one and
zero for \(y\ge2\). Put
\[
 a(x,y)=w((x-X)/h)y_+^2\kappa(y),\quad
 \varphi_Q=2a,\qquad
 \varphi_\eta=2\log(1+\eta a),\quad \eta\ge0.
 \tag{19}
\]
Their support lies in \(|x-X|\le1,\ 0\le y\le2\), whose distance
from c is at most \(\sqrt{17}<r\). Both tests are compactly supported
and \(C^{1,1}\); they have bounded weak Laplacians. There is no boundary
delta at y=0, because both their value and first y derivative vanish
there.

For a nonzero holomorphic V on this disk write
\[
 \nu_V(\varphi)=\sum_{V(z)=0}m_z\varphi(z)
 =\frac1{2\pi}\int\log|V(z)|\Delta\varphi(z)\,dA.
 \tag{20}
\]
For smooth tests this is the smoothed Jensen identity, also checked in
[Tao, Exercise7](https://terrytao.wordpress.com/2020/12/23/246b-notes-1-zeroes-poles-and-factorisation-of-meromorphic-functions/).
For (19), mollify inside the fixed support buffer. Tests converge
uniformly; their Laplacians are uniformly bounded and converge almost
everywhere, so local logarithmic integrability and dominated convergence
prove (20). This includes real multiple zeros, whose test value is zero.

Canonical conjugation and \(|y_j|\le1\) imply exactly
\[
 Q_{X,h}=\sum_jw_jy_j^2=\nu_F(\varphi_Q),\qquad
 \log Z_{X,h}(\eta)=\sum_j\log(1+\eta w_jy_j^2)
                  =\nu_F(\varphi_\eta).
 \tag{21}
\]
The factor two counts the lower conjugate copies via the upper half-plane.
The harmonic log of D contributes zero in (20).

Define the comparison values
\(\widehat Q=\nu_{\widehat F}(\varphi_Q)\) and
\(\widehat L_\eta=\nu_{\widehat F}(\varphi_\eta)\). Both are nonnegative.
The approximating function is **not** assumed to have all its zeros in
the canonical strip. Zeros between y=1 and y=2 retain their actual
cutoff weights; no artificial strip theorem is used.
Equations(18),(20) give the complete comparison
\[
 \boxed{
 |Q_{X,h}-\widehat Q|\le E_Q,\quad
 |\log Z_{X,h}(\eta)-\widehat L_\eta|\le E_\eta,\quad
 E_\varphi=\frac{\|\Delta\varphi\|_\infty}{2\pi}
 C_X(\delta/M_X)^{\alpha_X}.}
 \tag{22}
\]

All test constants can be read from fixed derivatives. If
\(v(y)=y_+^2\kappa(y)\), then almost everywhere
\[
 \Delta a=h^{-2}w''((x-X)/h)v+w((x-X)/h)v'',
 \quad
 |\nabla a|^2=h^{-2}|w'|^2v^2+w^2|v'|^2.
 \tag{23}
\]
For example
\[
 \frac{\|\Delta\varphi_Q\|_\infty}{2\pi}
 \le\frac{h^{-2}\|w''\|_\infty\|v\|_\infty+
                \|w\|_\infty\|v''\|_\infty}{\pi},
 \tag{24}
\]
\[
 \Delta\varphi_\eta
 =2\left(\frac{\eta\Delta a}{1+\eta a}
       -\frac{\eta^2|\nabla a|^2}{(1+\eta a)^2}\right).
 \tag{25}
\]
The denominators in (25) are at least one. This pays any selected
finite \(\eta\); growing \(\eta\) must retain these derivative costs.

## 4. Complete canonical source and a finite approximation

Use exactly the parent [source formula and majorant](../../manuscript/sections/02_source.tex),
on \(u\ge0\):
\[
 r_u=\pi e^{4u},\quad
 \Phi(u)=e^u\sum_{l\ge1}(2l^4r_u^2-3l^2r_u)e^{-l^2r_u},
 \qquad H_0(z)=\int_0^\infty\Phi(u)\cos(zu)\,du.
 \tag{26}
\]
For integer \(J\ge1\) and \(U>0\), truncate the displayed arithmetic
sum at J, call it \(\Phi_J\), and put
\[
 \widehat H_{J,U}(z)=\int_0^U\Phi_J(u)\cos(zu)\,du,\qquad
 \widehat F=D\widehat H_{J,U}.
 \tag{27}
\]
These are exact analytic functions defined by finite sums and compact
integrals; no quadrature or rounded samples have yet been substituted.

Write
\[
 C_2(J)=\sum_{l>J}l^4e^{-\pi(l^2-1)},\quad B_0=5C_2(0),
 \quad b=\frac{17}2,
\]
\[
 I_b=\int_0^\infty e^{(b+1)u}r_u^2e^{-r_u}\,du,\qquad
 I_b^{>U}=\int_U^\infty e^{(b+1)u}r_u^2e^{-r_u}\,du.
 \tag{28}
\]
Every point of the disk has \(|\Im z|\le b\). Splitting the omitted
arithmetic terms on [0,U] from the **complete** radial tail gives
\[
 \sup_{|\Im z|\le b}|H_0-\widehat H_{J,U}|
 \le \delta_H(J,U):=5C_2(J)I_b+B_0I_b^{>U}.
 \tag{29}
\]
There is no half-line factor of two: (26) is the cosine integral.
The finite prefix is not asserted to have complete source reflection
at the endpoint, and no derivative across a reflected prefix is used.

The tails are explicit. A ratio bound on consecutive terms gives
\[
 C_2(J)\le
 \frac{(J+1)^4e^{-\pi((J+1)^2-1)}}
 {1-16e^{-\pi(2J+3)}}\quad(J\ge0).
 \tag{30}
\]
The denominator is positive even at J=0. Substitution \(v=\pi e^{4u}\)
gives, with the upper incomplete gamma integral,
\[
 I_b^{>U}=\frac{\pi^{-19/8}}4
             \Gamma(35/8,\pi e^{4U}),\qquad
 I_b=\frac{\pi^{-19/8}}4\Gamma(35/8,\pi).
 \tag{31}
\]
Thus both independent tails tend to zero.

For an explicit bound on D throughout the **whole enlarged disk**, set
\[
 V_X=X+\frac92,\qquad
 \mathcal B_X=
 32\pi^{19/8}\exp\left(\frac{19}8+
              \frac{\pi^2(361+4V_X^2)}{768}\right).
 \tag{32}
\]
Then \(|D|\le\mathcal B_X\).
Indeed the [reciprocal-gamma product](https://dlmf.nist.gov/5.8#E2)
and \(\log|1+q|\le\Re q+|q|^2/2\) give
\[
 |\Gamma(w)^{-1}|\le |w|e^{\gamma\Re w+\pi^2|w|^2/12}.
 \tag{33}
\]
Apply this with \(w=s/2\), \(\gamma\le1\), \(|s|\ge1/4\),
\(\Re s\le19/4\) and
\(|s|^2\le361/16+V_X^2/4\). The prefactor becomes
\(8/|s|\le32\), proving (32).
This follows the method of parent Note28 but pays the new domain.
It is deliberately expensive in X; no practical-cost claim is made.

Consequently a valid input for (16),(22) is
\[
 \delta=\mathcal B_X\,[5C_2(J)I_b+B_0I_b^{>U}],
 \quad\text{provided }\delta\le\min(1,c_0/2).
 \tag{34}
\]
The canonical complete field is the object being approximated.
No zero outside the compact test is dropped from a purported global
observable: (21) itself is compact in x, and the true strip and
conjugation account for all its transverse copies.

## 5. Arbitrary height, small defects and the consuming inequality

For a nonzero test \(\varphi\) in (19), define
\(K_\varphi=\|\Delta\varphi\|_\infty/(2\pi)>0\).
Given any desired observable accuracy \(e>0\), choose
\[
 \delta_*=\min\left\{1,\frac{c_0}2,\;
 M_X\left(\frac{e}{2K_\varphi C_X}\right)^{(n_X+2)/2}\right\}.
 \tag{35}
\]
Choose finite J,U so that
\[
 5C_2(J)I_b\le\frac{\delta_*}{2\mathcal B_X},\qquad
 B_0I_b^{>U}\le\frac{\delta_*}{2\mathcal B_X}.
 \tag{36}
\]
Equations(30),(31) prove that these choices terminate; they may use
the explicit upper bound for \(B_0\) from (30). Then (22) has
\(E_\varphi\le e/2\). For \(\eta=0\), \(\varphi_\eta=0\) and its
comparison is exact without this prescription.

This is one quantified family for **every** real \(X\ge10\) and
\(0<h\le1\), with no exceptional centers in the error estimate.
It also works along any prescribed sequence with \(X\to\infty\),
\(h\downarrow0\), \(d\downarrow0\), or finite response strengths varying,
by retaining their explicit costs before choosing cutoffs. It is not a
uniform runtime result or a single fixed finite source valid at all
heights with vanishing error.

For a simple conjugate pair in the window plateau with \(|y|\ge d>0\),
\[
 Q_{X,h}\ge2d^2,\qquad
 \log Z_{X,h}(\eta)\ge2\log(1+\eta d^2)\quad(\eta>0).
 \tag{37}
\]
Therefore the genuine consuming inequalities are
\[
 \widehat Q+E_Q<2d^2,\qquad\text{or}\qquad
 \widehat L_\eta+E_\eta<2\log(1+\eta d^2).
 \tag{38}
\]
The error terms in these inequalities have now been paid.
**No bound placing \(\widehat Q\) or \(\widehat L_\eta\) below the
remaining margin is proved.** Accurate acquisition is distinct from
smallness. A fixed positive e cannot resolve every \(d>0\); (35),(36)
explicitly adapt to a declared d. All-window exact vanishing is the
RH reformulation identified once in Note01, not a new criterion.

The logarithmic integral for \(\widehat Q\) can have singularities at
approximate zeros; it is an exact integrable quantity in (20), not
permission to apply a smooth quadrature without further analysis.
A future numerical evaluator must pay its uniform field error on the
whole disk and its final observable integration error separately.

## 6. Limits and validation scope

The normalization requirement cannot be discarded. For fixed d>0,
\(c[(z-x_0)^2+d^2]\) and \(c[(z-x_0)^2-d^2]\) approach one another
uniformly on every fixed disk as \(c\to0\), but one retains the
nonreal pair and the other has real roots. Their unscaled safe anchors
also go to zero. This is an analytic information control, not a theta
perturbation and not a counterexample to (22).

For the collision-control families screened in
[Note01 §5](01_TND_OC_REFLECTION_AND_CONFIGURATION_REDUCTION_20261107.md),
the generic lemma remains valid whenever its actual bounds hold.
It is compatible with their nonreal zeros. Their absent canonical
identity prevents automatic reuse of (10)–(17),(26)–(34) with the same
constants; even if an individual control satisfies suitable analogues,
the comparison provides no small signed value. In particular the
finite-source approximation can itself have nonreal zeros, as the
repository's finite-source controls warn. Only the tested compact
observable and its paid error are transferred.

Time is fixed at \(\lambda=0\). The HDA negative-time theorem has not
been continued through zero; no Euler product is assigned to
\(\lambda>0\). The parent finite-Euler residual obstruction is neither
contradicted nor imported as an obstruction to this logarithm estimate.
The existing Green method remains a separate consumer requiring its
own signed upper comparison.

This is an approximation milestone under
[avoid01](../../../../../../avoid/01_restating_the_target.md), with the
number \(\alpha_X=2/(n_X+2)\) and constants stated above.
Keep the [result index](../../../../../../result-summaries/README.md),
[avoid index](../../../../../../avoid/README.md),
[collision screen](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [scope rule](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
The [source receipt](../references/01_TND_OC_OPENING_SOURCE_USE_20261107.md)
and [author self-check](../reviews/01_TND_OC_OPENING_AUTHOR_SELF_CHECK_20261107.md)
record actual inspection and assessment limits.

**E02 status amendment, 7 November 2026:** this is a separate-session internal
LLM assessment, with three read-only scope checks and one root writer.
Exact backend model/effort are not exposed; no cross-model or specialist
validation is claimed. The equations and proof are unchanged.
