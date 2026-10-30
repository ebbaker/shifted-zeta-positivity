# FCG-E02 R4 verification notes

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol**, reasoning effort **ultra**, existing Investigation05 **chat0047**, *Continue FCG-E02 R2 assessment*.

The [seven-check assessment][review] accepts [Note22][proof] without mathematical correction under the [frozen R4 request][packet]. These notes give supporting derivations and scope checks. The complete source, Note16 coefficient, accepted finite certificate and issued requests remain unchanged. Three read-only same-Sol contributions assisted this different-model internal assessment of the Astra/max proof, with shared premises and no specialist/formal independence.

## 1. Exact tail rejection and the zero case

Use \(E_i=e_i(R)>0\) at \(R=2r\), not \(e_i(r)\). With
\[
 Z=2|b|E_0+|h_1|E_1,\quad M_G=Z+R|b|E_1,\quad
 \nu=\max\{|h_0|/E_0,|h_1|/E_1\},
\]
the exact discriminant satisfies
\[
 |D_0|\le h_1^2+2|b||h_0|\le\nu Z.
\]
Subtracting the actual finite sum, tail and time penalty gives
\[
 d_N\le(\nu-\kappa_N)Z-\kappa_NR|b|E_1-2b^2r-F_N.
\]
Thus \(\nu\le\kappa_N\) implies \(d_N\le0\), and \(\nu<\kappa_N\), \(Z>0\), implies strict negativity. If \(Z=0\), positive \(E_i\) force \(b=h_1=0\); the whole row, all \(g_{mn}\), \(F_N,M_G,D_0,d_N\) then vanish. No division by \(Z\) or a jet minimum is made.

This bounds the exact candidate from above. It is not the earlier invalid inference from a negative interval lower bound or an unnecessarily enlarged substitute allowance. Precision cannot change its exact sign.

## 2. Complete-source differentiability and paid integration by parts

Differentiating the complete physical summand gives
\[
 \Phi_n'=(30\lambda_n^2e^{9u}-15\lambda_ne^{5u}
             -8\lambda_n^3e^{13u})e^{-\lambda_ne^{4u}}.
\]
The \(30\) combines \(18\) from the prefactor derivative and \(12\) from differentiating the exponential against its negative source term.

For \(u\ge0,n\ge1\), \(n^2e^{4u}\ge(n^2+e^{4u})/2\). Consequently a constant independent of \(n,u\) gives the separated majorant
\[
 |\Phi_n'(u)|\le Cn^6e^{-\pi n^2/2}
                  e^{13u-(\pi/2)e^{4u}}.
\]
The index sum is finite and locally uniform. Multiplication by any fixed polynomial in \(u\) and \(e^{\tau u^2}\) remains integrable and decays at infinity. This proves complete-series differentiation and the required payments for \(f'= (e^{\tau u^2}\Phi)'\) and \((uf)'=f+uf'\). It also gives \(f,uf\to0\) at infinity. At zero, the complete series is finite.

On finite intervals, integrate first and then remove the endpoint using these dominators:
\[
 h_0=[f\sin(au)/a]_0^\infty-\frac1a\int_0^\infty f'\sin(au)\,du,
\]
\[
 h_1=[uf\cos(au)/a]_0^\infty-\frac1a\int_0^\infty(uf)'\cos(au)\,du.
\]
Both displayed integral signs are negative. The zero endpoints vanish through \(\sin0=0\) and \(uf(0)=0\), respectively; no reflection shortcut removes a nonzero boundary value. Hence
\[
 |h_0|\le V_0/a,\quad |h_1|\le V_1/a,\qquad
 \nu(a)\le C_{\tau,r}/a.
\]
The \(E_i\) denominators are strictly positive complete moments on \(u>0\), not unknown jet minima. The finite derivative integrals defining \(C_{\tau,r}\) have not been numerically evaluated.

## 3. Fixed cap, not all degrees

For \(N\ge1\),
\[
 \kappa_N-\kappa_{N+1}=\frac{N+2}{2^{N+1}}>0.
\]
Thus \(a\ge\max\{r,C_{\tau,r}/\kappa_{N_{\max}}\}\) implies
\[
 \nu(a)\le\kappa_{N_{\max}}\le\kappa_N\quad(1\le N\le N_{\max}),
\]
which rejects every allowed degree through that cap. The inherited list has minimum tail factor \(\kappa_{32}=35/2^{32}\). The cutoff is a finite source-defined expression, not an acquired numerical height or a claim about the successful finite pilot.

Positive \(d_N\) necessarily requires \(\kappa_N<\nu\). For \(\nu>0\), taking logarithms gives precisely
\[
 N\log2-\log(N+3)>\log(1/\nu).
\]
This is a necessary payment only. It neither overcomes \(F_N\) nor fixes the separate time penalty. A positive rescaling of the source leaves \(\nu,C_{\tau,r}\) invariant and scales \(d_N\) quadratically, preserving its sign.

The theorem concerns the actual theta source with fixed positive radius and finite degree cap, using the unchanged absolute Cauchy tail. Growing degree, shrinking radius, a different envelope/reference or another coefficient are outside this stop. No theta collision follows.

## 4. Gaussian strictness and the quadratic reference

Deleting any nonnegative remainder still leaves \(|D_0|>2b^2r\) necessary. If \(b\ne0\) and it fails, the quadratic reference has zero discriminant at \(t_*=-D_0/(2b^2)\in[-r,r]\). Its spatial critical point is \(x_*=-h_1/b\), which need not lie in the rectangle. This is reference geometry, not a zero of the true transform.

For the issued Gaussian example, \(q=\beta-\tau>2r\) gives the integrable complex-bidisk majorant
\[
 u^j e^{-(q-2r)u^2+2ru}.
\]
The exact Gaussian transform is positive for all real \(T<\beta\). Its jets give
\[
 h_1=-a h_0/(2q),\quad b=(y-1)h_0/(2q),\quad
 D_0=(2-y)h_0^2/(2q).
\]
Set \(y=1+q/r+z\), \(z\ge0\). Since \(q>2r\), \(y>2\), and the time bracket has the exact factorization
\[
 q|2-y|-r(y-1)^2=-q(1+z)-rz^2<0.
\]
At the threshold \(z=0\), it is exactly \(-q\), so endpoint strictness is established. Every degree fails for this source under this necessary time condition even if the remainder were zero. Its actual transform never vanishes, and its same-information curvature is
\[
 H_A^2-HH_{AA}=H^2/[2(\beta-T)]>0.
\]
This is a non-theta adequacy counterexample, not an all-degree temporal-failure theorem for theta.

## 5. Direct comparison, replacement interface and controls

At an actual simple center zero, the inherited remainder gives
\[
 |H_A|\ge |h_1|-r|b|-e_1(r)>0
\]
for sufficiently small \(r\). It uses the same paid information and says nothing about component dominance on larger regions. The exact correlated-strip direct consumer can attain at least the coefficient's conservative uniform floor; that floor need not be the optimized direct distance.

Any eventual spatial Gaussian C01 comparison still uses the accepted compact-uniform derivative convergence. Its required spatial moments are finite because radial weights add only \(e^{ku}\) against a strictly decaying Gaussian in \(u\). No Gaussian constant or curvature sign is transferred to theta.

The replacement interface is valid only if \(U_3,U_4\) genuinely bound the moduli of the fully summed signed complex derivatives uniformly on the same bidisk. Then the same Taylor paths produce revised \(E_i,M_G\), with finite \(g_{mn}\) unchanged. Real-axis samples or a named unknown supremum do not provide such bounds. The right side of (18), including the time penalty, remains unpaid. A replacement is a coefficient revision, not a reinterpretation of the old exact candidate.

Controls use their own sources, observations, moments and actual event balls. A genuine included collision defeats any valid margin; a negative-Laguerre witness or relaxed profile is not thereby a collision. Arbitrary atomic sources need not have the \(L^1\) derivatives used above and need not have decaying Fourier jets, so the integration-by-parts cutoff is not assigned to them. Their own moment-admissible Taylor/row collision screen remains separate. Weighted-square events retain the no-all-real-threshold qualification.

The [small symbolic checker][checker] and [record][record] verify the derivative coefficients, Gaussian cancellations and strict factorization, tail constant and budget identities. They perform no source acquisition and do not certify the analytical dominators or theorem scope. Follow the [result index][results] and [avoid index][avoid], particularly [shared-premise review][a05], [scoped exclusions][a07] and [separate bounds][a12].

[review]: ../../reviews/fixed_coefficient_parameter_geometry/08_FCG_E02_R4_COEFFICIENT_LIMITS_ASSESSMENT_20261030.md
[proof]: 22_FIXED_DEGREE_TAIL_AND_QUADRATIC_TIME_LIMITS_B03_R4_20261030.md
[packet]: ../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R4_COEFFICIENT_LIMITS_ASSESSMENT_20261030.md
[checker]: ../../numerics/fixed_coefficient_parameter_geometry/verify_fcg_e02_r4.py
[record]: ../../numerics/fixed_coefficient_parameter_geometry/fcg_e02_r4_exact_algebra_20261030.json
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[a05]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
