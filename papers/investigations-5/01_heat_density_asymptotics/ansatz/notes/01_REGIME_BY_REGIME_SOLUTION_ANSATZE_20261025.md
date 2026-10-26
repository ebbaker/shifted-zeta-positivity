# Simple solution ansätze, separated by regime

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.
Chat0022, thread 01a17572-5411-7f32-9a12-7d1ba46ad679.

The author requested simpler analytical solution ansätze for all the
approximation families in the manuscript, explicitly allowing different
formulas in different regimes and complicated error terms. The requested
home for this new work is **ansatz/notes/**. This is a conceptual catalogue
and analytical derivation, not a manuscript revision or acceptance
certificate. No numerical, exact-arithmetic or machine-symbolic research
was executed. Existing onsets, physical regulator, normalization and
averaging kernel have not been changed.

## Current research state

The [maintained manuscript](../../manuscript/main.tex), through Notes54–55,
gives a finite analytical construction for every real time and height on
the declared strip, with positive per-scalar tolerances and both
infinite-time error limits. It retains actual covariance, direct time
rows and joining defects. Its existence result does not supply a short,
low-parameter description of the solution.

[Summary62](../../notes/62_CHAT0021_RESEARCH_SUMMARY_20261025.md) records
four subsequent in-note results: positive source compression; finite
evaluation and continuous-filter errors; a literal phase-index selector
using the authorized onset freedom; and polynomial additional-accuracy-bit
cost at a fixed descriptor/query box with explicit scalar providers.
Constants can still be very large and grow badly with height. The source
and evaluator algorithms were not executed in that chat, and a distinct
full-chain review remains open. The manuscript has not yet incorporated
Notes58–61. HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled remain.
The overview and progress register were read; their existing weak-filter
height-cost task is preserved alongside this author-requested ansatz work.

Lemma B2 bounds a source derivative; it is not itself a solution ansatz.
That bound and the analogous tail, moment, gate and transfer bounds can
remain elaborate. Simplification here concerns the field and observable
models which those bounds justify.

## One convention for every field model

Use the original field and heat sign,

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,\qquad H_t=-H_{zz},
\quad z=x+iy.
\]

For any proposed holomorphic field F retain the physical q=epsilon_g²:

\[
\rho_F=\frac{q|F_z|^2}{\pi(|F|^2+q)^2},\qquad R_F=K*\rho_F,\qquad
S_F=\log(|F|^2+q),\qquad U_F=K*S_F.                 \tag{A1}
\]

Away from zeros an exact alternative is

\[
\rho_F=\frac1{4\pi}\left|\frac{F_z}{F}\right|^2
\operatorname{sech}^2\!\left(\log\frac{|F|}{\sqrt q}\right). \tag{A2}
\]

Use A1 at zeros; the apparent singularity in A2 is only a representation
issue. The identity follows by writing r=|F|/sqrt(q) and
sech²(log r)=4r²/(1+r²)². Variable-q correction terms in the physical
evolution remain as defined in the manuscript.

For an amplitude-and-phase field F=A cos Theta, A1 is simply

\[
\rho_F=
\frac{q|A_z\cos\Theta-A\Theta_z\sin\Theta|^2}
{\pi(|A\cos\Theta|^2+q)^2}.                         \tag{A3}
\]

Amplitude must be retained: a constant rescaling changes this density at
fixed physical q. A good zero-location model alone is not a good density
model everywhere.

## The field models

### 1. Large negative time: Gaussian — established leading family

With T=-t and C=Phi(0)sqrt(pi)/2,

\[
F_-(t,z)=\frac C{\sqrt T}e^{-z^2/(4T)}.              \tag{A4}
\]

This is the existing leading field and itself solves the heat equation.
Its density can be displayed more simply than a long rational expansion:

\[
\rho_-=\frac{x^2+y^2}{16\pi T^2}
\operatorname{sech}^2\!\left[
\log\frac C{\epsilon_g\sqrt T}-\frac{x^2-y^2}{4T}\right]. \tag{A5}
\]

The fixed-regulator and adaptive-regulator scaling profiles in the paper
are two scalings of this same field, not separate ansatz families.
Higher endpoint corrections are Gaussian derivatives, hence Gaussian
times Hermite polynomials. No additional negative-time family is needed.

### 2. Finite-time core: Gaussian times a polynomial — new candidate

Fix the upper time b of this model's use, choose a>b, and let p_m(v) be a
real polynomial fixed once for the target accuracy. Use the positive source

\[
f_m(u)=e^{-au^2}p_m(u^2)^2.
\]

Its exact heat field is

\[
F_{\mathrm c}(t,z)=
\big[p_m(-\partial_z^2)\big]^2
\left\{\frac{\sqrt\pi}{2\sqrt{a-t}}
             e^{-z^2/[4(a-t)]}\right\},\qquad t<a.    \tag{A6}
\]

The square denotes composition of differential operators. Thus A6 is a
Gaussian times a finite even polynomial, with coefficient evolution fixed
by the heat equation. It has no source-cell endpoints or error-function
differences. This is a proposed alternative to the paper's finite
piecewise-polynomial sources and Note58's compactly supported polynomial
square; it is not the same stored source.

For tau=a-t and p_m(v)²=sum(c_k v^k), its explicit expansion is

\[
F_{\mathrm c}=\frac{\sqrt\pi}{2\sqrt\tau}e^{-z^2/(4\tau)}
\sum_{k=0}^{2m}\frac{(-1)^k c_k}{(4\tau)^k}
H_{2k}\!\left(\frac{z}{2\sqrt\tau}\right),            \tag{A7}
\]

where H_n is the physicists' Hermite polynomial.

There is a useful existence argument, but no useful degree bound yet.
Extend Phi evenly, set h(u)=exp(au²/2)sqrt(Phi(u)) and c=(a-b)/2>0.
The double-exponential source tail makes h an even member of
L²(exp(-cu²)du). Even Hermite polynomials give approximants
p_m(u²) converging to h in that norm. For fixed Y and j<=3,

\[
\sup_{t\le b,\ x\in\mathbb R,\ |y|\le Y}
|\partial_z^j(F_{\mathrm c}-H)|
\le C_j\|p_m-h\|_c(\|p_m\|_c+\|h\|_c)\longrightarrow0, \tag{A8}
\]

where one can take
C_j=sup_{u>=0}u^j exp(-cu²+Yu).
Indeed the weighted source error is bounded by this constant times
the Gaussian-weighted integral of |p_m-h||p_m+h|, followed by
Cauchy–Schwarz. The four-jet statement is an absolute field comparison,
not relative accuracy near zeros or a complete physical-tuple theorem.
The standard L² completeness input is
[DLMF 18.18(i)](https://dlmf.nist.gov/18.18#i).

A8 supplies a reason to investigate A6. It does not establish that a
low-degree polynomial works, an effective coefficient constructor, or
an improvement over Note58's proven descriptor bound. The original
negative endpoint and positive outer models should initially be retained.
No fixed A6 is proposed for t approaching a or for t tending to infinity.

### 3. Large positive time, inner heights: Gaussian envelope times cosine

Let L be the large real solution of

\[
4\pi e^{4L}=2tL+9,\qquad
\kappa=8tL-2t+36,\qquad
M_0=2\pi^2 e^{tL^2+9L-\pi e^{4L}}\sqrt{\frac{2\pi}{\kappa}}.
\]

The candidate is

\[
F_{\mathrm{in}}(t,z)=M_0(t)e^{-z^2/(2\kappa(t))}
\cos(L(t)z).                                       \tag{A9}
\]

The manuscript proves a moment-based comparison to
M(1-vz²/2)cos(mu z); it also proves mu-L=O(kappa^-1) and
v-kappa^-1=O(kappa^-3/2). A9 exponentiates the quadratic envelope
and substitutes explicit saddle quantities. The initial intended domain
is the inherited inner window |x| of order kappa^(1/3), with its full
buffers and fixed transverse strip. The substitutions need their own
error ledger, especially M to M0. The existing coarse mass allowance
does not automatically preserve every sharper clock/evolution rate.
A9 is not an exact heat solution when its coefficients vary with time.

For display L may be written exactly using the large real Lambert branch,

\[
L=-\frac14W_{-1}\!\left(-\frac{8\pi}{t}e^{-18/t}\right)
-\frac9{2t}.
\]

Replacing L by only its log-log asymptotic is adequate for some coarse
densities, but its phase error is multiplied by x. Do not make that
replacement in an oscillatory field over a growing interval without
paying the phase error.

### 4. Very large height at fixed sufficiently positive time: elementary cosine

For X=|x| and ell_X=log(X/(4pi)), define

\[
A_{\mathrm o}(t,X)=\frac{\pi^{1/4}}{16}X^{7/4}
\exp\!\left[-\frac{\pi X}{8}
+\frac t{16}\left(\ell_X^2-\frac{\pi^2}{4}\right)\right],
\]
\[
\Theta_{\mathrm o}(t,X)=\frac X4(\ell_X-1)
+\frac{\pi t}{16}\ell_X+\frac{7\pi}{8}.
\]

Then the proposed elementary reduction is

\[
F_{\mathrm o}(t,X)=A_{\mathrm o}(t,X)\cos\Theta_{\mathrm o}(t,X).
                                                               \tag{A10}
\]

This follows at leading order by reducing the existing linear gamma
model, not by fitting data. The two individual carriers have amplitude
A_o/2. Specifically, with s=(1+iX)/2,
|Mcal(s)|~pi^(1/4)X^(7/4)exp(-pi X/8)/32,
arg Mcal(s)=X(ell_X-1)/4+7pi/8+O(1/X), and
alpha(s)=ell_X/2+i pi/4+O(1/X).
Multiplication by exp(t alpha²/4) gives A10.

For fixed 32<=t<=T, combining these expansions with the manuscript's
linear-carrier comparison gives the expected carrier-scaled error
O_T((1+log²X)/X). This is a leading reduction with its algebra recorded
here; a finite four-jet and direct-time error ledger is still to be written.
It is not relative error divided by F_o at zeros. No extension to t=0
or arbitrary jointly growing t and X is asserted.

On a positive-height complex buffer, replace X by z and use the analytic
Log z; use even reflection for the other tail. The scalar function
|x| is not a holomorphic extension. The coefficient and phase use
[DLMF 5.11](https://dlmf.nist.gov/5.11), particularly the leading
log-Gamma, digamma and bounded-real-part gamma expansions.
At t=64 the phase agrees with Summary62's Note60 expansion, including
4pi log(X/(4pi)) and 7pi/8.

### 5. Joint large time and height: retain a saddle pair; test a Lambert-W reduction

The manuscript's established model is already short in structural form:

\[
P_*(t,z)=\mathcal S_t(s)+\mathcal S_t(1-s),\qquad s=(1+iz)/2,
\]
\[
\mathcal S_t(w)=
\frac{\mathcal M(p)e^{-(p-w)^2/t}}
{\sqrt{1-\tfrac t2\alpha'(p)}},\qquad
p=w+\tfrac t2\alpha(p),\quad
\alpha=\mathcal M'/\mathcal M,\quad
\mathcal M(p)=\frac{p(p-1)}{16}\pi^{-p/2}\Gamma(p/2).   \tag{A11}
\]

This covers the gap between the simple inner and fixed-time outer
regimes. For a simpler new candidate replace the saddle by p0 satisfying

\[
p_0=w+\frac t4\operatorname{Log}\frac{p_0}{2\pi}
=-\frac t4W_{\mathcal B}\!\left(-\frac{8\pi}{t}e^{-4w/t}\right)
\]

and set

\[
\mathcal M_{\mathrm{el}}(p)=\frac{\sqrt\pi}{8}p^{1/2}(p-1)
\exp\!\left[\frac p2\left(\operatorname{Log}\frac p{2\pi}-1\right)\right],
\]
\[
\mathcal C_W(t,w)=
\frac{\mathcal M_{\mathrm{el}}(p_0)e^{-(p_0-w)^2/t}}
{\sqrt{1-t/(4p_0)}},\qquad
F_W(t,z)=\mathcal C_W(t,s)+\mathcal C_W(t,1-s).        \tag{A12}
\]

A12 is a candidate, not an accepted replacement for A11. The large
saddle branch is selected by analytic continuation in w, with conjugate
reflection; a fixed library W_-1 branch of the winding exponential
argument is not a global branch rule. This follows from the defining
[Lambert-W identity and branch structure](https://dlmf.nist.gov/4.13).
The original gamma saddle remains the supported choice until both
field comparison and direct heat-residual/time estimates for A12 are paid.

## Simple density models within their own regimes

### 6. Near an isolated zero: rational peak

If F(z)=c(z-a)^m is the local model and
delta=(epsilon_g/|c|)^(1/m), then exactly for this model

\[
\rho_{\mathrm{zero}}(z)=
\frac{m^2\delta^{2m}|z-a|^{2m-2}}
{\pi(|z-a|^{2m}+\delta^{2m})^2}.                     \tag{A13}
\]

For a simple zero this becomes delta²/[pi(|z-a|²+delta²)²].
Freezing the physical regulator and local slope introduces errors for
the true field, which belong in the comparison estimate. This form
does not assume that every zero of H is simple or real.

### 7. Inner clock and resolved outer density: lattice or continuum

The manuscript's long Bernoulli expressions have the exact shorter
meaning

\[
d_j=(j+\tfrac12)\frac\pi L,\qquad
R_{\mathrm{lat}}=k_h(y)\sum_jk_\ell(x-d_j),\qquad
J_{\mathrm{lat}}=-\frac2\kappa k_h(y)\sum_jd_jk_\ell(x-d_j). \tag{A14}
\]

These sums are locally finite because the kernel has compact support.
They retain the phase and the model's exact continuity law. They are
an exact rewrite, not a faster evaluated algorithm. If only leading
coarse shape is wanted,

\[
R_{\mathrm{in}}\simeq\frac L\pi k_h(y),\qquad
R_{\mathrm{out}}\simeq\frac1{4\pi}\log\frac{|x|}{4\pi}\,k_h(y).
                                                               \tag{A15}
\]

The outer statement is used in the inherited resolved-regulator regime
(in particular fixed t>64 at large height), not throughout the regulator
transition. Continuum averaging discards lattice phase; it does not
inherit the sharper differentiated estimates merely from static accuracy.
For a variable phase, R=Theta_x k_h/pi and J=-Theta_t k_h/pi obey
continuity algebraically, but comparison of this proposed current to the
physical current still needs proof.

### 8. The regulator transition: two translated layers

Keep the manuscript's simple leading layer shape:

\[
R_{\mathrm{layer}}=
\frac{\omega}{2\pi}[k_h(y-d)+k_h(y+d)],\qquad
d=\frac{[\log(\epsilon_g/A_{\mathrm{arm}})]_+}{\omega}.
                                                               \tag{A16}
\]

Here A_arm and omega are the original linear gamma carrier amplitude
and local frequency. The supported coarse comparison has O(1) absolute
error; it is not an arbitrarily accurate replacement. Use the exact
ratio and its zero to locate the narrow transition. Substitution of a
rough asymptotic switching time can move the center by more than the
transition width. The two layers describe regularized density, not a
claim of nonreal zeros.

## Remaining formulas and what simplification means for them

| Manuscript family | Treatment in this catalogue |
| --- | --- |
| Negative fixed/adaptive scaling and Gaussian endpoint corrections | A4–A5; higher corrections remain Gaussian times polynomials. |
| Moment carrier, explicit clock, clock geometry | A9, A14–A15. Clock spacings and their Vandermonde products are already analytical; no new ansatz is required. |
| Finite source cells, positive cubic interpolation, signed-source transfer and Note58 polynomial square | Candidate A6–A8 replaces their field representation in a bounded-time core; transfer lemmas stay as error machinery. |
| Finite xi-derivative Taylor fallback | Remains a valid finite representation. Writing a heat exponential would only hide the same difficulty. A6 is a candidate alternative on its stated time domain, not a proved global replacement under adaptive q. |
| Linear gamma outer field | Elementary A10 on a fixed sufficiently positive time interval. |
| Full gamma saddle, positive endpoint and evolution | Existing A11; proposed A12 requires its own spatial and time budgets. |
| Root collars and regularization bridges | Local model A13; bridge inequalities remain in the errors. |
| Regulator switching profile | A16, retaining the exact center when needed. |
| Spatial/temporal joins and all-time assembly | Weighted sum of the selected fields, with all original supports and defects paid. |
| Effective constants, source conditioning and evaluator/filter costs | These are bounds or algorithms, not extra solution ansätze. |

For the exact cosine-cell benchmark, F=M cos(kz) with fixed k and
M'=k²M, the paper already gives elementary cell-averaged U, R and Q.
For example, with eta=epsilon/M and a=sinh²(ky)+eta²,

\[
U_{\mathrm{cell}}=2\log M+2\operatorname{arsinh}\sqrt a-2\log2.
\]

The other cell quantities can be retained as derivatives of this
potential with the prescribed cell average. This is not identical to
the fixed compact filter or a variable-q physical calculation; the
transverse averaging covariance correction cannot be discarded.

The narrow-filter gradient approximation to Q is likewise a separate
approximation:

\[
Q\simeq v_t(U_{xt}^2-U_{yt}^2)
+v_x(U_{xx}^2-U_{xy}^2)+v_y(U_{xy}^2-U_{yy}^2).
\]

It requires the manuscript's small-width, fixed-positive-regulator,
bounded-derivative hypotheses. It is not a general covariance closure.
For the full physical problem compute the actual Q from the same chosen
field and original filter, keeping its error allowance.

An all-time display can therefore be short:

\[
F_{\mathrm{ans}}=\chi_-F_-+\chi_{\mathrm c}F_{\mathrm c}
+\chi_+F_+,\qquad \chi_-+\chi_{\mathrm c}+\chi_+=1,
\]

where F_+ is selected by the positive-time subregime and the weights use
paid overlaps. This notation does not by itself prove that the proposed
new models cover the whole domain. Derivatives of the weights generate
heat and, for spatial joins, nonholomorphic defects; all belong in the
error ledger. In particular Q of the joined field is not the weighted
sum of the separate Qs.

## Decision and next bounded step

There is a useful list of simple shapes already: Gaussian; Gaussian
times polynomial; Gaussian-envelope cosine; explicit large-height
cosine; saddle pair; rational zero peaks; lattice density; and two
translated layers. Only the first, the original saddle/clock/layer
models and their stated comparisons are inherited results. The newly
proposed representations are not promoted to the manuscript's complete
all-time theorem by this catalogue.

Next **Analysis — Sol**: the bounded
[HDA-18-AN09 r1](../../research-progress/handoffs/HDA-18-AN09.md) asks
for an effective positive Gaussian-polynomial core construction and
four-jet degree/error ledger, or the first precise obstruction. It
decides whether A6 is a useful simplification rather than only an
existence family. No agent, new chat or research computation is dispatched.


## Author's subsequent priority — 25 October 2026

The author subsequently prioritized ansatz4 and other high-height
formulas across **all real times**, with accurate amplitude/phase and
piecewise transition descriptions. The core-first recommendation above
is historical. The [new overview](../research-overview/01_HIGH_HEIGHT_ANSATZ_RESEARCH_OVERVIEW_20261025.md),
[branch register](../research-progress/01_HIGH_HEIGHT_ANSATZ_RESEARCH_PROGRESS_20261025.md)
and [high-height handoff](../research-progress/handoffs/HDA-A01-AN01.md)
govern continuation. The catalogue and its original claims are preserved.
