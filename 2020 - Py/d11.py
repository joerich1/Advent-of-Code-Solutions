import d11_input
import numpy as np
# from scipy.ndimage import rotate
from skimage import data
from skimage.transform import rotate

inp = d11_input.go_numpy(d11_input.inp)
inp_test = d11_input.go_numpy(d11_input.inp_test)

# '.': 0, 'L': 1, '#': 2
trans_dict = d11_input.trans_dict
rev_trans_dict = d11_input.rev_trans_dict


def count_adj(x, arr):
    """Counts number of occupied seats adjacent to seat x"""
    # Look at adj. seats
    n_occ = 0

    if x[0] > 0 and x[1] > 0:  # Top left
        if arr[x[0] - 1, x[1] - 1] == 2:
            n_occ += 1

    if x[1] > 0:  # Top middle
        if arr[x[0], x[1] - 1] == 2:
            n_occ += 1

    if x[0] < arr.shape[1] - 1 and x[1] > 0:  # Top right
        if arr[x[0] + 1, x[1] - 1] == 2:
            n_occ += 1

    if x[0] > 0:  # Middle left
        if arr[x[0] - 1, x[1]] == 2:
            n_occ += 1

    if x[0] < arr.shape[1] - 1:  # Middle right
        if arr[(x[0] + 1, x[1])] == 2:
            n_occ += 1

    if x[0] > 0 and x[1] < arr.shape[0] - 1:  # Bottom left
        if arr[(x[0] - 1, x[1] + 1)] == 2:
            n_occ += 1

    if x[1] < arr.shape[0] - 1:  # Bottom middle
        if arr[(x[0], x[1] + 1)] == 2:
            n_occ += 1

    if x[0] < arr.shape[1] - 1 and x[1] < arr.shape[0] - 1:  # Bottom right
        if arr[(x[0] + 1, x[1] + 1)] == 2:
            n_occ += 1

    return n_occ


def seat(x, arr, part):
    """Part 1: If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
        Otherwise, the seat's state does not change.

        Part 2: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four
        or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become
        occupied, seats matching no rule don't change, and floor never changes."""

    if part == 1:
        n_occ = count_adj(x, arr)
        thresh = 4

    elif part == 2:
        n_occ = count_visible(x, arr, verbose=False)
        thresh = 5

    if (arr[x[0], x[1]] == 1) and (n_occ == 0):
        new = 2
        # print('Taken')

    elif (arr[x[0], x[1]] == 2) and (n_occ >= thresh):
        new = 1
        # print('Freed')

    else:
        new = arr[x[0], x[1]]
        # print('Bo Nix!')

    return new


def one_round(arr, part, verbose):
    new_arr = arr.copy()

    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            new_arr[i, j] = seat((i, j), arr, part)

    return new_arr


def sim_rounds(arr, part=1, verbose=False):
    new_arr = one_round(arr, part, verbose).copy()

    if verbose:
        i = 1
        print('Part=', part)
        print('Start:\n', arr)
        print(f'Round {i}:\n', new_arr)

    while True:
        if np.array_equal(arr, new_arr):
            if verbose:
                print('Converged!')
            break

        else:
            arr = new_arr.copy()
            new_arr = one_round(arr, part, verbose).copy()

            if verbose:
                i += 1
                print(f'Round {i}:\n', new_arr)

    # Return count occupied
    return np.count_nonzero(new_arr == 2)


#   PART 2
def look(x, y, delta_x, delta_y, arr, direction, verbose=False):
    x1 = x + delta_x
    y1 = y + delta_y

    if verbose:
        print(direction)

    while 0 <= x1 < arr.shape[1] - 1 and 0 <= y1 < arr.shape[0] - 1:
        if verbose:
            print(x1, y1)

        if arr[x1, y1] == 2:
            return 1

        else:
            x1 += delta_x
            y1 += delta_y

    return 0


def count_visible(loc, arr, verbose=False):
    x, y = loc
    n_occ = 0

    n_occ += look(x=x, y=y, delta_x=-1, delta_y=-1, arr=arr, direction='UL', verbose=verbose)  # Up left
    n_occ += look(x=x, y=y, delta_x=0, delta_y=-1, arr=arr, direction='UM', verbose=verbose)  # Up middle
    n_occ += look(x=x, y=y, delta_x=1, delta_y=-1, arr=arr, direction='UR', verbose=verbose)  # Up right
    n_occ += look(x=x, y=y, delta_x=1, delta_y=0, arr=arr, direction='R', verbose=verbose)  # Right
    n_occ += look(x=x, y=y, delta_x=1, delta_y=1, arr=arr, direction='DR', verbose=verbose)  # Down right
    n_occ += look(x=x, y=y, delta_x=0, delta_y=1, arr=arr, direction='D', verbose=verbose)  # Down
    n_occ += look(x=x, y=y, delta_x=-1, delta_y=1, arr=arr, direction='DL', verbose=verbose)  # Down left
    n_occ += look(x=x, y=y, delta_x=-1, delta_y=0, arr=arr, direction='L', verbose=verbose)  # Left

    return n_occ


def count_visible_vec(loc, arr, verbose=False):
    n_occ = 0
    arr_rotated = rotate(arr, angle=45)
    rot_size = arr_rotated.shape[0]
    # print(rot_size)
    size = arr.shape[0]
    x = loc[0] + 1
    y = loc[1] + 1
    x2 = (x + y - 1) - 2
    y2 = (size - x + y) - 2

    if np.count_nonzero(arr[loc[0] + 1:, loc[1]] == 2) > 0:  # E
        print(arr[loc[0] + 1:, loc[1]])
        n_occ += 1
    if np.count_nonzero(arr[:loc[0], loc[1]] == 2) > 0:  # W
        n_occ += 1
    if np.count_nonzero(arr[loc[0], :loc[1]] == 2) > 0:  # N
        n_occ += 1
    if np.count_nonzero(arr[loc[0]:, loc[1] + 1:] == 2) > 0:  # S
        n_occ += 1
    #print(x2, y2, '\n', arr_rotated)
    if np.count_nonzero(arr_rotated[x2 + 1:, y2] == 2) > 0:  # NE
        n_occ += 1
    if np.count_nonzero(arr_rotated[:x2, y2] == 2) > 0:  # SW
        n_occ += 1
    if np.count_nonzero(arr_rotated[x2, :y2] == 2) > 0:  # NW
        n_occ += 1
    if np.count_nonzero(arr_rotated[x2:, y2 + 1:] == 2) > 0:  # SE
        n_occ += 1

    return n_occ


# print('Part 1:', sim_rounds(inp, part=1, verbose=False))
print('Part 2:', sim_rounds(inp_test, part=2, verbose=False))  # 320 < answer < 7923
