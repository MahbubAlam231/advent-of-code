# -------------------------------------------------------------------
# Author(s)   : Mahbub Alam
# File        : 9-advent-of-code.py
# Created     : 02/10/2024 (Oct, Wed) 18:46:17 CEST
# Description :
# -------------------------------------------------------------------

# print("==================================================================\n")

import time

with open('9_input_advent.txt', 'r') as file1:
    file = file1.readlines()

lines = [line.strip().split() for line in file]

def partOne(lines):
    extrapolated = 0
    for line in lines:
        seq = list(map(int, line))
        sumLast = 0
        while set(seq) != {0}:
            sumLast += seq[-1]
            seq = [seq[i] - seq[i-1] for i in range(1, len(seq))]

        extrapolated += sumLast

    return(extrapolated)

ts = time.time()
print(partOne(lines))
print(f"\nProgram ran for {time.time() - ts:.3f} secs.\n")

def partTwo(lines):
    # _.reverse() doesn't work on sublists since it reverses in place
    # use reversed() to create new list
    lines = [reversed(line) for line in lines]

    return partOne(lines)

ts = time.time()
print(partTwo(lines))
print(f"\nProgram ran for {time.time() - ts:.3f} secs.\n")

