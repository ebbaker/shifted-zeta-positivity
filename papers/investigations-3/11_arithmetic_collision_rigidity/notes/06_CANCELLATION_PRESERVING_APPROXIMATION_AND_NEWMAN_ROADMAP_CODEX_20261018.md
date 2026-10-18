# Preserving modular cancellation: a finite approximation and a Newman roadmap

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model **gpt-6-astra (Codex)**, reasoning effort
**ultra**. Same-model parallel analysis and internal review; no specialist
review or new Newman bound.

**Assessment.** The useful next research step is a quantitative estimate on
the complete theta field at its own scale. [Note 05](05_COMPLEX_STRIP_CARRIERS_AND_SHARP_LOG_DERIVATIVES_CODEX_20261018.md)
already strengthens the packet theorem. The finite approximation below
preserves the cancellation responsible for exponential decay; it makes an
existing contour proposal more explicit. A lower bound or zero count that
consumes its error is still missing.

Read the [result-summary index](../../../../result-summaries/README.md),
[heat-flow results](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[control catalogue](../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../avoid/README.md). The relevant screens are
[target restatements](../../../../avoid/01_restating_the_target.md),
[controls](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scoped negative results](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
and [retaining cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## 1. What the present gain does and does not buy

The carrier and arithmetic tail are now holomorphic and nonvanishing in
a strip wider than the entire classical zero strip. Their logarithmic
derivatives are controlled independently of height. This is useful for
Rouché comparisons and evaluating quotients without an auxiliary pole.

However, one can already choose the full positive carrier
\(C=\sum_{n\ge2}H_n\), and write \(H/C=1+H_1/C\). All the strip and
curvature estimates apply to \(C\), and there is no omitted arithmetic
remainder at all. The unresolved first-mode cancellation remains.
Therefore adding primes, or merely reducing the fixed remainder tolerance,
cannot by itself be the mathematical mechanism for exclusion.

More precisely, for any positive smooth carrier \(A\) and \(h=H/A\),
away from the zeros of \(H\),
\[
 \left(\frac{h_x}{h}\right)^2-\frac{h_{xx}}h
 =\frac{\mathcal L_0}{H^2}+(\log A)_{xx}. \tag{1}
\]
At a stationary point this equals \(-H_{xx}/H+(\log A)_{xx}\).
Along the predecessor of a nondegenerate double event at time \(T\),
it is \(-1/(T-t)+O(1)\). Changing a carrier with bounded logarithmic
curvature only changes the bounded term. This is an identity and a scoped
limitation of carrier optimization, not an impossibility theorem for
quantitative modular arguments.

The proper planning scale is the published carrier
\(\Gamma_t(x)\asymp_T x^{7/4}\exp[-\pi x/8+(t/16)\log^2(x/(4\pi))]\).
This is a nonzero normalization, **not a lower bound on \(|H|\)**, which
vanishes at zeros. A separate positive margin for a normalized jet or
contour is essential. The precise carrier formula and derivative are in
[investigation 07, Note 02 §3](../../07_source_measurement_audit/notes/round-1/02_EXPLICIT_THETA_JET_AND_ENDPOINT_BOUNDS_CODEX_20261017.md).
Comparing the original source-tail error with this scale suggests
\(m^2\gtrsim x/8\), up to logarithmic factors; at \(x=6\,10^{12}\),
\(\sqrt{x/8}\approx8.66\,10^5\). This is a conditioning estimate, not a
complexity lower bound or a certified frontier.

## 2. A finite shifted-source approximation with exponential error

The source contour method is already present in
[07, Note 02 §1](../../07_source_measurement_audit/notes/round-1/02_EXPLICIT_THETA_JET_AND_ENDPOINT_BOUNDS_CODEX_20261017.md).
The new explicit item here is its finite-mode, complex-spectral-strip
derivative remainder. No novelty is claimed for contour shifting.

Choose \(0<d<\pi/8\), put \(c=\cos(4d)>0\), and let
\(w_t(v)=e^{tv^2}\Phi(v)\). The complete even source is holomorphic for
\(|\Im v|<\pi/8\); reflection supplies decay at both real infinities.
Shifting the entire Fourier contour and using
\(w_t(-u+id)=w_t(u-id)\) gives
\[
 H(t,z)=\frac{e^{-dz}}2\int_0^\infty
 \left[w_t(u+id)e^{izu}+w_t(u-id)e^{-izu}\right]du. \tag{2}
\]
The vanishing of the remote vertical sides follows from double-exponential
decay, uniformly on compact spectral sets. This identity holds for complex
\(z\). It uses full reflection **before** truncating any arithmetic sum.

Define \(\widetilde H_{m,d}\) by replacing \(\Phi\) in both terms on the
right of (2) with \(\sum_{1\le n<m}\phi_n\). It is an entire function of
\(z\), real on the real axis, and satisfies the same heat equation. It
need not be even in \(z\); no global all-real-zero model is asserted.

Fix \(0\le t\le T\), \(\Re z=x\ge0\), and \(|\Im z|\le Y\). Assume
\[
 b=4c\pi m^2-9-Y>0,\quad 8c\pi m^2\ge T,\quad
 r=\left(1+\frac1m\right)^4e^{-c\pi(2m+1)}<1.
\]
Set
\[
 S=\frac{(2\pi^2m^4+3\pi m^2)e^{-c\pi m^2}}{1-r},\qquad
 K_j=S\sum_{k=0}^j\binom jk\frac{d^{j-k}k!}{b^{k+1}}.
\]
Then, for every nonnegative integer \(j\),
\[
 \boxed{|\partial_z^j(H-\widetilde H_{m,d})(t,z)|\le K_je^{-dx}.} \tag{3}
\]

**Proof.** Put \(\lambda_n=\pi n^2\). On either shifted positive half-line,
\[
 |e^{t(u\pm id)^2}\phi_n(u\pm id)|
 \le(2\lambda_n^2+3\lambda_n)
       e^{Tu^2+9u-c\lambda_ne^{4u}}.
\]
The spectral exponential contributes at most \(e^{-dx+Yu}\), and a
spectral derivative contributes at most \((u+d)^j\). Using
\(e^{4u}\ge1+4u+8u^2\) absorbs the quadratic factor and leaves
\(e^{-c\lambda_n-(4c\lambda_n-9-Y)u}\). Expand \((u+d)^j\), integrate
its powers against this exponential, and replace the denominator by its
value at \(m\). The successive ratio of the remaining numerator is at
most \(r\), since its polynomial factor grows by at most
\(((n+1)/n)^4\). Summing a geometric series proves (3). The two halves
and the factor \(1/2\) cancel in the absolute bound.

For real \(x\), (2) also equals
\(\Re\int_0^\infty w_t(u+id)e^{ix(u+id)}du\). The otherwise missing
vertical segment is purely imaginary: \(w_t(iv)\) is real by evenness
and real symmetry. This observation explains why merely shifting each
uncompleted half-line mode would be wrong. A finite-prime orbit control
has a reflection defect; its vertical contribution cannot be discarded.

**A bounded check.** With \(d=\pi/16\), \(T=1/2\), \(Y=1\), and \(m=5\),
the conservative replacement \(c\ge7/10\) gives certified bounds
\[
 (K_0,K_1,K_2)<(8\,10^{-23},\ 1.61\,10^{-23},\ 3.23\,10^{-24}). \tag{4}
\]
The [record](../numerics/STRIP_CARRIER_CHECKS_20261018.json) gives exact
rational enclosures. Four shifted modes are retained. These certify the
tail formula, not numerical integration of those modes, a nonzero jet,
or a zero count. Finite integration endpoints and quadrature errors must
be added in an actual consumer.

## 3. What would make this a collision result

On a compact region \(D=[\tau,T]\times[0,X]\), define the approximating
real jet \(v=(\widetilde H_{m,d},\partial_x\widetilde H_{m,d})\).
If interval analysis proves throughout every cell of \(D\) that
\[
 \|v(t,x)\|_2>
 e^{-dx}\sqrt{K_0^2+K_1^2}+\epsilon_{\rm eval}(t,x), \tag{5}
\]
where \(\epsilon_{\rm eval}\) includes all quadrature, rounding, and
whole-cell errors, then \(H\) and \(H_x\) have no common real zero on
\(D\). Dividing both sides by an explicitly positive carrier changes
conditioning, not validity. A certified boundary comparison plus an exact
zero count is another consumer; a conjugation-symmetric cell containing
exactly one zero contains a real simple zero.

Equation (5) is a finite certificate specification, not a new analytic
lower bound and not evidence until its margin is certified. The first
benchmark should compare the direct complete-source method, the original
real packets, and (2) on **one identical box**, recording the minimum
normalized margin, total error, precision and cost. A box already covered
by published results tests machinery only. Require an actual efficiency
gain or new coverage before expanding the campaign.

The fixed shift does not solve the asymptotic problem. Relative to
\(\Gamma_t\), its error contains
\(\exp[(\pi/8-d)x+O_T(\log^2x)]e^{-c\pi m^2}\).
Ignoring logarithmic factors, balancing exponents requires
\[
 m^2\gtrsim\frac{\pi/8-d}{\pi\cos(4d)}x.
\]
For \(d=\pi/16\) this coefficient is \(\sqrt2/16\), versus \(1/8\)
for the crude unshifted comparison. As \(d\uparrow\pi/8\), the ratio
tends to \(1/(4\pi)\), while absolute constants and quadrature become
harder. This suggests a connection to the usual Riemann–Siegel length,
not a proof that this method beats it. A saddle-adapted contour or a
complete modular/dual expansion may improve conditioning, but its full
error and first derivatives must be proved before making that claim.

There is a concrete asymptotic refinement of (3). Choose constants
\(a_*>0\), \(b_*>1/(4\pi)\), and, for large \(x\),
\[
 d(x)=\pi/8-a_*\log x/x,\qquad m(x)=\lceil\sqrt{b_*x}\rceil.
\]
Let E_j(x) denote the right side of (3) with these parameters.
For each fixed derivative order and bounded \(T,Y\), (3) implies
\[
 E_j(x)=O\!\left(e^{-\pi x/8}
 \frac{x^{5/2+a_*(1-4\pi b_*)}}{(\log x)^2}\right). \tag{6}
\]
Indeed, \(c\sim4a_*\log x/x\), the rate \(b\sim16a_*\pi b_*\log x\),
\(1-r\sim8a_*\pi\sqrt{b_*}\log x/\sqrt x\), and
\(e^{-c\pi m^2}=x^{-4\pi a_*b_*}(1+o(1))\). The polynomial source
factor is \(O(x^2)\), while \(e^{-d(x)x}=e^{-\pi x/8}x^{a_*}\), giving
(6). All admissibility conditions hold eventually.
Relative to the **time-zero gamma envelope** \(x^{7/4}e^{-\pi x/8}\),
this error tends to zero if \(a_*(4\pi b_*-1)>3/4\).
For example \(a_*=4,b_*=1/10\) gives exponent
\(19/4-8\pi/5<-0.2765\) in that relative error, with \(m=O(\sqrt x)\).
This is an asymptotic tail estimate with unevaluated onset and constants;
it does not certify the cost or conditioning of evaluating the retained
modes. The derivative in (3) is taken with \(m,d\) fixed, selected at the
observation point or frozen for a cell. It is not the derivative of a
piecewise formula in which the cutoff and contour are varied with \(x\).
Most importantly, a small error relative to a gamma envelope is not a
lower bound for the complete oscillatory field or its jet.

The strongest analytic target is therefore a **strict lower bound for a
complete, physical-scale jet or complex boundary expression**, derived
after this modular completion. Seek the first positive margin on a fixed
time slab. Universal lower curvature or noncollision at every positive
time would be an RH-equivalent target, not an intermediate milestone.

## 4. Two complete routes from a finite gain to a bound on Lambda

The normalization is exactly [Polymath's](https://arxiv.org/html/1904.12438v2):
\(H_0(z)=\xi((1+iz)/2)/8\). [Platt–Trudgian, §3.4 and Corollary 2](https://arxiv.org/pdf/2004.09765)
give the published baseline \(\Lambda\le0.2\). Later claimed bounds have
different review and input statuses; no current-record claim is made here.

**Route A: continue below a known all-real time.** For a chosen
\(0<\tau<0.2\), prove no joint real zero on
\((\tau,0.2]\times\mathbb R\). The positive-threshold finite-collision
theorem then gives \(\Lambda\le\tau\). A compact certificate must be
joined to an explicit outer exclusion uniform in time on this slab.
An existential "sufficiently large" cutoff at each time, disconnected
windows, or a forecast from an asymptotic threshold does not close the
bridge. The repository already has this reduction; it is not a new result.

**Route B: use the published complex barrier contract.**
[Polymath, Theorem 1.2](https://arxiv.org/html/1904.12438v2#S1.Thmtheorem2)
gives \(\Lambda\le t_0+y_0^2/2\), subject to all three inputs: initial
zeta verification, final-time exterior nonvanishing, and a barrier valid
at every intermediate time. In its notation the exterior is
\[
 x\ge X+\sqrt{1-y_0^2},\quad y_0\le y\le\sqrt{1-2t_0},
\]
and the barrier is
\[
 X\le x\le X+\sqrt{1-y_0^2},\quad
 \sqrt{y_0^2+2(t_0-t)}\le y\le\sqrt{1-2t},\quad0\le t\le t_0.
\]
The initial input excludes zeta zeros for
\((1+y_0)/2\le\sigma\le1\), \(0\le\Im s\le X/2\).
All parameter restrictions of the source theorem remain in force.
The new zero-free carrier fits these complex regions, but does not
establish their theta nonvanishing. A real-axis packet theorem alone
cannot replace them. The
[existing audit](../../../investigations-2/newman_certificate_audit/README.md)
of [Gomila's package](https://github.com/judegomila/dbn-lambda-01787854-candidate-audit)
is the appropriate comparison if this consumer is chosen; its uncompleted
producer audit must not be silently promoted to a verified input.

At fixed \(y_0\), a certified decrease \(\Delta t_0\) decreases the bound
by that amount. At fixed \(t_0\), decreasing \(y_0\) by \(\Delta y\)
decreases it by \(y_0\Delta y-(\Delta y)^2/2\). These are budgeting
identities, not earned improvements. Choose parameters only after the
minimum complete margin and all coverage obligations are measured.

## 5. Controls and the next decision

| Control | Why it does not license the proposed theta conclusion |
| --- | --- |
| Finite-prime orbit and weighted-square controls | They pass higher-packet positivity and the new logarithmic bounds. They fail complete normalized analytic source reflection; using (2) without their defect term is invalid. |
| Reflected super-Gaussian and smooth positive-primitive controls | They may satisfy reflection and contour identities on their own analytic domains. They lack the exact theta square expansion and its stated finite-tail constants. Reflection by itself is not excluding. |
| Euler-factor controls \(\Phi_{c,p}\) | They preserve evenness but alter the normalized source data. Reusing theta mode coefficients or theta-specific margins is invalid; a domain containing a certified witness must fail any sound exclusion certificate. |
| Earlier \(q\) and \(q_{T,a}\) counter-kernels | Positive even heat sources can collide; they do not supply the exact theta square-source expansion used in (3). |
| Smooth-density and two-channel controls | Positive auxiliary forms do not imply a complete signed theta estimate. They fail the specified exact-source/quantitative premises, not general heat or positivity identities. |

These are analytic premise checks against the linked catalogue, not new
numerical replays. A control can pass a certificate on a box avoiding its
collision; rejection is required when the tested conclusion contradicts
its actual witness. On a collision box the true jet margin in (5) is zero.

**Recommended next work:** implement (2)–(5) on one bounded box and
compare it with the existing complete-source certificate at identical
tolerance. If it gains precision or a certified margin, pursue a slab
with an explicit outer consumer. In parallel, investigate whether the
modular completion yields a signed estimate rather than only a smaller
absolute error. Do not begin a large height scan, more prime-list
optimization, or another all-event criterion before that comparison.
This keeps the next milestone numerical and falsifiable, while leaving
the stronger analytic route open.
