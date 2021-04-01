import os
import numpy as np
import scipy.optimize as opt
from operator import itemgetter
import matplotlib.pyplot as plt
import Functions.InputOutput as io
import Functions.PhysicsMaths as pm
import Functions.Organisation as org
import Functions.DataProcessing as dp

# Organisation
root = os.getcwd()
dir_paths = io.get_config(file_path=os.path.join(root, 'Dirpaths.config'))
params = io.get_config(file_path=os.path.join(root, 'SlabWGParams.config'))
lm0, sub, wg, l1, l2, cov = itemgetter(
    "lambda0", "Substrate", "Waveguide", "Layer1", "Layer2", "Cover")(params)
dt_string = org.datetime_string()
out_path = os.path.join(dir_paths["slabwg"], "Multistack")
org.check_dir_exists(out_path)

# Parameters
thicknesses = [sub[2], wg[2], l1[2], l2[2], cov[2]]
indices = [sub[0], wg[0], l1[0], l2[0], cov[0]]
n_guesses = np.arange(np.min(indices), np.max(indices), 0.0001)
k0 = 2 * np.pi / lm0
beta_in = k0 * n_guesses
beta_matrix_out = np.ones((1, len(beta_in)))
n_eff = np.ones((1, len(beta_in)))

# Calculation
for y, b_in in enumerate(beta_in):
    beta_matrix_out[0, y] = abs(pm.multilayer_opt(b_in, thicknesses, indices, k0))
    try:
        beta_out, r = opt.newton(pm.multilayer_opt, x0=b_in,
                                 args=(thicknesses, indices, k0), maxiter=1000,
                                 tol=1e-10, full_output=True)
    except:
        beta_out = k0
    if abs(pm.multilayer_opt(beta_out, thicknesses, indices, k0).real) < 0.1:
        n_eff[0, y] = beta_out.real / k0

# Output Organisation
out_n_textstring = '_'.join([f'{n}' for n in indices])
outtxt_string = f'real_{wg[2]}_{l1[2]}_{out_n_textstring}_{dt_string}.txt'

# Data Processing
for neff in n_eff.T:
    txt_line = ', '.join([f'{n}' for n in neff.real])
    with open(os.path.join(out_path, outtxt_string), 'a') as f:
        f.write(f'{txt_line}\n')
dp.effective_index_finder(file_path=os.path.join(out_path, outtxt_string),
                          row_header=np.arange(1, 10, 1))
