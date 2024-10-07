# Given an array of integers, remove the smallest value. Do not mutate the
# original array/list. If there are multiple elements with the same value,
# remove the one with the lowest index.

def remove_smallest(numbers):
    outnums = []
    if len(numbers) == 0:
        return []
    
    minnum = min(numbers)
    trig = 1
    for x in numbers:
        if x == minnum and trig == 1:
            trig = 0
        else:
            outnums.append(x)
    return [outnums]
