# write a function that removes duplicates from an array of non negative numbers
# and returns it as a result.

The order of the sequence has to stay the same.

def distinct(seq):
    ret_arr = []
    for x in seq:
        if x not in ret_arr:
            ret_arr.append(x)
    return (ret_arr)

