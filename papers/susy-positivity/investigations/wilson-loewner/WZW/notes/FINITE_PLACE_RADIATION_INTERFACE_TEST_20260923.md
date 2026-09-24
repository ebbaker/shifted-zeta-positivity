# Two-prime radiation interface: a unitary delay model and a completion obstruction

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Status:** a specified thermal boundary coupling has actual logarithmic delays, an ordinary radiation-energy identity, and a norm identity limit. Its arithmetic amplitudes fail. Independently, the full archimedean factor times any finite Euler product cannot be a passive causal transfer for \(0<\omega<1/2\). These are scoped exclusions, not an obstruction to a coupled global realization or an RH result.

This executes the finite-place interface test proposed in Section 7 of the [arithmetic orbit-weight note](ARITHMETIC_ORBIT_WEIGHTS_AND_BOST_CONNES_TEST_20260923.md) and Section 5 of the [current manuscript](../manuscript.tex). It includes the [144-case diagnostic](../numerics/check_finite_place_interface.py), [compact record](../numerics/records/finite-place-interface-20260923.json), and [same-assistant audit](../reviews/review_codex_finite_place_interface_20260923.md). The manuscript remains the preceding synthesis; this is a research addendum.

## 1. What the test settles

There are two separate findings.

First, primitive thermal events can control an explicitly unitary radiation coupling. A pair of multiplicative delay loops gives delays \(\log2,\log3,\log4,\log6\), retains the primitive event on repeated traversals, and permits a complete accounting of coherent output, thermal fluctuations and stored radiation. Thus the passage from a primitive probability to a delayed measured amplitude can be made concrete in a simple model.

The resulting coefficients are not the required centered coefficients. A fixed loop has a temperature-independent ratio between successive repetitions. The target ratio is \(\ell^{(\beta-1)/2}\), with \(\beta=2\omega\). Neither the primitive probability nor thermal averaging changes the fixed loop ratio. The model also has a nonzero instantaneous response instead of the target's continuously varying archimedean front.

Second, a literal finite-product version of the proposed completed target has an unconditional stability obstruction:

\[
 A_{\beta/2}(p)Z_{S,\beta/2}(p)
 \quad\hbox{has a nonzero pole at}\quad
 p_\beta=\frac{1-\beta}{2}>0,\qquad 0<\beta<1.                 \tag{1}
\]

The full zeta quotient cancels this pole through the pole of \(\zeta(s)\) at \(s=1\); a finite Euler product does not. Consequently a finite-prime model cannot be required to equal that literal product for all times while remaining a zero-input-energy passive scattering system. Additional passive output channels cannot repair a scalar transfer with an uncancelled right-half-plane pole.

This refines the previous next-test specification. A finite thermal subsystem is legitimate, but its completed response must retain the effect of the omitted global arithmetic sector, or be tested on a finite time window. Keeping the exact archimedean factor while simply deleting all other primes is not a passive approximation.

## 2. Native preparation and an explicit real radiation coupling

Use the independently defined finite-place Hamiltonian

\[
 \mathcal H_S=(\log2)N_2+(\log3)N_3,\qquad S=\{2,3\},
 \quad
 \rho_\beta=\bigotimes_{\ell\in S}(1-q_\ell)q_\ell^{N_\ell},
 \quad q_\ell=\ell^{-\beta}.                                \tag{2}
\]

It is a normalized positive Gibbs state for every real \(\beta>0\). Set

\[
 P_\ell=|0\rangle_\ell\langle0|,\qquad
 Q_\ell=I-P_\ell,\qquad P_6=P_2P_3.
\]

These are the finite-place primitive projections of the preceding note. Their probabilities are \(1-q_\ell\) and \((1-q_2)(1-q_3)\). The infinite Bost–Connes KMS construction is background, not needed for the finite trace in this test; its existence in the critical interval is established in [Neshveyev, Introduction and Section 2](https://arxiv.org/html/0907.1456).

At each prime attach an oriented radiation loop with multiplicative coordinate \(1\le y\le\ell\), line element \(dx=dy/y\), and unit-speed propagation in \(x=\log y\):

\[
 (\partial_t+\partial_x)\psi_\ell=0,\qquad
 0<x<\tau_\ell,\qquad \tau_\ell=\log\ell.                    \tag{3}
\]

The ordinary energy stored in a loop is \(\int_0^{\tau_\ell}|\psi_\ell(t,x)|^2\,dx\). The incoming and outgoing port amplitudes use the ordinary time norm \(\int |f(t)|^2dt\). The metric is a specified modeling assumption; it is not inferred from the mere fact that \(\log\ell\) is an energy in (2). Once (3) is specified, its characteristics derive a flight time \(\log\ell\), and concatenating prime loops derives \(\log n\).

When \(P_\ell=1\), impose the boundary relation

\[
 \begin{pmatrix}y_\ell(t)\\u_\ell(t)\end{pmatrix}
 =
 \begin{pmatrix}-r_\ell&t_\ell\\t_\ell&r_\ell\end{pmatrix}
 \begin{pmatrix}f_\ell(t)\\v_\ell(t)\end{pmatrix},
 \qquad
 t_\ell=\sqrt{1-r_\ell^2},\qquad
 v_\ell(t)=u_\ell(t-\tau_\ell),                              \tag{4}
\]

with zero initial loop field. Here \(u_\ell\) launches the field into the loop and \(v_\ell\) is the returning field. When \(Q_\ell=1\), use the bypass \(y_\ell=f_\ell\) and a disconnected empty loop. On a common port-plus-loop space, the latter vertex is the identity matrix; the full vertex is the unitary block operator \(P_\ell\otimes U_\ell+Q_\ell\otimes I\). It commutes with \(\mathcal H_S\).

We choose the fixed values \(r_\ell=1/\ell\). They specify the candidate, not fitted thermal coefficients; all temperature dependence is in (2). The repetition argument below applies to every fixed \(0\le r_\ell<1\), so changing this choice cannot supply the target temperature dependence. The two stages are cascaded in the order 2 then 3 with no extra interstage delay.

This is an ideal occupation-controlled boundary model. It is not a claim to have manufactured a microscopic apparatus or derived the full arithmetic radiation geometry. The framework of operator-valued scattering and the need to retain finite feedback delays are described in [Combes–Kerckhoff–Sarovar, Sections IV and VII.10](https://arxiv.org/html/1611.00375). Here the delay fields and boundary equations are retained and solved explicitly; no zero-delay feedback approximation is used.

Preparation and readout are now fixed: prepare (2), leave the loops empty, inject the same phase-referenced signal in every preparation, and measure the mean outgoing amplitude with a phase-sensitive receiver. Record the inclusive output intensity as well. The controller is not reset between successive traversals. Since its occupations are unchanged, a repeated loop uses the same primitive event, not a new independent thermal trial.

## 3. Derived response and the four arithmetic labels

Put \(z_\ell=e^{-p\tau_\ell}\). Eliminating \(u_\ell,v_\ell\) from (4) gives the primitive-sector response

\[
 F_\ell(p)=-r_\ell+
       \frac{(1-r_\ell^2)z_\ell}{1-r_\ell z_\ell}
       =\frac{z_\ell-r_\ell}{1-r_\ell z_\ell}.                \tag{5}
\]

It is analytic and contractive for \(\Re p>0\), with unit modulus on the imaginary axis. Thermal averaging gives

\[
 R_{\ell,\beta}(p)=q_\ell+(1-q_\ell)F_\ell(p),\qquad
 R_\beta(p)=R_{2,\beta}(p)R_{3,\beta}(p).                    \tag{6}
\]

The product follows from the independent Gibbs preparation and the commuting, unchanged controllers. It is not an assumption that intensities multiply: (6) is the coherent mean amplitude.

Define

\[
 d_\ell=q_\ell-r_\ell(1-q_\ell),\qquad
 b_\ell=(1-q_\ell)(1-r_\ell^2).
\]

Then

\[
 R_{\ell,\beta}=d_\ell+
             \sum_{k\ge1}b_\ell r_\ell^{k-1}e^{-pk\log\ell}.
\]

Thus the actual cascade coefficients are

\[
 g_1=d_2d_3,\quad g_2=b_2d_3,\quad g_3=d_2b_3,\quad
 g_4=r_2b_2d_3,\quad g_6=b_2b_3.                            \tag{7}
\]

The primitive probabilities occur once per distinct prime, as desired. However, the necessary arithmetic coefficients from the note are

\[
 c_n(\beta/2)=n^{(\beta-1)/2}
                    \prod_{\ell\mid n}(1-\ell^{-\beta}).    \tag{8}
\]

Already the ratio invariant gives

\[
 \frac{g_4}{g_2}=r_2=\frac12,\qquad
 \frac{c_4}{c_2}=2^{(\beta-1)/2}.                            \tag{9}
\]

For \(0<\beta\le1\) the target ratio lies in \((1/\sqrt2,1]\), so this model fails throughout the interval. More generally, no fixed \(r_2\) can match the ratio on an open temperature interval. At \(\beta=1\), setting \(r_2=1\) to force the ratio to one closes the port, since \(t_2=0\); it does not give nonzero echoes.

One should compare arithmetic coefficients after allowing for the model's direct coefficient. Formally write \(\widehat c_n=g_n/g_1\). For the chosen vertices \(d_\ell>0\) throughout \(0<\beta\le1\), so this is well defined. It is only a comparison of path weights, not a new contractive physical readout. At \(\beta=1\):

| Label \(n\) | Measured \(g_n\) | Formally normalized \(\widehat c_n\) | Target \(c_n(1/2)\) |
|---:|---:|---:|---:|
| 1 | \(1/36\) | 1 | 1 |
| 2 | \(1/24\) | \(3/2\) | \(1/2\) |
| 3 | \(4/27\) | \(16/3\) | \(2/3\) |
| 4 | \(1/48\) | \(3/4\) | \(1/2\) |
| 6 | \(2/9\) | 8 | \(1/3\) |

The normalized composite does obey \(\widehat c_6=\widehat c_2\widehat c_3\). Multiplicativity alone therefore passes but is insufficient. The first-prime shift tangent also fails:

\[
 \left.\partial_\omega\widehat c_2\right|_{\omega=1/2}
       =12\log2,\qquad
 c_2'(1/2)=\frac32\log2.                                    \tag{10}
\]

For completeness, the unnormalized cascade tangent is
\(\partial_\omega g_2|_{1/2}=(\log2)/12-(\log3)/3\).
The record distinguishes the two normalizations.

The front is another independent failure. For \(\beta>0\),
\(R_\beta(p)\to d_2d_3>0\) as real \(p\to+\infty\), whereas
\(K_{\beta/2}(p)\sim(2\pi/p)^{\beta/2}\to0\).
Thus this real radiation channel does not produce the gamma factor or rational completion. Calling its coordinate archimedean does not supply those factors.

## 4. Ordinary radiation-energy balance, including thermal fluctuations

The vertex in (4) is unitary, so

\[
 |f_\ell|^2+|v_\ell|^2=|y_\ell|^2+|u_\ell|^2.
\]

For the active loop,

\[
 E_\ell(t)=\int_{t-\tau_\ell}^t|u_\ell(s)|^2ds,\qquad
 E_\ell'(t)=|u_\ell(t)|^2-|v_\ell(t)|^2.
\]

Consequently, after cascading the two stages, each controller sector \(a\) satisfies

\[
 \int_0^L|f(t)|^2dt
 =\int_0^L|y_a(t)|^2dt+E_{2,a}(L)+E_{3,a}(L).               \tag{11}
\]

All fields are initially zero in the loops. There is no thermal energy extraction: the coupling preserves the controller occupations. For \(r_\ell<1\), a finite-duration pulse eventually leaves the connected loops.

Let \(\mathbb E_\beta\) average the four primitive/nonprimitive sectors and let \(\bar y=\mathbb E_\beta y_a=R_\beta f\). Taking the expectation of (11) and using the variance identity gives

\[
 \boxed{\ \|f\|_{(0,L)}^2
 =\|\bar y\|_{(0,L)}^2
  +\mathbb E_\beta\|y_a-\bar y\|_{(0,L)}^2
  +\mathbb E_\beta(E_{2,a}(L)+E_{3,a}(L)).\ }                \tag{12}
\]

All norms are ordinary radiation norms. The second term is outgoing signal fluctuation correlated with the thermal controller, not absorption and not an unidentified loss port. For a mixed controller the inclusive output energy is the sum of the first two output terms. Equivalently, purifying the thermal state makes them the projections onto its coherent reference component and the orthogonal record components; that decomposition does not require postselection for the mean-amplitude measurement.

For a unit box pulse of width \(0.05\) and \(L=2.05\), the diagnostic finds:

| \(\beta\) | Coherent output | Fluctuating output | Stored in loops | Sum |
|---:|---:|---:|---:|---:|
| 0.5 | 0.1225510535 | 0.8087949189 | 0.0686540276 | 1 |
| 0.8 | 0.0753745193 | 0.8204159283 | 0.1042095524 | 1 |
| 1.0 | 0.0742723337 | 0.8009527178 | 0.1247749486 | 1 |

The program evaluates exact translated-box intersection lengths in floating arithmetic, including interference when pulses overlap. It does not replace flight times by a rounded time grid.

There is also a positive endpoint result. Since each \(F_\ell\) is a contraction,

\[
 \|R_{\ell,\beta}-I\|\le2(1-q_\ell),\qquad
 \|R_\beta-I\|\le2[(1-2^{-\beta})+(1-3^{-\beta})]\longrightarrow0. \tag{13}
\]

Thus this particular scattering family has even an operator-norm identity limit as \(\beta\downarrow0\), despite the absence of a limiting trace-class Gibbs state. This supplies an example of why the lack of a state-vector limit does not by itself exclude a scattering limit. It does not make the family arithmetic.

## 5. A broader limitation on a fixed bounded thermal readout

The centering gap is not repaired simply by choosing another fixed bounded observable.

**Proposition.** Fix a finite nonempty prime set \(S\), the Hamiltonian \(\mathcal H_S\), and a bounded, temperature-independent operator \(B\). For an integer \(n>1\) supported on \(S\), the function
\(\operatorname{Tr}(\rho_\beta B)\) cannot equal
\[
 n^{(\beta-1)/2}\prod_{\ell\mid n}(1-\ell^{-\beta})
\]
on any nonempty open interval of positive real \(\beta\).

**Proof.** In the occupation basis,

\[
 f_B(\beta)=\prod_{\ell\in S}(1-\ell^{-\beta})
       \sum_{\mathbf m\ge0}
       \langle\mathbf m|B|\mathbf m\rangle
       e^{-\beta\sum_\ell m_\ell\log\ell}.                   \tag{14}
\]

The series converges uniformly on compact subsets of \(\Re\beta>0\), since its diagonal entries are bounded and the dominating geometric products converge. Hence \(f_B\) is holomorphic there. The proposed centered expression is also holomorphic. Equality on an open real interval forces equality throughout that half-plane by the identity theorem. But for every positive real \(\beta\), \(|f_B(\beta)|\le\|B\|\), while the proposed expression tends to infinity as \(\beta\to+\infty\). This is a contradiction.

The use of large \(\beta\) is an analytic argument about the fixed Hamiltonian and readout, not a demand that the target physical program operate at large shift. It is precisely the analyticity of a fixed finite-place thermal readout that connects the intervals.

For one place, (14) becomes \((1-q)\sum_{m\ge0}b_mq^m\). A centered prime repetition would require, after cancelling \(1-q\), the nonanalytic expression \(\ell^{-r/2}q^{-r/2}\) at \(q=0\). This is the same obstruction in elementary power-series form.

The proposition applies when the isolated echo is the expectation of a fixed bounded operator in the native Gibbs state. It does **not** exclude coefficients obtained after an unbounded or temperature-dependent deconvolution, a genuinely temperature-dependent boundary dynamics, a different jointly prepared radiation state, or the full completed transfer \(K_{\beta/2}\). In particular, one cannot apply it to the deconvolved coefficients of an arbitrary completed response without proving that the coefficient extraction is such a fixed bounded readout.

The previous imaginary-time half-step formula uses a temperature-dependent operator, so it is consistent with this proposition. It still needs a physical port interpretation; the formula alone is not a fixed passive detector.

## 6. The finite Euler product cannot carry the unchanged completion

This obstruction is independent of the loop model. Write

\[
 d=\frac{1-\beta}{2},\quad s_-=p+d,\quad s_+=p+d+\beta,
\]
\[
 A_{\beta/2}(p)=\pi^{\beta/2}
     \frac{\Gamma(s_-/2)}{\Gamma(s_+/2)}
     \frac{s_-(s_--1)}{s_+(s_+-1)},\qquad
 Z_{S,\beta/2}(p)=
     \prod_{\ell\in S}\frac{1-\ell^{-s_+}}{1-\ell^{-s_-}}.   \tag{15}
\]

For \(0<\beta<1\), at \(p=d\) one has \(s_+=1\) and \(s_-=1-\beta\). Neither the numerator of the rational factor nor either gamma factor vanishes or diverges there. Each finite Euler factor is positive, finite and nonzero. Therefore

\[
 \boxed{\operatorname*{Res}_{p=d}
       [A_{\beta/2}(p)Z_{S,\beta/2}(p)]
 =-\beta(1-\beta)\pi^{(\beta-1)/2}
      \Gamma\!\left(\frac{1-\beta}{2}\right)
      \prod_{\ell\in S}
      \frac{1-\ell^{-1}}{1-\ell^{-(1-\beta)}}\ne0.}          \tag{16}
\]

The formula includes the empty product. In particular, \(A_{\beta/2}\) is not itself an independently passive causal scattering block in this interval.

A causal time-invariant contraction on ordinary \(L^2(0,\infty)\) has a holomorphic contractive Laplace multiplier on \(\Re p>0\). One elementary way to see its bound is to apply its adjoint to the Laplace evaluation vector \(t\mapsto e^{-\bar p t}\): this vector is an eigenvector of the adjoint with eigenvalue the conjugate multiplier, so contraction implies modulus at most one. Analyticity follows from the Laplace representation. If every finite-window causal compression is contractive, passage to increasing windows gives this global contraction on compactly supported inputs.

An uncancelled pole at \(d>0\) is consequently impossible for such a response. Agreement with (15) even on a safe right half-plane forces agreement by analytic continuation up to that pole. Adding zero-input passive ports does not evade the conclusion, because any measured scalar block of a passive multiport system is still contractive. A causal **unstable** response is not excluded by the pole argument; the missing property is the required ordinary energy bound.

For the actual completed quotient the factor \(\zeta(s_+)^{-1}\) has a zero at \(s_+=1\). The simple pole and residue-one statement used here are standard; see [DLMF 25.2(i) and 25.2.4](https://dlmf.nist.gov/25.2). Thus the full product has the regular value

\[
 K_{\beta/2}(d)=\frac{\xi(1-\beta)}{\xi(1)}
              =2\xi(1-\beta).                             \tag{17}
\]

This local cancellation is unconditional and uses no RH assertion. It is not a proof of contractivity of the full quotient.

For \(S=\{2,3\}\), the computed residues and the full quotient's finite comparison values are:

| \(\beta\) | Pole \(d\) | Finite-product residue | Full \(K_{\beta/2}(d)\) |
|---:|---:|---:|---:|
| 0.25 | 0.375 | -0.4238336217 | 0.9956782678 |
| 0.5 | 0.25 | -1.8332531812 | 0.9942415564 |
| 0.8 | 0.1 | -17.7210176988 | 0.9963110325 |
| 0.95 | 0.025 | -333.3685727766 | 0.9989035135 |

Adding finitely many primes does not remove the pole. In fact every added factor in the product in (16) exceeds one, so its residue magnitude increases. This does not contradict the full cancellation: the Euler products do not converge to the analytically continued zeta quotient in a neighborhood of this point.

At the endpoint \(\beta=1\), the two-prime product instead has a cubic boundary pole:

\[
 A_{1/2}(p)Z_{\{2,3\},1/2}(p)
       \sim-\frac{2}{3\log2\,\log3}\,\frac1{p^3},
       \qquad p\downarrow0.                               \tag{18}
\]

Indeed \(A_{1/2}(p)\sim-2/p\), and each Euler factor contributes
\((1-\ell^{-1})/(p\log\ell)\). This unbounded boundary behavior also precludes a contractive multiplier. The full modular half-shift quotient has \(K_{1/2}(0)=1\). The finite-product failure therefore does not challenge the existing global modular Hodge benchmark.

## 7. What changes in the next research question

The original coefficient identity survives. What fails is the simple fixed-controller loop readout, and the literal truncation that pairs a finite Euler product with an unchanged full archimedean factor.

The next candidate must address a **joint** archimedean/arithmetic boundary dynamics. A useful starting point remains the existing global modular exact-one-form channel at \(\beta=1\), with its already normalized radiation norm. A native thermal perturbation would have to change that channel's boundary dynamics or domain, not merely average a fixed bounded detector. Its first calculation should exhibit the moving cancellation at \(p=(1-\beta)/2\); only then should a scalar completed response be compared with the target. Declaring a zero at that location by multiplying in a designed filter would not derive it physically.

A bounded continuation test can use the tangent at \(\beta=1\):

\[
 \left.\partial_\beta\log K_{\beta/2}(p)\right|_{\beta=1}
   =-\tfrac12a_{1/2}(p),\qquad
 \left.\partial_\beta c_{\ell^r}(\beta/2)\right|_{\beta=1}
   =(\log\ell)\left[\frac r2(1-\ell^{-1})+\ell^{-1}\right]. \tag{19}
\]

The joint coupling must supply the archimedean front derivative as well, including the leading term \(-\tfrac12\log(p/(2\pi))\). No such perturbation is constructed in this note. The requirement in (19) is a test for an independently specified coupling, not permission to define the coupling from the target logarithmic derivative.

If finite computational data are needed first, use a finite **time** window instead of claiming a passive finite Euler completion. The formal causal kernel of \(A_{\beta/2}Z_{S,\beta/2}\) and that of the full quotient agree before the first omitted prime delay: in a far-right Laplace half-plane their Euler series agree term by term there, and the archimedean kernel is causal. For \(S=\{2,3\}\) this means \(L<\log5\), covering labels 2, 3 and 4. To examine the full scalar response through \(\log6\), include the prime 5 and take \(\log6<L<\log7\). A path-resolved experiment may isolate label 6 with just two loops, but a scalar trace through that time cannot omit label 5 without explanation.

Such finite-window agreement is not an assertion of contraction at arbitrary shift and does not provide a physical dilation. It avoids the false inference that a finite Euler truncation is globally passive and makes the next diagnostic faithful to the full target.

For clarity, causality of the formal archimedean kernel in this limited statement is elementary. The gamma portion of (15) is the Laplace transform of
\[
 \frac{2\pi^{\beta/2}}{\Gamma(\beta/2)}
 e^{-dt}(1-e^{-2t})^{\beta/2-1}1_{t>0}.
\]
This follows by the beta integral with substitution \(u=e^{-2t}\). The rational portion has a causal distributional inverse consisting of a direct term and exponential terms, one growing at rate \(d\). Thus it preserves support but does not supply passivity. No analytic continuation of a divergent Euler product is used to infer the finite-window agreement.

## 8. Verification, reproducibility and scope

The new program has **144 passing floating controls**, separate from the previous 87-case coefficient suite. It uses Python 3.10.0, mpmath 1.3.0 and 60 decimal digits. It solves the vertex equations independently of the closed transfer, performs native Gibbs sums through occupation 360 with an explicit omitted-mass bound, and constructs echo paths directly from the boundary recursion.

The energy checks cover all four controller sectors on five finite windows, and the thermal coherent/fluctuating decomposition at three temperatures. Other controls reproduce the repetition and tangent mismatches, calculate pole residues from symmetric samples, check two other finite prime sets, and compare the completed zeta factorization with the regular xi quotient near the cancellation. The record binds the program by SHA-256 and stores small tables only.

From the parent Wilson–Loewner directory, with Python 3 and mpmath available:

    python3 -B WZW/numerics/check_finite_place_interface.py --output /tmp/finite-place-interface-replay.json

The interval-overlap integrals are exact formulas evaluated in floating arithmetic; none of the controls is an interval certificate. The analytic proofs of (9), (12), the fixed-readout proposition, and (16) do not depend on the sample grid or cutoffs. Passing controls reproduce both the valid physics of the stated model and its failure to match the arithmetic target; they do not report a successful physical realization.

The research and audit were prepared by the same assistant, not an independent specialist. No general obstruction to temperature-dependent interactions, nonfactorized global scattering, or the shifted-zeta program is established.
