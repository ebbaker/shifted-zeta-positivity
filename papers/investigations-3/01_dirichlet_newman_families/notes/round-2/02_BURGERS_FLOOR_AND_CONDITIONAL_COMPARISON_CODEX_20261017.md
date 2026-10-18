# An explicit positive-time floor and a comparison conditional on confinement

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex), reasoning effort ultra**. Three
same-model subagents assisted with derivation, proof checks, and exact
scalar arithmetic. Their checks are internal same-model assistance, not
independent specialist review.

**Status.** Proved in this note: an explicit time-dependent lower bound
for \(S(x,p,t)\), uniform in every real \(x\), with no confinement input;
the associated loss budget; and the non-even barrier repairs requested
by [review 01](../../reviews/01_NORMALIZATION_AND_TRANSFER_CONTRACT_REVIEW_CODEX_20261017.md).
**Conditional on H12:** \(\Lambda_\chi\le27/100\) for every primitive
character of conductor \(q\ge10^{12}\) satisfying that confinement
hypothesis, and a conductor-aspect estimate
\(O((\log q)^{-4/7})\). The finite scalar inequalities are certified by
exact rational arithmetic. **H12 is still open for the character family.**
No unconditional upper bound below \(1/2\) is claimed in this round.

**Continuation, 17 October 2026.** Added by gpt-6.1-sol (Codex), reasoning
effort ultra, with LLM assistance for Edward Baker.
[Round 3](../round-3/03_SINE_TAIL_LIMIT_AND_COMPARISON_CODEX_20261017.md)
bypasses H12 by a sine-tail approximation and makes the quantitative
conclusions unconditional as proved there. H12 itself remains open for
the original flow. This note retains its historical conditional scope;
the scalar programme and stored record are unchanged.

This continues the [round-1 contract](../round-1/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md).
It follows the [result-summary index](../../../../../result-summaries/README.md),
[avoid index](../../../../../avoid/README.md),
[heat-flow summary 11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[control summary 12](../../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid 01](../../../../../avoid/01_restating_the_target.md),
[02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[06](../../../../../avoid/06_status_stronger_than_the_evidence.md), and
[07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
The quantitative target is a positive upper-bound milestone; this note
does not assert \(\Lambda_\chi=0\) or a GRH criterion. No originality claim
is made.

## 1. Contract, corrections, and source identity

Use round 1's Fourier family and normalization

\[
H_{t,\chi}(z)=\int_{\mathbb R}e^{tu^2}\Phi_\chi(u)e^{izu}\,du,
\quad s=(1+iz)/2,\quad \partial_tH=-\partial_z^2H,
\quad S(x,p,t)=-\Im(H'/H)(x+ip).
\]

Primitive \(\chi\) has conductor \(q>1\), parity
\(\mathfrak a\in\{0,1\}\), and the phase \(\alpha_\chi\) of round 1.
The imported strip-contraction theorem is
[Dobner, Theorem 3](https://arxiv.org/html/2005.05142v2):
for \(t\ge0\), the initial critical strip gives
\(|\Im\rho|\le\sqrt{\max(1-2t,0)}\le1\). Only this unconditional
strip input is used below; no claimed quasi-RH half-plane is used.

The time-zero bound of round-1 Lemma 3.4 is

\[
S(x,p,0)\ge C_{q,\mathfrak a}(p)
=\frac14\left[\log\frac q\pi+
\psi\left(\frac{1+p+2\mathfrak a}{4}\right)\right]
-\frac12\left(-\frac{\zeta'}\zeta\right)\left(\frac{1+p}{2}\right),
\qquad p>1. \tag{1}
\]

For complex characters, correct round-1 Lemma A's orientation. With
\(s_B=(1+y-ix)/2\), the exact identity is

\[
H_{0,\chi}(x+iy)=\bar\alpha_\chi(q/\pi)^{s_B/2}
\Gamma\left(\frac{s_B+\mathfrak a}{2}\right)L(s_B,\bar\chi).
\tag{2}
\]

The intended dominant Dirichlet sum therefore carries \(\bar\chi(n)\),
and its reflected sum \(\chi(n)\). Equation (2) follows from the
[Dirichlet functional equation](https://dlmf.nist.gov/25.15.E5).
The argument here does not use open Lemma A.

The first note was moved, at the user's request, into `notes/round-1`.
Only its relative Markdown links changed. The
[relocation record](../round-1/RELOCATION_20261017.json) preserves its old
SHA-256 `8e6ea15793b0a753a789f6f03dc86174438c8df507afd2a0d4671249c7f76b4e`
and its rebased SHA-256
`faee8afd944f98f3da773c9c527196dcc72761da11dba2b5828d6078f2898cc7`.
Review 01's source hash continues to identify the version actually reviewed.
Registered chat transcripts and the original numerical programmes retain
their historical text and bytes.

## 2. Growth, canonical sums, and characteristics

**Lemma 2.1 (proved).** On every bounded real time interval, the Dirichlet
flow is real entire in \(z\), jointly analytic in time and space, nonzero
as an entire function, and satisfies

\[
\log\max_{|z|\le R}|H_{t,\chi}(z)|
\le K_{\chi,T}(1+R)\log(2+R). \tag{3}
\]

It has infinitely many zeros at every real time.

*Proof.* The explicit kernel and its Hermitian symmetry give
\(|\Phi_\chi(u)|\le K_\chi e^{3|u|}e^{-c_\chi e^{4|u|}}\).
For bounded complex time, absorb the quadratic time weight and the
linear prefactor into half the negative double exponential. The remaining
integral on a disk is bounded, for \(R\ge1\), by a constant times
\(\int_0^\infty e^{Ru-ce^{4u}}du\le\frac14c^{-R/4}\Gamma(R/4)\).
This proves (3) and justifies all time/space differentiations. Fourier
injectivity excludes the identically zero function. Riemann–Lebesgue gives
\(H_t(x)\to0\) at both real ends. A finite zero set, together with order
at most one, would give \(H_t=P e^{az+b}\), impossible with those two
limits. Reality follows from the Hermitian kernel. \(\square\)

For a real entire function of order at most one with at least one zero,
whose zeros
\(\rho=a+iv\) lie in \(|v|\le1\), its genus-one product, with a separate
factor for a possible zero at the origin, gives

\[
S(x,p,t)=\sum_\rho\frac{p-v}{(x-a)^2+(p-v)^2}>0,
\qquad p>1. \tag{4}
\]

Zeros are counted with multiplicity. Keep canonical summands together
until taking imaginary parts: the exponential factor has real logarithmic
derivative, and the imaginary counterterms cancel by conjugation. Their
imaginary parts are absolutely summable because
\(\sum_{\rho\ne0}|\rho|^{-2}<\infty\) and \(|v|\le1\). No value is
assigned to a possibly divergent real sum \(\sum1/\rho\).

Put \(U=H'/H=u-iS\) on the line of height \(p\), and \(d=p-1\).
Differentiating the canonical sums yields

\[
|u_x|\le\sum_\rho|x+ip-\rho|^{-2}\le S/d,
\qquad
|S_{xx}|\le2\sum_\rho|x+ip-\rho|^{-3}\le2S/d^2.
\tag{5}
\]

The real characteristic equation \(x'=2u(x,p,t)\) is complete in both
time directions on every bounded interval of nonnegative time. Here are
the needed details. The strip makes \(ip\) uniformly zero-free on that
interval; continuity gives \(\inf_t|H_t(ip)|>0\). Jensen's formula and
(3) then give uniform counts \(N_t(R)=O_{\chi,T,p}(R\log(2+R))\).
The regularized difference

\[
U_t(x+ip)-U_t(ip)=\sum_\rho
\left(\frac1{x+ip-\rho}-\frac1{ip-\rho}\right) \tag{6}
\]

is absolutely convergent. For \(R\) larger than \(1+|x|+p\), split at
\(|\rho|=2R\). Nearby terms total \(O(N_t(2R)/d)\); the tail is bounded
by \(O(R\sum_{|\rho|>2R}|\rho|^{-2})=O(\log(2+R))\).
Thus

\[
|u(x,p,t)|\le K_{\chi,T,p}(1+|x|)\log(2+|x|). \tag{7}
\]

Smoothness gives local uniqueness, while
\(\int^\infty[(1+r)\log(2+r)]^{-1}dr=\infty\) prevents finite-time
escape, forwards or backwards. The characteristic flow is consequently
onto the real line. The constants in (3), (6), and (7) may depend on the
fixed character; their numerical sizes do not enter the estimate below.
This argument uses neither H12 nor high-height character asymptotics.

## 3. A proved positive-time floor and its loss

**Theorem 3.1 (proved).** Fix \(p>1\), put \(d=p-1\), and suppose the
explicit number \(C=C_{q,\mathfrak a}(p)\) in (1) is positive. Then, for
every real \(x\) and \(0\le t\le1/2\),

\[
\boxed{
S(x,p,t)\ge m_C(t):=
\frac{C e^{-2t/d^2}}
 {1+dC(1-e^{-2t/d^2})}.}
\tag{8}
\]

More generally any positive lower bound for \(C_{q,\mathfrak a}(p)\)
may replace \(C\). This is uniform over the family wherever that input
bound holds. H12 is not a premise.

*Proof.* The heat equation gives the complex Burgers identity
\(U_t=-U_{xx}-2UU_x\). Its imaginary part is

\[
S_t+2uS_x=-S_{xx}-2Su_x. \tag{9}
\]

Along a complete characteristic, (5) and \(S>0\) imply
\(dS/dt\ge-2S/d^2-2S^2/d\). Scalar differential comparison from
\(S(x,0)\ge C\) gives the solution (8) of this Riccati equation.
Onto characteristics make it a bound at every final real \(x\).
The right side increases with the initial value \(C\), proving the
last assertion. \(\square\)

On a prescribed interval \([0,T]\), this proves the explicit contract

\[
S(x,p,t)\ge C-\delta_C(T),\qquad
\delta_C(T)=C-m_C(T). \tag{10}
\]

For a retained fraction \(0<\theta<1\), the sufficient time for
\(m_C(t)\ge\theta C\) is

\[
0\le t\le T_\theta(C,p)=\frac{d^2}{2}
\log\frac{1+\theta dC}{\theta(1+dC)}. \tag{11}
\]

In particular the quarter-loss contract \(\delta\le C/4\) is proved
only up to (11) with \(\theta=3/4\), which is asymptotic to
\(d/(6C)\). It does not cover the whole comparison time of round 1's
zero-loss planning tables. The theorem therefore does **not** justify
those tables or establish constant-relative-loss persistence on their
intervals. The comparison below keeps the time dependence in (8).
No assertion that \(S\) is pointwise increasing in time is used.

## 4. The conditional comparison at a fixed reference height

Write **H12(T)** for the remaining hypothesis: for this fixed primitive
character and every \(t'>0\), all nonreal zeros have \(|\Re z|\le X(t')\)
uniformly for \(t\in[t',T]\), for some finite \(X(t')\). No explicit size
for \(X\), and no uniformity in the conductor, is required for this
compact-contact argument.

Choose \(p=3\), and let \(C>0\) be any proved lower bound for
\(C_{q,\mathfrak a}(3)\). Put

\[
D_C(t)=1+2C(1-e^{-t/2}),\quad
m_C(t)=C e^{-t/2}/D_C(t),
\quad I_C(t)=e^{-t}D_C(t)^{4/3},\quad
J_C(t)=\int_0^t I_C(s)\,ds. \tag{12}
\]

**Theorem 4.1 (proved conditional on H12(T)).** If \(T\le1/2\) and
\(J_C(T)\ge1/2\), then \(\Lambda_\chi\le T\).

*Proof.* At a highest simple nonreal zero, set \(Q=(\Im z)^2\le1\).
The round-1 paired-zero inequality, justified with the canonical sums
of Section 2, applies since \(9\ge5Q\). The own-pair term satisfies
\(8/(9-Q)\le1\), and (8) gives

\[
Q'\le-2-\left(\frac43m_C(t)-1\right)Q. \tag{13}
\]

Since \(D_C'/D_C=m_C\), the integrating factor is exactly \(I_C\).
The comparison curve is

\[
\overline Q(t)=\frac{1-2J_C(t)}{I_C(t)}. \tag{14}
\]

Until it reaches zero, it decreases from one: its descent rate is
\(2+(4m_C/3-1)\overline Q\ge2-\overline Q\ge1\) whenever
\(0\le\overline Q\le1\).

To justify comparison, start a strictly higher solution with initial
value \(1+\varepsilon\) and add a positive \(\varepsilon\) to the
right side of its differential equation. There is initially no contact
because all actual zeros have squared height at most one. H12(T) makes
any first positive contact occur in a compact set. At a simple contact,
(13) contradicts the strict derivative inequality. At a multiple contact,
backward Hermite splitting supplies an earlier zero higher by
\(c\sqrt v+O(v)\), contradicting first contact against a smooth curve.
Let \(\varepsilon\downarrow0\). This gives
\(M(t)\le\overline Q(t)\) before the latter reaches zero.

If \(T_0\le T\) is its first zero, strip contraction from any
\(t<T_0\) gives
\(\Lambda_\chi\le t+\overline Q(t)/2\). Letting \(t\uparrow T_0\)
proves the claim. Thus attainment of an initial global maximum is not
assumed. \(\square\)

The elementary integral in (12) is

\[
J_C(t)=\frac{3(1+2C)}{14C^2}(D_C(t)^{7/3}-1)
-\frac3{20C^2}(D_C(t)^{10/3}-1). \tag{15}
\]

Indeed, with \(E=e^{-t/2}\), one has
\(I_C(t)dt=(1+2C-D_C)D_C^{4/3}\,dD_C/(2C^2)\).
This also permits direct checking without a numerical ODE solver.

## 5. Exact scalar certificate and the conditional 0.27 statement

The [certificate programme](../../numerics/certify_dirichlet_scalar_conditional_20261017.py)
and [record](../../numerics/DIRICHLET_SCALAR_CONDITIONAL_CERTIFICATE_20261017.json)
use rational arithmetic for every deciding inequality. The fixed question
was whether \(C\ge6\), \(p=3\), and \(T=27/100\) make (15) exceed
\(1/2\), and whether the true floor is at least six for both parities
when \(q\ge10^{12}\). Only a prime-power sum up to 1000 and scalar
series enclosures are needed; there is no conductor sweep.

For even parity, \(\psi(1)=-\gamma\). The programme proves
\(\log10>23/10\), \(\log4<7/5\), and
\(\gamma<H_{1000}-\log1000<29/50\). It encloses
\(\sum_{p^k\le1000}(\log p)/p^{2k}\), then pays the positive tail
\((\log1000+1)/1000\), using \(\Lambda(n)\le\log n\). This gives
\((-\zeta'/\zeta)(2)<3/5\). Since \(\pi<4\), for both parities
(the digamma is increasing),

\[
C_{q,\mathfrak a}(3)>
\frac14\left(12\frac{23}{10}-\frac75-\frac{29}{50}\right)
-\frac{3}{10}=\frac{1221}{200}=6.105>6. \tag{16}
\]

At \(C=6\), \(T=27/100\), alternating rational Taylor sums enclose
\(e^{-T/2}\), and rational bisection encloses its required cube roots.
Outward decimal displays of the resulting rational interval are

\[
0.502464325582617834
\;\le\;J_6(27/100)\;\le\;0.502464325582617835.
\tag{17}
\]

The rigorous comparisons use the rational endpoints, not these displayed
decimals. The certified lower margin over \(1/2\) is at least
0.002464325582617834.
Because \(I_C\) increases with \(C\), (16)–(17) prove:

> **Conditional conclusion.** For every primitive character of conductor
> \(q\ge10^{12}\), **if H12(27/100) holds for that character**, then
> \(\Lambda_\chi\le27/100\).

This beats both \(1/2\) and the round-1 conditional strip baseline
0.2811856, while retaining a different, explicitly unproved hypothesis.
It uses no quasi-RH half-plane. A scalar certificate does not certify H12
or turn this into an unconditional family bound.

| File | SHA-256 |
| --- | --- |
| Scalar certificate programme | `0b7d513728d6c20ae380bb9b3ea9bc01a8c8963be1d9efd5aab970a4535b4cf9` |
| Scalar certificate record | `ff6e250a2340bdc88e00c6c2a9043257d50076c44231d7d0b7fd633de4030837` |

The record includes the actual runtime. Reproduction is documented in
[numerics](../../numerics/README.md); its runtime metadata can differ
across environments, while all deciding quantities are rational.

## 6. A conditional conductor-aspect rate

For \(0\le t\le1/2\),
\(D_C(t)\ge1+C e^{-1/4}t\) and \(e^{-t}\ge e^{-1/2}\). Hence

\[
J_C(t)\ge e^{-1/2}
\frac{(1+C e^{-1/4}t)^{7/3}-1}{(7/3)C e^{-1/4}}.
\tag{18}
\]

Define

\[
B(C)=\frac{e^{1/4}}C
\left[\left(1+\frac76e^{1/4}C\right)^{3/7}-1\right]. \tag{19}
\]

Whenever \(B(C)\le1/2\) and H12(B(C)) holds, Theorem 4.1 gives
\(\Lambda_\chi\le B(C)\). Since
\(C_{q,\mathfrak a}(3)=\frac14\log q+O(1)\), uniformly in the two
parities, this is \(O((\log q)^{-4/7})\), conditional on confinement for
each character. This rate is weaker than round 1's proposed
constant-relative-loss comparison. Its persistence estimate is proved
here rather than assumed. Equation (19) is a sufficient bound; it is
not the optimized root of (15).

## 7. Why H12 remains a separate arithmetic question

The generic strip and Burgers premises do not imply confinement. For
\(a>0\), \(0<r<1\), the explicit real entire heat flow

\[
F_t(z)=e^{a^2t}\cos(az)-\cosh(ar) \tag{20}
\]

has initial zeros \(2\pi n/a\pm ir\). For every
\(0<t<\log(\cosh(ar))/a^2\), its nonreal zeros still occur at every
\(2\pi n/a\), at heights
\(\pm a^{-1}\operatorname{arcosh}(e^{-a^2t}\cosh(ar))\).
It therefore fails H12. At any fixed \(p>1\), its global initial floor is

\[
\inf_x S_F(x,p,0)=\frac a2
\left[\tanh\frac{a(p-r)}2+\tanh\frac{a(p+r)}2\right]>0,
\tag{21}
\]

which grows like \(a\). Formula (21) follows by factoring (20) into two
sine functions; each resulting Poisson term is minimized at
\(\cos(ax)=-1\). Thus real-entire order one, bounded zero strip,
Burgers dynamics, and an arbitrarily large positive floor do not prove
H12. This is a scoped exclusion of that generic derivation. The example
has no primitive Dirichlet completion, Euler product, or integrable
rapidly decaying Fourier kernel. It does not refute a character-specific
proof of confinement or the conditional comparison above.

The repository's Euler-factor controls fail the particular logarithmic
Euler-product bound used in (1). The weighted-square, reflected, smooth,
and primitive-compatible controls do not have the full character
completion plus that Euler-product input. They can satisfy the generic
heat identities of Sections 2–3; those identities alone are not a
zero-time positivity mechanism. No claim is made that all such controls
fail the transport estimate, or that transport itself distinguishes
characters. The distinguishing input so far is the explicit growing
arithmetic floor (1); confinement remains missing.

## 8. Completed barrier repairs and round-1 interpretation

For use with the finite-character route, the following completes the
proof obligation in round-1 Proposition 3.1. Retain its notation
\(Y(t)=\sqrt{y_0^2+2(t_0-t)}\), \(w=\sqrt{1-y_0^2}\) and its two
barriers. Growth and regularization are supplied by Section 2. Suppose a
zero first enters the moving central rectangle
\([-X_-,X_+]+i[Y(t),1]\). Compactness gives a positive first time; the
barriers exclude the vertical sides and strip contraction excludes the
top. Rouché's theorem forces a contact at \(x+iY\) on the moving bottom.

A multiple zero splits backwards with a zero higher by
\(c\sqrt v+O(v)\), whereas the bottom changes by \(O(v)\), contradicting
first contact. This is the local backward Hermite expansion of
[Polymath, Proposition 3.1](https://arxiv.org/html/1904.12438v2), obtained
by applying the heat equation to the leading term of its Taylor series.
At a simple contact, the canonical vertical-velocity identity is

\[
\Im\dot z_j=-2\sum_{k\ne j}
\frac{\Im z_j-\Im z_k}{|z_j-z_k|^2}. \tag{22}
\]

Its own conjugate contributes \(-1/Y\). Another real zero contributes
strictly negatively. A nonreal pair \(a\pm iv\), with \(v\ge0\), contributes
\(-2K_Y(x-a,v)\), where

\[
K_Y(d,v)=\frac{2Y(d^2+Y^2-v^2)}
 {(d^2+(Y-v)^2)(d^2+(Y+v)^2)}.
\]

If \(v\le Y\), this is positive except for the excluded duplicate
contact. If \(v>Y\), the first-contact rectangle and the barriers force
\(|d|\ge w\), and
\(d^2+Y^2-v^2\ge1-y_0^2+Y^2-v^2\ge1-v^2>0\).
The last strict inequality uses positive-time strip contraction. There
is another zero by Lemma 2.1. Consequently
\(\Im\dot z_j<-1/Y=Y'(t)\), contradicting first entry. Final-time
exterior coverage and the barriers then yield the stated strip and
constant bound. Evenness and positivity on the imaginary axis are
unnecessary. This replaces the reflected extra zero used in Polymath's
printed proof, pp. 15–16.

For the proposal's strict count \(\Re s>\sigma_*\), raise \(y_0\) by a
small positive amount with \(t_0\) fixed. The initial threshold rises,
the required barrier narrows, and the extra final exterior strip lies in
the original final-time barrier. Apply the proved criterion and take the
limit. If \(t_0+y_0^2/2=1/2\), the unconditional strip bound suffices.
The limiting conclusion is the constant bound, not strict final exclusion
of a zero exactly at height \(y_0\).

Also adopt review 01's reporting corrections: only the two tested
leading-order row transfers are demoted; first-term dominance generally
is untested. Counts of 938 and 92,718 are conjugacy classes requiring
checks, not proven distinct constants. The original floating records
are historical diagnostics; cross-platform byte identity is not a theorem.

## 9. Decision and remaining deliverable

The positive-time persistence question now has a proved, explicit answer
with the loss (10). It is weaker than the proposed quarter-loss contract
on the full planned interval; the time-dependent comparison nevertheless
gives the conditional statement in Section 5. H12 is not discharged by
these estimates, by the scalar certificate, or by the original zeta
confinement import.

The next analytic task is therefore a character-specific proof of
H12(27/100), or a replacement comparison argument that does not need
compact attainment. It must use additional properties beyond the generic
premises refuted by (20). Keep conductor sweeps and per-character barrier
campaigns gated until that input is available. This note and certificate
await cross-model review; there is no manuscript or unconditional
upper-bound milestone to promote.
