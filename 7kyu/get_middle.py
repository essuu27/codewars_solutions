def get_middle(s):
    outstr = s[(len(s) // 2)]
    if ((len(s) % 2) == 0):
        outstr = s[(len(s) // 2) - 1] + outstr
    return(outstr)
