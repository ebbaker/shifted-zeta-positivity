# Global determination from separated sources, with a fixed-YM existence criterion

Date: 24 September 2026, America/New_York.  
Prepared for Edward Baker with substantial LLM assistance.  
Model exposed to this session: GPT-6 (Codex); exact variant and configured reasoning-effort label not exposed, not inferred.  
Baseline: b60a2e27b9a39be33b1b43bb7b99172cdc5e7573.  
Status: new research-note deductions with proofs, not independently reviewed. The existence and arithmetic identification of a YM source family remain open. No RH proof or novelty claim.

This develops the highest-priority route in the [critical review](../reviews/GLOBAL_MECHANISMS_CRITICAL_REVIEW_20260924.md): occurrence of a genuine source family, followed by a global identity determining its pairing. It removes the requirement to identify a separate native translation generator before attempting source existence. The [source ledger](GLOBAL_MECHANISMS_PRIMARY_SOURCE_LEDGER_20260924.md) records the literature checked.

## 1. The distinction that controls the argument

An exact source map into a positive OS space automatically induces a unitary translation group on its closed image. Finding that group among previously identified YM operators is an additional realization condition. It is useful for particular ansätze, but unnecessary for the bare reflected-pairing objective.

The proposed replacement is to derive a mixed identity for **separated arithmetic supports** from an actual YM source prescription. This is not a statement about spacelike-separated physical observables: arithmetic support and physical localization have no dictionary yet.

The identity below contains the arithmetic content explicitly. It must be derived, for example through an actual Poisson/trace relation for YM observables. Imposing it as a list of positive moment constraints is not an independent realization. The theorem establishes precisely what it would determine if derived.

## 2. Definitions and the separated-support target

Use the outline's normalization:
\[
\mathcal D=C_c^\infty(\mathbb R),\qquad
\mathcal D^0=\{f\in\mathcal D:\int e^{x/2}f(x)\,dx
=\int e^{-x/2}f(x)\,dx=0\},
\]
\[
T=-\partial_x^2+\tfrac14,\qquad
U_af(x)=f(x-a),\qquad Rf(x)=f(-x).
\]
Pairings are antilinear in the first argument. Write
\[
d_{p,m}=m\log p,\quad c_{p,m}=(\log p)p^{-m/2},
\quad n(r)=\frac{e^{-r/2}}{1-e^{-2r}}\quad(r>0).
\]

The map \(T:\mathcal D\to\mathcal D^0\) is a topological isomorphism for the usual compact-support test topologies, with inverse
\[
(T^{-1}f)(x)=\int e^{-|x-y|/2}f(y)\,dy.
\tag{1}
\]
The two moment conditions remove the exterior tails. On each enclosing compact interval the inverse is continuous, and its output is supported in the convex hull of the input support. “Same support” here means the same enclosing interval; holes in a disconnected support need not be preserved. Continuity follows from this integral formula and the equation \(h''=h/4-f\).

For \(f=Th,\ g=Tk\) with disjoint supports of \(h,k\), define
\[
\begin{aligned}
\mathfrak W_{\rm sep}(f,g)={}&
-\iint\overline{f(x)}\,g(y)n(|x-y|)\,dx\,dy\\
&-\sum_{p,m}c_{p,m}
\bigl(\langle f,U_{d_{p,m}}g\rangle_2+
\langle f,U_{-d_{p,m}}g\rangle_2\bigr).
\end{aligned}
\tag{2}
\]
The integral has no diagonal singularity. Only finitely many shifts meet the compact difference of the two supports, so the sum is finite. Both shift directions are necessary for a Hermitian pairing.

**Direct calculation.** The polarized gamma form is
\[
\tfrac12\iint
(\overline{f(x)}-\overline{f(y)})(g(x)-g(y))n(|x-y|)\,dx\,dy.
\]
When the supports are disjoint its two same-point terms vanish; its two cross terms combine into the first term of (2). The contact term vanishes by disjointness, and the pole term vanishes by pole neutrality. Consequently
\[
Q(Th,Tk)=\mathfrak W_{\rm sep}(Th,Tk)
\quad\text{if }\operatorname{supp}h\cap\operatorname{supp}k=\varnothing.
\tag{3}
\]
This is an unconditional identity for the explicit arithmetic form, not yet an identity for YM sources.

## 3. A determination theorem without a native generator

**Theorem 1 (three remaining constants).** Let \(B\) be a continuous Hermitian sesquilinear form on \(\mathcal D^0\), without any sign assumption. Suppose:

1. \(B(U_af,U_ag)=B(f,g)\) and \(B(Rf,Rg)=B(f,g)\).
2. For every disjointly supported \(h,k\in\mathcal D\),
   \(B(Th,Tk)=\mathfrak W_{\rm sep}(Th,Tk)\).
3. For every fixed \(h\in\mathcal D\), as real \(|\lambda|\to\infty\),
\[
\left|B\left(\lambda^{-2}T(e^{i\lambda x}h),
                   \lambda^{-2}T(e^{i\lambda x}h)\right)\right|
=O_h(\log(2+|\lambda|)).
\tag{4}
\]

Then there are real constants \(a_0,a_1,a_2\) such that, for every \(h,k\in\mathcal D\),
\[
B(Th,Tk)-Q(Th,Tk)
=a_0\langle h,k\rangle_2+
a_1\langle h',k'\rangle_2+
a_2\langle h'',k''\rangle_2.
\tag{5}
\]

In particular choose any nonzero \(h\in\mathcal D\), put
\[
h_r(x)=r^{-1/2}h(x/r),\qquad r\in\{1,2,3\},
\tag{6}
\]
and additionally require
\[
B(Th_r,Th_r)=Q[Th_r]\qquad(r=1,2,3).
\tag{7}
\]
Then \(B=Q\) on all of \(\mathcal D^0\).

**Proof.** Pull back the difference:
\[
C(h,k)=B(Th,Tk)-Q(Th,Tk).
\]
It is a continuous translation-invariant sesquilinear form on \(\mathcal D\). Its distribution kernel is invariant under simultaneous translations of its two coordinates. Equivalently it is a convolution kernel \(c(x-y)\). This standard distribution-kernel statement does not require temperedness: in difference and common-translation coordinates, translation invariance makes the distribution constant in the latter coordinate.

By (3) and hypothesis 2, the kernel vanishes on every product of disjoint test supports. Such product neighborhoods cover the complement of the diagonal. Its support is therefore contained in the diagonal, so \(c\) is supported at the origin.

A distribution supported at one point has finite order and is a finite linear combination of delta derivatives. Thus
\[
C(h,k)=\frac1{2\pi}\int p(\tau)
\overline{\widehat h(\tau)}\,\widehat k(\tau)\,d\tau
\]
for a polynomial \(p\). Hermiticity makes \(p\) real on the real axis; reflection makes it even.

The audited high-frequency calculation gives
\[
Q[\lambda^{-2}T(e^{i\lambda x}h)]
=\|h\|_2^2\log|\lambda|+O_h(1).
\]
Combining this with (4) yields
\[
C(e^{i\lambda x}h,e^{i\lambda x}h)
=O_h(\lambda^4\log(2+|\lambda|)).
\]
If \(p\) has degree \(d\) and leading coefficient \(b_d\ne0\), the same expression equals
\[
\frac1{2\pi}\int p(\lambda+\eta)|\widehat h(\eta)|^2\,d\eta
=b_d\|h\|_2^2\lambda^d+O_h(|\lambda|^{d-1}).
\]
Hence \(d\le4\). Write \(p(\tau)=a_0+a_1\tau^2+a_2\tau^4\), which gives (5) by Plancherel.

Let \(A_j=\|h^{(j)}\|_2^2>0,\ j=0,1,2\). The three equations (7) are
\[
a_0A_0+a_1A_1r^{-2}+a_2A_2r^{-4}=0,\qquad r=1,2,3.
\]
The coefficient matrix is a Vandermonde matrix in \(1,1/4,1/9\), times the nonzero column factors \(A_j\). Its determinant is
\(-5A_0A_1A_2/54\). All three constants vanish. Equation (1) then gives \(B=Q\). \(\square\)

**Why there are three constants.** Pole removal has order two. Local terms in the pulled-back \(h\)-pairing of differential order up to four survive the logarithmic growth bound after normalization by \(\lambda^{-2}\). One contact constant is not enough on this restricted test space under the hypotheses just stated.

**Sharpness control.** Every form
\[
B_a(Th,Tk)=Q(Th,Tk)+\sum_{j=0}^2a_j\langle h^{(j)},k^{(j)}\rangle_2
\tag{8}
\]
obeys hypotheses 1–3 and the separated-support identity. The added term on the normalized high-frequency tests is \(O(1)\). Thus even the more precise leading asymptotic \(\|h\|^2\log|\lambda|+O(1)\) does not remove these constants. Their positivity is neither claimed nor needed for this control.

If reflection is not independently available, the polynomial can have all degrees 0 through 4, leaving five real constants. The three-constant version must not silently assume this symmetry of a provisional YM source family.

## 4. What this theorem accomplishes, and what it does not

The earlier perturbations by arbitrary even Schwartz Fourier multipliers obey translations, reflection, and leading high-frequency growth. Theorem 1 shows exactly which perturbations survive the much stronger separated-support identity: a three-dimensional space after pole removal. This is a determination result among Hermitian forms of unknown sign, so it does not use the desired positivity.

The theorem is global from its statement. There is no maximum support length, prime cutoff chosen once and then frozen, lower-gap assumption, or estimate uniform in \(L\). A compact input simply makes the sum in (2) finite.

The remaining identity is substantial. For actual sources \(J\), it is
\[
\boxed{\quad
\langle JTh,JT k\rangle_{\rm OS}
=\mathfrak W_{\rm sep}(Th,Tk)
\quad\text{for all disjoint }h,k\in\mathcal D.
\quad}
\tag{9}
\]
It includes the singular correlations at every prime-power separation and the smooth archimedean tail between them. Translation invariance and local YM integration by parts do not derive it.

The new result reduces the matching problem to (9), a growth bound, symmetries, and three normalizations. It does **not** substantially reduce the amount of arithmetic information that must enter: almost all of that information remains in (9). Its value is a precise target with a proved uniqueness conclusion, rather than an unspecified appeal to “rigidity.”

The three anchor values need not be assumed positive without evidence. A fixed bump modulated sufficiently far in frequency makes all three dilated anchor values positive by the same audited high-frequency estimate. This only verifies consistency of a finite normalization choice; it proves no source existence.

## 5. Where an independent arithmetic identity might come from

Meyer's character calculation is a useful template because a single global construction combines a dilation sum and Fourier/Poisson duality. The prime terms arise from the Euler factorization of that dilation sum, while the archimedean term arises from the Fourier part. Its trace regularity and quotient topology are essential. See [Meyer, §§3–5, especially Theorem 5.8](https://arxiv.org/pdf/math/0412277).

One can specify the arithmetic relation to look for more sharply. On even Schwartz functions \(\phi\), with the additive Fourier transform
\(\mathcal F\phi(y)=\int e^{-2\pi ixy}\phi(x)\,dx\), let
\[
(\mathsf Z\phi)(x)=\sum_{n\ge1}\phi(nx),\qquad x>0.
\]
Poisson summation gives the exact global relation
\[
\mathsf Z\phi(x)
=x^{-1}\mathsf Z(\mathcal F\phi)(x^{-1})
+\tfrac12\bigl(x^{-1}\mathcal F\phi(0)-\phi(0)\bigr).
\tag{P}
\]
The last two terms vanish on the core
\(\phi(0)=\mathcal F\phi(0)=0\). Integer dilations compose multiplicatively; their Euler decomposition then distinguishes prime powers without listing them as target positive moments. This is an arithmetic model for a relation to derive or realize, not a relation already satisfied by Wilson loops. This even Schwartz core is not literally \(\mathcal D^0\); any occurrence theorem must state the map between the relevant module and the logarithmic source tests.

For a genuine YM proposal, specify the observable operations corresponding to integer dilation and Fourier duality, prove convergence of the summed insertion on a declared core, and establish the relevant quotient/trace regularity. Then separately derive that its trace calculation equals the OS pairing in (9), with the pole-sector sign accounted for. A vector identity (P) by itself does not fix that pairing. These are identifiable obligations that a proposed occurrence theorem can meet or fail.

The missing YM statement is not that one may write integer dilation symbols next to Wilson loops. It is that independently defined operations on a specified YM source core obey a Poisson/dilation relation whose **actual OS pairing** yields (9). If an auxiliary adelic space is introduced, one must either prove its occurrence with the requisite metric inside the YM representation or identify it as a change of model.

A character is a trace; the OS pairing is a vector inner product. Equality of traces, an algebraic module isomorphism, and an isometry are different assertions. A formal transfer of a character does not settle (9). The [spectral controls](SOURCE_SPECTRA_MODULAR_AND_LIOUVILLE_CONTROLS_20260924.md) explain additional pitfalls of unitarizing an entire jet module.

No such YM Poisson identity was found in the checked literature or existing notes.

## 6. Compact finite compatibility inside the specified YM representation

Here is a replacement for the previous criterion's assumption of already-defined maps on every test.

**Theorem 2 (finite compatibility with compact source control).** Fix Hilbert spaces
\(\mathcal K\hookrightarrow\mathcal H\) with compact, continuous, injective inclusion. Let \(F\subset\mathcal D^0\) be a countable vector space over \(\mathbb Q(i)\) whose intersection with each member of an exhausting sequence of compact-support test spaces is dense there.

Prescribe finite smooth seminorms \(p_I\) and constants \(C_I\) on that exhaustion. Unknowns are actual vectors \(v_f\in\mathcal K,\ f\in F\), subject to:

- rational complex linearity;
- \(\|v_f\|_{\mathcal K}\le C_Ip_I(f)\) whenever \(\operatorname{supp}f\subset I\);
- any stated relations closed under coordinatewise strong \(\mathcal H\) convergence on these bounded balls, involving finitely many coordinates at a time.

Suppose every finite subset of these constraints is simultaneously feasible in the same fixed coordinate balls. Then there is a continuous complex-linear
\[
J:\mathcal D^0\longrightarrow\mathcal H
\]
satisfying all the constraints, with \(Jf\in\mathcal K\) and the stated local bounds.

The closed relations may include bounded YM operator intertwinings, mixed matrix elements with specified YM vectors, the dense-test versions of (9), and the three anchors. To conclude Theorem 1, its symmetries and disjoint-support identity can be enforced on appropriate dense families and extended by continuity. The high-frequency bound requires uniform control, as explained below; a pointwise asymptotic on a dense list alone is insufficient.

**Proof.** For each \(f\), choose one enclosing interval and its finite bound \(M_f\). The image in \(\mathcal H\) of the closed \(\mathcal K\)-ball of radius \(M_f\) is compact and closed. Indeed, compact inclusion gives relative compactness, and weak compactness in \(\mathcal K\) identifies every strong \(\mathcal H\) limit with a vector in the same ball.

Take the product of these compact coordinate sets. All specified constraints are closed subsets. Additional bounds from other enclosing intervals are closed by the same weak lower-semicontinuity argument. Finite simultaneous feasibility gives the finite intersection property, hence a global assignment.

Rational linearity and local seminorm bounds extend this assignment uniquely to each full fixed-support test space. These extensions are complex-linear, since \(\mathbb Q(i)\) is dense in \(\mathbb C\), and agree on overlaps. The test-space inductive-limit topology gives a single continuous \(J\). Weak compactness in \(\mathcal K\) retains membership and the local bounds on extension. The required relations pass to limits under the stated closedness and continuity conditions. \(\square\)

For disjoint-support constraints, use countably many pairs of disjoint rational-endpoint intervals and dense test families on them; arbitrary disjoint compact supports are covered by finite such pieces and a partition of unity. For translations one can first use rational shifts and then continuity. This prevents a dense test list from accidentally failing to test the separated-support identity.

For the high-frequency condition, a sufficient closed family of bounds is
\[
\|J[\lambda^{-2}T(e^{i\lambda x}h)]\|_{\mathcal H}^2
\le D_I q_I(h)^2\log(2+|\lambda|),\qquad |\lambda|\ge1,
\tag{G}
\]
where \(q_I\) is a fixed continuous seminorm on profiles supported in \(I\) and \(D_I\) is independent of \(\lambda,h\). Include the rational-modulation tests in the countable source family. Enforcing (G) there extends it to all profiles and real modulations by continuity, with the same bound. Theorem 1 only requires its weaker per-profile consequence (4). Ordinary smooth-test continuity or the \(\mathcal K\) bound alone does not supply (G).

**Unbounded operators.** The relation \(Av_f=v_g\) for a fixed closed operator \(A\) is closed in strong \(\mathcal H\times\mathcal H\). Relations involving additional uncontrolled \(Av_f\) coordinates require graph bounds or separately compact coordinates. A formal differential symbol alone is insufficient.

**What is genuinely new relative to the earlier criterion.** Partial finite assignments suffice; neither a sequence of global maps nor a projectively surjective family of extension maps is assumed. The conclusion stays in the original Hilbert representation, rather than reconstructing a new state. The price is arbitrary finite feasibility within a single prescribed collection of compact bounds. That price has not been paid.

Merely appending the entire desired arithmetic pairing as positive moments and assuming finite feasibility would restate positivity. Theorem 2 is an extension tool, not an independent source of arithmetic feasibility. Its intended application uses a source law and mixed identities obtained from the model.

## 7. A concrete YM control operator and the first tractable lemma

Keep the finite Wilson slab, gauge group, coupling, and finite-volume boundary state fixed. On the compact spatial link manifold \(M\), use
\[
\mathcal H=L^2_{\rm cov}(M,\nu;\operatorname{End}\mathbb C^N),
\qquad d\nu=Z^{-1}\Omega^2dm.
\]
The reference endomorphism fiber is the same one already present in the finite-slab construction.

Choose an orthonormal Lie-algebra basis on every link and let \(D_{\ell,a}\) be its Haar derivatives. On smooth matrix functions define the quadratic form
\[
\mathfrak e(B)=\sum_{\ell,a}\|D_{\ell,a}B\|_{\mathcal H_{\rm full}}^2,
\qquad
E=\sum_{\ell,a}D_{\ell,a}^{*}D_{\ell,a},
\quad D_{\ell,a}^{*}=-D_{\ell,a}-2D_{\ell,a}\log\Omega.
\tag{10}
\]
The full derivative family is used; a single colored derivative need not preserve covariance. The product bi-invariant metric and gauge-invariant weight make the summed form gauge invariant. Its Friedrichs operator commutes with the gauge projection. Restrict it to the covariant subspace.

**Lemma 3 (a compact source norm and quantitative tail bound).** \(E\ge0\) is elliptic with compact resolvent on this finite compact manifold, and its covariant restriction has compact resolvent. For \(r>0\), set
\[
\mathcal K_r=\operatorname{Dom}(1+E)^{r/2},\quad
\|B\|_{\mathcal K_r}=\|(1+E)^{r/2}B\|_{\mathcal H}.
\]
Then \(\mathcal K_r\hookrightarrow\mathcal H\) is compact. With
\(P_R=\mathbf1_{[0,R]}(E)\),
\[
\|(1-P_R)B\|_{\mathcal H}
\le(1+R)^{-r/2}\|B\|_{\mathcal K_r}.
\tag{11}
\]

**Proof.** Smooth positivity of \(\Omega\) makes (10) a uniformly elliptic weighted Laplacian on a compact manifold without boundary, with a finite-dimensional matrix fiber. Standard elliptic compactness gives compact resolvent; restriction to a reducing subspace preserves it. Expand \(B\) in its eigenbasis. On eigenvalues exceeding \(R\), \(1\le(1+R)^{-r}(1+E)^r\), proving (11). Finite-rank spectral projections and this tail bound prove compact embedding. \(\square\)

These finite projections are smooth covariant boundary observables in the same state. They need not be finite words of fundamental Wilson loops. If that narrower algebra is required, approximation by gauge-averaged Peter–Weyl matrix polynomials must be included. Such polynomials are smooth boundary spin networks, with no new bulk matter. Their smooth approximation on a compact group supplies a useful admissible core, but their density alone does not select an arithmetic family.

The operator \(E\) is a regularity control, not the arithmetic generator. Its semiboundedness is harmless here.

## 8. Recommended next existence problem

Fix one finite pure SU(N) Wilson slab and the source core just described. Seek an independently specified system of source relations with the following properties:

1. Arbitrary finite sets admit covariant source vectors with common local \(\mathcal K_r\) bounds, as in Theorem 2.
2. Their OS pairings are stationary, reflection invariant, and obey (4).
3. A derived mixed Poisson/trace or insertion identity proves (9) for all separated supports.
4. Three independently normalized source values satisfy (7).

Then Theorems 1–2 give one global source map with pairing \(Q\). Assumed OS positivity gives RH through the verified restricted Weil criterion. No uniform positive gap, native generator, continuum limit, or simplicity of zeros is required.

The first tractable control lemma is Lemma 3, proved here. The first **unresolved and discriminating** task is to derive a source relation that produces the complete right side of (9), beginning with the smooth gamma tail and at least the full tower \(m\log2\) under one law, then explaining all primes through the same law. Checking finitely many separations is only a falsification/control step. A rule that inserts the coefficients by hand fails the intended test.

If no such mixed relation can even be specified, the compactness machinery should not be enlarged or numerically optimized. It has nothing arithmetic to extend.

## 9. Verification record

- Recomputed the off-diagonal gamma sign, the two prime-shift orientations, and the absence of pole/contact terms on separated pole-neutral tests.
- Proved the finite-order local ambiguity and checked the fourth-order cutoff against the normalized high-frequency tests.
- Checked the three-anchor Vandermonde determinant and the full three-parameter counterexample family.
- Checked the Poisson relation (P), including its half factors and the distinction between its Schwartz core and the pole-neutral logarithmic tests.
- Checked the finite-intersection argument in the original representation, the local test-topology extension, the closed-graph qualification, and the uniform growth bound (G) needed for passage from dense profiles to all profiles.
- Checked the weighted elliptic adjoint and the spectral tail bound.
- No numerical experiment was needed. No source occurrence, finite-feasibility theorem for arithmetic constraints, or mixed YM/arithmetic identity has been proved.

These arguments remain model-assisted research requiring an independent mathematical review.
