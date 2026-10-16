# Joint review of Investigations 21 and 22: direction, correctness and next steps

15 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork, reasoning effort
max; the session's configured identifier is `claude-opus-5-5`, and the serving
model may differ from the configured one. This is an internal review, not
independent specialist refereeing or formal verification.

This is a **joint review of Investigations 21 and 22**. It is filed only in
Investigation 22 because 22 has superseded 21 as the active home of the
manifold, connection and arithmetic-trace direction; the parts of 21 that it
assesses (the quaternion and octonion lifts, the controls, the outer theorem,
the finite certificates, the workstream structure PR01–PR03) are cited by
path. Reviewed at repository commit `7eefd2a` (15 October 2026, 16:55 EDT),
which is the current HEAD of the local clone; the working tree was clean.

## 1. Scope and method

Read in full: the Investigation 22 [README](../README.md),
[draft history](../DRAFT_HISTORY.md), both [research overviews](../research-overview/README.md),
all thirteen [coordination notes](../notes/00_research_coordination/README.md),
every subproject note under `notes/01`–`notes/06`, the fifteen prior
[reviews](README.md), the [numerics README](../numerics/README.md), and the
56-page [manuscript](../manuscript/theta_manifold_geometry.tex) in full. For
Investigation 21: the [README](../../21_quaternion_theta_geometry/README.md),
the three research overviews, the criteria baseline
[Note 1](../../21_quaternion_theta_geometry/notes/1_RH_CRITERIA_AND_QUATERNION_SETUP_20261014.md),
coordination [Note 63](../../21_quaternion_theta_geometry/notes/00_research_coordination/63_MANIFOLD_GEOMETRY_AND_THETA_BUNDLE_CONTINUATION_20261015.md)
(the note that spawned 22), the reviews index and [Review 25](../../21_quaternion_theta_geometry/reviews/25_OCTONIONIC_MACHINERY_LITERATURE_REVIEW_20261015.md),
and the [manuscript](../../21_quaternion_theta_geometry/manuscript/quaternion_theta_geometry.tex)
Sections 1, 2 (statement), 3 (collision criterion) and 14 (remaining program).
Also used: the portfolio's earlier Claude reviews in
[`papers/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md`](../../../../quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md)
and [`papers/investigations-2/brainstorm/reviews/REVIEW_OF_ACTIVE_LIFTED_THETA_DIRECTIONS_CLAUDE_20261013.md`](../../../brainstorm/reviews/REVIEW_OF_ACTIVE_LIFTED_THETA_DIRECTIONS_CLAUDE_20261013.md),
and the [Euler-factor controls](../../19_euler_factor_controls/README.md) of
Investigation 19.

Executed: twenty-four of the twenty-five Investigation 22 check programs
(`check_*.py`, `certify_*.py`) in a fresh environment; every one passes
with the assertion counts recorded in its receipt (Section 9 lists the
environment issues; the twenty-fifth, the chat-history audit, needs the
local registry's lock file and cannot be replayed from a clone).
Independently recomputed with a different library and method (mpmath,
tanh–sinh quadrature at 45 digits, no interval arithmetic): the two
validated weighted-square collision controls, the positive-tail inequality
of Note 03/10, the endpoint-only source tail bound of §7.3
(obs:average-value-tail) and the fixed-endpoint chord limit. Script and record:
[`recompute_controls_claude_20261015.py`](../numerics/recompute_controls_claude_20261015.py),
[`INDEPENDENT_RECOMPUTATION_CLAUDE_20261015.json`](../numerics/INDEPENDENT_RECOMPUTATION_CLAUDE_20261015.json).
Hand-verified: the covariant theta-source formula (Theorem "Exact covariant
theta-source formula"), the Hermitian connection and curvature, the
fixed-endpoint chord law and its sign, the exponential-average identity, the
weighted-comb reflection rigidity, the normalized recurrence core, the
one-sided observation quotient, the spacetime index formula for \(m=2,3\),
and the Jensen-surface equivalence.

## 2. Summary

**Correctness.** I found no mathematical error in the theorems of either
manuscript that I checked. The local heat-flow analysis of Investigation 22
(predecessor curves, the complete local stationary locus, the fixed-endpoint
and exponentially averaged chord laws, the quarter-turn profiles, the scalar
cone transfer) is correct and carefully stated. The theta identities
(covariant source formula, Hermitian and ASD connections, reflection
rigidity, recurrence core, coupled addition, prime dilations) are correct.
The three collision controls are correct and I reproduce their certified
numbers to all displayed digits. The reproducibility package is in good
order.

**Direction.** The direction is not fruitful as a route to RH, and the two
investigations have, by their own results, already demonstrated this; what
is missing is that the manuscripts do not draw the conclusion. Every
"conditional exclusion criterion" in Investigations 20–22 — the stationary
bounded-loss criterion, the chord criteria \(\mathcal C_j\ge-o(\sqrt E)\),
the exponentially averaged and endpoint-cutoff versions, the oriented
continuity modulus, the scalar cone target
\(WB_\partial\le C_0W^2+\varepsilon_0|W|\) — is **equivalent to RH for the
theta field**, not merely sufficient: under RH each hypothesis holds with
zero loss on the whole stationary set and every zero-free interval, at every
positive time (Proposition 1 below). Restricted to heat times
\(t\ge t_0\), each criterion is equivalent to \(\Lambda\le t_0\). There is
therefore no intermediate milestone between "a theta-specific signed
estimate" and RH itself, and the investigation's own control families show
that no property short of the complete Euler product can supply the sign.
The geometric apparatus (self-dual forms, hyperkähler lifts, jet surfaces,
calibrations, theta line bundle with ASD connection; in 21 the Fueter and
octonionic lifts) contributes no estimate, as the manuscripts say in each
section; it has been tested and found sign-blind, and should now be closed
as a source of estimates. This is the same conclusion the portfolio reached
on 10–11 October for the seventeen `newman_collisions` lifts (rules R1, R2,
R5 and the stop list of the 11 October brainstorm); Investigations 21 and
22 re-derive those rules in new coordinates without citing them.

**Note 11.** The next steps in
[coordination Note 11](../notes/00_research_coordination/11_SCALAR_MANUSCRIPT_AND_POSITIVE_TAIL_CONTINUATION_20261015.md)
are not the most fruitful. Its target is RH restated with acceptance tests
attached, and Notes 12–13 have already run one full cycle of it with the
expected outcome (Möbius and Poisson sectors fail at positive heat time;
only the functional equation survives the heat multiplier). Section 8
proposes a reordered program: state the equivalence in the manuscript and
stop the criterion treadmill; consolidate; keep the one quantitative
non-RH-equivalent target the program contains (an *effective* outer
theorem, which is the \(\Lambda\) frontier) as a separately judged task; and
treat the spacetime winding certificate as a computational tool to
benchmark, not a new principle.

## 3. What is proved, and what I checked

| Claim | Where | Status | Check |
| --- | --- | --- | --- |
| \(H\) jointly entire, \(H_t=-H_{zz}\), \(H(t,0)>0\), source majorant \(\Phi<4\pi^2e^{9u-\pi e^{4u}}\) | 22 §2, 21 §1 | proved | hand |
| Even-order predecessor curve, physical stationary pole \(\mathcal L_j/E=-r/s+O(1)\), complete local backward stationary locus is one analytic curve, scalar factor \(E=W^2Q(s)\) | 22 §2 | proved | hand (heat Taylor) |
| Signed stationary exclusion; fixed-endpoint chord law \(\mathcal C_j/\sqrt E\to-d_\delta<0\); starting-energy exclusion with \(o(\sqrt E)\); sharpness of exponent \(1/2\) for polynomial fields | 22 §7 | proved | hand; exact replay `check_chord_controls.py` (5,616) and `check_exponential_average_chords.py` (1,620) pass; polynomial limit recomputed |
| Exponential average \(\mathcal A_{j,\delta}=\int_0^\delta e^{-z}\mathcal C_j\,dz\); endpoint-only cutoff error \(\le B_j(T_*)e^{-\pi(N+1)^2/4}\sqrt E\) | 22 §7.3 | proved | hand; numerical spot check (actual \(2.1\cdot10^{-5}\) vs bound \(6.6\cdot10^{-2}\) at \(N=1\)) |
| Quarter-turn concentration, scaled profiles \(F_r\), odd-branch factor \(1+r^2\xi^2\) | 22 §7.4 | proved | `check_inner_turning_profile.py` (792) passes |
| \(\Phi=(\psi''-\psi)/8\), reconstruction \(8H=\tfrac12+(2t-x^2-1)J+4txJ_x-4t^2J_{xx}\), \(J>0\) for \(0\le t\le1/2\) | 22 §8.1 | proved | hand |
| Covariant source formula \(\Phi=\frac{y^{1/4}}{16\pi^2}(y^2\mathcal D^4\vartheta-3\pi^2\vartheta)(0,iy)\) | 22 §8.2 | proved | hand (equals \((D_y^2-\tfrac1{16})\) applied to \(y^{1/4}\vartheta\), i.e. the classical \((\partial_u^2-1)P/16\); see §5) |
| Hermitian metric \(h=e^{-2\pi(\Im z)^2/q}\), curvature \(-2\pi i\,dr\wedge ds\), semi-flat hyperkähler metric, base-rescaled ASD Chern connection, classification \(b=\tfrac{2\pi}3q^3+2\Re f\), flat physical restriction | 22 §8.3–8.5 | proved, standard | hand for the connection; `check_theta_chern_*.py`, `check_asd_path_metric.py` pass |
| Validated three-square control: collision at \(T=1/4\), \(x_*\in(44.1303,44.1304)\) with \(\Phi_a'(0)=0\), primitive endpoint, support-only localizers | 22 §9.1, Note 05/01 | validated (Arb) | **independently reproduced**: \(x_*=44.13034367\ldots\), \(\theta_*=0.879171448\ldots\), \(H_{xx}=-5.8048\cdot10^{-6}\), \(\Phi_a'''(0)=-39.9924\), \(\psi_a'(0)=-0.4999826\) |
| Four-square two-endpoint control at \(T=1/100\), \(x_*\in(83.5323729,83.5323730)\), \(\Phi'(0)=\Phi'''(0)=0\), \(\psi^{(2k+1)}(0)=-\tfrac12\) for \(k\le2\) | Note 05/03 | validated (Arb) | **independently reproduced**: \(x_*=83.532372961456\ldots\), \(q_*=0.8377475080\), \(G_{xx}=6.14083378\cdot10^{-12}\), \(\Phi^{(5)}(0)=-2.6568441\), \(\psi'(0)=-0.5000000000348\) |
| Reflected super-Gaussian control \(H_*(1/4,x)=cF(x)(1+\cos4x)\), exact double zero at \(\pi/4\), all Fourier–Gram forms positive | Note 05/04 | proved | hand |
| Weighted-comb reflection rigidity; source reflection plus endpoint forces \(a_n=1\) | 22 §9.2 | proved | hand (Poisson, Gaussian moments, periodicity) |
| Normalized recurrence core; sharp finite-hierarchy stability; absorption current; polynomial source obstruction; recurrence boundary cokernel; invariant total trace; signed observation quotient \(C_{\rm sign}=(a\cdot b+\|a\|\|b\|)/2\) | 22 §9.3–11 | proved | hand for the quotient and cokernel; exact replays pass |
| Multiplicative dilations \(D_d\Phi=\sum_{d|n}\phi_n\), sieve and Möbius identities, uniform moment tail, divergence of separated positive-time Möbius series | 22 §12 | proved (classical algebra plus explicit bounds) | `check_arithmetic_dilation.py` (47) passes; algebra hand-checked |
| Positive-tail orientation \(-H_{n,x}/\beta_n>x/[40(4\pi n^2-1)^2]\) on \([0,1/2]\times(0,30]\), \(n\ge2\) | Note 03/10 | proved | grid spot check: minimum ratio lhs/rhs \(=5.63\) at \(n=2,t=0,x=30\); no violation |
| Spacetime index \(\operatorname{ind}(H,H_x)=-\lfloor m/2\rfloor\) | Note 01/04 | proved | hand for \(m=2,3\); `check_spacetime_topology.py` (1,573, Sturm isolation) passes |
| RH \(\iff\) \(C_g(\mathbb R)\) has \(g+1\) components for all \(g\) | Note 01/05 | proved (Pólya–Jensen plus Harnack) | hand |
| 21: finite collision criterion RH \(\iff\) \(E>0\) on \((0,1/2]\times\mathbb R\) (Polymath confinement) | 21 §3 | proved | hand |
| 21: uniform four-jet asymptotic, strict signs for \(tL\ge61/24\), \(x\ge X_*\) unevaluated; explicit region \(tL\ge5\), \(x\ge4\pi e^{10^9}\) | 21 §§1–2 and the explicit-height appendix | proved per 21's reviews; not re-derived here | out of scope (see §8, item 3) |
| 21: certified bounded region \(\lvert x\rvert\le112\), \(0\le t\le1/2\) | 21 §9 | validated | not replayed; see §9 on R5 |

Two further remarks on the reviews already in the folder. They are
internally consistent and their stated scopes are honest; every one ends
with "no theta sign estimate is established", and that is the correct
reading. But fifteen reviews by the same coordinating model, of material
produced on the same day, are not independent review, and the thousands of
"exact assertions" they cite are replays of identities on polynomial germs
and rational surrogates (the receipts say so). Neither point is a
criticism of the notes; it is a caution against reading the verification
volume as evidence about the research direction.

## 4. The central point: the criteria are equivalent to RH

Write \(h_j=\partial_x^jH\), \(E=h_0^2+h_1^2\), \(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\),
\(\mathcal C_j(t;x,y)=h_j(t,x)\{h_j(t,y)-h_{j+1}(t,y)\}\), as in the 22 manuscript.

**Proposition 1 (necessity).** Assume RH. Then for every \(t>0\) and both
branches \(j=0,1\):

1. \(\mathcal L_j>0\) at every point of the stationary set \(S_j=\{h_{j+1}=0\}\);
2. \(\mathcal C_j(t;x,y)>0\) whenever \(h_{j+1}(t,x)=0\), \(y>x\), and \(h_j\) has no zero on \([x,y]\);
3. \(\mathcal A_{j,\delta}(t,x)=W^2-e^{-\delta}WW(x+\delta)\ge(1-e^{-\delta})W(t,x)^2\) on the same intervals, and the endpoint-cutoff version satisfies \(\mathcal A_{j,\delta,N}\ge-e^{-\delta}B_j(T_*)e^{-\pi(N+1)^2/4}\sqrt E\), i.e. hypothesis (obs:average-mixed-hypothesis) holds with \(K\equiv0\);
4. the one-sided turning increment \(\alpha_j(t,x+\ell)-\alpha_j(t,x)\) is negative on every regular segment from a stationary start, so Definition "one-sided modulus" holds with \(\omega\equiv0\);
5. on every full stationary start, \(0<W(t,x+\delta)/W(t,x)\le1\) for \(0<\delta<\) distance to the next zero of \(W\), so the scalar endpoint criterion (obs:cone-endpoint-criterion) holds with \(M=1\) and the exact endpoint, and with \(\eta_N=B_j(T_*)e^{-\pi(N+1)^2/4}\) for the cutoff endpoint.

*Proof.* RH gives \(\Lambda\le0\) (de Bruijn–Newman), so \(H(t,\cdot)\) has
only real zeros for every \(t\ge0\). At \(t>0\) they are simple: a multiple
real zero at \((T,a)\), \(T>0\), would by the local Hermite splitting lemma
(21, Lemma "Local splitting at a multiple zero") produce nonreal zeros at
times \(T-s\ge0\), contradicting \(\Lambda\le0\). Each slice is a real even
entire function of order at most one with only real zeros, so by Hadamard
\(H(t,z)=c\prod_k(1-z^2/a_k^2)\) with real \(a_k\) (evenness removes the
exponential factor); it lies in the Laguerre–Pólya class and so does every
derivative. For \(W=h_j\) the logarithmic derivative is
\(W'/W=\sum_\rho(x-\rho)^{-1}\) over the zeros of \(W\), hence
\[
 \mathcal L_j\;=\;W'^2-WW''\;=\;W^2\sum_{\rho}\frac1{(x-\rho)^2}\;>\;0
 \quad\text{wherever }W\ne0 ,
\]
which is (1) on \(S_j\cap\{W\ne0\}\) (and at \(W=0\in S_j\) both jets vanish,
excluded by simplicity). Between consecutive zeros of \(W\) the function
\(W'/W\) decreases strictly from \(+\infty\) to \(-\infty\), so \(W\) has
exactly one critical point per gap and is strictly monotone from that
point to the next zero, with \(|W|\) decreasing. For a stationary start
\(x\) and \(y\) in the same zero-free gap this gives \(W(x)W(y)>0\) and
\(W(x)W'(y)<0\), i.e. (2); (3) follows from (2) by the average identity, or
directly from \(0<W(x)W(x+\delta)\le W(x)^2\); (4) from
\(\alpha_j'=-\mathcal L_j/(h_j^2+h_{j+1}^2)<0\) on regular segments; (5) is
the monotonicity statement, and the cutoff version uses the manuscript's
own tail bound. \(\square\)

Combined with the exclusion theorems of 22 §2, §7 and §11 (which are
correct), every one of those "conditional criteria", applied to the theta
field on \((0,1/2]\times\mathbb R\), is **equivalent** to RH, for every
choice of exponent \(\gamma>1/2\), coefficient \(K\), length schedule,
cutoff schedule or cone \(\kappa\).

**Corollary 2.** For \(t_0\in(0,1/2]\), each criterion restricted to heat
times \(t\ge t_0\) implies \(\Lambda\le t_0\) (a collision at time
\(\Lambda\) exists when \(\Lambda>t_0\), by the compactness argument of 21
§3), and \(\Lambda<t_0\) implies each criterion on \(t\ge t_0\) with zero
loss, by the proof above. In particular, by Platt–Trudgian's
\(\Lambda\le0.2\) (2020), every hypothesis in the 22 manuscript holds
*unconditionally* for \(0.2<t\le1/2\), and the open region is exactly
\(0<t\le0.2\). (Two 2026 computer-assisted claims push the frontier further:
a self-published \(\Lambda\le0.1787854\) using Polymath's Theorem 1.2 with
Platt–Trudgian's verification height, and an arXiv preprint titled "A
conditional bound \(\Lambda\le0.13963\)". I have not been able to verify
either; the arXiv page could not be fetched in this session.)

Consequences for the two manuscripts and the program:

- The sentence "A uniform one-sided continuity estimate would prevent such
  concentration ... That estimate is a sufficient target, not an established
  property of theta" (Overview 01, and the equivalent sentences in 22 §1,
  §7, §13 and 21 §3) should be replaced by: *the estimate is equivalent to
  RH; under RH it holds with zero loss.* The manuscripts currently present a
  hierarchy of sufficient conditions as if some might be weaker than the
  conclusion. None is. The sharpness statements (exponent \(1/2\), location
  of the energy, cutoff rate gap) are correct statements about general
  backward-heat fields and carry no information about theta.
- The "remaining theta-specific estimate" is \(\Lambda=0\). A proof of any
  version of it on a declared domain covering all events is a proof of RH;
  a proof on \(t\ge t_0\) is a proof of \(\Lambda\le t_0\). Research on the
  criterion side therefore has exactly one quantitative target, the
  \(\Lambda\) frontier, and that target is governed by effective
  asymptotics and numerical verification height, not by new identities
  (Section 8, item 3).
- The Laguerre identity \(\mathcal L_0=H^2\sum_\rho(x-\rho)^{-2}\) is rule R2
  of the portfolio's 11 October brainstorm ("makes every pointwise sign test
  a tautology ... None of these is a reduction"). Investigation 21's
  criteria baseline (Note 1) states the Csordas–Escassut whole-plane
  equivalence at \(t=0\) and the sufficiency of the bounded-loss criterion,
  but neither investigation states necessity at \(t>0\), and neither cites
  the brainstorm's R1–R5 or its stop list ("lifts of the heat flow (any
  kind); stationary-sign or threshold-jet calibrations below
  \(x=6\cdot10^{10}\); transport/multiplier constructions; further
  rewritings of ... Laguerre expressions in new coordinates"). The geometric
  and criterion parts of Investigations 21 (14 October) and 22 (15 October)
  are, item by item, that stop list executed in quaternionic, octonionic, self-dual, hyperkähler, jet-surface
  and theta-bundle coordinates. Their one methodological improvement is that
  every criterion was tested against control families — which is rule R1 —
  and every test came out the way R1 predicts.

## 5. The geometric program

What the geometry established is correct and, as the manuscript says
repeatedly, standard: closed self-dual forms from holomorphic functions;
\(|f|^2|dz|^2+|dw|^2\) is flat in the coordinate \(F(z)\), \(F'=f\); the
jet surface \((P,f,w)\) has curvature \(-2|D|^2/\mathcal E^3\); complex
surfaces are calibrated, coassociative in \(\mathbb C^3\) and Cayley in
\(\mathbb C^4\); the theta bundle has the usual Hermitian metric and
curvature, and a base-only rescaling makes it ASD on the semi-flat family.
What the geometry showed about the problem is negative in every instance,
and the manuscript records each: curvature squares the Laguerre quantity;
the opposite-sign controls \(\varepsilon\pm z^2\) are unitarily congruent
surfaces; the restricted theta connection is flat on the physical path and
on the external two-source product, so no curvature term enters the
transform; the compact extension conflicts with fiber degree one; the
fiber Hilbert norm does not decay with the physical value. The covariant
source formula, which is the one new-looking identity, is the classical
\(\Phi=(\partial_u^2-1)P/16\) rewritten through the Hermite-weighted theta
jets \(\mathcal D^k\vartheta(0,iq)=\partial_w^k[e^{\pi w^2/2q}\vartheta(w,iq)]_{w=0}\),
whose modularity under \(q\mapsto1/q\) is the functional equation of
\(\Phi\) (I checked that \(J_4(1/q)=q^{9/2}J_4(q)\) reproduces \(\Phi(-u)=\Phi(u)\)).
It is a correct and pleasant repackaging, not new structure.

The same holds for 21's Fueter and octonionic lifts: Review 25 and the
reflected-lift note conclude that they are "finite algebraic reductions"
with "no new sign estimate", which is right. The honest status of the
geometric hypothesis that opened Investigation 22 ("transfer information
from the arithmetic family to the signed motion of the physical surface")
is that it was tested on the actual theta bundle and failed: the
construction is sign-blind by its own Section 8.5. I recommend closing
both geometric branches as sources of estimates, with 22 §§3–6 and 8.3–8.5
reduced to a short remark or an appendix in any consolidated manuscript.
The Jensen-surface note (RH \(\iff\) the real hyperelliptic curves
\(y^2=J_{2g+1}(x)\) are M-curves) is correct and is Pólya–Jensen plus
Harnack in different words; Review 13's assessment that it is vocabulary
and not publishable alone is right.

## 6. The arithmetic program

The controls are the most valuable part of both investigations. They
establish, with certificates, that the following properties *together* do
not exclude positive-time collisions: positivity of the source, rapid
decay, evenness (full source reflection), all odd primitive endpoints, the
first one or two odd source endpoints, positivity of every finite
moment and adjacent-square localizing matrix, positivity of every
Fourier–Gram form, monotonicity and log-concavity (21, Notes 53/56), and
the Jacobi heat equation with period two in \(\tau\). The reflection
rigidity theorem then shows that within polynomially weighted integer
combs, reflection alone forces \(a_n\equiv1\). So the only object that
passes all tests is theta itself, and the "arithmetic premise absent from
arbitrary positive mixtures" that Note 11 asks for is the complete
integer-square lattice with its reflection — which is to say, the full
functional equation and Euler product.

Investigation 19's Euler-factor control sharpens this further and should be
the first acceptance test for anything proposed under Note 11:
\(\Phi_{c,p}=\Phi+\tfrac c2[\Phi(u+a)+\Phi(u-a)]\), \(a=\tfrac12\log p\),
is positive and even, has the *same real zeros as \(\xi\) at \(t=0\)*, its
zeta is \(\zeta(s)Q_p(p^{-s})\) in the extended Selberg class, and its
Newman constant is positive. In the notation of 22 §12 it is
\(\Phi+\tfrac{c\sqrt p}2D_p\Phi+\tfrac c{2\sqrt p}D_{p}^{-1}\Phi\): it lies in
the span of the very dilation operators Section 12 manipulates, and the
prime-excision operators \(I-D_q\) at every prime \(q\ne p\) act on it
exactly as on \(\Phi\), since they commute with \(D_p\). Hence an argument
that uses the Euler factors at a finite set of primes (and otherwise only
the shape properties listed above) would apply verbatim to \(\Phi_{c,p}\)
for a prime \(p\) outside that set and would prove a false statement; a
successful mechanism must use the Euler factor at every prime
simultaneously. This is the structural form of what Notes 11–12 of
`03_theta_bundles_and_connections` found by direct calculation. At positive heat time the obstruction to doing so is
structural, not technical: the multiplier \(e^{tu^2}=e^{(t/16)\log^2y}\)
commutes with the inversion \(y\mapsto1/y\) and with nothing else, so the
functional equation is the only arithmetic symmetry that survives the
flow exactly, while the Euler product is a statement at \(\Re s>1\). The
divergence of the separated Möbius and Poisson sectors in §12 is this fact
in explicit form. The same fact underlies 21's outer theorem: its carrier
is a zeta value at real part \(1/2+tL/4\), and the threshold \(tL>2\) is
\(\Re s>1\). The "inner cusp" \(tL<2\) is the critical strip, and
\(tL\to0\) is the critical line. A sign estimate uniform down to
\(t\to0\) is a zero-free region shrinking to the line, which is RH again.

## 7. Assessment of Note 11's next steps

Note 11 proposes to "return to the scalar target
\(WB_\partial\le CW^2+\varepsilon_0|W|\) on prescribed positive cones ...
state one explicit source multiplier or bilocal identity, its complete
lower trace, and a one-sided estimate or vanishing-order argument", with
the asymmetric heat germs, weighted-square collisions and reflected-source
control as acceptance tests, and a rule rejecting proposals that only
rewrite the trace or divide by the unknown jet.

The hygiene is good and should be kept. The target is not. By Proposition 1
and Corollary 2 it is \(\Lambda=0\) restated, with no weaker version
available; the acceptance tests are necessary conditions that every
rewriting so far has failed, and the strongest available test
(\(\Phi_{c,p}\), all \(p\)) is missing from the list. Notes 12 and 13 then
executed the proposal once — prime dilation, Möbius inversion, resolvent,
Euler summation, Poisson duality — and ended with "the scalar signed
arithmetic estimate remains the next target", which is where Note 11
started. Continuing the cycle produces further correct identities with the
unknown moved into a new boundary term; the manuscript's §§10–12 already
contain several such relocations. I would also not rank the "compact-surface"
and "winding pilot" items above the arithmetic target as *routes*: the
first is vocabulary (Section 5), and the second is a finite-verification
tool (Section 8, item 4).

So: the steps are not the most fruitful. What follows is what I think is.

## 8. Recommended program, in order

1. **State the equivalence and reframe.** Add Proposition 1 and Corollary 2
   to the 22 manuscript (one page), relabel every "conditional criterion" as
   an RH-equivalent reformulation, and rewrite §13 accordingly: the
   outstanding problem is \(\Lambda=0\), and the only quantitative target is
   the \(\Lambda\) frontier. Make the same change in 21 §3. Cite R1, R2 and
   R5 of the 11 October brainstorm and Investigation 19's control where
   the controls are discussed. Cost: a day. Kill criterion: none; this is
   accuracy.

2. **Consolidate and stop the note cycle.** Two manuscripts of 56 and 96
   pages, about a hundred notes and fifty reviews were produced in two days. Write
   one short document (five pages) with three lists: proved facts worth
   keeping (the local heat-flow lemmas; the three controls and 19's; the
   reflection rigidity; the covariant jets and their modularity; the
   spacetime index formula), RH-equivalent reformulations (everything in
   Section 4), and closed mechanisms with the control that closed each.
   Freeze both manuscripts at that point. A sharp negative result is worth
   more than a vague positive one, and this document would be the sharp
   negative result; a fourteenth coordination note would not be.

3. **The one quantitative target: an effective outer theorem.** Investigation
   21's theorem (strict Laguerre signs for \(tL\ge61/24\), \(x\ge X_*\)) is
   the same statement as Polymath's first-term dominance, with a sharper
   constant and an unevaluated height. If \(X_*(t)\) could be made
   *effective and moderate*, this would lower the \(\Lambda\) frontier: at
   \(tL\ge61/24\) the numerical verification needed for \(\Lambda\le t_0\)
   would reach only \(4\pi e^{2.54/t_0}\) (about \(1.4\cdot10^{12}\) for
   \(t_0=0.1\), inside Platt–Trudgian's verified range) instead of
   Polymath's effective \(tL\approx4.5\) (inferred from their \(t=0.2\),
   \(X=6\cdot10^{10}\)). This is the D4 of the 11 October
   brainstorm and the only non-RH-equivalent deliverable the heat program
   contains. Its present status is negative: the explicit region needs
   \(tL\ge5\) and \(x\ge4\pi e^{10^9}\), and 22's refined outer budget
   (Note 06/01) still needs \(L-1\ge31{,}424{,}688\) *after* a factor-3974
   improvement. First bounded test: evaluate the exponent-pair constants
   and the starting height for the \(61/24\) theorem, and compare with
   Polymath's Section 8 at \(t=0.2\), \(X=6\cdot10^{10}\). Kill criterion:
   the evaluated \(X_*(0.15)\) exceeds \(10^{13}\), or the constant cannot be
   evaluated; then this lane is closed and the frontier belongs to
   verification height alone (the 2026 claims below 0.2 are of that type).
   This task is explicit analytic number theory with no geometry in it and
   should be judged on whether it beats the published machinery.

4. **The spacetime winding certificate, as a benchmark.** Note 01/04 is a
   correct and potentially useful computational idea: all events have index
   \(-\lfloor m/2\rfloor\) of one sign, so a zero winding of \((H,H_x)\)
   around a spacetime box excludes interior collisions with a
   one-dimensional computation. Angenent's degree mechanism is the
   antecedent, as the note says. Its value is purely as a cheaper
   certificate than interval checks of \(E>0\) over the box, and it should
   be tested as such: certify one box of 21's height-112 region by winding,
   compare cost with the existing cells, and compare with Polymath's
   barrier method, which also uses the argument principle. If it is not
   cheaper by a large factor, record it as a remark. It cannot address the
   unbounded small-time region, for the reason in Section 6.

5. **If the "lifted picture" interest is to continue, aim it at a
   different question.** The covariant jets \(\mathcal D^k\vartheta(0,iq)\)
   are Hermite-weighted theta series, i.e. Maass raising operators applied
   to \(\vartheta\), with exact modularity of weight \(k+\tfrac12\); the
   coupled addition formula is the theta addition formula in disguise.
   These are real structures, but the heat flow destroys all of them except
   the inversion, and the controls show that structure at \(t=0\) is
   insufficient. A new symmetry can only matter if it survives the Newman
   deformation as a relation carrying a sign (the 13 October review's
   "selection is solved; transfer is the problem"). Any proposal should
   state that relation first, test it on \(\Phi_{c,p}\) for all \(p\), and
   only then be written up.

## 9. Repository and verification hygiene

- **Committed merge-conflict markers (portfolio-level, not 21/22).** Commit
  `bd8d0a9` ("Euler factor controls (#3)") committed unresolved
  `<<<<<<< HEAD` / `>>>>>>> 94745f3` blocks in eight files:
  `papers/investigations-2/active/19_euler_factor_controls/{README.md, DRAFT_HISTORY.md, manuscript/euler_factor_controls.tex, numerics/README.md, reviews/README.md, reviews/1_MANUSCRIPT_AND_CERTIFICATE_VERIFICATION_CLAUDE_20261014.md}`
  and `papers/investigations-2/chat-histories/claude-cowork/{index.json, 0001_...json}`.
  The two JSON files no longer parse, so the portfolio-level Claude chat
  registry is broken until the markers are resolved, and the 19 manuscript
  will not compile. `tools/check_repository_hygiene.py` does not test for
  conflict markers; adding that test would have caught this.
- **Dependencies.** Five Investigation 22 checkers
  (`certify_square_support_endpoint_collision`, `check_period_two_contour`,
  `check_positive_tail_cone`, `check_theta_center_separation`,
  `check_theta_two_endpoint_control`) import `python-flint`, contrary to the
  repository's standard-library convention; for validated enclosures that
  is the right tool, but the convention should say so once. All pass with
  python-flint 0.9.0. `check_stationary_scalar_geometry.py` imports its
  sibling `check_joint_source_current` and therefore only runs from the
  `numerics` directory without `python -I`; `check_spacetime_topology.py`
  requires `--output`; `check_recurrence_manuscript_chat_history.py`
  requires `--repo`, `--output` and the formal-replay registry's lock file,
  which is not in git, so it is a local audit rather than a replayable
  check. Everything else runs as documented.
- **R5 overlap.** The finite certificates — 21's \(|x|\le112\),
  \(0\le t\le1/2\) region and 22's box \(t\in[0.009,0.011]\),
  \(x\in[28.2,28.4]\) — lie inside the region where Polymath 15 (barrier
  at \(6\cdot10^{10}\), \(t\le0.2\)) and Platt–Trudgian (\(\Lambda\le0.2\))
  already guarantee real simple zeros, hence strict Laguerre signs by
  Proposition 1. They verify known facts and are useful only as tests of
  the machinery, which is how 22's notes present them; 21's README table
  should say the same.
- **Assertion counts.** Totals such as "12,271 exact replay assertions" are
  counts of identity checks on polynomial germs and rational surrogates; the
  receipts say so, and the READMEs should keep saying so. They are not
  evidence about theta.

## 10. Minor corrections and suggestions

- 22 §1.1, item 1, and §7: add that the chord hypotheses are necessary
  under RH (Section 4); otherwise "conditional exclusion" reads as progress
  toward a weaker statement.
- 22 §7, Remark "Comparison with stationary and angular estimates": the
  comparison of exponents is correct for general fields; add that for the
  theta field all variants are equivalent.
- 22 §8.2: state that \(\mathcal D^k\vartheta(0,iq)\) is the Hermite-weighted
  theta series and that its \(q\mapsto1/q\) law reproduces \(\Phi(-u)=\Phi(u)\);
  this makes the "covariant source formula" transparent and prevents a reader
  from looking for hidden content.
- 22 §9.1: the three-square control's raw third weight is about
  \(5.77\cdot10^4\) and the four-square control's fourth weight about
  \(2.42\cdot10^7\); both are legitimate (the Gaussian endpoint factor
  compensates), but the text should display the raw weights so a reader does
  not assume the controls are small perturbations of theta.
- 22 §12: cite Investigation 19's \(\Phi_{c,p}\) as the control that lies in
  the dilation span and forces "every prime".
- 21 README, "Established coverage" table: add that the \(|x|\le112\) row is
  implied by Polymath 15 and Platt–Trudgian, and that the \(tL\ge61/24\)
  threshold is the condition \(\Re s>1\) for the carrier's zeta factor.
- Both manuscripts: "Laguerre–Pólya class" does not occur in either; the
  concept is the right frame for every criterion and should be named.

## 11. Provenance

Repository state reviewed: commit `7eefd2a`, clean working tree, read from
a fresh clone of `ebbaker/shifted-zeta-positivity` and compared with the
local clone. Check programs were run from a scratch directory with
Python 3.13, python-flint 0.9.0 and mpmath 1.3; exit codes, assertion
counts and the independent recomputation are recorded in
[`INDEPENDENT_RECOMPUTATION_CLAUDE_20261015.json`](../numerics/INDEPENDENT_RECOMPUTATION_CLAUDE_20261015.json).
Web sources consulted for the \(\Lambda\) frontier: the Wikipedia entry on
the de Bruijn–Newman constant (bounds 1/2, \(<1/2\), 0.22, 0.2 with
attributions), Tao's post on the Polymath 15 paper, the judegomila.com post
claiming \(\Lambda\le0.1787854\) (self-published, unverified), and the
arXiv listing of 2610.12803 (not fetched). This session's chat record is
kept in this investigation's `chat-histories/claude-cowork/` registry by the
standing project instruction. No file in the repository was modified other
than the addition of this review, the recomputation script and record, and
their README entries; nothing was committed.
