# A constructive revision: put arithmetic transport in the channel derivative

12 September 2026. **Positive deformed toy family; exact first and mixed variations.** This calculation follows the bounded-rotation obstruction in [01_RELATIVE_COMPLEX.md, §8](01_RELATIVE_COMPLEX.md#8-a-calculated-obstruction-to-a-first-prime-deformation). It is the most specific remaining candidate from this pass. It produces the leading prime-delay singularity but also a calculable remainder. Neither the variation nor the full deformed energy is identified with the full Weil form.

## 1. Independent energy, trace, and symmetry

Fix finitely many delays $d_j>0$, real coefficients $b_j>0$, and a real deformation parameter $\eta$ satisfying $|\eta|\sum_j b_j<1$. On the whole line let $U_d u(x)=u(x-d)$. Given $f\in C_c^\infty(I_L)$, extend it by zero to $F$, and vary complex fields $u_k\in H^1(\mathbb R)$ in

\[
\mathcal E_\eta[F,(u_k)]
=\sum_{k\ge0}{2\over a_k}\left[
\|F-u_k\|^2+a_k^{-2}\left\|u_k'-\eta\sum_j b_j u_k'(\cdot-d_j)\right\|^2\right],
\qquad a_k=2k+1/2. \tag{1}
\]

All coefficients and channel Hilbert metrics are specified before evaluating this positive energy. The same finite-energy weighted component space as the original tower applies. The condition on $\eta$ makes $u\mapsto u-\eta\sum b_jU_{d_j}u$ boundedly invertible on every ordinary Sobolev space, by its Neumann series. Thus the derivative domain remains $H^1$; no unknown target square root is used.

For each channel replace (4) of the relative-complex note by the graph differential

\[
u\longmapsto D_{k,\eta}u=
\left(u,a_k^{-1}\left[u'-\eta\sum_jb_j u'(\cdot-d_j)\right]\right). \tag{2}
\]

Its range is closed. On the even/odd channel spaces, $\mathsf q_\eta(u,w)=(0,D_{k,\eta}u)$, with actual adjoint $\mathsf q_\eta^*(u,w)=(D_{k,\eta}^*w,0)$, is nilpotent and gives the positive partner Hamiltonian. Its physical degree-one space is the quotient by this range, with the ordinary harmonic representative norm. This is a coupled derivative model, not an addition of decoupled SUSY fields.

The adjoint contains the *backward* whole-line translations: if $M_\eta u=u-\eta\sum b_jU_{d_j}u$, then $D_{k,\eta}^*(v,w)=v-a_k^{-1}M_\eta^*w'$. Because $M_\eta^*$ is invertible, its maximal domain in this expression is $L^2\oplus H^1$. No input-dependent gauge choice is made. Every complex test $f$, with arbitrary mean and parity, is an admissible boundary datum. The physical pairing is invariant under changes of auxiliary representative and unitary changes of internal port basis. It is **not** invariant under $\eta$: changing arithmetic coupling is intended to change the observable.

## 2. Exact reduced pairing

Define the scalar symbol $m_\eta(\tau)=1-\eta\sum_j b_je^{-i\tau d_j}$ and $s=\tau^2$. Direct minimization at each frequency gives, for the actual input $f$,

\[
\widehat u_{k,f,\eta}(\tau)
={a_k^2\over a_k^2+s|m_\eta(\tau)|^2}\widehat F(\tau). \tag{3}
\]

The harmonic boundary state is the direct sum of

\[
\sqrt{2/a_k}\left(F-u_{k,f,\eta},-a_k^{-1}M_\eta u_{k,f,\eta}'\right).
\]

Using the same positive component norms, its full Hermitian pairing is

\[
Z_\eta(g,f)={1\over2\pi}\int
B(s|m_\eta(\tau)|^2)\overline{\widehat G(\tau)}\widehat F(\tau)d\tau, \tag{4}
\]

where $B(s)=\sum_k (2/a_k)s/(a_k^2+s)$. The upper and lower bounds on $|m_\eta|$, together with the logarithmic asymptotic of $B$, show that this has the same finite-interval logarithmic form domain as the original kinetic tower. Finite sums and then monotone convergence prove (4); it is valid at every $L>0$. The bare infinite source is still not a Hilbert vector, as explained in the relative-complex note.

Importantly, every $U_{d_j}$ in (1) acts on an auxiliary field on the **whole line**. Replacing it by a compressed $T_{d_j}$ inside the bulk changes the equilibrium problem and (4). Only the input is supported in $I_L$.

## 3. A prime singularity plus a smoothing remainder

Termwise differentiation on $s>0$ gives

\[
B'(s)=\sum_{k\ge0}{2a_k\over(a_k^2+s)^2},\qquad
h(\tau)=2\tau^2B'(\tau^2). \tag{5}
\]

The digamma asymptotic yields $B(s)=\tfrac12\log s-\log2-\psi(1/4)+O(s^{-1})$, with differentiable asymptotic expansion. Therefore $h(0)=0$, $h(\tau)=1+O(\tau^{-2})$ as $|\tau|\to\infty$. At $\eta=0$,

\[
\partial_\eta Z_\eta(g,f)\big|_0
={1\over2\pi}\int -h(\tau)\sum_j b_j\cos(d_j\tau)
\overline{\widehat G(\tau)}\widehat F(\tau)d\tau. \tag{6}
\]

For the first prime set $d=\log2$, $c=\log2/\sqrt2$, $b=2c$. The desired prime multiplier is $-2c\cos(d\tau)$. Equation (6) equals it **plus**

\[
2c[1-h(\tau)]\cos(d\tau). \tag{7}
\]

The first piece is the exact pair of delta translations with the arithmetic coefficient. The remainder is nonzero: at $\tau=0$ it equals $2c$, canceling the desired prime multiplier there. Since $1-h\in L^1(\mathbb R)$, its inverse Fourier transform $k(x)$ is bounded and continuous. The extra kernel is

\[
c[k(x-x'-d)+k(x-x'+d)]. \tag{8}
\]

This is a translated nonlocal remainder, not a missing contact term that can be removed by changing one constant. The limit $h\to1$ explains why this family evades the finite-channel bounded-rotation obstruction: the leading derivative was changed across infinitely many masses. For a fixed finite tower, $h_N(\tau)\to0$ instead. The limits in channel count and input frequency do not commute.

Equation (6) is an indefinite *variation of positive energies*. Such a variation need not be positive, and its leading arithmetic match does not prove positivity of the full Weil form. This is a restricted success at the level of a calculated coupling, not completion of the target.

## 4. Two labels: the unwanted interaction can be located explicitly

Use independent parameters $\eta_p,\eta_q$ and $m=1-\eta_pb_pe^{-ia\tau}-\eta_qb_qe^{-ib\tau}$, where $a=\log p$, $b=\log q$. At zero parameters the mixed derivative of the multiplier in (4) is

\[
2s b_pb_q B'(s)\cos((a-b)\tau)
+4s^2b_pb_qB''(s)\cos(a\tau)\cos(b\tau). \tag{9}
\]

Because $B'(s)\sim1/(2s)$, $B''(s)\sim-1/(2s^2)$, the leading term is

\[
-b_pb_q\cos((a+b)\tau). \tag{10}
\]

Thus the apparent leading difference-label interaction cancels, but leaves a sum label $\log(pq)$. For distinct primes it is absent from the Weil form. At finite frequency (9) also retains smoothing remainders. At lengths below $a+b$, compression kills the leading delta translation (10), but need not kill those remainders. This is an endpoint-sensitive distinction between matching a principal singularity and matching the actual quadratic form.

A justified next modification is $M=(I-\eta_pb_pU_a)(I-\eta_qb_qU_b)$. Its high-frequency response is $\log|M|=\log|1-\eta_pb_pe^{-ia\tau}|+\log|1-\eta_qb_qe^{-ib\tau}|$; hence the leading mixed singularity vanishes. The *exact* mixed derivative is then

\[
4b_pb_q\cos(a\tau)\cos(b\tau)
\left[sB'(s)+s^2B''(s)\right], \tag{11}
\]

which tends to zero but is not identically zero. The gamma function is not an exact logarithm. Equations (7) and (11) give the next concrete residual kernels to control. Product composition cures the leading mixed delta without claiming to cure the full pairing.

### Finite coupling also tests the repetition coefficients

One must not replace a tangent calculation by setting its parameter to one. To test the actual deformed norm, absorb each parameter and coefficient into a real number $0<\alpha_p<1$, and use the product symbol $m(\tau)=\prod_p(1-\alpha_p e^{-ia_p\tau})$, with $a_p=\log p$. Its exact high-frequency change from the undeformed kinetic pairing is

\[
B(\tau^2|m(\tau)|^2)-B(\tau^2)
=-\sum_p\sum_{n\ge1}{\alpha_p^n\over n}\cos(n a_p\tau)
+O(\tau^{-2}). \tag{11a}
\]

The remainder estimate is uniform in frequency because the finite product is bounded above and away from zero. This follows directly from $B(s)=\tfrac12\log s+\text{constant}+O(s^{-1})$ and the convergent logarithm series. The desired coefficient of the cosine is instead $-2a_p p^{-n/2}$. Matching the first coefficient forces $\alpha_p=2a_p p^{-1/2}$ whenever this is in the stipulated range; it does not match all repetitions.

For $p=2$ this choice is admissible. Its second cosine coefficient has magnitude $(\log2)^2$, whereas the target requires $\log2$. Once $L>\log4$, their difference is a nonzero delta translation on the test interval; a continuous residual cannot cancel it as a distribution on all test pairs. Product composition therefore removes mixed-prime leading singularities but does **not** produce the correct repeated-prime weights at finite coupling. The primitive-length derivative in the delay note explains how those weights arise in a different observable; taking that derivative is not an identity for the positive norm here. This obstruction is specific to the stated scalar product family and leaves richer coupled channel models open.

## 5. Evaluate the residuals, including the contact generated by the limit

These residuals can be evaluated without an inverse spectral problem. Put $j(t)=e^{-t/2}/(1-e^{-2t})$ for $t>0$, and define the even integrable function

\[
R_h(x)=j(|x|)+|x|j'(|x|),\qquad R_h(0)=1/4.
\]

For one channel, the inverse Fourier transform of $4a\tau^2/(a^2+\tau^2)^2$ is $(1-a|x|)e^{-a|x|}$. Summing away from zero suggests $R_h$, but this misses a contact. Indeed $x\sum_{k<N}e^{-a_k|x|}$ converges in distributions to $xj(|x|)$, whose jump at zero is $1$, since $t j(t)\to1/2$. Differentiating this limit proves the full identity

\[
\mathcal F^{-1}h=\delta_0+R_h,\qquad k(x)=-R_h(x). \tag{12}
\]

Thus (8)'s correction is explicitly

\[
-c\,[R_h(x-x'-d)+R_h(x-x'+d)]. \tag{13}
\]

The contact in the infinite limit is essential. As a control, $\int R_h(x)dx=2[tj(t)]_{0}^{\infty}=-1$; then the multiplier value is $h(0)=1-1=0$, as (5) requires. The regular correction $k=-R_h$ is negative near zero and positive for sufficiently large $|x|$; it is not a nonnegative multiplication term or a single pole amplitude.

The mixed product-composition remainder in (11) is also explicit. If $V$ is the inverse Fourier transform of $sB'(s)+s^2B''(s)=\tau h'(\tau)/4$, distributional differentiation of (12) gives

\[
V(x)=-\tfrac14\,[j(t)+3t j'(t)+t^2j''(t)]_{t=|x|},\qquad V(0)=-1/16. \tag{14}
\]

There is no delta here: $x\delta_0=0$, and $xR_h(x)$ is continuous. The apparent inverse-power singularities in (14) cancel. In position space (11) is $b_pb_q\sum_{\epsilon,\epsilon'=\pm1}V(x-x'+\epsilon a+\epsilon'b)$. Its integral is zero, consistent with its multiplier vanishing at zero. These translated continuous kernels survive some interval compressions that remove their associated leading delta labels.

## 6. Next step and remaining arithmetic inputs

The next task is to determine whether a **single** additional constrained channel coupling cancels (13) and the four translates of (14) while also providing the fixed $w_0$ and both pole amplitudes. Any cancellation has to occur at the positive amplitude or quotient level, not by subtracting its answer from the norm afterward. The residue and finite-part accounting at $a_0=1/2$ is a natural first place to test, since the growing-pole replacement already fails as an independent channel. Equations (12)–(14) make this a specific kernel-matching problem.

At present $a_k,d_j,b_j$ are assigned, not dynamically selected. This model is strongest as an explicit candidate for coupling gamma modes to arithmetic transport: it is positive, has all-input coverage and an adjoint-compatible harmonic sector, and demonstrates both what the simplest coupling produces and why it falls short. Its residuals are mathematical tasks that can now be calculated without assuming the sign of $Q_{0,L}$.
