# Write a function that works basically like a Fibonacci, but summing the last 3
# (instead of 2) numbers of the sequence to generate the next.

def tribonacci(signature, n):
    if n < 1:
        return []
    for _ in range(n - 3):
        signature.append(sum(signature[-3:]))
    return signature[:n]
