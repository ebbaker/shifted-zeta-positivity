"""Exploratory sensitivity at the certified fixed-b endpoint limit.

Prepared for Edward Baker, 2026-10-08, with GPT-6 (Codex) assistance.
Exact serving variant and configured reasoning effort are not exposed.
Floating values are diagnostic only; no new exponent certificate is made.
"""
import json
from math import sqrt

# Positive root of the polynomial certified in check_geometry_optimization.py.
e = 98 / (286020 + sqrt(286020**2 + 4*1162800*49))
ell, b = 1/6 + e, 1/8
h = (1 + 3*ell + b)/2
delta = (1896 - 11520*e)/(2*(2448 + 6048*e))
x, alpha = 1/2, 5/6
D = 3 - 17*x/9
P = (2 - 8*x/9)*(1-x)
J = (alpha-delta)*D + delta*P
T = (alpha-delta)*delta*P/J
t = 1 + delta*P/(2*J)
r = ((2-8*x/9)*t - 5*x/9)/D
m = t-r
R = 1-delta+T/2
dE_dell = 5/4 + 3*T/4
row_to_boundary = h/(4*dE_dell)
short_slope = delta*P/D
long_slope = alpha-delta
theta_to_row = short_slope/(short_slope+long_slope)*5*t/6

# A local stationary scout in b and ell at y=0, not a global certificate.
def row_and_derivative(d):
    j = (alpha-d)*D+d*P
    numerator = (alpha-d)*d*P
    numerator_prime = (alpha-2*d)*P
    tp = (numerator_prime*j-numerator*(P-D))/(j*j)
    return 1-d+numerator/(2*j), -1+tp/2

left, right = .38, .40
assert row_and_derivative(left)[0] > 2/3 > row_and_derivative(right)[0]
for _ in range(60):
    mid = (left+right)/2
    if row_and_derivative(mid)[0] > 2/3:
        left = mid
    else:
        right = mid
d_stationary = (left+right)/2
rs, derivative = row_and_derivative(d_stationary)
ell_stationary = (5/12-d_stationary/2)/(3/4+3*d_stationary/2)
b_stationary = -(1+3*ell_stationary)*(derivative+1)/derivative

result = {
    'status': 'Exploratory floating sensitivities; not a new zero-free theorem or global certificate.',
    'limiting_point': dict(e=e, ell=ell, b=b, h=h, sigma=11/12-ell/4,
                          delta=delta, x=x, R=R, t=t, inverse_length=r, plain_length=m),
    'prime_lengths': dict(inverse_capacity=(1-r)/2, plain_capacity=2*(1-2*m)/9,
                         available=ell/h, second_inverse_width_slack=2*r-1),
    'mixed_moment_length': r+2*m,
    'local_sensitivities': dict(dE_dell=dE_dell,
                               boundary_gain_per_row_exponent_gain=row_to_boundary,
                               row_gain_per_one_minus_theta=theta_to_row,
                               boundary_gain_per_one_minus_theta=row_to_boundary*theta_to_row),
    'stationary_scout_at_y_zero': dict(delta=d_stationary, ell=ell_stationary,
                                      b=b_stationary, sigma=11/12-ell_stationary/4,
                                      globally_certified=False),
}
print(json.dumps(result, indent=2, sort_keys=True))
