# EMA smoothing, positivity, and continuation

20 September 2026. Prepared for Edward Baker for the next research session.

**Model:** OpenAI GPT-6 (Codex).  
**Reasoning effort:** not exposed to the assistant in this session; not inferred.  
**Origin:** Baker suggested an exponential moving average with a smoothing
length that adapts along the evolution, drawing on time-series analysis.
He explicitly requested consideration of multiple interpretations.  
**Status:** analytical evaluation and continuation plan, with 57 finite
diagnostics. The statements below are written derivations, not independently
reviewed proofs. No arithmetic contraction certificate, physical Wilson
realization, localization theorem, or all-depth path is constructed.

## 1. Assessment and recommended next experiment

The suggestion is useful in four distinct ways:

1. The parent Loewner investigation already expresses the full arithmetic
   kernel as a positive kernel minus twice an EMA. That internal EMA's
   rate is fixed by the arithmetic cancellation, not an adjustable control.
2. A causal EMA supplies the concentrating identity limit that the regular
   Wilson readout lacked. Its exact energy balance also tells us how much
   positivity the filter itself contributes.
3. An EMA can be used as an auxiliary mathematical regularization. A
   specific vanishing-smoothing condition preserves the central Weil limit,
   even though the filtered finite-shift operator differs from the target.
4. The gamma generator has an exact representation as a weighted
   sum of input-minus-EMA terms at many relaxation lengths. This connects
   the time-series intuition directly to an existing arithmetic structure.

An EMA is therefore worth testing, but “choose enough smoothing to get a
positive matrix” is not an adequate stopping condition. A large filter
can make an expanding operator contractive. We must either keep the
original norm comparison, or prove that the extra norm loss disappears
at the scale relevant to the Weil limit.

The recommended first experiment is a fixed-window comparison of:

- an output EMA \(S_{\ell,L}V_{\omega,L}\), with the added filter loss
  explicitly recorded and schedules \(\ell=\omega^q,\ q>1/2\);
- an EMA along the shift family, with a shrinking history and the correct
  average-shift normalization;
- the original transfer and an input-smoothed congruence as controls.

Only after that comparison should an adaptive smoothing rule be used in
the spatial Schur step. Sections 10–12 give the specific continuation
task and decision criteria.

## 2. Current project state and the meaning of positivity

The starting manuscript pair is Wilson–Loewner version 0.4:

- [Main manuscript, Section 5 source](../../wilson-loewner/sections/05_fixed_window.tex).
- [SI S10: fixed-window response](../../wilson-loewner/sections/s_fixed_window.tex).
- [SI S11: localization](../../wilson-loewner/sections/s_localization.tex).
- [SI S9: cumulative and joint gluing](../../wilson-loewner/sections/s_continuation.tex).
- [Earlier continuation agenda](../../wilson-loewner/notes/RESEARCH_CONTINUATION_20260920.md).

The arithmetic transfer \(V_{\omega,L}\) is a causal convolution
compressed to an interval, with strong initial value \(V_{0,L}=I\).
On the smooth core,

\[
\partial_\omega V_{\omega,L}=-G_{\omega,L}V_{\omega,L},\qquad
D_{\omega,L}=I-V_{\omega,L}^*V_{\omega,L},
\]
\[
Q_{0,L}[f]=\lim_{\omega\downarrow0}
\frac{\langle f,D_{\omega,L}f\rangle}{2\omega}.
\tag{2.1}
\]

The relevant positivity means \(D_{\omega,L}\succeq0\) on **all inputs**,
or positivity of a justified limiting form. It does not mean that the
kernel is pointwise nonnegative. A scalar trace, one signal, or one
positive finite compression does not establish this operator inequality.

The new Wilson calculation excluded one regular identity-plus-integral
response: its bounded first derivative cannot reproduce the logarithmically
unbounded arithmetic generator, and its persistent identity channel cannot
equal the compact positive-shift arithmetic transfer. It did not exclude
singularly concentrating response kernels. The auxiliary localization
product matches the prime-free factor algebraically; its physical origin
and positive cumulative norm remain open.

We use the translated interval \((0,L)\) below. The smoothing length
\(\ell\), the arithmetic shift \(\omega\), the support length \(L\), and
Loewner capacity are different parameters.

### 2.1 The inherited arithmetic EMA must not be confused with a new filter

The [parent decomposition](../../loewner/sections/03_decomposition.tex),
including its one-all-pass-section identity and discussion of growth,
already gives, for \(0<\omega\le1/2\),
\[
k_\omega=\widehat k_\omega
-2\,\mathrm{EMA}_{b}[\widehat k_\omega],\qquad
\widehat k_\omega\ge0,\qquad b=\tfrac12+\omega,
\tag{2.2}
\]
where
\[
\mathrm{EMA}_b[g](x)=b\int_0^x e^{-b(x-y)}g(y)\,dy.
\]
In length notation this is \(S_{1/b}\), and the corresponding factor
has symbol \(B_b(p)=(p-b)/(p+b)\). The representation is inherited;
it is not a new result of this session.

The cancellation fixes the rate. For a growing exponential,
\[
(I-2S_{1/c})e^{bx}
=\frac{b-c}{b+c}e^{bx}+\frac{2c}{b+c}e^{-cx}.
\tag{2.3}
\]
The growing term disappears precisely when \(c=b\). An arbitrary
adaptive replacement of \(b\), while keeping \(\widehat k_\omega\)
fixed, therefore changes the target and generally spoils this
cancellation. Nor is positivity of \(\widehat k_\omega\) a norm bound.

The all-pass section itself has an elementary boundary-storage identity.
If \(h=S_{1/b,L}f\), then \(f=h+b^{-1}h'\) and
\((I-2S_{1/b,L})f=b^{-1}h'-h\), whence
\[
\|f\|^2-\|(I-2S_{1/b,L})f\|^2
=\frac2b|h(L)|^2.
\tag{2.4}
\]
Applying it to the preceding positive-kernel factor explains how an
endpoint contribution can compensate its expansion. It does not prove
that the compensation is sufficient. This is consistent with the
parent endpoint-flux discussion.

The built-in length \(1/b\) does not tend to zero at zero shift:
the identity limit belongs to the complete product of factors.
The vanishing-length condition derived below concerns an **additional**
output smoother, not a requirement imposed on this internal EMA.

## 3. Boundary EMA: definition, energy, and the identity limit

For \(\ell>0\), define the zero-history causal EMA by

\[
(S_{\ell,L}f)(x)=\frac1\ell\int_0^x
e^{-(x-y)/\ell}f(y)\,dy.
\tag{3.1}
\]

Writing \(h=S_{\ell,L}f\), this is precisely

\[
\ell h'(x)+h(x)=f(x),\qquad h(0)=0.
\tag{3.2}
\]

It is the continuous exponential-filter analogue of the usual discrete
EMA recursion. The time-series reference is
[NIST, Single Exponential Smoothing](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc431.htm);
the operator and energy calculations here are derived directly.
We do not divide by \(1-e^{-x/\ell}\) to enforce constant preservation
at the left endpoint: that would be a different operator with a different
norm balance.

Let \(\mathsf A h=h'\) with domain
\(\{h\in H^1(0,L):h(0)=0\}\). Then
\(S_{\ell,L}=(I+\ell\mathsf A)^{-1}\). Squaring
\(f=h+\ell h'\) and integrating the cross term gives the exact identity

\[
\boxed{\ \|f\|^2-\|S_{\ell,L}f\|^2
=\ell^2\|(S_{\ell,L}f)'\|^2
 \ell |(S_{\ell,L}f)(L)|^2.\ }
\tag{3.3}
\]

It holds for complex \(L^2\) inputs as well as real signals. In particular
\(S_{\ell,L}\) is a contraction. Its own independent storage map is
\[
f\longmapsto
\bigl(\ell(S_{\ell,L}f)',\sqrt{\ell}\,(S_{\ell,L}f)(L)\bigr)
\in L^2(0,L)\oplus\mathbb C.
\tag{3.4}
\]
This is the filter's storage, not the arithmetic storage sought in the
Wilson construction.

The EMA is compact for every \(\ell>0\) and tends strongly to \(I\) as
\(\ell\downarrow0\). It cannot converge in operator norm. Thus it has
exactly the qualitative identity-limit behavior that escaped the
identity-plus-compact obstruction. This observation alone does not match
the arithmetic generator.

Increasing the smoothing length decreases every output norm. If
\(\ell_2\ge\ell_1>0\) and \(a=\ell_1/\ell_2\), the resolvent identity gives
\[
S_{\ell_2}=\bigl[aI+(1-a)S_{\ell_2}\bigr]S_{\ell_1}.
\tag{3.5}
\]
The bracket is a contraction, so
\(\|S_{\ell_2}g\|\le\|S_{\ell_1}g\|\).
This supplies a legitimate monotonic parameter for a fixed-window
search. It does not establish monotonicity in arithmetic shift.

## 4. Where the EMA is applied changes the question

### 4.1 Output smoothing adds a known positive defect

Define
\[
W_{\omega,L,\ell}=S_{\ell,L}V_{\omega,L}.
\]
Both factors are causal convolutions, so they commute on this fixed
interval. No commutation with their adjoints is asserted. Exactly,
\[
\boxed{\ I-W^*W
=D_{\omega,L}
V_{\omega,L}^*(I-S_{\ell,L}^*S_{\ell,L})V_{\omega,L}.\ }
\tag{4.1}
\]

The second summand is positive. A positive filtered defect can therefore
hide a negative arithmetic defect.
Indeed Young's bound gives
\(\|S_{\ell,L}\|\le1-e^{-L/\ell}\), which tends to zero as
\(\ell\to\infty\). At any fixed \(L,\omega\), sufficiently broad smoothing
can make \(S_{\ell,L}V_{\omega,L}\) contractive regardless of whether
\(V_{\omega,L}\) is contractive.

At fixed positive \(\omega\), if filtered contraction is established
along a sequence \(\ell\downarrow0\), strong convergence recovers
contraction of \(V_{\omega,L}\). A simultaneous zero-shift limit needs
the sharper scale estimate in Section 5.

### 4.2 Smoothing the test input on both sides preserves positivity

Instead compare
\[
\|S_{\ell,L}f\|^2-\|V_{\omega,L}S_{\ell,L}f\|^2
=\langle f,S_{\ell,L}^*D_{\omega,L}S_{\ell,L}f\rangle.
\tag{4.2}
\]
The range of \(S_{\ell,L}\) is \(H^1\) with zero left trace, which is
dense in \(L^2(0,L)\). Since \(D_{\omega,L}\) is bounded for fixed
positive shift,
\[
S_{\ell,L}^*D_{\omega,L}S_{\ell,L}\succeq0
\quad\Longleftrightarrow\quad D_{\omega,L}\succeq0.
\tag{4.3}
\]
The proof is positivity on a dense range followed by continuity.
There is no bounded inverse of this compact smoother. In particular,
positivity on finitely many smoothed test functions does not establish
(4.3) on all inputs.

This version is attractive as a change of test basis or numerical
preconditioner. It preserves the original question rather than supplying
new positivity. For the unbounded central form one would additionally
need approximation in its form norm; the bounded-defect argument above
does not silently establish that stronger assertion.

### 4.3 An adaptive rule must remain independent of the input

A length selected from an operator bound at \((L,\omega)\) is permissible.
Selecting a different length for each individual signal generally makes
the procedure nonlinear and does not yield the single linear contraction
required by the program.

If the length changes along boundary position itself, the norm identity
also changes. For \(f=h+\ell(x)h'\), \(h(0)=0\), and a smooth positive
\(\ell(x)\),
\[
\|f\|^2-\|h\|^2
=\int_0^L\ell(x)^2|h'|^2dx
-\int_0^L\ell'(x)|h|^2dx+\ell(L)|h(L)|^2.
\tag{4.4}
\]
Thus a variable-length filter is not automatically contractive merely
because every constant-length filter is. Nonincreasing \(\ell(x)\)
is one sufficient condition in this convention. This issue is distinct
from selecting a spatially constant \(\ell=\ell(L,\omega)\) at each
continuation step.

## 5. A sufficient smoothing-removal condition for the Weil limit

Fix \(L\) and \(f\in C_c^\infty(0,L)\). Write \(g_\omega=V_{\omega,L}f\).
The project's shift-kernel bounds give
\[
g_\omega(0)=0,\qquad
\|g_\omega-f\|_{H^1(0,L)}=O_f(\omega).
\tag{5.1}
\]
For completeness, apply the established right-Laplace-line bounds for
\(\partial_\omega K_\omega\) to the rapidly decaying transform of the
zero extension of \(f\), with one derivative in \(x\). The logarithmic
growth is integrable against this transform, uniformly for small
nonnegative shift. Integrating in shift proves (5.1). Causality gives
the left trace; the right trace is \(g_\omega(L)=O_f(\omega)\) because
\(f(L)=0\).

For any \(g\in H^1(0,L)\) with \(g(0)=0\), put \(h=S_\ell g\).
Then \(h'=S_\ell g'\), and
\[
h(L)=g(L)-\ell(S_\ell g')(L),\qquad
|\ell(S_\ell g')(L)|\le\sqrt{\ell/2}\,\|g'\|.
\]
Using (3.3) yields
\[
0\le \|g\|^2-\|S_\ell g\|^2
\le2\ell^2\|g'\|^2+2\ell|g(L)|^2.
\tag{5.2}
\]
Consequently the additional filter loss on the evolved smooth input is
\[
0\le E_{\omega,\ell}[f]
:=\|V_{\omega,L}f\|^2-\|S_\ell V_{\omega,L}f\|^2
\le C_{f,L}(\ell^2+\ell\omega^2).
\tag{5.3}
\]

**Sufficient central-limit condition.** If
\[
\boxed{\ \ell(\omega)^2/\omega\longrightarrow0,\ }
\tag{5.4}
\]
then
\[
\lim_{\omega\downarrow0}
\frac{\|f\|^2-\|S_{\ell(\omega),L}V_{\omega,L}f\|^2}{2\omega}
=Q_{0,L}[f].
\tag{5.5}
\]
This follows from (2.1), (4.1), and (5.3). It is a fixed-test result;
no operator-norm approximation to the unbounded central form is used.
It is sufficient, not claimed to be the sharp necessary condition
for every possible test or filter.

**Conditional all-depth route.** Suppose
\[
L_j\to\infty,\quad \omega_j\downarrow0,\quad
\ell_j^2/\omega_j\to0,\quad
\|S_{\ell_j,L_j}V_{\omega_j,L_j}\|\le1
\quad\text{on every input}.
\tag{5.6}
\]
Then central Weil positivity, and hence RH, follow by the existing
compact-support criterion. To prove this, fix a smaller interval and
one smooth input, extend it by zero into the larger interval, and
restrict the filtered output back to the smaller interval. Both
convolutions are causal with zero history, so this restriction is the
same fixed-window filtered operator. Apply (5.5). The constants in
(5.3) belong to the fixed test and fixed smaller interval; they need
not be uniform in \(L_j\).

Thus auxiliary smoothing can legitimately enlarge the construction
problem from \((L,\omega)\) to \((L,\omega,\ell)\). The difficult new
obligation is to maintain contraction while removing smoothing at
the rate (5.4). No such arithmetic schedule is established here.

There are two different accuracy thresholds:

- \(\ell=o(\sqrt{\omega})\) suffices for the **real quadratic-form
  limit** just proved.
- \(\ell=o(\omega)\) suffices to leave the **full first operator
  variation** unchanged on smooth tests, since
  \(S_\ell f=f-\ell f'+o(\ell)\).

For example \(\ell=c\omega\) preserves (5.5) but adds
\(-c\,\partial_x\) to the first response. Its real pairing with an
interior compactly supported test vanishes. It is therefore suitable
for a possible auxiliary positivity route but does not by itself
preserve the proposed physical transfer identity.

### 5.1 Why mere vanishing of the smoothing length is insufficient

Consider the explicitly nonarithmetic control
\(V_\omega^{\rm toy}=e^\omega I\) on \((0,L)\).
Its central form is \(-\|f\|^2\), so it expands every nonzero input.
For \(h(0)=0\), the fundamental theorem of calculus gives
\(\|h\|^2\le(L^2/2)\|h'\|^2\). Applying this to (3.3),
\[
\|S_{\ell,L}\|^2\le\frac1{1+2\ell^2/L^2}.
\tag{5.7}
\]
Choose \(\ell=2L\sqrt{\omega}\). Then
\[
\|S_{\ell,L}V_\omega^{\rm toy}\|^2
\le \frac{e^{2\omega}}{1+8\omega}<1
\qquad(0<\omega\le0.1).
\tag{5.8}
\]
The last inequality follows, for instance, from
\(e^{2\omega}-1\le2e^{0.2}\omega<8\omega\).
For fixed \(L\), this is an all-input filtered contraction with
\(\ell\to0\) despite negative central form.

One can even take \(L_j=j,\ \omega_j=j^{-4},\
\ell_j=2/j\) for \(j\ge2\). Both the shift and length of smoothing
vanish and the physical interval grows, but
\(\ell_j^2/\omega_j=4j^2\), violating (5.4).
This counterexample explains the need to track the *relative* scale.
It is a control on an invalid inference, not a counterexample to
arithmetic positivity.

For the simple test \(f=x(1-x)\) at \(L=1\), the filtered defect
divided by \(2\omega\) tends to \(19/30>0\) when
\(\ell=2\sqrt{\omega}\), whereas the original value is \(-1/30\).
With \(\ell=\omega^{3/4}\), it tends back to \(-1/30\).
The diagnostic record checks these two limits.

## 6. Adaptive smoothing contributes its own generator

At fixed \(L\), for a differentiable positive \(\ell(\omega)\), scalar
causal convolution and the resolvent derivative give
\[
\partial_\omega W_{\omega,L,\ell(\omega)}
=-\left[G_{\omega,L}
+\ell'(\omega)\mathsf A S_{\ell,L}\right]W_{\omega,L,\ell(\omega)},
\tag{6.1}
\]
\[
\ell'\mathsf A S_\ell
=\frac{\ell'}{\ell}(I-S_\ell).
\tag{6.2}
\]
The identities hold on the admissible core and at positive lengths.
Since \(S_\ell\) is a contraction, \(I-S_\ell\) is accretive.
Increasing the filter length with increasing shift therefore adds an
accretive term. Decreasing it gives the opposite sign. At a general
path parameter \(t\), the arithmetic term is
\(\dot\omega(t)G_\omega\) and the filter term is
\(\dot\ell(t)\mathsf A S_\ell\).

This is a potential control mechanism, but it also makes explicit
what has changed in the evolution. When length \(L\) grows, there
is an additional spatial gluing problem; (6.1) is a fixed-space
identity and does not replace it. Demanding positivity of its full
instantaneous generator would again be stronger than cumulative
contraction.

Appending a single EMA does not repair the excluded Gaussian readout.
For \(\mathcal V_\omega=I+\omega J+o(\omega)\) in norm with \(J\)
bounded, multiplication by \(S_{\ell(\omega)}\) has first variation
\(J-c\partial_x\) if \(\ell/\omega\to c<\infty\).
Its real pairing on compactly supported modulations remains bounded,
so it cannot match the logarithmic arithmetic growth. If
\(\ell/\omega\to\infty\), the first vector derivative diverges on
a test with \(f'\ne0\). More generally, existence of a finite first
derivative forces bounded \(\ell/\omega\), and each convergent
subsequence has the same obstruction. This is scoped to a single
EMA appended to that regular readout.

## 7. The gamma generator is already a multiscale EMA expression

Let \(a_n=2n+\tfrac12\). From the subtracted exponential tower,
\[
2\int_0^\infty e^{-a_nu}(I-T_u)\,du
=\frac2{a_n}(I-S_{1/a_n,L}).
\tag{7.1}
\]
The identity includes the tail beyond the left endpoint because
\(T_u\) uses zero-extended input. On the smooth core it gives
\[
G_{\Gamma,0,L}
=w_0 I+\sum_{n=0}^\infty\frac2{a_n}
(I-S_{1/a_n,L}).
\tag{7.2}
\]
The series converges there:
\(\|(I-S_{1/a_n})f\|\le a_n^{-1}\|f'\|\), and
\(\sum_n a_n^{-2}<\infty\).
The increasing number of active scales explains how the aggregate
can have an unbounded logarithmic generator even though each
individual EMA term is bounded.

After the lowest-mode/pole cancellation from SI S10, the *complete*
prime-free generator on \(L<\log2\) is
\[
\boxed{\ G_{0,L}
=(w_0+4)I+
\sum_{n=1}^\infty\frac2{a_n}(I-S_{1/a_n,L})
+2R_{-1/2,L},\ }
\tag{7.3}
\]
\[
(R_{-1/2,L}f)(x)=\int_0^x e^{(x-y)/2}f(y)\,dy.
\]
Each term \(I-S\) in the sum has a nonnegative real quadratic form.
The negative local constant \(w_0+4\), the remaining growing
exponential, and, on larger windows, the signed prime delays are
still present. They cannot be dropped or absorbed into arbitrary
filter choices. In particular (7.3) is not a positive factorization
of the full generator.

This is the most direct structural connection to the EMA suggestion.
The internal states \(h_n=S_{1/a_n}f\) satisfy elementary relaxation
equations
\[
a_n^{-1}h_n'+h_n=f,\qquad h_n(0)=0.
\]
It suggests a state-space interpretation of the gamma sector and a
multiscale numerical representation. It does not derive these states
from Wilson fields or a supersymmetry charge. The gamma/digamma
normalization is the one already used in the manuscript; see
[DLMF, §5.9](https://dlmf.nist.gov/5.9) for the standard integral
representations.

The auxiliary localization product remains relevant: a physical
construction would need to select these modes and account for the
removed mode and remaining signed contribution. EMA relaxation gives
another representation to test against that construction, not a
replacement for the localization calculation.

## 8. EMA along the shift path: a different viable interpretation

At fixed \(L\), average the family of operators rather than their
boundary coordinate. For example,
\[
\tau(\omega)\,\partial_\omega\overline V_\omega
+\overline V_\omega=V_\omega,\qquad
\overline V_0=I.
\tag{8.1}
\]
This corresponds to averaging successive outputs for the same input.
A common schedule must again apply to all inputs.

For a constant \(\tau>0\), the solution is
\[
\overline V_\omega=e^{-\omega/\tau}I+
\frac1\tau\int_0^\omega e^{-(\omega-s)/\tau}V_s\,ds.
\tag{8.2}
\]
It retains a nonzero identity channel at positive shift. Since the
remaining integral is compact (truncate away from zero, then use
local uniform boundedness for the small omitted interval), it cannot
equal the compact arithmetic \(V_\omega\). Its first shift derivative
at zero is also zero. These facts exclude exact transfer matching
with the same shift; they do not exclude an auxiliary positivity
argument with the correct normalization.

The general useful statement is simple. Let \(\mu_\omega\) be a
probability measure on \([0,\omega]\), possibly with mass at zero,
and define
\[
\overline V_{\omega,L}=\int V_{s,L}\,d\mu_\omega(s),\qquad
m_\omega=\int s\,d\mu_\omega(s)>0.
\tag{8.3}
\]
For each fixed smooth test, \(V_sf=f-sG_0f+o(s)\), uniformly in the
relative remainder for \(0<s\le\omega\). Integration therefore yields
\[
\overline V_\omega f=f-m_\omega G_0f+o(m_\omega),\qquad
\boxed{\ \lim_{\omega\downarrow0}
\frac{\|f\|^2-\|\overline V_\omega f\|^2}{2m_\omega}
=Q_{0,L}[f].\ }
\tag{8.4}
\]
Thus all-input contraction of these averaged operators along
\(L_j\to\infty,\ \omega_j\downarrow0\) would also suffice for RH,
by the same causal restriction argument. No lower bound on
\(m_\omega/\omega\) is needed analytically. Very small \(m_\omega\)
can, however, make numerical errors more difficult to control.
For a common construction across intervals, use the same averaging
measure when restricting a larger interval to a smaller one.

For (8.2),
\[
m_\omega=\omega-\tau(1-e^{-\omega/\tau})
\sim\omega^2/(2\tau).
\tag{8.5}
\]
Dividing its defect by \(2\omega\) would lose the first-order signal;
dividing by \(2m_\omega\) recovers it.
If \(\tau(\omega)=c\omega,\ c>0\), the bounded solution initialized
by continuity is instead
\[
\overline V_\omega=\frac1c\,\omega^{-1/c}
\int_0^\omega s^{1/c-1}V_s\,ds,\qquad
m_\omega=\frac{\omega}{1+c}.
\tag{8.6}
\]
It has no surviving atom at \(s=0\), and its first derivative is
\(-G_0/(1+c)\). A change of clock accounts for this first derivative,
but not automatically the entire finite-shift transfer.

There is also a distinction between averaging the operators and
averaging their defects. For a probability average,
\[
\begin{aligned}
\|f\|^2-\|\overline V f\|^2
={}&\int\langle f,D_s f\rangle\,d\mu(s)\\
&+\int\|(V_s-\overline V)f\|^2\,d\mu(s).
\end{aligned}
\tag{8.7}
\]
The additional term is the variance of the outputs and is positive.
On shrinking histories it is \(O_f(\int s^2d\mu)\), which is
at most \(O_f(\omega m_\omega)\), so it vanishes at the scale in
(8.4). Averaging the defects directly has the same central limit
without that variance term. Neither operation guarantees positivity
for an arbitrary expanding family.

A chronological EMA on a path that starts at shift \(1/2\) and later
decreases is not automatically covered by this result. It remembers
older, larger shifts. One must show that this old history becomes
negligible relative to the effective first moment, or explicitly
use histories whose shifts all tend to zero. Also, averages across
different interval lengths require zero-extension/restriction maps;
they cannot be treated as operators on one fixed space without
specifying those identifications.

## 9. The EMA memory must be carried across a spatial join

For a constant \(\ell\), split \((0,L+h)\) into the old and new
intervals. The EMA has the block form
\[
S_{\ell,L+h}=
\begin{pmatrix}A&0\\B&C\end{pmatrix},\qquad
A=S_{\ell,L},\quad C=S_{\ell,h},
\]
\[
(Bf)(z)=e^{-z/\ell}(S_{\ell,L}f)(L),\qquad 0<z<h.
\tag{9.1}
\]
The carried EMA state gives a rank-one cross block. It is bounded:
\[
\|B\|=\tfrac12
\sqrt{(1-e^{-2L/\ell})(1-e^{-2h/\ell})}.
\]
For \(V=\left(\begin{smallmatrix}X&0\\Y&Z\end{smallmatrix}\right)\),
\[
SV=\begin{pmatrix}AX&0\\BX+CY&CZ\end{pmatrix}.
\tag{9.2}
\]
Resetting the filter to zero on every new slab would omit \(BX\)
and change the global filtered operator.

Under strict contraction of the diagonal filtered blocks, the exact
Schur criterion applies with
\[
\widetilde E=I-(AX)^*(AX),\qquad
\widetilde F_{\rm out}=I-(CZ)(CZ)^*,
\]
\[
\boxed{\ \|\widetilde F_{\rm out}^{-1/2}
(BX+CY)\widetilde E^{-1/2}\|\le1.\ }
\tag{9.3}
\]
The new-slab defect is still the **output** defect. If \(\ell\)
changes between continuation steps, the old filtered block changes
too. Its change must be included with the signed shift changes.
The rank-one memory simplifies bookkeeping, but supplies no bound
on the arithmetic cross block \(Y\).

## 10. What to prioritize, and what would count as progress

| Interpretation | Potential benefit | Essential condition or limitation |
|---|---|---|
| Existing internal EMA correction | Exact pole cancellation and boundary storage in the inherited factorization | Its rate is \(b=1/2+\omega\); changing it independently changes the arithmetic target |
| EMA on boundary output | An adjustable contraction margin and a concentrating identity limit | Track filter storage; prove removal at \(\ell^2=o(\omega)\) for the Weil limit |
| EMA on inputs, with both norms compared | Smoother test basis without changing bounded-defect positivity | Dense-range/all-input argument; finite matrices still need complement bounds |
| EMA along the shift family | Average difficult directions and permit an effective clock | Shrinking history, correct first-moment normalization, complete output norms |
| EMA of cumulative defects | Average storage directly without output-variance contribution | Positivity of the average is a new all-input claim; history must vanish appropriately |
| Multiple EMA states in the generator | Exact representation of the gamma difference and its logarithmic growth | Preserve the fixed local term, residual pole and prime delays; physical origin remains open |

The next experiment should ask whether smoothing improves the estimates
*within a removal regime that preserves the target*. Otherwise the
filter may simply be absorbing the difficulty.

For the boundary-output variant, examine \(\ell=\omega^{3/4}\) and
\(\ell=c\omega\) as valid central-limit schedules, with
\(\ell=c\sqrt{\omega}\) as a deliberately contaminating control.
If exact Wilson first-variation matching is the objective, also use
\(\ell=\omega^{5/4}\). These are test families, not claimed successful
arithmetic schedules or preferred optimal exponents.

At fixed \((L,\omega)\), monotonicity (3.5) permits an exploratory search
for the smallest useful \(\ell\). A certified upper bound on that
threshold is more useful than a fitted matrix threshold. Track
\(\ell^2/\omega\), the norm margin, the unresolved complement, and the
added filter loss together. A threshold that stays too large as
\(\omega\) decreases would identify a concrete obstacle.

For the path-average variant, compare (8.6) for a small set of \(c\)
values against the original transfer and against the averaged defect.
Report the normalization \(m_\omega\) and the variance term separately.
The noncommuting products arising in the norm must be retained.

## 11. Concrete next-session work plan

1. **Audit these analytical reductions first.** Distinguish the inherited
   fixed-rate EMA correction (2.2) from the proposed auxiliary filters.
   Check the zero-history
   EMA energy identity, trace estimate (5.2), \(H^1\) control (5.1),
   and first-moment argument (8.4). In particular distinguish the
   real-form limit from exact operator matching.
2. **Build one controlled fixed-window pilot.** Use \(L=1/2<\log2\),
   the complete beta/pole transfer from SI S10, and ordinary unweighted
   norms. Compare original, output-filtered, input-congruence and
   path-averaged constructions on the same tests. Include oscillatory
   inputs and the weakest detected directions.
3. **Measure a real advantage.** Retain complete outputs and establish
   at least one explicit error or complement bound. A positive finite
   matrix alone is a diagnostic. Report which term prevents certification
   if the enclosure fails. No expensive archive replay is needed to
   begin this analytic and small-window work.
4. **Check the first arithmetic delay.** If the method survives the
   prime-free pilot, test \(\log2<L<\log3\) with the exact first delay
   and its sign. Do not tune away that contribution.
5. **Attempt one spatial/shift/filter step.** Carry the EMA memory
   (9.1), use the output defect in (9.3), and retain all signed
   parameter changes. The earlier log-7 pilot remains a possible
   later control; reaching an already certified central-form horizon
   is not itself a new result.
6. **Reconnect to physics only with a specified operator.** Decide
   whether the EMA states are merely numerical auxiliaries or candidates
   for actual boundary degrees of freedom. The latter need a physical
   action, adjoint, source map and localization-compatible charge.
   The fixed local normalization and pole cancellation remain tests.

The eventual continuation must still establish unbounded total length
and vanishing shift. For the output-filtered route it must also establish
\(\ell_j^2/\omega_j\to0\). A locally adjustable smoothing length does not
rule out finite-depth accumulation or unacceptable residual smoothing.
No arithmetic Loewner driver is supplied by any of these filter identities.

Suggested opening request:

> Continue from critical-path/notes/EMA_SMOOTHING_AND_POSITIVITY_CONTINUATION_20260920.md.
> First audit the EMA energy identity and the two sufficient limiting
> routes: output smoothing with ell squared divided by omega tending to
> zero, and shift-path averaging normalized by its first moment. Then
> construct a controlled comparison on L=1/2 using the full arithmetic
> transfer, including local and pole terms. Compare output smoothing,
> input congruence and path averaging, with complete output norms and
> explicit error bounds. Preserve the distinction between an auxiliary
> positivity method and a physical Wilson realization. Record a concrete
> gain, or a precisely scoped obstruction, before attempting spatial
> continuation or updating the manuscript.

## 12. Diagnostics, provenance, and preservation

[check_ema_controls.py](../numerics/check_ema_controls.py) is a standalone
Python standard-library program. Its
[record](../numerics/records/ema-controls.json) contains **57 passing
binary64 diagnostics** covering the energy and all-pass boundary identities, fixed-rate growth cancellation, direct convolution
versus the differential solution, complex inputs, filter memory across
a join, monotonicity in smoothing length, the gamma EMA sum, the
expanding toy control, the two removal rates, and path-EMA clock scaling.

The gamma-series diagnostic uses a finite sum and its elementary
positive-real tail estimate; it is not a certificate for a complex
operator. The rate controls use \(e^\omega I\), not an arithmetic
transfer computation. Quadrature tolerances and floating values are
diagnostics, not interval enclosures. No new finite arithmetic norm
matrix, rigorous complement bound, or positivity certificate was
computed in this session.

Run from this investigation:

    python3 numerics/check_ema_controls.py

The small [RESEARCH_RECORD.json](../RESEARCH_RECORD.json) pins this note,
the script and numerical output, and the main local inputs used here.
These hashes establish identity, not mathematical correctness.

The Wilson–Loewner version 0.4 PDFs, TeX sources and immutable snapshots
remain the manuscript baseline. Its 299 diagnostics are distinct from
these 57 new EMA controls. This continuation note is new research,
not a manuscript revision. The existing localization and cumulative
positivity obligations remain in force.
