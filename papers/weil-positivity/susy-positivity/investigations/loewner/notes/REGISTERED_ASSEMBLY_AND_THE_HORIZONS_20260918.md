# The registered assembly, three horizons, and what a lattice does not know

**Author: Claude Opus 5 (Anthropic), model `claude-opus-5`.** 18 September 2026
(New York). Third note of the Loewner investigation, carrying out the rest of
item 1 of the [opening note's](MARKOV_PART_AND_REALIZATIONS_20260917.md) plan
and of Section 6 of the
[contraction-margin note](CONTRACTION_MARGIN_FIRST_RUN_20260917.md): a
standard-library registered check programme, the horizons beyond $\log3$, the
cumulative Cayley coordinate, and the phase-matched lattice control on the form
side. Programmes:
[`numerics/check_contraction_margin.py`](../numerics/check_contraction_margin.py)
(registered, standard library, record
[`contraction-margin-checks.json`](../numerics/records/contraction-margin-checks.json)),
[`numerics/exploratory/contraction_margin_gj.py`](../numerics/exploratory/contraction_margin_gj.py)
and
[`numerics/exploratory/gram_control_vs_transfer.py`](../numerics/exploratory/gram_control_vs_transfer.py)
(unregistered, `mpmath`).

**Nothing here is a positivity statement. Every horizon used is one where the
margin of the localized Weil form is already known to be positive, and no claim
is made about the zeros.**

---

## 0. Summary

1. **The spike belongs in the weight, not in a substitution.** The single-atom
   kernel is exactly $\kappa_\omega(\tau)=\tau^{\omega-1}\widehat G(\tau)$ with
   $\widehat G$ *holomorphic on $|\tau|<\pi$* (Proposition 1.1), so every
   integral in the assembly is a Gauss--Jacobi integral for the weight
   $\tau^{\omega-1}$ and converges geometrically. Nothing forms $\tau$ by
   subtraction and nothing underflows. Thirty nodes per atom give the full
   40-digit answer where the previous note's substitution
   $\tau=u^{1/\omega}$ plus tanh--sinh rule needed hundreds and still left a
   floor (Section 1).
2. **Two rows of the contraction-margin note are superseded.** With the new
   quadrature at 40 digits, $\lambda_{\min}(D_{\omega,L})/2\omega$ at
   $L=\log3$, $N=24$ exceeds $m_L^{(24)}$ by
   $0.108\%,\,0.542\%,\,1.090\%,\,2.778\%,\,5.779\%$ at
   $\omega=0.002,\,0.01,\,0.02,\,0.05,\,0.1$ --- **linear in $\omega$ with
   slope $0.5394$ to four digits**, which is the first-order Galerkin term of
   that note's Proposition 2.2 and nothing else. The recorded $-0.3\%$ at
   $\omega=0.002$ and $+0.1\%$ at $\omega=0.01$ were the tanh--sinh noise floor,
   at the size the note itself estimated for it (Section 3).
3. **A registered standard-library check exists.** 53 cases, all passing, no
   `mpmath`, no `numpy`: the quadrature rules against exact moments, the kernel
   against an **exact closed-form Laplace transform**
   $\int_0^\infty e^{-p\tau}\kappa_\omega\,d\tau=
   \pi^\omega\frac{\Gamma((a+p)/2)}{\Gamma((b+p)/2)}\cdot\frac{(p+a)(p-b)}{(p+b)(p-a)}$
   to $1.4\times10^{-13}$ (Proposition 1.2 --- $\Gamma$ alone, no $\zeta$), the
   mass at three horizons against the first-order closed form, contraction and
   $\lambda_{\min}(D_N)/2\omega=m_L^{(24)}(1+\delta)$ with $\delta=+0.54\%$ at
   $\omega=0.01$, the first-order law on $e_1$ at all three horizons, and the
   Cayley coordinate (Section 2).
4. **The assembly is right at $L=\log5$ and $L=\log7$.** With four and six
   atoms, $V_{\omega,L}$ is a strict contraction and
   $\lambda_{\min}(D)/2\omega$ tracks $m_L^{(24)}$ to $1.20\%$ and $1.85\%$ at
   $\omega=0.01$ and to $0.241\%$ and $0.372\%$ at $\omega=0.002$ --- again
   exactly linear in $\omega$. The margins there are $2.54\times10^{-17}$ and
   $2.11\times10^{-22}$ in this basis: the transfer side and the form side
   agree at first order **over fourteen orders of magnitude of margin**
   (Section 4).
5. **Past $\log7$ the nested defect stops being a refinement and becomes
   necessary.** At $L=\log{11},\log{13}$ the plain $N=24$ Galerkin defect
   overstates $m_L^{(24)}$ by factors $5.26$ and $16.6$, because the
   first-order truncation term no longer collapses with $L$ as the margin does;
   nested in $64$ modes it returns $0.986$ and $0.988$ of it (Section 4.2).
6. **Proposition 2.2's nested limit is confirmed, and its $1/N'$ reading
   refined.** At $\omega=0.1$, $L=\log3$, the nested ratio falls
   $1.0578,\,1.0378,\,1.0207,\,1.0103,\,1.0025,\,0.9985$ for
   $N'=24,40,64,96,144,192$ --- **it crosses below $1$**, as that proposition
   requires of the $N'\to\infty$ limit, whose computable part predicts $0.9752$.
   The "roughly $1/N'$" reading, taken from two nestings, describes the first
   step only; the approach to the limit is slower (Section 3.2).
7. **The cumulative Cayley coordinate is one order better in $\omega$, for a
   structural reason.** $Z_{\omega,L}=(I-V)(I+V)^{-1}$ satisfies
   $Z_{-\omega}=-Z_\omega$ **because $K_{-\omega}=1/K_\omega$ and compression is
   a homomorphism of the causal algebra**, so $P=\frac2\omega\re Z$ is *even* in
   $\omega$: $P_{\omega,L}=Q_{0,L}+O(\omega^2)$, against
   $\lambda_{\min}(D)/2\omega=m_L-\omega m_L^2+O(\omega^2)$
   (Proposition 5.2). The exact congruence
   $D=\frac\omega2(I+V^*)P(I+V)$ holds to $10^{-41}$; $P\succeq0$ at every
   $\omega$ tested. On a Galerkin block the two estimators carry the *same*
   first-order truncation term (Proposition 5.3), so they differ at second
   order, measured as $0.03620\,\omega^2\,m_L$ (Section 5).
8. **What the transfer knows that a lattice does not.** In the same $N=24$ even
   block, replacing the zeros by the unfolded lattice gives, in $\log_{10}$
   against the true margin: Gram points $n\geq-1$, $+2.00,+2.44,+2.59$; Gram
   points $n\geq0$, $-1.41,-1.77,-1.35$; the phase-matched half-shifted
   lattice, $+0.030,+0.340,-0.119$ at $L=\log3,\log5,\log7$. The transfer gives
   $+0.0023,+0.0052,+0.0080$ --- and those shrink linearly to zero with
   $\omega$. The best lattice control misses by a factor wandering between
   $0.76$ and $2.19$; the transfer, which contains no zero and no lattice, is
   exact to first order (Section 6).

---

## 1. The quadrature that makes the assembly elementary

The contraction-margin note's Section 5 records that the spike
$k^\Gamma_\omega(\tau)\sim\omega\pi^\omega2^\omega\tau^{\omega-1}$ puts half its
mass below $\tau=2^{-1/\omega}$, that the kernel must therefore be evaluated in
the local coordinate of each atom, and that the substitution
$\tau=u^{1/\omega}$ followed by a tanh--sinh rule was needed. All three are
consequences of one avoidable choice: putting the singularity in the
*integrand*. Put it in the *weight* instead.

### 1.1 The analytic factor

**Proposition 1.1 (the atom is a weight times an analytic function).** Let
$a=\frac12-\omega$, $b=\frac12+\omega$, $0<\omega<\frac12$, and
\[
 G(\tau)=\frac{2\pi^\omega}{\Gamma(\omega)}\Big(\frac{2\sinh\tau}{\tau}\Big)^{\omega-1}e^{\tau/2},
 \qquad
 \Psi_c(\tau)=\int_0^1 v^{\omega-1}e^{c\tau(1-v)}G(\tau v)\,dv .
\]
Then $k^\Gamma_\omega(\tau)=\tau^{\omega-1}G(\tau)$; for every $c\in\mathbb R$,
$J_c(\tau):=\int_0^\tau e^{c(\tau-u)}k^\Gamma_\omega(u)\,du=\tau^{\omega}\Psi_c(\tau)$;
and the single-atom kernel of the $R_\omega$-form,
$\kappa_\omega=k^\Gamma_\omega-4\omega b\,J_{-b}-4\omega a\,J_a$, is
\[
 \kappa_\omega(\tau)=\tau^{\omega-1}\widehat G(\tau),\qquad
 \widehat G=G-4\omega\tau\big(b\,\Psi_{-b}+a\,\Psi_a\big),
\]
with $G$, $\Psi_c$ and $\widehat G$ holomorphic on the disc $|\tau|<\pi$ and
$\widehat G(0)=G(0)=\pi^\omega2^\omega/\Gamma(\omega)$.

*Proof.* $2\sinh\tau=e^{\tau}(1-e^{-2\tau})$ gives
$k^\Gamma_\omega=\frac{2\pi^\omega}{\Gamma(\omega)}(2\sinh\tau)^{\omega-1}e^{\tau/2}$
in the form stated. $\sinh\tau/\tau$ is entire, equals $1$ at $0$ and vanishes
exactly at $\tau=i\pi k$, $k\neq0$, so $\log(2\sinh\tau/\tau)$ and every power of
it are holomorphic on $|\tau|<\pi$. Substituting $u=\tau v$ in $J_c$ and
extracting $\tau^{\omega-1}$ from $k^\Gamma_\omega(\tau v)=(\tau v)^{\omega-1}G(\tau v)$
gives the $\Psi$ form; $\Psi_c$ is holomorphic there because
$|\tau v|\leq|\tau|$ for $v\in[0,1]$ and the $v$-integral converges absolutely
($\Re\omega>0$). $\square$

Everything the assembly integrates is therefore
$\int_0^{T}\tau^{\omega-1}\,(\text{holomorphic})\,d\tau$ with $T<\pi$ at every
horizon used here ($T=L\leq\log{13}=2.565$). The natural rule is **Gauss--Jacobi
for the weight $\tau^{\omega-1}$**, whose nodes and weights come from the
closed-form monic Jacobi recurrence with $\alpha=0$, $\beta=\omega-1$ by
Golub--Welsch. Its error for an integrand holomorphic in a Bernstein ellipse is
geometric in the node count.

Three things follow at once.

- **The local coordinate is automatic**, because each atom's contribution is
  integrated over *its whole support* $[\log n,L)$ in its own variable
  $\tau=t-\log n$: one rule per atom, no splitting at intermediate atoms, no
  global time formed by subtraction.
- **Nothing underflows.** The smallest node is $\sim10^{-5}$, not
  $\sim10^{-100}$: the $\tau^{\omega-1}$ that used to be evaluated is now
  integrated exactly by the rule. The same code therefore runs in double
  precision, which is what makes a registered check possible at all.
- **Convergence is immediate.** At $L=\log3$, $\omega=0.01$, 40 digits, the
  results at $30$, $45$ and $60$ nodes per atom agree in every printed digit
  ($\lambda_{\min}(D)=1.2562771190258\times10^{-9}$), and at $L=\log7$ the
  results at $40$ and $70$ nodes agree likewise. The tanh--sinh runs of the
  previous note used 262 kernel evaluations and about 40 s; these use 30--40 per
  atom and 1--7 s, at the same or higher precision.

### 1.2 The exact Laplace transform, and the Beta variable

**Proposition 1.2 (one atom, in closed form).** For $\Re p>b$,
\[
 \int_0^\infty e^{-p\tau}k^\Gamma_\omega(\tau)\,d\tau
 =\pi^\omega\frac{\Gamma\big((a+p)/2\big)}{\Gamma\big((b+p)/2\big)},
 \qquad
 \int_0^\infty e^{-p\tau}\kappa_\omega(\tau)\,d\tau
 =\pi^\omega\frac{\Gamma\big((a+p)/2\big)}{\Gamma\big((b+p)/2\big)}
  \cdot\frac{(p+a)(p-b)}{(p+b)(p-a)} .
\]

*Proof.* With $2\sinh\tau=e^\tau(1-e^{-2\tau})$ the first integrand is
$\frac{2\pi^\omega}{\Gamma(\omega)}e^{-(p-\omega+1/2)\tau}(1-e^{-2\tau})^{\omega-1}$;
the substitution $x=e^{-2\tau}$ turns it into
$\frac{\pi^\omega}{\Gamma(\omega)}\int_0^1x^{(p+a)/2-1}(1-x)^{\omega-1}dx
=\frac{\pi^\omega}{\Gamma(\omega)}B\big(\tfrac{p+a}2,\omega\big)$, and
$\frac{p+a}2+\omega=\frac{p+b}2$. For the second, the two smoothings multiply the
transform by $1-\frac{4\omega b}{p+b}-\frac{4\omega a}{p-a}$, whose numerator over
the common denominator is
$p^2+2\omega p-ab-4\omega(a+b)p=p^2-2\omega p-ab=(p+a)(p-b)$ since $a+b=1$ and
$b-a=2\omega$. $\square$

Two remarks.

*The Beta variable is explicit.* Dividing by the value at $p=0$,
$\pi^\omega\Gamma(a/2)/\Gamma(b/2)$, the normalized archimedean delay has Laplace
transform $B(\frac{p+a}2,\omega)/B(\frac a2,\omega)=\mathbb E\,U^{p/2}$ with
$U\sim\mathrm{Beta}(\frac a2,\omega)$. That is Proposition 1.1 of the
[opening note](MARKOV_PART_AND_REALIZATIONS_20260917.md), and the change of
variable above says what the Beta variable *is*: $U=e^{-2\tau}$, i.e. the
archimedean delay is $\tau=-\frac12\log U$. The Bessel-additivity reading of the
opening note --- $U=Z_a/(Z_a+Z_{2\omega})$ for squared Bessel processes of
dimensions $a$ and $2\omega$, which add to $b$ --- is thereby a statement about
$e^{-2\tau}$, and the two-line Beta-integral proof above is an elementary route
to the same proposition.

*This is the check that matters.* The right-hand sides involve $\Gamma$ and
nothing else: no $\zeta$, no $\xi$, no zeros. Asserting them against the
assembled kernel is a complete test that the Beta kernel, the local coordinates
and the $R_\omega$ correction are the right ones, and the registered programme
makes it at $p\in\{2,3,5,8\}$ and $\omega\in\{0.01,0.1\}$, agreeing to
$1.4\times10^{-13}$.

---

## 2. The registered programme

[`numerics/check_contraction_margin.py`](../numerics/check_contraction_margin.py),
standard library only, JSON to standard output, preserved record
[`numerics/records/contraction-margin-checks.json`](../numerics/records/contraction-margin-checks.json),
registered in the `CHECKS` dictionary of
[`validation/drafts.py`](../validation/drafts.py) so that
`python3 validation/drafts.py check --replay` requires byte-identical output.
53 cases in six groups, each check carrying its own tolerance; the programme
runs in about one second.

| Group | What it asserts |
|---|---|
| A | Gauss--Jacobi moments against $1/(\omega+m)$ for $m<64$ at four shifts; Gauss--Legendre moments against $1/(m+1)$ for $m<128$; the closed-form one-sided sine autocorrelations $S_{jk}$ against direct quadrature at 24 triples $(j,k,t)$. |
| B | $\widehat G$ by the $\Psi$ route against $\widehat G$ by an independent split rule (Gauss--Jacobi on $[0,1]$, Gauss--Legendre beyond), and the **Laplace transform of Proposition 1.2** at $p\in\{2,3,5,8\}$, $\omega\in\{0.01,0.1\}$. |
| C | The mass $\int_0^Lk_\omega$ at $L=\log3,\log5,\log7$ against the 40-digit assembly (agreeing to $10^{-13}$), and its two-point extrapolation $(1-\int_0^Lk_\omega)/\omega\to$ the closed form of Proposition 2.3 of the contraction-margin note ($0.6305160$, $0.6447529$, $0.8355651$). |
| D | $\lVert V_{\omega,\log3}\rVert<1$ at five shifts; $m_L^{(24)}$ from the closed-form Weil assembler, ported to the standard library, against its 40-digit value; $\lambda_{\min}(D_N)/2\omega=m_L^{(24)}(1+\delta)$ with $\lvert\delta\rvert<1\%$ at $\omega=0.01$ (measured $+0.536\%$); the first-order law on $e_1$ at every shift. |
| E | The first-order law on $e_1$ at $L=\log5,\log7$, where the margin itself ($2.5\times10^{-17}$, $2.1\times10^{-22}$) is below what double precision reads off a matrix of norm $1$ and only $\lvert\,\lVert V\rVert-1\rvert<10^{-12}$ is asserted. |
| F | The congruence $D=\frac\omega2(I+V^*)P(I+V)$ to $10^{-16}$; $P\succeq0$ at five shifts; and that $\lambda_{\min}(P)-\lambda_{\min}(D)/2\omega$ is quadratic in $\omega$ with the 40-digit coefficient. |

Two honesty notes are carried in the record itself. First, $\lambda_{\min}(D)$
is a $10^{-9}$ quantity read off matrices of norm $1$, so double precision
carries about four of its digits; the sharp assertions in group D are
contraction and $\lvert\delta\rvert<1\%$, and the comparison against 40 digits
is made at the $10^{-3}$ relative level the arithmetic supports (measured:
$5.7\times10^{-5}$). Second, the mass extrapolation is two-point and is
compared at $10^{-5}$, while the $10^{-13}$ agreement with the 40-digit assembly
is the sharp check.

The port of the Weil-form assembler needed complex digamma and trigamma, which
the standard library does not have; they are the Bernoulli asymptotic series
with argument shifted by recurrence, and reproduce `mpmath` to $10^{-15}$
relative. $m_L^{(24)}=6.2475139201\times10^{-8}$ against the 40-digit
$6.2475139834\times10^{-8}$: ten digits of the matrix, eight of the eigenvalue.

---

## 3. The corrected sweep at $L=\log3$

All rows: $N=24$, Gauss--Jacobi with 40 nodes per atom, 40 digits, records
[`cmgj_om*_log3_N24.json`](../numerics/exploratory/README.md). $m_L^{(24)}=6.2475139834\times10^{-8}$
(even block; odd block $1.8606\times10^{-5}$), $Q_{0,L}[e_1]=4.3474052991\times10^{-4}$.

| $\omega$ | $1-\lVert V_N\rVert$ | $\lambda_{\min}(D_N)/2\omega$ | ratio to $m_L^{(24)}$ | $(\text{ratio}-1)/\omega$ | $e_1$ ratio | $(\lambda_{\min}(P)-\lambda_{\min}(D)/2\omega)/(m_L\omega^2)$ |
|---|---|---|---|---|---|---|
| 0.002 | $1.25085\times10^{-10}$ | $6.2542610028\times10^{-8}$ | 1.00107995 | 0.539976 | 0.99883430 | 0.0362201 |
| 0.01 | $6.28139\times10^{-10}$ | $6.2813855951\times10^{-8}$ | 1.00542161 | 0.542161 | 0.99467622 | 0.0363546 |
| 0.02 | $1.26313\times10^{-9}$ | $6.3156282872\times10^{-8}$ | 1.01090263 | 0.545131 | 0.99060697 | 0.0365528 |
| 0.05 | $3.21053\times10^{-9}$ | $6.4210662474\times10^{-8}$ | 1.02777941 | 0.555588 | 0.98581621 | 0.0371707 |
| 0.1 | $6.60857\times10^{-9}$ | $6.6085742918\times10^{-8}$ | 1.05779264 | 0.577926 | 1.00202729 | 0.0382715 |

### 3.1 What is superseded, and why

The $e_1$ column and the mass reproduce the contraction-margin note's Table 3.1
and Table 3.4 **to every digit printed there** --- an independent confirmation of
the whole assembly by a completely different quadrature. The margin column does
not, at the two smallest shifts:

| $\omega$ | ratio, tanh--sinh (note, Table 3.1) | ratio, Gauss--Jacobi | difference in $\lambda_{\min}(D)$ |
|---|---|---|---|
| 0.002 | 0.99717 | 1.00108 | $9.8\times10^{-13}$ |
| 0.01 | 1.00109 | 1.00542 | $5.4\times10^{-12}$ |
| 0.02 | 1.00887 | 1.01090 | $4.7\times10^{-12}$ |
| 0.05 | 1.02764 | 1.02778 | $1.7\times10^{-12}$ |
| 0.1 | 1.05779 | 1.05779 | $<10^{-13}$ |

Every difference is at or below the $6\times10^{-12}$ floor that the note's own
Section 3.2 estimates for the tanh--sinh rule at $1/h=16$. The note was right
about its floor and drew its two smallest-$\omega$ rows from beneath it.

**Confirmed by the old programme itself.** Re-running
[`contraction_margin.py`](../numerics/exploratory/contraction_margin.py) at
$\omega=0.01$, $L=\log3$, $N=24$ with a finer step:

| $1/h$ | nodes | $\lambda_{\min}(D)/2\omega$ | ratio to $m_L^{(24)}$ |
|---|---|---|---|
| 16 (recorded) | 262 | $6.25435\times10^{-8}$ | 1.00109 |
| 20 | 330 | $6.2802275\times10^{-8}$ | 1.005236 |
| 26 | 426 | $6.2813814\times10^{-8}$ | 1.005421 |
| Gauss--Jacobi, 40 nodes | 80 | $6.2813856\times10^{-8}$ | 1.005422 |

The tanh--sinh rule converges to the Gauss--Jacobi value from below as its step
shrinks, reaching it to six digits at $1/h=26$ with five times the kernel
evaluations. The mass is $0.993732318687$ at every step, unchanged --- which is
why the mass and $e_1$ rows of the earlier note were right while the margin rows
were not: the floor lives in the oscillatory matrix elements alone. **Those two
rows are superseded; the $\omega\geq0.02$ rows stand.** Record
[`cm_om0.01_log3_N24_h26.json`](../numerics/exploratory/README.md).

What replaces them is cleaner than either. The relative excess over $m_L^{(24)}$
divided by $\omega$ is $0.5400,\,0.5422,\,0.5451,\,0.5556,\,0.5779$: linear in
$\omega$ with intercept $0.5394$ and a visible $O(\omega)$ curvature. That is
exactly the shape Proposition 2.2 of the contraction-margin note predicts --- a
first-order Galerkin truncation term $\frac\omega2(\lVert(I-P_N)Af_N\rVert^2-\lVert(I-P_N)Qf_N\rVert^2)$
plus the $-\omega m_L$ of Proposition 2.1, which is $10^{-9}$ and invisible.
Reading the intercept,
\[
 \lVert(I-P_{24})A_{0,L}f_{24}\rVert^2-\lVert(I-P_{24})Q_{0,L}f_{24}\rVert^2
 =2\times0.5394\times m_L^{(24)}=6.740\times10^{-8},
\]
and the subtracted term is computable directly from the closed-form Weil matrix
in 240 modes:
$\lVert(I-P_{24})Q_{0,L}f_{24}\rVert^2=1.5478\times10^{-8}=0.2477\,m_L^{(24)}$.
Hence $\lVert(I-P_{24})A_{0,L}f_{24}\rVert^2=8.288\times10^{-8}=1.3265\,m_L^{(24)}$
--- the sine-tail energy of the skew partner acting on the near-null vector,
inferred from a slope and a closed form, without ever assembling $A_{0,L}$.

### 3.2 The nested defect, and the limit

At $\omega=0.1$, $L=\log3$, $N=24$, nesting the defect in $N'$ modes
($D_{N\subset N'}=I_N-(V_{N'}^{\mathsf T}V_{N'})_{N\times N}$):

| $N'$ | 24 | 40 | 64 | 96 | 144 | 192 |
|---|---|---|---|---|---|---|
| ratio to $m_L^{(24)}$ | 1.05779 | 1.03784 | 1.02075 | 1.01028 | 1.00253 | 0.99848 |

**The sequence crosses below $1$.** That is what Proposition 2.2 requires: its
$N'\to\infty$ first-order coefficient is
$-(m_L^{(N)})^2-\lVert(I-P_N)Qf_N\rVert^2-\langle(I-P_N)Qf_N,(I-P_N)Af_N\rangle$,
whose first two terms are now known. Dropping only the cross term, the predicted
limit ratio is
\[
 1-\omega\Big(m_L^{(24)}+\frac{\lVert(I-P_{24})Qf_{24}\rVert^2}{m_L^{(24)}}\Big)
 =1-0.1\times0.24775=0.97523
\]
at $\omega=0.1$ (the $m_L^{(24)}$ inside the bracket is $10^{-8}$ and does not
matter). The measured sequence is heading there. The note's "roughly like $1/N'$", read off two nestings, describes the
first step; measured against the limit the approach is closer to $N'^{-0.6}$,
and the apparent steepening of the raw ratios ($0.83,1.28,1.73,3.46$ as
successive local exponents) is the crossing, not a decay law. **The $1/N'$
reading is withdrawn; the sign, the monotonicity and the crossing are what
Proposition 2.2 predicts and they are confirmed.**

At $\omega=0.05$, $N'=64$ gives $1.00637$ (the note's tanh--sinh run: $1.0061$).

---

## 4. The horizons

### 4.1 $\log5$ and $\log7$

Records [`cmgj_om*_log5_N24.json`](../numerics/exploratory/README.md),
[`cmgj_om*_log7_N24.json`](../numerics/exploratory/README.md); $N=24$, 40--70
nodes per atom, 50--70 digits. Atoms: $n\leq4$ at $\log5$, $n\leq6$ at $\log7$.

| $L$ | atoms | $m_L^{(24)}$ | $\omega$ | $1-\lVert V_N\rVert$ | $\lambda_{\min}(D_N)/2\omega$ | ratio | $(\text{ratio}-1)/\omega$ | $e_1$ ratio |
|---|---|---|---|---|---|---|---|---|
| $\log3$ | 2 | $6.2475\times10^{-8}$ | 0.002 | $1.2509\times10^{-10}$ | $6.25426\times10^{-8}$ | 1.00108 | 0.540 | 0.998834 |
| | | | 0.01 | $6.2814\times10^{-10}$ | $6.28139\times10^{-8}$ | 1.00542 | 0.542 | 0.994676 |
| $\log5$ | 4 | $2.5445\times10^{-17}$ | 0.002 | $5.1012\times10^{-20}$ | $2.55060\times10^{-17}$ | 1.00241 | 1.207 | 0.997521 |
| | | | 0.01 | $2.5750\times10^{-19}$ | $2.57497\times10^{-17}$ | 1.01199 | 1.199 | 0.988141 |
| $\log7$ | 6 | $2.1067\times10^{-22}$ | 0.002 | $4.2290\times10^{-25}$ | $2.11449\times10^{-22}$ | 1.00372 | 1.860 | 0.997491 |
| | | | 0.01 | $2.1456\times10^{-24}$ | $2.14560\times10^{-22}$ | 1.01849 | 1.849 | 0.988228 |

The within-basis caveat matters more here than at $\log3$. The recorded
converged margins at $\log5,\log7$ are $9.3\times10^{-18}$ and
$6.8\times10^{-28}$; the $24$-mode values above are $2.5\times10^{-17}$ and
$2.1\times10^{-22}$ --- a factor $3$ out at $\log5$ and six orders of magnitude
at $\log7$. Both sides of every comparison here are computed in that same
truncated basis, and none of them says anything about the converged margin.

Three readings.

- $V_{\omega,L}$ is a **strict contraction at every horizon and shift tested**,
  by margins down to $4\times10^{-25}$.
- The excess over $m_L^{(24)}$ is **exactly linear in $\omega$** at each
  horizon: the slope is $0.540$, $1.20$, $1.85$ at $\log3,\log5,\log7$, constant
  in $\omega$ to three digits across a factor of five in $\omega$. It is the
  Galerkin term and it vanishes with $\omega$; the transfer side and the form
  side agree in the limit.
- The margins span $6.2\times10^{-8}$ to $2.1\times10^{-22}$. **Over fourteen
  orders of magnitude, a kernel built from $\Gamma$, $\sinh$, $\exp$ and the
  integers below $e^L$ reproduces the smallest eigenvalue of the localized Weil
  form to within a term that is linear in $\omega$ and computable.** At
  $\log5$, nesting in 64 modes gives $0.98793$, again straddling.

### 4.2 Where a fixed basis stops working

Two horizons further out, at $\omega=0.01$, $N=24$:

| $L$ | atoms | $m_L^{(24)}$ | $\lambda_{\min}(D_N)/2\omega$ | plain ratio | nested in $N'=64$ |
|---|---|---|---|---|---|
| $\log{11}$ | 10 | $9.358\times10^{-28}$ | $4.924\times10^{-27}$ | 5.262 | 0.98595 |
| $\log{13}$ | 12 | $4.849\times10^{-29}$ | $8.046\times10^{-28}$ | 16.59 | 0.98780 |

The reason is structural rather than numerical. The margin $m_L^{(N)}$ collapses
superexponentially in $L$; the first-order Galerkin term, being a tail energy of
$A_{0,L}f_N$ in a fixed number of sine modes, does not collapse nearly as fast.
Their ratio is $0.005,\,0.012,\,0.018$ at $\log3,\log5,\log7$ and then $4.3$ and
$15.6$: somewhere between $\log7$ and $\log{11}$ the truncation overtakes the
object. Nesting removes it and both horizons return to within $1.5\%$ of
$m_L^{(24)}$. **Past $\log7$ the nested defect is not a refinement but a
requirement**, and the contraction-margin note's rule --- compare within a
basis, never a Galerkin $\lambda_{\min}(D_N)$ against a converged $m_L$ --- needs
this addition: at long horizons, do not compare a *plain* Galerkin
$\lambda_{\min}(D_N)$ against $m_L^{(N)}$ in its own basis either.

---

## 5. The cumulative Cayley coordinate

$Z_{\omega,L}=(I-V)(I+V)^{-1}$ and $P_{\omega,L}=\frac2\omega\re Z$ are the
coordinates of \[Wilson-lines manuscript, Proposition 7.7\]; $P\succeq0$ is the
positive-real criterion of its Proposition 7.8.

**Proposition 5.1 (the congruence).** $I-V^*V=\frac\omega2(I+V^*)P(I+V)$
whenever $I+V$ is invertible; hence $P\succeq0\iff\lVert V\rVert\leq1$.

*Proof.* $Z(I+V)=I-V$ and $(I+V^*)Z^*=(Z(I+V))^*=I-V^*$, so
$(I+V^*)(Z+Z^*)(I+V)=(I+V^*)(I-V)+(I-V^*)(I+V)=2(I-V^*V)$. $\square$

**Proposition 5.2 ($P$ is even in $\omega$).** On the exact compression,
$V_{-\omega,L}=V_{\omega,L}^{-1}$, hence $Z_{-\omega,L}=-Z_{\omega,L}$ and
$P_{-\omega,L}=P_{\omega,L}$. Consequently
\[
 P_{\omega,L}=Q_{0,L}+O(\omega^2),
\]
with an expansion in even powers of $\omega$ only, where
$\lambda_{\min}(D_{\omega,L})/2\omega=m_L-\omega m_L^2+O(\omega^2)$ carries a
first-order correction.

*Proof.* $K_{-\omega}=1/K_\omega$ by definition, and both are Laplace transforms
of causal distributions on $\Re p>b$ (the poles of either lie in
$\lvert\Re p\rvert\leq b$). Compression to $[0,L)$ is a homomorphism of the
causal convolution algebra (contraction-margin note, Section 2.1), so
$V_{-\omega,L}V_{\omega,L}=P_L(K_{-\omega}K_\omega)P_L=I$. Then
$Z_{-\omega}=(I-V^{-1})(I+V^{-1})^{-1}=(V-I)(V+I)^{-1}=-Z_\omega$, so
$\re Z$ is odd in $\omega$ and $P=\frac2\omega\re Z$ is even. Its value at
$\omega=0$ is $\re G_{0,L}=Q_{0,L}$, from $Z=\tanh(\omega G_{0,L}/2)+O(\omega^3)$.
$\square$

No exponential and no evenness of $g_\omega$ is needed for the parity: it is
just that the transfer inverts under $\omega\mapsto-\omega$ and that compression
respects products of causal symbols.

**Proposition 5.3 (the Galerkin term is common).** Let $f_N$ be the normalized
minimizer of $Q_{0,L}$ on $E_N$ with eigenvalue $m_L^{(N)}$, and let $P_N$ be
built from the Galerkin block $V_N$. Then
\[
 \langle f_N,P_Nf_N\rangle=m_L^{(N)}
 +\frac\omega2\Big(\lVert(I-P_N)Af_N\rVert^2-\lVert(I-P_N)Qf_N\rVert^2\Big)+O(\omega^2),
\]
the same first-order truncation term as $\langle f_N,D_Nf_N\rangle/2\omega$ in
Proposition 2.2 of the contraction-margin note. The two estimators therefore
differ at second order in $\omega$, and the Galerkin bias is common to both.

*Proof.* With $G=G_{0,L}$ and $X_N=P_NXP_N$: $V_N=I-\omega G_N+\frac{\omega^2}2(G^2)_N+O(\omega^3)$,
$(I+V_N)^{-1}=\frac12(I+\frac\omega2G_N)+O(\omega^2)$, so
$Z_N=\frac\omega2G_N-\frac{\omega^2}4\big((G^2)_N-G_N^2\big)+O(\omega^3)$ and
$\frac2\omega\re Z_N=Q_N-\frac\omega2\re\big((G^2)_N-G_N^2\big)+O(\omega^2)$.
On $f\in E_N$, $\langle f,\big((G^2)_N-G_N^2\big)f\rangle=\langle(I-P_N)G^*f,(I-P_N)Gf\rangle
=\lVert(I-P_N)Qf\rVert^2-\lVert(I-P_N)Af\rVert^2$, the cross terms cancelling in a
real space. $\square$

**What the numbers show.** At $L=\log3$, $N=24$, 40 digits, the congruence
residual $\max_{jk}\lvert D-\frac\omega2(I+V^*)P(I+V)\rvert$ is
$5.4\times10^{-42}$ to $1.1\times10^{-41}$ over the sweep --- the identity, at
working precision. $\lambda_{\min}(P)>0$ at every shift. And
\[
 \frac{\lambda_{\min}(P)-\lambda_{\min}(D)/2\omega}{m_L^{(24)}\,\omega^2}
 =0.03622,\;0.03635,\;0.03655,\;0.03717,\;0.03827
\]
at $\omega=0.002,\ldots,0.1$: constant to three digits over a factor of fifty in
$\omega$, so the difference is $0.03620\,\omega^2m_L$ exactly as Propositions 5.2
and 5.3 together require (the $+\omega m_L^2$ they also predict is $10^{-9}$
relative and invisible). In double precision only $\omega\geq0.02$ carries this,
the difference being $10^{-14}$ in absolute terms at $\omega=0.01$.

**What it is worth.** As an *estimator* of $m_L$ in a fixed basis the Cayley
coordinate buys nothing, because Proposition 5.3 says the dominant error --- the
Galerkin term --- is identical. What it buys is structural: $P$ is the object
whose positivity is the positive-real criterion, it is even in $\omega$ for a
one-line reason, and the congruence of Proposition 5.1 is now checked to
$10^{-41}$ rather than quoted. The $\omega^2$ coefficient $0.0362$ is a measured
number attached to the exact compression's second-order behaviour that the
defect's own second-order coefficient ($1.6$, from the previous note's two-point
fit) does not isolate.

---

## 6. The phase-matched lattice control, against the transfer

Under RH the localized Weil form is an absorption,
$Q_{0,L}[f]=\sum_\rho\lvert\widehat F(\gamma_\rho)\rvert^2$, so its margin is how
well a function supported in $I_L$ can avoid the Riemann zeros in frequency.
Replacing the zeros by an unfolded lattice of the same density gives a control.
The [Wilson-lines review of 17 September](../../wilson-lines/reviews/review_claude-fable-5-1_2026-09-17.md),
Section 3, showed that control is **phase-dependent**: the Gram points
($\theta(g_n)=n\pi$) sit half a step off in either direction depending on where
the sequence starts, and only the half-shifted lattice $\theta(t)=(k-\frac12)\pi$
--- the Gram's-law idealization, whose counting function matches $N_{\rm sm}$ on
average --- tracks the zeros.

Programme
[`gram_control_vs_transfer.py`](../numerics/exploratory/gram_control_vs_transfer.py),
record
[`gram_control_T3000_N24.json`](../numerics/exploratory/README.md);
all values are even-block $\lambda_{\min}$ in the **same $N=24$ sine basis the
transfer is compressed to**, point sets truncated at $T=3000$ (2469 Gram points;
$T=600$ changes the $\log_{10}$ gaps by less than $0.01$).

| $L$ | zeros (exact form) | Gram $n\geq-1$ | Gram $n\geq0$ | half-shifted | transfer, $\omega=0.01$ |
|---|---|---|---|---|---|
| $\log3$ | $6.2475\times10^{-8}$ | $+1.995$ | $-1.413$ | $+0.0297$ | $+0.00235$ |
| $\log5$ | $2.5445\times10^{-17}$ | $+2.444$ | $-1.768$ | $+0.3398$ | $+0.00518$ |
| $\log7$ | $2.1067\times10^{-22}$ | $+2.587$ | $-1.346$ | $-0.1190$ | $+0.00796$ |

(columns after the first are $\log_{10}$ of the ratio to the zeros; lowest
points $9.667$, $17.846$, $14.518$ against $\gamma_1=14.1347$.)

As ratios, the phase-matched lattice gives $1.071$, $2.187$, $0.760$; the
transfer gives $1.0054$, $1.0120$, $1.0185$, and those three are $0.540\omega$,
$1.20\omega$, $1.85\omega$ --- they go to zero with the shift, while the lattice
numbers do not go anywhere.

**The reading.** The best available zero-free surrogate for the margin, chosen
with the right phase, is correct to a factor that wanders between $0.76$ and
$2.19$ across three horizons and shows no sign of a law. The transfer, which
contains no zero and no lattice --- $\Gamma$, $\sinh$, $\exp$, the integers below
$e^L$, and two exponential smoothings --- is correct to first order in $\omega$
exactly, with a computable and vanishing remainder. The lattice reproduces the
*density* of the zeros; the transfer reproduces the *form*. That is what the
transfer knows that a lattice does not, and it is the reason the compression is
worth computing: the dichotomy is about $\lVert V_{\omega,L}\rVert$ at *all*
horizons, and a density surrogate cannot decide it even at one.

Note what this does **not** say. The transfer's agreement is with $m_L^{(N)}$ in
a truncated basis at horizons where $m_L>0$ is known; it is the first-order law
$\lVert f\rVert^2-\lVert V_{\omega,L}f\rVert^2=2\omega Q_{0,L}[f]+O(\omega^2)$,
which is an identity, verified. No zero is located and nothing is proved about
horizons where the margin is not known.

---

## 7. What remains

Item 1 of the opening note's plan is now closed. What it leaves:

1. **The second-order coefficient.** The exact compression's
   $\lambda_{\min}(D)/2\omega=m_L-\omega m_L^2+c_2\omega^2+O(\omega^3)$ and
   $\lambda_{\min}(P)=m_L+c_2'\omega^2+O(\omega^4)$ with $c_2'-c_2=0.0362\,m_L$
   measured at $L=\log3$, $N=24$. $c_2$ involves
   $2Q^2+[Q,A]$ (Proposition 2.1 of the contraction-margin note) and $c_2'$
   involves $\re(G^3)$ and the $\omega^3$ term of the generator. Computing
   either against the measurement would test the expansion at the next order and
   is within reach of the present instrument. Worth doing before anything else,
   because it is the only place where $A_{0,L}$ --- the compressed Hilbert
   transform of the interval and the odd part of the comb --- enters a number
   that has been measured.
2. **The Lax--Phillips dictionary at $\omega=\frac12$**, object by object, and
   what the $\omega$-deformation can and cannot move (opening note, item 2).
3. **The Beta law from a radial chain** --- the one question here that is about
   Loewner evolution. Proposition 1.2 above sharpens the target: the archimedean
   delay is exactly $-\frac12\log U$ with $U\sim\mathrm{Beta}(\frac a2,\omega)$,
   so what a radial chain would have to produce is $e^{-2\tau}$ Beta-distributed,
   not merely some additivity fraction.
4. **The comb in the Bost--Connes algebra** (opening note, item 4).
5. **The passivity statement** (opening note, item 5).

---

## 8. Status of every statement

- **Written proof, unconditional:** Propositions 1.1, 1.2, 5.1, 5.2, 5.3.
- **Registered computation (standard library, replayed byte-identically):**
  Section 2; 53 cases; record
  [`contraction-margin-checks.json`](../numerics/records/contraction-margin-checks.json).
- **Labelled numerical computation (unregistered, `mpmath`, 40--90 digits):**
  Sections 3, 4, 5 and 6, every row with a record in
  [`numerics/exploratory/`](../numerics/exploratory/README.md).
- **Superseded:** the $\omega=0.002$ and $\omega=0.01$ margin rows of Table 3.1
  of the contraction-margin note (§3.1 above); the "roughly $1/N'$" reading of
  its §3.3 (§3.2 above).
- **Reading:** the inferred value $\lVert(I-P_{24})Af_{24}\rVert^2=1.3265\,m_L^{(24)}$
  (§3.1), which combines a measured slope with a computed term and assumes the
  expansion of Proposition 2.2 is the whole first-order story; the $N'^{-0.6}$
  approach to the nested limit (§3.2); the reading of §6.
- **Not claimed:** anything about the zeros; any positivity; any horizon where
  $m_L>0$ is not already known; convergence of the sine basis, which is visibly
  incomplete at every $N$ used here.

See the [notes index](README.md) and the [investigation index](../README.md).
