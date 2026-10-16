# Floor-backed cumulative energy: a quantified obstruction to an HS complement estimate

20 September 2026. Prepared for Edward Baker.

**Model:** OpenAI GPT-6 (Codex; developer-provided identity).
**Effort setting:** not exposed in this session; not inferred.
**Status:** new analytic operator estimates with exact rational scalar checks.
No new floating coupling diagnostic, certificate of the target operator norm,
or independent specialist review is claimed.

## 1. Definite result and its scope

Keep
\[
 L=\tfrac12,\quad h=\tfrac1{20},\quad w=10^{-3},\quad
 \delta=\frac{24999}{500000000},\qquad
 \mathcal C=F^{-1/2}YE^{-1/2}.
\]
The [new review](../../wilson-loewner/reviews/review_gaussian_endpoint_followup_20260920.md)
is correct: every fixed finite-tower cumulative lower operator is compact.
Section 2 verifies its hypotheses, including a uniform bound near zero
independent of the anchor. Such an operator alone is not an invertible
all-input metric.

The specific estimate attempted here is more informative than the earlier
scalar route. Retain the **exact cumulative energy of all 32 prescribed
tower modes**, combine it by a valid convex combination with the scalar
floor, split in that energy metric, and use a Hilbert--Schmidt (HS) norm to
control the remaining mixed block. This is a natural finite-head/complement
certificate, but it cannot succeed at the head sizes treated here:

\[
 \boxed{\quad
 \|P_{\rm new}^{\perp}\mathcal B_{\theta_L,\theta_h}
                  P_{\rm old}^{\perp}\|_{\rm HS}>\frac32
 \quad}
 \tag{1.1}
\]

for **every** \(0<\theta_L,\theta_h\le1\) and **every** pair of
rank-16 heads in the normalized coordinates. The proxy
\(\mathcal B\), its coercive lower metrics, and their comparison with
\(\mathcal C\) are defined in Section 3. In particular (1.1) applies to
the explicit energy-orthogonal logarithmic heads in Section 4, which reach
distances of order \(he^{-64}\) from the join. It does not depend on
cosine resolution, quadrature accuracy, or how favorably the other three
blocks are computed. At \(\theta_L=\theta_h=1/2\), the stronger bound
is **HS norm greater than 3**.

This is an obstruction to **using HS as the upper estimate for that block**.
An HS norm above one does not prove its operator norm above one. In
particular neither \(\|\mathcal B\|>1\) nor \(\|\mathcal C\|>1\)
is established. Spectral-norm estimates with these same lower metrics
remain possible. The all-input target \(\|\mathcal C\|<1\) is unresolved.

A second concrete result addresses an elementary implementation of the
exact identity-minus-compact alternative. If one simply discards the
transfer kernel for delays below \(\rho=10^{-p}\), obtaining a transfer
error at most \(\delta/10\) requires
\[
 p>5296.682562\ldots;
 \tag{1.2}
\]
the outward rational check proves in particular \(p>5200\). This concerns
that diagonal-cutoff scheme, not the complexity of arbitrary approximations.

## 2. Compactness audit, with the hypotheses checked

The local requested review, both Gaussian handoffs, Gaussian calculation,
the [cumulative append note](CUMULATIVE_APPEND_SCALAR_OBSTRUCTION_20260920.md),
its [handoff](RESEARCH_CONTINUATION_AFTER_CUMULATIVE_APPEND_20260920.md),
the [original-transfer anchor](EMA_TOWER_ORIGINAL_TRANSFER_ANCHOR_20260920.md),
and [adaptive-EMA review](../reviews/ADAPTIVE_EMA_REVIEW_20260920.md)
were accessible. The relevant pilot, cumulative-storage formulas and
SI S9/S10 were also consulted. No conclusion here depends on an assumed
remote copy of unpublished work.

For \(0<s\le w\), on either finite window \(\ell\le L\), use the
complete absorbed kernel
\[
 k_s(u)=H_s(u)-2s\int_0^u e^{(1/2-s)(u-v)}H_s(v)\,dv,
\quad
 H_s(u)=A_su^{s-1}
       \left(\frac{\sinh u}{u}\right)^{s-1}e^{-3u/2},
\quad A_s=\frac{(2\pi)^s}{\Gamma(s)}.
 \tag{2.1}
\]
Its factorization is inherited from SI S10. The beta substitution agrees
with [DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1). Both original signed
pole contributions remain present; Section 7 records them explicitly.

For fixed \(s>0\), (2.1) is in \(L^1(0,\ell)\). Approximation by
bounded kernels gives Hilbert--Schmidt operators on the finite square,
and Young's inequality gives operator-norm convergence. Hence \(V_s\)
is compact. On \(s\in[\epsilon,w]\), the coefficient \(A_s\) is
continuous and bounded; a constant multiple of \(u^{\epsilon-1}\)
dominates the first term for \(u<\ell<1\). The convolution correction
is dominated by a constant times \(u^\epsilon\). Dominated convergence
therefore gives continuity in kernel \(L^1\), hence in operator norm.

There is no uniform integrable kernel majorant down to \(s=0\), and none
is used. Instead the elementary gamma bounds from the scalar obstruction
give
\[
 \|V_{s,\ell}\|
 \le\frac{\ell^s}{(1-s)(1-2s)}
                   (1+2s\ell e^{\ell/2})<1.01.
 \tag{2.2}
\]
For example \(\ell^s\le1\), \(e^{\ell/2}\le4/3\), and \(s\le.001\)
give the last strict bound. Thus compactness needs no positivity assumption.
Using the internally certified anchor improves the uniform constant to 1.

Each finite \(T_{M,\ell}\) is bounded and self-adjoint: it is a finite
sum of bounded EMA terms, a fixed scalar, and the two pole rank-one forms.
Consequently
\[
 K_{M,\ell}=2\int_0^w V_{s,\ell}^*
                   (T_{M,\ell}-s^2I/8)V_{s,\ell}\,ds
 \tag{2.3}
\]
exists as an improper operator-norm integral. On \([\epsilon,w]\)
the integrand is norm-continuous and compact. The missing piece has norm
at most
\[
 2\epsilon C^2(\|T_{M,\ell}\|+w^2/8),
 \qquad C=\sup_{0<s\le w}\|V_{s,\ell}\|.
 \tag{2.4}
\]
Taking \(\epsilon\downarrow0\) proves compactness. Self-adjoint
compactness gives \(\langle e_j,K_Me_j\rangle\to0\) along every
orthonormal sequence, which rules out \(K_M\succeq cI\), \(c>0\).
There is no exchange of a fixed finite tower with the unbounded full tower.

The actual defects instead satisfy
\[
 E=I-X^*X,\quad F=I-ZZ^*,\quad \delta I\preceq E,F\preceq I,
 \tag{2.5}
\]
and have identity-minus-compact structure. Their quadratic forms tend to
1 along an orthonormal sequence. This distinction persists after removing
any finite-dimensional head.

## 3. Coercive lower metrics and explicit upper caps

The anchor proves \(T_{32,L}\succeq I/40\). Compression transfers the
same inequality to \(T_{32,h}\): the local coefficient and kernels
\(e^{-a|x-y|}\), \(2\cosh((x-y)/2)\) are translation invariant.
Together with the bounded shift perturbation, this gives
\[
 0\preceq K_{32,\ell}\preceq D_{w,\ell}.
 \tag{3.1}
\]
The integral is along the actual \(V_s\) throughout. Its extension from
the inherited form identity to all inputs uses the bounded right side and
density. No instantaneous lower operator is exponentiated.

Let \(J_hv(t)=v(h-t)\). Define, for strictly positive weights,
\[
 A=\theta_L\delta I+(1-\theta_L)K_{32,L},\qquad
 B=\theta_h\delta I+(1-\theta_h)J_hK_{32,h}J_h.
 \tag{3.2}
\]
Then
\[
 \theta_L\delta I\preceq A\preceq E,\qquad
 \theta_h\delta I\preceq B\preceq F.
 \tag{3.3}
\]
These are legitimate, boundedly invertible, all-input lower metrics. They
retain the actual finite-tower directional energy, with the stated convex
weight, and control every omitted input by a separately justified floor.
They are not the unjustified sum \(\delta I+K\).

Put \(c_M=w_0+\sum_{n=0}^{M-1}2/a_n\), \(a_n=2n+1/2\), with
the unchanged \(w_0=-\gamma-\pi/2-3\log2-\log\pi\). The symmetric
EMA kernels are positive: zero extension and the Fourier multiplier
\(a^2/(a^2+\xi^2)\) prove \(\Re S_{1/a}\succeq0\). Therefore
\[
 T_{32,\ell}\preceq c_{32}I+2|c_\ell\rangle\langle c_\ell|
 \preceq\tau_\ell I,\qquad
 c_\ell(x)=\cosh((x-\ell/2)/2),
\]
\[
 c_{32}<2.314,\qquad
 c_{32}+2\|c_\ell\|^2=c_{32}+\ell+2\sinh(\ell/2),
\quad \tau_L=\frac{83}{25},\quad \tau_h=\frac{483}{200}.
 \tag{3.4}
\]
The negative EMA and odd-pole forms were dropped only in this **upper**
estimate. Rational intervals check the displayed caps. With the anchor
\(\|V_s\|\le1\),
\[
 K_{32,L}\preceq b_LI,\quad K_{32,h}\preceq b_hI,
\quad b_L=\frac{83}{12500}=.00664,\quad
 b_h=\frac{483}{100000}=.00483.
 \tag{3.5}
\]
In particular \(A\preceq b_LI\), \(B\preceq b_hI\), uniformly
in both convex weights. Sharper caps are
\(b_{\ell,\theta}=\theta\delta+(1-\theta)b_\ell\).
Equation (2.4) now bounds the omitted shift segment, for example on the
old window, by \(6.64000025\epsilon\). Thus a future quadrature of these
metrics must account explicitly for that segment; this note uses their
exact integrals and incurs no quadrature error.

The normalized proxy and comparison are
\[
 \mathcal B=B^{-1/2}YA^{-1/2},\qquad
 \mathcal C=(F^{-1/2}B^{1/2})\mathcal B(A^{1/2}E^{-1/2}),
\quad \|\mathcal C\|\le\|\mathcal B\|.
 \tag{3.6}
\]
Both outside factors are contractions by (3.3). Every inverse is justified.

There is also an exact measure of the lost high-frequency energy. Along
any orthonormal sequence in the complement of a finite head,
\[
 \frac{\langle e_j,Ee_j\rangle}{\langle e_j,Ae_j\rangle}
 \longrightarrow\frac1{\theta_L\delta}.
 \tag{3.7}
\]
The output statement is identical. Thus a global comparison \(E\preceq cA\)
requires \(c\ge1/(\theta_L\delta)\), which exceeds 40001 at weight
one half. This alone does not obstruct coupling: \(Y\) is also compact.
The following calculation quantifies the failure of a particular way to
bound that compact mixed operator.

## 4. A join-adapted, exactly energy-orthogonal split

For \(j=0,\ldots,15\), set
\[
 v_j(r)=\frac{r^{-1/2}}2
 \mathbf1_{[he^{-4(j+1)},he^{-4j}]}(r).
 \tag{4.1}
\]
The vectors are orthonormal in ordinary \(L^2\). Use
\(f_j(y)=v_j(L-y)\) on the old input and \(v_j(t)\) on the new
output. They resolve equal logarithmic bands at the join, including the
scale of the earlier logarithmically spread witness. Their jumps pose no
domain problem: \(A,B,E,F\) are bounded forms on all \(L^2\).

In normalized coordinates let
\[
 P_{\rm old}=\operatorname{proj}\operatorname{span}\{A^{1/2}f_j\},
 \qquad
 P_{\rm new}=\operatorname{proj}\operatorname{span}\{B^{1/2}v_j\}.
 \tag{4.2}
\]
Each rank is 16. Pulling these projections back through the invertible
square roots makes the physical head and complement orthogonal in the
respective **energy** inner products. It does not silently discard
ordinary metric cross blocks. The argument below actually allows any
heads of these ranks, including numerically optimized ones.

To see the logarithmic geometry, transform the leading kernel
\(A_w(t+r)^{w-1}\) on the small square by \(r=he^{-x}\),
\(t=he^{-y}\), using the unitary Jacobian square roots. It becomes
\[
 A_wh^w e^{-w(x+y)/2}
           [2\cosh((x-y)/2)]^{w-1}.
 \tag{4.3}
\]
Its decay along \(x=y\) takes a logarithmic distance of order \(1/w=1000\).
The head in (4.1) extends through 64 logarithmic units. The obstruction
below integrates the entire remaining corner and is not a finite sampling
of it.

## 5. All four blocks, and the unavoidable HS loss

Let \(P^0=P\), \(P^1=I-P\), and
\(\mathcal B_{ij}=P_{\rm new}^i\mathcal B P_{\rm old}^j\).
The usual sufficient estimate is
\[
 \|\mathcal B\|\le
 \left\|\begin{pmatrix}
 \beta_{00}&\beta_{01}\\ \beta_{10}&\beta_{11}
 \end{pmatrix}\right\|_{\mathbb R^2\to\mathbb R^2},
 \qquad \beta_{ij}\ge\|\mathcal B_{ij}\|.
 \tag{5.1}
\]
The attempted complement choice is
\(\beta_{11}=\|\mathcal B_{11}\|_{\rm HS}\) or a certified upper
bound for that HS norm. The other three entries may use their exact
operator norms; giving them this advantage will not save (5.1).

Here are fully explicit bounds for all four blocks. Write
\[
 \bar A=\frac{w}{(1-w)(1-2w)},\qquad
 \bar y=\bar A\left(\frac{22}7+\frac{80}{29}\frac4{25}\right)
       =\frac{363800}{101195703}<.003596.
 \tag{5.2}
\]
The complete-kernel Carleman estimate in the scalar note gives
\(\|Y\|\le\bar y\). Consequently, **including both one-sided
complements**,
\[
 \|\mathcal B_{ij}\|\le
 \frac{\bar y}{\delta\sqrt{\theta_L\theta_h}},
 \qquad i,j\in\{0,1\}.
 \tag{5.3}
\]
For weights one half these are strictly below 144. They are intentionally
conservative upper estimates, not favorable numerical measurements. The
failure proof below holds even if the first three are replaced by exact
values, so tightening them first is unnecessary for this attempted method.

### 5.1 Rigorous HS mass in the full corner

For \(0<u\le\eta=10^{-4}\), the signed kernel satisfies
\[
 k_w(u)\ge w b_\eta u^{w-1}>0,\qquad
 b_\eta=1-\frac52\eta-\frac{2\eta}{1-\eta/2}.
 \tag{5.4}
\]
Indeed \(A_w\ge w\), \(\sinh(u)/u\le e^u\), and (2.1) give
\(k_w(u)\ge A_wu^{w-1}(e^{-5u/2}-2ue^{u/2})\).
Use \(e^{-5u/2}\ge1-5u/2\) and \(e^{u/2}\le(1-u/2)^{-1}\).
The triangular section \(t+r=u<\eta<h\) has length \(u\), so
\[
 \|Y\|_{\rm HS}^2\ge
 \int_0^\eta u k_w(u)^2\,du
 \ge\frac w2 b_\eta^2\eta^{2w}
 \ge H_0:=\frac w2b_\eta^2(1-20w).
 \tag{5.5}
\]
The last step uses \(\log10000<10\) and \(e^{-z}\ge1-z\).
This integral includes all arbitrarily small positive delays. Exactly,
\[
 H_0=\frac{6393601759920001}{13059918400000000000}
      =.000489559089428920\ldots.
 \tag{5.6}
\]
An upper estimate follows from
\(|k_w(u)|\le\bar A u^{w-1}(1+cu)\), \(c=80/29\), and the
rectangular section length at most \(u\). With \(R=11/20\),
\[
 \|Y\|_{\rm HS}^2\le H_1:=\bar A^2
 \left(\frac1{2w}+\frac{2cR}{1+2w}
                    +\frac{c^2R^2}{2+2w}\right)
 =.000507214988971033\ldots.
 \tag{5.7}
\]
These are rational bounds; the decimals only display their sizes.

### 5.2 Removing finite heads cannot remove enough HS mass

For any operator \(D\) of rank at most \(n\), let \(Q\) project onto
its range. Orthogonal decomposition of the output gives
\[
 \|Y-D\|_{\rm HS}^2\ge\|(I-Q)Y\|_{\rm HS}^2
 =\|Y\|_{\rm HS}^2-\|QY\|_{\rm HS}^2
 \ge H_0-n\bar y^2.
 \tag{5.8}
\]
This elementary argument is valid on the infinite input and output spaces;
no finite singular-value approximation is used.

Now \(\mathcal R=\mathcal B-\mathcal B_{11}
=P_{\rm new}\mathcal B+P_{\rm new}^\perp\mathcal B P_{\rm old}\)
has rank at most 32. Take \(D=B^{1/2}\mathcal R A^{1/2}\) in (5.8).
Then
\[
 Y-D=B^{1/2}\mathcal B_{11}A^{1/2},\qquad
 \|Y-D\|_{\rm HS}^2\le b_Lb_h\|\mathcal B_{11}\|_{\rm HS}^2.
\]
It follows, uniformly over both convex weights and both rank-16 heads,
\[
 \boxed{\quad
 \|\mathcal B_{11}\|_{\rm HS}^2\ge
 \frac{H_0-32\bar y^2}{b_Lb_h}
 =2.36932194232857\ldots>\frac94.
 \quad}
 \tag{5.9}
\]
The numerator is positive: it exceeds \(.00007598\).
Using the sharper caps \(b_{L,1/2}b_{h,1/2}\) gives
\[
 \|\mathcal B_{11}\|_{\rm HS}^2>9.31008499787307>9.
 \tag{5.10}
\]
For completeness (5.7) and the lower floors give
\(\|\mathcal B_{11}\|_{\rm HS}<903\) at those weights. Thus all
four operator blocks have valid explicit upper bounds, and the chosen HS
upper-estimation route for the fourth block has a rigorous lower barrier:

| Block at weights 1/2 | Rigorous operator-norm upper bound | Additional information |
|---|---:|---|
| head / head | <144 | May be replaced by an exact or tighter finite calculation |
| head / complement | <144 | Entire old complement included |
| complement / head | <144 | Entire new complement included |
| complement / complement | <144 | Its HS norm is strictly between 3 and 903 |

Any comparison matrix in (5.1) using an HS upper bound for its last entry
has norm greater than 3 at weights one half, and greater than 3/2 for
every admissible pair of weights. It cannot have norm below one even if
its other three entries were zero. This is the precise failed estimate.

The same rank argument works whenever the sum of head ranks is at most
35, because
\[
 \frac{H_0-b_Lb_h}{\bar y^2}=35.3979699326031\ldots.
 \tag{5.11}
\]
At total rank 36 the present lower bound becomes inconclusive; it does
not predict success. In particular this theorem makes no claim about the
64-dimensional total head of the earlier 32-per-side cosine diagnostic.
Nor does it give a basis-independent complexity bound for other methods.

## 6. The identity-minus-compact alternative and a quantified cutoff loss

Retaining the actual identity part avoids (3.7). For a norm approximation
\(W\) to \(V_{w,\ell}\) with \(\|V-W\|\le\varepsilon\), the
anchor \(\|V\|\le1\) gives
\[
 \|V^*V-W^*W\|\le d_\varepsilon:=2\varepsilon+\varepsilon^2,
 \qquad
 D_{w,\ell}\succeq I-W^*W-d_\varepsilon I.
 \tag{6.1}
\]
The lower operator on the right is itself at least
\((\delta-2d_\varepsilon)I\). At \(\varepsilon=\delta/10\),
this exceeds \(\delta I/2\). Reflection supplies the output metric.
Thus (6.1) is a usable alternative that preserves the near-identity energy
on every omitted direction. A finite-rank \(W\) retains its full metric
cross blocks, or they can be treated with the same energy-orthogonal split.
No such norm approximation is certified here.

One simple way to produce a smooth kernel approximation fails on a
quantified scale. Let \(V_\rho\) retain only delays \(u\ge\rho\).
Apply \(V-V_\rho\) to the constant unit vector on \((0,\ell)\).
For outputs \(x\in[\rho,\ell]\), its value is
\(\ell^{-1/2}\int_0^\rho k_w(u)du\). For \(\rho\le\eta\), (5.4)
therefore gives
\[
 \|V-V_\rho\|\ge\sqrt{1-\rho/\ell}\,b_\eta\rho^w
 \ge(1-\eta/h)b_\eta\rho^w>.99\rho^w.
 \tag{6.2}
\]
To get a discarded-kernel norm at most \(\delta/10\) by this procedure
requires
\[
 \rho<\left(\frac{\delta/10}{.99}\right)^{1000},\qquad
 p>\frac{1000\log(.99/(\delta/10))}{\log10}
   =5296.68256238825\ldots\quad(\rho=10^{-p}).
 \tag{6.3}
\]
An elementary rational comparison also proves the weaker threshold 5200:
\((5/3)^5>10\), hence \(10^{-5.2}>(3/5)10^{-5}\), and
\(.99(3/5)10^{-5}>\delta/10\). Finer ordinary meshes near the
diagonal do not make this a practical estimate. Analytically retaining
the fractional kernel, or using another operator representation, can
avoid this particular loss. This is not a prohibition on such methods.

## 7. Complete history, normalization, and what has not been substituted

In the original representation, with \(a=1/2-w\), \(b=1/2+w\),
\[
 q_w(u)=\frac{2\pi^w}{\Gamma(w)}e^{-au}(1-e^{-2u})^{w-1},
 \quad k_w=q_w-4wb(e^{-b\cdot}*q_w)-4wa(e^{a\cdot}*q_w).
 \tag{7.1}
\]
For the old input, extended by zero, put \(u=q_w*f\) and
\(p_\lambda(x)=\int_0^x e^{\lambda(x-y)}u(y)dy\). At the join,
\[
 u(L+t)=\int_0^Lq_w(L+t-y)f(y)dy,
\quad
 p_\lambda(L+t)=e^{\lambda t}p_\lambda(L)
             +\int_0^t e^{\lambda(t-v)}u(L+v)dv.
 \tag{7.2}
\]
Both \(\lambda=-b,a\) states and the complete beta history survive.
The mixed operator throughout this calculation is exactly
\[
 Yf(t)=\int_0^L k_w(t+r)f(L-r)dr.
 \tag{7.3}
\]
Absorption into (2.1) is the inherited algebraic cancellation, not a reset
of either signed state. On the output side
\(V_{w,h}^*=J_hV_{w,h}J_h\), hence
\(F=J_hD_{w,h}J_h\), exactly as used in (3.2).

The fixed \(w_0\), identity initial normalization, causal convention and
ordinary interval norms are unchanged. The finite tower is a lower form,
not a small absolute remainder for the central mixed operator. Positive
shift compactness has not been applied at zero shift. There is no operator
exponential of an instantaneous lower bound, auxiliary output-filter
storage, averaging variance, central certificate on \(L+h\), or crossing
of the first prime delay in this calculation.

## 8. Evidence, replay, preservation, and consequence

The [new checker](../numerics/certify_cumulative_energy_hs_obstruction.py)
uses the anchor's outward rational interval primitives for constants and
exact fractions for all comparisons. It certifies (3.4), (5.9)--(5.11),
the four-block upper constants, and (6.1)--(6.3). The proofs connecting
these scalar comparisons to the infinite-dimensional operators are given
above; executable arithmetic is not a substitute for their specialist
review. No floating eigensolver or finite coupling quotient enters a sign
decision. Decimal values in the record are explanatory displays only.

From the repository root:

```sh
python3 -B papers/susy-positivity/investigations/critical-path/numerics/certify_cumulative_energy_hs_obstruction.py --output /tmp/cumulative-energy-hs-replay.json
python3 -B papers/susy-positivity/investigations/critical-path/numerics/certify_cumulative_energy_hs_obstruction.py --digits 60 --output /tmp/cumulative-energy-hs-replay-60.json
```

Both precisions passed. The inherited anchor and scalar-obstruction
certificates were replayed successfully; the inherited complete-output
finite diagnostic was not rerun. Its approximately .802 value remains a
diagnostic lower quotient, not an all-input upper bound. The original EMA
anchor remains internally certified and awaits specialist review.

The new note, checker, small records and
[handoff](RESEARCH_CONTINUATION_AFTER_ENERGY_HS_OBSTRUCTION_20260920.md)
are separate additions. Existing uncommitted changes, historical notes,
the current version-0.5 manuscript pair and every snapshot were preserved.
File identities and replay comparisons are recorded in the new provenance
record; no large matrices or generated archives were created.

The arithmetic result eliminates a specific tempting certificate route:
retaining finite tower energy and a scalar floor does not make an HS
estimate of the omitted join coupling sufficiently sharp, even with an
energy-orthogonal split and exact treatment of all retained modes. The
unresolved quantity is the **operator norm of the normalized
complement/complement block**, together with useful bounds for the two
one-sided blocks if that obstacle is overcome. Logarithmic corner geometry
or the true identity part of the defect must be treated more sharply than
this HS/cutoff approach does. No new positivity horizon or all-depth
continuation has been proved.

The physical branch is unchanged: the specified nonlocal Gaussian mode
preparation has weights proportional to \((k+1)q^k\) and its nonzero
singular response has a double pole. That scoped exclusion is not a
universal localization obstruction. Further physical work still requires
a new independently specified action or observable.
