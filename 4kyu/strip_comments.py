# write a routine that it strips all text that follows any of a set of
#  comment markers passed in.

def strip_comments(strng, markers):
    if any(mark in strng for mark in markers):
        print(f"> {strng}")
    return 0

