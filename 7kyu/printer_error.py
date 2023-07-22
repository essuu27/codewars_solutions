s="aaaxbbbbyyhwawiwjjjwwm"
err = 0
str = [chr(x) for x in range(110,123)]

for y in s:
    err = err + 1 if y in str;
    
print(err)
