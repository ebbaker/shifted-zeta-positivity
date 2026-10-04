# Higher-order reconstruction of the fixed prime response

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Internal analytic investigation, not independent specialist refereeing.

## Outcome and relation to earlier work

For the fixed weight of the [manuscript](../manuscript.tex), three-scale
symmetric extrapolation improves the short-interval approximation from
length \(X^{3/4}\) to length \(X^{11/12}\), with the same (O(X)) error
in the response's shell \(L^2\) norm. Consequently its exact signed
covariance has the same admissible variance exponents \(2+\delta\), for
every \(\delta\ge0\), as the original response. This extends the
[earlier second-order transfer](../../investigations/sonin-critical-boundary/notes/subpower-milestones/02_short_interval_transfer_and_gate_20261003.md).
It supplies more freedom in selecting the arithmetic interval length;
it supplies no fixed power saving, exponent descent, or new zero-free strip.

A search of the parent investigation notes found the second-order
transfer but no version of the Richardson or Peano-kernel extension
proved below. This records a project extension, not a priority claim.

Keep \(A=e^{-1/4}, B=e^{1/4}\), the complete zero-extended weight \(w\),
and \(V(x)=\sum_n\Lambda(n)w(n/x)\). For every real \(h>0\) and
\(x>0\), define

\[
D_h(t)=\psi(t+h/2)-\psi(t-h/2)-h,\qquad
V_h(x)=h^{-1}\int w(t/x)D_h(t)\,dt.
\]

In the approximation estimates below, impose \(1\le h\le AX\) on the
outer scale and \(X\le x\le2X\). The inner scales \(h/2\) and \(h/4\)
remain defined even when they are less than one.

The earlier finite-Fubini identity is exact for real \(x,h\):

\[
V_h(x)=\sum_n\Lambda(n)B_h[w(\cdot/x)](n),\qquad
B_hf(t)=h^{-1}\int_{-h/2}^{h/2}f(t+u)\,du.
\tag{1}
\]

Every expanded endpoint band is retained.

## 1. Two elementary improvements

The second moment of \(B_h\) is \(h^2/12\). Therefore

\[
R_{4,h}(x)=\frac{4V_{h/2}(x)-V_h(x)}3
\]

cancels the second-order Taylor term. Fourth-order Taylor remainder,
using the actual \(C^4\) zero extension, gives uniformly in every real \(n\)

\[
\left|\frac{4B_{h/2}-B_h}{3}[w(\cdot/x)](n)-w(n/x)\right|
\le\frac{\|w^{(4)}\|_\infty h^4}{4608x^4}.
\]

Summing over the complete expanded support and using
\(\psi(T)\le(4\log2)T\) yields
\(|R_{4,h}(x)-V(x)|\ll_w h^4/x^3\), hence

\[
\|R_{4,h}-V\|_{L^2[X,2X]}\ll_w h^4X^{-5/2}.
\tag{2}
\]

Thus \(h=X^{7/8}\) has \(O_w(X)\) norm error.

Now set

\[
R_{6,h}(x)=\frac{V_h(x)-20V_{h/2}(x)+64V_{h/4}(x)}{45}.
\tag{3}
\]

For scales \(a_i=(1,1/2,1/4)\) and coefficients
\(c_i=(1,-20,64)/45\), exact arithmetic gives

\[
\sum c_i=1,\qquad \sum c_i a_i^2=\sum c_i a_i^4=0,\qquad
\sum c_i a_i^6=1/64.
\tag{4}
\]

The fixed weight lies in \(W^{5,\infty}(\mathbb R)\): its first four
derivatives are continuous across the endpoints, and its fifth derivative
is bounded and piecewise smooth. Taylor expansion through degree four
is consequently legitimate with an absolute fifth-order remainder.
The resulting uniform bound is

\[
\left|\sum_i c_i B_{a_i h}[w(\cdot/x)](n)-w(n/x)\right|
\le\frac{\|w^{(5)}\|_\infty h^5}{614400x^5}.
\]

This alone gives norm error \(O_w(h^5X^{-7/2})\), permitting
\(h=X^{9/10}\). To reach order six, the endpoint jumps must be included
as measures rather than treating \(w\) as globally \(C^6\).

## 2. Exact sixth-order Peano kernel and endpoint atoms

For the unit-scale functional \(L=\sum_i c_iB_{a_i}-I\), all polynomial
moments through degree five vanish. Define the compactly supported,
even Peano kernel by, for \(v\ge0\),

\[
K(v)=\frac{(1/2-v)_+^6-40(1/4-v)_+^6+256(1/8-v)_+^6}{32400},
\qquad K(-v)=K(v).
\tag{5}
\]

This is \(L[(\cdot-v)_+^5]/5!\). The expression on the negative
half-line agrees with the even extension because \(L\) annihilates
degree-five polynomials. Set \(K_h(v)=h^5K(v/h)\). Repeated integration
of a sixth derivative measure gives the exact identity

\[
\sum_i c_i B_{a_i h}f(n)-f(n)
=\int K_h(t-n)\,d(D^6f)(t).
\tag{6}
\]

It applies to \(f(t)=w(t/x)\), for example by mollifying and passing
to the finite derivative measure. No derivative is discarded at a cap.

The kernel is nonnegative. Indeed, for \(0\le v\le1/4\),
\((1/2-v)^6\ge64(1/4-v)^6\), and beyond \(1/4\) only the first
term remains. Its exact mass and a convenient maximum are

\[
\int K(v)\,dv=\frac1{20643840},\qquad
\|K\|_\infty=K(0)=\frac7{33177600}.
\tag{7}
\]

For the mass, apply (6) to \(f(t)=t^6/6!\), using (4).
For the maximum, \(K\) decreases on the positive half-line. On
\([1/8,1/4]\), the ratio of the first and second fifth powers in
\(-K'\) is at least \(3^5>40\). On \([0,1/8]\), putting \(q=8v\)
reduces its sign to

\[
q(640-1120q^2+900q^3-217q^4)\ge0.
\]

For \(0\le q\le1\), the bracket is at least
\(640-1120q^2+683q^3\ge203\); its derivative is nonpositive on
that interval. The remaining interval is immediate.

Write the sixth derivative measure of the actual fixed weight as

\[
D^6w=q(u)\mathbf1_{(A,B)}(u)\,du+j_A\delta_A+j_B\delta_B,
\tag{8}
\]

where \(q=w^{(6)}\) on the interior is bounded,
\(j_A=w^{(5)}(A+)\), and \(j_B=-w^{(5)}(B-)\). More explicitly,
with the manuscript's exact normalization \(\nu\),

\[
j_A=\frac{8!\,8^8}{\sqrt\nu}A^{-11/2},\qquad
j_B=-\frac{8!\,8^8}{\sqrt\nu}B^{-11/2}.
\tag{9}
\]

To see (9), at either endpoint \(g^{(j)}=0\) for \(j<5\) and
\(g^{(5)}=-8!8^8/\sqrt\nu\). Five differentiations of
\(w(t)=t^{-1/2}g(-\log t)\) therefore leave only
\(-t^{-11/2}g^{(5)}\) at an endpoint.

Combining (1), (6), and (8) gives the exact residual

\[
\begin{split}
R_{6,h}(x)-V(x)
={}&x^{-6}\int_{Ax}^{Bx}q(t/x)\sum_n\Lambda(n)K_h(t-n)\,dt\\
&+x^{-5}\sum_{e\in\{A,B\}}j_e\sum_n\Lambda(n)K_h(ex-n).
\end{split}
\tag{10}
\]

The first line is bounded by

\[
\frac{\|q\|_\infty h^6}{20643840x^6}\psi(Bx+h/2)
\ll_w h^6/x^5.
\tag{11}
\]

For the second line use (7) and the mass of primes and prime powers in
the two closed bands \([ex-h/2,ex+h/2]\). Choosing closed bands here
handles all integer endpoint conventions; \(K_h(\pm h/2)=0\) also
makes the choice harmless in (10).

## 3. Elementary and sieve bounds for the cap bands

Since \(h\ge1\), each cap band contains at most \(h+1\le2h\)
integers, and \(\Lambda(n)\le\log n\). With \(x\asymp X\), this gives

\[
|R_{6,h}(x)-V(x)|\ll_w h^6\log X/x^5,\qquad
\|R_{6,h}-V\|_{L^2[X,2X]}\ll_w h^6\log X/X^{9/2}.
\tag{12}
\]

This version uses only elementary bounds and already permits

\[
h=X^{11/12}(\log X)^{-1/6}
\tag{13}
\]

with \(O_w(X)\) norm error, or any fixed pure power \(h=X^\tau\)
with \(\tau<11/12\). The logarithm in (12) must not be discarded at
the pure-power endpoint.

It can be removed using a precisely identified classical sieve theorem.
Montgomery and Vaughan's *The large sieve*, Mathematika 20 (1973),
119--134, Theorem 2 and its specialization (1.12), printed page 121,
state

\[
\pi(M+N)-\pi(M)<2N/\log N\qquad(M>0, N>1).
\tag{14}
\]

The original [author-hosted paper](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf)
was downloaded into temporary storage and page 121 was visually inspected
in this session; the [publisher record](https://doi.org/10.1112/S0025579300004708)
confirms the bibliography. A bounded endpoint adjustment covers closed
bands. Multiplying the prime count by \(\log(C_wX)\) gives prime mass
\(O(h\log X/\log h)\). The elementary identity
\(\psi(T)-\theta(T)=\sum_{k\ge2}\theta(T^{1/k})\), together with
Chebyshev, bounds all higher prime powers by \(O(\sqrt X\log X)\).
Consequently, for each fixed \(1/2<\tau<1\) and \(h=X^\tau\),
each cap-band mass is \(O_{w,\tau}(h)\), uniformly over \(x\in[X,2X]\).
Thus

\[
\boxed{\quad
\|R_{6,h}-V\|_{L^2[X,2X]}
\ll_{w,\tau}h^6X^{-9/2},\qquad h=X^\tau,\quad 1/2<\tau<1.
\quad}
\tag{15}
\]

In particular the pure power \(h=X^{11/12}\) has \(O_w(X)\) norm error.
The sieve theorem is used only as an upper bound on endpoint mass, not
as a centered mean-square power saving.

## 4. Exact signed covariance and exponent budget

Put

\[
\mathscr D_h(t)=\frac{D_h(t)-40D_{h/2}(t)+256D_{h/4}(t)}{45},\qquad
Q_{6,h}(X)=\int_X^{2X}|R_{6,h}(x)|^2\,dx.
\tag{16}
\]

The factors (40,256) include the normalizations of the narrower
intervals. In particular,

\[
R_{6,h}(x)=h^{-1}\int w(t/x)\mathscr D_h(t)\,dt.
\]

With the original Gram kernel
\(W_X(t,u)=\int_X^{2X}w(t/x)w(u/x)\,dx\), finite Fubini gives

\[
Q_{6,h}(X)=h^{-2}\int_{AX}^{2BX}\int_{AX}^{2BX}
\mathscr D_h(t)\mathscr D_h(u)W_X(t,u)\,dt\,du.
\tag{17}
\]

All signs between the three lengths and between the two coordinates are
retained. Equation (15) and the reverse triangle inequality imply

\[
\left|\sqrt{\mathcal V_g(X)}-\sqrt{Q_{6,h}(X)}\right|
\ll_{w,\tau}h^6X^{-9/2}.
\tag{18}
\]

Therefore, with the one choice \(h=X^{11/12}\), for every fixed
\(\delta\ge0\),

\[
\boxed{\quad Q_{6,h}(X)=O(X^{2+\delta})
\iff\mathcal V_g(X)=O(X^{2+\delta}).\quad}
\tag{19}
\]

For a raw arithmetic gate, set
\(S_6(X,h)=\int_{AX}^{2BX}|\mathscr D_h(t)|^2dt\).
Cauchy--Schwarz, \(\int w(t/x)^2dt=x\), and (15) give

\[
\mathcal V_g(X)\ll_w X^2S_6(X,h)/h^2+h^{12}/X^9.
\tag{20}
\]

If, for \(h=X^\tau\), an additional arithmetic theorem established
\(S_6(X,h)\ll Xh^2X^{-\kappa}L(X)\), with
\(L(X)=X^{o(1)}\), then (20) would prove every

\[
\delta>\max(0,1-\kappa,12\tau-11).
\tag{21}
\]

An unbounded \(L\) still does not give the frontier endpoint.
Alternatively, raw bounds of this form for each
\(S(X,a_i h)\), with its own length \((a_i h)^2\), imply the bound for
\(S_6\): the \(L^2\) triangle inequality costs at most
\((\sum|c_i|)^2=(17/9)^2\). This route does not exploit cross-length
cancellation, whereas a direct estimate in (17) could.

For comparison, the approximation contributions to the admissible
exponent are \(4\tau-3\) for one box, \(8\tau-7\) for \(R_4\),
\(10\tau-9\) using only the \(W^{5,\infty}\) estimate for \(R_6\),
and \(12\tau-11\) using (15). The corresponding lengths with quadratic
approximation cost are \(X^{3/4},X^{7/8},X^{9/10},X^{11/12}\).

## 5. What the regularity permits, and a relative-interval observation

Order six uses the finite measure \(D^6w\) at its actual endpoint
singularities. Higher Richardson cancellation by itself does not make
those atoms disappear. For a fixed finite collection of box scales, a
fifth-order endpoint kink contributes a layer of width \(h/x\), height
\((h/x)^5\), and integrated absolute size of order \((h/x)^6\).
Thus \(11/12\) is the endpoint furnished by this direct absolute
approximation method with the fixed weight. It is not an impossibility
theorem about all arithmetic methods, corrected endpoint formulas, or
other exact representations. In particular, signed cancellation could
improve an approximation estimate beyond its absolute-value bound.

For perspective, fixed relative intervals admit an exact representation
without a small approximation error. Choose \(0<r<\log2-a\), define

\[
E_r(t)=\psi(te^r)-\psi(te^{-r})-2t\sinh r,\qquad
U_r(x)=\frac1{2\sinh r}\int w(t/x)E_r(t)\frac{dt}{t}.
\]

Centering is exact because \(\int w=0\). Finite Fubini gives

\[
U_r(x)=\frac1{2\sinh r}\int_{-r}^r V(xe^u)\,du.
\tag{22}
\]

On a logarithmic mode \(p_g(y)=e^{sy}\), the corresponding normalized
response is multiplied by

\[
M_r(s)=\frac{\sinh((s+1/2)r)}{(s+1/2)\sinh r}.
\tag{23}
\]

Its zeros have real part \(-1/2\), and it never vanishes for
\(\Re s>-1/2\). The averaged probe has support
([-a-r,a+r]), still causal above the first packet, and transform
\(\widetilde G(-s)=G(-s)M_r(s)\). The same shell-to-Laplace argument
as the manuscript therefore excludes exactly the same right-of-strip
zeros; the converse follows from its absolutely summable zero series.
Hence the variance of \(U_r\) has precisely the same exponents as that
of \(V\). Its signed covariance is (17) with
\(\mathscr D_h(t)\mathscr D_h(u)/h^2\) replaced by
\(E_r(t)E_r(u)/(4\sinh^2r\,tu)\).

This optional observation reaches intervals of length comparable to \(X\)
through noncancellation, not through an (O(X)) approximation norm.
It offers no new arithmetic bound and is not a second central target.

## Verification and next use

Exact `Fraction` checks independently confirmed (4), the mass and maximum
in (7), and the \(1/614400\) fifth-order remainder constant. The Peano
kernel positivity, endpoint scaling, shell powers, and covariance
normalizations were derived above. The Montgomery--Vaughan primary
statement was visually checked, but its published sieve proof was not
independently reproved. No prime computation or large data set was run.

The useful deliverable is the signed three-length covariance (17) at
\(h=X^{11/12}\), together with its exact exponent equivalence (19).
It is available if an arithmetic argument works better at longer
intervals. An arithmetic power saving remains a separate theorem.
