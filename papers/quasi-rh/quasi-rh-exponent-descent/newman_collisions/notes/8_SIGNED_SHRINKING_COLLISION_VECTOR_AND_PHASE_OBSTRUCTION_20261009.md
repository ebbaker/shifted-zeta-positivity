# Signed shrinking-time collision vector and phase obstructions

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model audits are internal checks, not independent validation.

This continues the [heat integration handoff](../../reviews/HEAT_MANUSCRIPT_INTEGRATION_REVIEW_20261009.md).
The bounded task was a uniform, error-paid joint value/derivative inequality
in the regime below, or a precise obstruction to the chosen mechanism.
The present result pays the errors and proves two obstructions: genuine
adjacent cutoff terms defeat packetwise diagonal coercivity, and independent
phase relaxation admits an exactly zero joint vector with the exact weights
and derivative frequencies. It does not exclude collisions of the heat
function. The remaining input is an inequality using the actual arithmetic
phase correlations of the complete sum.

## 1. Scaling, fixed cutoff, and fixed-time derivatives

Put

\[
1\le\kappa\le2,\qquad 0<t\le1/20,\qquad
L=\kappa/t,\quad x=4\pi e^L,\quad R=L^{-1},\quad
N=\left\lfloor\sqrt{e^L+t/16}\right\rfloor.                 \tag{1}
\]

At each such parameter point, hold **both time and the integer cutoff fixed**
when differentiating in the spatial variable. A derivative along the curve
\(x=4\pi e^{\kappa/t}\) is not the derivative in the collision equation.
All limiting statements below are uniform in \(\kappa\in[1,2]\).

Use the manuscript's symmetric normalizer \(A_t\), exact normalized function
\(Q_t=H_t/A_t\), and holomorphic fixed-cutoff approximant \(F_{t,N}\).
The normalizer has no zeros, so \(H_t=H_t'=0\) is equivalent to
\(Q_t=Q_t'=0\). The input is
[Polymath, Theorem 1.3, equations (20)--(24)](https://arxiv.org/html/1904.12438v2#S1.Thmtheorem3),
with the disk/reflection/cutoff deductions proved in
[Heat Note 3](3_NORMALIZED_HEAT_COLLISION_CRITERION_20261008.md) and
[the stable manuscript, Section 5](../newman_collision_reductions.tex).
No conjectural zeta bound or numerical zero information is imported.

Define the three exponent functions

\[
\mathfrak a(\kappa)=\frac{\kappa(4-\kappa)}{16},\qquad
\mathfrak b(\kappa)=\frac{\kappa(\kappa+4)}{16},\qquad
\mathfrak d(\kappa)=\frac{\kappa(\kappa+12)}{16}.
                                                               \tag{2}
\]

Then \(\mathfrak a+\mathfrak b=\kappa/2\),
\(\mathfrak d-\mathfrak b=\kappa/2\), and
\(\mathfrak d=\kappa-\mathfrak a\).

## 2. Complete exponentially small error payment

**Proposition 1.** In (1), the manuscript's positive full-disk majorant
\(\eta_N\), with center \(x\), radius \(R\), and
\(\varepsilon=\tau=t\), satisfies

\[
\eta_N\le5e^{-\mathfrak b(\kappa)/t},\qquad
|Q_t(x)-F_{t,N}(x)|\le\eta_N,\qquad
|Q_t'(x)-F_{t,N}'(x)|\le L\eta_N.                \tag{3}
\]

These estimates include the upper-half approximation, conversion to the
symmetric normalizer, lower-half reflection, every possible integer-cutoff
change, and the Cauchy derivative error.

Here is a ledger proving the numerical constant in (3). Symbols
\(q_\pm,\alpha_-,K_*,V_n,P_n,U_n,E_m^{AB},E_m^C\) have exactly the
definitions in Section 5.2 of the manuscript. Since \(L\ge20\),
\(x>10^9\), \(e^{L/2}>22001\), and \(R\le1/20\), elementary bounds give

\[
|\log q_\pm-L|<10^{-9},\qquad
|\alpha_- -L/2|<10^{-9},\qquad K_*<1.3.          \tag{4}
\]

For example \(|\log q_\pm-L|\le2R/x\);
\(A_*/L<.502\), \(D_*<1.01/x\), and
\(K_*=\exp(RA_*(1+tD_*/2)/2)<1.3\).
The permitted natural cutoffs are \(m_-,m_+\), with
\(m_+-m_-\le1\), \(m_-\ge22000\), and the center cutoff \(N\) is among them.
Every correction index \(j\) thus obeys
\(|\log j-L/2|<10^{-4}\). Substitution into its exact majorant gives

\[
\log P_j\le-\mathfrak b/t+.251,\qquad
2\sum_{\text{cutoff correction}}P_j\le2.6e^{-\mathfrak b/t}.
                                                               \tag{5}
\]

The positive exponent corrections in \(E_m^C\) are less than .001:
the first is at most \(2.5/(22000-.125)\), and the second is bounded
using the decrease of \(L/e^L\) for \(L\ge20\). The perturbation from
\(\log q_-\) to \(L\) is less than \(10^{-9}\). Therefore

\[
E_m^C\le1.01e^{-\mathfrak b/t}.                  \tag{6}
\]

For completeness, the many-term absolute sum used to pay the **error**, not
the arithmetic collision vector, obeys

\[
\sum_{n\le m}V_n\le5e^{\mathfrak a/t},\qquad
1+m^{k_*}n^R<2.7,\qquad U_n\le.9/x.            \tag{7}
\]

To prove the first bound, compare the decreasing weight with its integral.
Writing \(n=e^{L/2-v}\) gives, apart from the less-than-\(10^{-8}\)
relative correction in (4),

\[
e^{\mathfrak a/t}\int_0^{L/2}e^{-v/2+tv^2/4}\,dv
\le4e^{\mathfrak a/t}.                         \tag{8}
\]

Here \(tv\le\kappa/2\le1\), so the integrand is at most
\(e^{-v/4}\). The first summand and the at-most-one edge interval fit
in the reserve from four to five, since \(\mathfrak a/t\ge15/4\).
The weight is decreasing because its logarithmic slope is at most
\(-1/2+3\cdot10^{-6}\). For the second bound in (7),
\(n^R\le e^{1/2+5\cdot10^{-6}}\) and
\(m^{k_*}\le e^{10^{-9}}\). For the third,
\(t^2\ell_n^2/16\le1/4+10^{-8}\), so the numerator in the
definition of \(U_n\) is at most \(.87600001\);
\(x>10^9\) allows the relaxed bound \(.9/x\).
Consequently, using \(\pi>3.14\),

\[
E_m^{AB}\le\frac{5(2.7)(.9)}{4\pi}e^{-\mathfrak d/t}
<e^{-\mathfrak d/t}\le.01e^{-\mathfrak b/t}.     \tag{9}
\]

The last comparison uses \(\kappa/(2t)\ge10\).
Combining (4)--(9) in the defined full-disk majorant gives

\[
\eta_N\le1.3(1.01+2.6+.01)e^{-\mathfrak b/t}
<5e^{-\mathfrak b/t}.
\]

The holomorphic remainder estimate and real symmetry supply the complete
disk estimate; Cauchy's formula on radius \(R\) gives its derivative at the
center. This proves (3), including points arbitrarily near a cutoff crossing.
No derivative of a jumping cutoff was taken.

The asymptotic ledger is also informative:

\[
K_*\longrightarrow e^{1/4},\quad E_m^C\asymp e^{-\mathfrak b/t},
\quad P_{N+O(1)}\asymp e^{-\mathfrak b/t},\quad
E_m^{AB}=O(e^{-\mathfrak d/t}).                 \tag{10}
\]

Thus a single cutoff coefficient is exponentially small, although a whole
endpoint block has exponentially large absolute mass. The raw derivative
error in (3) still tends to zero: uniformly it is at most
\(10t^{-1}e^{-5/(16t)}\).

## 3. Genuine phases and the exact paid joint inequality

Put \(s=(1-ix)/2\), \(\alpha(s)=\alpha_r+i\alpha_i\), and
\(\alpha'(s)=u+iv\). Set

\[
w_n=\exp\{t\log^2n/4-(1/2+t\alpha_r/2)\log n\},\qquad
\phi_n=\theta_t(x)+(x-t\alpha_i)\log n/2,
\]
\[
r_n=\frac2L\Re\{(\alpha(s)-\log n)(1+t\alpha'(s)/2)\},\qquad
c_n=\frac{tv\log n}{L},\qquad
h_n=(\cos\phi_n,\ r_n\sin\phi_n-c_n\cos\phi_n).
                                                               \tag{11}
\]

All these quantities are exact; \(w_n\) denotes a modulus, not a signed
coefficient. Direct fixed-time differentiation gives

\[
\mathcal V:=\left(F_{t,N}/2,\ 2F_{t,N}'/L\right)
=\sum_{n\le N}w_n h_n.                         \tag{12}
\]

The \(c_n\) term includes amplitude variation and must be retained.
At a genuine collision, (3) gives the necessary joint inequalities

\[
|\mathcal V_1|\le\eta_N/2,\qquad
|\mathcal V_2|\le2\eta_N,\qquad
|\mathcal V|^2\le17\eta_N^2/4
\le\frac{425}{4}e^{-2\mathfrak b/t}.            \tag{13}
\]

Hence the strict reverse of (13), established uniformly for the **actual**
phases, would exclude collisions in this scaling regime. This is a paid
interface; a lower bound for its left side has not been established.

It is possible to display precisely the signed arithmetic which that
bound must keep. With \(\Delta=\phi_n-\phi_m\),
\(\Sigma=\phi_n+\phi_m\), the exact kernel is

\[
\begin{split}
2h_n\cdot h_m={}&(1+r_nr_m+c_nc_m)\cos\Delta
 +(1-r_nr_m+c_nc_m)\cos\Sigma\\
&+(c_nr_m-c_mr_n)\sin\Delta
 -(c_mr_n+c_nr_m)\sin\Sigma.                   \tag{14}
\end{split}
\]

In particular
\(\Delta=(x-t\alpha_i)\log(n/m)/2\) and
\(\Sigma=2\theta_t+(x-t\alpha_i)\log(nm)/2\).
Taking absolute values of the whole tail discards these correlations.
The sum of (14) over all ordered pairs \(n,m\), with all diagonal and off-diagonal terms and weights
\(w_nw_m/2\), equals \(|\mathcal V|^2\).

## 4. Derivative information leaves the endpoint absolute obstruction

The explicit real-axis formulas give

\[
\alpha_r=L/2+O(x^{-2}),\quad
\alpha_i=-\pi/4+O(x^{-1}),\quad u=O(x^{-2}),\quad v=O(x^{-1}),
\]
\[
r_n=1-2\log n/L+O(t/(Lx)+1/(Lx^2)),\qquad c_n=O(t/x)
                                                               \tag{15}
\]

uniformly up to \(N\). These estimates follow directly from

\[
\alpha_r=\tfrac12\log(x/(4\pi))+\tfrac14\log(1+x^{-2})
 -(1+x^2)^{-1},\quad
\alpha_i=3x/(1+x^2)-\tfrac12\arctan x,
\]
\[
u=(7x^2-5)/(1+x^2)^2,\qquad v=x(x^2+5)/(1+x^2)^2.
                                                               \tag{16}
\]

**Proposition 2.** For the last block \(\lceil N/2\rceil\le n\le N\),
let \(q=\log2\). Then

\[
\sum w_n=(C_0+o(1))e^{\mathfrak a/t},\qquad
\sum w_n\sqrt{r_n^2+c_n^2}
=\left(\frac{2t}{\kappa}C_1+o(t)\right)e^{\mathfrak a/t},
                                                               \tag{17}
\]
\[
C_0=\int_0^q e^{-v/2}\,dv=2(1-2^{-1/2})>0,\qquad
C_1=\int_0^q v e^{-v/2}\,dv
=4-(2q+4)2^{-1/2}>0.
\]

Indeed write \(n=e^{L/2-v}\) and use the exact weights (11).
Their mass times the counting differential is
\(e^{\mathfrak a/t}e^{-v/2+tv^2/4}(1+o(1))\,dv\).
On the bounded interval \(0\le v\le\log2\), (15) gives
\(r_n=2v/L+o(1/L)\) and \(c_n=o(1/L)\).
Riemann sums with mesh \(O(e^{-L/2})\) prove (17); the floor and block
endpoint shifts are negligible. Positivity of \(C_1\) follows from its
integral, without subtraction of approximate decimal values.

The second expression in (17) is the phase-independent absolute budget
for the scaled derivative coordinate. Its extra factor \(t\) does not
overcome \(e^{\mathfrak a/t}\); on \([1,2]\),
\(\mathfrak a\ge3/16\). The raw derivative-coordinate budget multiplies
this by \(L/2\) and is asymptotic to \(C_1e^{\mathfrak a/t}\).
Thus a joint value/derivative triangle argument cannot regard this block
as a small perturbation of the leading term. This extends the earlier
value-only absolute-tail diagnostic.

## 5. A genuine-phase adjacent-packet obstruction

**Proposition 3.** Let \(M\) be an integer tending to infinity, and put

\[
x_M=4\pi M^2,\qquad t_M=\kappa/(2\log M),\qquad 1\le\kappa\le2.
                                                               \tag{18}
\]

The natural cutoff is exactly \(N=M\). For the two genuine terms
\(n=M-1,M\), define their diagonal energy and joint packet energy by

\[
D_M=|w_Mh_M|^2+|w_{M-1}h_{M-1}|^2,\qquad
J_M=|w_Mh_M+w_{M-1}h_{M-1}|^2.
\]

Then uniformly in \(\kappa\),

\[
D_M=(2\cos^2(\pi/8)+o(1))w_M^2,\qquad
J_M=O(w_M^2/M^2),\qquad J_M/D_M\longrightarrow0. \tag{19}
\]

This disproves a positive constant lower bound of joint packet energy
by its separate diagonal energy, even for the genuine phases.

To prove it, use the exact branch formula

\[
\theta_t=-\pi+\tfrac14\arctan x+\tfrac x4(1-L)
-\tfrac x8\log(1+x^{-2})+\tfrac t2\alpha_r\alpha_i.
\]

At (18), \(L=2\log M\), so

\[
\phi_M=\pi M^2-7\pi/8+O(M^{-2}),\qquad
\phi_M-\phi_{M-1}
 =2\pi M+\pi+O(M^{-1}).                       \tag{20}
\]

The second expansion follows from
\(-\log(1-1/M)=M^{-1}+(2M^2)^{-1}+O(M^{-3})\)
and \((x-t\alpha_i)/2=2\pi M^2+O(t)\).
Consequently the two cosines have opposite signs up to \(O(M^{-1})\),
and each squared cosine tends to \(\cos^2(\pi/8)\).
The exact weights obey

\[
w_M=M^{-(4+\kappa)/8}(1+o(1)),\qquad
w_{M-1}/w_M=1+O(M^{-1}).                       \tag{21}
\]

Moreover (15) yields
\(r_M=O(t/(LM^2)+1/(LM^4))\),
\(r_{M-1}=O(1/(ML))\), and \(c_n=O(t/M^2)\).
The value coordinate of the packet is \(O(w_M/M)\); its scaled
derivative coordinate is \(O(w_M/(ML))\). This proves (19).
In the energy expansion the adverse cross term satisfies

\[
2w_Mw_{M-1}h_M\cdot h_{M-1}
=-D_M+O(w_M^2/M^2).                            \tag{22}
\]

It therefore nearly cancels the two diagonal contributions.

The same conclusion holds for any fixed finite set of bounded spatial
translations of this packet, keeping time and its two indices fixed.
For \(|h|\le H\), (20) acquires only \(O_H(M^{-1})\) errors and (21)
keeps the same bounds. Summed energy for \(m\) fixed translated probes is
\(O_{H,m}(w_M^2/M^2)\), whereas the corresponding diagonal energy is
\((2m\cos^2(\pi/8)+o(1))w_M^2\). Carrier-scale translations \(h=O(1/L)\)
are included. Thus this particular packetwise coercivity mechanism is
not restored by a fixed collection of such probes.

This statement concerns a packet, not the complete sum or \(H_t\).
The packet is itself on the exponentially small edge-coefficient scale.
It does not assert that a complete signed estimate, averaging over a
larger range, or translated probes using arithmetic correlations fail.

## 6. Exact joint zeros after independent phase relaxation

**Proposition 4.** There is \(t_0>0\) such that for every
\(0<t<t_0\), \(\kappa\in[1,2]\), and the exact weights, frequencies,
and cutoff in (1), phases \(\psi_n\) exist with

\[
\psi_1=\theta_t(x),\qquad
\sum_{n\le N}w_n(\cos\psi_n,\ r_n\sin\psi_n-c_n\cos\psi_n)=0.
                                                               \tag{23}
\]

Hence no strictly positive lower bound for this joint vector can hold
for every independent choice of coefficient phases, even with the leading
phase and all exact derivative data fixed.

Here is an elementary proof. For sufficiently small \(t\), (15) and
the weight formula imply simultaneously, uniformly in \(\kappa\),

\[
\max_{n\le N}|r_n|\le1.01,\quad w_{257}\le.02,\quad
|r_1-1|\le.005,\quad
\max_{n\le256}\sqrt{c_n^2+(r_n-1)^2}\le.01,     \tag{24}
\]
\[
4.5\le S:=\sum_{n=2}^{256}w_n\le16,\qquad w_2\le.61.
\]

For fixed \(n\), \(w_n\to n^{-\sigma}\) with
\(\sigma=1/2+\kappa/4\in[3/4,1]\).
The limiting lower head sum is at least \(H_{256}-1>4.5\), and
the limiting upper sum is at most
\(\int_1^{256}u^{-3/4}du=12\); these give the reserved bounds.
The exact logarithmic slope
\(-1/2-t\alpha_r/2+t\log n/2\) is negative up to \(N\), so the
weights decrease. Thus (24) is a consequence of uniform asymptotics,
not an extra hypothesis. An explicit numerical value of \(t_0\) is not claimed.

For \(n>256\), take \(\psi_n=\pm\pi/2\). Their first coordinate
and amplitude-drift contribution are zero. Greedy signing of the real
numbers \(w_nr_n\) leaves a derivative residual \(d\) of modulus at
most their largest modulus, hence \(|d|\le.0202<.025\).
The leading term has \(w_1=1,c_1=0\); keep its actual phase. The target
to be canceled by the remaining head is

\[
T=(\cos\theta_t,\ r_1\sin\theta_t+d),\qquad .97\le|T|\le1.03.
                                                               \tag{25}
\]

Partition \(2,\ldots,256\) into two groups by always adding the next
weight to the lighter group. Their masses \(A,B\) satisfy
\(A+B=S\), \(|A-B|\le.61\), and
\(A,B\ge(4.5-.61)/2=1.945>|T|\).
Giving a common phase to each group produces two ellipse vectors
\(L_Ae(u)\), \(L_Be(v)\), where \(e(u)=(\cos u,\sin u)\) and

\[
\|L_A-AI\|\le.01A,\qquad \|L_B-BI\|\le.01B.
\]

Indeed their matrices have first row \((A,0)\) or \((B,0)\), and
second row \((-\sum w_nc_n,\sum w_nr_n)\).
Writing \(r=|T|\), at \(e(u)=T/r\) one has
\(|T+L_Ae(u)|\ge A+r-.01A>B(1+.01)\).
At \(e(u)=-T/r\), one has
\(|T+L_Ae(u)|\le A-r+.01A<B(1-.01)\).
Both inequalities follow from

\[
r-|A-B|\ge.36>.01(A+B),\qquad A>r.             \tag{26}
\]

The invertible matrix \(L_B\) has singular values between
\(B(1-.01)\) and \(B(1+.01)\). Thus
\(|L_B^{-1}(T+L_Ae(u))|\) is continuous and crosses one.
At a crossing choose \(e(v)=-L_B^{-1}(T+L_Ae(u))\), proving (23).

For clarity, multiply each first analytic term by a constant offset
\(e^{i\delta_n}\) and its reflected term by \(e^{-i\delta_n}\).
This preserves real symmetry and realizes the chosen phases while preserving
the exact local amplitude derivatives and phase frequencies. The offsets
generally destroy the genuine relation
\(\phi_n=\theta_t+(x-t\alpha_i)\log n/2\), including its logarithmic
and multiplicative correlations. Proposition 4 therefore asserts no
collision of the genuine approximant or of the heat flow. It is a theorem
about the independent-phase relaxation of this analytic mechanism.

## 7. Checkpoint and next admissible input

The bounded attempt has reached its obstruction stopping condition.
The errors are fully paid, the value-only absolute-tail obstruction has
been extended to the joint derivative budget, and both a genuine adverse
packet and an exact independent-phase zero have been proved.

A continuation must supply a signed inequality for the complete actual
sum (12), stronger than the collision bound (13), or a comparison
conditioned on both small coordinates which contradicts their genuine
logarithmic phases. Equivalently, with \(D=\sum_nw_n^2|h_n|^2\), a
sufficient signed estimate is

\[
2\sum_{n<m}w_nw_m h_n\cdot h_m>-D+17\eta_N^2/4. \tag{27}
\]

The sum/difference kernel (14) states that input
without discarding its adverse terms. Another independent-phase lower
bound or a packetwise diagonal-dominance argument cannot supply it.
Longer-range correlated probes are left open; no necessary probe range
or endpoint theorem has been proved here.

The [small checker](../../numerics/check_signed_heat_collision_scout.py)
and [record](../../numerics/signed_heat_collision_scout_record_20261009.json)
check finite rational kernel identities, exponent and payment ledgers,
logarithmic expansion reserves, and the uniform ellipse scalar margins.
They evaluate no heat functions, genuine phases, zero grid, or huge cutoff.
Analytic asymptotics, Polymath's theorem, and the full-disk argument remain
mathematical proof inputs. See the
[scoped review](../../reviews/HEAT_SIGNED_SHRINKING_COLLISION_REVIEW_20261009.md).
No manuscript changes, snapshot, commit, RH claim, or novelty claim are made.
