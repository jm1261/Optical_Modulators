import os
import math
import datetime
import numpy as np
import Functions.Organisation as org

''' Organisation '''
date = datetime.date.today()
root = os.getcwd()
dirpathsconfig = org.get_config(
    config_path=os.path.join(
        root,
        'Dirpaths.config'))
rootpath = os.path.join(
    dirpathsconfig['root'],
    dirpathsconfig['comsol'])
dirpath = os.path.join(
    rootpath,
    'Drude_Carrier_Conc_Simulation')
org.check_dir_exists(dir_path=dirpath)
outpath = os.path.join(
    dirpath,
    f'{date}')
org.check_dir_exists(dir_path=outpath)

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
for thickness in layerthicknesses:
    for ito in itothicknesses:

        ''' Calculations '''
        carrierdensity = [
            ((n * 1E12) / 0.0001) / (thickness * 1E-9)
            for n in twodconc]  # 1/m^3
        omegapsquared = [
            (n * (echarge ** 2)) / (emass * mstar * epsfreespace)
            for n in carrierdensity]
        drudereal = [
            epshighfreq - (omp / ((omega ** 2) + (gamma ** 2)))
            for omp in omegapsquared]
        drudeimag = [
            (omp * gamma) / (omega * ((omega ** 2) + (gamma ** 2)))
            for omp in omegapsquared]
        n = [
            math.sqrt(
                0.5 * (((drudereal[x] ** 2) + (drudeimag[x] ** 2)) ** 0.5)
                + (drudereal[x] / 2))
            for x in range(len(drudereal))]
        k = [
            math.sqrt(
                0.5 * (((drudereal[x] ** 2) + (drudeimag[x] ** 2)) ** 0.5)
                - (drudereal[x] / 2))
            for x in range(len(drudereal))]
        epsreal = [(n[x] ** 2) - (k[x] ** 2) for x in range(len(n))]
        epsimag = [2 * n[x] * k[x] for x in range(len(n))]

        ''' Data Output '''
        data = np.array(
            [
                biasvoltage,
                carrierdensity,
                drudereal,
                drudeimag,
                n,
                k,
                epsreal,
                epsimag])
        outdata = data.T
        headerstring = (
            'bias, n_density, drude_real, drude_imag, n, k, eps_real, '
            'eps_imag, n_eff, k_eff')
        filename = (
            f'AccumulationLayer_{round(thickness, 1)}nm'
            f'_ITOLayer_{round(ito, 1)}nm.csv')
        filepath = os.path.join(
            outpath,
            filename)
        np.savetxt(
            filepath,
            outdata,
            delimiter=',',
            header=headerstring)
