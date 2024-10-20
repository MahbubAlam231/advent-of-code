# -------------------------------------------------------------------
# Author(s)   : Mahbub Alam
# File        : 8-advent-of-code.py
# Created     : 02/10/2024 (Oct, Wed) 15:25:30 CEST
# Description :
# -------------------------------------------------------------------

# print("==================================================================\n")

from collections import deque
import re
import math
import time

with open('8_input_advent.txt', 'r') as file1:
    file = file1.read()

moves = deque(0 if x == 'L' else 1 for x in file.split('\n\n')[0])

nodesDict = {}

for node, left, right in re.findall(r"(\w{3}).*(\w{3}), (\w{3})", file):
    nodesDict[node] = (left, right)

def partOne(location, destinations):
    steps = 0
    notReached = True
    while notReached:
        location = nodesDict[location][moves[0]]
        moves.rotate(-1)
        steps += 1
        if location in destinations:
            notReached = False

    return steps, location

ts = time.time()
print(partOne('AAA', ['ZZZ'])[0])
print(f"\nProgram ran for {time.time() - ts:.3f} secs.\n")

def partTwo():
    locations = re.findall(r"(\w+A\b) =", file)
    destinations = re.findall(r"(\w+Z\b) =", file)

    loops = []
    for x in locations:
        loops.append(partOne(x, destinations))

    return(math.lcm(*map(lambda x: x[0], loops)))

ts = time.time()
print(partTwo())
print(f"\nProgram ran for {time.time() - ts:.3f} secs.\n")

