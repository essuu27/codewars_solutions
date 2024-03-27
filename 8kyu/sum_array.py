# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element
# ( by value, not by index! ).

def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr is not None and len(arr) > 1 else 0
