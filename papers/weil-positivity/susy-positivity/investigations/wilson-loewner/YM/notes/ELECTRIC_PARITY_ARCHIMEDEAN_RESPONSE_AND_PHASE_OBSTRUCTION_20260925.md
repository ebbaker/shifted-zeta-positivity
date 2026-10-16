# An electric parity response for the archimedean term, and its obstruction as a positive source

25 September 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance.

Model exposed: GPT-6 (Codex). Exact deployed variant and reasoning effort: unavailable; not inferred.

Status: analytical research deductions with proofs and floating controls; not independent human verification. No positive Weil-source construction or RH proof. The model and state remain the fixed four-dimensional SU(2) Wilson slab. The scalar class sector is embedded in its existing boundary Hilbert space as F(P)I; no extra matter or auxiliary physical theory is introduced.

## 1. Result and the two candidates

The [audit](../reviews/CHARACTER_CURRENT_AND_PRIME_DOMAIN_AUDIT_20260925.md) rederives the earlier character identities without relying on the 57 floating controls. They survive with clarified distribution domains and an additional opposite-current obstruction at phase pi.

This continuation tests exactly two mechanisms:

1. Smooth electric–Wilson currents and their positive quadratic responses. A dense-phase obstruction excludes a common nontrivial smooth radial current on the winding-generated packet space.
2. A normalized radial electric derivative, followed by the sum of logarithmic representation scale and logarithmic holonomy angle. This independently specified **signed insertion** has the exact archimedean mixed limit, including its contact constant and logarithmic growth. It also fails to remain finite on winding-created nonidentity phases.

For the second mechanism there are smooth physical packets F_R(f), a fixed densely defined symmetric insertion C_rho, and the original bounded winding operations V_a such that

\[
\lim_{A\to\infty}\lim_{R\to\infty}
\left\{\langle F_R(f),C_\rho F_R(g)\rangle_\nu
-\sum_{2\le a\le A}\Lambda(a)
 [\langle F_R(f),V_aF_R(g)\rangle_\nu
 +\langle V_aF_R(f),F_R(g)\rangle_\nu]\right\}
=Q(f,g)
\tag{1}
\]

for every f,g in the global pole-neutral test space. Equation (1) is a complete **signed mixed insertion limit**, not a norm identity. Its order of limits is specified; an arbitrary joint prime cutoff is not claimed for these modified packets. The insertion is defined in §3 without using a digamma function. Positivity and source occurrence fail for the direct constructions tested here; §§7–9 explain precisely what remains open.

The real-place logarithmic Fourier operator that appears in the limit is classical: see [Burnol, Spectral Analysis of the local Conductor Operator](https://arxiv.org/abs/math/9811040). No novelty is claimed for that operator or its Mellin diagonalization. The calculation here derives it from the explicitly specified finite-slab class observables and audits what that does and does not accomplish.

## 2. Candidate 1: smooth electric–Wilson currents

Let E_nu be the full weighted electric Friedrichs operator, ell=4 the number of distinct plaquette links, and X=(tr P)/2=cos theta. For a real smooth h on [-1,1], set

\[
A_{h,\nu}={i\over2\ell}[E_\nu,M_{h(X)}]
=-i(Y_h+\tfrac12\operatorname{div}_\nu Y_h),\qquad
Y_h=\ell^{-1}\nabla h(X).
\tag{2}
\]

These are actual full-state operators. On smooth covariant observables the displayed commutator is exact. The complete smooth flow supplies a self-adjoint closure and domain; the observable core is smooth covariant functions. The actual positive response is <A_h F,A_h G>_nu on that domain, not an unweighted radial norm. The weighted drift is bounded, although it need not preserve class functions.

On the one-plaquette radial coordinate, Y_h=-h'(cos theta)sin theta partial_theta. Fixed-phase character packets have principal current

\[
A_{h,\nu} S_R^\beta f
=N h'(\cos\beta)\sin\beta\, S_R^\beta(e^x f)+O(1).
\tag{3}
\]

Here multiplication by the smooth symbol can be replaced by its value at the packet's angular concentration: in the sine-series representation, summation by parts localizes the packet within O(1/N) of that angle, with rapidly decreasing scaled tails. Applying one derivative costs N. This proves the O(1) remainder. Equivalently the same estimate follows by Taylor expansion of the rapidly decreasing Fourier coefficients of h(cos theta). The actual drift is bounded and does not change (3).

**Dense-phase obstruction.** If ||A_h S_R^beta f|| remains bounded for every rational phase beta and one nonzero fixed f, then h'(cos beta)sin beta=0 at every such phase. Those phases are dense, so h' vanishes on (-1,1); h is constant and A_h=0. Thus no nonzero smooth current of the form (2) acts finitely on every rational-phase packet. Winding by all integers creates this dense collection of angles.

At beta=0 and pi, the next terms are h'(1)(-if') and h'(-1)(+if'), respectively. For h(X)=X this gives the explicit nonzero a=2 defect in audit (A7). For a>=3, audit (27) gives a positive N^2 norm coefficient. This excludes using that current as a common arithmetic derivative even at the first exceptional winding.

The same obstruction applies to finite positive sums of current norms: each positive summand's leading square must vanish at every phase. For a countable positive sum the conclusion applies to each summand. It does not exclude singular, phase-dependent, R-dependent, or nonlocal source relations. Such relations require separate domains and physical definitions.

Even on the identity component, the bare current response tends to <f',g'> and grows quadratically in input frequency. Smooth bounded Wilson multipliers instead have local packet limits. Neither is the required logarithmic archimedean response. This motivates the logarithmic scale pairing below; it is not a digamma functional calculus of A_nu.

## 3. Candidate 2: an independently defined radial electric parity response

Write H_cl=L2(SU(2),rho dg)^Ad for the actual closed class space. Define the unitary radial half-density map

\[
\mathscr W_\rho F(\theta)=\sqrt{2/\pi}\,v(\theta)F(\theta),
\qquad v(\theta)=\sqrt{\rho(\theta)}\sin\theta,
\qquad 0<\theta<\pi.
\tag{4}
\]

Its target is L2((0,pi),dtheta). Let D=sqrt(-partial_theta^2_Dirichlet), with normalized eigenvectors s_n=sqrt(2/pi)sin(n theta), eigenvalues n>=1, and domain H0^1(0,pi). Define the bounded partial isometry

\[
B=\partial_\theta D^{-1},\qquad
Bs_n=c_n:=\sqrt{2/\pi}\cos(n\theta),\quad B^*B=I,
\quad BB^*=I-\Pi_{\rm constants}.
\tag{5}
\]

The derivative is a closed map H0^1->L2; its adjoint is -partial_theta on H1. Formula (5) determines its bounded polar part and its actual adjoint. B is an isometry into the mean-zero cosine space, not a surjective unitary on the interval.

This construction uses a **specified compression and compensation** of electric energy, not a false restriction of E_nu. Indeed the class electric form is

\[
\ell^{-1}\mathfrak e_\nu(F(P),G(P))
={2\over\pi}\int_0^\pi\rho\sin^2\theta\,\overline{F'}G'\,d\theta.
\]

Its radial Friedrichs operator E_rad,rho=-v^{-2}partial_theta(v^2 partial_theta) is the form compression of E_nu/ell. Ground-state transformation gives

\[
\mathscr W_\rho E_{\rm rad,\rho}\mathscr W_\rho^{-1}
=-\partial_\theta^2+v''/v,\qquad
D_\rho^2:=\mathscr W_\rho^{-1}D^2\mathscr W_\rho
=E_{\rm rad,\rho}-M_{v''/v}.
\tag{6}
\]

The potential v''/v extends smoothly over both endpoints, because rho is a smooth central density. For Haar it is -1, giving the usual shifted Casimir n^2. The compensation in (6) is part of this candidate's definition, fixed from the actual marginal. It is **not** asserted to equal the full E_nu/ell, nor to be required by a YM Ward identity. The formal normalized radial derivative is partial_theta+cot theta+(rho'/2rho), followed by D_rho^{-1}; its bounded realization is B_rho=W_rho^{-1}BW_rho. The cotangent singularity makes its outputs generally nonsmooth at central holonomies, although they are genuine L2 boundary observables.

Fix the angle in **turns**, q=theta/(2pi). This normalization is independent of the desired multiplier: integer labels and the eigenangle circle pair by exp(2pi i n q)=exp(i n theta). Define

\[
C_\rho=\mathscr W_\rho^{-1}
  \big(\log D+B^*M_{\log q}B\big)\mathscr W_\rho.
\tag{7}
\]

No gamma function occurs in (4)–(7). The two logarithms measure the electric label and its dual normalized angle. This is a source/insertion ansatz with an explicit physical observable prescription, not a claim that YM uniquely selects it. Equivalently, in radians the operator is log(D/(2pi))+B* log(theta) B. Changing angle units and dual electric units inversely preserves their sum. Replacing q by c q while holding D fixed instead changes (7) by log(c) I, so normalization matters. The integer/angle duality is our independently stated scale convention; a claim of dynamical uniqueness of that convention would require more evidence.

**Domain and actual pairing.** Put

\[
\phi_n=\rho^{-1/2}\chi_n(P)I,\qquad
\mathscr C_\rho=\operatorname{span}\{\phi_n:n\ge1\}.
\]

These are smooth actual observables, an orthonormal basis of H_cl, with W_rho phi_n=s_n. The core lies in

\[
\mathscr W_\rho^{-1}\{u\in\operatorname{Dom}\log D:
                    (\log q)Bu\in L^2(0,\pi)\}.
\tag{8}
\]

Every finite cosine polynomial times log q is L2, so C_rho maps this core into the actual Hilbert space. It is symmetric and densely defined, hence closable. Its graph closure suffices here; essential self-adjointness or a positive closed quadratic form is **not** asserted. One may extend it by zero on H_cl's orthogonal complement in the full physical space, with domain C_rho's domain plus that complement. Nothing replaces the actual state.

For core vectors its exact state-dependent mixed response is

\[
\langle F,C_\rho G\rangle_\nu
=\langle\mathscr W_\rho F,(\log D)\mathscr W_\rho G\rangle_{d\theta}
 +\int_0^\pi\log q\,\overline{B\mathscr W_\rho F}\,B\mathscr W_\rho G\,d\theta.
\tag{9}
\]

Use of the unitary map in (9) evaluates a specified operator in nu; it is not a replacement of nu by Haar. The prescription includes rho in both operator and source. Like the earlier weight-transport control, it consequently works for every smooth positive marginal and does not identify special four-dimensional dynamics.

## 4. A proved archimedean mixed limit, including the contact term

Define one global packet law, for all compact smooth inputs, by

\[
F_R(f)=\sum_{n\ge1}n^{-1/2}f(\log(n/N))\phi_n,\quad N=e^R.
\tag{10}
\]

Each sum is finite and in the core. The definition differs from the previous S_R only by replacing the constant rho(0)^{-1/2} by the smooth multiplier rho(P)^{-1/2}. Localization at theta=0 proves

\[
\|F_R(f)-S_Rf\|_\nu\longrightarrow0.
\tag{11}
\]

This norm statement is used only for fixed bounded V_a, not to transfer unbounded-insertion limits. The latter are proved directly next.

**Theorem.** For all f,g in C_c^infinity(R),

\[
\lim_R\langle F_R(f),C_\rho F_R(g)\rangle_\nu
={1\over2\pi}\int_{\mathbb R}
 [\operatorname{Re}\psi(1/4+i\tau/2)-\log\pi]
 \overline{\widehat f(\tau)}\widehat g(\tau)\,d\tau.
\tag{12}
\]

**Proof, part I: a controlled cosine limit.** Set H_f(t)=t^{-1/2}f(log t), t>0. It is smooth and supported in [c,C] with c>0. Its even extension to the line is smooth. Let

\[
(\mathcal F_+H)(y)=2\int_0^\infty\cos(2\pi ty)H(t)\,dt.
\tag{13}
\]

This is the unitary involutive cosine transform on the half-line. If u_R^f=W_rho F_R(f), its rescaled cosine response satisfies the exact Poisson identity

\[
\sqrt{2\pi/N}\,(Bu_R^f)(2\pi y/N)
={2\over N}\sum_{n\ge1}H_f(n/N)\cos(2\pi ny/N)
=\sum_{k\in\mathbb Z}(\mathcal F_+H_f)(y+kN),
\quad0<y<N/2.
\tag{14}
\]

The transform on the right is Schwartz. For any M, the aliases k!=0 are O(N^{-M}) uniformly on [0,N/2], and the omitted primary tail y>N/2 has arbitrarily fast polynomial decay. The same estimates apply to mixed products in L1 with weight |log y|: at zero that weight is integrable and the functions are bounded; at infinity use their Schwartz bounds. Thus weighted convergence follows, not merely unweighted Plancherel convergence.

In the electric term, log n=R+log(n/N). In the angle term, log q=log y-R. Their R contributions cancel **exactly at finite R**, since B is an isometry. There is no divergent constant subtracted from a positive form in this argument: (7) is a fixed signed operator from the start. Riemann sums and (14) now give the limit

\[
\int_0^\infty\log t\,\overline{H_f(t)}H_g(t)dt
 +\int_0^\infty\log y\,
   \overline{\mathcal F_+H_f(y)}\mathcal F_+H_g(y)dy.
\tag{15}
\]

**Part II: compute, rather than assign, the multiplier.** Under H(t)->f(x)=e^{x/2}H(e^x) and the project's Fourier convention, (13) becomes

\[
\widehat{\mathcal F_+f}(\tau)=\gamma_+(\tau)\widehat f(-\tau),\qquad
\gamma_+(\tau)=\pi^{i\tau}
 {\Gamma(1/4-i\tau/2)\over\Gamma(1/4+i\tau/2)}.
\tag{16}
\]

One derives (16) by the Mellin cosine integral at z=1/2-i tau, initially with an exponential damping and then its limit, followed by the duplication/reflection identities. The oscillatory integral converges in the required strip; damping and the compact support of H justify the computation. This also verifies |gamma_+|=1 and gamma_+(tau)gamma_+(-tau)=1. These identities and the standard Mellin integrals are in [DLMF 5.9.6–7](https://dlmf.nist.gov/5.9#E6) and [5.5](https://dlmf.nist.gov/5.5).

Multiplication by log t becomes i partial_tau. The two differentiated input terms in log t+F_+ log y F_+ cancel because the transform reverses tau. The remaining multiplier is

\[
i\gamma_+(\tau)\gamma_+'(-\tau)
=i{\gamma_+'(\tau)\over\gamma_+(\tau)}
=\operatorname{Re}\psi(1/4+i\tau/2)-\log\pi.
\tag{17}
\]

The equality in the middle uses the derivative of gamma_+(tau)gamma_+(-tau)=1. Equations (15)–(17) prove (12), with its local constant fixed. \(\square\)

**Parity control.** Omitting B gives a sine transform in (14) and replaces 1/4 by 3/4 in (16)–(17). Thus the original character sine response alone gives the wrong gamma factor. The normalized electric derivative is an essential change of observable, not an invisible identification of sine and cosine channels. In the sine control the off-diagonal kernel is -exp(-3r/2)/(1-exp(-2r)). The cosine response has the requested exponent 1/2.

## 5. Off-diagonal kernel, logarithmic growth, and the full signed identity

The digamma integral [DLMF 5.9.16](https://dlmf.nist.gov/5.9#E16), with t=2r, gives

\[
m_+(\tau)-m_+(0)
=2\int_0^\infty(1-\cos(\tau r))
 {e^{-r/2}\over1-e^{-2r}}\,dr,
\qquad m_+(0)=\psi(1/4)-\log\pi.
\tag{18}
\]

The smooth difference cancels the 1/(2r) singularity. Fourier inversion of the difference form gives exactly the off-diagonal kernel -exp(-|x-y|/2)/(1-exp(-2|x-y|)). Equation (17), not the off-diagonal kernel alone, supplies the contact term. In particular m_+(0)=-EulerGamma-pi/2-3log2-log pi.

The sectorial digamma expansion [DLMF 5.11.2](https://dlmf.nist.gov/5.11#E2) yields

\[
m_+(\tau)=\log(|\tau|/(2\pi))+O(|\tau|^{-2}).
\tag{19}
\]

It also gives a global bound by a constant times log(2+|tau|). For the exactly pole-neutral probes f_lambda=lambda^{-2}(-partial_x^2+1/4)(e^{i lambda x}h), split the Fourier integral into |tau-lambda|<=|lambda|/2 and its complement. Schwartz decay bounds the complement and the differentiated-profile error; (19) on the first region gives

\[
Q_\infty[f_\lambda]=\|h\|_2^2\log|\lambda|+O_h(1).
\tag{20}
\]

This is a proved high-frequency statement for the limiting response. It does not assert uniformity in R and lambda simultaneously.

For each fixed a, (11) and the uniform boundedness of V_a imply that the mixed limit of F_R is the same as for S_R. Using the **actual** V_a, not its Haar conjugate, gives

\[
\lim_R\langle F_R(f),V_aF_R(g)\rangle_\nu
=a^{-1/2}\langle f,U_{\log a}g\rangle.
\tag{21}
\]

Combining (12) and finitely many instances of (21), then sending A to infinity, proves (1). For a given pair of compact tests the resulting arithmetic prime sum stabilizes. The construction and operators are fixed for all supports. This is an exact complete mixed *response* identity on the global pole-neutral space, with the pole term zero. It does not factor the response as <Jf,Jg>_OS. The audit's joint-cutoff theorem for raw S_R is not silently transferred through (11) to the unbounded infinite L.

## 6. All winding phases: the logarithmic response also fails

Let F_R^beta(f) use exp(i beta n) in (10), and let b(beta) in [0,pi] be the folded angle arccos(cos beta). At beta!=0 modulo 2pi the cosine response concentrates at b(beta)>0. There log q is smooth; its expectation tends to log(b(beta)/(2pi))<f,g>. The singularity at theta=0 contributes negligibly by repeated summation by parts. The representation logarithm still contributes R<f,g>+<f,xg>. Thus

\[
\langle F_R^\beta(f),C_\rho F_R^\beta(g)\rangle_\nu
=R\langle f,g\rangle+\langle f,xg\rangle
 +\log(b(\beta)/(2\pi))\langle f,g\rangle+o(1),
\quad\beta\ne0.
\tag{22}
\]

The Riemann-sum errors multiplied by R still tend to zero, since the coefficient envelopes are smooth and supported away from zero after scaling. At beta=pi this is concentration at the other endpoint with finite log q, so the same formula holds. At beta=0, (12) replaces (22): only there does the angular logarithm cancel R.

For distinct fixed phases the C_rho mixed response divided by R tends to zero. One can see this by localizing the angular multiplication away from zero and applying summation by parts to the electric coefficients; the identity-phase contribution is bounded by the weighted version of (14).

These conclusions extend to a fixed smooth multiplier of a packet. Its angular leading coefficient is its value at b(beta); in the sine or cosine coefficient description, its rapidly decreasing Fourier coefficients shift n by fixed integers. Taylor expansion gives O(N^{-1}) norm errors and O(N^{-1}log N) logarithmic errors. For the singular angular logarithm use the integrable-log bound in (14). This supplies the needed control beyond mere norm convergence.

Apply this observation to rho's smooth factors and the exact raw branching formula in the audit. For the original physical winding, all nonidentity roots carry positive weight, and

\[
\lim_R {1\over R}\langle V_aF_R(f),C_\rho V_aF_R(f)\rangle_\nu
={1\over a\rho(0)}\sum_{j=1}^{a-1}\rho(2\pi j/a)\,\|f\|_2^2>0,
\quad a>1, f\ne0.
\tag{23}
\]

Thus this candidate supplies a finite identity-phase archimedean response, but **not** a finite response on the winding-closed phase module. This includes winding by two, unlike the N^2 part of the current obstruction. Resetting log q separately at every root would change the operator and needs an independent definition and convergence proof. A single smooth correction cannot do it; a logarithm singular at the dense root set is not supplied by (7). No impossibility theorem for every measurable nonlocal correction is claimed.

## 7. Why these packets and fixed insertions do not produce a physical source limit

The preconditioned packets also converge weakly to zero and retain norm ||f||. Multiplication by the fixed smooth rho^{-1/2} preserves the weighted Sobolev estimates, so for every r>0 and nonzero f,

\[
\|(1+E_\nu)^{r/2}F_R(f)\|_\nu\asymp N^r.
\tag{24}
\]

They violate the fixed compact-source balls in the [finite-compatibility theorem](OFF_DIAGONAL_RIGIDITY_AND_COMPACT_SOURCE_EXISTENCE_20260924.md), with the domain distinctions in the [source-domain controls](SOURCE_DOMAIN_AND_WEIGHT_TRANSPORT_REVIEW_CONTROLS_20260925.md). No strong subsequence can retain their pairing.

**Fixed-insertion lemma.** Let u_R converge weakly to zero in a Hilbert space. If T is a fixed densely defined closable operator, u_R belongs to its domain, and ||Tu_R|| is bounded, then Tu_R converges weakly to zero. In particular a strong limit must be zero.

**Proof.** For v in the dense domain of T*, <v,Tu_R>=<T*v,u_R> tends to zero. Boundedness extends this to all v. \(\square\)

This includes fixed bounded electric parity operations, fixed smooth weight transport, and any proposed fixed closable square-root source response whose norms stay finite. A compact operator sends the raw weakly escaping packets strongly to zero. A divergent inserted norm is not an alternative finite source. These are general statements in the physical Hilbert space, independent of the arithmetic target.

**Control delimiting the obstruction.** An R-dependent unitary can preserve a nonzero strong limit: in the same class space, for integer R=k, define the smooth packets u_k=phi_{k+1}; the unitary exchanging phi_1 and phi_{k+1} maps u_k to phi_1. This is a control, not a candidate YM source law or a third mechanism. Such operators are not fixed and do not establish any required winding relations. A scale-dependent physical recentering is not excluded by the lemma, but would have to preserve the actual insertion/branching identities and admissible domains. The present calculation supplies no such occurrence theorem.

## 8. Positivity: a fixed signed response is not a renormalized norm

First the archimedean response alone is not nonnegative even on the global pole-neutral class. If h is a nonzero smooth compact bump, h_L(x)=L^{-1/2}h(x/L) and f_L=(-partial_x^2+1/4)h_L, then f_L is exactly pole neutral. Its Fourier mass concentrates near zero. Dominated convergence using (19) gives

\[
Q_\infty[f_L]\longrightarrow {m_+(0)\over16}\|h\|_2^2<0.
\tag{25}
\]

Hence there is no positive square root of this limiting response on the required domain. The prime terms might change its sign; this argument does not assert that the complete Weil form is negative.

Second, audit §6 proves that the positive infinite prime form has only the zero vector in its domain. At the packet level its finite cutoffs equal, after R->infinity,

\[
C_A^\rho\|f\|_2^2+Q_{{\rm prime},A}[f],\quad
C_A^\rho=\sum_{2\le a\le A}\Lambda(a)
 (1+\rho_a(0)/\rho(0))\longrightarrow+\infty.
\tag{26}
\]

The nonzero pole-neutral tests have nonzero L2 norm, so the two moment constraints do not remove (26). Adding the finite response (12) does not remove it either. A scalar normalization keeping (26) bounded must tend to zero; for fixed compact inputs it then erases the stabilized prime cross term. Subtraction restores a signed expression, whose positivity is a fresh question. The cancellation of R in (15) concerns two parts of an already signed operator and offers no positive prescription for the distinct A divergence.

An additional operator control makes the loss of positivity concrete. Define the state-transported character operation on this same class space by Vtilde_a phi_n=phi_{an}. It is explicitly different from the original V_a: Vtilde_a=rho^{-1/2}V_a rho^{1/2}. In its basis take u=phi_1+t phi_p with p prime, and cutoff A>=p. Then

\[
\langle u,(\mathcal L_A^{\sim}+(\mathcal L_A^{\sim})^*)u\rangle
=2t\log p\quad(t\in\mathbb R),
\]

whereas <u,C_rho u>=t^2 log p+O_t(1). The latter follows because the integral of log q times cos^2(p theta) stays bounded, and its mixed Fourier coefficient with cos theta is O(1/p). Choosing t=1 makes the signed completion tend to minus infinity. This is a rigorous same-state control against automatic operator positivity on the full class core. It is **not** a counterexample on the limiting pole-neutral source image and is **not** a claim about the original V_a's full-core sign. The distinction of adjoints is essential.

No subtraction or quotient with an independently proved positive completed limit has been established. Asserting positivity of (1) on every pole-neutral input would assert the outstanding Weil-positivity problem, not follow from OS positivity of nu.

## 9. What is proved and what remains

| Statement | Status and assumptions |
|---|---|
| Weighted winding adjoints, branching, raw prime distributional limit | Rederived in the audit; fixed smooth positive finite-slab state, fixed tests/phases; no RH |
| Opposite current at pi and dense-phase obstruction | Proved for the full smooth electric–Wilson currents (2); does not exclude all nonlocal observables |
| Exact archimedean signed response (12) | Proved for the specified compressed/compensated radial electric prescription (4)–(10), using Poisson estimates and Mellin cosine analysis |
| Contact, separated kernel, high-frequency growth | All fixed by (17)–(20); no contact calibrated to desired moments |
| Complete signed mixed limit (1) | Proved with the stated iterated limits and original V_a; not a positive-source identity |
| Common finite winding-closed response | Fails for both candidates: (3), (A7), and (23) |
| Positive infinite prime differences | Domain only zero on H_cl; no valid positive renormalization supplied |
| Physical occurrence by packet limit or fixed insertion | Excluded in the scoped sense of (24) and the fixed-insertion lemma |
| A different admissible YM law realizing Q as an OS pairing | Open; neither an impossibility theorem for all YM sources nor a successful occurrence theorem |

The strongest established result is therefore a complete signed mixed response with its archimedean normalization derived from an independent finite-state observable prescription, together with explicit reasons why it is not yet the sought positive physical source. A next successful construction must simultaneously provide a finite response on all required winding phases, a positive completion of the prime contribution without formal subtraction, and occurrence in the original physical representation (or explicitly justify a changed model). The earlier three-constant determination theorem and compact finite-compatibility theorem remain valid tools, but their source feasibility and compactness hypotheses are not verified by these packets.

## 10. Reproduction and source checks

The [control script](../numerics/check_archimedean_response.py) and [small record](../numerics/records/archimedean-response-20260925.json) use NumPy only. They compare the finite cosine/sine log-angle matrix with an independent Fourier/digamma integral, check the local constant and high-frequency asymptotics, examine nonidentity phases and the pi-current sign, and check the explicit negative full-core control. The prescribed nonconstant density checks a finite physical pairing; it is not a simulation of the Wilson state. Proofs above, not floating values, justify the limits. No large arrays or third-party PDFs are saved in the repository.

Primary-source checks were limited to DLMF's displayed cosine/sine Mellin integrals, gamma identities, digamma integral and asymptotic, and Burnol's definition and spectral interpretation of the conductor operator (PDF pages at zero-index 3 and 9). We independently derive the normalization in (16)–(17). Nothing in those sources establishes a YM occurrence theorem or the positivity of (1). The new analysis has not received independent human review.
