# The Zero-Sphere Program: a Quaternionic–Twistor Framework for the Riemann Hypothesis

**Edward B. Baker III** (edwardbaker86@gmail.com)
*Program document, August 2026. Prepared with substantial AI research assistance (Claude, Anthropic); every claim below is marked with its verification status. This is a research **program**, not a claimed proof. Underlying single-author work: 2015–2026 manuscripts listed in the source manifest (§12).*

**Verification legend.** [K] known — cited literature. [P] proved in the source memos at working-note rigor (proof or complete sketch; independently checkable in minutes-to-hours). [C] certified numerically (code included; reproduces in minutes). [O] open.

---

## 1. Summary

Rotate the critical line to the real axis: $s = \tfrac12 + iz$, $\Xi(z) := \xi(\tfrac12 + iz)$, an even entire function of order 1, real on $\mathbb{R}$; RH says all its zeros are real. $\Xi$ extends canonically to the quaternions as an *intrinsic slice regular* function, and by the zero-structure theorem for such functions its zero set consists of isolated real points and isolated round 2-spheres: **RH $\iff$ the quaternionic $\Xi$ has no zero spheres.** The program studies this sphere/point dichotomy through three lenses that turn out to be the same lens: (i) *twistor geometry* — zeros become components of a divisor on a quadric with a real structure $\sigma$, and RH says every component is individually $\sigma$-invariant; (ii) *positivity* — sphere-detecting inequality hierarchies graded by spherical Bessel tags, whose bottom rung is the classical Laguerre inequality; (iii) *the explicit formula* — a certified, prime-computable quadratic form whose exponential growth rate in its frequency window equals twice the largest sphere radius. The organizing statement (§8): the zero set carries two involutions, $\rho \mapsto 1-\rho$ (holomorphic; the explicit formula sees it) and $\rho \mapsto \bar\rho$ (antiholomorphic; defines the spheres), and **RH is the statement that they agree on zeros**. The program's central open problem is to import the second involution into explicit-formula arithmetic. The framework also proves two no-go results delimiting what cannot work, passes the two mandatory hardness checks (Davenport–Heilbronn; De Bruijn–Newman), and offers a self-contained, mathlib-scale formalization target that is valuable independently of RH.

## 2. The reformulation

Let $\mathbb{H}$ be the quaternions, $\mathbb{S} = \{J \in \mathbb{H}: J^2 = -1\}$ the sphere of imaginary units. A function $f$ on an axially symmetric domain is *slice regular* (Gentili–Struppa [K]) if holomorphic on each slice $\mathbb{C}_J = \mathbb{R} + J\mathbb{R}$; it is *intrinsic* if its power series has real coefficients, equivalently $f(x + yJ) = \alpha(x,y) + J\beta(x,y)$ with $\alpha + i\beta$ holomorphic and real on $\mathbb{R}$. Intrinsic slice regular functions form a commutative real algebra under **pointwise** operations, restricting on each slice to the ordinary complex algebra [K]. Since $\Xi$ is entire with real, even Taylor coefficients, $\Xi(q) = \sum c_{2n} q^{2n}$ is entire intrinsic; equivalently, Riemann's own formula extends verbatim:
$$\Xi(q) = 4\int_0^\infty \Phi(u)\cos(qu)\,du,\qquad \Phi(u) = \sum_{n\ge1}\big(2\pi^2 n^4 e^{9u/2} - 3\pi n^2 e^{5u/2}\big)e^{-\pi n^2 e^{2u}} > 0,$$
absolutely convergent on all of $\mathbb{H}$ [P; constant 4 certified against $\xi(\tfrac12+ix)$ to 10 digits, C].

**Zero structure** [K: Gentili–Stoppato]: the zero set of a nonzero slice regular function is a union of isolated points and isolated spheres $x + y\,\mathbb{S}$. For intrinsic $\Xi$: real zeros of the complex $\Xi$ give points; conjugate pairs $a \pm iy$ give the sphere $a + y\,\mathbb{S}$. Hence:

> **Reformulation.** RH $\iff$ the zero set of $\Xi: \mathbb{H} \to \mathbb{H}$ contains no 2-sphere.

This is a relabeling, not progress; its value is the structures it makes available (§§3–8). Historical note: the extension map here is exactly the rotation map $R$ of [Baker 2015, eq. 2.5]; that paper applied $\Delta \circ R$ (Fueter's theorem) to land in Fueter-regular functions, losing multiplicativity. The present program stops at $R$: the slice regular class satisfies all the desiderata (algebra closure, rigidity, one-slice determination) that motivated a decade-long search through twistor function theory.

## 3. Twistor geometry: where the rotational class lives

Coordinates as in [Baker, *Twistor holomorphicity*]: twistor space $\mathbb{CP}^3 \to \mathbb{HP}^1$, fiber coordinate $\eta \in \mathbb{S}$, real structure $\sigma$ (fixed-point-free, antiholomorphic; fibers = $\sigma$-invariant lines). Computations [P, memo 2]:

1. The lines $L_\zeta = \{(x + \eta y, \eta)\}$, $\zeta = x+iy$ (lifts of the spheres $x + y\mathbb{S}$; fibers when $y = 0$) have Plücker image a conic, and sweep the smooth **incidence quadric** $Q = \{(q,\eta): q \in \mathbb{C}_\eta\} \cong \mathbb{CP}^1_\zeta \times \mathbb{CP}^1_w$, with second ruling the fixed-complex-structure slices. The real structure restricts to $\rho(\zeta, w) = (\bar\zeta, -1/\bar w)$.
2. An intrinsic slice regular $f$ (stem function $F$) lifts to $\tilde f = F \times \mathrm{id}: Q \to Q$, holomorphic and $\rho$-equivariant; and $Q$ is the **maximal** holomorphic home — no extension to a neighborhood in $\mathbb{CP}^3$ exists unless $f$ is Möbius. This resolves, sharply, the rigidity tension of [Baker, *Twistor holomorphicity*, Prop. 3.1] (degree-one fiberwise maps of all of twistor space are Möbius): the rotational function class lives *on the incidence quadric*, not on twistor space.
3. The zero divisor of $\tilde\Xi$ is a union of first-ruling lines, one per zero. **The discriminating invariant is equivariant, not homological**: a real zero gives a $\sigma$-*fixed* component (a twistor fiber); a zero sphere gives a $\sigma$-*swapped pair* of components. Homology classes are identical. In the free quotient $Q/\sigma$: real zeros descend to $\mathbb{RP}^2$'s, spheres to $S^2$'s, so **RH $\iff$ every component of the zero locus in $Q/\sigma$ is nonorientable** [P].

Context [K]: the twistor lift of slice regular functions and the induced orthogonal complex structures are due to Gentili–Salamon–Stoppato (JEMS 2014), with the ruled-surface geometry developed by Altavilla–Sarfatti (Math. Z. 2019); the OCS rigidity/removability theory is Salamon–Viaclovsky (Math. Ann. 2009). The specific product-form lift on $Q$, its maximality, and the equivariant-divisor formulation of RH are, to our knowledge, new [P/O — literature check invited].

## 4. Two no-go results (what cannot work)

1. **Linear no-go** [P]: the extension maps ($R$ and the Fueter-side hierarchy $Q_\ell$ of [Baker 2015]) are $\mathbb{R}$-linear and injective in the complex input, so every continuous linear functional of any such extension is a linear functional of the complex $\Xi$ — no rotationally symmetric linear pairing can distinguish on-axis from off-axis zeros. This formalizes and generalizes the negative result of [Baker 2015, §4].
2. **Degree no-go** [P]: the quaternionic winding number (Brouwer degree of $f/|f|$ on 3-manifolds; the natural 4D argument principle) weights a real zero of multiplicity $m$ by $m$ and a zero sphere by $2m$ — exactly the complex count. Deformation-invariant integer counts cannot detect spheres (as they must not, by hardness check 1 below).

Consequence: any successful discriminant must be nonlinear **and** finer than homology — equivariant (§3), positivity-type (§6), or spectral.

## 5. Mandatory hardness checks

Any proposed sphere-excluding mechanism must pass both:

1. **Davenport–Heilbronn** [K/C]: $\Xi_{DH}(z) = \Lambda_{DH}(\tfrac12+iz)$ is even, real, entire, order 1, functional equation — and has genuine zero spheres; the first three (recomputed here, matching Spira): centers/radii $(85.6993, 0.3085)$, $(114.1633, 0.1508)$, $(166.4793, 0.0744)$. No Euler product. Symmetry + growth alone therefore cannot exclude spheres: the arithmetic input is not optional.
2. **De Bruijn–Newman** [K: $\Lambda \ge 0$, Rodgers–Tao]: under heat flow, spheres shrink to the axis and split into real pairs; $\Xi$ sits exactly at the boundary of the sphere-free regime. Any true criterion degrades only *polynomially or worse* as sphere radius $y_0 \to 0$; a soft argument stable under small perturbations proves too much and is wrong.

## 6. The positivity hierarchy (unitary/graded family)

The axis-visible certificate that zeros are real is a positivity: $-(\log\Xi)''(x) = \sum_\rho (x-\rho)^{-2}$, where real zeros contribute positively and a sphere $(a, y_0)$ contributes $2\,\mathrm{Re}\,(x - a - iy_0)^{-2} < 0$ exactly on $|x - a| < y_0$. The Laguerre inequality $L_1 = \Xi'^2 - \Xi\Xi'' \ge 0$ is thus the sphere/point dichotomy's bottom certificate; the generalized Laguerre family characterizes the Laguerre–Pólya class, so the full family is equivalent to RH [K: Csordas–Varga school].

**Numerics** [C]: $L_1[\Xi] > 0$ with relative margin $0.173$ on $[0,52]$; $L_1[\Xi_{DH}] < 0$ precisely inside the predicted windows $|x-a| < y_0$ at both computed spheres (e.g. observed $[85.417, 85.982]$ vs. predicted $[85.391, 86.008]$, the shaving accounted for by neighboring on-line zeros); positive on sphere-free stretches.

**Grading** [defined here; C]: sector functionals with spherical Bessel tags,
$\mathcal{E}_\ell = \int \big|\sum_\rho j_\ell(\lambda y_\rho)e^{i\lambda a_\rho}\big|^2 w(\lambda)\,d\lambda$:
real zeros vanish identically from every $\ell \ge 1$ sector ($j_\ell(0) = 0$); a sphere of radius $y_0$ enters sector $\ell$ at order $y_0^{2\ell}$ (measured log–log slopes 2.000, 4.000, 6.000 for $\ell = 1,2,3$; DH's three real spheres fit the $y_0^2$ law in $\ell=1$ to 2%). RH $\iff$ all $\ell \ge 1$ sectors vanish. These tags arise as the spherical-harmonic content of the rotationally extended zero set — the $B_\pm$/Bessel machinery of [Baker 2015, §§5–8] put to quadratic use, as the linear no-go demands.

## 7. The explicit-formula bridge (analytic family)

**Certified Guinand–Weil formula** [K formula; C certification]: with $\rho = \tfrac12 + i\gamma$, $h$ even, holomorphic in $|\mathrm{Im}| \le \tfrac12+\varepsilon$, $g = \widehat h/2\pi$:
$$\sum_\gamma h(\gamma) = h(\tfrac i2) + h(-\tfrac i2) + \frac{1}{2\pi}\int h(t)\big[\mathrm{Re}\,\psi(\tfrac14 + \tfrac{it}{2}) - \log\pi\big]dt - 2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(\log n),$$
verified zero-side vs. prime-side to $10^{-8}$–$10^{-10}$ on a Gaussian-modulated family (250 zeros; five $(c,\lambda)$ configurations).

**The quadratic form**: $Z(c,\lambda) = \sum_\gamma e^{i\lambda(\gamma-c)}e^{-(\gamma-c)^2/2\sigma^2} + (\gamma \to -\gamma)$ is unconditionally prime-computable, with the frequency $\lambda$ equal to the logarithmic prime scale ($\log n \approx \lambda$). Zero-side [P]: real zeros contribute boundedly to $|Z(c,\lambda)|^2$ uniformly in $\lambda$; a sphere $(a, y_0)$ contributes $2\cosh(2\lambda y_0)e^{-((a-c)^2 - y_0^2)/\sigma^2} + O(1)$. Hence
$$\limsup_{\lambda\to\infty}\frac{\log|Z(c,\lambda)|}{\lambda} = \sup_\rho y_\rho = \Theta - \tfrac12,$$
**RH $\iff$ subexponential growth of $Z$ in $\lambda$ at every window**, and the rate reads off the largest radius. On real data [C]: zeta zeros and DH on-line zeros flat; DH's sphere recovered at fitted rate 0.3085 vs. true 0.30852.

**Graded decomposition of the anomaly** [C; classical Gegenbauer]: $\sinh(2z)/2z = \sum_\ell (2\ell+1)i_\ell(z)^2$ (machine precision) — the anomaly kernel splits over the same quaternionic sectors with *modified* Bessel tags: the analytic ($i_\ell$) and unitary ($j_\ell$) families are Wick rotations of each other, matching at order $y_0^{2\ell}$, the analytic one exponentially amplified once $\lambda y_0 \gtrsim 1$.

**Honest accounting** [P/K]: at the exponential-rate level this is a Gaussian-mollified form of the classical equivalence between zero-free regions and prime-error terms; the wall (radius $y_0$ needs primes to $e^{1/y_0}$) is the old wall with its geometry exposed. Genuinely new leverage, if any, lies below that scale — §9.

## 8. The organizing statement: two involutions

The zero multiset carries the holomorphic involution $\rho \mapsto 1 - \rho$ (functional equation) and the antiholomorphic involution $\rho \mapsto \bar\rho$ (reality; the real structure $\sigma$ of §3). The explicit formula, being analytic in $\gamma$, natively pairs zeros by the first and is blind to the second; the sphere tags of §6 are functions of the conjugate pair $(\gamma, \bar\gamma)$ (e.g. divided differences $\frac{e^{i\lambda\bar\gamma} - e^{i\lambda\gamma}}{-i\lambda(\gamma - \bar\gamma)}$) — *conjugate-paired sums*, a class strictly between Weil-linear and fully quadratic. Sharpest scalar instance: $\sum_\rho \frac{1}{\rho(1-\rho)} = 2 + \gamma_E - \log 4\pi$ is classical; $\sum_\rho \frac{1}{\rho\bar\rho}$ is not prime-computable; the termwise difference vanishes exactly on-line.

> **RH is the statement that the two involutions coincide on the zero set** — arithmetically: functional-equation pairing = conjugation pairing; geometrically (§3): the zero divisor is $\sigma$-invariant component-by-component. The program's central problem is to import the antiholomorphic involution into explicit-formula arithmetic.

## 9. Open problems (ranked; each with its hardness check)

1. **The graded cone.** Does the $i_\ell$-graded decomposition of the Weil-type quadratic form define a positivity cone with better prime-side realizability or better cross-term control than the classical Weil cone? (Must fail for DH — it does, structurally, since DH has no prime side; must degrade polynomially in $y_0$ — it does, $y_0^{2\ell}$.)
2. **Conjugate-paired explicit formulas.** Any unconditional identity for sums $\sum_\gamma F(\gamma, \bar\gamma)$ beyond trivial cases. Even partial results (asymptotics, one-sided bounds) would be new tools with reach beyond this program.
3. **Cross-term calculus.** Quantify the off-diagonal of $|Z|^2$ under RH+GUE vs. unconditionally; determine the minimal sphere radius detectable at prime scale $e^\lambda$ — the precise gap any new idea must close.
4. **Coherent-mode detection.** A sphere contributes a coherent $e^{\pm\lambda y_0}$-asymmetric mode to the pair-correlation field, unlike GUE fluctuation; formulate sphere-detection as matched filtering and test whether coherence buys detection below the $\lambda \sim 1/y_0$ wall.
5. **Equivariant/OCS route.** Local models of the lift and induced orthogonal complex structures at point-zeros vs. sphere-zeros; whether Salamon–Viaclovsky-type removability, combined with growth and the positivity of $\Phi$, constrains $\sigma$-swapped components. (Must not be deformation-soft — check 2 of §5.)
6. **Spectral route.** The zero set of intrinsic $\Xi$ is an axially symmetric set of exactly S-spectrum type (Colombo–Sabadini–Struppa); quaternionic self-adjointness $\Rightarrow$ real S-spectrum. A quaternionic Hilbert–Pólya: natural home, same classical difficulty, possibly better-shaped invariants (de Branges canonical systems are quaternion-sized).

## 10. Formalization targets (for the Lean/mathlib community)

Tier 1 — *self-contained and valuable regardless of RH*: slice regular function basics, the representation formula, the zero-structure theorem, and the reformulation "RH $\iff$ no zero spheres." To our knowledge mathlib has quaternions as a normed algebra but no slice analysis; this would be a new mathlib theory of independent interest, of comparable scope to existing one-variable complex-analysis developments. Tier 2: the incidence-quadric lift and equivariant statements (§3); the two no-go results (§4). Tier 3: the certified explicit formula (§7) — natural continuation of the Loeffler–Stoll zeta/L-function formalization and the PrimeNumberTheoremAnd (Kontorovich–Tao) analytic infrastructure. The numerics (§§6–7) are all reproducible from the included ~400 lines of Python in minutes, providing test oracles for formalized statements.

## 11. What this program is and is not

It is not a proof strategy with a claimed endgame; the no-go results and hardness checks were derived precisely to prevent self-deception, and §7 identifies exactly where the program currently reduces to classical difficulty. It is a coherent reformulation with (i) verified structure theorems locating RH inside equivariant real geometry, (ii) a graded positivity framework whose bottom rung is classical and whose grading is new, (iii) a certified computational pipeline, and (iv) one sharp organizing question (§8) that is genuinely different in shape from the standard formulations and connects two communities (quaternionic/twistor function theory and analytic number theory) that do not currently talk.

## 12. Source manifest

Working memos (included): `RH_program_synthesis.md` (memo 1: program synthesis, function-class analysis, literature); `twistor_lift_computation.md` (memo 2: incidence quadric, lift, equivariant invariant, degree no-go); `memo3_explicit_formula_bridge.md` (memo 3: certified explicit formula, quadratic form, two involutions). Code (included): `xi_lib.py`, `run_experiments.py`, `explicit_formula.py`; figures `lab_results.png`, `bridge_results.png`. Underlying manuscripts (E. B. Baker III): *Quaternionic analysis with applications to the Riemann zeta function* (2015); *Twistor holomorphicity* (2017); *Frustrated conformal transformations and holomorphic maps on ambitwistor space* (2023); *Causal and self-dual morphisms in four complex dimensions* (2024); drafts on ASDYM symmetries and generalized isothermal coordinates (2023–2026).

Key references: Gentili–Struppa (Adv. Math. 2007); Gentili–Stoppato (zeros); Gentili–Salamon–Stoppato (JEMS 2014, arXiv:1205.3513); Salamon–Viaclovsky (Math. Ann. 2009, arXiv:0704.3422); Altavilla–Sarfatti (Math. Z. 2019); Colombo–Sabadini–Struppa (*Entire Slice Regular Functions*; S-spectrum); Csordas–Varga (Laguerre inequalities); Griffin–Ono–Rolen–Zagier (Jensen polynomials); Rodgers–Tao ($\Lambda \ge 0$); Titchmarsh (DH function); Iwaniec–Kowalski (explicit formula); Mason–Woodhouse (*Integrability, Self-Duality, and Twistor Theory*).
