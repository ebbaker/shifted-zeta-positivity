# Pair statistics, inverse-distance matrices, and deterministic heat relaxation

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual delegated configuration **gpt-6-astra (Codex)**, reasoning effort **ultra**. Status: **proved in-note in the stated information classes; internal same-model checks and parent integration review only**. No independent specialist review or novelty claim.

**Classification.** This is a quantitative screening and transfer note, not a simplicity criterion claimed as progress. It proves the two distinct inverse-square target constants, stability of weak pair laws under sparse repeated or nearly repeated points, an explicit shrinking-test error threshold for finite-population simplicity, and exact heat controls separating late simplicity from an early event and finite root positions from cap phase. It also records the companion matrix/heat-flow note's deterministic relaxation theorem and its exterior forcing term. None supplies an unchanged-theta exclusion estimate. Read the [result index][results], [avoid index][avoid], [collision controls][controls], [target rule][a01], [control rule][a02], [scope rule][a07], and [coupled-error rule][a12]. The [matrix companion][matrix], [canonical pair cancellation][pair], [complex cap estimate][cap], and [closure calculation][closure] retain their original hypotheses.

## 1. Which limit is being proposed?

There are different variables: real heat time t, root height/rank, and population size m. A PCC statement must prescribe a joint sequence of populations and an unfolding scale. For a finite real population x_1(t),...,x_m(t), counted with multiplicity, choose a spatial density rho(t)>0 and put y_i=rho x_i (a common translation is immaterial). Define the ordered off-diagonal pair measure

\[
 \mu_{t,m}=\frac1m\sum_{i\ne j}\delta_{y_i-y_j}.
 \tag{1}
\]

The labels, not distinct locations, specify the diagonal. Repeated locations with different labels contribute at zero. The unit-density sine-kernel candidate is

\[
 \mu_{t,m}\Longrightarrow R_2(s)\,ds,\qquad
 R_2(s)=1-\left(\frac{\sin\pi s}{\pi s}\right)^2,
 \tag{2}
\]

where convergence is against continuous compactly supported tests and must be stated along a particular t,m,height limit. A finite fixed population has an atomic pair measure and cannot itself converge to (2) without a population limit. A distance to GUE can be defined from a countable convergence-determining family of bounded compactly supported tests f_k (dense on each compact exhaustion and including nonnegative cutoffs controlling local masses), for example

\[
 d_{\rm pair}(\mu,R_2ds)=\sum_{k\ge1}2^{-k}
  \min\left\{1,\left|\int f_k\,d\mu-\int f_kR_2ds\right|\right\}.
 \tag{3}
\]

This is a diagnostic for the explicitly selected weak topology. It is not a lower bound on every gap or an estimate for the physical cap.

Montgomery's original paper assumes RH and studies high zero ordinates. His conjectured pair law uses the scale log T/(2 pi), with T a **height cutoff**, not heat time; he explicitly derives almost-all simplicity from the conjecture, not all-zero simplicity (pp.181,184). The same paper records Dyson's comparison with large complex Hermitian/unitary matrices. Primary source: [Montgomery, 1973](https://www-personal.umich.edu/~hlm/paircor1.pdf), especially pp.181–184. These are literature facts; everything below is derived here or imported explicitly from the repository.

The actual complete-source theorem already available in LHCT Note 03 gives, for every fixed finite set of late theta ranks,

\[
 y_j(t)=L_t x_j(t)/\pi\longrightarrow j-\tfrac12,
 \qquad L_t\sim\tfrac14\log t.
 \tag{4}
\]

Its target is a clock. A new GUE question is therefore necessarily a different joint high-population/high-rank/heat regime. There is presently no uniformity in m in (4) permitting interchange of limits. Taking t to infinity first at each fixed m and then m to infinity gives the clock pair law, not (2).

## 2. The inverse-distance matrix gives the exact relevant weight

For real distinct y_i define the antisymmetric matrix

\[
 A_{ij}=\begin{cases}(y_i-y_j)^{-1},&i\ne j,\\0,&i=j,\end{cases}
 \qquad
 Q_m=\frac1m\|A\|_F^2
      =\int s^{-2}\,d\mu_{t,m}(s).
 \tag{5}
\]

This is a concrete version of the proposed matrix quantity. For real roots the Frobenius norm gives the positive inverse-square weight. On complex-time continuations the holomorphic discriminant uses (z_i-z_j)^(-2), whereas a Frobenius norm uses |z_i-z_j|^(-2); those are different quantities and their phases cannot be discarded.

For a proper finite factorization H=U product_i(z-x_i), let b_i=(U_z/U)(t,x_i). The exact backward-heat equation yields

\[
 x_i'=2\sum_{j\ne i}\frac1{x_i-x_j}+2b_i,
 \quad
 \frac{\Delta'}{\Delta}=4m\rho^2Q_m+
 4\sum_{i<j}\frac{b_j-b_i}{x_j-x_i},
 \quad \Delta=\prod_{i<j}(x_j-x_i)^2.
 \tag{6}
\]

The last term retains the complete exterior and nonzero factor. This is BW12 Note 09 / LHCT Note 03 in matrix notation. It must be estimated jointly with the pair term.

Two exact target values make this statistic discriminating:

\[
 Q_m^{\rm clock}=\frac2m\sum_{d=1}^{m-1}\frac{m-d}{d^2}
 \longrightarrow\frac{\pi^2}{3},
 \tag{7}
\]

whereas the sine-kernel moment is

\[
 Q^{\rm sine}=\int_{\mathbb R}\frac{R_2(s)}{s^2}\,ds
             =\frac{2\pi^2}{3}.
 \tag{8}
\]

For (8), use

\[
 \left(\frac{\sin\pi s}{\pi s}\right)^2
 =\int_{-1}^{1}(1-|u|)\cos(2\pi us)\,du,
\]

Tonelli, and the elementary identity integral_R (1-cos(as))/s^2 ds=pi |a|. The result is 2 pi^2 integral_(-1)^1 |u|(1-|u|)du=2 pi^2/3. Near zero R_2(s)=pi^2 s^2/3+O(s^4); the moment is finite, and the tail is integrable. Thus even exact convergence to the two different pair laws gives different finite normalized inverse-square energies, not zero energy.

For the existing theta scaling rho=L/pi, (6) is 4m(L/pi)^2 Q_m plus its exterior term. LHCT03 proves the latter cancels this order-L^2 quantity, leaving

\[
 \Delta'/\Delta=-2m(m-1)/\kappa+O(\kappa^{-5/4})
 \tag{9}
\]

at fixed rank. A relative o(1) pair law alone does not resolve that much smaller complete response.

## 3. Weak PCC neither removes exceptional doubles nor controls (5)

**Sparse perturbation lemma.** Suppose an array of n real labeled points has pair measures (1) converging vaguely to a locally finite measure. One can add one repeated point to each array while preserving this limit. One can instead add a distinct point at distance at most n^(-2) from an old point, again preserving the limit, but making Q_(n+1) at least 2n^4/(n+1). If the original arrays are simple, the latter modified arrays remain simple.

**Proof.** For each fixed R, convergence implies that the number of ordered pairs at distance at most R is O_R(n): dominate its indicator by a fixed compactly supported continuous cutoff. By a diagonal choice, choose R_n tending to infinity so slowly that the number of pairs at distance at most R_n is o(n^2). An averaging argument supplies an index i_n with o(n) neighbors within R_n. Duplicate its location. For a test supported in [-R,R], the new ordered pairs affecting the integral number o(n), while the normalization changes from 1/n to 1/(n+1). Both changes tend to zero. The repeated pair adds an atom 2/(n+1) at zero, invisible in the limit. Alternatively add a point at distance epsilon_n in (0,n^(-2)] from this location, avoiding the finitely many old points. It has o(n) neighbors in each fixed range because R_n tends to infinity. The same convergence follows, but its one ordered near-pair contributes 2/((n+1)epsilon_n^2) to Q_(n+1). This proves the assertion. No claim is made that such arbitrary arrays are theta zero sets.

This is a scoped information-theoretic obstruction: weak pair-law data alone cannot rule out sparse multiple points or extremely close simple points. It agrees with Montgomery's almost-all conclusion. Full PCC at high ordinates would still leave any finite exceptional low zero untouched.

A valid transfer of (2) to (8) needs, in addition, small-gap uniform integrability and a large-gap tail bound:

\[
 \lim_{\delta\downarrow0}\limsup_n
   \int_{|s|<\delta}s^{-2}\,d\mu_n=0,
 \quad
 \lim_{R\to\infty}\limsup_n
   \int_{|s|>R}s^{-2}\,d\mu_n=0,
 \tag{10}
\]

where a zero-gap atom makes the first integral infinite. Cut off s^(-2) on delta<=|s|<=R, pass to the weak limit, then remove the two cutoffs. Equation (10) is a **new analytic hypothesis**, not a consequence of PCC, and its literal finite-array version is incompatible with an exact repeated point on infinitely many arrays. It must not be inserted as an assumption while advertising its conclusion as a proof of simplicity. For avoiding such an assumption during measurement one can use the regularized statistic integral (s^2+epsilon^2)^(-1)dmu, while retaining its epsilon dependence; no uniform epsilon-to-zero conclusion is then automatic.

For a finite simple population a proved bound Q_m<=C implies the explicit minimum-gap bound min_(i!=j)|y_i-y_j|>=sqrt(2/(mC)). This is elementary and much stronger than weak PCC. Its height/population deterioration and its need for a finite all-pairs bound remain visible.

### The extra rate that would make a pair estimate exclude every finite-window double

There is a precise quantitative strengthening of PCC worth recording once as a **conditional test**, without treating it as a new theta estimate. Let f_delta(s)=(1-|s|/delta)_+ and suppose an actual finite population satisfies the proved enclosure

\[
 \left|\int f_\delta\,d\mu_m-\int f_\delta R_2\,ds\right|
 \le e_m(\delta).
\]

The Fourier representation used above and 1-cos v<=v^2/2 imply R_2(s)<=pi^2 s^2/3, hence

\[
 \int f_\delta R_2\,ds\le\frac{\pi^2\delta^3}{18}.
\]

Every repeated pair contributes two ordered terms at zero, so one double forces integral f_delta dmu_m>=2/m. Consequently

\[
 \boxed{\frac{\pi^2\delta^3}{18}+e_m(\delta)<\frac2m
 \quad\Longrightarrow\quad\text{every point of this population is simple}.}
\]

For example, delta=o(m^(-1/3)) together with e_m(delta)=o(1/m) would suffice. Ordinary weak PCC supplies neither shrinking-test uniformity nor this error scale. At the stronger threshold 1/m the same estimate excludes every pair with |y_i-y_j|<=delta/2, because each such pair contributes at least one in total before dividing by m. These are exact counting implications, not established error bounds for theta; they identify the much stronger finite-population input a statistics route would have to pay.

## 4. Heat relaxation has a surviving deterministic version

The user's proposal to seek a decreasing root-distribution functional does have an exact finite-polynomial realization. The [matrix companion][matrix] supplies the detailed proof (the following y is sqrt(2) times its u): for a full monic heat polynomial with simple real roots, s=log(t+c), y=x/sqrt(t+c), the logarithmic energy

\[
 \mathcal E(y)=\tfrac14\sum_i y_i^2-2\sum_{i<j}\log(y_j-y_i)
\]

satisfies dy/ds=-grad cal E and dcal E/ds=-||grad cal E||^2. Its unique equilibrium is the scaled Hermite zero vector; the energy gap decays at least as exp(-(s-s_0)). This is a deterministic energy minimizer, not a random GUE sample.

For a proper cluster H=U product_i(z-x_i), the same rescaling instead gives the exact forcing

\[
 \frac{dy}{ds}=-\nabla\mathcal E+f,
 \quad f_i=2\sqrt{t+c}(U_z/U)(t,x_i),
 \quad
 \frac{d\mathcal E}{ds}=-\|\nabla\mathcal E\|^2
                 +\langle\nabla\mathcal E,f\rangle.
 \tag{11}
\]

The complete exterior term is therefore the new analytic obligation for a theta application. LHCT03's actual cancellation theorem shows why it cannot be omitted. The fixed-rank theta normalization in (4) is different from the polynomial sqrt(t) normalization.

Dyson Brownian motion includes stochastic diffusion and, in its stationary Gaussian version, confining drift. Its beta=2 stationary eigenvalue density has a Vandermonde-squared factor. The matrix/eigenvalue stochastic equations and stationary density are displayed in [Joyner–Smilansky, appendix by Zagier, 2015, equations (1.2)–(1.8)](https://people.mpim-bonn.mpg.de/zagier/files/arxiv/1503.06417/1503.06417v1.pdf). This primary source supports the stochastic comparison; it does not identify deterministic heat evolution with Dyson Brownian motion. Removing the noise leaves a deterministic gradient mechanism and changes its equilibrium.

## 5. Exact controls for the two remaining logical steps

**Late simple clock roots do not exclude an early heat event.** The entire heat field

\[
 H(\tau,z)=e^\tau\cos z+1
 \tag{12}
\]

obeys H_tau=-H_zz and reality symmetry. At (0,pi) it has H=H_z=0 and H_zz=1, an ordinary double event with local complex degree one for (H,H_z). For real t>0, the two roots in (0,2pi) are pi plus or minus arccos(e^(-t)); they are simple and tend to pi/2,3pi/2. For t<0 the pair is pi plus or minus i arcosh(e^(-t)). Thus the field is real-rooted and simple for every positive real time, and its late zero pattern tends to a clock, while the earlier event remains. The source is a positive atomic cosine measure, not the unchanged theta source. This is a control against the generic inference from late simplicity/regularization to absence of earlier charge, not a theta counterexample.

**Finite root positions do not determine physical cap phase, even for exact heat solutions.** Compare

\[
 H_1(\tau,z)=z,\qquad
 H_2(\tau,z)=e^{a^2\tau}\frac{\sin(az)}a,\qquad a>0.
 \tag{13}
\]

Both are exact real-type heat solutions and have the same tracked simple root z=0 at every time. Their root derivatives are respectively 1 and e^(a^2 tau). On regular projective disks |q|<=epsilon<1/a, q=H/H_z, their inverse maps are z=q and z=arctan(aq)/a. For the physical jet G=(H,H_z), the exact cap formula of LHCT02 gives, on t=T and -Y<=Im tau<=Y,

\[
 I_{T,1}=0,\qquad
 I_{T,2}=\frac{\epsilon^2}{1+\epsilon^2}\frac{a^2Y}{\pi}.
 \tag{14}
\]

These have identical one-root position data but different cap phase; the second has additional exterior roots. No unsupported scalar multiplication of a heat field was used: both fields satisfy the PDE exactly. This demonstrates the missing information for a finite-population statistic, not nonuniqueness from the full global zero set. It is consistent with LHCT02's actual nonzero fixed-width canonical theta cap and LHCT04's fully retained imaginary-time closures.

## 6. What survives as a research task

A pair-distribution program can now be stated precisely: select the joint heat/height/population limit; use the matrix (5) and either a clock target in the proved fixed-rank regime or a separately justified sine-kernel target elsewhere; pay small-gap and far-tail errors for the inverse-square weight; retain the exterior divided differences in (6); and finally retain complex-time derivative phase and the full boundary ledger. A useful next numerical experiment would compare the coupled quantity (6), not merely a histogram's distance to a target. No numerical experiment is required to establish the exact analytic screens above.

For the presently paid canonical cap geometry, the fixed-rank source estimate already proves late simplicity and evaluates the full cap more directly. The new Lyapunov theorem and singular-statistic transfer conditions are reusable independently, but neither supplies an opposing estimate on the complete closures or excludes a hypothetical endpoint event. Any proposed claim that PCC alone makes those cap and closure integrals zero is rejected only within that stated information class.

[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[matrix]: 06_PAIR_DISTANCE_MATRICES_AND_FORCED_HEAT_DISSIPATION_20261022.md
[pair]: 03_FIXED_RANK_PAIR_CANCELLATION_AND_TUBE_CONTROLS_20261022.md
[cap]: 02_COMPLEX_TIME_THETA_JETS_AND_LATE_CAPS_20261022.md
[closure]: 04_IMAGINARY_TIME_CLOSURE_CONCENTRATION_20261022.md
