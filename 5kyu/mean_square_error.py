# input two integer arrays of equal length, find the difference in value
# of two matching cells, square that difference and return the average of
# the differences

def solution(array_a, array_b):
    runsum = 0
    for (idx, cont1) in enumerate(array_a):
        runsum += (abs(cont1 - array_b[idx])**2)
    runsum =runsum/len(array_a)
    return(runsum)
    