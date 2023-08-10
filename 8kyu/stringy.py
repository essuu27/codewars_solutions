# write  a function stringy that takes a size and returns a string
# of alternating '1s' and '0s'

def stringy(size):
    y = 0
    str = ''
    while y < size:
        if y % 2 == 0:
            z = '1'
        else:
            z = '0'
        str = str + z
        y += 1
    return(str)

