import numpy as np


def readlines(data, to_int=False, to_np=False, np_map=None):
    """
    Reads a multi-line text input and splits lines into rows of an array.
    """
    if to_int:
        lines = [int(line) for line in data.split('\n')]
    else:
        lines = [line for line in data.split('\n')]
    if to_np:
        arr = np.empty(shape=(len(lines), len(lines[0])))
        #for row in lines:

    return lines
