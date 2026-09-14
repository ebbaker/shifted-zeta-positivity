# Arithmetic transport, loop norms, and the cost of coherence

12 September 2026. **Exact finite-interval identities and tested obstructions.** Positive transport spaces are independently specified below. Their prime-power expansion is calculated, but their norm is not the Weil form. The prospective combination with the relative complex remains a research direction.

## 1. Literature mechanism and the model chosen here

Quantum-graph trace formulas distinguish a positive spectral measure from its signed expansion in periodic orbits. [Kottos–Smilansky, equations (26), (27), (32), (35), (36)](https://arxiv.org/pdf/chao-dyn/9812005) explicitly derive the logarithm of a secular determinant as a sum of traces of powers, then reorganize it by primitive orbits and repetitions. This is a useful precedent for prime powers and their primitive-length coefficient. It does not supply arithmetic bond lengths or a Weil boundary pairing.

Here we choose a simpler transport model that can be solved without quantizing an infinite graph. For each prime $p$, specify the length $a=\log p$ and return amplitude $r=e^{-a/2}=p^{-1/2}$. These are **arithmetic input data**; the theory has not selected the primes or the attenuation exponent. A complex field $v(s,x)$ on an oriented channel $0\le s\le a$ obeys

\[
(\partial_s+\partial_x)v=0,\qquad v(s,x)=v(0,x-s). \tag{1}
\]

Thus its endpoint is a translation. The variable $x$ carries arithmetic scale, and $s$ is distance along the auxiliary channel. Subdividing a channel while keeping its total length and vertex amplitudes fixed preserves transport. Rescaling $x$, changing length, or changing $r$ does not. No supersymmetric cancellation is assumed.

Use the positive space of complex channel amplitudes with Lebesgue $L^2$ norms. Complex conjugation is the adjoint real structure. Whole-line translations are unitary; their interval compressions are contractions with explicitly retained escape channels. A lossless vertex can use the unitary matrix

\[
\begin{pmatrix}r&\sqrt{1-r^2}\\-\sqrt{1-r^2}&r\end{pmatrix}. \tag{2}
\]

Global phase changes of all amplitudes commute with transport and preserve norms. More generally changing phases at internal ports while conjugating incident vertex matrices is a unitary change of basis. There is no quotient of physical edge states and no ghost metric. No nontrivial supermultiplet has been constructed for this candidate: adding a factorization supercharge would add no arithmetic information. Its independent positive mechanism is transport with unitary vertices, not cohomology.

## 2. A single prime, all its active powers, and the endpoint reservoir

Translate the input interval to $0<x<L$ only for the delay calculation. Thus here $f_+(x)=f(x-L/2)$; we call this translated function $h(x)$ to keep the central pole amplitudes unambiguous. Its norm equals that of $f$. Define explicitly

\[
(T_a h)(x)=\begin{cases}h(x-a),&a<x<L,\\0,&0<x\le a.\end{cases}
\]

The adjoint is $T_a^*h(x)=h(x+a)$ for $0<x<L-a$, zero otherwise. Let

\[
P_a=T_a^*T_a=\mathbf1_{(0,(L-a)_+)},\qquad
\Pi_a=I-P_a=\mathbf1_{((L-a)_+,L)}. \tag{3}
\]

Here $(L-a)_+=\max(L-a,0)$. The right cap $\Pi_a$ records amplitude that cannot make another full forward translation inside the observation interval. The strict support convention makes $T_a=0$ when $a\ge L$.

For every input $h\in L^2(0,L)$, prescribe the recirculating amplitude by

\[
u_h(x)=h(x)+r h(x-a)+r^2h(x-2a)+\cdots, \tag{4}
\]

with zero extension in every term. Only $ka<L$ matters. This solves $u_h=h+rT_a u_h$ uniquely. After specifying (4), write $W_{a,r}=(I-rT_a)^{-1}$. It is a finite geometric polynomial on the interval and has norm at most $(1-r)^{-1}$. Define the observable state

\[
h\longmapsto Y_{a,r}h=
\left(\sqrt{1-r^2}\,u_h,\quad r\Pi_a u_h\right)
\in L^2(0,L)\oplus L^2(((L-a)_+,L)). \tag{5}
\]

This measures a positive weighted residence amplitude and the endpoint correction. It is not asserted to be the output power of a passive scattering experiment with unit input normalization. The physical scattering observable is separately calculated below.

**Proposition (finite-horizon Poisson identity).** For all complex $g,h\in L^2(0,L)$,

\[
\langle Y_{a,r}g,Y_{a,r}h\rangle
=\langle g,\mathcal P_{a,r}h\rangle,
\quad
\mathcal P_{a,r}=I+\sum_{k\ge1}r^k(T_{ka}+T_{ka}^*). \tag{6}
\]

The sum is finite. In particular the distributional kernel is

\[
\delta(x-x')+\sum_{ka<L}r^k
[\delta(x-x'-ka)+\delta(x-x'+ka)]. \tag{7}
\]

**Proof.** Put $W=W_{a,r}$, $T=T_a$. Multiplication on the left and right by $I-rT^*$ and $I-rT$ gives

\[
W+W^*-I=W^*(I-r^2T^*T)W
=(1-r^2)W^*W+r^2W^*\Pi_a W. \tag{8}
\]

The last expression is the Gram operator of (5). Expanding the finite geometric series and using $T_a^k=T_{ka}$ proves (6). This proof also fixes all contact and endpoint terms.

If the second component of (5) is omitted, the error is the nonnegative operator $r^2W^*\Pi_a W$, not zero. If $a\ge L$, (5) has components $\sqrt{1-r^2}h,rh$, so its norm is exactly $\|h\|^2$, as required by the inactive-delay cutoff.

## 3. Exact arithmetic match — as a signed difference

Setting $a=\log p$, $r=p^{-1/2}$ in (6) proves

\[
-\sum_{p^k<e^L}{\log p\over p^{k/2}}
\langle h,(T_{k\log p}+T_{k\log p}^*)h\rangle
=a\left(\|h\|^2-\|Y_{a,r}h\|^2\right). \tag{9}
\]

The sum on the left in (9) is for **one fixed prime** and all its powers. The state $Y_{a,r}h$ is independently positive and covers all inputs, but the prime form is a **difference** involving its norm. In the first-prime interval $a<L<2a$, the nonzero paired parts of $-ar(T_a+T_a^*)$ have eigenvalues $\pm ar$. The arithmetic correction therefore cannot be (5)'s norm or any other independently positive additive component.

For a whole-line channel $U_a h(x)=h(x-a)$, the same calculation gives the familiar positive multiplier

\[
\mathcal P_{a,r}(\tau)={1-r^2\over 1-2r\cos(a\tau)+r^2}.
\]

A passive vertex (2) with a delayed internal return has external scattering map

\[
h\longmapsto \mathscr S_{a,r}h=(rI-T_a)W_{a,r}h.
\]

Its exact positive escape identity is

\[
I-\mathscr S_{a,r}^*\mathscr S_{a,r}
=(1-r^2)W_{a,r}^*\Pi_a W_{a,r}. \tag{10}
\]

It follows simply by subtracting $(rI-T)^*(rI-T)$ from $(I-rT)^*(I-rT)$. On the whole line this scattering is unitary, so its norm defect is zero. Its positive phase-delay observable, in our Fourier convention, is $i\overline{\mathscr S(\tau)}\partial_\tau\mathscr S(\tau)=a\mathcal P_{a,r}(\tau)$. The desired prime contribution instead has multiplier $a(1-\mathcal P_{a,r})$. Neither the positive scattering defect nor the positive phase delay is the prime form.

Thus a working positive model, a signed arithmetic expansion, and the correct diagonal accounting have all been obtained, but their identification as the same observable has failed at a specific equation, (9).

## 4. Why primitive loops produce $\Lambda(p^k)$, and where this stops

Let $z\in\mathbb C$ with $\operatorname{Re}z>-1/2$ and put $x_p(z)=e^{-(1/2+z)\log p}$, so $|x_p|<1$. One primitive loop has secular factor $1-x_p(z)$. The reciprocal Euler factor obeys

\[
\partial_z\log(1-x_p(z))^{-1}
=-(\log p)\sum_{k\ge1}x_p(z)^k. \tag{11}
\]

The logarithm counts a $k$-fold repetition with $1/k$; differentiating contributes $k\log p$, leaving **$\log p$** rather than $k\log p$. This is the precise part of the arithmetic coefficient explained by primitive-orbit calculus. The choice $x_p=e^{-(1/2+z)a}$ supplies the attenuation $p^{-k/2}$. These are calculations from specified labels, not a dynamical derivation of those labels.

For two **independent** primitive loops, the determinant is $(1-x_p)(1-x_q)$, whose logarithm adds. There are no mixed powers $x_p^j x_q^k$. A shared scalar return instead has denominator $1-x_p-x_q$. Its logarithm contains

\[
-\log(1-x_p-x_q)=x_p+x_q+\tfrac12x_p^2+x_px_q+\tfrac12x_q^2+\cdots. \tag{12}
\]

Differentiation creates a mixed length $\log p+\log q=\log(pq)$, with coefficient proportional to $\log p+\log q$. For distinct primes the Weil prime sum has $\Lambda(pq)=0$. A graph allowing paths that switch between the loops must cancel such mixed primitive cycles through an independently established rule. Orthogonality of independent loops avoids (12), but supplies no joint control against the gamma and pole terms.

Two additional limits matter. First, at the central line the infinite product over all primes is not absolutely convergent; absolute convergence of this Euler expansion requires $\operatorname{Re}z>1/2$. All finite-interval operator calculations above avoid this issue by a finite active set. Second, replacing the scalar secular factor by a finite-dimensional truncated delay determinant does not preserve the mechanism: for a strictly forward nilpotent matrix $T$, $\det(I-rT)=1$ and $\operatorname{Tr}T^k=0$, although $W-I\ne0$. The operator logarithm contains translations but its ordinary finite trace does not. A quantum-graph trace must use the actual closed-channel space, not silently identify it with the truncated arithmetic input space.

**Finite primitive-sector sign obstruction.** Suppose a fixed finite-dimensional return matrix $M$ is intended to reverse every repetition coefficient of a single primitive loop, so that $\operatorname{Tr}M^k=-r^k$ for every $k\ge1$, with $r\ne0$. Near $z=0$, the determinant identity would force

\[
\det(I-zM)=\exp\left(-\sum_{k\ge1}{z^k\operatorname{Tr}M^k\over k}\right)
=\exp\left(\sum_{k\ge1}{(rz)^k\over k}\right)={1\over1-rz}.
\]

The left side is a polynomial, so this is impossible. For a single loop, assigning phase $-1$ already shows the problem: odd repetitions change sign and even repetitions do not. The positive control $M=(r)$ gives $\operatorname{Tr}M^k=r^k$ and determinant $1-rz$. This is an obstruction to a **fixed finite sector and ordinary trace**, with all repetitions required. It does not exclude length-dependent growing matrices, extra primitive lengths, infinite sectors, or non-trace boundary observables. A negative supertrace could produce these signs but would no longer itself be the required positive norm. These sign and repetition issues are not claimed as novel discoveries; the determinant argument records their precise scope for this candidate.

## 5. Coherent amplitudes generate difference labels and diagonal costs

There is a different mixed-label problem in a Gram norm. For $0<a<b$, choose constants $\alpha,\beta>0$ and prepare

\[
h\longmapsto h-\alpha T_a h-\beta T_b h.
\]

Squaring gives

\[
\begin{split}
\|h-\alpha T_a h-\beta T_bh\|^2={}&\|h\|^2
+\alpha^2\langle h,P_a h\rangle+\beta^2\langle h,P_b h\rangle\\
&-\alpha\langle h,(T_a+T_a^*)h\rangle
-\beta\langle h,(T_b+T_b^*)h\rangle\\
&+\alpha\beta\langle h,(T_a^*T_b+T_b^*T_a)h\rangle.
\end{split} \tag{13}
\]

The actual mixed operator is

\[
(T_a^*T_bh)(x)=\mathbf1_{(b-a,L-a)}(x)h(x-(b-a))
=P_aT_{b-a}h(x), \tag{14}
\]

not an unrestricted translation. With $a=\log2,b=\log3,L=5/4$, both first-prime delays act, $T_a^2=T_b^2=T_aT_b=0$, yet (14) is nonzero. It has length $\log(3/2)$, absent from the target, and a specific cap at $L-a$. This is a clean case where a forward-product test misses the mixed-adjoint interaction.

For a general channel-valued amplitude $v_0h+v_pT_a h+v_qT_bh$, let $d_j=\|v_j\|^2$. To obtain desired off-diagonal coefficients $-c_p,-c_q$ and avoid the isolated unwanted difference kernel in this three-term ansatz, require

\[
\langle v_0,v_p\rangle=-c_p,\quad
\langle v_0,v_q\rangle=-c_q,\quad
\langle v_p,v_q\rangle=0.
\]

The Gram matrix is positive only if

\[
d_0\ge {c_p^2\over d_p}+{c_q^2\over d_q},\qquad d_p,d_q>0. \tag{15}
\]

This is Cauchy–Schwarz on the orthogonal span of $v_p,v_q$, or its two-column Schur complement. For whole-line outputs the total scalar diagonal is $d_0+d_p+d_q\ge2(c_p+c_q)$. On the interval the diagonal is the *position-dependent* $d_0I+d_pP_a+d_qP_b$; applying the whole-line scalar budget blindly would be wrong. Additional translations could provide cancellations not allowed in this three-term ansatz. Equation (15) is a scoped lower bound, not an impossibility theorem for arbitrary coherent channels.

## 6. Gluing retains memory, not just endpoint values

At a cut $c\in(0,L)$, split $h=h_-+h_+$ into functions supported on opposite sides. The prime cross interaction is

\[
-2\operatorname{Re}\sum_{ka<L} a r^k
\int_{c}^{L}\overline{h_+(x)}h_-(x-ka)dx, \tag{16}
\]

where the zero extensions enforce both sides of the cut. This needs the input history in a band of width $ka$; a single scalar endpoint trace is insufficient. In (4), the state $u_h$ transports that history, and both components of (5) must be retained under gluing. A closed loop's primitive phase is invariant under moving a subdivision vertex; deleting the amplitude crossing the cut is not such an invariant operation.

This contrasts with one gamma exponential, whose cross term factors through one scalar response at the cut. An infinite gamma tower needs infinitely many responses; arithmetic delays need history channels. Their interface spaces are different and cannot be identified without a map.

## 7. An exact full-form organization and the remaining theorem

Return to the centered $f\in C_c^\infty(I_L)$, retaining the exact $C(f),S(f),w_0$ of [01_RELATIVE_COMPLEX.md](01_RELATIVE_COMPLEX.md). Let $\mathfrak P_L=\{p\text{ prime}:\log p<L\}$, $\vartheta_L=\sum_{p\in\mathfrak P_L}\log p$. Apply $Y_p=Y_{\log p,p^{-1/2}}$ to $h(x)=f(x-L/2)$. Equation (9), summed over primes, gives the exact identity

\[
Q_{0,L}[f]=K[\widetilde f]+(w_0+\vartheta_L)\|f\|^2+2|C(f)|^2
-2|S(f)|^2-\sum_{p\in\mathfrak P_L}(\log p)\|Y_p h\|^2. \tag{17}
\]

This includes *every active prime power*, all poles and the exact gamma normalization. For every fixed $L$, define two independently positive maps

\[
\begin{split}
f&\longmapsto\mathcal B_L f=
(\Psi^{\rm kin}(f),\sqrt{\vartheta_L}\,f,\sqrt2 C(f)),\\
f&\longmapsto\mathcal R_L f=
(\sqrt{-w_0}\,f,\sqrt2 S(f),(\sqrt{\log p}\,Y_ph)_{p\in\mathfrak P_L}).
\end{split} \tag{18}
\]

Their component norms are ordinary Hilbert norms, and

\[
Q_{0,L}[f]=\|\mathcal B_L f\|^2-\|\mathcal R_L f\|^2. \tag{19}
\]

The first map has domain $\mathcal D_{\log,L}$; the second is bounded on $L^2(I_L)$ for fixed $L$. Neither map uses zeros or a square root of the target. Equation (19) is an **exact organization, not a positive realization**: the missing inequality is precisely $\|\mathcal R_Lf\|\le\|\mathcal B_Lf\|$. Calling the map between their ranges a contraction would assume that inequality. A physical conservation law or a local unitary dilation that proves it independently would be substantive; none has been constructed here.

The loop organization improves the arithmetic bookkeeping over attaching a separate square for each prime power. It explains primitive-length weights, specifies endpoint completion, distinguishes the connected-loop sum labels from Gram difference labels, and gives a concrete family to couple to the gamma complex. It has not explained the global sign or selected the finite contact constant.

## 8. Numerical diagnostics and exact scope

[The checker](calculations/check_models.py) verifies (6), (8), (10), and (13)–(14) on finite complex vector spaces and checks (9) by quadrature with the *actual* logarithmic delays. At $L=2.3$ it includes three powers of 2 and two powers of 3. At $L=0.5,p=2$ it verifies exact cancellation of the inactive loop's identity term. The largest observed genuine-log identity error is below $2\times10^{-15}$. Omitting the endpoint component gives a finite-matrix error about $2.49$, so that control detects the intended failure.

These are floating-point identity diagnostics. Finite-matrix eigenvalues of the isolated prime provide controls of both signs, not a proof about the full continuum Weil operator. The mathematical proofs above are algebraic and independent of these diagnostics. A more general graph could evade the tested failures through extra channels, but must then specify the extra diagonal and mixed-cycle terms and derive their cancellation.
