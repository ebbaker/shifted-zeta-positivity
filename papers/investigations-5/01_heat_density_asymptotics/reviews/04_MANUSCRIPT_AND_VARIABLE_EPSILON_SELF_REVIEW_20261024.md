# Same-assistant assessment: manuscript and variable epsilon

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.

**Scope: same-assistant review, not independent mathematical review.**
The [manuscript][manuscript] consolidates existing analytical results.
[Note 14][variable] is the subsequent adaptive-regulator investigation.
This assessment checks definitions, derivations, scope, evidence and
document delivery; it does not establish a reduced boundary solution.

## 1. Manuscript consolidation

The draft has a single maintained LaTeX entry point and six section
files. It preserves the unnormalized physical density and fixed positive
epsilon, states the canonical source and heat normalization, and places
floating numerical observations in Appendix C. The bibliography links
the specific research notes and sibling saddle/Vandermonde inputs.
It does not import a high-height theorem from the abstract-only Polymath
reference.

The principal checks were:

- The negative-time field is differentiated before applying a
  regulator-safe density stability bound. The stated error is absolute,
  uniform for all real height and |y|<=A sqrt(T). The diffusive profile
  and fixed-physical-region orders are kept separate.
- The positive carrier uses the pointwise exp(mu |y|) cancellation;
  its regularization error counts locally contributing disks. The
  growing-window theorem retains finite source/carrier gates.
- The discriminant is the **squared** Vandermonde. Its normalization
  has exponent m(m-1), and the pair matrix is half the Hessian of minus
  its logarithm. The signed mean allowance, rather than the absolute
  first moment, pays the growing population's scale change.
- The all-height hierarchy's filter is explicitly spatial at a fixed
  time. A time average must average the allowance at constituent times;
  it is not evaluated at the central time.
- The source appendix states why there is no interior maximum on the
  far-left interval before the selected large saddle. It records the
  complete weighted allowance, including missing half-line Gaussian
  tails and normalization.
- The fixed-regulator obstruction is stated only for bounded transverse
  support and horizontal windows escaping to infinity. The manuscript
  does not present it as an obstruction to changing epsilon.

No mathematical correction to the earlier fixed-epsilon theorems was
required by this consolidation. Two display overflows and table spacing
were repaired during layout review. The final build has 15 pages, no
reported overfull/underfull boxes, no LaTeX warnings and no unresolved
reference markers. All 20 local note/record links in the exported PDF
resolve in the checkout. The editor compiler also returned success.
All pages were rendered for visual inspection; the build record identifies
the final source and export. This verifies document production, not
independent correctness of the mathematics.

## 2. Variable-regulator identities

With q=epsilon^2, r=log q, D=|H|^2+q and w=q/D, the forcing is

\[
\mathcal B_\epsilon=(q_t+(q_{xx}-q_{yy})/2)/D.
\]

The positive algebraic density remains q|H_z|^2/(pi D^2).
Its difference from Delta log D/(4pi) is C_epsilon from VE7--VE8.
The current equation acquires
(1-2w)(r_t rho+grad r dot j).
The signs in the filtered density equation follow by applying Delta
to the potential equation and using Delta U=4pi(R+F C_epsilon);
both -partial_t F C_epsilon and -square F C_epsilon/2 are retained.
Moving-filter commutators are listed separately.

The new [standard-library script][script] verifies all four cleared
polynomial identities for four positive regulators on H=z^2-2t:
16 exact zero residuals. Nonconstant controls also verify that the
discarded correction numerators are genuinely nonzero. This is stronger
than floating residual sampling for these polynomial controls, but it
is the same assistant's implementation, not an independent proof of
the general formulas or a canonical-theta certificate. The double event
of H is included; the identities imply no simplicity exclusion.

## 3. Weak bias and asymptotic choices

The weak error identity VE15 follows from the logarithmic zero-measure
bridge and the divergence form of C_epsilon. The extra terms have plus
signs after integration by parts. The inequality w<=log(1+q/|H|^2)
controls them by the same logarithmic integral, with the enlarged
test-function constant K_r. No uniform lower bound on epsilon is
silently inserted into that static estimate; spatial log-derivative
bounds and upper regulator values are explicit.

At negative time, epsilon=eta C_T makes T times the Gaussian density
exactly the new stationary profile. Substitution into the old finite
density inequality gives O(T^-1) scaled error, uniformly at all real
scaled heights. It is not the old fixed-epsilon T^2 profile.

At positive time, the new regulator bound uses **explicit upper**
source allowances: these make b_* of order kappa^-1/2 and c_* of
order L, including the needed lower orders. For epsilon/M bounded by
a constant times kappa^-p, the outside log bias is O(kappa^(1-2p));
the disk bias is smaller. Therefore p>=3/4 preserves the earlier
inner-window error. The recommended p=1 choice has O(kappa^-1)
regulator bias. The fully explicit saddle version pays M_0/M by
sqrt(2pi)/Z_-; it does not assume M=M_0 exactly.

The temporal derivative of the saddle exponent is L^2, while
L'=2L/kappa. These give the explicit VE33--VE34 forcing.
A small static bias does not make that forcing negligible.

## 4. Adverse control and open gates

The zero-free Gaussian with a height-matched regulator has
positive rho growing like x^2 but negative curvature density on y=0.
It establishes: “Unlike rho, tilde-rho need not be nonnegative.”
This is a preventive correction to any extension that treats the
fixed-epsilon potential identity as unchanged. The original
fixed-epsilon identity remains valid.

The control screen in the existing notes continues to apply to the
canonical source estimates. Generic regulator identities and weak bias
allow multiplicity; their validity on a collision is expected.
The explicit adaptive regulator is defined at every finite height,
but its positive-time approximation has only the proved growing-window
scope. An all-height positive stationary clock, outer-height error,
differentiated forcing/current budgets, a stable reduced boundary
solve, independent review and a certified finite onset remain open.

**Assessment:** the user's manuscript, variable-epsilon note and
continuation deliverables can be completed at the stated analytical
scope. HDA-07--09 remain gated for the larger evolution program.

[manuscript]: ../manuscript/main.tex
[variable]: ../notes/14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md
[script]: ../numerics/variable_epsilon_identity_checks.py
[record]: ../numerics/VARIABLE_EPSILON_IDENTITIES_20261024.json
