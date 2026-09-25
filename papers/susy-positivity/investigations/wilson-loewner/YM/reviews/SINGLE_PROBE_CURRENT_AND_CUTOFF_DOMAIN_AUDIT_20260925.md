# Audit of the detecting probe, full-current spectrum, and cutoff domains

25 September 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance.

Model exposed: GPT-6 (Codex). Exact deployed variant and reasoning effort: unavailable; not inferred. Baseline commit: `f8b8622fbd687bd152dd40dcc0c4bbd4576008e5`.

This is a substantive self-audit of the [new analysis](../notes/SINGLE_PROBE_OCCURRENCE_AND_PRIME_BOUNDARY_RESPONSE_20260925.md), not independent human or separate-model validation. The previous signed mixed identity is retained. The new exclusion of the **full** electric-current source action and the quantitative prime-cutoff response narrow its physical interpretation. No RH proof or independently established arithmetic occurrence theorem is claimed.

## 1. Findings and status

| Claim | Audit result and assumptions |
|---|---|
| A fixed compact smooth pole-neutral test detects every nontrivial zero | Proved by an infinite convolution and an exponential tilt. No arithmetic zeros are used to choose it. |
| Its translated Weil response is bounded or tempered exactly when RH holds | Proved using the unconditioned explicit formula and nonzero residues of a one-sided Laplace transform. This is a new criterion within this investigation, not a claim of novelty in the literature. |
| This response cannot tend to zero at large separation | Proved unconditionally: decay would imply RH, whose absolutely convergent positive atomic expansion then contradicts decay. RH is a consequence inside a contradiction argument. |
| The full interacting electric–Wilson current is purely absolutely continuous | Proved by a global flow cross-section on the actual link manifold, including all transverse links and the actual density. No class compression or continuum Hamiltonian is substituted. |
| A sharp prime cutoff leaves norm of order at least square root of A at the moving edges | Proved with explicit profiles by the unconditional PNT. It applies to exactly pole-neutral inputs. It is not merely the old divergent diagonal coefficient of positive squared differences. |
| One actual stationary correlation implies the complete source law | Conditional theorem, with analytic filtering domain and test continuity proved. The actual stationary family with that correlation has **not** been found. |
| OS axioms or a physical mass gap provide the missing correlation or its arithmetic temperedness | Not established. Physical spacetime and logarithmic character scale remain distinct. |

## 2. Probe construction and the complex-frequency trap

The untilted convolution density b has transform

\[
B(z)=\prod_{j\ge1}\frac{\sinh(2^{-j}z)}{2^{-j}z}.
\]

Convergence of the random sum gives compact support; arbitrary-power decay of its characteristic function gives a smooth density. Both are necessary: a finite convolution alone would not give the stated global C-infinity test. Summability of the product tail, together with the imaginary-axis zeros of each factor, proves absence of zeros away from that axis. Finite numerical samples cannot establish this fact.

The tilt \(h_*=e^x b/B(1)\) moves the transform zeros away from the closed strip relevant to zeta. For \(f_*=(-\partial^2+1/4)h_*\), its transform

\[
F(z)=(1/4-z^2)B(1+z)/B(1)
\]

has only the imposed pole-cancellation zeros at the strip boundary. In particular it is nonzero at every \(\lambda=\rho-1/2\), irrespective of RH or multiplicity.

For a real test, the unconditioned zero coefficient is **F(lambda)F(-lambda)**. It is a positive squared modulus only when lambda is purely imaginary. Replacing it by a squared modulus for an off-line zero would make the positivity argument circular and is not done. Repeated zeros contribute a multiplicity times the same nonzero residue; they do not cancel or require simple zeros.

## 3. The boundedness proof does not hide a positivity assumption

For Re z>1/2, absolute convergence justifies the Laplace-transform expansion

\[
\mathcal L C_*(z)=\sum_\rho
\frac{F(\lambda_\rho)F(-\lambda_\rho)}{z-\lambda_\rho}.
\]

The coefficients decay faster than every power in the zero ordinate, uniformly across the strip. Classical polynomial zero counting therefore gives a normally convergent meromorphic function, with a nonzero residue at every centered nontrivial zero.

Subexponential growth implies holomorphy on Re z>0. For the tempered-distribution version, multiply by a smooth cutoff equal to one sufficiently far along the positive half-line; correct near zero by a compactly supported locally integrable function. This avoids multiplying an arbitrary distribution by a discontinuous Heaviside function. Exponential damping then yields the holomorphic Laplace transform on Re z>0, agreeing with the original integral where it converges absolutely. A pole in that half-plane is impossible.

The reverse implication uses RH to obtain positive summable Fourier weights. It is not an assumption in the forward proof. The resulting criterion is exactly equivalent to RH for this deliberately detecting response. It must not be advertised as a consequence of general quantum-field temperedness without proving that this response is a physical distribution in the variable for which that axiom applies.

The unconditional nondecay argument is valid: assuming C0 first forces RH, and under that consequence the response has strictly positive long-time mean square. An actual C0 function has zero mean square. No claim is made that the response is bounded unconditionally.

## 4. Full-state current and fixed-force domain checks

The cross-section \(\Sigma=\{\theta=\pi/2\}\) is regular because the four-link plaquette map is a submersion and \(|\nabla\theta|^2=\ell\) in its open angle range. The flow coordinate
\(r=\log\tan(\theta/2)\) satisfies Yr=-1. Every noncritical full link configuration has a unique crossing of Sigma. The configurations with P=plus or minus I have measure zero, so they do not supply hidden point-spectrum vectors in this L2 representation.

Pulling back the **actual** nu measure produces a positive density on the product of the line and Sigma. The square root of that full density, not just the plaquette marginal, removes the weighted Jacobian. This proves a translation representation of the full current. Gauge covariance acts on the transverse fiber and preserves the line coordinate. Pure absolute continuity and decay of every finite-vector matrix coefficient follow.

The generator in these coordinates is \(i\partial_r\), since the group is \(e^{itA_\nu}\) and translates by r minus t. On the recovered source it is instead intertwined with \(-i\partial_x\), because \(J_{\rm rec}U_t=\mathscr U_{-t}J_{\rm rec}\). The opposite signs are consistent, not a new phase error.

This excludes generalized smooth-test sources **if their arithmetic translation is this current**. It does not exclude all generalized sources in the physical space. A native arithmetic generator remains optional.

The signed-insertion exclusion explicitly assumes the left vector lies in the adjoint domain, so that a finite Hilbert vector K* v represents the response. It does not assume that every distributional pairing has such a representative. It therefore strengthens, rather than silently repeats, the preceding closable positive-completion result.

## 5. Prime-cutoff profiles and order of limits

For f=Th, the positive-edge continuum limit is

\[
e^{s/2}\int_s^1e^{-u/2}f(u)du=h'(s)+h(s)/2,
\]

and the negative-edge limit is

\[
e^{-s/2}\int_{-1}^se^{u/2}f(u)du=-h'(s)+h(s)/2.
\]

Both signs were checked independently by differentiation and by numerical quadrature. The completed signed operator contains **minus** the prime shifts, so its edge profiles have the opposite signs. The sum of their squared norms is \(2\|h'\|^2+\|h\|^2/2\). It is nonzero for every nonzero h.

The PNT is used only on scaled intervals bounded away from zero. The family of Stieltjes integrands has uniformly bounded variation, including the endpoint at the sharp cutoff. This gives uniform convergence in the edge variable. No RH-strength remainder is used. The archimedean response has exponentially small tails there after pole neutrality; its contact stays at the original support.

The physical norm inequality takes R to infinity for **each fixed A**, and then A to infinity. It is a lower bound obtained by testing actual inserted vectors against strongly recovered physical vectors. It does not assert a norm-convergent inserted limit, substitute Haar adjoints, or promote the original compensated-packet prime tails to a proved joint limit.

The last cofinal-cutoff exclusion in the note has two explicit hypotheses: bounded inserted vectors and convergence of all translated responses. If both held, weak compactness would produce a forbidden current matrix coefficient. It does not claim either hypothesis separately holds.

A local counterterm with fixed compact support cannot touch the moving edges, even if its coefficients diverge. A nonlocal moving subtraction or a different regulator is not covered by this particular profile calculation. Such a proposal would still need an independent physical definition, preservation of the target mixed pairing, and a positive completed limit. Neither the older zero-domain theorem for positive prime differences nor the present calculation supplies that renormalization.

## 6. What is and is not verified in the occurrence theorem

The input is a stationary family of actual vectors with the one prescribed correlation. This is a continuum of scalar equalities, not a finite verification and not just the value at t=0. It carries the unresolved arithmetic identification. Calling it a natural axiom without deriving it would not advance the YM bridge.

Once that input is given, no additional target metric is chosen. Boundedness first implies RH. Uniqueness of Fourier transforms identifies the existing vector's spectral measure. The universal probe has no real Fourier zeros, and the unbounded filter domain is tested in that **actual** measure:

\[
\int|\widehat g/\widehat f_*|^2d\mu_v
=\sum_\gamma m_\gamma|\widehat g(\gamma)|^2<\infty.
\]

One must not assume the ratio is polynomially bounded; it need not be. Cancellation against the derived measure is the valid domain proof. Bounded spectral truncations converge in the same positive physical completion, and local smooth-test seminorms give continuity for all global compact supports.

This is a sufficient source-occurrence reduction with its analytic hypotheses verified. The substantive physical hypothesis is still missing. Extra locality, bounded-observable representatives, or compact preparation bounds are not automatic. This also does not conflict with the preceding nonclosability theorem: the resulting source is defined on the smooth-test space, not asserted to be a closable map from ordinary input L2.

## 7. Sources and numerical verification

Primary mathematical inputs checked in this continuation:

- [Connes–Consani, Appendix B](https://arxiv.org/html/2006.13771v1): explicit formula, prime-power coefficients, and completed gamma sign/normalization. The new criterion and current theorems are derived here, not attributed to that paper.
- [Elkies, *The product formula for xi and zeta; vertical distribution of zeros*, pp. 1–3](https://people.math.harvard.edu/~elkies/M229.15/zeta2.pdf): growth and zero counting with multiplicity. Only a polynomial bound is needed here.
- [DLMF §25.10](https://dlmf.nist.gov/25.10): location, symmetries and existence of nontrivial zeros.
- [DLMF §27.12](https://dlmf.nist.gov/27.12): unconditional PNT. Partial summation gives the weighted-prime version; higher prime powers contribute o(x).

The [new checker](../numerics/check_single_probe_and_prime_edges.py) produced [13 passing controls](../numerics/records/single-probe-prime-edges-20260925.json). At cutoffs 1000, 10000, 100000 and 1000000, relative two-edge profile errors were approximately 0.1480, 0.05074, 0.01609 and 0.006306. The final edge-energy ratio to the proved coefficient was 0.999265. These are finite floating comparisons to the analytic asymptotic, not a proof of it.

An initial 160/240-point quadrature comparison differed by about 1.0323e-7 relative to the predicted energy, just beyond the preset 1e-7 threshold. Increasing to 240/360 points reduced that discrepancy to about 8.204e-10; the threshold was not weakened. The saved script and record use the refined settings. No zero list, interacting-state sample, large array, or third-party PDF is saved.

## 8. Corrections to the research direction

No central equation from the preceding character, archimedean, or recentering notes is retracted. The following possibilities are now more sharply delimited:

1. Allowing a direct smooth-test domain does **not** rescue covariance under the full electric–Wilson current. Its complete physical spectrum is now computed and fails the necessary nondecaying correlation test.
2. Exact pole neutrality removes the full averaged exponential prime mode, but **not** the partial average at a moving cutoff. A source-local subtraction cannot fix that effect.
3. Full OS axioms and a mass gap are permitted but cannot be applied to an unidentified arithmetic coordinate. Decay from a justified clustering statement would actually exclude the detecting correlation along that parameter.
4. The useful surviving task is one actual stationary scalar mixed identity with the correct nondecaying response, or a physical interpretation that independently proves temperedness of the existing signed response. Neither task has been completed.

The new theorem narrows the amount of source data that needs to be identified and supplies a rigorous global extension once it is. It does not supply the missing physical observable itself.
