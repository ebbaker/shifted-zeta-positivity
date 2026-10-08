# Newman flow, finite collisions, and a positive-kernel obstruction

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed to this agent and are not inferred.

Status: a source-scoped literature check and elementary deductions. This note
does not establish exponent descent for zeta or a new zero-free region. The
positive-kernel construction below is an explicit mathematical counterexample
to a proposed *general analytic mechanism*, not a counterexample to RH or to
quasi-RH implying RH for zeta. No priority claim is made for these deductions.

## 1. Convention and the immediate limitation

Use the Fourier-heat convention

\[
 H_t(z)=\int_{\mathbb R}e^{tu^2}\Phi(u)e^{izu}\,du,
 \qquad \partial_tH_t=-\partial_z^2H_t.
\]

An irrelevant positive factor in the integral does not affect zeros. In the
usual Polymath/Rodgers–Tao zeta normalization, a zeta zero \(\rho=\beta+i\gamma\)
corresponds to an \(H_0\) zero whose imaginary part has magnitude
\(2|\beta-1/2|\). Thus a zero-free half-plane \(\Re s>\theta\), together with
the functional equation, supplies strip width \(W=2\theta-1\).

De Bruijn's theorem gives

\[
 \operatorname{Zeros}(H_{t+h})\subset
 \{z:|\Im z|\le\sqrt{\max(W_t^2-2h,0)}\}
 \tag{1}
\]

whenever the zeros of \(H_t\) lie in a strip of width \(W_t\). Consequently
\(\Lambda\le t+W_t^2/2\). If one repeatedly uses only (1), then

\[
 (t+h)+\frac{W_t^2-2h}{2}=t+\frac{W_t^2}{2}.
 \tag{2}
\]

The remaining waiting time falls, but its absolute endpoint does not improve.
At time zero, quasi-RH gives \(\Lambda\le(2\theta-1)^2/2\), a positive bound
unless \(\theta=1/2\). Rodgers–Tao's lower bound \(\Lambda\ge0\) supplies the
other inequality, not a route to eliminating this positive interval.

Sources: [de Bruijn's theorem as recorded in Newman–Wu, Theorem 7](https://arxiv.org/abs/1901.06596)
and [Rodgers–Tao](https://arxiv.org/abs/1801.05914). Their normalizations must be
checked before transferring constants; equation (1) fixes this note's choice.

## 2. Positive time localizes any nonreal zeros

Ki–Kim–Lee proved that, at every fixed positive time, all but finitely many
zeta heat-flow zeros are real and simple. A stronger input is available from
[Polymath 15, Theorem 1.5(i)](https://arxiv.org/html/1904.12438#S1.Thmtheorem5):
there is an absolute constant \(C\) such that, for \(0<t\le1/2\), a zero
\(H_t(x+iy)=0\) with \(x\ge\exp(C/t)\) must have \(y=0\).
Evenness gives the analogous assertion for negative \(x\).

This is uniform on a compact positive-time interval \(t\ge\varepsilon>0\).
It is not uniform as \(\varepsilon\downarrow0\). The bare statement “finitely
many exceptions at each time” would not by itself justify the compactness
argument below; the uniform cutoff does.

The original Ki–Kim–Lee paper is
[On the de Bruijn–Newman constant, Advances in Mathematics 222 (2009), 281–306](https://doi.org/10.1016/j.aim.2009.04.003).
The statements are also recorded in [Newman–Wu, Theorems 13–14](https://arxiv.org/abs/1901.06596).
The imported theorems are used here; their complete proofs were not independently
replayed in this scout.

### Proposition 1: positive zeta threshold entails a finite collision

If the zeta de Bruijn–Newman constant satisfies \(\Lambda>0\), then there is a
finite real \(x_*\ne0\) such that

\[
 H_\Lambda(x_*)=H'_\Lambda(x_*)=0.
 \tag{3}
\]

**Proof.** The initial width-one strip and (1) give \(\Lambda\le1/2\).
Choose \(t_n\uparrow\Lambda\) with \(\Lambda/2\le t_n<\Lambda\), so every
chosen time lies in the range of Theorem 1.5(i).
By the defining threshold property, each \(H_{t_n}\) has a nonreal zero \(z_n\).
The classical strip bound gives \(|\Im z_n|\le1\), while Theorem 1.5 gives
\(|\Re z_n|<\exp(2C/\Lambda)\). Passing to a subsequence, \(z_n\to z_*\).
Joint continuity gives \(H_\Lambda(z_*)=0\). All zeros of \(H_\Lambda\) are
real, so \(z_*=x_*\in\mathbb R\).

If this root were simple, the implicit-function theorem would supply a unique
nearby root for real times near \(\Lambda\). Conjugation symmetry forces that
unique root to be real. This contradicts the nonreal \(z_n\) eventually lying
in that neighborhood. Hence the root is multiple. Positivity of the kernel
gives \(H_t(0)>0\), so \(x_*\ne0\). \(\square\)

Thus a positive threshold cannot be explained solely by defects disappearing
at infinite height at that positive time. At the time-zero endpoint the
uniform compactness argument fails: its cutoff diverges like \(\exp(C/t)\).
This distinction matters when considering an infinite sequence of improving
positive-time statements.

### Corollary 2: an exact collision-exclusion target

For the zeta heat flow, RH is equivalent to

\[
 \text{there is no }(t,x)\in(0,\infty)\times\mathbb R
 \text{ with }H_t(x)=H'_t(x)=0.
 \tag{4}
\]

**Proof.** If RH holds, \(\Lambda=0\); zeros are real and simple for every
\(t>0\). Simplicity can be seen directly from the local heat-flow expansion:
a multiple real zero at time \(t>0\) produces nonreal zeros immediately before
\(t\), contradicting the threshold property. Conversely, if RH fails,
Rodgers–Tao and the threshold equivalence give \(\Lambda>0\), and Proposition 1
provides a positive-time multiple real zero. \(\square\)

The local expansion just invoked is [Polymath 15, Proposition 3.1(ii)](https://arxiv.org/html/1904.12438#S3.Thmproposition1).
At a real zero of multiplicity \(m\ge2\) at time \(T\), nearby zeros have the
form

\[
 x_*+\sqrt{2(t-T)}\,\lambda_j+O(|t-T|),
 \tag{5}
\]

where the \(\lambda_j\) are the distinct real zeros of the probabilists'
Hermite polynomial \(\operatorname{He}_m\). At least one \(\lambda_j\ne0\),
so immediately earlier times have nonreal zeros.

Under quasi-RH, one may restrict the time interval in (4) to
\(0<t\le W^2/2\); later multiple roots cannot occur because all zeros have
already become real. This is a reduction of the missing task. It is not a
proof of collision exclusion, and it does not make that task weaker than RH.

## 3. Why strict strip improvement need not reach time zero

The Ki–Kim–Lee strict-contraction theorem, recorded as Theorem 13 in
Newman–Wu, improves (1) strictly when the initial entire function has order
less than two, only finitely many nonreal zeros, and at least as many real
zeros as nonreal zeros in the upper half-plane. Positive-time zeta flow
meets these hypotheses whenever nonreal zeros
remain. Thus (2) is not the strongest available analytic observation.

Nevertheless, a strict improvement has no stated uniform positive size.
Successively improved upper bounds can converge to a positive threshold. The
local geometry of a double collision explains how the gain can degenerate.

### Proposition 3: double-collision normal form

Suppose a real analytic Fourier heat flow has an exact double real zero at
\((T,x_*)\). For \(t<T\) sufficiently close to \(T\), its two nearby zeros have
the form

\[
 a(t)\pm i y(t),\qquad
 a(t)=x_*+O(T-t),\qquad
 y(t)^2=2(T-t)+O((T-t)^2).
 \tag{6}
\]

**Proof.** Translate \(x_*\) to zero. Real Weierstrass preparation gives
\(H_t(z)=A(t,z)(z^2+b(t)z+c(t))\), with \(A(T,0)\ne0\) and
\(b(T)=c(T)=0\). At this point the heat equation gives
\(A(T,0)c'(T)=-2A(T,0)\), hence \(c'(T)=-2\). Completing the square,
\((z+b(t)/2)^2=b(t)^2/4-c(t)=2(t-T)+O((t-T)^2)\). This is (6).
\(\square\)

In particular, the bound contributed by this conjugate pair satisfies

\[
 t+\frac{y(t)^2}{2}=T+O((T-t)^2).
 \tag{7}
\]

The classical strip estimate is therefore asymptotically sharp at leading
order near an ordinary collision. Strict improvements away from the collision
do not contradict a positive collision time. Any argument that iterates them
down to zero needs a quantitative gain with nondegeneracy sufficient to rule
out a positive limiting endpoint.

## 4. Explicit positive, double-exponentially decaying obstruction

The following construction shows why positivity of the Fourier kernel, rapid
decay, evenness, a fixed narrow zero strip, and a finite exceptional set do not
by themselves remove positive thresholds.

Put

\[
 \phi(u)=e^{-\cosh u},\qquad
 Q(u)=\phi^{(4)}(u)+324\phi(u).
 \tag{8}
\]

### Proposition 4

The kernel \(Q\) is even, smooth, strictly positive, strictly decreasing for
\(u>0\), and double-exponentially decaying. For

\[
 F_t(z)=\int_{\mathbb R}e^{tu^2}Q(u)e^{izu}\,du
 \tag{9}
\]

the threshold \(\Lambda_Q\) is finite and strictly positive. At time zero
there are exactly four nonreal zeros, namely \(\pm3\pm3i\), and every other
zero is real. In particular,

\[
 0<\Lambda_Q\le\frac92.
 \tag{10}
\]

**Kernel positivity.** Write \(c=\cosh u\ge1\). Direct differentiation gives

\[
 Q(u)=\big(c^4-6c^3+5c^2+5c+321\big)e^{-c}.
\]

On \(c\ge0\), \(c^4-6c^3\ge-2187/16\), since its minimum occurs at
\(c=9/2\). On \(c\ge1\), \(5c^2+5c+321\ge331\). Thus the bracket is at
least \(3109/16>0\). The formula also establishes evenness and decay. Every
Gaussian weight \(e^{tu^2}\) is integrable against \(Q(u)\), for every real
\(t\), and (9) is jointly entire in \((t,z)\).

An exact certificate for the same lower bound is

\[
 c^4-6c^3+5c^2+5c+321
 =\frac{(2c-9)^2(4c^2+12c+27)}{16}
   +5(c^2-1)+5(c-1)+\frac{3109}{16}.
\]

For the general form of de Bruijn's theorem, the kernel assumptions are
local integrability, \(Q(-u)=\overline{Q(u)}\), and a bound
\(|Q(u)|\le A\exp(-|u|^{2+\alpha})\) for some \(A,\alpha>0\).
They are equations (10)–(11) preceding Theorem 7 in Newman–Wu. Our explicit
kernel satisfies them, for example with \(\alpha=1\) after increasing \(A\).
The same is true after multiplication by any fixed Gaussian weight. Thus the
threshold argument uses the general kernel theorem, not a zeta-only version.

The asserted monotonicity also has an elementary certificate:

\[
 Q'(u)=-\sinh(u)e^{-c}R(c),\qquad
 R(c)=c^2(c-5)^2-2c^2-5c+316.
\]

For \(1\le c\le8\), \(R(c)\ge316-128-40=148\). For \(c\ge8\),
\(R(c)\ge7c^2-5c+316>0\). Thus \(Q'(u)<0\) for every \(u>0\).

**Zeros at time zero.** Let

\[
 B(z)=\int_{\mathbb R}e^{-\cosh u}e^{izu}\,du=2K_{iz}(1),
\]

where \(K_\nu\) is the modified Bessel function. Pólya proved that all zeros
of \(K_{iz}(a)\) are real for every \(a>0\). A modern proof appears in
[Gasper, Section 2](https://arxiv.org/abs/0801.2996).

For completeness, there is a short spectral proof of the needed assertion.
If \(K_{iz}(1)=0\), put \(y(x)=K_{iz}(e^x)\), \(x\ge0\). The Bessel equation
and its decaying asymptotic imply

\[
 -y''(x)+e^{2x}y(x)=z^2y(x),\qquad y(0)=0,
\]

with \(y\) and \(y'\) decaying at infinity. Integration against
\(\overline y\) yields

\[
 z^2\int_0^\infty|y|^2dx
 =\int_0^\infty\big(|y'|^2+e^{2x}|y|^2\big)dx>0.
\]

The solution is not identically zero, by the usual large-argument asymptotic
of \(K_\nu\). Hence \(z^2\) is positive real, forcing \(z\) to be real.

Four integrations by parts in (8) give

\[
 F_0(z)=(z^4+324)B(z).
 \tag{11}
\]

The polynomial zeros are exactly \(3+3i,3-3i,-3+3i,-3-3i\). Since \(B\)
has no nonreal zero, these four roots are simple and no other nonreal zeros
occur. Therefore the entire zero set lies in \(|\Im z|\le3\).

**Threshold.** De Bruijn's theorem gives real zeros for all \(t\ge9/2\).
The same theorem gives upward persistence of the all-real property from any
time where it holds. Locally uniform convergence and Hurwitz's theorem make
this property closed in \(t\); the function cannot converge to the zero
function because \(F_t(0)>0\). It is therefore an upper ray with finite lower
endpoint. Each nonreal simple root of (11) persists for sufficiently small
positive \(t\), so the endpoint is strictly positive. This proves (10).
\(\square\)

Since \(F_0\) has only finitely many nonreal zeros, the Gaussian strong
universal-multiplier theorem of Ki–Kim–Lee additionally gives finitely many
nonreal zeros of \(F_t\) for each \(t>0\). This is an imported general theorem;
the proof of the positive-threshold obstruction does not need this extension.

### Corollary 5: arbitrarily narrow strips still permit positive thresholds

For \(a>0\), define \(Q_a(u)=aQ(au)\). Substitution in (9) gives

\[
 F^{[a]}_t(z)=F_{t/a^2}(z/a),\qquad
 \Lambda_{Q_a}=a^2\Lambda_Q.
 \tag{12}
\]

Its four nonreal time-zero zeros are \(\pm3a\pm3ai\). Thus for every desired
strip width \(w>0\), choosing \(a=w/3\) gives a strictly positive,
double-exponentially decaying kernel with all zeros in \(|\Im z|\le w\),
only four nonreal zeros at time zero, and a strictly positive threshold.

This changes the function with the scale. It is not a family of progressively
sharper bounds on one fixed zeta function. The construction does not preserve
zeta's Euler product, explicit formula, prime coefficients, or exact zero
density; these are precisely examples of additional arithmetic structure a
successful zeta-specific argument might have to use.

## 5. Research consequence

The Newman route now has a concrete missing statement: exclude simultaneous
real zeros of \(H_t\) and \(H'_t\) for positive times in the quasi-RH interval.
In integral form this asks to exclude simultaneous vanishing of

\[
 \int_{\mathbb R}e^{tu^2}\Phi(u)\cos(xu)\,du,
 \qquad
 \int_{\mathbb R}u e^{tu^2}\Phi(u)\sin(xu)\,du.
\]

The positive-kernel example rules out proving this from kernel positivity,
rapid decay, fixed-strip confinement, and finite exceptions alone. The
positive-time cutoff reduces every hypothetical positive threshold to a
finite-height collision, but the unknown threshold determines an unbounded
search height as it approaches zero. Fixed numerical verification cannot
close that quantifier gap.

A productive next step would therefore require an arithmetic collision
exclusion estimate, or a quantitatively nondegenerate improvement law that
prevents positive limiting thresholds. Neither is supplied by the presently
reviewed quasi-RH statement or by ordinary strip contraction.
