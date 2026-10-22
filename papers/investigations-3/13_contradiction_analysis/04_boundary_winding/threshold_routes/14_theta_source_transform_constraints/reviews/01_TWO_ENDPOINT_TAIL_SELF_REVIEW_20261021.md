# Self-review of the two-endpoint tail constraint

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. This is a review by the authoring assistant;
it is not independent review or specialist validation.

**Assessment:** [Note 01][note] has a coherent analytic proof of a sharp
coefficient-mass bound and a complete bounded complex-domain jet allowance.
The 192-bit checker passed. The result does not satisfy the program's
arithmetic-discrimination or direct-advantage gate. The progress register
must retain those limitations despite the large reduction relative to the
weaker one-endpoint class.

## Checks of the mathematics

- **Source normalization.** Repeated covariant differentiation contains
  both the second-jet and zero-mode corrections. The subtraction in (1)
  cancels the zero mode; the resulting source polynomial is
  \(2\lambda^2e^{9u}-3\lambda e^{5u}\), with no missing factor of two.
  The independent exact polynomial check gives
  \(-\phi_n'(0)=e^{-\lambda}(8\lambda^3-30\lambda^2+15\lambda)\).
- **Endpoint sign.** The primitive contributes \(\beta_n/8\), not zero.
  The first source mode has negative gamma and the later modes have
  positive gamma. Therefore the tail moment is \(B=-\gamma_1>0\).
  Both full endpoints, rather than a truncated sum, define R and B.
- **Sharp mass bound.** Strict monotonicity of r on \(\lambda\ge12\)
  makes Delta the minimum positive gap. The two-mode tail with
  weights \(R-M,M\) attains the high-mode mass bound and is nonnegative.
  Sharpness is for coefficient mass, not the later rectangular jet bound.
- **Exact hull and missing point at infinity.** The converse probability
  construction works because \(M<R\). It proves the closed convex hull
  description. Since \(Q_n\to0\), the closure contains zero; a finite
  tail need not attain it. No extra positive mass at an invented mode
  infinity is inserted into a source.
- **Complex observation.** Absolute values use \(|t|\le T\),
  \(|\Im z|\le Y\), and \(|z|\le Z\). The sine bound includes both
  \(|z|u\) and \(e^{Yu}\). The differentiated expression (16) retains
  the extra \(4t\) term; together with \(6t\), it gives the \(10T\)
  coefficient in (18). The denominator is \(d_nD_n^{k+1}\), not
  \(D_n^{k+2}\).
- **Convergence and scope of sources.** The weighted sums and compact
  mode bounds give normal convergence of the physical fields. Weighted
  relaxations are not assumed to retain full automorphy or every smooth
  endpoint. The actual canonical theta source supplies those identities.
- **Endpoint uncertainty.** The excess changes by
  \(\delta_\gamma-r_2\delta_\beta\). The separate
  \(\delta_\beta V_2\) term is included in (20). Exact endpoint values
  are used in the numerical example, not experimental tolerances.
- **Direct comparison.** Both consumers use the same approximant A and
  the same mode-width envelopes. Equation (21) is strictly positive,
  so common acquisition errors cannot reverse the allowance ordering.
  There is no asserted lower bound on an actual signed error.

## Computational verification and its limits

The [portable checker][script] was executed with Python 3.10.0,
python-flint 0.9.0, and 192-bit precision. Its [receipt][record] binds the
script hash and records outward balls, the domain, all arithmetic tail
payments, the mass extremizer and a second admissible noncanonical source.
The endpoint-subtraction constants overlap separate positive sums through
mode 5, with every omitted mode starting at 6 paid by a geometric majorant.
This is a check of the written proof's algebra and constants, not a
numerical proof of its universal quantifiers.

No oscillatory head integrals were acquired. There is no root search,
boundary charge computation, observed physical error, timing comparison,
or new collision-control event box. The approximate and certified numbers
in the note are not interchangeable; the receipt supplies the certified
enclosures.

## Controls and disposition

The strongest screen is the inherited finite-prime theorem: its tests can
include the fixed first coefficient and both present endpoints, while a
positive-time double occurs at an unbounded sequence of heights. Such a
control **passes this relaxation**, and is not falsely said to fail the
estimate just because it lacks full theta reflection. The present formula
uses only two consequences of reflection. The other controls have their
separate source-representation and endpoint assumptions listed in the note.

The finding supports a quantitative robustness tool, with same-assistant
review only. It does not justify TST-03 completion as an arithmetic
discriminator or a TST-05 transfer claiming physical exclusion. Stop the
specific direct-advantage comparison; preserve the full program as open.
No repository-wide result-summary promotion is requested at this stage.

[note]: ../notes/01_TWO_ENDPOINT_TAIL_CONSTRAINT_20261021.md
[script]: ../numerics/check_two_endpoint_tail.py
[record]: ../numerics/TWO_ENDPOINT_TAIL_CHECK_192_20261021.json
