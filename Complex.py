import numpy as np
import cmath
import functools as ftl
import scipy.optimize as opt

lm0 = 750
thicknesses = [0, 400, 100, 5, 0]
indices = [1.4542-0.0013957j, 2.0278, 1.6588-0.004666j, 0.6588-0.004666j, 1.4542-0.0013957j]
n_guesses = np.arange(np.min(indices), np.max(indices), 0.0001)
k0 = 2 * np.pi / lm0
beta_in = k0 * n_guesses
beta_matrix_out = np.ones((1, len(beta_in)))
n_eff = np.ones((1, len(beta_in)))

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
    return diff

for y, b_in in enumerate(beta_in):
    beta_matrix_out[0, y] = multilayer_opt(b_in, thicknesses, indices, k0)
    try:
        beta_out, r = opt.newton(multilayer_opt, x0=b_in,
                                 args=(thicknesses, indices, k0), maxiter=1000,
                                 tol=1e-10, full_output=True)
    except:
        beta_out = k0
    if (multilayer_opt(beta_out, thicknesses, indices, k0)) < 0.1:
        n_eff[0, y] = beta_out / k0

print(n_eff.real)
print(n_eff.imag)