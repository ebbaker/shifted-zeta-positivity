# Continue after the positive field-mixing calculation

12 September 2026. This is the current continuation for the active attempt in `papers/susy-positivity/attempts/topological-susy-bulk`. The user promoted the project from `brainstorm` to `attempts`; the older background and candidate package remain under `brainstorm`. Read [the new calculation](FIELD_MIXING_20260912.md) and then [the preceding loop-evolution continuation](CONTINUATION_20260912.md) for its full context.

**Status:** an explicit positive mixing field has been eliminated exactly. It removes the leading cusp of the original continuous error, but leaves a nonzero third-derivative jump. Two other closely related architectures have exact obstructions. No full Weil completion, new positivity interval, or proof of RH is claimed. The arguments are AI-assisted and not independently specialist-reviewed or formally verified.

## Current reading map

* [Field-mixing calculation](FIELD_MIXING_20260912.md): general mechanism, fixed model, proofs, closed relative complex, exact response, controls, limitations, and next conditions.
* [Previous continuation](CONTINUATION_20260912.md): exact loop evolution, contact/prime matching, original remainder, rational-transfer and infinite-rank arguments.
* [Shared background](../../background_section.tex) and [program overview](../../PROGRAM_OVERVIEW.md): authoritative conventions and program scope.
* [Topological background](../../brainstorm/TOPOLOGICAL_BULK_BOUNDARY_POSITIVITY_20260912.md): positive descent, saturation, gluing, and all-input coverage.
* [Superspace companion](../../brainstorm/SUPERSPACE_COHOMOLOGICAL_BOUNDARY_PAIRINGS_20260912.md): physical norm versus auxiliary energy, actual adjoint, protected pairings, and the exact-state problem.
* [Relative complex](../../brainstorm/candidate-bulk-theories/01_RELATIVE_COMPLEX.md), [delay channels](../../brainstorm/candidate-bulk-theories/02_DELAY_CHANNELS.md), and [earlier candidate continuation](../../brainstorm/candidate-bulk-theories/CONTINUATION.md): source constructions. The newer exact finite-coupling remainder supersedes the old tangent-residual target.
* [New checker](calculations/check_field_mixing.py), [diagnostics](results/field-mixing-diagnostics.json), and [pass record](results/field-mixing-pass-record.json).

The user prefers each map introduced acting on a test input before passing to operator notation. Explain the general construction before its examples. Keep an actual positive Hilbert pairing distinct from a proposed superspace interpretation, and distinguish arithmetic data assigned to a model from data selected by a symmetry.

## Fixed starting point

Use \(\log2<L\le\log3\), \(\mathcal P=\{2\}\), full primitive histories, \(c=w_0\), and unit evolution time. On the whole line let

\[
m(\tau)=\exp\!\left[c-\frac{2(\log2)2^{-1/2}e^{-i\tau\log2}}
 {1-2^{-1/2}e^{-i\tau\log2}}\right],\quad
v=\log|m|,\quad q=e^{-2v}.
\]

The baseline multiplier is \(Z(\tau)=B(\tau^2/q)\), where
\(B(s)=\sum_{k\ge0}(2/a_k)s/(a_k^2+s)\), \(a_k=2k+1/2\).
Its exact error is \(\rho=B(\tau^2/q)-B(\tau^2)-v\), and

\[
Q_{0,L}=Z+2C^*C-2S^*S-\mathscr R.
\]

The negative contact and both pole signs are included in this identity. They are not independently positive corrections. The symbol \(q\) is a scalar compliance and should not be confused with the odd symmetry \(\mathsf q\).

## Results to retain

**Pure relaxation of the old energy fails.** On packets \(f_N=e^{iNx}\phi\) supported in a subinterval shorter than \(\log2\),

\[
(Q-Z)[f_N]=\frac{\beta_0}{24N^2}\|\phi\|^2+O(N^{-3}),
\qquad \beta_0=\mathbb E(q-1)>0.
\]

The expansion is uniform on fixed finite-dimensional spaces of profiles. Thus no form bounded above by \(Z\) plus a finite-rank source contribution can equal \(Q\). This excludes adding response fields to the unchanged old energy whenever setting them to zero recovers the old problem, even if the new fields are infinite-dimensional. It does not exclude changing old coefficients or source maps. See the full proof and a working relaxation control in §3.

**A changed positive stiffness can remove the leading error.** For one mass use

\[
\mathcal E_{a,\delta}[F;u,w]=\frac2a\left(
\|F-u\|^2+\frac{\|M(u'-w)\|^2}{a^2(1-\delta)}
+\frac{\|w\|^2}{a^2\delta}\right),
\quad 0<\delta<1.
\]

This family is positive before matching; its parameter is not derived from a Ward identity. Its relative differential, adjoint, domains and nonzero harmonic classes are specified in §§4–5. Eliminating the fields gives

\[
X=(1-\delta)q+\delta,\qquad
T_a(\tau,X)=\frac2a\frac{\tau^2}{\tau^2+a^2X}.
\]

Replace the old mass channel \(T_a(\tau,q)\) in the tower. For \(a=1/2\), the choice \(\delta=1/24\) cancels the complete inverse-square error. The remaining symbol is

\[
\widetilde\rho(\tau)=
-\frac{(q-1)(319q+89)}{11520\tau^4}+O(\tau^{-6}).
\]

Its kernel is \(C^2\) and has third-derivative jump
\(\mathbb E[-(q-1)(319q+89)/11520]<0\). Hence it still has infinite rank on every nonempty interval, and no net finite-rank correction, including just pole amplitudes, completes the model. The positivity of the component energy has survived; the full arithmetic identity has failed.

**More positive convex splits do not remove the next error.** Finitely many compliances \(X_k=(1-\delta_k)q+\delta_k\), with \(0\le\delta_k\le1\), may cancel the first cusp if \(\sum2a_k\delta_k=1/24\). Their inverse-fourth coefficient still has strictly negative mean for one-prime \(c\le0\). See §7. This is a theorem about this specified family, not about all coupled mass matrices.

**A simple derivative cost for the splitting field also fails.** Adding \(\mu\|w'\|^2\), \(\mu>0\), inside the parentheses above gives

\[
X_\mu=(1-\delta)q+\frac{\delta}{1+a^2\mu\delta\tau^2}.
\]

The leading residual coefficient is \((2a\delta-1/24)q+1/24\). Since the first Fourier coefficient of \(q\) is nonzero, cancellation at the active shift \(\log2\) forces \(2a\delta=1/24\), leaving a diagonal derivative jump \(-1/24\). Thus this extension does not even retain the first-cusp match. The limits of small derivative cost and high frequency do not commute. See §9 before trying this modification again.

## Next substantive investigation

Pursue one **joint two-mass/history system or a field-valued source modification**, with its bare positive energy specified first. Do not choose its maps through the unknown target's spectral factor or an asserted contraction. The result should be an explicit complete response, or an exact obstruction to the stated architecture.

For a finite diagonal replacement by phase-dependent compliances, the first two whole-line tail conditions are

\[
\sum_k2a_k(q-X_k)=\frac{q-1}{24},\qquad
\sum_k2a_k^3(X_k^2-q^2)=\frac7{960}(q^2-1).
\]

In the fixed model \(q>1\). Some channels must therefore soften even though the first equation requires a weighted net stiffening. This explains why the all-stiffening splits fail. An independently defined cross coupling might permit this redistribution. A scalar source fit or merely solving these equations is not yet such a construction.

1. Define the positive space, trace/source, fields, coefficients and actual adjoints; state whether whole-line history or finite-interval history is used.
2. Eliminate the fields exactly on arbitrary complex inputs, with the full tower and exterior energy retained.
3. Test contact/delta coefficients and both inverse-square and inverse-fourth coefficients. On a finite interval, check every active shifted singularity as well as the diagonal. A phase-wise match is a stronger preliminary filter.
4. Compute the remaining continuous kernel and both pole amplitudes. A finite-order asymptotic match does not establish equality.
5. Prove an actual symmetry or gluing statement if claiming protection. Quotient representative independence alone does not fix the pairing under coefficient changes.
6. Advance to two primes or gluing only after a first-prime architecture survives these tests. Dense mixed delay sets are outside the isolated-cusp proof used here.

The old low-frequency negative-defect witness remains numerical. Certifying it would settle the separately scoped no-independent-positive-addition statement, but neither the present pure-relaxation restriction nor the field-mixing obstruction depends on it. No certificate was created in this pass. The alternative even-sector scalar problem remains a different possible restricted task.

## Reproduction and verification status

From this attempt directory, with Python and NumPy:

```bash
python3 calculations/check_field_mixing.py --output /tmp/field-mixing-diagnostics.json
python3 calculations/check_loop_evolution.py --output /tmp/loop-evolution-replay.json
```

The first program checks exact rational coefficients, complex matrix elimination, harmonicity, the derivative-cost variant, high-frequency packets, and two quadrature resolutions of the old bump. The second replays the prior loop model. All checks passed in the recorded environment. Floating-point tolerances and observed refinement differences are diagnostics, not interval error bounds.

No large data, numerical spectral square roots or zeta-zero data are needed. All arrays are transient. Follow [the repository large-file policy](../../../../LARGE_FILES.md) if a later pass produces large data. The source hashes and claims ledger for this pass are in [the pass record](results/field-mixing-pass-record.json). A hash certifies file identity, not a mathematical sign.
