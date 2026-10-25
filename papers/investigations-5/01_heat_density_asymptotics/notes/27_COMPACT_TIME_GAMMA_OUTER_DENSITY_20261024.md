# Compact positive-time outer density from the complete gamma convolution

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from this conversation's session metadata. Chat 0006.

**Status: proved in-note; same-assistant review only.** This advances
HDA-19 beyond [Note 25][n25]. For every compact interval
`I=[t_a,t_b]` strictly above 64, it gives a two-factor holomorphic outer
approximation, source-derived simple-zero collars, and an absolute
approximation to the **unchanged, unnormalized, adaptively regulated**
spatially averaged density on all sufficiently large heights. The formula
retaining phase has error `O_I(log^2|x|/|x|)`; its continuum simplification
has the additional `O((log|x|)^-4)` kernel-phase error.

The constants and onset are uniform on each stated compact interval but
are not numerically instantiated. This is not a joint large-time/height
result, an inner/outer overlap, or a current/potential/covariance evolution
theorem. HDA-19 remains **Partial**, and HDA-18 remains gated. No numerical
execution, interval certificate, new RH criterion or novelty claim is made.
[Review 10][review] records the same-assistant audit.

## 1. Contract and classification

Keep the canonical complete source and its normalization:

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad H_t=-H_{zz},\quad H(0,z)=\xi((1+iz)/2)/8.
\tag{GO1}
\]

Fix `I=[t_a,t_b]` with `64<t_a<=t_b<infinity`, fixed positive widths
`ell,h`, and a finite observation strip `|y|<=Y`. Use the kernel

\[
k(v)=\frac{315}{256}(1-v^2)^4\mathbf1_{|v|\le1},\quad
k_\ell(v)=\ell^{-1}k(v/\ell),\quad
K(u,v)=k_\ell(u)k_h(v).
\]

The proof uses the entire buffer `|Re z-X|<=ell+2`,
`|Im z|<=Y+h+2`, with `X` sufficiently large. This includes the support
of every translated averaging kernel at `(X,y)`, the collars that meet
that support, and a fixed complex-analytic margin. Constants below may
depend on these fixed data and the fixed regulator parameter eta.

Use exactly [Note 20][n20], FB1--FB2. On this interval write

\[
\epsilon_g(t,u)=E_0(t)e^{-\beta(t)u^2/2},\qquad
\beta(t)=\chi(t)/\kappa(t),\quad
0<\beta_*:=\min_{t\in I}\beta(t),
\tag{GO2}
\]

where `E_0` is positive and smooth. The positivity of beta_* uses the
specific strictly positive switch for every `t>64`, not just a generic
smooth cutoff. Put

\[
q=\epsilon_g^2,\quad r=\log q,\quad
\rho=\frac{q|H_z|^2}{\pi(|H|^2+q)^2},\quad R=K*\rho.
\tag{GO3}
\]

No density or total mass is normalized. A nonvanishing analytic factor
introduced below is only a proof device; GO3 and its q remain unchanged.
Only spatial averaging and a static absolute sup-norm error are asserted.

This is an **approximation milestone** under [avoid/01][a01], judged by
its function, domain and vanishing absolute error, not an RH-equivalent
criterion. Read the [result index][results], [heat-flow cluster][geometry],
[control screen][controls] and [avoid index][avoid], particularly
[scope][a07] and [cancellation][a12]. Section 8 names the premises that
the collision controls fail. No collision outside the eventual domain is
excluded by this argument.

## 2. Exact convolution and the outer pair

Define the exact gamma factor, not the saddle mass of Note 19 and not
the Stirling approximation denoted M_0 in Polymath:

\[
\mathcal M(w)=\frac{w(w-1)}{16}\pi^{-w/2}\Gamma(w/2),\qquad
\alpha(w)=\frac{\mathcal M'(w)}{\mathcal M(w)}
=\frac1w+\frac1{w-1}-\frac{\log\pi}{2}+\frac12\psi(w/2).
\tag{GO4}
\]
\[
\mathcal G_t(w)=\mathcal M(w)e^{t\alpha(w)^2/4},\qquad
s=\frac{1+iz}{2},\qquad
P(t,z)=\mathcal G_t(s)+\mathcal G_t(1-s).
\tag{GO5}
\]

All factors are holomorphic and nonzero in the far-height strips where
used. The apparent poles of the separate factors away from these strips
play no role. P is a local outer approximation, not a proposed entire
replacement for H and not an asserted exact heat solution.

For every real `t>0`, the exact complete-source identity is

\[
H(t,z)=\frac1{\sqrt{\pi t}}\int_{\mathbb R}
 e^{-v^2/t}\frac{\xi(s+v)}8\,dv.
\tag{GO6}
\]

Indeed the Gaussian average of `cos((z-2iv)u)` is
`e^{tu^2} cos(zu)`. Absolute integration is justified by the complete
source bound against `e^{t_b u^2+(Y+h+2)u}`; this is integrable by its
superexponential tail. This is also the exact all-positive-time formula
(35) in [Polymath, Section 4][polymath]. We do not change the hypotheses
of that paper's separate small-time Theorem 1.5.

**Outer field estimate.** For some finite `C,X_0` depending only on the
fixed contract, uniformly for `t in I`, `x>=X_0`, `|y|<=Y+h+2`,

\[
\boxed{|H(t,z)-P(t,z)|\le
 C\delta(x)\bigl(|\mathcal G_t(s)|+|\mathcal G_t(1-s)|\bigr),
 \qquad \delta(x)=\frac{1+\log^2x}{x}.}
\tag{GO7}
\]

The right side is the sum of the two carrier amplitudes, not `|P|`,
which vanishes near its zeros. The estimate is holomorphic-domain
control and will be converted into local collars before using q.

## 3. Proof of the field estimate, with all three source regions paid

Write `sigma=Re s`, which stays in a fixed compact real interval. Split
GO6 into `v>=2-sigma`, `v<=-1-sigma`, and the bounded interval between.
On the right use `xi(w)/8=M(w) zeta(w)`. On the left use the exact
functional equation `xi(w)=xi(1-w)` and substitute `v -> -v`.
This gives the same right-arm problem with center `1-s` and lower limit
`1+sigma`. Both centers have bounded real part and imaginary part
`+x/2` or `-x/2`. Every mode is retained in the zeta remainder.

### 3.1 Uniform gamma estimates and the right-arm Taylor error

The sectorial log-gamma and digamma estimates in
[DLMF 5.11.1--5.11.2 and 5.11(ii)][gamma] imply, for either center w,

\[
\Re\alpha(w)=\tfrac12\log(x/(4\pi))+O_Y(x^{-1}),\quad
|\Im\alpha(w)|\le C_Y,\quad
\alpha'(w)=O_Y(x^{-1}),\quad\alpha''(w)=O_Y(x^{-2}).
\tag{GO8}
\]

These hold on slightly larger sectors. Cauchy's formula on disks of
radius a fixed fraction of x gives the derivative bounds from the
holomorphic remainder; no real-axis big-O is differentiated. In
particular, if the fixed lower integration endpoint is v_0 and
`v_0<=v<=x^(1/3)`,

\[
\log\mathcal M(w+v)=\log\mathcal M(w)+v\alpha(w)+E(w,v),
\qquad |E(w,v)|\le C_Y v^2/x.
\tag{GO9}
\]

Choose a continuous logarithm along this zero-free region. For
`a=Re alpha(w)`, `b=Im alpha(w)`, the full linearized Gaussian integral is
exactly `exp(t alpha(w)^2/4)`. Its absolute Gaussian integral divided by
the modulus of this answer costs `exp(tb^2/4)`, bounded on the fixed
contract. Completing the real square, including the small quadratic
perturbation in GO9, gives

\[
\frac{\int_{v_0}^{x^{1/3}}e^{-v^2/t+av}
 |e^{E(w,v)}-1|\,dv}{\sqrt{\pi t}\,
 |e^{t\alpha(w)^2/4}|}
\le C_{I,Y}\frac{1+\log^2x}{x}.
\tag{GO10}
\]

For clarity, `|e^E-1|<=C v^2/x` on this range, since
`v^2/x<=x^(-1/3)` apart from a bounded initial segment. The real Gaussian
has mean `t*a/2`, variance `t/2`, and second moment `O_I(1+log^2x)`.
The discarded linearized range `v<v_0` costs at most

\[
 C_{I,Y}\exp\{-t_a\log^2(x/(4\pi))/16+C_{I,Y}(1+\log x)\}.
\tag{GO11}
\]

This is smaller than every fixed inverse power of x, after a
contract-dependent onset. It is not an estimate uniform as `t_a -> 0`.

The infinite positive tail has not been discarded without payment.
For all `v>=0`, the same sectorial digamma estimate along the horizontal
ray yields

\[
\log\frac{|\mathcal M(w+v)|}{|\mathcal M(w)|}
 \le C_Yv+\tfrac12v\log(x+v).
\tag{GO12}
\]

For all sufficiently large x and all `v>=x^(1/3)`, the right side is at
most `v^2/(2t_b)`. To see uniformity in v, the ratio
`v/[C_Y+(1/2)log(x+v)]` is eventually increasing there, and its value at
`x^(1/3)` tends to infinity. Thus the Gaussian tail is bounded by
`C_I exp(-x^(2/3)/(4t_b)) |M(w)|`, also at most that order times
`|G_t(w)|`. The same bound applies to the linearized tail. This retains
the carrier's exponential decay in height, rather than replacing it by
a source moment bound before division.

### 3.2 The complete arithmetic tail

For `Re(w+v)>=2`, the absolutely convergent Dirichlet series gives

\[
|\zeta(w+v)-1|\le3\,2^{-\Re w-v}.
\tag{GO13}
\]

The coefficient 3 follows by keeping the n=2 term and integrating the
remaining decreasing series. In GO9--GO10 replace a by `a-log 2`.
The resulting ratio of Gaussian factors is

\[
\exp\{-\tfrac t2 a\log2+\tfrac t4(\log2)^2+\tfrac t4 b^2\}
\le C_{I,Y}x^{-t_a\log2/4}.
\tag{GO14}
\]

The paid far tail obeys GO12. Since `t_a>64`, the power
`t_a log(2)/4` is greater than 1, so GO14 is absorbed in GO7. No finite
list of theta or Dirichlet modes is substituted for this full tail.
The series input is [DLMF 25.2.1][zeta].

### 3.3 The bounded middle strip

Here `-1<=Re(s+v)<=2` and v stays bounded in terms of Y. By the functional
equation, the xi value can be evaluated with real part in `[1/2,2]`.
Euler summation [DLMF 25.2.8][zeta], with `N=ceil x`, bounds zeta there
by `C x`: the finite sum is at most N, the integral remainder at most
`C x N^(-1/2)`, and the pole term is bounded since `|Im w|=x/2`.
Uniform bounded-real-part Stirling then gives

\[
|\xi(s+v)/8|\le C_Y x^4e^{-\pi x/8}.
\tag{GO15}
\]

The rough fourth power is sufficient. Meanwhile either outer carrier has
logarithmic modulus

\[
\log|\mathcal G_t(w)|=-\pi x/8+
\frac t{16}\log^2(x/(4\pi))+O_{I,Y}(1+\log x).
\tag{GO16}
\]

Consequently the entire bounded middle integral, divided by either
carrier, is bounded by the form in GO11 with a larger constant. The
right arm, reflected left arm, middle interval, Gaussian extensions and
infinite tails now sum to GO7. This proof establishes existence of finite
uniform constants and an eventual threshold. It does not supply a
numerical or interval-certified value for that threshold.

## 4. Analytic phase, all nearby zeros, and actual field floors

On a sufficiently far-right strip choose conjugate-compatible logarithms
of the two factors, and set

\[
\mathcal A(t,z)=\exp\{(\log\mathcal G_t(s)+\log\mathcal G_t(1-s))/2\},
\quad
\Theta(t,z)=\frac{\log\mathcal G_t(s)-\log\mathcal G_t(1-s)}{2i}.
\tag{GO17}
\]

Thus `P=2 A cos Theta`. On the real axis `A(t,x)>0`,
`theta(t,x):=Theta(t,x)` is real, and
`A(t,x)=|G_t((1+ix)/2)|`. A choice of branch changes theta by an integer
multiple of `2pi`, which does not change the formulas below.

Let

\[
\omega(t,X)=\partial_x\theta(t,X)
=\frac12\Re\left[\alpha(s_X)+\frac t2\alpha(s_X)\alpha'(s_X)\right],
\quad s_X=(1+iX)/2.
\tag{GO18}
\]

The estimates in Section 3, including one additional sectorial term if
needed, imply uniformly on each fixed complex buffer

\[
\omega(t,X)=\frac14\log(X/(4\pi))+O_I(\log X/X),\quad
\partial_z^2\Theta(t,z)=O_{I,Y}(X^{-1}),\quad
|\partial_z\log\mathcal A(t,z)|\le C_{I,Y}.
\tag{GO19}
\]

For the last bound the two leading logarithms cancel in
`(i/4)[(log G_t)'(s)-(log G_t)'(1-s)]`; bounding them separately by
`O(log X)` would lose the useful amplitude comparison. In particular,
`|A(t,z)|` is bounded above and below by fixed multiples of
`A_X=A(t,X)` on the complete local buffer.

Dividing GO7 by the nonzero A gives the relative trigonometric estimate

\[
|H/\mathcal A-2\cos\Theta|
 \le C\delta(X)\bigl(|e^{i\Theta}|+|e^{-i\Theta}|\bigr).
\tag{GO20}
\]

Fix once and for all `0<r_0<pi/10`. The real phase roots `d_j` solve
`theta(t,d_j)=(j+1/2)pi`; on an enlarged local interval they are unique
and have spacing comparable to `pi/omega`. On the circles
`|z-d_j|=r_0/omega`, GO19 gives
`Theta(z)-Theta(d_j)=theta'(d_j)(z-d_j)+O(1/(X omega^2))`.
Hence `|cos Theta|` is bounded below by a fixed positive multiple of
r_0 there, while the two exponentials remain bounded. For sufficiently
large X, Rouche's theorem applied to GO20 gives exactly one H zero,
counting multiplicity, in each circle. It is simple, and real because H
is real under conjugation and the circle is conjugation invariant.

These are all the zeros that can meet the inner buffer. Indeed

\[
|\cos(u+iv)|^2=\cos^2u+\sinh^2v
\]

shows that at a zero of H, GO20 forces `|Im Theta|<=C delta(X)` and
`dist(Re Theta,pi/2+pi Z)<=C delta(X)`. On the convex local rectangle,
`Theta'` differs from the positive number omega by `O(1/X)`.
It therefore has an injective local phase coordinate (integrate the
real part of its derivative along the line segment), with inverse
Lipschitz constant at most `2/omega`. The nearby phase root is real and
inside the enlarged interval. No additional nonreal zero can escape
these disks. The actual root a_j satisfies

\[
|a_j-d_j|\le C\delta(X)/\omega.
\tag{GO21}
\]

Now recenter disjoint collars of radius `R_c=r_0/omega` at the actual
roots; increasing the initial circle radius slightly in the argument
above, or first using the smaller displacement circles, supplies the
same boundary estimates. Outside these actual collars, throughout the
kernel support,

\[
|H(t,z)|\ge c A_X,
\qquad
|H(t,z)|\ge c A_X\omega|z-a_j|quad (|z-a_j|\le R_c).
\tag{GO22}
\]

The first bound follows from GO20 and the trigonometric lower bound away
from all phase roots. For the second, `H/(z-a_j)` is holomorphic and
zero-free on the collar; its boundary modulus is at least `c A_X/R_c`.
Apply the maximum-modulus principle to its reciprocal. There are at
most `C omega` collars meeting the support or its small enlargement.
Both the exterior floor and the analytic-unit floor are proved from the
complete field comparison; neither is a sampled minimum or an assumed
zero separation. See [Note 09][n09] for the same quotient principle.

## 5. Pay the shrinking-regulator transfer separately

Let `nu_t` be the planar zero measure with multiplicities. For the
translated test function `psi(u,v)=K(X-u,y-v)`, the exact identity and
bound [Note 14][n14], VE15--VE18, give

\[
|R(t,X,y)-(K*\nu_t)(X,y)|\le
\frac{\mathcal K_r(\psi)}{4\pi}\int_{\operatorname{supp}\psi}
 \log(1+q/|H|^2)\,du\,dv,
\tag{GO23}
\]
\[
\mathcal K_r(\psi)=\|\Delta\psi\|_\infty+
2\|\nabla r\|_\infty\|\nabla\psi\|_\infty+
(\|\Delta r\|_\infty+\|\nabla r\|_\infty^2)\|\psi\|_\infty
\le C_I(1+X^2).
\]

Here `r=2 log E_0-beta u^2`, so `r_u=-2 beta u`,
`Delta r=-2 beta`. In particular the adaptive curvature terms have not
been dropped. Define

\[
\lambda_X(t)=\frac{\sup_{|u-X|\le\ell+2}\epsilon_g(t,u)}{A_X}.
\]

Using GO22 outside the collars, and its linear floor inside each one,
the simple-root logarithmic integral yields

\[
\int_{\operatorname{supp}\psi}\log(1+q/|H|^2)
\le C\lambda_X^2
\left[1+\frac{1+\log(1+C/\lambda_X^2)}{\omega}\right].
\tag{GO24}
\]

This follows from `C omega` disks, each with slope `c A_X omega` and
radius `r_0/omega`, and
`I_1(a,R)<=pi a^2[1+log(1+R^2/a^2)]`. Full disks can be used to
majorize their intersections with the support. The field floors hold on
those full disks within the chosen margin.

GO2 and GO16 imply

\[
\log\lambda_X\le-\tfrac12\beta_*(X-\ell-2)^2+
\pi X/8+C_I(1+\log^2X),\qquad
|\log\lambda_X|\le C_I(1+X^2)
\tag{GO25}
\]

after increasing X_0; the second inequality also uses bounded beta and
positive E_0 on I. Thus all the polynomial factors in GO23--GO24 are
absorbed by the Gaussian decay. Uniformly in the observation strip,

\[
\boxed{|R-K*\nu_t|(t,X,y)\le C_{I,\ell,h,Y}
 e^{-\beta_*X^2/4}.}
\tag{GO26}
\]

There is no regulator floor on the unbounded domain. GO26 instead uses
its actual upper bound and both logarithmic-regulator derivatives, with
proved physical-field collars. This is the additional regularization
payment; it is distinct from approximating the zero locations.

## 6. An explicit finite phase formula and its absolute error

Freeze the phase at the observation height X:

\[
p=\frac\pi\omega,\qquad v=\frac{\theta(t,X)}\omega,\qquad
b_j=X+\frac{(j+1/2)\pi-\theta(t,X)}\omega.
\tag{GO27}
\]

Equations GO19 and GO21 show, for all labels in the fixed enlarged
horizontal buffer,

\[
|a_j-b_j|\le\frac{C}{\omega}\left(\delta(X)+\frac1X\right).
\tag{GO28}
\]

There are `O(omega)` relevant labels. The globally Lipschitz, compactly
supported k_ell handles kernel-edge crossings without a missing count.
Since all the zeros in the kernel buffer are real,

\[
\left|(K*\nu_t)(X,y)-k_h(y)
 \sum_{j\in\mathbb Z}k_\ell(v-(j+1/2)p)\right|
\le C_{I,\ell,h,Y}\delta(X).
\tag{GO29}
\]

The sum has an exact five-term expression already derived in
[Note 19][n19], SC11. To state the final formula without a growing sum,
write `mathcal B_m(w)=B_m({w})`, and

\[
a_m=k_\ell^{(m)}(\ell),\qquad
(a_4,a_5,a_6,a_7,a_8)=\frac{315}{256}
\left(\frac{384}{\ell^5},\frac{3840}{\ell^6},
\frac{17280}{\ell^7},\frac{40320}{\ell^8},\frac{40320}{\ell^9}\right).
\]
\[
\mathscr P_\ell(p,v)=\frac1p+
\sum_{m=4}^8\frac{p^m a_m}{(m+1)!}
\left\{\mathcal B_{m+1}\left(\frac{v-\ell}p+\frac12\right)
-(-1)^m\mathcal B_{m+1}\left(\frac{v+\ell}p+\frac12\right)\right\}.
\tag{GO30}
\]

Set `R_out(t,X,y)=k_h(y) mathscr P_ell(p,v)`. This is an exact
periodization formula for the frozen lattice, not a Fourier truncation.
Combining GO26 and GO29 proves

\[
\boxed{\sup_{t\in I,\ |y|\le Y}
|R(t,X,y)-R_{\rm out}(t,X,y)|\le
C_{I,\ell,h,Y}\frac{1+\log^2X}{X},\qquad X\ge X_0.}
\tag{GO31}
\]

The density's absolute scale is `omega/pi`, growing like `log X/(4pi)`.
The bounded Bernoulli functions in GO30 give
`|mathscr P_ell-1/p|<=C_ell p^4` for sufficiently small p. With GO19,

\[
\boxed{\sup_{t\in I,\ |y|\le Y}
\left|R(t,X,y)-\frac{k_h(y)}{4\pi}\log\frac{X}{4\pi}\right|
\le C_{I,\ell,h,Y}
\left\{(\log X)^{-4}+\frac{1+\log^2X}{X}\right\}.}
\tag{GO32}
\]

For negative heights use `X=|x|`: evenness and conjugation of H, the
even regulator and the even kernels give the same averaged density.
The conclusions hold throughout both tails, not just at selected heights.
For `|y|>h`, the leading profiles vanish and the regularization payment
GO26 still controls the true off-axis density. Fixed widths matter; no
shrinking-width or growing-transverse-strip theorem is asserted.

### A nonuniform layer at the regulator switch

For each fixed y with `|y|<h`, Note 25 and GO32 together give

\[
\lim_{X\to\infty}\frac{R(t,X,y)}{\log X}=
\begin{cases}
0,&t\le64,\\
k_h(y)/(4\pi),&t>64.
\end{cases}
\tag{GO33}
\]

At every finite X the left-hand expression is continuous in t. Thus
this limiting profile cannot be approached uniformly on a time interval
crossing 64: a uniform limit of continuous functions would be continuous.
This is a scoped failure of uniformity of the displayed limiting profile,
not an obstruction to an interpolating time/height approximation. It is
created by the chosen regulator's spatial switch; H itself has no time
discontinuity. The vanishing beta_* as `t_a` decreases to 64 is therefore
a real additional layer in all-time assembly, not merely a loose constant.

## 7. What this adds, and the next analytical task

| Error or obligation | Present payment |
| --- | --- |
| Complete field, two gamma factors | GO7, absolute error relative to the sum of carrier amplitudes; includes reflected arm, bounded middle, all arithmetic modes and both Gaussian extensions. |
| Actual zero collars and lower bounds | GO21--GO22, on the full fixed complex buffer, uniformly on each compact I. |
| Adaptive density versus zero measure | GO26, Gaussian in height after the physical amplitude and log-regulator derivatives are paid. |
| Frozen phase versus actual zero measure | GO28--GO29, O(log^2 X/X). |
| Five-term phase representation | Exactly zero truncation error. Omitting phase costs O((log X)^-4). |
| Instantiated constants or certified finite onset | Not supplied. |
| Current, time derivative, source-anchored potential, actual Q and Delta Q | Not proved here. Static GO31 must not be differentiated or promoted to those budgets. |
| Joint time/height regime and overlap with Note 19 | Open; compact-time constants cannot be used as t tends to infinity, and GO33 requires a regulator layer near 64. |

The fundamental formula GO6 is exact heat evolution. The asymptotic pair
GO5 is not assigned that property: its heat residual and the observables
built from it would require their own comparisons. No covariance is
chosen to force an equation to hold. Note 25's scoped positive-cutoff
potential obstruction is unchanged; this construction has no finite
source endpoint and does not contradict it.

**Next owner: Analytical — Astra.** Derive a time-dependent outer
validity/error budget, including the regulator layer near 64, and determine how to bridge it to Note 19's
`|x|~kappa^(1/3)` inner window. The real Gaussian tilt in this proof has
size `O(t log x)`, while its local gamma curvature payment involves
`O(t^2 log^2 x/x)` and the absolute integration pays an additional
`exp(t (Im alpha)^2/4)`. These observations diagnose why the present
compact-time proof does not itself supply a joint overlap; they are not
a claimed sufficient joint-regime bound. A complex saddle or an
intermediate-height approximation must be developed before an overlap
is asserted. Then pay the positive evolution/potential/covariance terms.
No numerical packet is justified merely by the existence of an eventual
onset; there is currently no pending Sol assignment.

## 8. Collision-control screen and provenance

The distinguishing input is the **unchanged complete theta identity**
`xi(w)/8=M(w) zeta(w)`, together with its exact reflection and the full
Dirichlet-series tail, not positivity, endpoint matching, moments or
source shape alone. This is legitimate source information for an
approximation problem, not a restatement of a desired no-collision sign.

| Control family in [the repository screen][controls] | Premise of this proof that is not shared |
| --- | --- |
| Euler-factor controls | Their completed transform contains the added Euler factor and changed completion; it is not GO1 with the unchanged GO4 and ordinary zeta series. Full reflection alone does not remove that factor. |
| Weighted-square controls and finite theta/zero-tail modifications | The unchanged full coefficients and completed functional equation used to reflect the left arm are absent; finitely many endpoint conditions do not supply them. |
| Reflected super-Gaussian and smooth shape/positive-primitive controls | Reflection and shape do not supply the canonical gamma times ordinary zeta identity in GO4/GO13. |
| Finite-prime-compatible orbit controls | They do not retain full theta reflection or the unchanged complete coefficient sequence. Finite orbit identities do not justify the left-arm replacement. |
| Atomic fixed-event and finite-profile threshold controls, including their compact-source extensions | They lack the canonical xi completion and full source profile; matching finite profiles/moments does not establish GO6 with the canonical xi. |
| RH-conditional normalized-endpoint controls | They explicitly fail ordinary Dirichlet-series arithmetic, so GO13 is not their remainder estimate. |

This is a premise screen, not fresh computation of those controls. An
event below the eventual height threshold, at another time, or for a
changed source is not contradicted by GO31. In particular this proof
makes no assertion at t=0 and does not establish RH. Eventual real and
simple high zeros have existing literature antecedents; the useful
investigation gain is the stated regulator/kernel density comparison.

The [reference catalog][references] records the inspected primary
sections and the existing Polymath reading-copy provenance. Standard
special-function and complex-analysis inputs are attributed there;
this note derives the particular compact-time and weak-transfer estimates.
The author/model attribution and same-assistant status apply to the
new derivation, not to those earlier sources. No independent reviewer
or numerical validation participated in this continuation.

[n25]: 25_OUTER_CONTOUR_BOUNDS_AND_CUTOFF_OBSTRUCTION_20261024.md
[n20]: 20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md
[n19]: 19_EXPLICIT_SADDLE_CLOCK_AND_EXACT_PHASE_20261024.md
[n14]: 14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md
[n09]: 09_COMPLETE_SOURCE_MOMENT_TRANSFER_AND_WEAK_CURRENT_20261024.md
[review]: ../reviews/10_GAMMA_OUTER_DENSITY_SELF_REVIEW_20261024.md
[references]: ../references/README.md
[polymath]: https://arxiv.org/html/1904.12438v2
[gamma]: https://dlmf.nist.gov/5.11
[zeta]: https://dlmf.nist.gov/25.2
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
