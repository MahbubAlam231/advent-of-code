# -------------------------------------------------------------------
# Author(s)   : Mahbub Alam
# File        : 6-advent-of-code.py
# Created     : 30/09/2024 (Sep, Mon) 22:01:47 CEST
# Description :
# -------------------------------------------------------------------

# print("==================================================================\n")

import re
import math
import time
ts = time.time()

with open('6_input_advent.txt', 'r') as f:
    file = f.read()

data = re.findall(r"(\d+) *(\d+) *(\d+) *(\d+)", file)
times = list(map(int, data[0]))
dists = list(map(int, data[1]))

def partOne(times, dists):
    numRaces = len(times)
    ways = 1
    for i in range(numRaces):
        t, d = times[i], dists[i]
        b = math.sqrt((t*t)/4 - d) + t/2
        a = -math.sqrt((t*t)/4 - d) + t/2
        if b == int(b):
            ways *= (int(b) - int(a) - 1)
        else:
            ways *= (int(b) - int(a))

    return ways

print("part 1")
print(partOne(times, dists))
print(f"\nProgram ran for {time.time() - ts:.5f} secs.")

ts = time.time()

times, dists = [int("".join(data[0]))], [int("".join(data[1]))]
partTwo = partOne

print("\npart 2")
print(partTwo(times, dists))
print(f"\nProgram ran for {time.time() - ts:.5f} secs.")

