# -------------------------------------------------------------------
# Author(s)   : Mahbub Alam
# File        : advent-of-code-3.py
# Created     : 27/09/2024 (Sep, Fri) 09:14:52 CEST
# Description :
# -------------------------------------------------------------------

# print("==================================================================\n")


import re

with open('3_input_advent.txt', 'r') as file1:
    lines = file1.readlines()

data = [line.replace('\n', '') for line in lines]
# dataArr = [list(line) for line in data]

def partOne():
    symNbd = set()
    partNum = []
    for i, line in enumerate(data):
        for sym in re.finditer(r"[^.\d]", line):
            symNbd |= {(x, y) for x in range(i-1, i+2) for y in range(sym.start()-1, sym.end()+1)}

    for i, line in enumerate(data):
        for m in re.finditer(r"\d+", line):
            mSet = {(i, j) for j in range(m.start(), m.end())}

            if mSet.intersection(symNbd):
                partNum.append(int(m.group()))

    return(sum(partNum))

print(partOne())

def partTwo():
    gears = []
    nums = []
    for i, line in enumerate(data):
        for gear in re.finditer(r"[*]", line):
            gears.append([i, gear])

        for m in re.finditer(r"\d+", line):
            nums.append([i, m])

    gearRatio = []
    for gear in gears:
        gearNbd = {(x, y) for x in range(gear[0]-1, gear[0]+2) for y in range(gear[1].start()-1, gear[1].end()+1)}
        gearAdj = []
        for m in nums:
            mNbd = {(m[0], y) for y in range(m[1].start(), m[1].end())}
            if mNbd.intersection(gearNbd):
                gearAdj.append(int(m[1].group()))

        if len(gearAdj) == 2:
            gearRatio.append(gearAdj[0] * gearAdj[1])

    return(sum(gearRatio))

print(partTwo())

