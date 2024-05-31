test = 'K-P'
outstr = ''

[[outstr =+ x] for x in range(ord(test[0]), ord(test[2])+1)]
print(outstr)
