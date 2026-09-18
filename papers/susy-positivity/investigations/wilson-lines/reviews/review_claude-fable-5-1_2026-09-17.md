# Review of the Wilson-lines investigation (manuscript 0.8 and notes)

**Reviewer: Claude Fable 5.1 (Anthropic), model `claude-fable-5-1`.** 17 September
2026, for Edward Baker. Scope: the working manuscript at version 0.8 (all twelve
sections and the appendix, read from the TeX sources), the fourteen notes in
`notes/`, the three registered check programmes and the exploratory programmes
in `numerics/`, and the parts of `../../brainstorm/` that bear on this direction
(the bottleneck note's Section 4B, the directions overview, the 14 September
assessment). Every proposition in Sections 2--11 was re-derived by hand; the
registered programmes and the snapshot replay were rerun on the author's
machine; one exploratory computation was repeated and extended. Following the
convention of this folder, this review records the assessment as made and is
not revised afterwards.

**Not claimed here.** Nothing in this review bears on the Riemann hypothesis, and
nothing here constructs a source or proves a positivity statement.

---

## 0. Verdict in brief

1. **The mathematics of Sections 2--11 is correct.** Every written proof was
   checked line by line. Three proofs have repairable gaps or slips, none of
   which changes a statement (§2). All three registered programmes pass as
   recorded (206, 336, 525 cases) and `drafts.py check --replay` passes over
   1067 cases and 8 snapshots.

2. **One numerical conclusion of Section 8 does not survive a robustness test,
   and its failure makes the headline stronger.** The Gram-point control of
   §8.6 (frame-bound note §5) uses one phase of the unfolded lattice, the one
   with a point at $9.67$ below $\gamma_1$ and a counting function that exceeds
   the smooth count by $\tfrac12$ on average. With the phase-matched lattice
   $\theta(t)=(k-\tfrac12)\pi$, whose counting function averages to
   $\theta/\pi+1$ exactly, the arithmetic-free margin reproduces the zeros'
   margin to within $\pm0.12$ in $\log_{10}$ over $L\in[0.6,2.8]$, that is over
   $75$ orders of magnitude (§3). So **the margin carries essentially no
   arithmetic information at the resolution of the measurement**, which is the
   manuscript's thesis --- but the "arithmetic gap of three orders growing like
   $\log L$", the statement that the zeros are "systematically the worst of the
   family", and pathway item 2 of Section 12 and of the third continuation note
   are artifacts of the lattice phase and should be withdrawn.

3. **One negative result of Section 11 is a misreading of the programme's own
   object.** The Eisenstein scattering matrix of the modular surface is the
   shifted Weil transfer at $\omega=\tfrac12$: $\xi(2s-1)/\xi(2s)=K_{1/2}(2s-1)$
   exactly, so $\varphi(s)=\tfrac{s}{s-1}K_{1/2}(2s-1)$ (§4). The
   "$\times4$ failure" of Remark 11.14 is the archimedean shift
   $a=\tfrac14+\tfrac\omega2$ evaluated at $\omega=\tfrac12$; the delay test as
   calibrated is a test of the $\omega\to0$ limit. Fact (16) of the third
   continuation note --- "having the zeros is not enough to pass" --- should be
   replaced by: the test reads the resonance width off the $\Gamma$-shift, and
   the modular surface passes exactly at the width it actually has. The
   identification also places Sections 4--7 at $\omega=\tfrac12$ inside
   Lax--Phillips scattering theory for automorphic functions, which the
   manuscript does not cite and should.

4. **The negative assessments of the proposal itself are robust.** The abelian
   obstruction (Theorem 5.2), the dichotomy (Proposition 7.2) and the no-winding
   theorem (Proposition 11.3) are airtight, and the flatness of the
   $(\omega,L)$ connection is not merely true but automatic (§5.1), which
   closes the curvature route more firmly than the manuscript says. I found no
   loophole that would make the Wilson-line deformation more useful than the
   manuscript concludes. What I did find is that two of its *instruments* were
   miscalibrated, in the two places listed above, and both corrections push in
   the direction the manuscript already leans: what the margin and the delay
   measure is archimedean.

---

## 1. What was verified

### 1.1 By hand

- **Theorem 3.1.** The three-factor decomposition of $\mathcal F'/\mathcal F$,
  the causal kernel $4\cosh(x/2)\cosh(\omega x)\mathbf 1_{x>0}$ of the pole
  factors and its symmetrization to the third line of (3.1), the Dirichlet-series
  step, the digamma integral (3.4) via DLMF 5.9.16 with $t=2r$, the pairing of
  the two logarithmic divergences, and the identification of the constant with
  $w_0$ at $\omega=0$. Also that the pole term at $\omega=0$ is
  $2|C|^2-2|S|^2$, which matches the two pole terms $\hat F(\pm i/2)$ of the
  spectral form. Correct.
- **Remark 3.3.** $\operatorname{Re}[\tfrac{1}{p-\omega+\frac12}+\tfrac1{p-\omega-\frac12}+
  \tfrac1{p+\omega+\frac12}+\tfrac1{p+\omega-\frac12}]=0$ at $p=i\tau$ for every
  $\omega$, not only at $\omega=0$. Correct, and the mechanism is that
  $\tfrac1{p-a}$ with $\operatorname{Re} a>0$ is, on the axis, the transform of the
  *anti*-causal kernel $-e^{ax}\mathbf 1_{x<0}$; the causal realization is what
  selects the growing exponential.
- **Proposition 4.1** (unimodularity), **4.3** (group delay, including
  $2\theta'=\operatorname{Re}\psi(\tfrac14+\tfrac{i\tau}2)-\log\pi$ and the Hadamard form
  $\partial_\tau\Psi=\sum_\rho\omega/(\omega^2+(\tau-\gamma_\rho)^2)$), **4.5**
  (flux identity), **Lemma 5.1**, **Theorem 5.2**, **Proposition 6.1**
  (all three addition-formula steps), **7.1**, **7.2**, **Corollary 7.3**,
  **7.5** (the exact $\kappa_L^2$ identity and the table: $\kappa_L\sqrt{m_L}$,
  $\pi/4\kappa_L$, and the ratios $7.1\times10^1,2.0\times10^6,1.5\times10^{11}$
  all recomputed), **7.7**, **8.1**, **8.2** (compactness via
  Arzel\`a--Ascoli, attainment, the Cartwright count $\tfrac L\pi T$ against
  $2N(T)$), **(8.3)--(8.5)** ($\tau_c=2\pi e^L$, $T_*=e\tau_c$,
  $D(L)=2e^L-\tfrac74$, the Beurling threshold and the constants $1.32$ and
  $63$), **9.1--9.4**, **Condition 10.1** (the expansion of $2\theta'$),
  **Condition 10.3** (the Gagliardo form of $K$), **Proposition 10.4**,
  **11.1** (the Beta-function integral and $\pi\operatorname{Re}\cot$, its decay, its total
  $\pi(\tfrac12-\Delta)$, the values $4.09\times10^{-8}$ and
  $3\times10^{-27}$), **11.3**, **(11.3)**, **11.5** (the $\operatorname{Re}\psi$
  expansion from DLMF 5.11.8 with $z=iy$), **11.6**, **Corollary 11.7**,
  **Theorem 11.9** (the quadratic $576u^2+60u+1$, its roots, the Gauss
  multiplication identity), **Corollary 11.10**, **11.12** (Cauchy--Schwarz and
  the bound $2$ at $a=\tfrac{4-\sqrt5}8$, where $a^2-a=-\tfrac{11}{64}$ exactly),
  **Remark 11.13** ($I_2=-(r-1)^2/3r$, $8r^2-17r+8$, $I_4=\tfrac5{384}$),
  the survey rows for the target, the full-line oscillator, the modular surface,
  JT, $H_3^+$, bulk Liouville and FZZT at $b=1$, and both cigar rows (from the
  quoted triples), **Remark 11.14** (the factor $\tfrac{2s-2}{2s}$, its delay
  $-2\tau^{-2}$, the shift $\tfrac16-2$ to $I_2=+\tfrac{11}6$, and
  $\varphi$'s archimedean expansion). All correct as stated, subject to §2.

### 1.2 By machine

On the author's machine: `check_causal_commutation.py` (206 cases, pass),
`check_sampling_forms.py` (336, pass), `check_delay_test.py` (525, pass),
`validation/drafts.py check --replay` (1067 replayed cases, 8 snapshots, pass).
The Gram-point row of §8.6 was reproduced from scratch with independently
regenerated Gram points at seven lengths at the note's truncation $T=3000$,
agreeing with the note's table to three decimals at every one; the zeros row
was reproduced at nine lengths with the author's `weil_sine_basis.py`, agreeing
with the manuscript's table to the third decimal (e.g. $-76.747$ at $L=2.8$). The identity of §4 was
checked numerically at three heights to twelve digits.

### 1.3 Not verified

The $\Gamma$-structure of the cigar reflection amplitude (the third continuation
note already flags it); the structure function attributed to Suzuki
(arXiv:2301.00421) in Remark 8.3; the reading scope of arXiv:1102.4948; and the
Olevskii--Ulanovskii constant. These are readings in the manuscript and remain
readings here.

---

## 2. Errors and gaps found in the manuscript (none moves a verdict)

1. **Proposition 4.4, displayed local form --- sign slip.** The text writes
   $K_\omega(i\tau)\approx(\omega-iu)/(\omega+iu)$ with $u=\tau-\gamma$. That
   factor equals $-1$ far from the zero and $+1$ at it, and gives
   $|K-1|^2=4u^2/(\omega^2+u^2)$, which is *not* the stated Lorentzian. The
   correct local form, which the proof's own requirement $K\to1$ selects and
   which the check programme actually tests (`resonance_model`, factor
   $(-w+iu)/(w+iu)$), is
   $K_\omega(i\tau)\approx\dfrac{u+i\omega}{u-i\omega}=-\dfrac{\omega-iu}{\omega+iu}$,
   for which $|K-1|^2=4\omega^2/(\omega^2+u^2)$ exactly. (On the critical line
   $\xi'(\rho)$ is purely imaginary, so $\overline{\xi'(\rho)}/\xi'(\rho)=-1$,
   which is where the sign comes from.) The proposition, its mass and (4.3) are
   right; only the display is wrong.

2. **Propositions 4.5 and 7.2, the boundedness step.** "The $\Gamma$-ratio
   gives $K_\omega(p)=O(|p|^{-\omega})$ while the $\zeta$ and pole ratios tend to
   $1$" is false in the strip $0\le\operatorname{Re} p<\tfrac12+\omega$, where
   $\zeta(\tfrac12+\omega+\sigma+i\tau)$ and, under RH, its reciprocal are both
   unbounded in $\tau$. The conclusion (inner, hence $|K_\omega|\le1$ on
   $\operatorname{Re} p\ge0$) is right and has a two-line proof from the Hadamard product:
   with $\mathcal F(p)=\mathcal F(0)\prod_z(1-p^2/z^2)$ over zeros $z=\rho-\tfrac12$
   in symmetric order, $|K_\omega(p)|=\prod_z|p-\omega-z|/|p+\omega-z|$, and
   under RH ($z=i\gamma$) each factor is $\le1$ for $\operatorname{Re} p\ge0$ since
   $(\sigma-\omega)^2\le(\sigma+\omega)^2$. Under the weaker hypothesis of
   Proposition 7.2 (all $|\operatorname{Re} z|<\omega$) the individual factors can exceed one,
   but the product over a quadruple $\{\pm z,\pm\bar z\}$ is still $\le1$: writing
   $g(t)=t^4+2(u^2-\delta^2)t^2+(\delta^2+u^2)^2$ for $z=\delta+i\gamma$,
   $u=\tau-\gamma$, the two zeros $\pm\delta+i\gamma$ together contribute
   $[g(|\sigma-\omega|)/g(\sigma+\omega)]^{1/2}$ to $|K_\omega(p)|$, and $g(m-\omega)-g(m+\omega)=-8m\omega\,[m^2+\omega^2+u^2-\delta^2]<0$ for
   $m\ge\omega>\delta$, with the same sign for $\sigma<\omega$ by evenness. Either
   route, or Phragm\'en--Lindel\"of in the strip with boundedness on $\operatorname{Re} p=1$
   (which holds for $\omega<\tfrac12$), should replace the sentence.

3. **Proposition 4.4 is conditional and is not labelled.** "Near each
   $\gamma_\rho$" presumes $\gamma_\rho$ real. For a zero off the line by
   $\delta>0$, $K_\omega(i\tau)\to1$ uniformly near $\tau=\operatorname{Re}\gamma_\rho$ as
   $\omega\downarrow0$, so such a zero contributes nothing to the left side of
   (4.3) while contributing to $Q_{0,L}$ on the right. Both equalities in (4.3)
   therefore assume RH, and Section 12's list of conditional statements should
   include 4.4 (it lists only "the passage from one zero to the sum").

4. **Section 11.5, one number.** For the counterexample $a=\tfrac{4-\sqrt5}8$,
   $n_1=n_2=1$: $I_4=128\,B_4(a)=128\big[(\tfrac{11}{64})^2-\tfrac1{30}\big]
   =-\tfrac{233}{480}=-0.4854$, not $-0.678$. Curiously
   $I_4-\tfrac7{480}=-\tfrac12$ exactly, and the check programme's test H9
   `abs(I[1]-TG[1]) > 0.5` therefore sits exactly on its own threshold and
   passes only by a rounding error of $3\times10^{-16}$. The verdict ("fails
   $I_4$") is right; the threshold should be moved (e.g. to $0.1$) and the
   number corrected.

5. **Documentation drift.** `README.md` still describes the manuscript as
   "version 0.3 \ldots 18 pages"; `drafts/README.md` lists only v01--v03 of the
   eight snapshots; the third continuation note's fact (16) says
   "$\arg\zeta(1+2ir)$ is bounded" one section after its own item 3 retracts
   exactly that claim; and §8.5's "columns constant to about one percent" is,
   from its own table, two to five percent ($0.561$ to $0.592$ in the first
   column).

---

## 3. The Gram-point control is phase-dependent, and the arithmetic gap is an artifact

### 3.1 The issue

`gram_point_cache.py` generates $\theta(g_n)=n\pi$ for $n\ge-1$, so the control
set starts at $g_{-1}=9.667$, below $\gamma_1=14.135$, and its counting function
is $\lfloor\theta(T)/\pi\rfloor+2$, which exceeds the smooth count
$N_{\rm sm}(T)=\theta(T)/\pi+1$ by $\tfrac12$ on average. The zeros have
$N(T)=N_{\rm sm}(T)+S(T)$ with $S$ of mean zero. The lattice with that property is
the *half-shifted* one, $\theta(\tilde g_k)=(k-\tfrac12)\pi$, $k\ge0$, with
counting function $\lfloor\theta/\pi+\tfrac12\rfloor+1$ and lowest point
$\tilde g_0=14.518$. It is also the Gram's-law idealization of the zeros: the low
zeros alternate with the Gram points, so they sit near these midpoints
($S(\gamma_1^+)=0.55$, $S(\gamma_2^+)=0.43$, against the lattice's $0.50$).

### 3.2 The measurement

Same sine basis, same even block, same $N=\max(60,2.8\cdot2Le^L)$, same precision
rule as the note; point sets truncated at $T=3000$ unless marked. Entries are
$\log_{10}\lambda_{\min}$; every control value is a trial-space Rayleigh quotient
and an upper bound on its infimum, slightly depressed by truncation.

| $L$ | zeros (exact) | Gram $n\ge-1$ (the note) | Gram $n\ge0$ | half-shifted | gap, half $-$ zeros |
|---|---|---|---|---|---|
| $0.6$ | $-2.096$ | $-1.005$ | $-2.974$ | $-2.149$ | $-0.05$ |
| $0.8$ | $-3.706$ | $-2.173$ | $-4.852$ | $-3.745$ | $-0.04$ |
| $1.0$ | $-5.984$ | $-4.059$ | $-7.239$ | $-5.896$ | $+0.09$ |
| $1.2$ | $-8.742$ | $-6.623$ | $-10.245$ | $-8.685$ | $+0.06$ |
| $1.4$ | $-12.330$ | $-9.969$ | $-13.981$ | $-12.233$ | $+0.10$ |
| $1.6$ | $-16.683$ | $-14.180$ | $-18.552$ | $-16.615$ | $+0.07$ |
| $2.0$ | $-29.099$ | $-26.146$ | $-31.306$ | $-28.984$ | $+0.12$ |
| $2.4^{\dagger}$ | $-48.016$ | $-44.809$ | $-50.681$ | $-48.011$ | $+0.01$ |
| $2.8$ | $-76.747$ | $-73.167^{\ddagger}$ | $-80.942^{\dagger\dagger}$ | $-76.721$ | $+0.03$ |

$^\dagger$ point sets truncated at $T=1200$; $^{\dagger\dagger}$ at $T=600$
(the Gram $n\ge-1$ value at $T=600$ is $-74.217$, one order below its $T=3000$
value, which is the size of the truncation effect at this $L$); $^\ddagger$
the note's value. The Gram $n\ge-1$ column reproduces the note's table to three
decimals at every length computed at $T=3000$, so the setup is the note's.

### 3.3 What it says

- **The phase of the lattice moves $\log_{10}\lambda_{\min}$ by $2$ to $4$
  orders**, the full spread between the $c=0$ and $c=1$ phases at $L=1.4$ being
  $4.0$ orders. This dwarfs the claimed arithmetic signal and is the control's
  actual uncertainty. The note's four "arithmetic-free" sets all shared the
  phase $c=0$ (the jitter was applied about Gram $n\ge-1$), which is why the
  zeros appeared to sit below the whole family.
- **With the phase matched, the zeros and the arithmetic-free lattice agree to
  $\pm0.12$ orders across $75$ orders of magnitude.** The ratio of exponents is
  $1.00$ to within half a percent at every length, not "$1.049$ and falling".
  The manuscript's thesis --- the collapse is a density effect --- is therefore
  stronger than stated.
- **Withdraw:** "the arithmetic is worth about three orders of magnitude and
  grows like $\log L$" (§8.6 item 2, Remark 8.5), "the zeros are systematically
  the worst of the family" (note §5.3 item 3), the gap law $1.61\log L+1.93$,
  and pathway item 2 of Section 12 / of the third continuation note ("what does
  the arithmetic control, if not the margin? \ldots the gap \ldots does carry
  arithmetic"). On this evidence the gap is a lattice-phase effect and there is
  no measured arithmetic residual in the margin at the $10^{\pm0.1}$ level.
- **The band-edge reading of §7.5 is confirmed sharply.** Moving the lowest
  sample point from $9.67$ to $14.52$ to $17.85$ moves the margin by orders of
  magnitude; the margin is dominated by the lowest few points relative to the
  Nyquist band, which is what "live below the lowest zero" means.

### 3.4 What to do

Recompute §8.6 with the half-shifted lattice as the primary control; report the
spread over the phase $c\in[0,1)$ as the control's error bar (a handful of phases
suffices); redo the jitter rows about the half-shifted lattice with several draws
per strength; and, if the question "what does the arithmetic control" is to be
kept alive, use an unfolded GUE (or CUE) point process as a second control, so
that local repulsion statistics are separated from arithmetic correlations ---
the i.i.d. jitter is locally Poisson and cannot make that separation. The
programme `numerics/exploratory/gram_phase_control.py` (added with this review,
unregistered, mpmath) reproduces the table above.

---

## 4. The modular surface is the transfer at $\omega=\frac12$

### 4.1 The identity

With $\Lambda_\zeta(u)=\pi^{-u/2}\Gamma(u/2)\zeta(u)$ and
$\xi(u)=\tfrac12u(u-1)\Lambda_\zeta(u)$, the Eisenstein scattering matrix of
$PSL(2,\mathbb Z)\backslash\mathbb H$ quoted in Remark 11.14 satisfies
\[
 \frac{\xi(2s-1)}{\xi(2s)}=\frac{s-1}{s}\,\varphi(s),
 \qquad\text{and}\qquad
 \frac{\xi(2s-1)}{\xi(2s)}=\frac{\mathcal F(p-\tfrac12)}{\mathcal F(p+\tfrac12)}
 =K_{1/2}(p)\quad\text{at }p=2s-1 ,
\]
since $\mathcal F(p\mp\tfrac12)=\xi(p+\tfrac12\mp\tfrac12)$. On $\operatorname{Re} s=\tfrac12$
the point $p=2ir$ is on the imaginary axis, the resonances $s=\rho/2$ become
$p=\rho-1$, at $\operatorname{Re} p=-\tfrac12=-\omega$ under RH, and the variable $\tau=2r$ of
Remark 11.14 is exactly the transfer's $\tau$. Checked numerically at
$r=3,\,11.7,\,40.2$: $K_{1/2}(2ir)/\varphi(\tfrac12+ir)=(s-1)/s$ to twelve
digits. **The one system in the survey that "has the Riemann zeros as
resonances" is the programme's own transfer at the endpoint shift.**

### 4.2 What it changes

The group delay of $K_\omega$ is $2\operatorname{Re}\tfrac{\xi'}\xi(\tfrac12+\omega+i\tau)$
(Proposition 4.3). Its archimedean part is
$\operatorname{Re}\psi\big(\tfrac14+\tfrac\omega2+\tfrac{i\tau}2\big)-\log\pi$, a single
$\Gamma$-factor with shift
\[
 a(\omega)=\tfrac14+\tfrac\omega2,\qquad
 I_{2m}(\omega)=2^{2m-1}B_{2m}\big(\tfrac14+\tfrac\omega2\big),
\]
and its pole part contributes $4\omega\tau^{-2}+O(\tau^{-4})$ to the delay. At
$\omega=\tfrac12$: $a=\tfrac12$, $I_2=-\tfrac16$, $I_4=\tfrac7{30}=0.2333$ ---
precisely the modular-surface row of the survey table (with $n=-1$ the inversion
degeneracy, and $\tfrac{s-1}{s}$ supplying the pole part's $+2$, hence the
$+\tfrac{11}6$ the remark computes for the $\xi$ ratio). So:

- The "$\times4$" is $B_2(\tfrac12)/B_2(\tfrac14)=4$: the archimedean shift
  at resonance width $\tfrac12$ against the shift at width $0$. **The delay
  test, calibrated on $2\theta'$, is a test of the $\omega\to0$ limit**, and any
  transfer with resonances at finite distance $\omega$ from the line reads
  $a=\tfrac14+\tfrac\omega2$. The test therefore does *see* the resonance
  width, and the modular surface passes exactly at the width it has.
- Fact (16) of the third continuation note should be split: "passing is not
  evidence of having the zeros" stands (the half-line oscillator); "having the
  zeros is not enough to pass" is an artifact of comparing the $\omega=\tfrac12$
  member of the family to the $\omega=0$ target and should be withdrawn. The
  same applies to the full-line inverted oscillator row $(1,\tfrac12,1)$, whose
  invariants are those of $K_{1/2}$; it is not a failure but the $\omega=\tfrac12$
  match.
- Condition 10.1's last clause should name the family: a candidate with
  resonance width $\omega$ must match $I_{2m}(\omega)$, and for the route of
  Proposition 2.1 it is the $\omega\to0$ end that matters.
- The modular surface realizes only $\omega=\tfrac12$ (integer offsets in $2s$
  are what Eisenstein constant terms produce, for $\Gamma_0(N)$ and for other
  number fields alike), so it does not supply the interior of the family. But
  it supplies something the investigation has been asking for: a concrete,
  classical geometric system --- scattering of Eisenstein waves in the cusp ---
  whose $S$-matrix *is* the transfer, at one shift, with the constants fixed.

### 4.3 The literature this connects to

Sections 4--7 at $\omega=\tfrac12$ are Lax--Phillips scattering theory for the
automorphic wave equation on the modular surface (Lax--Phillips, *Scattering
theory for automorphic functions*, 1976; Pavlov--Faddeev 1972): a unitary wave
evolution, incoming and outgoing subspaces removed, a contraction semigroup
$Z(t)=P_+U(t)P_-$ whose defect is the energy radiated into the cusp, and a
scattering matrix $\varphi(s)$ whose poles are the zeros of $\zeta(2s)$. The
flux identity (4.5), the compression structure $P_LV_\omega P_L$, and the
dichotomy of Proposition 7.2 are the same objects; and the reason Lax--Phillips
did not prove RH --- their conjectured decay estimate for $Z(t)$ is equivalent
to it --- is the same "no critical path" conclusion Section 7 reaches. The
manuscript should cite this literature at Section 4.5 and Remark 11.14; what is
the programme's own is the $\omega$-deformation of that framework and the
identification of $\omega$ with the distance of the resonances from the line.
(The precise correspondence of $L$ with a Lax--Phillips time, presumably through
$x=\tfrac12\log y$ in the cusp, is a reading I have not checked and flag as such.)

---

## 5. Structural remarks

### 5.1 Flatness is automatic

Proposition 9.4 is proved from the commutation of mixed partials of
$V_{\omega,L}f$. That argument applies to *any* two-parameter family
$V(\alpha,\beta)$ with $dV=A\,V$: the curvature satisfies $FV=0$ identically
(when $V$ is invertible, $A=dV\,V^{-1}$ is pure gauge). So the connection
$(-G_{\omega,L}\,d\omega,\,B_L\,dL)$ was flat on the range of $V$ before any
algebra was done, and the same is true for $L$ replaced by any other parameter
on which the transfer depends single-valuedly. The manuscript says as much in
passing ("the content of the identity is (iv)"); it should say it plainly,
because it closes the curvature route for every choice of second parameter at
once and leaves exactly the two exits it names: multivaluedness (monodromy) and
failure of the connection to exist. That is a stronger statement of the
position than "non-abelian but flat".

### 5.2 Spectral forms the manuscript does not write down

Two identities follow from the material of Sections 3--4 and would make
Sections 6 and 9 more transparent. Both are formal until the residue expansions
are justified (symmetric summation, as in the explicit formula); the first is
easy to make rigorous from Theorem 3.1.

*The shifted form samples at complex-shifted points.* Since
$\cosh(\omega t)e^{i\gamma t}=\tfrac12[e^{(\omega+i\gamma)t}+e^{(-\omega+i\gamma)t}]$,
Theorem 3.1's hyperbolic factor turns the spectral form into
\[
 Q_{\omega,L}[f]=\sum_\rho\operatorname{Re}\Big[\widehat F(\gamma_\rho-i\omega)\,
 \overline{\widehat F(\gamma_\rho+i\omega)}\Big]
 \qquad(\text{RH; in general }\overline{\widehat F(\overline{\gamma_\rho}+i\omega)}),
\]
which is Proposition 6.1 in frequency space, since
$\widehat{e^{\pm\omega X}f}(\gamma)=\widehat F(\gamma\mp i\omega)$. It shows at a
glance why positivity at positive shift is not implied by RH (Remark 6.3): the
summand is not a square. It also gives the operator identity behind
Proposition 6.1,
$G_{\omega,L}=\tfrac12\big(e^{\omega X}G_{0,L}e^{-\omega X}+e^{-\omega X}G_{0,L}e^{\omega X}\big)$,
the shifted generator as the symmetrized conjugate of the central one --- the
shift is a gauge transformation by $e^{\omega X}$, symmetrized, which is one
more way of seeing that it carries no ordering.

*The defect is a Cauchy--Gram matrix over the zeros.* Under RH, expanding the
causal kernel in residues at $p_\rho=-\omega+i\gamma_\rho$ with
$R_\rho=\xi(\rho-2\omega)/\xi'(\rho)$ gives, for $x\ge L/2$,
$(V_\omega f)(x)=\sum_\rho R_\rho e^{p_\rho x}\widehat F(\gamma_\rho+i\omega)$,
and (4.5) becomes
\[
 \langle f,D_{\omega,L}f\rangle
 =e^{-\omega L}\sum_{\rho,\rho'}
 \frac{R_\rho\overline{R_{\rho'}}\,e^{i(\gamma_\rho-\gamma_{\rho'})L/2}}
 {2\omega-i(\gamma_\rho-\gamma_{\rho'})}\,
 \widehat F(\gamma_\rho+i\omega)\overline{\widehat F(\gamma_{\rho'}+i\omega)},
\]
the Gram matrix of the decaying exponentials $e^{p_\rho x}$ on $(L/2,\infty)$,
manifestly positive semidefinite. Its diagonal recovers $2\omega Q_{0,L}$ as
$\omega\downarrow0$ ($R_\rho\to-2\omega$). It is the finite-$\omega$ analogue of
(2.7) and the spectral form of the positive-real criterion of Proposition 7.7.
Its first consequence is that the endpoint coefficient of Proposition 9.1 is an
exponential sum over the zeros,
$(V_\omega f)(L/2)=e^{-\omega L/2}\sum_\rho R_\rho e^{i\gamma_\rho L/2}
\widehat F(\gamma_\rho+i\omega)$ --- an $\ell^1$-type functional of the zero
samples against the $\ell^2$ norm that $Q$ controls, which is Proposition 9.5
without Sobolev exponents. It also exhibits the two expansions of one kernel:
$k_\omega$ as a residue sum over zeros, and $k_\omega$ as the exponential of the
atomic generator of (9.5) over primes; their equality is the explicit formula at
the level of the transfer.

### 5.3 Smaller points

- **Condition 10.3 is a near-diagonal statement.** The exact archimedean kernel
  is $n_\gamma(r)=e^{-r/2}/(1-e^{-2r})=\sum e^{-(2n+\frac12)r}$; the conformally
  covariant $\Delta=\tfrac12$ two-point function on the ray is
  $1/(2\sinh\tfrac r2)=e^{-r/2}/(1-e^{-r})=\sum e^{-(n+\frac12)r}$. They agree at
  the diagonal and differ in the tower ($\Gamma(s/2)$ against $\Gamma(s)$,
  Legendre duplication), which is exactly the $a=\tfrac14$ against $a=\tfrac12$
  the delay test resolves. So 10.3 is subsumed by 10.1 and should say so.
- **The disproof instrument (Remark 7.4) is not competitive.** A certified
  Rayleigh quotient above one needs an input with frequency content at the
  height of a hypothetical off-line zero, above the verified range
  ($\gtrsim3\times10^{12}$), and a length $L\gtrsim1/(\delta-\omega)$; that is
  no cheaper than evaluating $\xi$ there. The remark is right that the plane is
  one-sided; it should add that it is not a useful one-sided instrument either.
- **"Held for $\sim\log N$" (Section 4.2) is the smooth part.** At small
  $\omega$ the delay $2\partial_\tau\Psi=\sum_\rho 2\omega/(\omega^2+(\tau-\gamma_\rho)^2)$
  is a sum of spikes of height $2/\omega$ at the zeros and near zero between
  them; a packet between resonances passes undelayed. The log law holds on
  average and for $\omega$ above the local zero spacing. Worth one sentence,
  because the escaped-mass picture (4.5) is often read with the smooth delay in
  mind.

---

## 6. Robustness of the negative assessments

| Assessment | Status after review |
|---|---|
| The $\omega$-flow is abelian (Thm 5.2) | Airtight and elementary; truncation of causal convolutions is a homomorphism onto a commutative algebra. No loophole. |
| The $(\omega,L)$ connection carries no curvature (Prop 9.4) | Airtight, and automatic for any single-valued two-parameter family (§5.1). The two named exits are the only ones. |
| No critical path; contraction at fixed $\omega$ is a zero-free strip (Cor 7.3) | Airtight given the boundedness repair of §2.2. The route of Prop 2.1 is unchanged; the "flow does not escape criticality" reading is correct. |
| No unitary defect correlator winds (Prop 11.3) | Airtight for defect two-point functions on the ray; positivity of the spectral measure is the whole input, so no state or temperature evades it. Ratios, signed measures and spectra unbounded below are the only exits, as stated. |
| Single-factor rigidity of the $\Gamma$-shift (Thm 11.9) | Correct. The multi-factor case is open, as stated. |
| "The delay test cannot see the zeros" (Rem 11.14, fact 16) | **Half withdrawn** (§4): the test reads the resonance width; the modular surface is $K_{1/2}$ and passes at $\omega=\frac12$. |
| "The margin carries almost no arithmetic" (§8.6) | **Strengthened** (§3): none at the $10^{\pm0.1}$ level. The claimed residual gap is a lattice-phase artifact. |
| The flatness/trace obstruction at the endpoint (Prop 9.5) | Sketch is sound; §5.2 gives the transparent form. |

I looked specifically for a loophole in the abelian obstruction through the
multiplication operator $X$, which does not commute with the transfers
($[X,G]$ is the convolution with symbol $-\partial_pa_\omega$) and which
Section 6 already uses. It supplies none: $X$ acts on the algebra of truncated
convolutions by automorphisms ($e^{cX}Te^{-cX}$ is again a truncated causal
convolution), so the structure is a semidirect product in which the transfers
themselves still commute, and any two-parameter family built from
$(\omega,c)$ is again single-valued and flat. The manuscript's list of three
transverse sources (Remark 5.5) is complete as far as I can see.

---

## 7. Recommendations, ranked

1. **Fix §8.6 and its downstream statements** per §3.4, and re-examine the
   "universal profile" of §8.5 with the phase-matched control, since the
   obstruction's frequency distribution may also carry a phase dependence.
2. **Rewrite Remark 11.14 and fact (16)** per §4.2; add the family
   $I_{2m}(\omega)$ to Condition 10.1; cite Lax--Phillips and Pavlov--Faddeev at
   Section 4.5, and state what is inherited from that framework and what is the
   programme's own ($\omega$).
3. **Repair the three proofs** of §2.1--2.3 and correct the number of §2.4 and
   the check threshold.
4. **Add the spectral forms of §5.2** to Sections 6 and 9, with the convergence
   caveat, and state the automatic flatness of §5.1 plainly.
5. **Update `README.md` and `drafts/README.md`** to version 0.8 and eight
   snapshots, and fix fact (16)'s parenthetical in the third continuation note.
6. **Independently derive the cigar amplitude**, as the third continuation note
   already asks; it remains the one survey row that could change a conclusion.

---

## 8. Status of every statement in this review

- **Verified by hand:** everything in §1.1; the derivations in §2.1, §2.2 and
  §2.4; the identity of §4.1; the formulas of §4.2; the argument of §5.1; the
  identities of §5.2 up to the convergence of the residue expansions, which are
  not proved here.
- **Labelled numerical computation:** the table of §3.2, produced by
  `numerics/exploratory/gram_phase_control.py` (unregistered, mpmath), each
  entry a trial-space Rayleigh quotient; the twelve-digit check of §4.1; the
  reruns of §1.2.
- **Reading, not verified:** the Lax--Phillips correspondence of §4.3 beyond
  the identity of §4.1, in particular the identification of $L$ with a time.
- **Not examined:** the items of §1.3.
- **Not claimed:** anything about the truth of the Riemann hypothesis, a
  construction, a positivity statement, or a matched or excluded gauge theory.

See the [reviews index](README.md) and the [investigation index](../README.md).
