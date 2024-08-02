# Write a function which returns the n-th term of the following series, where
# n is the input parameter giving the number of terms in the calculation
# 1 + 1/4 + 1/7 + 1/10 + ...

def series_sum(n):
    y = [1/((x*3)+1) for x in range(n)]
    return f"{sum(y):.2f}"
