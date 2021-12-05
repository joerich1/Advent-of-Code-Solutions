"""
ADVENT OF CODE: 2015
DAY: 11
AUTHOR: JOSEPH RICHARDSON
"""

import numpy as np
import pandas as pd

# VARIABLES
inp = 'hxbxwxba'
valid = 'abcdefghjkmnpqrstuvwxyz'
straights = [valid[a:a+3] for a in range(len(valid)-2)]


# PART 1
def is_valid(password):
    valid_password = [False, False]
    # Condition 1
    for straight in straights:
        if straight in password:
            valid_password[0] = True
            break

    # Condition 2
    found = 0
    for letter in valid:
        if letter * 2 in password:
            found += 1
            ind = password.index(letter * 2)
            try:
                password.index(letter * 2, ind+2)
                found += 1
                break
            except ValueError:
                pass

    if found >= 2:
        valid_password[1] = True

    if valid_password == [True, True]:
        return True
    else:
        return False


def increment_password(password):
    ind = valid.index(password[-1])
    return 0


def part1(password):
    valid_password = is_valid(password=password)

    while not valid_password:
        password = increment_password(password=password)
        valid_password = is_valid(password=password)

    return password


# PART 2
def part2(data):
    return 0


print(f'PART 1: {part1(password=inp)}')
#print(f'PART 2: {part2()}')