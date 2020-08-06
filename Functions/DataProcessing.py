import numpy as np


def effective_index_finder(file_path,
                           row_header):
    '''
    '''
    data = np.genfromtxt(file_path, delimiter=',')
    columns = len(data[0])
    for i in range(0, columns):
        column = data[:, i]
        uniques = np.unique([round(x, 1) for x in column])
        means = []
        for y in uniques:
            meanarray = []
            for z in column:
                if z <= y + 0.1 and z >= y - 0.1:
                    meanarray.append(z)
                else:
                    pass
            if len(meanarray) == 0:
                pass
            else:
                means.append(sum(meanarray) / len(meanarray))
        text_line = ', '.join([f'{mean}' for mean in means])
        with open(f'{file_path[0:-4]}.csv', "a") as outfile:
            outfile.write(f'{row_header[i]}, {text_line}\n')
