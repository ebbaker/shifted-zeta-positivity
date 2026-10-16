# Energy-exchanging thermal boundary coupling and rigidity of the modular front

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Status:** negative structural test for regular passive parallel boundary loads with finite total response spectral weight. Native Bost–Connes transition probes fall in this class and cannot supply the arithmetic shift. The exact statements concern their Kubo response and its conservative linear boundary realization. No exact finite-coupling microscopic quantum scattering construction, general bulk-coupling obstruction, or RH result is claimed.

This carries out the agreed structural test following the [finite-place radiation interface investigation](FINITE_PLACE_RADIATION_INTERFACE_TEST_20260923.md). The [program](../numerics/check_thermal_boundary_structure.py), [203-case record](../numerics/records/thermal-boundary-structure-20260923.json), and [same-assistant audit](../reviews/review_codex_thermal_boundary_structure_20260923.md) accompany the calculation. It is a research addendum; manuscript sources and PDFs are unchanged.

## 1. Result and research decision

The preceding test left open whether energy exchange, rather than a fixed primitive gate, could turn thermal arithmetic data into the required deformation of the global modular channel. This test allows that exchange explicitly. The native isometries \(v_2,v_3\) change the occupation energies. Their self-adjoint combinations \(v_\ell+v_\ell^*\) have nonzero retarded thermal response, which supplies a positive oscillator admittance.

Connect that admittance to the existing **full** modular Hodge response. The Euler factors and archimedean completion remain together throughout; no finite Euler truncation is used. The connection is conservative in its linear response realization and preserves the ordinary coherent radiation norm. Nevertheless, it fails the necessary front test.

The reason extends beyond two selected transition frequencies. If the load's positive response spectral measure has finite total mass, its admittance is \(O(p^{-1})\) on the positive real Laplace axis. At the favorable zero-extra-lead reference this changes the modular response only at order \(p^{-1}\), leaving its leading \(p^{-1/2}\) front unchanged. The arithmetic family requires the leading power \(p^{-\beta/2}\) and a logarithmic parameter tangent at \(\beta=1\).

**Decision:** park the regular finite-place Bost–Connes boundary-realization branch as an active route to arithmetic positivity. Retain the thermal coefficient identity and the completed tests. More prime modes or fitted loop/coupler constants within the same finite-spectral-mass class cannot repair this failure. Reopening the branch should require a specific independently defined interaction outside the stated class, with its domain and positive energy already identified.

This decision applies to the tested program of boundary additions. It does not rule out distributed interactions that alter the modular core, a different asymptotic geometry, or a well-defined singular continuum coupling. None of those mechanisms has been constructed here.

## 2. The global reference channel and the required tangent

Use the existing exact-one-form modular benchmark

\[
 K(p)=K_{1/2}(p)=\frac{\xi(p)}{\xi(p+1)},\qquad
 K_{\beta/2}(p)=
 \frac{\xi(p+(1-\beta)/2)}{\xi(p+(1+\beta)/2)}.
\]

The [modular Hodge note](MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md) specifies its geometry, fixed output orientation and ordinary radiation normalization. Its fixed-shift causality uses the known half-shift innerness result; compare [Suzuki, Sections 1.2–1.4 and Theorem 2.2](https://arxiv.org/html/1204.1827). This known reference is an input to the present test, not a new derivation of arithmetic positivity.

The positive-real high-frequency behavior is

\[
 K(p)\sim\sqrt{2\pi}\,p^{-1/2},\qquad
 K_{\beta/2}(p)\sim(2\pi/p)^{\beta/2}.                        \tag{1}
\]

Writing
\[
 a_{1/2}(p)=\frac{\xi'(p)}{\xi(p)}
                 +\frac{\xi'(p+1)}{\xi(p+1)},
\]
the necessary beta tangent is

\[
 T_{\rm arith}(p)=
 \left.\partial_\beta\log K_{\beta/2}(p)\right|_{\beta=1}
 =-\tfrac12a_{1/2}(p)
 =-\tfrac12\log\frac{p}{2\pi}+O(p^{-1}).                    \tag{2}
\]

Physical radiation time and inverse temperature beta are separate variables. All asymptotic statements in this note use real \(p\to+\infty\), which is already sufficient to distinguish analytic response functions.

All dynamical times below use the same normalized radiation time conjugate to \(p\). The fixed conversion from physical wave time in the modular note can be absorbed into one consistent choice of energy and temperature units. A different fixed time calibration changes the transition-frequency constants, not the high-frequency powers or the exclusion.

At a regular exterior cusp port retain the common reference delay
\[
 r_b(p)=e^{-bp}K(p),\qquad b>0.
\]
The arithmetic comparison at that port is \(e^{-bp}K_{\beta/2}(p)\). The case \(b=0\) below is the favorable algebraic zero-extra-lead control used in the earlier cusp test; it is not asserted to be the chosen regular geometric cross-section.

## 3. Native probes that exchange thermal energy

On the two-place occupation space take

\[
 H_S=\sum_{\ell=2,3}\epsilon_\ell N_\ell,\qquad
 \epsilon_\ell=\log\ell,\qquad
 \rho_\beta=\bigotimes_{\ell=2,3}(1-q_\ell)q_\ell^{N_\ell},
 \quad q_\ell=e^{-\beta\epsilon_\ell}.
\]

The multiplicative isometry raises the occupation:
\[
 v_\ell|m\rangle=|m+1\rangle,\quad
 v_\ell^*v_\ell=I,\quad v_\ell v_\ell^*=I-P_\ell,
 \quad [H_S,v_\ell]=\epsilon_\ell v_\ell.
\]

Choose the bounded self-adjoint probe
\[
 B_\ell=v_\ell+v_\ell^*,\qquad \|B_\ell\|\le2.
\]
It does not commute with \(H_S\). A real boundary effort \(U(t)\) drives the microscopic probe through
\[
 H_{\rm probe}(t)=H_S-U(t)\sum_\ell g_\ell B_\ell.            \tag{3}
\]
For bounded real \(U(t)\), the instantaneous perturbation is bounded and self-adjoint on the original domain of \(H_S\). This is an actual occupation-changing interaction, unlike the stationary primitive projections used in the preceding delay model.

We calculate its **linear response around the uncoupled Gibbs state**. With the sign convention in (3), the retarded susceptibility is
\[
 \chi_{\ell,\beta}(t)
 =i\,1_{t>0}\operatorname{Tr}
       \rho_\beta[B_\ell(t),B_\ell(0)].
\]
The general retarded-response formalism originates in [Kubo](https://www.jstage.jst.go.jp/article/jpsj1946/12/6/12_6_570/_article/-char/en); the mixed-state spectral and Laplace representation is also set out by [Giesbertz](https://arxiv.org/abs/1601.00747). The following specialized calculation is direct.

Since
\[
 B_\ell(t)=e^{i\epsilon_\ell t}v_\ell+
                e^{-i\epsilon_\ell t}v_\ell^*,
\]
one has
\[
 [B_\ell(t),B_\ell(0)]
      =-2i\sin(\epsilon_\ell t)P_\ell.
\]
Consequently

\[
 \boxed{\quad
 \chi_{\ell,\beta}(t)=
       2(1-q_\ell)\sin(\epsilon_\ell t)1_{t>0},\qquad
 \chi_{\ell,\beta}(p)=
       \frac{2\epsilon_\ell(1-q_\ell)}
            {p^2+\epsilon_\ell^2}.\quad}                   \tag{4}
\]

The factors \(1-\ell^{-\beta}\) are native and positive. The \(\log\ell\) labels in (4) are transition frequencies. They are not silently identified with flight delays; the global modular core already supplies its own arithmetic delays.

Measuring the conjugate flow \(I=\sum_\ell g_\ell\,d\langle B_\ell\rangle/dt\) yields the admittance

\[
 Y_\beta(p)=\sum_{\ell=2,3}
        w_{\ell,\beta}\frac{p}{p^2+\epsilon_\ell^2},
 \qquad
 w_{\ell,\beta}=2g_\ell^2\epsilon_\ell(1-q_\ell)>0.          \tag{5}
\]

For \(\Re p>0\), each summand is positive real, since
\[
 \frac{p}{p^2+\epsilon^2}
   =\frac12\left(\frac1{p-i\epsilon}+\frac1{p+i\epsilon}\right).
\]

As a useful control, replacing the Bost–Connes isometry by the usual bosonic annihilation/creation ladder gives \([a,a^*]=I\), hence susceptibility \(2\epsilon/(p^2+\epsilon^2)\), independent of beta. Ordinary harmonic modes alone therefore supply no temperature variation of their coherent linear response. The bounded isometry probe in (4) does supply variation; the question is whether that variation has the required structure.

## 4. Conservative linear realization and its microscopic scope

At fixed beta, (5) has an exact conservative oscillator realization. The common nonnegative strength \(\lambda\) corresponds to replacing each microscopic coupling \(g_\ell\) in (3) by \(\sqrt\lambda\,g_\ell\):

\[
 \ddot x_\ell+\epsilon_\ell^2x_\ell
       =\sqrt{\lambda w_{\ell,\beta}}\,U,\qquad
 I=\sum_\ell\sqrt{\lambda w_{\ell,\beta}}\,\dot x_\ell,
 \qquad \lambda\ge0.                                      \tag{6}
\]

With zero initial **coherent perturbation**,
\[
 E_{\rm load}=\frac12\sum_\ell
        (|\dot x_\ell|^2+\epsilon_\ell^2|x_\ell|^2),\qquad
 \dot E_{\rm load}=\operatorname{Re}(\bar U I).              \tag{7}
\]

Thus the effective load is a positive dynamical system that stores and returns energy. It is not an assigned arithmetic filter; all its frequencies and thermal weights came from (3)–(5).

There are two distinct exactness statements. Formula (4) is the exact Kubo susceptibility of the specified uncoupled thermal probe. Equations (6)–(7) are an exact linear realization of that susceptibility. Identifying their closed-loop response with the full microscopic quantum system at finite coupling would require deriving the interacting equilibrium state, radiative dressing and fluctuation channels. That stronger identification is not made here. The linear boundary model is the specified candidate being tested, and its first weak-coupling response is the natural susceptibility test of (3).

In particular, a finite-temperature probe is not noiseless:

\[
 \langle B_\ell(t)B_\ell(0)\rangle_\beta
       =e^{-i\epsilon_\ell t}+q_\ell e^{i\epsilon_\ell t},
\]
\[
 \tfrac12\langle\{B_\ell(t),B_\ell(0)\}\rangle_\beta
       =(1+q_\ell)\cos(\epsilon_\ell t),\qquad
 \frac{1+q_\ell}{1-q_\ell}
       =\coth(\beta\epsilon_\ell/2).                        \tag{8}
\]

The energy identity (7) concerns the coherent perturbation. It must not be used to claim that the full quantum output intensity of an initially excited thermal sector is bounded by a noiseless incident signal alone. A microscopic model would account for emitted fluctuations and the corresponding change of internal thermal energy. The present structural exclusion is already visible in the coherent response and does not require suppressing these fluctuations.

## 5. Connection to the unchanged global modular channel

Use the established output orientation in which the measured core response is \(r=r_b\), while the physical reflected wave has the opposite sign. Let \(f,g\) be the external incident and measured outgoing amplitudes, and let \(a,ra\) be the incident and measured outgoing amplitudes of the core. Connect the load in parallel at the common effort:

\[
 U=f-g=a-ra,\qquad
 f+g=a+ra+I,\qquad I=\lambda Y_\beta U.                    \tag{9}
\]

These are reciprocal effort-continuity and flow-addition conditions. They imply
\[
 f=a+\tfrac12 I,\qquad g=ra+\tfrac12 I.
\]
Eliminating the internal amplitudes gives

\[
 \boxed{\quad
 S_{\beta,\lambda,b}(p)
 =\frac{r_b(p)+J_\beta(p)(1-r_b(p))}
        {1+J_\beta(p)(1-r_b(p))},\qquad
 J_\beta=\frac{\lambda Y_\beta}{2}.
 \quad}                                                   \tag{10}
\]

The factor of two is fixed by the port normalization, not fitted to the target. This extends the earlier scalar cusp load to a dynamical thermal admittance. The full \(\xi(p)/\xi(p+1)\) stays inside (10).

The connection has an ordinary coherent energy identity. Since
\[
 |f|^2-|g|^2
   =|a|^2-|ra|^2+\operatorname{Re}(\bar U I),
\]
integration to time \(L\) yields

\[
 \|f\|_{(0,L)}^2-\|g\|_{(0,L)}^2
 =E_{\rm load}(L)
   +\bigl(\|a\|_{(0,L)}^2-\|ra\|_{(0,L)}^2\bigr)\ge0.       \tag{11}
\]

Here \(ra\) means the causal core output. The last nonnegative term is the radiation deficit of the already established core. By its causal isometry it equals the later output energy for the core input stopped at \(L\). No positivity of the unknown variable-shift target is assumed.

Analytic passivity follows independently. The core admittance
\[
 M_r=\frac{1+r}{1-r}
\]
is positive real in the right half-plane. Adding \(\lambda Y_\beta\) preserves this property, and its Cayley transform is (10). Hence (10) is analytic and contractive there. Equivalently, if \(N,D\) are its numerator and denominator,

\[
 |D|^2-|N|^2
 =1-|r|^2+\lambda\operatorname{Re}Y_\beta\,|1-r|^2\ge0.     \tag{12}
\]

For the undamped finite oscillator load, boundary modulus is one away from isolated resonance expressions, with the scattering limit taken at those points. This is a statement about the effective coherent linear system, subject to the microscopic distinction in Section 4.

## 6. Finite response spectral mass fixes the leading exponent

The high-frequency restriction is not peculiar to the chosen two transitions.

**Proposition: regular parallel-load front rigidity.** Let the unchanged zero-extra-lead core satisfy \(K(p)\sim c\,p^{-1/2}\), \(c>0\), on the positive real axis. Let a passive load have admittance
\[
 Y(p)=\int_{(0,\infty)}
           \frac{p}{p^2+\Omega^2}\,d\nu(\Omega),
 \qquad \nu\ge0,\quad C:=\nu((0,\infty))<\infty.            \tag{13}
\]
For any fixed finite \(\lambda\ge0\), its parallel connection (10) satisfies
\[
 S(p)=K(p)+\frac{\lambda C}{2p}+o(p^{-1}),
 \qquad S(p)\sim c\,p^{-1/2}.                              \tag{14}
\]
In particular, it cannot equal \(K_{\beta/2}\) for any fixed \(0<\beta<1\).

**Proof.** For positive \(p\),
\[
 0\le pY(p)=\int\frac{p^2}{p^2+\Omega^2}\,d\nu(\Omega)\le C.
\]
Dominated convergence gives \(pY(p)\to C\). Direct subtraction in (10) gives
\[
 S-K=\frac{(\lambda Y/2)(1-K)^2}
                  {1+(\lambda Y/2)(1-K)}.
\]
Since \(K\to0\) and \(Y\sim C/p\), (14) follows. The ratio of (14) to the target leading term in (1) tends to zero for \(0<\beta<1\), rather than to one. If \(C=0\), the load is zero and the same exclusion is immediate.

The assumption in (13) has a native thermal meaning. For a self-adjoint probe \(B\), write its transition spectral measure as
\[
 d\nu_\beta(\Omega)
 =\sum_{E_n>E_m}
   2(E_n-E_m)(\rho_m-\rho_n)|B_{mn}|^2
       \delta_{E_n-E_m}(d\Omega).
\]
The Gibbs weights decrease with energy, making this a positive measure. When the sum converges,
\[
 C_\beta=\operatorname{Tr}\rho_\beta[B,[H_S,B]].            \tag{15}
\]
The same paired-state expansion gives \(Y_\beta=p\chi_\beta\) in the form (13).

For a finite linear combination of native isometries, their adjoints and finite products, the energy jumps are bounded and the necessary commutators are bounded. Therefore (15) is finite. For the explicit two-prime probe,
\[
 C_\beta=2\sum_{\ell=2,3}g_\ell^2\log\ell\,(1-\ell^{-\beta}).
\]
The occupation space is infinite; no artificial occupation cutoff is used in this argument. Countably many transition frequencies also remain excluded if their total response spectral mass is finite.

Boundedness of an arbitrary operator \(B\) alone is **not** asserted to imply finite (15) for an unbounded Hamiltonian. The energy regularity or the spectral-mass assumption is essential. This is not a theorem about every self-adjoint coupling to the modular system, every bounded operator, or every passive boundary admittance.

At a physical exterior port \(b>0\) and \(C>0\), the fixed delayed core is exponentially small as \(p\to+\infty\), while
\[
 S_{\beta,\lambda,b}(p)\sim\frac{\lambda C_\beta}{2p}
 \quad(\lambda>0).
\]
Thus the load produces a prompt response at the port, before the common reference delay of \(e^{-bp}K_{\beta/2}\). The favorable \(b=0\) control already fails by (14); using the regular exterior port does not repair it.

## 7. Calibration at the half shift and the logarithmic tangent

An active added load at beta one does not reproduce the bare reference \(K\):
\[
 S_{1,\lambda,0}-K
 =\frac{(\lambda Y_1/2)(1-K)^2}
              {1+(\lambda Y_1/2)(1-K)}\ne0
\]
for nonzero coupling. Temperature variation alone with a fixed added load therefore fails to anchor at the existing half-shift channel.

To give the candidate a more favorable test, allow an additional switch
\[
 \lambda(\beta)=1-\beta,\qquad 0<\beta\le1.
\]
This is an explicitly granted control, not a consequence of the KMS condition. It turns the load off at beta one. A microscopic coupling amplitude would scale as \(\sqrt{1-\beta}\); a differentiable amplitude vanishing at beta one would instead give a zero first response tangent, which also fails (2).

For this calibration the measured one-sided beta tangent is

\[
 T_{\rm native}(p)=
 \left.\partial_\beta\log S_{\beta,1-\beta,0}(p)\right|_{1}
 =-\frac{Y_1(p)(1-K(p))^2}{2K(p)}.                         \tag{16}
\]
Only \(Y_1\) enters at first order, since the switch is zero at the reference. Its actual temperature derivative enters at the next order.

For \(g_2=g_3=1\),
\[
 C_1=\log2+\frac43\log3
       =2.157963565450758\ldots,
\]
\[
 T_{\rm native}(p)\sim
       -\frac{C_1}{2\sqrt{2\pi}}p^{-1/2},
 \qquad
 \frac{C_1}{2\sqrt{2\pi}}=0.430451452912066\ldots.           \tag{17}
\]
No nonzero constant calibration of the switch can turn this into the logarithmic behavior in (2).

| \(p\) | Native calibrated beta tangent | Required beta tangent |
|---:|---:|---:|
| 4 | -0.00829133535 | -0.18017398910 |
| 16 | -0.02298548304 | -0.57680527944 |
| 64 | -0.02671355563 | -1.18784040183 |
| 256 | -0.01931372941 | -1.86048555036 |
| 1024 | -0.01144961633 | -2.54850631516 |

The table illustrates an analytic exclusion, rather than establishing the asymptotic result by extrapolation.

The short-time version makes the same failure explicit. The inverse load kernel is
\[
 y_1(u)=\sum_\ell w_{\ell,1}\cos(\epsilon_\ell u)\,1_{u>0},
\]
with \(y_1(0+)=C_1\). If \(k\) is the half-shift core kernel, the calibrated transfer tangent has kernel
\[
 -\tfrac12y_1*(\delta-2k+k*k).
\]
Since \(k(u)\sim\sqrt2\,u^{-1/2}\), this tangent tends to the finite value \(-C_1/2\) at the front. The required arithmetic transfer tangent instead has
\[
 \left.\partial_\beta k_{\beta/2}(u)\right|_{\beta=1}
 \sim\frac1{\sqrt2}u^{-1/2}
       [\log u+\log(2\pi)-\psi(1/2)].                      \tag{18}
\]
The native regular correction cannot change this singular exponent. It is therefore unnecessary to proceed to the prime-echo matching tests for this class.

Two supplementary checks are consistent with this conclusion. First, the native positive transition frequencies give \(Y_\beta(p)=O(p)\) at \(p=0\), so \(S_{\beta,\lambda,0}'(0)=K'(0)\) for every fixed finite coupling. The arithmetic slope is \(-2\xi'(s)/\xi(s)\) at \(s=(1+\beta)/2\) and is not a constant function of beta; the record also samples its beta derivative at one. Second, for bounded \(\lambda(\beta)\), the bounded-isometry weights tend to zero as \(\beta\downarrow0\), so \(S_{\beta,\lambda(\beta),0}\) tends pointwise back to \(K\), not to the required identity. Neither supplementary observation is needed for the front-rigidity proof.

## 8. What a possible escape would have to change

As a diagnostic only, solve the first-order matching equation for the load that an added parallel branch would need under the favorable switch:

\[
 Y_{\rm required}^{(1)}(p)
       =\frac{a_{1/2}(p)K(p)}{(1-K(p))^2}
       \sim\sqrt{2\pi}\,p^{-1/2}\log\frac{p}{2\pi}.         \tag{19}
\]

In particular \(pY_{\rm required}^{(1)}(p)\to+\infty\), whereas every load in (13) has \(pY(p)\to C<\infty\). Formula (19) is an acceptance test, not an independently derived physical admittance. Its global positive-real property has not been established and must not be presumed from its positive large-real-\(p\) asymptotic.

An infinite-spectral-mass continuum can be meaningful in other passive models; finite mass is not a universal law of physics. Such a proposal would need its own domain, boundary normalization, energy identity and coupling derivation. Similarly, an interaction that changes the bulk/asymptotic propagation is outside the fixed-core parallel architecture. The present result identifies these as departures from the tested construction, not as existing solutions.

The research decision is to stop incremental modifications of the regular finite-place boundary load. The coefficient dictionary remains a useful separate result, but it no longer supplies a sufficiently concrete lead for the main positivity effort.

The next main arithmetic task should return to the complete transfer and seek a cumulative storage identity on the first arithmetic window \(\log2<L<\log3\), as proposed in the [earlier research assessment](RESEARCH_AVENUES_20260923.md). There the exact kernel contains its full archimedean term and first translated copy, so the energy cross terms can be exposed without imposing a globally passive finite Euler product. A positive storage formula must be derived from independently specified state variables; numerical positivity or a norm defined by the desired transfer would not satisfy that task. No new storage identity is claimed in this addendum.

## 9. Numerical checks and provenance

The completed diagnostic has **203 passing floating controls**, using Python 3.10.0, mpmath 1.3.0 and 60 decimal digits. Occupation sums run through 400, with explicit omitted-mass bounds for the bounded probe. Their matrix elements use the actual infinite-ladder action, not a truncated creation matrix whose artificial top state changes the commutator.

The checks reproduce native correlations, the retarded Laplace response, the double-commutator sum rule, the bosonic temperature-independent control and the fluctuation/response ratio. Oscillator work is integrated from its driven trajectory and compared with stored energy. Independent boundary equations are solved and checked against (10), the flux identity and right-half-plane contractivity for the full modular response. Further controls cover the finite spectral-mass bound, preserved high-frequency exponent, calibrated tangent, prompt exterior-port response, low-frequency slope and hot endpoint.

The numerical tables do not prove a general spectral theorem or asymptotic statement. Those conclusions follow from the displayed algebra, positive spectral measure and dominated-convergence argument. No interval certificate, zero table, external numerical dataset, sibling-program import or nonlinear microscopic scattering simulation is used.

From the parent Wilson–Loewner directory, with Python 3 and mpmath available:

    python3 -B WZW/numerics/check_thermal_boundary_structure.py --output /tmp/thermal-boundary-structure-replay.json

The compact record binds the program by SHA-256. Earlier suites remain separate and unchanged. The analysis and audit are by the same assistant; no independent specialist review or novelty claim for the Kubo/sum-rule machinery is made.
