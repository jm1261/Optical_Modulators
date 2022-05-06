import os
import math
import numpy as np
import matplotlib.pyplot as plt
import Functions.Organisation as org


def load_csv(file_path,
             col_indices):
    '''
    '''
    x, y = np.genfromtxt(
        fname=file_path,
        delimiter=',',
        unpack=True,
        usecols=col_indices,
        skip_header=1)
    return x, y


if __name__ == '__main__':

    ''' Organisation '''
    root = os.getcwd()
    dirpathsconfig = org.get_config(
        config_path=os.path.join(
            root,
            '..',
            'Dirpaths.config'))
    rootpath = os.path.join(
        dirpathsconfig['root'],
        dirpathsconfig['comsol'])
    dirpath = org.find_path(
        default=rootpath,
        dir_path=True)

    ''' Constants '''
    c = 3E8
    echarge = 1.60217662E-19
    emass = 9.10938356E-31
    mstar = 0.35
    epsfreespace = 8.854187812813E-12
    epshighfreq = 3.8
    gamma = 2E14  # rad/s

    ''' Parameters '''
    wavelength = 635E-9  # m
    frequency = c / wavelength
    omega = frequency * 2 * np.pi
    biasvoltage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    twodconc = [20, 40, 55, 75, 100, 120, 135, 155, 175, 200]  # 1/cm^2
    layerthicknesses = np.arange(1, 10.1, 1)  # nm
    itothicknesses = range(25, 155, 25)

    ''' Loop Thicknesses '''
    for ito in itothicknesses:

        ''' Plot Carrier '''
        fig, ax = plt.subplots(1, figsize=[10, 7])
        for index, thickness in enumerate(layerthicknesses):
            filename = (
                f'AccumulationLayer_{round(thickness, 1)}nm'
                f'_ITOLayer_{round(ito, 1)}nm.csv')
            filepath = os.path.join(
                dirpath,
                filename)
            bias, carn, epsdr, epsdi, n, k, epsr, epsi, neff, keff = np.genfromtxt(
                fname=filepath,
                delimiter=',',
                unpack=True,
                skip_header=1)
            absorpt = [(4 * np.pi * (keff[i] - keff[0])) / wavelength for i in range(1, len(keff))]
            total_absorpt = [k * 100E-6 for k in absorpt]
            transmission = [np.exp(-l) * 100 for l in total_absorpt]
            #opl = [n * 100E-6 for n in neff]
            #opl0 = 1.723 * 100E-6
            #delta_opl = [np.pi * 2 * (o/opl0) for o in opl]
            ax.plot(bias[1: ,], transmission, f'C{index}x', markersize=4, label=f'{thickness}nm')
        ax.legend(frameon=True, loc=0, prop={'size': 12})
        ax.set_xlabel('Bias Voltage [V]', fontsize=14, fontweight='bold')
        ax.set_ylabel('Transmission [%]', fontsize=14, fontweight='bold')
        ax.set_title(f'ITO Thickness {ito}nm Transmission 100um Length', fontsize=18, fontweight='bold')
        ax.tick_params(
            axis='both',
            labelsize=14)
        plt.savefig(
            os.path.join(
                dirpath,
                f'{ito}_opl.png'))
        fig.clf()
        plt.close(fig)
