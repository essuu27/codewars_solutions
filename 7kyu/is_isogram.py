# Create a function that determines whether a string that contains only letters is 
# an isogram. Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    outstr = {s.lower() for s in string}
    return True if len(string) == len(outstr) else False
