# Review of reciprocal precision and kernel costs

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded metadata. Separate same-model internal checks of
[Note 08](../notes/08_RECIPROCAL_PRECISION_AND_BANDLIMITED_ARITHMETIC_COSTS_20261020.md); no specialist review or priority claim.

**Disposition:** the finite-sum precision estimate, improved reciprocal-energy
envelope, and scoped arbitrary-Fourier-sign kernel bound pass internal
review. No complete signed estimate or simplicity theorem follows. The
[progress register](../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md)
keeps the strict-surplus and all-zero gates open.

## 1. Reciprocal precision and energy

1. **Uniform source ranges.** For fixed typicality parameter `theta`, the chosen `V=(1/2+log ell/ell)L/ell` exactly meets BdR Proposition18's lower threshold and, at sufficiently large height, both upper and lower admissibility requirements of Proposition1. Taking its `T=t` is allowed. The constants and height threshold can depend on `theta`, but not on the horizontal distance `h`. Both regimes in equation (R2) are retained. At `h=c/log t`, this gives the stated `t^(1/2+o(1))`, uniformly for `c` in a fixed positive compact interval.

2. **Finite cutoff and derivative.** Simonic's explicit remainder has a bounded multiplier when `|t|/N` tends to zero: its term involving `1-y cot y` is `O(|t|/N)`. On the fixed-cutoff disc all real parts remain in `(0,1]`, and all heights satisfy the theorem. Hence the `N^(-1/2)` remainder and its Cauchy derivative bound are valid. The analytic logarithm is available on the disc under RH; the stated positive-real-part derivative estimate gives the needed `O(log^2 gamma)` bound. Exact division then proves equation (R7), with logarithmic factors absorbed in `gamma^(o(1))`. No differentiation of the varying cutoff occurs.

3. **Energy saddle and tails.** Equation (R10) follows with a constant independent of `a=log(1/h)`. In `ell in [a-sqrt(a),2a]`, expanding its product gives at most `a+(3+2theta)log a+O_theta(1)`. Writing `u=A-ell` then gives `F_a<=2e^A u e^(-u)/a` where positive, yielding `O_theta(h^(-1)a^(2+2theta))`. The two lower ranges have exponentially smaller maxima. For all `ell>=2a`, the small-shift regime gives `F_a<=-L/4` uniformly once `a` is large. In the other source regime, `C_theta V/L` tends to zero and the same tail bound holds. That regime is impossible below `ell=2a` because `V/L>=1/(4a)>h`. Thus the bound controls the entire unbounded integral, not just its central saddle. The finite integration-length logarithm is `O(a)` and is negligible.

4. **Compact heights and multiplicity.** On a fixed compact height range, finitely many boundary poles have some finite maximal order `m0`, with no simplicity requirement. The crude `O(h^(-2m0))` integral bound suffices and is absorbed by the claimed exponential envelope. Negative heights are identical by conjugation. Choosing `theta=min(epsilon/2,1/2)` gives the stated exponent `2+epsilon`. The exact cubic lower energy cost of a double zero remains compatible with this upper bound.

5. **Finite inverse checks.** Equation (R13)'s endpoint term is correct. Its two Laplace pieces have disjoint time supports, so Plancherel separates their energies exactly. Each finite Euler factor is nonzero at a nontrivial zero, preserves its order, and its rough-integer Dirichlet positivity is only being asserted in its convergence half-plane.


The prior finite-sum conditioning discussion is in review 07 and the
progress register, not in Note 07's Jensen derivation. The current note
describes the comparison of cutoff sizes directly. The coordinating agent
also checked the primary theorem ranges and the complete energy saddle.

## 2. Arbitrary Fourier signs and the paid kernel class

**Result: passes.** I independently checked the discrete prime weights,
Poisson admissibility, positive-weight PNT argument, complete archimedean
budgets, and sequence-versus-infimum distinction. No substantive correction
is required.

1. The declared stripwise quadratic decay makes the periodization
   continuous by uniform convergence; its Fourier coefficients are
   `a phi(ka)` and only finitely many are nonzero. Therefore (K6) is valid
   pointwise without a Schwartz assumption. Since `h` is real on the real
   line, opposite Fourier samples are conjugate even when `h` is not even.
   Continuity and compact support give zero endpoint samples, and
   `a=Delta` proves `I Delta>=1` exactly.

2. The power weights in the von Mangoldt payment are correct:
   `Lambda(p^k)=log p` for every positive k, so
   `C_p=2a_p sum p^(-k/2)|phi(k a_p)|`. Poisson gives a lower bound
   `sum |phi(k a_p)|>=(1/a_p-I)_+/2`; multiplying by the smallest
   retained power weight yields (K9), with no lost factor two.
   Distinct primes have disjoint positive-power indices.

3. On `exp(pi Delta)<p<exp(2pi/I)`, only the first harmonic survives;
   the upper inequality and `I Delta>=1` ensure that this harmonic lies
   within support. Hence
   `Re phi(log p/(2pi))>=pi/log p-I/2`, and its absolute payment is
   exactly bounded below by `p^(-1/2)(1-I log p/(2pi))`.
   No Fourier positivity premise is needed outside this forced shell.

4. With `B=2pi/I`, the PNT sum has constant
   `4 exp(B/2)/B^2 = I^2 exp(pi/I)/pi^2`. The partial-summation proof uses
   a decreasing positive weight and avoids subtracting uncontrolled
   main terms. The lower omitted shell costs at most `2 exp(eta B/4)`;
   divided by the main scale this is `O(B^2 exp(-(2-eta)B/4))`, uniformly
   for fixed `eta<2`. This is the exact point where the fixed gap below
   two is used. Nothing here establishes the same estimate when that
   gap closes without further control.

5. I reopened [Goldston–Gonek, Lemma 1](https://arxiv.org/pdf/math/0511092).
   The shifted Fourier phase, the coefficient `1/pi` after combining
   opposite prime frequencies, the digamma/log-pi integral, and both
   shifted pole terms in (K2) match the primary formula. For the modulus
   envelope the pole payment is nonnegative. For the exact envelope its
   negative part is explicitly paid by (K5). Condition (K4) gives the
   lower gamma main term with precisely the factor `1/(2pi)`.

6. Along a competitive sequence, these complete budgets force
   `I=O(1/log L)`, allowing the uniform small-I shell asymptotic. A putative
   leading coefficient below one half then forces
   `I<=pi(1-2delta+o(1))/log L`, and monotonicity of
   `I^2 exp(pi/I)` for small I gives a superlinear prime cost, contradicting
   competitiveness. Thus (K16) is valid. The additional uniformity
   requirement before taking an infimum in (K17) is necessary and is
   correctly stated.

7. Fejer sharpness is admissible. The added direct verification (K17a)
   correctly bounds the integral of the absolute digamma error by
   `O(1/(Delta sqrt(gamma))+log(gamma)/(Delta^2 sqrt(gamma)))`,
   uniformly for `Delta>=1`; this proves (K4) without relying on
   cancellation in the gamma integral. At `Delta=log L/pi`, (K17b)
   makes the modulus pole payment negligible relative to `LI`; hence
   the exact-pole budget follows as well. Its prime cost is of lower
   order than `L/log L`, giving the claimed sharp leading coefficient
   within every stated class containing these choices.

8. The zero-payment conclusion follows from the powers of the prime two
   alone and is sharp at bandwidth `log 2/(2pi)`. The note correctly
   leaves approximate notches at unrestricted bandwidth, the class
   `I Delta>=2`, missing archimedean budgets, and genuinely signed prime
   estimates outside the theorem. It is an absolute-envelope result,
   not an all-kernel or all-zero simplicity obstruction.

## 3. Canonical-system assessment

No independent theta Hamiltonian or terminal nondegeneracy estimate was
obtained. The following checked assessment is retained here without
promoting it to a separate research criterion.

### Primary-source match and the common real factor

Write `F(z)=xi(1/2+iz)=xi(1/2-iz)`. Under RH its paired product gives `Im(F'/F)<0` in the upper half-plane. Thus `E=F+iF'` satisfies

\[
|E|^2-|E^\#|^2=-4|F|^2\Im(F'/F)>0.
\]

But at an exact order-m real zero `r`, with `c_m=F^(m)(r)/m!`,

\[
E(z)=(z-r)^{m-1}\{i m c_m+O(z-r)\}.
\]

The strict half-plane inequality therefore does not exclude common real zeros. With `E=A-iB`, the diagonal is

\[
K_E(x,x)=(F'(x)^2-F(x)F''(x))/\pi.
\]

Its positivity at every zero of `F` is the missing first-jet assertion itself. Dividing by the convergent real product `G(z)=prod_(gamma>0)(1-z^2/gamma^2)^(m_gamma-1)` removes common real zeros, but replaces the real part by `F/G`. The inner quotient `E^#/E` is unchanged: an inverse construction applied after this division cannot recover the removed multiplicities. Likewise `-F'/F` is Herglotz, but an order-m zero supplies positive spectral mass `m`, not an impermissible higher-order pole.

[Suzuki, *Hamiltonians arising from L-functions in the Selberg class*, §1, equations(1.1)–(1.4), pp.1–2](https://arxiv.org/pdf/1606.05726) introduces exactly `E_xi=(xi+xi')(1/2-iz)=F+iF'`, distinguishes the half-plane inequality from the additional absence of real zeros, and retains RH plus the simplicity conjecture in the direct inverse construction. His shifted construction on pp.3–4 explicitly allows multiple critical-line zeros. This source supplies no missing no-common-zero implication under RH alone. It confirms that the candidate is already known and must not be recorded as a new criterion.

### Quantitative checks on the two shortcuts

For `h>0`, the shifted `E_h(z)=F(z+ih)=xi(1/2+h-iz)` has no real zeros and satisfies strict HB under RH. Its product gives

\[
K_{E_h}(x,x)=\frac{|F(x+ih)|^2}{\pi}
 \sum_\lambda\frac{m_\lambda h}{(x-\lambda)^2+h^2}.
\]

At a fixed order-m zero `r`, the other-zero sum is `O(h)` and real Taylor coefficients give `|F(r+ih)|^2=c_m^2 h^(2m)(1+O(h^2))`. Hence

\[
K_{E_h}(r,r)=\frac{m c_m^2}{\pi}h^{2m-1}(1+O(h^2)).          \tag{C1}
\]

A double zero gives `F''(r)^2 h^3/(2pi)+O(h^5)`, despite strict positivity for every `h>0`. Thus positivity at fixed shifts supplies no positive endpoint lower bound. This is a spectral shift, not physical theta heat time or Jensen degree. It is consistent with Note07's already quantified loss of finite strictness. Note05's real-zero source controls satisfy the same product argument, but do not preserve exact zeta arithmetic.

The other shortcut would identify `(F,-F')` with a regular finite-interval canonical-system solution `JY'=zHY`, where `M=int_0^L||H||<infinity` and `Y(0,z)=v_0!=0` is constant. The transfer matrix and inverse give

\[
\|Y(L,z)\|\le\|v_0\|e^{|z|M},\qquad
\|Y(L,x)\|\ge\|v_0\|e^{-|x|M}\quad(x\in\mathbb R).          \tag{C2}
\]

The second bound indeed prevents common endpoint zeros, even for semidefinite `H`. But the first bound prevents the proposed identification: Stirling and `zeta(sigma)->1` imply

\[
\log F(iY)=\tfrac12Y\log Y+O(Y),
\]

which has infinite exponential type. The same holds after any fixed invertible constant change of the endpoint pair. If such finite systems with fixed initial vector approximate this pair locally uniformly, their masses `M` must diverge, so (C2)'s lower bound degenerates. This excludes only the **finite-integrable, constant-initial-data, unmodified-endpoint** implementation. Singular/infinite systems or other normalizations remain outside that statement. [Remling, §6 and Theorem7.3](https://math.ou.edu/~cremling/research/preprints/dB.pdf) distinguishes regular finite systems from the general framework that can have singular endpoints.


The primary-source comparison supplies no missing no-common-zero
implication from RH. It closes only the stated shortcuts for this round;
singular or infinite systems with independently justified normalization
remain outside the finite-endpoint comparison.

## 4. Verification scope and remaining gap

All estimates keep their quantifiers: the finite-sum shift is
`c/log gamma`, with `c` in a fixed positive compact set; the energy bound
allows every fixed finite multiplicity at compact heights; the kernel
optimization assumes `I Delta<=eta<2` for fixed `eta` and the complete
archimedean budgets. Neither the coefficient `1/2` nor the energy exponent
`2+epsilon` is asserted to be a best-known bound for every RH method.

No numerical sign scan, new zero certificate, or manuscript was produced.
The prior exact-algebra replay is unchanged and does not test these
infinite estimates. Approximation precision is now adequate at the
specified scale, but the finite expression still lacks the sign needed
for multiplicity exclusion. The improved energy bound is still
superpolynomial and permits the exact cubic cost of a double zero.
