# Review of the buffered conductor refinement

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Review type: separate same-model derivation and script inspection by the
integrating agent. This is not independent specialist refereeing, source
proof replay, or formal verification.

The [new note](../notes/MIXED_CONDUCTOR_REFINEMENT_20261008.md) gives a
valid conditional refinement of the existing two-conductor reduction.
No blocking mathematical issue was found in the stated scope. Its
additional removable sector is not a bound for the complete residual.

## Operational losses and continuous cutoffs

The review checked the source energy note's formulas for \(r_{\rm new}\),
\(m_{\rm new}\), and the buffered wedge, including its lower bound
\(a_r>-(39/14)\ell\). With \(\ell=10^{-6}\), the new
\(s=\eta-d(1-x)a_r+\ell\) is positive and below \(\eta+2\ell\).
Thus \(\gamma_\ell=\gamma-3\ell\) leaves at least \(\ell\) of
low-row reserve, even at the smallest \(d\).

Both discarded-ratio exponents equal \(K_s-\gamma_\ell\). The
affine formula for \(\tau\) was independently substituted. Maximizing
and minimizing it over the closed wedge gives the displayed functions
\(\tau_H\) and \(\tau_L\); the corner values are limiting geometric
values, not assertions of realized arithmetic witnesses. The positivity
of \(\tau-\tau_{\rm old}\) also includes the permitted negative
\(a_r\), rather than silently restricting to the ideal triangle.

The exact rational interval and automatic-differentiation implementations
were inspected. Addition, multiplication, reciprocal, and derivative
rules enclose the full closed cells; reciprocal rejects intervals
containing zero. The 1,024 cells cover the parameter rectangle. The
script was rerun and its output compared byte for byte with
[the saved certificate](../numerics/mixed_conductor_refinement_certificate_20261008.json).
They agree. The inherited rational bounds for the crossing lengths were
checked against the existing energy-localization note. No floating sample
is used to establish a continuous extremum.

## The added plain-ratio sector

The key new estimate uses the minimum of the marked inverse moment and
the full-bin count times the pointwise inverse/physical-prime envelope.
Both bound the same positive selected mass
\(\sum_{\mathcal C_+}|M_rQ_I|^2\). They therefore give exponent
\(1-\mu_C\) without enlarging a signed row sum or modifying a coefficient.

The weighted plain-pair lemma then permits a cutoff increase \(2\mu_C\).
To isolate only the part with large total ratio conductor, the proof
subtracts the small-total-conductor contribution after the whole plain
annulus has been bounded. This subtraction is necessary and valid:
the absolute tuple majorant already allows additional plain-pair
restrictions. There is no total-conductor restriction hidden inside a
positive inverse norm.

The subregion identity (20) was independently derived from
\(1-R^*=d-dF(1-x)/2\) and the formula for \(r_{\rm new}\).
The rational lower bound for \(\mu_C\) exceeds \(1/25000\), so the
extra exponent width \(1/12500\) is valid. The example retains a
positive gap between the required mixed saving and the available
complete-moment count saving; it is not already a full-moment proof.

## Scope that must remain attached

The source family inputs, physical annuli, strict inverse capacities,
whole slots, common orientation, row selector, and zero masks remain
hypotheses. In particular, the pointwise envelopes must cover the
derivative profiles before Sobolev selection. The explicit assumption
that the actual witness and slot losses fit \(s_0+\ell\) has not been
derived for every source setup. The note correctly makes that an
operational condition rather than inferring it from the geometric wedge.

The new sector is a conditional deduction from these inputs. The
remaining large-plain/large-total signed sum still needs a new arithmetic
estimate. None of the finite certificates proves that estimate or makes
the fixed boundary improvement iterable.
