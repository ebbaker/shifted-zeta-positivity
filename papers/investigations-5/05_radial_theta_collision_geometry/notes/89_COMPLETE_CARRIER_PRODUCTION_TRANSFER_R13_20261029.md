# Complete actual-to-carrier production and dissipation transfer

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
ultra**, Investigation05 **chat0033**, *Investigate radial theta collision
geometry*. Parent research synthesis with same-model contributing
derivations and checks; no independent specialist review.

**Status: proved in-note from the accepted R11/R12 inputs; fixed E08
assessment pending.** Both the complete signed production and the exact
unabsorbed dissipation admit their actual-path carrier counterparts with
finite absolute-error integrals and explicit decaying tails. This extends
the selected-I1 comparison to the whole weighted-energy balance. It proves
no sign, finite original dissipation, stationary convergence or new physical
domain. The equally informed direct method supplies the complete proof.

The [frozen R13 intake][intake] records this consumer before derivation;
[Progress05][progress] remains the sole live register. [Note90][n90] pays
the distinct feedback-ratio defect and states the limits of a scalar
carrier interpretation. [Continuation91][next] gives the next model
handoff; [Review45][review] records the present internal checking. No
manuscript integration is part of this research return.

Under [avoid/01][a01], the result is a quantitative complete-correction
estimate on the already covered low mark, not another noncollision
criterion. The [result index][results], [control register][controls] and
[pattern index][avoid], particularly [scoped conclusions][a07] and
[quantitative utility][a20], govern its interpretation.

## 1. Exact triples and the full balance

Use the R12 decomposition in [Notes82][n82]–[83][n83], accepted by
[Review43][r43], at the unchanged mark (T,A)=(1/4,2):
\[
 W=W_c+e,\quad W_c=ah,\quad
 J_2=J_c+e_2,\quad J_c=a_2h,\quad Z=Z_c+Z_e,
\]
\[
 Z_c=\omega\{a\mathcal A_T h-\tau h\},\quad
 Z_e=\omega\{\mathcal A_Te-(2e_1,e_1+2e_2)\},
\]
where a=(m0/M,m1/M), a2=m2/M and tau=(2a1,a1+2a2).
The path alpha is the **same actual feedback path** in every equation.
In particular it is not recomputed from W_c or from e.

For a radial spatial triple X=(w,z,j), with w,z two-component and j
scalar, define
\[
 E(X)=\|w\|_2^2,\quad G(X)=\|\nabla w\|_2^2,\quad
 N(X)=\|\Delta w\|_2^2,\quad Y(X)=\|z\|_2^2,\quad Q(X)=\|j\|_2^2,
\]
\[
 F(X)=G(X)+Y(X)+Q(X),\qquad l=\log\omega,
 \quad h_\omega=d-2v\cdot\nabla l,\quad\nu=21/4.
\]
Write the **exact**, unabsorbed dissipation and production as
\[
 \mathcal D_s(X)=2N(X)+2\|\nabla z\|_2^2
             +2\|\nabla j\|_2^2+\alpha(s)\mathscr H_{\rm rad}(w),
                                                               \tag{1}
\]
\[
\begin{split}
 \mathcal P_s(X)={}&2\int|\nabla l|^2|z|^2
                   +2\langle z,\omega\mathscr C_0w\rangle\\
 &+\alpha\left\{10G(X)+\nu E(X)+\int h_\omega|z|^2
                   +\int d|j|^2+2\langle z,\omega\mathscr C_1w\rangle
            \right\}.                                        \tag{2}
\end{split}
\]
The actual, carrier and centered triples
X_a=(W,Z,J2), X_c=(W_c,Z_c,J_c), and X_e=(e,Z_e,e2) obey their inherited
common equations and exact canonical residual relations. For these three
triples separately,
\[
 \boxed{\frac d{ds}F(X)+\mathcal D_s(X)=\mathcal P_s(X).}       \tag{3}
\]
The carrier and centered identities use their instantaneous E(X), not
E0. Equation (3) follows from the shared linear equations and spatial
radial-square identity of [Note42][n42]. It requires neither E_c'=0 nor feedback generated
by the carrier; exactly the same observation justified R12's centered
production. The physical feedback in (3) remains the actual alpha.

D in (1) has **two** units of N. The retained R11 dissipation has one
unit after absorption of C0; this distinction is kept in all constants
below. No I1 completion is added to another full payment for the same
term. Both C0 and C1 in (2) are the full cutoff commutators.

Preparation mismatch and the combined sphere identities are those of
accepted [Note83][n83]. In particular neither R_c nor R_e is replaced by a
zero-mismatch field, and at r=1 their relation vectors cancel their own
residuals. All integrations are over the whole space, including the inner
ball. There is no artificial evolving-sphere boundary. If a primitive
representation is used, the centered endpoint factors delta_(j0)-a_j
remain; the argument below does not erase or newly estimate those traces.

## 2. Existing actual-window and centered-tail budgets

Use the accepted R11 constants F_* and E0 from [Note76][n76], and put
\[
 C_*=\kappa_0+\kappa_1\bar\alpha,
 \qquad Q_A:=F_*+C_*(F_*+E_0),\qquad U_A:=F_*+E_0.
\]
Then for every t>=0,
\[
 F(X_a(s))\le F_*,\quad E(X_a(s))=E_0,
\]
\[
 \int_t^{t+1}\left\{N(W)+2\|\nabla Z\|_2^2
          +2\|\nabla J_2\|_2^2+\alpha\mathscr H_{\rm rad}(W)\right\}ds
 \le Q_A.                                                     \tag{4}
\]
No finite half-line bound for this actual integrand is assumed.

Let
\[
 C_E=L_0+L_1,\qquad
 C_{\rm energy}=T_0+T_1+C_Z^2+L_2,
\]
\[
 \Lambda=C_{\rm energy}+2(C_{\rm energy}+C_E)(\kappa_0/a_*+\kappa_1),\qquad
 \rho(s)=e^{-B(s)/4}.
\]
Here L_j,T_j,C_Z are the accepted R12 constants. The symbol C_energy
denotes the centered **energy** allowance; it is distinct from the
selected C1 norm constant used in the earlier note.
R12 gives
\[
 E(X_e(s))\le C_E\rho(s)^2,\qquad
 F(X_e(s))\le C_{\rm energy}\rho(s)^2,                                  \tag{5}
\]
\[
 \int_t^\infty\left\{N(e)+2\|\nabla Z_e\|_2^2
          +2\|\nabla e_2\|_2^2+\alpha\mathscr H_{\rm rad}(e)\right\}ds
 \le\Lambda\rho(t)^2.                                        \tag{6}
\]
These are already proved and [assessed][r43] before the current full
comparison. They retain C0, C1, the true mismatch, cutoff derivatives,
the second jet and the full radial remainder. Thus no full-comparison
conclusion is being used to pay its own input.

Define the augmented quadratic norm
\[
 V(X)=N(X)+E(X)+F(X),
\]
\[
 V_A:=Q_A+U_A,\qquad
 V_e:=\Lambda+\frac{2}{a_*}(C_{\rm energy}+C_E).
\]
Equations (4)–(6) and B(s)-B(t)>=a_*(s-t) imply
\[
 \boxed{\int_t^{t+1}V(X_a)\,ds\le V_A,
 \qquad\int_t^\infty V(X_e)\,ds\le V_e\rho(t)^2.}             \tag{7}
\]
In particular (7) pays the second derivatives in C0. It does not suppose
a pointwise uniform H2 norm for actual fields or carrier fields.

## 3. Unit-window lemma

Suppose nonnegative functions A,E satisfy
\[
 \int_t^{t+1}A\le A_*,\qquad
 \int_t^\infty E\le E_*\rho(t)^2\quad(t\ge0).
\]
Set
\[
 S_*:=\frac1{1-e^{-a_*/4}}<\infty.
\]
Partition [t,infinity) into [t+n,t+n+1]. Cauchy–Schwarz on each window,
followed by the error tail and B(t+n)>=B(t)+a_*n, yields
\[
 \boxed{\int_t^\infty\sqrt{AE}\,ds
             \le S_*\sqrt{A_*E_*}\rho(t).}                   \tag{8}
\]
This deliberately sufficient bound uses fixed unit windows, including
the initial one. No continuous-time regularity of A beyond integrability
and no optimization of a window length is hidden. It applies even when
the actual function A has infinite total integral.

## 4. Complete production as a bounded symmetric form

Fix an auxiliary time s and **freeze the actual value of alpha(s)**.
The following spatial-form estimates hold for every admissible radial
triple with w in H2 and z,j in L2; no PDE, canonical residual relation,
preserved energy or feedback law for the test triple is assumed. The
weighted C0/C1 operators map this domain into L2 by the full coefficient
bounds in [Note40][n40]. Their already paid coefficients give
\[
 \|\omega C_0w\|_2\le A_2\sqrt{N(X)}+A_1\sqrt{G(X)}+A_0\sqrt{E(X)},
\]
\[
 \|\omega C_1w\|_2\le B_1\sqrt{G(X)}+B_0\sqrt{E(X)}.
\]
The first inequality uses the full coefficient A2 and the whole-space
identity ||D²w||2²=||Delta w||2². No second-derivative term is removed.
Further,
\[
 2|\nabla l|^2\le8,\qquad 0<h_\omega\le265/24,
 \qquad 0<d\le6,\qquad 0\le\alpha\le\bar\alpha.
\]
Using 2sqrt(xy)<=x+y in the absolute value of (2) proves
\[
 |\mathcal P_s(X)|\le C_PV(X),                                \tag{9}
\]
with the explicit fixed constant
\[
\begin{split}
 C_P=\max\big\{&A_2,\quad
 A_1+\bar\alpha B_1+10\bar\alpha,\quad
 A_0+\bar\alpha B_0+\nu\bar\alpha,\\
 &8+A_2+A_1+A_0+
        \bar\alpha(265/24+B_1+B_0),\quad 6\bar\alpha\big\}.
                                                               \tag{10}
\end{split}
\]
Every constant was paid before this comparison. In (9) no diffusion is
absorbed: it is an absolute-form bound used solely for comparing the
exact productions, while (3) retains the full dissipation (1).

For each s let p_s be the symmetric real bilinear polarization of P_s.
Because V is a squared Hilbert norm, (9) implies
\[
 |p_s(X,Y)|\le C_P\sqrt{V(X)V(Y)}.                            \tag{11}
\]
For an elementary verification, polarization gives
|p_s(X,Y)|<=C_P(V(X)+V(Y))/2. Replace X,Y by lambda X,lambda^(-1)Y and
minimize over lambda>0 to obtain (11). Thus this statement does not need
a separately imported operator theorem. The estimates apply to arbitrary spatial triples in that domain.
Polarization and rescaling do not recompute alpha or define any new
feedback evolution. The actual, carrier and centered triples are
admissible elements of this space.

Since X_c=X_a-X_e,
\[
 \delta P:=\mathcal P_s(X_a)-\mathcal P_s(X_c)
       =2p_s(X_a,X_e)-\mathcal P_s(X_e),
\]
\[
 |\delta P|\le2C_P\sqrt{V(X_a)V(X_e)}+C_PV(X_e).
\]
Apply (7) and (8). The complete production correction obeys
\[
 \boxed{\int_t^\infty|\delta P(s)|\,ds
 \le 2C_PS_*\sqrt{V_AV_e}\,\rho(t)+C_PV_e\rho(t)^2.}          \tag{12}
\]
This single estimate includes the C0 second-derivative pairing, every
lower commutator coefficient, the weight potential, both actual gradient
and field energies, the second jet and full I1. It is not merely the
previous I1 estimate counted a second time.

## 5. Complete exact dissipation as a squared Hilbert norm

The radial remainder from [Note42][n42] has the explicit squared-operator
representation
\[
 \mathscr H_{\rm rad}(w)
 =\int g_v(q)|X\cdot\nabla w+\tfrac32w|^2
                  +\int p_v(q)|w|^2,
\]
\[
 g_v(q)=\frac{11+5q}{(1+q)^2},\qquad
 p_v(q)=\frac{q(203+59q+69q^2+21q^3)}{4(1+q)^4}\ge0,
 \qquad q=|X|^2.                                             \tag{13}
\]
Therefore D_s(X) is the squared norm of the linear feature vector
\[
 \left(\sqrt2\Delta w,\ \sqrt2\nabla z,\ \sqrt2\nabla j,
 \sqrt\alpha\sqrt{g_v}(X\cdot\nabla w+\tfrac32w),
 \sqrt\alpha\sqrt{p_v}w\right).
                                                               \tag{14}
\]
The same alpha occurs for actual, carrier and errors. No time derivative
of alpha is taken in this polarization. Equation (14) includes the full
radial remainder; it is not dropped or estimated using an unproved
carrier derivative bound.

The distinction between exact and retained dissipation gives directly
from (4),(6)
\[
 \int_t^{t+1}\mathcal D_s(X_a)\,ds\le2Q_A,
 \qquad\int_t^\infty\mathcal D_s(X_e)\,ds\le2\Lambda\rho(t)^2.
                                                               \tag{15}
\]
The exact coefficient 2 on N is paid here. Quadratic polarization and
(14) imply
\[
 |\delta D|:=|\mathcal D_s(X_a)-\mathcal D_s(X_c)|
 \le2\sqrt{\mathcal D_s(X_a)\mathcal D_s(X_e)}
                          +\mathcal D_s(X_e).
\]
Applying (8) to (15) gives
\[
 \boxed{\int_t^\infty|\delta D(s)|\,ds
 \le4S_*\sqrt{Q_A\Lambda}\,\rho(t)
                         +2\Lambda\rho(t)^2.}                 \tag{16}
\]
Setting t=0 in (12),(16) proves finite total corrections with all early
costs included. Neither original dissipation nor carrier dissipation is
asserted integrable on the half-line. Carrier finite-window second
spatial derivatives follow by X_c=X_a-X_e and (15), so no independent
carrier H2 theorem has been assumed.

## 6. Energy difference and a meaningful complete limiting balance

The original and carrier weighted energies differ by a decaying amount:
\[
 |F(X_a)-F(X_c)|
 \le2\sqrt{F_*C_{\rm energy}}\,\rho+C_{\rm energy}\rho^2.                          \tag{17}
\]
This is polarization of the exact squared norm F and (5), not a claim
that F(X_a) or F(X_c) individually converges. Likewise the field energies
satisfy
\[
 |E_0-E(X_c)|
 \le2\sqrt{E_0C_E}\,\rho+C_E\rho^2.                          \tag{18}
\]
In particular the carrier field energy tends to E0, while the carrier
profile and the complete weighted energy still need not have a limit.
Equation (18) alone is not stationary convergence.

Subtract the two **exact** balances (3). With deltaF=F(X_a)-F(X_c),
\[
 \delta F'(s)+\delta D(s)=\delta P(s).                         \tag{19}
\]
Both right-hand correction functions are absolutely integrable by
(12),(16), and deltaF(S)->0 by (17). Hence
\[
 \boxed{\int_t^\infty[\delta P(s)-\delta D(s)]\,ds
                         =-\delta F(t).}                     \tag{20}
\]
This is a genuine full-balance statement. Its integrands are differences
formed at each finite s before integration; it is **not** a subtraction
of two separately divergent integrals. It also shows finite total
variation of deltaF, but gives no sign for either carrier quantity.

## 7. Dependency and scope audit

Inputs (4) and (6) are the already assessed R11 actual-window and R12
centered-tail estimates. The actual window need not decay; only the
centered tail does. The new bridge is the fixed unit-window lemma,
followed by exact quadratic polarization. The carrier comparison is
not used upstream to prove any of these inputs. The same actual alpha
path and the already paid physical mass floor remain throughout.

No contribution is omitted: C0's second derivatives are in V and (7);
all C0/C1 coefficients are in Cp; weight and J2 terms are in (2),(10);
all gradient and second-derivative dissipation is in (14); the complete
radial square is there as well. Whole-space integrations preserve the
inner ball and combined sphere cancellation. The genuine raw carrier
and centered mismatches remain those of R12.

The direct comparator has the same inputs and obtains the same result.
The gain is finite complete correction instead of a horizon-growing
constant-envelope allowance. It is not a primitive-specific benefit,
a new physical domain, a favorable sign or a closed scalar replacement
flow. The carrier still depends on the full source and actual path.
Its feedback ratio and the equation-forcing interpretation have the
separate payments and scope in [Note90][n90].

At an admitted double event the positive mass premise used to obtain
uniform K fails. Generic finite-path estimates for collision controls
can still hold on each compact regular interval. Weighted-square
low-mark admission and collisions elsewhere, variable-kernel cosine
failure, primitive-identity admission, and the distinction between a
Laguerre witness and a double event retain their accepted scopes. No
new event or quantitative source discriminator is asserted. The detailed
control premises remain those of [Review43][r43] and the
[control register][controls]; this transfer invents no additional
source-moment failure or event location.


[n40]: 40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md
[n42]: 42_RADIAL_DRIFT_PRODUCTION_IMPROVEMENT_B02_R4_20261029.md
[n76]: 76_UNIFORM_RESIDUAL_AND_FIXED_JET_CLOSURE_R11_20261029.md
[n82]: 82_COMMON_CARRIER_SYNCHRONIZATION_R12_20261029.md
[n83]: 83_FINITE_CENTERED_PRODUCTION_CORRECTION_R12_20261029.md
[r43]: ../reviews/43_COMMON_CARRIER_AND_PRODUCTION_E08_R12_ASSESSMENT_20261029.md
[n90]: 90_CARRIER_FEEDBACK_DEFECT_AND_STATIONARY_CANDIDATE_R13_20261029.md
[next]: 91_COMPLETE_CARRIER_REDUCTION_AND_MODEL_CONTINUATION_R13_20261029.md
[review]: ../reviews/45_COMPLETE_CARRIER_REDUCTION_INTERNAL_REVIEW_R13_20261029.md
[intake]: ../research-progress/handoffs/CTF-B02_COMPLETE_CARRIER_REDUCTION_R13_INTAKE_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
