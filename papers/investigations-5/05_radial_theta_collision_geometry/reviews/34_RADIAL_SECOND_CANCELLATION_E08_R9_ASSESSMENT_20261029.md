# CTF-E08 R9: radial deadline proof and direct-comparison assessment

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, Investigation05 **chat0029**, **Assess CTF-E08 R8 Sol**.

**Verdict: accepted without mathematical correction within the inherited
prepared radial class and the declared displayed-split comparison.**
All eight obligations in the [frozen R9 packet][packet] pass. Under
m=int W0=0, the issued theorem proves
\[
S_{\max}\le S_9=(1-\varepsilon_9)S_{1,\rm opt}<S_{1,\rm opt},
\quad\varepsilon_9=\frac{41}{441}
 \left[1-\left(\frac{2873}{2880}\right)^{4/5}\right]>0.
\]
This accepts [Note63][n63]'s scoped theorem. Its issued deadline is
**longer** than the stronger same-data direct deadline S_w established in
[the prior supporting addendum][extra]. Thus the accepted narrow gain
supplies no demonstrated advantage over that direct comparator, no
source-specific regularity through a deadline and no new physical region.
[Self-assessment33][r33] remains the author's own check.

## 1. Full-source concentration and preparation costs

Note55's per-positive-summand calculation gives
ell_n''<=-149/2<-74 and ell_n'(0)<=5/26<1/5. The polynomial identity
used for the second derivative is correct. Summing the first-derivative
inequality, with full-tail domination, proves q'<=(1/5-74u)q. No claim
that a sum preserves log concavity is needed.

For p=(1+u^2)q, p'<=(6/5-74u)p. Integration from u to u+t gives
p(u+t)<=p(u)exp(6t/5-74ut-37t^2). Integrating u>=0 proves the stated
survival bound for p/M. Tonelli gives
\[
\mathbb E e^{4U}=1+4\int_0^\infty e^{4t}\Pr(U\ge t)dt
\le1+4e^{169/925}\sqrt{\pi/37}<8/3.
\]
The shifted half-line Gaussian is bounded by its **full-line** integral;
there is no missing factor of two. The elementary bounds
sqrt(pi/37)<1/3 and exp(169/925)<=925/756<5/4 are valid.

The exact spherical Jacobian, raw-vector domination by rho(1+u^2),
positive convolution and vector Young give
\[
P_0\le\overline P=\sqrt{MR_0},\qquad
E_0\le(8\pi)^{-3/2}M^2,\qquad
7<R_0/M<26/3<9.
\]
R0 includes the full preparatory moment6M. All source terms are retained.
No physical first-jet floor is an input. Exact integral expressions pay
the bound analytically; numerical deadline acquisition would additionally
need rigorous numerical budgets, including a positive lower E0. None
was acquired in this task.

## 2. Actual fixed-path transition derivatives

On every compact lifespan interval, alpha is continuous and bounded.
Subtracting the additive Brownian path leaves an ordinary integral
equation with smooth globally bounded spatial drift derivatives. Its
starting-point derivatives obey exactly
\[
J'=-\alpha Dv(X)J,\qquad
K'=-\alpha Dv(X)K-\alpha D^2v(X)[Jh,Jk].
\]
Here J0=I and K0=0. No derivative of the realized feedback path occurs.
The minimum radial eigenvalue of Dv is 7/8; tangential eigenvalues exceed
one. Writing f=(1+r^2)^(-1), direct differentiation gives
\[
\partial_{jk}v_i=-2f^2(\delta_{ij}x_k+\delta_{ik}x_j+\delta_{jk}x_i)
                  +8f^3x_ix_jx_k,
\]
whose Frobenius norm is bounded by 6sqrt3 r f^2+8r^3f^3<20. This bounds
the bilinear operator norm as well. With kappa=7/8 and tau=exp(-kappa B),
contraction and variation of constants therefore give
\[
\|J\|\le\tau,\qquad
|K[h,k]|\le(20/\kappa)\tau(1-\tau)|h||k|.
\]
These uniform bounds justify differentiating the expectation of the
bounded exponential test by dominated difference quotients. The drift
sign is -alpha v, correctly matching the forward density equation.

## 3. Signed Taylor cancellation and the curvature term

The zero vector mass cancels the constant Taylor term componentwise.
Radiality and the paid first absolute moment give int y_i W0(y)dy=0.
Taylor's integral remainder and the vector triangle inequality give
\[
|\widehat W_s(\xi)|\le\frac{R_0}{2}
 \{\tau^2|\xi|^2+(20/\kappa)\tau(1-\tau)|\xi|\}.
\]
The factor1/2 is correct. The second term is the essential non-affine
curvature cost; no purely quadratic frequency bound for all compression
has been proved. Spatial starting-point differentiation is distinct from
physical frequency differentiation of the source or mark.

## 4. Declared comparator

The old first-moment cap gives
G>=E0 R^2-Pbar^2 tau^2 R^7/(10pi^2). Optimizing this **displayed split**
puts r(B)^5=20pi^2 E0/(7Pbar^2 tau^2), with low-frequency allowance
2E0/7. Thus G>=(5/7)E0 r(B)^2 and
\[
\alpha\ge c_1e^{\beta B},\qquad c_1=(5/21)r_0^2,\quad
\beta=4\kappa/5=7/10,
\]
\[
S_{1,\rm opt}=1/(\beta c_1)
 =6\left(\frac7{20\pi^2}\right)^{2/5}
   \overline P^{4/5}E_0^{-2/5}.
\]
The optimization gain over Note28's half-energy split is correctly
credited to the comparator, not to radial second cancellation. The word
optimal is restricted to that displayed expression, not all Fourier
arguments or all direct methods.

## 5. Complete finite compression window

In the unnormalized Fourier convention the squared-frequency and
fourth-power integrals over a ball are R^5/(10pi^2) and R^7/(14pi^2).
Minkowski therefore gives exactly Note63(12). At R=kr(B), normalized by
sqrt(2E0/7), the two terms are
\[
k^{7/2}\sqrt{5Z/28}\,e^{-3\kappa B/5}
 +\frac{80}{7}\sqrt{R_0/M}\,k^{5/2}(1-e^{-\kappa B}),
\quad Z=(R_0/M)r_0^2.
\]
The initial Young and carrier bounds give
\[
Z^5\le\frac{400\pi}{49\cdot512}(R_0/M)^3<3^5.
\]
For k=21/20, k^7<3/2 and k^3<6/5. The first squared term is below
45/56<81/100. On the closed compression window
B<=b0=(8/7)log(2880/2873), the second term is at most
(80/7)3(6/5)(7/2880)=1/10. Hence the full normalized norm is strictly
below1 and alpha>=k^2 c1 exp(beta B) on that window. This prices curvature;
it is not an assumed interval of physical or auxiliary time.

## 6. Complete conditional deadline

Since E0>0, G>0: a zero-gradient L2 field on all of Euclidean space
would vanish. Consequently alpha>0 and B is a strictly increasing clock.
Conditional on m=0, Note28 supplies finite breakdown and B tending to
infinity. Integrating ds/dB over the two ranges gives
\[
S_{\max}\le\frac1{\beta c_1}
 [k^{-2}(1-e^{-\beta b_0})+e^{-\beta b_0}].
\]
Now 1-k^(-2)=41/441 and beta b0=(4/5)log(2880/2873), proving the exact
epsilon9 and strict saving. The labeled decimal 0.0180819995 percent is
a constant-only illustration. No numerical theta horizon, iterative
restart or unknown positive exponential upper allowance is used.

## 7. Matched information and the stronger direct comparisons

The earlier [supporting addendum][extra] is separately identified; it is
not an amendment to the packet. Its direct comparison is verified here.
From the same cap A|xi|, A=Pbar tau, retaining the full Plancherel deficit
weight gives
\[
G\ge R^2E_0-(2\pi)^{-3}\int_{|\xi|\le R}
 (R^2-|\xi|^2)|\widehat W_s(\xi)|^2d\xi
\ge R^2E_0-\frac{A^2R^7}{35\pi^2}.
\]
Optimization at R^5=10pi^2 E0/A^2 gives the complete direct deadline
\[
S_{\rm w}=6(10\pi^2)^{-2/5}\overline P^{4/5}E_0^{-2/5},\qquad
S_{\rm w}/S_{1,\rm opt}=(2/7)^{2/5}.
\]
Since (2/7)^(2/5)<2/3 and 1-epsilon9>9/10, it follows exactly that
\[
\boxed{S_{\rm w}<S_9<S_{1,\rm opt}.}
\]
This uses identical M,R0,E0 and no radial second cancellation or carrier
concentration premise. **R9's issued deadline does not improve this
stronger same-information direct comparator.** This utility qualification
does not invalidate its explicitly scoped split theorem or exclude every
possible second-cancellation estimate. No new such estimate was attempted.
There is also no established ranking against a separately paid exact-P0
deadline, and no measured acquisition-cost advantage.

At theta's actual mark (1/4,2), Note55 already gives
mu=|(H,H_a)|>=35M2/18>0; Note29 then pays every finite auxiliary horizon.
This is stronger physical information. The hypothetical m=0 upper deadline
is not theta's actual breakdown time. R8's accepted closed local bound
and open extended lifespan are unchanged; no proof makes them reach S9
or S_w. A smaller upper deadline is not regularity through that deadline.

## 8. Controls and retained fields

| Control | Actual sufficient premise or qualification |
| --- | --- |
| Positive weighted-square | Positive weights preserve the per-square slope inequality at T=1/4, hence concentration and preparation costs at each fixed frequency. The three-square collision near44.13 shares the R9 premises; full unit coefficients/reflection fail but are not a separator here. |
| Gaussian-polynomial cosine | For q*=(64u^4+6)e^(-4u^2), M0=9sqrt(pi)/4, M2=21sqrt(pi)/32, M4=123sqrt(pi)/256. Their ratio is 97/248. Thus R0/M>=7+8(97/248)=314/31>9, using e^(4u)>=1+8u^2. It fails this sufficient concentration payment, still satisfies the generic transition estimate, and remains admitted by S_w. Its event is (1/4,2sqrt6). |
| R6 polynomial kernels | Full cosine/Newman compatibility fails. Standard domination by rho(1+u^2) is not supplied. Their admitted radial fields retain the generic Taylor estimate with actual moments; no universal failure is asserted. |
| Finite-prime orbit | Full reflection/canonical source fails; generic radial preparation survives on its moment domain. Concentration is unacquired; high-gap locations remain qualified. |
| Reflected super-Gaussian | Full square arithmetic fails. Generic preparation survives; no concentration value is asserted. Its pi/4 event is elsewhere. |
| Smooth shape / positive primitive | The named properties do not identify theta or supply this quantitative concentration. No new event or failed concentration premise is invented. |
| Euler-factor | Modified source/conductor; generic argument survives for admitted data. Concentration is unacquired; a Laguerre witness is not automatically a double event. |
| Atomic/profile / continuous compact | Atoms remain outside the imported source-function theorem. Admitted continuous preparation needs the actual concentration condition; no new instance is asserted. |
| RH-conditional endpoint | Retain RH, altered arithmetic and escaping heights. Concentration is unacquired. |

Actual fixed-mark jets retain multiplication before preparation. The
initial residual is nonzero; full source/cutoff commutators, combined
Theta+R cancellation at r=1 and the whole inner ball remain. With the
theta operator, controls also retain any raw source mismatch. No
residual-energy bound through the new deadline is obtained.

## Evidence and disposition

All **17** frozen inputs match at intake and final recheck, including both
unchanged TeX sources. The packet SHA-256 remains
`9017a5d090c8d215380c9986d8214808c514432c390cc818a3760e28d9d1cf12`.
The separately identified supporting addendum remains SHA-256
`b7b2d5833cb955d42891735d1f6c19c74423451c83a93243be54ef339230d116`.
The supplied constant script was replayed without writing its record:
all 12 exact checks pass and stdout is byte-identical to the frozen JSON.
Its floating illustrations remain labeled and are not source certificates
or substitutes for the all-parameter proof.

Actual assessment **gpt-6.1-sol / ultra**, chat0029, turn
`01a1898e-7cea-7f93-adc2-6bdd140d351e`. Three read-only same-model
contributing audits supported the parent verdict. This is different-model
internal assessment of Astra/max's R9, with prior supporting-contributor
overlap and shared premises including Notes28/40/55. It is not specialist
or formal independence. No new source acquisition, candidate, k/b0
optimization, PDE evolution, manuscript edit or build occurred.

**E08 R9 complete; B02 remains partial; E03/B03 remain gated.**
[Return65][return] and [Continuation66][next] record the consequence and
next conceptual decision. The [result index][results], [spatial results][spatial],
[control screen][controls], [avoid index][avoid], [scope][a07] and
[quantitative utility][a20] retain their stated meanings.

[packet]: ../research-progress/handoffs/CTF-E08_RADIAL_SECOND_CANCELLATION_ASSESSMENT_REQUEST_R9_20261029.md
[n63]: ../notes/63_RADIAL_SECOND_CANCELLATION_DEADLINE_B02_R9_20261029.md
[r33]: 33_RADIAL_SECOND_CANCELLATION_B02_R9_SELF_ASSESSMENT_20261029.md
[extra]: ../notes/CTF_B02_R9_WEIGHTED_DIRECT_COMPARISON_CHAT0029_20261029.md
[return]: ../notes/65_RADIAL_DEADLINE_E08_R9_RESEARCH_RETURN_20261029.md
[next]: ../notes/66_RADIAL_DEADLINE_ASSESSMENT_AND_MODEL_CONTINUATION_20261029.md
[results]: ../../../../result-summaries/README.md
[spatial]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
