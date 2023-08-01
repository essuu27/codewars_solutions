# write a function that takes a PascalCase string and returns the
# string in snake_case notation

def to_underscore(string):
    outstr = ''
    for x in str(string):
        substr = x.lower()
        if x.isupper() and len(outstr) > 1:
            substr = f'_{substr}'
        outstr += substr
    return(outstr)
