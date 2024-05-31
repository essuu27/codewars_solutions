def compSame(array1, array2):
    for x in array1:
        if (x**2) in array2:
            result = True
        else:
            result = False
            break
    if len(array1) != len(array2):
        result = False
    return (result)


a = [121, 144, 19, 161, 19, 144, 19, 11]
# a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

print(compSame(a, b))
