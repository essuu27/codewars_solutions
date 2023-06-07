# Pass in two arrays, a and b. Remove every b[value] for a[]

def array_diff(a, b):
    for x in b:
        while x in a:
            a.remove(x)
    return a
