"""
ADVENT OF CODE: 2021
DAY: 3
AUTHOR: JOSEPH RICHARDSON
"""

from day03_input import raw
from day03_input import test
import gozer
import numpy as np


inp = gozer.readlines(raw, to_int=False, to_np=False)
inp_test = gozer.readlines(test, to_int=False, to_np=False, np_map = None)


def vectorize(data):
    vec = np.empty(shape=(len(data), len(data[0])))
    for i in range(len(data)):
        for j in range(len(data[0])):
            vec[i, j] = int(data[i][j])
    return vec


def part1(data):
    gamma = ''
    epsilon = ''
    vec = vectorize(data)
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


def part2(data):
    vec = vectorize(data)
    vec_o2 = vec.copy()
    vec_co2 = vec.copy()
    # O2 rating
    for col in range(len(data[0])):
        bool_map0 = vec_o2[:, col] == 0
        ones = np.count_nonzero(~bool_map0)
        zeros = np.count_nonzero(bool_map0)
        if ones >= zeros:
            vec_o2 = vec_o2[np.where(vec_o2[:, col] == 1)]
        else:
            vec_o2 = vec_o2[np.where(vec_o2[:, col] == 0)]
        if vec_o2.shape[0] == 1:
            break

    # CO2 rating
    for col in range(len(data[0])):
        ones = np.count_nonzero(vec_co2[:, col] == 1)
        zeros = np.count_nonzero(vec_co2[:, col] == 0)
        if ones >= zeros:
            vec_co2 = vec_co2[np.where(vec_co2[:, col] == 0)]
        elif ones == zeros:
            vec_co2 = vec_co2[np.where(vec_co2[:, col] == 0)]
        else:
            vec_co2 = vec_co2[np.where(vec_co2[:, col] == 1)]
        if vec_co2.shape[0] == 1:
            break

    o2 = int(np.array2string(vec_o2.astype(int), separator='')[2:-2], 2)
    co2 = int(np.array2string(vec_co2.astype(int), separator='')[2:-2], 2)
    return o2 * co2


print(f'PART 1: {part1(data=inp)}')
print(f'PART 2: {part2(data=inp)}')