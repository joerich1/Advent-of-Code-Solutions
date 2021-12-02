"""
ADVENT OF CODE: 2021
DAY: XX
TIME: XX MINUTES
AUTHOR: JOSEPH RICHARDSON
"""

from day_xx_input_template import raw
from day_xx_input_template import test
import gozer
import numpy as np
import pandas as pd

dict_map = {}

# If lines from a text input needs to be split into rows of a list
inp = gozer.readlines(raw, to_int=False, to_np=False)
inp_test = gozer.readlines(test, to_int=False, to_np=False, np_map = None)
# print(inp)
# print(inp_test)


# PART 1
def part1(data):
    return 0


# PART 2
def part2(data):
    return 0


print(f'PART 1: {part1(data=inp_test)}')
print(f'PART 2: {part2(data=inp_test)}')
