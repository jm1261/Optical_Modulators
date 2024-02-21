import numpy as np
import matplotlib.pyplot as plt


#W = 5E-8
e = 1.6E-19
eps_s = 3.2
N_D = 3E26

N_D_range = np.arange(1E20, 1E27, 1E20)

W = []
for n in N_D_range:
    w = 1 / (e * n)
    W.append(w)


fig, ax = plt.subplots(1)
ax.plot(voltage_range, W)
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()