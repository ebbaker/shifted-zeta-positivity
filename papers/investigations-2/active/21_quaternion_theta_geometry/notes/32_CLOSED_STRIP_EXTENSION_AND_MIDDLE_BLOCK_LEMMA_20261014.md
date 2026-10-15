# Closed strip extension and the remaining middle-block lemma

14 October 2026 (America/New_York). Prepared for Edward Baker with
substantial LLM assistance. Recorded parent model **gpt-6-astra**,
reasoning effort **ultra**, verified from the current turn metadata.
Parallel work checked the arithmetic sources, the signed cutoff
implications, and the analytic boundary issue. This is research with an
internal LLM audit, not external peer review or formal verification.

This continues [Note 31](31_SIGNED_CUTOFF_LEMMA_AND_THRESHOLD_EIGHT_THIRDS_20261014.md)
in response to the request for the remaining closed strip
\(5/2\le\theta\le8/3\). The full requested strip is **not yet proved**.
The unconditional result below covers
\[
                 61/24\le\theta\le8/3,
\]
including both endpoints of this new substrip, at sufficiently large
height. In fact it covers every \(\theta\ge61/24\) in the allowed time
range. Thus the previously excluded boundary \(8/3\) is resolved.
The smaller interval \(5/2\le\theta<61/24\), including \(5/2\), remains
open. Section 6 gives a proved conditional reduction of the entire
requested strip to one precise middle-block estimate.

## 1. Unconditional statement

Use \(\partial_tH=-\partial_x^2H\), \(h_k=\partial_x^kH\),
\(E=h_0^2+h_1^2\), and
\(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\), \(j=0,1\). Put
\[
 L=\log(x/(4\pi)),\qquad\theta=tL,\qquad\omega=L/4,\qquad
 \theta_*=\frac{61}{24}.
\]
Keep the explicitly nonvanishing Stirling carrier \(M_t\), its logarithmic
derivative input \(\alpha=M_0'/M_0\), and the two analytic branches of
[Note 17](17_UNIFORM_OUTER_CUSP_SIGNS_AND_THRESHOLD_FOUR_20261014.md):
\[
 s_+=(1+ix)/2,\qquad
 Q=M_t(s_+)\zeta\bigl(s_++t\alpha(s_+)/2\bigr),\qquad
 \Gamma=|M_t(s_+)|.
\]
Here \(M_t(s)=M_0(s)\exp(t\alpha(s)^2/4)\). Its definition does not
divide by a physical jet.

**Theorem 1.** There is a finite, presently unevaluated \(X_*\) such
that, uniformly for
\[
 x\ge X_*,\qquad 0<t\le1/2,\qquad \theta\ge61/24,                 \tag{1}
\]
\(Q\ne0\) and, with \(\phi=\arg Q\),
\[
 \frac{1}{2|Q|}
 \left(h_0,\frac{h_1}{\omega},\frac{h_2}{\omega^2},
                         \frac{h_3}{\omega^3}\right)
 =(\cos\phi,-\sin\phi,-\cos\phi,\sin\phi)+O(L^{-1}).             \tag{2}
\]
In particular \(E>0,\mathcal L_0>0,\mathcal L_1>0\) throughout (1).
Reflection gives the corresponding full signs at negative heights.
The lower boundary in (1) is included; there is no additional
\(+\varepsilon\) in its statement. Fixed positive margins inside the
proof pay the small losses of the imported exponent-pair bounds.

**Corollary 2.** For the exact staircase cutoff of Note 31, every integer
\(N\ge8\), and \(j=0,1\), throughout (1),
\[
 \mathcal L_j^{(N)}\ge-A_j^*(t,x)E,\qquad
 \mathcal L_j^{(N)}\ge-e^{-2ax}B_j e^{-cN^2}.                  \tag{3}
\]
The source-defined \(A_j^*\) is independent of \(N\) and locally bounded;
\(B_j,c\) are independent of \(t,x,N\). These are an exact relative-loss
bound with power \(p=0\), and a zero-energy-loss bound with the complete
Gaussian pair-tail allowance. Section 5 specifies the constants.
The full energy and full stationary sets remain the observations.

The finite certificate through height 112 is unchanged. Neither (1) nor
(3) supplies the unevaluated transition from 112 to \(X_*\), or a result
in the still smaller cusp. No RH conclusion follows.

## 2. Primary arithmetic inputs and their endpoint scope

Write a pair as \((k,l)\) and use the following limiting pairs:
\[
 \begin{aligned}
 P&=(13/84,55/84),\\
 AP&=(13/194,76/97),\\
 A^2P&=(13/414,359/414),\\
 D&=(18/199,593/796),\\
 R&=(4742/38463,35731/51284).
 \end{aligned}                                               \tag{4}
\]
The letter \(D\) here names this particular pair; it is not an assertion
that an arbitrary pair transformation preserves exponent-pair status.

The primary references are:

- Jean Bourgain, *Decoupling, exponential sums and the Riemann zeta
  function*, [arXiv:1408.5794v2](https://arxiv.org/pdf/1408.5794v2),
  Section 5, Theorem 6, printed pages 20–21.
- Timothy S. Trudgian and Andrew Yang, *Toward optimal exponent pairs*,
  [arXiv:2306.05599v3](https://arxiv.org/html/2306.05599v3),
  Section 1.1, equations (1.1)–(1.2), Lemma 1.1, and equation (1.10).

Bourgain proves \(P\) with an arbitrary positive loss in both coordinates.
Trudgian–Yang prove \(D,R\) with such losses and give the \(A\)-process
\[
 A(k,l)=\left(\frac{k}{2k+2},\frac{k+l+1}{2k+2}\right).
\]
Their definition is uniform over arbitrary intervals
\(I\subset(M,2M]\). For \(f(y)=(T/(2\pi))\log y\), its derivative is the
exact monomial in that definition with parameter \(\sigma=1\).
All derivative-approximation errors are zero. Conjugation supplies
the opposite phase sign. At the heights used below \(T/(2\pi)\ge M\).
Thus, for every fixed \(\eta>0\), each pair in (4) gives
\[
 \sup_{I\subset(M,2M]}
 \left|\sum_{n\in I}n^{-iT}\right|
 \ll_\eta T^{k+\eta}M^{l-k},\qquad T\ge2\pi M.                \tag{5}
\]
Bourgain also discusses proper subintervals explicitly; no completed
dyadic block or unproved maximal completion is being substituted.
His proof's logarithmic completion cost is absorbed by choosing a
sufficiently small initial positive loss before fixing \(\eta\) in (5).

The limiting coordinates in (4) are not used with zero loss.
For the descendants of \(P\), continuity of \(A\) allows the initial
positive loss to be chosen so that both resulting coordinates differ
from (4) by at most \(\eta\). More explicitly, under equal positive
coordinate increments \(\epsilon\), the two coordinate increments of
\(A\) are respectively
\[
 \frac{\epsilon}{2(1+k)(1+k+\epsilon)},\qquad
 \frac{\epsilon(1+k-l)}{2(1+k)(1+k+\epsilon)}.
 \tag{6}
\]
They are nonnegative and at most \(\epsilon/2\) on the pairs used here.
A further application is continuous as well. If both final increments
are at most \(\eta\), their total contribution to the logarithm of (5)
is at most \(\eta\log T\), since \(1\le M\le T\).
The bound (5) is a full bound in this range, with no secondary error
term suppressed.

## 3. Exact margins for the new closed boundary

For a block with \(\beta=\log M/\ell\), where
\(\ell=\log(u/(4\pi))\), the unperturbed weighted exponent is
\[
 F_{k,l}(\beta;\theta)
  =k+(l-k-\tfrac12)\beta-\frac{\theta}{4}\beta(1-\beta).
                                                               \tag{7}
\]
At \(\theta=\theta_*=61/24\) its second derivative is \(61/48>0\).
It suffices to check the endpoints on each of these five intervals:

| pair | beta interval | left value of \(F\) | right value of \(F\) |
| --- | --- | --- | --- |
| \(A^2P\) | \([1/5,3/10]\) | \(-43/13800\) | \(-869/662400\) |
| \(AP\) | \([3/10,3/8]\) | \(-459/310400\) | \(-145/198656\) |
| \(D\) | \([3/8,81/200]\) | \(-215/407552\) | \(-21807/254720000\) |
| \(R\) | \([81/200,3/7]\) | \(-4368359/49232640000\) | \(-1/1176\) |
| \(P\) | \([3/7,1/2]\) | \(-1/1176\) | \(-11/2688\) |

These intervals cover \([1/5,1/2]\) exactly, with shared endpoints.
Convexity gives the uniform margin
\[
 F_{k,l}(\beta;\theta_*)\le-\mu_*,
 \qquad \mu_*=\frac{21807}{254720000}.                         \tag{8}
\]
No rounded decimals or sampled interval checks are needed.

Fix \(\eta=\rho=1/100000\). On the shrinking complex disc used below,
increase the starting height until
\[
 \theta_u=t\ell\ge\theta_*-\rho,\qquad
 \sigma=\Re w\ge\tfrac12+\theta_u/4-\delta,\qquad
 0\le\delta\le\rho,\quad \delta=O(L^{-1}).                     \tag{9}
\]
For \(\beta\le1/2\), the three losses in the exponent are at most
\(\eta,\delta/2,\rho/16\). The harmless final extension
\(\beta\le1/2+O(1/(u\ell))\) costs at most \(\rho\), after increasing
height. Its contribution tends to zero uniformly even when
\(\theta_u\le\ell/2\) grows. The conversion \(T\asymp u\) changes only
bounded factors in (5).
The exact surviving margin is
\[
 \mu_*-\rho(1+1/2+1/16+1)
       =\frac{76399}{1273600000}>\frac1{20000}.                \tag{10}
\]
Thus every high block has a fixed power saving even at
\(\theta=61/24\). This is why (1) includes its lower endpoint.

## 4. Uniform analytic replacement and full physical signs

Follow the complete two-branch approximation and disc bookkeeping in
Notes [17](17_UNIFORM_OUTER_CUSP_SIGNS_AND_THRESHOLD_FOUR_20261014.md)
and [19](19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md).
For \(|z-x|\le1/L\), write \(z=u+iv\), and let
\[
 w=w_\pm(z)=\sigma+i\tau,\qquad
 N_{\rm RS}=\left\lfloor\sqrt{u/(4\pi)+t/16}\right\rfloor .
\]
Here \(|\tau|\asymp u\), and
\(\log N_{\rm RS}\le\ell/2+O(1/u)\).
The Riemann–Siegel cutoff \(N_{\rm RS}\) is different from the source
cutoff \(N\) in (3). Conditions (9) hold uniformly in (1). In particular
\(\sigma\ge9/8\) for sufficiently large height.

For each fixed nonnegative integer \(r\), set
\[
 S_r=\sum_{n\le N_{\rm RS}}(\log n)^r
                     e^{t\log^2n/4}n^{-w}.
\]
We claim, uniformly on this disc and throughout (1),
\[
              S_r-(-1)^r\zeta^{(r)}(w)=O_r(L^{-1}).           \tag{11}
\]
For \(r=0\), the \(n=1\) difference is zero.

**Small indices.** Split at \(Y=\exp(\ell/5)\). The inequality
\(e^q-1\le qe^q\) bounds the small-index discrepancy by
\[
 \frac t4\sum_{n\ge2}(\log n)^{r+2}
                    n^{-(1/2+\theta_u/5-\delta)}.             \tag{12}
\]
Write \(\theta_u=\theta_*-\rho+s\), \(s\ge0\). Since
\[
 \frac12+\frac{\theta_*}{5}=\frac{121}{120},\qquad
 \frac1{120}-\frac{\rho}{5}-\rho>\frac1{240},
\]
the exponent in (12) is at least \(1+1/240+s/5\).
With
\[
 D_r=\sum_{n\ge2}(\log n)^{r+2}n^{-1-1/240}<\infty,
\]
(12) is at most
\[
 \frac{D_r}{4\ell}(\theta_*-\rho+s)2^{-s/5}=O_r(\ell^{-1}).
\]
This last bound explicitly covers growing \(\theta_u\), rather than
treating it as fixed. The omitted ordinary zeta tail is
\[
       O_r(\ell^r e^{-\ell/40})                              \tag{13}
\]
because \(\sigma\ge9/8\).

**High indices.** On the exact dyadic blocks
\((M,\min(2M,N_{\rm RS})]\), starting at \(M=Y\), use
\[
 W_r(y)=(\log y)^r e^{t\log^2y/4}y^{-\sigma}.
\]
For large height it is decreasing:
\[
 y(\log W_r)'=\frac r{\log y}+\frac t2\log y-\sigma
       \le\frac{5r}{\ell}-\frac12+\delta+O(1/u)<0.
\]
Exact Abel summation and (5) therefore give a bound by a constant times
\(W_r(M)T^{k+\eta}M^{l-k}\), \(T=|\tau|\).
Choose the pair from the table by the left block endpoint \(\beta\).
The bound is valid on the whole block irrespective of whether its
right endpoint crosses a table boundary, since (5) already controls
every shortened subinterval. Equations (8)–(10) give
\[
 \sum_{Y<n\le N_{\rm RS}}(\log n)^r
             e^{t\log^2n/4}n^{-w}
      =O_r(\ell^{r+1}e^{-\ell/20000}).                        \tag{14}
\]
There are \(O(\ell)\) blocks; the final shortened block is included.
Equations (12)–(14) prove (11).

**All approximation errors.** The imported input remains D. H. J.
Polymath, *Effective approximation of heat flow evolution of the
Riemann xi function*, [Theorem 1.3](https://arxiv.org/html/1904.12438v2#S1),
as matched to the analytic branches in Notes 17 and 19. The complete
positive weight sum in \(e_A+e_B\) is \(O(u^{1/4})\), while its per-index
error is \(O(L^2/u)\). The third error obeys the same explicit exponent
formula as before. Hence
\[
 e_A+e_B=O(L^2u^{-3/4}),\qquad
 e_{C,0}\ll\exp[-\ell/4-\theta_u\ell/16]=O(u^{-2/5}).          \tag{15}
\]
For the last inequality,
\(1/4+(\theta_*-\rho)/16>2/5\).
All three imported errors are paid.

Carrier magnitudes on the disc are comparable to \(\Gamma\).
Equation (11) for \(r=0\), (15), and Schwarz reflection give
\[
 H(t,z)-Q_+(z)-Q_-(z)=O(\Gamma/L),\qquad |z-x|\le1/L.         \tag{16}
\]
The half-plane \(\Re w\ge9/8\) gives both
\[
 \zeta(9/8)^{-1}\le|\zeta(w)|\le\zeta(9/8)
\]
and bounded fixed-order logarithmic derivatives of \(\zeta\).
The carrier is consequently nonzero. Cauchy estimates on (16), followed
by the carrier differentiation from Note 17, prove all four components
of (2). The moving floor cutoff is never differentiated.

Increase \(X_*\) until \(\omega\ge1\) and every normalized component error
in (2) is at most \(1/8\). The phase-uniform quadratic estimates of
Note 17 then give
\[
 E\ge2|Q|^2\ge\frac{2\Gamma^2}{\zeta(9/8)^2},\qquad
 \mathcal L_0\ge\frac{31}{16}|Q|^2\omega^2,\qquad
 \mathcal L_1\ge\frac{31}{16}|Q|^2\omega^4.                    \tag{17}
\]
This proves Theorem 1, including the real boundary \(\theta=61/24\).
The disc itself can cross slightly below that boundary; (9)–(10)
explicitly absorb this crossing.

## 5. Signed cutoffs without a new truncation assumption

Keep precisely Note 31's retained domain
\[
 \Omega_N=\{(v,n):0\le v\le\tfrac12\log N,\ n\le e^{2v}\}.
\]
Set
\[
 a=\pi/16,\quad\beta_0=\pi/\sqrt2,\quad C_0=2(2\pi^2+3\pi),
 \quad c=\beta_0/2,\quad D_0=C_0/(2\beta_0),
\]
\[
 \mathsf M_k=C_0\int_0^\infty(v+a)^k
          \exp(v^2/2+10v-\beta_0e^{4v})\,dv,\qquad0\le k\le3.
\]
These are fixed complete-source constants, independent of height,
time, and cutoff. Note 31's exact paired estimate and complete tail
payment remain unchanged:
\[
 |\mathcal L_j^{(N)}|\le e^{-2ax}\mathsf M_j\mathsf M_{j+2},
\]
\[
 |\mathcal L_j-\mathcal L_j^{(N)}|
 \le e^{-2ax}B_j e^{-cN^2},\quad
 B_j=(\mathsf M_j+\mathsf M_{j+2})D_0+D_0^2,\quad N\ge8.
                                                               \tag{18}
\]
They retain both pair sectors, every retained cross term, and every
retained/omitted and omitted/omitted pair.

Use the new independent lower envelope (17) to define
\[
 A_j^*(t,x)=
  \frac{e^{-2ax}\mathsf M_j\mathsf M_{j+2}\zeta(9/8)^2}
       {\Gamma(t,x)^2}.                                     \tag{19}
\]
It is prescribed without measuring or dividing by \(E\), independent
of \(N\), and locally bounded through every finite point of (1).
It is not bounded uniformly as height tends to infinity.
Equations (17)–(19) prove both bounds in (3). The second uses the
independently proved full sign, and has zero energy loss.
No stationarity of the raw cutoff is assumed.

## 6. What is still missing at five halves

The largest-block endpoint by itself is favorable:
\[
 F_P(1/2;5/2)=-1/672.
\]
It does not control intermediate blocks. At \(\beta=2/5\), the pair
\(D\), the best of the five pairs used here at this point, gives
\[
 F_D(2/5;5/2)=\frac9{3980}>0.                                \tag{20}
\]
Thus this upper bound permits growth and cannot yield the required
uniform small analytic remainder. It does not prove that the actual
sum grows, that a theta sign fails, or that every possible arithmetic
method is obstructed. The claim is only about these explicit bounds.
At \(\theta=5/2\), absolute treatment of low indices requires
\(\alpha<1/5\) for a split \(Y=e^{\alpha\ell}\); moving that split
past the failing \(\beta=2/5\) is not a repair.

The following precise conditional lemma isolates the missing arithmetic
without requesting a new bound on all block lengths.

**Lemma 3 (conditional middle-block transfer, closed endpoints).**
Suppose there exist constants \(C,\kappa>0,T_0\) such that, whenever
\(T\ge T_0\), \(\beta=\log M/\log T\in[7/25,47/100]\), and
\(I\subset(M,2M]\) is any integer interval,
\[
 \left|\sum_{n\in I}n^{-iT}\right|
 \le C T^{\,\beta/2+(5/8)\beta(1-\beta)-\kappa}.               \tag{MB}
\]
Then a uniform version of (2), both full strict Laguerre signs, and
the two cutoff estimates hold at sufficiently large height throughout
the **entire closed strip** \(5/2\le\theta\le8/3\).
The hypothesis (MB) is not established in this note.

**Proof of the implication.** Split low indices at
\(Y=\exp(19\ell/100)\). At \(\theta=5/2\) the absolute discrepancy
exponent is
\[
 \frac12+\frac{(5/2)(1-19/100)}4=\frac{161}{160}>1.
                                                               \tag{21}
\]
Shrinking-disc perturbations leave it at least \(1+1/320\), so its
contribution is \(O_r(L^{-1})\). Uniformly on this fixed strip,
\(\sigma\ge11/10\) at large height, which pays the ordinary zeta tail by
\(O_r(\ell^r e^{-19\ell/1000})\).

For high blocks use \(A^2P\) on \([19/100,2/7]\), and \(P\) on
\([23/50,1/2]\). The exact endpoint values at \(\theta=5/2\) are
\[
 \begin{array}{c|cc}
 A^2P&-3293/3312000&-1/4508\\
 P&-41/84000&-1/672 .
 \end{array}                                                \tag{22}
\]
Convexity supplies strict margins on both full intervals. Choose the
imported positive losses small enough to preserve those margins.
The assumed range in (MB) overlaps the first interval by \(1/175\)
and the second by \(1/100\). These fixed overlaps absorb the difference
\(\log|\tau|=\ell+O(1)\) between the exponent in (MB) and the block
coordinate used on the complex disc.

For the remaining blocks, (MB) and Abel summation give, apart from
fixed logarithmic factors, the exponent
\[
 -\kappa-\frac{\theta_u-5/2}{4}\beta(1-\beta)+o(1)
                     \le-\kappa/2                         \tag{23}
\]
at sufficiently large height, uniformly on the closed strip.
The \(o(1)\) includes the disc displacement, the change of logarithmic
coordinate, and bounded scaling constants. At the real lower boundary
\(\theta=5/2\), its disc displacement still tends to zero and is absorbed
by \(\kappa\); there is no need to discard the boundary.
Summing the \(O(\ell)\) blocks proves (11) on the full requested strip.
The imported errors (15) remain \(o(L^{-1})\), using for example the
conservative bound \(e_{C,0}=O(u^{-2/5})\).
The same analytic and cutoff transfer then applies, with
\(\zeta(11/10)\) in the lower envelope. This proves the conditional
lemma, not its unproved arithmetic hypothesis.

The middle bound is deliberately stronger than what the five proved
pair estimates currently supply. At \(\beta=2/5\), it asks for a
power improvement of \(9/3980+\kappa\) over (20).
A direct signed estimate for the complete theta observation could
avoid (MB); this sufficient condition is not claimed necessary.
The full-amplitude cutoff identity of Note 31 alone supplies no such
sign or energy-relative bound near a hypothetical collision.

## 7. Validation and continuation

The [exact checker](../numerics/check_remaining_strip_lemma.py) and
[small execution record](../numerics/REMAINING_STRIP_LEMMA_CHECKS_20261014.json)
record **97 passing exact rational checks** of the pair arithmetic,
closed interval coverage, every endpoint,
the perturbation budget, and the explicit gap at five halves.
They also check the finite arithmetic in the conditional transfer.
The parent replay was byte-identical to the producing agent's receipt.
They do not verify the external exponent-pair theorems, prove (MB),
or substitute for the analytic arguments above.

Reproduction from the repository root:

    python3 papers/investigations-2/active/21_quaternion_theta_geometry/numerics/check_remaining_strip_lemma.py --output /tmp/inv21-remaining-strip-replay.json

The [internal review](../reviews/23_CLOSED_STRIP_AND_MIDDLE_BLOCK_REVIEW_20261014.md)
records the independent audit and replay. No broad numerical sweep,
new quadrature, zero search, or finite-height certificate was run.
The finite cover through 112 and the manuscript are unchanged.
No commit, tag, or manuscript snapshot folder was created.

The next genuinely missing lemma is now (MB), or a signed physical
substitute on \(5/2\le\theta<61/24\). The new result resolves the
upper boundary \(8/3\) but does not resolve \(5/2\).
The rational threshold \(61/24\) was chosen for a short proof with
strict margins; no optimality or priority claim is made.

This is the same investigation-21 history 10, thread
01a13d83-a46b-74f0-bb7c-121d159a60a0. The actual current turn is
01a13d9a-fea1-7af1-9ca6-51d8429ae89a, with recorded gpt-6-astra and
ultra effort. The prior final reply was refreshed at the start of this
turn. The bounded final-capture worker will wait for the actual completed
response; native completion-hook activation has not been verified.
