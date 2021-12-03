"""
ADVENT OF CODE: 2021
DAY: 3
AUTHOR: JOSEPH RICHARDSON
"""

from day03_input import raw
from day03_input import test
import gozer
import numpy as np


inp = gozer.readlines(raw, to_int=True, to_np=True, np_map=None)
inp_test = gozer.readlines(test, to_int=True, to_np=True, np_map=None)


def part1(vec):
    gamma = ''
    epsilon = ''
    for col in range(vec.shape[1]):
        zeros = np.count_nonzero(vec[:, col] == 0)
        ones = np.count_nonzero(vec[:, col] == 1)
        if ones > zeros:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return int(gamma, 2) * int(epsilon, 2)


def part2(vec):
    vec_o2 = vec.copy()
    vec_co2 = vec.copy()
    # O2 rating
    for col in range(vec.shape[1]):
        ones = np.count_nonzero(vec_o2[:, col] == 1)
        zeros = np.count_nonzero(vec_o2[:, col] == 0)
        if ones >= zeros:
            vec_o2 = vec_o2[np.where(vec_o2[:, col] == 1)]
        else:
            vec_o2 = vec_o2[np.where(vec_o2[:, col] == 0)]
        if vec_o2.shape[0] == 1:
            break

    # CO2 rating
    for col in range(vec.shape[1]):
        ones = np.count_nonzero(vec_co2[:, col] == 1)
        zeros = np.count_nonzero(vec_co2[:, col] == 0)
        if ones >= zeros:
            vec_co2 = vec_co2[np.where(vec_co2[:, col] == 0)]
        else:
            vec_co2 = vec_co2[np.where(vec_co2[:, col] == 1)]
        if vec_co2.shape[0] == 1:
            break

    o2 = int(np.array2string(vec_o2, separator='')[2:-2], 2)
    co2 = int(np.array2string(vec_co2, separator='')[2:-2], 2)
    return o2 * co2


print(f'PART 1: {part1(vec=inp)}')
print(f'PART 2: {part2(vec=inp)}')