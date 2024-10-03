# Given an n x n array, return the array elements arranged from 
# outermost elements to the middle element, traveling clockwise.

def snail(snail_map):
    moves = {0: [1,0], 1: [0, 1], 2: (-1, 0), 3: (0, -1)}
    coords = [-1, 0]
    my_dir = 0
    my_stage = 1

    if all(not sublist for sublist in snail_map):
        return([])

    output = []
    pathlen = len(snail_map)
    while pathlen > 0:
        for _ in range(pathlen):
            coords[0] += moves[my_dir][0]
            coords[1] += moves[my_dir][1]
            output.append(snail_map[coords[1]][coords[0]])

        my_dir += 1
        if my_dir > 3:
            my_dir = 0
        
        my_stage += 1
        if my_stage > 1:
            my_stage = 0
            pathlen -= 1
    return (output)
