# Exact mixed prime response and the finite translate obstruction

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort:
**ultra**. Two parallel same-model checks examined the operator algebra,
preparation, controls and modulation argument. They are internal checks;
the proposed Claude reconciliation and specialist human review remain open.
Repository baseline: `b2a957e9edd5230b6343b2677cad057dbb9b7a6c`.

**Status: opening round derivation.** The fixed-source mixed difference has
an exact trace identity retaining the compressed inverse and its return
terms. For the actual Sonin projection it is exactly a mixed boundary
correction. A prepared modulation family distinguishes this response from
the full Weil form of every nonzero fixed finite translate combination.
This is a scoped obstruction to a literal reduction, not a sign estimate
or an exclusion of collective arithmetic estimates.

The [initial proposal][proposal] asks for this calculation before any
prime-pair computation. The governing [result index][results], especially
[Sonin summary 07][s07], and [avoid index][avoid], especially
[01][a01], [02][a02], [07][a07], [10][a10] and [12][a12], determine the
claim classification: the identities and obstruction below are bounded
analytic outputs. The all-support comparison remains the original
positivity target and is not counted again as progress.

## 1 The source and the four actual projections

Work on \(\mathcal H=L^2(\mathbb R,dx)\), with inner product antilinear
in its first slot, \(\widehat F(t)=\int F(x)e^{-itx}\,dx\), inverse
measure \(dt/(2\pi)\), and \(U_av(x)=v(x-a)\). Fix one interval
\(I_L=(-L/2,L/2)\) and one source
\[
F=\mathcal A h,\qquad \mathcal A=-\partial_x^2+\tfrac14,
\qquad h\in C_c^\infty(I_L;\mathbb C).
\tag{1}
\]
The [canonical audit][canonical], §2, proves that this is exactly the
two-moment neutral class on the same support:
\(\int F(x)e^{\pm x/2}\,dx=0\). Neither zero mean nor additive parity
is imposed. This single \(F\), without normalization or preparation
changes between corners, is used throughout the four-place comparison.

Let \(\Pi_\infty\) be the cutoff-1 archimedean Sonin projection in
logarithmic coordinates and \(\mathcal K_\infty=\operatorname{Ran}
\Pi_\infty\). For every finite prime set \(A\), define
\[
\mathscr D_A=\prod_{j\in A}(I-j^{-1/2}U_{\log j}),\qquad
M_A=\left.\Pi_\infty\mathscr D_A^*\mathscr D_A
\Pi_\infty\right|_{\mathcal K_\infty},
\]
\[
\Pi_A=\mathscr D_A\Pi_\infty M_A^{-1}
\Pi_\infty\mathscr D_A^*,\qquad
B_A[F]=\|C_F\Pi_A\|_{\rm HS}^2.
\tag{2}
\]
Here \(C_F\) is ordinary convolution by \(F\). Every inverse in (2)
acts on \(\mathcal K_\infty\), with the displayed projections implementing
extension to \(\mathcal H\). Specifically,
\[
\ell_A^2I\le M_A\le u_A^2I,\quad
\ell_A=\prod_{j\in A}(1-j^{-1/2})>0,\quad
u_A=\prod_{j\in A}(1+j^{-1/2}).
\tag{3}
\]
These are the actual orthogonal projections from the canonical audit §3
and [finite Euler identity][euler], §2. The original semilocal stability
theorem and changing inner product are in
[Connes–Consani–Moscovici, Theorem 4.6 and §4.8](https://arxiv.org/html/2310.18423v2#S4.SS7).
Stability does not remove \(M_A^{-1}\).

Fix finite \(S\) and distinct primes \(p,q\notin S\). The four operators
are (2) with \(A=S,S\cup\{p\},S\cup\{q\},S\cup\{p,q\}\). Write
\[
\mathfrak M_{S;p,q}[F]
=B_{S\cup\{p,q\}}[F]-B_{S\cup\{p\}}[F]
-B_{S\cup\{q\}}[F]+B_S[F].
\tag{4}
\]
Archimedean smoothing makes \(C_F\Pi_\infty\) Hilbert–Schmidt;
bounded finite transport propagates this to all four corners. No trace
of an unsmoothed projection is used.

For \(d_F=\operatorname{diam}(\operatorname{supp}F)\), put
\(\kappa_F(a)=\int\overline{F(x)}F(x+a)\,dx\). Then
\(\kappa_F(a)=0\) for \(|a|\ge d_F\). Active prime powers satisfy
\(m\log j<d_F\); \(\{j:j\text{ prime},j\le e^{d_F}\}\) is a safe
complete place set. The Sonin cutoff stays 1 when \(L\) changes.
Neither (2) nor (4) requires that \(S\) already contain the active primes.

## 2 The exact inverse metric formula

Rebase on the current actual projection \(P=\Pi_S\), with
\(\mathcal K=\operatorname{Ran}P\) and \(V=C_F|_{\mathcal K}\).
All compressions in this section act on \(\mathcal K\). Set
\[
r_j=j^{-1/2},\quad \beta_j=\frac{2r_j}{1+r_j^2}<1,\quad
E_j=-\frac{\beta_j}{2}(U_{\log j}+U_{\log j}^*),\qquad j=p,q.
\tag{5}
\]
The ambient \(E_p,E_q\) commute, are selfadjoint and have norms at most
\(\beta_p,\beta_q\). Also
\(d_j^*d_j=(1+r_j^2)(I+E_j)\), where
\(d_j=I-r_jU_{\log j}\). Scalar factors cancel between the compressed
metric and smoothed numerator. Define
\[
a=PE_pP,\quad b=PE_qP,\quad c=PE_pE_qP,\qquad
\mathsf M=I+a+b+c,
\]
\[
N_0=V^*V,\quad N_p=V^*E_pV,\quad N_q=V^*E_qV,
\quad N_{pq}=V^*E_pE_qV.
\tag{6}
\]
Thus \(N_0,N_p,N_q,N_{pq}\) are trace class, and
\[
I+a\ge(1-\beta_p)I,\quad I+b\ge(1-\beta_q)I,
\quad \mathsf M\ge(1-\beta_p)(1-\beta_q)I.
\tag{7}
\]
The four traces are exactly
\[
\begin{aligned}
B_S&=\operatorname{Tr}N_0,\\
B_{S\cup\{p\}}&=\operatorname{Tr}(I+a)^{-1}(N_0+N_p),\\
B_{S\cup\{q\}}&=\operatorname{Tr}(I+b)^{-1}(N_0+N_q),\\
B_{S\cup\{p,q\}}&=\operatorname{Tr}\mathsf M^{-1}
(N_0+N_p+N_q+N_{pq}).
\end{aligned}
\tag{8}
\]
For example, \(d_pd_qP(Pd_q^*d_p^*d_pd_qP)^{-1/2}\) is an
isometry onto \(\mathscr D_{\{p,q\}}\mathcal K\), and source convolution
commutes with both transports. Its Hilbert–Schmidt norm proves the last
line. The other lines follow by the same argument. This uses the actual
transported space, without assuming invariance under individual translations.

Introduce the trace-class source defects
\[
L_p=N_p-aN_0,\qquad L_q=N_q-bN_0,\qquad L_{pq}=N_{pq}-cN_0.
\tag{9}
\]
Substitution into (8) and the bounded inverse identities give
\[
\boxed{
\mathfrak M_{S;p,q}[F]
=\operatorname{Tr}_{\mathcal K}\mathsf M^{-1}
\left[L_{pq}-(b+c)(I+a)^{-1}L_p
-(a+c)(I+b)^{-1}L_q\right].}
\tag{10}
\]
Indeed, the difference first becomes
\(\operatorname{Tr}[(\mathsf M^{-1}-(I+a)^{-1})L_p
+(\mathsf M^{-1}-(I+b)^{-1})L_q+\mathsf M^{-1}L_{pq}]\), and
\[
\mathsf M^{-1}-(I+a)^{-1}
=-\mathsf M^{-1}(b+c)(I+a)^{-1}.
\tag{11}
\]
The analogous identity with \(a,b\) interchanged finishes the proof.
No interchange of noncommuting compressed factors is made.

Writing \(A_F=C_F^*C_F\), these defects are also
\[
L_j=PE_j(I-P)A_FP,\qquad
L_{pq}=PE_pE_q(I-P)A_FP.
\tag{12}
\]
Their trace-class justification is (9), not an assumption that \(A_FP\)
is trace class. In particular the terms subtracted in (10) cannot be
discarded as small without an estimate. The metric contains the return
\[
c-ab=PE_p(I-P)E_qP.
\tag{13}
\]
Even though the ambient translations commute, \(a\) and \(b\) need not.
Both the off-range return (13) and the source defects survive compression.
Moreover \((I+a)^{-1}=\sum_{n\ge0}(-a)^n\) in operator norm: repeated
compressed returns are already present at one prime. A finite polynomial
in ambient translations does not retain these inverses.

## 3 All mixed arithmetic bulk terms cancel

For finite \(A\), the finite Euler identity proves independently that
\[
B_A[F]=\Gamma[F]-W_A[F]+K_A[F],
\]
\[
W_A[F]=\sum_{j\in A}\sum_{m\ge1}(\log j)j^{-m/2}
\{\kappa_F(m\log j)+\kappa_F(-m\log j)\}.
\tag{14}
\]
Here \(\Gamma[F]=\int\gamma_\infty(t)|\widehat F(t)|^2dt/(2\pi)\),
\(\gamma_\infty(t)=\Re\psi(1/4+it/2)-\log\pi\). To specify the
independent boundary term, let \(R_+=1_{(0,\infty)}\), \(\chi=I-R_+\),
\(D=-i\partial_x\), and let \(\mathcal F_A\) be the actual finite Euler
involution of the finite Euler note, §§1–2. Put
\[
T_A=\chi\mathcal F_AR_+,\quad C_A=\chi\mathcal F_A\chi,\quad
a_{F,e}(t)=\tfrac12(|\widehat F(t)|^2+|\widehat F(-t)|^2),
\quad X_{F,e}=R_+a_{F,e}(D)\chi.
\]
\[
K_A[F]=2\Re\operatorname{Tr}_{\chi\mathcal H}
\left(C_A(I_\chi-C_A^2)^{-1}T_AX_{F,e}\right).
\tag{15}
\]
The inverse acts on \(\chi\mathcal H\); the established bound
\(T_AT_A^*=I_\chi-C_A^2\ge g_AI_\chi\), \(g_A>0\), justifies it.
The crossing operator \(X_{F,e}\) is trace class by the Schwartz cutoff
lemma. \(C_A\) is compact, but need not be Hilbert–Schmidt.

Since \(\Gamma\) is constant across the four corners and \(W_A\) is
additive in individual primes, (14) gives the actual-source equality
\[
\boxed{\mathfrak M_{S;p,q}[F]=\Delta_p\Delta_qK_S[F].}
\tag{16}
\]
This remains valid for inactive primes. A complete residual
\(Q[F]-B_A[F]\) has mixed difference \(-\mathfrak M\); a partial
arithmetic residual has the same mixed difference because its added
prime terms also cancel. Once all active primes are present,
\(Q[F]=B_A[F]-K_A[F]\). These statements keep complete and partial
arithmetic bookkeeping separate as required by the place-addition
note, (A9)–(A10).

The condition \(\log(pq)\ge d_F\) only kills the literal sample
\(\kappa_F(\log(pq))\); it need not kill the sample at
\(\log(p/q)\), and it gives no vanishing theorem for (10).
Equation (16) identifies a boundary response, not a new composite-prime
label in the Weil bulk.

## 4 A prepared modulation test for the actual Sonin boundary

Fix nonzero \(h\in C_c^\infty(I_L)\) and \(\tau\ge1\). Define
\[
F_\tau=\tau^{-2}\mathcal A(e^{i\tau x}h)
=e^{i\tau x}g_\tau,\qquad
g_\tau=h-\frac{2i}{\tau}h'+\frac{\mathcal A h}{\tau^2}.
\tag{17}
\]
Every source is exactly prepared on the same interval. The envelope
\(g_\tau\to h\) in \(C_c^\infty\), and
\(\|F_\tau\|_2\to\|h\|_2>0\). Thus the following limit does not arise
by shrinking the source norm to zero.

**Proposition.** For every fixed finite \(A\),
\[
K_A[F_\tau]\longrightarrow0.
\quad\text{Consequently}\quad
\mathfrak M_{S;p,q}[F_\tau]\longrightarrow0
\tag{18}
\]
for every fixed quartet. The same holds for a fixed finite linear
combination of such mixed differences with fixed coefficients.

**Proof.** Let \(Z_h=R_+|\widehat h|^2(D)\chi\), and let
\(\mathcal M_\tau\) denote multiplication by \(e^{i\tau x}\).
The source-smoothed cutoff lemma in the finite Euler note §3 gives
\(Z_h\in\mathfrak S_1\) and continuity of \(h\mapsto Z_h\) in
trace norm on a fixed compact smooth support. Direct Fourier conjugation
shows
\[
X_{e^{i\tau x}h,e}
=\tfrac12\left(\mathcal M_\tau Z_h\mathcal M_\tau^*
+\mathcal M_{-\tau}Z_{\bar h}\mathcal M_{-\tau}^*\right).
\tag{19}
\]
Here \(|\widehat{\bar h}(t)|^2=|\widehat h(-t)|^2\), which accounts
for the even symbol without imposing parity.

The operator \(Y_A=C_A(I_\chi-C_A^2)^{-1}T_A:R_+\mathcal H\to
\chi\mathcal H\) is compact because \(C_A\) is compact. For a rank-one
crossing operator \(Z=|u\rangle\langle v|\),
\[
\operatorname{Tr}(Y_A\mathcal M_\tau Z\mathcal M_\tau^*)
=\langle\mathcal M_\tau v,Y_A\mathcal M_\tau u\rangle\to0.
\]
Indeed \(\mathcal M_\tau u\rightharpoonup0\) by the Riemann–Lebesgue
lemma, and compactness gives \(\|Y_A\mathcal M_\tau u\|\to0\).
Finite-rank approximation in trace norm proves the limit for every
\(Z\in\mathfrak S_1\), uniformly in the approximation error because
modulation preserves trace norm. Apply this to (19). Finally replace
\(h\) by \(g_\tau\): the additional error tends to zero since
\(Z_{g_\tau}\to Z_h\) and \(Z_{\bar g_\tau}\to Z_{\bar h}\) in trace
norm. Equation (15) gives the first limit, and (16) gives the rest. ∎

The proposition uses the actual finite-place compact boundary operator.
Its limits are for fixed \(A,S,p,q,L\); no uniformity in a growing
prime set or support is asserted.

## 5 What this rules out on a finite translate span

[Claude's reply][reply], §5, predicts that the mixed term is sampled
autocorrelation through the compressed metric and that its accumulation
over a group of primes is the Weil form on a span of translates.
Equations (10) and (16) give the complete operator comparison. The
following two consequences distinguish literal versions of that prediction.

First, suppose a fixed finite accumulation \(\mathcal E[F]\) of mixed
responses were equal, on every prepared source in \(I_L\), to
\[
Q\left[\sum_{j=1}^n c_jU_{t_j}F\right],
\tag{20}
\]
where the shifts are distinct and the coefficient vector is fixed and
nonzero. It cannot be so. To prove this, set
\(H_\tau=\sum_jc_jU_{t_j}F_\tau\). These sources remain prepared, on a
fixed enlarged support, and
\[
H_\tau=e^{i\tau x}\sum_jc_je^{-i\tau t_j}U_{t_j}g_\tau.
\]
Distinct translates of nonzero compactly supported \(h\) are linearly
independent: Fourier transformation would otherwise make a nonzero
exponential polynomial vanish wherever \(\widehat h\ne0\).
Their finite Gram matrix is therefore positive definite. Since
\(g_\tau\to h\), it follows that \(\|H_\tau\|_2^2\ge\eta>0\)
for all sufficiently large \(\tau\), independently of the phases.

The envelopes above have uniformly bounded Schwartz seminorms. The
digamma asymptotic in the stated gamma normalization therefore yields
\[
\Gamma[H_\tau]=(\log\tau)\|H_\tau\|_2^2+O(1).
\tag{21}
\]
For clarity, split the Fourier integral into \(|t-\tau|\le\tau/2\)
and its complement. On the first part,
\(\gamma_\infty(t)=\log\tau-\log(2\pi)+O(|t-\tau|/\tau+1/\tau)\);
uniform Schwartz tails make the complementary integral negligible.
The complete prime sum on this fixed enlarged support is bounded, since
it has finitely many active powers and
\(|\kappa_{H_\tau}(a)|\le\|H_\tau\|_2^2=O(1)\). Pole neutrality gives
\[
Q[H_\tau]\longrightarrow+\infty,
\qquad \mathcal E[F_\tau]\longrightarrow0.
\tag{22}
\]
This disproves (20), also with a fixed nonzero scalar multiplying its
right side. It does not disprove a separately specified signed combination
of Weil Gram entries, a subtraction, a renormalization, or a statement
only about equivalence of positivity properties. Those claims need their
own formula and quantifiers; the phrase “Weil form on a span” does not
specify them.

Second, a universal expression for \(\mathcal E[F]\) as a fixed linear
combination of finitely many fixed autocorrelation samples is trivial on
this source class.
Indeed
\(\kappa_{F_\tau}(a)=e^{i\tau a}(\kappa_h(a)+O(\tau^{-1}))\).
After grouping repeated frequencies and the conjugate terms, such a
formula is a finite exponential polynomial plus \(o(1)\). By (18) it
tends to zero. Averaging its product with each conjugate frequency on
\([1,T]\) forces every grouped coefficient to vanish. A real smooth
positive bump can be chosen with \(\kappa_h(a)>0\) at every specified
\(|a|<L\); samples at \(|a|\ge L\) already vanish for all sources.
Thus a nonzero mixed response, if established, cannot be a fixed linear
combination of bare fixed samples such as \(\pm\log p\pm\log q\).
This does not assert that the actual mixed response is nonzero, nor
exclude a trace involving samples with intervening projections and inverses.

## 6 The generic sign control and its missing premise

The one-prime control in [place addition][addition], (A14), extends to a
mixed sign control that preserves preparation and a single unitary group.
Take \(\mathcal H_0=\mathbb C^2\), let \(P_0\) project onto
\((1,1)/\sqrt2\), and set
\[
U_a^0=\operatorname{diag}(1,e^{-ita}),\quad t=\pi/\log2,\qquad
(C_F^0)^*C_F^0=\operatorname{diag}(k_1,k_2),\quad k_i\ge0.
\]
Use the actual weights \(r_j=j^{-1/2}\) for \(j=2,3\), and put
\[
h_{j1}=(1-r_j)^2,\quad
h_{j2}=1+r_j^2-2r_j\cos(t\log j),\quad
z_j=\frac{h_{j2}-h_{j1}}{h_{j2}+h_{j1}}.
\]
Both \(z_2,z_3>0\): equality for \(j=3\) would require
\(\log3/\log2\in2\mathbb Z\), which is impossible. Direct rank-one
compression gives, with \(d=(k_2-k_1)/2\),
\[
B_j=B_0+dz_j,\quad
B_{23}=B_0+d\frac{z_2+z_3}{1+z_2z_3},\qquad
\boxed{\mathfrak M_{\varnothing;2,3}
=-d\frac{z_2z_3(z_2+z_3)}{1+z_2z_3}.}
\tag{23}
\]
It has either sign. Moreover \(C_F^0=\int F(a)U_a^0\,da\) can be
realized by a compact prepared source with any prescribed two Fourier
values: the functionals \(h\mapsto\widehat h(0),\widehat h(t)\)
are linearly independent on every nonempty interval, and preparation
multiplies those values by \(1/4,t^2+1/4\). Thus neither exact pole
neutrality, actual prime weights, a unitary translation group nor positive
compressed metrics gives a mixed sign. The missing premise is the actual
Sonin projection in \(L^2(\mathbb R)\). This control is not an
actual-Sonin counterexample.

The other controls have different scopes. The [smooth-density witness][s04]
changes the discrete prime measure, and its quoted cosine source is not
on this prepared core; it screens arguments indifferent to that arithmetic
replacement. The two-channel obstruction in the same summary screens a
specified decomposition into separately positive gamma and prime channels;
it does not exclude (10). The [collision controls][s12] screen later
noncollision implications: the Euler-factor family changes the arithmetic
family, weighted-square families lose full reflection, reflected families
lose the integer-square source, and the smooth/primitive families do not
have the full theta arithmetic. None is supplied with the actual Sonin
source/projection contract used here. No noncollision or positivity
conclusion is inferred from the identities, so these controls are not
being required to contradict an unrelated finite Sonin theorem.

## 7 The next decision within round 1

The opening contract and exact derivation are now written, with a precise
actual-Sonin obstruction to the literal finite-translate equality. Round 1
remains active. Following the [portfolio review cadence][portfolio], a
formal review follows a coherent round output rather than gating each note.
The original proposal's cross-model reconciliation remains to be performed;
same-model checks do not substitute for it.

The next useful analytic input is either an explicit corrected signed
Weil-Gram identity retaining all metric and boundary terms, or a signed
estimate for the paired expression (10) on an actual prepared source class,
with declared \(S,p,q,L\) dependence and an improvement to a named residual
budget. A bound that merely assumes \(K_A\le B_A\) is the original
target. Generic positivity and separate absolute bounds do not supply that
input. No prime-pair sweep, projection discretization, manuscript, global
sign theorem, or numerical gain is claimed by this opening note.

[proposal]: ../../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md
[portfolio]: ../../../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md
[canonical]: ../../../../weil-positivity/susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md
[addition]: ../../../../weil-positivity/susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md
[euler]: ../../../../investigations/sonin-critical-boundary/notes/FINITE_EULER_BOUNDARY_IDENTITY_20261003.md
[reply]: ../../../../brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md
[results]: ../../../../../result-summaries/README.md
[s07]: ../../../../../result-summaries/07_sonin_critical_boundary.md
[s04]: ../../../../../result-summaries/04_positive_constructions_and_scoped_obstructions.md
[s12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
