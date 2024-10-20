# -------------------------------------------------------------------
# Author(s)   : Mahbub Alam
# File        : advent-of-code-21.py
# Created     : 24/09/2024 (Sep, Tue) 23:09:29 CEST
# Description :
# -------------------------------------------------------------------

# print("==================================================================\n")

import re

games=open('2_input_advent.txt', 'r')

maxBlue=14
maxRed=12
maxGreen=13
validGames=[]
sumPower=0

for game in games:
    sets = game.split(';')
    blue=[0]
    red=[0]
    green=[0]

    for set in sets:

        try:
            blue.append(int(re.search(r"\d+(?= blue)", set).group(0)))
        except:
            # if can't, do that
            pass

        try:
            red.append(int(re.search(r"\d+(?= red)", set).group(0)))
        except:
            # if can't, do that
            pass

        try:
            green.append(int(re.search(r"\d+(?= green)", set).group(0)))
        except:
            # if can't, do that
            pass

    if max(blue) <= maxBlue and max(red) <= maxRed and max(green) <= maxGreen:
        gameNo=re.search(r"\d+(?=:)", game)
        validGames.append(int(gameNo.group(0)))

    sumPower+= max(blue) * max(red) * max(green)

print(sum(validGames))
print(sumPower)

games.close()
