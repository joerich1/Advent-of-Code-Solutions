import numpy as np


def readlines(data, to_int=False, to_np=False, np_map=None):
    """
    Reads a multi-line text input and splits lines into rows of an array.
    """
    if to_int and not to_np:
        lines = [int(line) for line in data.split('\n')]

    else:
        lines = [line for line in data.split('\n')]

    if to_np:
        arr = np.empty(shape=(len(lines), len(lines[0])))
        for row in range(len(lines)):
            for char in range(len(lines[0])):
                if np_map:
                    arr[row, char] = np_map[lines[row][char]]
                else:
                    arr[row, char] = lines[row][char]

        if to_int:
            return arr.astype(int)
        else:
            return arr

    return lines
