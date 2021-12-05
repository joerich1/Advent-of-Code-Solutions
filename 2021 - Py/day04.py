"""
ADVENT OF CODE: 2021
DAY: 4
AUTHOR: JOSEPH RICHARDSON
"""

from day04_input import test, raw
import numpy as np

def create_boards(data, n):
    boards = np.empty(shape=(n, 5, 5)).astype(int)
    for board in range(2, len(data.split('\n')), 6):
        to_int = [list(map(int, data.split('\n')[board + x].split())) for x in range(5)]
        boards[(int((board - 2) / 6))] = to_int
    return boards

def is_bingo(board):
    if board.sum(axis=0).max() == 50000:
        return True
    elif board.sum(axis=1).max() == 50000:
        return True

def play(data, n, part):
    nums = [int(num) for num in data.split()[0].split(',')]
    boards = create_boards(data, n)
    for num in nums:
        for b in range(n):
            boards[b][boards[b] == num] = 10000
            if is_bingo(boards[b]):
                if part == 1:
                    return boards[b][boards[b] < 10000].sum() * num
                else:
                    # Check if last board. All other boards are filled with -1
                    if boards[boards == -1].shape[0] == (n - 1) * 25:
                        return boards[b][boards[b] < 10000].sum() * num
                    boards[b, :, :] = -1

data_in = raw  # Set to: test, raw
n_data = int((len(data_in.split('\n')) - 1) / 6)
print(f'PART 1: {play(data=data_in, n=n_data, part=1)}')
print(f'PART 2: {play(data=data_in, n=n_data, part=2)}')