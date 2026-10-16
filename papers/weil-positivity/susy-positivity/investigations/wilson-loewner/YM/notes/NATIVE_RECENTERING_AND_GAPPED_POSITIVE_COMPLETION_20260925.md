# Native electric recentering and the limits of a gapped positive completion

25 September 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance.

Model exposed: GPT-6 (Codex). Exact deployed variant and reasoning effort: unavailable; not inferred.

Status: analytical continuation with proofs and small floating controls, not independent human verification. No implication from four-dimensional YM existence and mass gap to RH is established. All OS axioms and a physical mass gap are allowed assumptions for the explicitly identified continuum statements. The main construction remains in the same fixed four-dimensional SU(2) Wilson slab and its actual state.

## 1. Concrete results and the two mechanisms

This follows the [critical review](../reviews/ELECTRIC_PARITY_RESPONSE_CRITICAL_REVIEW_20260925.md) and its [bounded winding-occurrence obstruction](BOUNDED_WINDING_OCCURRENCE_OBSTRUCTION_20260925.md). Two source mechanisms are tested.

1. **Long-time evolution by the full electric–Wilson current.** A specific scale-dependent unitary, already defined by the physical current, converts the identity-phase packets into a nonzero strong limit in the original boundary Hilbert space. Its exact pairing is ordinary L2. Winding produces a computable weak limit with a strictly positive norm defect. This is an actual source construction, but not a Weil source.
2. **Positive constrained energy, with a coercive term.** Minimizing the positive prime-difference energy over unresolved physical vectors is a Schur-complement prescription, not formal subtraction. Every finite-cutoff prescription has an actual positive Hilbert pairing. Its completed value diverges for every nonzero fixed bounded readout when a uniform coercive bound is present. A physical gap supplies such a bound only on a properly identified vacuum-orthogonal sector.

There is also a source-domain result relevant to the first mechanism: no fixed closable operator applied to an L2-isometric source law can produce the complete Weil norm on the global pole-neutral class. If the form is positive, its discrete spectral measure makes it nonclosable in the ordinary input-L2 topology. This does not prohibit a source law defined continuously only on the smooth-test space.

Section 8 gives a useful consequence of an additional natural physical assumption, local phase-space compactness: the compact existence criterion can use actual bounded local observables followed by Euclidean preparation in an assumed continuum YM vacuum. Its arithmetic finite-feasibility hypothesis remains unproved.

## 2. Full-state current, flow, and domains

Keep the spatial \(6^3\) lattice, time slices -2 through 2, beta \(8/5\), theta angle zero, and four-link plaquette P. On the full compact central-slice link manifold M put

\[
d\nu=w\,dm,
\qquad w=Z^{-1}\Omega^2>0,
\qquad \mathcal H=L^2_{\rm cov}(M,\nu;\operatorname{End}\mathbb C^2).
\tag{1}
\]

The Haar measure m is normalized. The scalar class sector consists of \(F(P)I\), and its actual marginal is \(\rho(g)dg\). Both w and rho are fixed smooth positive functions. Write \(X=\tfrac12\operatorname{tr}P=\cos\theta\), \(\ell=4\), and retain the full weighted electric operator \(E_\nu\).

The current and its geometric vector field are

\[
A_\nu=\frac{i}{2\ell}[E_\nu,X]
=-i\left(Y+\tfrac12\operatorname{div}_\nu Y\right),
\qquad Y=\ell^{-1}\nabla X.
\tag{2}
\]

The complete smooth gauge-equivariant flow \(\Phi_t\) of Y defines the self-adjoint generator and its unitary group on the full covariant Hilbert space:

\[
\mathscr U_t=e^{itA_\nu},\qquad
\mathscr U_t F(U)=j_t(U)^{1/2}F(\Phi_tU),
\quad \Phi_t^*\nu=j_t\nu.
\tag{3}
\]

This is not a replacement by a radial compression. Smooth covariant functions form the initial observable core, and the complete-flow representation specifies the closed generator's domain. It agrees with (2) there, including the full state drift.

Because the four plaquette links are distinct,

\[
|\nabla\theta|^2=\ell,\quad
Y\theta=-\sin\theta,\quad
\operatorname{div}_mY=-3\cos\theta.
\]

Thus, away from the two central holonomies,

\[
\tan(\theta_t/2)=e^{-t}\tan(\theta/2),\qquad
j_t=\left(\frac{\sin\theta_t}{\sin\theta}\right)^3
\frac{w(\Phi_tU)}{w(U)}.
\tag{4}
\]

The factor 3 follows from the SU(2) fundamental Casimir in the existing normalization, equivalently \(\Delta_mX=-3\ell X\). The sign in (3) is important: positive t contracts the argument theta toward zero and expands the support of a packet initially concentrated there.

For \(0\leq\theta<\pi\), the full trajectory has a limit \(\Phi_\infty U\) with \(P(\Phi_\infty U)=I\). Indeed

\[
\|Y\|=\sin\theta/\sqrt\ell,
\qquad \int_t^\infty\|Y(\Phi_sU)\|ds=\theta_t/\sqrt\ell.
\tag{5}
\]

Finite remaining length gives a Cauchy trajectory on compact M. This proves convergence of the other link variables too, not only of P. The set P=-I has measure zero. Set \(w_\infty(U)=w(\Phi_\infty U)\) almost everywhere. It is measurable, bounded above and below by the same positive bounds as w. No smoothness assertion about its extension over P=-I is needed.

## 3. A strong physical source limit

For \(f\in\mathcal D=C_c^\infty(\mathbb R)\), let \(N=e^R\), and use the already defined raw identity-phase packets

\[
S_Rf=\rho(0)^{-1/2}\sum_{n\geq1}n^{-1/2}f(\log(n/N))\chi_n(P)I.
\tag{6}
\]

Define a single global prescription

\[
J_Rf=\mathscr U_RS_Rf.
\tag{7}
\]

The time R depends on the representation scale, not on the input support. Each finite-R vector is a smooth actual boundary observable in the same state. The electric-current parameter is not physical Hamiltonian time and is not assigned that interpretation.

Put \(y=2\tan(\theta/2)\), \(H_f(t)=t^{-1/2}f(\log t)\), and

\[
(J_Hf)(\theta)=\frac{(1+y^2/4)^{3/2}}{y}
\int_0^\infty H_f(t)\sin(yt)\,dt.
\tag{8}
\]

The endpoint y=0 is understood by its limit. The integral is well defined because \(H_f\) is smooth with compact support away from zero.

**Theorem 1 (native recentering).** For every f in the global test space,

\[
J_Rf\longrightarrow J_{\rm rec}f
\quad\text{strongly in }\mathcal H,
\]
\[
(J_{\rm rec}f)(U)=
\sqrt{\frac{w_\infty(U)}{\rho(0)w(U)}}\,(J_Hf)(\theta(U))I,
\tag{9}
\]

and its exact actual reflected pairing is

\[
\langle J_{\rm rec}f,J_{\rm rec}g\rangle_\nu
=\langle f,g\rangle_{L^2(\mathbb R)}.
\tag{10}
\]

Consequently it extends to an isometric source map from L2 into the physical boundary completion. No assertion that every limiting source is a finite Wilson polynomial or a bounded pointwise observable is required.

**Proof.** First use Haar measure as a calculation of the geometric flow, and omit \(\rho(0)^{-1/2}\) in (6); call that packet \(\sigma_Rf\). The radial unitary

\[
(\mathcal RF)(y)=\sqrt{2/\pi}\,
\frac{y}{(1+y^2/4)^{3/2}}F(\theta(y))
\]

maps the Haar class space onto \(L^2(\mathbb R_+,dy)\). The Haar version of (3) becomes \(h(y)\mapsto e^{-t/2}h(e^{-t}y)\). Therefore the exact recentered profile is

\[
\mathcal R\mathscr U_R^0\sigma_Rf(y)
=\sqrt{2/\pi}\frac{1}{N\sqrt{1+(y/2N)^2}}
\sum_{n\geq1}H_f(n/N)
\sin\bigl(2n\arctan(y/(2N))\bigr).
\tag{11}
\]

On every compact y interval, this converges uniformly by Riemann sums to the unitary half-line sine transform

\[
\mathcal SH_f(y)=\sqrt{2/\pi}\int_0^\infty H_f(t)\sin(yt)dt.
\]

The squared global norm of (11) is exactly \(\sum_n N^{-1}|H_f(n/N)|^2\), which converges to \(\|H_f\|_2^2=\|f\|_2^2\). Local convergence and bounded norms give weak convergence on the whole half-line, by density of compactly supported L2 tests. Sine Plancherel gives the same norm for the limiting function. Weak convergence plus norm convergence proves strong convergence, without an unproved uniform tail estimate. Applying \(\mathcal R^{-1}\) gives (8).

For the actual state, (4) yields exactly

\[
\mathscr U_R S_Rf
=\rho(0)^{-1/2}
\sqrt{w(\Phi_RU)/w(U)}\,
\mathscr U_R^0\sigma_Rf.
\]

The multiplier converges almost everywhere to \(\sqrt{w_\infty/w}\) and is uniformly bounded. Norm equivalence transfers the geometric strong convergence from Haar to nu. Dominated convergence applied to the fixed limiting vector handles the multiplier difference. This proves (9) in the full physical space, without supposing that the full current preserves the original class subspace.

Unitarity and the audited raw packet pairing give
\(\langle J_Rf,J_Rg\rangle_\nu=\langle S_Rf,S_Rg\rangle_\nu\to\langle f,g\rangle\). Strong convergence proves (10). \(\square\)

This overcomes weak escape for the identity component by a particular native scale-dependent unitary. It is not a counterexample to either the fixed-insertion lemma or the bounded winding-occurrence theorem: the operator depends on R, and it does not recover the full winding module strongly with unchanged windings.

It also does not solve the arithmetic problem. The norm in (10) has no logarithmic growth on the fixed-support pole-neutral modulations, and hence is not Q.

## 4. All the winding norm is accounted for

**Theorem 2 (weak winding response and lost norm).** For each fixed integer \(a\geq1\),

\[
\mathscr U_RV_aS_Rf\rightharpoonup
\frac1{\sqrt a}J_{\rm rec}(U_{\log a}f),
\tag{12}
\]

and

\[
\lim_R\left\|\mathscr U_RV_aS_Rf-
\frac1{\sqrt a}J_{\rm rec}(U_{\log a}f)\right\|_\nu^2
=\left(\frac{\rho_a(0)}{\rho(0)}-\frac1a\right)\|f\|_2^2
=\frac{\sum_{j=1}^{a-1}\rho(2\pi j/a)}{a\rho(0)}\|f\|_2^2.
\tag{13}
\]

For a>1 and f nonzero this is strictly positive.

**Proof.** The exact branching identity expresses \(V_aS_Rf\) as identity phase with coefficient \(a^{-1/2}\), plus the nonidentity roots with their actual density weights. Theorem 1 treats its identity term.

For every other fixed phase beta, \(\mathscr U_RS_R^\beta f\) tends to zero locally on \(\theta\leq\pi-\epsilon\). In (11), the coefficient now has \(e^{i\beta n}\). Repeated discrete summation by parts, with a smooth compact coefficient envelope at scale N, gives arbitrarily rapid decay on compact y intervals; the slowly varying sine phase does not cancel a fixed nonzero beta. The full density factor remains bounded. These local estimates and uniformly bounded global norms imply weak convergence to zero against all physical vectors, since the complement of the excluded measure-zero set exhausts M. The nonidentity mass has moved toward the repelling holonomy P=-I, rather than being deleted.

Unitarity and the actual winding norm formula give the full limiting squared norm \(\rho_a(0)\rho(0)^{-1}\|f\|^2\). Subtract the squared norm \(a^{-1}\|f\|^2\) of the weak limit to obtain (13). \(\square\)

In particular

\[
\lim_R\langle J_Rf,\mathscr U_RV_aS_Rg\rangle_\nu
=a^{-1/2}\langle f,U_{\log a}g\rangle.
\tag{14}
\]

This is an actual-state mixed limit with a strongly occurring first source, but not strong occurrence of the wound second source. Treating its weak contraction \(a^{-1/2}U_{\log a}\) as a norm-preserving winding would lose exactly (13).

The compensated packets \(F_Rf\) of the electric-parity note have the same strong limit after \(\mathscr U_R\), since \(\|F_Rf-S_Rf\|_\nu\to0\). Conjugating the signed insertion by \(\mathscr U_R\) preserves each finite-R mixed response exactly. Thus the complete iterated signed Weil identity survives recentering, but becomes a scale-dependent inserted pairing. Mere strong convergence of the source vectors does not pass an unbounded insertion through the limit.

## 5. A further obstruction to completing the recentered source by one closed operator

There is a global source-domain issue beyond the earlier high-frequency L2 bound.

**Theorem 3 (no closable norm completion of an L2 source).** Let \(J_0:L^2(\mathbb R)\to\mathcal H\) be an isometry into a Hilbert space. There is no fixed closable linear operator T, with domain containing \(J_0\mathcal D^0\), such that

\[
\langle TJ_0f,TJ_0g\rangle=Q(f,g)
\quad(f,g\in\mathcal D^0).
\tag{15}
\]

The output Hilbert space may differ from \(\mathcal H\). In particular (15) is impossible for \(J_0=J_{\rm rec}\), even if arbitrary OS axioms, a gap, or other physical properties are assumed.

**Proof.** If T existed, positivity in (15) would imply RH by the restricted Weil criterion. Under this consequence, not as an assumption used to construct T, the explicit formula is

\[
Q(f,g)=\sum_\gamma m_\gamma
\overline{\widehat f(\gamma)}\widehat g(\gamma),
\tag{16}
\]

with discrete zero ordinates and their positive multiplicities. Choose one ordinate \(\gamma_0\) and \(h\in C_c^\infty\) with \(\widehat h(0)=1\). For L tending to infinity, put

\[
f_L=\frac{-\partial_x^2+1/4}{\gamma_0^2+1/4}
\left[L^{-1}e^{i\gamma_0x}h(x/L)\right]\in\mathcal D^0.
\tag{17}
\]

Then \(\|f_L\|_2\to0\) and

\[
\widehat f_L(\gamma)
=\frac{\gamma^2+1/4}{\gamma_0^2+1/4}
\widehat h(L(\gamma-\gamma_0)).
\]

These evaluation vectors converge in \(\ell^2(m_\gamma)\) to the nonzero unit evaluation at \(\gamma_0\). Indeed the other ordinates are isolated from \(\gamma_0\); Schwartz bounds for \(\widehat h\), together with the polynomial bound on the zero-counting function, give a summable dominating sequence after the displayed polynomial factor. Consequently

\[
Q[f_L]\longrightarrow m_{\gamma_0}>0,
\qquad Q[f_L-f_{L'}]\longrightarrow0\quad(L,L'\to\infty).
\]

Thus \(J_0f_L\to0\) while \(TJ_0f_L\) is Cauchy and converges to a nonzero Hilbert vector. This contradicts closability. \(\square\)

The argument says that, if Q is positive, it is not a closable quadratic form on ordinary global input L2. It does not say that Q fails to be a continuous form on \(\mathcal D^0\), or that a continuous \(\mathcal D^0\)-to-Hilbert source cannot exist. The supports in (17) grow with L, so the sequence is not convergent to zero in the smooth compact-test topology. Restriction of Fourier transforms to a mass shell in ordinary quantum field theory illustrates why a test-function source need not be closable in a larger ambient L2 topology.

This theorem excludes turning the recovered ordinary-L2 source into a Weil source by a single closable square-root insertion. It is stronger than merely observing that the signed response has no currently known positive square root. A different source topology, or a directly specified generalized source law, is necessary for that strategy even in the positive case.

## 6. Positive constrained energy: a precise second candidate

Return to the actual one-plaquette class space and the original \(V_a\), with their weighted adjoints. Let \(\mathfrak h\) be an independently specified densely defined nonnegative closed energy form on that space, with a uniform coercive bound

\[
\mathfrak h[u]\geq\delta\|u\|_\nu^2,\qquad \delta>0.
\tag{18}
\]

For example, the compression of the full electric form plus \(\delta\|u\|^2\) is available in the fixed slab. A physical Hamiltonian form supplies (18) on its vacuum-orthogonal sector if it has a gap and the proposed source domain lies in that sector. The finite-slab state is not silently identified with a continuum vacuum, and its electric gap is not the Clay physical mass gap.

An added scalar term is not necessary for the corresponding connected electric-sector test: the class electric form has compact resolvent and constants as its kernel, so it has a positive gap on the nu-mean-zero class subspace. One can restrict the input form and readout to that closed subspace, keeping the winding-difference norms in the full class space. The proof below is unchanged. It does not require the windings to preserve the connected subspace or to commute with the energy.

Define the finite positive form and its associated self-adjoint operator by

\[
\mathfrak q_A[u]=\mathfrak h[u]
+\sum_{2\leq a\leq A}\Lambda(a)\|(I-V_a)u\|_\nu^2,
\qquad K_A\geq\delta I.
\tag{19}
\]

Finite winding terms are bounded forms, so \(\mathfrak q_A\) is closed on the form domain of \(\mathfrak h\). No Haar adjoint is used in its operator expression. Let \(B:\mathcal H_{\rm cl}\to\mathcal Y\) be a fixed bounded readout, and fix y in its constrained range. The proposed effective source energy is

\[
\Gamma_A[y]=\inf_{Bu=y}\mathfrak q_A[u].
\tag{20}
\]

The infimum is over the declared form domain. Whenever the affine constraint is nonempty, the form Hilbert space gives a unique minimizer \(u_{A,y}\). Its actual positive source is \(K_A^{1/2}u_{A,y}\) in the original class Hilbert space, and its pairing is \(\mathfrak q_A(u_{A,y},u_{A,z})\). An auxiliary physical direct sum is not needed to represent the norm.

For a finite-dimensional surjective readout this is explicitly

\[
u_{A,y}=K_A^{-1}B^{*\nu}(BK_A^{-1}B^{*\nu})^{-1}y,
\qquad
\Gamma_A(y,z)=\langle y,(BK_A^{-1}B^{*\nu})^{-1}z\rangle.
\tag{21}
\]

Thus the prescription really integrates out unconstrained vectors by a positive Schur complement. It is a natural attempt to remove a divergent local contribution without subtracting it by hand.

**Theorem 4 (coercive Schur completion diverges).** Under (18), for every fixed bounded B and every nonzero y,

\[
\Gamma_A[y]\longrightarrow+\infty.
\tag{22}
\]

The convention is \(\Gamma_A[y]=+\infty\) if a constraint is infeasible. The result also holds with additional cutoff-independent constraints or nonnegative form terms.

**Proof.** The values are nondecreasing. If a cofinal sequence of values stayed bounded, choose approximately minimizing \(u_A\). Coercivity bounds their physical norms. Pass to a weakly convergent subsequence \(u_A\rightharpoonup u\). Boundedness of B preserves \(Bu=y\). For any fixed finite K, the finite prime form is weakly lower semicontinuous and \(\mathfrak d_K[u_A]\leq\mathfrak q_A[u_A]\) once A exceeds K. Hence \(\sup_K\mathfrak d_K[u]<\infty\). The audited zero-domain theorem for the full positive prime-difference form forces \(u=0\), contradicting y nonzero. No compact resolvent is needed. \(\square\)

**Susceptibility corollary.** The opposite prescription, using the inverse energy as a positive susceptibility, has a zero limit:

\[
K_A^{-1}\longrightarrow0\quad\text{strongly},\qquad
\|K_A^{-1/2}v\|_\nu\longrightarrow0
\quad(v\in\mathcal H_{\rm cl}).
\tag{22a}
\]

To prove this, put \(u_A=K_A^{-1}v\). Coercivity bounds its norm and its energy, since
\(\mathfrak q_A[u_A]=\langle u_A,v\rangle\leq\delta^{-1}\|v\|^2\).
The same finite-form lower-semicontinuity argument makes every weak cluster point zero. Hence \(u_A\rightharpoonup0\), its energy \(\langle u_A,v\rangle\) tends to zero, and (18) gives strong convergence. Finally
\(\|K_A^{-1/2}v\|^2=\langle v,K_A^{-1}v\rangle\to0\).
Thus a fixed smeared source followed by the positive inverse square root disappears; exchanging energy for susceptibility does not yield a finite nonzero Weil pairing.

There is a quantitative control for a concrete physical readout. Write \(u=\sum_n c_n\chi_n\), impose \(c_m=b\ne0\), and let \(c_\rho>0\) be the actual norm-equivalence lower bound. The readout is bounded, since
\(c_m=\langle\rho^{-1}\chi_m,u\rangle_\nu\). Keeping only the coordinate pm in each prime difference and those coordinates in the coercive norm gives

\[
\mathfrak q_A[u]\geq c_\rho|b|^2
\left(\delta+\sum_{p\leq A}
\frac{\delta\log p}{\delta+\log p}\right)\longrightarrow\infty.
\tag{23}
\]

For each prime, the scalar minimum of
\(\log p\,|c_{pm}-b|^2+\delta|c_{pm}|^2\)
is \(\delta\log p/(\delta+\log p)|b|^2\). The labels pm are distinct and differ from m, so no norm coordinate is counted twice. The resulting summands tend to delta along the primes. This proof uses only infinitely many primes, not an asymptotic prime-counting estimate.

Consequently the mass-gap-type bound helps prove failure of this particular positive completion. It cannot be invoked to justify subtracting its divergence. A changed, cutoff-dependent readout, loss of coercivity, or a different prime observable would be a different candidate needing its own domain and positivity proof.

## 7. What the extra physical assumptions do and do not supply

Assume a continuum pure four-dimensional YM theory satisfies the full OS reconstruction hypotheses in its gauge-invariant observable sector, with vacuum \(\Omega_{\rm vac}\), physical Hamiltonian H, and

\[
H\Omega_{\rm vac}=0,\qquad
H\geq\Delta(1-P_{\rm vac}),\qquad\Delta>0.
\tag{24}
\]

These are allowed physical hypotheses, not results proved here. They refer to the continuum vacuum; the explicit packet construction above stays in the fixed regulator and is not asserted to have a continuum limit.

On the excited subspace (24) makes \(H^{-1/2}\) bounded by \(\Delta^{-1/2}\), and gives exponential Euclidean decay. Neither estimate repairs weak escape by a fixed bounded operation. Nor does a gap imply compactness of energy-bounded sets: a positive lower spectral bound controls low energies, while compactness also needs restrictions on the number and localization of states.

The scope of the mass gap and OS reconstruction agrees with [Jaffe–Witten's official formulation, §§4–5](https://www.claymath.org/library/monographs/MPPc.pdf#page=121). Nothing in that formulation identifies arithmetic support translations with physical spacetime translations. The previous semibounded-generator and boost obstructions must not be evaded by confusing these actions.

The present results do not prove that the OS axioms plus a gap cannot imply RH by some other use of YM dynamics. They show exactly what those assumptions accomplish in the two specified constructions. No independence result in mathematical logic is claimed.

## 8. A natural compactness assumption gives an actual continuum source criterion

An additional useful assumption is **local phase-space compactness**. In the reconstructed vacuum observable net, let \(\mathcal A(O)\) be a local von Neumann algebra and fix \(\beta>0\). Assume the map

\[
\Theta_{\beta,O}:A\mapsto e^{-\beta H}A\Omega_{\rm vac}
\tag{25}
\]

maps its operator-norm unit ball to a relatively compact Hilbert set. The usual energy nuclearity condition is stronger and implies this compactness. This is an additional natural physical hypothesis, not a consequence of a mass gap alone. The original physical motivation is the phase-space condition of [Buchholz–Wichmann](https://doi.org/10.1007/BF01454978); only the explicit compactness assumption (25) is used below.

**Lemma 5 (compact balls made of actual prepared observables).** For each finite M,

\[
\mathcal K(O,M)=\{e^{-\beta H}A\Omega_{\rm vac}:A\in\mathcal A(O),\ \|A\|\leq M\}
\tag{26}
\]

is norm compact, including its limit points. Moreover

\[
\|\mathbf1_{(E,\infty)}(H)v\|\leq M e^{-\beta E}
\quad(v\in\mathcal K(O,M)).
\tag{27}
\]

**Proof.** Relative compactness follows from (25). If a sequence in (26) has a strong limit, take an ultraweakly convergent subnet of its bounded operators in the local von Neumann algebra. The operator ball is ultraweakly compact, and vector functionals are normal. The prepared vectors then converge weakly to the preparation of the limiting operator, which must equal the original strong limit. Thus the image is norm closed. The spectral theorem and \(\|A\Omega_{\rm vac}\|\leq M\) prove (27). \(\square\)

Use one fixed beta, nested bounded regions \(O_I\) for arithmetic support intervals I, and bounds \(M_f=C_Ip_I(f)\) for predetermined smooth seminorms. The existing countable finite-compatibility proof applies directly with the compact coordinate sets (26): if every finite subset of independently specified closed source relations is feasible in these same sets, there is one continuous global source map J retaining those relations and bounds. Its vectors still have the form

\[
Jf=e^{-\beta H}A_f\Omega_{\rm vac},\qquad
A_f\in\mathcal A(O_I),\quad \|A_f\|\leq C_Ip_I(f).
\tag{28}
\]

This is stronger than merely placing the limit in a Hilbert completion. If the vacuum is separating for these local algebras, as supplied by the usual local vacuum hypotheses with a nonempty spacelike complement, injectivity of \(e^{-\beta H}\) also makes \(A_f\) unique and enforces its linearity when J is linear. Separatingness is unnecessary for the vector existence conclusion itself.

If the independent source relations further give the separated-support mixed identity, translation/reflection symmetry, logarithmic growth and three anchors in the [determination theorem](OFF_DIAGONAL_RIGIDITY_AND_COMPACT_SOURCE_EXISTENCE_20260924.md), the resulting reflected pairing equals Q and OS positivity implies RH. The unproved input is arithmetic finite feasibility from actual YM source relations. Neither nuclearity nor Reeh–Schlieder density establishes it: density approximates already existing target vectors, and does not show that an indefinite proposed Gram matrix has positive realizations or uniformly bounded preparation cost.

This is an explicit conditional physical framework, not a deduction of RH from standard physical axioms alone. It identifies a natural extra assumption worth using because it addresses occurrence, while leaving the arithmetic assertion visible and unassumed.

## 9. Research disposition and verification

The strongest new affirmative result is Theorem 1: a native current recovers the identity packet as a nonzero source in the same fixed state, with a proved strong limit and exact mixed norm. Theorem 2 quantifies why this does not recover all winding components. Theorem 3 excludes completing any such L2-isometric source by a fixed closable operator. Theorem 4 excludes the tested positive Schur-complement renormalization under a uniform coercive bound, and (22a) shows that the inverse-energy susceptibility instead vanishes. Lemma 5 supplies genuine prepared-observable compact sets when local phase-space compactness is assumed.

The useful next source class is therefore a **directly specified generalized source with smooth-test bounds**, not a closable insertion on the recovered ordinary-L2 source or an infinite unrenormalized prime-difference energy. For a continuum approach, local phase-space compactness may now be assumed as an explicit physical aid. The remaining mathematical task is to derive the arithmetic mixed relation for such sources from independently specified YM observables. Assuming positivity of the already completed Weil response would not meet that task.

The [checker](../numerics/check_current_recentering.py) and [small record](../numerics/records/current-recentering-20260925.json) contain 19 passing floating controls: sine-transform quadrature refinement, local recentering, mixed winding coefficients, and the missing norm for windings 2, 3 and 5. They also record the quantitative gapped lower bound (23) at growing cutoffs. Prescribed radial-density comparisons are not simulations of the full interacting current; the full-state claim rests on (3)–(11). No numerical zero list, large arrays, or third-party PDFs are saved. A separate [assumption and domain audit](../reviews/OS_MASS_GAP_AND_SOURCE_DOMAIN_AUDIT_20260925.md) records the precise proof dependencies and limits.
