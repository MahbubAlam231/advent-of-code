# -------------------------------------------------------------------
# Author(s)   : Mahbub Alam
# File        : 11.py
# Created     : 24/09/2024 (Sep, Tue) 19:08:08 CEST
# Description : day 1 both problems
# -------------------------------------------------------------------

# print("==================================================================\n")


strDigits3Dict = {
    'one' : 1,
    'two' : 2,
    'six' : 6
}

strDigits4Dict = {
    'four' : 4,
    'five' : 5,
    'nine' : 9
}

strDigits5Dict = {
    'three' : 3,
    'seven' : 7,
    'eight' : 8
}


def isADigit(s, i):
    if s[i].isdigit():
        return [True, 1, s[i]]
    # The order of 3, 4, and 5 is important down.
    elif s[i: i+3] in strDigits3Dict.keys():
        return [True, 3, strDigits3Dict[s[i: i+3]]]
    elif s[i: i+4] in strDigits4Dict.keys():
        return [True, 4, strDigits4Dict[s[i: i+4]]]
    elif s[i: i+5] in strDigits5Dict.keys():
        return [True, 5, strDigits5Dict[s[i:i+5]]]
    else:
        return [False, 0]

def calval(s):
    i=0
    while i < len(s):
        if s[i].isdigit():
            first = s[i]
            break
        i+= 1

    j=len(s) - 1
    while j > -1:
        if s[j].isdigit():
            last=s[j]
            break

        j = j - 1

    return(int(first+last))

def newcalval(s):
    i=0
    while i < len(s):
        if isADigit(s, i)[0]:
            first = isADigit(s, i)[2]
            break
        i+= 1

    j=len(s) - 1
    while j > -1:
        if isADigit(s, j)[0]:
            last=isADigit(s, j)[2]
            break
        j = j - 1

    # return "success"
    return int(str(first)+str(last))



calvallist=[]
newcalvallist=[]

with open('1_input_advent.txt', 'r') as file1:
    for x in file1:
        calvallist.append(calval(x))
        newcalvallist.append(newcalval(x))

    print(f"Old calibration sum: {sum(calvallist)}")
    print(f"New calibration sum: {sum(newcalvallist)}")



