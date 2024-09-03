# Check whether two arrays, a and b, are the "same", with the values of b
# are the values of a^2.

def comp(a, b):
    if not a or not b or len(a) != len(b):
        return False
    return sorted(x**2 for x in a) == sorted(b)
