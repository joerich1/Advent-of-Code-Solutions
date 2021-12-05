"""
ADVENT OF CODE: 2021
DAY: 5
TIME: 70 MINUTES
AUTHOR: JOSEPH RICHARDSON
"""

from day05_input import raw
from day05_input import test
import gozer

inp = gozer.readlines(raw, to_int=False, to_np=False)
inp_test = gozer.readlines(test, to_int=False, to_np=False, np_map=None)


def parse(data):
    dir = []
    for line in data:
        start, end = line.split(' -> ')
        x0, y0 = start.split(',')
        x1, y1 = end.split(',')
        dir.append([int(x0), int(y0), int(x1), int(y1)])
    return dir


# PART 1
def create_board(dire):
    ma = max(max(x) if isinstance(x, list) else x for x in dire)
    board = []
    for j in range(ma + 1):
        board.append([0] * (ma + 1))
    return board


def count(board):
    c = 0
    for i in range(len(board)):
        c += sum(x > 1 for x in board[i])
    return c


def part1(data):
    dir = parse(data)
    board = create_board(dir)

    for x0, y0, x1, y1 in dir:
        if x0 > x1:
            x0, x1 = x1, x0
        if y0 > y1:
            y0, y1 = y1, y0
        if y1 - y0 == 0:
            for x in range(x0, x1 + 1):
                board[y1][x] += 1
        elif x1 - x0 == 0:
            for y in range(y0, y1 + 1):
                board[y][x1] += 1

    return count(board)


# PART 2
def part2(data):
    dir = parse(data)
    board = create_board(dir)

    for x0, y0, x1, y1 in dir:
        if y1 - y0 == 0:
            if x0 > x1:
                x0, x1 = x1, x0
            for x in range(x0, x1 + 1):
                board[y1][x] += 1

        elif x1 - x0 == 0:
            if y0 > y1:
                y0, y1 = y1, y0
            for y in range(y0, y1 + 1):
                board[y][x1] += 1

        else:
            x = x0
            y = y0
            while x != x1:
                board[y][x] += 1
                if x0 < x1:
                    x += 1
                else:
                    x -= 1
                if y0 < y1:
                    y += 1
                else:
                    y -= 1
            board[y][x] += 1

    return count(board)


print(f'PART 1: {part1(data=inp)}')
print(f'PART 2: {part2(data=inp)}')
