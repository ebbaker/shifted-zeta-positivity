# Exact phase-current interface for the second stationary sign

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort is not exposed and is not inferred.
Internal derivation, not independent mathematical validation. This note
addresses Notes 5, 6, 9 and 10 of investigation 17; it proves no new
genuine-theta sign.

The companion [carrier-defect analysis](12_EXACT_CARRIER_DEFECT_AND_CUTOFF_EDGE_MASS_20261010.md) identifies the actual cutoff-edge arithmetic cost. The [high-height calibration](15_NONVACUOUS_HIGH_HEIGHT_SECOND_STATIONARY_SIGN_20261010.md) verifies a bounded genuine stationary branch; neither note claims a uniform phase cone.

## 1. An exact identity without dividing by a physical jet

In this note \(F\) denotes a complete complex channel with real observation
\(H=2\Re F\). It is distinct from the real normalized finite approximation
called \(F\) in Notes 12 and 15.

Let a real scalar observation be represented by a complete complex channel
\(H=2\operatorname{Re}F\), and define at fixed time
\[
 U=F',\qquad V=F'',\qquad W=F''',
\]
\[
 I_1=\operatorname{Im}(V\overline U),\qquad
 I_2=\operatorname{Im}(W\overline V).
\]
At a genuine physical stationary point \(H''=0\), write
\(U=p+iq\), \(V=iv\), \(W=r+is\), with all five coordinates real.
Then
\[
 I_1=vp,\qquad I_2=-vr,\qquad
 \mathscr L_1= -H'H'''=-4pr.
\]
Consequently the division-free exact identity is
\[
 \boxed{|F''|^2\mathscr L_1=4I_1I_2\quad\text{on }H''=0.} \tag{1}
\]
If \(F''\ne0\), the desired stationary sign is equivalent to
\(I_1I_2\ge0\). In particular, either of the two cones
\(I_1,I_2\ge0\) and \(I_1,I_2\le0\) is sufficient.

The exceptional set is essential. At a complex zero \(F''=0\), both currents
vanish regardless of \(H'H'''\); (1) says nothing. Analyticity alone does not
allow filling this case by continuity on the stationary set: a zero of
\(\operatorname{Re}F''\) can be isolated. A complete theorem must prove, for
example,
\[
 F''=0\Longrightarrow F'=0,
\]
or directly handle the exceptional stationary set. The former implication
makes the target zero at the exception and involves no division.

On a patch where both \(F'\) and \(F''\) are nonzero, put
\[
 b_1=\operatorname{Im}(F''/F'),\qquad
 b_2=\operatorname{Im}(F'''/F'').
\]
Then (1) has the especially simple form
\[
 \boxed{\mathscr L_1=4|F'|^2b_1b_2\quad\text{on }H''=0.} \tag{2}
\]
The quantities \(b_1,b_2\) are the spatial phase derivatives of consecutive
complex derivative channels. This is a useful interface only if their signs
can be estimated independently from the complete theta representation.
Imposing their product sign solely on the physical stationary set merely
rephrases the original scalar target.

## 2. A relative-error cone that pays all degeneracies

The following sufficient condition is stronger than the target but has a
natural perturbative interpretation. Let \(a_1,a_2\) be real and
\(\kappa_1,\kappa_2>0\), with
\(0\le\delta_1<\kappa_1\), \(0\le\delta_2\le\kappa_2\). Suppose the *complete*
channel obeys, pointwise on the required neighborhood,
\[
 |F''-(a_1+i\kappa_1)F'|\le\delta_1|F'|, \tag{3}
\]
\[
 |F'''-(a_2+i\kappa_2)F''|\le\delta_2|F''|. \tag{4}
\]
Then
\[
 I_1\ge(\kappa_1-\delta_1)|F'|^2,\qquad
 I_2\ge(\kappa_2-\delta_2)|F''|^2.
\]
Equation (3) also shows that \(F''=0\) forces \(F'=0\): otherwise the
imaginary part of \((a_1+i\kappa_1)F'\overline{F'}\) would exceed its
permitted error. Thus (1) proves everywhere on \(H''=0\), including all
complex-channel zeros,
\[
 \boxed{\mathscr L_1\ge
 4(\kappa_1-\delta_1)(\kappa_2-\delta_2)|F'|^2\ge0.} \tag{5}
\]
All coefficients may vary with the point. Since the hypotheses concern
actual successive jets, no omitted derivative of a varying coefficient is
implicit. A same-sign negative imaginary cone follows by conjugating \(F\).
The real growth rates \(a_j\) are unrestricted. This makes (3)--(4) compatible
with nonconstant normalizers, provided they are included in the actual jets.

A direct scalar counterpart requires no complex channel. If real functions
\(p,q\), \(q\ge0\), and a residual \(R\) satisfy
\[
 H'''+pH''+qH'=R,\qquad |R|\le q|H'|,
\]
then on \(H''=0\),
\[
 \mathscr L_1=q(H')^2-H'R\ge0.
\]
Both versions demand error *relative to the vanishing signal*. The absolute
truncation bound in Note 9 does not by itself supply such a condition. A
fixed absolute residual is insufficient arbitrarily close to a collision.

For absolute complex-jet approximations \(f_j\),
\(|F^{(j)}-f_j|\le\epsilon_j\), the exact paid current interface is
\[
 |I_k-\operatorname{Im}(f_{k+1}\overline{f_k})|
 \le |f_{k+1}|\epsilon_k+|f_k|\epsilon_{k+1}
       +\epsilon_k\epsilon_{k+1},\quad k=1,2. \tag{6}
\]
Separate common-sign margins in (6), plus the exceptional-set treatment,
would certify (1). This uses the same complete third-jet payment that was
large in the high cell of Note 6; it does not erase that payment.

## 3. Amplitude-phase form and the first relevant corrections

On a patch where \(F\ne0\), write
\(H=R\cos\theta\), \(R=2|F|>0\), and let
\[
 a=R'/R,\qquad b=\theta',
\]
\[
 C=a'+a^2-b^2,\qquad D=b'+2ab,
\]
\[
 E=C'+aC-bD,\qquad K=D'+bC+aD.
\]
Then
\[
 H'=R(a\cos\theta-b\sin\theta),
\]
\[
 H''=R(C\cos\theta-D\sin\theta),\quad
 H'''=R(E\cos\theta-K\sin\theta).
\]
Define two real quantities
\[
 P=b(a^2+b^2)+ab'-ba',
\]
\[
 Q=b(C^2+D^2)+CD'-DC'.
\]
At \(H''=0\), a division-free identity is
\[
 \boxed{(C^2+D^2)\mathscr L_1=R^2PQ.} \tag{7}
\]
Indeed, \(aD-bC=P\) and \(ED-KC=-Q\), while
\((\cos\theta,\sin\theta)\) is parallel to \((D,C)\) when this vector
is nonzero. Both sides vanish when \(C=D=0\), so (7) remains valid there,
but again loses its sign implication at that exception.

For constant logarithmic amplitude derivative \(a\) and constant phase
speed \(b\ne0\), the formula reduces to
\[
 \mathscr L_1=R^2b^2(a^2+b^2)>0
 \quad\text{at }H''=0.
\]
The obstruction lies in the phase-curvature corrections \(ab'-ba'\) and
\(CD'-DC'\), not merely in amplitude size. This also shows why retaining
only a leading reflected wave cannot decide a nearly cancelling branch.

One sufficient patchwise condition is \(b>0\), \(C^2+D^2>0\), together with
\[
 |ab'-ba'|\le(1-\eta_1)b(a^2+b^2),
\]
\[
 |CD'-DC'|\le(1-\eta_2)b(C^2+D^2),
\]
for \(\eta_1,\eta_2\ge0\). It yields
\[
 \mathscr L_1\ge R^2\eta_1\eta_2b^2(a^2+b^2).
\]
As in (3)--(4), the substantive input would be a complete-source bound on
these turning corrections relative to their corresponding squared
amplitudes. Neither modular evenness nor an absolute contour norm proves it.

## 4. Positive coefficients and arbitrarily narrow relative bandwidth fail

For any odd positive integer \(N\), let \(\nu=N+2\) and
\[
 H_N(x)=\cos(Nx)+\frac{N(N+1)}{(N+2)^2}\cos((N+2)x). \tag{8}
\]
Both cosine coefficients are positive, and the two positive frequencies
have relative separation \(2/N\to0\). At \(x_0=\pi/2\), put
\(s=\sin(N\pi/2)\in\{-1,1\}\). Since
\(\sin(\nu\pi/2)=-s\) and both cosines vanish,
\[
 H_N''(x_0)=0,
\]
\[
 H_N'(x_0)=-s\frac{N}{N+2},\qquad
 H_N'''(x_0)=-sN(3N+2).
\]
Therefore
\[
 \boxed{\mathscr L_1(H_N;x_0)
 =-\frac{N^2(3N+2)}{N+2}<0.} \tag{9}
\]
This is an exact genuine stationary violation, not a near-stationary
sample. It also avoids the complex-channel exception. For
\[
 F_N=\tfrac12\left(e^{iNx}+\frac{N(N+1)}{(N+2)^2}e^{i(N+2)x}\right),
\]
one has \(F_N''(x_0)=isN/2\ne0\). The currents satisfy
\[
 I_1=-\frac{N^2}{4(N+2)}<0,\qquad
 I_2=\frac{N^2(3N+2)}4>0.
\]
Equation (1) exactly reproduces (9).

There is also a smooth positive-density control. For each fixed \(N\),
replace \(H_N\) by \(e^{-\varepsilon x^2}H_N\), with
\(\varepsilon>0\) sufficiently small. Its Fourier density is a positive
sum of four Gaussian translates, even and Schwartz. Because
\(H_N'''(x_0)\ne0\), the ordinary IFT gives a nearby genuine zero of the
new second derivative; continuity preserves the strict negative sign (9).
This argument claims no sharp compact bandwidth for the smoothed source.
The atomic example already proves the exact narrow-band obstruction.
A local positive-time backward heat extension follows by weighting its
positive spectral density by \(e^{tu^2}\) for times below its Gaussian
integrability threshold; coefficients can be shifted so the violation
occurs at any chosen interior reference time.

Thus positivity of Fourier weights, symmetry and small relative bandwidth
cannot establish the desired sign. Cancellation can reverse one derivative
phase current while leaving the next with the opposite sign. A dominance
or relative phase-cone estimate must include precisely that cancellation.

## 5. What modular pairing would have to add

The full pairing in Notes 9--10 preserves the target and cancels algebraic
endpoint contributions before truncation. It proves neither (3)--(4) nor a
common-sign bound on the two exact currents. A representation change alone
cannot supply it: at physical stationarity (1) is algebraically equivalent
to the scalar sign whenever the divisor is nonzero.

There is also freedom in choosing a channel \(F\): adding \(iK\), for real
\(K\) on the real axis, leaves \(H\) unchanged while changing the separate
currents. A useful claim must fix the complete theta-derived channel and
retain its endpoints. The raw half-line channel has algebraic imaginary
endpoint terms even when the complete real observation is exponentially
small; they must not be mistaken for a uniform relative phase margin.

The meaningful next target is therefore one of the following, on a stated
unbounded region and with exceptional sets covered:

1. A complete-source proof of the relative successive-derivative cones
   (3)--(4), or weaker same-sign current inequalities with explicit zero
   handling.
2. A signed relation \(H'''+pH''+qH'=R\), \(q\ge0\), whose residual is paid
   relative to \(|H'|\), using modular/arithmetic structure.
3. A matched asymptotic that retains the terms controlling \(P,Q\) in (7)
   through their common vanishing scale, rather than a fixed absolute
   remainder.

The positive-spectrum control rules out treating generic spectral
concentration as the missing arithmetic input. No genuine theta claim or
RH implication is established here.

## 6. A well-defined endpoint-subtracted channel for testing the cone

There is a natural exact way to remove the algebraic imaginary endpoint
before asking for a phase estimate. Let
\(m_t(u)=e^{tu^2}\Phi_e(u)\) be the complete glued theta source of Note 9,
with its holomorphic extension to the source strip. This \(m_t\) is
distinct from the logarithmic Stirling carrier denoted by \(m_t(s)\) in
Notes 12 and 15. Fix \(0<a<\pi/8\), and define
\[
 F_a(x)=\frac12e^{-ax}\int_0^\infty e^{ixs}m_t(s+ia)\,ds. \tag{10}
\]
The single-source contour shift, justified by the same closed-strip decay,
gives
\[
 F_0(x)=F_a(x)+\frac i2\int_0^a e^{-xy}m_t(iy)\,dy.
\]
Complete evenness and conjugation make \(m_t(iy)\) real. Therefore
\[
 H_t(x)=2\operatorname{Re}F_a(x)
\]
for every real \(x\). This is an exact complete-source choice of channel,
with the algebraic endpoint removed by an imaginary correction whose real
observation is zero. Its physical spatial jet interface is
\[
 F_a^{(j)}(x)=\frac12e^{-ax}\int_0^\infty
 (is-a)^j e^{ixs}m_t(s+ia)\,ds,\qquad j=0,1,2,3. \tag{11}
\]
The contour height must be held fixed in these derivatives. One may choose
it separately for a physical center and keep it fixed throughout that
center's disk, as Note 9 does. If one instead defines a moving channel
\(F_{a(x)}\), extra endpoint derivative terms must be included. They are
purely imaginary on the real axis and do not change the physical jets,
but they do change the separate phase currents.

For comparison, repeated integration by parts in the unshifted half-line
channel gives
\[
 F_0(x)=\frac i2\left(\frac{m_t(0)}x-
 \frac{m_t''(0)}{x^3}+\cdots\right)
\]
with the usual finite-order remainder bounds supplied by integrable source
derivatives. All algebraic terms are imaginary because the source is even.
Consequently the leading endpoint products in \(I_1,I_2\) have zero
imaginary part. The current signs are then sensitive to much smaller terms
carrying the physical scalar information. The contour channel (10)
removes this explicit conditioning obstruction; it does not prove the
remaining currents have compatible signs.

This gives a concrete channel on which the relative cone question can be
posed without discarding unmatched raw boundary terms. It also sharpens
what a numerical next step should measure: the two current signs and their
relative margins for (11), using fixed contours and complete tail payments,
on genuine \(H''=0\) branches.
