# Write a function that checks in the input is a perfect square, return True if it
# is or False is it is not.

def checker(n):
    return (int(n**(1/2)) == float(n**(1/2))) if n > -1 else False


print(checker(-1))
