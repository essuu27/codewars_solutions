# Given a string, you have to return a string in which each character
# (case-sensitive) is repeated once

def double_char(string):
    outstr = ''
    outstr = ''.join([outstr + x*2  for x in string])
    return(outstr)
