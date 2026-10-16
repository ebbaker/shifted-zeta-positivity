# Distributional electric sources, compact returns, and spacetime translations

25 September 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Model exposed: GPT-6 (Codex); exact serving variant and reasoning effort unavailable, not inferred. Starting checkout: `be3e2d55d1423e9cb28c0238fce809e154458813`; the initial working tree was clean. Status: proved deductions from the stated hypotheses, with a substantive self-audit; no independent specialist verification or RH proof is claimed.

## 1. Scope and outcome

This continuation follows the review, its errata, the response, and Claude's reply. It tests exactly two candidates:

1. Distributional sources propagated by the **uncompensated radial electric wave**, using both scalar and adjoint polarizations already present in the reference-color boundary space of the fixed four-dimensional SU(2) slab.
2. Distributional sources covariant under **ordinary spacetime translations** in an explicitly assumed infinite-volume continuum vacuum theory.

The first candidate has an actual positive, state-dependent mixed pairing and a strong spectral-cutoff limit. It fails a new obstruction: an exact Weil source cannot have a nonzero translation that returns to the identity modulo a compact operator. More generally, every nonzero time-step unitary on its source closure must have the entire unit circle as essential spectrum. This is proved directly from the geometric Weil formula, without zero spectra or RH. The weighted radial electric wave has a compact return at parameter $2\pi$, including its adjoint polarization, so no distributional seed repairs it.

The second candidate fails because Lorentz covariance makes the spectrum of any nonzero straight spacetime translation absolutely continuous off the vacuum. A proof by averaging the momentum spectral measure is given below; no asymptotic completeness or particle hypothesis is used. It cannot carry the detecting correlation. This is conditional on the stated continuum representation, and is not a claim about the finite torus state.

These exclude two specified source relations, not all YM source laws. The most substantial constructive identity remains the complete **signed** mixed packet limit. Neither candidate establishes a specifically four-dimensional arithmetic mechanism or a positive Weil norm.

## 2. A short-support mixed test, including its normalization

Keep the conventions and the complete $Q$ in Section 1 of the manuscript. Write $T=-\partial^2+1/4$, $U_tg(x)=g(x-t)$, and $\widehat g(\tau)=\int e^{-i\tau x}g(x)\,dx$. For any nonzero $h\in C_c^\infty(\mathbb R)$, set

\[
h_R(x)=R^{1/2}h(Rx),\qquad f_R=R^{-2}Th_R\in\mathcal D^0,\quad R\ge1.
\tag{1}
\]

These are shrinking-support tests, different from the earlier fixed-support modulations. Put $c_h=\|h''\|_2^2>0$. Direct differentiation and Fourier scaling give

\[
\|f_R\|_2^2=c_h+\frac{\|h'\|_2^2}{2R^2}+\frac{\|h\|_2^2}{16R^4},\qquad
\widehat f_R(\tau)=R^{-5/2}(\tau^2+1/4)\widehat h(\tau/R).
\tag{2}
\]

**Lemma 1 (short-support mixed asymptotics).** With the contact convention of the question,

\[
Q[f_R]=c_h\log R+d_h+o(1),\qquad
d_h=\frac1{2\pi}\int u^4\log\frac{|u|}{2\pi}|\widehat h(u)|^2\,du.
\tag{3}
\]

For fixed $t\ne0$, define $b(t)=\Lambda(a)/\sqrt a$ if $|t|=\log a$ for an integer $a\ge2$, and zero otherwise. Then

\[
Q(f_R,U_tf_R)=-b(t)\|f_R\|_2^2+O_{h,t}(R^{-5}).
\tag{4}
\]

For each fixed $g\in\mathcal D^0$,

\[
Q(f_R,g)=O_{h,g}(R^{-5/2}).
\tag{5}
\]

**Proof.** Once the support diameter is below $\log2$, all prime terms of the diagonal vanish exactly. Its archimedean integral after scaling is

\[
\frac1{2\pi}\int m_+(Ru)(u^2+(4R^2)^{-1})^2|\widehat h(u)|^2\,du.
\]

Use $m_+(v)=\log(|v|/(2\pi))+O(v^{-2})$ for $|v|\ge1$. On $|u|\le1/R$ the integrable $u^4\log|u|$ singularity and the factor $R^{-4}$ make the error tend to zero; on the complement the error is dominated by integrable Schwartz bounds, with an additional $O(R^{-2}\log R)$ from the polynomial factors. This proves (3), including the $-\log(2\pi)c_h$ constant. The finite contact is the original

\[
m_+(0)=-\gamma_E-\pi/2-3\log2-\log\pi.
\]

It has not been freely reset: adding a constant $c$ to the multiplier changes (3) by $c c_h+o(1)$. The obstruction below is insensitive to this finite change, but the exact target and the mixed identities are not.

At fixed $t\ne0$, the two supports are disjoint for large $R$. Their archimedean kernel is exactly $-n_\Gamma(|x-y|)$, smooth on the relevant rectangle. Move both copies of $T$ onto that kernel. Its derivatives there are bounded, and $R^{-4}\|h_R\|_1^2=R^{-5}\|h\|_1^2$. The prime shifts are locally discrete. Eventually only a shift exactly cancelling $t$ can contribute; it contributes the term displayed in (4). This argument also works when $t$ is itself a prime-power separation: it does not incorrectly discard that contact. For (5), the archimedean integral is $O(R^{-5/2})$ by (2) and Schwartz decay of $\widehat g$. Only finitely many primes can meet the fixed enclosing supports, and integration by parts against each smooth translate of $g$ gives the same bound. All pole moments vanish exactly. ∎

## 3. New obstruction: compact returns, including distributional source laws

**Theorem 2.** Suppose a continuous linear law $J:\mathcal D^0\to\mathcal H$ into a positive physical Hilbert space has the exact complete pairing $Q$. Let $V_t$ be its induced translation group on $\mathcal S=\overline{J\mathcal D^0}$, or an independently specified physical unitary group satisfying $JU_t=V_tJ$. For every $L\ne0$ and every nonzero Laurent polynomial $p$, the restriction $p(V_L)|_{\mathcal S}$ is not compact. In fact

\[
\sigma_{\rm ess}(V_L|_{\mathcal S})=\{z:|z|=1\}.
\tag{6}
\]

In particular, $V_L-e^{i\phi}I$ cannot be compact on the source closure or on the ambient physical sector containing it.

**Proof.** Set $x_R=Jf_R/\sqrt{\log R}$, for (R>1). Equations (3) and (5), density of $J\mathcal D^0$ in $\mathcal S$, and boundedness imply $x_R\rightharpoonup0$ in the physical Hilbert space and $\|x_R\|^2\to c_h$. For every nonzero integer $k$, (4) gives

\[
\langle x_R,V_L^kx_R\rangle\longrightarrow0.
\tag{7}
\]

Thus for $p(z)=\sum_{j=m}^n p_jz^j$,

\[
\|p(V_L)x_R\|^2\longrightarrow c_h\sum_j|p_j|^2>0.
\tag{8}
\]

A compact operator takes a bounded weakly null family to a norm-null family, contradicting (8). More generally polynomial approximation gives, for every continuous $F$ on the circle,

\[
\|F(V_L)x_R\|^2\longrightarrow
c_h\int_0^{2\pi}|F(e^{i\theta})|^2\frac{d\theta}{2\pi}.
\tag{9}
\]

If an open arc missed the essential spectrum, a nonzero continuous $F$ supported in that arc would have compact $F(V_L)$, by continuous functional calculus in the Calkin algebra. This contradicts (9). ∎

This proof does not assume RH and does not invoke an arithmetic spectral measure. Positivity is used only through the hypothesized physical norm and compact-operator argument. It strengthens the earlier exclusion of *exactly periodic* sources. It does not strengthen “pure point” to “impossible”: a Kronecker flow can have full-circle essential spectrum at every nonzero time and is not excluded by this theorem. Also, compact resolvent of $G$ alone does not imply a compact return for $e^{-itG}$.

The proof's weakly null family is a **contradiction test** for an assumed exact source, not a proposed recovery of physical vectors from weakly escaping packets. No source limit is inferred from its weak convergence.

## 4. Candidate A: actual electric standing waves in the fixed state

### 4.1 Physical sector and compression

Keep exactly the $6^3\times\{-2,-1,0,1,2\}$ SU(2) Wilson slab, $\beta=8/5$, theta zero, and $d\nu=Z^{-1}\Omega^2dm$. For the four-link plaquette write

\[
P=\cos\theta I+i\sin\theta\,\omega\cdot\sigma,
\quad \Sigma(P)=\omega\cdot\sigma,
\quad d\mu_\rho(\theta)=\tfrac2\pi\rho(\theta)\sin^2\theta\,d\theta.
\]

The values of $\Sigma$ at $P=\pm I$ are immaterial. It is bounded, measurable and gauge covariant elsewhere. The physical closed sector

\[
\mathcal H_{\rm pol}=\{F_0(\theta)I+F_1(\theta)\Sigma(P)\}
\simeq L^2(\mu_\rho)\oplus L^2(\mu_\rho)
\tag{10}
\]

uses the existing scalar and adjoint channels, not new matter or an auxiliary Hilbert embedding. Orthogonality follows from $\operatorname{tr}\Sigma=0$, $\Sigma^2=I$, and the trace/2 convention.

Compress the actual full electric **form**, divided by $\ell=4$, to this sector. Differentiation on SU(2), with the metric already fixed in Section 2 of the manuscript, gives

\[
q_\rho[F]=\frac2\pi\int_0^\pi\rho\{\sin^2\theta(|F_0'|^2+|F_1'|^2)+2|F_1|^2\}\,d\theta.
\tag{11}
\]

Every distinct link supplies the same term; the angular identity is $\sum_j|\nabla_{S^2}\omega_j|^2=2$. Scalar-adjoint cross terms have zero trace. Take the closed forms starting from smooth covariant plaquette functions and their Friedrichs operators $E_0,E_1\ge0$. These are compressed operators, not a claim that the full $E_\nu$ reduces this sector.

With $v=\sqrt\rho\sin\theta$, the actual unitary $WF=\sqrt{2/\pi}\,vF$ gives

\[
WE_0W^{-1}=-\partial_\theta^2+v''/v,
\quad WE_1W^{-1}=-\partial_\theta^2+2\csc^2\theta+v''/v.
\tag{12}
\]

The first operator has Dirichlet boundary conditions; the second has the Friedrichs inverse-square endpoint conditions. Smooth even positive $\rho$ makes (v''/v) smooth and bounded up to both endpoints. **No density potential is subtracted.** The state dependence is retained.

The wave prescription is

\[
G_{\rm el}=\sqrt{1+E_0}\oplus(-\sqrt{1+E_1}),\qquad V_x=e^{-ixG_{\rm el}}.
\tag{13}
\]

The two signs allow both frequency directions in the existing polarizations. This is an explicitly chosen electric-wave source relation, with parameter $x$ conjugate to electric frequency; it is not physical Euclidean time. The unit shift uses the fixed Casimir units. Any fixed positive shift or common wave-speed rescaling has the same obstruction. There is no claim that the YM dynamics forces the identification of arithmetic translation with (13).

### 4.2 Observable seeds, domain, and the positive mixed identity

An independent seed is a holonomy-angle evaluation distribution at a fixed interior angle, for example $\theta_0=\pi/2$, in either polarization; finite angular derivatives are further examples. More generally let $b_{s,n}$ be its coefficients in the actual orthonormal electric eigenbasis $e_{s,n}$, with

\[
\sum_{s,n}(1+\omega_{s,n}^2)^{-r}|b_{s,n}|^2<\infty
\tag{14}
\]

for some finite $r$, where $\omega_{s,n}>0$ are the eigenvalues of $\sqrt{1+E_s}$. Evaluation and its finite derivatives satisfy such a condition by one-dimensional Sobolev evaluation. No zero ordinates or digamma multiplier define this seed. Write $\epsilon_0=1,\epsilon_1=-1$. Spectral cutoff sources converge **strongly**:

\[
J_bf=\lim_{N\to\infty}\sum_{s,n\le N}
b_{s,n}\widehat f(\epsilon_s\omega_{s,n})e_{s,n}.
\tag{15}
\]

For any compact smooth $f$, Fourier decay together with (14) proves convergence, continuity in fixed-support smooth-test seminorms, and arbitrary electric regularity after smearing. The actual state-dependent pairing is exactly

\[
B_b(f,g)=\langle J_bf,J_bg\rangle_\nu
=\sum_{s,n}|b_{s,n}|^2
\overline{\widehat f(\epsilon_s\omega_{s,n})}
\widehat g(\epsilon_s\omega_{s,n}).
\tag{16}
\]

The eigenfrequencies, eigenfunctions, and coefficients of the fixed geometric seed depend on $\rho$. This is a positive completed norm because the source series converges in the actual physical space; no finite-matrix surrogate, subtraction, constraint, contact adjustment, or renormalization is involved. Multiplying by an independently defined finite-order electric or source derivative is covered by increasing $r$. Some such sources fall outside ordinary-input-norm bounds; this is precisely why the distributional possibility deserves a separate test.

There are no character scaling packets or winding operations in (15), hence no discarded rational-phase branches. If winding-modified seeds are included and remain in (14), all their coefficients enter (16). An extension claiming covariance under (13) is subject to the theorem for **every** seed, not just the identity-phase seed. Abandoning that covariance is a different candidate and is not excluded here.

### 4.3 Failure even for arbitrary distributional seeds

Put $V_\rho=1+v''/v\in C^\infty[0,\pi]$. In Haar coordinates, $1+E_0=-\partial^2$ has eigenvalues $n^2$, $n\ge1$. The adjoint channel $1+E_1=-\partial^2+2\csc^2\theta$ has eigenvalues $n^2$, $n\ge2$. One way to check the latter is the intertwiner $A=\partial-\cot\theta$: $A\sin(n\theta)$ is an eigenfunction for $n\ge2$, $A\sin\theta=0$, $A^*A=-\partial^2-1$, and $AA^*=-\partial^2+2\csc^2\theta-1$. Its missing adjoint kernel would be proportional to $1/\sin\theta$, which is not in $L^2$; the eigenfunctions are complete in the Friedrichs sector.

The actual operators in (12), shifted by one, differ from these by the **bounded retained potential** $V_\rho$. The min-max principle therefore gives

\[
|\omega_{s,n}^2-n^2|\le\|V_\rho\|_\infty,
\qquad \omega_{s,n}=n+O_\rho(n^{-1}).
\tag{17}
\]

Consequently $V_{2\pi}-I$ is a diagonal compact operator on (10). Its singular values tend to zero in both polarizations. Theorem 2 excludes (16) equalling $Q$ globally for every seed satisfying (14), and in fact excludes **any** Hilbert-valued source covariant under (13), with no seed-order bound.

This tests a pure-point physical generator that avoids the earlier full-current absolutely-continuous theorem and does not preserve the excluded winding module. Its failure is the asymptotic spacing, not smoothness of the state or finite lattice size alone. The ordinary scalar wave with only positive frequencies was already excluded by its one-sided spectrum; the two-polarization calculation rules out that repair without importing a second Hilbert space. The full many-link electric operator need not have (17), and is not excluded by this argument. Nor are all compact-manifold waves or all pure-point flows.

## 5. Candidate B: spacetime-covariant sources in a continuum vacuum

This part explicitly changes from the prepared finite torus/slab state to a continuum theory on Minkowski $\mathbb R^{1,3}$. Assume continuum YM existence and full OS reconstruction, a separable physical Hilbert space, a strongly continuous positive-energy unitary Poincaré representation, and a unique translation-invariant vacuum. A physical mass gap may also be assumed, as authorized, but is not needed for the argument below. These are representation and vacuum assumptions; no arithmetic source correlation is added.

The candidate source relation for a fixed nonzero real four-vector $a$ is

\[
JU_t=V_tJ,\qquad V_t=e^{-itP\cdot a}.
\tag{18}
\]

Its independent physical meaning is translating a fixed gauge-invariant preparation or field smearing along a straight spacetime direction. For an actual prepared vector $b=A\Omega_{\rm vac}$, polynomial derivative smearing gives

\[
J_bf=\{p(i\lambda)\widehat f(\lambda)\}(P\cdot a)b,\quad
B_b(f,g)=\int\overline{\widehat f(\lambda)}\widehat g(\lambda)
|p(i\lambda)|^2\,d\mu_b^a(\lambda).
\tag{19}
\]

The combined multiplier is bounded for each test; an unbounded factor is not applied separately to $b$. This is positive, state-dependent, and well defined by strong spectral truncations. Genuine distributional preparations can be admitted whenever their smearing yields a continuous law into this same physical Hilbert space. The following conclusion needs only that law and (18), so no ultraviolet seed assumption is hidden.

**Lemma 3 (spectral type of a spacetime line).** Under the representation assumptions above, the spectrum of $P\cdot a$ on the orthogonal complement of the vacuum is absolutely continuous with respect to Lebesgue measure, for every $a\ne0$.

**Proof without a particle decomposition.** Let (E(dp)) be the joint momentum spectral measure and let $\mu=\sum_n2^{-n}\langle e_n,E(\cdot)e_n\rangle$ for an orthonormal basis. Then $\mu(B)=0$ iff $E(B)=0$. Lorentz covariance makes this measure class invariant. Average $\mu$ over a smooth nonnegative compactly supported density on the connected Lorentz group which is positive near the identity. The average $\bar\mu$ has the same null sets: one implication follows from covariance; conversely the integrands $\langle U(\Lambda)e_n,E(B)U(\Lambda)e_n\rangle$ are nonnegative continuous functions, so zero average forces their value at the identity to vanish.

For each nonzero forward-cone momentum $p$, the function $\Lambda\mapsto a\cdot\Lambda p$ is a nonconstant real-analytic function on this group. Its critical set has Haar measure zero; the submersion/coarea theorem on the complement shows that the inverse image of every Lebesgue-null subset of the line has Haar measure zero. Tonelli therefore shows that the pushforward of $\bar\mu$ under $p\mapsto a\cdot p$, restricted to $p\ne0$, annihilates every such null set. Equivalence of measure classes proves the assertion for $E$. At $p=0$, uniqueness leaves just the vacuum. ∎

The nonconstancy assertion includes timelike, spacelike and lightlike $a$: a nonzero linear functional cannot be constant on a nonzero forward Lorentz orbit. The argument needs infinite-volume continuous Lorentz covariance, not simply a gap on a spatial torus. Standard mass-shell representation theory gives the same conclusion; see [Bekaert–Boulanger](https://arxiv.org/abs/hep-th/0611263). The measure-averaging proof above supplies the needed step directly and does not assume asymptotic completeness.

It follows that every finite-vector coefficient has the form

\[
\langle v,V_tv\rangle=|\langle\Omega_{\rm vac},v\rangle|^2+c_v(t),
\qquad c_v\in C_0(\mathbb R).
\tag{20}
\]

If this were $C_*(t)$, boundedness would imply RH by the earlier one-probe criterion. Under that consequence its absolutely convergent Fourier series has nonzero frequencies at the zero ordinates, zero Cesàro mean, and positive mean square. Averaging (20) then kills the vacuum constant, and $C_0$ contradicts the positive mean square. Hence no such vector exists, and no exact $Q$-source can obey (18). This uses the reviewed probe theorem in its actual scope; it does not identify arithmetic regularity with an OS axiom.

There are no winding operations or prime subtractions in this candidate. All field and contact renormalizations must be fixed by the underlying physical observable prescription; if their smeared limits are genuine vectors covariant under (18), the exclusion still applies. Formal distributional coefficients outside the physical Hilbert space are not positive source norms. Choosing a non-geometric source action instead is outside this theorem.

## 6. What remains open

The short-support test adds a necessary spectral condition that is stronger than nonperiodicity and can actually be checked for an uncompensated native electric candidate. The continuum result independently checks ordinary spacetime translation, including spatial directions, rather than citing clustering without hypotheses. Both leave a precisely bounded conclusion.

A successful source may still use non-geometric relations, a different native pure-point action, the full many-link sector, or a compact-occurrence argument without a native generator. Such proposals must supply the complete reflected mixed pairing, retain it strongly in the physical representation, and derive any subtraction or constraint independently. Full OS axioms, continuum existence and a gap have not supplied that identification. The one-correlation theorem remains a conditional reduction in data, not a demonstrated reduction in difficulty. No positive completion of $Q$ or YM-to-RH implication is established here.

The [audit](../reviews/COMPACT_RETURN_AND_CONTINUUM_TRANSLATION_AUDIT_20260925.md) lists the essential checks. The separate [tail audit](../reviews/PROBE_TAIL_CERTIFICATION_AUDIT_20260925.md) proves only the post-cutoff estimate and retains diagnostic labels for the floating zero comparison. Numerical housekeeping is not used in either physical obstruction.
