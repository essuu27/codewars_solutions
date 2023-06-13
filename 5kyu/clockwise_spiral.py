# Return an NxN two-dimensional array with numbers 1 
# through NxN represented as a clockwise spiral.

def create_spiral(n):
    if not isinstance(n, int):
        return([])
    
    arr = []
    step = 1
    cnt = 0
    mydir = 1
    coords = [-1,0]

# Make an empty array
    arr = [[0 for _ in range(n)] for _ in range(n)]

    while (n > 0):
        for _ in range(n):
            cnt += 1

            match mydir:
                case 1:
                    coords[0] += 1
                case 2:
                    coords[1] += 1
                case 3:
                    coords[0] -= 1
                case 4:
                    coords[1] -= 1

            arr[coords[1]][coords[0]] = cnt

        mydir += 1
        if mydir == 5:
            mydir = 1
        step += 1
        if (step == 2):
            step = 0
            n -= 1

    return(arr)
