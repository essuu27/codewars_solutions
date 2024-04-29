# Write a method that converts a string to camelCase
def camel_case(s):
    outstr = ''
    upsy = 1
    for x in s:
        if upsy == 1:
            x = x.upper()
            upsy = 0
        if x.isspace():
            upsy = 1
            continue
        outstr += x
    return (outstr)
