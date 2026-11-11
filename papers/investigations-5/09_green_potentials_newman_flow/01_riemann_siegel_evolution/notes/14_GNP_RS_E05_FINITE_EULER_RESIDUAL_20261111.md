# GNP-RS-E05 r1 — finite Euler reference and exceptional-center residual

11 November 2026, America/New_York. Prepared for Edward Baker with
substantial OpenAI Codex LLM assistance, **gpt-6.1-sol, effort ultra**
by explicit execution dispatch. The exceptional-center proof uses the
twisted-moment route independently derived by the dispatched Sol/ultra
assessor.

**Status: proved in-note from named inherited inputs**, with a
[separate internal assessment][review] that includes proof-route contributions.
This is the
return to the [frozen E05 r1 request][request]. The estimates concern
the frozen finite Euler reference and the complete theta field. The
every-center Green margin remains open. Use the [result index][results],
[heat-flow cluster][r11], [avoidance index][avoid] and
[collision controls][controls]. The transfer and mean law are acquisition
estimates under [avoid01][a01]. The exceptional-center result is a scoped
obstruction to the separate nonnegative residual payment under
[avoid07][a07] and [avoid12][a12].

## 1. Exact prime calibration and relative log transfer

Keep [E01][e01], [B02][b02] and [E04][e04]'s notation:
\(L_X=\log(X/(4\pi))\), \(\lambda=c/L_X\), \(1/2\le c\le1\), with
\(\lambda\) fixed throughout the spatial integral. Use the complete
\(V_\lambda=H_\lambda/C_-\), the real two-arm formula
\(S_\lambda=A_\lambda+e^{i\phi_\lambda}\bar A_\lambda\)
of E04 §1, and its correction and residual. Write
\(W_X=[X-R_X,X+R_X]\), \(d\mu_X=K(x-X)\,dx\) on \(W_X\), and
\(q_X=\mu_X(W_X)\). Retain the exact tail \(T_X\) and allowance
\(C_*/L_X\). Fix a prime cutoff \(P\ge2\) and put
\[
 \sigma_c=\tfrac12+\tfrac c4,\qquad
 E_P(x)=\prod_{p\le P}\left(1-p^{-\sigma_c}
                                  e^{i\nu_\lambda(x)\log p}\right)^{-1},
 \qquad
 S_P^{\rm ref}(x)=E_P(x)+e^{i\phi_\lambda(x)}\overline{E_P(x)} .
\]
Here \(\nu_\lambda(x)=x/2+\pi\lambda/8\) and
\(\phi_\lambda(x)=2\Theta(\lambda,x)\). The reference and its inverse
are bounded on the real line by constants depending on \(P\) uniformly
over the frozen band. This follows from \(p^{-\sigma_c}\le p^{-5/8}<1\).
The same bounds give uniform bounds on \(\log|E_P|\) and on the first
derivatives in \(x\) or \(\lambda\) of \(E_P\) and its inverse, with
\(c\) fixed.

For \(K(t)=1/[16\cosh(\pi t/8)]\), its Fourier integral is
\(\widehat K(\omega)=1/[2\cosh(4\omega)]\). Indeed the contour
rectangle of height \(i\pi\) for \(e^{iaz}/\cosh z\) gives
\((1+e^{-\pi a})\int_{\mathbb R} e^{iau}/\cosh u\,du
=2\pi e^{-\pi a/2}\), using the pole \(i\pi/2\) and vanishing
vertical integrals as the width tends to infinity. Rescaling gives
the stated transform. At \(\omega=(\log n)/2\) it equals
\(n^{-2}/(1+n^{-4})\). The finite-prime Euler logarithms have
uniformly absolutely convergent expansions, so
\[
 \int_{\mathbb R}K(x-X)\log|E_P(x)|\,dx
   = P_{c,\lambda}^{(\le P)}(X)
   := \sum_{p\le P}\sum_{k\ge1}
     \frac{p^{-k(5/2+c/4)}}{k(1+p^{-4k})}
       \cos\!\left(k\nu_\lambda(X)\log p\right).
 \tag{E05.1}
\]
The same fixed \(\lambda\) and \(c\) are used on both sides. This
truncates the primes and retains all their powers. The omitted
prime terms have absolute sum at most \((2/3)P^{-3/2}\) by
E01 (E5), since their prime powers exceed \(P\).
The finite-window reference error is \(O_P(X^{-4})\), by the
bounded reference log and the kernel tail of B02 §2.

Define the exact relative residual
\[
 R_P(X,c)=\int_{W_X}\frac{|V_\lambda-S_P^{\rm ref}|^2}{|E_P|^2}
                    \,d\mu_X.
\]
Apply E04 (E04.2) with \(V_\lambda/E_P\) and \(S_P^{\rm ref}/E_P\)
and any fixed \(\delta>0\). For \(b_\delta=(\delta+\sqrt{\delta^2+4})/2\)
the regularized log of the latter is
\[
 \tfrac12\log(|S_P^{\rm ref}/E_P|^2+\delta^2)
 =\log b_\delta+
   \Re\log\!\left(1+e^{i\phi_\lambda}
                      \frac{\bar E_P}{b_\delta^2 E_P}\right).
\]
The coefficient of \(e^{i\phi_\lambda}\) has modulus
\(b_\delta^{-2}<1\) and bounded derivative depending on \(P,\delta\).
Thus the power series and integration by parts from E04 §3
give \(O_{P,\delta}(1/L_X)\) for the integrated phase term,
including both endpoints. Jensen bounds the integrated relative
error term by \((q_X/2)\log(1+R_P/(q_X\delta^2))\).
Restoring \(\log|E_P|\) and using (E05.1), the exact critical-log
tail and E01 gives a uniform bound for all sufficiently large
\(X\) and all \(c\) in the band:
\[
 \boxed{\begin{aligned}
 J_\lambda(X)\le{}&
 P_{c,\lambda}^{(\le P)}(X)-P_{c,\lambda}(X)
 +q_X\log b_\delta+
 \frac{q_X}{2}\log\!\left(1+\frac{R_P(X,c)}{q_X\delta^2}\right)\\
 &+T_X+\frac{C_*}{L_X}
    +\frac{C_{P,\delta}}{L_X}+D_P X^{-4}.
 \end{aligned}}
 \tag{E05.2}
\]
The constants \(C_{P,\delta},D_P\) can be taken nonnegative.
The transfer requires no positive floor for the exact field or
the reflected reference. Only the unreflected finite product is
divided out.

## 2. Exact relative-residual mean at \(c=1\)

For this section use the auxiliary variable \(u\) and time \(1/L_u\)
as in [E03][e03] §§1–3. Abbreviate the corresponding weight, phase,
frequency, unreflected arm and Euler product by \(w_n(u),\phi(u),
\nu(u),A(u),E(u)\). The Euler product exponent is \(\sigma=3/4\).
Write \(D=\prod_{p\le P}p\) and
\[
 Q(u)=E(u)^{-1}=\sum_{d\mid D}\mu(d)d^{-3/4}e^{i\nu(u)\log d},
 \qquad B(u)=A(u)Q(u)-1.
\]
Here \(\mu\) is the Möbius function. The coefficient of
\(e^{i\nu(u)\log k}\) in \(B\) is
\[
 b_k(u)=\sum_{\substack{d\mid D,\ d\mid k\\ k/d\le N_u}}
                  \mu(d)d^{-3/4}w_{k/d}(u)-\mathbf1_{k=1}.
\]
The coefficient at \(1\) vanishes identically. For \(k>1\),
\(\sup |b_k|\) and total variation on \([T,2T]\) are
\(O_P(k^{-5/8})\). Each summand uses E03's decreasing weights
\(w_n\le n^{-5/8}\) after its single activation at \(u=4\pi n^2\).
Summing variation over its jump and decreasing portion gives the
stated bound. For fixed \(k>1\), all eligible divisors are active
eventually and the coefficient tends uniformly on the dyadic
interval to \(k^{-3/4}\mathbf1_{(k,D)=1}\) by the divisor sum
\(\sum_{d\mid(k,D)}\mu(d)\).

The diagonal in the mean of \(|B|^2\) therefore tends to
\[
 \mu_P:=\sum_{\substack{k>1\\(k,D)=1}}k^{-3/2}
   =\zeta(3/2)\prod_{p\le P}(1-p^{-3/2})-1
 \tag{E05.3}
\]
by the summable majorant \(O_P(k^{-5/4})\). For \(k\ne l\),
the E03 first derivative estimate on
\(\nu(u)\log(k/l)\) gives \(O(1/|\log(k/l)|)\) for the
unweighted partial integral. Integrating by parts against
the bounded-variation amplitude \(b_kb_l\) pays all jumps
and endpoints by its supremum and variation. Summing
\(O_P((kl)^{-5/8}/|\log(k/l)|)\) for \(k,l\le D N_{2T}\)
as in E03 §2 gives the averaged cost \(O_P(T^{-5/8}(1+\log T))\).
Thus the dyadic mean of \(|B|^2\) tends to \(\mu_P\).

The complete reflected reference residual without the approximation
error has the squared relative modulus
\[
 \left|\frac{S_{1/L_u}(u)-S_P^{\rm ref}(u)}{E(u)}\right|^2
 =2|B(u)|^2+
   2\Re\!\left[e^{-i\phi(u)}B(u)^2\frac{\bar Q(u)}{Q(u)}\right].
\]
The multiplier \(\bar Q/Q=\bar Q E\) admits a uniformly absolutely
convergent expansion in \(e^{i\nu(u)\log r}\) for positive rational
\(r\): expand \(E\) over integers with prime factors at most \(P\)
and multiply by the finite conjugate polynomial \(\bar Q\).
Approximate the multiplier by any fixed finite subseries with
uniform error \(\varepsilon\); its effect on the dyadic cross term
is bounded by \(2\varepsilon\) times the dyadic mean of \(|B|^2\).
For each fixed \(r\) in the subseries and \(k,l\le D N_{2T}\),
the phase \(-\phi(u)+\nu(u)\log(klr)\) has second derivative
of fixed sign with magnitude \(\asymp 1/T\) on \([T,2T]\)
for large \(T\). In fact \(\phi''(u)=1/(2u)\) at the auxiliary
time, and the \(\nu''(u)\log(klr)\) term is
\(O_{P,r}(1/(T^2\log T))\). E03's split at first derivative
magnitude \(T^{-1/2}\) gives \(O_{P,r}(\sqrt T)\) for every
unweighted partial integral. The amplitude variation bound
then gives averaged cost
\(O_{P,r}(T^{-1/2}(\sum_{k\le D N_{2T}}k^{-5/8})^2)
=O_{P,r}(T^{-1/8})\).
Take \(T\to\infty\) for the finite subseries, then
\(\varepsilon\downarrow0\). The reflected cross term has mean zero.

The complete correction and residual divided by \(E\) are
\(O_P(u^{-1/4})\) by E04 §1. The relative main expression is
\(O_P(u^{3/16})\), so the pointwise cost in its squared modulus
is \(O_P(u^{-1/16})\). Hence the mean of the auxiliary complete
relative squared residual tends to \(2\mu_P\).

Return to the original fixed \(1/L_X\) in each \(W_X\).
For \(x\in W_X\), E03 §3 gives a time difference
\(O(R_X/(XL_X^2))\). The same section bounds the normalized
complete arm sum by \(O(x^{7/32})\) and its time derivative
by \(O(L_x^2x^{7/32})\) at intermediate times. The Euler
reference and inverse have bounded modulus and time derivative
except for the reflected phase derivative \(O(L_x)\), which
is already included in the latter arm estimate. Thus
\((S_\lambda-S_P^{\rm ref})/E_P\) has the same size and
time-derivative bounds with constants depending on \(P\).
Paying the full \(O_P(x^{-1/4})\) error at each endpoint as in
E03 gives \(O_P(R_X X^{-9/16}+X^{-1/32})\) for the
fixed-time squared-residual comparison on \(W_X\).
The auxiliary square is \(O_P(x^{3/8})\), so the two edge
and kernel-mass estimates of E03 §3 apply without alteration.
The kernel mass \(1/2\) yields the exact limit
\[
 \boxed{\lim_{T\to\infty}\frac1T\int_T^{2T}R_P(X,1)\,dX=\mu_P.}
 \tag{E05.4}
\]
Here \(\mu_P\to0\) by domination by \(\sum k^{-3/2}\).
All limits in height use fixed \(P\).

### Consequence at \(c=1\) in dyadic density

Let \(m_*>0\) be the unchanged margin. Choose fixed \(\delta>0\)
so \(q_X\log b_\delta\le m_*/5\), possible since \(q_X\le1/2\)
and \(\log b_\delta\downarrow0\). Choose fixed \(P\) large enough
that the absolute prime tail is at most \(m_*/5\).
If \(R_P\le r=\delta^2m_*/5\), the logarithmic payment is at
most \(r/(2\delta^2)=m_*/10\). The remaining errors of
(E05.2) together are eventually at most \(m_*/5\) for each
fixed \(P,\delta\). Hence for sufficiently large \(X\) the set
\(\{X:J_{1/L_X}(X)\ge m_*\}\) lies in \(\{X:R_P(X,1)>r\}\).
Markov and (E05.4) give an upper dyadic density at most
\(\mu_P/r\). Taking arbitrarily large fixed \(P\) after the
height limit proves
\[
 \lim_{T\to\infty}\frac{1}{T}\big|\{X\in[T,2T]:
                J_{1/L_X}(X)\ge m_*\}\big|=0 .
 \tag{E05.5}
\]
This statement gives no rate and covers the \(c=1\) slice only.

## 3. Unbounded residual at arbitrarily high centers

First prove unboundedness of the exact complete quadratic moment
\(M(X,1)=\int_{W_X}|V_{1/L_X}(x)|^2\,d\mu_X\) from E03.
Fix coprime positive integers \(a,b\), and set \(s=\log(a/b)\).
Twist the auxiliary height mean of \(|V_{1/L_u}(u)|^2\)
by \(e^{ius/2}\). For the two equal arm squares the same-arm
phase is \(\nu(u)\log(n/m)+us/2\). A nonresonant pair has
\[
 |\log(an/(bm))|\ge \frac{|an-bm|}{\max(an,bm)}
                   \gg_{a,b} T^{-1/2}.
\]
The derivative perturbation
\((\nu'-1/2)\log(n/m)=O(1/(T\log T))\) preserves this
lower bound up to a constant, and the derivative is monotone
on the active interval. Hence each partial integral is
\(O_{a,b}(\sqrt T)\). E03's amplitude variation and weight
sum give an averaged cost \(O_{a,b}(T^{-1/8})\) for all such
pairs. The resonant pairs \(n=bj,m=aj\) have residual phase
\(\pi\log(b/a)/(8L_u)\) tending to zero. Each eventually
uses all of \([T,2T]\). Their amplitudes tend to
\((ab)^{-3/4}j^{-3/2}\), dominated by
\((ab)^{-5/8}j^{-5/4}\). The two arm squares thus give limit
\(2\zeta(3/2)(ab)^{-3/4}\). The reflected cross terms retain
the E03 second derivative bound because the twist is linear
in \(u\). The bound \(O(T^{-1/8})\) and complete squared
approximation error still apply.

The E03 fixed-time comparison is unchanged in absolute value.
With \(t=x-X\) the twist in the centered moment becomes
\(e^{ixs/2}e^{-its/2}\). On the common interior of the dyadic
interval the Fubini weight differs from
\(\int_{\mathbb R}K(t)e^{-its/2}\,dt\) by \(O(T^{-4})\),
since it includes all \(|t|\le R_T\). The boundary cost is
unchanged from E03 by \(|e^{-its/2}|=1\). Thus
\[
 \lim_{T\to\infty}\frac1T\int_T^{2T}e^{iXs/2} M(X,1)\,dX
      =2\zeta(3/2)(ab)^{-3/4}\widehat K(s/2).
 \tag{E05.6}
\]
No equidistribution rate or estimate uniform in \(a,b\) is used.

Fix a second prime cutoff \(U\), independent of the reference \(P\).
Use torus coordinates \(z_p\) for \(p\le U\) with probability Haar
measure \(dz\), and define
\[
 E_U(z)=\prod_{p\le U}(1-p^{-3/4}z_p)^{-1},\quad
 \tau_p(t)=e^{it\log p/2},\quad
 C_U=\zeta(3/2)\prod_{p\le U}(1-p^{-3/2}),
 \quad F_U(z)=2C_U\int_{\mathbb R}K(t)|E_U(z\tau(t))|^2\,dt .
\]
The function \(F_U\) is continuous because the finite product is
bounded. A character \(\chi(z)=\prod_{p\le U}z_p^{\ell_p}\)
corresponds to \(a/b=\prod_{p\le U}p^{\ell_p}\) in lowest terms.
Expanding the absolutely convergent Euler product inside
\(\int\chi(z)|E_U(z\tau(t))|^2\,dz\), orthogonality keeps
\(n=bj,m=aj\), with \(j\) supported on primes at most \(U\).
It gives \((ab)^{-3/4}e^{-its/2}\prod_{p\le U}(1-p^{-3/2})^{-1}\).
Thus the right side of (E05.6) is exactly
\(\int\chi(z)F_U(z)\,dz\). On the trajectory
\(z_p(X)=e^{iX\log p/2}\), the unweighted mean of each
nonconstant character tends to zero by integrating its nonzero
frequency. Unique factorization ensures the frequency is nonzero.

For fixed \(U\), use the nonnegative finite trigonometric polynomial
\[
 W_N(z)=\prod_{p\le U}\frac1N\left|\sum_{j=0}^{N-1}z_p^j\right|^2 .
\]
Each factor has Haar mean one, and outside
\(|\arg z_p|<\eta\) it is at most
\(1/(N\sin^2(\eta/2))\). The product therefore concentrates
at \(z=1\) by a union bound and continuity, so
\(\int W_N F_U\,dz\to F_U(1)\).
For every fixed \(U,N\), (E05.6) and the character means give
\[
 T^{-1}\int_T^{2T}W_N(z(X))M(X,1)\,dX\longrightarrow\int W_N F_U\,dz,
 \qquad
 T^{-1}\int_T^{2T}W_N(z(X))\,dX\longrightarrow1 .
\]
If \(M(X,1)\le H\) eventually, nonnegativity would imply
\(F_U(1)\le H\) for every fixed \(U\), taking the height limit
before the concentration limit.

In fact \(F_U(1)\) grows without bound. For
\(|t|\le1/\log U\) and \(p\le U\),
\(\cos(t\log p/2)\ge7/8\). With \(r=p^{-3/4}<1\) this gives
\(|1-r\tau_p(t)|^2\le1-(3/4)r\) and
\(|E_U(\tau(t))|^2\ge\exp((3/4)\sum_{p\le U}p^{-3/4})\).
The harmonic sum up to \(\lfloor U\rfloor\) is bounded above
by \(\prod_{p\le U}(1-1/p)^{-1}\). Taking logs and paying the
summable higher powers \(O(\sum p^{-2})\) gives
\(\sum_{p\le U}1/p\ge\log\log U-O(1)\).
Since \(p^{1/4}\ge4\) above a fixed cutoff,
\(\sum_{p\le U}p^{-3/4}\ge4\log\log U-O(1)\).
With \(C_U\ge1\) and \(K(t)\ge K(1)>0\) on this short
interval for large \(U\), it follows that
\(F_U(1)\gg (\log U)^2\). For any \(H\), choose \(U\) and then
\(N\) fixed with \(\int W_N F_U\,dz>H\). The height limits
then contradict eventual \(M(X,1)\le H\).

Finally let \(B_P=\sup|E_P(x)|<\infty\) on the \(c=1\) band.
The weighted \(L^2(d\mu_X)\) triangle inequality gives
\[
 R_P(X,1)\ \ge\
 B_P^{-2}\big(\sqrt{M(X,1)}-2B_P\sqrt{q_X}\big)_+^2.
 \tag{E05.7}
\]
Thus for each fixed \(P\) and any prescribed \(B>0\) there
are arbitrarily high \(X\) with \(R_P(X,1)>B\).

## 4. Scope and collision controls

For every fixed \(P,\delta>0\) the separate nonnegative relative
\(L^2\) payment in (E05.2) is unbounded at arbitrarily high
centers in the \(c=1\) subfamily. The other terms are bounded
for that pair, so this particular allowance cannot satisfy the
eventual every-center margin. The signed Green value at those
centers remains open.

Even before any phase estimate, the same separate Jensen payment
with the regularized reference integral fails for any choice of
\(\delta>0\) at each center. The integrand of that reference
term is bounded below by \(\log\delta\), so the two terms together
are at least
\[
 q_X\log\delta+\frac{q_X}{2}\log(1+R_P/(q_X\delta^2))
 =\frac{q_X}{2}\log(\delta^2+R_P/q_X)
 \ge\frac{q_X}{2}\log(R_P/q_X)
\]
at centers with \(R_P>0\). The reference log integral less the
prime subtraction is bounded for fixed \(P\). As \(q_X\to1/2\),
the last lower bound is unbounded by (E05.7), independently of
the regulator choice. The obstruction still has fixed-reference
scope. Adaptive prime sets, signed use of the relative residual
with the phase, and other comparisons need their own estimates.
The simultaneous statement (E05.5) concerns the actual Green
value in dyadic density and leaves the exceptional set unresolved.

Use the collision screens in [B02 §5][b02], [E03 §5][e03] and
[E04 §4][e04] on the domains recorded in [controls12][controls].
The log transfer and harmonic kernel identity are generic. The
source-dependent premise is the literal complete formula with
canonical coefficients, reflection, correction and residual, and
its correspondence with the prime baseline.

| Control family | Premise absent from the theta-specific argument |
| --- | --- |
| Euler-factor and translated sources | The unchanged theta Dirichlet weights and prime subtraction. |
| Weighted squares and finite-prefix or finite-tail modifications | The full unmodified square coefficients together with canonical reflection. |
| Finite-prime orbits | Full reflection and all source coefficients, despite the selected-prime data. |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Ordinary theta/zeta Dirichlet arithmetic in the inherited field estimate. |
| Atomic and exact finite-profile controls, their continuous extensions, and heat counter-kernels | The complete canonical field with its two-arm formula and retained correction. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic despite completion and residue matching. |
| Fixed theta amplitude with variable readout | The actual cosine readout and corresponding physical Newman equation. |
| Relaxed positive Green profiles | Identification with the exact integer zero measure and the complete critical-boundary field. |

The conclusions require no new numerical campaign. The exceptional
statement uses fixed finite test polynomials and the complete
normalized field at the original times.

[request]: ../research-progress/handoffs/04_GNP_RS_E05_FINITE_EULER_RESIDUAL_R1_20261111.md
[e01]: 03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_PROOF_20261111.md
[b02]: 05_GNP_RS_B02_JENSEN_AND_SHIFTED_ZETA_COMPARISON_20261111.md
[e03]: 07_GNP_RS_E03_COHERENT_JENSEN_OBSTRUCTION_20261111.md
[e04]: 11_GNP_RS_E04_REGULARIZED_LOG_TRANSFER_20261111.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

[review]: ../reviews/08_GNP_RS_B04_INTERNAL_REVIEW_20261111.md
