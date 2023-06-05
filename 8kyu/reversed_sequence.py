# Write a function that will make a range of integers from 1 to (n) and then return that 
# range reversed ie. n = 3 returns [3, 2, 1]

def reverse_seq(n):
    return([x for x in reversed(range(1,n+1))])
