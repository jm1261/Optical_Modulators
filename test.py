import os
import numpy as np
import matplotlib.pyplot as plt


def import_dispersion(root, metal):
    '''
    '''
    filename = f'{metal}_Dispersion.csv'
    file_path = os.path.join(root, "Dispersions", filename)
    wavelength, n, k = np.genfromtxt(fname=file_path,
                                     delimiter=',',
                                     skip_header=1,
                                     unpack=True)
    wavelength *= 1000
    return filename, wavelength, n, k


def plot_dispersion(filename,
                    wavelength,
                    n,
                    k,
                    save=False,
                    show=False):
    '''
    '''
    fig, ax = plt.subplots(1, 1, figsize=[10, 7])
    line1 = ax.plot(wavelength, n, 'r', lw=2, label='n')
    ax2 = ax.twinx()
    line2 = ax2.plot(wavelength, k, 'b', lw=2, label='k')
    ax.set_ylabel('Refractive Index [n]', fontsize=14, fontweight='bold')
    ax2.set_ylabel(
        'Extinction Coefficient [k]', fontsize=14, fontweight='bold')
    ax.set_xlabel('Wavelength [nm]', fontsize=14, fontweight='bold')
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax.legend(lines, labels, frameon=True, ncol=1, loc=0, prop={'size': 14})
    if save:
        out_path = os.path.join(root, "Dispersions", f'{filename[0:-4]}.png')
        plt.savefig(out_path)
    if show:
        plt.show()
    fig.clf()
    plt.close(fig)


def dielectric_function(n, k):
    '''
    '''
    real_dielectric = n**2 - k**2
    imaginary_dielectric = 2 * n * k
    return real_dielectric, imaginary_dielectric


def plot_dielectric(filename,
                    wavelength,
                    real,
                    imaginary,
                    save=False,
                    show=False):
    '''
    '''
    fig, ax = plt.subplots(1, 1, figsize=[10, 7])
    line1 = ax.plot(wavelength, real, 'r', lw=2, label='real')
    ax2 = ax.twinx()
    line2 = ax2.plot(wavelength, imaginary, 'b', lw=2, label='imaginary')
    ax.set_ylabel('Refractive Index [n]', fontsize=14, fontweight='bold')
    ax2.set_ylabel(
        'Extinction Coefficient [k]', fontsize=14, fontweight='bold')
    ax.set_xlabel('Wavelength [nm]', fontsize=14, fontweight='bold')
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax.legend(lines, labels, frameon=True, ncol=1, loc=0, prop={'size': 14})
    if save:
        out_path = os.path.join(root, "Dispersions",
                                f'{filename[0:-4]}_Dielectric.png')
        plt.savefig(out_path)
    if show:
        plt.show()
    fig.clf()
    plt.close(fig)


def damping_constant(wavelength, real):
    '''
    '''
    term1 = wavelength * real
    term2 - 1 - real
    return term1, term2


def plasma_frequency(wavelength, real, imaginary):
    '''
    '''
    wav_squared = [(x ** 2) for x in wavelength]
    imaginary_squared = [(x ** 2) for x in imaginary]
    one_minus_real = [(1 - x) for x in real]
    one_minus_real_squared = [(x ** 2) for x in one_minus_real]
    term1 = [(wav_squared[x]*(imaginary_squared[x]+one_minus_real_squared[x]))
             for x in range(0, len(wav_squared))]
    
    return term1, one_minus_real


if __name__ == "__main__":
    root = os.getcwd()
    filename, wavelength, n, k = import_dispersion(root=root,
                                                   metal='Gold')
    plot_dispersion(filename=filename, wavelength=wavelength,
                    n=n, k=k, save=False, show=False)

    frequency = (3e8/(wavelength/1e9))
    omega = frequency/2*np.pi

    real_dielectric, imaginary_dielectric = dielectric_function(n=n, k=k)
    plot_dielectric(filename=filename, wavelength=wavelength,
                    real=real_dielectric, imaginary=imaginary_dielectric,
                    save=True, show=False)
    term1, term2 = damping_constant(wavelength=frequency,
                                    real=real_dielectric)
    term1, term2 = plasma_frequency(wavelength=omega,
                                    real=real_dielectric,
                                    imaginary=imaginary_dielectric)
    plt.plot(term2, term1)
    plt.xlim(0, 200)
    plt.ylim(0, 4e33)
    plt.show()
