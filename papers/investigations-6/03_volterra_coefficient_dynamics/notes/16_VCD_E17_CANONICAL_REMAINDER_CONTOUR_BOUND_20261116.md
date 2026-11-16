# VCD-E17 r1 — Complete canonical remainder contour bound

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded task dispatch **gpt-6.1-sol / ultra**.
Separate runtime configuration or backend attestation unavailable.

**Complete, proved in-note.** The [frozen task][request] executes the
[B05 contour estimate][decision]. This is an intermediate quantitative
upper estimate for the canonical score remainder at time zero. Read the
[result index][results], [coefficient cluster][cluster], [control catalog][catalog]
and [avoid index][avoid], particularly [classification][a01],
[control premises][a02], [scope][a07] and [separate bounds][a12].
The [midpoint synthesis][midpoint] gives the preceding closure boundary.

## 1. Exact remainder on the strip

Use the complete source \(\Phi\) of the [manuscript, §2][ms], with
\(Z=\int_{\mathbb R}\Phi>0\). At \(\lambda=0\) the [E06 score][e06]
is \(V'=-\Phi'/\Phi=8\pi\sinh(4u)+b(u)\) on the real line. Put
\[
 g(u)=b(u)\Phi(u)=-\Phi'(u)-8\pi\sinh(4u)\Phi(u),\qquad
 B(z)=\frac1Z\int_{\mathbb R}g(u)e^{izu}\,du .
\]
This is the Fourier transform of the exact canonical remainder times
its density, with the same probability normalization as \(F\).

For \(w\in S=\{w:|\operatorname{Im}w|<\pi/8\}\), write
\(r_m(w)=\pi m^2e^{4w}\) and
\(s_m(w)=e^w(2r_m(w)^2-3r_m(w))e^{-r_m(w)}\).
On every compact subset of \(S\) there are constants \(c,C>0\)
with \(\operatorname{Re}r_m(w)\ge c m^2\) and \(|r_m(w)|\le C m^2\).
The complete sum of the \(s_m\) and each fixed termwise derivative
thus converge locally normally by polynomial-Gaussian domination.
The sum agrees on the positive real axis with the manuscript source.
The identity \(\Phi=(p''-p)/8\) and theta reflection in manuscript
§2 give evenness on the real axis for this same sum. The identity
theorem extends that reflection to \(S\). Hence \(g=-\Phi'-8\pi\sinh(4w)\Phi\)
is holomorphic and odd on \(S\). This continuation uses the product
formula for \(g\) and requires no statement about zeros of \(\Phi\) in \(S\).

Suppress \(w\) in \(r_m\). Differentiation gives
\[
 s_m'(w)=e^w(-8r_m^3+30r_m^2-15r_m)e^{-r_m}.
\]
Since \(8\pi\sinh(4w)=4r_m/m^2-4\pi e^{-4w}\), the exact
complete expansion is
\[
 \boxed{
 g(w)=e^w\sum_{m\ge1}
 \bigl[
  8(1-m^{-2})r_m^3-(30-12m^{-2})r_m^2+15r_m
  +8\pi e^{-4w}r_m^2-12\pi e^{-4w}r_m
 \bigr]e^{-r_m}.}
 \tag{1}
\]
In particular the \(m=1\) cubic coefficient vanishes before taking
absolute values. All modes, including the remaining first-mode terms,
are retained.

## 2. Contour shift and positive allowance

For real \(u\ge0\) set \(r_m=r_m(u)\) and define the positive polynomial
expression
\[
 P_m(u)=8(1-m^{-2})r_m^3+(30-12m^{-2})r_m^2+15r_m
         +8\pi e^{-4u}r_m^2+12\pi e^{-4u}r_m .
\]
For \(v\in[0,\pi/8)\) and \(|t|\le v\) the modulus of \(r_m(u+it)\)
is \(r_m(u)\) and its real part is at least \(\delta r_m(u)\),
where \(\delta=\cos(4v)>0\). By (1),
\[
 |g(u+it)|\le e^u\sum_{m\ge1}P_m(u)e^{-\delta r_m(u)} .
 \tag{2}
\]
Oddness gives the same bound at \(-u+it\). For any \(\delta>0\)
put \(a=\pi e^{4u}\). Since \(r_m\ge\pi\) and \(e^{-4u}\le1\),
there is an absolute \(C\) with \(P_m(u)\le C r_m^3\), so
\[
 \sum_{m\ge1}P_m(u)e^{-\delta r_m(u)}
 \le C a^3 e^{-\delta a}\sum_{m\ge1}m^6e^{-\pi\delta(m^2-1)} .
 \tag{3}
\]
For fixed \(\delta\) the series is finite, and the preceding factor
decays faster than \(e^{-c u}\) for every fixed \(c\). Consequently
\[
 A_Y(\delta)=\frac2Z\int_0^\infty e^{(1+Y)u}
                     \sum_{m\ge1}P_m(u)e^{-\delta r_m(u)}\,du
 \tag{4}
\]
is positive and finite for every \(\delta>0\) and finite \(Y\ge0\).

For \(z=x+iy\) shift to the line \(\operatorname{Im}w=t_0\),
where \(t_0=v\) if \(x\ge0\) and \(t_0=-v\) if \(x<0\).
On the ends of the rectangle with \(\operatorname{Re}w=\pm R\)
the other integrand factor is bounded by
\(e^{v|x|+Y R}\) for \(|y|\le Y\). Equations (2)–(3) send the end
integrals to zero as \(R\to\infty\). Those estimates also give absolute
convergence on both horizontal lines. Cauchy's theorem yields the
shifted Fourier integral. On the shifted line
\(\lvert e^{iz(u+it_0)}\rvert=e^{-v|x|-yu}\).
Together with (2) and reflection this proves
\[
 |B(x+iy)|\le e^{-v|x|}A_Y(\cos(4v)),
 \qquad |y|\le Y,\qquad 0\le v<\pi/8 .
 \tag{5}
\]

## 3. Lattice asymptotic

For \(j\in\{1,2,3\}\) set \(f_j(t)=t^{2j}e^{-t^2}\) for \(t\ge0\).
For \(a=\pi e^{4u}\) and \(h=\sqrt{\delta a}\),
\[
 \delta^{j+1/2}\sum_{m\ge1}(am^2)^j e^{-\delta am^2}
 =a^{-1/2}h\sum_{m\ge1}f_j(mh) .
 \tag{6}
\]
For each \(j\), \(f_j(t)\le C_j e^{-t^2/2}\).
The decreasing Gaussian gives, for every \(h>0\),
\[
 h\sum_{m\ge1}f_j(mh)\le C_j\int_0^\infty e^{-t^2/2}\,dt .
\]
For fixed \(a\), \(h\downarrow0\) with \(\delta\). The error of the
right-endpoint sum for \(f_j\) is bounded by
\(h\int_0^\infty |f_j'(t)|\,dt\), by integrating the difference on
each lattice cell. Thus the limit of (6) is
\(a^{-1/2}\int_0^\infty t^{2j}e^{-t^2}\,dt\). Squaring the
full-line Gaussian integral and using polar coordinates gives
\(\int_0^\infty e^{-t^2}\,dt=\sqrt\pi/2\). Integration by parts
multiplies the previous even Gaussian moment by \((2j-1)/2\), so
\[
 \int_0^\infty t^6e^{-t^2}\,dt=\frac{15\sqrt\pi}{16}.
\]

At each fixed \(u\), the scaled \(m^{-2}r_m^3\) sum tends to zero
because \(m^{-2}r_m^3=a r_m^2\), and by (6) its
\(\delta^{7/2}\)-scaled sum is bounded by a constant times
\(\delta a^{1/2}\). All the degree one and two terms tend to zero
after the same scaling, using (6) and the extra factors
\(\delta^{3-j}\). For domination in \(u\), use \(m^{-2}\le1\)
in the cubic expression and apply (6) to the bound \(P_m(u)\le C r_m^3\).
The scaled integrand in (4), including its exponential weight,
is bounded uniformly in \(\delta>0\) by a constant times
\[
 e^{(1+Y)u}a^{-1/2}=\pi^{-1/2}e^{-(1-Y)u}.
\]
For each fixed \(0\le Y<1\) this is integrable. Dominated convergence
and the cubic coefficient \(8\) give
\[
 \lim_{\delta\downarrow0}\delta^{7/2} A_Y(\delta)
 =\frac{2}{Z}\,8\,\frac{15\sqrt\pi}{16}
       \int_0^\infty e^{(1+Y)u}(\pi e^{4u})^{-1/2}\,du
 =\boxed{\frac{15}{Z(1-Y)}} .
 \tag{7}
\]
The scaled pointwise limit has divergent integral for \(Y\ge1\).
Fatou's lemma then gives \(\delta^{7/2}A_Y(\delta)\to+\infty\)
for fixed finite \(Y\ge1\). Equations (3)–(5) still apply at fixed
contour height there. The normalized convergence in (7) is nonuniform
as \(Y\uparrow1\). For each fixed \(\delta>0\), \(A_Y(\delta)\le
A_1(\delta)<\infty\) for \(Y<1\), so the ratio to the right-hand
asymptotic in (7) tends to zero as \(Y\uparrow1\) at that \(\delta\).

## 4. Optimization within the displayed allowance

Write \(p=7/2\), \(K_Y=15/[Z(1-Y)]\) and \(t=\pi/8-v\). For each fixed
\(0\le Y<1\), \(\cos(4v)=\sin(4t)\) and (7) give
\[
 e^{-vX}A_Y(\cos(4v))=e^{-\pi X/8}e^{Xt}A_Y(\sin(4t)),
 \qquad
 A_Y(\sin(4t))\sim K_Y(4t)^{-p}\quad(t\downarrow0).
\]
For \(X>0\) the function \(e^{Xt}t^{-p}\) on \(t>0\) has its
minimum \((eX/p)^p\) at \(t=p/X\), as follows by differentiating
its logarithm. For \(X\) large, this choice is in \((0,\pi/8]\)
and gives the corresponding asymptotic upper bound for the infimum.
For every \(\epsilon\in(0,1)\) choose \(t_1\in(0,\pi/8)\) so that
\(A_Y(\sin(4t))\ge(1-\epsilon)K_Y(4t)^{-p}\) for \(0<t<t_1\).
For \(t\ge t_1\), positivity and monotonicity of \(A_Y\) in \(\delta\)
give \(e^{Xt}A_Y(\sin(4t))\ge e^{Xt_1}A_Y(1)\), which grows faster
than \(X^p\). Taking the infimum and then letting \(\epsilon\downarrow0\)
proves
\[
 \boxed{\displaystyle
 \inf_{0\le v<\pi/8}e^{-vX} A_Y(\cos(4v))
 \sim \frac{15}{Z(1-Y)}
              \left(\frac{eX}{14}\right)^{7/2} e^{-\pi X/8}
 \qquad (X\to+\infty).}
 \tag{8}
\]
For each fixed \(X>0\) the infimum is at most \(A_1(1)\) by taking
\(v=0\), so (8) also fails to be uniform up to \(Y=1\).

The lower asymptotic in (8) controls only the infimum of the displayed
positive majorants. The bound on \(|B|\) is one-sided. Taking the
absolute values in (2) discards cancellation between terms and
the phase of the complete integral. A sharper bound exploiting
that cancellation remains open here. This calculation supplies
a canonical Fourier-scale upper allowance for the [paired E18 task][e18].
Signed control, a relative lower margin near zeros and a degree
update for induction are separate requirements.

## 5. Control premises

The [catalog][catalog], [B05][decision], [E07 screen][e07screen]
and [E15 comparisons][e15screen] give the premise checks below.
For a positive source \(\Psi\) its own score remainder times its
density is \(g_\Psi=-\Psi'-8\pi\sinh(4u)\Psi\), with Fourier
normalization \(\int\Psi\). The canonical-symbol test against \(\Psi\)
uses \(b\Psi\) in the Fourier integral.
For a compact multiplier \(\Psi=(1+h)\Phi\),
\[
 g_\Psi=(1+h)g-h'\Phi .
\]
For nonzero compact \(h\), the correction \(hg-h'\Phi\) is
nonzero, since its vanishing would give \(h'=bh\), whose only
compactly supported solution is zero by the first-order integrating
factor. This correction is compactly supported. By the identity
theorem it cannot extend holomorphically to \(S\).

| Control family | Premise comparison for E17 |
| --- | --- |
| Euler-factor translates | The same complete integer-square expansion fails. The forward tail of \(\Phi(u-\tfrac12\log p)\) starts at \(r_1/p^2\), and the Fourier field has the additional multiplier \(1+c\cos(\tfrac12 z\log p)\). |
| Weighted-square examples, finite-source audit and finite-prime orbits, including E07 | Complete equal coefficients fail, and the analytic continuation of each perturbed right-half-line mode sum fails full even reflection. Finite score rows and the first-mode cancellation can survive. E07's inherited nonreal-zero result is confined to its finite square-change class. |
| Reflected super-Gaussian and smooth shape or positive-primitive controls | The complete canonical square expansion fails. The reflected super-Gaussian also fails exponential confinement. |
| E10 and E12 compact multipliers | Full real reflection jet and exact real tails survive. The holomorphic own-remainder premise fails by the nonzero compact correction above, and their canonical score tests use \(b\Psi\). Their Fourier zero locations remain open. |
| BW-01 atoms and finite-profile controls, including triangular extensions | Atoms have no full-line density and the compact extensions fail strict positivity on the full line. |
| RH-conditional endpoint controls | The unchanged complete theta source and ordinary Dirichlet arithmetic fail. Their zero statements retain the RH hypothesis. |
| Fixed theta amplitude with variable observation | The varied observation fails the literal exponential Fourier readout. |
| BW-08 actual-profile relaxation | The relaxed data do not provide the physical full-line source and its Fourier field. |

These comparisons test the premises used for (1)–(8). No
control calculation of a corresponding optimized allowance or
zero test enters this proof.

[request]: ../research-progress/handoffs/VCD-E17-r1.md
[decision]: ../brainstorm/notes/10_VCD_B05_CANONICAL_FOURIER_SCORE_DECISION_20261116.md
[ms]: ../manuscript/main.tex
[e06]: 06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md
[e07screen]: 07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md#3-catalog-screen
[e15screen]: 13_VCD_E15_SHARED_MEMORY_EQUIVALENCE_20261116.md#6-canonical-input-and-control-scope
[midpoint]: 15_VCD_MIDPOINT_RESEARCH_SYNTHESIS_20261116.md
[e18]: ../research-progress/handoffs/VCD-E18-r1.md
[results]: ../../../../result-summaries/README.md
[cluster]: ../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[catalog]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
