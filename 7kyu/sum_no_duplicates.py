# write a function that sums a list, but ignores any duplicate 
# items in the list.

def sum_no_duplicates(mylist):
    sum = 0
    for x in range(0, len(mylist)):
        if mylist.count(mylist[x]) == 1:
            sum += mylist[x]
    return (sum)
