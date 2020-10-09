import os
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
import Functions.InputOutput as io

root = os.getcwd()
config = io.get_config(file_path=os.path.join(root, '400nm_SiN_params.config'))
neff_2, alt, op, neff_1, wav, ml = itemgetter(
    "n_eff_2", "accumulation_layer_thickness", "overlap_percentage",
    "n_eff_1", "wavelength", "modulator_length")(config)
delta_n = np.arange(0, 1.01, 0.1)

fig, ax = plt.subplots(1, 1, figsize=[10, 7])
for i in range(0, len(alt)):
    delta_n_eff = neff_2 - (op[i] * delta_n)
    optical_path_1 = ml * neff_1
    optical_path_2 = [(ml * neff_2) for neff_2 in delta_n_eff]
    path_difference = [(op2 - optical_path_1) for op2 in optical_path_2]
    remainder = [(pd % wav) for pd in path_difference]
    phase = [(rem / wav) for rem in remainder]
    phase_in_rads = [(phs * 2) for phs in phase]
    ax.plot(delta_n_eff, phase_in_rads, color=f'C{i}', label=f'{alt[i]}')
ax.legend(loc=3, ncol=2, prop={'size': 14})
ax.set_xlabel('Arm Effective Index [RIU]', fontsize=14, fontweight='bold')
ax.set_ylabel('Phase [pi]', fontsize=14, fontweight='bold')
ax.tick_params(axis='both', colors='black', labelsize=14)
plt.show()
    
