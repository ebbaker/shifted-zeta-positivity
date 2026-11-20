# AGC-JH-E04 return r1

19 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex LLM assistance. Helper dispatch gpt-6.2-sol, effort ultra. Lead
settings and independent serving-backend metadata were unavailable.

**Disposition:** the fixed exact-rational check is complete. The indicated
formulas agree in all specified cases. The moving polynomial is an algebra
control with six simple roots at the checked slice, outside the canonical
theta comparison. Review is internal and uses the written formulas as
inputs. [Request r1](AGC_JH_E04_REQUEST_R1_20261119.md).

- **Weyl and simplex increment.** With \(\beta_j=j/(j+1)\), the rational
  Weyl cross multiplication gives \(h_N^*\xi\) over \(P_NP_{N+2}\) at
  \(N=2,3,4\). The first two nonzero Fourier coefficients from return walks
  independently agree with the mixed-node formula at each degree. The
  variance from the coefficient of the combined node polynomial agrees
  with the trace formula, taking values \(29/252,233/2160,82/825\),
  respectively. [Note03](../../notes/03_AGC_JH_DEGREE_TIME_INTERFACE_20261119.md).
- **Forced hierarchy.** At time zero the polynomial has exactly the two
  target roots \(4/3,2/3\) on the interior of the specified circle. The
  remaining roots are strictly exterior, and the separations persist on a
  small time neighborhood by continuity. The residue calculation gives
  \(\gamma=-56053/40040\) and \(\delta=-29327/20020\). In the center, gap,
  \(M,S_2,T_2\) and all five selected split rows, the unforced recurrence,
  isolated force and full recurrence agree with direct finite root-sum
  differentiation. Omitting all forcing gives a \(D\) prediction-minus-
  actual residual \(29327/20020\); omitting just the moving-kernel terms
  gives an \(M\) residual \(-12827024807769/64192192064000\).
  [Note02](../../notes/02_AGC_JH_FORCED_INTEGER_HIERARCHY_20261119.md).
- **Signed first variation.** For the two stated \(h=\pm1/64\) polynomial
  cases, the Laurent coefficients of the collar logarithm give
  \(\Delta c=1/128\) and \(\Delta D=h\). The respective linear terms are
  \(255/16384,-257/16384\). The exact remainder is \(1/16384\) in both
  cases and the enclosure \(13/3600\) is smaller than either linear term
  in absolute value. The \(h<0\) collar bound \(449/9216\) also gives a
  common valid bound for both fields. [Note04](../../notes/04_AGC_JH_SIGNED_GAP_REMAINDER_20261119.md).

The [replay script](../../numerics/check_agc_jh_interface_20261119.py) uses
the Python standard library. The [execution record](../../numerics/03_AGC_JH_EXACT_CHECKS_20261119.json)
contains the source and code hashes, exact values, sensitivity residuals,
runtime and environment. No degree sweep, floating estimate, parity-control
sampling or canonical input acquisition took place. The checks can support
the next internal assessment of the conditioned formulas. Any canonical
signed seed, contour data or comparison gain still needs separate evidence.
