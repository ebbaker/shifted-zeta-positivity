# Curvature cones, sharp candidate-null payments, and localized Poisson transforms

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Proofs and parallel cross-audits are
internal LLM work, not independent mathematical validation.

This executes the first analytical steps of
[the program in Heat Note 23](23_SIGNED_CANDIDATE_LOCALIZATION_AND_RESONANT_BOUNDARY_PROGRAM_20261010.md).
It uses the complete physical dictionary and imported holomorphic disk of
[the microlocal manuscript](../13_microlocal_phase_space/microlocal_coherent_currents_and_zero_atlases.tex),
the diagonal-annihilating kernel of
[project 09 Note 7](../09_prime_phase_torus/notes/7_DIAGONAL_ANNIHILATING_PAID_KERNELS_AND_NEAR_PAIR_BOUNDS_20261010.md),
and the exact finite Poisson formula of
[project 09 Note 9](../09_prime_phase_torus/notes/9_COUPLED_MOBIUS_PRIMITIVE_FRONTIER_AND_RESONANT_SUBLATTICES_20261010.md).
The retained signed main inequality remains open.

## 1. Exact localization of ordinary threshold candidates

At a real physical center write
\[
M_j=\sum_{n\le N}q_n(\log n-\mu)^j=X_j+iY_j,
\qquad \mathcal K=2Y_3^2+3X_2X_4-\Gamma X_2^2.
\]
The coefficient is the density-strengthened
\(\Gamma=\gamma_{\rm count}/c^2\). Its imported counting constant
remains symbolic. Let \(P_{\rm err}\ge0\) be an admissible total
physical threshold payment. The ordinary-double, all-real threshold
implication requires \(\mathcal K+P_{\rm err}\ge0\), in the
range of its imported counting theorem. This section additionally assumes
\(\Gamma>0\).

Completing the square gives the exact identity
\[
\mathcal K+P_{\rm err}
=2Y_3^2+P_{\rm err}+\frac{9X_4^2}{4\Gamma}
 -\Gamma\left(X_2-\frac{3X_4}{2\Gamma}\right)^2.
\tag{1}
\]
Consequently every surviving candidate satisfies
\[
r_-\le X_2\le r_+,\qquad
r_\pm=\frac{3X_4\pm
 \sqrt{9X_4^2+4\Gamma(2Y_3^2+P_{\rm err})}}{2\Gamma}.
\tag{2}
\]
The roots bracket zero. Equivalently its signed curvature lies in a band
centered at \(3X_4/(2\Gamma)\), with half-width
\[
\sqrt{\frac{2Y_3^2+P_{\rm err}}\Gamma
                +\frac{9X_4^2}{4\Gamma^2}}.
\tag{3}
\]
This retains the orientation of \(X_4\), unlike an absolute envelope.
At \(X_2=0\), the expression is \(2Y_3^2+P_{\rm err}\ge0\),
so this test cannot exclude that locus by itself.

Equations (1)–(3) are pointwise identities. A measured payment can itself
depend on \(X_2\); in that case (2) is an implicit pointwise test, not
a fixed global interval in the free variable \(X_2\).
For a uniform cell statement first choose constants
\[
\Gamma\ge G>0,\quad |Y_3|\le B_3,\quad |X_4|\le B_4,
\quad P_{\rm err}\le P_{\rm up}.
\]
Then a necessary cell-level bound is
\[
|X_2|\le R_G:=
\frac{3B_4+\sqrt{9B_4^2+4G(2B_3^2+P_{\rm up})}}{2G}.
\tag{4}
\]
Indeed \(\mathcal K+P_{\rm err}
\le 2B_3^2+3|X_2|B_4+P_{\rm up}-G|X_2|^2\),
which is strictly negative beyond its positive root. A certified lower
bound \(|X_2|>R_G\) therefore excludes this ordinary threshold candidate
on the whole cell. This corollary needs all moment and payment enclosures,
and a justified positive coefficient bound. Eventual asymptotic positivity
of \(\Gamma\) is insufficient for a finite numerical use of (4).

On the closed shrinking sector \(1\le\kappa\le3/2\), the imported
complete moment bounds give \(|Y_3|,|X_4|=O(Nw_N)\), while
\(\Gamma\asymp L\) for the fixed imported counting constant. Equations
(3)–(4) imply
\[
|X_2|=O\left(\frac{Nw_N}{\sqrt L}
                  +\sqrt{\frac{P_{\rm err}}L}\right).
\tag{5}
\]
The signed band center is only \(O(Nw_N/L)\). These are necessary
localizations, not a sign for the remaining small-curvature region.
Higher multiplicity is not covered by the ordinary-double premise.

## 2. Sharp support payment for the degree-six extension

Use real physical \(c>0\), \(L>0\), \(\eta>0\),
\(\epsilon=d/c\), and \(A_c=-d\mu\). The full-sum candidate
coordinates are
\[
X_0=F/2,\qquad e_1=F'/2=A_cX_0-cZ_1,
\quad Z_1=Y_1+\epsilon X_1.
\]
The complete holomorphic disk, with its real symmetry, implies at a genuine
joint zero
\[
s^2+|r|\le1,\qquad
s=2X_0/\eta,\quad r=2e_1/(L\eta).
\tag{6}
\]
This is Schwarz–Pick for \((Q-F)(x+\zeta/L)/\eta\).

Retain the exact finite-moment kernel
\[
\mathcal J^\dagger=\mathcal K+
 X_0(\Gamma X_4-3X_6+2\epsilon Y_6)-2Z_1Y_5.
\]
Set
\[
H=3X_6-\Gamma X_4-2\epsilon Y_6,\qquad
R=H+\frac{2A_c}{c}Y_5,\qquad
D=\frac{2L}{c}|Y_5|,\quad B=|R|.
\]
Substitution of the physical derivative coordinate gives the exact identity
\[
\mathcal K-\mathcal J^\dagger
=RX_0-\frac{2Y_5}{c}e_1.
\tag{7}
\]
Define, for nonnegative arguments,
\[
h(D,B)=
\begin{cases}
D+B^2/(4D),&D>0,\ B\le2D,\\
B,&D=0\text{ or }B\ge2D.
\end{cases}
\]
Then every genuine joint-zero candidate satisfies
\[
\boxed{\quad
|\mathcal K-\mathcal J^\dagger|
 \le\Pi^\dagger_{\rm curved}:=\frac\eta2 h(D,B).
\quad}
\tag{8}
\]
No positivity assumption on \(\Gamma\) is needed here.

For a proof, divide (7) by \(\eta/2\), use (6), and align the
signs of the two real coordinates. The maximal absolute linear functional
on that body is
\[
\max_{0\le y\le1}\{D(1-y^2)+By\}=h(D,B).
\]
For \(D>0\) its maximizing value is
\(y=\min\{B/(2D),1\}\); for \(D=0\), take \(y=1\).
This proves (8), including the degenerate branches. It is sharp support
for frozen finite features on the necessary body. Every real first jet
in the body can be realized by a real disk map
\((s+\lambda\zeta)/(1+s\lambda\zeta)\),
\(\lambda=r/(1-s^2)\), when \(|s|<1\), with constant maps at
\(|s|=1\). This does not assert arithmetic-state realizability or
simultaneous saturation of independent higher-jet error payments.

The fifth and sixth moments here are finite logarithmic features. No
approximation to genuine fifth or sixth derivatives has been introduced.
For certified use, \(h\) is continuous, homogeneous, and nondecreasing
in each nonnegative argument. Outward upper endpoints give the safe bound
\(\eta_{\rm up}h(D_{\rm up},B_{\rm up})/2\), with its branch and
division evaluated outward.

## 3. Exact size of the support improvement

The previous payments are
\[
\Pi^\dagger_{\rm slab}=\frac\eta2(D+B),\qquad
\Pi^\dagger_{\rm box}=
\frac\eta2\left\{|H|+D+\frac{|A_c|}{L}D\right\}.
\]
They satisfy
\[
\Pi^\dagger_{\rm curved}\le\Pi^\dagger_{\rm slab}
\le\Pi^\dagger_{\rm box}
\le\left(1+\frac{2|A_c|}{L}\right)\Pi^\dagger_{\rm slab}.
\tag{9}
\]
The triangle inequality gives the middle comparison. Its reverse form
\(|H|\le B+|A_c|D/L\) gives the final comparison.

Let \(\varphi=(1+\sqrt5)/2\). The sharp global comparison is
\[
\varphi^{-1}(D+B)\le h(D,B)\le D+B.
\tag{10}
\]
For \(D>0\), set \(z=B/D\). On \([0,2]\) the ratio is
\((1+z^2/4)/(1+z)\); its derivative changes sign at
\(z=\sqrt5-1\), where the ratio is \(\varphi^{-1}\).
On \([2,\infty)\), the ratio is \(z/(1+z)\ge2/3\).
The degenerate \(D=0\) case is direct. Thus the maximum relative
reduction of the slab payment is \((3-\sqrt5)/2\), about 38.2%.
Since the actual drift obeys \(A_c=O(x^{-1})\), this refinement changes
neither the power nor the exponential scale of the box or slab payment.
It may recover a finite margin, but supplies no opposite signed main term.

The density contribution in the complete extended kernel is itself exactly
\[
\Gamma(X_0X_4-X_2^2).
\tag{11}
\]
On exact complete candidates it is \(-\Gamma X_2^2\); its departure
on paid candidates is at most \(|\Gamma|\eta|X_4|/2\). This sign
belongs to the complete sum. Imposing \(X_0=0\) on each block or
sublattice would introduce an unjustified extra constraint. Localization
(5) identifies the region where this helpful term can degenerate.

## 4. Sublattice saddles share a rational frequency grid

For the exact sublattice integrals of project 09 Note 9, define
\[
J_f[A,B]=\int_A^B w(n)v(\log n-\mu)
 e^{i\{\theta_t+T\log n-2\pi f n\}}\,dn.
\]
The substitution \(n=qu\) gives, exactly,
\[
I_{q,k}[a,b]=\frac1q J_{k/q}[qa,qb].
\tag{12}
\]
The leading stationary coefficient satisfies the corresponding exact
algebraic relation
\[
B_{q,j}(k)=\frac1q B_{1,j}(k/q),\qquad k>0,
\tag{13}
\]
where the \(q=1\) coefficient is extended to positive real dual
frequency. Its saddle in the original variable is \(n=qP/k\),
\(P=T/(2\pi)\). Its amplitude is
\(\sqrt P\,w(qP/k)/k\), and its phase is
\(\theta_t+T\log(qP/k)-T-\pi/4\), proving (13).

In particular \(k=q\ell\) samples the same carried datum as the
integer dual frequency \(\ell\), scaled by \(1/q\).
Other modes sample rational frequencies. This is a useful way to retain
the coupling of the reflected weights, centers and carriers: they are
prescribed functions on related frequency grids, not independently
adjustable phases. Endpoints \(qa,qb\) still depend on the literal
sublattice and its floors. Equations (12)–(13) do not equate their finite
ranges, assert a stationary approximation, or give the signed Möbius sum
its needed sign.

## 5. A local Fourier ceiling for macroscopic blocks

The global Fourier ceiling \(M\ge4P\) in project 09 Note 9 protects
intervals starting at \(1/2\). For a particular literal half-integer
interval \([a,b]\), \(a>0\), it is enough to choose an integer
\[
M\ge1,\qquad M\ge2P/a.
\tag{14}
\]
Keep exactly the same resonant integrals and endpoint-tail functions from
that note. At every endpoint \(z\ge a\),
\(\omega=P/z\le M/2\), so their denominators have no pole.
For every \(|k|>M\) and \(u\in[a,b]\),
\[
|g_k|\ge\pi|k|,\quad
|g_k'|\le\pi|k|/u,\quad
|g_k''|\le2\pi|k|/u^2,
\qquad g_k=T/u-2\pi k.
\tag{15}
\]
Indeed \(T/u=2\pi P/u\le\pi M<\pi|k|\); positive modes
are separated by subtraction and negative modes by addition.
Two integrations by parts and summation of \(k^{-2}\) therefore give
\[
\left\|\sum_{u=p}^r z_{qu}-\widetilde V_q[a,b]\right\|
\le\frac{2}{\pi^2M}
\int_a^b\left(\|a_q''\|+
 \frac{3\|a_q'\|}{u}+\frac{5\|a_q\|}{u^2}\right)du,
\tag{16}
\]
where \(a=p-1/2,b=r+1/2\), and \(\widetilde V_q\) retains
the complete finite integral sum and both exact endpoint terms. This is
the same finite Poisson proof, with its separation condition localized.

For the \(q=1\) block \(\lfloor N/2\rfloor<n\le N\),
\(a=\lfloor N/2\rfloor+1/2\) and \(b=N+1/2\).
Taking \(M=\lceil2P/a\rceil\) gives \(M\asymp N\), instead
of \(M\asymp N^2\). On this macroscopic range, fixed-degree feature
polynomials and the physical amplitude satisfy
\[
\|a_1^{(j)}\|\le C_D A_v w_N N^{-j},\quad j=0,1,2.
\]
Thus the right side of (16) is \(O_D(A_vw_N/N^2)\).
If the complement is kept exact, the perturbation of the full quadratic
by this block replacement is at most
\[
\|Q\|(2\|Y\|\,\delta+\delta^2)
=O_D(\|Q\|A_v^2w_N^2/N),
\tag{17}
\]
using \(\|Y\|=O_D(A_vNw_N)\),
\(\delta=O_D(A_vw_N/N^2)\), and real-part contraction.
Every block/complement cross term is accounted for by this full-vector
perturbation. Quadrature or any further stationary approximation needs
its own error bound. Equations (14)–(17) make a faithful macroscopic
stationary/endpoint diagnostic feasible without deleting endpoints or
changing the original integer cutoff.

## 6. An endpoint bundle bound for the coupled frontier

This section gives an upper envelope for outer-cutoff transitions. It does
not compute their signs or give a lower bound for their size. Recombine the
complete block and complement first, so their artificial shared boundary
cancels when the two vectors use the same global ceiling \(M\ge4P\).
Different localized ceilings require their respective endpoint terms and
residuals to be recombined instead. Write \(b_q=\lfloor N/q\rfloor+1/2\), \(1\le q\le N\),
and fix a transition-width parameter \(R_0>0\). Select the exact modes
\[
\mathcal T_q(R_0)=\{k\in\mathbb Z_{>0}:
 |P/k-b_q|\le R_0b_q/\sqrt T\},\qquad
E_q=\sum_{k\in\mathcal T_q}I_{q,k}[1/2,b_q].
\tag{18}
\]
Uniformly in the closed shrinking sector, for sufficiently small time,
\[
\#\mathcal T_q=O_{R_0}(q),\quad
\|I_{q,k}[1/2,b_q]\|=O_{R_0,D}(A_vw_N/q),\quad
\|E_q\|=O_{R_0,D}(A_vw_N).
\tag{19}
\]
These are bounds on exact oscillatory integrals, not their Gaussian leading
coefficients.

Here is a proof with the uniformity in \(q\) retained. The literal
endpoint obeys \(N/2\le qb_q\le3N/2\). Put
\(r=R_0/\sqrt T\le1/4\). The selected modes lie in
\[
\frac{P}{b_q(1+r)}\le k\le\frac{P}{b_q(1-r)}.
\]
The length of this interval is \(O_{R_0}(\sqrt T/b_q)=O_{R_0}(q)\);
including one possible extra integer preserves that bound. Its modes
also lie inside the full ceiling \(\lceil4P\rceil\).

On \([b_q/2,b_q]\), original indices lie in \([N/4,3N/2]\).
The amplitude has supremum and total variation
\(O_D(A_vw_N)\), while the phase's second derivative has magnitude
at least \(T/b_q^2\asymp q^2\). Splitting at a derivative threshold
\(\sqrt T/b_q\) and integrating by parts on either remaining monotone
piece bounds its integral by \(O_D(A_vw_Nb_q/\sqrt T)\), which is
\(O_D(A_vw_N/q)\).

On \([1/2,b_q/2]\), the phase derivative is positive and at least
\(T/(3u)\). One integration by parts gives an upper bound by a constant
times
\[
\frac1T\left[u\|a_q(u)\|\big|_{\rm endpoints}
       +\int_{1/2}^{b_q/2}(u\|a_q'(u)\|+\|a_q(u)\|)du\right].
\]
The continuous complete weighted moment bounds and their amplitude
derivative counterparts from project 09 Note 9 bound this bracket by
\(O_D(A_vNw_N/q)\). To include the lower half-index, put
\(y=\log(N/(qu))\). On \(q/2\le qu\le3N/2\), the reserves
of that note give \(w(qu)/w_N\le C e^{4y/5}\) for \(y\ge0\),
with a fixed exponent gap below one. Integrating logarithmic bins therefore
bounds the continuous moment integral by \(C_D(N/q)w_N\), and
\(u\|a_q(u)\|\le C_DA_v(N/q)w_N\) bounds both endpoint terms. Since \(T\asymp N^2\), this is smaller
than the outer integral bound by \(O(N^{-1})\). Summing the
\(O_{R_0}(q)\) modes proves (19).

For the complete paid Poisson vectors \(\widetilde V_q\), use the
complete bound \(\|\widetilde V_q\|\le C_DA_v(N/q)w_N\).
Deleting the bundles (18) changes the real-vector frontier quadratic by
at most
\[
C_{R_0,D}\|Q\|A_v^2Nw_N^2H_J(H_N+1),
\qquad H_m=\sum_{j=1}^m1/j.
\tag{20}
\]
To check the coefficient sum, the exact
\(c_J(q)=\sum_{j\mid q,\,j\le J}\mu_{\rm Mob}(q/j)\)
gives
\[
\sum_{q\le N}\frac{|c_J(q)|}{q}\le H_JH_N,
\qquad \sum_{q\le N}|c_J(q)|\le NH_J.
\]
For each \(q\), the quadratic perturbation is bounded by
\(\|Q\|(2\|\widetilde V_q\|\|E_q\|+\|E_q\|^2)\).
The two displayed coefficient estimates give (20).
With \(J=\lceil N^{2/5}\rceil\), \(A_v=O(1)\), and the physical
matrix scale \(\|Q\|=O(L)\), this envelope is
\[
O_{R_0,D}(L^3N^{-\kappa/4}).
\tag{21}
\]
It is below the previously displayed \(L^4N^{-\kappa/4}\) upper-budget
scale, but that scale is not a positive floor for the actual payment or
available margin. One may use (20) as an explicit additional payment after
making its constants effective; deleting endpoints without including that
payment is not justified. Signed cancellation could make their actual
contribution smaller.

The first active Möbius band has the particularly simple exact coefficient
\[
c_J(q)=-1,\qquad J<q\le\min\{2J,N\}.
\tag{22}
\]
For these \(q\), every proper divisor is at most \(q/2\le J\),
while the divisor \(q\) is excluded. Subtract its \(\mu_{\rm Mob}(1)=1\)
term from \(\sum_{j\mid q}\mu_{\rm Mob}(q/j)=0\) to get (22).
Together with \(c_J(1)=1\) and \(c_J(q)=0\) for \(1<q\le J\),
this identifies a useful bounded target: compare the complete \(q=1\)
quadratic with the negatively weighted first active band, retaining every
\(q>2J\) term in a separate exact remainder. A separate sublattice
candidate equation would invalidate this comparison.

## 7. Bounded complete-orbit pilot

The numerical diagnostic
[pilot_complete_centered_jets.py](../13_microlocal_phase_space/numerics/pilot_complete_centered_jets.py)
and its [record](../13_microlocal_phase_space/numerics/PILOT_COMPLETE_CENTERED_JETS_20261010.json)
evaluate all terms at \(M=N\in\{22066,50000,100000\}\),
\(t=1/(2\log M)\), \(x=4\pi M^2+h\), with
\(h=0,.25,.35,.5,1,2,4,6,8\). Decimal phase reduction protects the
large common height before complex128 summation; selected complete sums
were recomputed with 75-digit Decimal arithmetic.

No counting constant is selected. The records retain each quadratic as an
affine expression in \(\Gamma\), with the physical parameterization
\[
\Gamma=\Gamma_0+
 \frac{G_{\rm density}}{(4C_{\rm count}+1)^2},
\quad \Gamma_0=\frac{18(\log A)''+9/x^2}{c^2},\quad
G_{\rm density}=\frac{9\log x}{2(8\pi)^2c^2}.
\]
For diagnostics, payments are evaluated at the two endpoints of the
coefficient range associated with \(C_{\rm count}\ge0\). The finite
range of the imported count theorem and the all-real threshold hypotheses
are not established by this pilot.

The following values are rounded numerical measurements, not interval
bounds. The fourth-jet column is the *upper payment*
\(\widehat\delta_4=24L^4\eta+E_4\), not a measured genuine-function
error. The quadratic ratio is evaluated at the diagnostic coefficient
range endpoints across the nine sampled heights.

| Cutoff | Holomorphic value payment eta at h=0 | Fourth-jet upper payment at h=0 | Largest absolute Bell residual payment E4 in samples | Physical quadratic payment / absolute K | Detected finite critical points | Smallest absolute F / eta at those points |
| --- | --- | --- | --- | --- | --- | --- |
| 22066 | 0.00964146 | 37049.8 | 8.5301e-8 | 12.94–72.53 | 13 | 77.50 |
| 50000 | 0.00578247 | 30431.2 | 2.2292e-8 | 12.65–28.64 | 13 | 200.08 |
| 100000 | 0.00374947 | 25295.5 | 7.0809e-9 | 4.86–26.44 | 14 | 185.54 |

All sampled states fail the paid joint value/derivative candidate screen;
the minimum first-jet curved predicate is about 82.20, above its candidate
allowance of one. A separate step-.125 scan and numerical refinement detects
13, 13 and 14 sign-changing critical points of the finite F. Their closest
finite values remain about .7472, 1.1570 and .6957. These are detected
critical points, not certified total counts; scanning can miss other roots
and proves no interval coverage.

Every sampled K is numerically positive throughout its affine diagnostic
coefficient range. Jdagger changes sign in the first two windows, but those
states do not meet the candidate constraints. Its sign cannot replace K
through the candidate-only payment there. The curved/slab ratios at the
recorded coefficient endpoints range approximately from .6233 to .9911,
consistent with (10).

The complete physical Bell correction is tiny compared with the Cauchy
fourth-jet payment at these moderate cutoffs. Thus this pilot does not
expose the desired threshold sign, and merely extending this particular
sparse sweep would not settle it. For a candidate-level test, either a
sharper complete holomorphic jet payment or a different useful sign margin
must be obtained; the positive sampled K also supplies no such margin.
This is evidence about the bounded diagnostic, not a uniform obstruction
or a bound on the actual approximation error.

The retained 22066 center certificate calibrates F, Fprime and the complete
current to within 1e-10 in numerical midpoint comparisons. Raw derivatives
through order four pass displaced-sum finite-difference controls. Complete
75-digit moment comparisons have relative differences below 1e-10, with
observed errors around machine precision. An independent full replay
matches every record field except elapsed time. None of these floating
controls is an outward sign enclosure.

The companion
[exact localization/support checker](../13_microlocal_phase_space/numerics/check_candidate_localization_and_support.py)
and its [small record](../13_microlocal_phase_space/numerics/CANDIDATE_LOCALIZATION_SUPPORT_RECORD_20261010.json)
pass 6914 exact rational controls for Sections 1–3: complete-square algebra,
physical candidate-null identity, support attainment/comparisons, and upper
endpoint monotonicity. These controls do not evaluate Sections 4–6's
oscillatory integrals or make their asymptotic constants effective.

## 8. Complete coupled Möbius diagnostic

The additional
[pilot_coupled_mobius_frontier.py](../13_microlocal_phase_space/numerics/pilot_coupled_mobius_frontier.py)
and its [record](../13_microlocal_phase_space/numerics/PILOT_COUPLED_MOBIUS_FRONTIER_20261010.json)
compute the exact-coefficient representation of the complete small-gcd
frontier at \(N=100000\), \(J=\lceil N^{2/5}\rceil=100\), and
\(h=0,.35\), using the same protected actual phases.
All 34511 nonzero integer coefficients are included, with their range
from -5 to 4. The divisor identity is checked for every integer through N.
A sublattice with \(q>N/2\) consists of one term; its Jdagger vanishes
by the exact diagonal-annihilation identity. That exact zero is optimized,
not replaced by a numerical tail estimate.

The source keeps both phase channels and every BB, CC and mixed BC
contribution. It uses summed sublattice moments, with O(N log N) work,
and never expands all N squared ordered pairs. Its hash-bound dependency
is the unchanged primary pilot source. Formal Fraction controls through
N=12 verify the direct pair/gcd identity and singleton annihilation in
234 assertions. These controls do not certify the huge-height signs.

The following affine expressions are rounded numerical diagnostics in the
symbolic coefficient Gamma:

| Height offset | Complete q=1 contribution | First active band 101<=q<=200 | All q>200 | Complete frontier |
| --- | --- | --- | --- | --- |
| 0 | 22359.825 + 11.927 Gamma | -987.300 + 2.493 Gamma | 13.472 - 0.825 Gamma | 21385.997 + 13.595 Gamma |
| .35 | 239137.769 - 243.413 Gamma | -1522.089 + 4.960 Gamma | -412.531 + 2.524 Gamma | 237203.149 - 235.930 Gamma |

The first active band is negative over the diagnostic coefficient range at
both tested heights. Its magnitude is insufficient to overcome the complete
q=1 contribution, and the full frontier remains numerically positive. The
remaining q terms are retained and can have either sign. No candidate
constraint is imposed on an individual sublattice, and the tested complete
states do not meet the joint candidate tolerances.

Thus this calculation supplies a concrete cancellation to retain, but does
not supply an opposite threshold sign. It directs the next estimate toward
the complete q=1 term together with its coupled rational-grid correction,
under actual candidate conditioning. An isolated sign theorem for the first
active band would not suffice. The localized ceiling in Section 5 provides
a tractable way to inspect its macroscopic stationary/boundary content;
the lower-index complement and all cross terms must remain in the estimate.

## 9. Resulting signed criterion and next bounded proof task

The analytical continuation can now replace the former candidate-null
payment in project 09 Note 7 by (8). On a rigorously stated ordinary
threshold-candidate region, a sufficient exclusion is
\[
U_{\rm rem}+E_{\rm transform}+B_{\rm near}
 +\Pi^\dagger_{\rm curved}+E_{\rm phys}<0.
\tag{23}
\]
The remainder includes every separated pair and every retained low-index
near pair, with actual phases, signed Möbius weights, both channels and
all complete mixed terms. Endpoint transitions are either included in its
signed main expression or paid by an effective bound such as (20). Curvature
localization (1)–(5) can restrict the candidate region after the coefficient
and payment bounds have been justified. The positive diagnostic frontiers
are outside that candidate region and decide no uniform sign there.

The next bounded proof task is an effective one-sided estimate for this
complete candidate-conditioned resonant contribution, using the rational
frequency coupling (12), the local Fourier remainder (16), and literal
endpoint terms. The current pilot gives no negative complete threshold
margin. The newly sharpened null payment and the endpoint envelope alone
cannot supply one. Higher multiplicity and uniform parameter/cutoff coverage
remain separate open obligations.

[Internal review](../13_microlocal_phase_space/reviews/7_CANDIDATE_LOCALIZATION_AND_SIGNED_PILOT_INTERNAL_REVIEW_20261010.md)
records the analytical cross-audits and independent numerical replays.
