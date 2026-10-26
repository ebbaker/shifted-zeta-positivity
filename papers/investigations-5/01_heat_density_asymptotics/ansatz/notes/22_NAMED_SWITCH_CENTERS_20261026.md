# Named centers at the physical regulator switch

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, base chat0025, thread `01a179ab-8856-7ba0-89a2-500b2d854c80`.
Configuration is read from this turn's source metadata. Contributing
agents supplied same-model analytical checks; this is not independent
specialist validation.

**Status: proved in-note from named inputs, at the compact high-height
comparison scope; same-model internal assessment only.** This executes
[HDA-A03-AN01 r1](../research-progress/handoffs/HDA-A03-AN01.md).
Every named one-arm center below differs from the exact historical linear
center by o(1/(X log X)). The corrected centers have an explicit earlier
shift of order 1/(X² log X); the uncorrected elementary center has a later
shift of order 1/(X² log²X). Even a fixed factor two changes the center by
only order 1/(X log²X), although this is larger than the curvature shifts.
The existing density-layer error is not sharpened by these statements.

Read the [result index](../../../../../result-summaries/README.md),
[heat-flow results](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../../avoid/README.md), specifically
[classification01](../../../../../avoid/01_restating_the_target.md),
[signed payments12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
[scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[status19](../../../../../avoid/19_status_files_that_lag_the_findings.md)
and [gain20](../../../../../avoid/20_volume_without_a_gain.md).
This is quantitative approximation, not an RH criterion. [Inputs22](22_NAMED_SWITCH_CENTERS_INPUTS_20261026.json)
pins the working-tree inputs; the [work record](../numerics/A03_AN01_ANALYTICAL_WORK_RECORD_20261026.json)
records final evidence identities and housekeeping checks. No numerical, sampling, machine-symbolic,
exact-arithmetic or interval research was run.

## 1. Fixed contract and actual compact input

Fix ell,h,eta>0 and observation |y|<=1. Put r=ell+2, b=1+h+2,
and use the full rectangles |Re z-X|<=r, |Im z|<=b with one further
analytic unit. Throughout 63<=t<=65 and X tends to positive infinity;
evenness gives the opposite-height charts. Constants and finite onsets
may depend on these fixed data. Set

\[
L=\log(X/(4\pi)),\quad \lambda=\log X,\quad \Lambda=1+\lambda,
\quad s_X=(1+iX)/2,
\]
\[
M(w)=w(w-1)\pi^{-w/2}\Gamma(w/2)/16,\quad\alpha=M'/M.
\tag{NC1}
\]

The complete canonical H, H_t=-H_zz and H(0,z)=xi((1+iz)/2)/8
are unchanged. So are physical q=epsilon_g² and K=k_ell k_h,
unnormalized density/current, additive potentials and actual covariance.
We do not use an eventual large-t theorem at t=64. The input here is
the actual compact theorem in [Ansatz Note20](20_COMPACT_POSITIVE_FIELD_BRIDGE_20261026.md),
RB1--13, itself using the fixed-order theorem of
[Note19](19_ARBITRARY_FIXED_POSITIVE_TIME_ORDER_20261026.md).
Its P4 bound is C A Lambda^d X^-7 for spatial orders 0<=d<=3,
C A Lambda² X^-7 for direct first time, and C A X^-7 for the
actual heat residual. A=|S(s)|+|S(1-s)| is a positive arm envelope.
Every full arithmetic tail, connector, middle and gamma end is included
before absorption; 63 log2/4>7 is the compact arithmetic gate.

Choose a single fixed V=Sigma+3, where Sigma bounds |Re w| for w=s,1-s
on the largest rectangle. In particular Re(w+V)>2. Define

\[
G(t,w)=M(w)e^{t\alpha(w)^2/4},\qquad
J(t,w)=(\pi t)^{-1/2}\int_V^\infty e^{-v²/t}M(w+v)\,dv,
\]
\[
p=w+(t/2)\alpha(p),\quad B=1-(t/2)\alpha'(p),\qquad
S(t,w)=M(p)e^{-(p-w)^2/t}B^{-1/2}.
\tag{NC2}
\]

Use precisely the branch and gates of parent Note30 and compact RB1;
the square root is near one. V is fixed in t and z. The reference J
depends on this decomposition and is not an intrinsic amplitude of H.
On the real axis define positive one-arm moduli

\[
A_{lin}=|G(t,s_X)|,\quad A_J=|J(t,s_X)|,\quad A_S=|S(t,s_X)|,
\]
\[
A_0=|C_+(t,X)|=A_o(t,X)/2,\quad
A_1=|C_+(t,X)(1+D_+(t,X))|.
\tag{NC3}
\]

C_pm and D_pm are exactly RB6 of Note20, including unwrapped phase
7pi/8 and b_pm=Log(z/(4pi))/2 ± i pi/4. For the fixed P4 model one
may also take A_4=|S(t,s_X)(1+C2+C4)(t,s_X)|, with the finite
coefficients of Note19 FO8. All these arms are nonzero after an onset:
their ratios to nonzero G or C tend to one. No logarithm of H or of a
vanishing cosine is taken.

## 2. Paid amplitude and direct time comparisons

From compact RB8/RB11, on the full larger holomorphic buffers,

\[
\log(J/G)=U+O(\Lambda^4/X²),\quad
\log(S/G)=U+O(\Lambda^4/X²),\qquad
U=t\alpha'/4+t²\alpha²\alpha'/8.
\tag{NC4}
\]

The logarithms are the branches of the near-one ratios. The direct
time remainder in either identity is O(Lambda^6/X²). This is established
by differentiating the fixed Gaussian kernel for J, and the exact
implicit identity for S, as in RB8a/RB11. It is not a derivative of an
O allowance. To recall the payments: gamma cubic/quadratic-square error
is C Lambda^4/X²; arithmetic is C X^(-t log2/4); original middle and
missing lower Gaussian are C exp(-2L²+C(1+L)); both infinite gamma ends
are C exp(-c X^(2/3)). Their direct kernel derivatives retain the same
exponentials with at most two additional logarithmic moment powers.

The sectorial gamma inputs are CB4 of
[Note03](03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md).
Their primary source, [DLMF5.11](https://dlmf.nist.gov/5.11), was rechecked
on 26 October 2026 for its sector and logarithm conventions. With
b_+=L/2+i pi/4 on the real axis,

\[
\log M(s_X)=\log C_+(0,X)+i/(24X)+O(X^{-2}),
\]
\[
\alpha(s_X)=b_+-7i/(2X)+O(X^{-2}),\quad
\alpha'(s_X)=-i/X+O(X^{-2}).
\tag{NC5}
\]

Define g(t)=7pi t/16 and h(t,X)=pi t² L/32. Expanding exact
holomorphic quantities before taking real parts gives

\[
\log(G/C_+)=i/(24X)-7itb_+/(4X)+O(\Lambda/X²),
\]
\[
\Re U=h/X+O(\Lambda²/X²),\quad
\Re D_+=(g+h)/X.
\tag{NC6}
\]

The determinant t alpha'/4 is retained in U; its leading value is
imaginary on the real axis. Also log|1+D|=Re D+O(|D|²), with
|D|<=C Lambda²/X. Consequently Delta_A=log(A/A_lin) satisfies:

| Named modulus A | Delta_A | Direct partial_t Delta_A |
| --- | --- | --- |
| A_0, elementary one arm | -g/X + O(Lambda/X²) | -7pi/(16X) + O(Lambda/X²) |
| A_1, corrected elementary | h/X + O(Lambda^4/X²) | pi t L/(16X) + O(Lambda^6/X²) |
| A_J, fixed truncated gamma arm | h/X + O(Lambda^4/X²) | pi t L/(16X) + O(Lambda^6/X²) |
| A_S, full gamma saddle | h/X + O(Lambda^4/X²) | pi t L/(16X) + O(Lambda^6/X²) |
| A_4, P4 one arm | h/X + O(Lambda^4/X²) | pi t L/(16X) + O(Lambda^6/X²) |

For the last row, FO8 gives C2=O(X^-3), C4=O(X^-5), with direct-time
derivatives of the same orders on this compact t-domain (use
p_t=alpha/(2B), |p| comparable to X, alpha^(j)=O(X^-j)). Thus it is
within the displayed allowance. The real positive exponential rewrite
A_exp=(A_o/2)exp((g+h)/X) has the same corrected row within its paid
error; it is not identified exactly with A_1. Its holomorphic arm is
C_+(t,z) exp([g(t)+pi t² Log(z/(4pi))/32]/z), so its modulus on
real X is A_exp and the later phase comparison applies to it. Replacing any one-arm
modulus A by 2A adds log2 to Delta exactly. In particular A_o=2A_0,
not A_0, and 2A_1 is the corresponding corrected cosine amplitude.

For clarity the full buffered field comparisons being consumed are:

| Two-arm field F | Field error divided by comparable envelope E_o | Spatial jet order d<=3 | Direct first-time error |
| --- | --- | --- | --- |
| G(s)+G(1-s) | C Lambda²/X | C Lambda^(2+d)/X | C Lambda^4/X |
| J(s)+J(1-s) | C e_J | C Lambda^d e_J | C Lambda² e_J |
| S(s)+S(1-s) | C X^-3 | C Lambda^d X^-3 | C Lambda² X^-3 |
| C_++C_- | C Lambda²/X | C Lambda^(2+d)/X | C Lambda^4/X |
| F1=sum C_pm(1+D_pm) | C Lambda^4/X² | C Lambda^(4+d)/X² | C Lambda^6/X² |
| P4 | C X^-7 | C Lambda^d X^-7 | C Lambda² X^-7 |

Here e_J=X^(-t log2/4)+exp(-2L²+C(1+L))+exp(-cX^(2/3));
constants can be enlarged on the fixed compact domain. Choose c>0
smaller once, and enlarge the linear-log middle constant once, to absorb
the polynomial tail weights introduced by kernel differentiation. For J, the exact
decomposition leaves complete ordinary arithmetic and bounded middle;
for S use RB4 with fixed J=0, whose local allowance is X^-3. Spatial
Cauchy disks of radius c/Lambda pay the displayed jet powers. For G,
differentiate its explicit log directly and use H_t=-H_zz plus its
exact residual; for J use the fixed kernel; for F1/P4 use RB9/FO5.
This table preserves the distinction between field error and residual.

In particular the truncated arm has exact forcing

\[
(\partial_t-\tfrac14\partial_{ww})J
 =\frac{e^{-V²/t}}{4\sqrt{\pi t}}
  [M'(w+V)+(2V/t)M(w+V)],
\tag{NC7}
\]

with the superalgebraic lower-Gaussian/middle payment relative to G.
For F1 use the exact RB10 residual; for P4 the exact FO30 identity at
J=2 and its C A X^-7 allowance. None of these fields is declared to
solve the homogeneous heat equation merely because it approximates H.

## 3. Sensitivity on an actual rounding neighborhood

Preserve the historical definition, exactly,

\[
b_{lin}(t,X)=\log(\epsilon_g(t,X)/A_{lin}(t,X)),\qquad
b_{lin}(t_0,X)=0,\quad t_0=t_{c,lin}(X).
\tag{NC8}
\]

The fixed regulator of parent Note20 FB1--2 is
epsilon_b=eta C(1+t²)^(-1/4), C=Phi(0)sqrt(pi)/2, and, above64,

\[
\epsilon_g=E_0(t)e^{-\beta(t)X²/2},\quad
E_0=\epsilon_b^{1-\chi}(M_0/\kappa)^\chi,
\quad\beta=\chi/\kappa.
\tag{NC9}
\]

M0,kappa are the original real source-saddle data of parent Note19;
they are not the gamma factor M or its complex saddle p. For
delta=t-64 in (0,1], the exact flat switch gives

\[
\log\beta=-64/\delta+f(\delta),\qquad
f(0)=1-\log\kappa(64),
\tag{NC10}
\]

where f extends smoothly to0 with its first two derivatives bounded.
Indeed log chi=-64/delta+1/(1-delta/64)
-log(1+exp[-64/delta+1/(1-delta/64)]). The last term is flat at0;
subtract log kappa. Thus directly, without differentiating a center
allowance,

\[
\beta'/\beta=64/\delta²+f',\quad
\beta''/\beta=(64/\delta²+f')²-128/\delta³+f''.
\tag{NC11}
\]

All required derivatives of log E0 are bounded on this fixed interval.
The exact time derivative is

\[
b_{lin,t}=(\log E_0)'-\tfrac12 X²\beta'
                          -\tfrac14\Re\alpha(s_X)².
\tag{NC12}
\]

At64 b is pi X/8+O(Lambda²)>0, and at each fixed small delta>0
it is negative of order X². NC12 is strictly negative in a fixed
sufficiently small right neighborhood of64 for large X: beta'>0,
Re alpha² is positive of order lambda², and (log E0)' is bounded.
This reproves local existence and uniqueness of t0. The equation at
t0 and Stirling imply

\[
\beta(t_0)=\pi/(4X)+O(\Lambda²/X²),\qquad
t_0-64=\frac{64}{\lambda+c_0+O(1/\lambda)},\quad
c_0=\log\frac{4e}{\pi\kappa(64)}.
\tag{NC13}
\]

The second formula locates the neighborhood; it is not substituted for
the exact t0. Set

\[
w_X=128/(\pi X\lambda),\qquad
\mathcal N_M=\{|t-t_0|\le M w_X\},
\tag{NC14}
\]

for each fixed M>0. Uniformly there, delta is comparable to64/lambda.
NC11 yields beta(t)/beta(t0)=1+O_M(lambda/X), and hence

\[
B_0:=b_{lin,t}(t_0,X)
 =-\frac{\pi X\lambda²}{512}[1+O(1/\lambda)],
\]
\[
b_{lin,t}(t,X)=B_0[1+O_M(\lambda/X)],\qquad
|b_{lin,tt}(t,X)|\le C_M X\Lambda^4.
\tag{NC15}
\]

For the last bound log A_lin is affine in t, so its second derivative
is zero; NC11 bounds X² beta''. This supplies neighborhood control
at the physical rounding scale, with the essential X factor. It does
not differentiate JT30 or its O term.

## 4. Centers, finite-height first corrections and error payments

For each named A define b_A=b_lin-Delta_A and its comparison center
t_A by b_A(t_A,X)=0 in N_M. Write m=c X lambda² for a uniform lower
bound on -b_lin,t there, D=|Delta_A(t0)|, and H_A=sup_NM |Delta_A,t|.
All one-arm rows have D+H_A<=C Lambda/X after enlarging the onset;
the same rows multiplied by a fixed positive constant have D=O(1).
At the two endpoints of N_M, b_lin has opposite signs and magnitude
comparable to M lambda, whereas Delta is bounded. Also b_A,t<0.
Therefore each center exists uniquely there, for large enough X.

The mean-value bound |t_A-t0|<=C D/m and Taylor's formula give

\[
\boxed{t_A-t_0=\frac{\Delta_A(t_0,X)}{B_0}
 +O\left(\frac{X\Lambda^4D²}{m³}
                    +\frac{H_AD}{m²}\right).}
\tag{NC16}
\]

To check the error, insert h0=Delta(t0)/B0 into b_lin(t0+h0)-Delta(t0+h0).
Its residual is bounded by C X Lambda^4 h0²+H_A|h0|; division by
the lower derivative bound proves NC16. For unscaled one-arm rows the
nonlinear error is O(X^-4). Substituting NC6 into NC16 gives the actual
finite-height leading corrections

\[
\boxed{t_{A_0}-t_0=-\frac{7\pi t_0}{16XB_0}
       +O(1/(X³\lambda)+X^{-4}),}
\]
\[
\boxed{t_A-t_0=\frac{\pi t_0²L}{32XB_0}
          +O(\Lambda²/X³),\quad A=A_1,A_J,A_S,A_4,A_{exp}.}
\tag{NC17}
\]

Keeping B0 exact avoids imposing its coarser relative 1/logX error on
these finite-height corrections. The elementary center is later; the
corrected centers are earlier. Any pair in the corrected row differs
by O(Lambda²/X³). In particular all obey

\[
\frac{t_{A_0}-t_0}{w_X}
 =\frac{7\pi t_0}{4X\lambda}[1+O(1/\lambda)],
\]
\[
\frac{t_A-t_0}{w_X}
 =-\frac{\pi t_0²L}{8X\lambda}[1+O(1/\lambda)],
\qquad t_A-t_0=o(w_X).
\tag{NC18}
\]

The leading asymptotic forms in NC18 are explanatory; NC17 is the more
accurate paid correction. For the factor-two distinction NC16 instead
gives

\[
t_{2A}-t_A=\frac{\log2}{B_0}
                +O(1/(X²\lambda²)),\qquad
\frac{t_{2A}-t_A}{w_X}
 =-\frac{4\log2}{\lambda}[1+O(1/\lambda)].
\tag{NC19}
\]

It is also sub-width, but only inverse-logarithmically. This shows why
a first curvature correction is useful for arm accuracy without being
necessary merely to achieve o(w_X) centering. A fixed multiplicative
amplitude change and an O(logX/X) logarithmic change have different
center effects and must use the same sensitivity NC15.

All assertions have a finite sufficient onset: impose the compact
branch/source gates of Notes19--20; near-one ratios <1/4; lambda large
enough that 32/lambda<t0-64<128/lambda<1; C_M lambda/X<1/4;
and the displayed derivative/remainder smallness gates. Each follows
eventually from the proved inequalities. No numeric X0, certified
center query or affordable root-finding bound is supplied.

## 5. What the displacement changes in the inherited layer

Parent Note28 JT33 uses exactly t0. Re-expressing its times around a
new center means t=t_A-w_X tau=t0-w_X(tau-(t_A-t0)/w_X).
For bounded tau, NC18 changes its leading normalized density profile
by O(1/X), and NC19 by O(1/logX), since k_h is Lipschitz and
tau -> max(tau,0) is Lipschitz. Both lie within the inherited
O(1/logX) allowance. Thus that inherited resolved law can be restated
around these centers with the same error, but is not sharpened.

There is also a direct paid local layer-change bound. For each actual
holomorphic arm a_A define omega_A=partial_X arg a_A(t,X), retaining
the coherent near-one log; omega_lin=Im partial_X log G. On N_M,
omega_lin is lambda/4+O(1) and b_lin=O_M(lambda). The full-buffer
log ratios of every unscaled one-arm model have size C Lambda²/X.
Cauchy on radius c/Lambda gives

\[
|\omega_A-\omega_{lin}|\le C\Lambda³/X,\quad
|\Delta_A|\le C\Lambda/X.
\tag{NC20}
\]

No derivative of a real modulus allowance is used. With
d_A=max(b_A,0)/omega_A, and L_A=omega_A[k_h(y-d_A)+k_h(y+d_A)]/(2pi),
the Lipschitz bounds and omega_A comparable to lambda give

\[
|d_A-d_{lin}|\le C_M\{ |\Delta_A|/\lambda
                         +|\omega_A-\omega_{lin}|/\lambda\},
\]
\[
|L_A-L_{lin}|\le C_M(|\Delta_A|+|\omega_A-\omega_{lin}|)
                    \le C_M\Lambda³/X=o(1).
\tag{NC21}
\]

Consequently the inherited |R_H-L_lin|<=C implies |R_H-L_A|<=C+o(1)
on this actual switch neighborhood. Multiplying the modulus by two
adds a bounded layer change instead, again leaving the O(1) rate.
These are comparisons of layer expressions, not a new density theorem.
The comparison centers do not redefine the historical t_c,lin in JT26.

The first unpaid improved consumer is a vanishing absolute bound for
R_H-L_A (or a specified next layer profile) with the fixed horizontal
average, corrected phase, finite-period smoothing and adaptive terms
retained. Parent JT24 discarded order-one frozen-profile/unit/rounding
contributions. Small center displacement and X^-7 field error do not
pay that discarded contribution. A different useful consumer is the
actual filtered density/current/time/covariance of the fixed P4 field,
with no replacement by this two-layer shape. That is the next packet
[HDA-A03-AN02 r1](../research-progress/handoffs/HDA-A03-AN02.md).
No direct density-time, current, covariance, forcing, regulator or
spatial-join rate is inferred by differentiating the inherited O(1).

## 6. Controls, disposition and continuation

The complete arithmetic/completed-source premises used above fail for
the controls as follows: Euler factors change the canonical coefficients;
weighted-square and finite theta/zero-tail sources lack the full exact
source/completion; reflected super-Gaussian and positive-primitive
sources lack the gamma-times-ordinary-zeta identity; finite-prime orbit
controls retain only selected arithmetic constraints, not the complete
canonical coefficients and reflection. Generic heat flow or saddle
shape rejects none of them. The center perturbation lemma is generic
and is not claimed to exclude a colliding source. The result draws no
RH, global noncollision or global zero-simplicity conclusion.

**Disposition — Analysis, Sol:** A03-AN01 r1 CLOSED at its requested
field/arm/named-center and precise-unpaid-consumer scope. Accept NC15--19
as the new measurable gain from actual compact inputs, with all source
and same-model-review qualifications retained. HDA-A03 stays Partial
as a physical-layer program; LT-06 remains open for new physical
consumers. Parent HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled
are unchanged. [Assessment16](../reviews/16_NAMED_SWITCH_CENTERS_ASSESSMENT_20261026.md)
records internal checks. Manuscript integration is explicitly left to
concurrent base chat0024; this note does not claim a changed reading copy.

**Next deliverable — Analysis, Sol:** execute the new fixed-P4 physical
consumer packet, with output-specific requested rates and scoped stop
conditions. It advances the actual tuple comparison, separately from
sharpening a simplified two-layer shape. No exceptional resistant
analytical mechanism has appeared that requires Astra escalation.
