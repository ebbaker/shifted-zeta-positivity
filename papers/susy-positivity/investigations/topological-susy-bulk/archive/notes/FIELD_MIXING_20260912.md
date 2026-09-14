# A positive low-mass mixing field: exact response and the next obstruction

12 September 2026. AI-assisted mathematical continuation. **This pass constructs and eliminates an explicit positive two-field channel. It cancels the previous remainder's entire inverse-square term, but leaves a nonzero inverse-fourth-power term and an infinite-rank error. It does not complete the Weil form or establish a new positivity range.** The proofs below are written analytic arguments, with exact rational checks and numerical diagnostics; they have not received independent specialist or formal verification.

The current attempt is in `papers/susy-positivity/attempts/topological-susy-bulk`. It was moved from `brainstorm`. Relevant background remains in [the topological note](../../brainstorm/TOPOLOGICAL_BULK_BOUNDARY_POSITIVITY_20260912.md), [the superspace companion](../../brainstorm/SUPERSPACE_COHOMOLOGICAL_BOUNDARY_PAIRINGS_20260912.md), and [the candidate package](../../brainstorm/candidate-bulk-theories/README.md). This pass follows §14 of [the preceding continuation](CONTINUATION_20260912.md).

## 1. What is being tested

A positive energy can contain extra response fields, and eliminating them can produce a nonlocal boundary form. That mechanism was suggested in the previous continuation. There are two materially different choices:

* Enlarge the variables over which the **unchanged** old energy is minimized. Its minimum can only decrease.
* Change a coefficient or a source map in the old energy while introducing a new field. The new minimum can move in either direction.

Section 3 proves that the first choice cannot complete the present loop-evolution norm, even with finitely many additional source amplitudes. Sections 4–7 develop one concrete instance of the second choice: split the derivative of a low gamma mode between the existing loop history and an ordinary derivative channel. All component norms are positive before elimination. A single dimensionless parameter controls the split; the response is calculated for the whole family before imposing a matching condition.

The background's distinctions remain essential. The ordinary norm of a harmonic state can be nonzero when its auxiliary supersymmetric energy vanishes. A quotient supplies representative independence, but changing its metric or differential need not preserve that norm. The construction here gives a closed relative complex and a positive boundary pairing. It supplies no local superspace action or Ward identity selecting arithmetic data.

## 2. Fixed model and notation

Let \(I_L=(-L/2,L/2)\), with

\[
\log2<L\le\log3,
\qquad f,g\in C_c^\infty(I_L;\mathbb C).
\]

Write \(F,G\) for zero extension to the whole line, and use
\(\widehat F(\tau)=\int F(x)e^{-i\tau x}\,dx\), with inner products conjugate-linear in the first argument. Set

\[
a_k=2k+\tfrac12,\qquad
B(s)=\sum_{k\ge0}\frac2{a_k}\frac{s}{a_k^2+s},
\qquad \ell=\log2,\quad r=2^{-1/2}.
\]

Use **full primitive histories**, including repetitions whose direct translations are inactive on this interval. The horizon-truncated generator is a different model. Let \(U_\ell F(x)=F(x-\ell)\), and put

\[
M=\exp\!\left[cI-2\ell\big((I-rU_\ell)^{-1}-I\big)\right],
\quad c=w_0=\psi(1/4)-\log\pi.
\tag{2.1}
\]

Its multiplier and real logarithmic modulus are

\[
m(\tau)=\exp\!\left[c-\frac{2\ell r e^{-i\ell\tau}}
 {1-r e^{-i\ell\tau}}\right],\quad
v(\tau)=\log|m(\tau)|,
\quad q(\tau)=|m(\tau)|^{-2}=e^{-2v(\tau)}.
\tag{2.2}
\]

The scalar \(q\) is a compliance multiplier; it is unrelated to the odd charge \(\mathsf q\). Both \(M\) and \(M^{-1}\) are bounded on every fixed Sobolev space. The previous positive pairing is

\[
Z(g,f)=\frac1{2\pi}\int B(\tau^2/q(\tau))
 \overline{\widehat G(\tau)}\widehat F(\tau)\,d\tau.
\]

Define the exact residual symbol

\[
\rho(\tau)=B(\tau^2/q(\tau))-B(\tau^2)-v(\tau).
\tag{2.3}
\]

For \(C(f)=\int f(x)\cosh(x/2)dx\) and
\(S(f)=\int f(x)\sinh(x/2)dx\), write

\[
P(g,f)=2\overline{C(g)}C(f)-2\overline{S(g)}S(f).
\]

Then the exact target is

\[
Q_{0,L}(g,f)=Z(g,f)+P(g,f)
 -\frac1{2\pi}\int\rho(\tau)
 \overline{\widehat G(\tau)}\widehat F(\tau)d\tau.
\tag{2.4}
\]

Every subsequent comparison uses (2.3), not a derivative at zero coupling. Contact and prime coefficients in (2.4) are those in the previous continuation; only the first 2-delay acts directly in this length range.

## 3. A restriction on adding response variables to the unchanged energy

The previous one-prime cusp contains a stronger sign consequence. Regard \(q\) as a function of \(\theta=\ell\tau\), and write

\[
q(\theta)-1=\sum_{n\in\mathbb Z}\beta_n e^{-in\theta}.
\]

The coefficients are absolutely summable, in fact exponentially decaying. For a nontrivial prime and \(c\le0\), strict Jensen gives

\[
\beta_0=\frac1{2\pi}\int_0^{2\pi}e^{-2v(\theta)}d\theta-1
 >e^{-2c}-1\ge0.
\tag{3.1}
\]

Choose a nonzero \(\phi\in C_c^\infty(J)\), where \(J\subset I_L\) has length less than \(\ell\), and set \(f_N(x)=e^{iNx}\phi(x)\). The exact asymptotic statement is

\[
\mathscr R[f_N]
=-\frac{\beta_0}{24N^2}\|\phi\|^2+O(N^{-3}),
\qquad
(Q_{0,L}-Z)[f_N]
=\frac{\beta_0}{24N^2}\|\phi\|^2+O(N^{-3}).
\tag{3.2}
\]

Here \(\mathscr R\) is the compression of the convolution with symbol \(\rho\). The constants depend on the fixed model and packet profile.

**Proof.** The previous tail formula is
\(\rho(\tau)=-(q(\tau)-1)/(24\tau^2)+O(\tau^{-4})\).
Set \(\tau=N+\eta\) in its pairing. On \(|\eta|<N/2\), replacing the denominator by \(N^2\) costs \(O(N^{-3})\), since \(\widehat\phi\) is rapidly decreasing. The complementary tail is smaller than any prescribed inverse power after using the boundedness of \(\rho\) near zero. For the leading term, expand \(q-1\) in its absolutely convergent Fourier series. Plancherel gives

\[
\frac1{2\pi}\int e^{-in\ell\eta}
 |\widehat\phi(\eta)|^2d\eta
=\langle\phi,U_{n\ell}\phi\rangle=0\quad(n\ne0).
\]

Thus only \(\beta_0\) survives, independently of the phase \(N\ell\). The pole amplitudes of \(f_N\) decay faster than any inverse power by integration by parts. This proves both formulas. The same estimates are uniform on any fixed finite-dimensional space of such profiles. In particular this is a sign statement about admitted compact tests, not an inference from a single whole-line multiplier value.

**Consequence.** No boundary form \(Z_{\mathrm{rel}}\) satisfying

\[
Z_{\mathrm{rel}}[f]\le Z[f]+\|\Lambda f\|_{\mathbb C^d}^2
\quad\text{for all smooth compact }f
\tag{3.3}
\]

with finite \(d\) can equal \(Q_{0,L}\). To prove it, take \(d+1\) linearly independent profiles supported in the same \(J\). For each large \(N\), a nonzero combination of their modulated versions lies in \(\ker\Lambda\). Normalize its profile in \(L^2\). Uniformity of (3.2) makes \((Q-Z)[f_N]>0\), contradicting (3.3). The argument also covers a fixed finite-rank Hermitian addition, by writing it through finitely many linear amplitudes and working on their common kernel. No smoothness assumption on those amplitudes is required beyond being defined on these tests.

This applies to the preceding schematic energy
\(\|JF-Du-Ew\|^2+\|Aw\|^2\), **when setting \(w=0\) recovers the old problem with the same source and coefficients**. In the infinite tower this must be interpreted through its channel energies and their admissible old minimizers; the divergent raw source is not an ambient Hilbert vector. Setting the new variables to zero still proves the required inequality. Field-valued \(w\) of infinite dimension does not evade this monotonicity.

The restriction does not apply when the old coefficients, source injection, or allowed old configurations are changed. It does not exclude jointly positive field theories in general. It is also distinct from the previous numerical evidence against *independent positive addition*, which concerns the opposite ordering and is not certified here.

**Control.** The positive scalar energy
\(|F-u-w|^2+s|u|^2+b|w|^2\), \(s,b>0\), has minimum
\(|F|^2/(1+s^{-1}+b^{-1})\), strictly below the old minimum
\(s|F|^2/(1+s)\). Pure relaxation really does implement such decreases; it fails here because (3.2) requires increases in infinitely many independent directions.

## 4. Define a positive derivative-splitting field

Fix one mass \(a>0\) and a parameter \(0<\delta<1\). Keep the source \(F\), and introduce fields \(u\in H^1(\mathbb R)\), \(w\in L^2(\mathbb R)\). Define

\[
\mathcal E_{a,\delta}[F;u,w]
=\frac2a\left(
\|F-u\|^2
+\frac{\|M(u'-w)\|^2}{a^2(1-\delta)}
+\frac{\|w\|^2}{a^2\delta}\right).
\tag{4.1}
\]

The derivative flux is split into two fields. One goes through the full loop evolution; the other has an ordinary positive cost. The loop constraints in the preceding continuation, §7, realize \(M(u'-w)\) without using a target spectral square root. The two positive weights are declared before minimization.

This is a change to the old derivative stiffness: setting \(w=0\) multiplies its cost by \(1/(1-\delta)\). Therefore it is outside the hypothesis of §3. The limit \(\delta\downarrow0\) recovers the old channel after forcing \(w\to0\).

For completeness, its relative complex is explicit. On ordinary Hilbert spaces \(E^0=L^2(\mathbb R;\mathbb C^2)\), \(E^1=L^2(\mathbb R;\mathbb C^3)\), put

\[
D_{a,\delta}(u,w)=
\left(u,\frac{M(u'-w)}{a\sqrt{1-\delta}},
\frac{w}{a\sqrt\delta}\right),
\quad \operatorname{Dom}D_{a,\delta}=H^1\oplus L^2.
\tag{4.2}
\]

Its first and third components control \(u,w\); the second and bounded inverse of \(M\) then control \(u'\). These observations prove closedness and closed range. If \(Y=(y_0,y_1,y_2)\), its actual adjoint is

\[
D_{a,\delta}^*Y=
\left(y_0-\frac{M^*y_1'}{a\sqrt{1-\delta}},
-\frac{M^*y_1}{a\sqrt{1-\delta}}+
\frac{y_2}{a\sqrt\delta}\right),
\quad \operatorname{Dom}D_{a,\delta}^*=L^2\oplus H^1\oplus L^2.
\tag{4.3}
\]

Here \(M^*\) reverses the histories; it is not replaced by \(M\). On the graded sum the odd operator \(\mathsf q(U,Y)=(0,D_{a,\delta}U)\) is nilpotent and has the adjoint determined by (4.3). The partner Hamiltonian is nonnegative on its natural domain.

Prepare the class of \(\sqrt{2/a}(F,0,0)\) in
\(E^1/\operatorname{ran}D_{a,\delta}\). It is nonzero for nonzero \(F\): exactness would force \(u=F\), \(w=0\), and \(u'=0\), hence \(F=0\) in whole-line \(L^2\). The harmonic representative is obtained by the following explicit minimization. Representative independence follows from this quotient; invariance under changing \(\delta\) does not.

## 5. Eliminate both fields and retain the full pairing

Define

\[
X(\tau)=(1-\delta)q(\tau)+\delta.
\tag{5.1}
\]

For fixed \(u\), the second field solves

\[
\widehat w_f(\tau)=\frac{\delta}{X(\tau)}i\tau\widehat u_f(\tau).
\tag{5.2}
\]

Indeed minimizing \(A|d-w|^2+B|w|^2\), with
\(A=|m|^2/(1-\delta)\), \(B=1/\delta\), gives the effective cost
\(|d|^2/X\). The first field therefore solves

\[
\widehat u_f(\tau)=\frac{a^2X(\tau)}{\tau^2+a^2X(\tau)}\widehat F(\tau).
\tag{5.3}
\]

The positive upper and lower bounds on \(X\) imply \(u_f\in H^2\) and \(w_f\in H^1\) for every \(F\in L^2\). All smooth complex inputs, both parities and arbitrary means are covered. The harmonic state is

\[
\Psi_{a,\delta}(f)=\sqrt{2/a}\left(
F-u_f,-\frac{M(u_f'-w_f)}{a\sqrt{1-\delta}},
-\frac{w_f}{a\sqrt\delta}\right).
\tag{5.4}
\]

Substitution into (4.3) verifies harmonicity. Completion of squares gives its exact polarized norm:

\[
Z_{a,\delta}(g,f)=\frac1{2\pi}\int
\frac2a\frac{\tau^2}{\tau^2+a^2X(\tau)}
\overline{\widehat G(\tau)}\widehat F(\tau)d\tau.
\tag{5.5}
\]

Replace the corresponding old channel in the tower by (5.5). With
\(T_a(\tau,X)=(2/a)\tau^2/(\tau^2+a^2X)\), the new full positive multiplier is

\[
\widetilde Z(\tau)=B(\tau^2/q)+T_a(\tau,X)-T_a(\tau,q).
\tag{5.6}
\]

The subtraction in (5.6) only removes the old channel that has been replaced. Positivity is established by the sum of its remaining positive channels and (4.1), before writing (5.6). The exact change is

\[
\Delta_{a,\delta}(\tau)=
\frac{2a\delta(q-1)\tau^2}
 {(\tau^2+a^2X)(\tau^2+a^2q)}.
\tag{5.7}
\]

It is bounded and \(O(\tau^{-2})\); no contact or prime delta coefficient is changed. The natural logarithmic form domain remains the same. The infinite source must still be projected channel by channel before taking its direct sum.

Equations (4.1)–(5.7) use whole-line fields and whole-line output energies. There are no imposed side walls at \(\partial I_L\). Restricting the fields to the input interval without eliminating the exterior would be a different response problem; no endpoint energy has been discarded here.

## 6. Exact cancellation of the first cusp, and a surviving third-derivative jump

The digamma expansion, after substitution of \(1/4+i\tau/2\), is

\[
B(\tau^2)=\log|\tau|-\log2-\psi(1/4)
-\frac1{24\tau^2}-\frac7{960\tau^4}+O(\tau^{-6}).
\tag{6.1}
\]

The external identity used here is [NIST DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2); the normalization is checked from [DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6). Both official displays were read in this pass. Substitution and the two rational coefficients were derived and checked separately in the accompanying program. No prior claim about the sign of the Weil form is used.

Write \(\widetilde\rho=\rho+\Delta_{a,\delta}\). Its inverse-square coefficient is

\[
\left(-\frac1{24}+2a\delta\right)(q-1).
\tag{6.2}
\]

Thus \(\delta=1/(48a)\) cancels this coefficient at **every phase**, including all translated first-derivative cusps. It is an admissible positive split for every gamma mass. For the proposed low mode \(a=1/2\), this is

\[
\delta=\frac1{24},\qquad X=\frac{23q+1}{24}.
\tag{6.3}
\]

This parameter was selected by a necessary matching equation in an independently positive family. It is not presented as a value forced by supersymmetry or arithmetic geometry.

At (6.3) the exact remaining symbol satisfies

\[
\boxed{\quad
\widetilde\rho(\tau)=\frac{d_4(\ell\tau)}{\tau^4}+O(\tau^{-6}),
\qquad d_4(\theta)=-\frac{(q(\theta)-1)(319q(\theta)+89)}{11520}.
\quad}
\tag{6.4}
\]

To check the constants, the inverse-fourth-power term is

\[
-\frac7{960}(q^2-1)+\frac14(X^2-q^2)
=\frac{-319q^2+230q+89}{11520}.
\]

For the stipulated \(c=w_0\), \(q>1\) at every real phase. An elementary bound suffices: \(w_0<-3\), and
\(v\le c+2\ell r/(1+r)<c+2\log2<0\).
Thus \(d_4<0\) pointwise. There is also a useful stronger one-prime scope: for any \(c\le0\), set \(\mu=\mathbb E q>1\). Then \(\mathbb E q^2\ge\mu^2\), so

\[
\gamma_0:=\mathbb E d_4
\le-\frac{(\mu-1)(319\mu+89)}{11520}<0.
\tag{6.5}
\]

This produces a local kernel obstruction even when \(q-1\) itself changes sign. Expand \(d_4(\theta)=\sum_n\gamma_n e^{-in\theta}\). The function

\[
\widetilde\rho(\tau)-\frac{d_4(\ell\tau)}{(1+\tau^2)^2}
\]

is \(O(\tau^{-6})\) and bounded near zero. Multiplying it by \(\tau^4\) gives an integrable function, so its inverse transform \(Q_4\) is \(C^4\). Since

\[
\mathcal F^{-1}(1+\tau^2)^{-2}(x)
=G_2(x):=\tfrac14(1+|x|)e^{-|x|},
\]

the residual kernel is

\[
\widetilde R(x)=\sum_n\gamma_n G_2(x-n\ell)+Q_4(x).
\tag{6.6}
\]

The series converges absolutely with the needed derivatives away from its shifts. The kernel is \(C^2\). Expanding
\(G_2(x)=1/4-x^2/8+|x|^3/12+O(x^4)\) shows

\[
\boxed{\quad
\widetilde R'''(0+)-\widetilde R'''(0-)=\gamma_0<0.
\quad}
\tag{6.7}
\]

The first cusp has been removed, but the third derivative has a nonzero jump. As in the earlier column argument, choose arbitrarily many distinct points in a subinterval of length less than \(\ell\). The translated columns \(\widetilde R(x-y_j)\) have distinct nonzero third-derivative jumps. They are linearly independent. Approximate delta inputs place these columns in the closed range of any hypothetical finite-rank integral operator, a contradiction. Thus the compression has infinite rank on every nonempty interval.

The smooth rank-two kernel \(2\cosh((x-y)/2)\) does not remove this jump. Consequently no finite collection of scalar boundary amplitudes can turn the fixed response (5.6), (6.3) into the full target. This is an analytic failure test for this specified field model, independent of quadrature signs. A field coupled through pole variables could still change an infinite-rank response; the exclusion is about a **net finite-rank correction**, not the number of named fields.

**Controls.** If there is no loop and \(c=0\), then \(q=X=1\), (5.7) vanishes, and the original gamma channel is recovered for every split parameter. For nonconstant one-prime data, (6.2) verifies a genuine successful cancellation by a positive field. The pole kernel really has rank at most two. These controls distinguish the present failure from a claim that positive fields cannot change continuous kernels.

## 7. Finitely many splits in the same family cannot remove the next term

For a finite set of masses, allow positive splits \(0\le\delta_k\le1\), with endpoints interpreted as limits. Put

\[
X_k=(1-\delta_k)q+\delta_k.
\]

The first-cusp matching condition is

\[
\sum_k2a_k\delta_k=\frac1{24}.
\tag{7.1}
\]

The next coefficient is

\[
d_{4,\mathrm{finite}}(q)
=-\frac7{960}(q^2-1)
 +\sum_k2a_k^3(X_k^2-q^2).
\tag{7.2}
\]

At \(c=w_0\), every \(q>1\) and \(1\le X_k\le q\), so (7.2) is strictly negative. More generally it is a quadratic polynomial \(Aq^2+Bq+C\) with \(A<0\), \(C>0\), and value zero at \(q=1\). Hence it factors as \((q-1)(Aq-C)\). For \(c\le0\), Jensen for this concave quadratic gives \(\mathbb E d_{4,\mathrm{finite}}\le d_{4,\mathrm{finite}}(\mathbb E q)<0\). The third-jump argument therefore still applies whenever (7.1) has removed the first jump.

Adding more independent channels of this particular convex-compliance type cannot complete the remainder. This does not exclude a coupled matrix of gamma modes, a frequency-dependent compliance with its own derivative dynamics, a source change, or an infinite construction with separately justified limits. No general theorem about those alternatives is claimed.

## 8. Checks, limitations, and what the background changes

The [checker](calculations/check_field_mixing.py) specifies (4.2) as a complex matrix at selected frequencies, minimizes it independently, and compares the resulting norm and equilibrium fields with (5.2)–(5.5). Its largest energy discrepancy is \(4.45\times10^{-16}\). Exact `Fraction` calculations verify the coefficients \(-1/24\), \(-7/960\), \(\delta=1/24\), and all coefficients in (6.4).

The [diagnostic record](results/field-mixing-diagnostics.json) also records phase-preserving large-frequency checks, packets of support diameter \(0.4<\log2\), a successful pure-relaxation control, and two resolutions of the previous smooth complex bump. For the fixed first-prime model it finds

\[
\beta_0\approx1.4775993\times10^6,
\qquad \gamma_0\approx-9.9923622\times10^{11}.
\]

The large coefficients reflect the strong multiplier scaling; the asymptotics start at correspondingly high frequencies. They are not estimates of every finite-interval pairing.

For the previous \(L=1\) complex bump the calculated defect changes from approximately \(-0.0008460031\) to \(-0.0008905513\). The blend increases the positive energy while the target stays fixed. These numbers remain floating-point evidence, without certified Fourier tails, quadrature errors or rounding bounds. **The old requested negative-defect certificate has not been supplied in this pass**, and is not a premise of the analytic obstructions. No full-form eigenvalue sweep was run.

The [fresh replay](results/loop-evolution-replay.json) reruns the preceding loop-evolution checker. Earlier relative-complex, historical positivity and literature audits retain their recorded status; they are not all freshly replayed or recertified here.

The background notes sharpen the interpretation in three ways. First, (5.4) is a surviving relative class of a different differential, not the cohomology class of a factor applied to its own input. Second, its physical pairing uses the ordinary Hilbert adjoint, with whole-line output and the source covered for every complex test. Third, neither \(\delta\), the loop data, nor the finite contact is derived from a protected observable. Subdivision of a transport realization with fixed return and total length represents the same \(M\); changing these data changes the pairing. No invariance under that change is claimed.

The old rational-transfer obstruction was also rechecked: after removing finite Blaschke zeros, the specified boundary logarithmic modulus forces the rational outer factor's logarithmic derivative to equal \(-2\ell r/(1-rz)^2\). A rational logarithmic derivative has only simple poles. The double pole is impossible. The old one-prime inverse-square subtraction and first-derivative jump \(+\beta_0/24\) have the stated sign. The control \(1-\alpha z\) has the admissible simple-pole logarithmic derivative and the familiar \(\alpha^n/n\) coefficients. These checks validate the stated scopes, without claiming novelty.

## 9. Giving the splitting field a derivative cost restores a first cusp

One immediate extension can be tested in this pass. Add \(\mu\|w'\|^2\) inside the parentheses of (4.1), with \(\mu>0\) and \(w\in H^1\). The energy remains positive. The same elimination gives

\[
X_\mu(\tau)=(1-\delta)q(\tau)
+\frac{\delta}{1+a^2\mu\delta\tau^2},
\qquad Z_{a,\delta,\mu}(\tau)=T_a(\tau,X_\mu(\tau)).
\tag{9.1}
\]

For any fixed positive \(\mu\), the leading residual coefficient is now

\[
\rho_{\delta,\mu}(\tau)
=\frac{(2a\delta-1/24)q(\ell\tau)+1/24}{\tau^2}
+O(\tau^{-4}).
\tag{9.2}
\]

It cannot vanish at all phases for nonconstant \(q\). There is also a direct finite-interval test, avoiding an inference from whole-line mismatch alone. The first complex Fourier coefficient \(q_1\) of \(q\) is strictly positive. To see it, expand

\[
q(\theta)=e^{-2c}\exp\!\left[4\ell\sum_{n\ge1}r^n\cos(n\theta)\right].
\]

On the unit circle this is an absolutely convergent product of power series in \(e^{i\theta}\) and \(e^{-i\theta}\) with nonnegative coefficients, including a strictly positive first coefficient. The cusp at the **active** shift \(\ell<L\) therefore forces \(2a\delta=1/24\). That leaves a constant inverse-square residual \(1/24\), giving the nonzero diagonal first-derivative jump \(-1/24\). A smooth pole kernel cannot cancel it. Thus this derivative-cost extension also fails the full matching test for every fixed \(\mu>0\). The added four-component matrix minimization is checked in the same diagnostic program.

There is no contradiction with §6: taking \(\mu\downarrow0\) before high frequency recovers (5.1), whereas taking high frequency first removes its constant compliance term. The two limits do not commute. This rules out this explicit derivative penalty; it does not rule out general dynamics for the mixing field.

## 10. Next decision

The next construction must change more than the number of pure relaxation fields, the number of convex compliance splits, or the derivative penalty in §9. A nontrivial source/history coupling or a matrix of jointly coupled masses could change the response in ways not covered here. Its positive bare form, adjoint, all-input preparation and complete eliminated symbol should be specified before judging it. The target still includes both pole amplitudes and the complete regular kernel. A finite-order tail match is a necessary test, not the desired identity.

For a candidate replacing finitely many scalar channels by compliances \(X_k(\tau)\) depending only on the loop phase, necessary whole-line tail conditions are

\[
\sum_k2a_k(q-X_k)=\frac{q-1}{24},\qquad
\sum_k2a_k^3(X_k^2-q^2)=\frac7{960}(q^2-1).
\tag{10.1}
\]

At \(c=w_0\), the second right side is positive. Therefore a diagonal response in this class must have at least one \(X_k>q\) at each phase: some effective channel must soften, while the first equation requires a weighted net stiffening. The all-stiffening family in §§4–7 cannot do both. These are useful necessary conditions for a new independently defined field system, not a prescription to reconstruct one from target eigenvalues. For finite-interval matching, test the diagonal and every active shifted coefficient; full phase-wise tail matching is a stronger preliminary filter.

No new all-length construction, arithmetic selection principle, superspace Ward identity, or proof of RH results from this pass.
