
my_string = 'The Quick Brown fox jumped over the lazy black dog'
testset = [chr(i) for i in range(ord('a'), ord('z')+1)]
score = True

for x in my_string:
    if x != ' ' and x.lower() not in testset:
        print(x, testset)
        score = False

print(score)
