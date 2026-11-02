# MC05-E01: separate check of source heat, Schur nonclosure and the theta oscillator

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewer **gpt-6.1-sol (Codex), reasoning effort ultra**, verified in session 01a19a54-ed89-7c00-8f73-efd0c7a7a8db, turn 01a19a54-ed9e-7702-9cd0-35e66e2e20db, agent /root/review_response_oscillator. Authoring model **gpt-6-astra / ultra**, verified in the author rollout identified below.

**Disposition: accept the fixed exact identities, scoped nonclosure and oscillator reformulation; no mathematical correction identified. MC05-E01 r1 is complete.** No rectangular-ratio sign estimate, complete signed Mellin bound, all-minor theorem or RH proof is acquired. The physical state and its zero-location reformulation are useful exact constructions at the scope claimed.

This is separate cross-model internal checking with shared baseline premises, not independent specialist review. Only this review is owned here; no frozen return, support record, catalog, register or shared history was changed.

## Inputs and provenance

| Input | Verified SHA-256 |
| --- | --- |
| [Request r1](../numerics/MC05_E01_REVIEW_REQUEST_R1_20261101.json) | c503b9c596622f0972c3479ee4833828b997b47f12dd320c04132e78d6559765 |
| [Frozen return](../notes/01_THETA_SCHUR_CONSTRAINT_RETURN_20261101.md); matches request | a992f6ea3cc566d2d1b96e5b7b0a0ecde9367be2a252d17a0f9b3f7af8e19965 |
| [Fixed exact checker](../numerics/mc05_b01_heat_cofactor_check.py); matches support record | 0ddf8ed914fae1e83e1935a49282df281cbcd76abd5d9c8b0f8cad7093f9ea5c |
| [Support record](../numerics/MC05_B01_HEAT_SCHUR_RECORD_20261101.json) | f825bd9d9cc76df3380c2239655c9ae28746707a53de11cae54d31ff5a1d7aa1 |
| Initial Mellin assessment | ee4280708b43d4d080fe98c128d58c0180f0ba0851b730bd859c2a899f84d9de |
| Parent Note04 | f4ff6338794cf359bf06ea6ec17867fd5aef44910de1796b3c26396f8fb5b720 |
| Continuation05 | 7cfa21664fe85e64749a7fc4e32c420300b8d91590f0dc62da35cf3816e677d7 |
| Launch record | 501acdcfa663b5eb4959c348095a4e79c70053907660b599f3585862a526f60a |
| Accepted J-E03 Review01 | c13e63e7c017285932e75d2add333b8d683e5ed3b9a096f6e20e31e88e0a2dfe |
| [Selected physical-source catalog](../../../../references/07_PARALLEL_PHYSICAL_ASSESSMENT_SOURCES_20261101.md), read version | a2b8f2b11a875c5f60dfa7f68ff4254d1601d54d090d960306689cca4c3217f3 |

**The suspected second-wave turn mismatch is resolved without correction.** The author session is 01a19a49-f8de-7770-a4ee-ec2acf3ace08, agent /root/mc01_thermal. Its rollout contains one child turn, 01a19a49-f900-7ae0-8f31-61b472611c01, recorded as gpt-6-astra / ultra. The MC05 follow-up arrived before that turn completed; its completion message reports both MC01 and MC05 and the assessed MC05 hash. Thus the header and support record use the actual authoring turn. A separate new turn identifier must not be invented merely because the assignment was called a second wave. The inherited root turn appearing in that rollout is not the child's authoring turn.

Read with the [result summaries](../../../../../../../result-summaries/README.md), [theta bookkeeping](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), [patterns to avoid](../../../../../../../avoid/README.md), [reformulations](../../../../../../../avoid/01_restating_the_target.md), [shared premises](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md) and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## Heat and Schur algebra

**Accept equations (1)–(4).** Differentiating the full moments gives
\[
\dot c_n=(2n+2)(2n+1)c_{n+1},\qquad
\partial_\tau F=(4w\partial_w^2+2\partial_w)F.
\]
The double-exponential tail dominates the required derivatives uniformly on compact real parameter sets. The negative-index convention is consistent, including the vanishing prefactor at \(n=-1\). Dividing by \(c_0\), using \(\dot c_0=2c_1\), and taking the formal logarithm gives the stated equation for \(G=\log(F/c_0)\). At coefficient \(w^m\), the linear term is
\[
[4m(m+1)+2(m+1)]t_{m+1}=2(m+1)(2m+1)t_{m+1},
\]
and the quadratic term is \(4\sum_{a+b=m+1}ab\,t_at_b\). The low-order examples, Jacobi–Trudi specialization and restriction to a formal logarithm are correct. No global zero-free logarithm or finite Toda reduction has been assumed.

**Accept equations (5)–(6) and the ratio normalization.** The largest index \(c_{k+3}\) in \(\dot D_{3,k}\) comes only from the upper-right entry. Its positive cofactor is
\[
D_{2,k-1}=\det\begin{pmatrix}c_{k-1}&c_k\\c_{k-2}&c_{k-1}\end{pmatrix}.
\]
Only \(\dot D_{3,k+1}/D_{3,k+1}\) contributes \(c_{k+4}\) to \(\partial_\tau\log\eta_k\). Its coefficient is
\[
(2k+8)(2k+7)\frac{D_{2,k}}{D_{3,k+1}}>0
\]
at \(\tau=0\), using the accepted lower-order positivity. Every denominator and remaining rational expression uses coefficients through \(c_{k+3}\). The logarithms need only a possibly \(k\)-dependent neighborhood of zero, not global heat-time determinant positivity.

The factorial budget yields \(Q_{3,k}=B_{3,k}\eta_k\) with the stated \(B_{3,k}\). Dividing the Gaussian comparator \((2k+5)/(2k-1)\) by \(B_{3,k}\) gives \(k/(k+3)\). The isolated positive coefficient of \(c_{k+4}\) does not sign the complete derivative or bound \(\eta_k\).

## Compact perturbation and exact scope of nonclosure

**Accept equations (7)–(9).** Integration by parts \(2N+2\) times against the compactly supported bump has no boundary terms. Powers through \(u^{2N}\) vanish, while \(u^{2N+2}/(2N+2)!\) gives exactly \(\epsilon\int\psi\), with positive sign. Even extension is smooth because the perturbation vanishes near zero.

On a compact interval containing its support and staying away from zero, the canonical \(\Phi\), \(R'\) and \(K\) have positive minima. Their dependence on the positive source and its jet through order seven is continuous. Taking sufficiently small \(|\epsilon|\) preserves these signs for both choices of sign; outside that interval the source is identical. This proves preservation rather than assuming that every familiar collision control has those signs. Origin germ and exterior tails are exactly fixed. Real analyticity, the global canonical square expansion and modular source identity have not been preserved or claimed.

The first \(N\) connected coefficients remain fixed, and \(\delta t_{N+1}=\epsilon\int\psi/c_0\). Hence \(\dot t_N\) changes by the asserted nonzero quantity. Taking \(N=k+3\) leaves \(\eta_k\), the displayed prefactor and lower rational expression fixed while changing its derivative by equation (9). This proves failure of deterministic universal finite-prefix closure in the stated smooth positive even class with the stated preserved signs and tails. It does not prove sign reversal, defeat every inequality, construct a collision or exclude a theta-specific constraint using infinite canonical information.

## Hilbert-space state, zeros and dynamics

**Accept equations (10)–(15).** For every finite real \(\tau\), Tonelli sums the nonnegative even-moment series into the double integral with \(\cosh(uv)\). The inequality
\[
\cosh(uv)\le e^{(u^2+v^2)/2}
\]
gives precisely the square of the stated finite source integral. Thus \(\chi_\tau\) has a positive finite norm. Expanding the coherent pair in equation (12) cancels its \(e^{-u^2/2}\) against the displayed weight and removes the odd number states; the coefficient of \(|2n\rangle\) is \(b_n/\sqrt{(2n)!}\). Its Bochner norm is integrable.

The Bargmann coefficient is therefore \(b_n/(2n)!=c_n\), as required. The [primary stellar convention, Definition 1 and equations (1)–(3)](https://arxiv.org/pdf/1907.11009v3), PDF p.2, fixes both the factorial and conjugation; those passages were inspected directly. The unnormalized function must be divided by \(\mathcal N_\tau\) to represent the normalized state, which equation (15) does.

For clarity, analytic continuation of the inherited normalization first gives
\[
\mathcal B_0(z)=H(0,iz)=\tfrac18\xi((1-z)/2).
\]
The functional equation \(\xi(s)=\xi(1-s)\) gives the return's \(\tfrac18\xi((1+z)/2)\). This checks the sign, factor 8 and spectral factor 2. The normalization is also explicit in the shared primitive brainstorm's Riemann split-integral derivation. The completed \(\xi\) has the nontrivial zeta zeros, so all of its zeros belong to the full RH statement. Conjugating \(z\) to the coherent amplitude preserves the imaginary axis. Since the Gaussian factor and norm in \(Q\) never vanish, the claimed all-zero axis condition is exactly RH. Automatic nonnegativity of \(Q\) gives no zero-confinement estimate.

This is an exact physical reformulation over infinitely many locations, classified once as such. No finite experiment, state preparation theorem, finite stellar-rank theorem or finite-minor upgrade is used.

**Accept equation (17), its domains and normalized flow.** The coherent pair is an eigenvector of \(a^2\) with eigenvalue \(u^2\). Multiplying the norm-integrable source integrand by \(u^{2m}\) proves membership in the domain of every \((a^2)^m\) and permits norm differentiation. More explicitly, complex \(\tau\) in any compact set is dominated by the same integral with \(e^{(C+1/2)u^2}\); this proves an entire Hilbert-valued orbit. For any radius \(R\), summing the absolute Taylor majorant introduces only \(e^{Ru^2}\), still integrable. Thus the analytic-orbit claim is justified, including unbounded-generator domains, without a bounded semigroup assertion on the whole Hilbert space.

Norm differentiation gives \(\mathcal N'/\mathcal N=\operatorname{Re}\langle\psi,a^2\psi\rangle\), and the amplitudes are real for real \(\tau\), so the expectation here is real. The stated normalized equation follows. The term “one-sided” describes the annihilation-only generator; the constructed orbit itself exists for all finite real \(\tau\). The flow is nonunitary. The source paper's squeezing generator on PDF p.3 contains both annihilation and adjoint creation terms; that comparison was inspected directly. No channel or physical implementation is established by naming \(a^2\).

## Fixed support replay, controls and stop

One read-only replay of the unchanged exact checker passed; its complete returned JSON equals the saved exact-check section. It checks the two specified cofactor cases and the discriminants \(-3,109\). Analytically, the polynomial orbit satisfies \(\dot c_0=2c_1,\dot c_1=12c_2,\dot c_2=0\). At \(\tau=1\), the roots have positive product 15, negative sum \(-13\) and positive discriminant, so both are negative. At zero its roots are nonreal. Both are finite, normalizable Fock states with positive displayed coefficients. Vanishing higher moments rule out a nonzero positive half-line moment source. The witness screens generic reverse axis-confinement assertions for that polynomial/Fock class only.

Gaussian sources require an additional width condition for this oscillator norm; the theta proof uses its stronger tail. Euler-factor and altered square-source controls fail literal canonical data while still permitting generic heat algebra, and where tails suffice the oscillator construction. Reflected/shape/primitive controls require their own norm payment. None is assigned an uncomputed \(R'/K\) sign or curvature sign. Compact nonclosure perturbations fail canonical modular/spectral information; the finite-Fock witness fails positive moment-source realization. These distinctions preserve the scopes of the inherited collision controls.

**Accepted:** heat/Schur identities, cofactor and ratio bookkeeping, compact finite-prefix nonclosure with preserved local signs, actual oscillator norm and analytic dynamics, and the complete Husimi-zero reformulation. **Corrections:** none; the questioned authoring turn was verified. **Unresolved fixed-review defects:** none identified. **Unresolved research obligations:** independent theta-specific higher-coefficient/initial-data control and the complete signed Mellin comparison, including \([0,2]\), remaining compact ranges and unbounded \(s\). The bounded review stops here; no new candidate, numerical campaign or broader physical theorem is issued.
