# Given an array of ones and zeroes, convert the equivalent binary value
# to an integer.

def binary_array_to_number(arr):
    return int(''.join(str(x) for x in arr), 2)
