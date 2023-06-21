# Take a list of integers, each cell should be +1 value the previous cell.
# Not all cells are in the list. Return the completed list.
# Note: the task implies that the input list is sorted but that is not stated
# so I put a sort() in here "just in case".

def pipe_fix(nums):
    inpipe = nums
    outlist = []

    my_pipe = list(sorted([int(x) for x in inpipe]))

    for x in range(my_pipe[0], my_pipe[-1] + 1):
        outlist.append(x)

    return(outlist)