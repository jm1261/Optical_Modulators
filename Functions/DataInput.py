import csv
import numpy as np


def fpp_csv_in(file_path):
    '''
    Loads a standard csv in, columns are not unpacked.
    Args:
        file_path: <string> path to file
    Returns:
        data: <n-dimensional array> array of data contained within the csv
    '''
    sample, current, voltage, sheet = np.genfromtxt(file_path,
                                                    delimiter=',',
                                                    skip_header=2,
                                                    unpack=True)
    return sample, current, voltage, sheet
