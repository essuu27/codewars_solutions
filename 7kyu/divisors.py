# Count the number of divisors of a positive integer n.

def divisors(n):
    return sum(1 for x in range(1, n+1) if (n // x) == (n / x))
