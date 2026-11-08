# E10 r2: canonical all-order transverse moments and the one-pair allowance

7 November 2026 UTC. Prepared for **Edward Baker** with substantial OpenAI
Codex assistance. Observable executor dispatch selection:
**gpt-6.1-sol, ultra**. This is tool-selected provenance, not independent
verification of the serving backend.

**Proved in-note:** the canonical time-zero local transverse moment obeys
one bound with explicit factorial dependence simultaneously for every
integer order. The numerical value of this bound, optimized over any
integer orders, cannot exclude one off-line pair by its center-average
signal. This is a scoped limitation of the specified allowance, not a
lower bound for the actual moment or exceptional probability.

[Request24](../research-progress/handoffs/24_TND_O_E10_R2_ALL_ORDER_REQUEST_20261107.md),
[inputs24](../research-progress/handoffs/24_TND_O_E10_R2_ALL_ORDER_INPUTS_20261107.json)
and [Decision10](../brainstorm/notes/10_TND_O_B04_R2_B05_ALL_ORDER_MOMENT_DECISION_20261107.md)
fix this revision. All eight input sizes and SHA-256 hashes matched at
entry and before writing; [return24](../research-progress/handoffs/24_TND_O_E10_R2_ALL_ORDER_RETURN_20261107.json)
records the exact inputs and output hash. This proof uses no E10 r1
transport result.

## 1. Imported constants and coordinate conversion

Fix one density exponent \(c\in(0,1)\). Choose constants \(K,D_c\ge1\)
so that the following published bounds hold:

\[
 N_\zeta(u+1)-N_\zeta(u)\le K\log(u+2)\quad(u\ge1),
 \tag{1}
\]
\[
 N_\zeta(\sigma,V)\le D_c V\log V\,
          e^{-c(\sigma-1/2)\log V}
 \quad(V\ge2,\ 1/2<\sigma<1).
 \tag{2}
\]

Here the first count includes all nontrivial zeros and the second only
those with real part greater than \(\sigma\); multiplicity is retained.
The convention \(N_\zeta(V)=\#\{0<t<V\}\) makes its increment count
\([u,u+1)\). Endpoint changes can instead be absorbed by covering with
two unit intervals as below. Importantly, \(D_c\) depends on the one
fixed \(c\), not on \(\sigma\) as \(\sigma\downarrow1/2\).

These are Corollary 2.3 and Theorem 2.4 of
[Maples–Rodgers, arXiv:1404.3080v2](https://arxiv.org/html/1404.3080v2),
version dated 4 June 2016. Their §4 equation (18) explicitly records the
exponential tail for the scaled displacement
\((\beta-1/2)\log V\), uniformly for \(V\ge2\), and confirms the needed
uniformity. Those selected primary passages were freshly checked on
7 November 2026. Enlarging the imported constants to the ranges in
(1)–(2) introduces no order dependence. No fixed-order constant from
Proposition 2.5, and no assertion for arbitrary positive tests from
its equation (19), is used.

For the complete canonical slice
\[
 H_0(z)=\tfrac18\xi(\tfrac12+iz/2),
\]
write its zeros as \(z_j=x_j+iy_j\). The exact correspondence is
\[
 \beta_j=\tfrac12-y_j/2,\qquad t_j=x_j/2,
 \qquad |y_j|=2|\beta_j-1/2|<1.
 \tag{3}
\]
Reflection across the critical line preserves \(t_j\) and multiplicity;
it exchanges the two signs of \(y_j\). There is exactly one doubling
for this reflection when bounding \(|y_j|>v\) by a right-half-plane
count. Opposite H roots have negative horizontal coordinate and cause
no further doubling in the positive band used below.

## 2. The all-order theorem

Let \(0\le\chi\le1\) be fixed, supported in \([-1,1]\), with
\(I_\chi=\int_\mathbb R\chi(u)\,du>0\). A compact \(C^2\) profile is
allowed; the proof needs only these boundedness/integrability properties.
Put, for every \(T\ge4\), \(L=\log T\), \(0<R\le1\) and
\(X\in[T,2T]\),
\[
 Q_X=\sum_j\chi((x_j-X)/R)y_j^2.
 \tag{4}
\]
Every sum includes the entire zero multiset. It is finite because the
support and the canonical strip restrict contributing zeros to a compact
rectangle. Define the fixed constants
\[
 a=c/2,\qquad C_0=8D_c,\qquad C_1=4K,\qquad
 A=C_1/a^2,\qquad C=\max\{1,C_0I_\chi/C_1\}.
 \tag{5}
\]
In particular \(A,C\ge1\), and none depends on \(T,R,p\).
Then **simultaneously for all integers \(p\ge1\)**,
\[
 \boxed{\mathcal M_p(T,R):=
  \frac1T\int_T^{2T}Q_X^p\,dX
  \le U_p(T,R):=
    CR A^p\frac{(2p)!}{L^p}.}
 \tag{6}
\]
Thus the same inequality holds for any integer-valued \(p=p(T)\),
and for any \(R=R(T)\in(0,1]\); there is no order-dependent threshold
or suppressed fixed-order constant.

### Complete band tail and local count

All roots that contribute for some center in \([T,2T]\) have
\(x_j\in B=[T-R,2T+R]\). For \(0<v<1\), reflection, (2), and
\(t_j\le T+R/2<2T\) give
\[
\begin{aligned}
 B_T(v)&:=\#\{j:x_j\in B,\ |y_j|>v\}\\
 &\le2N_\zeta(1/2+v/2,2T)\\
 &\le4D_cT\log(2T)e^{-(c/2)v\log(2T)}\\
 &\le C_0TL e^{-avL}.
\end{aligned}
 \tag{7}
\]
We used \(\log(2T)\le2L\). For \(v\ge1\), the left side is zero.
This pays both the ordinate conversion and transverse factor two,
with constants uniform as \(v\downarrow0\).

For a fixed center, all possible contributing zeta ordinates lie in
\([u,u+R]\), \(u=(X-R)/2\ge1\). Cover this closed interval by
\([u,u+1)\cup[u+1,u+2)\). Applying (1), and using
\(u+3\le T+3\le T^2\), gives
\[
 n_X:=\#\{j:|x_j-X|\le R\}
 \le K\log(u+2)+K\log(u+3)\le C_1L.
 \tag{8}
\]
The local count includes on-line zeros as well as off-line ones.

### Direct layer cake and center integration

For \(p\ge1\), weighted Hölder (or weighted Jensen) and (8) yield
\[
 Q_X^p\le(C_1L)^{p-1}
       \sum_j\chi((x_j-X)/R)|y_j|^{2p}.
 \tag{9}
\]
If all weights vanish this is immediate. Otherwise the total weight
is at most \(n_X\), and the inequality follows by dividing by that
weight. The power test is used directly; no general atomic-test
comparison is needed.

Each root has the center-width bound
\[
 \int_T^{2T}\chi((x_j-X)/R)\,dX\le RI_\chi.
 \tag{10}
\]
For the complete finite band, direct layer cake gives
\[
\begin{aligned}
 \sum_{x_j\in B}|y_j|^{2p}
 &=2p\int_0^1v^{2p-1}B_T(v)\,dv\\
 &\le C_0TL\,2p\int_0^\infty v^{2p-1}e^{-aLv}\,dv\\
 &=C_0TL\frac{(2p)!}{(aL)^{2p}}.
\end{aligned}
 \tag{11}
\]
Critical-line zeros contribute zero. Multiplicities and strict tail
thresholds are compatible with this integral identity. Integrating
(9), then using (10)–(11), proves
\[
 \mathcal M_p
 \le C_0I_\chi R C_1^{p-1}a^{-2p}(2p)!L^{-p}
 =\frac{C_0I_\chi}{C_1}
       R A^p(2p)!L^{-p}\le U_p.
 \tag{12}
\]
All steps hold for every integer \(p\) with the same constants. The
factorial is the exact Gamma-integral output, not an implicit
fixed-order dependence.

## 3. Exact one-pair center signal

Declare a plateau \(\chi=1\) on \([-\eta,\eta]\),
\(0<\eta<1\). Suppose the canonical slice has two selected conjugate
H roots \(x_0\pm id\), \(0<d<1\), with
\[
 x_0\in[T+R,2T-R].
 \tag{13}
\]
This is a conditional signal calculation, not a claim that such a pair
exists. Its entire weight profile is contained in the center band.
The two selected copies contribute exactly
\[
 Q_X^{\rm pair}=2d^2\chi((x_0-X)/R).
\]
Nonnegativity of all other terms gives, with
\(I_p=\int\chi(u)^p\,du\),
\[
 \boxed{\mathcal M_p\ge S_p:=
       \frac RT(2d^2)^p I_p
       \ge\frac{2\eta R}{T}(2d^2)^p.}
 \tag{14}
\]
Here \(2\eta\le I_p\le I_\chi\le2\) for every integer \(p\ge1\).
The last expression is the plateau contribution from the exact center
interval \([x_0-\eta R,x_0+\eta R]\), of length \(2\eta R\).
Additional multiplicity can only increase \(Q_X\).

## 4. Uniform allowance comparison, including growing order

A contradiction from (6) and this selected-pair signal would require
\(U_p<S_p\). Define
\[
 B_d=\sqrt{2d^2L/A}>0.
\qquad
 \frac{U_p}{S_p}
 =\frac{CT}{I_p}\frac{(2p)!}{B_d^{2p}}.
 \tag{15}
\]
The exponential series gives
\(e^{B_d}\ge B_d^{2p}/(2p)!\). Therefore
\[
 \boxed{\frac{U_p}{S_p}
 \ge\frac{CT}{I_\chi}e^{-B_d}
 \ge\frac{CT}{I_\chi}e^{-\sqrt{2L/A}}
 \longrightarrow\infty.}
 \tag{16}
\]
The divergence is uniform over **all** integer orders \(p\ge1\),
all \(0<d<1\), and all admissible \(R\). For example,
\(L\ge8\) implies \(\sqrt{2L/A}\le L/2\), so the ratio is at
least \((C/I_\chi)T^{1/2}\). The same proof compares \(U_p\)
with the plateau lower signal, replacing \(I_p\) by \(2\eta\).
No order schedule, including one tending arbitrarily fast to infinity,
can make this particular upper allowance smaller than the one-pair
signal at large height.

For completeness, Markov's inequality yields the separate statement
\[
 \frac1T\bigl|\{X\in[T,2T]:Q_X\ge2d^2\}\bigr|
 \le\min\{1,U_p/(2d^2)^p\}.
 \tag{17}
\]
The pair would force the left side to be at least \(2\eta R/T\).
The ratio of the second allowance in (17) to that forced fraction is
at least \((CT/(2\eta))e^{-\sqrt{2L/A}}\). The ratio of the trivial
allowance 1 to it is \(T/(2\eta R)\ge T/(2\eta)\). Thus their minimum
also cannot exclude the pair, uniformly over all orders.

Equations (16)–(17) lower-bound the **chosen upper allowance**, not
\(\mathcal M_p\) and not the actual exceptional probability. The
actual moment could be much smaller, even zero. The proof does not
assert that this allowance is an optimal consequence of every piece of
canonical arithmetic information.

## 5. Scope, verification and remaining gap

The gain is a complete canonical inequality with a displayed all-order
constant, together with a uniform order comparison for its specified
consumer. It extends the earlier fixed-order bookkeeping without assuming
RH, simplicity, or transport to time zero. The finite time-zero sums
are the full canonical zero multiset in the band; no zero prefix or
source truncation is substituted. No collision-time theorem follows.

The bound imports genuine canonical density information. Polynomial
heat controls are not asserted to satisfy that arithmetic density
hypothesis. The scoped failure follows instead by comparing the exact
allowance (6) with (14). It does not exclude sharper local density,
prime correlations, coupled estimates, other observables or all moment
methods. The missing input remains a stronger independently acquired
canonical endpoint/flux estimate that beats the one-pair center cost.
This retains the [result index](../../../../../result-summaries/README.md),
[controls](../../../../../result-summaries/12_collision_controls_and_screening.md),
[patterns index](../../../../../avoid/README.md),
[target classification](../../../../../avoid/01_restating_the_target.md)
and [scope discipline](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
The theorem is a quantitative corollary of its imported density/count
inputs; no priority claim is made, and all-covering-window transverse
vanishing is still RH.

The primary-source check above was limited to the named passages.
[Source-use11](../references/11_TND_O_ALL_ORDER_DENSITY_SOURCE_USE_20261107.md)
and the existing [catalog record08](../references/08_TND_O_B03_LOCALIZED_STATISTICS_SOURCE_USE_20261106.md)
already identify the article; no new article, PDF or bibliography entry
was added. The frozen source/normalization and localized-statistics
sections, Note16 and current register supplied context, not additional
unproved premises for (6).

One theorem/consumer package and one local consistency/repair check were
completed. The check rederived the coordinate/reflection factors, closed
unit-interval cover, layer-cake factorial, cancellation of \(R\) in the
ratio, and its uniformity for varying \(p,d,R\). No mathematical repair,
numerical or symbolic research run, subdelegation, redesign, manuscript
edit, commit or push was needed. Only this note and return24 were written.
No worker source transcript exists; none was invented. This internal LLM
proof package retains shared-premise limitations and awaits assessment;
it is not independent specialist review.
