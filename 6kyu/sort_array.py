# Sort an array so the odd numbers in ascending order while leaving the even numbers
# at their original positions.

def sort_array(source_array):
    arrodd = []

    for x in source_array:
        arrodd.append(x) if (x % 2) != 0 else None

    arrodd = sorted(arrodd)

    for x, y in enumerate(source_array):
        source_array[x] = arrodd.pop(0) if (y % 2) != 0 else source_array[x]
    return(source_array)
