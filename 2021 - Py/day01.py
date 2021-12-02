"""
ADVENT OF CODE: 2021
DAY: 1
TIME: 9 MINUTES
AUTHOR: JOSEPH RICHARDSON
"""

from day01_input import raw
import gozer


# If lines from a text input needs to be split into rows of a list
inp = gozer.readlines(raw, to_int=True)


# PART 1
def part1():
    start = inp[0]
    count = 0
    for i in range(1, len(inp)):
        this = inp[i]
        if this > start:
            count += 1
        start = this
    return count


# PART 2
def part2():
    start = inp[0] + inp[1] + inp[2]
    count = 0
    for i in range(1, len(inp)-2):
        next = inp[i] + inp[i+1] + inp[i+2]
        if next > start:
            count += 1
        start = next
    return count


print(f'PART 1: {part1()}')
print(f'PART 2: {part2()}')
