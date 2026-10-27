# Buffered transverse response with a complete resolution allowance

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.

**Status:** analytical theorem under the declared local data; no acquired
canonical growing-height constants or numerical certificate. This begins
TRD-01/02/05 in the [sole progress register][progress]. The fixed-window
leading coefficient is inherited; the quantitative remainder and explicit
uniform regulator allowance below are the deliverable of this note.

Read the [result index][results], [geometry cluster][geometry],
[control cluster][controls] and [avoid index][avoid]. Under
[target classification][classify] this is a quantitative diagnostic and
transfer estimate, not an exclusion criterion. The scope rules in
[avoid07][scope] and the coupled-accounting rule in [avoid12][coupled]
apply. Review is recorded separately in [Review01][review]; it is internal
same-model review, not independent specialist validation.

## 1. Declared window and local data

Let H be the unchanged canonical field, H_t=-H_zz. It is jointly
holomorphic in (t,z), by domination of its complete source integral by
Phi(u) exp(|t|u^2+|z|u) on compact sets. Fix a nonnegative
smooth compactly supported chi on C and put psi(z)=chi(z)(Im z)^2,
q=Delta psi, K=supp psi; in particular supp q is contained in K.
Define Y_chi(tau)=sum_{H(-tau,z)=0} chi(z)(Im z)^2, with multiplicity.
Work in a bounded conjugation-symmetric open
neighborhood Omega of K with a compact buffer. Assume every time-zero
zero in its closure is real, its boundary is zero-free, and enumerate the
finitely many sites a_j, of multiplicities m_j. This holds for a fixed
admissible window under either RH regime. All counts include multiplicity.

Choose disjoint disks D_j={|z-a_j|<R_j} compactly inside Omega. Choose a
time cap tau_0>0 so that for 0<=tau<=tau_0 each disk has exactly m_j
zeros, all in |z-a_j|<R_j/2, and no other zeros meet K. Specify the
zero-free collar as part of the data; an unbuffered zero count is
insufficient. Existence follows by compactness and Rouche. Effective
use requires actual wall and field-change bounds, not just this existence.

For example, on any compact zero-free remainder E, an initial normalized
floor b and a uniform bound V on |H_t/A| pay tau_0 V<=b/2. Here A is one
fixed nonzero constant. Canonical upper bounds can use
|A|^{-1} integral_0^infinity u^2 Phi(u) exp(Bu) du for negative real time on
|Im z|<=B. Floors and zero counts still need their own acquisition.

The local response constants below use H itself; the potential will use
f_tau=H(-tau,.)/A. Write c_j=H_z^{m_j}(0,a_j)/m_j! and
d_j=H_z^{m_j+1}(0,a_j)/(m_j+1)!, so c_j is nonzero and d_j/c_j is real.
The last assertion uses H(t,conjugate z)=conjugate H(t,z) for real t.

## 2. A root gate and a second-order response remainder

For m>=1 define

\[
 P_m(w)=e^{\partial_w^2}w^m
 =\sum_{\ell=0}^{\lfloor m/2\rfloor}
   \frac{m!}{\ell!(m-2\ell)!}w^{m-2\ell}.
 \tag{R1}
\]

Its simple roots are i h_k with h_k real, symmetric about zero, and
sum_k h_k^2=2m(m-1). These are the ordinary Hermite roots with the
normalization fixed by (R1); for m=2 they are +/-i sqrt(2).

At one site suppress j. The heat equation and the vanishing initial jets
give the holomorphic removable extension

\[
 G(r,w)=r^{-m}H(-r^2,a+rw)
 =cP_m(w)+rdP_{m+1}(w)+O(r^2).
 \tag{R2}
\]

Choose pairwise disjoint closed epsilon-disks about i h_k, invariant as
a collection under conjugation, all inside |w|<W. A completely declared
gate consists of rho>0, a bound B on |H(-r^2,a+rw)| for |r|<=rho,
|w|<=W, and

\[
 p_*=\min_k\min_{|w-ih_k|=\epsilon}|P_m(w)|>0,
 \quad 0<r_*\le\rho/2,
 \quad \frac{2Br_*}{\rho^{m+1}}<|c|p_*.
 \tag{R3}
\]

Cauchy's coefficient bound gives
|G-cP_m|<=B rho^{-m}|r|/(rho-|r|), hence (R3) supplies one simple
holomorphic root w_k(r) in each disk for |r|<=r_*. Reduce r_* if needed
so these m roots lie in D and the independent fixed-disk count excludes
additional roots. Such gates exist for each fixed event. A canonical
upper bound for B is integral Phi(u) exp(rho^2 u^2+rho W u) du; it does
not give a lower bound for |c| or the exterior walls.

The recurrence P_{m+1}=wP_m+2P'_m implies
w'_k(0)=-2d/c=:b, independent of k and real. Since
|w_k(r)-ih_k|<=epsilon, Cauchy gives, for |r|<=r_*/2,

\[
 z_k(-r^2)=a+irh_k+br^2+r^3 e_k(r),
 \qquad |e_k(r)|\le D:=2\epsilon/r_*^2.
 \tag{R4}
\]

Take r_max<=r_*/2 and r_max^2<=tau_0. Put
H_k=|h_k|+D r_max^2 and B_x=|b|+D r_max. Let C_0=||chi||_infinity,
L_x=||chi_x||_infinity and L_yy=||chi_yy||_infinity. Define

\[
 C_j=\sum_{k=1}^{m_j}\left\{
 C_0(2|h_k|D+D^2r_{\max}^2)
 +H_k^2\left(L_x B_x+\tfrac12L_{yy}H_k^2\right)\right\}.
 \tag{R5}
\]

Use the respective local data for every j and the smallest permitted
time cap. Then

\[
 \left|Y_\chi(\tau)
 -2\tau\sum_j\chi(a_j)m_j(m_j-1)\right|
 \le C_\chi\tau^2,\qquad C_\chi=\sum_j C_j.
 \tag{R6}
\]

Proof: conjugate roots have equal y^2, so chi can be replaced exactly
in their sum by chi_e(x,y)=[chi(x,y)+chi(x,-y)]/2. For this even part,
|chi_e(x,y)-chi(a,0)|<=L_x|x-a|+(L_yy/2)y^2. Equation (R4) gives
|x-a|<=B_x tau, |y|<=H_k sqrt(tau) and
|y^2-tau h_k^2|<=(2|h_k|D+D^2r_max^2)tau^2. Multiply, sum, and use
the root square sum in (R1). Simple clusters actually remain real by
uniqueness and conjugation and contribute zero exactly. This improves
the inherited unspecified o(tau) remainder on a fixed buffered window;
it is not an all-height or multiplicity-uniform constant.

The local Taylor/Hermite mechanism agrees with [Polymath Proposition3.1][poly].
The explicit root gate, common real drift and paired cutoff estimate above
are supplied here rather than imported as a stronger published remainder.

## 3. Uniform regulator bias, including coalescing clusters

Keep the fixed disks and time cap. Suppose |f_tau|>=b_j on the boundary of D_j
and |f_tau|>=b_0 on E_0=K minus the union of D_j, uniformly in time.
Set U_j=b_j/(2R_j)^{m_j}; the intentionally generous 2R_j pays every
root in the inner half-disk. Factor

\[
 f_\tau(z)=u_{j,\tau}(z)\prod_{k=1}^{m_j}(z-z_{jk}(\tau)),
 \qquad |u_{j,\tau}|\ge U_j\quad\hbox{on }\overline D_j.
 \tag{R7}
\]

The bound follows from the boundary floor and the minimum-modulus
principle for the zero-free unit. No separation among the split roots is
used. In particular it survives their coalescence at tau=0.

Let A_j=area(K intersection D_j) and A_0=area(E_0). Zero-area pieces
are omitted. For eta>0 put

\[
 I_j(\eta)=
 \begin{cases}
 \displaystyle \frac{m_j\pi^2}{\sin(\pi/m_j)}
       (\eta/U_j)^{2/m_j},&m_j>1,\\[4pt]
 \displaystyle B_j\{1+\log(1+A_j/B_j)\},\quad
       B_j=\pi(\eta/U_j)^2,&m_j=1.
 \end{cases}
 \tag{R8}
\]

Then the auxiliary potential in the overview satisfies

\[
 |Y_{\chi,\eta}(\tau)-Y_\chi(\tau)|
 \le {\cal B}_\chi(\eta)
 :=\frac{\|q\|_\infty}{4\pi}
 \left(\sum_j I_j(\eta)+A_0\eta^2/b_0^2\right).
 \tag{R9}
\]

Proof: if |f_tau|<s in D_j, one of the m_j factors in (R7) has modulus
less than (s/U_j)^{1/m_j}. The sublevel area is at most
m_j pi (s/U_j)^{2/m_j}, and also at most A_j after restriction to K.
Layer-cake integration of log(1+eta^2/|f_tau|^2) gives (R8): for m>1
use integral_0^infinity (exp(v)-1)^(-1/m) dv=pi/sin(pi/m); for m=1
integrate min(A_j,B_j/(exp(v)-1)). The latter integral equals
A_j log(1+B_j/A_j)+B_j log(1+A_j/B_j), bounded by (R8).
The zero-free piece uses log(1+s)<=s. Finally
Delta log|f_tau|^2=4pi sum multiplicity delta_zero, distributionally,
and the smooth compact test produces no omitted spatial boundary term.

For a fixed window of maximum cluster multiplicity M>=2 the bound is
O(eta^{2/M}); when all sites are simple it is O(eta^2 log(1/eta)).
These are sufficient upper allowances. Their sharpness for the weighted
moment is not asserted.

## 4. Complete field-to-response allowance

Let f_tilde be any field with ||f_tilde-f_tau||_{infinity,K}<=delta;
it need not be holomorphic for this weak-potential comparison. Define its
regulated moment by the same compact test. The real gradient of
v -> log(|v|^2+eta^2) has norm at most 1/eta. With
D_chi=||q||_1/(4pi), the full allowance is

\[
 \left|\widetilde Y_{\chi,\eta}(\tau)
 -2\tau\sum_j\chi(a_j)m_j(m_j-1)\right|
 \le C_\chi\tau^2+{\cal B}_\chi(\eta)
                       +D_\chi\delta/\eta.
 \tag{R10}
\]

For a Book estimate in an envelope norm, first multiply by its actual
envelope and divide by |A| to obtain this delta on K; an envelope-relative
allowance cannot be inserted as the normalized absolute delta directly.
This adds the actual source/evaluation error rather than assuming an
arbitrarily small regulator is free. A sufficient fixed-window choice is
eta=tau^{M/2+epsilon}, delta=o(tau eta), epsilon>0, with M>=1.
For M=1 the logarithm in (R8) is still paid. The moment then resolves its
linear coefficient. A preexisting fixed-resolution physical tuple does
not automatically supply this accuracy schedule or these auxiliary tests.

## 5. Growing windows and populations: exact outstanding obligations

For a family chi_X, repeat the complete construction with its own buffer,
sites, zero counts, analytic root gates, time cap tau_X, floors U_j,b_0,
norms ||q_X||_1, ||q_X||_infinity and remainder C_X. Write
N_X^chi=sum chi_X(a_j)m_j and M_X^chi=sum chi_X(a_j)m_j(m_j-1),
assuming N_X^chi>0. Equation (R10) implies

\[
 \left|\frac{\widetilde Y_{\chi_X,\eta}}{2\tau N_X^\chi}
             -\frac{M_X^\chi}{N_X^\chi}\right|
 \le\frac{C_X\tau}{2N_X^\chi}
 +\frac{{\cal B}_X(\eta)+D_X\delta/\eta}{2\tau N_X^\chi}.
 \tag{R11}
\]

Thus a growing-window limit follows if tau<=tau_X and all three terms
on the right tend to zero. This is a sufficient uniformity theorem in
declared local data; no canonical estimates for those growing data have
been acquired. Its first unprovided input is a time/height-uniform
combination of the root gates, walls and multiplicities, not a favorable
choice of eta alone.

If a weighted fraction p_X of zero labels belongs to multiple sites,
M_X^chi/N_X^chi>=p_X. For multiplicities <=M,
M_X^chi/N_X^chi<=(M-1)p_X. A fixed finite exceptional set contributes
O(1/N_X^chi) when N_X^chi grows and chi_X is uniformly bounded, while its
fixed local moment remains measurable. Without a multiplicity cap the
weighted statistic must be retained. These are algebraic population
consequences, not a bound on the canonical multiplicity fraction.

All cutoff derivatives in (R5),(R9),(R10) are paid; they encode the
spatial transition collar. No hard-window flux has been discarded. A
time-dependent family is evaluated pointwise here. Differentiating it
would add sum (partial_tau chi_X)(z_k)y_k^2 and the corresponding moving
test terms; (R10) does not prove that differentiated theorem.

The exact close-pair field z^2-a^2-2t has Y(tau)=4(tau-a^2/2)_+
on a cutoff equal to one near its roots. At zero its roots are simple,
but tau>>a^2 resolves the pair like a double event. Its uniform
simple-cluster time cap must therefore shrink on the a^2 scale. This
calibrates the missing small-gap control; it has a negative Newman
threshold and is not a canonical realization of regime C.

## 6. Conditional atlas and control screen

| Regime and region | Joint observation data | Output and limit |
| --- | --- | --- |
| A, t=-tau near zero, compact window seeing an off-axis zero | Fixed buffer and normalization; eta->0 and delta/eta->0 | Unregulated moment has a positive limit; (R9) applies to complex clusters too, but (R6)'s real-endpoint premise does not |
| A, t=T-tau at its finite real event | Same local gates at T; width O(sqrt(tau)); eta=tau^{M/2+epsilon} | (R6)-(R10) with source e^{Tu^2}Phi; no unchanged-source time shift and no exclusion of T |
| B, t=-tau, fixed window | Fixed height/transverse width/cutoff; tau<=local gates; resolution schedule in Section4 | Quantitative weighted multiplicity response, O(tau^2) plus explicit bias and transfer |
| C, t=-tau, fixed window | Same fixed data, all clusters simple | Unregulated Y eventually exactly zero; (R9)-(R10) bound the auxiliary regulated signal |
| B or C, growing height X | All window data in Section5; record both tau log X and tau(log X)^2 | (R11) under the displayed uniformity conditions; no source-derived X(tau) acquired |
| C, compact escape | A buffered disk of radius R, with the simple-root and no-entry gates | Those gates yield a conditional time interval with R_*(tau)>=R; no rate or monotonicity follows |
| Fixed positive time / remote times | Book domains, envelopes, fixed transverse strips and their own regulators | Inherited matching inputs; no claim that a common leading field profile distinguishes the regimes |

This is a first local/resolution atlas. A quantitative match over all
remote-time and high-height overlap domains remains TRD-01 work.

| Existing control | Result of the screen and missing premise for a canonical conclusion |
| --- | --- |
| Hermite and close-pair heat polynomials | Pass the local theorem and exhibit its resolution cost; lack complete theta arithmetic/global zero statistics |
| Positive atomic and theta-close multiple endpoints | The local theorem permits their multiple sites; preservation lists differ, and unchanged ordinary theta arithmetic fails |
| Euler-factor controls | Local estimate still holds wherever its real-window premise holds; coefficients/completion differ, and an all-real slice cannot be assumed for every parameter |
| Weighted-square and finite-tail controls | Can pass a local finite-window version, but lack the global all-real interval for an RH population interpretation |
| Reflected/shape/primitive/finite-prime/finite-profile controls | Shared local estimates do not reject their events; they lack the complete normalized theta source, with additional missing premises varying by family |
| All-multiple coarse-count control | Can pass these diagnostic laws and coarse counts; neither (R10) nor coarse walls supplies the missing multiplicity-sensitive canonical upper bound |

This analytical screen reuses the established control records, with no
new control computation. The estimates intentionally hold for colliding
controls. An independent theta estimate contradicting the response has
not been supplied. TRD-06's actual U/R/J/Q system is untouched; no closure
for its signed covariance or means has been introduced.

## 7. Bounded continuation

**26 October continuation:** [Note03](03_CANONICAL_FIXED_STRIP_ALLOWANCE_FAILURE_20261026.md) completes the negative
alternative below for an explicit fixed-transverse-width family. Its
regulator-optimized R11 allowance fails with a declared polynomial raw
field-error budget, and the separate global source-majorant time gate
fails when height grows faster than log(1/tau). These are scoped failures
of the specified bounds, not actual-error or zero-dynamics lower bounds.
The next bounded question is the localized replacement stated there;
individual-site canonical gates remain unacquired.

Acquire one genuinely height-uniform canonical family of zero counts,
wall floors and local analytic gates, or prove that a proposed explicit
family fails a stated (R11) payment. Prioritize the gate tau<=tau_X and
the field normalization/floor costs before selecting a numerical survey.
The separate [Dobner budget][budget] pursues a constructed witness upper
bound and does not provide this growing-window lower exclusion.

[progress]: ../research-progress/01_THREE_REGIME_DYNAMICS_RESEARCH_PROGRESS_20261026.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[classify]: ../../../../avoid/01_restating_the_target.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[coupled]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[review]: ../reviews/01_OPENING_RESPONSE_AND_BUDGET_REVIEW_20261026.md
[budget]: 02_DOBNER_COMPLETE_CONDITIONAL_BUDGET_20261026.md
[poly]: https://arxiv.org/html/1904.12438v2#S3
