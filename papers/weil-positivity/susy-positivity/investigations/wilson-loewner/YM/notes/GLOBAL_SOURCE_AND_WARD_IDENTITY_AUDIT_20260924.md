# Global YM sources: growth, dynamics, uniqueness, and compactness

Date: 24 September 2026, America/New_York.  
Prepared for Edward Baker with substantial LLM assistance.  
Model: GPT-6 (Codex). Reasoning effort: not exposed; not inferred.  
Status: analytical research continuation; elementary propositions with proofs and a conditional existence criterion. Not independently reviewed. No global YM realization or RH proof is claimed.

This continues [the global existence proposal](YM_EXISTENCE_ASSUMED_OS_AND_GLOBAL_SCOPE_20260924.md). The [project outline](../PROJECT_OUTLINE.md) supplies the full arithmetic and physical background. OS positivity is an accepted hypothesis. The task here is to identify restrictions and an existence mechanism that apply to all compact supports, rather than extend a list of numerical support lengths.

## 1. Fixed target and normalization

Let \(\mathcal D=C_c^\infty(\mathbb R)\) and
\[
\mathcal D^0=\{f\in\mathcal D:\int e^{x/2}f(x)\,dx=\int e^{-x/2}f(x)\,dx=0\}.
\]
Write \(U_a f(x)=f(x-a)\), use inner products antilinear in the first argument, and set \(\widehat f(\tau)=\int e^{-i\tau x}f(x)\,dx\). For \(\operatorname{supp}f\subset I_L=(-L/2,L/2)\), the pole-neutral Weil form is
\[
Q[f]=\frac1{2\pi}\int a_\Gamma(\tau)|\widehat f(\tau)|^2\,d\tau
-2\sum_{m\log p<L}(\log p)p^{-m/2}\operatorname{Re}\langle f,U_{m\log p}f\rangle,
\tag{1}
\]
where
\[
a_\Gamma(\tau)=\operatorname{Re}\psi(1/4+i\tau/2)-\log\pi
=\log\frac{|\tau|}{2\pi}+O(|\tau|^{-2})
\quad (|\tau|\longrightarrow\infty).
\tag{2}
\]
Here \(\psi=\Gamma'/\Gamma\). The form on all of \(\mathcal D\) has the additional pole term specified in the outline. Polarization defines \(Q(f,g)\). Formula (1) is continuous on each smooth compact-support test space, and
\[
Q(U_a f,U_a g)=Q(f,g),\qquad a\in\mathbb R.
\tag{3}
\]
The pole-neutral space is translation invariant. In (1), translating the interval does not change which prime-power shifts can overlap the supports.

The target is a single continuous linear map into a specified YM OS source space,
\[
J:\mathcal D^0\longrightarrow\mathcal H_{\mathrm{YM}},\qquad
\langle Jf,Jg\rangle_{\mathrm{OS}}=Q(f,g).
\tag{4}
\]
The model, state, source prescription, and arithmetic operations are fixed across supports. The map must have the stated observable interpretation; an arbitrary embedding into a Hilbert space is not the intended conclusion. All results below hold without assuming the sign of \(Q\).

## 2. Exact pole-neutral probes at arbitrarily high frequency

Set \(T=-\partial_x^2+1/4\). Integration by parts gives
\[
T(C_c^\infty(I_L))\subset\mathcal D^0\cap C_c^\infty(I_L).
\]
In fact this is equality. If \(f\) is pole neutral, the solution
\[
h(x)=\int e^{-|x-y|/2}f(y)\,dy
\]
satisfies \(Th=f\). Its two exterior tails vanish by the two moment constraints. It is smooth and supported in the convex hull of the support of \(f\). This gives a useful exact parametrization without projection errors or support enlargement.

Fix nonzero \(h\in C_c^\infty(I_L)\), and for \(\lambda>1\) define
\[
f_\lambda=\lambda^{-2}T(e^{i\lambda x}h)
=e^{i\lambda x}\left(h-\frac{2i}{\lambda}h'
+\frac{h/4-h''}{\lambda^2}\right).
\tag{5}
\]
Every \(f_\lambda\) is exactly pole neutral and has the same fixed support. Its \(L^1,L^2,L^\infty\) norms are bounded independently of \(\lambda\), and \(\|f_\lambda\|_2\to\|h\|_2\).

**Proposition 1.** For this family,
\[
Q[f_\lambda]=\|h\|_2^2\log\lambda+O_{h,L}(1).
\tag{6}
\]

**Proof.** Write the parenthesis in (5) as \(h_\lambda\). It converges to \(h\) in every smooth seminorm with fixed support, at rate \(O(\lambda^{-1})\), and its Fourier transforms have uniform Schwartz bounds. In the gamma integral substitute \(\tau=\lambda+\eta\). For \(|\eta|\le\lambda/2\), (2) gives \(a_\Gamma(\lambda+\eta)=\log\lambda+O(1)\), uniformly. The complementary integral, including the region where \(\lambda+\eta\) is near zero, is bounded by the uniform Schwartz tails and the bound \(|a_\Gamma(t)|\le C+\log(2+|t|)\). Plancherel and \(\|h_\lambda\|_2^2=\|h\|_2^2+O(\lambda^{-1})\) give the leading term in (6). There are finitely many prime terms at fixed \(L\), and their total absolute value is at most
\[
2\|f_\lambda\|_2^2\sum_{m\log p<L}(\log p)p^{-m/2}=O_{h,L}(1).
\]
There is no pole term on this family. This proves (6). ∎

The estimate concerns high frequency at one fixed support length. It is an unconditional necessary test for any global source ansatz, not a small-\(L\) positivity certificate and not a uniform lower bound on arbitrary tests.

## 3. Ordinary smearing of bounded loops cannot be the required source

**Proposition 2.** Suppose a proposed source has the form
\[
Jf=\int f(x)A(x)\,dx
\tag{7}
\]
as a Bochner integral in the OS Hilbert space, where \(A\) is strongly measurable and \(\int_I\|A(x)\|_{\mathrm{OS}}dx<\infty\) on every compact interval. Then it cannot satisfy (4).

**Proof.** On the fixed support of (5),
\[
\|Jf_\lambda\|_{\mathrm{OS}}
\le\|f_\lambda\|_\infty\int_{I_L}\|A(x)\|_{\mathrm{OS}}dx=O(1).
\]
This contradicts (6). ∎

This applies directly to ordinary locally integrable smearing of the existing slice loops \(Q_x\), whose reflected norm is one. It also applies to a single finite-norm vector orbit \(A(x)=V(x)v\) under a unitary group, and to any finite sum of such ordinary smearing prescriptions with locally integrable norms.

**Scope of the exclusion.** It excludes (7), not YM realization. A continuous distribution-valued source, a source involving derivatives of the input, or an infinite sequence of insertions with controlled singular limits is not covered by the hypothesis. Those possibilities need their own domain and norm analysis; merely calling a bounded loop family a generalized source does not change (7). The earlier rejection of an ordinary \(L^2\)-bounded source is therefore sharpened into a test of the actual normalized-loop ansatz.

The source norm must grow like \(\sqrt{\log\lambda}\) on (5). Smooth-test continuity permits this. Demanding a source bound solely in terms of \(\|f\|_\infty\), \(\|f\|_1\), or \(\|f\|_2\) would incorrectly exclude every exact realization.

## 4. The arithmetic translation action cannot be Euclidean decay

Equation (3) has a direct implication. If (4) holds, define on the source image
\[
V(a)Jf=J(U_a f).
\tag{8}
\]
This is well defined: a null source remains null by (3). It extends to a unitary group on \(\overline{J\mathcal D^0}\). Strong continuity follows from test-space continuity of translations and of \(J\). This is a necessary consequence of an exact realization, not a construction of one.

**Proposition 3.** Suppose the YM model additionally has a physical Euclidean transfer semigroup \(e^{-aH}\), \(H\ge0\). There is no continuous map satisfying both (4) and
\[
J(U_a f)=e^{-aH}Jf,\qquad a\ge0.
\tag{9}
\]

**Proof.** Equations (3), (4), and (9) imply \(\|e^{-aH}Jf\|=\|Jf\|\). For any \(a>0\), the spectral theorem gives
\[
0=\int_{[0,\infty)}(1-e^{-2aE})\,d\mu_{Jf}(E),
\]
so \(Jf\in\ker H\). Hence \(J(U_a f)=Jf\). Differentiating at zero in the test topology gives \(J(f')=0\). Now put \(r_\lambda=(i\lambda)^{-1}f_\lambda'\). This remains pole neutral, and it has the form \(e^{i\lambda x}(h+O(\lambda^{-1}))\), with the error controlled in all smooth seminorms before modulation. The proof of Proposition 1 gives
\[
Q[r_\lambda]=\|h\|_2^2\log\lambda+O(1)>0
\]
for sufficiently large \(\lambda\), whereas \(Jr_\lambda=0\). Contradiction. ∎

This proposition assumes a transfer semigroup in addition to OS positivity. The standard lattice transfer-matrix setting is background, not something established by OS positivity alone; see [Lüscher (1977)](https://link.springer.com/article/10.1007/BF01614090), whose publisher abstract was checked.

The logarithmic arithmetic coordinate therefore needs a different action: for example, an independently justified spatial, scale, or internal unitary action on the source sector. This does not prove that any such candidate works. Nor does it exclude a physical causal source/readout realization using a different relation between its time variable and the arithmetic source parameter. The existing Loewner-capacity transport is not already a stationary representation of \((\mathbb R,+)\); its two-parameter unitary transport identity alone does not supply (8).

## 5. Full finite-lattice Ward identities determine the state, not the source map

Fix a finite Wilson lattice and write its compact configuration manifold as \(M=SU(N)^E\), with normalized product Haar measure \(m\) and smooth real action \(S\). Let \(D_{\ell,a}\) be a left-invariant derivative on link \(\ell\) in a Lie-algebra direction. The full integration-by-parts equations are
\[
\int D_{\ell,a}F\,d\mu=\int F D_{\ell,a}S\,d\mu,
\qquad F\in C^\infty(M).
\tag{10}
\]

**Proposition 4.** A normalized positive Borel measure \(\mu\) satisfying (10) for every smooth \(F\), link, and direction must be the Wilson measure \(Z^{-1}e^{-S}m\).

**Proof.** Define the finite positive measure \(d\nu=e^S d\mu\). Apply (10) to \(F=e^S h\):
\[
\int D_{\ell,a}h\,d\nu
=\int D_{\ell,a}(e^S h)\,d\mu
-\int e^S hD_{\ell,a}S\,d\mu=0.
\]
Thus \(\nu\) is invariant under each one-parameter left-translation flow. These flows generate the connected product group \(SU(N)^E\). Uniqueness of normalized Haar measure gives \(\nu=c m\), and normalization of \(\mu\) gives the claim. No density for \(\mu\) was assumed beforehand. ∎

This is an elementary finite-dimensional uniqueness argument, not a new solution of the continuum YM problem. It makes the role of dynamical identities precise. A truncated list of Wilson-loop equations is not the full hypothesis (10). In particular, finite-N trace identities do not turn a finite selected loop list into every smooth test equation.

Even the full conclusion fixes only the state. It does not identify \(f\mapsto Jf\), the arithmetic action on those sources, or their Weil pairing. A bootstrap can therefore solve the YM state problem and still leave the RH bridge untouched. On an already specified finite Wilson lattice, direct use of that known state is cleaner than introducing free moments and then reconstructing the same state.

## 6. What a global pairing-uniqueness proof must actually establish

Let \(\mathcal V=\overline{\mathcal D^0}\otimes\mathcal D^0\), with the projective locally convex tensor topology; the bar denotes conjugate vector space, not completion. Continuous sesquilinear pairings are continuous linear functionals on \(\mathcal V\). Let \(\mathcal R\) be the closed span of tensors expressing independently proved source Ward/intertwining relations.

**Sufficient uniqueness criterion.** If \(\mathcal V/\mathcal R\) is one dimensional, one nonzero normalization fixes a continuous pairing annihilating \(\mathcal R\). More generally, finite quotient dimension requires that many independent normalizations. The proof is simply linear duality on the quotient. An involution-compatible formulation can restrict to Hermitian pairings, but must not assume their positivity.

To use this criterion, one must prove three different statements:

1. A nonzero source module with these relations occurs in the chosen YM observable sector.
2. The relations and normalizations determine its pairing in the class of continuous Hermitian forms of unknown sign.
3. The explicit arithmetic form satisfies the same relations and normalizations.

OS positivity then supplies the sign. Writing relation tensors from the desired equality itself does not establish statement 1 or derive any new information.

There is a useful underdetermination test. For any real even Schwartz function \(a\),
\[
R_a(f,g)=\frac1{2\pi}\int a(\tau)\overline{\widehat f(\tau)}\widehat g(\tau)\,d\tau
\tag{11}
\]
is a continuous Hermitian pairing invariant under common translations and reflection \(x\mapsto-x\). It is bounded in ordinary \(L^2\). Thus \(Q+R_a\) preserves those symmetries and the leading logarithmic growth. Imposing any finite list of pairing normalizations gives only finitely many real linear constraints on the infinite-dimensional space of such \(a\), leaving a nonzero choice. A nonzero \(a\) gives a nonzero pairing on \(\mathcal D^0\): use \(f=Th,g=Tk\), and density of Fourier transforms of compactly supported smooth functions in \(L^2\) to test the multiplier \((\tau^2+1/4)^2a(\tau)\).

Consequently translation/reflection covariance, logarithmic leading behavior, and finitely many calibration values do not uniquely identify the Weil form. This is an obstruction to that proposed uniqueness argument, not a claim that every perturbed form is realized in YM. A mixed arithmetic/dynamical identity carrying more information is still needed.

## 7. A nonconstructive limit that does preserve the pairings

The previous proposal warned that weakly convergent source vectors can lose norm. The following gives a concrete sufficient replacement in a fixed YM Hilbert space.

**Proposition 5: compact source control.** Let \(\mathcal H\) be the fixed OS Hilbert space and let \(\mathcal K\hookrightarrow\mathcal H\) be an injective compact continuous inclusion of Hilbert spaces. Suppose linear maps \(J_n:\mathcal D^0\to\mathcal K\) obey:

- For every compact support interval \(I\), there are \(C_I\) and a finite smooth seminorm \(p_I\), independent of \(n\), such that \(\|J_nf\|_{\mathcal K}\le C_I p_I(f)\) for all \(f\in\mathcal D^0\) supported in \(I\).
- On a countable set of tests whose linear span is dense in each space of tests supported in an exhausting sequence of compact intervals, \(\langle J_nf,J_ng\rangle_{\mathcal H}\to Q(f,g)\) for every selected pair.

Then some subsequence converges in \(\mathcal H\) on every test to a continuous linear map \(J:\mathcal D^0\to\mathcal H\) satisfying (4). Each \(Jf\) belongs to \(\mathcal K\), with the same local seminorm bound.

**Proof.** The first hypothesis and compact inclusion make each selected vector sequence precompact in \(\mathcal H\). A diagonal subsequence converges on the countable set and hence on its finite linear span. The uniform local seminorm estimates extend the limit continuously to every fixed-support test space and imply convergence there on each individual test. Choosing the countable dense family compatibly through the exhausting intervals makes these extensions agree. They define a map on \(\mathcal D^0\) with its usual inductive-limit test topology. Strong \(\mathcal H\) convergence preserves inner products; continuity of \(Q\) extends the identity from the dense family to all tests. For each fixed test, boundedness in the Hilbert space \(\mathcal K\) gives a weakly convergent subsubsequence there. Its image agrees with the unique strong \(\mathcal H\) limit, proving membership and the lower-semicontinuous bound in \(\mathcal K\). ∎

This is a sufficient criterion, not a claim that the required sequence exists. The unresolved hypothesis is global approximation with uniform source control. If only partial maps on finite test lists are produced, a compatible extension theorem with these bounds must still be proved. Matching a few finite Gram matrices does not establish the hypothesis. Bounds may depend on support and derivatives; they need not be uniform in \(L\) or bounded in ordinary \(L^2\).

This criterion addresses an actual finite-regulator model. In the existing boundary construction,
\[
\mathcal H=L^2_{\mathrm{cov}}(\nu;\operatorname{End}\mathbb C^N),
\quad d\nu=Z^{-1}\Omega^2dU
\]
on the compact central-slice link manifold. The finite Wilson action is smooth, and differentiation under the compact half-slab integral shows \(\Omega\) is smooth and strictly positive. Take \(\mathcal K\) to be its gauge-covariant Sobolev subspace \(H^s\), \(s>0\). Equivalence of the smooth positive weighted norms and compact Sobolev inclusion on a compact manifold give \(\mathcal K\hookrightarrow\mathcal H\) compactly. Gauge covariance is a closed condition. Thus a concrete stronger source norm is available without changing the state or adjoining matter.

For integer \(s\), sums of squared link-derivative norms give a useful Sobolev control. The corresponding weighted adjoints must be retained: for a Haar-divergence-free derivative \(D\),
\[
D^*=-D-2D\log\Omega
\tag{12}
\]
on smooth boundary functions in \(L^2(\nu)\). Treating \(D\) as skew-adjoint in the weighted state would omit the dynamical term. The full covariant derivative family, with its color indices contracted appropriately, is the natural object; an individual Lie-algebra component need not preserve the gauge-covariant sector.

Admissible source relations must also survive the limit. Bounded operators on \(\mathcal H\) pass through strong convergence. For an unbounded insertion, one needs convergence or weak compactness of its graph data and closedness of its graph; bounded source norms alone are not a substitute. Merely belonging to \(\mathcal K\) does not supply the missing arithmetic intertwining.

## 8. Consequences for the next investigation

The current best-defined candidate is a generalized source in the existing YM boundary completion, assembled from covariant loop functions and properly adjointed link/field insertions, with local smooth-test bounds. This names a source pool, not a discovered arithmetic module. Its reference-color sector remains explicit; no bulk matter or continuum limit has been silently introduced.

The next task is to specify one native source action and test its relations before choosing any numerical support windows:

1. Choose actual operators on the boundary source core, their adjoints, and the intended action on \(\mathcal D^0\). In particular, identify what implements logarithmic translation. Proposition 3 rules out identifying it with Euclidean decay; the existing contour transport does not supply stationarity by itself.
2. Derive the mixed relations among these operators from the Wilson state and observable algebra, retaining the \(D\log\Omega\) term and any domains. Determine whether they constrain the prime-power contribution jointly with the archimedean term.
3. Audit the space of pairings obeying those relations. An infinite family of perturbations such as (11) would show that a proposed relation set is insufficient. A rigidity theorem would identify the needed nonconstructive occurrence problem.
4. If approximation is the practical route, seek estimates in the concrete \(\mathcal K\) norm of Proposition 5 and a theorem producing approximants for arbitrary finite test/identity sets. This addresses norm preservation and compatibility from the outset.

The additional native causal-transfer objective remains in scope, but its preparation, physical time, readout, and energy identities must be stated separately. The present results do not identify that transfer.

No arithmetic module, determining mixed Ward relation, or uniformly controlled approximating family has yet been found. What this continuation establishes is narrower and useful: two precisely scoped source/action exclusions, full finite-state uniqueness, a test for insufficient pairing identities, and a nonconstructive limit criterion in the actual finite YM boundary space. These replace the unspecific instruction to try larger \(L\) with explicit mathematical obligations.

## 9. References and verification scope

- [Connes–Consani, *Weil positivity and Trace formula: the archimedean place*, Appendices B–C](https://arxiv.org/html/2006.13771v1): normalization and RH-sufficient prescribed Mellin vanishing. The pole-neutral logarithmic class above corresponds to vanishing at Mellin arguments 0 and 1.
- [Lüscher, *Construction of a selfadjoint, strictly positive transfer matrix for Euclidean lattice gauge theories*](https://link.springer.com/article/10.1007/BF01614090): transfer-matrix background; publisher abstract checked, not the full proof.
- [Finite-slab reflection and discrete hierarchy](FINITE_SLAB_REFLECTION_AND_DISCRETE_HIERARCHY_20260924.md): the exact boundary space and normalized loop vectors used here.
- [First interacting slab test](FIRST_INTERACTING_SLAB_TEST_AND_CONTINUATION_20260924.md): the existing numerical experiment, distinct from these analytic arguments.

The propositions were checked by the displayed analytic arguments, including exact pole neutrality, Fourier normalization, the finite prime bound, the spectral-theorem step, the integration-by-parts sign, and the strong-limit argument. No new simulation was run. These are research-note deductions using standard tools, with no claim of literature novelty or independent verification.
