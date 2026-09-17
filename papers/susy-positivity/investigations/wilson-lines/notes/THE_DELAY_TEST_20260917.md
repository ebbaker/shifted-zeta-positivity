# The delay test, run: no correlator can wind

**Author: Claude Opus 5 (Anthropic).** 17 September 2026. Research note, running
item 1 of the revised pathway in
[the second continuation note](CONTINUATION_20260917_SESSION2.md) --- the
group-delay test of manuscript Condition 10.1, promoted to first place by
[the frame-bound note](FRAME_BOUND_AND_THE_DENSITY_20260917.md).

**No manuscript change has been made.** Version 0.4 is current. Section 6 lists
what this recommends, and the recommendation is a **replacement of
Condition 10.1**, not an addition to it.

---

## 0. Summary

1. **The test can be run, and it returns exactly zero.** For a defect primary of
   dimension $\Delta$ on a ray, the group delay of the causal ray kernel is, in
   closed form,
   \[
     \mathcal T_\Delta(\tau)=\pi\,\operatorname{Re}\cot\big(\pi(\Delta+i\tau)\big)
     =\frac{\pi\sin(2\pi\Delta)}{\cosh(2\pi\tau)-\cos(2\pi\Delta)} .
   \]
   It is **exponentially small**, $\sim2\pi\sin(2\pi\Delta)e^{-2\pi\tau}$, where
   the target $2\theta'(\tau)\sim\log\frac\tau{2\pi}$ grows. And when $2\Delta$ is
   an integer it **vanishes identically** --- which is the case for every
   protected operator of the $\frac12$-BPS Wilson-line defect CFT: $\Delta=1$ for
   the five scalars, $\frac32$ for the fermions, $2$ for the displacement, $L$ for
   the $(Y\!\cdot\!\Phi)^L$ tower. The protected sector has **zero** group delay at
   every frequency and every coupling.
2. **The failure is structural, not a bad choice of operator.** Reflection
   positivity plus a dilatation generator bounded below makes the ray kernel
   completely monotone, so its causal symbol is a Stieltjes transform of a
   positive measure. Such a function has positive real part on the whole real
   axis: **no zeros, hence no winding**. Its argument is confined to an interval
   of length $\frac\pi2$ (length $\pi$ if a real subtraction is needed), so
   $\int_0^T\mathcal T\,d\tau\leq\pi$ for every $T$, against
   $\int_0^T2\theta'=2\theta(T)$, which is $175.9$ at $T=100$ and $4069.1$ at
   $T=10^3$. No correlator of a unitary defect CFT can pass, whatever the theory.
3. **The thing that is really being demanded is that the object be an inner
   function.** $e^{2i\theta(\tau)}=\pi^{-i\tau}\Gamma(\frac14+\frac{i\tau}2)/
   \Gamma(\frac14-\frac{i\tau}2)$ is unimodular with unbounded phase winding;
   manuscript Proposition 4.5 already says $K_\omega$ is inner. A two-point
   function is never inner. **The object to match is a ratio --- a reflection
   coefficient --- and not any Green's function.** That is the manuscript's own
   scattering dictionary (§4.4) taken literally, and Condition 10.1 does not
   currently say it.
4. **The obstruction is $D\geq0$, not discreteness.** A *continuous* dilatation
   spectrum bounded below gives the same Stieltjes transform and the same bounded
   phase. What is needed is a sector on which the dilatation generator is **not
   bounded below**.
5. **The delay clause is satisfiable, and by something already known and very
   simple.** The phase shift of the inverted harmonic oscillator on the half-line
   is $\eta(\tau)=\arg\Gamma(\frac14+\frac{i\tau}2)$
   \cite{BhaduriKhareLaw}, and
   \[
     2\eta'(\tau)-2\theta'(\tau)=\log\pi\qquad\text{exactly, for every }\tau .
   \]
   That system is $H=\frac12(xp+px)$ --- the dilatation generator itself --- on a
   ray, with continuous spectrum on all of $\mathbb R$. So the clause is satisfied
   by the *free* generator, and the constant it misses is exactly the conductor
   $\pi^{-s/2}$. **The delay clause does not discriminate among candidates.** What
   it discriminates is whether $D$ is bounded below.
6. **One interacting theory does wind**: the bulk Liouville reflection amplitude,
   with $\frac{d}{dP}\arg S(P)=4Q\log P+O(1)$, $Q=b+b^{-1}$, verified here to ten
   digits at three values of $b$. The coefficient is $\geq8$ where the target
   needs $1$, but the two are in different variables and no dictionary has been
   fixed; the shape is right and nothing else in the survey has it.
7. **So Condition 10.1 should be replaced** (Section 6): (a) the object is a
   ratio, not a correlator; (b) $D$ is not bounded below; and (c) the
   discriminating data is not the $\log\tau$, which every $\Gamma$-ratio supplies,
   but the additive constant $-\log\pi$ and the bounded fluctuation
   $S(\tau)=\pi^{-1}\arg\zeta(\frac12+i\tau)$ --- the conductor and the primes.

---

## 1. What object the test can be run on

The manuscript's outlook says: *take a protected open Wilson line two-point
function in the defect setting of* \cite{OWL}, *extract the phase of its spectral
kernel against the dilatation eigenvalue, and compare its derivative with
$2\theta'(\tau)$*.

**There is no such two-point function in \cite{OWL}.** That paper establishes the
existence of supersymmetric open Wilson lines --- only in the superconformal
versions of the $\mathcal N=2$ theories, and in $\mathcal N=4$ coupled to a three
dimensional defect hypermultiplet, where the supersymmetric configuration is a
semicircle related to the ray by a conformal transformation --- and computes
**expectation values**, perturbatively, with localization proposed for the
non-perturbative answer. It contains no two-point function of open Wilson lines
and no correlator of insertions along the line.

*Reading scope.* Abstract fetched directly; the body through a secondary reading,
so the negative statement is "not found", not "certainly absent". The abstract's
existence statement and the semicircle-to-ray remark are verbatim.

So the test has to be run on the object that does exist and is known exactly: the
**two-point functions of the defect CFT on the $\frac12$-BPS Wilson line in
$\mathcal N=4$**. These are

\[
 \langle\!\langle\Phi^a(t_1)\Phi^b(t_2)\rangle\!\rangle
 =\frac{\delta^{ab}\,2B(\lambda)}{|t_{12}|^{2}},\qquad
 \langle\!\langle\mathbb D^i(t_1)\mathbb D^j(t_2)\rangle\!\rangle
 =\frac{\delta^{ij}\,12B(\lambda)}{|t_{12}|^{4}},
\]

with $B(\lambda)=\frac{\sqrt\lambda I_2(\sqrt\lambda)}{4\pi^2I_1(\sqrt\lambda)}$
the Bremsstrahlung function, and more generally $C_L(\lambda)/|t_{12}|^{2L}$ for
the protected $(Y\!\cdot\!\Phi)^L$ tower. **Every protected dimension is an
integer or a half-integer and is coupling-independent; the whole coupling
dependence sits in the normalization.** The non-protected spectrum is discrete,
fixed by a quantum-spectral-curve quantization condition, and its lowest state
tends to $2$ rather than growing. This is the strongest possible case to run the
test on, and Section 2 runs it.

---

## 2. The delay of a defect two-point function, in closed form

Put the defect on a ray $r>0$ and set $x=\log r$, so the dilatation generator
translates $x$; this is the coordinate of manuscript §10.4, in which the Weil
form is exactly translation invariant. A defect two-point function in the ray
frame is a function of $u=x_1-x_2$,
\[
 G_\Delta(u)=\Big(2\sinh\tfrac u2\Big)^{-2\Delta},
\]
the conformally covariant form of $C/|r_1-r_2|^{2\Delta}$ after stripping the
weight $(r_1r_2)^{\Delta}$; the normalization $C$ is a positive constant and
drops out of every phase below. Its causal symbol, the analogue of the
manuscript's $K_\omega$, is

\[
 \widehat k_+(\tau)=\int_0^\infty e^{-i\tau u}G_\Delta(u)\dd u
 =\Gamma(1-2\Delta)\,\frac{\Gamma(\Delta+i\tau)}{\Gamma(1-\Delta+i\tau)} ,
\]

checked against direct quadrature at $25$ points. The group delay is
$\mathcal T_\Delta=-\frac{d}{d\tau}\arg\widehat k_+$, and since
$\frac{d}{d\tau}\arg\Gamma(a+i\tau)=\operatorname{Re}\psi(a+i\tau)$ and
$\psi(1-z)-\psi(z)=\pi\cot\pi z$,

> **Proposition 2.1.** For every $\Delta$,
> \[
>  \mathcal T_\Delta(\tau)=\operatorname{Re}\psi(1-\Delta+i\tau)-\operatorname{Re}\psi(\Delta+i\tau)
>  =\pi\operatorname{Re}\cot\big(\pi(\Delta+i\tau)\big)
>  =\frac{\pi\sin(2\pi\Delta)}{\cosh(2\pi\tau)-\cos(2\pi\Delta)} .
> \]

Three corollaries, all verified numerically to $10^{-11}$ or better.

* **Exponential decay.** $\mathcal T_\Delta(\tau)=2\pi\sin(2\pi\Delta)\,
  e^{-2\pi\tau}\big(1+O(e^{-2\pi\tau})\big)$. At $\tau=3$ and $\Delta=\frac14$ it
  is $4.09\times10^{-8}$; the target there is $2\theta'(3)=-0.744$, and by
  $\tau=10$ the target is $+0.464$ and the delay is $3\times10^{-27}$.
* **Total.** For $0<\Delta<\frac12$, $\int_0^\infty\mathcal T_\Delta
  =\pi(\frac12-\Delta)$, exactly; $\mathcal T_\Delta$ is periodic in $\Delta$ with
  period one.
* **Protected operators give exactly nothing.** $\sin(2\pi\Delta)=0$ whenever
  $2\Delta\in\mathbb Z$, so $\mathcal T_\Delta\equiv0$ for
  $\Delta=1,\frac32,2,3,\ldots$ --- the entire protected spectrum of the
  Wilson-line defect CFT. Not small: zero, at every frequency, at every coupling.

That is the test, run. It fails, and it fails by an infinite margin in the most
literal way available.

---

## 3. Why no correlator can pass

The zero above is a coincidence of half-integer dimensions; the following is not.

Radial quantization of the ray about the pinned endpoint gives the
boundary-channel decomposition
\[
 G(u)=\sum_n\big|\langle\Omega|O|n\rangle\big|^2e^{-\Delta_nu}
 =\int_{[0,\infty)}e^{-\Delta u}\dd\mu(\Delta),\qquad \mu\geq0,
\]
using only that the defect Hilbert space has a positive inner product and that
the dilatation generator is bounded below --- reflection positivity and the
unitarity bound. (For $G_\Delta$ itself this is the primary plus its descendants,
$\mu=\sum_k\frac{\Gamma(2\Delta+k)}{k!\,\Gamma(2\Delta)}\delta_{\Delta+k}$, with
manifestly positive coefficients; checked against the closed symbol.) By
Bernstein's theorem this is exactly the statement that $G$ is completely monotone
on $u>0$. Hence

\[
 \widehat k_+(\tau)=\int\frac{\dd\mu(\Delta)}{\Delta+i\tau},
 \qquad
 \operatorname{Re}\widehat k_+=\int\frac{\Delta\dd\mu}{\Delta^2+\tau^2}>0,
 \qquad
 \operatorname{Im}\widehat k_+=-\tau\!\int\frac{\dd\mu}{\Delta^2+\tau^2}<0 .
\]

> **Proposition 3.1 (no winding).** Let $G$ be the ray kernel of a two-point
> function in a unitary defect theory whose dilatation generator is bounded below.
> Then for $\tau>0$, $\arg\widehat k_+(\tau)\in(-\frac\pi2,0)$, so
> \[
>  \int_0^T\mathcal T(\tau)\dd\tau=\arg\widehat k_+(0^+)-\arg\widehat k_+(T)<\frac\pi2
>  \qquad\text{for every }T .
> \]
> If a real subtraction is needed to make the transform converge, $\widehat k_+$ is
> Nevanlinna rather than Stieltjes and the bound is $\pi$ instead of $\frac\pi2$.
> Either way it is a constant. The target has
> $\int_0^T2\theta'=2\theta(T)\to\infty$: $175.9$ at $T=100$, $4069.1$ at
> $T=10^3$, $6.37\times10^4$ at $T=10^4$.

Two sharper readings of the same fact, both worth keeping.

**No resonances.** $\operatorname{Re}\widehat k_+>0$ on the whole real axis, so
$\widehat k_+$ has **no zeros there**. Phase winding is zeros crossing the
contour; a positive spectral measure forbids them outright. The manuscript's
scattering dictionary (§4.4) lists the zeros of $\xi$ as the resonances of
$K_\omega$; a correlator of a unitary theory has none to list.

**The obstruction is $D\geq0$, not discreteness.** Nothing above used that the
spectrum is discrete. A *continuous* dilatation spectrum on $[0,\infty)$ gives the
same Stieltjes transform and the same bounded phase. The hypothesis that does the
work is $\operatorname{supp}\mu\subseteq[0,\infty)$.

### 3.1 The three escapes, one of which the manuscript already calls a trap

Winding therefore requires one of exactly three things.

1. **A signed measure**, that is a non-unitary theory. Excluded by assumption.
2. **A spectrum not bounded below**, so that the imaginary axis is not inside the
   region of absolute convergence and the object on the axis is a *continuation
   past poles* rather than a transform. This is precisely the trap of manuscript
   Remark 4.2: $a_\omega$ has poles at $\operatorname{Re}p=+\omega$, its
   continuation to the axis is not the causal symbol, and the residues crossed are
   the entire form. The same phenomenon, seen from the side of the candidate
   rather than of the target.
3. **A ratio.** $K_\omega=\mathcal F(p-\omega)/\mathcal F(p+\omega)$ is not a
   transform of anything positive; it is unimodular, and unimodularity is
   incompatible with being a Stieltjes transform, which decays like $1/\tau$.

Route 3 is the one the Weil family takes, and the manuscript's own central
identity says so. Proposition 4.3 reads $2\theta'(\tau)=b(\tau^2)+w_0$: the *same
real function* is the archimedean multiplier of the form and the phase derivative
of the transfer. Read as a spectral weight the archimedean data is a positive
multiplier with no phase at all; read as a ratio it is a winding phase.

> **A correlator gives you only the first reading.** Condition 10.1, as written,
> asks a correlator for the second.

---

## 4. What does wind

### 4.1 The dilatation generator on a ray

The inverted harmonic oscillator on the half-line --- $V=-\frac12m\omega^2x^2$
with a hard wall at the origin --- has scattering phase shift
$\eta(\tau)=\arg\Gamma(\frac14+\frac{i\tau}2)$ \cite{BhaduriKhareLaw}. Since
$\theta(\tau)=\arg\Gamma(\frac14+\frac{i\tau}2)-\frac\tau2\log\pi$,

\[
 2\eta'(\tau)-2\theta'(\tau)=\log\pi\quad\text{exactly},
\]

verified to $10^{-14}$ at four frequencies. The inverted oscillator is
unitarily equivalent, by a rotation of the phase plane, to
$H=\frac12(xp+px)$ --- the dilatation generator --- whose spectrum on $L^2$ is all
of $\mathbb R$, continuous and unbounded in both directions, which is exactly what
Proposition 3.1 says is required.

Two consequences, and they cut in opposite directions. **The delay clause of
Condition 10.1 is satisfied by a free one-dimensional Hamiltonian**, so as a test
of a gauge theory it has almost no discriminating power: anything whose symbol is
a $\Gamma$-ratio at quarter-integer argument will pass. And **what the free
generator misses is exactly the conductor**: the constant $\log\pi$, which is the
$\pi^{-s/2}$ of the completion. The prime data is the bounded fluctuation
$S(\tau)$, which the free generator also misses. So the archimedean $\log\tau$ is
the cheap part of the target, and the program has been treating it as the test.

### 4.2 Liouville

The bulk Liouville reflection amplitude
\[
 S(P)=-\big(\pi\mu\gamma(b^2)\big)^{-2iP/b}\,
 \frac{\Gamma(1+2iPb)\,\Gamma(1+2iP/b)}{\Gamma(1-2iPb)\,\Gamma(1-2iP/b)}
\]
is unimodular for real $P$ --- an inner function --- and
\[
 \frac{d}{dP}\arg S(P)=-\frac2b\log\big(\pi\mu\gamma(b^2)\big)
 +4b\operatorname{Re}\psi(1+2ibP)+\frac4b\operatorname{Re}\psi(1+2iP/b)
 =4Q\log P+O(1),
\]
$Q=b+b^{-1}$; the coefficient is reproduced to ten digits at $b=\frac12,1,\frac{17}{10}$.
So an interacting theory with a continuum does produce a logarithmically growing
delay. The coefficient $4Q\geq8$ against the target's $1$ is not yet a mismatch:
$P$ and $\tau$ are different variables and no dictionary has been fixed. What can
be said is that the *shape* is right, that the continuum is exactly the ingredient
Proposition 3.1 demands, and that the boundary (FZZT) amplitude, built from double
$\Gamma$ functions, is in the same class. Nothing else in the survey behind this
note has the right asymptotics; in particular the boundary reflection factors of
integrable field theory are finite products of $\sinh$ blocks, whose phases
saturate, so their delays decay.

### 4.3 What the target is, exactly

\[
 e^{2i\theta(\tau)}=\pi^{-i\tau}\,
 \frac{\Gamma(\frac14+\frac{i\tau}2)}{\Gamma(\frac14-\frac{i\tau}2)} ,
\]
unimodular (verified), with poles at $\tau=i(\frac12+2n)$ and zeros at
$\tau=-i(\frac12+2n)$ --- an inner function of Blaschke type. The full target adds
$\arg\zeta(\frac12+i\tau)$, whose derivative is the bounded fluctuation. The
program's $\log\tau$ is the $\Gamma$; the arithmetic is the fluctuation.

---

## 5. What I think this means

The delay test was billed as *the first test in this program that a gauge theory
can fail*. It is, and it does --- but the failure is not informative about gauge
theory. Every two-point function of every unitary defect theory fails it, by
Proposition 3.1, and a free particle on a half-line passes it, by §4.1. A test
with that profile is not measuring what the program wants measured.

This is the same shape of conclusion as the frame-bound note reached on the
arithmetic side, and for a related reason. There, the superexponential collapse
of the margin turned out to be a property of the *density* of the zeros and
almost independent of the primes. Here, the logarithmic growth of the delay turns
out to be a property of the *archimedean factor* and independent of the theory.
Both quantities are dominated by the archimedean place, and the program has been
using both as its principal tests. **The discriminating data in this program is
the constant and the fluctuation, not the leading term.** That is now true twice,
and it is worth saying once, loudly, rather than twice, locally.

Concretely, the two things a candidate must reproduce that are *not* archimedean:
the conductor $\pi^{-s/2}$, which appears here as the exact constant $\log\pi$
between $2\eta'$ and $2\theta'$; and the fluctuation $S(\tau)$, which is where the
primes live and which no object examined in this note or the last has any of.

---

## 6. Recommendation: replace Condition 10.1

Condition 10.1 currently reads: *the object must be a bilinear in unbounded
endpoint operators joined by a transport --- not a character --- and its group
delay must grow like $\log\tau$ with smooth part $2\theta'(\tau)$.*

The first clause stands: \cite{OWL}'s open Wilson line satisfies it structurally,
and §1 does not disturb that. The second should be replaced by three clauses,
none of which it currently implies.

**(10.1a) The object is a ratio.** What must have the phase is a reflection
coefficient --- unimodular on the critical line, inner in a half-plane --- and not
a correlator. Proposition 3.1 makes this a theorem rather than a preference:
a two-point function of a unitary defect theory has bounded total phase, whatever
the theory, the operator or the coupling.

**(10.1b) The dilatation generator is not bounded below on the relevant
sector.** This is what Proposition 3.1 actually forbids; discreteness is
irrelevant, and a continuum bounded below fails for the same reason a discrete
spectrum does.

**(10.1c) The test is the constant and the fluctuation, not the growth.** Any
$\Gamma$-ratio gives $\log\tau$; the free dilatation generator on a ray gives the
smooth part exactly, up to $\log\pi$. A candidate is distinguished by reproducing
the conductor and by having any fluctuation at all.

A worked instance of the replacement is available and cheap: fix a dictionary
between the Liouville momentum $P$ and the dilatation eigenvalue $\tau$, and ask
whether the coefficient $4Q$ can be brought to $1$ and what the constant then is.
That is a two-hour calculation and it would be the first quantitative comparison
in this program between the target's archimedean data and an interacting theory's.

Also, in the manuscript's outlook item 1 and in Condition 10.1's discussion, the
phrase *"take a protected open Wilson line two-point function in the defect
setting of \cite{OWL}"* should be corrected: no such correlator exists in that
paper, which computes expectation values. The natural substitute, named in §1
here, is the defect CFT on the $\frac12$-BPS Wilson line.

---

## 7. Status of every statement

* **Written proof.** Proposition 2.1, from $\frac{d}{d\tau}\arg\Gamma(a+i\tau)=
  \operatorname{Re}\psi(a+i\tau)$ and the reflection formula. Proposition 3.1,
  from Bernstein's theorem and the elementary sign computation; its hypotheses are
  reflection positivity and $D\geq0$, and its conclusion is a bound, not an
  asymptotic. The three escapes of §3.1 are a complete case division of how
  winding can occur, given those hypotheses.
* **Written computation, verified.** Every number in §§2--4:
  $157$ checks in six groups in the [check
  programme](../numerics/check_delay_test.py), standard library only, JSON to
  stdout, deterministic on replay, worst errors $10^{-14}$ (A), $10^{-11}$ (C),
  exact (D), $10^{-10}$ (E), $10^{-14}$ (F). Group B is normalized by the
  truncation tail of the channel sum and is a consistency check, not an identity.
* **Reading.** §1's description of \cite{OWL} and of the Wilson-line defect CFT
  spectrum; the identification of $\eta(\tau)$ in \cite{BhaduriKhareLaw}; the
  Liouville reflection amplitude and the statement about integrable boundary
  reflection factors. Scope is stated in §1 for \cite{OWL}. The
  Bremsstrahlung-function normalizations $2B$ and $12B$ are quoted, not
  re-derived.
* **Unconditional.** Nothing in this note uses the Riemann hypothesis. Nothing
  computes with $\zeta$ or $\xi$ beyond $\theta$ and $\psi$, which are archimedean.
* **Not claimed.** No gauge theory is matched. \cite{OWL} is not excluded --- what
  is excluded is every *correlator*, including its own, as a carrier of the phase;
  the construction itself is untouched and still satisfies the first clause of
  Condition 10.1. No source is constructed and no positivity is proved. The
  Liouville comparison of §4.2 is an observation about asymptotics, not a proposed
  identification: no dictionary has been fixed, and until one is, the factor of
  $4Q$ means nothing.

---

## 8. Reproduction

```sh
python3 numerics/check_delay_test.py      # 157 checks, six groups, standard library
```

The programme is written to the investigation's conventions and replays
deterministically, with its record at
[`numerics/records/delay-test-checks.json`](../numerics/records/delay-test-checks.json).
It is **not yet in the `CHECKS` dictionary** of `validation/drafts.py`: adding it
edits a file `BUILD_RECORD.json` hashes, so registration has to be paired with a
`drafts.py record`, and that belongs with the manuscript pass that acts on
Section 6.

---

## References for this note

* \cite{OWL} E. B. Baker III, *Supersymmetric open Wilson lines*, JHEP **2011**
  (2011) 140, [arXiv:1102.4948](https://arxiv.org/abs/1102.4948).
* \cite{BhaduriKhareLaw} R. K. Bhaduri, A. Khare and J. Law, *Phase of the Riemann
  zeta function and the inverted harmonic oscillator*, Phys. Rev. E **52** (1995)
  486; and R. K. Bhaduri, A. Khare, J. Law, M. V. N. Murthy and S. Tomsovic,
  *The phase of the Riemann zeta function*, Pramana **48** (1997) 537.
* D. Correa, J. Henn, J. Maldacena and A. Sever,
  [arXiv:1202.4455](https://arxiv.org/abs/1202.4455); S. Giombi, R. Roiban and
  A. A. Tseytlin, [arXiv:1706.00756](https://arxiv.org/abs/1706.00756);
  S. Giombi and S. Komatsu,
  [arXiv:1802.05201](https://arxiv.org/abs/1802.05201); A. Grabner, N. Gromov and
  J. Julius, [arXiv:2001.11039](https://arxiv.org/abs/2001.11039) --- the defect
  CFT spectrum and normalizations of §1.
* A. Zamolodchikov and Al. Zamolodchikov,
  [hep-th/9506136](https://arxiv.org/abs/hep-th/9506136); V. Fateev,
  A. Zamolodchikov and Al. Zamolodchikov,
  [hep-th/0001012](https://arxiv.org/abs/hep-th/0001012) --- Liouville and its
  boundary reflection amplitude.
* A. Connes and C. Consani, *The scaling Hamiltonian*,
  [arXiv:1910.14368](https://arxiv.org/abs/1910.14368) --- the scaling generator
  with continuous spectrum on all of $\mathbb R$, which is the object §4.1
  identifies.
