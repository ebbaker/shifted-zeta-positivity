# Internal review of the signed carrier, saddle and high stationary continuation

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the active reasoning effort is not exposed and is not
inferred. Separate-agent derivations and cross-checks are internal LLM
work, not independent mathematical validation.

## Reviewed work and verdict

- [Note 12](../notes/12_EXACT_CARRIER_DEFECT_AND_CUTOFF_EDGE_MASS_20261010.md):
  exact carrier defect, genuine stationary identity and uniform absolute
  cutoff-edge mass theorem.
- [Note 13](../notes/13_PHASE_CURRENTS_RELATIVE_CONES_AND_BANDWIDTH_OBSTRUCTION_20261010.md):
  phase currents, sufficient relative cone, narrow-band counterexample,
  complete shifted channel and exceptional sets.
- [Note 14](../notes/14_FIXED_PRODUCT_SADDLES_AND_SIGN_OSCILLATION_20261010.md):
  exact time-zero gamma insertion, fixed-product sign oscillation and
  matched endpoint payment.
- [Note 15](../notes/15_NONVACUOUS_HIGH_HEIGHT_SECOND_STATIONARY_SIGN_20261010.md),
  [checker](../numerics/check_high_stationary_s1_cell.py), and
  [record](../numerics/HIGH_STATIONARY_S1_CELL_RECORD_20261010.json):
  bounded nonempty high-height second stationary sign.

The stated identities, asymptotic scope and conditional interval result
pass this internal review. The numerical result assumes the complete
holomorphic disk approximation. No uniform genuine-theta sign, new
collision-exclusion coverage or RH conclusion is obtained.

## 1. Carrier and cutoff-edge audit

The prescribed carrier is the manuscript's Stirling expression, with
all of its physical drift retained. It is not an exact log-Gamma carrier.
Complex differentiation of alpha is denoted by \(\alpha_s\); all
primes in the operator formulas mean physical \(x\)-differentiation with
\(t,N\) fixed. These two clarifications were applied during review.

Conjugating \(D=\partial_x^2-a\partial_x+b\) by \(A\) gives
\[
A^{-1}D(Aq)=q''-\rho q'+\Omega^2q,
\quad \rho=\Omega'/\Omega,
\quad a=2\lambda+\rho,
\quad b=\lambda^2+\Omega^2+\lambda\rho-\lambda'.
\]
Substitution of the exact logarithmic derivative
\(-i\Omega+h\log n\) produces precisely the printed \(E_n\), with
\(E_1=0\). Differentiation of \(R=DH\), followed by elimination of
\(H\) on \(H''=0\), gives
\[
-H'H'''=(b-a'+ab'/b)H'^2-H'(R'-b'R/b).
\]
Division requires \(b,\Omega\ne0\), which hold eventually in the
specified sector. There is no division by \(H'\) in this identity.

The error operator is exactly
\[
(\partial_x+\lambda-b'/b)
(\partial_x^2-\rho\partial_x+\Omega^2)e.
\]
Its expansion retains the full third derivative and the Cauchy factors
\(6L^3,2L^2,L,1\). The signed sufficient criterion fixes the genuine
slope's sign only after paying its error and then pays both factors.
It does not assert an automatic relative margin near a vanishing slope.

The actual dictionary has
\[
\sigma=\tfrac12+\tfrac t2\Re\alpha
       =\tfrac12+\kappa/4+O(t/x^2),
\quad N=\lfloor\sqrt{e^L+t/16}\rfloor,
\]
so \(\log N=L/2+O(e^{-L/2})\) uniformly for
\(1\le\kappa\le3/2\). No restriction to a subsequence avoiding cutoff
transitions is needed. Differentiating first at fixed \(t,N\), and
only then evaluating along the sector, avoids differentiating the floor.

For \(y=\log(N/n)\), the limiting weight is \(e^{-y/2}\,dy\), and
\[
\beta_n\longrightarrow-\pi/8-iy/2,\qquad Z_n/b\longrightarrow-\pi/8-iy/2.
\]
The uniform majorant
\(u^{-3/4}(1+|\log u|)\), \(u=n/N\), is integrable at zero.
This pays the full small-index complement, including \(n=1\), and
justifies both absolute-mass limits. Their ratio tends to one;
this is not a bound for the ratio of the actual signed observations.
It rules out a fixed reserve from that absolute comparison, not every
possible reserve tending to zero.

## 2. Phase-current and generic-source audit

At \(H=2\Re F\), \(H''=0\), writing \(F''=iv\) gives
\[
|F''|^2\mathscr L_1
 =4\Im(F''\overline{F'})\Im(F'''\overline{F''}).
\]
At \(F''=0\) this identity loses its sign implication. The stated strict
first relative cone forces \(F'=0\) there, and therefore handles the
exceptional case. Continuity along the real stationary set alone would
not do so. The amplitude-phase identity retains both turning terms
\(ab'-ba'\) and \(CD'-DC'\), with the same explicit exceptional set.

For odd \(N\), the positive two-frequency example has
\[
H_N'(\pi/2)=-sN/(N+2),\quad
H_N'''(\pi/2)=-sN(3N+2),\quad
H_N''(\pi/2)=0.
\]
Its negative Laguerre sign and opposite phase currents are exact, with
nonzero complex \(F_N''\). The relative bandwidth tends to zero.
The Gaussian smoothing argument preserves the stationary violation by
the ordinary IFT; it claims no sharp compact support after smoothing.
These are generic-source obstructions, not counterexamples for theta.

The shifted complete channel retains its purely imaginary endpoint
correction, which has zero real observation. Spatial derivatives of the
shifted integral hold the contour height fixed. A moving contour changes
the individual phase currents through additional imaginary terms.
Consequently a phase-cone claim must specify its complete channel.

## 3. Exact saddle insertion and endpoint audit

The second and fourth order derivatives of the non-divisor logarithm
agree with the corresponding alpha derivatives because its two factors
depend on \(\mu+\nu\) and \(\mu-\nu\), with identical scaling \(1/4\).
Subtracting the two fourth-order readouts cancels \(b'''\) and leaves
\[
Q_P=m_4-m_2b^2+5m_2b'+2(b')^2-b^2b'-2bb''.
\]
The gamma amplitude constant \(512\), real-readout constants \(4096\)
and \(32768\), and phase shift \(-\pi/4\) were recomputed independently.
The balanced \(P=1\) term first appears through \(-b^2b'\); evaluating
the polynomial only at the saddle would miss it.

The original endpoint proof was strengthened during review. The primary
[Bessel connection formula](https://dlmf.nist.gov/10.27.E4) and
[I-function series](https://dlmf.nist.gov/10.25.E2), on the order circle
\(|\nu|=1/4\), bound the Bessel function and its first two Euler
derivatives by \(C_P|z|^{-1/4}\) on the bounded closed quadrant.
Cauchy in order then pays the required order derivatives. The source
and its spatial derivative are bounded by
\(C_Pe^{9s}(1+s^2)\) for \(s\le0\), uniformly up to the contour edge.
One integration by parts retains the endpoint and proves
\[
|N_{j,P}(x,a)|\le C_{j,P}e^{-2ax}/x.
\]
At the shrinking contour height this is negligible relative to the
fixed-product gamma terms along their sign subsequences. The transfer
to both signs of the actual matched summand is therefore valid.

The conclusion holds for fixed \(P\) at time zero. The positive-time
raw negative-half-line integral diverges; inserting the formal heat
multiplier does not fix it. The geometric width \(\sqrt x\) at
\(P\approx x/(4\pi)\) is not a proved uniform expansion or a replacement
for the \(O(x\log x)\) paid product cutoff. No time-zero statement here
refutes a sign restricted to the positive shrinking sector.

## 4. Outward high-height check

The generating checker ran successfully with all 22,066 terms. Its
SHA-256, matching the retained record, is

~~~text
d5f2ab504352b71c02625e4ef3332411ba3d8768a8df9d2ab83643b8d1b76c27
~~~

Both imported interval-source hashes were also verified. A separate
agent statically audited the implementation and used exact rational
arithmetic on the saved decimal strings to check all twelve signs,
products, four hulls, five candidate intervals and endpoint signs.
This record-consistency check is not a second complete summation.

The moments are regenerated at offset \(87.41\). The spatial transport
path is the full interval from offset zero to \(87.44\), while time
transport uses the actual final rectangle and \(10^{-8}\) time width.
Taylor remainders through derivative three use the absolute twelfth
moment. The third exponential derivative and every mixed time term
are present, as are the full physical normalizer dictionary and its
derivative bounds.

The third physical-jet Cauchy error is \(472.2189594\), rounded upward.
It is not hidden by small finite-sum transport errors. Fully paid
enclosures give \(K_1<-44.407\), \(K_3>298.863\), and opposite endpoint
signs for \(K_2\). Since \(H'''=AK_3>0\), the actual \(H''\) is strictly
increasing, yielding exactly one zero per time. Monotonicity of the
normalized \(K_2\) is not assumed.

The complete candidate band has
\[
H'H'''/A^2<-13941.9506.
\]
The positive quotient \(-H'''/H'\) is reported only after the denominator
has been rigorously separated from zero. It supplies no independent
relative theorem near a multiple zero.

## Remaining proof obligations

The continuation supplies a useful local sign certificate and more
precise failure tests for proposed uniform arguments. It still lacks a
signed complete-source estimate at positive time with a useful relative
margin as \(H_x\to0\) on \(H_{xx}=0\). A growing-product asymptotic must
retain its endpoints, transition and heat weights. The imported disk
interface and predecessor-neighborhood coverage retain their prior status.
None of these obligations is inferred from the bounded calibration,
the absolute-mass theorem, or the time-zero product calculation.
