# Given any number of boolean flags function should return true if and only
# if one of them is true while others are false

def only_one(*numbers):
    truecnt = sum(x is True for x in numbers)
    return truecnt == 1
