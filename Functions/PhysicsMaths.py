import cmath
import numpy as np
import functools as ftl



def multilayer_opt(beta, d, n, k_0):
    '''
    Multilayer dispersion matrix taken from a series of notes found at
    fotonica.intec.ugent.be/download/ocs131.pdf. Calculates the k vectors at
    each layer, and uses it to determine a dispersion matrix for each layer.
    Finds the product of the matrices throughout the structure. More details
    found in the notes.
    Args:
        beta: <float> propagation constant
        d: <array> layer thicknesses
        n: <array> layer refractive indices
        k0: <float> incident k vector
    Returns:
        diff: <array> propagation dispersion matrix
    '''
    k_x = [cmath.sqrt(((k_0 * n_i) ** 2) - (beta ** 2)) for n_i in n]
    alpha = [(1j * k_xi) for k_xi in k_x]
    delta_p1 = [(a * d_i) for a, d_i in zip(alpha[1:], d[1:])]
    matrices = [
        np.array(
            [
                [(a + a_p1) * np.exp(-d_p1), (a - a_p1) * np.exp(d_p1)],
                [(a - a_p1) * np.exp(-d_p1), (a + a_p1) * np.exp(d_p1)]
            ]
        ) / (2 * a)
        for a, a_p1, d_p1 in zip(alpha, alpha[1:], delta_p1)]
    M = ftl.reduce(np.matmul, matrices)
    diff = M[0, 0]
    return abs(diff)
