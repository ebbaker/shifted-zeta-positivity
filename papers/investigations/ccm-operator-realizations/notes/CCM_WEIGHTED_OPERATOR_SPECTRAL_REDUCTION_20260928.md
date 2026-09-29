# Weighted Xi jump operator: exact conjugation, essential edge, and localization

28 September 2026. Prepared for Edward Baker with LLM assistance. Model: GPT-6 (Codex); exact serving variant and configured effort are not exposed to this agent. Analytic working derivation, not formal verification or independent human refereeing. Analytic derivation; no numerical sweep. The repository LARGE_FILES policy was read.

## 1. Result and inputs

The positive weighted jump operator has essential spectral **bottom exactly 1/4**, unconditionally. Its spectrum strictly below 1/4 consists of isolated eigenvalues of finite multiplicity, with only possible accumulation at 1/4. A subthreshold eigenfunction a fixed distance below 1/4 is quantitatively concentrated in a bounded interval. This gives a compact reduction at each fixed spectral depth; it does not exclude eigenvalues accumulating toward the threshold, and does not prove RH.

The proof needs no PNT estimate. The exact annihilator identity combines the gamma and prime diagonal contributions before estimating them. The resulting weighted prime off-diagonal operator is norm summable and has small exterior compression.

Inputs and normalization are from the repository note [CCM_COMPLEMENT_DENSITY_AND_WEIGHTED_GAP_20260928.md](CCM_COMPLEMENT_DENSITY_AND_WEIGHTED_GAP_20260928.md), Sections 1 and 5:

\[
k(x)=e^{x/2}\sum_{n\ge1}\frac\pi2(ne^x)^2
  \bigl(2\pi(ne^x)^2-3\bigr)e^{-\pi(ne^x)^2},
\quad \widehat k=\Xi/4,
\]
\[
c(x)=\cosh(x/2),\quad m(x)=k(x)c(x),\quad d\mu=m(x)dx,
\quad M=\int d\mu=\tfrac18,\quad s=2M=\tfrac14.
\tag{1}
\]

k is real, even, strictly positive, and smooth. It and all its derivatives decay superexponentially. Let J be the self-adjoint operator of the closure, on L2(mu), of

\[
\mathcal E(u)=\frac12\iint H(|x-y|)k(x)k(y)|u(x)-u(y)|^2dxdy
+\sum_{n\ge2}q_n\int k(x)k(x+\log n)|u(x+\log n)-u(x)|^2dx,
\tag{2}
\]
where
\[
H(t)=\frac{e^{-t/2}}{1-e^{-2t}},\qquad q_n=\frac{\Lambda(n)}{\sqrt n}.
\]
Initially the form is on compact smooth functions. All arguments respect parity; the RH interpretation below is in the even sector.

Write the original Weil form as Q=Q0+Qpole, with
\[
Q_0(f,f)=\langle f,A_\Gamma(D)f\rangle
-\sum_{n\ge2}q_n\langle f,(T_{\log n}+T_{-\log n})f\rangle,
\quad A_\Gamma(t)=\Re\psi(\tfrac14+\tfrac{it}2)-\log\pi.
\tag{3}
\]
The prime sum here is initially interpreted on compact tests. T_l is translation by l; the choice of sign in its definition does not affect the paired expression.

## 2. Exact conjugation: all pole ranks cancel

The unconditional radical identity Q(k,kv)=0 gives the signed-jump identity
\[
Q(ku,ku)=\mathcal E(u)-s\|u\|_\mu^2
+2\left|\int u\,d\mu\right|^2
-2\left|\int u\,d\nu\right|^2,
\quad d\nu=k(x)\sinh(x/2)dx.
\tag{4}
\]
But the last two terms are exactly Qpole(ku,ku). Consequently, for every compact smooth u, of either parity,
\[
\boxed{\ \mathcal E(u)=s\|u\|_\mu^2+Q_0(ku,ku).\ }
\tag{5}
\]

Define the unitary Uu=sqrt(m)u from L2(mu) to L2(dx), and
\[
a(x)=\sqrt{k(x)/c(x)}.
\tag{6}
\]
Then ku=aUu. The precise closed-form operator identity proved below is
\[
\boxed{\ UJU^{-1}=sI+A_0-K,\qquad
A_0=M_a\bigl(A_\Gamma(D)+6\bigr)M_a,\quad
K=6M_{a^2}+P_a,\ }
\tag{7}
\]
where A0 denotes the operator associated to the nonnegative sandwich form, not an unjustified product of unbounded operators, and
\[
P_a=\sum_{n\ge2}q_nM_a(T_{\log n}+T_{-\log n})M_a.
\tag{8}
\]
K is bounded self-adjoint and generally signed. Individual weighted shifts in (8) need not be compact on L2.

The scalar bound used here is explicit. From the digamma series,
\[
A_\Gamma(t)\ge A_\Gamma(0)
=-\gamma-\frac\pi2-3\log2-\log\pi>-6,
\tag{9}
\]
and A_Gamma(t)=log(2+|t|)+O(1). Thus A_Gamma+6 is strictly positive, with minimum approximately 0.6278.

## 3. Bounded weighted prime sum and exterior lower bound

For every fixed 0<gamma<pi/2 there is a finite C_gamma such that
\[
0<a(x)\le C_\gamma\exp(-\gamma e^{2|x|})\quad(x\in\mathbb R).
\tag{10}
\]
This follows directly from the leading theta term
`a(x) ~ sqrt(2) pi exp(2|x|) exp(-(pi/2)e^(2|x|))` and a larger constant on a compact interval. Define
\[
a_*:=\sup_x a(x),\quad a_R:=\sup_{|x|\ge R}a(x),\quad
b_n:=\sup_x a(x)a(x+\log n).
\]
Since `|x|+|x+log n|>=log n`, arithmetic-geometric means give
\[
e^{2|x|}+e^{2|x+\log n|}\ge2n,\qquad
b_n\le C_\gamma^2e^{-2\gamma n}.
\tag{11}
\]
Moreover `||M_a T_log n M_a||=b_n`. Hence (8) converges absolutely in operator norm, using only Lambda(n)<=log n, and
\[
\|P_a\|\le2\sum_{n\ge2}q_nb_n<\infty.
\tag{12}
\]

If v=Uu is supported in {|x|>=R}, (7), (9), and (12) give
\[
\boxed{\ \mathcal E(u)\ge(s-d_R)\|u\|_\mu^2,\qquad
d_R=6a_R^2+2\sum_{n\ge2}q_n\min\{a_R^2,b_n\}.\ }
\tag{13}
\]
One can replace the minimum in this bound by the sharper supremum of `a(x)a(x+log n)` subject to both endpoints lying outside [-R,R]. The stated version is convenient and explicit. Dominated convergence and (11) give d_R->0. Splitting the sum at n approximately e^(2R) gives, for fixed gamma as in (10),
\[
d_R=O_\gamma\bigl((1+R)e^R e^{-2\gamma e^{2R}}\bigr).
\tag{14}
\]
These are lower bounds for the **complete** gamma-plus-prime energy. The prime-only PNT error bound decays much more slowly; exact cancellation with the gamma diagonal makes the combined estimate stronger. This compares proved bounds, not claimed optimal errors for the prime diagonal itself.

The exterior lower edge is sharp without PNT as well. Let v_R be normalized even pairs of fixed smooth bumps translated beyond [-R,R]. Since a and a' tend superexponentially to zero and `A_Gamma(t)+6<=C(1+t²)`, one has `a0[v_R]<=C||a v_R||H1²->0`. The exterior weighted prime expectation also tends to zero by (13). Hence `E(U^-1 v_R)->s`. The infimum of the exterior Dirichlet Rayleigh quotient therefore tends exactly to s. These u_R are legitimate compact smooth tests even though division by sqrt(m) makes their unweighted amplitudes large.

There is no conflict with the known zero gap after truncating the positive prime-jump energy to finitely many primes. Deleting terms of (8) retains the full diagonal s supplied by annihilation. Deleting positive jumps in (2) also deletes their diagonal rates, and is a different operation.

## 4. Closure, the core, and local compactness

Let H_log have norm
\[
\|w\|_{H_{\log}}^2=\int(1+\log(2+|t|))|\widehat w(t)|^2dt.
\]
The form
\[
\mathfrak a_0[v]=\|(A_\Gamma(D)+6)^{1/2}(av)\|_2^2,
\quad
D(\mathfrak a_0)=\{v\in L^2:av\in H_{\log}\}
\tag{15}
\]
is densely defined and closed: multiplication by a is bounded and the square-root multiplier is closed. Its norm, after adding ||v||2^2, is equivalent to `||v||2^2+||av||H_log^2`.

Compact smooth functions are a form core. Here are the details needed because a tends to zero:

1. For v in (15), truncate v by smooth cutoffs chi_R(x)=chi(x/R). Then v_R->v in L2 and a v_R=chi_R av->av in H_log. A convenient proof uses the equivalent norm
   `||w||2^2 + integral_0^1 ||w(.+h)-w(.)||2^2 dh/h`.
   In the product difference, the term containing the difference of w converges by dominated convergence. The other is bounded by `C h^2 R^-2 ||w||2^2`, which is integrable against dh/h and tends to zero.
2. With v_R compactly supported, approximate w_R=av_R by compact smooth functions w_j in H_log using convolution. Keep their supports in one fixed larger compact interval. Then v_j=w_j/a is compact smooth, and v_j->v_R in L2 since a is bounded below there; also av_j=w_j->w_R in H_log.

The bounded perturbation K now makes the form of sI+A0-K closed on exactly (15). Its compact-core values equal the nonnegative jump form by (5); therefore it is the closure defining UJU^-1. In particular this also resolves the domain interpretation in (7). The closed jump form still equals its integral expression: its difference map into the L2 space of the jump measure is closed, as seen by almost-everywhere convergence in each marginal.

For every smooth compact chi,
\[
\chi(A_0+1)^{-1/2}:L^2\longrightarrow L^2
\quad\hbox{is compact}.\tag{16}
\]
Indeed a form-bounded sequence v_j has av_j bounded in H_log. Multiplication by chi/a is bounded on H_log (it is smooth and compactly supported), so chi v_j is H_log-bounded and has common compact support. Rellich compactness follows because the Fourier weight tends to infinity: high frequencies have uniformly small L2 mass, and the bounded-frequency spatially restricted operator is compact. This proves local compactness without assuming RH or global compact resolvent.

The perturbation K is relatively compact with respect to A0. First `M_a²` is approximable in operator norm by its compact spatial truncations. For P_a, if chi_R is one on [-R,R],
\[
\|P_a-\chi_RP_a\chi_R\|\longrightarrow0.
\tag{17}
\]
For every fixed prime shift its coefficient tends uniformly to zero when at least one endpoint escapes. Equation (11) supplies a summable dominating sequence, so the whole series converges in norm. Each truncated operator times `(A0+1)^(-1/2)` is compact by (16). It follows that `K(A0+1)^(-1/2)` is compact. This is relative compactness, not a claim that P_a itself is compact.

## 5. Essential edge and the exact remaining spectral question

Resolvent identities and the relative compactness just proved give
\[
\sigma_{\rm ess}(UJU^{-1})=s+\sigma_{\rm ess}(A_0)
\subset[s,\infty).
\tag{18}
\]
The existing exact even eigenfunctions
\[
u_j=\frac{k^{(2j)}}k-4^{-j},\qquad j=1,2,\ldots,
\tag{19}
\]
are independent, have zero mu-mean, and satisfy Ju_j=s u_j. Their finite-energy/core assertions are also immediate from (15): `a Uu_j=k^(2j)-4^-j k` is rapidly decaying and smooth. The polarized annihilation identity gives the operator equation. Thus s is an eigenvalue of infinite multiplicity in the even sector and
\[
\boxed{\ \inf\sigma_{\rm ess}(J^+)=s=\tfrac14.\ }
\tag{20}
\]
The same essential lower edge holds on the full space, since it contains this even eigenspace. No assertion here identifies the entire essential spectrum as a half-line.

Below s the spectrum is discrete, with finite multiplicities; for every delta>0 there are only finitely many eigenvalues at most s-delta. Since E is nonnegative, J>=0. Since the continuous gamma conductance is strictly positive almost everywhere, E(u)=0 forces u to be constant almost everywhere. Constants belong to the form domain, so zero is a simple eigenvalue. These facts even imply an unconditional **strictly positive but unspecified** spectral gap above constants; they do not give its sharp value s.

Let L2_0(mu)^+ denote the even mu-mean-zero space. Then the preceding weighted criterion becomes
\[
\boxed{\ \mathrm{RH}\iff
\sigma(J|_{L^2_0(\mu)^+})\cap(0,s)=\varnothing.\ }
\tag{21}
\]
Thus an RH counterexample must give a discrete subthreshold even eigenmode; conversely any such eigenmode gives a negative Weil test after form-core approximation. A smooth eigenfunction is not needed for this implication. The compact approximants converge in energy and variance, and a strict negative margin persists.

## 6. Exact IMS identity and quantitative localization

The usual uniform supremum of unweighted jump rates is unsuitable: long prime jumps from far tails into the center have total rate tending to s, not to zero. Use the conjugated off-diagonal coefficients instead.

Choose a real even cutoff eta_R, zero on [-R,R], one outside [-R-1,R+1], with 0<=eta_R<=1 and Lipschitz constant at most a fixed ell. For compact smooth u, direct polarization gives
\[
\mathcal E(\eta_Ru)-\Re\mathcal E(u,\eta_R^2u)
=\frac12\iint H(|x-y|)k(x)k(y)
\Re(u(x)\overline{u(y)})(\eta_R(x)-\eta_R(y))^2dxdy
\]
\[
\hspace{1cm}+\sum_{n\ge2}q_n\int k(x)k(x+\log n)
\Re(u(x)\overline{u(x+\log n)})
(\eta_R(x)-\eta_R(x+\log n))^2dx.
\tag{22}
\]
After U, this right side is `<v,B_R v>` for a bounded self-adjoint operator, with
\[
\boxed{\ \|B_R\|\le e_R:=
\frac{a_*a_R}{2}\int_{\mathbb R}H(|t|)\min\{1,\ell^2t^2\}\,dt
+\sum_{n\ge2}q_n\min\{a_*a_R,b_n\}.\ }
\tag{23}
\]
For the gamma part use Schur's test, quadratic vanishing at t=0, and the fact that a nonzero cutoff difference requires at least one endpoint outside [-R,R]. For each prime shift the same observation bounds the coefficient by both a_*a_R and b_n. The symmetrized weighted-shift operator has norm at most the stated single prime summand. Consequently
\[
e_R=O_\gamma\bigl((1+R)e^R e^{-\gamma e^{2R}}\bigr)\to0.
\tag{24}
\]
Multiplication by eta_R or eta_R² preserves the form domain, by the H_log product estimate in Section 4. Core approximation therefore extends (22) to that domain.

Suppose Ju=lambda u, ||u||mu=1, and lambda<=s-delta. The eigenfunction form identity in (22) and the exterior estimate (13) imply, whenever d_R<delta,
\[
\boxed{\ \|1_{\{|x|\ge R+1\}}u\|_\mu^2
\le\|\eta_Ru\|_\mu^2
\le\frac{e_R}{\delta-d_R}.\ }
\tag{25}
\]
This is an explicit uniform localization statement for all eigenmodes at a fixed depth delta. For instance d_R<=delta/2 gives tail mass at most 2e_R/delta. As delta tends to zero, the required central region can grow; no fixed region handles the entire unresolved threshold limit.

For a smooth real partition sum_i chi_i²=1, the full IMS formula is similarly
\[
\sum_i\mathcal E(\chi_i u)-\mathcal E(u)
=\frac12\iint J_{\rm jump}(dx,dy)
\Re(u(x)\overline{u(y)})\sum_i(\chi_i(x)-\chi_i(y))^2,
\tag{26}
\]
where the symmetric jump measure contains the continuous gamma part and both orientations of each prime shift. Equation (22) is the single-cutoff version needed for (25), and keeps every long jump.

## 7. Fixed-depth compact Birman--Schwinger problem

For 0<lambda<s let
\[
T_\lambda=(A_0+s-\lambda)^{-1/2}K(A_0+s-\lambda)^{-1/2}.
\tag{27}
\]
It is compact self-adjoint by Section 4. K need not be positive. Congruence of closed forms and min--max still give
\[
N(J^+<\lambda)=n(T_\lambda^+>1),
\tag{28}
\]
where the superscript means restriction to the even sector, N counts operator eigenvalues strictly below lambda, and n counts compact-operator eigenvalues strictly above one. The simple constant eigenfunction makes the left side at least one for every lambda>0. Therefore
\[
\mathrm{RH}\iff n(T_\lambda^+>1)=1
\quad\hbox{for every }0<\lambda<s.
\tag{29}
\]
At a fixed depth, compactness and (25) make controlled central-space approximations plausible theorem targets. A rigorous certification must include both spatial and frequency errors, not merely a finite matrix. Proving (29) only for lambda<=s-delta excludes deeper outliers but leaves a threshold layer. The infinite eigenspace at s and the degeneration of the inverse in (27) as lambda approaches s mean that a uniform endpoint argument remains a substantive missing ingredient.

## 8. Stop/go assessment

**Proved here from the stated exact-form inputs:** the closed conjugation (7), norm-summable weighted prime off-diagonal operator, a superexponential complete-form exterior lower bound, local compactness, essential lower edge exactly s, discrete subthreshold spectrum, quantitative localization away from s, and a compact signed Birman--Schwinger reduction at each fixed depth.

**Still open:** exclusion of all subthreshold even eigenvalues, uniform control as lambda approaches s, and a structural explanation forcing the optimal positive gap to be s. No statement above establishes RH, rules out shallow subthreshold modes, or identifies the full essential spectrum beyond its bottom.

The separate PNT-based [exterior note](CCM_PRIME_RETURN_AND_EXTERIOR_COERCIVITY_20260928.md) analyzes the prime diagonal itself and supplies an independent lower-bound argument. The present proof instead uses exact gamma-prime cancellation, so it should not be presented as a consequence of any finite-prime positive-jump approximation.
