# Removing confinement from the strip comparison by a real sine tail

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex), reasoning effort ultra**.
Three same-model subagents assisted with construction and adversarial checks.
**Status: proved in-note; internal same-model checks only.** No independent
specialist review or priority claim is asserted.

This note completes the next analytic task after
[round 2](../round-2/02_BURGERS_FLOOR_AND_CONDITIONAL_COMPARISON_CODEX_20261017.md).
It removes H12 from that comparison by approximation; it does **not**
claim that H12 itself has been proved for the original character flow.
The results are incorporated in the [manuscript](../../manuscript/main.tex).
The proof uses [Cardon's Theorem 1.5](https://arxiv.org/html/1401.0237v2)
for genus-one strip functions, checked against the printed arXiv v2,
p. 3. The Fourier-only version of the strip theorem would not suffice
for the approximants constructed here.

Read with the [result-summary index](../../../../../result-summaries/README.md),
[avoid index](../../../../../avoid/README.md),
[summary 12](../../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid 01](../../../../../avoid/01_restating_the_target.md),
[06](../../../../../avoid/06_status_stronger_than_the_evidence.md),
[07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and
[16](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).
The target is an explicit positive upper bound, not a GRH criterion.

## 1. Comparison to be completed

For a real entire heat flow, write
\(F_t=e^{-t\partial_z^2}F\) and
\(S_F(x,p,t)=-\Im(F_t'/F_t)(x+ip)\). Fix the reference height \(p=3\).
For \(C>0\), set

\[
D_C(t)=1+2C(1-e^{-t/2}),\quad
m_C(t)=Ce^{-t/2}/D_C(t),\quad
I_C(t)=e^{-t}D_C(t)^{4/3},\quad
J_C(t)=\int_0^t I_C(s)\,ds. \tag{1}
\]

Round 2 proves the following compact-case statement: if the initial zeros
lie in \(|\Im z|\le1\), \(S_F(x,3,0)\ge C\) globally, the growth permits
complete Burgers characteristics, and nonreal zeros are uniformly
confined on every positive compact time interval, then
\(J_C(T)\ge1/2\), \(T\le1/2\), implies that \(F_T\) has only real zeros.
Its proof uses the floor \(S_F\ge m_C\) and, at a highest simple zero,

\[
Q'\le-2-\left(\frac43m_C(t)-1\right)Q,
\qquad 0<Q\le1. \tag{2}
\]

We retain that proved statement and discharge its extra hypotheses on
approximants with a real lattice tail.

**Theorem 1.1 (comparison without confinement).** Let \(F\) be a nonzero
real entire function of order at most one, all of whose zeros lie in
\(|\Im z|\le1\). Suppose \(S_F(x,3,0)\ge C_0>0\) for every real \(x\).
Then for \(0<T\le1/2\),

\[
J_{C_0}(T)\ge1/2\quad\Longrightarrow\quad
F_T\text{ has only real zeros}. \tag{3}
\]

The heat operator is its convergent entire-function differential series,
equivalently the Gaussian imaginary-translation integral in Section 4.
It preserves nonzeroness by the inverse semigroup identity proved in Section 4.
In the Dirichlet application nonzeroness also follows
directly from Fourier injectivity, as in round-2 Lemma 2.1.

## 2. The approximants and their global initial floor

Use a real canonical product

\[
F(z)=c e^{az}z^m\prod_{\rho\ne0}E_1(z/\rho),\qquad
E_1(w)=(1-w)e^w,\qquad c,a\in\mathbb R,\ c\ne0. \tag{4}
\]

The product includes multiplicities and complete conjugate pairs.
For \(R\ge4\), retain only zeros with \(|\rho|\le R\), obtaining \(P_R\).
Fix a comparison input \(0<C<C_0\), put

\[
\kappa=2(C+1),\quad h=\pi/\kappa,\quad
M=\lfloor R/(4h)\rfloor,
\]
\[
L_M(z)=\prod_{k>M}\left(1-\frac{z^2}{k^2h^2}\right)
=\frac{\sin(\kappa z)}{\kappa z\prod_{k=1}^M(1-z^2/(k^2h^2))},
\qquad G_R=P_RL_M. \tag{5}
\]

All added zeros are real. Every \(G_R\) is real entire of exponential
type with only finitely many nonreal zeros. Since \(P_R\to F\) and
\(L_M\to1\) locally uniformly, \(G_R\to F\).

The point of adding a tail rather than just truncating is the **global**
floor. A finite polynomial's Poisson sum tends to zero at real infinity,
so finite products alone would lose that floor.

Write \(\rho=u+iv\), \(|v|\le1\). Canonical regularization gives

\[
S_F(x,p,0)=\sum_\rho\frac{p-v}{(x-u)^2+(p-v)^2},\quad p>1, \tag{6}
\]

with positive, absolutely convergent terms. For \(|x|\le R/2\),
\(|\rho|>R\), and \(R\ge4\),
\(|x-u|\ge|\rho|-1-R/2\ge|\rho|/4\). Thus

\[
S_{P_R}(x,p,0)\ge C_0-\delta_R,\qquad
\delta_R=16(p+1)\sum_{|\rho|>R}|\rho|^{-2}\longrightarrow0. \tag{7}
\]

For the complementary region, the full lattice \(h\mathbb Z\) has
Poisson sum

\[
\sum_{n\in\mathbb Z}\frac{p}{(x-nh)^2+p^2}
=\frac{\kappa\sinh(2\kappa p)}{\cosh(2\kappa p)-\cos(2\kappa x)}
\ge\kappa\tanh(\kappa p). \tag{8}
\]

Removing its central \(2M+1\) zeros costs, when \(|x|\ge R/2\), at most

\[
\frac{(2M+1)p}{(R/2-Mh)^2}
\le\frac{8p}{hR}+\frac{16p}{R^2}. \tag{9}
\]

Both remaining Poisson sums are nonnegative. Equations (7)–(9) give

\[
\inf_x S_{G_R}(x,p,0)\ge
\min\left\{C_0-\delta_R,\,
\kappa\tanh(\kappa p)-\frac{8p}{hR}-\frac{16p}{R^2}\right\}.
\tag{10}
\]

At \(p=3\), \(\kappa\tanh(3\kappa)>C+1\), since
\(\kappa=2(C+1)>2\) and \(\tanh(3\kappa)>1/2\).
Consequently every sufficiently large \(R\) satisfies
\(S_{G_R}(x,3,0)\ge C\) for every real \(x\). No effective truncation
radius is needed; this is a proof by approximation, not a finite zero
verification.

## 3. Confinement for each fixed approximant

For fixed \(R\), absorb the finite canonical exponentials into a real
linear exponential. Equation (5) becomes

\[
G_R(z)=e^{b_R z}r_R(z)\sin(\kappa z), \tag{11}
\]

where \(b_R\in\mathbb R\), \(r_R\) is real rational, and every finite
pole of \(r_R\) is real and is canceled by a sine zero. Its asymptotic
form is \(r_R(w)=c_Rw^{d_R}(1+O_R(1/w))\), with
\(c_R\in\mathbb R\setminus\{0\}\), \(d_R\in\mathbb Z\).

Fix a bounded time interval \([0,T]\) and a strip \(|\Im z|\le B\).
For large \(|x|=|\Re z|\), and every real \(v\), put
\(w=z+2i\sqrt t\,v\). Its real part is still \(x\), so it avoids every
rational pole. Expansion at infinity and integer-power estimates give

\[
\left|\frac{r_R(w)}{c_R z^{d_R}}-1\right|
\le\frac{A_{R,T,B}(1+|v|)^K}{|x|} \tag{12}
\]

for a fixed finite \(K\). For positive degree expand
\((w/z)^{d_R}-1\); for negative degree use
\((z^{|d_R|}-w^{|d_R|})/w^{|d_R|}\) and \(|w|\ge|x|\).
The rational remainder itself is \(O(1/|w|)\), uniformly along this line.
This proves (12) including the unbounded Gaussian integration tails.

Insert (12) into the Gaussian heat integral. The weight
\(e^{2ib_R\sqrt t\,v}\) has modulus one, while the sine contributes at
most \(O_B(e^{2\kappa\sqrt T|v|})\). The Gaussian absorbs that factor
and the polynomial in (12). Its leading exponential integrals are exact.
Uniformly on the fixed strip and time interval,

\[
\frac{(G_R)_t(z)}
 {c_R z^{d_R}e^{b_Rz+(\kappa^2-b_R^2)t}}
=\sin\bigl(\kappa(z-2b_Rt)\bigr)+O_{R,T,B}(|x|^{-1}). \tag{13}
\]

No contour displacement past rational poles is involved.

Choose a fixed \(0<\eta<\min(h/4,1/2)\). On circles of radius \(\eta\)
centered at the real points \(nh+2b_Rt\), the main sine term is uniformly
bounded away from zero. For sufficiently large \(|n|\), (13) and Rouché
give exactly one zero of \((G_R)_t\) in each disk. Reality and symmetry
of the disk force that zero to be real and simple. On the remainder of
\(|\Im z|\le1\) outside these disks, the sine's modulus has a uniform
positive lower bound; (13) excludes all other sufficiently distant zeros.
All thresholds can be chosen uniformly for \(0\le t\le T\).

The zero strip needed here follows from Cardon's Theorem 1.5: take
\(\phi(z)=e^{-tz^2}\), \(\alpha^2=2t\), and quadratic factor
\(\gamma_2=0\) for \(G_R\). Its genus-one product belongs to the
required strip class. It follows that all zeros stay within
\(|\Im z|\le\sqrt{\max(1-2t,0)}\). This also identifies the differential
operator with the Gaussian integral. The hypotheses are not being
inferred from an integrable Fourier kernel, which \(G_R\) need not have.

We have therefore proved H12 for every **fixed approximant**, even
uniformly on \([0,T]\). No bound uniform in \(R\) is asserted or needed.
The same asymptotic proves that the approximant flows are nonzero and
have infinitely many zeros. Their exponential-type growth, uniform on
bounded time intervals, gives the complete-characteristic hypothesis
used in the compact-case comparison: Jensen and the canonical
logarithmic-derivative difference give at most linear real drift: the near-zero count is \(O_R(1+|x|)\),
and the reciprocal-square tail in the derivative difference is bounded.
This is more than the completeness argument in round 2 requires.

## 4. A common majorant and passage through the heat operator

Local uniform convergence alone does not justify passing an infinite
heat operator to the limit. Here a common sub-Gaussian majorant does.
Fix \(1<\sigma<2\), for example \(\sigma=3/2\).
Order at most one implies \(N(r)\le K(1+r)^\sigma\).
Use
\(\log|E_1(w)|\le K|w|\) for \(|w|\ge1/2\), and
\(\log|E_1(w)|\le K|w|^2\) for \(|w|\le1/2\).
Splitting the product at \(|\rho|=2|z|\), partial summation gives

\[
|z|\sum_{|\rho|\le2|z|}|\rho|^{-1}
+|z|^2\sum_{|\rho|>2|z|}|\rho|^{-2}
\le K'(1+|z|)^\sigma. \tag{14}
\]

The constants are independent of the truncation radius \(R\).
The fixed origin factor and linear exponential can be absorbed, so
\(|P_R(z)|\le\exp(K''(1+|z|)^\sigma)\). Also,

\[
|L_M(z)|\le\prod_{k\ge1}(1+|z|^2/(kh)^2)
=\frac{\sinh(\kappa|z|)}{\kappa|z|}\le e^{\kappa|z|}. \tag{15}
\]

Thus the \(G_R\) share a majorant \(\exp(A(1+|z|)^\sigma)\),
independent of \(R\). In

\[
F_t(z)=\pi^{-1/2}\int_{\mathbb R}e^{-v^2}
F(z+2i\sqrt t\,v)\,dv, \tag{16}
\]

that majorant is dominated by an integrable Gaussian for \(z\) in any
compact set and \(0\le t\le T\). Dominated convergence, with a compact
range split in \(v\), proves
\((G_R)_t\to F_t\) locally uniformly in \(z\), uniformly for bounded
nonnegative \(t\). Cauchy estimates give the derivative version if needed.
For nonzeroness, compose (16) with the real-translation Gaussian. Absolute
sub-Gaussian domination permits Fubini. In polar coordinates, the angular
mean of \(F(z+2\sqrt t\,r e^{i\theta})\) is \(F(z)\) by holomorphy;
the remaining normalized radial Gaussian has mass one. Thus the composition
is the identity, and a zero heat limit would force \(F\equiv0\).

Fix \(C<C_0\) with \(J_C(T)>1/2\). Section 2 supplies the exact global
floor \(C\) for large \(R\); Section 3 supplies all the compact-case
hypotheses. Hence \((G_R)_T\) has only real zeros. Hurwitz's theorem in
each open half-plane, and nonzeroness of \(F_T\), imply the same for
\(F_T\). This proves (3) whenever \(J_{C_0}(T)>1/2\), by taking
\(C\uparrow C_0\).

For equality, first use \(T+\varepsilon\le1/2\), where the integral is
strictly larger, then let \(\varepsilon\downarrow0\) and use locally
uniform heat continuity and Hurwitz again. If \(T=1/2\), ordinary strip
contraction already gives the conclusion. This handles the endpoint
without silently replacing a limiting floor by an attained one.

## 5. Dirichlet consequences and the certificate's scope

The phase-normalized primitive Dirichlet family is real entire of order
at most one. Its initial zeros lie in the critical strip, and round 1's
Euler-product argument gives

\[
C_{q,\mathfrak a}(3)
=\frac14\left[\log\frac q\pi+
\psi(1+\mathfrak a/2)\right]
-\frac12\left(-\frac{\zeta'}\zeta\right)(2). \tag{17}
\]

The [round-2 certificate](../../numerics/DIRICHLET_SCALAR_CONDITIONAL_CERTIFICATE_20261017.json)
proves, with exact rational decisions,
\(C_{q,\mathfrak a}(3)>6.105\) for every \(q\ge10^{12}\), both parities,
and
\(J_6(27/100)>0.502464325582617834>1/2\).
Its original statement was conditional on an analytic contract and H12;
this note supplies the missing implication by approximation. The stored
record and programme are unchanged. Their numerical facts do not change
status merely because the analytic consumer is now complete.

**Corollary 5.1 (proved in-note).** In the normalization
\(s=(1+iz)/2\), every primitive Dirichlet character of conductor
\(q\ge10^{12}\) satisfies \(\Lambda_\chi\le27/100\), without a GRH,
quasi-RH, or H12 assumption.

The exact elementary majorant from round 2 is

\[
B(C)=\frac{e^{1/4}}C
\left[\left(1+\frac76e^{1/4}C\right)^{3/7}-1\right]. \tag{18}
\]

Whenever \(B(C)\le1/2\) and \(C\le C_{q,\mathfrak a}(3)\), the
completed theorem gives \(\Lambda_\chi\le B(C)\). Thus
\(\Lambda_\chi=O((\log q)^{-4/7})\), uniformly over primitive characters
as \(q\to\infty\). Dobner's published lower bound \(\Lambda_\chi\ge0\)
then gives \(\Lambda_\chi\to0\). This is smoothing in the conductor
aspect; no zero-time GRH assertion follows.

## 6. Controls and a literature correction

The periodic counterexample in round 2 still shows that bounded strip,
Burgers dynamics, and a large initial floor do not prove H12. The new
argument does not make that false inference. It only needs confinement
for the explicitly constructed approximants and proves it there. Its
quantitative conclusion is compatible with that counterexample's
positive, conductor-free reality time. For an exact quantitative screen,
take \(F_t=e^t\cos z-\cosh(9/10)\). It has nonreal zeros at
\(T=27/100\), since \(\cosh(9/10)>281/200>100/73>e^{27/100}\).
Its actual initial height-three floor is less than one. For any
\(C\le1\), \(D_C(t)\le1+t\) on this interval, so
\(J_C(T)\le T(1+T)^2=435483/10^6<1/2\). The comparison therefore
rejects this false 0.27 conclusion on a control that shares the generic
strip and heat premises.

For the repository's Euler-factor controls, the precise Euler-product
allowance in (17) fails. The weighted-square, reflected, smooth, and
primitive-compatible controls lack the primitive character completion
and that arithmetic allowance. The general comparison theorem may apply
to such a control when its **actual** floor is used; it does not supply
the character floor to a function that lacks the arithmetic premise.
This is a quantitative screen, not a claim that generic transport rejects
all controls.

There is a correction to the initial search statement. Ki–Kim–Lee,
*On the de Bruijn–Newman constant*, Advances in Mathematics 222 (2009),
281–306, Section 6, Example 1, pp. 303–304, extend their qualitative
results to real primitive Dirichlet characters, including strict
\(\Lambda_\chi<1/2\). The earlier search missed this real-character
precedent. The original article was inspected through its
[full transcription](https://paperzz.com/doc/6928362/on-the-de-bruijn%E2%80%93newman-constant),
with bibliographic identity checked against the
[journal DOI](https://doi.org/10.1016/j.aim.2009.04.003).
Their complex-character example is a real self-dual combination; it is
not the non-even individual-character family here. No claim of priority
for the present quantitative theorem is made.

## 7. Review and manuscript handoff

The [focused check](../../reviews/02_SINE_TAIL_AND_MANUSCRIPT_CHECK_CODEX_20261017.md)
records the internal same-model adversarial checks, including the general
strip-operator import, the global floor at both real ends, common heat
majorant, rational-sine expansion, and limiting endpoint. The manuscript
states the quantitative theorem and the mechanism, citing this note for
the extended approximation proof and round 2 for the scalar certificate
and canonical/Burgers details. The manuscript has one editable source;
its [draft history](../../DRAFT_HISTORY.md) records the milestone.
