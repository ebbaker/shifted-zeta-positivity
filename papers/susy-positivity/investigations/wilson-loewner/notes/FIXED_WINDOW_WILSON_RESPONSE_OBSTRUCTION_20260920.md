# Fixed-window Wilson response: normalization, first variation, and a regularity obstruction

20 September 2026. Research calculation prepared for Edward Baker.

**Model:** OpenAI GPT-6 (Codex). **Reasoning effort:** the configured effort level is not exposed to the assistant in this session; no level is inferred.

**Status:** a specified Gaussian Wilson probe response and an analytical exclusion of its regular-readout class. This is not a construction of the arithmetic transfer, an exclusion of all Wilson realizations, or a positivity certificate. The finite diagnostics below check formulas, not the operator proofs or an interacting field theory. This note continues [the fixed-window recommendation](RESEARCH_CONTINUATION_20260920.md).

## 1. Result and scope

A retarded readout of the existing ordinary-reflection Wilson states can be given an explicit direct identity channel and baseline subtraction. This defines a linear operator on every input, with exact initial identity and causal support. Its first variation can be calculated in the free endpoint and direct Gaussian bulk model at positive bulge height. It is bounded, even when the bulk variation is nonzero.

That response cannot match the full arithmetic first variation on any nonempty window, including every (0<L<\log 2). The arithmetic generator has logarithmic high-frequency growth and requires a (1/u) causal finite-part distribution. Finite local renormalizations and regular endpoint/reflection kernels cannot produce it. A second obstruction applies at positive shift: the tested response is identity plus a compact operator, whereas the arithmetic finite-window transfer is compact.

The full pole calculation adds a useful exact constraint. One rational pole cancels the lowest gamma mode. The remaining arithmetic transfer before the first integer delay is a shifted gamma kernel minus its growing-exponential average. In particular, the required first-variation kernel away from the diagonal is

\[
 b(u)=2\frac{e^{-u/2}}{1-e^{-2u}}-4\cosh(u/2)
     =2\frac{e^{-5u/2}}{1-e^{-2u}}-2e^{u/2},\qquad 0<u<L.
\]

Its singularity, signed pole correction, and fixed contact term are separate matching obligations. The obstruction concerns the regular reflected readout defined here and the bounded-derivative class in Section 5. It leaves open a singular source-to-response construction with a justified renormalized limit. No real Loewner driver or shift/capacity clock is assumed or obtained.

## 2. The full arithmetic target on the fixed window

Use (I_L=(-L/2,L/2)), ordinary unweighted (L^2(I_L)), zero extension (F), and the smooth core (C_c^\infty(I_L)). Set (d=x+L/2). Since every nontrivial arithmetic delay is at least (\log 2), it acts as zero on this window. This does **not** remove the local term or either pole.

The inherited causal generator is, on the core,

\[
\begin{split}
 (G_{0,L}f)(x)={}&w_0 f(x)
 +2\int_0^\infty n_\Gamma(u)\{f(x)-F(x-u)\}\,du\\
 &+4\int_0^d\cosh(u/2)f(x-u)\,du, \tag{2.1}\\
 n_\Gamma(u)={}&\frac{e^{-u/2}}{1-e^{-2u}},\qquad
 w_0=-\gamma-\frac\pi2-3\log2-\log\pi.
\end{split}
\]

The difference makes the first integral convergent at zero. The part (u>d) remains a local loss term; deleting that tail changes the operator. For example an entirely finite-window expression is

\[
 G_{0,L}f=(w_0+T(d))f
 +2\int_0^d n_\Gamma(u)\{f(x)-f(x-u)\}\,du
 +4\int_0^d\cosh(u/2)f(x-u)\,du, \tag{2.2}
\]

where, by setting (v=e^{-u/2}),

\[
 T(d)=2\int_d^\infty n_\Gamma(u)\,du
 =\log\frac{1+e^{-d/2}}{1-e^{-d/2}}+2\arctan(e^{-d/2}). \tag{2.3}
\]

This is the nonsymmetric causal operator, not just its real form. In particular the causal pole kernel is (4\cosh(u/2)\mathbf1_{u>0}); only after taking the symmetric part does it become (2\cosh((x-y)/2)). Its form is (2|C(f)|^2-2|S(f)|^2), so it is not an independent positive Gram contribution.

### 2.1 A diagonal/off-diagonal matching condition with a fixed finite part

Let (A_L=-G_{0,L}) be the required first response derivative. Define

\[
 c_\epsilon=-w_0-T(\epsilon).
\]

Then in (L^2(I_L)) on the smooth core,

\[
 (A_Lf)(x)=\lim_{\epsilon\downarrow0}
 \left[c_\epsilon f(x)+\int_\epsilon^{d}b(u)f(x-u)\,du\right], \tag{2.4}
\]

where an integral with (d\le\epsilon) means zero. The omitted pole integral on (0<u<\epsilon) tends to zero, and the subtracted gamma integral converges by the smooth zero extension. Formula (2.3) gives

\[
 \boxed{c_\epsilon=\log\epsilon+\gamma+\log(2\pi)+O(\epsilon).} \tag{2.5}
\]

Thus a physical cutoff must produce both the singular off-diagonal part and the correlated contact subtraction. The finite part (\gamma+\log(2\pi)) is fixed **in this hard-delay-cutoff convention**. Other regulator schemes must explicitly convert their finite part to (2.4); it is not an adjustable physical constant. Equivalently, in the difference convention (2.1), the local constant is the inherited (w_0\simeq-5.3721834192256654).

The pole correction is visible even away from zero. With (z=e^u), (b(u)=0) is (z^3-z-1=0). Its unique root with (z>1) gives

\[
 u_*\simeq0.2811995743229617<\log2.
\]

The required (b) is positive below (u_*) and negative above it. For windows larger than (u_*), a pointwise nonnegative off-diagonal first-response ansatz therefore also fails. A positive Gram kernel is not generally pointwise positive, and its derivative need not be positive: this sign observation alone is not an exclusion of reflection positivity.

### 2.2 Absorbing the first pole, at finite shift as well

The inherited Laplace symbol, with the prime term inactive after compression, is

\[
 a_0^{<}(p)=\psi\left(\frac14+\frac p2\right)-\log\pi
             +\frac2{p+1/2}+\frac2{p-1/2}.
\]

The digamma recurrence yields the exact simplification

\[
 \boxed{a_0^{<}(p)=\psi\left(\frac54+\frac p2\right)-\log\pi
                       +\frac2{p-1/2}.} \tag{2.6}
\]

Equivalently, set (n_1(u)=e^{-2u}n_\Gamma(u)) and (w_1=w_0+4). Then

\[
 G_{0,L}=w_1 I+2\int_0^\infty n_1(u)(I-T_u)\,du
                     +2R_{-1/2,L},\qquad
 (R_{-1/2,L}f)(x)=\int_0^d e^{u/2}f(x-u)\,du. \tag{2.7}
\]

This does not discard (w_0): the change to (w_1) accounts exactly for the removed (n=0) mode. Nor is (e^{u/2}) a stable decaying covariance mode. It is a perfectly bounded Volterra kernel on a fixed finite window; its presence does not by itself prohibit a physical realization with additional structure.

At positive shift (0<\omega\le1/2), let (K_\omega^{<}) denote the archimedean-plus-rational factor whose compression equals the full arithmetic transfer here. Gamma recurrence gives

\[
 K_\omega^{<}(p)=
 \pi^\omega
 \frac{\Gamma((p+5/2-\omega)/2)}{\Gamma((p+5/2+\omega)/2)}
 \left(1-\frac{2\omega}{p-1/2+\omega}\right). \tag{2.8}
\]

This equality is between arithmetic factors, not a Wilson construction. It follows by absorbing ((p+1/2-\omega)/(p+1/2+\omega)) into the gamma ratio. The full zeta quotient still differs from this factor outside the small-window compression.

Writing

\[
 h_\omega(u)=\frac{2\pi^\omega}{\Gamma(\omega)}
 e^{-(5/2-\omega)u}(1-e^{-2u})^{\omega-1}\mathbf1_{u>0},
\]

the exact small-window kernel is

\[
 \boxed{k_\omega^{<}(u)=h_\omega(u)
 -2\omega\int_0^u e^{(1/2-\omega)(u-v)}h_\omega(v)\,dv.} \tag{2.9}
\]

Differentiating on the smooth core gives (2.7), including the remaining pole. For every positive shift the kernel is locally integrable, with leading singularity proportional to (u^{\omega-1}); at zero shift its distributional limit is (\delta_0). The initial identity is therefore supplied by a singular limit, rather than by a persistent direct delta channel at positive shift.

The recurrence used here is [DLMF 5.5.2](https://dlmf.nist.gov/5.5.E2); the gamma recurrence is [DLMF 5.5.1](https://dlmf.nist.gov/5.5.E1). The arithmetic factorization itself is inherited from [SI S1](../sections/s_arithmetic.tex).

## 3. A defined Wilson boundary readout

This section specifies an independently chosen test observable and readout. Its failure is a result of the calculation, rather than a normalization left unresolved.

### 3.1 Fields, contours, reference sector, regulator and adjoint

For a fully calculable control, take an abelian Gaussian probe model: independent Hermitian bulk gauge components and six real scalars with equal Feynman-gauge covariance (g^2/(4\pi^2|X-Y|^2)), and an independent complex defect scalar doublet with covariance (\delta_{mn}/|a-b|). The latter normalization strips the positive coupling/color factor of the free endpoint propagator. Keep the physical polarization (q_2,\bar q_2).

One explicit smooth regulator replaces each massless covariance by its heat-kernel integral over heat times (s\ge\epsilon^2): (g^2\int_{\epsilon^2}^\infty(4\pi s)^{-2}e^{-|X-Y|^2/(4s)}ds) for each bulk component, and (4\pi\int_{\epsilon^2}^\infty(4\pi s)^{-3/2}e^{-|a-b|^2/(4s)}ds) for the defect scalar. The probability measure is normalized and independent of the deformation. This is a precise fixed-gauge Gaussian control, not a complete interacting gauge/defect action. Reflection positivity of this cutoff measure is not assumed.

Use the existing tangent map (M), with columns ((-e_7,e_8,e_9,e_6)). In the ((x^0,x^3))-plane let

\[
 X_{r,\eta}(t)=(rt,\eta r\varphi(t)),\qquad
 \varphi(t)=t^2(1-t),\quad 0\le t\le1.
\]

The ket curve (C_{r,\eta}) is traversed from (t=1) to zero, from the defect point (a_r=(r,0)) to the common reference (b=0). Its reference tangent is (-e_0), so the reflected reverse joins smoothly. Set (r=e^x), (\eta(\omega)=\eta_0+\omega), with fixed (\eta_0>0). This is a chosen test deformation; (\omega) is the parameter to be compared with shift. It is not identified with capacity or logarithmic radius.

Let

\[
 F_{\omega,\epsilon}(x)=e^{x/2}
 U_M(C_{e^x,\eta(\omega)})q_{2,\epsilon}(a_{e^x}),\qquad
 \mathsf K_{\omega,\epsilon}(x,y)
 =\langle\Theta_0F_{\omega,\epsilon}(x)F_{\omega,\epsilon}(y)\rangle_\epsilon.
\]

The abelian reference color fiber is one-dimensional with the ordinary complex inner product; its contraction at (b) is the identity. There is no extra defect field at the reference, and no field at a bulk tip. The physical bra uses ordinary time reflection, reversed ordering and (N=-MR), exactly as in [SI S7](../sections/08_reflection.tex). No internal rotation is inserted into the metric.

The chosen physical endpoint pair has a nonzero contraction. Replacing it by (q_2,\bar q_1) to require the same fixed-H Poincare charge would give the zero pairing from [SI S6](../sections/07_endpoints.tex), not a normalization improvement. No common endpoint supercharge or protected interacting expectation is assumed here.

### 3.2 Input-to-output action and its exact normalization

Define the retarded readout on arbitrary inputs by

\[
 \boxed{(\mathcal V_{\omega,L}^{\epsilon}f)(x)=f(x)
 +\int_{-L/2}^{x}
 [\mathsf K_{\omega,\epsilon}(x,y)-\mathsf K_{0,\epsilon}(x,y)]f(y)\,dy.} \tag{3.1}
\]

The integral can equivalently be read as the pairing of the output row (\Theta_0F_\omega(x)) with the source state (\int_{-L/2}^x F_\omega(y)f(y)dy), minus the baseline pairing. Thus it is a specified linear readout built from Wilson-dressed fields, with a direct identity channel. Its initial operator is exactly (I); it never uses an inverse square root of the compact free Gram kernel.

The support is explicitly (y\le x), including the delta on (x=y). Retardation in logarithmic radius is an imposed readout rule in (3.1), not a consequence of Euclidean time reflection. Deriving such a rule from boundary dynamics would be an additional physical requirement even if this test succeeded. In particular the Gram operator and the response (3.1) are distinct objects.

At fixed regulator these are bounded operators, norm-continuous at zero for this smooth contour family. The same holds in the Gaussian limit established below. The adjoint in the fixed arithmetic norm is the ordinary upper-triangular integral adjoint:

\[
 ((\mathcal V^\epsilon_{\omega,L})^*g)(y)=g(y)
 +\int_y^{L/2}\overline{[\mathsf K_{\omega,\epsilon}(x,y)-\mathsf K_{0,\epsilon}(x,y)]}g(x)\,dx.
\]

It is not contour reversal with an unchanged scalar map. A finite local normalization may replace the direct term by (m_\omega(x)f(x)), with (m_0=1) and bounded derivative; Section 5 shows why this does not repair the first variation. No such factor is included in the tested definition (3.1).

## 4. First variation using the existing insertion and Gaussian tools

At fixed endpoints the exact tangent-connection insertion from [SI S4](../sections/05_variation.tex) is

\[
 \partial_\omega U_M=
 \int_0^1 U_M(1,s)\mathcal F_{\nu\mu}
       \partial_\omega X^\nu\dot X^\mu U_M(s,0)\,ds.
\]

Here (\mathcal F) is the curvature of (iA+MX), including the scalar gradients and commutators. This tangent-one-form version includes the arclength and polarization variations of the equivalent unit-vector formula. The bulge variation vanishes at both endpoints, so the endpoint displacement terms vanish; the (q_2) polarization and radial weights are fixed. Both bra and ket vary in (\mathsf K).

For a general normalized average the differentiation rule would also include

\[
 \partial_\omega\langle\mathcal O\rangle_\omega
 =\langle\partial_\omega\mathcal O\rangle_\omega
 -\langle\mathcal O\,\partial_\omega S_\omega\rangle_{\omega,c}, \tag{4.1}
\]

and the derivative of any external normalization or shift-dependent source identification. The action and normalized measure of this control do not vary, so the second term here is exactly zero. No measure term is silently discarded in extending a claim to another model: such an extension would need its own calculation.

At free endpoint order (U=1),

\[
 \mathsf K_\omega^{(0)}(x,y)=\frac{\sqrt{rs}}{r+s}
                         =\frac1{2\cosh((x-y)/2)},\qquad
 \partial_\omega\mathsf K_\omega^{(0)}=0. \tag{4.2}
\]

Consequently (\mathcal V_\omega^{(0)}=I): even after solving normalization and support, the free response produces none of (2.1).

### 4.1 A nonzero response that still fails the test

The direct Gaussian bulk term supplies a stronger control than the zero result. Equal gauge/scalar propagators cancel all same-branch contractions. Ordinary reflection leaves the spatial-current cross contraction, with numerator (2v_{\mathrm{sp}}\cdot w_{\mathrm{sp}}). In this independent **abelian Gaussian** model the exponential average is exact. Removing the regulator gives

\[
 \mathsf K_\omega(x,y)
 =G_o(x-y)\exp\{\lambda B_{\eta(\omega)}(r,s)\},\qquad
 \lambda=\frac{g^2}{4\pi^2},\quad G_o(u)=\frac1{2\cosh(u/2)}, \tag{4.3}
\]

where

\[
 B_\eta(r,s)=2\eta^2rs\int_0^1\!\int_0^1
 \frac{\varphi'(v)\varphi'(t)}
 {(rv+st)^2+\eta^2[r\varphi(v)-s\varphi(t)]^2}\,dv\,dt. \tag{4.4}
\]

The order-(g^2) term is precisely the existing direct bulk sector, generalized to unequal endpoint radii. Treating the exponential as exact is justified only in this Gaussian abelian model. Endpoint-to-line interactions, defect vertices, endpoint self-energy and their counterterms from the interacting theory are absent by its definition; this is not their completed sum.

Differentiating (4.4), put (A=(rv+st)^2), (H=[r\varphi(v)-s\varphi(t)]^2). The two numerator derivatives and denominator derivative combine to give

\[
 \partial_\eta B_\eta(r,s)=4\eta rs\int_0^1\!\int_0^1
 \frac{\varphi'(v)\varphi'(t)A}{(A+\eta^2H)^2}\,dv\,dt. \tag{4.5}
\]

Since (|\varphi'(v)|\le2v) and (4rsvt\le(rv+st)^2), the absolute integrands give the uniform bounds

\[
 |B_\eta(r,s)|\le2\eta^2,\qquad
 |\partial_\eta B_\eta(r,s)|\le4\eta. \tag{4.6}
\]

These also control the apparent reference corner (v=t=0). On compact positive ranges of (r,s,\eta), the regulated cross contractions and their first derivatives converge by dominated convergence; the heat-regularized propagator and its radial derivative admit constant multiples of the corresponding unregulated bounds. Thus this is a continuum calculation for the stated Gaussian readout, not just a fixed-cutoff assertion. It does not justify removal of interacting defect/junction counterterms.

In particular,

\[
 J_0(x,y):=\left.\partial_\omega\mathsf K_\omega(x,y)\right|_0
 =\lambda G_o(x-y)e^{\lambda B_{\eta_0}(r,s)}
                   \partial_\eta B_{\eta_0}(r,s), \tag{4.7}
\]

and (|J_0|\le2\lambda\eta_0 e^{2\lambda\eta_0^2}) for (\lambda\ge0). It follows that

\[
 \mathcal V_{\omega,L}=I+\omega\mathcal J_L+o(\omega)
 \quad\text{in operator norm},\qquad
 (\mathcal J_L f)(x)=\int_{-L/2}^x J_0(x,y)f(y)dy, \tag{4.8}
\]

with (\|\mathcal J_L\|\le2L\lambda\eta_0e^{2\lambda\eta_0^2}). Uniform smoothness in the compact parameter set justifies the norm remainder. The kernel is finite at (x=y), unlike (b(x-y)\sim1/(x-y)).

At (r=s=1,\eta_0=0.3), diagnostics give

\[
 B_{0.3}(1,1)\simeq0.0102220294386856,\qquad
 \partial_\eta B_{0.3}(1,1)\simeq0.0680705213083742.
\]

The first value agrees with [SI S8](../sections/09_response.tex). Its derivative was checked against independent central differences of (4.4), after a two-triangle change of variables removing the corner. Thus a nonzero Wilson shape response exists in the tested sector, but it has the wrong operator regularity to be the prescribed shift derivative.

## 5. Two precisely scoped obstructions

### 5.1 First variation: regular kernels cannot reproduce the generator

**Proposition.** Suppose a response of the form (3.1), possibly with a local multiplier (m_\omega), has a first derivative on the smooth core of the form

\[
 Af=q(x)f(x)+\int_{-L/2}^x j(x,y)f(y)dy,
\]

where (q\in L^\infty(I_L)) and the integral defines a bounded (L^2) operator. A square-integrable kernel, a uniformly bounded kernel, or the Schur bounds suffice. Then (A\ne-G_{0,L}) on (C_c^\infty(I_L)), for every (L>0) in the prime-free range.

**Proof.** Take (0\ne\chi\in C_c^\infty(I_L)) and (f_N(x)=e^{iNx}\chi(x)). The inherited real form, with no prime delays, is

\[
 Q_{0,L}[f]=\frac1{2\pi}\int_\mathbb R
 [\Re\psi(1/4+i\tau/2)-\log\pi]|\widehat F(\tau)|^2d\tau
 +2|C(f)|^2-2|S(f)|^2.
\]

The digamma asymptotic and the rapidly decaying transform of (\chi) imply

\[
 \frac{Q_{0,L}[f_N]}{\|\chi\|^2}
 =\log N-\log(2\pi)+o(1). \tag{5.1}
\]

The two pole moments tend to zero by integration by parts. The asymptotic follows by splitting the translated Fourier integral into a neighborhood of (N) and its rapidly decaying tails; the standard digamma expansion is [DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2). If (A=-G_{0,L}) on the core, then (\Re\langle f_N,Af_N\rangle/\|\chi\|^2\to-\infty), contrary to boundedness of (A). This uses the localized real form to disprove operator equality; it does not replace the full matching target by a form. In particular no Fourier multiplier is assigned to the growing pole on the unweighted whole line. \(\square\)

The Gaussian response (4.8) satisfies the hypotheses. Any finite smooth clock change merely multiplies its bounded derivative and still fails. A singular clock or a regulator-dependent deformation requires a new limit analysis and is outside this proposition.

Adding a finite local multiplier, even one chosen to insert (w_0) by hand, cannot repair the singular gamma term. Nor can the regular pole kernel alone cancel logarithmic high-frequency growth. Conversely, matching only the singular gamma part would still leave the fixed finite contact and full (b(u)) in (2.4) unmatched.

The statement also rules out a regulator removal for which first derivatives converge on every smooth test while their operator norms stay uniformly bounded: the limit would extend to a bounded operator. A successful renormalized family must violate this bounded-derivative assumption in a controlled way. Mere smoothness at each fixed regulator does not exclude such a singular limit.

### 5.2 Positive shift: a persistent direct identity channel also fails

For the Gaussian response, the retarded kernel difference in (3.1) is bounded on the finite square. Its integral operator is Hilbert--Schmidt, hence compact. Thus (\mathcal V_{\omega,L}=I+\text{compact}) for every fixed shift.

By contrast (V_{\omega,L}) from (2.9) is compact for every (\omega>0). Indeed truncate its locally integrable convolution kernel away from (u=0), approximate the remainder on ((0,L)) by bounded kernels, and use the (L^1)-kernel Young bound for the operator-norm error. Each approximant on the finite square is Hilbert--Schmidt. Therefore

\[
 \|\mathcal V_{\omega,L}-V_{\omega,L}\|\ge1
 \quad(\omega>0) \tag{5.2}
\]

for the direct coefficient one. The reason is that the difference is (I+\text{compact}), whose essential norm is one. A scalar direct coefficient (m_\omega\ne0) changes this lower bound to (|m_\omega|), and still precludes equality. A nonzero bounded multiplication operator on this nonatomic interval is likewise not compact.

This does not contradict the arithmetic strong initial limit (V_{\omega,L}\to I). Strong limits of compact operators can be the identity; operator-norm limits cannot. The precise lesson is that a successful positive-shift transfer must replace the direct delta channel by a singularly concentrating kernel, or use another boundary evolution with the same effect. An identity-plus-regular-correlator correction leaves that channel in place.

## 6. What remains required of a viable construction

The exact calculation supplies a specific next target, not a driver:

1. Specify boundary source dynamics or a justified singular response limit that yields the hard-cutoff-equivalent distribution (2.4), including the finite part (2.5). The regular opposite-ray reflected kernel alone cannot do this. The full even angular covariance has the needed short-distance tower, but its support and its contact subtraction still need a physical source-to-response interpretation.
2. Explain the cancellation of the lowest gamma mode and the signed exponential response in (2.7) or (2.9). A determinant ratio or a covariance with the right decay rates does not establish these operations. Inserting them as external filters would reproduce arithmetic by design, not derive it from Wilson dynamics. The follow-up [Localization and the pole cancellation](LOCALIZATION_AND_THE_POLE_CANCELLATION_20260920.md) develops Edward Baker's proposal to derive the cancellations through a defect-compatible localization calculation, with an exact auxiliary boson–fermion product as a comparison target.
3. Include the derivative of the measure, source identifications and all endpoint/junction renormalizations in any interacting proposal. A boundary differential/amputation operation may evade the regularity hypotheses, but then its domain, causal support and exact normalization must be proved; a finite-mode inverse of a Gram matrix is insufficient.
4. Only after a successful operator test, constrain a regular inverse-Loewner velocity and a clock through (\partial_t\mathcal V=-\dot\omega G_\omega\mathcal V). Capacity, shift and support length remain distinct. The existing bare-transport no-closure example still prevents a universal geometry-only argument.

The next integer threshold remains (\log2<L<\log3), where the generator adds (-2(\log2)/\sqrt2\,T_{\log2}), with (\cosh(\omega\log2)) in its positive-shift coefficient. Nothing in this fixed-window obstruction supplies that delay or excludes a construction with additional arithmetic structure.

## 7. Cumulative positivity and later gluing remain separate obligations

Even a successful first-variation match would not prove the finite-shift flow or its contraction. The needed independent storage law remains

\[
 \|f\|^2=\|\mathcal V_{\omega,L}f\|^2+\|\mathcal B_{\omega,L}f\|^2.
\]

After transfer matching, it must give

\[
 \|\mathcal B_{\omega,L}f\|^2
 =2\omega Q_{0,L}[f]+o(\omega),\qquad
 D_{\omega,L}=2\int_0^\omega V_{s,L}^*\Re G_{s,L}V_{s,L}\,ds
\]

in the form sense. For directions with positive (Q_{0,L}), the amplitude has size (\sqrt\omega). A smoothly varying Wilson state difference (F_\omega-F_0), when it is (O(\omega)) in its positive Hilbert norm, has squared norm (O(\omega^2)) and cannot be that amplitude. This excludes that simple amplitude prescription under its norm regularity assumption, not all cumulative amplitudes.

No positivity of the accumulated defect follows from the Gaussian kernel used in (3.1); positive reflection pairings do not imply a balance law for this imposed readout. Conversely the research goal is positivity of the accumulated defect, not positivity of every instantaneous generator or monotonicity in shift. The archived negative instantaneous one-vector test still does not prove negativity on the evolved vector.

For a later causal spatial split,

\[
 V_{\omega,L+h}=\begin{pmatrix}X&0\\Y&Z\end{pmatrix},\quad
 E=I-X^*X,\quad F_{\rm out}=I-ZZ^*,
\]

the inherited strict-diagonal criterion is

\[
 \|V_{\omega,L+h}\|\le1
 \iff\|F_{\rm out}^{-1/2}YE^{-1/2}\|\le1.
\]

It keeps the **output** defect of the new slab and the complete cross map. Simultaneous shift changes require the signed metric changes and Schur criterion of [SI S9](../sections/s_continuation.tex). A fixed-window calculation supplies none of these estimates. The all-depth objective remains all-input contraction at (L_j\to\infty), (\omega_j\downarrow0), including control that prevents finite-depth accumulation. No new central positivity, cumulative contraction or gluing certificate is claimed here.

## 8. Reproducibility and provenance

The new [standard-library diagnostic](../numerics/check_fixed_window_response.py) and its [small record](../numerics/records/fixed-window-response-checks.json) contain **31 passing checks**. They compare the subtracted integral with the digamma generator, check the finite-shift gamma/pole absorption and first derivative, check the fixed cutoff finite part and off-diagonal sign, and compare the analytic Gaussian insertion with finite differences and the existing equal-radius response. The recorded nonzero unequal-radius derivative is approximately (0.0647903496622915) at (r=e^{-1/4},s=e^{1/4},\eta=0.3).

Run from the investigation directory with:

```sh
python3 numerics/check_fixed_window_response.py
```

The calculations use ordinary binary64 quadrature and are not rigorous numerical enclosures. The two operator obstructions are analytical arguments above; finite tests do not prove them. The new diagnostic uses the arithmetic target explicitly as a comparison and does not construct it from field data. It reuses the corner-resolving quadrature infrastructure of the existing reflection calculation.

Inherited inputs are [the shift equation](../sections/03_shift_evolution.tex), [the arithmetic normalization and factorization](../sections/s_arithmetic.tex), [the Wilson insertion](../sections/05_variation.tex), [endpoint restrictions](../sections/07_endpoints.tex), [ordinary reflection](../sections/08_reflection.tex), and [the direct bulk response](../sections/09_response.tex). New calculations here are the combined local/pole matching distribution, the finite-shift lowest-mode absorption, the specified retarded readout, its unequal-radius Gaussian derivative, and the two scoped exclusions. They have not received independent mathematical review. Manuscript sources and dated manuscript snapshots are not changed by this research calculation.

This research note and its diagnostic were developed with OpenAI GPT-6 (Codex) for Edward Baker. The LLM-assisted derivations and claims require author verification before promotion to a manuscript.
