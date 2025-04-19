# -------------------------------------------------------------------
# Author(s)   : Mahbub Alam
# File        : 10-advent-of-code.py
# Created     : 19/10/2024 (Oct, Sat) 09:07:38 CEST
# Description : x
# -------------------------------------------------------------------

# print("==================================================================\n")

from collections import deque
import time
ts = time.time()

with open('10_input_advent.txt', 'r') as f:
    data = [line.strip() for line in f]

def neighbor(position):# {{{
    """
    returns neighbor of each position
    """
    i, j = position
    tile = data[i][j]
    nbd = []

    if tile == '|':
        nbd = [(i - 1, j), (i + 1, j)]
    if tile == '-':
        nbd = [(i, j - 1), (i, j + 1)]
    if tile == 'L':
        nbd = [(i - 1, j), (i, j + 1)]
    if tile == 'J':
        nbd = [(i - 1, j), (i, j - 1)]
    if tile == '7':
        nbd = [(i + 1, j), (i, j - 1)]
    if tile == 'F':
        nbd = [(i + 1, j), (i, j + 1)]
    if tile == "S":
        if (i, j) in neighbor((i - 1, j)):
            nbd.append((i - 1, j))
        if (i, j) in neighbor((i + 1, j)):
            nbd.append((i + 1, j))
        if (i, j) in neighbor((i, j - 1)):
            nbd.append((i, j - 1))
        if (i, j) in neighbor((i, j + 1)):
            nbd.append((i, j + 1))

    nbd = [p for p in nbd if p[0] in range(140) and p[1] in range(140)]

    return nbd
# }}}

# there are some edge cases but this works
S_pos = "".join(data).index("S")
loop = deque([(S_pos//140, S_pos%140)])

def full_loop():# {{{
    """
    find the loop that the animal is in
    """

    S_nbd = neighbor(loop[0])
    loop.appendleft(S_nbd[0])
    loop.append(S_nbd[1])

    loop_ends = False

    # extend loop as long as possible
    while not loop_ends:
        extend_right = [pipe for pipe in neighbor(loop[-1]) if pipe not in loop]
        if extend_right:
            loop.append(extend_right[0])
        else:
            loop_ends = True

        extend_left = [pipe for pipe in neighbor(loop[0]) if pipe not in loop]
        if extend_left:
            loop.appendleft(extend_left[0])
        else:
            loop_ends = True

    return loop
# }}}

loop = full_loop()

def part_1():

    return len(loop)//2

print(part_1())
print(f"\nProgram ran for {time.time() - ts:.3f} secs.\n")

ts = time.time()

def part_2():# {{{
    """
    Using shoelace formula and Pick's theorem
    Num of interior points = area_bounded_by_loop + 1 - boundary_points/2

    """

    # Shoelace formula
    area = 0
    for i in range(len(loop)):
        area += loop[(i+1)%len(loop)][0] * loop[i][1] - loop[i][0] * loop[(i+1)%len(loop)][1]

    # returns signed area
    area = abs(area / 2)

    # Pick's theorem
    return int((area + 1) - len(loop)/ 2)
    # return area
# }}}

print(part_2())
print(f"\nProgram ran for {time.time() - ts:.3f} secs.\n")
