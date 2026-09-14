# Relative channel cohomology and a nonzero gamma boundary state

12 September 2026. **Analytic toy construction, with proofs.** The kinetic energy being represented is already in the positive-factorizations manuscript. The contribution of this investigation is a different differential, a surviving boundary class, its adjoint-compatible pairing, a geometric realization and explicit gluing, and a restriction on one proposed arithmetic deformation. No new positivity range for the full Weil form is claimed.

## 1. Fixed normalization and the part to be constructed

Put $I_L=(-L/2,L/2)$. Write $F(x)=\widetilde f(x)$ for the zero extension of a complex $f\in C_c^\infty(I_L)$, and $\widehat F(\tau)=\int F(x)e^{-i\tau x}dx$. Inner products are conjugate-linear in the first argument. Define

\[
C(f)=\int_{I_L}f(x)\cosh(x/2)dx,\qquad
S(f)=\int_{I_L}f(x)\sinh(x/2)dx.
\]

For $a>0$, the channel to be derived has kernel

\[
W_a(x,x')={2\over a}\delta(x-x')-e^{-a|x-x'|}. \tag{1}
\]

For $a_k=2k+1/2$, $k=0,1,\ldots$, the sum of its *combined* multipliers is

\[
B(\tau^2)=\sum_{k\ge0}{2\over a_k}{\tau^2\over a_k^2+\tau^2}
=\operatorname{Re}\psi(1/4+i\tau/2)-\psi(1/4). \tag{2}
\]

Here $\psi=\Gamma'/\Gamma$. Subtracting the two partial-fraction series in [DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6) proves (2): the $k$-th real difference is $v^2/[u(u^2+v^2)]$, with $u=k+1/4=a_k/2$, $v=\tau/2$. Substitution gives exactly the summand in (2), fixing the factors of two.

Define $K[F]=(2\pi)^{-1}\int B(\tau^2)|\widehat F(\tau)|^2d\tau$. The full target is

\[
Q_{0,L}[f]=K[F]+w_0\|f\|^2+2|C(f)|^2-2|S(f)|^2
-\sum_{p^m<e^L}{\log p\over p^{m/2}}
\langle f,(T_{m\log p}+T_{m\log p}^*)f\rangle, \tag{3}
\]

where $p$ ranges over primes, $m\ge1$, $T_d f(x)=\widetilde f(x-d)$ on $I_L$, and

\[
w_0=-\gamma_E-\pi/2-3\log2-\log\pi=-5.3721834192\ldots.
\]

The finite-interval domain is $\mathcal D_{\log,L}=\{f\in L^2(I_L):\int\log(2+|\tau|)|\widehat F(\tau)|^2d\tau<\infty\}$. Equations below first hold on the test core. This construction supplies only $K$ in (3).

## 2. An independently positive complex

The arithmetic coordinate is $x\in\mathbb R$. One auxiliary complex scalar $u(x)$ is an even component. The odd component is a pair $w(x)=(w_1(x),w_2(x))$. Use the ordinary positive spaces

\[
E^0=L^2(\mathbb R),\quad E^1=L^2(\mathbb R;\mathbb C^2).
\]

The allowed auxiliary variation $u\in H^1(\mathbb R)$ changes a pair by

\[
u\longmapsto (u,a^{-1}u'). \tag{4}
\]

Only now denote this map by $D_a$. It is closed, densely defined, injective, and has closed range: convergence of $D_a u_n$ forces convergence of $u_n$ and $u_n'$, while $\|D_a u\|\ge\|u\|$. Thus the positive quotient

\[
\mathcal H_a=E^1/\operatorname{ran}D_a
\simeq\ker D_a^*
\]

has its ordinary quotient norm, namely the norm of the orthogonal representative. We are quotienting *auxiliary variations*, not declaring positive-norm vectors null in the original metric. The physical metric is fixed before matching (1).

Integration by parts on the whole line gives

\[
D_a^*(v,w)=v-a^{-1}w',\qquad
\operatorname{Dom}D_a^*=L^2\oplus H^1. \tag{5}
\]

There are no interval side walls: the auxiliary fields extend outside the support of $f$. Introduce the odd symmetry on $E^0\oplus E^1$ by

\[
\mathsf q(u,w)=(0,D_a u),\qquad
\mathsf q^*(u,w)=(D_a^*w,0). \tag{6}
\]

Its domain is $H^1\oplus E^1$, and the adjoint has domain $E^0\oplus\operatorname{Dom}D_a^*$. These give

\[
\mathsf q^2=0,\quad
H_a=\{\mathsf q,\mathsf q^*\}
=\operatorname{diag}(D_a^*D_a,D_aD_a^*)\ge0.
\]

The real supercharges $Q_1=\mathsf q+\mathsf q^*$, $Q_2=i(\mathsf q-\mathsf q^*)$ are self-adjoint on the common natural domain; $Q_1^2=Q_2^2=H_a$, $\{Q_1,Q_2\}=0$. Equation (6) specifies the transformations of state components; it is a linear supersymmetric quantum-mechanical channel model, **not** an interacting superspace Lagrangian or a claimed twist of a relativistic multiplet. Auxiliary time evolution is $e^{-tH_a}$ in Euclidean time, or $e^{-itH_a}$ in real time. The standard Hilbert-complex and SUSY algebra are established frameworks; (4) and the boundary preparation below are this investigation's choices. See [Witten, equations (9)–(12)](https://www.ias.edu/sites/default/files/sns/files/supersymmetry-and-morse-theory-1982.pdf) and [Brüning–Lesch](https://doi.org/10.1016/0022-1236(92)90147-B).

## 3. Boundary preparation and all-input coverage

For an actual input $f$, prepare the class of $\sqrt{2/a}(F,0)$. To find its physical representative, solve

\[
u_f-a^{-2}u_f''=F,\qquad u_f\in H^1(\mathbb R).
\]

There is a unique solution for every $F\in L^2$:

\[
u_f(x)={a\over2}\int_{I_L}e^{-a|x-y|}f(y)dy,\qquad
\widehat u_f(\tau)={a^2\over a^2+\tau^2}\widehat F(\tau). \tag{7}
\]

It is actually in $H^2$. Define the linear boundary map, explicitly on $f$, by

\[
f\longmapsto\Psi_a(f)=\sqrt{2/a}\,(F-u_f,-a^{-1}u_f'). \tag{8}
\]

The minus sign in the second component makes it a harmonic representative in this complex; it does not change its energy relative to the original tower. Equations (5) and (7) give $D_a^*\Psi_a(f)=0$. It follows that $(0,\Psi_a(f))$ is annihilated by both supercharges and by $H_a$, on their actual domains. All complex inputs occur, including nonzero means and both reflection parities. There is no chirality or differential constraint on $f$.

The class is nonzero for nonzero $F\in L^2$. Indeed, $(F,0)=D_a u$ would imply $u=F$, $u'=0$, hence $u=0$ on the whole line. Equivalently, the multiplier of (8)'s squared norm vanishes only at the single point $\tau=0$, so its null space in $L^2(\mathbb R)$ is zero.

This addresses the exact-state problem at its actual scope. The old factorization differential built from the boundary amplitude $A:f\mapsto\Psi_a(f)$ makes $(0,Af)$ exact. The present differential is built from the **different** map (4); $(F,0)$ is not in its range. No quotient by the old $\mathsf q_{\rm fac}$ is being taken.

## 4. Full Hermitian pairing and contact term

For a second input $g$, extend it by zero to $G$ and solve for $u_g$ by (7). The pairing is

\[
Z_a(g,f)={2\over a}\int_{\mathbb R}
\left[\overline{G-u_g}(F-u_f)+a^{-2}\overline{u_g'}u_f'\right]dx. \tag{9}
\]

Using the weak equation for $u_f$, including its exterior decay, gives

\[
Z_a(g,f)={2\over a}\langle G,F-u_f\rangle
={1\over2\pi}\int {2\over a}{\tau^2\over a^2+\tau^2}
\overline{\widehat G(\tau)}\widehat F(\tau)d\tau. \tag{10}
\]

Substitution of (7) in the first expression proves (1), including $2/a$ times the contact delta. Positivity follows from (9), not from defining a kernel inner product to be the answer. In particular an exponential *negative* nonlocal contribution coexists with a positive total Gram form.

If $P_a$ denotes orthogonal projection onto $\ker D_a^*$ and $J F=(F,0)$, (8) is $\sqrt{2/a}P_aJF$. These operator symbols abbreviate the already specified preparation.

## 5. What is protected, including the bra

**Proved invariances.**

* Changing the representative $JF\mapsto JF+D_a v$, $v\in H^1$, changes neither (8) nor (9).
* Replacing $D_a$ by $D_aR$, with $R$ a bounded invertible reparametrization preserving the operator domain and with bounded inverse there, leaves its range and hence $P_a$, (8), and the full Hermitian pairing unchanged.
* For $t\ge0$, $\langle\Psi_a(g),e^{-tD_aD_a^*}\Psi_a(f)\rangle=Z_a(g,f)$. Both states are harmonic. Their actual Hilbert adjoints implement the bra; no holomorphic bilinear form, Berezin norm, or supertrace is substituted.

If an insertion formulation is wanted, one may adjoin a unit vacuum and use the creation map carrying it to (8). Both this map and its adjoint graded-commute with $\mathsf q$, because its image is killed by $\mathsf q$ **and** $\mathsf q^*$. This is a reformulation of the computed preparation, not a newly derived local insertion action. The state-pairing formulation (9) needs no path-integral Ward assumptions.

**A useful failure/control.** For the unprojected source, $Z_t=(2/a)\langle JG,e^{-tD_aD_a^*}JF\rangle$ is generally $t$-dependent. At frequency $\tau$, its diagonal multiplier is

\[
{2\over a}\left[{\tau^2\over a^2+\tau^2}
+{a^2\over a^2+\tau^2}e^{-t(1+\tau^2/a^2)}\right]. \tag{11}
\]

The second term disappears as $t\to\infty$; it is not protected at finite $t$. Heat preparation is a projection limit, and has done the minimization in another form. Changing $a$, or the physical metric on $E^1$, changes (10). In particular this construction does not claim that a $\mathsf q$-exact deformation of an action automatically fixes a positive cohomology norm.

## 6. A literal extra coordinate and a gluing calculation

Introduce an auxiliary segment $0\le y\le h$, $x\in\mathbb R$, a complex field $U(x,y)$, and an endpoint mass coefficient $\mu>0$. Prescribe $U(\cdot,0)=F$; the upper trace $u=U(\cdot,h)\in H^1(\mathbb R)$ is free. Use

\[
\mathcal E[U]=\int_0^h\|\partial_y U(\cdot,y)\|^2dy+\mu\|u'\|^2. \tag{12}
\]

The domain is $H^1([0,h];L^2(\mathbb R))$, with the stated top trace regularity. It is nonempty for every $F\in L^2$, for example $U=(1-y/h)F$. Conditional on $u$, the minimizing field is linear in $y$, and the energy is $h^{-1}\|F-u\|^2+\mu\|u'\|^2$. Its upper boundary equation is

\[
\partial_yU(\cdot,h)-\mu u''=0.
\]

Taking $h=a/2$, $\mu=2/a^3$, proves (7)–(10). This is an explicit massless segment with a positive tangential energy at its far end, or a string with one mass atom followed by a free massless tail. It supplies the coefficient without inverse reconstruction of an unknown target. The general measure-valued string framework is established in [Kwaśnicki–Mucha, Appendix A, Theorems A.2–A.3](https://arxiv.org/pdf/1707.02475); (12)'s elementary special case is solved here. No BPS label is attached to its upper boundary equation.

Subdividing the segment, retaining each interface value and minimizing it, replaces resistances $h_1,h_2$ by $h_1+h_2$. Thus subdivision preserving total resistance is an exact invariant. Changing that resistance changes the boundary response; topological invariance of arbitrary thickness has not been proved.

For gluing along $x=c$, let $F=F_-+F_+$, with disjoint left/right supports. Contact terms have zero cross pairing. The channel cross term is exactly

\[
Z_a(F_-,F_+)=-\left(\int_{x<c}\overline{F_-(x)}e^{a(x-c)}dx\right)
\left(\int_{y>c}F_+(y)e^{-a(y-c)}dy\right). \tag{13}
\]

One complex interface response per channel carries this interaction. Orthogonally adding left and right boundary states would lose it. Another verification: truncating the $u$-integral to an interval $(l,r)$ requires exterior energies $(2/a^2)(|u(l)|^2+|u(r)|^2)$. These impose transparent conditions $u'(l)=a u(l)$, $u'(r)=-a u(r)$. Dropping these terms, or imposing homogeneous Dirichlet side conditions, changes (1). At a cut the common trace must be varied once, with opposite outward fluxes, rather than duplicating independent endpoint reservoirs.

## 7. Infinite tower and a possible origin of its labels

Take the Hilbert direct sum of the harmonic spaces $\ker D_{a_k}^*$ with ordinary component norms. Prepare the sum of states (8). Equation (10), monotone convergence on diagonal inputs, and Cauchy–Schwarz on pairs prove

\[
\Psi^{\rm kin}(f)=(\Psi_{a_k}(f))_{k\ge0},\qquad
\|\Psi^{\rm kin}(f)\|^2=K[F]. \tag{14}
\]

This exists precisely on the logarithmic form domain (with $F\in L^2$). Smooth inputs are a core. Each finite partial tower is positive. No independent subtraction of its divergent contact sum is made. **The raw tower source** $(\sqrt{2/a_k}JF)_k$ has infinite norm for $F\ne0$, since $\sum 2/a_k=\infty$; it cannot be treated as a Hilbert vector before projection. The projected sum (14) is legitimate. Limits of (11) must therefore be taken with this distinction. Direct-sum closed differentials give a well-defined harmonic physical space, while the boundary preparation is unbounded.

A concrete label source is the independent oscillator $A_z=-\partial_z^2+z^2-1/2$ on $L^2(\mathbb R_z)$. With creation/annihilation operators, $A_z=2N+1/2$, so its eigenvalues are $a_k$, and $\operatorname{Tr}e^{-tA_z}=e^{-t/2}/(1-e^{-2t})$. Integrating this positive heat trace against the translation difference gives (2). This offers a simple channel geometry, not a derivation of why arithmetic chooses the offset $1/2$, the spacing (2), or the couplings $2/a_k$. Those remain specified data. Ordinary SUSY oscillator cancellation would remove some of this ordinary trace; it is not to be replaced by a supertrace.

## 8. A calculated obstruction to a first-prime deformation

One reasonable experiment is to rotate the auxiliary range: $D_{a,\eta}=e^{\eta X}D_a$, with a fixed bounded skew-adjoint $X$ on $E^1$, keeping $JF$ fixed. Its harmonic projection is $P_{a,\eta}=e^{\eta X}P_ae^{-\eta X}$. Then

\[
{d\over d\eta}\|\sqrt{2/a}P_{a,\eta}JF\|^2\big|_0
={2\over a}\langle JF,[X,P_a]JF\rangle,
\]

and its absolute value is at most

\[
{4\over a}\|X\|\,\|P_aJF\|\,\|(1-P_a)JF\|. \tag{15}
\]

For $F_N=\chi(x)e^{iNx}$, $\chi\in C_c^\infty(I_L)$, Fourier splitting near $N$ and rapid decay away from $N$ show

\[
\|(1-P_a)JF_N\|^2
={1\over2\pi}\int{a^2\over a^2+\tau^2}|\widehat\chi(\tau-N)|^2d\tau
=O(N^{-2}).
\]

Thus (15) is $O(N^{-1})$. But when $L>\log2$, choose $\chi$ with nonzero overlap with its translate by $d=\log2$. The desired first-prime perturbation on $F_N$ is

\[
-2{\log2\over\sqrt2}\operatorname{Re}\left[e^{-iNd}
\int\overline{\chi(x)}\chi(x-d)dx\right], \tag{16}
\]

which has nonzero order-one subsequences. Hence a bounded range rotation of one channel, or of any fixed finite tower, cannot supply the exact prime term as its first variation. This is a *tangent obstruction for this model*, not a theorem about arbitrary coherent deformations or an infinite tower. The constants in the finite-tower estimate are not uniform as channel masses increase. Arithmetic may need to couple arbitrarily high channel masses, change the injection, or use a different physical space.

Adding new quotient directions while retaining the old ones also cannot by itself produce the prime correction: distance to a larger subspace decreases for every input, whereas the prime correction has both signs. A rotation need not have that monotonicity, which is why (15) was tested separately.

## 9. What this success adds, and what it does not

Equations (4)–(14) establish an infinite-dimensional positive physical sector, nonzero classes for every required input, the whole polarized nonlocal kernel including its contact term, an actual adjoint, restricted auxiliary invariance, and interface variables. These resolve specific questions left open by simply grading the energy factor. The calculation also shows that projection has retained the old minimization rather than bypassed it. The value is structural and diagnostic, not a new proof of gamma kinetic positivity.

The missing pieces of (3) are exactly $w_0\|f\|^2$, both poles jointly, and all prime delays. Adding independent positive states can supply $2|C|^2$, but not $w_0\|f\|^2-2|S|^2$. At $L=1$ even the complete gamma subsystem is negative on a known odd input; it cannot remain a separately positive additive subsystem there. The delay analysis in [02_DELAY_CHANNELS.md](02_DELAY_CHANNELS.md) provides an exact next arithmetic object and the diagonal accounting it demands.
