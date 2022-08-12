import math
import statistics


def standard_deviation(x):
    '''
    Calculate standard deviation of array.
    Args:
        x: <array> data array
    Returns:
        stdev: <float> standard deviation of x
    '''
    return statistics.stdev(x)


def standard_error_mean(x):
    '''
    Standard error of the mean of an array.
    Args:
        x: <array> data array
    Returns:
        SEOM: <float> standard error of the mean of x
    '''
    return statistics.stdev(x) / math.sqrt(len(x) - 1)


def quadrature(x, y, z, delta_x, delta_y):
    '''
    Quadrature error for z array, calculated from x and y.
    Args:
        x: <array> x-data array
        y: <array> y-data array
        z: <array> z-data array
        delta_x: <array> error x-data array
        delta_y: <array> error y-data array
    Returns:
        delta_z: <array> error z-data array
    '''
    delta_z = z * math.sqrt(((delta_x / x) ** 2) + ((delta_y / y) ** 2))
    return delta_z


def addition_error(delta_x, delta_y):
    '''
    Error of adding/subtracting two values with an associated error.
    Args:
        x: <float> x data point
        y: <float> y data point
        delta_x: <float> delta_x data point
        delta_y: <float> delta_y data point
    Returns:
        delta_z: <float> associated error with added/substracted value
    '''
    return math.sqrt((delta_x ** 2) + (delta_y ** 2))


def round_sig(x, sig_fig):
    '''
    Round value to given significant figure.
    Args:
        x: <float> data point
        sig_fig: <int> number of significant figures
    Returns:
        value: <float> rounded value
    '''
    return round(x, sig_fig - int(math.floor(math.log10(abs(x)))) - 1)


if __name__ == "__main__":
    wg1 = [0.01, 0.01, 0.00, 0.01]
    wg2 = [0.03, 0.03, 0.02, 0.03]
    wg3 = [0.05, 0.05, 0.05, 0.05]
    wg4 = [0.07, 0.07, 0.06, 0.07]
    mean = sum(wg4)/len(wg4)
    error = standard_error_mean(x=wg4)
    print(f'data set = {wg4}')
    print(f'average = {mean} +/- {error}')
