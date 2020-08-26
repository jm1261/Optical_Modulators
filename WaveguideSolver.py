import numpy as np
import cmath
import functools as ftl
import scipy.optimize as opt
# Break it down simply
thicknesses = [0, 400, 10, 5, 0]  # nm
n = [1.4542, 2.0278, 1.6588, 0.6588, 1.4542]
lambda0 = 750  # nm
k0 = 2 * np.pi / lambda0
beta_in = k0 * 2.0278
# Create a [1, 1] matrix for the beta_out values
beta_out = np.ones((2))
n_eff = np.ones((2))
# Calculations
def multilayer_opt(beta, d, n, k_0):
    k_x = [cmath.sqrt(((k_0 * n_i) ** 2) - (beta ** 2)) for n_i in n]
    alpha = [(1j * k_xi) for k_xi in k_x]
    delta_p1 = [(a * d_i) for a, d_i in zip(alpha[1:], d[1:])]
    matrices = [
        np.array(
            [
                [(a + a_p1) * np.exp(-d_p1), (a - a_p1) * np.exp(d_p1)],
                [(a - a_p1) * np.exp(-d_p1), (a + a_p1) * np.exp(d_p1)]
            ]
        ) / (2 * a)
        for a, a_p1, d_p1 in zip(alpha, alpha[1:], delta_p1)]
    M = ftl.reduce(np.matmul, matrices)
    diff = M[0, 0]
    return abs(diff)
beta_out = abs(multilayer_opt(beta_in, thicknesses, n, k0))
try:
    b_out, r = opt.newton(multilayer_opt, x0=beta_in, args=(t, n, k0), maxiter=1000, tol=1e-10, full_output=True)
except:
    b_out = k0
if abs(multilayer_opt(b_out, thicknesses, n, k0).real) < 0.1:
    n_eff = b_out.real / k0
print(beta_out)
print(b_out.real)
print(n_eff)