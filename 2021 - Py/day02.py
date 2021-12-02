"""
ADVENT OF CODE: 2021
DAY: 2
TIME: 11 MINUTES
AUTHOR: JOSEPH RICHARDSON
"""

from day02_input import raw
from day02_input import test
import gozer

# If lines from a text input needs to be split into rows of a list
inp = gozer.readlines(raw, to_int=False, to_np=False, np_map=None)
inp_test = gozer.readlines(test, to_int=False, to_np=False, np_map=None)


# PART 1
def part1(data):
    horiz = 0
    depth = 0

    for row in data:
        command = row.split(' ')

        if command[0] == 'forward':
            horiz += int(command[1])
        elif command[0] == 'down':
            depth += int(command[1])
        else:
            depth -= int(command[1])

    return horiz * depth


# PART 2
def part2(data):
    horiz = 0
    depth = 0
    aim = 0

    for row in data:
        command = row.split(' ')

        if command[0] == 'forward':
            horiz += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == 'down':
            aim += int(command[1])
        else:
            aim -= int(command[1])

    return horiz * depth


print(f'PART 1: {part1(inp)}')
print(f'PART 2: {part2(inp)}')
