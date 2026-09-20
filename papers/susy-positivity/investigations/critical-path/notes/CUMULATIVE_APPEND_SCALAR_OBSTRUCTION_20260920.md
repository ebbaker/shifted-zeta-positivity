# Cumulative append coupling: a scalar obstruction and complete-output diagnostics

20 September 2026. Prepared for Edward Baker.

**Model:** OpenAI GPT-6 (Codex; developer-provided identity).
**Reasoning effort:** not exposed in this session; no setting is inferred.
**Status:** analytic bounds with exact rational checks, plus separately labelled
floating diagnostics. Specialist mathematical review remains outstanding.

## 1. Result and scope

For the prescribed test
\[
L=\tfrac12,\qquad h=\tfrac1{20},\qquad R=L+h=\tfrac{11}{20}<\log2,
\qquad w=\tfrac1{1000},
\]
write the original arithmetic transfer as
\[
V_{w,R}=\begin{pmatrix}X&0\\Y&Z\end{pmatrix},\quad
E=I-X^*X,\quad F=I-ZZ^*,\quad \mathcal C=F^{-1/2}YE^{-1/2}.
\]
The [anchor](EMA_TOWER_ORIGINAL_TRANSFER_ANCHOR_20260920.md) supplies
\(E,F\succeq\delta I\), where
\(\delta=24999/500000000=0.000049998\).
The elementary sufficient estimate
\[
\|\mathcal C\|\le \|Y\|/\delta
\tag{1.1}
\]
cannot certify this append, even if its numerator is evaluated exactly:
\[
\boxed{55<\|Y\|/\delta<72.}
\tag{1.2}
\]
The exact bounds used have decimal displays 55.9758151914 and
71.9031622484. They enclose the **best upper bound available from (1.1)**,
not the actual normalized coupling. In particular, (1.2) does not imply
\(\|\mathcal C\|>1\).

There is also a quantitative obstruction involving both omitted spaces.
Let \(P_L,P_h\) select cosine modes 0 through 31 on their respective
intervals, and let \(P_\ell^\perp=I-P_\ell\). Then
\[
\boxed{\|P_h^\perp YP_L^\perp\|/\delta>46.}
\tag{1.3}
\]
The computed exact lower bound has display 46.4126946124. Thus a small
finite mixed matrix followed by scalar-anchor control of everything
omitted cannot close the estimate at this resolution.

In contrast, complete-output calculations in the actual restricted
defect metrics give a coupling quotient approximately **0.801830639**
with 32 modes per window. Its instantaneous central counterpart is
approximately **0.801829271**. These are finite-input diagnostics;
neither bounds the all-input coupling from above. The new result is a
scoped obstruction to absolute mixed-block estimates with scalar defect
normalization, together with evidence that directional storage is the
quantity worth retaining. No all-input append certificate is claimed.

## 2. Anchor hypotheses, shorter windows, and orientation

The three requested starting files were available and read first:
the [handoff](RESEARCH_CONTINUATION_AFTER_EMA_ANCHOR_20260920.md),
the [anchor](EMA_TOWER_ORIGINAL_TRANSFER_ANCHOR_20260920.md), and
the [review](../reviews/ADAPTIVE_EMA_REVIEW_20260920.md).
The preceding [audit](ADAPTIVE_EMA_AUDIT_AND_PILOT_20260920.md) and
[cumulative-storage note](../../wilson-loewner/notes/SHIFT_FLOW_CUMULATIVE_STORAGE_AND_CRITICAL_PATH_20260919.md)
supply the kernel and gluing conventions.

The anchor uses the complete prime-free arithmetic kernel, ordinary
unweighted interval norms, identity initial normalization, and zero
history at the left endpoint. Its finite gamma tower is a lower bound
in positive-form order; it is not a norm approximation to the generator.
The bounded shift perturbation is integrated along the actual evolution
\(\partial_s V_s=-G_sV_s\), using a scalar Gronwall inequality.
Its rational certificate was replayed successfully at 40 and 60 digits
in this session; both replay payloads match their historical records.
That checks the implementation and arithmetic, not independent specialist
validation of the analytic reduction.

For \(0<\ell\le L\), let \(J_\ell\) be zero extension into \((0,L)\)
and \(R_\ell\) restriction of the output. Causality and translation
invariance give
\[
V_{s,\ell}=R_\ell V_{s,L}J_\ell,\qquad
\|V_{s,\ell}\|\le\|V_{s,L}\|.
\]
Consequently the same scalar defect floor applies at \(h\), without
recalibrating any local coefficient. If \(\mathscr J_\ell f(x)=f(\ell-x)\),
the real causal kernel obeys
\[
V_{w,\ell}^*=\mathscr J_\ell V_{w,\ell}\mathscr J_\ell,\quad
F=\mathscr J_h(I-Z^*Z)\mathscr J_h\succeq\delta I.
\tag{2.1}
\]
The required output defect is therefore coercive. Its replacement by
the input defect in an unreflected mixed expression would be incorrect.

The exact inherited Schur criterion remains
\[
\|V_{w,R}\|<1\quad\Longleftrightarrow\quad\|\mathcal C\|<1.
\tag{2.2}
\]
Nothing below establishes its right side on the full spaces. In
particular, this work does not substitute a separate central-form
certificate at \(R\) for the requested cumulative estimate.

## 3. Complete append response and endpoint memory

For \(a=1/2-w\), \(b=1/2+w\), set
\[
q_w(u)=\frac{2\pi^w}{\Gamma(w)}e^{-au}(1-e^{-2u})^{w-1},\qquad
k_w=q_w-4wb(e^{-b\cdot}*q_w)-4wa(e^{a\cdot}*q_w).
\tag{3.1}
\]
These are the inherited original beta kernel and **both** signed rational
pole contributions. Since \(R<\log2\), every nontrivial integer delay
lies outside the window. Equation (3.1) is the complete arithmetic
kernel on this window, not the gamma-only transfer.

For an old input \(f\), define \(u=q_w*f\), with \(f\) extended by zero
after \(L\), and
\[
p_\lambda(x)=\int_0^x e^{\lambda(x-y)}u(y)\,dy.
\]
On the added interval,
\[
u(L+t)=\int_0^Lq_w(L+t-y)f(y)\,dy,
\quad
p_\lambda(L+t)=e^{\lambda t}p_\lambda(L)
 +\int_0^t e^{\lambda(t-s)}u(L+s)\,ds.
\tag{3.2}
\]
Thus \(Yf(t)=u(L+t)-4wbp_{-b}(L+t)-4wap_a(L+t)\).
Resetting either pole state, or resetting the beta history, changes \(Y\).
Equivalently, with \(r=L-y\),
\[
Yf(t)=\int_0^L k_w(t+r)f(L-r)\,dr,\qquad 0<t<h.
\tag{3.3}
\]
This reflected old-input coordinate turns the join into a corner Hankel
kernel. The output coordinate \(t\) in (3.3) is not reflected.

The exact absorbed expression is particularly convenient for estimates:
\[
k_w(u)=H_w(u)-2w\int_0^u e^{a(u-v)}H_w(v)\,dv,
\quad H_w(u)=A_wu^{w-1}F_w(u),
\tag{3.4}
\]
\[
A_w=\frac{(2\pi)^w}{\Gamma(w)},\qquad
F_w(u)=\left(\frac{\sinh u}{u}\right)^{w-1}e^{-3u/2}.
\]
Absorption is an algebraic cancellation of the lowest gamma mode and one
pole factor. The code checks (3.1) and (3.4) independently at six delays;
their smooth kernel factors agree to about \(1.1\,10^{-18}\) in the
reported run. The beta identity underlying the factorization is
[DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1).

At zero shift the fixed generator normalization is still
\[
G_0=(w_0+4)I+\sum_{n=1}^\infty\frac2{a_n}(I-S_{1/a_n})+2R_{-1/2},
\quad a_n=2n+\tfrac12,
\]
\[
w_0=-\gamma-\pi/2-3\log2-\log\pi.
\tag{3.5}
\]
No local subtraction has been changed. Its mixed kernel is
\[
g(u)=-\frac{2e^{-5u/2}}{1-e^{-2u}}+2e^{u/2}.
\tag{3.6}
\]
For each generator EMA, the incoming resolvent state
\(z_n=\int_0^L e^{-a_n(L-y)}f(y)\,dy\) contributes
\(-2e^{-a_nt}z_n\) on the added interval. The growing pole contributes
\(2e^{t/2}\int_0^L e^{(L-y)/2}f(y)\,dy\).
Before cancellation there is also the decaying pole, which cancels the
\(n=0\) nonlocal gamma term exactly. Along the shift flow these states
must be evaluated on the evolving input. They are not zero at the join.

## 4. A rigorous two-sided enclosure of the scalar-route loss

All estimates in this section apply to arbitrary inputs; the lower
bound uses a particular explicit input/output pair.
For \(0<w<1\),
\[
1-w\le\Gamma(1+w)\le1.
\tag{4.1}
\]
For the upper inequality use concavity of \(t^w\) under the probability
measure \(e^{-t}dt\), whose mean is one. For the lower inequality use
\(t^w\ge1+w\log t\); the negative part of
\(\int e^{-t}\log t\,dt\) has absolute value at most
\(\int_0^1-\log t\,dt=1\). This proof needs no rounded gamma value.
Because \(2\pi<7<e^2\),
\[
w\le A_w\le\frac{w}{(1-w)(1-2w)}=:\overline A.
\tag{4.2}
\]

The elementary inequalities \(1\le\sinh u/u\le e^u\) yield
\(e^{-5u/2}\le F_w(u)\le1\). Keeping the negative term in (3.4),
\[
k_w(u)\ge A_wu^{w-1}\big(e^{-5u/2}-2u e^{u/2}\big),
\quad
|k_w(u)|\le A_wu^{w-1}(1+2u e^{R/2}).
\tag{4.3}
\]
For the lower estimate we will use only the region where the bracket is
positive; no positivity of the kernel on the whole window is asserted.

### 4.1 Lower bound by a logarithmically spread corner test

Put \(\varepsilon=10^{-4}\), \(T=50\). On both reflected old input and
new output use the unit function
\[
v(r)=\frac{r^{-1/2}}{\sqrt T}
\mathbf1_{[\varepsilon e^{-T},\varepsilon]}(r).
\tag{4.4}
\]
The old input is \(f(y)=v(L-y)\). This is an ordinary \(L^2\) test;
no smoothness or flow derivative is needed. Its support fits both windows.
On the support of the mixed integral,
\[
u=t+r\le2\varepsilon,\qquad
u^w\ge1-w(T+10)=\frac{94}{100},
\]
using \(\log(1/\varepsilon)<10\). Moreover
\[
e^{-5u/2}-2u e^{u/2}
\ge 1-5\varepsilon-\frac{4\varepsilon}{1-\varepsilon}=:b_* >0.
\tag{4.5}
\]
Under logarithmic coordinates, the Carleman pairing becomes
\[
\iint\frac{v(t)v(r)}{t+r}\,dr\,dt
=\frac1T\int_{-T}^T\frac{T-|s|}{2\cosh(s/2)}\,ds
\ge\pi-\frac8T.
\tag{4.6}
\]
Indeed the whole-line integral of \(1/(2\cosh(s/2))\) is \(\pi\),
and its first absolute moment is at most
\(2\int_0^\infty se^{-s/2}ds=8\). Extending
\(1-|s|/T\) outside \([-T,T]\) only decreases the integral.
Combining (4.2)--(4.6) gives
\[
\|Y\|\ge\langle v,Yf\rangle
>\frac1{1000}\frac{94}{100}b_*
 \left(\frac{157}{50}-\frac8{50}\right)=:\underline y.
\tag{4.7}
\]
The exact rational comparison is \(\underline y/\delta>55\).

### 4.2 Upper bound on every input

Since \(0<u<R<1\), (4.3) implies
\[
|k_w(t+r)|\le\overline A\left(\frac1{t+r}+2e^{R/2}\right).
\]
The rectangular Carleman kernel has norm at most \(\pi\): weighted
Schur with weight \(r^{-1/2}\) follows from
\(\int_0^\infty r^{-1/2}/(t+r)\,dr=\pi t^{-1/2}\).
The constant kernel has norm \(\sqrt{Lh}\). Hence
\[
\|Y\|\le\overline A\big(\pi+2e^{R/2}\sqrt{Lh}\big)
<\overline A\left(\frac{22}7+\frac{80}{29}\frac4{25}\right)=:\overline y.
\tag{4.8}
\]
Here \(e^{11/40}\le40/29\) and \(\sqrt{1/40}<4/25\).
The exact comparison is \(\overline y/\delta<72\).

The standard-library
[rational checker](../numerics/certify_cumulative_scalar_obstruction.py)
verifies these rational comparisons, the elementary exponential
inequalities used for the logarithms, and the stated pi bounds using
Machin's identity and alternating rational series. Its
[small record](../numerics/records/cumulative-scalar-obstruction-20260920.json)
contains exact fractions. As with the anchor, the analytic reduction
must also be reviewed; passing arithmetic alone is not that review.

### 4.3 Both omitted cosine spaces remain substantial

For an orthogonal cosine projection through mode \(N-1\) on length
\(\ell\), the test (4.4) satisfies
\[
\|P_\ell v\|^2\le\frac{2N-1}{\ell}\|v\|_1^2
\le\frac{2N-1}{\ell}\frac{4\varepsilon}{T}.
\tag{4.9}
\]
Reflection only changes cosine signs. At \(N=32\), (4.9) gives
\(\|P_Lf\|<0.032\), \(\|P_hv\|<0.101\).
Using orthogonal projections and (4.8),
\[
|\langle v,Yf\rangle-
\langle P_h^\perp v,Y P_L^\perp f\rangle|
\le\overline y(0.032+0.101).
\]
The remaining vectors have norm at most one, so
\[
\|P_h^\perp YP_L^\perp\|
\ge\underline y-0.133\overline y>46\delta.
\tag{4.10}
\]
This proves (1.3). These are raw cosine complements, not the images of
those complements under the defect square roots. Equation (4.10)
therefore obstructs the scalar-normalized tail estimate, not the true
defect-normalized one.

## 5. What the finite arithmetic EMA tower does and does not control

The finite tower retains the endpoint state of every included mode.
It supplies legitimate all-input diagonal form bounds by the anchor's
Robin-to-Neumann decomposition. However, positive order of an omitted
global gamma form does not make its spatial mixed block small.

After keeping modes \(0,\ldots,M-1\), its omitted generator mixed
kernel, in the reflected coordinates, is minus
\[
r_M(t+r)=\frac{2e^{-(2M+1/2)(t+r)}}{1-e^{-2(t+r)}}.
\tag{5.1}
\]
For every finite \(M\ge1\),
\[
0<r_M(u)\le1/u,\quad ur_M(u)\longrightarrow1\ (u\downarrow0),
\quad \|r_M(t+r)\|_{L^2(0,L)\to L^2(0,h)}=\pi.
\tag{5.2}
\]
The upper bound follows from \(1-e^{-2u}\ge2ue^{-2u}\) and the
Carleman Schur estimate. For the lower bound use (4.4), first shrink
\(\varepsilon\) at fixed \(T\), then let \(T\to\infty\).
On each finite logarithmic support the pairing tends to the Carleman
pairing. These unit tests concentrate at the join and converge weakly
to zero as \(\varepsilon\to0\). Any fixed finite-rank input and output
projections consequently remove a norm tending to zero. In fact
\[
\|(I-P_h)r_M(t+r)(I-P_L)\|=\pi
\tag{5.3}
\]
for **any** fixed finite-rank orthogonal projections. The corresponding
off-diagonal block of \(Q_0=\Re G_0\) has the factor \(1/2\), so its
omitted mixed-block norm is \(\pi/2\). Finite pole terms do not remove
this corner singularity. This is a specific failure of unweighted
operator-norm truncation, not a failure of the positive-form lower
operator used in the anchor.

For fixed positive \(w\), the cumulative mixed kernel instead behaves
as \(A_w u^{w-1}\). It is Hilbert--Schmidt on the rectangle because
its near-corner squared integral is proportional to
\(\int_0^h u^{2w-1}du<\infty\). Thus the noncompact assertion (5.2)
must not be transferred to \(Y\) at positive shift. The independent
finite-shift witness (4.10) is what supplies the numerical obstruction
at the requested \(w\). The central mixed operator is not even a
Hilbert--Schmidt kernel; its noncompact limit explains why small-shift
and finite-resolution limits require care.

A useful legitimate way to retain the finite tower in cumulative
metrics is to integrate its lower form **along the actual flow**.
For \(\ell=L\) or \(h\), write \(T_{M,\ell}\) for the finite tower
on that window. The anchor's perturbation estimate gives
\[
I-V_{w,\ell}^*V_{w,\ell}
\succeq 2\int_0^w
 V_{s,\ell}^*(T_{M,\ell}-s^2I/8)V_{s,\ell}\,ds.
\tag{5.4}
\]
For the output metric, reflect this inequality using (2.1).
This leaves complete outputs and the nonnormal flow inside the
integral; an operator exponential of \(T_M\) is not justified.
At high frequencies a bounded finite tower need not give a sharp
metric after integration, so (5.4) is a possible component of a
future estimate rather than a ready complement certificate.

## 6. Complete-output finite-input diagnostics

Use orthonormal cosines \(\phi_j^\ell(x)=\rho_j\cos(j\pi x/\ell)\),
including the constant mode. Let \(U\) and \(W\) be the isometries
from the finite coefficient spaces into old input and new output.
The diagnostic matrices are
\[
E_N=I-(XU)^*(XU),\qquad F_N=I-(Z^*W)^*(Z^*W),\qquad Y_N=W^*YU.
\tag{6.1}
\]
The complete response functions are integrated before forming either
Gram matrix. Reflection supplies \(F_N=J_ND_{h,N}J_N\), with
\(J_N=\operatorname{diag}((-1)^j)\). There is no premature finite
output projection. In exact arithmetic,
\[
c_N=\|F_N^{-1/2}Y_NE_N^{-1/2}\|
=\sup_{f\in\operatorname{ran}U,\,v\in\operatorname{ran}W}
\frac{|\langle v,Yf\rangle|}{\sqrt{\langle f,Ef\rangle\langle v,Fv\rangle}}
\le\|\mathcal C\|.
\tag{6.2}
\]
This direction is crucial: even an interval-certified \(c_N<1\)
would still be insufficient to prove the all-input result.

The central comparison uses the complete \(Q_{0,L}\), \(Q_{0,h}\)
and the mixed kernel \(g(t+r)/2\). The code evaluates central
translation correlations directly, including the gamma integral beyond
the interval and both signed pole rank-one terms. It does not truncate
the arithmetic EMA tower for this diagnostic.

| Modes per window | Output/delay order | Cumulative quotient | Central quotient |
|---:|---:|---:|---:|
| 8 | 96 | 0.79841991494 | 0.79840725185 |
| 16 | 144 | 0.80127600385 | 0.80127215472 |
| 16 | 208 | 0.80127600385 | 0.80127215472 |
| 32 | 240 | 0.80183063889 | 0.80182927067 |
| 32 | 320 | 0.80183063889 | 0.80182927067 |

The 32-mode cumulative quadrature refinement changes the quotient by
about \(1.9\,10^{-12}\). This is a convergence check, not an interval
error enclosure. The finite mixed norm is approximately 0.00194261745,
giving scalar normalization 38.8539031; the rigorous all-input lower
bound (4.7) is larger, illustrating the unseen corner directions.

At the refined 32-mode point, the smallest restricted defect eigenvalues
divided by \(2w\) are approximately 0.0335098614 and 1.5893079664.
The unit old/new pair maximizing the finite quotient has
\[
\langle f,Ef\rangle\approx0.0001276692,\quad
\langle v,Fv\rangle\approx0.0034944355,\quad
|\langle v,Yf\rangle|\approx0.0005355675.
\]
Its coefficients are saved in the small record. The new-output metric
is much larger in these directions than the transferred scalar anchor.
This explains part of the scalar loss without replacing a finite
observation by an all-input lower bound.

Projecting the output first would discard positive Gram contributions
with norms about \(2.11\,10^{-6}\) and \(2.14\,10^{-6}\), thereby
artificially increasing the diagonal defects. Those losses are recorded
as controls and are not counted as arithmetic storage. No auxiliary
smoother or shift averaging is used anywhere in this calculation.

## 7. The remaining proof obligation and the program

The concrete unresolved inequality is
\[
|\langle v,Yf\rangle|^2\le c^2\langle f,Ef\rangle\langle v,Fv\rangle
\quad\text{for every }f,v,\qquad c<1.
\tag{7.1}
\]
The missing estimate must preserve directional storage in both spaces,
including their near-join high-frequency directions and their mixed
terms with the finite heads. An unweighted mixed-block remainder,
divided by the scalar \(\delta\), cannot serve that purpose at the
tested resolution. The rigorous witness quantifies this failure before
any large numerical expansion is attempted.

One precise next route is to use the actual \(E\)- and \(F\)-orthogonal
decompositions into a finite head and its energy-orthogonal complement.
Then the coupling has four blocks in genuine Hilbert metrics. Bounds
\(c_{ij}\) on all four block norms imply
\(\|\mathcal C\|\le\|[c_{ij}]_{i,j=0,1}\|\).
The present calculation diagnoses only the head/head quotient; it
supplies no certificate for the other three normalized blocks.
Constructing computable coercive lower metrics, potentially using
(5.4) and endpoint-adapted estimates, is a concrete intermediate task.
Replacing ordinary cosine complements by energy-orthogonal ones requires
an explicit calculation; it cannot be assumed for free.

An alternative implementation may use the inherited Cayley congruence,
which preserves the full normalized coupling. It changes coordinates,
not the proof obligation. Any comparison with the central form must
retain its domain and finite-test scope. No operator lower bound is
exponentiated through a nonnormal evolution in this note.

The overall target remains the cumulative defect. Instantaneous
positivity is useful where it is proved but need not persist along a
successful continuation. The result here provides no new positivity
horizon, prime-threshold append, all-depth path, arithmetic Loewner
driver, physical Wilson realization, or localization theorem.
Localization remains a separate possible explanation of the prescribed
spectrum and cancellations.

## 8. Reproduction and preservation

From the repository root, with Python and NumPy available:

```bash
python3 papers/susy-positivity/investigations/critical-path/numerics/certify_cumulative_scalar_obstruction.py \
  --output /tmp/cumulative-scalar-obstruction-replay.json
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 \
  papers/susy-positivity/investigations/critical-path/numerics/diagnose_cumulative_append.py \
  --output /tmp/cumulative-append-diagnostics-replay.json
```

The first command uses only the standard library. The second reuses
the existing pilot's quadrature and complete arithmetic kernel. It
records its dependencies' hashes, Python and NumPy versions, parameters,
and the finite weak pair. It requires no matrix archive. Numerical
last bits can vary with library/platform; all floating numbers remain
diagnostic.

The new [provenance record](../numerics/records/cumulative-append-provenance-20260920.json)
identifies the read inputs, new outputs and replay comparisons.
The [next-session handoff](RESEARCH_CONTINUATION_AFTER_CUMULATIVE_APPEND_20260920.md)
states the next bounded task. Historical notes, dirty pre-existing
index edits, manuscript sources and snapshots are preserved. All new
files are small source or record files under the repository's normal
notes/numerics placement; no large derived data are stored.
