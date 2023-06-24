# Return a dictionary with the count of all the occurring characters in a string

def count(string):
    counts = {x: string.count(x) for x in string}
    return counts
