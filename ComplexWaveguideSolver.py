import os
import numpy as np
import scipy.optimize as opt
from operator import itemgetter
import matplotlib.pyplot as plt
import Functions.InputOutput as io
import Functions.PhysicsMaths as pm
import Functions.Organisation as org

# Organisation
root = os.getcwd()
dir_paths = io.get_config(file_path=os.path.join(root, 'Dirpaths.config'))
params = io.get_config(file_path=os.path.join(
                       root, 'SlabWaveguideParams.config'))
dt_string = org.datetime_string()
out_path = os.path.join(dir_paths['slabwg'], 'Absorption')
org.check_dir_exists(out_path)

# Parameters
lm0, sub, wg, l1, l2, cov = itemgetter(
    "lm0", "Sub", "Wg", "L1", "L2", "Cov")(params)
acc_layer_thicknesses = np.arange(0, l2[2]+0.5, 0.5)
thicknesses = [np.array([sub[2], wg[2], l1[2] - x, x, cov[2]])
               for x in acc_layer_thicknesses]
n = [complex(sub[0], sub[1]), complex(wg[0], wg[1]), complex(l1[0], l1[1]),
     complex(l2[0], l2[1]), complex(cov[0], cov[1])]
k0 = 2 * np.pi / lm0
n_guesses = np.arange(cov[0], wg[0], 0.01)
beta_in = k0 * n_guesses
beta_mat_out = np.ones((len(acc_layer_thicknesses), len(beta_in)))
n_eff = np.ones((len(acc_layer_thicknesses), len(beta_in)))

# Calculation
for x, t in enumerate(thicknesses):
    for y, b_in in enumerate(beta_in):
        beta_mat_out[x, y] = abs(pm.complex_multilayer_opt(b_in, t, n, k0))
        try:
            beta_out, r = opt.newton(pm.complex_multilayer_opt,
                                     x0=b_in, args=(t, n, k0), maxiter=1000,
                                     tol=1e-10, full_output=True)
        except:
            beta_out = k0
        if abs(pm.multilayer_opt(beta_out, t, n, k0)) < 0.1:
            n_eff[x, y] = beta_out / k0

# Organisation
n_textstring = ','.join([f'{ns}' for ns in n])
title_string = f'wg:{wg[1]}nm layer:{l1[1]}nm RIU:{n_textstring}'
out_n_textstring = '_'.join([f'{ns}' for ns in n])
outname_string = f'complex_{wg[2]}_{l1[2]}_{out_n_textstring}_{dt_string}.png'
outtxt_string = f'comeplex_{wg[2]}_{l1[2]}_{out_n_textstring}_{dt_string}.txt'
outtxt_path = os.path.join(out_path, outtxt_string)

# Plotting
fig, ax = plt.subplots(1, 1, figsize=[10, 7])
cb = ax.pcolor(acc_layer_thicknesses, n_guesses, beta_mat_out.T)
fig.colorbar(cb)
for neff in n_eff.T:
    ax.plot(acc_layer_thicknesses, neff, 'wo', ms=2)
    with open(outtxt_path, 'a') as f:
        f.write(f'{neff.real}-{neff.imag}i\n')
ax.set_ylim([cov[0], wg[0]])
ax.set_xlabel('Accumulation Layer Thickness', fontsize=14, fontweight='bold')
ax.set_ylabel(r'$n_{eff}$', fontsize=14, fontweight='bold')
ax.set_title(title_string, fontsize=14, fontweight='bold')
plt.savefig(os.path.join(out_path, outname_string))
plt.show()
fig.clf()
plt.close(fig)
