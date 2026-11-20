# Summing the contour expansion for a large-time theta zero

20 November 2026. Prepared for Edward Baker with OpenAI Codex LLM assistance. The desktop chat records gpt-6.2-astra and max reasoning effort. The public archive supplies no separate per-turn configuration.

Every integral in the logarithm expansion can be evaluated analytically. The full sum admits a convergent series in the odd cumulants of the positive-half-line theta source. This gives the first distortion that a change of lattice spacing alone cannot absorb. For the first two positive zeros,

\[
 \lim_{T\to\infty} L_T^3\kappa_T^2
       \left(1-\frac{x_2(T)}{3x_1(T)}\right)=\frac{4\pi^2}{3}.
\]

Sections 1–4 derive the finite-time resummation and bound the error of its closed cubic expression on a growing interval of indices. Section 5 derives the limit, and Section 6 reports a finite-time interval check. Section 7 gives the coefficients in standard functions and an obstruction to a finite algebraic expression for the continuous inverse phase.

This is an exploratory calculation of zero positions in the large-positive-time regime. Its quantitative outputs concern the distortion of the first two positions and errors at \(T=1000\). The earlier-time signed gap problem remains open. [Starting loop and saddle estimates](../../01_jacobi_integer_hierarchy/brainstorm/notes/07_LARGE_TIME_FACTORIZATION_AND_BACKWARD_PROPAGATION_20261120.md) · [Result index](../../../../../result-summaries/README.md) · [Heat-flow results](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md) · [Patterns index](../../../../../avoid/README.md) · [Criterion classification](../../../../../avoid/01_restating_the_target.md)

## 1. Evaluate every loop integral

Use \(L=L_T\) from the large saddle \(4\pi e^{4L}=2TL+9\), and \(\kappa=8TL-2T+36\). Fix a positive index \(k\), \(q=(k-\tfrac12)\pi\), \(s=\sin q=(-1)^{k-1}\), and \(r=1/2\). Put

\[
 f(w)=\frac{H(T,w/L)}{H(T,0)},\qquad g(w)=f(w)-\cos w,\qquad
 \Gamma=\{|w-q|=r\}.
\]

Assume the indexed circle test of Note 07. It gives \(G=\max_{|w-q|\le r}|g(w)|<\sin r\), and identifies the unique zero in the circle as \(Lx_k\). This holds eventually for each fixed \(k\). Oriented counterclockwise, the starting loop is

\[
 Lx_k-q=-\frac{1}{2\pi i}\oint_{\Gamma}
                   \log\!\left(1+\frac{g(w)}{\cos w}\right)\,dw .
\]

Write \(D=d/dw\). Define real polynomials by

\[
 P_0(X)=1,\qquad P_1(X)=X,\qquad
 P_{n+1}(X)=(X^2+n^2)P_{n-1}(X)\quad(n\ge1).
\]

Then the original logarithm expansion, in its original order, is

\[
 \boxed{\displaystyle Lx_k-q=\sum_{n\ge1}\frac{s^n}{n!}
             \left[P_{n-1}(D)g(w)^n\right]_{w=q}.}                    \tag{1}
\]

Indeed \(-\log(1+g/\cos)=\sum_{n\ge1}(-1)^n(g/\cos)^n/n\) on \(\Gamma\). With \(h=w-q\), \(\cos(q+h)=-s\sin h\). For an analytic \(J\), the first two residues of \(J(h)/\sin^n h\) are \(J(0)\) and \(J'(0)\). The identity
\((D_h^2+n^2)\csc^n h=n(n+1)\csc^{n+2}h\) and two integrations by parts in a residue give \(P_{n-1}(D)J(0)/(n-1)!\) at every order, where the operator acts before evaluation. This proves (1). In particular the first four terms are

\[
 s g+\frac{(g^2)'}2+\frac{s}{6}\big((g^3)''+g^3\big)
   +\frac{(g^4)'''+4(g^4)'}{24},\qquad w=q .
\]

An equivalent formula for integrating a Fourier mode is

\[
 \operatorname{Res}_{h=0}\frac{e^{iyh}}{\sin^n h}
 =\frac{i^{n-1}}{(n-1)!}\prod_{j=1}^{n-1}(y+n-2j).
\]

It follows either from the recurrence or by substituting \(v=e^{2ih}-1\) in the residue. With \(\eta=G/\sin r<1\), the error after \(n=m\) in (1) is at most \(r\eta^{m+1}/[(m+1)(1-\eta)]\) in \(Lx_k\). The bound uses the intact \(g^n\) on the circle. Taking separate absolute values of all differentiated source terms can lose its cancellation.

## 2. Sum all powers at a given derivative order

Let \(A(w)=\arcsin(sg(w))\) on the branch through zero of the arcsine. Its power series gives \(\max|A|\le b=\arcsin G<r\). Since \(\sin A=sg\), the integrand has the exact factorization

\[
 \frac{f(q+h)}{\cos(q+h)}
 =\left(1-\frac{A(q+h)}{h}\right)
 \frac{\cos((h+A(q+h))/2)\,\operatorname{sinc}((h-A(q+h))/2)}
      {\operatorname{sinc}h},\qquad \operatorname{sinc}v=\frac{\sin v}{v}.
\]

The final quotient has a holomorphic logarithm on the disk. Its loop integral vanishes. Integrating the logarithm of the first factor yields the exact alternative sum

\[
 Lx_k-q=\sum_{m\ge0}\frac1{(m+1)!}
        \left[D^m A(w)^{m+1}\right]_{w=q}.                           \tag{2}
\]

The first terms are \(A,\ AA',\ A(A')^2+A^2A''/2\). The \(m\)-th term has magnitude at most \(r(b/r)^{m+1}/(m+1)\) by Cauchy's estimate. To check the regrouping, replace \(g\) by \(\lambda g\). Choose \(\lambda_0>1\) with \(\lambda_0G<\sin r\). The same summable estimate holds on \(|\lambda|\le\lambda_0\), and Cauchy's estimate in \(\lambda\) permits summation in either order at \(\lambda=1\). The first term already sums every contribution containing zero derivatives of \(g\).

For the positive atomic heat solution \(e^t\cos w+c\), take \(\rho=ce^{-t}\) and remove the constant normalization from the logarithm. Here \(g=\rho\), so (2) sums the entire calculation to \(x_k=q+s\arcsin\rho\). The original circle expansion holds for \(|\rho|<\sin r\). The explicit branch continues to \(\rho=1\), where adjacent roots meet and the one-zero contour test fails. This checks the signs, the branch choice, and what can happen past convergence on the original circle.

## 3. The complete theta sum in source cumulants

Give \(U\ge0\) density \(e^{Tu^2}\Phi(u)/H(T,0)\). Let \(a=\mathbb E_T U\), and let \(\gamma_j\) be the cumulants of this half-line law, defined as the derivatives at zero of \(\log\mathbb E_T e^{vU}\). Put \(y=ax\) and

\[
 K(y)=\log\mathbb E_T e^{iy(U-a)/a},\qquad
 H_o(y)=-\frac{K(y)-K(-y)}{2i}=\sum_{j\ge1}c_j y^{2j+1},
 \qquad c_j=\frac{(-1)^{j+1}\gamma_{2j+1}}{(2j+1)!\,a^{2j+1}} .
\]

Within its logarithm disk the field factors as
\(\exp((K(y)+K(-y))/2)\cos(y-H_o(y))\), after normalization by \(H(T,0)\). The even part has a zero-free exponential and its logarithm integrates to zero. Near \(q\), dividing \(\cos(y-H_o(y))\) by \(y-H_o(y)-q\) likewise leaves a holomorphic unit. This explains the cancellation of the even cumulants **after summing the loop**. The rescaling from \(w=Lx\) to \(y=ax\) also accounts for the displacement due to the mean.

Write \(Y(q)=a x_k\) at \(q=q_k\), extending \(Y\) by the inverse of \(y-H_o(y)\) through zero. Its full explicit series is

\[
 \boxed{\displaystyle
 Y(q)=\sum_{N\ge0}q^{2N+1}
  \sum_{\substack{m_j\ge0\\\sum j m_j=N}}
  \frac{(2N+|\mathbf m|)!}{(2N+1)!\prod_j m_j!}
       \prod_j c_j^{m_j},\qquad |\mathbf m|=\sum_jm_j .}              \tag{3}
\]

Each inner sum is finite. In particular

\[
 Y(q)=q+c_1q^3+(3c_1^2+c_2)q^5+(12c_1^3+8c_1c_2+c_3)q^7+\cdots.
\]

To derive (3), let \(\theta(u)=u-H_o(u)\). The contour integral of \(u\theta'(u)/(\theta(u)-q)\) around the unique preimage gives \(Y(q)\), with factor \(1/(2\pi i)\). Expanding in \(q\) and integrating by parts gives
\([q^m]Y=\frac1m[u^{m-1}](1-\sum_{j\ge1}c_j u^{2j})^{-m}\) for \(m\ge1\). The multinomial formula gives (3). These are classical inverse-series coefficients applied to the theta source. [Lagrange inversion, DLMF §1.10(vii)](https://dlmf.nist.gov/1.10.vii)

### A convergence test and a tail bound

For \(R>0\) set

\[
 \delta=\frac{R^2}{2a^2}\mathbb E_T[(U-a)^2e^{R|U-a|/a}],\quad
 M=-\log(1-\delta),\quad v_0=R/2,\quad B=M/6,\quad Q=v_0-B .
\]

Require \(\delta<1\) and \(Q>0\). Centering and Taylor's integral remainder give \(|e^{K(y)}-1|\le\delta\) for \(|y|\le R\). Hence \(|K|,|H_o|\le M\), which implies \(\sum |c_j|v_0^{2j+1}\le M\sum_{j\ge1}2^{-(2j+1)}=B\). For \(|q|<Q\), Rouché on \(|u|=v_0\) counts one simple solution of \(\theta(u)=q\). On the real interval its branch is increasing, by continuity of the nonzero derivative and its value at zero. This identifies the positive roots indexed by \(q_k<Q\).

The same argument with every \(c_j\) replaced by \(|c_j|\) gives an analytic majorant whose displacement from \(q\) is bounded by \(B\). Its nonnegative coefficients dominate the sum of absolute values of the individual monomials in (3). Cauchy's estimate bounds the error after \(N=N_0\ge0\) in \(Y(q)\) by

\[
 B\frac{(|q|/Q)^{2N_0+3}}{1-(|q|/Q)^2}.
\]

This justifies regrouping at the physical coefficients. The test holds eventually with \(R=a\sqrt\kappa/4\). In fact \(X=\sqrt\kappa(U-a)\) tends to a standard normal \(G_0\) with convergence of \(\mathbb E[X^2e^{|X|/4}]\). On the near-left and right saddle regions a Gaussian majorant still integrates the extra weight. On the far-left interval its cost \(e^{O(L\sqrt\kappa)}\) and polynomial factors are absorbed by \(e^{-c\kappa}\), since \(L/\sqrt\kappa\to0\). Centering at the mean shifts the standardized variable by \(O(\kappa^{-1/2})\). Thus \(\limsup\delta\le (1+1/16)e^{1/32}/16<0.07\), using \(e^{|x|/4}\le e^{x/4}+e^{-x/4}\). This finite test gives \(Q\ge a\sqrt\kappa/8-C_0\) for an absolute \(C_0\) and sufficiently large \(T\). [Complete-source saddle domination](../../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/brainstorm/01_CAP_AT_INFINITY_20261020.md) · [Weighted source estimates](../../../../investigations-5/01_heat_density_asymptotics/manuscript/05_appendices.tex)

## 4. All powers of the cubic contribution in closed form

The terms of (3) containing only \(c_1\) have coefficients \(\binom{3m}{m}/(2m+1)\) multiplying \(c_1^m q^{2m+1}\). Write \(h=-c_1>0\), as holds for theta at sufficiently large time by Section 5. Their exact sum is

\[
 Y_3(q)=\frac{2}{\sqrt{3h}}\sinh\!\left(\frac13
              \operatorname{arsinh}\!\left(\frac{3\sqrt{3h}}2q\right)\right).
\]

The triple-angle identity gives \(Y_3+hY_3^3=q\). Its power series converges for \(|c_1q^2|<4/27\), which includes \(|q|<Q\) because \(Q\le v_0-|c_1|v_0^3\). For \(c_1=0\) use \(Y_3(q)=q\).

Mixed terms can keep that cubic sum intact. Let \(J(y)=H_o(y)-c_1y^3\). Then

\[
 Y(q)=Y_3(q)+\sum_{m\ge1}\frac{1}{m!}
   \frac{d^{m-1}}{dq^{m-1}}\!\left[Y_3'(q)\,J(Y_3(q))^m\right].       \tag{4}
\]

To prove it, multiply \(J\) by a parameter \(\lambda\) and write \(u=q+\lambda J(Y_3(u))\), \(Y=Y_3(u)\). Inversion at \(\lambda=0\) gives (4). For each \(|q|<Q\), the strict margin on \(|y|=v_0\) persists for \(|\lambda|\) slightly larger than 1 in \(y-c_1y^3-\lambda J(y)=q\). The corresponding root is analytic in \(\lambda\), which justifies evaluation at one. In (4), the term indexed by \(m\) includes every power of \(c_1\) with exactly \(m\) insertions from the higher odd cumulants. Equation (3) or (4) retains them all.

### How many zeros share this expansion?

Put \(\ell=a\sqrt\kappa\), \(S=\kappa+2T\), and \(\alpha=2S/(3\kappa^{3/2})\). For **every fixed \(C>0\)**, (3) converges absolutely for all \(q_k\le C\ell\) once \(T\) is large enough depending on \(C\). Here \(\ell\sim(\sqrt{2}/4)\sqrt{T}(\log T)^{3/2}\). On this whole range,

\[
 a x_k=q_k-\alpha(q_k/\ell)^3+
               O_C\!\left(\kappa^{-1}(q_k/\ell)^3\right),\qquad
 |a x_k-Y_3(q_k)|=O_C\!\left(\kappa^{-1}(q_k/\ell)^5\right).
\]

For the proof use \(W=\sqrt\kappa(U-L)\) and write \(p_T(u)=Tu^2+9u-\pi e^{4u}\). On \(|w|\le\kappa^{1/12}\), Taylor expansion about \(L\) gives the following expression for the unnormalized density of \(W\), up to a constant independent of \(w\),

\[
 e^{p_T(L+w/\sqrt\kappa)-p_T(L)}b(L+w/\sqrt\kappa)
 =e^{-w^2/2}\left(1-\alpha w^3+
                       O\!\left(\frac{1+w^4+w^6}{\kappa}\right)\right).
\]

Here \(p_T'''(L)=-4S\). The quartic exponent remainder is \(O(w^4/\kappa)\), the square of the cubic is \(O(w^6/\kappa)\), and the complete theta prefactor in this interval is \(1+O(\kappa^{-1})\). Outside it, the Gaussian and far-left bounds of Section 3 absorb any fixed weight \(e^{4C|w|}\) and any fixed polynomial, with a tail smaller than every power of \(\kappa^{-1}\). Integrating the expansion gives \(\mathbb EW=-3\alpha+O(\kappa^{-1})\). For a standard Gaussian \(G_0\), \(\mathbb E[G_0^3 e^{i\zeta G_0}]=i(3\zeta-\zeta^3)e^{-\zeta^2/2}\). Centering cancels the linear term, so uniformly on the complex disk \(|\zeta|\le4C\),

\[
 K(\ell\zeta)=-\zeta^2/2+i\alpha\zeta^3+O_C(\kappa^{-1}).
\]

The Gaussian transform is bounded away from zero on that fixed disk, which justifies the logarithm. The odd part has supremum \(O_C(\kappa^{-1/2})\) there. Using this bound directly in the Cauchy and Rouché argument of Section 3 gives an inverse radius at least \(2C\ell-O_C(\kappa^{-1/2})\). It also gives absolute convergence of the individual terms in (3).

To get the sharper remainder, \(H_o(\ell\zeta)+\alpha\zeta^3\) is \(O_C(\kappa^{-1})\) on \(|\zeta|\le4C\) and vanishes to order at least three. After removing its exact cubic coefficient, the remaining \(J(\ell\zeta)\) vanishes to order at least five. Cauchy's estimate gives the respective bounds \(O_C(\kappa^{-1}|\zeta|^3)\) and \(O_C(\kappa^{-1}|\zeta|^5)\) on \(|\zeta|\le2C\). The inverse equation then gives \(|Y-q|\ll_C\kappa^{-1/2}|Y/\ell|^3\), hence \(|Y|\le2|q|\) eventually. Substituting in the cubic term gives the first displayed estimate. For the second, \(Y+hY^3=q+J(Y)\) and \(Y_3+hY_3^3=q\). The real map \(u\mapsto u+hu^3\) has derivative at least one, so \(|Y-Y_3|\le|J(Y)|\). All thresholds here may depend on the fixed \(C\).

## 5. A canonical distortion of the first two zeros

Write \(v=U-L\), \(d=\mathbb E_Tv\), \(S=\kappa+2T\), \(p_0=\Phi(0)/H(T,0)\), and \(\beta=b'/b\) for the complete prefactor \(b\) of Note 07. The half-line integration-by-parts identity for each integer \(j\ge0\) is

\[
 \kappa\mathbb E_T v^{j+1}
 =j\mathbb E_T v^{j-1}
  +\mathbb E_T\!\left[v^j\left\{-\tfrac S4(e^{4v}-1-4v)+\beta(U)\right\}\right]
  +(-L)^j p_0 ,
\]

with the first term zero for \(j=0\). The known inputs are \(d=-2S/\kappa^2+O(\kappa^{-3/2})\), \(\mathbb E_Tv^2=\kappa^{-1}+O(\kappa^{-3/2})\), and \(\mathbb E_T |v|^j e^{4|v|}=O_j(\kappa^{-j/2})\) for the orders through five used here. Further, \(|\beta(u)|=O(e^{-4u})\), \(e^{-4L}=16\pi/S\), and the endpoint terms are smaller than every inverse power of \(\kappa\). [Saddle shift in Note 07](../../01_jacobi_integer_hierarchy/brainstorm/notes/07_LARGE_TIME_FACTORIZATION_AND_BACKWARD_PROPAGATION_20261120.md) · [Complete-source score identity](../../../../investigations-5/01_heat_density_asymptotics/manuscript/07_explicit_clock.tex)

The row \(j=3\) gives \(\mathbb E_Tv^4=3/\kappa^2+O(\kappa^{-5/2})\), since the exponential remainder starts with \(v^2\). In the row \(j=2\), expand that remainder through its quadratic term. This gives
\(\kappa\mathbb E_Tv^3=2d-2S\mathbb E_Tv^4+O(\kappa^{-3/2})\).
Subtracting \(3d\mathbb E_Tv^2-2d^3\) from the raw third moment yields

\[
 \gamma_3=-\frac{4S}{\kappa^3}+O(\kappa^{-5/2}).
\]

For fixed \(k\), the terms after \(c_1q_k^3\) in (3) are \(O_k((a\sqrt\kappa)^{-5})\) by its tail bound. Forming \(Y(q_2)/(3Y(q_1))\) uses \(q_2=3q_1\) and \(q_2^2-q_1^2=2\pi^2\). With \(a=L+O(\kappa^{-1})\) this gives

\[
 \boxed{\displaystyle
 1-\frac{x_2}{3x_1}=
 \frac{4\pi^2 S}{3L^3\kappa^3}
     +O\!\left(\frac{1}{L^3\kappa^{5/2}}\right).}                     \tag{5}
\]

Since \(S/\kappa\to1\), the limit in the opening follows. More generally \(q_k^2-q_1^2=\pi^2k(k-1)\) gives, for every fixed \(k\ge2\),

\[
 \lim_{T\to\infty} L^3\kappa^2
       \left(1-\frac{x_k(T)}{(2k-1)x_1(T)}\right)
       =\frac{2\pi^2}{3} k(k-1).
\]

Dividing two positions removes the common lattice frequency. The negative skew of the tilted source puts each fixed higher zero slightly inside the odd multiple predicted from the first. In time alone \(L\sim(\log T)/4\) and \(\kappa\sim8TL\) give \(1-x_2/(3x_1)\sim64\pi^2/[3T^2(\log T)^5]\).

## 6. A finite check with the complete theta source

At \(T=1000\), an Arb calculation encloses

\[
 8.7369418009258\,10^{-8}<
        1-\frac{x_2}{3x_1}<8.7369418009259\,10^{-8}.
\]

The complete-source contour allowance is below \(0.009662\) for both indices. With \(R=16\) the phase test gives \(Q>7.9972>3\pi/2\). Direct signs at the two ends of each root bracket provide a comparison for the following upper bounds on absolute error in physical \(x\).

| Expression | Error for \(x_1\) | Error for \(x_2\) |
| --- | ---: | ---: |
| Mean lattice \(q/a\) | \(1.28\,10^{-8}\) | \(3.46\,10^{-7}\) |
| First four original logarithm terms, (1) | \(9.32\,10^{-20}\) | \(2.97\,10^{-16}\) |
| First four arcsine terms, (2) | \(3.23\,10^{-18}\) | \(6.18\,10^{-16}\) |
| Closed cubic sum \(Y_3/a\) | \(2.09\,10^{-15}\) | \(5.06\,10^{-13}\) |
| Complete inverse through \(q^5\), (3) | \(8.13\,10^{-22}\) | \(1.78\,10^{-18}\) |
| Complete inverse through \(q^7\), (3) | \(3.34\,10^{-28}\) | \(6.58\,10^{-24}\) |

The groupings use different source inputs. Direct signs and both series evaluations share the source normalization. The finite check certifies these particular errors. The proof of (5) uses the saddle estimates.

Farther along the sequence, \(q_{40}/(a\sqrt\kappa)\approx0.987720\). Direct signs enclose \(x_{40}=92.49456351756309795525\ldots\). The errors in \(q_{40}/a\), \(Y_3(q_{40})/a\), and the polynomial through \(q_{40}^7\) are below \(0.006298\), \(6.390\,10^{-6}\), and \(3.990\,10^{-11}\), respectively. For the index check take \(X=(q_{40}+1/2)/a\). On \([0,X]\) the centered transform has real part at least \(b_*=1-X^2\gamma_2/2>0.5074\). The physical phase has derivative at least \(a-\sqrt{\gamma_2}/b_*>1.3204\), starts at zero, and differs from \(ax\) by less than \(\pi/2\). The signed bracket lies in this interval with \(|ax-q_{40}|<1/2\). Thus its phase crosses exactly the fortieth level there. This checks the displayed finite approximations at that index. The finite complex-disk convergence test quoted above covers the first two.

The implementation integrates the first square mode on \([1,2]\) with the peak divided out. All real tests used there satisfy \(|g(u)|\le (u+2)^7e^{16(u+2)}\). On \([0,1]\) the maximum of \(Tu^2+9u-\pi e^{4u}\) is at 1 by the derivative signs and the concavity of its derivative. On \([2,\infty)\) its tangent at 2 gives an integrable exponential majorant. On \([1,2]\) the remaining prefactor modes sum to at most \(32e^{-3\pi e^4}\) by the square-series ratio. The program adds all three omitted parts to every integral. Their combined absolute allowance is below \(2.353\,10^{-107}\) in the scaled integrals. The direct root brackets use full-source signs after a Newton candidate and the index checks above. [Replay program](../../01_jacobi_integer_hierarchy/numerics/check_large_time_resummation.py) · [Outward intervals and signed truncation errors](../../01_jacobi_integer_hierarchy/numerics/08_LARGE_TIME_LOOP_RESUMMATION_20261120.json)

## 7. What the full sum requires

All cumulants in (3) admit expressions in standard functions without a numerical source quadrature. With \(b_n=\pi n^2\), set \(J(b,v)=b^{-v}\Gamma(v,b)\) and

\[
 P(s)=\tfrac14\sum_{n\ge1}\{2b_n^2J(b_n,(9+s)/4)
                  -3b_nJ(b_n,(5+s)/4)\},\qquad
 P_T(s)=\sum_{j\ge0}\frac{T^j}{j!}P^{(2j)}(s).
\]

Substitution of \(b_ne^{4u}\) into the two half-line integrals gives \(P(s)=\int_0^\infty e^{su}\Phi(u)\,du\). Expanding \(e^{Tu^2}\) therefore gives \(\gamma_m=\partial_s^m\log P_T(s)|_{s=0}\) for \(m\ge1\). The double-exponential tail dominates the absolute expansions on compact subsets in \(T,s\), also for the two polynomial source terms separately. This supplies a nested convergent formula for every coefficient in (3), using arbitrarily high odd cumulants across the full series. [Upper incomplete gamma definition, DLMF 8.2.2](https://dlmf.nist.gov/8.2.E2)

One possible finite closure can be excluded exactly. **At a fixed finite \(T\), the continuous inverse-phase germ \(Y(q)\) is not algebraic in \(q\).** To see this, write \(M(s)=\mathbb E_T e^{sU}\) and \(b(s)=(2s)^{-1}\log(M(s)/M(-s))\) for \(s>0\). Positive mass above every fixed \(A\) implies \(b(s)\to\infty\). Positive continuous density at zero gives \(M(-s)\ge c_T/s\) for large \(s\), and the double-exponential tail gives \(\log M(s)=O_T(s\log(2+s))\). Thus \(b(s)=O_T(\log s)\). The real-source phase at physical \(z=-is\) continues along this ray as \(-is b(s)\), since both transforms inside its logarithms are strictly positive there.

An algebraic inverse germ would give a nonzero polynomial relation between the physical argument and its phase near zero, and hence on that ray by continuation. Substitute \(z=-is\), \(\Theta(z)=-is b(s)\), and divide by \(s^d\), with \(d\) the highest total degree. The leading homogeneous part is a nonzero polynomial in \(b(s)\). All lower-degree parts tend to zero because \(b(s)=O(\log s)\). The leading part cannot tend to zero as \(b(s)\to\infty\). This proves the stated exclusion. It leaves open transcendental special-function expressions and formulas specific to the discrete \(q_k\).

The identities (1)–(4) apply within the specified cosine, count and analyticity hypotheses. Each actual double in a covered disk fails the strict one-zero contour comparison. In the phase description a zero amplitude or a critical phase value prevents the stated simple inverse branch there. The Euler-factor family changes the theta coefficients. Weighted-square, finite-tail and finite-prime families lose the complete normalized theta source. Reflected and positive-primitive controls lack its square expansion. Finite-profile and atomic controls change the full profile, and the RH-conditional endpoint controls change ordinary Dirichlet arithmetic. The altered-observation controls fail the cosine observation. Some controls can share a leading saddle or the general growth obstruction. Neither observation transfers the canonical coefficient in (5) or yields an earlier-time collision exclusion. [Collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Branch premise screen](../../01_jacobi_integer_hierarchy/research-overview/01_AGC_JH_RESEARCH_OVERVIEW_20261119.md) · [Shape-only arguments](../../../../../avoid/02_shape_only_arguments_and_the_controls.md) · [Scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
