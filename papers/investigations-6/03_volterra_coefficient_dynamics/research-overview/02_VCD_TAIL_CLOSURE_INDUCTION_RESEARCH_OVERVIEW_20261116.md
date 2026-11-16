# Tail closure and degree induction for the theta Jacobi chain

**Sub-investigation organization, 16 November 2026, chat0004:** the three
routes discussed in [note28](../notes/28_VCD_COLLISION_CONTROL_ROUTE_DISCUSSION_20261116.md)
now have individual READMEs and scientific overviews:
[gap transport](../01_cluster_gap_transport/README.md),
[degree contraction](../02_degree_nonreality_contraction/README.md), and
[multiscale collision bounds](../03_multiscale_collision_bounds/README.md).
Edward selects gap transport first; its
[continuation](../01_cluster_gap_transport/notes/01_VCD_GT_SETUP_CONTINUATION_20261116.md)
guides the later plan/register setup. No child plan or progress file is
created yet, and parent B07/E25 retain their ownership/status. The child
overviews cite the [result](../../../../result-summaries/README.md) and
[avoid](../../../../avoid/README.md) indexes with route-specific control
screens. Organizational update for Edward Baker with Codex assistance;
actual model/effort unavailable, no new mathematical result.

**Cluster-resolution discussion, 16 November 2026, chat0004:** [note27](../notes/27_VCD_CLUSTER_RESOLUTION_AND_HEAT_COLLISIONS_20261116.md) develops the author's unresolved-pair idea in manuscript §10.4: compact convergence uniform in heat time, error bounds for the pair center and squared separation, and shrinking uncertainty near a stipulated fixed double event. §5.3 now explicitly says polynomial phase does not count F zeros. [Assessment11](../reviews/11_VCD_CLUSTER_RESOLUTION_ASSESSMENT_20261116.md) is same-assistant checking; no collision exclusion or growing-domain result. B07 unactivated/E25 unissued. For Edward Baker with Codex assistance; actual model/effort unavailable. [Result](../../../../result-summaries/README.md) clusters13/18 and [avoid](../../../../avoid/README.md) patterns01/02/07/13/15 are linked precisely in note27.

**Fixed-zero discussion, 16 November 2026, chat0004:** [note26](../notes/26_VCD_FIXED_ZERO_STABILIZATION_AND_PHASE_20261116.md) records manuscript Proposition 10.2 and Corollary 10.3: isolated clusters stabilize, and a fixed simple real zero has an alternating displacement asymptotic with successive ratio O_r(log²(N+1)/N²). The statement is conditional on the chosen limiting zero and is not uniform over increasing zero index. [Assessment10](../reviews/10_VCD_FIXED_ZERO_COROLLARY_ASSESSMENT_20261116.md) is same-assistant checking. B07 remains ready/unactivated and E25 unissued. For Edward Baker with Codex assistance; actual model/effort unavailable. The [result index](../../../../result-summaries/README.md) and [avoid index](../../../../avoid/README.md), specifically cluster18 and pattern13 linked in note26, govern this classification.

**Manuscript discussion update, 16 November 2026, chat0004:** the [expanded analytical manuscript](../manuscript/README.md) now derives the background and relevant E04/E08/E13/E15/E21/E22/E24 results in one development. [Integration25](../notes/25_VCD_ANALYTICAL_READOUT_MANUSCRIPT_INTEGRATION_20261116.md) maps the sections, classifies the conditional zero results and applies the existing control catalog. Polynomial phase and a local zero-displacement lemma make the missing Fourier-readout input explicit. [Assessment09](../reviews/09_VCD_READOUT_MANUSCRIPT_ASSESSMENT_20261116.md) is same-assistant checking only. No B07 activation, E25 issue or canonical zero theorem. For Edward Baker with Codex assistance; actual model/effort unavailable. The result/avoid indexes and specific patterns cited below remain governing.

**Current B06 research update, 16 November 2026, chat0003:** [Synthesis23](../notes/23_VCD_B06_SIGNED_ERROR_CONSUMER_SYNTHESIS_20261116.md) selects a directed signed enclosure for the physical E15 quadrature error. E21 gives its exact probability factor; E22 pays a degree-only phase budget O(|z|² log²(N+1)/N), uniform in |Im z|<=1; E24 compares coefficient cost and proves pointwise/conditional contour consumers. [E23](../reviews/08_VCD_E23_SIGNED_ERROR_CONSUMER_ASSESSMENT_20261116.md) accepts the proofs and clarified synthesis within scope. The canonical boundary separation and finite-model zero count remain unproved; weighted-square controls share the phase estimate. B07 owns that next conceptual question. Prepared for Edward Baker with Codex assistance; lead actual settings unavailable, fixed helper dispatches Sol6.1/ultra. Earlier readiness labels and input hashes are historical; register02 remains authoritative. The result/avoid indexes and specific scopes cited below remain governing.

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. This setup's recorded turn
configuration is **gpt-6-astra / max**; separate backend attestation is
unavailable. Edward selects **ultra** for subsequent investigation runs
and explicitly permits **GPT-6.1 Sol** subtasks. Requested future settings
are distinct from the configuration that authored these documents.

**Research proposal; no closure invariant or zero-confinement theorem has
been established.** This is a new phase of the existing VCD investigation,
not a new manuscript or a replacement for its completed coefficient work.
Start with the [plan](../research-plan/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PLAN_20261116.md),
[sole live register](../research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md)
and [continuation prompt](../notes/03_VCD_TAIL_CLOSURE_INDUCTION_CONTINUATION_20261116.md).
The [first overview](01_VOLTERRA_RESEARCH_OVERVIEW_20261113.md) retains the
broader coefficient background.

**Activated-session update, 16 November 2026:** [Synthesis09](../notes/09_VCD_CONNECTED_RESEARCH_SYNTHESIS_20261116.md) supersedes the setup-time unassessed/readiness descriptions below for the memory and score foundations. Notes04–08 and10 have internal E09/E11 acceptance. A source characterization, exponential score estimate and scoped finite-closure obstructions are now available; no source-sensitive zero-confinement invariant has been established. Lead backend/effort unavailable, helpers explicitly Sol6.1/ultra. The [live register](../research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md) owns current status.

**Midpoint extension, 16 November 2026:** Edward asks to investigate
truncation of the intermediate-mode sum as well as closure of the boundary
memory. Section 4.1 makes that strategy explicit; §5 relates it to the
completed research. This is a planning addition, not a restart or a new
research result. Prepared for Edward Baker with OpenAI Codex assistance,
recorded authoring configuration **gpt-6-astra / max**; the prior research
lead's unavailable configuration remains unavailable.

## 1. Scientific objective and the author's choices

Investigate whether the complete theta source imposes a class of
constraints on the unresolved part of its Jacobi chain that can be
propagated when one more polynomial degree is retained. The desired
inductive object combines a tail response, a controlled closure residual,
and source consistency. Its intended consequence is a restriction on the
zeros of the scalar Fourier observation.

The long-term possibility is a sequence of analytically controlled
approximants whose nonreal zeros are confined to strips approaching the
real axis on every fixed complex region. A valid limiting argument would
then establish real zeros for the actual time-zero theta field. The
unresolved work is the source-sensitive invariant and its propagation;
the limiting argument alone is not progress toward that conclusion.

Edward's directions in the [16 November discussion, especially §7](../brainstorm/notes/03_VCD_INDUCTION_TRUNCATION_AND_ZERO_CONTROL_20261116.md)
fix the research emphasis:

- Keep the orthogonal-polynomial/Jacobi-chain representation. Do not
  reopen the Jensen-polynomial program as a substitute.
- Model the influence of the omitted tail. BBGKY-style hierarchy closure
  and projection with memory are sources of ideas, not assumed theorems
  about the theta field.
- Also retain finitely many amplitudes at the midpoint of the evolution
  and approximate their omitted bilinear contribution. Keep the error in
  the retained amplitudes separate from the omitted-mode error.
- Allow finite approximants to have nonreal zeros. Their distance from
  the real axis may shrink with degree; neither finite-stage reality nor
  simplicity is a mandatory premise.
- Seek an induction mechanism. A sequence of larger numerical windows
  or smaller absolute approximation errors is not the research objective.
- Support substantial research in one activated prompt. The lead may
  complete multiple linked conceptual, analytical, diagnostic and review
  steps, delegating fixed work to Sol 6.1 and continuing after its returns.

The [result index](../../../../result-summaries/README.md), particularly
[cluster 18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
and the [avoid index](../../../../avoid/README.md) govern interpretation.
Use [01](../../../../avoid/01_restating_the_target.md) for classification,
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md) for
control premises, [03](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
for exact representations, [07](../../../../avoid/07_scoped_exclusions_read_as_universal.md)
for scoped failures and [10](../../../../avoid/10_numerics_ahead_of_the_question.md)
for the structural purpose of calculations.

## 2. Fixed source, variables and normalization

For \(u\ge0\), retain the complete canonical sum
\[
 r_m(u)=\pi m^2e^{4u},\qquad
 \Phi(u)=\sum_{m\ge1}e^u(2r_m(u)^2-3r_m(u))e^{-r_m(u)},
 \qquad W_\lambda(u)=e^{\lambda u^2}\Phi(u),
\]
with its canonical smooth even extension. The
[analytical manuscript, §2](../manuscript/main.tex) derives this source,
reflection, tails and the normalization
\[
 H_\lambda(z)=\frac12\int_{\mathbb R}W_\lambda(u)e^{izu}\,du,
 \qquad H_0(z)=\frac18\xi((1-iz)/2).
\]
Write \(Z_\lambda=\int W_\lambda\),
\(d\mu_\lambda=W_\lambda du/Z_\lambda\), and
\(F_\lambda=2H_\lambda/Z_\lambda\), so \(F_\lambda(0)=1\).
The positive normalization does not change zeros. The variables are:

| Symbol | Meaning and initial domain |
| --- | --- |
| \(u\) | Real source coordinate |
| \(n\), \(N\) | Polynomial degree and number of retained sites; nonnegative degree, \(N\ge1\) |
| \(\lambda\) | Newman time, initially \([0,1/2]\) |
| \(x\) | Real observation height; absolute zeta height is \(|x|/2\) |
| \(z=x+iy\) | Complex observation variable |
| \(s\), \(\zeta\) | Laplace/resolvent variables for a tail response; not Fourier height |

The primary zero target is at \(\lambda=0\). The lead may use uniform
\(\lambda\)-identities within the stated band when they help the same
program; proving a time-descent theorem is not a mandatory detour.

Let \(P_n\) be monic orthogonal polynomials for \(W_\lambda du\),
\(h_n=\int P_n^2W_\lambda du\), \(\beta_n=h_n/h_{n-1}\) for
\(n\ge1\), and \(a_n=\sqrt{\beta_n}\); set \(\beta_0=a_0=0\).
For the probability measure use \(q_n=\sqrt{Z_\lambda/h_n}\,P_n\).
Multiplication by \(u\) is the zero-diagonal Jacobi operator with link
\(a_n\) between sites \(n-1,n\). Its monic recurrence and time laws are
\[
 uP_n=P_{n+1}+\beta_nP_{n-1},\qquad
 \partial_\lambda\log h_n=\beta_n+\beta_{n+1},\qquad
 \partial_\lambda\beta_n=\beta_n(\beta_{n+1}-\beta_{n-1}).
\]
These are derived in [manuscript §3](../manuscript/main.tex), with the
classical source passages catalogued in the [reference index](../references/README.md).
The entrywise Lax equation is not a global unbounded-operator evolution
theorem. All uses of complex exponentials must specify a scalar/vector
domain; \(e^{izJ}\) is not presumed bounded on the whole Hilbert space.

## 3. What is already available

| Input | Source status and usable scope |
| --- | --- |
| Recurrence, coefficient flow, multiplication representation | Derived in the analytical draft; internal assessment accepted the draft within scope. No special finite theta closure follows. |
| \(\beta_n+\beta_{n+1}\le\operatorname{arcosh}^2(2n+12)/16\), all \(n\ge0\), \(0\le\lambda\le1/2\) | [Proved in-note](../notes/01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md), [accepted without correction within scope](../reviews/01_VCD_E02_ENVELOPE_ASSESSMENT_20261113.md) by same-worker internal assessment. Weighted-square collision controls pass it. |
| Norm product and finite Gaussian-quadrature readout | [Manuscript §§4–5 and Appendix A](../manuscript/main.tex), using branch 02's [finite-chain proof](../../02_jacobi_chain_height_flow/notes/02_JCH_E01_R1_FINITE_CHAIN_READOUT_20261113.md). The original absolute bound remains; the 16 November expansion derives the signed error and conditional zero consumers in §§7–10. Canonical contour separation is still open. |
| Finite coefficient acquisition | [TN6-E02](../../notes/06_TN6_E02_CERTIFIED_COEFFICIENT_ACQUISITION_20261114.md) is certified within its frozen N=16 scope; [E03](../../reviews/02_TN6_E03_ACQUISITION_ASSESSMENT_20261114.md) accepted it as a finite certificate. No growing-degree theorem or speed law. |
| Tail-memory identities, fixed-vector entire domains, complex quadrature convergence | [E04](../notes/04_VCD_E04_TAIL_FOUNDATIONS_20261116.md): **complete, checked in-note**; [E09](../reviews/04_VCD_E09_TAIL_SCORE_ASSESSMENT_20261116.md) accepted without mathematical correction within scope. Unscaled moving-site complex tail bounds fail for actual theta. |
| Canonical score domain, compression and residual accounting | [E05](../notes/05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md): **proved in-note** and accepted within E09 scope. Retained score entries are computable from the exact coefficient head; this does not compute the retained propagator. |
| Shrinking-strip limiting argument | Standard conditional application of Rouché/Hurwitz, explained in Note03 §7 and tied to [checked source passages](../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md). Its approximant premises remain unproved. |

For fixed \(\lambda\), the bare approximation
\(F_{\lambda,N}(z)=\langle e_0,e^{izJ_N}e_0\rangle\) matches moments
through degree \(2N-1\). The existing envelope supplies, for real \(x\),
\[
 |F_\lambda(x)-F_{\lambda,N}(x)|
 \le\frac{|x|^{2N}}{(2N)!}\frac{h_N}{h_0}
 \le\left[\frac{e|x|\operatorname{arcosh}(2N+10)}{8N}\right]^{2N}.
\]
Thus growing real-height windows are already available. Reproducing this
bound, or certifying more samples of it, is not the new scientific target.

## 4. Exact retained dynamics and the tail to be closed

Freeze \(\lambda\) and put \(\psi(x)=e^{ixJ}e_0\). Then
\[
 \psi_n'=i(a_n\psi_{n-1}+a_{n+1}\psi_{n+1}),\qquad
 \psi_n(0)=\delta_{n0},\qquad F_\lambda(x)=\psi_0(x).
\]
Inserting the polynomial-basis identity at the scalar's endpoint merely
selects index zero. Truncation changes the evolution: retained dynamics
may leave the finite chain and return, whereas \(e^{ixJ_N}\) removes
those excursions.

For retained sites \(0,\ldots,N-1\), let \(y\) be their exact amplitude
vector, and let \(J^{[N]}\) be the disconnected tail starting at \(N\).
Define
\[
 k_N(t)=\langle e_N,e^{itJ^{[N]}}e_N\rangle.
\]
Block elimination of the initially zero tail gives
\[
 y'(x)=iJ_Ny(x)-\beta_Ne_{N-1}
       \int_0^x k_N(x-s)y_{N-1}(s)\,ds. \tag{M}
\]
The minus sign and \(a_N^2=\beta_N\) arise from the two boundary
crossings. This is an exact real-height memory equation, not a closure.
The disconnected operator is justified by cutting a bounded finite-rank
edge of the self-adjoint chain. [E04 §§2–4](../notes/04_VCD_E04_TAIL_FOUNDATIONS_20261116.md)
checks this domain argument and fixed-vector entire continuation; it does
not supply a uniform complex bound over unscaled moving tail sites.

The tails satisfy the same one-site relation:
\[
 k_n'(x)=-\beta_{n+1}\int_0^x k_{n+1}(x-s)k_n(s)\,ds,
 \qquad k_n(0)=1,
\]
and, for real \(s>0\),
\[
 \widehat k_n(s)=\frac{1}{s+\beta_{n+1}\widehat k_{n+1}(s)}. \tag{R}
\]
The exact \(|k_n(x)|\le1\) justifies the Laplace transform. The
equivalent resolvent has
\(m_n(\zeta)=1/(\zeta-\beta_{n+1}m_{n+1}(\zeta))\).
Its half-plane sign concerns source spectral data, not Fourier zeros.

A proposed closure supplies a tractable response \(\widetilde k_N\)
and a justified residual description. A family of admissible responses
may be preferable to one guessed function. The recursion reconstructs
an inward response from a deeper tail; a forward induction or justified
terminal condition must be supplied, not assumed. Ordinary truncation
discards the memory term. Retaining the exact \(k_N\) would only restate
the original infinite problem.

### 4.1. Midpoint-mode truncation and a joint closure

The [author's midpoint clarification](../brainstorm/notes/03_VCD_INDUCTION_TRUNCATION_AND_ZERO_CONTROL_20261116.md)
inserts the identity between two half-height propagators. With the usual
Hermitian inner product and real \(x\),
\[
 F_\lambda(x)=\langle e^{-ixJ/2}e_0,e^{ixJ/2}e_0\rangle,
 \qquad \|e^{ixJ/2}e_0\|^2=1.
\]
The bra of \(e^{ixJ/2}e_0\) has the opposite exponential sign. The
midpoint decomposition is consequently a bilinear amplitude sum, not
a probability sum.

For fixed \(\lambda\), set
\[
 c_n(z)=\langle e_n,e^{izJ/2}e_0\rangle
       =\int q_n(u)e^{izu/2}\,d\mu_\lambda(u).
\]
E04's fixed-vector domain applies to \(c(z)=e^{izJ/2}e_0\). The real
polynomial basis identifies the continuous bilinear pairing
\(B(v,w)=\sum_n v_nw_n\) with \(\int vw\,d\mu_\lambda\), giving
\[
 F_\lambda(z)=\sum_{n\ge0}c_n(z)^2,
 \qquad \|c(z)\|_{\ell^2}^2=F_\lambda(i\Im z). \tag{P}
\]
This uses the spectral representation on the stated vectors, not an
assumption that complex exponentials are bounded operators. On the real
axis, \(c_n(x)=i^n b_n(x)\) with real \(b_n\), so the bilinear terms
have sign \((-1)^n\); their absolute squares sum to one.

Define the exact midpoint head and omitted contribution by
\[
 \mathbf c_N(z)=\Pi_Nc(z),\qquad
 S_N(z)=\sum_{n<N}c_n(z)^2,\qquad
 R_N(z)=\sum_{n\ge N}c_n(z)^2,
 \qquad F_\lambda=S_N+R_N. \tag{P1}
\]
For every fixed compact complex set \(K\), the entire \(\ell^2\)-valued
orbit has compact image, hence its projection tails tend to zero uniformly:
\[
 \sup_{z\in K}|R_N(z)|
 \le\sup_{z\in K}\|(I-\Pi_N)c(z)\|^2\longrightarrow0. \tag{P2}
\]
Thus the series is absolutely and locally uniformly convergent, and
\(S_N,R_N\) are entire even functions. These are generic representation
consequences of the established domains, recorded here for the dedicated
E13 audit; they are not a new theta zero estimate. They do not contradict
E04's divergence over moving tail origins: (P2) projects one fixed
\(e_0\)-orbit, rather than bounding \(k_N\) uniformly in \(N\).

The exact \(S_N\) is not yet a computable finite closure. Each retained
\(c_n\) includes excursions through the full chain; even
\(c_0(z)=F_\lambda(z/2)\). A finite sum of these functions is generally
not a polynomial in \(z\). The identities
\[
 S_{N+1}=S_N+c_N^2,\qquad R_{N+1}=R_N-c_N^2
\]
are exact bookkeeping, not a predictive induction from finite data.

A useful model could instead produce retained amplitudes
\(\widetilde{\mathbf c}_N\) and an omitted contribution \(\widetilde R_N\),
linked to the same source-consistent boundary closure, and form
\[
 G_N=\widetilde{\mathbf c}_N^{\mathsf T}\widetilde{\mathbf c}_N+\widetilde R_N.
\]
The two errors must both remain visible:
\[
 F_\lambda-G_N
 =(\mathbf c_N+\widetilde{\mathbf c}_N)^{\mathsf T}
   (\mathbf c_N-\widetilde{\mathbf c}_N)
   +(R_N-\widetilde R_N). \tag{P3}
\]
A norm bound on the first term and an absolute bound on the second give
convergence if they tend to zero on compact sets. They do not by
themselves yield a sign or zero-free region. Preserve correlations
between these errors when a proposed signed estimate needs them; see
[pattern12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
Equation (M) at height \(z/2\) governs the retained amplitudes;
E04's vector Duhamel formula supplies the omitted tail from the same
boundary forcing. The model still owes a useful
update/base or terminal condition and a Fourier-zero consequence.

There is an exact baseline to retain. If
\(\widetilde{\mathbf c}_N=e^{izJ_N/2}e_0\) and \(\widetilde R_N=0\), then
transpose symmetry of the finite matrix gives
\[
 \widetilde{\mathbf c}_N^{\mathsf T}\widetilde{\mathbf c}_N
 =e_0^{\mathsf T}e^{izJ_N}e_0=F_{\lambda,N}(z). \tag{P4}
\]
That choice is the existing Gaussian-quadrature approximation. The new
question is whether a source-constrained joint amplitude/tail description
retains enough additional information to support induction and zero
confinement. It is not a claim that splitting the same finite exponential
already improves that approximation.

## 5. Source consistency and hierarchy methods

Put \(V_\lambda=-\log W_\lambda\). The source identity is
\[
 \int V_\lambda'P_nP_{n-1}W_\lambda\,du=n h_{n-1},
 \qquad a_n[V_\lambda'(J)]_{n,n-1}=n\quad(n\ge1). \tag{S}
\]
The latter is a matrix element of multiplication by \(V_\lambda'\)
on polynomial vectors. Its integrability is part of the source-tail
analysis. A polynomial score gives a banded matrix and finite neighboring
relations; the Gaussian and quartic illustrations are inherited, with
[Van Assche §3, equation (3.1)](../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md)
checked for the quartic case.

For theta the score contains the complete sum. In particular, the finite
matrix correction
\[
 C_N^V=\Pi_N V_\lambda'(J)\Pi_N\big|_{\operatorname{ran}\Pi_N}
                -V_\lambda'(J_N)
\]
cannot be set to zero without justification. Writing it is only a
definition. The completed [E05](../notes/05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md)
now expresses the retained score block through polynomial derivatives,
so its value is determined by the exact retained head. The predictive
size/sign estimate and link to boundary memory remain unpaid. This
finite score bookkeeping must not be confused with computing
\(\Pi_Ne^{izJ/2}e_0\) from the same head.

The [completed session](../notes/09_VCD_CONNECTED_RESEARCH_SYNTHESIS_20261116.md)
constrains both closure formulations:

| Completed finding | Consequence for a midpoint candidate |
| --- | --- |
| E04: fixed-vector analyticity; unscaled moving-tail nonuniformity | Use the former for (P); do not assume the latter disappears after a midpoint split. |
| E06: fixed polynomial score leaves \(n+O_p(\log^{d+1}(n+2))\); exponential reference leaves bounded canonical \(b\) and relative score error \(O(\log n/n)\) | Fixed polynomial negligibility remains excluded at its fixed-degree/coefficient scope. Retain the exact bounded remainder and needed correlations; a small relative score defect alone supplies no signed Fourier margin. |
| E08: all adjacent canonical identities identify theta in the stated integrability class; the next defect cancels from the finite commutator | Full source identification is available, but neither a finite predictive update nor a zero theorem follows from it. |
| E07 and E10: distinct finite-information controls | A new midpoint premise must be compared with each control's actual preserved data and conclusion, as in §7. Do not merge their zero and smoothness assertions. |

These inputs retain their **proved-in-note** or **complete, checked-in-note**
source status and [E09](../reviews/04_VCD_E09_TAIL_SCORE_ASSESSMENT_20261116.md)/[E11](../reviews/05_VCD_E11_SMOOTH_DEFECT_ASSESSMENT_20261116.md)
internal acceptance. No completed proof or issued request is superseded
by the new truncation choice.

BBGKY suggests reconstructing unresolved higher objects while retaining
consistency between levels; projection with memory identifies the exact
feedback that a closure approximates. [Chorin–Hald–Kupferman §2,
equations (2.4)–(2.7)](../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md)
and [Akbari et al. §§II.B–C and III.C](../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md)
are checked analogies. Their statistical/fermionic assumptions and
particular closure results are not theta premises. Here degree is not
particle-correlation order; no small-correlation or short-memory
parameter has been established.

Three candidate ways to organize the same question remain open:

1. A source-constrained class of tail responses stable under (R).
2. A structured residual hierarchy that retains source correlations
   discarded by independent absolute bounds.
3. A self-consistent response model with a proved defect and stability
   estimate, rather than an assumed equality of neighboring tails.

These are candidates for comparison within the program, not selected
closures or a requirement to survey unrelated representations. The
midpoint head/omitted-sum formulation can organize any of them; it must
still specify the extra source information it carries.

## 6. The intended induction and its zero consequence

Seek an inductive package whose hypotheses are verifiable from the
unchanged source and whose step advances the retained degree. It should
identify the true-tail membership statement, its update, the controlled
residual and the property of the scalar observation that follows. A
list of coefficient upper bounds alone need not determine any of these.

For a chosen closure producing entire \(G_N\), a sufficient final output is
\[
 G_N\to F_0\quad\hbox{locally uniformly on }\mathbb C,
 \qquad L_N\to\infty,\quad\delta_N\to0,
\]
\[
 G_N(z)=0,\quad |z|<L_N
       \quad\Longrightarrow\quad |\Im z|\le\delta_N. \tag{T}
\]
A small disk around a hypothetical nonreal zero of \(F_0\) contradicts
(T) by Rouché. Widths depending on each fixed compact radius also suffice.
No labeling of zeros or simplicity assumption is required. Real-axis
error alone does not supply the locally uniform complex convergence.

**Classification:** once local uniform convergence of the chosen family
has been established, existence of unspecified exhausting radii and
shrinking widths in (T) is equivalent to RH. Conversely, under RH each
compact set \(\{|z|\le j,\ |\Im z|\ge1/j\}\) is zero-free for
\(F_0\), hence eventually for \(G_N\) by uniform convergence; a
diagonal choice gives \(L_N\to\infty\), \(\delta_N\to0\).
Compact-dependent widths and an unspecified growing-window formulation
therefore have the same qualitative strength. Prescribed rates or a
specified invariant can be stronger requirements. The qualitative
criterion is stated here as the target, not evidence toward it; sample
checks do not support its exhausting assertion. A bare Jacobi approximation need not preserve
real zeros even for a Gaussian, as [Note03 §4](../brainstorm/notes/03_VCD_INDUCTION_TRUNCATION_AND_ZERO_CONTROL_20261116.md)
illustrates. The new work must establish an invariant or an applicable
estimate, not merely rename the required zero property.

## 7. Control screen and the scope of possible failures

The [full catalog](../../../../result-summaries/12_collision_controls_and_screening.md)
and the existing [VCD analytical screen](../notes/02_VCD_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md)
were applied as a premise comparison at setup; no certificates were rerun.
The [brainstorm §6–7 screen](../brainstorm/notes/03_VCD_INDUCTION_TRUNCATION_AND_ZERO_CONTROL_20261116.md)
covers the generic memory identities as well.

| Control family | Current premise comparison; what is not established |
| --- | --- |
| Positive three- and four-square sources | Pass the coefficient envelope, quadrature and generic memory identities. Complete canonical equal coefficients and full reflection are absent. Failure of a new quantitative closure condition has not been demonstrated. |
| Nonzero finite theta-tail changes with nonnegative resulting source; nonzero nonnegative finite zero-tail sources | The catalog's finite-source measurement audit is **proved in-note**: finitely many real and infinitely many nonreal zeros at every real heat time, within this class. These change the complete source; this is not an obstruction theorem for Jacobi compression of the unchanged theta measure. No new closure inequality has been tested on them. |
| Atomic/finite-profile sources | Atomic members have finite chains and terminating memory; they lack the positive full-line density/score needed for (S). Continuous compact triangular extensions have infinite chains but lack global strict positivity. |
| Euler-factor translates | Lack the unchanged theta summand score. The inherited envelope fails for the checked c=1/2, p=23, lambda=0 example; no extension to all parameters. |
| Reflected super-Gaussian | Fails exponential confinement at large source coordinate, while generic chain/memory identities remain. Its individual envelope comparison is untested. |
| Smooth shape/positive-primitive sources | Lack the exact theta square-summand formula. Weaker score/envelope comparisons remain untested. |
| Finite-prime square perturbations | Lack full canonical reflection; finite constraints and some score bounds can persist. No exclusion of controlled infinite assembly. |
| RH-conditional endpoint constructions | Retain their RH hypothesis and lack ordinary Dirichlet arithmetic/unchanged theta formula. No new coefficient comparison. |
| Fixed source with altered readout | Retains coefficients but fails the literal Fourier/Newman observation. |
| Actual-profile positive-measure relaxation | Does not supply the same full-line physical source and Fourier field. |
| E07 finite canonical-score controls | Preserve any specified finite head/canonical-score data and arbitrarily small bounded score error, but have nonreal zeros in their stated finite square-change class. Higher smooth reflection fails; no compact zero location is prescribed. |
| E10 smooth compact-multiplier controls | Preserve the full reflection jet, exact real tails, finite head/lower score defects and envelope while changing the next defect. Canonical arithmetic square structure fails; their Fourier zero locations are unestablished. |

Regular controls satisfy integration by parts with their **own** score.
That does not establish (S) with the unchanged canonical theta score.
Nor does absence of the canonical formula prove failure of a particular
derived inequality. Each candidate must identify its actual distinguishing
premise, or be rejected as insufficient within its tested class.

The midpoint identity, parity decomposition and compact convergence apply
to the real Jacobi controls with the required exponential moments, including
the E07/E10 classes. They therefore supply no new discriminator. E07's
finite-data obstruction and E10's next-equation obstruction do not exclude
growing-degree, compact-dependent confinement with a further proved
canonical premise. Merely using the exact full-source amplitudes would
hide that premise inside the unknown solution. A new inequality remains
untested until its actual source/region/quantifiers have been specified.

## 8. What would count as scientific progress

Useful outcomes include a verifiable source constraint on tail responses,
a noncircular class-membership lemma, an invariant one-site update,
a residual estimate with a named zero-sensitive consumer, or a scoped
obstruction showing why a specified closure loses necessary information.
A complete induction could eventually combine these with (T).

Exact identities are retained as infrastructure. A numerical diagnostic
is useful only when it decides a stated candidate lemma or controls a
specified proof constant. High-degree sampling, generic positivity and
smaller absolute error without an induction consequence do not complete
this program. A failed candidate may trigger a revised B decision and
new bounded Sol work during the same prompt; it does not automatically
end the investigation.

## 9. Ownership, references and execution

VCD owns this source-constrained tail-closure question and its induction
tasks. Branch 02 retains its fixed-initial-basis transport results and
JCH statuses; the new use of a Jacobi tail transfers none of those tasks.
The parent TN6 family owns shared interfaces only. No QTT or ITP task is
activated by this setup.

The [reference index](../references/README.md) identifies the existing
canonical catalog, branch-only [passage records](../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md)
and [bibliography](../references/induction.bib). This overview reuses those
checked passages; it is not a new literature audit. Previous direct-PDF
retrieval failures remain failures. New sources and newly inspected
passages must be recorded immediately under
[REFERENCE_WORKFLOW](../../../../REFERENCE_WORKFLOW.md).

The plan implements the author's investigation-specific change to
[INVESTIGATION_SETUP_WORKFLOW](../../../../INVESTIGATION_SETUP_WORKFLOW.md)
and [GPT_RESEARCH_MODEL_WORKFLOW](../../../../GPT_RESEARCH_MODEL_WORKFLOW.md):
bounded work packets serve a sustained lead session, and their completion
does not force a user handoff. Setup has prepared the documents; research
has since completed the first connected round described above. B04 remains
the next ready conceptual decision, E12 its reserved execution, and E13
the newly ready, unissued midpoint foundation task. This planning update
does not dispatch them; a subsequent continuation can proceed through
multiple linked steps under the existing authorization.
