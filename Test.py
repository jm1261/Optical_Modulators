import os
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
import Functions.PhysicsMaths as pm

root = os.getcwd()

lm0 = 750
n = [1.4542, 1, 1, 1, 1]
atl = np.arange(0, 5.5, 0.5)
thicknesses = [np.array([0, 400, 100, x, 0]) for x in atl]
k0 = 2 * np.pi / lm0
n_guesses = np.arange(np.min(n), np.max(n), 0.01)
beta_in = k0 * n_guesses
beta_mat_out = np.ones((len(atl), len(beta_in)))
n_eff = np.ones((len(atl), len(beta_in)))

for x, t in enumerate(thicknesses):
    for y, b_in in enumerate(beta_in):
        beta_mat_out[x, y] = abs(pm.multilayer_opt(b_in, t, n, k0))
        try:
            beta_out, r = opt.newton(pm.multilayer_opt, x0=b_in,
                                     args=(t, n, k0), maxiter=1000,
                                     tol=1e-10, full_output=True)
        except:
            beta_out = k0
        if abs(pm.multilayer_opt(beta_out, t, n, k0).real) < 0.1:
            n_eff[x, y] = beta_out.real / k0

fig, ax = plt.subplots(1, figsize=[10, 7])
cb = ax.pcolor(atl, n_guesses, beta_mat_out.T)
fig.colorbar(cb)
for neff in n_eff.T:
    ax.plot(atl, neff.real, 'wo', ms=2)
plt.show()