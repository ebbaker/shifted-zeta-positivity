# MC08-E01 r1: explicit local no-jump admissibility

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual authoring model **gpt-6.1-sol (Codex), reasoning effort ultra**, recorded in chat `01a19d66-56e2-7ff2-a549-03561c41f801`, turn `01a19d66-5954-7bd1-a3e4-a07132e0161f`. Two read-only same-model checking subtasks audited the symbol/control algebra and the constants; a final bounded check of this written return found no blocker. See the [limited checking record](../reviews/01_MC08_E01_BOUNDED_CHECK_20261102.md). These checks share the inputs and do not complete the later separate MC08-E03 assessment or constitute specialist review.

**Disposition: MC08-E01 r1 complete, proved in-note with exact rational support.** For the unchanged canonical theta source and backward shift, on the full one-particle space,
\[
\boxed{0\le v\le\frac1{25},\qquad
R(v):=-[G(v)+G(v)^\dagger]
\ge\frac1{8000}(2I-S-S^\dagger)\ge0.} \tag{1}
\]
The exact normalized transfer therefore has a bounded, norm-continuous, time-dependent one-particle Lindblad completion with this prescribed no-jump propagator. The convenient point \(v=1\) is **not covered by this estimate**; no failure there is inferred. This is a local physical-realization result with an explicit source bound, not a new signed-minor or Mellin-curvature estimate. The polynomial control below satisfies the stronger dynamical premise and still has a negative fermionic amplitude.

## 1. Frozen input and classification

The [overview](../research-overview/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_OVERVIEW_20261102.md) and [sole live register](../research-progress/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md) specify E01 r1. Inputs were read and hashed before use:

| Input | SHA256 |
| --- | --- |
| [MC02 transfer](../../02_fermionic_correlators/notes/01_THETA_ORBITAL_COMPARISON_RETURN_20261101.md) | `61207dbe824e5a67794d7c3be1811a95c1c69fa8006c4c7cc8d703a867706901` |
| [Separate MC02 review](../../02_fermionic_correlators/reviews/01_MC02_E01_SEPARATE_REVIEW_20261101.md) | `9f7a265228c203d5e3bcc27813a3690b8f9c4ee327f933fcde4301ec0f5a9d0e` |
| [Continuous-v input](../../brainstorm/notes/01_CONTINUOUS_V_EVOLUTION_AND_HERMITIAN_SCOPE_20261102.md) | `ca1a8445165cd36d515e81f319824162158851118ab42382780054d6f5da8928` |
| MC08 overview | `cd337511861cb72380b02a8afc76b15654fa495023f0b90609dda3a0d4a7e88a` |
| [Source record 12](../../../../references/12_OPEN_QUANTUM_DYNAMICS_SOURCES_20261102.md) | `1ec1f662627653edc9e9e8ccca38a06fc5c252628d46c72ffb5e391e9407359a` |

The three baseline hashes match the request. No input correction or contract change was needed. The source remains at source heat time zero:
\[
\Phi(u)=\sum_{m\ge1}(2\pi^2m^4e^{9u}-3\pi m^2e^{5u})e^{-\pi m^2e^{4u}},
\quad c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du,
\quad F(w)=\sum_{n\ge0}c_nw^n.
\]
Every summand is positive for \(u\ge0\), so \(c_n>0\). \(F\) is entire. Keep \(S|0\rangle=0\), \(S|j\rangle=|j-1\rangle\), and \(K_v=F(vS)/F(v)\).

Read with the [result index](../../../../../../../result-summaries/README.md), specifically [theta/physical results](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and the [avoid index](../../../../../../../avoid/README.md), specifically [reformulations](../../../../../../../avoid/01_restating_the_target.md), [generic re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [joint signed estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). The existing all-sector sign statement is an RH-equivalent reformulation, stated once in the baseline. This return proves a different, weaker realization property; its numerical gain is the explicit interval in (1).

## 2. Complete-source constants without quadrature

Put
\[
\psi(u)=e^u\sum_{m\ge1}e^{-\pi m^2e^{4u}},\quad
J_0=\int_0^\infty\psi(u)\,du,\quad
J_2=\int_0^\infty u^2\psi(u)\,du,\quad
C=\int_0^\infty\psi(u)\cosh(2u)\,du.
\]
Termwise differentiation gives \(\Phi=(\psi''-\psi)/8\). The complete Jacobi inversion identity gives \(\psi'(0)=-1/2\): if \(\vartheta(y)=1+2\sum_{m\ge1}e^{-\pi m^2y}=y^{-1/2}\vartheta(1/y)\), differentiation at one yields \(\vartheta'(1)=-\vartheta(1)/4\), and \(\psi'(0)=(\vartheta(1)-1+4\vartheta'(1))/2=-1/2\). This is the inherited canonical endpoint, not an endpoint assigned to a truncated sum.

All outer boundary terms vanish by double-exponential decay. Two integrations by parts give
\[
c_0=\frac1{16}-\frac{J_0}{8},\qquad
c_1=\frac{2J_0-J_2}{16},\qquad
F(4)=\int_0^\infty\Phi(u)\cosh(2u)\,du
=\frac1{16}+\frac{3C}{8}. \tag{2}
\]
For example, the general real-\(s\) identity is \(\int\Phi\cosh(su)=1/16+(s^2-1)\int\psi\cosh(su)/8\). This checks the factors in (2).

Here are uniform bounds paying the entire mode sum and integration tail. Since \(e^{4u}\ge1+4u\), \(\pi>3\), and \(e^3>20\),
\[
\psi(u)\le\sum_{m\ge1}e^{-\pi m^2}e^{-(4\pi m^2-1)u},\quad
\sum_{m\ge1}e^{-\pi m^2}<\sum_{m\ge1}20^{-m^2}\le\frac1{19}.
\]
Writing \(a_m=4\pi m^2-1>11\), integrate the positive terms and use that \(a/(a^2-4)\) decreases for \(a>2\):
\[
J_0<\frac1{209},\qquad J_2<\frac2{19\,11^3}=\frac2{25289},\qquad
C<\frac1{19}\frac{11}{117}=\frac{11}{2223}. \tag{3}
\]
For a lower bound, retain only \(m=1\) and \(0\le u\le1/16\). On this interval \(e^{4u}\le e^{1/4}<4/3\), so \(\pi e^{4u}<88/21<9/2\). Since \(e^{9/2}<100\) and \(e^u\ge1\),
\[
J_0>\frac1{1600}. \tag{4}
\]
The elementary exponential bounds can be checked using rational Taylor estimates: \(\sum_{k=0}^8 3^k/k!=89641/4480>20\); \(e<\sum_{k=0}^3 1/k!+(1/24)/(1-1/5)=87/32<11/4<25/9\); hence \(e^{9/2}<(11/4)^4(5/3)=73205/768<100\). Also \(e^{1/4}<\sum_{k\ge0}(1/4)^k=4/3\). The familiar rational bounds \(3<\pi<22/7\) suffice throughout.

Equations (2)--(4) imply
\[
\frac{207}{3344}<c_0<\frac1{16},\qquad
b_1:=\frac{c_1}{c_0}>16c_1=2J_0-J_2>
\frac{23689}{20231200}>\frac1{1000}, \tag{5}
\]
and
\[
q_4:=\frac{F(4)-c_0}{c_0}
<\frac{3(11/2223)+1/209}{8(207/3344)}
=\frac{320}{8073}<\frac1{25}. \tag{6}
\]
No finite theta cutoff or floating integration enters these inequalities.

## 3. Zero-free disk, derivative and inverse

Positive coefficients and (6) imply, for every complex \(|w|\le4\),
\[
\left|\frac{F(w)}{c_0}-1\right|\le q_4<\frac1{25}.
\]
Thus \(F\) is zero-free on a neighborhood of this closed disk. The canonical logarithm \(B(w)=\log(F(w)/c_0)\), \(B(0)=0\), obeys
\[
B(w)=\sum_{n\ge1}b_nw^n,\qquad
|B(w)|\le-\log(1-q_4)<\frac1{24},\qquad
|b_n|\le\frac1{24\,4^n}. \tag{7}
\]
The logarithmic bound uses its convergent \(\log(1+z)\) series and \(-\log(1-q)\le q/(1-q)\). Cauchy's coefficient estimate is on radius four, with a genuine analytic neighborhood.

Operator power series and their derivatives converge in norm on compact intervals. For \(0\le v\le1/25\), the Neumann series gives a bounded inverse of \(F(vS)\), so direct differentiation and commutativity give
\[
G(v)=K'_vK_v^{-1}=SF'(vS)F(vS)^{-1}-\frac{F'(v)}{F(v)}I
=\sum_{n\ge1}n b_n v^{n-1}(S^n-I). \tag{8}
\]
At zero the continuous extension is \(G(0)=b_1(S-I)\), with no \(0^0\) ambiguity. In particular \(R(0)=b_1(2I-S-S^\dagger)\). Endpoint contraction \(\|K_v\|\le1\) has not been used to infer instantaneous dissipativity.

## 4. The half-infinite symbol and the zero angle

Let \(a_n(v)=n b_n v^{n-1}\), real for real \(v\), and
\[
r_v(\theta)=2\sum_{n\ge1}a_n(v)(1-\cos n\theta).
\]
For a finite sequence \(x\), put \(p_x(e^{i\theta})=\sum_{j\ge0}x_je^{ij\theta}\). Direct Fourier expansion gives
\[
\langle x,R(v)x\rangle=\frac1{2\pi}\int_{-\pi}^{\pi}
r_v(\theta)|p_x(e^{i\theta})|^2\,d\theta. \tag{9}
\]
Norm convergence extends this to all \(\ell^2\). Conversely, normalized Hardy kernels give Poisson averages tending to the continuous \(r_v\), so (9) also proves \(R\ge0\) iff \(r_v\ge0\). Only the sufficient direction is needed for (1).

Use the identity and bound
\[
\frac{1-\cos n\theta}{1-\cos\theta}
=\left|\sum_{j=0}^{n-1}e^{ij\theta}\right|^2\le n^2,
\]
extending the quotient at zero by \(n^2\). It follows that
\[
R(v)\ge\left[b_1-\sum_{n\ge2}n^3|b_n|v^{n-1}\right]
(2I-S-S^\dagger). \tag{10}
\]
In particular the previously proposed sufficient condition is valid on the actual half-infinite space, not just on finite matrices. The zero-angle limit is controlled by the same absolutely summable majorant:
\[
\lim_{\theta\to0}\frac{r_v(\theta)}{2(1-\cos\theta)}
=\sum_{n\ge1}n^3 b_n v^{n-1}.
\]
No angular sampling or continuity across a nonexistent spectral gap is involved.

## 5. Explicit interval and exact tail payment

Put \(x=v/4\). Equation (7) gives
\[
\sum_{n\ge2}n^3|b_n|v^{n-1}
\le\frac1{96}\sum_{n\ge2}n^3x^{n-1}
=\frac1{96}\left[\frac{1+4x+x^2}{(1-x)^4}-1\right]. \tag{11}
\]
The right side increases for \(0\le x<1\). When \(v\le1/25\), \(x\le1/100\), and its endpoint value is exactly
\[
T_*:=\frac{2650133}{3073907232}<\frac7{8000}.
\]
Together with \(b_1>1/1000=8/8000\), (10) proves (1). A single analytical bound suffices; no refinement or numerical campaign was needed. The relative margin is strictly positive, while the spectral infimum remains zero. Indeed \(r_v(0)=0\), and Poisson kernels in (9) have Rayleigh quotients tending to zero. This is consistent with, and avoids relying on, the absence of a gap at zero.

## 6. Bounded Lindblad completion on the infinite one-particle space

Define
\[
H(v)=\frac{i}{2}[G(v)-G(v)^\dagger],\qquad L(v)=\sqrt{R(v)}.
\]
Then \(H=H^\dagger\), \(L^\dagger L=R\), and \(-iH-R/2=G\), with the convention in [Castin--Dalibard--Mølmer, equations (2), (4)--(8) and Section 2](https://arxiv.org/html/0805.4002v1). Those passages were re-inspected for this return; no theorem about an unbounded generator is imported.

An explicit common bound is
\[
A_*:=\frac1{96}(1-1/100)^{-2},\quad
\sup_v\|G(v)\|\le2A_*,\quad
\sup_v\|H(v)\|\le2A_*,\quad
\sup_v\|R(v)\|\le4A_*,\quad
\sup_v\|L(v)\|\le2\sqrt{A_*}.
\]
Equation (8) makes \(G,H,R\) norm-continuous (indeed real analytic). Uniform polynomial approximation to the square root on \([0,4A_*]\) makes \(L\) norm-continuous even though zero lies in the spectrum.

For every \(0\le a\le b\le1/25\), the exact no-jump propagator is
\[
V(b,a)=K_bK_a^{-1},\quad \partial_bV(b,a)=G(b)V(b,a),\quad V(a,a)=I.
\]
For every vector, \(\partial_b\|V(b,a)f\|^2=-\langle V(b,a)f,R(b)V(b,a)f\rangle\le0\); hence every intermediate \(V\) is a contraction, not merely the endpoint from zero.

The trace-class equation
\[
\dot\rho=G\rho+\rho G^\dagger+L\rho L^\dagger
=-i[H,\rho]+L\rho L^\dagger-\tfrac12\{R,\rho\} \tag{12}
\]
has a unique norm-continuous propagator because its generator is bounded and norm-continuous in trace norm. For completeness, start with \(\mathcal V(b,a)\rho=V(b,a)\rho V(b,a)^\dagger\), and iterate the variation-of-constants equation inserting \(\mathcal J_t\rho=L(t)\rho L(t)^\dagger\). Each time-ordered term is CP, its trace-norm bound is at most \((\sup\|L\|^2(b-a))^k/k!\), and the series converges in map norm. Positivity persists after tensoring with any finite ancilla, so the sum is CP. Cyclicity of the trace and \(G+G^\dagger+R=0\) give trace preservation. Uniqueness gives composition on every intermediate interval. Thus this is a CPTP, CP-divisible, time-dependent one-particle completion directly on \(\ell^2\). No mode limit is needed for this claim; no homogeneous semigroup is asserted.

The selected no-jump branch is exactly \(K_v\rho K_v^\dagger\) from zero, and its probability is \(\operatorname{Tr}(K_v\rho K_v^\dagger)\); the normalized conditional state divides by that probability. The jump-free operator is unchanged. For example, (6) also gives \(\|K_v^{-1}\|<13/12\), so a normalized one-particle input has no-jump probability at least \((12/13)^2\) on this interval. This coarse lower bound follows from the exact operator and does not encode an amplitude sign.

This abstract completion chooses one jump operator \(\sqrt R\) acting within the one-particle Hilbert space. It is not yet the linear fermion-loss instrument of E02, a locality theorem, or a microscopic reservoir realization. Those require the B01 decision.

## 7. Finite cutoffs and particle limits

For \(\mathcal H_N=\operatorname{span}\{|0\rangle,\ldots,|N\rangle\}\), the backward shift leaves \(\mathcal H_N\) invariant. Using the **original** scalar \(F(v)\), not a truncated normalization, one has \(K_{v,N}=K_v|_{\mathcal H_N}\), \(G_N=G|_{\mathcal H_N}\), and
\[
R_N=P_NR|_{\mathcal H_N},\qquad H_N=P_NH|_{\mathcal H_N}.
\]
These inherit (1) with the same constants for every finite \(N\). Although \(F(vS_N)\) is invertible for every finite \(v\), that fact establishes neither infinite-space invertibility nor dissipativity outside the proved interval. Also \(\sqrt{R_N}\) need not equal \(P_N\sqrt R|_{\mathcal H_N}\); finite completed channels have not been identified as invariant restrictions of the infinite one.

For each fixed finite particle number \(r\), \(\wedge^r V\) is a contraction with bounded no-jump generator \(d\Gamma_r(G)\), norm at most \(r\|G\|\), and \(d\Gamma_r(R)\ge0\). Thus the inherited exact conditional-sector amplitudes remain represented on arbitrary finite sectors, with no mode cutoff required. This is not a proof of a compatible full-Fock **jump** dynamics: generator bounds grow with \(r\), the full-Fock generator can be unbounded, and a common linear-loss construction, its domain, convergence and signed readout remain E02 obligations. No operator-norm convergence of finite cutoffs is claimed.

## 8. Exact controls and scoped limitations

For the Gaussian \(F(w)=c_0e^{aw}\), \(a>0\), (8) gives \(G=a(S-I)\), \(R=a(2I-S-S^\dagger)\), and \(H=ia(S-S^\dagger)/2\) at every \(v\ge0\). It is the normalization comparison with known nonnegative minors, but has the same fixed-metric Jordan obstruction as theta.

More decisively, take \(F_*(w)=1+w+2w^2\). Its roots have modulus \(1/\sqrt2\), and it has the same exact-generator construction for \(0\le v<1/\sqrt2\). Put \(x=\cos\theta\). Direct algebra, retained in the support program, gives
\[
r_{*,v}(\theta)=
\frac{2(1-x)(1-2v^2)(1+7v+2v^2+8vx)}
{(1+v+2v^2)|1+ve^{i\theta}+2v^2e^{2i\theta}|^2}\ge0. \tag{13}
\]
The last numerator factor is at least \(1-v+2v^2>0\). Yet
\[
\langle0,1|\Gamma(K_{*,v})|1,2\rangle
=-\frac{v^2}{(1+v+2v^2)^2}<0\quad(v>0).
\]
Thus even exact local no-jump Lindblad admissibility does not imply nonnegative ordered fermionic amplitudes. This is stronger screening than endpoint CP alone. Also \(b_{*,3}=-5/3\), giving a negative three-step coefficient \(-5v^2\) in \(G_*\), although (13) is nonnegative: classical nonnegative jump rates are a different condition.

The [standing control inventory](../../../../../../../result-summaries/12_collision_controls_and_screening.md) and [control discipline](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md) give the remaining scope:

| Family | Premise assessment for this return |
| --- | --- |
| Polynomial relaxation | Passes the stronger dissipativity premise; fails unchanged canonical reconstruction and has the displayed negative minor. |
| Euler-factor sources | Change the canonical coefficients; generally change the fixed primitive endpoint/normalization used in (2). The source-specific constants (2)--(6) are not imported. Their own local admissibility can be tested by the same generic argument; no sign assigned. |
| Reflected / smooth positive-primitive sources | Fail unchanged arithmetic theta expansion. Some matched endpoints may survive. The mode envelope and constants (3)--(6) have not been established for them; no claim that they fail the resulting dissipativity inequality. |
| Weighted-square / finite-prime changes | Fail canonical weights; full source reflection and hence the fixed endpoint in (2) may fail. Their discrete transfer remains available under their own convergence assumptions. |
| Other CPTP completions / unravelings | Can change the selected instrument or phase readout. Positivity of a channel or of state density matrices does not sign the fixed real occupation amplitude. |

More generally, the Cauchy argument gives some sufficiently small admissible interval for **any** real analytic coefficient source with \(c_0,c_1>0\) and a convergent positive coefficient sum on a disk. This explains why the qualitative local result is generic; only the paid interval here is theta-specific. No collision control is excluded from that generic property merely by failing exact reconstruction. A positive-time collision alone assigns no time-zero minor sign.

Outside the local interval the bound is silent. A zero \(w_0\) of \(F\) yields a kernel of \(F(vS)\) for \(v>|w_0|\), by the backward-shift eigenvector with eigenvalue \(w_0/v\). At equality, normalized length-M truncations of the unit-modulus backward-shift eigenvector are approximate eigenvectors: their defect tends to zero, and the absolutely convergent power series transfers that property to F(vS). Thus a boundary zero also prevents a bounded inverse. Such a zero obstructs this globally bounded-invertible generator formula; finite-time ODEs with bounded integrable generators are invertible. This does not exclude unbounded generators, other parameterizations, or enlarged systems. No scalar attenuation, source change, memory kernel, or alternative interpolation was used.

## 9. Evidence and continuation

[Exact support program](../numerics/mc08_e01_exact_bounds.py) and [small execution record](../numerics/MC08_E01_EXACT_BOUNDS_20261102.json) replay rational inequalities, the exponential estimates and the polynomial identity. They check this proof's constants and algebra, not theta quadrature, unknown minors, or universal claims by finite samples. The polynomial identity is compared coefficient by coefficient. The analytical source, tail, symbol and CP proofs above remain the evidence for the infinite statements.

The unpaid research is the common fermionic instrument and its signed readout, followed by a source-dependent signed comparison. No new range of the order-three neighboring-index estimate or real Mellin curvature has been proved. The parameter \(v\) remains jump-length activity, not source heat time or Mellin tilt.

**Next: [B] MC08-B01 — Astra.** Select and freeze one physical architecture using this E01 return and its limited checking status. Compare at most the default finite-mode quadratic Hamiltonian plus linear fermion loss and one explicitly specified alternative if needed. Fix locality, system/environment size, measurement and parity convention, success probability, finite/infinite scope and the unchanged signed observable. Issue E02 only after that choice; E03 remains the planned separate assessment of the frozen E01/E02 results. Do not spend the next task optimizing \(v_*\) without a concrete consumer.

For model changes, use the [continuation note](../research-progress/handoffs/01_MC08_E01_CONTINUATION_20261102.md). The [sole live register](../research-progress/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md) owns current status. This chat has its own unique [branch history registration](../chat-histories/index.json); the brainstorm chat stays in its existing home.
