# UAR-04: uniform signed residual increment across every cutoff prefix

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**. Separate same-model derivation, source/comparator audit and adversarial proof review; internal LLM work, no independent specialist human review.

**Outcome: proved in-note, with outward checks of constants.** For the corrected residual and ordinary piecewise integral fixed by [UAR-01][contract],

\[
\boxed{\mathcal B(t)=\sup_{x\in J_t}|\mathcal I_t(x)|
 <3.246\exp\{-13/(16t)\}<2.846\times10^{-7},\quad0<t\le1/20.} \tag{1}
\]

Here J_t=[4pi exp(1/t),4pi exp(2/t)]. Every partial prefix, either frozen cutoff, same-cutoff overlap and both limiting descriptions of a switch are included. This is a bound for the **complete residual increment**, rather than a component or model-error bound. The proof encloses the signed retained expression analytically; it needs no H values, inferred edge data or retained-integral quadrature. No numerical quadrature payment is incurred. The complete error terms and outward arithmetic are paid below.

UAR-04 is Complete at its quantitative uniform-domain gate. UAR-05 is Ready to select and pay a nonzero physical anchor and approximant separation. Equation (1) supplies neither that anchor nor collision exclusion, a total cost advantage, the real bridge, complex exterior or a Newman bound.

Classification under [avoid/01][a01]: an explicit arithmetic upper estimate, not a reformulation of nonvanishing. Read the [result summaries][results] and [patterns to avoid][avoid], especially [controls][controls], [theta bookkeeping][theta], [scope][a07], [normalization][a08] and [signed recombination][a12]. The endpoint identity, source contour and first finite correction are inherited. The new estimating inputs are the signed saddle enclosure, the finite rotating-frequency estimate and the decreasing-height transition-prefix bound. The [review][review] distinguishes them from the inherited representations.

## 1. Complete signed object and error ledger

Keep exactly UAR-01's A, theta, omega<0, corrected f_N=(G_N-Chat_N^an)/A and r_N=H/A-f_N. At a real sector center c, set

\[
L=\log(c/(4\pi))=\kappa/t,\quad1\le\kappa\le2,\quad
S_c=e^{-3L/4-tL^2/16},\quad Z_c=e^{-L/4-tL^2/16}.
\]

Freeze N as either UAR-01 extremal cutoff; do not differentiate the floor. Let

\[
\widehat r_N=K_N/A+\widehat e_{edge,N},\quad
r_N=\widehat r_N+d_{AB,N}+d_{edge,N},\quad
Z_v=e^{-i\theta}(v-i v_x/\omega).
\]

K_N is the prescribed signed finite gamma/heat correction of [UAR-02][finite]. The edge model is exactly [UAR-03's][edge] bounded double integral, with common limits V_t=S_t=2sqrt(2/t), descending contour and the analytic reflected channel. Assemble

\[
\widehat\Xi_t(x)=Z_{\widehat r_{N(x)}}(x)
 -Z_{\widehat r_{N(a_t)}}(a_t)
 +\sum_{a_t<\xi_n\le x}Z_{h_n}(\xi_n).                   \tag{2}
\]

The sum has its **positive** sign. It belongs to the ordinary piecewise integral; it is not subtracted to form a compensated endpoint quantity. Initially coincident switches are owned by the initial right chart and omitted. At a left-limit terminal description omit its coincident final switch.

The complete endpoint allowance is

\[
|\mathcal I_t(x)|\le |\widehat\Xi_t(x)|
 +\Delta_{AB}(x)+\Delta_{AB}(a_t)
 +9\epsilon_x+9\epsilon_{a_t},                            \tag{3}
\]

where Delta_AB(c)=160 exp(a_*/t)/c^2, a_*=kappa(4-kappa)/16, and epsilon_c=1000 Z_c exp(-3.99L). We estimate (2) as a signed expression first, then apply a conservative majorant. No favorable cancellation between its finite and edge blocks or between different crossings is assumed. The crucial leading edge cancellation and the signed heat moment are retained *inside* the contour before a norm.

For clarity, the widened-disk contour argument below bounds the retained compact edge directly. It therefore supplies its endpoint enclosure without paying epsilon once to infer the model from the exact edge. Only (3)'s one exact-minus-model payment is necessary. Even the redundant doubled allowance 18epsilon per endpoint is affordable; we use it in the final rounded ledger so the conclusion also survives that alternative proof organization.

## 2. Signed saddle enclosure of the retained edge

Use the auxiliary physical disk |z-c|<=rho=1/4, leaving UAR-01's original residual contract unchanged. Write z=X+iy. The two reflected real-parameter channels have sigma=(1-y)/2 and (1+y)/2, both in [.375,.625]. Set

\[
T=X/2+\pi t/8,\quad a=\sqrt{T/(2\pi)},\quad q=N+1/2,
d=q-a,\quad\zeta=d+(1+i)r,\quad u=\sigma+\sqrt t\,v.
\]

For either original frozen N on this auxiliary disk, |d|<.500001, a>22025 and |u|<4 on the retained v interval. The a-variation over rho is less than rho/(8pi·22025); together with the original cutoff-extrema displacement it stays within that d allowance. Gamma poles and logarithmic cuts remain far away.

Factoring the exact contour integrand at its saddle gives

\[
M(iT+u)=M_0(iT)e^{u(\log a+i\pi/4)+\eta},\quad
|\eta|\le\frac1{2T}+\frac{3|u|}{2T}+\frac{u^2}{4(T-3)}
 <1.7/a^2,                                                \tag{4}
\]

and the remaining small exponent is

\[
h=-u\log(1+\zeta/a)-i2\pi a^2
 [\log(1+\zeta/a)-\zeta/a+\zeta^2/(2a^2)],\quad
B_1=-u\zeta-i(2\pi/3)\zeta^3.                             \tag{5}
\]

The gamma estimate in (4) is a bounded horizontal Taylor/Stirling estimate, using the safe remainder from UAR-03. It is not applied on an infinite left heat tail. The heat phase exp(-i pi sqrt(t)v/4) cancels its counterpart in exp(u i pi/4), leaving exp(i pi sigma/4). Thus the first signed Gaussian moment in B_1 is **sigma**, since E[v]=0, rather than E[|u|].

On the retained rectangle, |zeta|/a<.001 and |h|<.65. The opening bound uses |zeta|<=.50001+sqrt(2)S_t<18.389 and a>.9999999999exp(10). As t decreases the relevant t^(-j/2)exp(-1/(2t)), j<=3, decrease; larger kappa increases a. The logarithm series yields

\[
|h-B_1/a|\le[2|\zeta|^2+(\pi/2)|\zeta|^4]/(.999a^2),\quad
|h|\le[4|\zeta|+(2\pi/3)|\zeta|^3]/(.999a).               \tag{6}
\]

The descending saddle kernel K_d=(1+i)exp(i2pi zeta^2)/(exp(i pi w)-exp(-i pi w)), w=q+(1+i)r, has denominator modulus >=2. With H=r+d/2,

\[
|K_d|\le(\sqrt2/2)e^{\pi d^2}e^{-4\pi H^2},\qquad
|\zeta|^2=2H^2+d^2/2.                                    \tag{7}
\]

For D=.50001 define

\[
\begin{aligned}
m_0&=(\sqrt2/4)e^{\pi D^2}<.777,\\
m_2&=1/(4\pi)+D^2/2,\\
m_4&=3/(16\pi^2)+D^2/(4\pi)+D^4/4,\\
m_6&=15/(64\pi^3)+9D^2/(32\pi^2)+3D^4/(16\pi)+D^6/8.
\end{aligned}
\]

These are the normalized moments of (7); E|zeta|<=sqrt(m2) and E|zeta|^3<=sqrt(m2 m4). After the signed heat integral, the first correction costs

\[
\frac{m_0}{a}[.625\sqrt{m_2}+(2\pi/3)\sqrt{m_2m_4}]
 <.391/a.                                                \tag{8}
\]

Put H2=16m2+(16pi/3)m4+(4pi^2/9)m6. Equations (6) and |exp(h)-1-h|<=exp(.65)|h|^2/2 give the integrated second-order cost

\[
\frac{m_0}{a^2}\left[
 \frac{2m_2+\pi m_4/2}{.999}
 +\frac{e^{.65}H2}{2(.999)^2}\right]<3.57/a^2.             \tag{9}
\]

The corresponding exponential-kernel mass is <.777. Equation (4) therefore pays the true gamma prefactor by <1.322/a^2. The complete central second-order cost is <5/a^2.

### Leading profile, orientation and all added model tails

The full descending kernel integral satisfies

\[
\int_{+\infty}^{-\infty}K_d(r)\,dr
 =(-1)^{N-1}e^{i\pi/8}F(2d),\quad F=C_0.                 \tag{10}
\]

One verification uses [Polymath Proposition 6.2][polymath] only for a limiting identity: fix real d in (-1/2,1/2), put a_j=j+1/2-d and N=j, and let j increase. Gaussian domination of the exact contour, or UAR-03's all-r bound, justifies its leading limit. The published expansion at its **natural** cutoff has the same limit. Factor the common parity (-1)^N from the denominator. Both sides of (10) are entire in d, with Gaussian domination on compact d sets, so analytic continuation gives (10) through the two removable points and the slightly enlarged d range. No published natural-cutoff remainder is assigned to the alternate frozen integer.

The constant saddle factor is a^(-iT)exp(iT/2)=U exp(-i pi/8), so (10) restores the opposite phase. After adding the reflected channel, the leading term is exactly **minus** the printed correction exp(-i pi y/8)Chat_N(X). This fixes its orientation, parity and sign.

Extending the retained leading and linear kernel to the full r,v lines adds **model** tails, distinct from the exact edge tails already paid by UAR-03:

- Heat model tails: E[u 1_(|v|>V)]=sigma P(|v|>V). Their cost is at most P(|v|>V)(m0+.391/a)<exp(-V^2)<=exp(-4L).
- Contour model tails: for |r|>=S_t>=12.649, |K|<1.552exp(-12r^2), |zeta|<1.455|r| and |E B1|<7|r|^3. Their two-sided Mills payment is bounded by 3.104exp(-12S_t^2)[1/(24S_t)+(7/a)(S_t^2/24+1/288)]<exp(-12S_t^2)<=exp(-48L).

The bracket decreases as t falls; a^2<=1.001exp(L). Both model tails together are <2.002exp(-3L)/a^2<2e-26/a^2. Consequently the compact edge minus its leading printed profile, per channel in P=exp(t pi^2/64)|M0(iT)| units, has the complete bound

\[
.391/a+6/a^2.                                            \tag{11}
\]

### Analytic correction and the actual normalizer

Equation (10) also gives |F|<.777 and |F'|<2.22 on the required thin complex profile strip. For d=alpha+i beta, replace H in (7) by r+(alpha+beta)/2 and d^2 by (alpha-beta)^2; exactly the same modulus and |zeta|^2 identities hold. Here |alpha-beta|<.50001, including the original extrema displacement and the rho/(8pi·22025) complex a variation. Differentiating (10) under the integral gives |F'|<=2pi m0 sqrt(m2)<2.22. The reflected profile has the same bound, so the analytic D and B profiles inherit these constants; no Re/Im operation is imposed on a complex argument.

Let T_±=(c±rho)/2+pi t/8, a_-=sqrt(T_-/(2pi)), W=(T_+/T_-)^(3/2), and

\[
J=\frac{3(.777)}{4T_-}+\frac{.777}{T_-^2}
  +\frac{2.22+2.22/T_-}{4\pi a_-}.                        \tag{12}
\]

The derivative of exp(pi z/8)Chat_N^an(z) has this slow bracket. Integrating along the vertical segment pays the complete printed-to-analytic conversion by 2.000002 rho W J·P/|A(z)|. The coefficient 2P follows directly from the exact M0(iT) identity in [old Note 20][old20], not from a separate norm of a large physical correction.

Direct subtraction of the two alpha channels, with beta=alpha(1+t alpha'/2), gives

\[
|\alpha(s)-\alpha(1-s)+i\pi/2|<7.01/c,\quad
|\beta(s)-\beta(1-s)+i\pi/2|<8.061/c,
\quad|A_z/A+\pi/8|<3/c.                                  \tag{13}
\]

For example expand log(s) and log(1-s) around log(X/2)∓i pi/2; the log difference costs <1.001/c and the rational terms <6.001/c, whose sum is <7.01/c. The beta correction costs <1.051/c, using t|alpha|<=1.05 and |alpha'|<1.000001/c. Thus |A_z/A|<.4 on the auxiliary disk, rather than a bound growing as L/4. The inherited real prefactor formula from [old Note 22][old22], evaluated with rho, gives P/A(t,X)<1.001Z_c; vertical movement costs <exp(.1). Hence

\[
P/|A(t,z)|<1.107Z_c.                                    \tag{14}
\]

Both reflected errors in (11), the conversion (12) and (14) now give

\[
\sup_{|z-c|\le1/4}|\widehat e_{edge,N}(z)|
 <1.107Z_c[2(.391/a_-+6/a_-^2)+2.000002\rho WJ]
 <.97 S_c.                                               \tag{15}
\]

The [outward record][record] uses a_- and the exact factor exp(L/2)/a_- in both leading inverse-a terms and the conversion; their monotone opening reserve proves the last ceiling. The model is holomorphic and real symmetric; only now apply real Schwarz-Pick. Since rho|omega(c)|>rho L/4.001>1, its coupled rotating factor is one:

\[
|Z_{\widehat e_{edge,N}}(c)|<.97S_c.                      \tag{16}
\]

## 3. Finite correction: the two rotating weights add to two

On the real axis let q_n=g_n(s)/A, ell=log n and k_n=q_n chi_n. Its exact logarithmic derivative is

\[
q_n'/q_n=i\nu_n+d_n,\quad\nu_n=\omega+\ell/2,\quad
d_n=it\ell\alpha'(s)/4,\quad|d_n|<.253/c.
\]

The full-cutoff bound ell<=L/2+.001 and |omega|>L/4.001 imply |nu_n/omega|<=1, including the alternate integer. In the rotating map of k_n+conjugate(k_n), the main two channel weights are 1+nu_n/omega and 1-nu_n/omega. They are nonnegative and sum to two. Consequently

\[
|Z_{k_n+\bar k_n}|
 \le2|q_n|\left[|\chi_n|
 +\frac{|d_n\chi_n|+|\chi_{n,x}|}{|\omega|}\right].         \tag{17}
\]

This retains the channel phase relation; the independent derivative triangle would lose it. UAR-02 proves |chi_n|<.5/c. Explicit differentiation with |s|>.499c, |alpha'|<1.01/c, |alpha''|<2.1/c^2 gives

\[
c^2|\chi_{n,x}|\le\frac1{12(.499)^2}
 +1.05(.05/4+1.05^2/8)+\frac{1.01^2(.0525)}8<.5.          \tag{18}
\]

The full one-channel real mass is <7exp(a_*/t), including the extra extremal mode. Summing (17) yields

\[
|Z_{K_N/A}(c)|<7.001e^{a_*/t}/c<.558 S_c,\quad
e^{a_*/t}/c=S_c/(4\pi).                                  \tag{19}
\]

Equations (16),(19) enclose the retained signed endpoint by <1.528S_c. We use C=1.53 below. The finite Gaussian tails, true gamma remainder and derivative of A in q_n are all included. No fixed-mode heat-weight limit replaces modes near N.

## 4. Every transition prefix and the complete theorem

The earlier UAR-03 bound |Z_hn(xi_n)|<3Z_(xi_n)/n^2 can be sharpened when summed, since its height envelope decreases. Fix t, put delta=t/16 and

\[
U_x=\sqrt{x/(4\pi)+\delta},\quad U_0=\sqrt{e^{1/t}+\delta},
\quad \bar S(v)=\exp[-(t\log^2(v^2-\delta)+12\log(v^2-\delta))/16].
\]

At a crossing its allowance is <F(n)=3 Sbar(n)/n. Both F and Sbar decrease, and

\[
-\bar S'(v)=\bar S(v)\frac{(t\log(v^2-\delta)+6)v}{4(v^2-\delta)}
 \ge\frac74\frac{\bar S(v)}v.
\]

If the included crossings are n_first through n_last, then n_first>U0, n_last<=Ux. A decreasing-integrand comparison pays the first discrete term separately:

\[
\sum |Z_{h_n}|\le F(n_{first})+\int_{n_{first}}^{n_{last}}F(v)\,dv
 <.000137S_0+\frac{12}{7}(S_0-S_x).                       \tag{20}
\]

The bound includes a singleton prefix; for no crossings the right side is nonnegative. The endpoint ownership conventions only remove a coincident integer, preserving the inequalities. The first-term ceiling is uniform because 3/U0<3exp(-10)<.000137. This is an allowance, not a lower bound on actual jumps or a sampled cancellation law.

Apply (16),(19),(20) to the already assembled (2). Since C=1.53<12/7,

\[
|\widehat\Xi_t(x)|
 <(C+12/7+.000137)S_0+(C-12/7)S_x<3.245S_0.             \tag{21}
\]

There is no sum of local increment radii: same-N endpoints telescope exactly. Both component errors decrease with c. Even with the deliberately redundant doubled edge payment described after (3),

\[
\mathcal B(t)<3.245S_0+2\Delta_{AB}(a_t)+36\epsilon_{a_t}
 <3.246S_0,\qquad S_0=e^{-13/(16t)}.                     \tag{22}
\]

Indeed Delta_AB/S_c=(10/pi^2)exp(-L)<2.1e-9 and epsilon_c/S_c=1000exp(-3.49L)<5e-28. At t=1/20 the final outward ceiling is 2.844874972032e-7. All scalar maxima follow from monotonicity at L>=20, t<=.05; no finite height mesh substitutes for this proof.

## 5. Comparator, interpretation and validation

The strongest applicable inherited source comparator uses the **corrected** residual, Polymath Proposition 6.1's actual finite-mode relative allowance, its factorized Corollary 6.4 edge error, slow P/A normalization and optimized analytic radii. It is stronger than the literal old Note 22 scalar envelope and stronger than an unconverted S04 raw-residual allowance. The finite allowance is exp[(t^2|alpha-log n|^2/8+t/4+1/6)/(T-3.33)]-1; it must not be weakened to the later .626 majorant. Same-norm comparison must also include analytic Chat conversion, cutoff payments and both endpoint errors.

For reference, the stronger stated Proposition 6.3 error boxes, before the later 1.24 simplification, assign per real channel at least .397·9^(1/2)P/a. Both channels therefore assign >=2.382(P/A)/a, before their other nonnegative payments. On a real center P/A>.999Z_c, by direct substitution in m0; the logarithmic error is bounded by (3L+10)/(.99c)<1.2e-8 and decreases. Optimizing the analytic radius cannot lower the generic rotating multiplier below one. At x=a_t+1, S_x/S_0>.999999 (since -d log S/dx=(tL+6)/(8x)<2/c there); hence any two-endpoint ledger retaining these independent published edge error boxes assigns >4.75S_0 to this ordinary prefix, before finite errors, conversion or transitions. The new complete coefficient 3.246 is <.684 of that assigned floor. This is a **scoped allowance comparison for that source-error-box class**, not an actual-error lower bound or a proof that every phase-aware refinement of the inherited source loses. In particular the proof of the source theorem can itself be sharpened; no optimal direct physical-consumer or total-cost advantage is claimed. The principal UAR-04 gate met here is the first explicit complete theorem for every ordinary prefix on the declared uniform J_t.

The [primary record][record] pins the exact mathematical sources and checks 192/256-bit outward reserves, frequency-weight and Gaussian-moment identities, prefix signs/ownership premises, and invalid-sector/missing/stale-source guards. The [separate same-model review][review] includes a fresh 192-bit replay with the same checker. Written analysis proves the uniform estimates; precision, hashes and replay counts do not prove them and do not make this independent specialist validation.

The [fresh own-source controls][control-record] reject the five existing event boxes and retain the separate Euler negative-Laguerre witness in unchanged downstream consumers. The historical producer date is preserved separately from this execution. Finite-prime and weighted-square controls lack the unchanged full normalized theta coefficient/reflection data. Shape, reflected and positive-primitive controls lack this theta square expansion and matching completed contour. Euler deformations change the level/coefficients; polynomial, counter-kernel and moving-wall controls lack the arithmetic source premise. The generic rotation identity and small approximation error distinguish none of these by themselves. No theta constant is substituted into another source; no analytic-only control receives an invented event height.

**Decision:** UAR-04 is Complete with a usable complete uniform increment. UAR-V1's increment instance has the declared same-model review and source-control scope. UAR-05 is Ready for a specified paid anchor and strict approximant-separation margin. UAR-06 waits for that physical result and its review. The source return still contains Z_Q(a_t), the full signed variation of f_N and its transitions; (1) does not assert that their combination is nonzero. No manuscript change, snapshot, commit, coverage extension or Newman claim is made.

[contract]: ../../notes/07_UAR01_CORRECTED_RESIDUAL_AND_TRANSITION_CONTRACT_20261019.md
[finite]: 08_UNIFORM_FINITE_GAMMA_HEAT_REMAINDER_20261019.md
[edge]: 09_UNIFORM_COHERENT_EDGE_AND_CUTOFF_MATCHING_20261019.md
[old20]: ../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md
[old22]: ../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md
[polymath]: https://arxiv.org/html/1904.12438v2#S6.SS2
[record]: ../numerics/UAR04_UNIFORM_SIGNED_INCREMENT_20261019.json
[control-record]: ../numerics/UAR04_SOURCE_CONTROLS_20261019.json
[review]: ../reviews/10_UAR04_UNIFORM_SIGNED_INCREMENT_INTERNAL_REVIEW_20261019.md
[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
