# Corrected propagation and a contour requirement for exterior force

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**. Rodgers–Tao chat0001, thread
`01a17a51-75b1-7bd1-86ef-6dc9485dced3`.

**Status:** bounded source audit RT-01 r1 completed; finite-cluster
identities and conditional transfer estimates proved below, with
same-model internal checks only. No canonical contour floor, new
Rodgers–Tao energy bound, collision exclusion, or Newman bound is proved.
This is an application requirement and a scoped diagnostic, not another
RH criterion. No priority claim is made for the elementary identities.

The [overview](../research-overview/01_RODGERS_TAO_RESEARCH_OVERVIEW_20261026.md)
and [initial note](01_INITIAL_RESULTS_AND_BOUND_REQUIREMENTS_20261026.md)
set the task. Read the [result index](../../../../../result-summaries/README.md),
especially [controls](../../../../../result-summaries/12_collision_controls_and_screening.md)
and [local geometry](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
and the [avoid index](../../../../../avoid/README.md), especially
[target classification](../../../../../avoid/01_restating_the_target.md),
[shared premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[coupled estimates](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
and [checked imports](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).
The [input record](02_PROPAGATION_INPUTS_20261026.json) identifies the
versions inspected; the [assessment](../reviews/01_PROPAGATION_AND_CONTOUR_TRANSFER_ASSESSMENT_20261026.md)
records the checking scope.

## 1. What the corrected argument actually consumes

Use the canonical convention `H_t=-H_zz`, `H(0,z)=xi((1+iz)/2)/8`.
Write **R** for the paper's large parameter T, **T** for a hypothetical
positive threshold, `L=log(X/(4pi))`, and `mathcal L=1+log X`.
The heat-coordinate mean spacing is asymptotic to `4pi/L`.

The source is [Rodgers–Tao arXiv v5](https://arxiv.org/abs/1801.05914v5),
3 July 2021, whose version record explicitly identifies corrected
Section 8 boundary accounting. Numbering below is the **PDF numbering**;
the experimental HTML renumbers the results. The archived 61-page PDF
was rehashed and selected passages read; pages 21, 39–40 and 56–59 were
also rendered for visual checks. This is not a full proof audit.

All energies in this source table count **ordered** pairs. For `j!=k`,
put `g_jk=x_k-x_j`, `d_jk=xi_k-xi_j`; their ratio is positive for real
ordered labels. The reference locations are determined by

\[
\Psi(u)=\frac{u}{4\pi}\log\frac{u}{4\pi}-\frac{u}{4\pi},
\qquad \Psi(\xi_j)=j\ (j>0),\qquad \xi_{-j}=-\xi_j.
\tag{1}
\]

They are not the Riemann xi function. Define

\[
V(r)=r^{-2}+2r-3,\quad
\widetilde E_{jk}=d_{jk}^{-2}V(g_{jk}/d_{jk})
=g_{jk}^{-2}-d_{jk}^{-2}+2(g_{jk}-d_{jk})d_{jk}^{-3},
\]
\[
E^I=\sum_{j\ne k\in I}g_{jk}^{-2},\qquad
\widetilde E^I=\sum_{j\ne k\in I}\widetilde E_{jk},\qquad
J_R=[.5R\log R,3R\log R]_{\mathbb Z^*}.
\tag{2}
\]

| PDF input and location | Hypotheses and normalization | Output and exact use |
| --- | --- | --- |
| (38), (42)–(45), pp.20–21 | Fixed classical locations (1) | `xi_j~4pi j/log j`; the derivative-consistent local gap formula is `4pi(k-j)/log(xi_j/(4pi))+O((k-j)^2/(j log^2 xi_j))` (source normalization caution in §8); global reference-gap comparison pays reference sums and removed strips. |
| Theorem 9 / Corollary 10, (48)–(52), pp.23–26 | Lemma 4 analytic estimates, all-real zeros for `Lambda<t<=0`, zero-free lower half-plane | `x_j=xi_j+O(log_+xi_j)` and mesoscopic rigidity (52). These count and locate zeros; they do not lower-bound every gap. |
| Theorem 11 / (56), p.27 | Real simple zeros above Lambda, differentiable labels, growth giving principal-value convergence | `x_k'=2 sum'_(j!=k)(x_k-x_j)^(-1)`. The prime is the symmetric index principal value. |
| Lemma 12(iii),(iv), pp.29–30 | Finite labeled K inside the full real-root flow | `(E^K)'<=B_K`, with B_K in (3); for adjacent zeros `(g^2)'<=8`. Internal dissipation is retained in the exact identity. |
| (62)–(63), Lemma 16, pp.39–40 | Reference gaps, (50), cancellation in the reference cubic sum | Nonnegative (2); `tilde E^I=E^I-sum_(j!=k in I)d_jk^(-2)+O(log_+^(O(1))(|I_-|+|I_+|))`. |
| Section 7 / Theorem 17, (65), pp.40–55 | Proposition 13 gap control, Proposition 15 weak integrated energy, mesoscopic rigidity, weighted Hamiltonian computation, and a fixed relaxation interval | `integral_(Lambda/4)^0 tilde E^(J_R) dt=o(R log^3 R)`. Its natural scale is `R log R` particles times `log^2 R` per particle. |
| Proposition 27, pp.55–56 | Average candidate endpoint locations; Fubini–Tonelli and Theorem 17 | Select I^0 containing `[.9R log R,2.1R log R]`, inside `[.8R log R,2.2R log R]`, with the integrated dyadic payment (4). |
| Proposition 28, pp.56–58 | `I` contains `[R log R,2R log R]`, lies in J_R; `Lambda/4<=t1<=t2<=0`; `t2-t1<=1/(100 log^2 R)`; selected I^0 | For `I'=[I_-+log^3 R,I_+-log^3 R]`, `tilde E^(I')(t2)<=tilde E^I(t1)+tilde O(1+D_I)`, `D_I=|I_--I_-^0|+|I_+-I_+^0|`. |
| Proposition 26, pp.55–57 | Good initial time from Theorem 17, then Proposition 28 on `O(log^2 R)` short steps | Total index shrinkage `O(log^5 R)` and polylogarithmic added error give `tilde E^([R log R,2R log R])(0)=o(R log^3 R)`. |

Here `tilde O` permits fixed powers of log R, and constants may depend
on the fixed negative Lambda. It is not an effective numeric allowance.

For the finite interval K selected in Proposition 28, the named consumer is

\[
B_K(t)=4\sum_{\substack{k,k'\in K\\k\ne k'}}\sum_{j\notin K}
\frac{1}{(x_k-x_{k'})^2(x_k-x_j)(x_{k'}-x_j)}.
\tag{3}
\]

This sum is absolutely convergent in its exterior index under the
source's growth hypotheses. Its immediate payment is not a pointwise
field error. With

\[
Q_{I^0}(t)=\sum_{\pm}\sum_{1\le2^n\le .1R\log R}
2^{-n}\widetilde E^{[I^0_\pm-2^n,I^0_\pm+2^n]}(t),
\qquad \int_{\Lambda/4}^{0}Q_{I^0}(t)\,dt=\widetilde O(1),
\tag{4}
\]

the reconstructed schematic boundary bound, retaining the local
notation and baseline repairs discussed in Section 8, is

\[
B_K(t)\le C(\log R)^C(1+D_I)
\{1+Q_{I^0}(t)+R^{-1}\widetilde E^{J_R}(t)\}.
\tag{5}
\]

The baseline 1 makes explicit a classical reference-energy payment; see
Section 8. Equations (4), Theorem 17, and a bounded integration interval
pay (5) by a polylogarithm. This is an additive propagation statement.

The geometry making it possible is specific. In each `log^3 R` endpoint
strip, (50) selects an exterior boundary gap at t2 of size at least
`1/log R`. Since `(g^2)'<=8`, throughout the short step

\[
g(t)^2\ge (\log R)^{-2}-8(t_2-t)
\ge .92(\log R)^{-2}.
\tag{6}
\]

Only the **two separating boundary gaps** receive this floor. Internal
small gaps are retained in the energy. The exterior sum is split at
`|x_k-x_k'|=1`: far pairs cost a polylogarithm, and near pairs cost (4)
and the global remainder in (5). Converting raw energy back to (2) pays
the ordered reference strip term

\[
2\sum_{\substack{j\in I\setminus I',\ k\in I\\j\ne k}}
d_{jk}^{-2}=\widetilde O(1).
\tag{7}
\]

Thus a replacement must pay the same energy, the time integral, the
boundary selection and losses (6)–(7). A finite-chart estimate below is
an interface to (3), not a replacement proof of all these steps.

## 2. Three uses of the negative-threshold hypothesis

1. **Real-root domain.** `Lambda<0` puts the working times strictly
   above Lambda. All zeros are real and simple, the real ODE is usable,
   and the lower half-plane is zero-free in the zero-count argument.
2. **Relaxation time and constants.** In Section 7, the weighted energy
   is `sum psi_R(j)psi_R(k) tilde E_jk`, with
   `psi_R(j)=(1+|j|/(R log R))^(-100)`. The nearby-pair Hamiltonian uses
   the relation `0<|j-k|<(R^2+|j|+|k|)^(.1)` and the logarithmic
   renormalization `log(1/|r|)+|r|-1`. Proposition 22 gives its derivative
   `-4 tilde E_R+o(R log^3 R+tilde E_R)`. Lemma 24 and Corollary 25
   dissipate large Hamiltonian values over the interval
   `[Lambda/2,Lambda/4]`, of fixed length `|Lambda|/4`. Earlier gap and
   integrated-energy constants also use time away from Lambda. This is
   not a bound uniform as the available relaxation time vanishes.
3. **Arithmetic endpoint.** Time zero is the actual zeta slice. Section 9
   converts Proposition 26 into density-one spacing
   `(4pi+o(1))/log R`, contradicting the positive proportion of smaller
   zeta gaps in the cited Conrey–Ghosh–Goldston–Gonek–Heath-Brown theorem
   (choose fixed `.77<lambda<1`). Montgomery's pair correlation is also
   discussed. These underlying papers were not independently reaudited.

For `T=Lambda>0`, real simple evolution is available at `t>T`, but an
analogue of each quantitative input must be proved on the new interval.
Constants obtained on `[T+sigma,b]` cannot be declared uniform as
`sigma` tends to zero. A later positive endpoint is not the zeta slice.
For `G(s,z)=H(a+s,z)`, that slice is `s=-a`, so time translation does
not restore the missing arithmetic endpoint. Forward regularization can
be useful without producing this contradiction.

There is also a distinct **domain mismatch**. The paper's Lemma 4
estimates H and H_z/H on curves `z=x-i kappa log_+ x` (quotient and
nonvanishing part for sufficiently large fixed kappa). Its saddle-point
calculation has a bounded negative-time version not intrinsically
requiring real zeros; its zero-count use does require them. Ansatz
Note26 supplies a positive-time **fixed transverse chart**, with only a
shrinking signed overlap into negative time. It is not a direct new
proof of Lemma 4 on the paper's growing imaginary curves or its fixed
negative interval.

## 3. Exact finite-block observable and common-motion cancellation

Fix a real interval of times `[u,v]` strictly in the simple-root regime
and a fixed finite set K of labels. In a simply connected spatial
neighborhood containing the whole block, factor

\[
H(t,z)=U_H(t,z)P_H(t,z),\quad
P_H=\prod_{i\in K}(z-a_i(t)),\quad D_H=2(U_H)_z/U_H.
\tag{8}
\]

There must be no other H zeros in this neighborhood. U_H is a
holomorphic zero-free unit. Differentiating the actual heat equation at
a simple root proves

\[
a_i'=f_i+D_H(a_i),\qquad
f_i=2\sum_{j\in K\setminus\{i\}}(a_i-a_j)^{-1}.
\tag{9}
\]

Let `g_ij=a_i-a_j` and `d_ij=xi_i-xi_j`, reversing both orientations
together relative to Section 1, and keep ordered pairs. Direct finite
algebra gives

\[
E_K'= -\mathcal Q_K+B_H,\qquad
E_K=\sum_{i\ne j}g_{ij}^{-2},\quad
\mathcal Q_K=\frac12\sum_{i\ne j}
\left(\frac{f_i-f_j}{g_{ij}}\right)^2\ge0,
\]
\[
B_H=-2\sum_{i\ne j}
\frac{D_H(a_i)-D_H(a_j)}{g_{ij}^3}.
\tag{10}
\]

For example, `E_K=(1/4)sum_i f_i^2`; the triple cross terms cancel.
Differentiating this along the internal motion proves the displayed
dissipation, or it follows by the finite expansion in Lemma 12(iii).
Where the full canonical zero ODE is justified, inserting
`D_H(z)=2 sum'_(j outside K)(z-x_j)^(-1)` at the block roots makes
B_H exactly (3). The contour definition below avoids evaluating or
truncating that infinite tail. It includes the entire exterior unit,
including any analytic canonical-product contribution.

For two drift fields with
`sup_J |(D_H-D_F)'|<=kappa` on a real interval J containing the block,
the real-segment integral gives

\[
|[D_H(a_i)-D_H(a_j)]-[D_F(a_i)-D_F(a_j)]|
\le\kappa |g_{ij}|,
\qquad |B_H-B_F[a]|\le2\kappa E_K.
\tag{11}
\]

Here `B_F[a]` is evaluated on the **same true roots**, not on model
roots. No root matching is hidden in (11). By comparison, independent
absolute drift errors at each root, each at most A0, pay
`4 A0 sum_(i!=j)|g_ij|^(-3)`. The coupled payment (11) instead uses
inverse squares; a common drift cancels identically. This is a genuine
improvement of the stated error payment at small gaps, not a canonical
numeric gain or a bound for the energy itself.

The corresponding renormalized exterior term cannot be silently
identified with (10). With fixed nonzero signed reference gaps d_ij,
its drift contribution is

\[
\widetilde B_D=2\sum_{i\ne j}
(D(a_i)-D(a_j))(d_{ij}^{-3}-g_{ij}^{-3}).
\]

Consequently its error on the same true roots is bounded by

\[
|\widetilde B_H-\widetilde B_F[a]|
\le2\kappa\sum_{i\ne j}|g_{ij}d_{ij}^{-3}-g_{ij}^{-2}|.
\tag{12}
\]

This is generally linear in a small spacing displacement, while
`tilde E` is quadratic there. A bound `O(kappa tilde E)` does not
follow. The selected consumer is the raw exterior term used inside
Proposition 28, with the separate conversion (7); no Book covariance or
pair-Laplacian identification is asserted. Moving labels, changing K,
or time-dependent weights add their own terms.

## 4. A contour estimate that does not require internal separation

Use one time-independent, positively oriented, simple piecewise smooth
contour Gamma, symmetric about the real axis, inside one paid analytic
chart. Let its length be p. For every t in `[u,v]`, the H zeros inside
Gamma are exactly those labeled K, counted with multiplicity, with no
other H zeros enclosed. Let J be one time-independent real interval
inside Gamma containing that entire H block for every t, with
`dist(J,Gamma)>=b>0`. Assume F is holomorphic on a neighborhood of the
closed interior, has the real symmetry, and on Gamma

\[
|F|\ge m>0,\quad |H-F|\le\delta_0<m,\quad
|(H-F)_z|\le\delta_1,\quad |F_z|\le M_1.
\tag{13}
\]

All these bounds may depend on t. Assume the functions have the mild
time continuity/measurability needed for these suprema and, for
(18)–(19), that A_F+kappa is integrable on `[u,v]`. Rouche gives equal
total zero counts, with
multiplicity, inside Gamma. It does not give simple roots or a matching
of individual zeros. The cluster's identification, count, and real
location still have to be established by the chosen application.

For z inside Gamma away from the roots, the residue theorem gives

\[
A_H(z):=\frac{1}{2\pi i}\oint_\Gamma
\frac{H_z(\zeta)/H(\zeta)}{\zeta-z}\,d\zeta
=\frac{(U_H)_z}{U_H}(z).
\tag{14}
\]

The residues at the roots subtract the logarithmic derivative of P_H.
Thus the right side extends holomorphically across every internal root,
even a multiple root. Define A_F analogously, using all its interior
zeros with multiplicity, and put `D_F=2 A_F`. F need not solve the heat
equation. In particular the nonzero actual residual of F_N is not
discarded: no root-motion or propagation equation for F is used.

On Gamma, division in (13) yields

\[
\left|\frac{H_z}{H}-\frac{F_z}{F}\right|
\le Q_1:=\frac{\delta_1+M_1\delta_0/m}{m-\delta_0}.
\]

Differentiate (14), retaining the length and distance losses:

\[
\sup_{z\in J}|(D_H-D_F)'(z)|
\le\kappa_{\rm jet}:=\frac{p}{\pi b^2}Q_1.
\tag{15}
\]

There is a scalar alternative. Since `|H/F-1|<=q:=delta0/m<1`
on Gamma, the principal logarithm
`h=log(H/F)=log(1+(H-F)/F)` is single valued on a thin collar of Gamma,
with `|h|<=nu:=-log(1-q)` on Gamma. Integration by parts around the closed
contour, followed by differentiation, gives

\[
D_H(z)-D_F(z)=\frac{1}{\pi i}\oint_\Gamma
\frac{h(\zeta)}{(\zeta-z)^2}\,d\zeta,
\qquad
\kappa_{\log}:=\frac{2p\nu}{\pi b^3}.
\tag{16}
\]

Both formulas are valid even if H and F have different interior root
locations and multiplicities. The logarithm is needed only on the
collar, not across their zeros. Use
`kappa=min(kappa_jet,kappa_log)` when both inputs are available.
No minimum **internal** gap enters this drift comparison. The separating
contour margin and its buffer remain essential.

## 5. Complete payment for one named term

Equations (11), (13), and (15)–(16) give the following precise B4/B5
requirement for B_K in (3), on a chosen finite chart:

\[
\boxed{\quad
\int_u^v 2\kappa(t) E_K(t)\,dt\le\mathcal A_{\rm err}.
\quad}
\tag{17}
\]

Together with an upper allowance for the **same-root** model term
`integral B_F[a]`, (17) pays the exterior contribution in the exact
balance (10). In an RT-sized application the sum of all such payments,
boundary selections, (7), and any contour quadrature/evaluation errors
must fit the additive allowance in Proposition 28, or a declared
improvement of it. No numerical quadrature is assumed exact here.

For a fully specified finite-block sufficient bound that avoids
unknown root values in B_F, define

\[
A_F(t)=\max\{0,\sup_{x\in J}[-D_F'(t,x)]\}.
\]

Real symmetry makes this real. The mean-value formula and (10) imply

\[
E_K'(t)\le2(A_F(t)+\kappa(t))E_K(t),\quad
E_K(t)\le E_1^+\exp\!\left(2\int_u^t(A_F+\kappa)\,dr\right),
\tag{18}
\]

where E1+ is any independently justified upper bound for E_K(u).
Substitution into (17) makes its sufficient condition explicit:

\[
2E_1^+\int_u^v\kappa(t)
\exp\!\left(2\int_u^t(A_F+\kappa)\,dr\right)dt
\le\mathcal A_{\rm err}.
\tag{19}
\]

All constants, time limits, contour floors, buffers, and the initial
energy now appear. Root enclosures at u can supply E1+: if
`|a_i-hat a_i|<=rho_i` and
`hat g_ij=|hat a_i-hat a_j|>r_ij:=rho_i+rho_j`, then

\[
E_1^+=\sum_{i\ne j}(\widehat g_{ij}-r_{ij})^{-2}.
\tag{20}
\]

A concrete independent acquisition test is available on a disk of
radius rho_i about a real simple model root hat a_i. If
`F(hat a_i)=0`, Taylor's theorem and a full-disk second-derivative bound
give one H root in that disk by Rouche whenever
`|F_z(hat a_i)| rho_i-(1/2) sup_disk|F_zz| rho_i^2 > sup_disk|H-F|`.
Compare H with the nonzero-slope linear polynomial on the disk boundary.
Disjoint disks centered on the real axis then give one real H root each
by conjugation symmetry. The enclosing-contour count must also show that
these disks exhaust K. This is a testable sufficient margin for initial
data, not an assertion that the canonical model passes it.

If an actual model energy is compared at an endpoint, its inverse-square
error is at most the **summed**, ordered allowance

\[
\sum_{i\ne j}
\frac{r_{ij}(2\widehat g_{ij}+r_{ij})}
{(\widehat g_{ij}-r_{ij})^2\widehat g_{ij}^{2}}.
\tag{21}
\]

The enclosures require independent root-count and localization margins;
(20)–(21) are not proofs that those margins exist. For (12), use its
displayed sum instead of E_K, with its own position allowances.

This is a complete conditional payment for a named term, not the full
RT comparison. In particular, (18) is multiplicative in raw E_K and
retains its reference baseline. On an RT-sized block,
`sum d_ij^(-2)` has order `R log^3 R`. A merely bounded growth factor
for raw energy cannot yield `tilde E=o(R log^3 R)`. One must either
retain the corrected weighted boundary cancellation or prove a better
matched estimate. This is the first specific loss if one tries to
replace Proposition 28 with a global Lipschitz/Gronwall argument.

## 6. Comparison with the current retained-arithmetic contract

[Ansatz Note26](../../../01_heat_density_asymptotics/ansatz/notes/26_RETAINED_ARITHMETIC_MOVING_POSITIVE_BAND_20261026.md)
and [Assessment20](../../../01_heat_density_asymptotics/ansatz/reviews/20_RETAINED_ARITHMETIC_MOVING_BAND_ASSESSMENT_20261026.md)
retain their status **proved in-note from named inputs; same-model
internal assessment only**. The same frozen-N field F_N, including its
explicit RS correction and all `2N=O(sqrt X)` modes, is reported on
`0<=t<=1` through the signed-window overlap. In fixed buffered charts,

\[
|\partial_z^j(H-F_N)|\le C_j E_o\mathcal L^j\eta_X,
\quad j\le3,\quad \eta_X=\mathcal L^2X^{-3/4}.
\tag{22}
\]

Direct time, actual residual, and residual_z allowances are also
available. The constants/onsets are finite and uninstantiated. Here
the theorem, finite model, domain, union and assessment were inspected;
no independent reproof of the approximation is claimed. Current
Note26/Assessment20 hashes agree with the initial input record.

For example let `E_Gamma=sup_Gamma E_o`. If a separate calculation gives
`m=mu E_Gamma` and `M1<=nu1 mathcal L E_Gamma`, (22) supplies
`delta0=C0 E_Gamma eta_X` and
`delta1=C1 E_Gamma mathcal L eta_X`. Then

\[
Q_1\le\mathcal L\eta_X
\frac{C_1+\nu_1 C_0/\mu}{\mu-C_0\eta_X},
\qquad \mu>C_0\eta_X.
\tag{23}
\]

There is no assumption that a positive envelope is a lower bound for
the oscillatory field: **mu is new data**. The ratio of the envelope
supremum to a contour minimum can be costly even on a fixed chart.

For a microscopic contour with
`p=p0/mathcal L`, `b=b0/mathcal L`, (15)–(16) become

\[
\kappa_{\rm jet}\le
\frac{p_0\mathcal L^2\eta_X}{\pi b_0^2}
\frac{C_1+\nu_1 C_0/\mu}{\mu-C_0\eta_X},\qquad
\kappa_{\log}\le
\frac{2p_0\mathcal L^2}{\pi b_0^3}
\left[-\log\left(1-\frac{C_0\eta_X}{\mu}\right)\right].
\tag{24}
\]

These shrinking contours are subsets of the already paid fixed chart;
the losses in (24) are proved explicitly. On
`Delta t=c/mathcal L^2`, the integrated relative error coefficient in
(11) is at most `2c sup(kappa/mathcal L^2)`. Thus at fixed p0,b0,mu,nu1
it is `O(eta_X)`. For a block spanning `M/mathcal L`, typically p0
grows like M; that factor is retained. Growing M, deteriorating mu,
or shrinking b0 require a new joint budget. The fixed-buffer source
constants have not been proved uniform in a growing chart.

For this selected positive finite-chart consumer, the **first unpaid
input is a usable contour margin and cluster identification**, then the
model exterior-curvature/payment and initial energy data. The high-height
field-domain gap is not reopened. Higher approximation orders are not
yet justified as the priority. No finite-height core, explicit numerical
onset, practical evaluator cost, RT-sized chart assembly, or global
positive-threshold coverage follows from (24).

## 7. Collision controls and the precise endpoint limitation

The elementary exact heat pair

\[
H_s(z)=z^2-2s,\qquad F_s(z)=z^2-2s-\varepsilon,
\quad s>0,\quad\varepsilon>0,
\tag{25}
\]

is a particularly informative local control. Both satisfy
`partial_s=-partial_zz`; their difference is the constant epsilon, so
all spatial derivative differences and both heat residuals vanish.
On `|z|=r`, with `r^2>2s+epsilon`, the contour minimum of F is at least
`r^2-2s-epsilon`. Choose fixed r, small fixed epsilon, and a sufficiently
short fixed s interval: (13) then holds uniformly through s=0.
Both polynomial units are 1, so D_H=D_F=0 and their actual exterior
transfer error is exactly zero.

Nevertheless the ordered energies are

\[
E_H(s)=\frac1{4s},\qquad
E_F(s)=\frac1{4s+2\varepsilon},\qquad
\frac{|E_H-E_F|}{E_H}=\frac{\varepsilon}{2s+\varepsilon}\longrightarrow1.
\tag{26}
\]

The unordered energies are half these. For this model, resolving
relative energy uniformly toward the event needs `epsilon=o(s)`;
outer contour isolation alone does not provide it. The H roots have
gap `sqrt(8s)`, and (10) gives
`E_H'=-1/(4s^2)=-4 E_H^2`, entirely from internal dissipation.
At the event, the strict direct first-jet exclusion also fails:
`|F(0,0)|=epsilon` is exactly its scalar error allowance, and `F_z=0`.

More generally an isolated finite heat collision has an analytic
zero-free unit in a fixed neighborhood. Its bounded exterior derivative
is therefore compatible with the already known Hermite splitting
`E_K(T+s)~constant/s`. Excellent exterior control does not exclude it.
An independent canonical estimate forcing `s E_K(T+s)->0` would still
be final-strength endpoint information; it has not been obtained here.

| Control family from the repository screen | Result of the present analytical screen |
| --- | --- |
| Polynomial/Hermite | Passes heat, real simple post-event roots, cluster contour isolation and bounded or zero unit drift. Equations (25)–(26) refute exclusion from these premises or from absolute field/jet accuracy plus that contour floor. It lacks theta arithmetic. |
| Positive kernels q and q_(T,a) | Canonical theta completion is absent. A local isolated event still has a regular unit; no contradiction to (11) or (15) is expected. The cited threshold examples remain separate from local-only events. |
| Euler-factor controls | Unchanged ordinary theta/Dirichlet coefficients fail. Their isolated local events do not fail the generic contour estimate; no theta-specific new inequality is asserted here. |
| Weighted-square / finite-tail controls | Full canonical reflection/completion fails. Their event constructions do not have a finite all-real heat threshold; they screen the local inference, not a finite-threshold theorem. |
| Reflected and smooth/positive-primitive controls | Full arithmetic data fail; the generic analytic-unit estimate remains compatible with their events. |
| Finite-prime / finite-profile controls | Full identities/profile growth or threshold eventual simplicity fail as recorded in the source controls. Finite-prime events are not asserted to give finite all-real thresholds. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet arithmetic fails; these screen the time-zero simplicity inference under RH, separately from the positive-threshold question. |

For each family the unchanged-theta identity is an absent possible
future premise, not a failed inequality proved in this note. The actual
failed proposed inference is that the shared local bounds force endpoint
nonconcentration. No certificates for these controls were rerun. This
does not exclude methods using new canonical arithmetic information.

## 8. Literal-source cautions preserved by this audit

These are targeted reading observations, not a retraction of the
published propagation theorem. The continuation must not quote the
intermediate displays without their payments.

- Equation (45) on PDF p.21 prints `log xi_j` in the leading reference
  gap. From the exact definition (1), `Psi'(u)=log(u/(4pi))/(4pi)`.
  Taylor inversion gives the shifted logarithm in this note's source
  table with the stated quadratic remainder. Using the printed
  `log xi_j` instead requires an additional
  `O(|k-j|/log^2 xi_j)` error. The printed denominator was visually
  checked. Leading asymptotics and the polylogarithmic estimates used
  here are unaffected by keeping this normalization payment.
- On PDF p.58 the final dyadic expression prints centers I_+/- where
  the preceding weight and Proposition 27 use I^0_+/-. Keeping the
  latter centers is the consistent integration route used in (4)–(5).
- That same near-pair estimate replaces raw E by tilde E without an
  explicit classical baseline. At `x=xi`, tilde E vanishes but the raw
  near-pair sum is positive. The elementary inequality
  `g^(-2)<=tilde E_jk+3 d^(-2)` pays an additional reference sum, of
  polylogarithmic size in this weighted estimate. That baseline is the
  1 in (5), and fits the final permitted `tilde O(1)`.
- Proposition 27's prose on p.55 says the dyadic cutoff is `10R log R`;
  its display and proof use `.1R log R`. This note uses the latter.
- Lemma 16's proof on p.40 prints a maximum of the distances to the two
  endpoints in the truncated odd cubic sum. At an endpoint a one-sided
  cubic sum is order one, so that maximum cannot be literal. The bound
  by `C/(1+min(j-I_-,I_+-j))^2`, plus the displayed long-range
  remainder, is summable and preserves the stated polylogarithmic
  conclusion. The maximum was visually checked in the PDF.

The note uses the named theorem conclusions with these local
notation/payment cautions exposed. It does not independently verify
every estimate in Sections 2–9 or the cited arithmetic papers.

## 9. Return and next question

RT-01 r1 has its requested dependency map, sign classification, named
term (3), complete conditional requirement (13)–(24), source-contract
comparison and analytical control. RT-02–04 advance at the conditional
interface level. The full corrected energy comparison RT-05 remains open.

**Next bounded request:** select one nonvacuous canonical positive-time
finite-chart family and acquire or certify the independent Gamma margin,
interior zero count/real location, and initial-energy data needed by
(13), (19), and (20). State the height/time interval, p0,b0,M and every
constant. Compare the resulting exterior payment with the matched
separate-drift baseline and with the dyadic term in (5). If the margin
cannot be acquired, record the specific cancellation or contour segment
that prevents it; do not request extra field orders without this test.
Any extension from a fixed family to `t downarrow T` must explicitly
confront (25)–(26) and identify new arithmetic input.

The practical parent return is **B3 first, then B4/B5**. The field
allowance can pay a microscopic exterior transfer at fixed margins;
the missing lower data and matched energy/boundary budget are now
specified. No numerical campaign or manuscript production is needed for
this bounded return.
