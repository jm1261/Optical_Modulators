import os
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
import Functions.InputOutput as io
import Functions.Organisation as org

# Functions 4.7843


def tick_function(X):
    '''
    Converts frequency ticks to wavelength ticks, converts from Hz to μm.
    Args:
        X: [array] array of x ticks to convert
    Returns:
        ["%.3f" % z for z in V]: [array] array of converted X ticks.
    '''
    V = (c/(X * 1E12)) * 1E6
    return ["%.3f" % z for z in V]


# Organisation
root = os.getcwd()
dir_paths = io.get_config(file_path=os.path.join(root, '..', "Dirpaths.config"))
datetimestring = org.datetime_string()

# Parameters
c = 3E8  # Speed of light
e = 1.60217662E-19  # Electron charge
eps0 = 8.854187812813E-12  # Permittivity free space
e_m = 9.10938356E-31  # Electron mass
mstar = 0.35
eps = 3.5  # eps inf
lm0 = 635  # nm
m = e_m * mstar
#f_THz = np.arange(901, 1, -1)
#wav_range = c / (f_THz * 1E12)
omega = f_THz * 1E12 * 2 * np.pi
ns = np.arange(-2, 2, 0.1)
ns *= 1E14  # cm^2

# Calculations
plasma_freq = [((n * 1E6) * (e ** 2)) / (eps0 * m) for n in ns]
eps_drude = [eps - (om_p / (omega ** 2)) for om_p in plasma_freq]

# Axis labels
ticks = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900]
wav_ticks = [round((c / (t * 1E12)) * 1E6, 3) for t in ticks]

# Plotting
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()
for eps, label in zip(eps_drude, ns):
    ax1.plot(f_THz[::-1], eps.real, label=f'{label:01.2e}')
ax1.legend(loc=0, prop={'size': 12})
ax1.axhline(y=0, color='black', linestyle='--')
plt.ylim(-10, 6)
ax1.set_xticks(ticks)
ax1Ticks = ax1.get_xticks()
ax2Ticks = ax1Ticks
ax2.set_xticks(ax2Ticks)
ax2.set_xbound(ax1.get_xbound())
ax2.set_xticklabels(tick_function(ax2Ticks))
ax1.set_xlabel("Frequency [THz]", fontsize=14, fontweight='bold')
ax2.set_xlabel("Wavelength [μm]", fontsize=14, fontweight='bold')
ax1.set_ylabel("Epsilon [au]", fontsize=14, fontweight='bold')
plt.show()
