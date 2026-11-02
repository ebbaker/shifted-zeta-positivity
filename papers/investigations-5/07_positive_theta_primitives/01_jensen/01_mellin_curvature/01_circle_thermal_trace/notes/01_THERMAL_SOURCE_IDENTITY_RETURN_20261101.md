# MC01-B01 return: filtered circle thermal states and the signed response obstruction

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Contributor `/root/mc01_thermal`, actual recorded **gpt-6-astra (Codex), ultra**, child `01a19a49-f8de-7770-a4ee-ec2acf3ace08`, own turn `01a19a49-f900-7ae0-8f31-61b472611c01`. The child's rollout records these settings; the inherited parent configuration agrees. This is a contributing same-model derivation, **pending separate checking**, not specialist review.

**Disposition: the bounded assessment is complete, with an exact physical observable dictionary and a scoped failure of thermal-positivity-only transfer. No quantitative improvement to the Mellin comparison is proved.** The complete source is a positive, temperature-dependent insertion in the circle heat trace on the required half-line. Its derivative determinants are expectations of explicit signed response polynomials in independent copies of that filtered thermal state. Thermal variance positivity does not sign that observable. The surviving fourth-response term is written explicitly below and retained through the complete Mellin curvature.

## 1. Contract, selection and frozen inputs

This executes [MC01-B01's r1 contract](../research-progress/01_CIRCLE_THERMAL_TRACE_RESEARCH_PROGRESS_20261101.md) under [Continuation05](../../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md). Two candidates were compared: (i) differentiated modular reflection, which supplies exact parity and endpoint constraints but no immediate inequality for separated temperatures; and (ii) the thermal cumulant relation after the complete source reconstruction. **Candidate (ii) is selected and worked once.** Reflection remains an exact boundary input, not a discarded condition.

The [launch record](../../numerics/PARALLEL_PHYSICAL_LAUNCH_RECORD_20261101.json) freezes HEAD and actual working-tree input hashes before the parallel wave. The [local execution record](../numerics/MC01_B01_THERMAL_IDENTITY_RECORD_20261101.json) gives hashes of this return, its exact checker and the read mathematical inputs, checked against that baseline. No sibling return was used. Inputs include the local overview/register, accepted Jensen Review01, the initial Mellin assessment, Notes03–05, parent overview, the theta differential-closure note and the common primary-source inspection record. The source polynomial recurrence itself is already part of Jensen's first-mode machinery; it is not claimed as new.

Read with the [result index](../../../../../../../result-summaries/README.md), particularly [physical-channel lessons](../../../../../../../result-summaries/06_physical_channels_wzw_ym_and_collar.md), [theta identities](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../../../../avoid/README.md), particularly [reformulations](../../../../../../../avoid/01_restating_the_target.md), [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [joint signed estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scoped failures](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 2. The exact physical state after source reconstruction

Keep physical heat time zero. On the circle of circumference \(2\pi\), let
\[
L=-\pi\partial_x^2,\qquad \beta=e^{4u},\quad X=\beta L,
\qquad P_0(x)=x(2x-3).
\]
The complete source is exactly
\[
\boxed{\Phi(u)=\frac{e^u}{2}\operatorname{Tr}\{P_0(\beta L)e^{-\beta L}\}
=e^u\sum_{n\ge1}P_0(\pi\beta n^2)e^{-\pi\beta n^2}.} \tag{1}
\]
The twofold degeneracy of nonzero circle modes accounts for the factor \(1/2\). The zero mode contributes zero. Expanding (1) gives precisely
\((2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}\), with no omission of a mode or term.

For \(u\ge0\), every nonzero \(x_n=\pi\beta n^2\) exceeds \(3/2\), so \(P_0(x_n)>0\). Hence
\[
\varrho_u=\frac{P_0(\beta L)e^{-\beta L}}
{\operatorname{Tr}(P_0(\beta L)e^{-\beta L})} \tag{2}
\]
is a positive trace-one operator. The unbounded polynomial insertion times the heat semigroup is trace class; (2) needs no bounded-operator claim for \(P_0\) itself. Equivalently use the probabilities
\[
\rho_u(n)=\frac{P_0(x_n)e^{-x_n}}{\sum_{m\ge1}P_0(x_m)e^{-x_m}},\quad n\ge1. \tag{3}
\]
This is a **filtered thermal state**, not the original Gibbs state and not a supersymmetric index. In particular the insertion varies with temperature; ignoring that variation would give the wrong susceptibility. Its positivity is asserted only for \(\beta\ge1\), which is exactly the source half-line used in the Mellin integral. No positive-filter assertion is made for all \(\beta>0\).

Full theta reflection gives
\[
p(-u)=p(u)+\sinh u,\qquad (\partial_u^2-1)\sinh u=0,
\]
so the complete \(\Phi\) is even. This uses the entire theta spectrum. In particular \(\Phi'(0)=0\), not the first mode's derivative. Reflection fixes origin identities in the following thermal expressions, but does not turn their separated-temperature determinants into positive quantities.

## 3. Exact thermal response polynomials and a three-copy observable

Define
\[
P_{m+1}(x)=4xP_m'(x)+(1-4x)P_m(x).
\tag{4}
\]
Termwise differentiation of the complete series gives
\[
\Phi^{(m)}(u)=e^u\sum_{n\ge1}P_m(x_n)e^{-x_n},\qquad
\frac{\Phi^{(m)}(u)}{\Phi(u)}=E_{\rho_u}\frac{P_m(X)}{P_0(X)}. \tag{5}
\]
The only even response polynomials needed at order three are
\[
\begin{aligned}
P_2(x)&=32x^4-224x^3+330x^2-75x,\\
P_4(x)&=512x^6-8448x^5+41408x^4-68096x^3+30930x^2-1875x.
\end{aligned} \tag{6}
\]
Let \(r=P_2/P_0\), \(z=P_4/P_0\), and distinguish the local temperature variable \(X\) from the source ratios
\[
R(u)=E_{\rho_u}r(X)=\Phi''/\Phi,
\qquad S(u)=E_{\rho_u}z(X)=\Phi^{(4)}/\Phi. \tag{7}
\]
For fixed ordered source points \(u_1<u_2<u_3\), take independent filtered circle states \(\rho_{u_j}\). Multilinearity of a determinant gives the exact identity
\[
\boxed{
\det\begin{bmatrix}1&1&1\\R(u_1)&R(u_2)&R(u_3)\\S(u_1)&S(u_2)&S(u_3)\end{bmatrix}
=E_{\rho_{u_1}\otimes\rho_{u_2}\otimes\rho_{u_3}}
\det\begin{bmatrix}1&1&1\\r(X_1)&r(X_2)&r(X_3)\\z(X_1)&z(X_2)&z(X_3)\end{bmatrix}.} \tag{8}
\]
Thus the unchanged signed insertion is the expectation on the right divided by \(V(R(\mathbf u))\). Positivity of the product density operator does not imply positivity of this signed diagonal observable. Ordering \(u_j\) also does not order \(X_j=\pi e^{4u_j}n_j^2\) for every occupation tuple; exchanging thermal and spectral ordering would be another unjustified step.

Equation (8), inserted into
\[
M_3(s)=\int_{\Omega_3}\prod_j u_j^{2s}\Phi(u_j)V(\mathbf u^2)
\det[1,R(u_j),S(u_j)]\,d\mathbf u, \tag{9}
\]
is an explicit three-copy circle-thermal representation of the complete observable. At integer \(k\ge0\), its coefficient consumer remains
\[
M_3(k)=(2k)!(2k+2)!(2k+4)!D_{3,k}.
\]
The general finite-order version of (8) uses rows \(P_{2i}/P_0\); it is an observable dictionary, not an all-order positivity argument or a new claimed RH equivalence. No noninteger Toeplitz integration by parts is used.

## 4. Where ordinary thermal positivity fails to transfer

Let \(\ell_j=\partial_u^j\log\Phi\), and write, for a single mode,
\[
a(u,n)=u+\log P_0(x_n)-x_n,
\quad q=\partial_u a=9-4x+\frac{12}{2x-3},
\quad b=4xq',\quad c=4xb',\quad d=4xc'. \tag{10}
\]
Primes on functions of \(x\) in (10) mean \(x\)-derivatives. In particular
\[
b(x)=-16x-\frac{96x}{(2x-3)^2}<0\qquad(x\ge\pi). \tag{11}
\]
Every individual source mode has negative logarithmic second derivative. But differentiation of the normalized state gives
\[
\partial_uE_{\rho_u}f=E_{\rho_u}(4Xf')+\operatorname{Cov}_{\rho_u}(f,q), \tag{12}
\]
and therefore the complete-source responses are
\[
\begin{aligned}
\ell_1&=Eq,\\
\ell_2&=Eb+\kappa_2(q),\\
\ell_3&=Ec+3\operatorname{Cov}(q,b)+\kappa_3(q),\\
\ell_4&=Ed+4\operatorname{Cov}(q,c)+3\operatorname{Var}(b)
+6\kappa(q,q,b)+\kappa_4(q).
\end{aligned} \tag{13}
\]
All expectations here are in the actual complete state (3). The notation \(\kappa(q,q,b)=E[(q-Eq)^2(b-Eb)]\); \(\kappa_4(q)=E[(q-Eq)^4]-3\operatorname{Var}(q)^2\). These formulas follow by repeated use of (12), or differentiation of the log partition function with its temperature-dependent insertion. They do not import a thermodynamic inequality. The positive thermal variance in \(\ell_2\) opposes (11), and the third and fourth cumulants and mixed terms have no sign supplied by positivity of the state.

A fixed exact witness makes the failed transfer concrete. Consider **only as an auxiliary comparison class** the single nonzero energy source
\(\phi_*(u)=e^uP_0(\pi e^{4u})e^{-\pi e^{4u}}\). It is positive on \(u\ge0\); its filtered state is a point mass, so all thermal fluctuations vanish. At \(x=4\), corresponding to \(u_*=(\log(4/\pi))/4>0\), exact rational differentiation of (6) yields
\[
r_x(4)=\frac{952}{25}>0,\qquad
\lim_{u_j\to u_*} \frac{\det[1,r(x_j),z(x_j)]}{V(r(\mathbf x))}
=\frac12\frac{d^2z}{dr^2}(4)
=\boxed{-\frac{157375}{99127}<0}. \tag{14}
\]
The confluence formula follows from divided differences, with the same \(1/2\) normalization as the inherited source construction. Since \(r_x(4)>0\), nearby distinct ordered source points retain a negative determinant ratio. Thus positivity of the filtered thermal state, even with zero variance and strictly log-concave individual source mode, cannot imply an everywhere nonnegative derivative-overlap observable. This refutes that specific positivity-only transfer.

**Scope is essential:** \(\phi_*\) lacks the complete theta spectrum and full reflection. It is not substituted for \(\Phi\), is not an approximation with an asserted error, and is not a counterexample to the actual signed integral's positivity or to the Mellin curvature bound. No integer Toeplitz endpoint identity is inferred for it. The known negative origin region of the complete theta \(h_3\), retained from the accepted baseline, independently makes an everywhere-positive observable unavailable for theta itself. Neither fact excludes a different integrated comparison.

The [exact checker](../numerics/mc01_b01_thermal_polynomial_check.py) verifies (6) and (14) with rational arithmetic, with no quadrature or source truncation. The local record states the finite exploratory rational points as well as the frozen \(x=4\) witness. They are checks of a derivation, not evidence for theta's global response.

## 5. Exact residual and its full Mellin consumer

The genuinely unpaid quantity can now be identified without replacing the signed insertion. From the elementary logarithmic derivative identities,
\[
R=\ell_2+\ell_1^2,\qquad
S=\ell_4+4\ell_1\ell_3+3\ell_2^2+6\ell_1^2\ell_2+\ell_1^4,
\]
put
\[
\boxed{U(u)=S-R^2
=\ell_4+4\ell_1\ell_3+2\ell_2^2+4\ell_1^2\ell_2
=R''+2\ell_1R'.} \tag{15}
\]
Equations (10)–(13) specify \(U\) completely in actual thermal cumulants. Using the accepted \(R'>0\), regard \(U\) as a function of \(y=R(u)\) and let
\(\chi(\mathbf u)=U[y_1,y_2,y_3]\) be its second divided difference. Then
\[
\boxed{h_3=1+\chi,\qquad A=1+E_s\chi.} \tag{16}
\]
This uses the exact divided difference of \(y^2\), which is one. It is a generic identity specialized here to an explicit thermal response, not a new sufficient estimate. For the Gaussian source \(e^{-a u^2}\), \(R=4a^2u^2-2a\) and \(U=-8aR-8a^2\) is affine in \(R\), so \(\chi=0\) and \(h_3=1\), checking normalization.

With the original positive carrier \(\mu_s\), \(T=2\sum_j\log u_j\), \(m=E_sT\), the complete curvature is exactly
\[
\mathcal C_3(s)=\operatorname{Var}_sT
+\frac{\operatorname{Cov}_s(\chi,(T-m)^2)}{1+E_s\chi}
-\left(\frac{\operatorname{Cov}_s(\chi,T)}{1+E_s\chi}\right)^2. \tag{17}
\]
The accepted signed-averaging result supplies \(1+E_s\chi>0\), not positivity of \(1+\chi\) pointwise. The unsupplied comparison, displayed only to specify the residual, is
\[
(1+E_s\chi)^2[\kappa_3(s)-\operatorname{Var}_sT]
-(1+E_s\chi)\operatorname{Cov}_s(\chi,(T-m)^2)
+\operatorname{Cov}_s(\chi,T)^2\ge0. \tag{18}
\]
Equation (18) is **an exact restatement of the desired bound**, not an advance toward it. No thermal variance inequality used here bounds its centered-square covariance, or its balance with the carrier variance. In particular (13) still contains actual third/fourth and mixed thermal cumulants, (15) takes a divided difference across three source points, and (17) subsequently averages over those points. A bound at one fixed temperature cannot be substituted for those joint operations. The circle state identifies a physical realization of this obligation; it does not pay it.

## 6. Domains, boundaries, tails and control screen

For every finite \(m\), (4) is a degree \(m+2\) polynomial, and the full source derivatives obey a bound of the form
\[
|\Phi^{(m)}(u)|\le C_m e^{(4m+9)u}e^{-\pi e^{4u}},\quad u\ge0.
\]
Indeed factor the first exponential and bound the remaining complete square sum by \(\sum n^{2m+4}e^{-\pi(n^2-1)}<\infty\). This justifies termwise derivatives and the needed fixed-log-power integrations; it is not a determinant-relative error estimate. At the origin the complete source and its derivatives are smooth and \(\Phi(0)>0\), and \(u^{2s}|\log u|^p\) is locally integrable for every fixed \(p\) and \(s\ge0\). The parameters \(\beta\), \(u\), Mellin tilt \(s\), and physical heat time remain distinct.

At collision faces, use the smooth undivided product
\(h_3w_s=(\prod u_j^{2s})V(\mathbf u^2)\det[\Phi^{(2i)}(u_j)]\).
No boundary sign is inferred by dropping a quotient singularity. Absolute integrability, full tails and compact-\(s\) domination justify (8), (9) and (17). These identities cover all \(s\ge0\). **The inequality (18) is unpaid on all of \([0,2]\), the rest of every compact range and unbounded \(s\).** No spatial-tail theorem is being promoted to a large-\(s\) theorem.

| Control or relaxation | Precisely established screen and remaining limit |
| --- | --- |
| Gaussian | Gives \(\chi=0\) and the known Gaussian equality normalization; it is not the unchanged square-spectrum circle source. |
| One-mode witness (14) | Passes positive filtered thermal state and single-mode log-concavity; fails full spectrum/reflection. It excludes only the positivity-only pointwise transfer, not (18) for theta. |
| Association-only two-point relaxation from the initial assessment | Fails the actual thermal/source realization; shows that normalized association information by itself cannot pay the integrated budget. No thermal-state counterexample is asserted. |
| Modified Euler-factor source | Has changed arithmetic reconstruction, not literal (1) with the unchanged circle spectrum. Its actual Mellin comparison is untested here. |
| Weighted-square and finite-prime square perturbations | The thermal-polynomial identities can survive after changing the spectral weights, but unchanged unit multiplicities and full normalized reflection fail in the cited controls. Therefore thermal positivity alone does not distinguish them. No new \(R'/K\) or curvature sign is assigned. |
| Reflected super-Gaussian and smooth shape/positive-primitive controls | Can retain smoothness/evenness and relevant decay but do not give literal (1) with the complete integer-square spectrum. Their value of (18) remains untested. |

No control is declared to fail an uncomputed quantitative bound. Positive-time collisions do not contradict a time-zero, fixed-order assertion. No new external theorem or source is imported; the thermal, derivative and determinant identities are derived here from the frozen canonical series.

## 7. Outcome and one next recommendation

The additional physical description is concrete: a free particle on a circle, an explicit positive temperature-dependent spectral insertion, and an explicit signed observable on three independent thermal copies. It retains all modes and normalizations. This is a physical reformulation of the source/finite-order determinant, with no claim of novelty in the literature, topological protection, a local interacting theory, or a new all-order RH criterion. The useful failure is also concrete: ordinary state positivity and variance positivity do not control the required derivative overlap, and (15)–(18) isolate the source-dependent non-Gaussian correction that remains.

**Next: [E] MC01-E01 — Sol**, separate checking of this frozen return: rederive (1), (4)–(8), (10)–(18); replay only the fixed rational checker; check the factor \(1/2\), Gaussian normalization, endpoint/full-spectrum qualifications, and the exact scope of the witness. Accept only these identities and the scoped failure, or record corrections without changing this return. No further thermal conceptual search or numerical campaign is issued. A future attempt to bound (18), if selected by the coordinator, is B work rather than an automatic continuation of this completed assessment.
