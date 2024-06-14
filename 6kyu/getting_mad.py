# In an array of integers, find the minimum absolute difference between two array 
# elements ai and aj, where i != j, is the absolute value of ai - aj.

def getting_mad(arr: list) -> int:
    y = sorted(arr, reverse=True)
    dy = abs(y[0] - y[1])
    for i in range(1, len(y) - 1):
        current_diff = abs(y[i] - y[i + 1])
        if current_diff < dy:
            dy = current_diff
    return dy

