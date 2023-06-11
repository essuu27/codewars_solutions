"""
Given a non-negative integer n and an arbitrary base b, return 
the number reversed in that base.

My description: Make a string 's' of number 'n', in numeric base 'b'
then reverse 's', convert back from base 'b' to decimal and return.
"""

def reverse_number(n, b):
    if b < 2:
        return n
    
    b_n = []
    bigsum = 0

    while n>0:
        dig = int(n%b)
        b_n.append(dig)
        n //= b

    for x in b_n:
        bigsum = (bigsum * b) + x

    return bigsum
