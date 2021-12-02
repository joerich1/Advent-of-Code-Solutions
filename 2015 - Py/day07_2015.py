"""
ADVENT OF CODE: 2015
DAY: 7
AUTHOR: JOSEPH RICHARDSON
"""

from day07_2015_input import raw
from day07_2015_input import test
import gozer
from collections import defaultdict

dict_map = defaultdict(str)

# If lines from a text input needs to be split into rows of a list
inp = gozer.readlines(raw, to_int=False, to_np=False)
inp_test = gozer.readlines(test, to_int=False, to_np=False, np_map=None)


# PART 1
def fill_dict(data):
    for line in data:
        commands = line.split(' -> ')
        try:
            dict_map[commands[1]] = int(commands[0])
        except:
            dict_map[commands[1]] = commands[0]


def parse_command(key, command):
    if isinstance(command, int):
        return command

    c = command.split(' ')

    if len(c) == 1:
        dict_map[key] = parse_command(c[0], dict_map[c[0]])
        return dict_map[key]

    elif c[1] == 'AND':
        try:
            a = int(c[0])
        except:
            a = parse_command(c[0], dict_map[c[0]])
            dict_map[c[0]] = a

        b = parse_command(c[2], dict_map[c[2]])
        dict_map[c[2]] = b
        dict_map[key] = a & b
        return dict_map[key]

    elif c[1] == 'OR':
        dict_map[c[0]] = parse_command(c[0], dict_map[c[0]])
        dict_map[c[2]] = parse_command(c[2], dict_map[c[2]])
        dict_map[key] = dict_map[c[0]] | dict_map[c[2]]
        return dict_map[key]

    elif c[1] == 'LSHIFT':
        dict_map[c[0]] = parse_command(c[0], dict_map[c[0]])
        dict_map[key] = dict_map[c[0]] << int(c[2])
        return dict_map[key]

    elif c[1] == 'RSHIFT':
        dict_map[c[0]] = parse_command(c[0], dict_map[c[0]])
        dict_map[key] = dict_map[c[0]] >> int(c[2])
        return dict_map[key]

    else:
        ans = parse_command(c[0], dict_map[c[1]])
        dict_map[key] = ~ ans + 65535+1
        return dict_map[key]


def part1(data):
    fill_dict(data)
    return parse_command(key='a', command=dict_map['a'])


# PART 2
def part2(data, new_b):
    fill_dict(data)
    dict_map['b'] = new_b
    return parse_command(key='a', command=dict_map['a'])


part1_a = part1(data=inp)
print(f'PART 1: {part1_a}')
print(f'PART 2: {part2(data=inp, new_b=part1_a)}')