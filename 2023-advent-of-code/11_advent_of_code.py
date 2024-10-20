# -------------------------------------------------------------------
# Author(s)   : Mahbub Alam
# File        : 11_advent_of_code.py
# Created     : 20/10/2024 (Oct, Sun) 18:20:13 CEST
# Description : x
# -------------------------------------------------------------------

# print("==================================================================\n")

import time
import numpy as np

with open('11_input_advent.txt', 'r') as f:
    data = [list(line.strip()) for line in f]

def solution(part, exp_const):
    """
    :exp_const: 1 and 1 000 000
    :returns: sum of shortest distances between galaxies

    """
    space_matrix = np.array(data)
    m, n = space_matrix.shape

    row_blank_space = np.array([i for i in range(m) if '#' not in space_matrix[i]])

    col_blank_space = np.array([j for j in range(n) if '#' not in space_matrix[:,j]])

    galaxies = list(zip(*np.where(space_matrix == '#')))

    exp = exp_const - 1
    dist = 0
    while galaxies:
        (i_0, j_0) = galaxies.pop()
        for (i, j) in galaxies:
            x_1, x_2 = sorted((i_0, i))
            y_1, y_2 = sorted((j_0, j))
            # find the spaces in between coordinates of galaxies
            row_exp = np.sum(np.isin(row_blank_space, range(x_1, x_2)))
            col_exp = np.sum(np.isin(col_blank_space, range(y_1, y_2)))
            # adding the adjusted distance between (i, j) and (i_0, j_0)
            dist += abs(i - i_0) + abs(j - j_0) + (row_exp + col_exp) * exp

    return f"{part} : {dist}"

ts = time.time()
print(solution("Part_1", 2))
print(f"\nProgram ran for {time.time() - ts:.3f} secs.\n")

ts = time.time()
print(solution("Part_2", 1000000))
print(f"\nProgram ran for {time.time() - ts:.3f} secs.\n")
