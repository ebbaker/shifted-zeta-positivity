# Reflection networks and the even tower: which reflection glues the endpoint kernel

**19 September correction notice (Codex):** the continuum Gram claim below
requires an ultraviolet regulator and a domain; the backtracking calculation
misses a leading spike divergence; a norm is not automatically protected by
supersymmetry. Read the [review](../reviews/review_codex_2026-09-18.md) and the
[angular-smearing continuation](ANGULAR_SMEARING_AND_ROBIN_MODEL_20260919.md).
The latter constructs the regulated free Gram kernel and distinguishes its
positive difference-form limit from its divergent covariance. The original
derivation below is retained as a research record, with these qualifications.

**Author: Claude Fable 5.1 (Anthropic), model `claude-fable-5-1`.** 18 September
2026, for Edward Baker. Research note, answering the head item of
[CONTINUATION_20260918_CLAUDE.md](CONTINUATION_20260918_CLAUDE.md): *construct the
positive pairing before adding arithmetic* --- write one actual reflected-state
transport network, specify endpoint operators, colour contractions, reflection
and paths, compute its free kernel, and check whether the even image average
survives. It builds on the two endpoint notes of the same day
([matter](ENDPOINT_MATTER_CONTINUATION_20260918.md),
[transport](ENDPOINT_TRANSPORT_AND_SHIFT_20260918.md)) and on the source paper
[Baker, arXiv:1102.4948](https://arxiv.org/abs/1102.4948), Sections 3.1--3.2 and
Appendices B--C, which I read in full this session.

**Not claimed.** Nothing here constructs the prime atoms, the contact or pole
terms, or any statement about the Riemann hypothesis. Reflection positivity of
the interacting defect theory is *used as a hypothesis*, not proved. Clifford
identities are finite matrix identities under the displayed bulk BPS equation of
the transport note; they are not a count of physical defect supercharges, and
the defect endpoint conditions are not solved. Session cut short: Section 5 lists
what was not done.

Check programme: [`numerics/check_reflection_networks.py`](../numerics/check_reflection_networks.py),
1196 finite cases, record
[`reflection-networks-checks.json`](../numerics/records/reflection-networks-checks.json).

---

## 0. Summary

1. **There are two reflections, and they glue the two halves of the kernel.**
   The archimedean kernel is $n_\gamma=\tfrac12(G_s+G_o)$, same-ray plus
   opposite-ray. A reflection *within* the defect, $\Theta_1:x_1\to-x_1$, pairs a
   point $r$ with $-r$ and produces the opposite-ray kernel
   $G_o(u)=\frac1{2\cosh(u/2)}=\sum_n(-1)^ne^{-(n+\frac12)u}$, the **alternating**
   half-integer tower. A reflection *through* the defect, $\Theta_3:x_3\to-x_3$,
   fixes every defect point and produces the same-ray kernel
   $G_s(u)=\frac1{2\sinh(u/2)}$. Exact bookkeeping:
   $n_\gamma=G_o+G_-$, with $G_-=e^{-3u/2}/(1-e^{-2u})$ the odd tower: **the even
   tower is the alternating tower plus the three-quarter tower.**

2. **The through-the-defect network delivers the even average as a manifestly
   Gram kernel.** With the origin (the dilation fixed point) as common reference
   and $\Phi_r=W_{\rm up}[0\leftarrow r]\,q(r)$ the endpoint field transported to
   the origin along the semicircle of diameter $[0,r]$, the $\Theta_3$-even
   combination $\Phi_+(r)=\Phi_r+\Phi_{-r}$ has
   $\langle\Theta_3(\Phi_+(r_1))\,\Phi_+(r_2)\rangle\cdot\tfrac{\sqrt{r_1r_2}}4
   =n_\gamma(\log r_1/r_2)$ **at free level, exactly**; every one of the four
   transport paths is a gauge-invariant open Wilson line through the origin,
   smooth ($C^1$) there; and the kernel is positive semidefinite in $(r_1,r_2)$
   **if** the interface theory is Osterwalder--Schrader positive under $\Theta_3$
   (Section 2.2). The even image average survives.

3. **The whole two-variable family of kets shares one bulk supercharge.** Every
   upper semicircle ending at the origin, traversed into the origin --- $[0,r]$
   right-to-left and $[-r,0]$ left-to-right, for every $r$ --- is annihilated by
   the special supercharge $\epsilon_s=0$, $J\epsilon_c=-\epsilon_c$
   ($J=i\Gamma_I\Gamma_3$). This is Codex's fixed-row solution (1.5) with the
   shared endpoint moved to $0$, where $\epsilon_s=-0\cdot\Gamma_1\epsilon_c$
   vanishes, and it removes the obstruction of the transport note's Section 1 for
   this network: the failure there was a property of *pairwise* semicircles, not
   of semicircles glued at a common reference. The inversion picture makes it
   obvious: circles tangent to the $x_3$-axis at the origin are the inversion
   images of vertical lines, all traversed downward. Verified as finite Clifford
   identities (groups C--E of the programme).

4. **The within-the-defect network fails twice.** Its pairing path
   $r_1\to0\to-r_2$ meets the origin with a backtracking cusp (angle $\pi$: both
   semicircles are tangent to the $x_3$-axis there), which carries a logarithmic
   junction divergence, and its two halves share no bulk supercharge (the origin is
   the left endpoint of one arc and the right endpoint of the other, so Codex's
   shared-endpoint criterion fails). This is the sharp negative of the session,
   and it is the version of the pairwise obstruction that survives: **the
   opposite-ray half of the kernel cannot be glued within the defect; it must be
   glued through it.**

5. **Where the scalar coupling's parity enters.** From Appendix B of the source,
   $X^H_3$ sits in the 3d multiplet $\{A_3,\lambda^2,X^H_A\}$ with the normal
   gauge component, and the defect couples to $D_3X^H$, so $X^H_3$ is
   $\Theta_3$-**odd** (Section 3). Then the reflected bra carries $-X^H_3$: the
   full pairing path has the scalar coupling flip sign at the origin, and no
   *single* supercharge annihilates the whole path (group E). This is not a
   defect of the construction: a Gram pairing $\langle\Theta\Phi,\Phi\rangle$ is a
   norm, protected by $\{Q,Q^\dagger\}$ and never by $Q$ alone. What the
   cohomological route needs is a common $Q$ on the *kets*, and item 3 supplies
   it. If instead $X^H_3$ were $\Theta_3$-even the whole path would be BPS under
   the one charge; both cases are recorded.

---

## 1. The setting and the target normalization

Defect at $x_3=0$; bulk $\mathcal N=4$ SYM on both sides, same gauge group
(interface, $N_+=N_-$); 3d hypermultiplet scalars $q_m$ in the fundamental with
free propagator $\propto1/|x-y|$ (source, Section 3.2). Defect coordinate $x_1$
along a line in the defect, points $\pm r$, $u=\log(r_1/r_2)>0$. The semicircle
operator of the source is (30), $\frac1N\,q_1\,P\exp\int_C(i\,dx\cdot A+d|x|\,X^H_3)\,\bar q_1$
--- note the source's remark that the two ends of a semicircle are locally
annihilated by *different* supercharges because the relative sign of $iA_3$ and
$X^H_3$ flips with the direction of $dx$, which is why the ends carry
$q_1,\bar q_1$ (or, by the Majorana argument of its Appendix C, $\bar q_1,q_2$).
The matter note's free kernels are
$G_s=\frac{\sqrt{r_1r_2}}{r_1-r_2}=\frac1{2\sinh(u/2)}$,
$G_o=\frac{\sqrt{r_1r_2}}{r_1+r_2}=\frac1{2\cosh(u/2)}$,
$n_\gamma=\frac{G_s+G_o}2$.

**Bookkeeping (exact, group A).** In $t=e^{-u/2}$:
$G_s=\frac t{1-t^2}$, $G_o=\frac t{1+t^2}$, $n_\gamma=\frac t{1-t^4}$,
$G_-=\frac{t^3}{1-t^4}$, and
\[
 n_\gamma=G_o+G_-,\qquad G_o=\sum_{n\ge0}(-1)^ne^{-(n+\frac12)u},
 \qquad G_-=\sum_{n\ge0}e^{-(2n+\frac32)u}.
\]
So $G_o$ is the same-ray tower with the $\Theta_1$-parity $(-1)^n$ of the $n$-th
descendant inserted, $n_\gamma$ its projection to even descendants, $G_-$ to odd.
$G_o$ is regular on the diagonal with transform $\pi/\cosh(\pi\tau)>0$; $G_s$,
$n_\gamma$, $G_-$ all carry the $\frac1{2u}$ singularity and are positive only as
difference energies (group B). The divergent constant of the Weil form's
archimedean line lives entirely in the same-ray half.

## 2. The through-the-defect network

### 2.1 Definition

Let $C_r$ be the upper semicircle of diameter $[0,r]$ (for $r<0$, of $[r,0]$),
oriented from $r$ to the origin. Define the colour vector at the origin
\[
 \Phi^a_r=\big[\,P\exp\!\int_{C_r}(i\,dx\cdot A+|dx|\,X^H_3)\;q(r)\big]^a ,
 \qquad \Phi_+(r)=\Phi_r+\Phi_{-r}\quad(r>0).
\]
Each $\Phi_r$ is a functional of fields in the closed upper half-space
$x_3\ge0$ (the endpoint field lives on the reflection plane itself). The
Euclidean reflection $\Theta_3$ sends $\Phi_r$ to a bra:
\[
 \Theta_3\Phi_r=\bar q(r)\,P\exp\!\int_{\overline{C_r}'}(i\,dx\cdot A\pm|dx|\,X^H_3),
\]
the transport along the *lower* semicircle of diameter $[0,r]$ from the origin to
$r$, with the sign of the scalar coupling fixed by the $\Theta_3$-parity of
$X^H_3$ (Section 3). The pairing
\[
 \mathcal K(x,y)=\sum_a\langle(\Theta_3\Phi_x)_a\,\Phi^a_y\rangle
 =\Big\langle\bar q(x)\,W_{\rm low}[x\leftarrow0]\,W_{\rm up}[0\leftarrow y]\,q(y)\Big\rangle ,
 \qquad x,y\in\R ,
\]
is a gauge-invariant open Wilson line from $y$ up over the upper semicircle
$[0,y]$ into the origin and down through the lower semicircle $[0,x]$ to $x$.
**Smoothness at the origin.** Every upper semicircle with an endpoint at the
origin, traversed into it, arrives with tangent $-e_3$; every lower semicircle
leaving the origin departs with tangent $-e_3$. So each of the paths is $C^1$
at the origin (curvature jumps from $2/|y|$ to $2/|x|$, harmless), and it
*pierces* the defect there. At the outer endpoints the arcs meet the defect
perpendicularly, exactly as the source's semicircle does.

### 2.2 Positivity, conditional

If the Euclidean interface theory is invariant under $\Theta_3$ and
Osterwalder--Schrader positive for it, then for any finite combination
$A=\sum_ic_i\Phi^a_{x_i}$ (colour index free but at the $\Theta_3$-fixed origin)
one has $\sum_a\langle\Theta_3(A)_aA^a\rangle\ge0$, i.e. $\mathcal K$ is a
positive semidefinite kernel on the defect line, and so is its restriction to
even combinations,
\[
 \mathcal K_+(r_1,r_2)=\langle\Theta_3(\Phi_+(r_1))\,\Phi_+(r_2)\rangle
 =\mathcal K(r_1,r_2)+\mathcal K(r_1,-r_2)+\mathcal K(-r_1,r_2)+\mathcal K(-r_1,-r_2).
\]
The lattice statement behind this is Osterwalder--Seiler positivity for a
reflection through a plane of sites with an open string of links ending on the
plane, for which $\Theta$ conjugates the string into the reflected string in the
conjugate representation; the gauge-theory RP applies to all functions of the
half-space link variables, gauge invariant or not, and the colour trace at the
fixed point is what makes the pairing gauge invariant. **Hypotheses to be
audited:** (i) $\Theta_3$-invariance of the defect action (68) of the source,
with the induced parities of $X^V,X^H$ (Section 3); (ii) positivity of the
defect measure including the fermions and auxiliary fields; (iii) that a Wilson
line piercing the defect at the origin needs no extra local coupling at the
piercing point at the order considered. I have not proved any of the three.

### 2.3 The free kernel

At order $g^0$ the transports are the identity and
$\mathcal K(x,y)\propto\frac1{|x-y|}$, so
\[
 \tfrac{\sqrt{r_1r_2}}4\,\mathcal K_+(r_1,r_2)
 =\tfrac14\Big[\tfrac{2\sqrt{r_1r_2}}{r_1-r_2}+\tfrac{2\sqrt{r_1r_2}}{r_1+r_2}\Big]
 =\tfrac12(G_s+G_o)=n_\gamma(u).
\]
The even image average survives, as the covariance of the transported even field
$\Phi_+$. The difference energy of $n_\gamma$ is then
$\re\psi(\frac14+\frac{i\tau}2)-\psi(\frac14)$ by (2.2) of the matter note.
Nothing new is claimed at this order beyond the *placement* of the average inside
a Gram construction; that placement was the open item.

### 2.4 The common bulk supercharge of the kets (proof sketch under the displayed BPS equation)

Take the transport note's equation (1.1) and its solution (1.2) for an upper
semicircle $(c,R)$ traversed right-to-left with scalar sign $+$:
$\epsilon_s=-c\Gamma_1\epsilon_c-RJ\Gamma_1\epsilon_c$. Repeating the computation
for a lower semicircle, for the reverse traversal, and for scalar sign $-$ gives
the one-line orientation table
\[
 \epsilon_s=-c\,\Gamma_1\epsilon_c-\sigma R\,J\Gamma_1\epsilon_c,\qquad
 \sigma=(\text{side})\times(\text{direction})\times(\text{scalar sign}),
\]
with side $+1$ upper, direction $+1$ right-to-left (group C, 722 cases: the
residual vanishes at six angles for every sign pattern).

*Kets.* $C_r$ for $r>0$ is $(c,R)=(\frac r2,\frac r2)$, upper, right-to-left,
$\sigma=+1$: $\epsilon_s=-\frac r2(1+J)\Gamma_1\epsilon_c$. $C_{-r}$ is
$(-\frac r2,\frac r2)$, upper, left-to-right, $\sigma=-1$:
$\epsilon_s=+\frac r2(1+J)\Gamma_1\epsilon_c$. A common solution for all $r>0$
and both signs requires $(1+J)\Gamma_1\epsilon_c=0$, i.e.
\[
 J\epsilon_c=-\epsilon_c,\qquad \epsilon_s=0 ,
\]
a special supercharge whose Killing spinor $x\cdot\Gamma\,\epsilon_c$ vanishes at
the common reference point. It annihilates every arc of every circle tangent to
the $x_3$-axis at the origin traversed downward through it, on either side
(group D, 366 cases), which is the statement that under inversion about the
origin these arcs are vertical lines traversed the same way. The $J=+1$
eigenspace does not work with $\epsilon_s=0$ (group D, last cases).

*Full pairing path.* With the scalar coupling $\Theta_3$-even, the lower half
$[0,r_1]$ traversed $0\to r_1$ has $\sigma=(-1)(-1)(+1)=+1$ and the same
condition $J\epsilon_c=-\epsilon_c$: the whole path is BPS under the one charge,
for all $r_1,r_2$ (group E, kernel of $(r_1-r_2)(1+J)/2$ is the $J=-1$ space).
With the scalar coupling $\Theta_3$-odd, $\sigma=-1$ on the lower half, the
constant coefficients become $-\frac{r_1}2(1-J)$ and $-\frac{r_2}2(1+J)$, whose
difference has determinant $-r_1r_2\ne0$: no common charge for the full path
(group E). As said in the summary, the second case is the norm of a BPS state
and is the expected one.

## 3. The parity of the scalar coupling

Appendix B of the source decomposes the bulk vector multiplet under the defect
into a 3d vector multiplet $\{A_k,\lambda^1,X^V_A\}$ and a 3d hypermultiplet
$\{A_3,\lambda^2,X^H_A\}$, and the defect action (68) contains
$\sigma^I_{mn}\,\bar q^m(F^{Ia}_V-D_3X^{Ia}_H)T^aq^n$. For (68) to be
$\Theta_3$-invariant with $F_V$ even, $D_3X^H_I$ must be even, hence
$X^H_I$ odd --- the same parity as $A_3$, with which it shares a multiplet. So the
semicircle's scalar $X^H_3$ is $\Theta_3$-odd, the reflected bra carries
$-X^H_3$, and the second case of Section 2.4 is the physical one. This is a
*reading* of the source's action, not an independent derivation of the defect
theory's discrete symmetries; DeWolfe--Freedman--Ooguri should be checked for
the fermionic terms before it is used in a manuscript.

## 4. The within-the-defect network, and why it fails

Take $\Theta_1:x_1\to-x_1$, reference at the origin (the only dilation-fixed
point on the plane $x_1=0$), the same kets $\Phi_r$. The pairing
$\langle\Theta_1(\Phi_{r_1})\Phi_{r_2}\rangle$ is the open line
$r_2\to0\to-r_1$ along the upper semicircles $[0,r_2]$ and $[-r_1,0]$, which
both meet the origin tangent to the $x_3$-axis: incoming tangent $-e_3$,
outgoing $+e_3$, a backtracking cusp. Locally $x(s)\approx(s^2/r_2,\,-s)$,
$y(t)\approx(-t^2/r_1,\,t)$, the combined propagator numerator
$|\dot x||\dot y|-\dot x\cdot\dot y\to2$, and
$\iint ds\,dt\,2/|x-y|^2\sim\int d\rho\,\rho\cdot2/\rho^2=2\log(1/\epsilon)$:
a logarithmic junction divergence with the antiparallel cusp's coefficient,
infrared-regulated by the curvature (hand computation, not registered). Its two
halves share no bulk supercharge: $[0,r_2]$ and $[-r_1,0]$ have the origin as
left endpoint of one and right endpoint of the other, and the transport note's
criterion $(\Delta c)^2=(\Delta R)^2$ reads $(r_1+r_2)^2=(r_1-r_2)^2$ (group E,
determinant $r_1r_2$). Under inversion the two halves are vertical lines
traversed in opposite directions with the same scalar coupling --- the
quark--antiquark configuration, which is not BPS. Its free kernel is $G_o$
alone: **the within-defect reflection can only ever see the alternating tower.**

## 5. Status, and what was not done

**Written (elementary) proof:** the bookkeeping of Section 1 (group A) and the
transform of $G_o$ (group B). **Proof sketch under the displayed bulk BPS
equation:** the orientation table and everything in Section 2.4 (groups C--E
verify the algebra at finite points). **Conditional / reading:** positivity of
$\mathcal K$ and $\mathcal K_+$ (on OS positivity of the interface theory under
$\Theta_3$, Section 2.2); the parity of $X^H_3$ (Section 3). **Observation:**
the cusp coefficient of Section 4. **Not done, in priority order:**

1. **Audit the OS positivity hypothesis** for the D3--D5 interface under
   $\Theta_3$: parities of all defect fields from hep-th/0111135, positivity of
   the fermionic and auxiliary sectors, and the piercing point.
2. **Solve the defect endpoint conditions** for the kets $\Phi_{\pm r}$ under the
   common charge of Section 2.4 --- the source's Appendix C fixes which $q_m$
   pairs with which supercharge at an endpoint pointing into or out of the
   defect; both kets here point *into* the origin, so the endpoint polarization
   is the same for $\Phi_r$ and $\Phi_{-r}$, which is what the even average
   needs. Check this against (81)--(84) of the source.
3. **First interaction correction of $\mathcal K_+$ in one local scheme**, as the
   handoff asked: the source's (31) (arc self-exchange, constant $\frac12$ per
   arc), (42) (line--endpoint exchange), the self-energy (57), *plus the new
   exchange between the upper and lower arcs across the defect and any piercing
   term*. The two arcs are not one circle, so the constant-$\frac12$ property of
   (31) fails for the cross term; compute it. Then read off whether the
   endpoint weight moves from $\frac12$ through the matter note's (3.5).
4. **Compare with the pairwise semicircle** $\mathcal O(-r_2,r_1)$ of the matter
   note: the difference from the network path is a Stokes term at $O(g^2)$; it
   quantifies what "gluing at the origin" costs.
5. **Do not** conclude anything about the primes from this. A Gram kernel built
   from free defect fields has a spectral measure that is a sum of Lorentzians
   ($\sum_n2a_n/(a_n^2+\tau^2)$, $a_n=2n+\frac12$); the Weil kernel's is the
   discrete zero measure. The construction here settles the *placement* of the
   archimedean half inside a positive pairing and nothing more.

See the [notes index](README.md) and the [investigation index](../README.md).
