# The transfer is an inner function: resonance, escaped mass, and an answer to Problem 8.1

**Author: Claude Opus 5 (Anthropic).** 17 September 2026. Research note,
written after [manuscript 0.1](../manuscript.pdf) and answering its
Problem 8.1. **No manuscript change has been made**; Section 9 lists the changes
this note recommends, for a separate pass.

Everything below concerns the arithmetic side. No gauge theory is chosen, no
source is constructed, and no positivity is proved. Sections 2, 3 and 5 are
**conditional on the Riemann hypothesis** and are labelled where they occur; they
are not a route to a proof, and Section 5.1 explains structurally why no
statement of this kind could be.

> **Status, same day.** Section 6 of this note is **corrected** by the
> [critical-path note](CRITICAL_PATH_20260917.md), Section 6: the prolate-leakage
> proposal is too simple, since the recorded collapse of the margin is far
> steeper than the bandwidth-$\gamma_1$ prolate rate. Section 5.1's Proposition 4
> is **upgraded** there to Corollary C, with a proof and a dichotomy. Everything
> else here stands.

Numerical verifications quoted here were run with `mpmath` outside the
repository and are labelled; they are not registered check programmes.
Section 9 says which of them should become one.

---

## 0. Summary

Five things, in the order they were found.

1. **The transfer symbol is unimodular on the critical line**, exactly and
   unconditionally: \(|K_\omega(i\tau)|=1\) for every real \(\tau\) and every
   \(\omega\). It follows from the functional equation and nothing else.
   Verified to 31 digits.
2. **Under RH the transfer is a unitary all-pass filter**, causal, and inner in
   the right half-plane, with zeros at \(\omega+i\gamma_\rho\). Consequently the
   contraction defect is an exact boundary flux:
   \(\langle f,D_{\omega,L}f\rangle=\int_{L/2}^\infty|(V_\omega f)(x)|^2dx\).
   Weil positivity on \(I_L\) is the statement that the flow pushes mass out of
   the leading endpoint and never pulls it in.
3. **The Weil form is the resonant absorption at the zeros.** As
   \(\omega\downarrow0\), \(|K_\omega(i\tau)-1|^2\) becomes a Lorentzian of
   height 4 and width \(\omega\) at each \(\gamma_\rho\), of mass \(4\pi\omega\),
   so \(\frac1{2\pi}\int|K_\omega-1|^2|\widehat F|^2\to
   2\omega\sum_\rho|\widehat F(\gamma_\rho)|^2=2\omega\,Q_{0,L}[f]\). The zeros
   are the resonances of the filter; the Weil form is the total resonant
   response of the input. Verified numerically to better than 0.5%.
4. **The Weil symbol is the group delay.** The phase of \(K_\omega\) is
   \(-2\arg\xi(\frac12+\omega+i\tau)\), whose \(\tau\)-derivative is \(\pi\)
   times the zero density, with smooth part \(\theta'(\tau)\). So the group delay
   is \(2\theta'(\tau)=b(\tau^2)+w_0\). **This explains the density identity of
   the companion investigation** rather than merely reproducing it. Verified.
5. **Problem 8.1 is answered, negatively, three times over.** The flow
   formulation does not escape the criticality. The useful part is the reason:
   the shifted family is a **graded** criterion, and a bound at fixed \(\omega\)
   buys exactly a zero-free strip of width \(\omega\) --- a real theorem, but not
   RH. The missing quantifier is \(\omega\downarrow0\), not uniformity in \(L\).
   Section 6
   then extracts from this a candidate **mechanism** for the superexponential
   collapse of the margin, which is open direction A2 of the companion
   investigation.

---

## 1. The symbol is unimodular, exactly and unconditionally

Recall \(\mathcal F(p)=\xi(\frac12+p)\) and
\(K_\omega(p)=\mathcal F(p-\omega)/\mathcal F(p+\omega)\).

> **Proposition 1.** For every real \(\tau\) and every \(\omega\) with
> \(\xi(\frac12+\omega+i\tau)\neq0\), \(|K_\omega(i\tau)|=1\).

*Proof.* \(\xi(s)=\xi(1-s)\) gives
\(\xi(\frac12-\omega+i\tau)=\xi(\frac12+\omega-i\tau)\), and \(\xi\) has real
Taylor coefficients about \(s=\frac12\), so \(\xi(\bar s)=\overline{\xi(s)}\) and
\(\xi(\frac12+\omega-i\tau)=\overline{\xi(\frac12+\omega+i\tau)}\). Numerator and
denominator are complex conjugates. \(\square\)

Two lines, no hypothesis, and the program's background does not record it. Its
consequence is that \(\Theta_\omega\) is an **all-pass filter**: it changes no
amplitude at any frequency, only phase. Everything below is a consequence of
asking where the phase goes.

*Numerical check (mpmath, 30 digits, not a repository programme).* Worst
\(\big||K_\omega(i\tau)|-1\big|\) over \(\omega\in\{0.5,0.3,0.05,0.001\}\) and
\(\tau\in\{0.3,5,14.1,30,123.456\}\): \(5.9\times10^{-31}\).

### 1.1 A trap worth recording

\(K_\omega\) has poles only where \(\xi(\frac12+p+\omega)=0\), i.e. at
\(p=\rho-\frac12-\omega\); under RH these sit on \(\operatorname{Re}p=-\omega\). But
\(a_\omega=-\partial_\omega\log K_\omega\) has poles at \(p=\rho-\frac12\pm\omega\),
so under RH it has poles on \(\operatorname{Re}p=+\omega\), inside the right half-plane.
Therefore:

- the contour of the inverse Laplace transform **may** be moved from
  \(\operatorname{Re}p=\eta>1\) to \(\operatorname{Re}p=0\) for \(K_\omega\), and
- it **may not** for \(a_\omega\).

This matters because unimodularity forces
\(\operatorname{Re}a_\omega(i\tau)=-\partial_\omega\log|K_\omega(i\tau)|=0\), which looks like
it makes \(Q_{\omega,L}\) vanish. It does not: \(a_\omega(i\tau)\) is an analytic
continuation past the poles at \(\operatorname{Re}p=+\omega\) and is *not* the symbol of the
causal operator. The residues picked up in that crossing are the whole of the
form, and as \(\omega\downarrow0\) they become \(2\pi\sum_\rho\delta(\tau-\gamma_\rho)\),
which is the spectral form \(Q_{0,L}[f]=\sum_\rho|\widehat F(\gamma_\rho)|^2\).
I nearly concluded the opposite; the next reader should not have to.

Separately: the four apparent poles of \(a_\omega\) at \(p=\pm\frac12\pm\omega\)
in the factor decomposition of manuscript Theorem 3.1 **cancel** between the
\(\frac12s(s-1)\), \(\Gamma\) and \(\zeta\) factors --- \(\psi\) has a pole at
\(p=-\frac12\) and \(\zeta'/\zeta\) has one at \(p=\frac12\), with matching
residues. The manuscript's proof is unaffected, because it transforms each factor
separately on \(\operatorname{Re}p=\eta>1\) where all converge, and sums; but one must not say
that \(a_\omega\) has those poles.

## 2. Under RH the transfer is unitary, and the defect is a boundary flux

**Conditional on RH throughout this section.**

Under RH, \(K_\omega\) is analytic on \(\operatorname{Re}p\geq0\) (its poles sit at
\(\operatorname{Re}p=-\omega\)), is bounded there --- the \(\Gamma\)-ratio gives
\(K_\omega(p)=O(|p|^{-\omega})\) as \(|p|\to\infty\) in the closed right
half-plane, while the \(\zeta\) and pole ratios tend to 1 --- and is unimodular on
the boundary by Proposition 1. So \(K_\omega\) is an **inner function** of the
right half-plane, with zeros exactly at \(p=\omega+i\gamma_\rho\); the Blaschke
condition \(\sum_\rho\omega/(1+\gamma_\rho^2)<\infty\) holds, so it is
essentially the Blaschke product over the Riemann zeros translated right by
\(\omega\).

Since no pole lies between \(\operatorname{Re}p=\eta>1\) and \(\operatorname{Re}p=0\), the inverse Laplace
contour may be moved to the imaginary axis, and the causal kernel \(k_\omega\) is
the inverse Fourier transform of \(K_\omega(i\cdot)\). Hence:

> **Proposition 2 (conditional on RH).** \(V_\omega\) is unitary on
> \(L^2(\mathbb R)\) and causal. Consequently, for \(f\) supported in \(I_L\),
> \[
>   \langle f,D_{\omega,L}f\rangle
>   =\lVert(1-P_L)V_\omega f\rVert^2
>   =\int_{L/2}^{\infty}\big|(V_\omega f)(x)\big|^2\,dx .
> \]

*Proof.* \(\lVert V_\omega f\rVert=\lVert f\rVert\), so
\(\lVert f\rVert^2-\lVert P_LV_\omega f\rVert^2
=\lVert V_\omega f\rVert^2-\lVert P_LV_\omega f\rVert^2
=\lVert(1-P_L)V_\omega f\rVert^2\). Causality gives
\(\operatorname{supp} V_\omega f\subseteq[-L/2,\infty)\), so the mass outside \(I_L\) is all to
the right. \(\square\)

**This is the sharpest statement in the note.** The contraction defect is not an
abstract operator quantity: it is the **flux of \(|V_\omega f|^2\) through the
leading endpoint** of the interval. Weil positivity on \(I_L\) says the flow
pushes mass out of the moving end and never pulls it in.

It also confirms, from a second direction, what Section 6 of the manuscript found
geometrically: the endpoint variation is rank one and sits at the leading
endpoint (Proposition 6.1 there). The defect is the flux through exactly that
point. The two statements are the same fact seen from either side.

*Caveat on direction.* Proposition 2 uses RH. It is the easy direction of the
program (RH \(\Rightarrow\) contraction) made explicit, not a route to a proof.
Its value is that it exhibits the mechanism, which is what Sections 5 and 6 use.

## 3. The Weil form is the resonant absorption at the zeros

Near a simple zero \(\gamma\), write \(\xi(\frac12+\omega+i\tau)\approx
\xi'(\rho)\,(\omega+i(\tau-\gamma))\). By Proposition 1 the numerator is its
conjugate, so
\[
 K_\omega(i\tau)\;\approx\;e^{i\alpha}\frac{\omega-i(\tau-\gamma)}{\omega+i(\tau-\gamma)} ,
\]
a Blaschke factor times a constant phase, and matching the requirement that
\(K_\omega\to1\) away from the zero as \(\omega\downarrow0\) fixes the constant.
The result is a clean line shape:

> **Proposition 3.** As \(\omega\downarrow0\), near each \(\gamma_\rho\),
> \[
>  |K_\omega(i\tau)-1|^2=\frac{4\omega^2}{\omega^2+(\tau-\gamma_\rho)^2}+o(1),
> \]
> a Lorentzian of height 4 and half-width \(\omega\), of total mass
> \(4\pi\omega\). Hence for any admissible \(f\),
> \[
>  \frac1{2\pi}\int_{\mathbb R}|K_\omega(i\tau)-1|^2|\widehat F(\tau)|^2\,d\tau
>  \;\longrightarrow\;2\omega\sum_\rho|\widehat F(\gamma_\rho)|^2
>  \;=\;2\omega\,Q_{0,L}[f].
> \]

The right-hand identity is the spectral form of the target. So the leading
behaviour of the defect, \(\langle f,D_{\omega,L}f\rangle=2\omega Q_{0,L}[f]+o(\omega)\),
is not a formal consequence of the flow identities but a statement about **line
shapes**: each zero is a resonance of the all-pass filter, of width \(\omega\)
and fixed integrated strength, and the Weil form is the total resonant response
of the input.

*Numerical check (mpmath, not a repository programme).* At \(\gamma_1=14.1347251\):

| \(\omega\) | \(\frac1{2\pi}\int_{|\tau-\gamma_1|<1}|K_\omega-1|^2\) | \(2\omega\) | ratio |
|---|---|---|---|
| 0.05 | 0.0973377 | 0.1 | 0.9734 |
| 0.02 | 0.0395859 | 0.04 | 0.9896 |
| 0.01 | 0.0198975 | 0.02 | 0.9949 |

Over a window containing thirteen zeros, \([10,60]\):

| \(\omega\) | integral | \(2\omega\times13\) | ratio |
|---|---|---|---|
| 0.02 | 0.517612 | 0.520 | 0.99541 |
| 0.01 | 0.259417 | 0.260 | 0.99776 |

The pointwise line shape matches too: at \(\omega=0.01\) and
\(\tau-\gamma_1\in\{0,\omega,2\omega,5\omega\}\) the computed
\(|K_\omega-1|^2\) is \(3.99987,\,1.97679,\,0.78149,\,0.14500\) against the
Lorentzian's \(4,\,2,\,0.8,\,0.153846\).

### 3.1 What RH is, in this language

A zero at \(\operatorname{Re}\rho=\frac12+\delta\) puts a **pole** of \(K_\omega\) at
\(\operatorname{Re}p=\delta-\omega\). For \(\omega>\delta\) that pole is still in the left
half-plane and \(K_\omega\) remains inner; for \(\omega<\delta\) it crosses into
the right half-plane, \(K_\omega\) is no longer bounded there, \(V_\omega\) is
unbounded, and \(\lVert V_{\omega,L}\rVert>1\) for \(L\) large. So

> **the shift \(\omega\) is a detection threshold: the family at shift
> \(\omega\) sees only zeros at distance more than \(\omega\) from the critical
> line.**

That is why Proposition 2.2 of the manuscript quantifies over \(\omega_j\downarrow0\)
and why the shift disappears from the conclusion. It is also the cleanest
statement of what the shifted family is *for*, and it is the hinge of Section 5.

## 4. The Weil symbol is the group delay

Write \(\xi(\frac12+\omega+i\tau)=Re^{i\Psi}\). By Proposition 1,
\(K_\omega(i\tau)=e^{-2i\Psi(\tau,\omega)}\), so the filter's phase is
\(\varphi=-2\Psi\) and its **group delay** is
\[
 -\frac{d\varphi}{d\tau}=2\,\partial_\tau\Psi
 =2\,\operatorname{Re}\frac{\xi'}{\xi}\Big(\tfrac12+\omega+i\tau\Big).
\]
By the argument principle \(\partial_\tau\Psi\) is \(\pi\) times the density of
zeros, whose smooth part is \(\theta'(\tau)\), \(\theta\) the Riemann--Siegel
theta function. Hence

> **the group delay of the transfer is \(2\theta'(\tau)\), which is exactly
> \(b(\tau^2)+w_0\).**

The companion investigation found \(b(\tau^2)+w_0=2\theta'(\tau)\) as an
identity between special functions and drew from it that the contact constant is
"not an independent object requiring a mechanism". Section 4 says *why*: the
archimedean symbol is a **phase derivative**, the contact is the \(-\log\pi\)
inside it, and neither is a separate ingredient because a phase has no
separate ingredients. It also explains the unboundedness rule: the group delay
grows like \(\log\tau\), so a packet at frequency \(N\) is held for a time
\(\sim\log N\), which is Proposition 3.4's \(Q_L[\chi e^{iNx}]/\log N\to\lVert\chi\rVert^2\)
read as a delay rather than as a divergence.

*Numerical check (mpmath, not a repository programme).* Over \(\tau\in[20,70]\),
which contains 16 zeros, \(\int\operatorname{Re}(\xi'/\xi)(\frac12+\omega+i\tau)\,d\tau\) is
\(49.712\) at \(\omega=0.2\) and \(50.121\) at \(\omega=0.05\), against
\(\pi\times16=50.265\); the residual difference from
\(\theta(70)-\theta(20)=47.792\) is the constant and \(S(T)\) terms of the
Riemann--von Mangoldt formula. (Quadrature must be split at the zeros; a naive
rule under-resolves peaks of width \(\omega\) and reports a ratio near 0.64.)

## 5. Problem 8.1: the flow formulation does not escape the criticality

Manuscript Problem 8.1 asked whether a strict contraction
\(\lVert V_{\omega,L}\rVert\leq1-\varepsilon\) at fixed \(\omega>0\), uniform in
\(L\), is consistent, and observed that if it were, the flow formulation would be
the only formulation in the program where a mechanism with a margin is not
self-refuting. **The answer is no.** Three arguments, increasingly sharp.

### 5.1 It is the wrong kind of statement (this is the decisive one)

Section 3.1 gives the shifted family a reading that makes the answer immediate.

> **Proposition 4 (sketch; the shifted family is a graded criterion).** Suppose
> \(\xi\) has a zero \(\rho_0\) with \(|\operatorname{Re}\rho_0-\frac12|=\delta>\omega\).
> Then \(K_\omega\) has a pole at \(\operatorname{Re}p=\delta-\omega>0\), the
> causal kernel \(k_\omega\) acquires a component growing like
> \(e^{(\delta-\omega)x}\), and \(\lVert V_{\omega,L}\rVert\to\infty\) as
> \(L\to\infty\). Contrapositively: if \(\lVert V_{\omega,L}\rVert\leq1\) for all
> large \(L\) at one fixed \(\omega\), then \(\xi\) has no zero at distance more
> than \(\omega\) from the critical line.

So the shifted family is not one criterion but a **graded family** of them, one
per \(\omega\), interpolating between the trivial statement at \(\omega=\frac12\)
(no zeros outside the critical strip) and the Riemann hypothesis as
\(\omega\downarrow0\). Each \(\omega\) buys exactly a zero-free strip of width
\(\omega\).

That settles Problem 8.1 at the level of quantifiers. A mechanism producing a
strict contraction at one fixed \(\omega>0\), however uniform in \(L\), would
establish a zero-free strip of width \(\omega\) --- a real and currently open
theorem, and a strong one, but **not** the Riemann hypothesis. The quantifier
that is missing from such a statement is \(\omega\downarrow0\), not uniformity in
\(L\); and the margin cannot survive that limit, because
\(\langle f,D_{\omega,L}f\rangle=2\omega Q_{0,L}[f]+o(\omega)\) vanishes with
\(\omega\) by construction. The hoped-for escape does not exist even in
principle, and the correct reading of the manuscript's Proposition 2.2 is that
its two limits do different jobs: \(L_j\to\infty\) covers every test function,
and \(\omega_j\downarrow0\) closes the detection threshold.

### 5.2 The escaped mass vanishes (conditional on RH)

By Proposition 2, \(\langle f,D_{\omega,L}f\rangle=\int_{L/2}^\infty|(V_\omega f)|^2\).
Fix \(g\in C_c^\infty([0,1])\) and let \(f_L(x)=g(x+L/2)\), a copy of \(g\) parked
at the trailing endpoint of \(I_L\). Then \(V_\omega f_L\) is a translate of the
fixed function \(h=k_\omega*g\), so
\[
 \frac{\langle f_L,D_{\omega,L}f_L\rangle}{\lVert f_L\rVert^2}
 =\frac{1}{\lVert g\rVert^2}\int_L^\infty|h(u)|^2\,du\;\longrightarrow\;0
 \qquad(L\to\infty),
\]
because \(h\in L^2\). So \(\inf\operatorname{spec}D_{\omega,L}\to0\) at every
fixed \(\omega\): no uniform margin. The rate is the \(L^2\) tail of \(h\), which
is governed by the poles of \(K_\omega\) at \(\operatorname{Re}p=-\omega\) and should be
\(e^{-2\omega L}\) up to the density of zeros; I have not made that precise and
it is not needed for the conclusion.

### 5.3 Zero avoidance (conditional on RH, and the most informative)

By Proposition 3, \(\langle f,D_{\omega,L}f\rangle\approx2\omega\sum_\rho|\widehat F(\gamma_\rho)|^2\).
A margin would say that no unit \(f\) supported in \(I_L\) can make its Fourier
transform small at every \(\gamma_\rho\) simultaneously. That is false, and gets
more false as \(L\) grows: the space of functions supported in \(I_L\) and
essentially bandlimited below \(\gamma_1=14.1347\) has dimension about
\(L\gamma_1/\pi\), and every one of them has \(|\widehat F|\) small at every
\(\gamma_\rho\).

## 6. A candidate mechanism for the collapse of the margin

Section 5.3 is worth more than the answer to Problem 8.1, because it converts the
program's least-understood number into a classical question.

Combining Propositions 2 and 3, the margin of the flow --- and, in the limit, the
margin of the central form --- is
\[
 \lambda_{\min}(Q_{0,L})
 =\min_{\lVert f\rVert=1,\ \operatorname{supp} f\subseteq I_L}\ \sum_\rho|\widehat F(\gamma_\rho)|^2 .
\]
This is exact and is just the spectral form; what Section 3 adds is the reading:
**the margin is how well a function supported in an interval can avoid the
Riemann zeros in frequency.** Two consequences.

**The band edge is explained rather than observed.** The cheapest way to avoid
every \(\gamma_\rho\) is to live below the lowest one, so the near-null
directions are bandlimited below \(\gamma_1\). That is exactly the numerical
observation of the bottleneck note and selection rule 7's second half, which the
companion investigation recorded as a measurement. Here it is a consequence.

**The collapse should be prolate decay.** The best such \(f\) is the interval's
leading prolate spheroidal function at bandwidth \(\gamma_1\), and its
out-of-band leakage is the classical Slepian eigenvalue deficit, which decays
superexponentially in the time--bandwidth product \(c=L\gamma_1/2\) once the
mode count \(2c/\pi\) is exceeded. That is the right shape to compare with the
recorded margins --- \(\lesssim10^{-9}\) at \(L=1\), \(1.2\times10^{-24}\) at
\(L=3\), and Zhu's \(3.2\times10^{-283}\) at \(L=2\) in his own normalization.

> **This is a candidate mechanism for open direction A2 of the companion
> investigation**, which asks for "a mechanism rather than a measurement" for the
> collapse. **It is not yet a computation.** I have not done the prolate estimate,
> and the comparison above is a shape comparison, not a fit; the leakage of the
> leading prolate is an upper bound on \(\lambda_{\min}\) and would need the zeros
> above \(\gamma_1\) handled before it could be a two-sided statement. That is the
> first thing to do next, and it is cheap.

## 7. What this does to the Wilson-line picture

**The abelian obstruction is explained, not weakened.** Manuscript Theorem 4.2
proves the shift flow is abelian; Section 1 says why in one word --- it is an
*all-pass filter*, and a filter that changes only phase is a phase, hence
abelian. Nothing here reopens that.

**Condition W1 sharpens into a checkable test.** The manuscript's first proposed
condition asks for an unbounded connection in an infinite-dimensional
representation. Section 4 gives the quantitative form: the holonomy's **group
delay must grow like \(\log\tau\)**, with the smooth part exactly
\(2\theta'(\tau)\). A holonomy in a finite-dimensional representation of a
compact group has a bounded group delay, which is the same exclusion with a
number attached, and which can now be checked against a candidate by computing
one phase derivative.

**The picture the mathematics is pointing at is scattering, not holonomy.** A
causal, unitary, all-pass operator with poles just off the axis, whose phase
derivative is a density of states, is a **scattering matrix**; its resonances are
the zeros, and its group delay is the Wigner--Smith time delay. The flow
formulation therefore lands, from the program's own shifted family, on the object
that a Wilson-line picture would have to reproduce: not a holonomy with a
curvature, but a **scattering phase whose Wigner delay is the smooth zero
density**. I record plainly that this neighbourhood is crowded --- the idea of the
zeros as resonances or scattering phases is old --- and claim nothing new for the
idea. What is this program's own is the derivation from \(K_\omega\), the exact
constants in Sections 3 and 4, and the fact that the archimedean symbol and the
contact are a single phase derivative.

**The endpoint story is confirmed.** Proposition 2 says the defect is the flux
through the leading endpoint, which is exactly the point where manuscript
Proposition 6.1 found the rank-one endpoint variation. The two are the same fact.

## 8. Status of each claim

- **Proposition 1** is a written proof, unconditional, and verified to 31 digits.
- **Section 1.1** is a written argument about pole locations and contour shifts;
  the cancellation of the \(\pm\frac12\pm\omega\) poles is elementary from the
  residues of \(\psi\) and \(\zeta'/\zeta\).
- **Proposition 2** is a written proof **conditional on RH**, using boundedness
  of \(K_\omega\) on the closed right half-plane, which rests on the
  \(\Gamma\)-ratio asymptotic quoted without proof here.
- **Proposition 3**'s line shape is a written local computation; the passage to
  the sum over all \(\rho\) is stated, not proved uniformly, and is supported by
  the two numerical tables. Verified at one zero and over a thirteen-zero window
  to better than 0.5%.
- **Section 4** is a written derivation resting on the argument principle and the
  Riemann--von Mangoldt formula, both standard, and is verified to 0.3% at
  \(\omega=0.05\).
- **Section 5.1** is an argument about quantifiers and is unconditional.
  **Sections 5.2 and 5.3** are conditional on RH.
- **Section 6** is a **proposal with a numerical shape comparison**, not a
  computation. The prolate estimate has not been done.
- **Section 7** is assessment.
- All numerics here were run with `mpmath` outside the repository and are not
  registered check programmes.

## 9. Recommended changes to the manuscript (not made)

Held for a separate pass, at the investigator's instruction.

1. **New section between the present Sections 3 and 4**, "The transfer is an
   all-pass filter": Proposition 1, the trap of Section 1.1, Proposition 2, and
   Proposition 3. This is the natural home for the material and it makes the
   present Section 4 a corollary rather than a surprise.
2. **Fold Section 4 of this note into the present Section 3** as a remark, since
   it explains the density identity the manuscript already cites.
3. **Replace Problem 8.1 by a theorem** with the three arguments of Section 5,
   and re-rank the order of work in Section 8 accordingly: the decisive question
   is now the prolate estimate of Section 6, not the criticality question.
4. **Sharpen Condition 7.1 (W1)** to the group-delay form of Section 7.
5. **Extend the check programme** with: unimodularity on a grid, the Lorentzian
   line shape and its mass, and the window-absorption identity. These need
   \(\xi\), so under the repository's standard-library rule they should be built
   from **hard-coded published zero ordinates** via a finite Blaschke product,
   as `check_explicit_formula.py` in the companion investigation does, verifying
   the mechanism rather than the arithmetic.
6. **Add a reference** for prolate spheroidal functions and the Slepian
   eigenvalue decay, once Section 6 is actually computed.
