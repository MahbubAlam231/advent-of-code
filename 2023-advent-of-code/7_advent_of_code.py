#!/usr/bin/python3
# -------------------------------------------------------------------
# Author(s)   : Mahbub Alam
# File        : 7-advent-of-code.py
# Created     : 01/10/2024 (Oct, Tue) 01:35:47 CEST
# Description :
# -------------------------------------------------------------------

# print("==================================================================\n")

import re
import time

with open('7_input_advent.txt', 'r') as f:
    file = f.read()

data = re.findall(r"(\w{5}) (\d+)", file)

def kind(hand):# {{{
    hand = list(hand)
    hand.sort()
    # x = hand.count(hand[0])
    y = hand.count(hand[2])
    if len(set(hand)) == 1:
        return 6
    elif len(set(hand)) == 5:
        return 0
    elif len(set(hand)) == 4:
        return 1
    elif len(set(hand)) == 2:
        return y+1
        # return f'{y+1}'
        # if y == 4:
        #     return 5
        # else:
        #     return 4
    else:
        return max(y, 2)
        # return f'{max(y, 2)}'
        # if y == 3:
        #     return 3
        # else:
        #     return 2# }}}

def newKind(hand):# {{{
    hand = list(hand)
    hand.sort()
    if len(set(hand)) == 1:
        return 6
    elif len(set(hand)) == 2:
        if 'J' in hand:
            return 6
        else:
            return kind(hand)
    elif len(set(hand)) == 5:
        if 'J' in hand:
            return 1
        else:
            return kind(hand)
    elif len(set(hand)) == 4:
        if 'J' in hand:
            return 3
        else:
            return kind(hand)
    else:
        if hand.count('J') >= 2:
            return 5
        # elif hand.count('J') == 2:
        #     return 5
        elif hand.count('J') == 1:
            if kind(hand) == 3:
                return 5
            else:
                return 4
        else:
            return kind(hand)# }}}

valueDict = {# {{{
    '2' : '02',
    '3' : '03',
    '4' : '04',
    '5' : '05',
    '6' : '06',
    '7' : '07',
    '8' : '08',
    '9' : '09',
   'T' : '10',
    'J' : '11',
    'Q' : '12',
    'K' : '13',
    'A' : '14'
}

def valueFun(x):

    return valueDict.get(x, '00')

    # if x == 'T':
    #     return '10'
    # elif x == 'J':
    #     return '11'
    # elif x == 'Q':
    #     return '12'
    # elif x == 'K':
    #     return '13'
    # elif x == 'A':
    #     return '14'
    # else:
    #     return '0' + x}}}

def newValueFun(x):# {{{
    return '01' if x == 'J' else valueFun(x)# }}}

def rank(hierarchy, worth, data):# {{{
    """
    Hierarchy is the kind of hand it is: possible values - kind, newKind
    Worth is the value of each card: possible values - valueFun, newValueFun
    Data is a list of tuples (hand, bid) = datum
    """
    def sortFun(hand):
        return f"{hierarchy(hand)}" + "".join(map(worth, hand))

    data.sort(key=lambda x: sortFun(x[0]))
    return data# }}}

def solution(hierarchy, worth, data):# {{{
    """
    Hierarchy is the kind of hand it is: possible values - kind, newKind
    Worth is the value of each card: possible values - valueFun, newValueFun
    """

    data = rank(hierarchy, worth, data)

    total = 0
    for i, datum in enumerate(data, start=1):
        total += i*int(datum[1])

    return total# }}}

# def rank1(worth, hands):# {{{
#     # can use sort function with a key
#     values = [(tuple(map(worth, tuple(hand))), hand, bid) for hand, bid in hands]
#     values.sort()
#     sortedHands = [value[1:] for value in values]

#     return sortedHands# }}}

# def solution1(hierarchy, worth):# {{{
#     """
#     Hierarchy is the kind of hand it is.
#     Worth is the value of each card.
#     """
#     # can use a two-step sort function with a key
#     categories = [[] for i in range(7)]
#     for i in range(7):
#         categories[i] = [(hand, bid) for hand, bid in data if hierarchy(hand) == f'{i}']

#     start = 0
#     total = 0
#     for i in range(7):
#         for j, (hand, bid) in enumerate(rank1(worth, categories[i]), start=1):
#             total += (start+j)*int(bid)
#         start += len(categories[i])

#     return total# }}}

# ts = time.time()
# print(f"Part 1 : {solution1(kind, valueFun)}")
# print(f"\nProgram ran for {time.time() - ts:.3f} secs.\n")

ts = time.time()
print(f"Part 1 : {solution(kind, valueFun, data)}")
print(f"\nProgram ran for {time.time() - ts:.3f} secs.\n")

# ts = time.time()
# print(f"Part 2 : {solution1(newKind, newValueFun)}")
# print(f"\nProgram ran for {time.time() - ts:.3f} secs.\n")

ts = time.time()
print(f"Part 2 : {solution(newKind, newValueFun, data)}")
print(f"\nProgram ran for {time.time() - ts:.3f} secs.\n")

