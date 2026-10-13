# Relaxing the Matching Condition: the Discriminant Is Exactly $r^2 - t^2$

*Working memo #8 — August 23, 2026. Follows memo 7. Tests whether the ADHM dictionary survives weakening the four-dimensional matching condition to something that only constrains the object on a single slice. Certified by `lab_adhm_relax.py`.*

---

## 0. Result

Memo 7 required the full identity $\det(\Delta^\dagger\Delta) = P_p$ on all of $\mathbb{H}$, which is strong. The natural relaxation — ask only that the object agree with $p$ (or with a Jensen truncation of $\Xi$) **on one slice** — turns out to fail, but for a reason worth having, because it is exact rather than heuristic.

**The one-slice condition is completely characterised and completely contentless.** It forces $\lambda = 0$ and $T_a = e_a S$ for a single real symmetric $S$, with $[T_0,S] = 0$: the data becomes commutative and $\mathbb{C}_e$-valued. And it is satisfiable for **every** real monic $p$ of degree $k$, hyperbolic or not. So the relaxation is worse than the original on both counts at once — it loses all discriminating power *and* still destroys the noncommutativity.

**The reason is quantitative.** Inside that family there is an exact formula. Diagonalise the commuting pair $(T_0, S)$ jointly, with eigenvalues $\tau_j, \sigma_j$, and set $t = \langle \operatorname{Im} q, e\rangle$, $r = |\operatorname{Im} q|$, $B_j = (x_0-\tau_j)^2 + r^2 + \sigma_j^2$. Then

$$\det M(q) = \prod_j (B_j - 2t\sigma_j), \qquad P_p(q) = \prod_j (B_j - 2r\sigma_j).$$

The two differ only in $t$ versus $r$, and Cauchy–Schwarz gives $t^2 \le r^2$ **with equality exactly on the slice $\Pi_e$**. Pairing conjugate roots makes every factor strictly decreasing, so

$$\det M(q) - P_p(q) > 0 \quad\text{for every } q \notin \Pi_e, \text{ whenever } S \neq 0,$$

and $\equiv 0$ when $S = 0$. So **one slice plus a single off-slice point already forces hyperbolicity** — the threshold is not two slices, it is one point. And the entire discriminating information is the quantity $r^2 - t^2$, weighted by the imaginary parts of the roots: supported exactly on the 2-sphere directions transverse to any single slice, and vanishing identically on the slice.

A one-slice condition is therefore not merely weak. It is evaluated precisely on the locus where the discriminant is zero — **blind by construction.**

---

## 1. What the question can mean

Three readings, because ADHM data does not come with a quaternion-valued function to restrict.

The instanton construction produces a bundle and a connection. The canonical real-valued object is $\det(\Delta^\dagger\Delta)$, whose zero locus is the real jumping locus, and that is what memo 7 matched. So:

- **R1 (one slice).** $\det(\Delta^\dagger\Delta) = P_p$ on $\Pi_e = \{x_0 + y e\}$ only.
- **R2 ($m$ slices).** The same on $m$ distinct slices — the interpolation between R1 and memo 7.
- **R3 (spectrum).** Drop matching entirely and use the quaternionic right-eigenvalue classes of $T$, which are 2-spheres unless real. This is the most faithful to the original program's intent: the zero-sphere structure is *native* to quaternionic linear algebra, so a rigidity condition on the spectrum would be exactly the shape wanted.

A fourth, weaker reading — require only that the jumping locus meet the slice in $Z(p)$, as sets rather than as polynomials — is contentless for a trivial reason: $\det M|_{\Pi_e}$ is a non-negative polynomial of degree $2k$ required to vanish at $k$ prescribed points, which any number of things do.

**On $\Xi$ specifically.** $\Xi$ is entire, ADHM data has finite charge $k$, so only the Jensen/Hadamard truncations are in scope. That is not the limitation it looks like, because the R1 answer is *uniform in $k$*: the condition is contentless at every finite charge, so no limiting procedure recovers content.

## 2. R1, completely characterised

> **Proposition.** With $\Delta^\dagger\Delta$ real, R1 holds if and only if
> $$\lambda = 0,\quad T_a = e_a S\ (a=1,2,3)\ \text{with } S := T_e \text{ real symmetric},\quad [T_0,S]=0,\quad C = T_0^2 + S^2,$$
> together with invariance of the joint spectrum $\{(\tau_j,\sigma_j)\}$ of $(T_0,S)$ under $\sigma \mapsto -\sigma$; and then $p(v) = \det(vI - (T_0+iS)) = \prod_j (v - \tau_j - i\sigma_j)$.

*Forward direction.* Restricting to $\Pi_e$ and running memo 7's substitution for this single $e$ gives $\det(uvI - uN - v\bar N + C) = p(u)p(v)$ with $N = T_0 + iT_e$, and the $u^{k-1}v^{k-1}$ coefficient still yields the trace relation $\operatorname{tr} C = \operatorname{tr} T_0^2 + \operatorname{tr} T_e^2$. Let $g_{ab} = \operatorname{tr}(T_aT_b)$ for $a,b\ge1$ — the Frobenius Gram matrix of $T_1,T_2,T_3$, so $g \succeq 0$. Then $\operatorname{tr} T_e^2 = e^{\mathsf T}ge$ and $\sum_{a\ge1}\operatorname{tr}T_a^2 = \operatorname{tr} g$, so the relation reads

$$\operatorname{tr} g + \|\lambda\|^2 = e^{\mathsf T} g e \le \lambda_{\max}(g) \le \operatorname{tr} g,$$

forcing $\lambda = 0$, $\operatorname{rank} g \le 1$, and $e$ a unit top eigenvector, i.e. $g = \kappa\,ee^{\mathsf T}$. Then $\|T_a - e_aT_e\|_F^2 = \kappa e_a^2 - 2\kappa e_a^2 + \kappa e_a^2 = 0$, so $T_a = e_aS$. Substituting into the ADHM equations, $[e_bS, e_cS] = 0$, leaving $e_a[T_0,S] = 0$ for each $a$; since $|e| = 1$ some $e_a \neq 0$, so $[T_0,S] = 0$. Finally $C = T_0^2 + S^2 = \bar N N$ structurally. $\square$

*One extra condition for sufficiency*, missing from my first draft and caught by an adversarial review pass. With $[T_0,S] = 0$ the identity becomes $\det M = \bar p(u)\,p(v)$, which equals $p(u)p(v)$ only if $p$ has real coefficients — hence the $\sigma \mapsto -\sigma$ invariance. Equivalently $\operatorname{tr}(T_0^m S^n) = 0$ for all odd $n$; in particular $\operatorname{tr} S = 0$ is forced, and for $k = 2$ with $p$ non-hyperbolic, $T_0$ must be scalar. Counterexample to the version without it: $k=2$, $T_0 = 0$, $S = \operatorname{diag}(1,2)$ satisfies every other listed condition and matches no real $p$ at all.

**Every real monic $p$ arises.** Pair the conjugate roots, put real parts in $T_0$ and imaginary parts in $S$ — both diagonal, hence commuting, and the pairing supplies the $\sigma$-invariance. Verified exactly (rational arithmetic) for $z^2+1$, $z^2+z+1$, $(z-\tfrac12)^2+4$, $(z-1)((z+2)^2+9)$, $((z-1)^2+4)^2$ (repeated roots), the memo-5 quartic $X^4+10X^3+26X^2+22X+3$, $(z^2+1)(z^2+4)$, and all-real $p$; odd $k$, repeated roots, and even-multiplicity real roots all fine. Numerically, solving R1 from random starts reproduces the characterisation: residuals $\sim 10^{-15}$ with $|\lambda| \sim 10^{-8}$, $\max_a|T_a - e_aS| \sim 10^{-9}$, $\|[T_0,S]\| \sim 10^{-16}$ — and no branch with $\lambda \neq 0$, non-collinear $T_a$, or $[T_0,S]\neq0$ was found at $k = 2,3,4$.

**A degeneration worth recording.** $\lambda = 0$ means the last row of $\Delta$ vanishes, so the matched data is not a *regular* ADHM datum — it sits outside the instanton moduli space proper. Memo 7's matched data has the same defect. It is expected, since a nonempty jumping locus is exactly what we asked for, but it means the objects produced are degenerate as gauge theory, not merely commutative.

## 3. The deficit formula and the real threshold

This is the part worth keeping. Inside the R1 family, with $A_j = (x_0-\tau_j)^2$ and $B_j = A_j + r^2 + \sigma_j^2$:

$$\det M(q) = \prod_j (B_j - 2t\sigma_j), \qquad P_p(q) = \prod_j (B_j - 2r\sigma_j), \qquad t = \langle\operatorname{Im}q, e\rangle,\ r = |\operatorname{Im}q|.$$

Conjugate pairing turns each side into a product over pairs of $B^2 - 4s\sigma^2$ with $s = t^2$ on the left and $s = r^2$ on the right, and

$$B^2 - 4r^2\sigma^2 = \big(A + (r-\sigma)^2\big)\big(A + (r+\sigma)^2\big) \ \ge\ 0,$$

so every factor is positive and strictly decreasing in $s$ on $[0, r^2]$. Since $t^2 \le r^2$ with equality iff $\operatorname{Im}q \parallel e$:

$$\boxed{\ \det M(q) \ \ge\ P_p(q)\ \text{ on all of } \mathbb{H},\ \text{ with equality exactly on } \Pi_e \cup \{S = 0\}.\ }$$

Verified on 4000 random points of $\mathbb{H}$ per case: formula error $\sim 10^{-14}$, minimum deficit $+2.6\times10^{-3}$ ($z^2+1$), $+6.9\times10^{-3}$ ($(z-1)((z+2)^2+9)$), $+3.0\times10^{-4}$ (memo-5 quartic), fraction of points with positive deficit $1.000$ in every non-hyperbolic case and $0.000$ in the hyperbolic ones. An independent check by exact rational arithmetic over 4000 random configurations up to $k=8$ found zero violations.

Three consequences.

**(i) The threshold is one slice plus one point.** A single $q_0 \notin \Pi_e$ forces $S = 0$. Numerically: $p = z^2+1$ with one slice plus one point gives best residual $0.42$ — no solution — against $\sim 10^{-15}$ for one slice alone. Two full slices is sufficient but massively redundant.

**(ii) Two slices always work, for a reason worth writing correctly.** For $e' \not\parallel e$, R1 on both gives $S' = T_{e'} = (e\cdot e')S$ and $e_aS = T_a = (e\cdot e')e'_aS$; if $S \neq 0$ this forces $e = (e\cdot e')e'$, hence $|e\cdot e'| = 1$ and $e' = \pm e$. Since $\Pi_{-e} = \Pi_e$, the right hypothesis is exactly $e' \neq \pm e$.

**(iii) The forcing is not uniform.** For two slices at angle $\theta$, the best residual attainable by $S \neq 0$ data scales as $O(\theta^2)$: measured $2.1\times10^{-4}$ at $\theta = 10^{-2}$, $2.1\times10^{-8}$ at $10^{-4}$, $2.0\times10^{-14}$ at $10^{-7}$. So any *approximate* two-slice condition with tolerance $\varepsilon$ admits non-hyperbolic $p$ as soon as $\varepsilon \gtrsim \theta^2$. This is the same softness the program has met before — cf. the $j_\ell(\lambda y_0) \to 0$ degradation in `twistor_lift_computation.md` §5a and the $\Lambda \ge 0$ discussion in §6.

## 4. R3: the quaternionic spectrum places no reality constraint

ADHM reality makes $T$ quaternionic **symmetric** ($T^{\mathsf T} = T$ entrywise, all four blocks symmetric), not quaternionic **Hermitian** ($T^\dagger = T$, which needs $T_0$ symmetric and $T_{1,2,3}$ antisymmetric). The quaternionic spectral theorem applies to the latter and gives real spectrum — verified, 200 random Hermitian $3\times3$ giving $\max|\operatorname{Im}| = 1.4\times10^{-15}$ over all right-eigenvalue classes. It does not apply to the former.

And in fact: over 150 admissible ADHM data at each of $k = 2,3,4$, the fraction with a non-real right-eigenvalue class was $1.00$, with median $|\operatorname{Im}|/\|T\|$ of $1.41$, $1.57$, $1.77$. So the ADHM equations permit zero spheres freely. The class supplies no isolation, hence nothing for a symmetry argument to contradict.

## 5. Reading the mechanism

Three ways to say the same thing, in increasing order of usefulness.

1. **Abelianisation.** Restricted to one slice, quaternionic ADHM data degenerates to $T_0 + Se$ with $[T_0,S] = 0$ — a $\mathbb{C}_e$-valued *normal* matrix, i.e. ordinary one-variable complex linear algebra. A slice cannot see quaternionic noncommutativity. This is the qualitative version, and it is a sharper instance of the appendix's opening complaint that the slice extension carries "the same stem on every slice".

2. **Landing on Hilbert–Pólya.** Within the R1 family, "$p$ hyperbolic" is exactly "$S = 0$", i.e. "$T_0 + iS$ is self-adjoint". So the relaxation does not fail into nothing — it fails into the Hilbert–Pólya statement, with no new input supplied by the geometry. That is memo 6's "restatement masquerading as mechanism" again, but now with a named destination, and the destination is the one route `PROGRAM_CLOSED.md` records as *not* closed. Which is a useful negative: the geometry contributed nothing on top of an operator-theoretic reformulation that was already available without it.

3. **Blindness by construction, quantitatively.** The whole discriminant is $r^2 - t^2$ — the deviation of $\operatorname{Im}q$ from the slice direction — weighted by the $\sigma_j$, i.e. by the imaginary parts of the roots, which is what RH is about. The slice is precisely the equality locus of the Cauchy–Schwarz inequality $t^2 \le r^2$. So a condition imposed on one slice is evaluated exactly where the discriminant vanishes.

Reading 3 is the transferable one, and it gives a cheap test for any future proposal: **if the condition you are imposing can be stated slice by slice, it carries no information about reality of zeros.** The information lives on the transverse sphere directions and nowhere else.

This is now the fourth independent appearance of that fact in this project — the appendix's $-2B/r$ transverse trace term (Corollary A.11), the twistor note's $\sigma$-type of divisor components (§3), memo 7 §6's rotated-frame degeneracy, and now the exact deficit $r^2 - t^2$. It should be treated as a structural feature of the quaternionic setting rather than four coincidences.

## 6. Assessment

The relaxation was worth testing and the answer is clean: there is no intermediate regime. Below one off-slice point the condition says nothing; at one off-slice point it collapses the data completely. The "sweet spot" — enough constraint to force hyperbolicity, not enough to trivialise — does not exist in this family, and the deficit formula shows why: the constraint and the collapse are driven by the same quantity, so they switch on together.

This is consistent with the original design rather than a surprise about it. The zero-sphere program always relied on rotational symmetry to convert one off-axis zero into a whole sphere — i.e. it always relied on the transverse directions. Removing them and hoping to keep the conclusion was never going to work. What is new is that the trade-off is now exact and quantitative, and that the non-uniformity in (iii) shows it degrades gracefully in exactly the way that makes near-misses (like the memo-5 quartic, whose conjugate pair sits at $\pm0.0088$) hardest to exclude.

`PROGRAM_CLOSED.md` stands. Nothing here bears on the rationality obstruction, which remains the reason geometry contributes nothing until an arithmetic object is constructed.

**Novelty status: unchecked, and assume known.** As with memo 7 §4, the results here are elementary statements about commuting real symmetric pairs and Cauchy–Schwarz. The deficit formula in particular is the kind of thing that falls out of standard axially-symmetric-monogenic or Vekua computations. Do not treat any of it as new.

---

*Certified by `lab_adhm_relax.py`: the complex adjoint and right-eigenvalue classes sanity-checked against the quaternionic spectral theorem; R1 solved numerically at k = 2, 3 and its structure inspected; explicit data exhibited for six non-hyperbolic p and verified to machine precision on the slice; the slice ladder (1 slice, 1 slice + 1 point, 2 generic, 2 orthogonal, 3 slices) searched; the deficit formula verified on 4000 random points of H per case; the spectrum census run at k = 2, 3, 4. The Proposition of §2 and the inequality of §3 are proofs, not computations; both were reproduced by an independent adversarial review pass, which supplied the missing sufficiency condition in §2 and the sharper threshold in §3.*
