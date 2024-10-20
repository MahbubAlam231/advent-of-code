# -------------------------------------------------------------------
# Author(s)   : Mahbub Alam
# File        : 4-advent-of-code.py
# Created     : 28/09/2024 (Sep, Sat) 13:53:26 CEST
# Description :
# -------------------------------------------------------------------

# print("==================================================================\n")

import re

with open('4_input_advent.txt', 'r') as f:
    cards = f.read()

def partOne(cards):
    cards = cards.split('\n')
    cards.pop(-1)
    points = 0

    for card in cards:
        split1 = card.split(' | ')
        split2 = split1[0].split(': ')
        # print(split1)

        myNums = set(split1[1].split())
        winningNums = set(split2[1].split())

        if myNums.intersection(winningNums):
            points += 2**(len(myNums.intersection(winningNums)) - 1)

    return(points)

print(partOne(cards))

def partTwo(cards):
    copiesDict = {}
    regex = r'Card (.*):(.*)\|(.*)'
    cardSplit = re.findall(regex, cards)
    for i in range(1, 1 + len(cardSplit)):
        copiesDict[i] = 1


    for cardNum, winningNums, myNums in cardSplit:
        intersec = set(winningNums.split()).intersection(set(myNums.split()))
        for i in range(1, 1+len(intersec)):
            copiesDict[int(cardNum)+i] += copiesDict[int(cardNum)]

    sum = 0
    for i in range(1, 1+len(cardSplit)):
        sum += copiesDict[i]

    return(sum)

print(partTwo(cards))
