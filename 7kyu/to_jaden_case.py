# Take a string, capitalise each word and return that string

def to_jaden_case(string):
    words = string.split(' ')
    outstr = ''
    for x in words:
        outstr = outstr + x.capitalize() + ' '
    outstr = outstr[:-1]
    return (outstr)
