# Depth extension with an adaptive shift

Research note, 10 September 2026. Working conventions: *Finite-horizon Weil coercivity and shifted-zeta contraction*, v0.3, repository commit `a566944dc1be2899e37fce3d0e857516ced33d8f`.

This note develops consequences of that manuscript's normalization while the author verifies it separately. It makes no claim of a completed all-depth proof or of literature novelty. The analytic deductions below have been checked within this investigation, not independently reviewed by a specialist. The numerical sign result is isolated in Section 8; the other numerical quantities are diagnostics. No synced project source or repository manuscript was changed.

## 1. What the path should measure

Write

\[
D_{\omega,L}=I-V_{\omega,L}^*V_{\omega,L}.
\]

At zero shift, \(V_{0,L}=I\) for every horizon, including a horizon at which the central Weil form might be negative. Consequently the entire zero-shift axis has zero *unscaled* defect and cannot by itself distinguish a successful critical path.

The meaningful infinitesimal quantity is

\[
\lim_{\omega\downarrow0}\frac{\langle f,D_{\omega,L}f\rangle}{2\omega}
=Q_{0,L}[f]
\]

for fixed smooth compactly supported tests. This is a fixed-test limit, not convergence in bounded-operator norm. In particular, a bounded defect at positive shift cannot dominate a fixed positive multiple of the unbounded form \(Q_{0,L}\) on its entire domain.

The diagonal proposition in the manuscript still gives the ultimate target: contractions at \(L_j\to\infty\), \(\omega_j\downarrow0\). Choosing a path does not remove the need for positivity at every fixed compact support eventually encountered by that path.

A useful intermediate variable emerges below:

\[
\boxed{\quad\omega\kappa_L,\qquad
\kappa_L=\sup_{f\ne0}\left(\frac{Q_{0,L}[X_Lf]}{Q_{0,L}[f]}\right)^{1/2},
\quad X_Lf(x)=(x-L/2)f(x).\quad}
\]

This is defined when the central form is strictly positive. It measures how coordinate multiplication transfers a weak vector into more energetic directions. It contains information beyond the smallest eigenvalue.

## 2. An exact hyperbolic identity

Let \(Q=Q_{0,L}\), \(X=X_L\), \(C_\omega=\cosh(\omega X)\), and \(S_\omega=\sinh(\omega X)\). Then

\[
\boxed{Q_{\omega,L}[f]=Q[C_\omega f]-Q[S_\omega f].}\tag{2.1}
\]

This includes both reflection sectors and complex-valued tests.

**Derivation.** Off the diagonal, the central gamma kernel is

\[
r(t)=e^{t/2}-\frac{e^{-5t/2}}{1-e^{-2t}},\qquad t>0.
\]

The bounded gamma shift difference in Lemma 3.2 of the manuscript multiplies this kernel by \(\cosh(\omega(x-y))-1\). Each prime-power kernel is multiplied by \(\cosh(\omega\log n)\). The same rule therefore applies to the complete central kernel. Now use

\[
\cosh(\omega(x-y))=
\cosh(\omega(x-L/2))\cosh(\omega(y-L/2))
-\sinh(\omega(x-L/2))\sinh(\omega(y-L/2)).
\]

The multiplier equals one on the diagonal, so the local distribution term is unchanged. Its difference from one vanishes quadratically there, making the product with the logarithmic singularity an ordinary integrable kernel. Thus the identity first holds on a smooth core and extends to the common logarithmic form domain. Smooth bounded multipliers, extended smoothly outside the finite interval, act continuously on that domain.

An equivalent form is

\[
Q_{\omega,L}=C_\omega\bigl(Q-T_\omega Q T_\omega\bigr)C_\omega,
\qquad T_\omega=\tanh(\omega X),\tag{2.2}
\]

understood as a congruence of forms.

If \(Q\succeq mI\), \(m>0\), the form domain is a Hilbert space with norm \(\|f\|_Q=Q[f]^{1/2}\). Coordinate multiplication is bounded on it: the logarithmic form norm and \(\|\cdot\|_Q\) are equivalent, and smooth multipliers preserve the former. Equation (2.2) gives the exact criterion

\[
Q_{\omega,L}\succeq0
\quad\Longleftrightarrow\quad
\|T_\omega\|_{Q\to Q}\le1.\tag{2.3}
\]

Since \(T_\omega\) is odd, it exchanges the two reflection sectors. Equivalently, both energy transfers from even to odd and from odd to even must have norm at most one. Their weights are the actual sector forms, not their separate least eigenvalues.

No monotonicity of \(\|T_\omega\|_{Q\to Q}\) in \(\omega\), uniqueness of a first crossing, or existence of an all-depth critical curve is asserted.

## 3. A relative inequality and a sufficient path

**Proposition.** Suppose \(Q\succeq mI\), and let \(\kappa=\|X\|_{Q\to Q}\). For \(0\le\omega\kappa\le\pi/4\),

\[
\boxed{Q_{\omega,L}\succeq\cos(2\omega\kappa)Q_{0,L}.}\tag{3.1}
\]

For \(0<\omega\le\min(1/2,\pi/(4\kappa))\), the manuscript's energy argument consequently gives

\[
\boxed{\|V_{\omega,L}\|\le
\exp\!\left[-\frac{m}{2\kappa}\sin(2\kappa\omega)\right]<1.}\tag{3.2}
\]

**Proof.** Put \(t=\omega\kappa\). The Taylor coefficients of \(\tanh z\), in absolute value, are the coefficients of \(\tan z\). The analogous majorant for \(\operatorname{sech}z\) is \(\sec z\). For \(t<\pi/2\), norm-convergent functional calculus on the energy Hilbert space gives

\[
\|T_\omega\|_Q\le\tan t,
\qquad \|C_\omega^{-1}\|_Q\le\sec t.
\]

For \(t\le\pi/4\), the first coefficient below is nonnegative, and

\[
Q_{\omega,L}[f]
\ge(1-\tan^2t)\|C_\omega f\|_Q^2
\ge(1-\tan^2t)\cos^2t\,Q[f]
=\cos(2t)Q[f].
\]

Use (3.1) in \(d\|V_{s,L}f\|^2/ds=-2Q_{s,L}[V_{s,L}f]\), integrate, and pass to the strong zero-shift limit exactly as in Proposition 3.4 of v0.3. This proves (3.2). No bounded inverse of \(V\) is used.

Thus \(\omega\bar\kappa_L\le\theta<\pi/4\), for a proved upper bound \(\bar\kappa_L\), is a sufficient interior path condition. For example \(\theta=1/2\) is a convenient fixed choice. A recursive sequence can use

\[
\omega_j=\min\{\omega_{j-1},1/(j+1),\theta/\bar\kappa_{L_j},1/2\}.
\]

This produces shifts tending to zero *if the depth recursion reaches unbounded horizons*. The factor \(1/(j+1)\) is optional when divergence of \(\kappa_{L_j}\) is established.

The coordinate midpoint is a natural optimal choice for this sufficient bound. The norm of \(X-aI\) on the energy space is convex in real \(a\), and reflection makes it even in \(a\). Hence its minimum occurs at the midpoint \(a=0\).

These are sufficient generator-based conditions. Cumulative contraction can survive after (2.3) fails.

## 4. What a depth update must carry

Append an interval of length \(h<\log2\) to \((0,L)\). In the spatial decomposition into old and new intervals, the central form has blocks

\[
Q_{0,L+h}=\begin{pmatrix}A&B^*\\ B&F\end{pmatrix},
\qquad A=Q_{0,L},\quad F=Q^\gamma_{0,h}.
\]

The cross block \(B\) is bounded on the ordinary \(L^2\) spaces; Section 5 proves an explicit estimate. The form domain decomposes as the direct sum of the two logarithmic domains. One way to justify this is to use smooth functions avoiding the split as a common core: removing a shrinking neighborhood of one interior point converges in \(H^s\), \(0<s<1/2\), for smooth inputs, hence in the logarithmic norm. Equality of the closed forms then follows from their equality on this core and boundedness of \(B\).

Assume \(A\succeq m_LI>0\), \(F\succeq m_hI>0\), and define

\[
c=\|F^{-1/2}BA^{-1/2}\|.
\]

If \(c<1\), then

\[
(1-c)(A\oplus F)\preceq Q_{0,L+h}\preceq(1+c)(A\oplus F),\tag{4.1}
\]

and in particular

\[
m_{L+h}\ge(1-c)\min(m_L,m_h).\tag{4.2}
\]

The proof is the Cauchy inequality for the normalized cross form: \(2|\langle Bf,g\rangle|\le c(A[f]+F[g])\).

More importantly for a path, the same update preserves a bound on the energy multiplication norm:

\[
\boxed{\kappa_{L+h}\le
\sqrt{\frac{1+c}{1-c}}
\max\{\kappa_L+h/2,\ \kappa_h+L/2\}.}\tag{4.3}
\]

Indeed, global centered coordinate multiplication restricts to \(X_L-h/2\) on the old interval and \(X_h+L/2\) on the new one. Its norm in the direct-sum energy is at most the displayed maximum. Comparing that energy with the new one by (4.1) proves (4.3).

This gives a concrete recursive state: central positivity, the complete normalized cross coupling, and a coordinate-energy norm bound. Equations (4.1)–(4.3), followed by (3.2), are inequalities that survive a successful depth extension. They do not yet establish a uniform arithmetic bound on \(c\) or prevent the allowed extension lengths from accumulating at a finite depth.

## 5. An explicit local extension lemma

There is an elementary sufficient bound on \(c\). It is useful for exposing the remaining problem, though extremely conservative.

Use the manuscript's

\[
G_0(t)=e^{t/2}t/\sinh t-4t\cosh(t/2),\quad
w(t)=(G_0(t)-1)/t.
\]

Then \(r(t)=-1/(2t)-w(t)/2\). Fix a finite ceiling \(R>L\) and any valid

\[
W_R\ge\sup_{0\le t\le R}|w(t)|.
\]

For \(R<3\), the profile-variation bound \(K_R\) from v0.3 is one such computable choice. For an append with \(L+h\le R\), the gamma cross block is the sum of half a Carleman operator and a smooth kernel. The former has norm at most \(\pi/2\): Schur's test with weight \(t^{-1/2}\) uses

\[
\int_0^\infty\frac{u^{-1/2}}{u+v}\,du=\pi v^{-1/2}.
\]

The smooth part has norm at most \(W_R\sqrt{Lh}/2\). Each arithmetic cross delay has norm at most one. Consequently

\[
\|B\|\le b(L,h):=\frac\pi2+\frac{W_R\sqrt{Lh}}2
+\sum_{\log n<R}\frac{\Lambda(n)}{\sqrt n}
\le b_R:=\frac\pi2+\frac{W_RR}2
+\sum_{\log n<R}\frac{\Lambda(n)}{\sqrt n}.\tag{5.1}
\]

For \(h<\log2\), the new diagonal is prime-free and obeys

\[
F\succeq g(h)I,\qquad g(h)=-\gamma-\log(\pi h)-W_Rh.\tag{5.2}
\]

To see (5.2), extend the Jacobi fractional estimate used in Lemma 4.1 of v0.3 to the full polynomial space, starting at degree zero. For \(0<\nu<1\),

\[
\|I_\nu\|\le(h/2)^\nu
\sqrt{\Gamma(1-\nu)/\Gamma(1+\nu)}.
\]

The same proof works for degree zero; it is only the separate \(\nu\uparrow1\) tail estimate that requires positive degree. Differentiate the squared estimate for \((2\pi)^\nu I_\nu\) at zero on polynomials. This gives the logarithmic floor \(-\gamma-\log(\pi h)\). The smooth causal convolution costs at most \(\int_0^h|w(t)|dt\le W_Rh\). Extend by the polynomial form core.

Combining (5.1) and (5.2),

\[
\boxed{m_Lg(h)>b_R^2
\quad\Longrightarrow\quad
c\le\frac{b_R}{\sqrt{m_Lg(h)}}<1.}\tag{5.3}
\]

Since \(g(h)\to\infty\) as \(h\downarrow0\), every strictly positive finite horizon admits some further positive extension, within these conventions.

For a prescribed slack \(0<\rho<1\), it suffices to choose \(h\le1\) so small that

\[
\log(1/h)>\gamma+\log\pi+W_R+
\max\{m_L,b_R^2/(\rho^2m_L)\}.
\]

Then \(c<\rho\), and (4.2) preserves at least \((1-\rho)m_L\).

**The limitation is now quantitative.** This elementary estimate asks for extension lengths roughly \(\exp(-\mathrm{const}/m_L)\). If \(m_L\) decreases, a succession of such lengths can have a finite sum. Local extendibility does not prove that the horizons tend to infinity.

For scale, at \(R=2\) the manuscript's analytic formulas give \(W_R<6\) and the arithmetic sum in (5.1) is below 3, hence \(b_R<11\). With the published \(m_{\log7}=1.37\times10^{-28}\), the symbolic choice \(h=e^{-10^{31}}\) makes \(m_Lg(h)>4(11)^2\). Thus the lemma gives an utterly negligible further extension with floor at least \(m_L/2\). This illustrates the inadequacy of the absolute bound; it is not a useful new computational horizon. See `local_extension_check.json` for the coarse constant checks.

The needed improvement is a bound on \(F^{-1/2}BA^{-1/2}\) that retains the arithmetic interaction with weak directions and allows extension lengths whose total diverges.

## 6. The weakest generator direction initially bends downward

The exact identity also gives

\[
Q_{\omega,L}=Q+\omega^2 B_2+O_L(\omega^4),\qquad
B_2=\tfrac12[X,[X,Q]],\tag{6.1}
\]

where the commutator expression denotes its bounded form extension. The factors \((x-y)^2\) remove the kernel singularity.

For a normalized lowest eigenvector \(Qe=me\),

\[
\langle e,B_2e\rangle
=m\|Xe\|^2-Q[Xe]
=-\langle Xe,(Q-mI)Xe\rangle\le0.\tag{6.2}
\]

This assertion does not require a simple eigenvalue. Reflection sends \(Xe\) into the opposite sector when \(e\) has definite parity. A nearly null even vector can therefore suffer a significant negative shift correction when multiplication by \(x\) sends it into much stronger odd modes.

Equation (6.2) concerns the instantaneous generator on that vector. The actual energy derivative is evaluated on the moving vector \(V_{s,L}f\), so it does not imply failure of the accumulated contraction defect.

## 7. A model showing what a path cannot accomplish by itself

Consider a two-sector model

\[
Q_L=\begin{pmatrix}m(L)&0\\0&M\end{pmatrix},\quad
X=\begin{pmatrix}0&a\\a&0\end{pmatrix},\quad 0<m(L)\le M.
\]

It has the same hyperbolic identity and reflection symmetry. Its weaker shifted diagonal is

\[
m(L)\cosh^2(a\omega)-M\sinh^2(a\omega).
\]

The generator is positive precisely while

\[
\tanh^2(a\omega)\le m(L)/M,
\]

and \(\kappa_L=a\sqrt{M/m(L)}\). Thus an adapted path is perfectly natural. Nevertheless, if \(m(L)\downarrow0\) at some *finite* \(L_*\), every such small-shift positive path can end at \((L_*,0)\). The existence of a local path is not a proof that its depth becomes unbounded.

This is the issue an arithmetic recursion must rule out. It is safer to work with the discrete block inequalities than to assume norm differentiability in depth: a newly active delay has operator norm one even immediately after its onset, and unit-coordinate differentiation moves delay boundaries.

## 8. Computations and a validated generator witness

The script `explore_path.py` assembles the central form on polynomial inputs and retains two additional modes for coordinate multiplication. Arb encloses matrix entries; mpmath computes exploratory generalized eigenvalues. The values below are finite-input diagnostics, not full-norm upper bounds and therefore not certified safe shifts.

| Horizon | Even head minimum, 128 inputs | Finite-input coordinate-energy norm | Diagnostic quadratic root |
|---|---:|---:|---:|
| log 3 | 5.53687e-8 | 61.1160 | 1.64023e-2 |
| log 5 | 9.29277e-18 | 2.53434e6 | 3.94632e-7 |
| log 7 | 6.80190e-28 | 2.32554e11 | 4.30021e-12 |

The root is \(\sqrt{Q[e]/(-B_2[e])}\) for the retained ground vector; it is not a root enclosure for the full shifted operator. Increasing from 64 to 128 inputs changed the log 7 energy norm substantially, so convergence of that diagnostic has not been established. The double-commutator coefficient was also compared against a small-shift finite difference; this is an algebraic numerical check, not interval certification of a spectral curve.

**Computer-assisted working result, in the adopted normalization.** At

\[
L=\log7,\qquad \omega=10^{-11},
\]

an explicitly saved real even polynomial \(f\), of degree at most 126, has

\[
\boxed{-2.999\times10^{-27}
<\frac{Q_{\omega,L}[f]}{\|f\|^2}
<-2.998\times10^{-27}<0.}\tag{8.1}
\]

`certify_generator_witness.py` proposes the vector using mpmath, rounds its Legendre coordinates to exact decimal rationals, and evaluates its Rayleigh quotient in Arb at 1792 bits. The vector coefficients and all parameters are saved in `generator_witness_log7.json`.

Re-evaluating the saved rational vector at 2048 bits reproduces the displayed enclosures and passes both the negative-generator and coordinate-energy lower-bound checks; see `generator_witness_log7_replay.json`. This is a precision replay of the same construction, not an independent implementation of its analytic formulas.

For the shifted generator the gamma profile is exactly

\[
G_\omega(t)=\cosh(\omega t)G_0(t).
\]

On \(|t|=3\), \(|G_\omega(t)|<256\cosh(3|\omega|)\). Degree 220 therefore has the explicit full-operator profile remainder

\[
\eta_{220,\omega}\le
\frac{256\cosh(3|\omega|)(L/3)^{221}}{221(1-L/3)}
<9.342\times10^{-42}.
\]

All prime terms are kept exactly as balls. The model Rayleigh quotient is approximately \(-2.9981370602909482\times10^{-27}\), leaving a large gap above the profile error. A polynomial negative witness needs no lower bound on the omitted spatial modes: one admissible vector with a negative enclosed value suffices.

The same rational vector, with its complete polynomial output under \(X\), also proves

\[
\boxed{\kappa_{\log7}>2.32\times10^{11},}\tag{8.2}
\]

using the central positivity supplied by v0.3 to define the energy norm. Both numerator and denominator are enclosed with their profile errors. This is a lower bound, not the upper bound needed in (3.2).

Result (8.1) establishes failure of generator positivity at that point. It does not establish noncontractivity of \(V\), a negative central Weil form, or a failure of RH. It lies outside the positive-shift interval certified in v0.3 and is consistent with all its stated results.

## 9. Consequences for the next investigation

There are two related paths to study.

1. A generator-positive path controlled by (2.3) or the sufficient invariant \(\omega\kappa_L<\pi/4\). The explicit recursion (4.1)–(4.3) gives a way to carry it forward. The present absolute cross bound is too costly to show unbounded depth.
2. A cumulative-storage path based directly on the contraction defect. The witness shows why this larger admissible region matters. At a positive shift and spatial split, the exact test is

\[
\left\|(I-ZZ^*)^{-1/2}Y(I-X^*X)^{-1/2}\right\|\le1.
\]

An interior bound with slack is preferable for an inverse-based recursion; on its exact boundary the defect may become singular. Changing the shift also changes the old defect, so positivity at one shift must not be silently carried to a smaller shift. A family estimate such as Section 3, or a separate validated continuation, is needed.

The next useful experiment is to measure the *cumulative* normalized coupling through a prime threshold at several shifts around the generator scale, retaining the full output Gram and the weak vectors. The next useful theorem is an arithmetic bound on that coupling, or on the central coupling in Section 4, which permits a sequence of extension lengths with divergent sum. A new full depth certificate is not asserted by this note's exploratory matrices.

The De Bruijn–Newman analogy motivates looking for a boundary, but does not identify it here. Rodgers and Tao prove that the De Bruijn–Newman constant is nonnegative; combined with the classical RH equivalence, RH would give equality to zero. Their parameter is a heat deformation of the xi kernel, whereas \(\omega\) here is a shifted quotient and \(L\) is a support cutoff. No map between those deformations, or transferred monotonicity theorem, has been established in this investigation.

## Sources and reproduction

- [v0.3 manuscript source](https://github.com/ebbaker/shifted-zeta-positivity/blob/a566944/papers/weil-depth/manuscript/finite_horizon_weil.tex), especially Sections 2–5 and 7, Appendix B.
- [Source numerical builder](https://github.com/ebbaker/shifted-zeta-positivity/blob/a566944/papers/weil-depth/numerics/certify_arb.py), copied without changes to `reference_certify_arb.py`. Repository licensing is preserved in `REFERENCE_LICENSE`.
- [Rodgers–Tao, The De Bruijn–Newman constant is non-negative](https://arxiv.org/abs/1801.05914).

Dependencies used: Python 3.10.0, python-flint 0.9.0 / FLINT 3.6.0, mpmath 1.4.1. A temporary environment for this session is `/private/tmp/weil-path-env`.

From this folder:

```sh
python explore_path.py --n 128 --horizons 3 5 7 --shifts 1e-12 1e-11 --bits 1792 --digits 100 --output diagnostics_N128.json
python certify_generator_witness.py --output generator_witness_log7.json
python certify_generator_witness.py --vector-record generator_witness_log7.json --bits 2048 --output generator_witness_log7_replay.json
python check_local_extension.py --output local_extension_check.json
```

Keep Python assertions enabled. The scripts and records are research artifacts; the normalization and analytic deductions remain subject to the author's planned independent verification.
