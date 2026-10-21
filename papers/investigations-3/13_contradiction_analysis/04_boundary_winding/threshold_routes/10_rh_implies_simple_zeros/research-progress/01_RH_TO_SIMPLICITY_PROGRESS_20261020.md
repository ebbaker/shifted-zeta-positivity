# RH-to-simplicity progress

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded turn metadata. Separate same-model internal review;
no specialist review.

**State: RH ⇒ simplicity remains unproved.** The structural transfer
and the bounded arithmetic, source-control and energy investigations
are recorded below. The latest concrete gain is [Note 16][n16]: under
RH, each fixed compact Gevrey taper of order 1<sigma<2 has actual complete
error E_(N,w)≪(loglog N)^B/log N for every fixed B>1+2sigma. The direct
infimum corollary gives d_N²≪_B(loglog N)^B/log N for every fixed B>3,
by choosing one sufficiently large fixed p in w_p. This supersedes the
previous no-global-upper/no-convergence status for that fixed class.
No sharp first-order constant, multiple-zero exclusion or new excluded
height interval has been obtained. The [program][program] retains its
event-exclusion gates; no novelty or optimality claim is made.
The original scope was selected in [chat 0003][origin]; this round is
[chat 0004][current].

| Task | Current status | Evidence / unresolved requirement |
| --- | --- | --- |
| RHS-00 | Complete: scope and literature | [Opening analysis][opening] §§1–2, 9; primary inputs rechecked in [review 02][review]. No methodological priority or relative-difficulty theorem claimed. |
| RHS-01 | Complete: inherited transfer and control screen; strengthened through Note 09 | Opening §§3–6. [Note 01][n1] proves finite root-label continuation under RH, exact endpoint/middle complement, and retained multiplicity phase atom. [Note 05][n5] adds an RH-conditional, uniformly close positive-source control with an exact double event, unchanged leading tail and pole residue one. [Note 09][n9] adds a distinct ordinary-Dirichlet control with exact finite data, positive coefficients, residue one and RH-sized prime-counting error, but failed reflection/entireness. |
| RHS-02 | Actual full-norm Gevrey upper rate proved; event-excluding signed gate remains unmet | Notes 01–03 treat fixed-width, finite-prime and signed-error envelopes, and finite Euler-control rejection. [Note 04][n4] proves exact subtraction costs, a sharp actual-tail asymptotic and the fully optimized rational-power absolute-payment barrier. Note 05 screens one finite horizontal-shift consumer exactly and identifies the normalized source control's failed Dirichlet-series premise. [Note 06][n6] proves a sharp full-window correlation resolution cost, the additive-one limit of universal phase positivity, and a local Möbius-energy cost. [Note 07][n7] proves localized quadratic-to-linear dominance and exact theta Jensen coalescence rates. [Note 08][n8] obtains vanishing finite-sum relative error, a stronger energy envelope and a broader signed-Fourier kernel cost. [Note 09][n9] constructs near-zero prime-payment kernels outside the fixed class and improves sufficient multiplicity-extraction cost under a separately certified gap. [Note 10][n10] closes the full-height improvement for those uniform phase-return constructions, with leading costs at least one/three-halves. [Note 11][n11] proves the sharp leading one-half absolute-envelope floor for the full admissible nonnegative-kernel class under complete gamma/pole budgets, with a joint prime-cost/logarithmic-spread bound. [Note 12][n12] gives both matched extractors leading square-root summand count, while retaining inverse-mollifier residues and endpoint energy. [Note 13][n13] supplies a nonnegative companion for certified-gap polynomial kernels and a complete quartic prime-cost comparison. The strip and general-gap extensions remove the specified support/factorization restrictions; [Note 14][n14] proves nearly complete off-diagonal cancellation for the original theta modes at all large heights. Note 13 §§7–8 proves the complete remote-gap comparison and a normalized separate-payment lemma; §9 proves quantitative coherent saturation of the exact signed base sum. The endpoint continuation identifies the physical/scaled phase-energy costs, while Hopf/Julia reproduces the Poisson consumer and formal bare Euler heat diverges. [Note 15][n15] computes the exact multiplicity-dependent ratio energy, its heat crossover and signed arithmetic cancellation cost; Note 12 §§5–7 quantifies the linear Möbius taper and closes fixed-a/log N untapered convergence even in the simple case; Note 15 §§7–9 retains the prime-error remainder, Jensen variance and full heat drift. Note 12 §§8–9 extends the full-norm obstruction to logarithmically growing damping and finite-order smooth tapers; Note 15 §9.1 shows the tested fixed-time averages remain endpoint-compatible. Note 12 §§10–12 pays the actual Gevrey local transfer and proves stronger prescribed-approximant lower constants, while its tested absolute transfer allowance fails. [Note 16][n16] now proves actual full-norm convergence and the rate (loglog N)^B/log N for each fixed compact Gevrey order 1<sigma<2, together with the direct d_N² infimum corollary. Note 12 §13 gives actual joint-scale lower rates for the declared moving almost-linear tapers. These gains supply no opposing estimate at an original multiple zero. |
| RHS-03 | Finite-wall subtask proved under RH; strict surplus still gated | Note 01 §2 covers every finite cap and multiplicity. Cap mass remains `(m-1)pi`; the Gaussian sign is event-compatible. Note 04 identifies the exterior inverse-square sum needed for effective deflation, but wall continuation gives no quantitative upper bound for it. |
| RHS-04 | Full-height approximation bound proved for a fixed class; no new exclusion | Note 16 bounds the actual norm at all heights for each fixed compact Gevrey order 1<sigma<2. Structural statements cover all finite heights/multiplicities under RH. Neither the logarithmic upper allowance nor the stated arithmetic failure ranges give an all-zero signed exclusion or a new theta exclusion class. |
| RHS-05 | Reviews of bounded attempts completed; full-argument review remains gated | [Reviews 02–16](../reviews/README.md) check the stated proofs, imports and controls. Review 04 checks uniform optimization and certified subtraction; [review 05][review5] checks source positivity, the whole-tail relative bound, exact residue normalization and the distinct curvature control. [Review 06][review6] checks correlation normalization, clustered configurations, phase minima and local pole/energy constants. [Review 07][review7] checks local dominance, complete coefficient errors and Hermite coalescence. [Review 08][review8] checks the reciprocal estimates, complete energy saddle, kernel budgets and canonical-system premise. [Review 09][review9] checks the normalized arithmetic control, translated kernels and stable extraction with their distinct premises. [Review 10][review10] checks the primary approximation, return-height bound and scoped complete-envelope comparison. [Review 11][review11] checks continuous Gram/Fubini, all-zero and all-prime-power payments, stable Poisson and the full-class scope. [Review 12][review12] checks the evaluation, mollifier, signed-kernel and energy comparisons, including its §§5–10 endpoint, ratio-energy, heat crossover, damping/taper closures, actual Gevrey transfer and arithmetic-remainder continuations. The bounded Lean check verifies only the abstract projection inequality. [Review 13][review13] checks the two kernel extensions and full theta-mode cancellation. [Review 14][review14] checks the complete remote-gap comparison and bounded event attempts; [review 15][review15] checks coherent saturation and its explicit constants. [Review 16][review16] checks the complete moving-line convolution, both height regimes, quantitative global rate, direct infimum corollary, compact-height asymptotic and moving-taper lower rates. Same-model internal validation; no simplicity theorem. |

## Quantitative outcomes

- Under RH, [Note 16][n16] proves E_(N,w)≪(loglog N)^B/log N for
  each fixed compact Gevrey taper of order 1<sigma<2 and every fixed
  B>1+2sigma. Its uniform full-height domination pays the remaining
  norm, so E_(N,w)→0. Since d_N² is an infimum over all length-N
  Dirichlet polynomials, d_N²≤E_(N,w); choosing one fixed
  w_p(u)=exp(1−(1−u)^(-p)) with B>3+2/p gives the direct corollary
  d_N²≪_B(loglog N)^B/log N for every fixed B>3. No changing taper,
  novelty, best-known-bound, optimality or simplicity claim is made.
- Note 16 also proves the complete fixed-height asymptotic with error
  O_(T,w)(loglog N/(log N)²), and convergence of the complete local
  profile-mass sum for 1<sigma<2. These do not remove the extra global
  logarithmic allowance or establish a sharp first-order constant.
- [Note 12 §13][n12] proves an actual joint-scale lower rate for the
  declared almost-linear flat tapers w_eta: at an exact order-m zero,
  m≥2, liminf eta_N^(2m−3)(log N)E≥A_m/|rho|² under its stated
  uniform transfer condition. For eta_N=(log N)^(-theta), 0<theta<1,
  a double costs (log N)E≳(log N)^theta; a triple with
  1/3<theta<1/2 forces the full norm to diverge despite vanishing
  extracted coefficient. The fixed-taper upper theorem is not uniform
  in this moving family.

- Under RH, Note 12 §12 proves the actual local profile of every fixed
  normalized Gevrey-flat logarithmic taper admitting the compact
  extension specified in §12, at a zero of any exact multiplicity. The full reciprocal tail is exponentially small in a
  positive power of log N; the finite Laurent remainder is paid.
  Hence liminf (log N)E_(N,w)≥Σ C_m(w)/|rho|², over distinct zeros.
  No simplicity or inverse-derivative moment is assumed. This is a
  full-norm lower bound, not a matching upper or global asymptotic.
- Note 12 §11 proves C_m(w)>m² for every fixed flat taper, with infimum
  m², and the sharp joint inequality C2≥(9δ²+10δ+1)/(4δ), δ=C1−1>0.
  If A and B are the reciprocal-square masses of exact simple and
  exact double zeros, the actual lower bound is at least
  K+[sqrt(B(4A+9B))−3B]/2, K=Σm²/|rho|². Its uniform gap is positive
  when A,B>0. Sharpness concerns the two local costs, not the global
  norm. Fixed Gevrey approximants approach the same model infima.
- Note 12 §10 proves that w_p(u)=exp(1−(1−u)^(-p)), p>1, removes
  the earlier extracted-coefficient obstruction under RH. Its tested
  transfer from damped approximants nevertheless has an absolute
  allowance growing at least as a exp(9a/16); this does not establish
  growth of the actual error. That failed payment remains valid as a
  scoped comparison; Note 16's different, coherent convolution proof
  now supplies the full upper rate for each fixed 1<sigma<2 taper.
- The [Lean check](../numerics/lean/README.md) passed in the existing
  Multipass Linux VM. It verifies the projection identity and three
  consequences from explicit real-inner-product hypotheses. It does
  not formalize the analytic hypotheses, actual zeta transfer or
  RH-to-simplicity.


- At an exact order-m critical zero, k=m−1, Note 12 §8 proves that
  damping c loglog N/log N with 0<c<=k has normalized complete squared
  error limsup at least m²/|rho zeta^(m)(rho)|², after division by
  (log N)^(2(k−c)). Under RH the truncation remainder has the same
  normalized limsup. Thus c<k forces unbounded error and c=k prevents
  convergence. No sufficient threshold or conclusion for arbitrary
  oscillating damping subsequences is asserted.
- For every fixed C^(k+1) taper with first nonzero endpoint derivative
  w^(k)(1), Note 12 §9 gives an explicit positive full-error limsup
  at multiplicity k+1 and infinite limsup at larger multiplicity.
  The positive constant is [(k+1)|w^(k)(1)|/(|rho|^(k+1)
  |zeta^(k+1)(rho)|)]². Infinitely flat and N-dependent tapers remain
  outside this result; a higher endpoint order supplies no upper bound.
- Note 15 §9.1 proves that the actual ratio energy increases between
  any two fixed positive heat times for sufficiently small epsilon.
  Fixed integrable time averages retain the simple-zero first-order
  mass regardless of endpoint multiplicity. Their o(epsilon)
  renormalized excess therefore cannot exclude a multiple endpoint.
  The positive-source cosh control also refutes structural positivity
  of J−H/2; it does not share the original theta arithmetic.


- Note 12 §7 proves, for every fixed a>0, that the untapered damped
  Möbius polynomial has limsup complete squared error at least
  exp(-2a) B², where B=limsup |M(x)|/sqrt(x). A simple critical zero
  gives B>=1/|rho zeta'(rho)|>0; any multiple critical zero gives
  B=infinity. Under RH the truncation remainder I has the same limsup.
  Thus the previously proposed o(1/log N) payment at a=2 is impossible
  even in the all-simple case. The §6 liminf comparison stays valid;
  its proposed research target is superseded. Sections 8–9 extend the
  closure to the explicitly stated growing-damping and taper classes.
- Note 15 §7 computes the exact squared error of the exponentially
  smoothed prime-error approximation: epsilon times sum d_m/|rho|²,
  up to o(epsilon), where d_1=0, d_2=1/4 and d_m>0 for m>=2.
  A double conjugate pair forces coefficient at least 1/[2(gamma²+1/4)].
  The checked RH prime-error mean square contains m², so it does not
  remove this remainder. Section 8 proves the independent-prime Jensen
  allowance adds variance with liminf at least one, too large for the
  original O(epsilon) ratio error. Neither yields an opposing bound.


- At heat time t=v epsilon² in the zeta-shift convention, Note 15 §5
  proves J_t(epsilon)/epsilon tends to sum C_m(sqrt(v/2))/(sigma²+gamma²).
  The profile strictly decreases from c_m to m/2 for m>=2; for a double
  C_2(r)=1+1/[4(1+r²)]. Its global large-v excess has coefficient
  (K_sigma−M_sigma)/4, one-quarter of Burnol's multiplicity penalty at
  sigma=1/2. A multiple endpoint therefore requires an O(epsilon)
  energy drop over an O(epsilon²) heat interval. Smooth positive source
  moments do not give the uniform time bound needed to exclude it.
- In Note 15 §6 the exact Möbius Gram diagonal is asymptotic to
  (log(2pi)−EulerGamma)/(2 zeta(2) epsilon), while the full norm tends
  to one. The absolute double sum diverges for epsilon<=1/2. Its signed
  first-order remainder must be retained to absolute scale epsilon;
  no sharp upper bound for that remainder is obtained.
- Note 12 §6 proves liminf (log N) I_(N,a/log N)
  >=(sqrt K−sqrt(aC))_+². At a=2 every multiple zero requires a positive
  truncation payment; an exact double pair gives the explicit lower
  bound (sqrt(2Z+3/(gamma²+1/4))−sqrt(2Z))². The checked RH estimates
  apply at larger damping. Section 7 supersedes seeking a vanishing
  bound in this coupled regime: this fixed sequence cannot converge.


- Under RH, the weighted squared error of xi(s)/xi(s+epsilon), and also
  zeta(s)/zeta(s+epsilon), divided by epsilon tends to
  sum c_m/(sigma²+lambda²), with c_m=m(1−binom(2m,m)/4^m).
  [Note 15][n15] proves tightness through exact positive Poisson mass.
  At sigma=1/2 the coefficient is Z/2 plus nonnegative multiplicity
  excess, where Z=2+EulerGamma−log(4pi). A double conjugate pair adds
  1/[2(gamma²+1/4)]. The available upper Z permits this excess;
  no upper Z/2, effective cutoff, or simplicity conclusion is obtained.
- For the exact linear-logarithmic polynomial V_N in Note 12 §5,
  a double zero forces limsup E_N>=4/(|rho|^4 |zeta''(rho)|²)>0;
  multiplicity at least three forces infinite limsup. This quantitative
  extraction uses the complete Mellin norm. Wei–Wu already prove that
  convergence of this sequence implies simplicity; it is not a known
  consequence of RH. Burnol's squared-multiplicity lower constant and
  BCF's simplicity-dependent sharp upper retain their distinct scopes.


- At an isolated order-m endpoint, the physical phase density satisfies
  integral rho_t² dx=pi m(m−1)/(4t)+O(t^(−1/2)) on a fixed event window.
  Its temporal cost is logarithmically divergent. With positive derivative
  scale beta(t)=sqrt(2t), the outer-root cap instead has squared-density
  cost C_m/sqrt(2t)+O(1), with C_2=pi+2, which is time integrable.
  Both caps retain phase (m−1)pi. The full spacetime phase form includes
  its derivative-scale term. This is a quantitative comparison, not an
  opposing source estimate or a collision exclusion.


- Under RH, a target-vanishing component centered on the independently
  empty interval near ordinate zero can recover a fixed base test's exact
  signed zero sum from its complete coherent absolute-prime envelope:
  0<=U(f+(gamma²−g²)delta^(q+1/2)r_delta)−S_gamma(f)
  <=K_f,q,g delta^(1/2−q), along delta gamma in the positive integers.
  Note 13 §9 gives an explicit q=2 constant and retains every pole,
  prime power and zero multiplicity. This can strictly improve the base
  absolute envelope. It does not improve on the directly retained signed
  value or show that value is below two. The opposing pole/prime terms
  grow exponentially; no evaluation-cost or varying-base height gain is
  asserted. The unbounded family has infimum equal to the actual target
  multiplicity, which is an optimization scope statement, not its estimate.


- For any fixed integer q>=2 and fixed independently known gap |lambda|<g,
  multiply the centered sinc^(2q) kernel by
  ((x+gamma)^2-g^2)/(gamma^2-g^2). Although this signed test has a potentially
  helpful negative pole term, its complete envelope is no smaller than
  the carrier's for every bandwidth once gamma is sufficiently large.
  The comparison retains exact signed poles; its threshold depends on q,g
  and is not numerically instantiated. An elementary g=1/8 gap is proved.
  A remote added component with zero target value also cannot help when
  its prime contribution is paid separately. Coherent mixed payment is treated separately by §9;
  normalization-changing combinations remain outside these results.


- For the actual positive theta modes, D(a)=sum_n(f_n(a)^2+f_n'(a)^2)
  equals c_theta a^(-4)+O(a^(-6)), with c_theta>0. The complete first-jet
  energy J(a)=H(0,a)^2+H_x(0,a)^2 is O(a^5 exp(-pi a/4)). Consequently
  the retained cross term X satisfies 0<=1+X/D=J/D<<a^9 exp(-pi a/4).
  This unconditional large-height asymptotic excludes any fixed or algebraic
  relative diagonal coercivity for that exact mode decomposition. It is
  not a signed lower bound for J or a simplicity conclusion.
- Note 11 §7 removes finite Fourier support: for each nonnegative kernel
  holomorphic on a strip wider than one-half with quadratic strip decay,
  the same joint prime-cost/moment inequality and leading one-half floor
  hold under RH and the complete gamma/pole budgets. Constants in those
  inequalities do not require a uniform strip-width margin across kernels.
- Note 13 §6 removes the polynomial assumption from exact zero-side gap
  replacement. Finite moves of paired odd real zeros produce a globally
  nonnegative companion no larger outside the certified central gap,
  preserving bandwidth when present and admitting a strip version.
  Asymmetric gaps and non-even kernels are included; negatives in other
  gaps and transfer of arithmetic/gamma/pole budgets are not.


- Note 12 uses a classical Riemann–Siegel expansion with value error
  O(gamma^(-5/4)) and a discrete Cauchy formula whose alias error is
  explicitly paid. RH supplies normalized logarithmic-derivative error
  gamma^(-3/4+o(1)) for the geometric widths, at total summand count
  gamma^(1/2+o(1)). The matched one-width test also reaches exponent
  one-half, with error gamma^(-1/2+o(1)). Thus the earlier exponents one
  versus three-halves are specific to the declared Euler-sum payment.
  This is an asymptotic exact-arithmetic count, not an executed certificate,
  optimal complexity or a simplicity margin.
- The Riesz Möbius mollifier at a=c/log gamma has paid absolute error
  gamma^(1/2+o(1)) Y^(-a+a/log log gamma). A sufficient vanishing-error
  choice has log Y=K(log gamma)^2, K>1/(2c); this is not a necessary
  length bound. A functional-equation shift must retain every crossed
  reciprocal-zeta residue, including the displayed double-zero term.
- With an independently certified noncentral gap, every admissible even
  polynomial times a nonnegative carrier has a same-bandwidth globally
  nonnegative companion with a no-larger complete zero sum. For the
  quartic-times-sixth-sinc family, the signed member also has the larger
  leading complete absolute prime payment, uniformly in the gap parameters.
  No full gamma/pole-envelope dominance or general signed-kernel barrier
  is inferred. The exact signed arithmetic remains open.
- For an order-m endpoint cluster, M=m(m-1)/2 and the complete exterior
  inverse-square sum S give inverse-gap energy M/(8t)+MS/4+O(t).
  The exterior forcing is essential to the log-energy finite part.
  Fixed-reference subtraction leaves logarithmic divergence; canonical
  heat subtraction leaves a compatible positive finite part. RH supplies
  no pre-zero all-real interval or opposing energy estimate.


- At the endpoint Euler control's added zeros, the exact Poisson increment
  is `delta log(p) coth(delta log(p)/2)>2`, tending to two. Its changed
  prime coefficients and conductor are both retained.
- The absolute-prime Poisson envelope exceeds two for **every** `sigma>1`
  when `gamma>=2pi exp(9)`. The exact un-deflated fixed-width consumer
  itself also diverges at high height, by the RH local zero count.
- For the squared-sinc finite-prime test and its declared absolute-value
  envelope, optimizing all bandwidths `Delta>=1` gives
  `(1/2+o(1)) log(gamma)/log log(gamma)`. This is an estimator limitation
  at a classical multiplicity scale, not a new multiplicity theorem.
- After retaining the signed Chebyshev error and cancelling pole/main
  terms exactly, its global RH envelope pays
  `(pi c^2/12) gamma log^2(gamma)` at `Delta=c log(gamma)`.
  The envelope-only operator norm has the same order. For every prime
  `p>=101`, the exact endpoint control satisfies the identical input
  bound, including constants.
- Nonnegative logarithmic coefficients reject every nonconstant member
  of the declared finite Euler-polynomial class: a degree-`d` factor
  produces a negative coefficient at some `p^k` with `1<=k<=12^d`
  and an explicit margin. No factorization of a hypothetical original
  multiple zero into that class follows. A separate positive-source
  control adds isolated double zeros while retaining the displayed
  gamma factor, conductor one and simple-pole order. It fails the
  ordinary Dirichlet series and nonnegative logarithmic coefficients,
  so these completion normalizations alone do not fill the gap.
- At a hypothetical ordinary double event, RH's deflated product gives
  `D_s>=6s^4 h2^2/a^4` for `0<s<=a^2/4`. The sign is compatible with
  the event and is shared by the control; it provides no contradiction.
- For fixed Poisson width `delta`, deleting every noncentral zero within
  `H=c log(gamma/(2pi))` leaves actual tail tending to
  `delta^2/(pi c)` and involves asymptotically
  `(c/pi) log^2(gamma/(2pi))` zeros counted with multiplicity. Note 04
  supplies complete tail, location and membership budgets. A narrow
  certified multiplicity interval can recover two; it does not force one.
- For `K(v)=[delta^2/(delta^2+v^2)]^n`, every arithmetic derivative stays
  at `Re s=1/2+delta>1`. Nevertheless its full absolute-prime envelope,
  optimized over **both** `delta>1/2` and integer `n>=1`, has infimum
  `(1/(4sqrt(pi))+o(1)) log(gamma)/sqrt(log log(gamma))`.
  The declared nonnegative trigonometric-combination class likewise
  retains infimum `(1/4+o(1)) log(gamma)`. Signed estimates and exact
  certified subtraction are not covered by these estimator limitations.

- Under RH, Note 05 merges consecutive distinct high zeros `b<c` into an
  exact double pair `+/-a` through an explicit positive-source change.
  Its uniform relative error is at most
  `epsilon=4e/b^2+4(d+e)^2/(b^2c^2)->0`, with `d,e` defined there.
  It preserves the leading theta tail, functional equation, displayed
  completion, pole residue one and normalization at positive real
  infinity. It fails ordinary Dirichlet-series arithmetic, with an
  algebraic large-real correction. The added event escapes to infinity;
  this screens fixed positive tolerance and the named structural
  premises, not height-dependent certified margins or exact theta data.
- A **separate** polynomial control retains any fixed strict slack below
  theta's global log-concavity floor and still has an endpoint double
  zero under RH. This curvature claim is not asserted for the normalized
  merger. The finite horizontal-shift consumer is an exact average of
  Poisson consumers, no smaller than its starting-width value; the
  positive Euler-quotient estimate gives the opposite direction from
  the needed upper bound. No event exclusion follows from either screen.

- For the declared squared-sinc **full-window second moment**, an
  all-zero certificate requires correlation excess below two. Note 06
  proves the sharp geometric floor
  `liminf Delta W/N^(3/2)>=1/2`, where `W` is the window width and
  `N` counts multiplicities. It also pays projection to an enlarged
  interval by `N^2/(pi^4 Delta^3 R^3)` without dropping exterior zeros.
  The floor holds before any arithmetic error and includes clusters;
  it is not a bound against every localized correlation method.
- Retaining all inequalities valid for arbitrary unimodular
  multiplicative prime phases gives exact minimum
  `mu(V)=-C_V+1+o(1)`. The optimized complete envelope gains only
  one additive unit over Note 02, retaining leading constant `1/2`.
  This universal phase class does not include actual-height or
  multiple-zero conditioning; no bad actual-zero phase is asserted.
- A zero `rho` of exact multiplicity `m` forces a sharp local weighted
  Möbius energy of order `alpha^(1-2m)`. For a double,
  `liminf alpha^3 E(alpha)>=16/|rho zeta''(rho)|^2>0`.
  The exact ordered Möbius correlation must carry that cost; the
  checked RH upper bound still permits it. The finite-interval
  consequence is a limsup, not a lower-liminf theorem. No derivative
  moment assuming simplicity was used.

- For every nonnegative compact observation measure, the full-zero
  quadratic excess obeys `E>=2(L_gamma-1)`, where `L_gamma` is its matched
  nonnegative linear zero mass. An excess margin `eta` transfers a linear
  margin at least `eta/2`. The linear kernel has bandwidth `Delta`; direct
  exact payment of the quadratic diagonal can reach bandwidth `2Delta`.
  Exterior zeros and all errors remain. For the untruncated finite
  projection, the matched kernel also dominates the original Fejér kernel.
  Signed observation forms require their own cross-term estimate.
- For the unchanged theta Jensen family, an exact multiplicity-m zero
  produces an m-root Hermite cluster with spacing of order `d^-1/2` and
  positive Laguerre margin of order `d^(1-m)`. For a double at
  `r=-gamma^2`, the separation is `2|r|/sqrt(d)+O(d^-1)` and the margin
  is `r^2 f''(r)^2/(2d)+O(d^-2)`. Complete positive-moment remainder
  bounds pay the approximation. Strict finite Jensen hyperbolicity was
  already proved under RH in Investigation 22 and permits repeated
  limiting zeros; it cannot be passed to strictness of the limit.

- Under RH, at `delta=c/log gamma`, the fixed finite Euler sum with
  `N=ceil(gamma^(1+epsilon))` approximates `delta zeta'/zeta` with error
  `gamma^(-epsilon/2+o(1))`. Cauchy's inequality pays the derivative
  remainder while the cutoff stays fixed. This supplies finite-distance
  relative precision; it gives neither the required sign nor an endpoint
  lower bound for `zeta''(rho)`.
- Direct use of a checked RH reciprocal estimate improves the recorded
  energy bound to `log(2+E(alpha)) <<_epsilon alpha^-1 log^(2+epsilon)(1/alpha)`.
  Both height regimes and all compact-height poles are retained. This
  is stronger than Note 06's Mertens-envelope bound, but still permits
  every fixed polynomial divergence, including a double zero's cubic cost.
- For any admissible nonnegative bandlimited kernel with `h(0)=1`,
  mass `I` and `I Delta<=eta<2` for fixed `eta`, Poisson summation forces
  positive first Fourier samples on a prime shell and exact absolute
  payment at least `(I^2/pi^2+o(I^2)) exp(pi/I)`. With explicit gamma
  localization and pole budgets, the sharp leading envelope remains
  `(1/2+o(1)) log gamma/log log gamma`, even allowing arbitrary Fourier
  signs. The class `I Delta>=2` and unbudgeted kernels are not covered.

- Under RH, Note 09's normalized reciprocal-tail control inserts zeros
  of any prescribed order m>=2 while retaining residue one, positive
  ordinary/logarithmic coefficients and exact agreement on all integers
  supported on primes at most P. Its logarithmic-weight changes are
  O_m(log P/sqrt P) uniformly; its ratio to zeta is
  1+O_(m,epsilon)(P^-epsilon) on each fixed Re s>=1/2+epsilon.
  It retains the global RH prime-counting error class. Exact reflection,
  entire completion and Note 08's unchanged-zeta tail remainder fail.
- Two translated nonnegative kernels give I Delta tending to two from
  below and absolute prime cost C tending to one; three give I Delta
  tending to three, I tending to zero and C asymptotic to
  [-zeta'(3/2)/zeta(3/2)] I/pi. Complete gamma/pole budgets can be paid,
  and explicit scalar-square versions exist. This refutes unrestricted
  extensions of Note 08's prime-payment lower bound. Note 10 now resolves
  the full-height comparison for this uniform-alignment construction:
  RH forces log X <= (2+o(1)) log log R, and the complete envelopes have
  leading costs at least one and three-halves, respectively, against
  L/log L. Both exceed Fejér's one-half. A refinement gives
  log X <= 2 ell + 6 log ell + O(1), ell=log log(dR).
  The prime-payment counterexamples themselves remain valid.
- With a separately certified noncentral gap d, geometric widths
  a_j=d 2^(j-r) give a nonnegative product kernel with leakage at most
  C log gamma 2^(-r(r+1)) and arithmetic error amplification below two.
  For d of order 1/log gamma, the stated sufficient fixed-sum cutoff
  improves from gamma^(3/2+o(1)) for the matched single-width payment to
  gamma^(1+o(1)). This recovers any actual multiplicity; it does not force
  one, supply the gap, or establish optimal computational complexity.

- [Note 11][n11] proves under RH, for every admissible nonnegative
  bandlimited h with h(0)=1, a joint cost
  C+I M >= c I^3 exp(pi/I) for 0<I<=1/4, where M is the logarithmic
  pair moment of h/I. No Fourier-sign or I Delta restriction remains.
  The complete gamma budget gives M<=(1+o(1))L, and the sharp leading
  absolute-prime envelope floor is (1/2-o(1))L/log L for the entire
  declared class. Exact pole retention still requires its stated
  negative-part budget. This closes that absolute-payment route, not
  the retained signed arithmetic or all possible multiplicity methods.

The frozen [exact algebra contract][contract] and [replay][replay] passed
265 rational fixtures. They check finite constants and the control sum,
not theta zeros or the infinite analytical estimates. It was unchanged
and not rerun for Notes 04–11, which received analytical cross-checks. No
numerical sign scan or manuscript was started. The original BW09, HFCE and PSC registers
retain their existing states; the earlier manuscript was reviewed but
not changed.

## Remaining task and stopping boundaries

The next positive gate is still **one independently justified signed
arithmetic estimate under RH and the putative event**. For the finite-prime
comparison, the precise target is `Q_Delta>G_Delta+P_Delta-2` at a declared
bandwidth, with all terms defined in Note 02. Equivalently, Note 03's
exactly cancelled formula requires `(2/V) I>G+R-2`; this is a target,
not an additional result. Its displayed RH envelope is insufficient. An unquantified successful
bandwidth at every zero is merely equivalent to simplicity. A promising
continuation must obtain a bound, reject the endpoint control on its own
complete data, and explain how it improves on direct first-jet exclusion.

Do not repeat product-only phase positivity, discard endpoint deficits,
continue the Euler Dirichlet series termwise into the critical strip,
or optimize the already-failed absolute-value envelopes again. Do not
switch to a Gaussian numerical campaign using separately paid Hermite
remainders. Do not reapply only a global RH Chebyshev-error bound to Note 03's
single partial-summation transport. Note 04 now quantifies justified
zero deflation and closes its specified rational-power absolute-payment
test; do not repeat that optimization or its nonnegative-combination
appendix without an additional input. A successful deflated estimate
would need certified noncentral membership and enough count, location,
tail and signed arithmetic precision to put the upper endpoint below two.
Note 05 also prevents replacing the missing arithmetic estimate by
fixed relative source accuracy, the leading tail and the named completion
normalizations alone. Its normalized control fails the ordinary
Dirichlet series; the separate strong-curvature control must not be
given that control's preservation list. An exact theta or discrete
arithmetic argument must still produce an opposing inequality.
Note 06 closes neither signed correlations nor the Möbius route in
general. It rules out a leading improvement from universal phase
positivity in the selected Fejér envelope and quantifies the specific
full-window second-moment cost. A useful localized correlation estimate
must pay the exterior zeros and fit the absolute remaining slack;
an average with error o(N) is insufficient to exclude one double.
The Möbius calculation still lacks a subcubic upper bound for its
signed off-diagonal sum or total energy. Shifted negative moments may not be continued to
zero shift at fixed height outside their hypotheses.
Note 07 additionally shows that this nonnegative localized quadratic
consumer cannot avoid a matched one-point test at the same bandwidth.
Its conclusion is not a prohibition against a better linear kernel or
separately controlled signed correlations. Strict finite Jensen signs
and fixed-degree/increasing-shift hyperbolicity do not supply a margin in
the unshifted infinite-degree limit. Do not start a coefficient-shift
scan to address that different limit.

The finite-zeta precision gap in [review 07][review7] is now filled at
`w=c/log gamma`: Note 08 uses RH to control reciprocal error for the
longer fixed sum. This does not fill the endpoint coefficient gap or
give the sign needed by the existing multiplicity consumer. The stronger
energy upper bound likewise remains far above the exact cubic event cost.
Do not treat either numerical exponent improvement as a simplicity margin.
The restriction I Delta<=eta<2 belongs to Note 08's earlier proof.
[Note 11][n11] now proves the leading one-half floor for every admissible
nonnegative bandlimited kernel under the complete gamma/pole budgets,
without a restriction on I Delta or Fourier signs. Do not repeat this
absolute-payment optimization with a new kernel. A retained signed
arithmetic estimate or another consumer requires its own justified gain.

The canonical-system assessment in [review 08][review8] checks the primary
source's separate no-common-real-zero premise. Strict half-plane positivity
alone permits common real factors. A finite-integrable system with constant
initial data cannot directly realize unmodified xi's infinite exponential
type; singular or infinite endpoint constructions are not ruled out.

Note 09 now supplies explicit kernels in part of the class left outside
Note 08: near-zero absolute prime payment is possible with mass tending
to zero and I Delta tending to three. Do not extend the fixed margin
below two in the prime-cost bound to that class. [Note 10][n10] now proves
that the uniform root-of-unity return height forces full-envelope leading
cost at least d/2 for the stated d=2,3 constructions. Do not repeat that
alignment construction as a proposed improvement. Note 11's different
full-tail proof now covers partial/nonuniform alignment, other translation
patterns and all other kernels in the declared admissible class when the
complete budgets hold. Its joint moment payment preserves the small-C
counterexamples. The extraction result requires an independent noncentral gap
and returns two at a double zero; its sharper finite precision is not
a signed exclusion. The new arithmetic control fails exact reflection
and the full zeta tail, so it must not inherit Note 05's different
completion-preservation list.

Actual-height/event-conditioned signed arithmetic, correlated full-source
estimates, and consumers without the displayed complete-envelope
hypotheses remain outside these scoped conclusions. Omitting a required
gamma or pole payment is not a valid change of consumer. No successful all-height signed exclusion estimate has been obtained. Weak Mertens and all-zero negative
moments of zeta's derivative cannot be imported as consequences of RH.

Notes 12–13 refine these stop rules. Use the same corrected value algorithm
when comparing extraction methods; do not present the earlier Euler-sum
exponents as a general complexity separation. Do not move an inverse-zeta
contour across the critical line without every reciprocal-zero residue.
The polynomial gap replacement is an exact zero-side comparison, not a
transfer of arithmetic error or gamma/pole budgets. Ordinary theta moment
bounds do not control inverse-gap energy; the pre-zero interval used in
Rodgers–Tao is unavailable from RH alone. These are scoped assessments,
not prohibitions against a new signed estimate using unchanged arithmetic.

The latest continuations close two class loopholes, not the signed gate:
finite Fourier support is unnecessary for Note 11's stated strip-analytic
absolute-payment theorem, and a polynomial factorization is unnecessary
for Note 13's central-gap replacement. Their complete-budget limitations
remain. Note 14 rules out fixed or algebraic relative diagonal coercivity
for the actual raw theta modes; their cross terms cancel to exponential
relative accuracy even away from events. A coherent signed estimate may
still use that cancellation. The checked full-window density formula has
error far above one double zero's normalized excess and supplies no
shrinking-window theorem.

The remote-gap comparison in Note 13 §§7–8 pays the exact signed pole,
gamma and full prime-power terms together. Do not claim a gain for its
fixed sinc-power family by displaying only the negative pole factor, or
for a target-vanishing remote component whose prime sum is paid separately.
Section 9 now resolves one coherent mixed-prime construction quantitatively:
it approaches exactly S_gamma(f), with nonnegative explicit excess. Do not
interpret that conversion or its unrestricted infimum as a bound on the
unknown multiplicity. Arbitrary carriers and varying-base height estimates
remain outside these comparisons. The localized reciprocal-energy check
and the coherent positive theta-tail check supplied no opposing event
bound: the first retains the same exponent deficit, and the second has a
signed differentiated kernel. The primitive/reflection identity likewise
retains exactly the event contact and its boundary term.

The endpoint recheck makes two further boundaries explicit. Hopf's
strict normal derivative of xi/xi' is 1/m; its full Julia inequality is
exactly the existing Poisson bound. The named derivative-zero theorem
excludes the open left half-strip, not a common critical-line zero.
Formal nonnegative Euler-heat logarithmic coefficients also do not give
a positive-time arithmetic representation: their prime terms fail the
term test in every half-plane. The completed theta heat retains all
mixed derivatives. None of these checks closes RHS-02 or licenses an
endpoint energy bound from source-moment upper bounds alone.

The ratio identity in Note 15 supplies a multiplicity-dependent exact
coefficient, with no opposing upper bound. Do not replace its harmonic
upper Z by Z/2, or discard mass outside fixed local zero windows without
the complete Poisson accounting. Note 12 §5 also prevents importing
linear-taper convergence from the different RH-conditional damped
approximants. The BCF negative derivative hypothesis assumes simplicity;
the Wei–Wu conclusion explicitly contains it. The polynomial-taper local grouped-pole model does not pay its
contour/other-zero remainder. Section 12 now pays the corresponding
actual local transfer for the specified fixed Gevrey-flat class. These are scoped
limitations and quantitative costs, not a closure of the arithmetic lane.

The new heat comparison is a joint-limit statement: do not interchange
the heat-time and shift limits, differentiate compact-parameter value
convergence, or claim monotonicity at arbitrary finite parameters. The
exact source covariance controls linear harmonic mass; it leaves the
nonlinear energy redistribution intact. The arithmetic Gram formula must
keep its square cutoff order and signed off-diagonal terms, since their
absolute double sum diverges. For the exact untapered coefficients, fixed damping a/log N is now
closed by Note 12 §7: no vanishing truncation bound can hold even in the
all-simple case. Do not repeat that proposed target. Sections 8–9 now
close convergence for c loglog N damping at c<=m−1 under an order-m
zero, and for fixed tapers whose endpoint order k is less than m.
Those finite-order and damping arguments alone prove no convergence
outside their failure ranges. Note 16 separately proves convergence for
the fixed Gevrey class specified below. The general damping envelope
must hold eventually; a subsequence cannot be substituted.
Infinitely flat tapers remain outside that finite-endpoint obstruction.
Section 10 proves coefficient suppression for the explicit w_p, p>1.
Section 12 gives actual local transfer and full-norm lower constants
for its general fixed compact-extension Gevrey class.
The prior no-global-upper/no-convergence status is superseded by
Note 16 for each fixed compact Gevrey order 1<sigma<2. Its actual rate
has an extra power of loglog N, so it supplies no opposing simple-zero
constant. Do not extend it uniformly to changing tapers or all Gevrey
orders. Note 12 §13 separately pays the declared moving almost-linear
family's local transfer and lower rate; it supplies no upper estimate.
The stronger lower constants do not themselves imply simplicity.
Note 15 §§7–8 also prohibits dropping the explicit prime-error
linearization remainder or using the independent-prime Jensen allowance
as an O(epsilon) estimate. The complete finite-window heat identity in
§9 retains its imaginary drift term and agrees with the existing double
profile; it supplies no opposing bound. Its §9.1 further rules out
global dissipation of the actual unrenormalized energy and shows that
fixed integrable time averaging loses the endpoint excess to first
order. Shrinking-time averages require their own complete estimate.
The cosh control disproves structural J−H/2 positivity but fails the
unchanged theta/arithmetic premises. Section 8.3 also shows independence
is forced for an exact binary prime-product representation; changing
correlations without changing coefficients cannot rescue that Jensen
bound. No positive gate has been closed by these comparisons.

The unconditional alternatives in the opening remain separate. The
parallel investigation remains open; this register does not mark the
unproved arithmetic and all-zero tasks complete.

[program]: ../research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md
[opening]: ../brainstorm/01_RH_IMPLIES_SIMPLICITY_20261020.md
[n1]: ../notes/01_FINITE_WALLS_ARITHMETIC_RESOLUTION_AND_GAUSSIAN_SCREEN_20261020.md
[n2]: ../notes/02_FINITE_PRIME_FEJER_RESOLUTION_TEST_20261020.md
[review]: ../reviews/02_FIRST_ANALYTICAL_ROUND_REVIEW_20261020.md
[contract]: ../numerics/EXACT_ALGEBRA_CONTRACT_20261020.md
[replay]: ../numerics/EXACT_ALGEBRA_REPLAY_20261020.json
[origin]: ../chat-histories/0003_2026-10-20T18-25-04Z_analyze-simple-zero-contradiction.json
[current]: ../chat-histories/0004_2026-10-20T18-46-56Z_investigate-rh-implies-simplicity.json

[n3]: ../notes/03_SIGNED_PRIME_TRANSPORT_AND_EULER_RIGIDITY_20261020.md
[review3]: ../reviews/03_SIGNED_TRANSPORT_AND_COEFFICIENT_REVIEW_20261020.md

[n4]: ../notes/04_ZERO_DEFLATION_AND_RATIONAL_RESOLUTION_20261020.md
[review4]: ../reviews/04_DEFLATION_AND_RESOLUTION_REVIEW_20261020.md

[n5]: ../notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[review5]: ../reviews/05_SOURCE_CONTROL_AND_SHIFT_AUDIT_20261020.md

[n6]: ../notes/06_SIGNED_CORRELATION_RESOLUTION_AND_MOBIUS_ENERGY_20261020.md
[review6]: ../reviews/06_CORRELATION_AND_MOBIUS_ENERGY_REVIEW_20261020.md

[n7]: ../notes/07_LOCAL_CORRELATION_AND_JENSEN_MARGIN_COMPARISONS_20261020.md
[review7]: ../reviews/07_LOCAL_CORRELATION_AND_JENSEN_MARGIN_REVIEW_20261020.md

[n8]: ../notes/08_RECIPROCAL_PRECISION_AND_BANDLIMITED_ARITHMETIC_COSTS_20261020.md
[review8]: ../reviews/08_RECIPROCAL_PRECISION_AND_KERNEL_REVIEW_20261020.md

[n9]: ../notes/09_ARITHMETIC_CONTROLS_TRANSLATED_KERNELS_AND_STABLE_EXTRACTION_20261020.md
[review9]: ../reviews/09_CONTROLS_KERNELS_AND_EXTRACTION_REVIEW_20261020.md

[n10]: ../notes/10_UNIFORM_PRIME_PHASE_RETURN_HEIGHT_COST_20261020.md
[review10]: ../reviews/10_PRIME_PHASE_RETURN_HEIGHT_REVIEW_20261020.md

[n11]: ../notes/11_FULL_ABSOLUTE_PRIME_ENVELOPE_AND_LOGARITHMIC_SPREAD_20261020.md
[review11]: ../reviews/11_GENERAL_KERNEL_ENVELOPE_REVIEW_20261020.md

[n12]: ../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md
[n13]: ../notes/13_CERTIFIED_GAP_SIGNED_POLYNOMIAL_KERNELS_20261020.md
[review12]: ../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md

[n14]: ../notes/14_EXACT_THETA_MODE_GRAM_CANCELLATION_20261020.md
[review13]: ../reviews/13_STRIP_KERNEL_GAP_REPLACEMENT_AND_THETA_GRAM_REVIEW_20261020.md

[review14]: ../reviews/14_REMOTE_GAP_COMPLETE_PAYMENT_AND_EVENT_ATTEMPTS_REVIEW_20261020.md

[review15]: ../reviews/15_COHERENT_REMOTE_GAP_SATURATION_REVIEW_20261020.md

[n15]: ../notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md

[n16]: ../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md
[review16]: ../reviews/16_GEVREY_GLOBAL_APPROXIMATION_REVIEW_20261020.md
