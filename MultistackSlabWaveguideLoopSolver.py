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
params = io.get_config(file_path=os.path.join(
                       root, 'SlabWaveguideParams.config'))
datetimestring = org.datetime_string()
lm0, sub, wg, l1, l2, cov = itemgetter(
    "lm0", "Sub", "Wg", "L1", "L2", "Cov")(params)

# Parameters
acc_layer_thicknesses = np.arange(0, l2[1]+0.5, 0.5)
delta_n = np.arange(l2[0]-1, l2[0]+0.01, 0.01)
thicknesses = [np.array([sub[1], wg[1], l1[1] - x, x, cov[1]])
               for x in acc_layer_thicknesses]

for dn in delta_n:
    n = [sub[0], wg[0], l1[0], round(dn, 4), cov[0]]
    k0 = 2 * np.pi / lm0
    n_guesses = np.arange(cov[0], wg[0], 0.01)
    beta_in = k0 * n_guesses
    beta_mat_out = np.ones((len(acc_layer_thicknesses), len(beta_in)))
    n_eff = np.ones((len(acc_layer_thicknesses), len(beta_in)))

    # Calculations
    for x, t in enumerate(thicknesses):
        for y, b_in in enumerate(beta_in):
            beta_mat_out[x, y] = abs(pm.multilayer_opt(b_in, t, n, k0))
            try:
                beta_out, r = opt.newton(pm.multilayer_opt,
                                         x0=b_in,
                                         args=(t, n, k0),
                                         maxiter=1000,
                                         tol=1e-10,
                                         full_output=True)
            except:
                beta_out = k0
            if abs(pm.multilayer_opt(beta_out, t, n, k0).real) < 0.1:
                n_eff[x, y] = beta_out.real / k0

    # Organisation
    n_textstring = ','.join([f'{ns}' for ns in n])
    title_string = f'wg:{wg[1]}nm layer:{l1[1]}nm RIU:{n_textstring}'
    out_n_textstring = '_'.join([f'{ns}' for ns in n])
    outname_string = f'{wg[1]}_{l1[1]}_{out_n_textstring}_{datetimestring}.png'
    outtxt_string = f'{wg[1]}_{l1[1]}_{out_n_textstring}_{datetimestring}.txt'
    outtxt_path = os.path.join(dir_paths["slabwgri"], outtxt_string)

    # Plotting
    fig, ax = plt.subplots(1, 1, figsize=[10, 7])
    cb = ax.pcolor(acc_layer_thicknesses, n_guesses, beta_mat_out.T)
    fig.colorbar(cb)
    for neff in n_eff.T:
        ax.plot(acc_layer_thicknesses, neff.real, 'wo', ms=2)
        txt_line = ', '.join([f'{n}' for n in neff.real])
        with open(outtxt_path, 'a') as f:
            f.write(f'{txt_line}\n')
    ax.set_ylim([cov[0], wg[0]])
    ax.set_xlabel('Accumulation Layer Thickness',
                  fontsize=14, fontweight='bold')
    ax.set_ylabel(r'$n_{eff}$', fontsize=14, fontweight='bold')
    ax.set_title(title_string, fontsize=14, fontweight='bold')
    plt.savefig(os.path.join(dir_paths["slabwgri"], outname_string))
    fig.clf()
    plt.close(fig)

    dp.effective_index_finder(file_path=outtxt_path,
                              row_header=acc_layer_thicknesses)
