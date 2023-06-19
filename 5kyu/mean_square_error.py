# Given two same-sized arrays of integers, return the average of 
# the sum of the squares of the difference between two matching
# cells

def solution(array_a, array_b):
    runsum = 0
    for (idx, cont1) in enumerate(array_a):
        runsum += (abs(cont1 - array_b[idx])**2)
    runsum =runsum/len(array_a)
    return(runsum)
    