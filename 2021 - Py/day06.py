"""
ADVENT OF CODE: 2021
DAY: 6
AUTHOR: JOSEPH RICHARDSON
"""

from day06_input import test, raw
import numpy as np
from collections import Counter

def sim_days(data, n_days):
    counter = Counter(data)
    fish = np.empty(shape=(9, 2)).astype(int)
    fish[:, 0] = range(9)
    fish[:, 1] = [counter[x] for x in range(9)]
    for day in range(n_days):
        to_add = fish[0, 1]
        fish[:8, 1] = fish[1:, 1]
        fish[6, 1] += to_add
        fish[8, 1] = to_add
    return fish[:, 1].sum()

print(f'PART 1: {sim_days(data=raw, n_days=80)}')
print(f'PART 2: {sim_days(data=raw, n_days=256)}')
