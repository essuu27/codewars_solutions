# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element
# ( by value, not by index! ).

def sum_array(arr):
    if arr is not None:
        if len(arr) > 1:
            return sum(sorted(arr)[1:-1])
    return 0
