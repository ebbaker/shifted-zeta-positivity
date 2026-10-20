# Review of arithmetic controls, translated kernels, and extraction

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded metadata. Separate same-model internal checks of
[Note 09](../notes/09_ARITHMETIC_CONTROLS_TRANSLATED_KERNELS_AND_STABLE_EXTRACTION_20261020.md); no specialist review or priority claim.

**Disposition:** the three stated quantitative results pass internal
review. The gap input, recurrence-height cost and failed control premises
remain explicit. The [progress register](../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md)
keeps the signed arithmetic, strict-surplus and all-zero gates open.

## 1. Normalized arithmetic control

**Verdict: the construction and stated scope check.** One terminology correction was incorporated before integration: the finite *reciprocal* local factors have poles only on Re s = −1/2 and no finite zeros. This replaces the sentence saying that those factors have zeros there. The no-cancellation conclusion is unchanged.

- **Exact residue and positive coefficients.** The canonical Euler-tail logarithm at 1 is real, with |b_P| = O_m(P^{-1/2}). Uniformly in the prescribed ordinate, A_P ∼ (log 2)/log P, so λ_P = b_P/A_P = O_m(log P/√P), and |λ_P| < 1 eventually. The corrected first-prime coefficient is (1+λ_P)a_{q,1} > 0. All higher local logarithmic coefficients remain positive. Exponentiating the complete local logarithm therefore gives strictly positive ordinary coefficients even when the correcting exponential alone has signed coefficients. D_P(1)=b_P gives exact residue one. The correction and tail involve only primes above P, so agreement holds for every P-smooth integer, not merely n≤P.
- **Uniform proximity and coefficient error.** The integer-tail bound (A7) and the one-sign coefficient estimate (A8) prove (A9), including ε>1/2, uniformly in both the evaluation height and prescribed ordinate. Their supremum on Re s≥1/2+ε is O_{m,ε}(P^{-ε}). This approximation is unconditional in that half-plane. The uniform logarithmic-weight discrepancy is O_m(log P/√P). It does not imply a uniform ordinary-coefficient discrepancy for every n.
- **Inserted event and failed completion.** Under RH the shifted reciprocal zeta poles lie on Re s=0 or farther left, and the finite reciprocal Euler poles lie on Re s=−1/2. Thus the open right half-plane has only the inserted B_P zeros at 1/2±iγ, each of order m, and no B_P poles. Multiplication adds these orders to any pre-existing zeta zeros. At s_0=i(τ−γ), for a nontrivial ordinate τ≠γ, the first shifted denominator has a zero; neither another reciprocal factor nor the finite factors nor exp(D_P) cancels its pole. R_P(1−s_0) is finite and nonzero. The standard reflection equation fails, and forcing reflection introduces genuine poles on Re s=1. The standard completion is not entire.
- **Exact arithmetic is not transferred.** Finite-prefix or P-smooth coefficient agreement does not supply the exact zeta Euler-sum remainder from Note 08. The latter uses all ordinary zeta coefficients equal to one. The control therefore does not refute an argument retaining that exact remainder, all Λ coefficients, or the functional equation. It also does not combine with Note 05's different preservation list to form a control preserving both lists.

**The Chebyshev extension (A11)-(A12) also checks.** Define ψ_P(x)=Σ_{n≤x}Λ_P(n). Its difference from ψ is exactly the tail term

    −2m Σ_{p>P, k≥1, p^k≤x} Λ(p^k)(p^k)^{−1/2} cos(kγ log p)

plus λ_P Σ_{P<q≤min(2P,x)} a_{q,1} log q. The first has absolute value O_m(√x): partial summation of ψ(t)≪t gives Σ_{n≤x}Λ(n)/√n≪√x. The second vanishes for x≤P; otherwise it is O_m(√P log P)≤O_m(√x log(2x)). All implied constants are uniform in P and γ once P is sufficiently large depending on m. Consequently

    ψ_P(x)−ψ(x)=O_m(√x log(2x)),

and under RH,

    ψ_P(x)=x+O_m(√x log²(2x)).

This preserves the global RH-sized Chebyshev error class, while changing the actual logarithmic weights. It is not an unchanged-arithmetic model.

**Repository comparison.** Targeted comparison found the finite Euler-factor exclusion in Note 03 explicitly leaves arbitrary infinite assemblies outside its proposition. The present shifted reciprocal *tail* is outside that finite class and improves the earlier ζ^r preservation list by retaining pole order and exact residue, finite coefficient data, and arbitrarily small uniform logarithmic-weight perturbations. No claim of exhaustive literature novelty is made. The relevant scope discipline is [avoid/07](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md); the existing controls are indexed in [result-summaries/12](../../../../../../../result-summaries/12_collision_controls_and_screening.md).

## 2. Translated kernels and discrete prime payment

**Disposition: passes.** No substantive mathematical correction was found. The construction disproves a uniform extension of Note 08's prime-payment lower bound through the boundary \(I\Delta\to2\), and an unrestricted extension of its small-mass lower bound for that payment. It does not establish an improved complete envelope as a function of target height.

1. **Continuous phase recurrence.** Unique factorization implies that every nonzero integer combination of the finitely many \(\log p\) is nonzero. Consequently each nonconstant torus character has vanishing continuous-time average. Approximation of a nonnegative bump by trigonometric polynomials gives arbitrarily large positive return times in the desired open phase set. Independence involving the number one is unnecessary here; the argument correctly avoids an integer-time Kronecker assertion. An additional lower bound on the return time, and avoidance of the discrete zeros of \(\sin (\pi\Delta R)\), are legitimate.

2. **Normalization and all prime powers.** The translated Fejér sum has exactly \(h(0)=1\), \(I=d/(\Delta D_R)\), and the Fourier phase sum in (K2). Continuity gives zero endpoint samples. The estimate \(|z^{jk}-\omega^{jk}|\le jk|z-\omega|\) gives precisely \(d(d-1)k\epsilon/2\) in (K6). Equation (K7) then pays the entire finite prime-power list, with the stated normalization and no missing factor of \(\pi\). Its \(O(\Delta^{-2})\) error is small enough both for the two-copy limit and the three-copy first-order asymptotic.

3. **Payment limits and the boundary.** For two copies the surviving even powers are the positively weighted sum \(\sum\Lambda(n)n^{-1}(1-\log n/T)\), \(T=\pi\Delta\), whose main term is \(T/2\). Thus \(C(h)\to1\). The convergence *from below* applies to \(I\Delta\to2\), as the note states; no direction for \(C(h)\to1\) or monotonicity in \(\Delta\) is needed. For three copies, the surviving series converges absolutely to \(-\zeta'(3/2)/\zeta(3/2)\), yielding \(C(h)\sim A_3 I/\pi\to0\). The exact-zero-payment theorem is respected: no constructed payment is asserted to equal zero. The first family excludes uniformity of Note 08 (K15) as the fixed gap below two closes; the second excludes an unrestricted version of that prime-payment lower bound.

4. **Full gamma and pole accounting.** For every target height in \([4dR,8dR]\), the translated centers remain within a fixed small fraction of the height. The local absolute digamma error is \(O_d(1)\); the quadratic tail, including the region where its imaginary argument is small, contributes the stated \(O_d(L/(\Delta^2\sqrt\gamma))\) scale before normalization. Hence the absolute gamma budget (K12) follows. Every pole argument has horizontal distance at least \(\gamma\), so (K13) follows from the elementary sine bound. The chosen \(R\ge e^{\Delta^2}\) makes its relative cost vanish. A target zero exists in the displayed interval at sufficiently large return times by the usual zero count; no multiple zero is selected or inferred.

5. **Explicit scalar square.** Convolution of the two interval Fourier transforms has intersection midpoint \(v/2\) and length \(\Delta-|v|\), giving exactly the phase and sine numerator in (K16), including its denominator \(\pi(i-j)R\Delta^2\). The cross-payment estimate follows even from \(\Lambda(n)\le\log n\), giving \(O_d(e^{\pi\Delta}/(R\Delta))\). The normalization \(g(0)^2=1+O_d((\Delta R)^{-1})\) and mass \(d/\Delta+O_d((R\Delta^2)^{-1})\) preserve both payment asymptotics. On the real line \(g\) is real, so the entire continuation \(g(z)^2\) realizes the required nonnegative scalar square there. Cauchy–Schwarz pays its real-axis gamma integral and its complex pole values. Only the translated-sum family asserts approach to \(I\Delta=2\) from below, correctly.

6. **Remaining cost.** The recurrence proof supplies existence and arbitrarily large lower bounds for \(R\), but no upper bound sufficient to improve the height-dependent envelope. The value \(U\sim dL/(2\pi\Delta)+C(h)\) therefore cannot be optimized in \(\gamma\) by treating \(R\) as freely small. If \(R\ge\exp(\exp(\Delta^2))\), the explicitly paid sequence is indeed uncompetitive: \(U/(L/\log L)\to\infty\). The final disposition preserves this distinction. No claim against every bandlimited full-envelope method, and no exclusion of an original theta zero, follows.

## 3. Stable geometric-width extraction

- **All-zero leakage:** On the near shell the certified gap gives `(d/|v|)^(2r)<=1`. On each far shell, `d<=1/2` and `r>=1` give `(d/|v|)^(2r)<=d^2/k^2`. The disjoint shell definitions and `n_k<<log(gamma+k+3)` therefore pay every noncentral ordinate, including negative ordinates and multiplicity, in equation (E8). The remaining `log(k+1)/k^2` series converges. No exterior contribution is omitted.

- **Center uncertainty:** Every rational factor in `K_r` is positive on the real line. Its logarithmic derivative has absolute value at most the sum of `1/a_j`, strictly below `2/a_*`. The resulting two-sided multiplicative bound survives the absolutely convergent sum over zeros and proves equation (E9). The stated `e<<tau a_*/log gamma` sufficiency follows from the multiplicity count and equation (E8). The exact-center interval (E15) is correctly kept separate from this additional error.

- **Uniform reciprocal envelope:** With fixed typicality parameter, BdR Propositions1 and18 apply to the chosen `V`. The first regime is maximal at the smallest width; the `log^+` expression with a sufficiently large fixed constant also dominates the larger-shift regime. Equation (E11) is uniform in all widths, including when their number grows. No fixed-width estimate is being silently extended to zero at a fixed height.

- **Finite analytic approximation:** The discs have real part between `1/2+a/2` and `1/2+3a/2<=7/8`, and `N>=2gamma` keeps all heights uniformly away from Simonic's `|t|=2pi N` endpoint. His remainder and the fixed-cutoff Cauchy derivative estimate are therefore uniform in `a,r,N`. The logarithm is analytic on the discs under RH. The independent upper bound `Re log zeta<=L/2+O(1)` and the center lower bound prove the displayed `a|zeta'/zeta|` estimate. Exact division pays the reciprocal denominator before taking real parts. Enlarging the fixed constant in (E14) enforces both nonvanishing of `A_N` and error at most `tau/2` per input; amplification below two then gives combined error at most `tau`.

- **Integer enclosure:** If the nonnegative leakage is at most `tau` and the arithmetic error is at most `tau`, then `m` lies in `[Mhat-2tau,Mhat+tau]`. Its length is `3tau<=3/8<1`. This certifies whichever integer is present; it does not force that integer to be one.

- **Cutoff asymptotics:** Taking `r=sqrt(ell/log2)+O_tau(1)` gives `log(V/(a_*L))=ell+sqrt(ell log2)-log ell+O(1)`. Substitution yields `2R_*=L[1+sqrt(log2/ell)+O(log ell/ell)]`. The logarithm of the polynomial prefactor in (E14) is only `O(log L)`, and the `2gamma` alternative is eventually smaller. Thus (E17) follows. Under the separately stated single-width payment, `a` has order `L^(-3/2)`, giving `2R_*=(3/2+o(1))L` and the sufficient cutoff (E18). The draft correctly presents these as two specified sufficient schemes, not optimal complexity bounds or superiority over direct first-jet certification.

The separately certified gap, count constants, optional center error and numerical roundoff remain visibly unpaid until supplied. No simplicity hypothesis is used, and no claimed all-height simplicity conclusion follows from the extraction theorem.

The coordinating agent separately checked the rational residues, coefficient
norm and complete count tail, and reopened the finite q-binomial identity.
A second same-model check also verified these identities and the stated
sufficient-cutoff comparison. These checks are not different-model or
specialist validation.

## 4. Event-conditioned finite-sum assessment and verification scope

No opposing signed estimate was obtained from imposing ζ(ρ)=ζ′(ρ)=0 on Note 08's controlled finite sum. Subtracting its exact value and first jet at ρ merely enforces the stipulated vanishing; it does not bound the surviving second or higher coefficient, nor force the logarithmic-derivative consumer below two. This is an assessed branch with no new criterion or claimed quantitative gain. The exact fixed-cutoff remainder and division payment must remain in any future event-conditioned estimate.

No numerical sign scan, new zero certificate, manuscript or snapshot was
produced. The earlier finite exact-algebra replay was unchanged and does
not verify these infinite estimates. The analytical gain is the specified
control construction, the discrete counterexample to an unrestricted
prime-payment bound, and the stable extraction cost under a paid gap.
None demonstrates that the computed multiplicity must be one.
