def dominator(arr):
    maxcount = 0
    maxn = 0
    for x in arr:
        if arr.count(x) > maxcount:
            maxn = x
            maxcount = arr.count(x)
    outn = maxn if arr.count(maxn) > len(arr)/2 else -1

    return (outn)


my_arr = [10, 3, 10, 10, 10, 5]

print(dominator(my_arr))
