# Isolated Zeros and Transverse Rigidity

**A self-contained brief for the quaternionic / gauge-theoretic approach to RH.**

*Assembled 2026-08-23 from working memos 6–8, `twistor_lift_computation.md`, `appendix_extension_uniqueness.tex`, and the lab code listed in §9. Written to stand alone: nothing below depends on the slice-regular material except where explicitly marked as an inherited constraint. All results are stated with their status (proved / machine-verified / inherited / conjectural).*

---

## 0. Scope, and what was deliberately left out

This document collects everything from the quaternionic RH work that is **not** about slice regular functions, plus the small number of slice-regular results that survive as constraints on what to try next.

The slice-regular investigation was a detour. Its own conclusion was that it could not contribute: the extension carries the same stem on every slice, and that triviality is *forced* — $\mathbb{H}$ has no commutative subalgebra larger than a slice, so $\mathbb{C} \to \mathbb{H}$ cannot do the work that $\mathbb{R} \to \mathbb{C}$ does. Nothing is lost by dropping it.

Three things from that period are load-bearing anyway and are carried here as **inherited constraints** (§6), because they rule out approaches one would otherwise waste time on:

- multiplicative rigidity (§6.1) — kills any functional-calculus-style construction, and its proof assumes no symmetry and no regularity;
- the linear no-go (§6.2) — any discriminating functional must be nonlinear;
- the Vekua trace term (§2.3) — the cleanest instance of the central principle below.

Everything else here is independent of slice regularity.

**The one substantive result of the whole arc is §2**: a structural principle about *where* information about reality of zeros lives in the quaternionic setting, now with four independent derivations and one exact formula. §§3–5 are the negative results that established it. §§6–8 are what to do next.

---

## 1. The strategy

### 1.1 The idea

Let $\Xi$ be the Riemann $\Xi$-function, real entire, with RH equivalent to all its zeros being real. Identify $\mathbb{H}$ with $\mathbb{R}^4$, write $q = x_0 + x_1 i + x_2 j + x_3 k$, $\operatorname{Im} q = q - x_0$, $r = |\operatorname{Im}q|$, and $\mathbb{S} = \{J \in \mathbb{H} : J^2 = -1\}$ the 2-sphere of imaginary units, with $\mathbb{C}_J = \mathbb{R} + J\mathbb{R}$ the **slice** through $J$.

The strategy:

> Find a class $\mathcal{C}$ of functions $\mathbb{H} \to \mathbb{H}$ in which **no member has a 2-sphere in its zero set**. Show that $\Xi$ admits a member of $\mathcal{C}$ that is **rotationally symmetric**. Conclude RH.

The mechanism is that symmetry converts a single off-axis zero into a whole sphere of them: if $F(uq\bar u) = u F(q)\bar u$ for all unit $u$ and $F(a + bI_0) = 0$ with $b \neq 0$, then $F$ vanishes on the entire sphere $a + b\mathbb{S}$, which $\mathcal{C}$ forbids. So all zeros are real.

### 1.2 The logical skeleton

Two observations fix where the difficulty must sit.

**Symmetry cannot be dropped from the argument, only from the class.** Without it, a member of $\mathcal{C}$ extending $\Xi$ from a slice simply has $\Xi$'s non-real zeros as isolated points on that slice; there is no contradiction. The class may be defined without reference to symmetry — that is desirable — but the particular member attached to $\Xi$ must be symmetric.

**For a symmetric member, "isolated zeros" *is* the conclusion, not a step toward it.** An equivariant $F$ has the axial form $F(q) = A(x_0,r) + \omega B(x_0,r)$ with $\omega = \operatorname{Im}q/r$ and $A,B$ real, so its off-axis zero set is $\{A = B = 0\} \times \mathbb{S}$ — a union of spheres, automatically. Membership in a sphere-free class, for a symmetric function, therefore says exactly "no off-axis zeros."

So the entire content sits in **existence**: proving that $\Xi$ has a symmetric member of $\mathcal{C}$.

### 1.3 Proposition 1 (no free lunch)

> **Proposition 1.** Let $\mathcal{C}$ be any class of functions $\mathbb{H} \to \mathbb{H}$ no member of which has a 2-sphere in its zero set. Suppose one proves a theorem of the form
> $$\textit{if } f \textit{ is real entire and has property } P, \textit{ then } f \textit{ admits an equivariant extension in } \mathcal{C}.$$
> Then $P$ implies that $f$ is hyperbolic (all zeros real).

*Proof.* If $f$ has a zero $a + ib$ with $b \neq 0$, any equivariant extension vanishes on the sphere $a + b\mathbb{S}$, contradicting the defining property of $\mathcal{C}$. So no such extension exists, so $P$ fails. $\square$

Consequently **any route of this shape is a hyperbolicity criterion factory, not a proof mechanism.** The geometry contributes exactly the step "symmetric + sphere-free $\Rightarrow$ real", which is a triviality; the whole weight rests on a hypothesis $P$ at least as strong as the conclusion.

This is not fatal — Weil positivity is also "just" a criterion, and in characteristic $p$ the criterion got proved — but it dictates where to aim. A route is worth pursuing only if $P$ is a condition on $\Xi$ that is **independently provable** or at least independently *natural*: a growth bound, a positivity of the Fourier kernel $\Phi$, a self-adjointness, a Fredholm-determinant representation. Any $P$ that amounts to restating hyperbolicity is a relabeling.

### 1.4 Where to aim

The productive form is therefore: a class $\mathcal{C}$ whose **existence theorem is cheap** and whose **isolation property is a theorem**. Nonlinear self-duality is the natural home for that shape — existence from a PDE/twistor correspondence, isolation from a Liouville or energy argument — which is why the Yang–Mills excursion was not a wrong turn. §7 develops this.

---

## 2. The transverse-sphere principle

### 2.1 Statement

> **Principle.** In the quaternionic setting, all information distinguishing real zeros from zero spheres is supported on the directions **transverse to any single slice** — the 2-sphere of complex structures — and vanishes identically on each slice.

**Working test, and the practical payoff of this whole document:**

> **If a proposed condition can be stated slice by slice, it carries no information about reality of zeros.**

This is cheap to apply and it kills proposals before they cost anything. Four independent derivations follow. They share no machinery beyond living on $\mathbb{H}$, which is why the principle should be treated as structural rather than as four coincidences.

### 2.2 Instance A — equivariance makes isolation the conclusion

§1.2 above. Equivariance forces the axial form $A + \omega B$; the sphere directions are quotiented out entirely; what remains is a problem in the half-plane $(x_0, r)$ in which "no off-axis zero" is verbatim hyperbolicity.

### 2.3 Instance B — the Vekua trace term (inherited)

For an equivariant $F = A(x_0,r) + \omega B(x_0,r)$ of class $C^1$ off $\mathbb{R}$, the left Cauchy–Fueter operator $\mathcal{D} = \partial_{x_0} + i\partial_{x_1} + j\partial_{x_2} + k\partial_{x_3}$ acts by

$$\mathcal{D}F = \Big(A_{x_0} - B_r - \frac{2}{r}B\Big) + \omega\,(A_r + B_{x_0}).$$

The coefficient $2$ in $-\tfrac2r B$ is the **transverse dimension count** — the trace of the two directions the symmetry removed. Holomorphic data on a slice satisfies the *uncorrected* Cauchy–Riemann system $A_{x_0} = B_r$, $A_r = -B_{x_0}$. Subtracting the two systems gives $\tfrac2r B \equiv 0$, hence $B \equiv 0$, hence $F$ constant:

> **No nonconstant holomorphic function admits an equivariant Fueter-regular extension.** Posed as a boundary-value problem, the equivariant extension problem into $\ker\mathcal{D}$ is *empty*.

Two lessons. First, the transverse directions are the only place the obstruction lives — it is literally the trace over them. Second, this is a **nonexistence** result, not a uniqueness one: it is the first instance of the trade-off in §3.

*Practical use:* for any candidate class defined by a linear PDE, write the equivariant reduction and check whether the $1/r$ trace term can be absorbed. If not, the symmetric member does not exist. This is a five-minute test.

### 2.4 Instance C — the $\sigma$-type of divisor components

On the incidence quadric $Q \cong \mathbb{CP}^1_\zeta \times \mathbb{CP}^1_w$ (the locus of points paired with their own slice's complex structure), with real structure $\rho(\zeta, w) = (\bar\zeta, -1/\bar w)$, the zero divisor of a lifted real entire function decomposes into components indexed by the zeros. Homologically nothing distinguishes the cases: two real zeros and one conjugate pair both give class $2[\text{ruling}]$. What differs is the **action of the real structure on the components**: real zeros give $\sigma$-invariant components (twistor fibres, descending to $\mathbb{RP}^2$ in the quotient $Y = Q/\sigma$), conjugate pairs give $\sigma$-swapped pairs (descending to $S^2$). So

$$\text{RH} \iff \text{every component of the zero locus of } \tilde\Xi \text{ in } Y \text{ is nonorientable.}$$

Equivalently, in the value-curve picture: real zeros are crunode-type real nodes, conjugate pairs are acnode-type. The invariant is not homological and not a deformation invariant — it changes exactly when zeros collide on the axis, which is the correct behaviour (see §6.3).

The relevant point for the principle: the invariant is an equivariance property under the antipodal map on the **fibre sphere**, i.e. it is a statement about the sphere directions, invisible on any fixed $w$.

### 2.5 Instance D — the exact deficit $r^2 - t^2$

This is the sharpest form, and it is a formula rather than a mechanism. It arises in the ADHM family of §4, where the following holds exactly.

Let $T_0, S$ be commuting real symmetric $k\times k$ matrices, jointly diagonalised with eigenvalues $\tau_j, \sigma_j$; let $e \in \mathbb{R}^3$ be a unit vector with associated imaginary unit and slice $\Pi_e = \{x_0 + y e\}$; and set

$$t = \langle \operatorname{Im}q,\, e\rangle, \qquad r = |\operatorname{Im}q|, \qquad B_j = (x_0-\tau_j)^2 + r^2 + \sigma_j^2 .$$

Then the geometric object's determinant and the target polynomial are

$$\det M(q) = \prod_j (B_j - 2t\sigma_j), \qquad P_p(q) = \prod_j (B_j - 2r\sigma_j),$$

**differing only in $t$ versus $r$.** Pairing conjugate roots ($\sigma \mapsto -\sigma$) turns each into a product over pairs of $B^2 - 4s\sigma^2$ with $s = t^2$ on the left and $s = r^2$ on the right, and

$$B^2 - 4r^2\sigma^2 = \big((x_0-\tau)^2 + (r-\sigma)^2\big)\big((x_0-\tau)^2 + (r+\sigma)^2\big) \ \ge\ 0,$$

so every factor is positive and strictly decreasing in $s$ on $[0, r^2]$. Cauchy–Schwarz gives $t^2 \le r^2$ **with equality exactly when $\operatorname{Im}q \parallel e$, i.e. exactly on $\Pi_e$.** Hence

$$\boxed{\ \det M(q) \ \ge\ P_p(q) \ \text{ on all of } \mathbb{H}, \text{ with equality exactly on } \Pi_e \cup \{S = 0\}.\ }$$

The discriminant is $r^2 - t^2$, weighted by the $\sigma_j$ — the imaginary parts of the zeros, which is what RH is about. A slice is precisely the equality locus of a Cauchy–Schwarz inequality. So a one-slice condition is **blind by construction**, not merely weak.

*Verified:* formula error $\sim 10^{-14}$ over 4000 random points of $\mathbb{H}$ per case; minimum deficit $+2.6\times10^{-3}$ for $z^2+1$, $+6.9\times10^{-3}$ for $(z-1)((z+2)^2+9)$, $+3.0\times10^{-4}$ for the memo-5 quartic; fraction of points with positive deficit $1.000$ in every non-hyperbolic case and $0.000$ in hyperbolic ones. Independent exact rational check over 4000 configurations up to $k=8$: zero violations.

### 2.6 What the principle rules out

- Any condition of the form "the object restricts to $\Xi$ on a slice", however the object is defined. (Proved for the ADHM family in §4.5; the principle predicts it generally.)
- Any condition imposed on a fixed complex structure.
- Any invariant computed from one 2-plane of data — including "the real axis of a second slice", since $\Pi_e \cap \Pi_{e'} = \mathbb{R}$ for every $e'$.

And it sharpens the target: whatever the discriminating structure is, it must be evaluated on at least one point genuinely off any single slice — and, by §6.3, must not be a deformation invariant.

---

## 3. The rigidity / existence trade-off

> **Observed regularity.** Across the classes tried, the constraint that forces zero isolation and the constraint that destroys existence of the symmetric member are *the same constraint*. There is no intermediate regime.

Three instances, with nothing in common but the ambient $\mathbb{H}$:

1. **Fueter/Vekua** (§2.3). Class rigid enough to be interesting; equivariant member does not exist at all (nonconstant).
2. **ADHM matching** (§4.4). Class genuinely noncommutative and carrying structural positivity; the matching condition collapses the data onto its commutative real locus, and hyperbolicity becomes the spectral theorem.
3. **Totally-real complexification** (§5). Isolation is *free* (Stein), existence and uniqueness both hold, no symmetry assumed — and then the only available symmetry hypothesis is unsatisfiable.

In case 3 the trade-off appears in its purest form, since that class was constructed specifically to have cheap existence. That is the strongest evidence that the trade-off is structural.

**Quantitatively** (from §2.5): in the ADHM family, one slice gives no constraint and one slice plus a single point gives total collapse. Constraint and collapse are driven by the same quantity $r^2 - t^2$, so they switch on together.

---

## 4. Gauge theory: the ADHM results

### 4.1 Setup and conventions

Atiyah's quaternionic normal form for charge-$k$ $SU(2)$ ADHM data:

$$\Delta(q) = \begin{pmatrix} T - q I_k \\ \lambda\end{pmatrix}, \qquad T \in \mathbb{H}^{k\times k},\ \lambda \in \mathbb{H}^{1\times k},$$

with the **ADHM condition** that $\Delta^\dagger\Delta$ be real, and **regularity** — the datum is a genuine instanton — the condition that $\Delta^\dagger\Delta$ also be nonsingular for every $q \in \mathbb{H}$. That second condition is precisely *no real jumping lines*, so the real jumping locus is exactly $Z(\det \Delta^\dagger\Delta) \subset \mathbb{H}$.

The **dictionary** under test: for a monic real $p$ of degree $k$, the zero set of the rotational extension of $p$ (real roots as points, conjugate pairs as 2-spheres) is exactly the zero set of

$$P_p(q) := p(x_0 + ir)\,p(x_0 - ir) = \prod_m\big((x_0-\rho_m)^2 + r^2\big).$$

Both sides are canonical objects of their theories; nothing was reverse-engineered.

Why ADHM at all: it was the one candidate with the algebraic shape that Weil's argument needs and that the commutative trace-form route lacked — a noncommutative algebra with a positive involution and positivity supplied structurally.

### 4.2 Proposition 2 — what reality forces

Machine-derived symbolically at $k = 2, 3$:

> $\Delta^\dagger\Delta$ is real for all $q$ **iff** (i) all four real blocks $T_a$ are **symmetric**, and (ii) the nonlinear equations
> $$[T_0, T_a] - \varepsilon_{abc}[T_b, T_c] + \operatorname{Im}_a(\lambda^\dagger\lambda) = 0, \qquad a = 1,2,3$$
> hold (convention: for $a$, take $\{b,c\} = \{1,2,3\}\setminus\{a\}$ with $b<c$ and $\varepsilon_{abc}$ the sign; so $a{=}1 \to -[T_2,T_3]$, $a{=}2 \to +[T_1,T_3]$, $a{=}3 \to -[T_1,T_2]$).
> And then
> $$\Delta^\dagger\Delta = M(q) = C + |q|^2 I - 2\sum_{a=0}^{3} x_a T_a, \qquad C = \sum_a T_a^2 + \operatorname{Re}(\lambda^\dagger\lambda) \succeq 0 .$$

$C$ is a sum of squares of symmetric matrices plus a Gram matrix: **the positivity is automatic.** Note also that (i) makes $T$ quaternionic *symmetric* ($T^{\mathsf T} = T$), **not** quaternionic Hermitian ($T^\dagger = T$) — a distinction that matters in §4.7.

### 4.3 Proposition 3 — noncommutativity is available

Exact rational witness at $k=2$: $T_0 = \begin{pmatrix}0&1\\1&0\end{pmatrix}$, $T_1 = \operatorname{diag}(1,-1)$, $T_2 = T_3 = 0$, $\lambda = (1, 2i)$ satisfies all three ADHM equations exactly, with $[T_0,T_1] = \begin{pmatrix}0&-2\\2&0\end{pmatrix} \neq 0$. (With $\lambda = 0$ and $k=2$ the Plücker relation forces all commutators to vanish, so the imaginary part of the $\lambda$-Gram is the source of noncommutativity at low charge.)

Census: solving the ADHM equations alone from 120 random starts gives 120/120 exact solutions at $k = 2,3,4$, with largest normalised commutator $\max_{ab}\|[T_a,T_b]\|/\|T\|^2$ equal to $1.453,\ 1.611,\ 1.360$. The noncommutative locus is generic, not a curiosity.

### 4.4 Theorem 4 — matching rigidity

> **Theorem.** Let $\Delta^\dagger\Delta$ be real and suppose $\det(\Delta^\dagger\Delta)(q) = P_p(q)$ identically on $\mathbb{H}$, for a monic real $p$ of degree $k \ge 1$. Then $\lambda = 0$, $T_1 = T_2 = T_3 = 0$, $T = T_0$ is real symmetric, and $p = \det(zI - T_0)$. In particular **$p$ is hyperbolic**.

*Proof.* Restrict $q$ to a slice $\Pi_e$, continue $y \to i\eta$, and set $u = x_0 + \eta$, $v = x_0 - \eta$; with $N = T_0 + iT_e$, $T_e = \sum_{a\ge1}e_aT_a$, the identity becomes

$$\det(uv\,I - uN - v\bar N + C) = p(u)\,p(v).$$

The $u^k$ coefficient gives $p(v) = \det(vI - N)$ (so $p$ is the characteristic polynomial of $T_0 + iT_e$ for every unit $e$). The $u^{k-1}v^{k-1}$ coefficient of $\det(uvI + uB_1 + vB_2 + B_3)$ is $\operatorname{tr}B_3 + \operatorname{tr}B_1\operatorname{tr}B_2 - \operatorname{tr}(B_1B_2)$, giving

$$\operatorname{tr}C = \operatorname{tr}(N\bar N) = \operatorname{tr}T_0^2 + \operatorname{tr}T_e^2 \qquad \text{for every unit } e.$$

The left side is $e$-independent, so the quadratic form $e \mapsto \operatorname{tr}T_e^2 = \sum_{ab}e_ae_b\operatorname{tr}(T_aT_b)$ is constant on $S^2$, forcing $\operatorname{tr}(T_aT_b) = \kappa\delta_{ab}$ and $\operatorname{tr}T_e^2 = \kappa$. But $\operatorname{tr}C = \operatorname{tr}T_0^2 + 3\kappa + \|\lambda\|^2$, so $2\kappa + \|\lambda\|^2 = 0$ with both terms non-negative: $\kappa = 0$, $\lambda = 0$, and $\operatorname{tr}T_a^2 = 0$ for a real symmetric matrix forces $T_a = 0$. Then $C = T_0^2$ and $\det M = \prod_j((x_0-\tau_j)^2 + r^2)$ with $\tau_j$ real. $\square$

Three points about the proof. It uses **only the linear part** of the reality condition (block symmetry) — not the nonlinear ADHM equations, and not even $C \succeq 0$; symmetry is load-bearing in exactly one place, $\kappa = \|T_1\|_F^2 \ge 0$. Summing over $e = i,j,k$ suffices, so three slices, not the sphere. And $k \ge 2$ is not needed.

*Verification:* every step symbolic or numeric; an exact ideal-membership certificate at $k=2$ for symbolic monic $p$ (modulo the affine-linear coefficient equations, $2\sum_{a\ge1}\operatorname{tr}T_a^2 + 3\|\lambda\|^2$ is a rational combination of four of the rest); and existence tracking hyperbolicity on all 12 test cases (§9.2), including a correct NO for the memo-5 quartic.

### 4.5 Theorem 5 — the one-slice relaxation, characterised

> **Theorem.** With $\Delta^\dagger\Delta$ real, the relaxed condition $\det(\Delta^\dagger\Delta) = P_p$ **on a single slice $\Pi_e$** holds iff
> $$\lambda = 0,\quad T_a = e_aS\ (a=1,2,3)\ \text{with } S := T_e \text{ real symmetric},\quad [T_0,S] = 0,\quad C = T_0^2 + S^2,$$
> together with invariance of the joint spectrum $\{(\tau_j,\sigma_j)\}$ of $(T_0,S)$ under $\sigma \mapsto -\sigma$; and then $p(v) = \prod_j(v - \tau_j - i\sigma_j)$.
>
> **Every** real monic $p$ of degree $k$ arises. The relaxed condition has no discriminating power, and the data is forced commutative and $\mathbb{C}_e$-valued.

*Proof of the forward direction.* The trace relation of §4.4 holds for the single $e$. With $g_{ab} = \operatorname{tr}(T_aT_b)$ ($a,b\ge1$) the Frobenius Gram matrix, $g \succeq 0$, it reads $\operatorname{tr}g + \|\lambda\|^2 = e^{\mathsf T}ge \le \lambda_{\max}(g) \le \operatorname{tr}g$, forcing $\lambda = 0$, $\operatorname{rank}g \le 1$ and $e$ a top eigenvector, so $g = \kappa\,ee^{\mathsf T}$; then $\|T_a - e_aT_e\|_F^2 = \kappa e_a^2 - 2\kappa e_a^2 + \kappa e_a^2 = 0$. Substituting into the ADHM equations, $[e_bS, e_cS] = 0$ leaves $e_a[T_0,S] = 0$, and $|e| = 1$ gives $[T_0,S] = 0$. Then $C = T_0^2+S^2 = \bar N N$ and the identity holds exactly. $\square$

The $\sigma$-invariance is needed for sufficiency, since $[T_0,S]=0$ makes the identity read $\bar p(u)p(v)$, which equals $p(u)p(v)$ only when $p$ is real. It forces $\operatorname{tr}S = 0$, and for $k=2$ with non-hyperbolic $p$ forces $T_0$ scalar. Counterexample to the version without it: $k=2$, $T_0 = 0$, $S = \operatorname{diag}(1,2)$ satisfies everything else and matches no real $p$.

Realisability: put real parts of the roots in $T_0$ and imaginary parts in $S$, both diagonal. Verified exactly for $z^2+1$, $z^2+z+1$, $(z-\tfrac12)^2+4$, $(z-1)((z+2)^2+9)$, $((z-1)^2+4)^2$, the memo-5 quartic, $(z^2+1)(z^2+4)$, and all-real $p$; repeated roots, even-multiplicity real roots and odd $k$ all fine.

### 4.6 Proposition 6 — the deficit and the one-point threshold

The formula of §2.5 lives in exactly the family of Theorem 5. Consequences:

- **One slice plus one off-slice point forces hyperbolicity.** Numerically, $p = z^2+1$ with one slice plus one point: best residual $0.42$; one slice alone: $3\times10^{-15}$.
- Two non-parallel slices suffice, for the right reason: $S' = T_{e'} = (e\cdot e')S$ and $e_aS = (e\cdot e')e'_aS$, so $S \neq 0$ forces $e = (e\cdot e')e'$, hence $|e\cdot e'| = 1$ and $e' = \pm e$. Since $\Pi_{-e} = \Pi_e$, the right hypothesis is exactly $e' \neq \pm e$. But this is far from minimal.
- **The forcing is not uniform.** For two slices at angle $\theta$, the best residual attainable by $S \neq 0$ data scales as $O(\theta^2)$: measured $2.1\times10^{-4}$ at $\theta = 10^{-2}$, $2.1\times10^{-8}$ at $10^{-4}$, $2.0\times10^{-14}$ at $10^{-7}$. Any *approximate* condition with tolerance $\varepsilon$ admits non-hyperbolic $p$ once $\varepsilon \gtrsim \theta^2$. See §6.4.

### 4.7 Proposition 7 — the spectrum places no constraint

The most faithful reading of the original programme is that the zero-sphere structure is *native* to quaternionic linear algebra: right-eigenvalue classes of a quaternionic matrix are 2-spheres unless real. So one might hope the ADHM equations force real spectrum, with no matching condition at all.

They do not. Quaternionic **Hermitian** matrices have real spectrum (verified: 200 random Hermitian $3\times3$, $\max|\operatorname{Im}| = 1.4\times10^{-15}$ over all classes), but ADHM reality gives quaternionic **symmetric**, and over 150 admissible data at each of $k = 2,3,4$ the fraction with a non-real class was $1.00$, median $|\operatorname{Im}|/\|T\|$ of $1.41, 1.57, 1.77$. Zero spheres are permitted freely; the class supplies no isolation, hence nothing to contradict.

### 4.8 Reading

Within the family that the matching condition allows, "$p$ hyperbolic" is exactly "$S = 0$", i.e. "$T_0 + iS$ is **self-adjoint**". So the relaxation does not fail into nothing — it lands on the **Hilbert–Pólya statement**, with no new input supplied by the geometry. That is a named destination but not a mechanism, and it is worth noting that the operator route is the one direction not closed by this work.

Also: $\lambda = 0$ in both Theorem 4 and Theorem 5 means the last row of $\Delta$ vanishes, so the matched data is not a *regular* ADHM datum — it sits outside the instanton moduli space proper, not merely on its commutative locus. Expected, since a nonempty jumping locus is what was requested, but it means the objects produced are degenerate as gauge theory.

---

## 5. The totally-real complexification

This section corrects an error in the earlier work and supplies the purest instance of §3.

### 5.1 The construction, and a correction

`appendix_extension_uniqueness.tex`, Remark A.7, asserts that uniqueness of an extension from a slice "can only come from symmetry or from holomorphic geometry upstairs — never from ellipticity alone", on the grounds that a slice has codimension two, is polar in $\mathbb{R}^4$, and is massively underdetermined as Cauchy data.

**That is false as stated** (recorded separately in `appendix_ERRATA.md`, since the appendix is listed elsewhere as a possible standalone artifact and must not be circulated with the remark as printed). The argument silently fixes the complex structure for which the slice is a *complex line*. But $\mathbb{H}$ carries a 2-sphere of compatible complex structures. Take $J_\eta(q) := q\eta$ for a unit imaginary $\eta$; if $I_0 \perp \eta$ then $\mathbb{C}_{I_0} = \operatorname{span}\{1, I_0\}$ is **maximally totally real** in $(\mathbb{H}, J_\eta)$ — the same real 2-plane, a complex line for $J_{I_0}$ and totally real for $J_\eta$ (verified: $\langle J(\text{span}), \text{span}\rangle = 0$ exactly in the orthogonal case, $J(\text{span}) = \text{span}$ exactly in the parallel case).

Consequently restriction from $J_\eta$-holomorphic maps to $\mathbb{C}_{I_0}$ is a **bijection** on germs — uniqueness by the identity theorem, existence by complexification of real-analytic data, entire data giving entire extensions. The codimension-two objection fails because $\bar\partial F = 0$ for a map $\mathbb{C}^2 \to \mathbb{C}^2$ is **overdetermined**, not determined.

Concretely with $\eta = i$, $I_0 = j$: write $q = z_1 + z_2 j$ with $z_1, z_2 \in \mathbb{C}_i$; then $qi = (iz_1) + (-iz_2)j$, so $J_i$ acts as $+i$ on $z_1$ and $-i$ on $z_2$, and the holomorphic coordinates are $(z_1, w)$ with $w = \bar z_2$. The slice $\mathbb{C}_j$ is $\{z_1, w \text{ both real}\} = \mathbb{R}^2$.

### 5.2 The zero set, and the invariant

For intrinsic data with stem $G$, in the coordinates $\zeta_\pm = z_1 \pm iw$ the unique extension is

$$A = \tfrac12\big(G(\zeta_+) + G(\zeta_-)\big), \qquad B = \tfrac1{2i}\big(G(\zeta_+) - G(\zeta_-)\big),$$

so $F = 0 \iff G(\zeta_+) = G(\zeta_-) = 0$, i.e.

$$Z(F) = Z(G) \times Z(G) \quad\text{— always discrete.}$$

(Verified: restriction to $\mathbb{C}_j$ reproduces the stem, and $\#Z(F) = \#Z(G)^2$ exactly, for $z^2\pm1$, $(z^2+1)(z-1)$, $z^3-2z$.) And independently of the formula: $\mathbb{C}^2$ is Stein, so no zero set has a compact positive-dimensional component — **no 2-sphere can occur in the zero set of any holomorphic map $\mathbb{C}^2 \to \mathbb{C}^2$.** Isolation is free, with no symmetry assumed.

The reality involution is $\tau(\zeta_+,\zeta_-) = (\bar\zeta_-, \bar\zeta_+)$, whose fixed locus is the slice. Then $Z(F) \cap \mathbb{C}_j = \{(\rho, \bar\rho) : \rho \in Z(G)\}$, and the **diagonal** point $(\rho,\rho)$ is $\tau$-fixed iff $\rho$ is real. In $(z_1,w)$ coordinates the point with $\zeta_\pm = \rho, \rho'$ has $w = (\rho - \rho')/2i$, so $w = 0$ exactly on the diagonal and $(\rho,\bar\rho)$ has $w = \operatorname{Im}\rho$. This is the crunode/acnode invariant of §2.4 in the simplest possible setting.

### 5.3 Why it fails

$R_u(q) = uq\bar u$ is $J_\eta$-holomorphic iff $u\eta\bar u = \eta$, i.e. iff $u \in \mathbb{C}_\eta$: the class is preserved only by the **circle** fixing $\eta$, not by $SO(3)$ (verified: 0 violations in 400 trials for $u \in \mathbb{C}_\eta$, 400/400 violations for generic $u$). The fixed locus of that circle in $\mathbb{H}$ is $\mathbb{C}_\eta$ — a slice, i.e. $\{w = 0\}$.

Now impose the **weakest** hypothesis that still manufactures spheres: invariance of the zero **set** (not the function). A $U(1)$-orbit is connected, $Z(F)$ is discrete, and a connected subset of a discrete set is a point — so every point of $Z(F)$ must be $U(1)$-fixed, i.e. $Z(F) \subseteq \{w=0\}$. But $Z(F) = Z(G)\times Z(G)$ has off-diagonal points with $w = (\rho-\rho')/2i \neq 0$ whenever $|Z(G)| \ge 2$.

> **So the symmetry hypothesis is unsatisfiable for any $G$ of degree $\ge 2$, RH or no RH.** (Verified: $z^2\pm1$ give 2 off-locus points, $(z^2+1)(z-1)$ gives 6, degree 1 gives 0.)

This is the trade-off of §3 in its purest form: a class built to have cheap existence and free isolation, failing at the symmetry step instead. Note the failure is *not* about noncommutativity or about PDE trace terms — it is a dimension count between the zero set and the fixed locus of the available symmetry group. Three unrelated mechanisms, one outcome.

---

## 6. Inherited constraints

Any new proposal must clear these. The first two come from the slice-regular period; they are carried because they constrain the new direction.

### 6.1 Multiplicative rigidity

> Let $T$ assign to every real entire $f$ a function $Tf : \mathbb{H} \to \mathbb{H}$ such that $T$ is a unital $\mathbb{R}$-algebra homomorphism into $\mathbb{H}$-valued functions with **pointwise** operations, $T(\mathrm{id})(q) = q$, and $f \mapsto Tf(q)$ sequentially continuous for locally uniform convergence. Then $T$ is the rotational (slice) extension.

No equivariance, no regularity, no measurability assumed. The reason is Frobenius: for fixed $q$ the image of $\mathrm{ev}_q \circ T$ is a commutative subalgebra of $\mathbb{H}$, hence lies in a single slice, so a multiplicative theory has no choice but to recycle the one-variable stem slice by slice. Dropping the normalisation, every such $T$ is $Tf(q) = \mathsf{R}f(p(q))$ for an arbitrary symbol $p$.

**Consequence:** any class arising as the image of a product-preserving extension *operator* is slice regular. This does not constrain individual functions or classes not defined operator-wise — which is the loophole the rest of this document lives in — but it does kill functional-calculus constructions outright.

*Status: proved; novelty unchecked and plausibly standard (Frobenius plus a character argument).*

### 6.2 The linear no-go

Every operator in the classified family of equivariant *linear* extensions is injective in $f$, and no continuous linear functional of any of them distinguishes on-axis from off-axis zeros. Transferable form: **any discriminating functional must be nonlinear in the extension.**

*Status: inherited; proved in the slice-regular/Fueter setting. The general claim is a reasonable extrapolation, not a theorem.*

### 6.3 Softness — deformation invariants fail

Two independent computations show that natural topological invariants weight a zero sphere by exactly $2$, matching the complex count and therefore carrying no information:

- the homology class of the zero divisor on $Q$: both a pair of real zeros and a conjugate pair give $2[\text{ruling}]$;
- the Brouwer degree of $f/|f|$ on a boundary sphere (the 4D argument principle): local degree $m$ at a real zero of multiplicity $m$, local degree $2m$ at a zero sphere of multiplicity $m$. So the winding counts $r + 2s$ — the complex count again.

Both are **deformation invariants**, which is exactly why they fail: they cannot distinguish $\Xi$ from a Davenport–Heilbronn-style function with implanted conjugate pairs, since the two are connected by a deformation. The $\sigma$-equivariant component type of §2.4 is the minimal refinement that is *not* deformation-invariant — it changes precisely when zeros collide on the axis.

**Screening rule:** if the proposed invariant is deformation-invariant, it is dead on arrival.

### 6.4 "Barely true" — the $\Lambda \ge 0$ constraint

Under the De Bruijn–Newman flow, a conjugate pair collides on the axis and splits into two real zeros as $t$ increases; $\Lambda \ge 0$ (Rodgers–Tao) says $\Xi$ sits exactly at the closure of the sphere-free region. Therefore **every discriminating functional must be merely non-strictly positive in the limit**, degrading continuously to zero as sphere radius $\to 0$.

This is a consistency requirement, and everything in this document satisfies it: the deficit of §2.5 degrades as $r^2 - t^2$ weighted by $\sigma^2$; the ADHM residual for the memo-5 quartic (conjugate pair at $\pm 0.0088$ after normalisation) is $1.0\times10^{-3}$ against $10^{-13}$ for hyperbolic targets; the two-slice forcing degrades as $O(\theta^2)$. A proposal that claims a *uniform* separation is wrong.

### 6.5 Rationality — the wall

The reason geometry contributes nothing until an arithmetic object is constructed.

Weil's argument needs (a) a finite-dimensional **$\mathbb{Q}$**-algebra with a positive anti-involution, (b) a distinguished element not fixed by the involution with an arithmetic identity $FF^\dagger = q\cdot 1$, (c) definiteness of the trace form proved independently, by Hodge index on a $\mathbb{Z}$-lattice. Finite rank is available for $\zeta$ — Connes stresses that RH reduces to positivity of quadratic forms involving finitely many primes. **Rationality is not, and is not the kind of thing one finds by looking harder:** the entries of everything constructed here are moments $M_k = \int_0^\infty \Phi(u)u^k\,du$ of Riemann's kernel. Over $\mathbb{R}$, signature is a complete invariant of a quadratic form, so "realise the trace form geometrically" asks for nothing.

The ADHM work of §4 was aimed at the one part of this that looked circumventable — memo 6's finding that the reality involution on a zero multiset gives a *commutative* algebra with trivial involution, for which "trace form definite" *is* "totally real". Noncommutativity turned out to be available (§4.3) and then annihilated (§4.4). **Rationality was never touched and is untouched.**

---

## 7. Live directions

### 7.1 Transform, not matching

Every dictionary tried has been a **matching**: identify an analytic object with a geometric one by equality of zero loci. Four have now failed for the same structural reason (§§2.4, 4.4, 4.5, 5.3). The model of the alternative is Fueter's theorem: $\Delta \circ \mathsf{R}$ is a **transform**, not an extension — it does not restrict to $f$ anywhere, and that is exactly why it exists where the equivariant extension does not (§2.3).

So the question to ask is not "which geometric object has $\Xi$'s zeros as its degeneracy locus" but "which transform carries $\Xi$'s data to a geometric object, and what does reality of zeros become on the other side". Concretely, in the gauge-theoretic setting the natural candidate is the Penrose/Ward direction: a holomorphic bundle on twistor space built from $\Xi$'s data by an integral transform, with the reality of zeros read off the $\sigma$-type of its jumping divisor rather than imposed on it.

This is the most promising shape and the least developed. It is also where the rationality wall (§6.5) reappears, so temper expectations.

### 7.2 Zero-divisor symmetry in a bundle setting

§5.3 killed zero-*set* symmetry for a class whose zero set is discrete, by a dimension count against the fixed locus of the available circle. That argument does not apply when the object is a **divisor on a bundle** rather than a zero set of a function, because:

- the relevant symmetry acts on the fibre sphere, not on $\mathbb{H}$, so the fixed-locus count is different;
- the divisor can be positive-dimensional without the underlying object being degenerate;
- the invariant of §2.4 is already stated in this language ($\sigma$-type of divisor components), and it is not a deformation invariant, so it clears §6.3.

The concrete open question: is there a construction attaching to $\Xi$ (or to its Jensen truncations) a holomorphic bundle on $Q$ or on $\mathbb{CP}^3$, **not of product type**, whose jumping divisor's $\sigma$-type encodes reality of zeros? The appendix's incidence-rigidity theorem forced the product form only for fibration-compatible *self-maps* of $Q$; bundles and non-product divisors are untouched by it. This is the gap flagged in §0 and it remains open.

### 7.3 Nonlinearity, done properly

The correct statement of why nonlinearity helps is not "nonlinear generalises linear". It is: **nonlinear self-dual systems are equivalent to linear data in an auxiliary space** — Lax pairs downstairs, holomorphic bundles upstairs (Ward). One-variable complex analysis is the rank-one case of that; going nonlinear means going from functions to bundles without leaving the holomorphic category.

Two facts make this the right home for §1.4's shape:

- For linear overdetermined systems, rigidity means the solution space is a small vector space, hence spanned by low-degree polynomials: rigidity and triviality coincide. For nonlinear self-duality, rigidity means finite-dimensional *moduli* with discrete invariants, and the elements are arbitrarily complicated. Charge-$k$ $SU(2)$ instantons on $\mathbb{R}^4$ form an $(8k-3)$-dimensional moduli space; nothing in it is trivial.
- The abelian case is *literally* linear ($U(1)$ ASD is ASD Maxwell) and has **no** finite-energy instantons on $\mathbb{R}^4$ ($H^2(S^4) = 0$). The nonabelian nonlinearity is the entire reason the moduli space is nonempty.

Adjacent target not yet examined: **Hitchin's spectral curves** for monopoles — a curve in mini-twistor space $T\mathbb{P}^1$ with a reality condition $\sigma(S) = S$ plus a vanishing condition $H^0 = 0$ playing the role of nondegeneracy. That is structurally closer to what is wanted than ADHM (a curve with a real structure and a reality condition on it, rather than a determinant to match), and the dictionary "degree-$k$ spectral curve $\leftrightarrow$ degree-$k$ Jensen truncation" is at least type-correct. Untested.

### 7.4 What would count as progress

In order of value:

1. A **transform** (§7.1) rather than a matching, with the reality of zeros appearing as an output rather than an input.
2. A non-product bundle construction (§7.2) whose jumping divisor $\sigma$-type is the invariant, surviving the screening checklist of §8.
3. A property $P$ of $\Xi$ (§1.3) that is analytically natural, provable or at least independently studied, and implies existence of the geometric object. Candidate flavours: positivity/decay conditions on $\Phi$, Fredholm determinant representations, self-adjointness of an associated operator. Note that positivity of $\Phi$ alone is insufficient — there are positive kernels whose cosine transforms have complex zeros.
4. Negative results that close a direction cheaply, using §8. These are worth having; four of the five results in this document are of that kind.

---

## 8. Screening checklist

Apply to any new proposal, in this order. Each step is minutes of work.

1. **Slice-statable?** If the condition can be written slice by slice, it carries no information (§2). Stop.
2. **Deformation-invariant?** If the discriminating invariant is a homology class, a degree, a charge, or a divisor degree, it weights spheres by 2 and fails Davenport–Heilbronn (§6.3). Stop.
3. **Uniform separation claimed?** If the proposal claims a bounded-below discriminant, it contradicts $\Lambda \ge 0$ (§6.4). It is wrong.
4. **Multiplicative?** If the class is the image of a product-preserving extension operator, it is slice regular (§6.1). Stop.
5. **Linear functional?** If the discriminant is a continuous linear functional of the extension, it cannot separate (§6.2). Reformulate quadratically or nonlinearly.
6. **Trace term.** If the class is defined by a linear PDE, write the equivariant reduction $A(x_0,r) + \omega B(x_0,r)$ and check whether the $1/r$ transverse trace term can be absorbed. If not, the symmetric member does not exist (§2.3).
7. **Rigidity/existence.** Ask separately: does the class forbid spheres, and does the symmetric (or symmetric-zero-set) member exist? Expect these to fail together (§3). If a proposal claims both, look for the dimension count between the zero locus and the fixed locus of the available symmetry group (§5.3).
8. **Rationality.** Does anything in the construction supply a $\mathbb{Q}$-structure? If not, the positivity cannot be a theorem in Weil's sense (§6.5). This does not kill a proposal but caps what it can prove.
9. **Circularity.** Write down what the geometric hypothesis is equivalent to. If it is equivalent to hyperbolicity by a spectral theorem or by Sylvester's law, it is a restatement (§4.4, §4.8).

---

## 9. Reference data and reproduction

### 9.1 $\Xi$, its moments, and the Jensen polynomials

$$\Xi(z) = 4\int_0^\infty \Phi(u)\cos(zu)\,du, \qquad \Phi(u) = \sum_{n\ge1}\big(2\pi^2n^4e^{9u/2} - 3\pi n^2 e^{5u/2}\big)e^{-\pi n^2 e^{2u}} .$$

With $M_k = \int_0^\infty \Phi(u)u^k\,du > 0$ and $b_m = 4M_{2m}/(2m)!$, the function $H(w) = \Xi(\sqrt{-w}) = \sum_m b_m w^m$ has positive coefficients and only real negative zeros iff RH. With $\gamma(m) = m!\,b_m$, the Jensen polynomials are

$$J^{d,n}(X) = \sum_{j=0}^d \binom{d}{j}\gamma(n+j)X^j, \qquad \text{RH} \iff \text{every } J^{d,n} \text{ hyperbolic (Pólya)}.$$

Validation to reproduce: $4M_0 = 0.4971207782$ against $\xi(\tfrac12) = 0.4971207174$, relative error $1.2\times10^{-7}$ (quadrature-limited), and all $b_m > 0$.

Caution when using these numerically: the roots of $J^{d,n}$ span many orders of magnitude, so normalise (dividing all roots by the largest modulus is a dilation of $q$ and harmless).

### 9.2 Standard test set

Any new discriminant should be run against all of these. The first group must pass, the second must fail.

**Hyperbolic:** $z^2-1$; $(z-1)(z-2)$; $(z-1)(z-2)(z-3)$; $(z^2-1)(z^2-4)$; $(z-1)^2(z+3)$; $J^{2,0}$, $J^{3,0}$, $J^{3,1}$ of $\Xi$.

**Not hyperbolic:** $z^2+1$; $z^2+z+1$; $(z^2+1)(z-1)$; $(z^2+1)(z^2-1)$; $(z^2+1)(z^2+4)$; $(z-1)((z+2)^2+9)$; and the essential one —

**The memo-5 quartic** $X^4 + 10X^3 + 26X^2 + 22X + 3$. Roots (normalised): $-1$, $-0.254256 \pm 0.008822i$, $-0.025679$. It is *barely* non-hyperbolic, and it **passes** the Newton/first-Turán test ($\sum\rho^2 = e_1^2 - 2e_2 = 1.130 > 0$). Any proposed discriminant that accepts it is at most as strong as Turán, which is a theorem for $\Xi$ and provably strictly weaker than hyperbolicity. This is the single most useful test in the set.

**Reference results.** ADHM matching (§4.4) residuals: hyperbolic cases $10^{-15}$ to $10^{-12}$; non-hyperbolic $0.56$ to $3.04$; memo-5 quartic $1.0\times10^{-3}$ (a near-miss, consistent with §6.4). Existence tracked hyperbolicity on all 12 cases.

### 9.3 Code inventory

| file | contents |
|---|---|
| `lab_qalg.py` | quaternionic matrix algebra over sympy (four real blocks); multiplication table verified |
| `lab_adhm_num.py` | fast numeric layer: ADHM residual, $C$, $\det M$, $P_p$, search; cross-checked against the symbolic layer |
| `lab_adhm_check.py` | §4.2–4.4: reality conditions derived, noncommutativity census, the identity chain, the 12-case existence search |
| `lab_adhm_certificate.py` | exact ideal-membership certificate for Theorem 4 at $k=2$, symbolic monic $p$ |
| `lab_adhm_clifford.py` | the axially-symmetric-but-unmatchable Clifford ansatz (shows axial symmetry is strictly weaker than matching) |
| `lab_adhm_relax.py` | §4.5–4.7 and §2.5: one-slice characterisation, slice ladder, deficit formula, spectrum census |
| `lab_totally_real.py` | §5 in full: the totally real slice, existence/uniqueness, $Z(F) = Z(G)^2$, the $\tau$-invariant, and the unsatisfiability of the symmetry hypothesis |
| `lab_tower_check.py` | §6.5: moments, Jensen polynomials, trace forms and their signatures |
| `lab_lorentzian_test.py` | the Lorentzian $=$ first Turán reduction and the memo-5 counterexample |

Dependencies: `sympy`, `mpmath`, `numpy`, `scipy`. The searches are least-squares from many random starts; hyperbolic targets converge to $10^{-13}$ or better, non-hyperbolic ones plateau, and the gap is ten to twelve orders of magnitude — that gap is the signal, not the absolute residual.

---

## 10. Status and honesty notes

**What is proved.** Proposition 1; Proposition 2 (symbolically at $k=2,3$); Theorem 4 (with an exact certificate at $k=2$ and an independent adversarial reproduction); Theorem 5; Proposition 6's inequality; the results of §5. All were reproduced by independent adversarial review passes, which found no counterexamples and supplied two corrections now incorporated (the sufficiency condition in Theorem 5, and the one-point rather than two-slice threshold in Proposition 6).

**What is empirical.** Proposition 3's census and Proposition 7. Both are strong (100% of samples) but are samples.

**What is inherited and not independently verified here.** §6.1, §6.2, §6.3's degree computation, §2.4.

**Novelty: assume everything here is known until checked.** This is not modesty; it is the lesson of the one novelty check this project actually ran, which found a result it had believed new to be Landau (1912) plus a folklore almost-periodicity argument. Specifically:

- Theorem 4 is a rigidity result about determinantal representations of real polynomials by symmetric pencils. That circle is heavily worked — Lax conjecture, Helton–Vinnikov, hyperbolic polynomials — and ADHM linear algebra has been studied since 1978.
- §5 is elementary several-complex-variables: totally real submanifolds, complexification, Stein-ness. The observation that a slice is totally real for a different complex structure is the kind of thing that is standard in the twistor literature.
- §2.5's deficit formula is the kind of identity that falls out of routine axial-monogenic or Vekua computations.
- §6.1 is Frobenius plus a character argument.

If any of this is to be circulated, each item needs a literature sweep of the same depth as the oscillation-lemma check, and the prior should be that it comes back known.

**Programme status.** The geometric route to RH was closed by the author on 2026-08-23 on effort grounds, after the review recorded in `PROGRAM_CLOSED.md`. Nothing in this document reopens it. The rationality obstruction (§6.5) is the reason, it is independent of every geometric choice, and none of the work since has touched it. This brief exists to make the next attempt — by whoever, whenever — cheaper and better targeted, and in particular to make it cheap to *stop*.

The single most valuable thing here is §8. Four of the five results below it are negative, each closed a direction in under a day, and the checklist is what made that possible.
