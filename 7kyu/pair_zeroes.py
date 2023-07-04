# Input a list of integers. Return the list with every double-zero [0, 0] replaced
# by a single zero [0]

def pair_zeros(arr):
    nums = []
    sw = 0
    for x in arr:
        if x == 0:
            if sw == 1:
                sw = 0
                x = None
            else:
                sw = 1
        if x != None:
            nums.append(x)

    return(nums)