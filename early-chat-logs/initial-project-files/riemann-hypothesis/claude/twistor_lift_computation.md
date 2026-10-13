# The Twistor Lift of Intrinsic Slice Regular Functions: Explicit Computation and the Discriminating Invariant

*Working note #2 — August 17, 2026. Continues `RH_program_synthesis.md`. All coordinates follow Thol.pdf / Tconffinal.pdf conventions.*

## 1. Setup: coordinates on twistor space

$\pi:\mathbb{CP}^3\to\mathbb{HP}^1$, $[z_1,z_2,z_3,z_4]\mapsto[z_1+z_2j,\,z_3+z_4j]$, chart $z_4=1$, $q=(z_3+j)^{-1}(z_1+z_2j)$, fiber coordinate $\eta(w)=(w+j)^{-1}i(w+j)$ (stereographic $\mathbb{C}\to I_u$; this is eq. (2.3) of Thol with $w=z_3$). The real structure is the fixed-point-free antiholomorphic involution $\sigma[z_1,z_2,z_3,z_4]=[-\bar z_2,\bar z_1,-\bar z_4,\bar z_3]$; fibers of $\pi$ are exactly the $\sigma$-invariant lines; in $(q,\eta)$ coordinates $\sigma(q,\eta)=(q,-\eta)$.

**Twistor lines over spheres.** For $\zeta=u+iv\in\mathbb{C}$, the "graph line" $L_\zeta=\{(u+\eta v,\;\eta):\eta\in I_u\}$ (Thol Def. 2.1 with $h=u$, $\rho=v$, $M=\mathrm{id}$). Substituting $\eta(w)$ and clearing:

$$z_1+z_2j=(w+j)(u+\eta(w)v)=\zeta w+\zeta j \;\Longrightarrow\; L_\zeta=\{[\zeta w,\ \zeta,\ w,\ 1]:w\in\mathbb{CP}^1\}.$$

For $v>0$: the holomorphic lift of the sphere $S_\zeta=u+vI_u$; for $v=0$: **the twistor fiber $F_u=\pi^{-1}(u)$** (check: $\sigma[uw,u,w,1]=[-u,u\bar w,-1,\bar w]\sim[u w',u,w',1]$ with $w'=-1/\bar w$, so $L_u$ is $\sigma$-invariant with the antipodal map on the $w$-parameter). One parametrization uniformly covers spheres and real points; $\sigma(L_\zeta)=L_{\bar\zeta}$.

**Plücker coordinates.** From the points $w=0,\infty$: $[p_{12}:p_{13}:p_{14}:p_{23}:p_{24}:p_{34}]=[\zeta^2:0:\zeta:-\zeta:0:1]$ — a **conic** in the Klein quadric ($p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}=\zeta^2-\zeta^2=0$ ✓). So the family $\{L_\zeta\}_{\zeta\in\mathbb{CP}^1}$ is a conic of lines; its ruled surface is a quadric (next).

## 2. The incidence quadric and the lift

The union $\bigcup_{\zeta\in\mathbb{CP}^1}L_\zeta$ satisfies $z_1=\zeta w,z_2=\zeta,z_3=w,z_4=1$, hence is the smooth quadric

$$Q:\; z_1z_4=z_2z_3,\qquad Q=\{(q,\eta):q\in\mathbb{C}_\eta\}\ \cong\ \mathbb{CP}^1_\zeta\times\mathbb{CP}^1_w,$$

i.e. the **incidence variety of points with their own slice's complex structure** — precisely the locus $\mathcal{L}$ on which (see §3) the naive lift is holomorphic. Its two rulings have transparent meaning:

- **Ruling A** ($\zeta=$ const): the lines $L_\zeta$ — twistor lifts of spheres, degenerating to fibers over $\mathbb{R}\cup\{\infty\}$;
- **Ruling B** ($w=$ const): the loci $\{(q,\eta_0):q\in\mathbb{C}_{\eta_0}\}$ — a full slice with its fixed complex structure.

The chart identity $q=(w+j)^{-1}\zeta(w+j)$ says: the point of $Q$ with coordinates $(\zeta,w)$ is $x+y\,\eta(w)$ where $\zeta=x+iy$ — the coordinates *are* (complex label of the sphere, complex structure). The real structure restricts to $\rho(\zeta,w)=(\bar\zeta,\,-1/\bar w)$ (conjugation × antipodal), fixed-point free.

**Theorem (lift; verified directly).** Let $f$ be intrinsic slice regular ($f(x+yJ)=\alpha(x,y)+J\beta(x,y)$, $F=\alpha+i\beta$ holomorphic on $\mathbb{C}$). Then the map

$$\tilde f=F\times\mathrm{id}:\;Q\to Q,\qquad (\zeta,w)\mapsto(F(\zeta),\,w)$$

is holomorphic, $\rho$-equivariant ($F(\bar\zeta)=\overline{F(\zeta)}$ by intrinsicness), and covers $f$ on the real slice: over $q=x+y\eta(w)$ it returns $\alpha+\beta\,\eta(w)=f(q)$ with the *same* complex structure label.

*Direct check that $Q$ is the natural domain:* the naive assignment $(q,\eta)\mapsto(f(q),\eta)$ on the full $\mathbb{H}\times I_u$ is holomorphic iff $d(f)$ intertwines $dq\mapsto\eta\,dq$; for $f=q^2$, $d(q^2)=dq\,q+q\,dq\mapsto \eta\,dq\,q+q\eta\,dq$, which equals $\eta\,d(q^2)$ iff $q\eta=\eta q$ iff $q\in\mathbb{C}_\eta$ — i.e. exactly on $Q$. **This resolves the rigidity tension of Thol Prop. 3.1:** an intrinsic function does *not* extend to a holomorphic self-map of any neighborhood of $Q$ in $\mathbb{CP}^3$ (unless Möbius); the rotational-symmetry class lives on the incidence quadric, not on all of twistor space. The "class of functions with rotational symmetry" = holomorphic self-maps of $(Q,\rho)$ of product type $F\times\mathrm{id}$ with $F$ $\rho$-real — a *commutative* function theory in one complex variable $\zeta$, fibered trivially over the sphere of complex structures. (Closure under $+,\times,\circ$ is now visible by inspection.)

## 3. The two model cases and the invariant

Zero divisor of $\tilde f$ (as the divisor $F^{-1}(0)\times\mathbb{CP}^1_w$ in $Q$, i.e. the union of Ruling-A lines over the zeros of $F$):

**Case A: $f(q)=q^2-1$.** $F(\zeta)=\zeta^2-1$, zeros $\zeta=\pm1$ (real). Zero divisor $=F_{1}+F_{-1}$: **two $\sigma$-fixed rulings** (twistor *fibers*). Downstairs: two real point zeros.

**Case B: $f(q)=q^2+1$.** $F(\zeta)=\zeta^2+1$, zeros $\zeta=\pm i$. Zero divisor $=L_{i}+L_{-i}$: **one $\sigma$-swapped pair of rulings** ($\sigma(L_i)=L_{-i}$, each individually *not* invariant, each transverse to the fibers). Downstairs: the zero sphere $I_u$.

**The invariant that differs is equivariant, not homological:** in $H_2(Q;\mathbb{Z})$ both divisors have class $2[\text{Ruling A}]$ — identical. What differs is **the action of the real structure on the components of the zero divisor**: fixed components vs. swapped pairs. Equivalent formulations, each computed above or below:

1. *Divisor form:* zeros real $\iff$ every component of $Z(\tilde f)$ is a $\sigma$-invariant line ($=$ a twistor fiber).
2. *Value-curve form:* the Klein-quadric curve $\zeta\mapsto\mathrm{Pl}(L_{F(\zeta)})=[F^2:0:F:-F:0:1]$ passes through the fiber-point $\mathrm{Pl}(F_0)=[0:\dots:0:1]$ once per zero of $F$; at a multiple passage the curve has a node whose branches are **individually $\sigma$-real (crunode type)** for a pair of real zeros, and **exchanged by $\sigma$ (acnode/solitary type)** for a conjugate pair. Real zeros vs. zero spheres = hyperbolic vs. elliptic real nodes of the value curve at real points of the Klein quadric.
3. *Quotient form:* $\sigma$ acts freely; in $Y=Q/\sigma$ (an $S^2$-family over the closed half-plane $\overline{\mathbb{C}^+}$ whose boundary fibers over $\mathbb{R}\cup\{\infty\}$ are $\mathbb{RP}^2$'s), a real zero descends to an $\mathbb{RP}^2$ (nonorientable), a zero sphere to an $S^2$ (orientable). **RH $\iff$ every component of the zero locus of $\tilde\Xi$ in $Y$ is nonorientable.**

## 4. Verified no-go extension: the quaternionic winding also weights spheres by 2

Candidate nonlinear invariant: the Brouwer degree of $f/|f|:\partial\Omega\to S^3$ (the 4D argument principle; equivalently the Cauchy–Fueter-type winding, and the natural target of Quat_Riemann §7's unfinished branch-cut analysis). Computed:

- $f=q^m$ on $|q|=1$: preimages of generic $w$ are the $m$ slice roots; the ℝ-linear Jacobian of $q\mapsto q^m$ splits into the slice plane (det $m^2|q|^{2(m-1)}>0$) and the orthogonal plane, where $vq=\bar qv$ gives $L(v)=\big(\sum_i q^i\bar q^{\,m-1-i}\big)v=\frac{\sin m\psi}{\sin\psi}\,v$ (a real scalar, $q=e^{u\psi}$), det $\ge0$. All preimages positive: **local degree at a real zero of multiplicity $m$ is $m$.**
- $f=q^2+1$ near the zero sphere: local model $f(x+yJ)=-2(y-1)+2xJ$; on the boundary $S^1_\phi\times S^2_J$ of a tubular neighborhood the map is $(\phi,J)\mapsto\cos\phi'+J\sin\phi'$, which hits a generic target twice ($(\phi_0,J_0)$ and $(-\phi_0,-J_0)$), both positively (forced by matching the global degree of $q^2+t$, $t\in[0,1]$, on a large $S^3$, which is $2$, and the homology $[S^3_R]=[S^2\times S^1]$ in $\mathbb{H}\setminus S^2$): **local degree at a simple zero sphere is $2$** ($2m$ for multiplicity $m$).

So the topological winding counts $r+2s$ — exactly the complex count. **The "$c=2$ conspiracy" of Quat_Riemann §4 persists for the nonlinear degree.** This is consistent with, and required by, the Davenport–Heilbronn test (degree is deformation-invariant = too soft). The discriminant must be finer than homology *and* finer than degree: the $\sigma$-equivariant component type of §3 is the minimal such refinement, and it is *not* a deformation invariant — components change type precisely when zeros collide on the axis (see §6).

## 5. Generalization toward RH: three analytic forms of the invariant

The equivariant invariant is a relabeling *locally*; its value is that it points at the right *global* quantities. Three concrete crystallizations, ordered by tractability:

**(5a) The graded Laguerre hierarchy (recommended).** The classical certificate that a node at a real point is a crunode is a *positivity*: for $\Xi$ real entire of genus 1,
$$-\big(\log\Xi\big)''(x)=\sum_\rho\frac{1}{(x-\rho)^2},\qquad x\in\mathbb{R},$$
where a real zero contributes $(x-\rho)^{-2}>0$ and a conjugate pair (zero sphere of radius $y_0$) contributes $2\,\mathrm{Re}\,(x-z_0)^{-2}$, which is **negative** for $|x-a|<y_0$: spheres, and only spheres, push the expression down. Positivity for all real $x$ is the Laguerre inequality $\Xi'^2-\Xi\Xi''\ge0$ — necessary for RH; and the **generalized Laguerre inequalities $L_n(\Xi)(x)\ge0$ (all $n\ge1$, all $x\in\mathbb{R}$) characterize the Laguerre–Pólya class, so the full family is equivalent to RH** (Csordas–Varga line of work). The twistor reading: $L_1\ge0$ is the statement that the value curve meets the real Klein quadric "from the crunode side" at $F_0$; the higher $L_n$ are its jets. **Proposed new object:** replace the axis-evaluation by the sphere-average pairings of Quat_Riemann §§6–8 — the $\ell$-sector functionals
$$\mathcal{E}_\ell(x;\lambda)=\Big\langle Q_\ell\big(\tfrac{\xi'}{\xi}\big),\,Q_\ell\big(\tfrac{\xi'}{\xi}\big)\Big\rangle_{x,\lambda}$$
built from the Bessel kernels $E_\ell$. These are *quadratic* in the zeros (the no-go of memo §5 does not apply); a real zero enters the $\ell$-sector through $j_\ell(\lambda\cdot0)=\delta_{\ell0}$-type factors while a sphere of radius $y_0$ enters through $j_\ell(\lambda y_0)\ne0$ — so the hierarchy is a **Bessel-graded family of Laguerre-type inequalities in which the sphere contribution is structurally tagged by its radius.** Concrete conjecture to test first (numerically, then via the explicit formula): each $\mathcal{E}_\ell$-positivity is implied by RH, the family jointly implies it, and the $\ell$-grading diagonalizes the radius-dependence that the classical $L_n$'s mix. This passes the two hardness tests by construction: DH fails the inequalities (its spheres make terms negative), and small spheres degrade positivity only quantitatively ($j_\ell(\lambda y_0)=O((\lambda y_0)^\ell)$ — which also *predicts* that high-$\ell$ tests lose power near the axis, matching "RH is barely true").

**(5b) Sign-constancy on the degenerate curves.** The lift meets the real slice of the Klein quadric exactly over $D=\{\zeta:\mathrm{Im}\,\Xi(\zeta)=0\}$ (where the sphere $S_\zeta$ maps to a *real* value — the collapse locus of the rotational picture; on the axis this is automatic). RH $\iff$ **$\Xi$ has constant sign on every connected component of $D\cap\mathbb{C}^+$.** These curves are the "x-ray" curves of Arias de Reyna's plots of $\zeta$; in this framework they acquire intrinsic meaning (the locus where Ruling-A lines become $\sigma$-invariant under the value map) and a 1D Sturm-type structure: along each component $\Xi$ is real-valued and real-analytic, so RH becomes an oscillation-theory statement on a canonical family of curves. Tractable sub-questions: topology of $D$ for $\Xi$ (components, endpoints at zeros of $\Xi'$ — contact with Speiser's theorem: RH $\iff$ $\zeta'\ne0$ in $0<\sigma<\tfrac12$), and the behavior of the explicit formula restricted to $D$.

**(5c) Real-enumerative asymptotics.** For the Hadamard/Jensen truncations $\Xi_N$ (real polynomials, hence rational curves of degree $2N$ in the Klein quadric via $[\Xi_N^2:0:\Xi_N:-\Xi_N:0:1]$), the crunode/acnode counts at $F_0$ are exactly (real zeros)/2-vs-(conjugate pairs), and the Jensen–Pólya program (hyperbolicity of Jensen polynomials, Griffin–Ono–Rolen–Zagier) says RH $\iff$ acnode count $\to0$ appropriately. Signed counts weighting acnodes by $-1$ (Welschinger-style) are deformation-invariant where unsigned ones are not; the open question worth one focused attempt: is there a signed/equivariant count of fiber-rulings of the truncation surfaces whose *stability* converts GORZ-type asymptotic hyperbolicity into a statement with a geometric proof mechanism? (Highest risk, highest novelty.)

## 6. The heat-flow picture (coherence check)

Under the De Bruijn–Newman flow $\Xi_t$, zeros move; a conjugate pair collides on the axis and splits into two real zeros as $t$ increases. In the present language: **an acnode-type node of the value curve converts to a crunode-type node through a real tacnode** (σ-swapped ruling pair → σ-fixed ruling of multiplicity 2 → two σ-fixed rulings); in the quotient $Y$, an $S^2$ component collides with the $\mathbb{RP}^2$ boundary stratum and splits into two $\mathbb{RP}^2$'s. $\Lambda\ge0$ (Rodgers–Tao) says $\Xi=\Xi_0$ sits exactly at the closure of the acnode-free region — every discriminating functional must therefore be merely *non-strictly* positive in the limit, which is what the $j_\ell(\lambda y_0)^2$-type sphere terms in (5a) exhibit as $y_0\to0$. The framework is consistent with the known hard boundary of the problem.

## 7. Status and next actions

Established this session: explicit lift $\tilde f=F\times\mathrm{id}$ on the incidence quadric $(Q,\rho)$, with a self-contained proof that $Q$ is the maximal holomorphic home (resolving the Thol rigidity tension); explicit Plücker data; the discriminating invariant (σ-equivariant type of zero-divisor components; equivalently crunode/acnode; equivalently $\mathbb{RP}^2$/$S^2$ in $Y$); proof that homology class *and* quaternionic winding number both weight spheres by exactly 2 (the no-go extends to the nonlinear degree); three analytic generalizations with the graded Laguerre hierarchy (5a) as the recommended spearhead.

Next concrete steps, in order:
1. **Numerics:** implement $\mathcal{E}_\ell$ (or the simplest sphere-tagged quadratic functional) for (i) $\Xi$ via its cosine transform, (ii) Davenport–Heilbronn, (iii) toy LP functions with one implanted conjugate pair; verify the sphere terms flip sign/degrade positivity as predicted, and measure sensitivity vs. radius (the $j_\ell(\lambda y_0)$ scaling).
2. **Analysis:** express $\mathcal{E}_\ell$ through the explicit formula (Weil pairing with Bessel-transformed test functions $\;\widehat{h}\sim j_\ell$-family); determine which classical positivity (Weil cone) the $\ell=0$ case reduces to, and what is genuinely new for $\ell\ge1$.
3. **Geometry:** compute the degenerate-curve system $D$ for $\Xi$ numerically to moderate height (ties (5b) to (5a): the sphere terms live where $D$ leaves the axis).
