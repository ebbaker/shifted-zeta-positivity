# Continue the physical Wilson--Loewner program from genuine trace growth

21 September 2026. Prepared for Edward Baker.
Model: OpenAI GPT-6 (Codex; developer-provided identity).
Effort: not exposed; not inferred.
Status: internal analytical calculation and floating controls; specialist review
outstanding. No arithmetic positivity result or continuum QFT certificate.

## User's clarified objective

Fix a theory, such as four-dimensional Yang--Mills or N=4 SYM. A specified
Loewner driver generates an actual curve; the curve defines a Wilson observable.
Investigate how that geometric evolution induces an expectation-value evolution.
An explicit expectation value is not required. Derive equations and look for a
useful closed family of observables within the fixed theory.

Do not revert to fitting Gaussian preparations or requiring an arithmetic match
before understanding this physical evolution. A new bulk action is not required
for each observable. Do not confuse a genuine growing trace with a smooth test
curve moved by the inverse Loewner map. A deterministic driver does not require
averaging over contours; the field-theory expectation is already quantum.

The user regards the cumulative arithmetic estimates as a separate workstream
and may request a separate manuscript later. Do not move or rewrite manuscripts
yet. Keep this investigation focused on the physical question; preserve v0.5,
every snapshot, all historical research notes, and existing worktree changes.
Follow repository instructions and LARGE_FILES.md. Record the actual model and
only an exposed effort setting. No sub-agents were used for the present work.

## Read first

1. [Genuine Loewner trace and the YM hierarchy](GENUINE_LOEWNER_TRACE_YM_HIERARCHY_20260921.md).
2. `numerics/check_growing_trace_hierarchy.py` and its small record
   `numerics/records/growing-trace-hierarchy-20260921.json`.
3. `sections/05_variation.tex`, for conventions and the earlier smooth-contour
   identity; its inverse-map examples do not solve growing-tip evolution.
4. The earlier Wilson-lines note
   `../../wilson-lines/notes/DEFORMATION_FLOW_AND_THE_SHIFT_20260917.md`, Section 5,
   for the historical Makeenko--Migdal analogy. Correct its overstatement:
   factorization is needed for the product-of-expectations large-N reduction,
   not for the unfactorized quantum hierarchy itself.

If files are unavailable, ask for them before making claims about their contents.
The local checkout may contain results absent from the remote repository.

## Exact result to retain

In pure Euclidean SU(N) YM, close the actual trace by the straight return chord.
At fixed positive Yang--Mills field-flow time tau, write R_t(r) for outward
radial transport to r q(t), U_t for the actual prefix, and Q_t=R_t(1)^(-1)U_t.
The quantum measure and action are fixed; using the flowed connection changes
the observable, not the bulk action and not the field distribution to a Gaussian.

Set k=q1 q2'-q2 q1', Fhat(r)=R(r)^(-1)F12(rq)R(r), J=int_0^1 r Fhat(r)dr.
The moving-tip connection cancels against the chord endpoint variation:

    Q' = i k J Q
    W' = i k M1
    M1' = q'^mu M_D,mu + 2 i k M2.

Here M1=<tr(JQ)>/N, M_D uses the r^2-weighted, radially transported D_mu F12,
and M2 uses the ordered two-curvature integral
`integral_(0<s<r<1) r s Fhat(s) Fhat(r) ds dr`, followed by Q and normalized
trace. Order matters. These equations retain the full interacting expectation.

For u(t)=a t the upper-half-plane tip solves

    a q + 2 log(1-a q/2) = a^2 t,
    q' = a-2/q,
    q = 2i sqrt(t)+(2a/3)t-(i a^2/18)t^(3/2)+(a^3/135)t^2+...

The last local ODE is specific to a linear driver. The oriented enclosed area
is A(t)=-(2a/9)t^(3/2)+O(t^(5/2)). The constant driver gives an exactly
backtracking loop and W=1, a feature of this completion only.

The short-time expectation satisfies

    W_tau(t) = 1-(2a^2/81) C_tau t^3 + O_(tau,a)(t^(7/2)),
    C_tau = <tr(F12[B_tau](0)^2)>/N.

The note gives an explicit smooth-field error bound, not just a formal series:

    |tr Q/N - 1 + A^2 tr(F0^2)/(2N)|
       <= (K0 K1/6) I I1 + (K0^3/48) I^3,
    I=int |k|, I1=int |k| |q|.

K0 bounds curvature and K1 its unit-direction planar covariant derivatives on
the swept chords. Averaging requires finite <K0 K1> and <K0^3>. The continuum
existence and moment hypotheses were not proved. The limit t->0 is taken at
fixed tau; do not remove tau first or import the result to an unsmeared cusped
loop without a new argument.

## Next bounded calculation

Audit the first-moment evolution against the finite-regulator Schwinger--Dyson
identity, using the same pure YM action and the specified completion. Obtain an
explicit formula for the derivative moment or a quantified residual. Retain:

- the transverse current in equation (22) of the note: a planar curve does not
  set D3 F3nu or D4 F4nu to zero;
- finite-N product expectations and all derivative/contact terms from insertions;
- the derivative of the flow map B_tau[A] if working at positive tau;
- cusp and contact renormalization if instead proposing to pass to the unflowed
  observable. Compare that choice explicitly with the flowed probe.

The first task is not to claim W and M1 already form a closed system. M2 and the
transverse-current insertion remain independent unknowns. Do not identify
E[B_tau] with delta S[A]/delta A. A local Cartan-valued source-free field in
equation (23) exhibits the failure of deleting the transverse term, with omitted
operator norm 1/2 when b=1. This is an algebraic control, not a vacuum no-go.

Makeenko's 0810.2183, lecture 3, gives the bare loop-equation structure and its
supersymmetric extension. Shen--Smith--Zhu 2512.00570 gives rigorous finite-lattice
equations including open lines for a different YM--Higgs action; use it as a
methodological reference, not as a theorem for our pure-YM or supersymmetric
observable. A direct N=4 extension is another candidate later, but scalar
arclength terms invalidate automatic backtracking cancellation.

## Reproduction and review scope

From the investigation directory:

```sh
python3 -B numerics/check_growing_trace_hierarchy.py --output /tmp/growing-trace-replay.json
```

The checker requires NumPy only. It passed all four driver samples, exact
rational coefficient checks, noncommuting transport and gauge-frame controls,
the Abelian area check, and two evaluations of the remainder inequality.
The largest finite-difference matrix-derivative discrepancy was below 1.314e-10.
These checks do not sample a Yang--Mills path integral or prove renormalization.
Specialist review should focus on the contour completion, insertion ordering,
averaging domains and the scope of the positive-flow observable.
