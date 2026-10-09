# Native coprime inverse test and the weighted response tail

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed;
the exact serving variant is not inferred. Same-model derivations and audits
are internal validation, not independent specialist review or formal verification.

This is the second ordered task following the
[source fourth-proof audit](16_SOURCE_FOURTH_MARKED_BRIDGE_20261009.md).
It tests the actual native \(g=1\) inverse-pair block before any absolute
packet estimate. The complete signed Euler resummation is exact and its
collision correction converges on the source's buffered contours.
Those contours reproduce the existing exponent and do not supply the
required \(1/540\) gain. A weighted large-response tail gives a precise
alternative correlation target. Neither target is proved here.

## 1 The native coprime block

Retain the original good ideals, native zero-extended character \(\psi_u\),
inverse annulus \(A_0\), \(D=U^r\), original whole slots, and
\[
 V_u=\mathbf1_{\mathcal C_+}(u)|S_u|^4|Q_J(u)|^2.
\]
The \(g=1\) term of note 14 is the real signed expression
\[
 T_1(u)=\sum_{(a,b)=1}
 \mu_F(a)\mu_F(b)\psi_u(a)\overline{\psi_u(b)}
 A_0(Na/D)\overline{A_0(Nb/D)}.                 \tag{1}
\]
It contains every balanced coprime pair in the original annuli. For large
\(U\), these pairs have \(N(ab)\ge c^2D^2\), so they survive the original
half-power ratio cutoff. This is an actual native algebraic test; no
formal phase model is identified with a detector bin.

Let \(L_u(s)\) denote the original good-Euler-factor Hecke \(L\)-function
for \(\psi_u\), including its row zeros, and \(L_u^{\rm conj}(t)\) the function
for the conjugate presentation on the same physical row.
In the initial region \(\Re s,\Re t>1\),
\[
 \mathscr E_u(s,t)
 =\sum_{(a,b)=1}\frac{\mu_F(a)\mu_F(b)\psi_u(a)
                         \overline{\psi_u(b)}}{(Na)^s(Nb)^t}
 =\prod_{p\ {\rm good}}\left(1-x_p-y_p\right),                  \tag{2}
\]
where \(x_p=\psi_u(p)(Np)^{-s}\), \(y_p=\overline{\psi_u(p)}(Np)^{-t}\).
There are exactly three local states: absent, left, and right. A common
prime is excluded by coprimality. The complete correction is
\[
 \boxed{\mathscr E_u(s,t)=
       L_u(s)^{-1}(L_u^{\rm conj}(t))^{-1}C_u(s,t),\qquad
 C_u(s,t)=\prod_{p\ {\rm good}}
 \left(1-\frac{x_py_p}{(1-x_p)(1-y_p)}\right).}                \tag{3}
\]
If \(\psi_u(p)=0\), all three factors at that prime are one.
The identity applies separately to either native orientation. Conjugating
the entire presentation also conjugates its fixed ray factor; flipping
only the symbol orientation at a fixed ray factor is not that operation.
There is no deletion of a physical zero.

On compact real ranges with \(\Re s,\Re t\ge\sigma_0>0\) and
\(\Re(s+t)\ge1+\delta\), the individual denominators stay away from zero and
\[
 \left|\frac{x_py_p}{(1-x_p)(1-y_p)}\right|
 \le \frac{(Np)^{-\Re(s+t)}}{(1-(Np)^{-\sigma_0})^2}.
\]
The sum over good prime ideals converges. Therefore the correction product
is holomorphic and uniformly bounded there, independently of the row and
the imaginary parts. A zero of a finite correction factor is allowed by
this statement; no lower bound or cancellation of reciprocal poles is
inferred. In particular both real parts greater than \(1/2\) suffice.
Equation (3) supplies a meromorphic continuation through this domain
where the reciprocal functions are defined. It does not supply bounds
across their poles.

There is a stronger conclusion in the narrower domain needed here.
Good Eisenstein prime ideals exclude all primes above 6, hence have norm
at least 7. If both real parts exceed \(1/2\), then
\(|x_p|+|y_p|<2/\sqrt7<1\). Every local numerator and denominator in
(3) is nonzero. Absolute convergence then makes \(C_u\) nonvanishing.
On closed real ranges \(\Re s,\Re t\ge1/2+\delta_0\), it is bounded
above and below by positive constants uniformly over rows and heights:
handle the finitely many small prime factors separately and use the
summable bounds on \(C_{u,p}-1\) for the remaining product.
Thus this correction cannot cancel a reciprocal pole in this narrower
domain. This statement uses the actual good-prime exclusions; it is not
a lower bound for the selected correlation integral.

With \(\widehat A_0(s)=\int_0^\infty A_0(x)x^{s-1}\,dx\), exact double
Mellin inversion on the initial absolute lines gives
\[
 T_1(u)=\frac1{(2\pi i)^2}\int\!\!\int
 \widehat A_0(s)\widehat{\overline{A_0}}(t)
 D^{s+t}\frac{C_u(s,t)}{L_u(s)L_u^{\rm conj}(t)}\,ds\,dt.       \tag{4}
\]
Conjugation of the profile is explicit:
\(\widehat{\overline{A_0}}(t)=\overline{\widehat A_0(\bar t)}\).
The expression in (4) is not replaced by the product of two absolute
Möbius sums or by a single scalar reciprocal value.

## 2 The exact contour budget

The primary [30 September companion manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
printed pp. 56–58, was inspected in memory. Its SHA-256 is
8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7.

For a bin parameter \(a\), put \(d=2a-1\). Source Lemmas 8.1–8.2 bound
the reciprocal on central contours at real part \(a+6e\), where \(e>0\)
is the preliminary buffer. Pure twists and additional frequencies obey
the one cumulative source allowance in each \(L\)-argument. The vertical
tails stay on the absolute line, with finite smooth orders chosen in the
source order; an infinite unbuffered contour shift is not authorized.

Using precisely this central rectangle in (4), its reciprocal bounds,
the uniformly bounded correction, and the original permitted seminorms
gives
\[
 D^{-1}|T_1(u)|\ll_\varepsilon
       U^\varepsilon H^bD^{\,2a+12e-1}
       =U^{(d+12e)r+\varepsilon}H^b.                         \tag{5}
\]
Horizontal joins and separate tails are controlled with the original
finite height allocation and sufficiently large fixed tail orders.
Pure norm twists are placed in their respective \(L\)-arguments first;
the tail estimates differentiate the untwisted profile transforms.
Increasing the later external tail order does not increase the already
fixed internal height order. Each \(L\)-argument keeps its original
cumulative frequency allocation.
All occurrences of the reciprocal remain inside the same buffered
rectangle. The corresponding deleted-\(g\) version uses the same argument
with the correction product \(C_{u,g}\) omitting primes dividing \(g\).
The deleted reciprocal factors are obtained from the original ones by
the safe finite products \(\prod_{p\mid g}(1-x_p)^{-1}\) and
\(\prod_{p\mid g}(1-y_p)^{-1}\), which cost an arbitrarily small power
for polynomial-size \(g\) on these contours. No potentially zero
correction factor is divided out. This agrees with note 14's
fixed-gcd estimate.

Thus summing (5) against the selected fourth mass gives
\(U^{1+dr+12er+\varepsilon}H^b\). The literal buffer is
\(\rho=12e\), not an arbitrarily small loss after \(e\) is fixed.
For the high-gcd and completed-gcd removals in notes 14–15, the explicit
allocation \(\rho\le10^{-5}\) therefore requires
\(e\le1/1200000\), as well as the source's target-dependent \(e_0\)
and all its remaining height and loss conditions.

For an *absolute central-contour bound* to give the desired fixed saving
\(\chi=1/540\), the scale factor in (4) instead needs
\[
 \Re s+\Re t\le 1+d-\frac{\chi}{r}
                  =2a-\frac{\chi}{r}.                      \tag{6}
\]
A symmetric choice is \(a-\chi/(2r)\) in both variables. Its distance
below the source central line is \(6e+\chi/(2r)\).
Throughout \(7/10\le r<73/100\),
\[
 \frac5{3942}<\frac{\chi}{2r}\le\frac1{756}.
\]
These real parts still exceed \(1/2\) in the present \(a\)-range, so the
collision correction is not the obstacle. The missing reciprocal
control is. The source bin gives zero-free control only to the right
of its buffer; it can contain a witness zero with real part in
\([a,a+e)\). Moving below \(a\) is not justified and, for a matching witness
presentation, can cross a reciprocal pole. The correction cannot cancel
such a pole while both real parts exceed \(1/2\). A Mellin profile or
a signed average may still cancel particular residues, but no such
estimate has been supplied. Ignoring the residues would assume the new
zero-exclusion conclusion that the program is trying to prove.

This diagnoses a limitation of the absolute-contour route, not a lower
bound for (1), an impossibility theorem, or a proof that a row average
cannot gain. Oscillation on the existing contour or a selected average
of the full expression may still supply the missing correlation.
Proving only the \(g=1\) bound would also not control the remaining
\(1<Ng<G_0\) sectors. A uniform version with the natural
\(g^{-1-d}\) decay, or a bound for their complete signed aggregate,
is needed.

## 3 A precise positive alternative: weighted inverse response tail

Put \(q_u=|M_u|^2\), \(\chi=1/540\), and
\[
 \mathcal B=\{u\in\mathcal C_+:q_u>U^{dr-2\chi}\},\qquad
 T(t)=\sum_{u\in\mathcal C_+:\ q_u>t}V_u.
\]
The mass of the complement is immediately bounded:
\[
 \sum_{u\notin\mathcal B}V_uq_u
       \ll U^{1+dr-2\chi+\varepsilon}H^b.
\]
Consequently the new correlation statement
\[
 \boxed{\sum_{u\in\mathcal B}V_u
                  \ll U^{1-\chi+\varepsilon}H^b}            \tag{7}
\]
together with the original pointwise inverse envelope implies the desired
\(F_J\ll U^{1+dr-\chi+\varepsilon}H^b\).
Equation (7) is sufficient and stronger than necessary.
Here the envelope with exponent \(dr+\varepsilon\) uses the source's
procedure of choosing its buffer for each requested small loss. If the
buffer has already been fixed, so the literal pointwise exponent is
\((d+\rho)r\), (7) must instead save \(\chi+\rho r\) in its mass exponent.
For a fixed positive allocation margin \(\delta_{\rm tail}\), a robust
version is \(\sum_{\mathcal B}V_u\ll
U^{1-\chi-\rho r-\delta_{\rm tail}+\varepsilon}H^b\).
The complement has spare saving \(\chi\); that spare does not erase a
fixed buffer loss in the high-response contribution.

A less restrictive exact formulation uses layer integration. If the
actual pointwise bound gives \(q_u\le B_U\), then, for
\(t_0=U^{dr-2\chi}\),
\[
 F_J=\sum_uV_u\min(q_u,t_0)
             +\int_{t_0}^{B_U}T(t)\,dt.                    \tag{8}
\]
Thus a bound for the integral at the mixed target is sufficient, without
requiring the uniform cutoff mass in (7). This identity holds for the
finite physical row family even with sharp selectors.

The scalar facts \(\sum V_u\ll U\) and \(q_u\ll U^{dr}\) alone give no
saving in (7) or (8): their maximum envelopes permit the fourth mass to
sit entirely on large inverse responses. Such scalar examples are
diagnostics of the available inequalities, not native detector examples.
Unweighted counts of \(\mathcal B\), or global inverse mass, do not supply
the \(V_u\)-weighted correlation. The high-response route therefore
isolates the same missing dependence in a positive form.

## 4 What the test changes next

The \(g=1\) resummation uses the actual Möbius coefficients, annular balance,
native orientation, and physical zero convention. It rules out promoting
the existing buffered absolute contour estimate into the new theorem.
The marked Gauss estimate in note 16 and the weighted tail (7) remain
concrete sufficient alternatives. The next source/application audit must
now retain the literal buffer \(12e\), actual original slot identities,
and simultaneous witness losses; an arithmetic sample slot vector does
not certify those data.
